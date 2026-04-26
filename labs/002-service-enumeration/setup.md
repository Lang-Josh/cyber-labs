# Setup

## Prerequisites

- Kali can reach the owned Linux target at `192.168.50.10`.
- Nmap is installed on Kali.
- You have permission to scan the target.
- The target is a sandbox VM or lab host, not a live production system.

## Setup steps

1. Start the Kali VM.
2. Start the owned Linux target VM.
3. Confirm the target IP is still `192.168.50.10` from the lab console or VM settings.
4. Create local result folders if they are missing:

```bash
mkdir -p results/logs results/screenshots
```

5. From Kali, confirm basic reachability:

```bash
ping -c 4 192.168.50.10
```

If ping is blocked but you know the target is online, continue with the TCP scan steps. Some Linux hosts block ICMP echo requests by default.

6. Record the date, Kali IP, target IP, and any known target role in `results.md`.
