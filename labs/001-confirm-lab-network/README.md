# 001 - Confirm Lab Network

## Difficulty

Level 0

## Goal

Confirm that the Mac, Kali VM, and Raspberry Pi can reach each other on the lab network before running any other labs.

## Lab summary

This lab verifies basic network connectivity between the admin workstation, attacker VM, and Linux target. You will confirm each device's IP address, send ICMP echo requests with `ping`, inspect neighbor entries with `arp`, and record the results.

This lab does not require logging into third-party systems, changing device configuration, scanning public networks, or modifying live lab machines.

## Tools used

- `ip addr`
- `ping`
- `arp`

## Lab IPs

The expected IP addresses come from `shared/ip-plan.md`.

| Device | Role | Expected IP |
| --- | --- | --- |
| Kali VM | Attacker | `192.168.50.10` |
| Mac host | Admin workstation | `192.168.50.20` |
| Raspberry Pi 1 | Linux target | `192.168.60.10` |

## Files in this lab

- objectives.md
- hardware.md
- topology.md
- setup.md
- instructions.md
- expected-output.md
- results.md
- cleanup.md
- lessons-learned.md
- configs/
- results/
