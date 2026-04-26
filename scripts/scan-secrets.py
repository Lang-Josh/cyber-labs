#!/usr/bin/env python3
"""
Scan committed files for accidentally included secrets.
Used by CI on every PR and runnable locally.

Checks for:
- GitHub personal access tokens
- Private key headers
- Generic high-confidence secret patterns

Usage:
    python3 scripts/scan-secrets.py
"""

import os
import re
import sys
from pathlib import Path

PATTERNS = [
    (r"github_pat_[A-Za-z0-9_]{80,}", "GitHub fine-grained PAT"),
    (r"ghp_[A-Za-z0-9]{36}", "GitHub classic PAT"),
    (r"ghs_[A-Za-z0-9]{36}", "GitHub Actions token"),
    (r"-----BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----", "Private key"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key ID"),
    (r"(?i)(password|passwd|secret|token)\s*=\s*['\"][^'\"\$]{8,}['\"]", "Hardcoded credential"),
]

SKIP_DIRS = {".git", "node_modules", "__pycache__"}
SKIP_FILES = {
    "credentials.example.md",
    "scan-secrets.py",
}
SKIP_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".pdf",
                   ".zip", ".tar", ".gz", ".bin", ".asar", ".pack", ".idx", ".rev"}


def should_skip(path):
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return True
    if path.name in SKIP_FILES:
        return True
    if path.suffix.lower() in SKIP_EXTENSIONS:
        return True
    return False


def scan_file(path):
    hits = []
    try:
        text = path.read_text(errors="ignore")
    except Exception:
        return hits

    for lineno, line in enumerate(text.splitlines(), start=1):
        for pattern, label in PATTERNS:
            if re.search(pattern, line):
                hits.append((lineno, label, line.strip()[:120]))

    return hits


def main():
    repo_root = Path(__file__).parent.parent
    found_any = False

    for path in sorted(repo_root.rglob("*")):
        if not path.is_file():
            continue
        if should_skip(path):
            continue

        hits = scan_file(path)
        if hits:
            found_any = True
            rel = path.relative_to(repo_root)
            for lineno, label, snippet in hits:
                print(f"SECRET  {rel}:{lineno}  [{label}]")
                print(f"        {snippet}")

    if found_any:
        print("\nSecret scan failed. Rotate any real credentials and remove them from the repo.")
        sys.exit(1)

    print("Secret scan passed. No secrets found.")


if __name__ == "__main__":
    main()
