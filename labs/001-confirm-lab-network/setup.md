# Setup

## Pre-checks

- Confirm you are working only with owned lab systems.
- Confirm the Mac, Kali VM, and Raspberry Pi are powered on.
- Confirm the devices are connected to the intended lab network.
- Confirm the expected IP addresses in `shared/ip-plan.md`.
- Keep `shared/credentials.example.md` as the only credential reference. Do not record real passwords.

## Expected addresses

| Device | Expected IP |
| --- | --- |
| Kali VM | `192.168.50.10` |
| Mac host | `192.168.50.20` |
| Raspberry Pi 1 | `192.168.60.10` |

## Prepare result folders

From this lab directory, create result folders if they are missing:

```bash
mkdir -p results/logs results/screenshots
```

## Record the environment

Before running the tasks, update `results.md` with:

- Date
- Device names
- Observed IP addresses
- Whether the Raspberry Pi is expected to be routed from `192.168.50.0/24` to `192.168.60.0/24`

## No live-system changes

Do not change network settings during this lab. If a command fails, record the failure and use the troubleshooting notes as follow-up work.
