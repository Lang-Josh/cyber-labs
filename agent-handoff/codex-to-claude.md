# Codex to Claude

## Current task

Updated repository instructions so future lab work starts by inspecting all files, including hidden files and directories.

## Files changed

- Updated `AGENTS.md` Reference files section to require full repository file discovery before creating, replacing, or modifying labs.
- Added an explicit hidden-file-aware `find` example and warning not to rely only on `rg --files`.
- Added repository-level reading requirements for `AGENTS.md`, `CLAUDE.md`, `README.md`, `.codex/notes.md`, shared files, templates, and `agent-handoff/claude-to-codex.md`.
- Updated `.codex/notes.md` with the same hidden-file-aware discovery and reading requirements.

## Requested review

Please check:
- The new discovery rule is clear enough for future lab work.
- The required reading list includes the right repository-level context files.
- The `find` command is appropriate for listing hidden and visible files while excluding `.git`.
