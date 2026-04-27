# Codex to Claude

## Current task

Replaced `labs/001-network-discovery` with `labs/001-confirm-lab-network`.

This is a Level 0 baseline connectivity lab for confirming that the Mac host, Kali VM, and Raspberry Pi can reach each other on the lab network before later labs are run.

## Files changed

- Deleted `labs/001-network-discovery/`.
- Added `labs/001-confirm-lab-network/README.md`.
- Added `labs/001-confirm-lab-network/objectives.md`.
- Added `labs/001-confirm-lab-network/hardware.md`.
- Added `labs/001-confirm-lab-network/topology.md`.
- Added `labs/001-confirm-lab-network/setup.md`.
- Added `labs/001-confirm-lab-network/instructions.md`.
- Added `labs/001-confirm-lab-network/expected-output.md`.
- Added `labs/001-confirm-lab-network/results.md`.
- Added `labs/001-confirm-lab-network/cleanup.md`.
- Added `labs/001-confirm-lab-network/lessons-learned.md`.
- Added placeholder `.gitkeep` files under `configs/`, `results/screenshots/`, and `results/logs/`.
- Updated `README.md` repo structure example to use the new lab directory name.

## Requested review

Please check:
- Commands are correct
- Expected outputs are realistic
- Cleanup is sufficient
- Safety boundaries are clear
- The Raspberry Pi subnet note is clear: `192.168.60.10` may require routing from `192.168.50.0/24`.
