# Results

Use this file to record actual results. Do not paste secrets, real credentials, private keys, or data from non-lab systems.

## Summary

Date:

Lab operator:

## Expected devices

| Device | Expected IP | Expected gateway | Observed IP | Observed gateway | Status |
| --- | --- | --- | --- | --- | --- |
| Kali VM | `192.168.50.10` | `192.168.50.1` |  |  |  |
| Mac host | `192.168.50.20` | `192.168.50.1` |  |  |  |
| Raspberry Pi 1 | `192.168.60.10` | `192.168.60.1` |  |  |  |

## Reachability matrix

| Source | Target | Command | Result | Notes |
| --- | --- | --- | --- | --- |
| Kali VM | Mac host `192.168.50.20` | `ping -c 4 192.168.50.20` |  |  |
| Kali VM | Raspberry Pi `192.168.60.10` | `ping -c 4 192.168.60.10` |  |  |
| Mac host | Kali VM `192.168.50.10` | `ping -c 4 192.168.50.10` |  |  |
| Raspberry Pi | Kali VM `192.168.50.10` | `ping -c 4 192.168.50.10` |  |  |

## ARP observations

| Device checked | Command | Relevant entries | Notes |
| --- | --- | --- | --- |
| Kali VM | `arp -n` |  |  |
| Mac host | `arp -n 192.168.50.10` |  |  |
| Raspberry Pi | `arp -n` |  |  |

## Actual command outputs

Paste sanitized command output here or store text files under `results/logs/`.

## Screenshots

Store screenshots in:

```text
results/screenshots/
```

## Follow-up work

- Routing needed between `192.168.50.0/24` and `192.168.60.0/24`:
- Devices with unexpected IP addresses:
- Devices still using DHCP:
- Commands that failed:
- Notes before starting Level 1 labs:
