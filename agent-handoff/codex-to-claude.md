# Codex to Claude

## Current task

Updated lab 001 so it requires the static IP plan from `shared/ip-plan.md` before validation.

## Files changed

- Updated `shared/ip-plan.md` to make the current baseline static plan explicit:
  - Attacker/Admin network: `192.168.50.0/24`, gateway `192.168.50.1`
  - Target network: `192.168.60.0/24`, gateway `192.168.60.1`
- Updated `labs/001-confirm-lab-network/` docs so lab 001 expects:
  - Kali VM: `192.168.50.10/24`
  - Mac host: `192.168.50.20/24`
  - Raspberry Pi 1: `192.168.60.10/24`
- Added static-IP examples under `labs/001-confirm-lab-network/configs/`:
  - `macos-static-ip.example.md`
  - `kali-static-ip.example.md`
  - `raspberry-pi-static-ip.example.md`
- Updated `results.md` to capture expected and observed gateways, unexpected IPs, and devices still using DHCP.

## Validation

- `python3 scripts/check-lab-structure.py labs/001-confirm-lab-network` passed.
- `python3 scripts/scan-secrets.py` passed.

## Requested review

Please check:

- The static addressing requirement is clear enough for a beginner running lab 001.
- The NetworkManager examples are acceptable for Kali and Raspberry Pi OS in this lab context.
- The repo should treat `192.168.60.0/24` as part of the current baseline now, not future-only.
