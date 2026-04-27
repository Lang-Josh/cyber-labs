# Codex Local Notes

## Required reading before any task

Before creating, replacing, or modifying any lab, inspect the full repository file list, including hidden files and directories.

Use a command that includes hidden paths and excludes Git internals, such as:

```bash
find . -path ./.git -prune -o -type f -print
```

Then read repository-level instruction and context files that may affect the task. Do not rely only on `rg --files`, because it can omit hidden files depending on ignore rules and configuration.

Read these files from the repo before starting lab work:

- AGENTS.md — your role, rules, and lab structure requirements
- CLAUDE.md — Claude Code role, rules, and coordination expectations
- README.md — repository overview and structure
- .codex/notes.md — Codex-specific repository notes and lab context
- shared/ip-plan.md — all lab IP addresses
- shared/hardware-inventory.md — available hardware and roles
- shared/common-commands.md — standard commands used across labs
- shared/credentials.example.md — placeholder credential format, never store real secrets
- templates/lab-template/ — the structure every lab must follow
- agent-handoff/claude-to-codex.md — current instructions from Claude Code

## Required writing after any task

Update this file when handing off to Claude Code:
- agent-handoff/codex-to-claude.md
