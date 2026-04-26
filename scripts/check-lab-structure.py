#!/usr/bin/env python3
"""
Validate that every lab directory contains all required files and none are empty.
Used by CI on every PR and runnable locally.

Usage:
    python3 scripts/check-lab-structure.py
    python3 scripts/check-lab-structure.py labs/002-service-enumeration
"""

import os
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "objectives.md",
    "hardware.md",
    "topology.md",
    "setup.md",
    "instructions.md",
    "expected-output.md",
    "results.md",
    "cleanup.md",
    "lessons-learned.md",
]

REQUIRED_DIRS = [
    "configs",
    "results/logs",
    "results/screenshots",
]


def check_lab(lab_path):
    errors = []

    for filename in REQUIRED_FILES:
        fpath = lab_path / filename
        if not fpath.exists():
            errors.append(f"Missing file: {filename}")
        elif fpath.stat().st_size == 0:
            errors.append(f"Empty file: {filename}")

    for dirname in REQUIRED_DIRS:
        dpath = lab_path / dirname
        if not dpath.is_dir():
            errors.append(f"Missing directory: {dirname}")

    return errors


def main():
    repo_root = Path(__file__).parent.parent

    if len(sys.argv) > 1:
        targets = [Path(sys.argv[1])]
    else:
        labs_dir = repo_root / "labs"
        if not labs_dir.exists():
            print("No labs/ directory found.")
            sys.exit(0)
        targets = sorted([p for p in labs_dir.iterdir() if p.is_dir()])

    if not targets:
        print("No lab directories found.")
        sys.exit(0)

    all_passed = True

    for lab_path in targets:
        errors = check_lab(lab_path)
        if errors:
            all_passed = False
            print(f"FAIL  {lab_path.name}")
            for e in errors:
                print(f"      - {e}")
        else:
            print(f"PASS  {lab_path.name}")

    if not all_passed:
        print("\nStructure check failed. Fix the issues above before merging.")
        sys.exit(1)

    print(f"\nAll {len(targets)} lab(s) passed structure check.")


if __name__ == "__main__":
    main()
