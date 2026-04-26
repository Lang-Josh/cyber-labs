# AGENTS.md

## Role

This repository is a personal cybersecurity lab knowledge base. Codex should help create, organize, and maintain reproducible lab files.

## Primary responsibilities

Codex may:
- Create lab directories
- Fill in lab template files
- Write setup instructions
- Write hardware lists
- Write topology documentation
- Write expected output files
- Write result summaries
- Create config files
- Create scripts
- Create GitHub issues
- Create branches
- Open pull requests
- Update documentation

## Hard rules

- Do not modify live lab machines.
- Do not SSH into real devices unless explicitly instructed.
- Do not assume hidden local state.
- All work must be reproducible from committed files.
- Prefer documentation, templates, scripts, and infrastructure-as-code.
- Do not store real passwords, API keys, tokens, private keys, or personal secrets.
- Use credentials.example.md for placeholder credentials only.
- Keep each lab self-contained.
- Keep instructions granular and beginner-friendly.
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

## Naming

Use this naming style:
001-network-discovery
002-service-enumeration
003-ssh-bruteforce
004-dvwa-sql-injection
005-wazuh-detection

## Reference files

Before creating any lab, read these files from the repo:

- shared/ip-plan.md — lab IP addresses and network layout for all devices
- shared/hardware-inventory.md — available physical and virtual hardware and their roles
- shared/common-commands.md — standard commands used across labs
- shared/credentials.example.md — placeholder credential format, never store real secrets
- templates/lab-template/ — the required structure every lab must follow

## Agent coordination

Before starting any task, read:
agent-handoff/claude-to-codex.md

After completing work, update:
agent-handoff/codex-to-claude.md

Use GitHub issues and PR comments as the primary multi-agent coordination system.

## Safety

This repo is for owned, sandboxed systems only. Do not provide instructions that target third-party networks or systems.
