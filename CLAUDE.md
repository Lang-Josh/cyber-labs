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

## Agent coordination

Use the agent-handoff folder for coordination.

Claude Code may write:
agent-handoff/claude-to-codex.md

Claude Code should read:
agent-handoff/codex-to-claude.md

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
