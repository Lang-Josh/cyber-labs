# Kali Static IP Example

Use this as a checklist for assigning the Kali address from `shared/ip-plan.md`.

## Target values

| Setting | Value |
| --- | --- |
| IP address | `192.168.50.10` |
| Prefix | `/24` |
| Gateway | `192.168.50.1` |
| DNS | `192.168.50.1`, or a lab-approved DNS resolver |

## NetworkManager example

Run this on Kali after replacing `CONNECTION_NAME` with the active lab connection name.

Find the connection name:

```bash
nmcli connection show
```

Assign the static address:

```bash
sudo nmcli connection modify "CONNECTION_NAME" \
  ipv4.method manual \
  ipv4.addresses 192.168.50.10/24 \
  ipv4.gateway 192.168.50.1 \
  ipv4.dns 192.168.50.1
```

Reconnect:

```bash
sudo nmcli connection down "CONNECTION_NAME"
sudo nmcli connection up "CONNECTION_NAME"
```

## Verification

Run this on Kali:

```bash
ip addr
ip route
ping -c 4 192.168.50.20
```

Expected result:

- The lab interface shows `192.168.50.10/24`.
- The default or lab route uses `192.168.50.1` when the lab router is available.
- Kali can reach the Mac at `192.168.50.20`.
