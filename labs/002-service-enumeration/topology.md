# Topology

## Devices

| Device | Role | IP Address | Notes |
| --- | --- | --- | --- |
| Kali | Scanner | Example: `192.168.50.20` | Runs Nmap from the lab network |
| Linux target | Owned target | `192.168.50.10` | Receives enumeration traffic |

## Diagram

```text
Kali scanner                         Owned Linux target
192.168.50.20  ------------------>   192.168.50.10
                isolated lab network
```

## Network notes

- The Kali IP may differ in your environment.
- The target IP for this lab is `192.168.50.10`.
- Keep both systems on an owned, isolated lab network.
- Do not scan third-party networks or production systems.
- This lab collects network observations only; it does not require logging into the target or changing target configuration.
