# Setup

## Pre-checks

- Confirm you are working only with owned lab systems.
- Confirm the Mac, Kali VM, and Raspberry Pi are powered on.
- Confirm the devices are connected to the intended lab network.
- Confirm the expected IP addresses in `shared/ip-plan.md`.
- Keep `shared/credentials.example.md` as the only credential reference. Do not record real passwords.
- Use the Raspberry Pi's directly connected monitor and keyboard. Do not SSH into the Pi for this lab.

## Expected addresses

| Device | Expected IP |
| --- | --- |
| Kali VM | `192.168.50.10` |
| Mac host | `192.168.50.20` |
| Raspberry Pi 1 | `192.168.60.10` |

## Static IP prerequisite

Before running the validation tasks, assign the static addresses above using the examples in `configs/`:

- `configs/macos-static-ip.example.md`
- `configs/kali-static-ip.example.md`
- `configs/raspberry-pi-static-ip.example.md`

Use the router or firewall gateway from `shared/ip-plan.md` when the segmented lab network is available:

| Network | Gateway |
| --- | --- |
| `192.168.50.0/24` | `192.168.50.1` |
| `192.168.60.0/24` | `192.168.60.1` |

If the Raspberry Pi still shows a DHCP address, stop and fix the static assignment before continuing.

## Verify assigned addresses

Run this on Kali and the Raspberry Pi:

```bash
ip addr
ip route
```

On the Mac, confirm the static address in System Settings or with:

```bash
ifconfig
netstat -rn
```

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
- Whether the observed IPs match the static IP plan

## No live-system changes

Do not improvise new IP addresses during this lab. If a command fails, record the failure and use the troubleshooting notes as follow-up work.
