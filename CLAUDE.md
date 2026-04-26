# CLAUDE.md

## Role

This repository is a personal cybersecurity lab knowledge base. Claude Code should help review, refine, and maintain reproducible lab files.

## Primary responsibilities

Claude Code may:
- Review lab setup instructions
- Improve clarity and correctness
- Check whether expected outputs match tasks
- Create or revise lab documentation
- Create or revise config files
- Create or revise detection logic
- Review Codex-generated pull requests
- Add missing cleanup steps
- Add troubleshooting notes
- Suggest safer lab boundaries

## Hard rules

- Do not modify live lab machines.
- Do not SSH into real devices unless explicitly instructed.
- Do not assume hidden local state.
- All lab work must be reproducible from committed files.
- Do not store real passwords, API keys, tokens, private keys, or personal secrets.
- Keep lab docs concise, direct, and actionable.
- Every lab must include setup, tasks, expected output, cleanup, and learning objectives.

## Required lab structure

Each lab should use this structure:

labs/000-lab-name/
  README.md
  objectives.md
  hardware.md
  topology.md
  setup.md
  instructions.md
  expected-output.md
  results.md
  cleanup.md
  lessons-learned.md
  configs/
  results/
    screenshots/
    logs/

## Reference files

Before creating or reviewing any lab, read these files from the repo:

- shared/ip-plan.md — lab IP addresses and network layout for all devices
- shared/hardware-inventory.md — available physical and virtual hardware and their roles
- shared/common-commands.md — standard commands used across labs
- shared/credentials.example.md — placeholder credential format, never store real secrets
- templates/lab-template/ — the required structure every lab must follow

## Agent coordination

Before starting any task, read:
agent-handoff/codex-to-claude.md

After completing a review, update:
agent-handoff/claude-to-codex.md

Use GitHub issues and PR comments as the primary multi-agent coordination system.

## Review style

When reviewing another agent's work:
- Check reproducibility
- Check missing steps
- Check command correctness
- Check security boundaries
- Check whether expected outputs are realistic
- Leave concrete changes, not vague feedback

## Safety

This repo is for owned, sandboxed systems only. Do not provide instructions that target third-party networks or systems.
