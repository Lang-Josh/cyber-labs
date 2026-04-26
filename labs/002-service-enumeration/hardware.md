# Hardware

## Required systems

- Kali Linux VM or host on the isolated lab network.
- Owned Linux target VM at `192.168.50.10`.
- Host-only, NAT lab, or otherwise isolated network where both systems are allowed to communicate.

## Recommended target services

The exact target may vary, but this lab works best if the Linux target exposes several common services, such as:

- SSH on TCP/22
- HTTP on TCP/80
- SMB on TCP/139 and TCP/445, if intentionally enabled for the lab

Do not enable services on a live or production machine for this lab.
