#!/usr/bin/env python3
"""
Run a lab against the Kali VM and compare real output to expected-output.md.

Flow:
  Mac (this script) → SSH → Kali VM → runs commands → Raspberry Pi / target

Config — create .lab-runner.env in the repo root (gitignored):
  KALI_HOST=192.168.50.10
  KALI_USER=kali
  KALI_SSH_KEY=~/.ssh/id_rsa   # optional, uses SSH agent if omitted

Usage:
  python3 scripts/run-lab.py labs/002-service-enumeration
  python3 scripts/run-lab.py labs/002-service-enumeration --dry-run
"""

import datetime
import os
import re
import subprocess
import sys
from pathlib import Path


# ── Config ────────────────────────────────────────────────────────────────────

def load_config():
    config = {
        "host": os.environ.get("KALI_HOST", ""),
        "user": os.environ.get("KALI_USER", "kali"),
        "key":  os.environ.get("KALI_SSH_KEY", ""),
    }

    env_file = Path(__file__).parent.parent / ".lab-runner.env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            mapping = {"KALI_HOST": "host", "KALI_USER": "user", "KALI_SSH_KEY": "key"}
            if k.strip() in mapping:
                config[mapping[k.strip()]] = v.strip()

    return config


# ── Markdown parsing ──────────────────────────────────────────────────────────

def extract_tasks(instructions_path):
    """Return list of {name, command} dicts parsed from instructions.md."""
    text = Path(instructions_path).read_text()
    tasks = []

    headers = re.findall(r"^## (Task \d+[^\n]*)", text, re.MULTILINE)
    sections = re.split(r"^## Task \d+[^\n]*\n", text, flags=re.MULTILINE)[1:]

    for header, section in zip(headers, sections):
        blocks = re.findall(r"```bash\n(.*?)```", section, re.DOTALL)
        if blocks:
            tasks.append({
                "name": header.strip(),
                "command": blocks[0].strip(),
            })

    return tasks


def extract_expected_patterns(expected_path):
    """Extract meaningful lines from expected-output.md for fuzzy comparison."""
    if not Path(expected_path).exists():
        return []

    text = Path(expected_path).read_text()
    patterns = []

    blocks = re.findall(r"```(?:text|bash)?\n(.*?)```", text, re.DOTALL)
    for block in blocks:
        for line in block.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if re.search(r"\d+/tcp|\d+/udp|open|closed|filtered|ssh|http|ftp|smb", line, re.I):
                patterns.append(line)
            elif len(line) > 15:
                patterns.append(line)

    return patterns[:30]


# ── SSH execution ─────────────────────────────────────────────────────────────

def run_on_kali(command, config, timeout=120):
    ssh = ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "ConnectTimeout=10",
           "-o", "BatchMode=yes"]

    if config["key"]:
        ssh += ["-i", os.path.expanduser(config["key"])]

    ssh += [f"{config['user']}@{config['host']}", command]

    try:
        result = subprocess.run(ssh, capture_output=True, text=True, timeout=timeout)
        output = result.stdout
        if result.stderr:
            output += "\n[stderr]\n" + result.stderr
        return output, result.returncode
    except subprocess.TimeoutExpired:
        return f"TIMEOUT: command exceeded {timeout}s", 1
    except Exception as e:
        return f"ERROR: {e}", 1


# ── Output comparison ─────────────────────────────────────────────────────────

def compare(real_output, patterns):
    matched, missed = [], []
    for pattern in patterns:
        tokens = [t for t in re.split(r"\s+", pattern) if len(t) > 3]
        if tokens and any(t in real_output for t in tokens):
            matched.append(pattern)
        else:
            missed.append(pattern)
    return matched, missed


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    dry_run = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if not args:
        print("Usage: python3 scripts/run-lab.py <lab-directory> [--dry-run]")
        print("       python3 scripts/run-lab.py labs/002-service-enumeration")
        sys.exit(1)

    lab_dir = Path(args[0])

    if not lab_dir.exists():
        print(f"Lab directory not found: {lab_dir}")
        sys.exit(1)

    instructions  = lab_dir / "instructions.md"
    expected_path = lab_dir / "expected-output.md"
    results_dir   = lab_dir / "results" / "logs"
    results_dir.mkdir(parents=True, exist_ok=True)

    config = load_config()

    if not config["host"] and not dry_run:
        print("ERROR: KALI_HOST not set.")
        print("Create .lab-runner.env with KALI_HOST=<ip> or export KALI_HOST=<ip>")
        sys.exit(1)

    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'=' * 60}")
    print(f"Lab:    {lab_dir.name}")
    print(f"Kali:   {config['user']}@{config['host']}" if config["host"] else "Kali:   (dry run)")
    print(f"Date:   {stamp}")
    if dry_run:
        print("Mode:   DRY RUN — commands will be printed but not executed")
    print(f"{'=' * 60}")

    tasks    = extract_tasks(instructions)
    patterns = extract_expected_patterns(expected_path)
    all_outputs = []

    for task in tasks:
        print(f"\n{task['name']}")
        print(f"  $ {task['command']}")

        if dry_run:
            print("  [skipped — dry run]")
            continue

        output, code = run_on_kali(task["command"], config)
        all_outputs.append(output)

        safe_name = re.sub(r"[^\w-]", "-", task["name"].lower())
        log_file  = results_dir / f"{safe_name}.txt"
        log_file.write_text(output)

        status = "OK" if code == 0 else f"EXIT {code}"
        print(f"  Status: {status}")
        print(f"  Saved:  {log_file}")

    if not dry_run and patterns and all_outputs:
        combined         = "\n".join(all_outputs)
        matched, missed  = compare(combined, patterns)
        total            = len(matched) + len(missed)

        print(f"\n{'=' * 60}")
        print(f"OUTPUT COMPARISON  {len(matched)}/{total} expected patterns found")

        if matched:
            print("\n  Confirmed:")
            for m in matched:
                print(f"    + {m}")

        if missed:
            print("\n  Not found in real output:")
            for m in missed:
                print(f"    - {m}")

        if missed:
            print("\n  Review expected-output.md — some patterns may need updating.")

    if not dry_run:
        print(f"\n{'=' * 60}")
        print(f"Results saved to: {results_dir}")
        print("Next: fill in results.md and lessons-learned.md, then commit.")


if __name__ == "__main__":
    main()
