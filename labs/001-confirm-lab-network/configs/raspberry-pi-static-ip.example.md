# Raspberry Pi Static IP Example

Use this as a checklist for assigning the Raspberry Pi address from `shared/ip-plan.md`.

## Target values

| Setting | Value |
| --- | --- |
| IP address | `192.168.60.10` |
| Prefix | `/24` |
| Gateway | `192.168.60.1` |
| DNS | `192.168.60.1`, or a lab-approved DNS resolver |

## NetworkManager example

Use the Raspberry Pi's directly connected monitor and keyboard. Do not SSH into the Pi for this setup unless a separate instruction explicitly allows it.

Find the connection name:

```bash
nmcli connection show
```

Assign the static address after replacing `CONNECTION_NAME` with the active lab connection name:

```bash
sudo nmcli connection modify "CONNECTION_NAME" \
  ipv4.method manual \
  ipv4.addresses 192.168.60.10/24 \
  ipv4.gateway 192.168.60.1 \
  ipv4.dns 192.168.60.1
```

Reconnect:

```bash
sudo nmcli connection down "CONNECTION_NAME"
sudo nmcli connection up "CONNECTION_NAME"
```

## Verification

Run this on the Raspberry Pi:

```bash
ip addr
ip route
ping -c 4 192.168.60.1
ping -c 4 192.168.50.10
```

Expected result:

- The lab interface shows `192.168.60.10/24`.
- The route table uses `192.168.60.1` when the lab router is available.
- The Raspberry Pi can reach Kali at `192.168.50.10` when routing between lab subnets is available.

If `nmcli` is not available, record that in `results.md` and use the Raspberry Pi OS network configuration method for the installed OS version. Do not store passwords or real secrets in this repo.
