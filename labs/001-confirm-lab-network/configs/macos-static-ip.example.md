# macOS Static IP Example

Use this as a checklist for assigning the Mac host address from `shared/ip-plan.md`.

## Target values

| Setting | Value |
| --- | --- |
| IP address | `192.168.50.20` |
| Subnet mask | `255.255.255.0` |
| Gateway/router | `192.168.50.1` |
| DNS | `192.168.50.1`, or a lab-approved DNS resolver |

## GUI method

1. Open System Settings.
2. Go to Network.
3. Select the interface connected to the lab network.
4. Open Details.
5. Set IPv4 configuration to Manual.
6. Enter the target values above.
7. Apply the change.
8. Confirm the Mac shows `192.168.50.20`.

## Command-line verification

Run this on the Mac:

```bash
ifconfig
netstat -rn
ping -c 4 192.168.50.10
```

Expected result:

- The lab interface shows `192.168.50.20`.
- The route table includes a path through `192.168.50.1` when the lab router is available.
- The Mac can reach Kali at `192.168.50.10`.
