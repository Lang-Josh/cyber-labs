# Claude to Codex

## Review result

Reviewed PR #5 (`codex/lab-001-static-ip-plan`) on 2026-04-29. Three issues must be fixed before merge. Full comments posted on the PR.

**Approved:**
- `192.168.60.0/24` as current baseline (not future-only) — correct call.
- NetworkManager examples for Kali and Raspberry Pi OS — commands are correct.
- Task 0 gate, `results.md` gateway columns, topology and hardware changes — all good.

## Required changes before merge

**1. `labs/001-confirm-lab-network/expected-output.md` — split merged code blocks**

The Kali section and Raspberry Pi section each show `ip addr` and `ip route` output merged into one code block. They are separate commands with separate output. Split each into two labeled code blocks so a beginner knows which output comes from which command.

Affects two sections: Kali IP address check (near top) and Raspberry Pi IP address check (near bottom).

**2. `labs/001-confirm-lab-network/configs/kali-static-ip.example.md` and `configs/raspberry-pi-static-ip.example.md` — DNS placeholder note**

Both files set `ipv4.dns` to the gateway IP. Add a note that this is a placeholder and `1.1.1.1` can be used if the lab router is not yet running a resolver. Lab 001 does not test DNS so this does not block the lab, but it will cause confusing failures in general system use.

**3. `labs/001-confirm-lab-network/cleanup.md` — clarify static IPs are kept, not reverted**

Step 4 says "Leave device network settings unchanged." Now that static IPs are a prerequisite assigned before the lab, a beginner could read this as an instruction to revert to DHCP. Change to: "Keep the static IP assignments in place. They are intentional and will be used by later labs."
