# Instructions

## Safety scope

Run these commands only on the Mac, Kali VM, and Raspberry Pi that belong to this lab. Do not test public IP addresses, third-party networks, or production systems.

## Task 1: Confirm the Kali VM IP address

Run this on Kali:

```bash
ip addr
```

Expected behavior:
Kali shows an active network interface with `inet 192.168.50.10/24`. The interface name may be `eth0`, `ens33`, `enp0s3`, or another Linux interface name.

Record the interface name and IP address in `results.md`.

## Task 2: Confirm Kali can reach the Mac

Run this on Kali:

```bash
ping -c 4 192.168.50.20
```

Expected behavior:
Kali receives replies from the Mac host. Packet loss should be `0%` on a healthy local lab network.

Record the packet loss and average round-trip time in `results.md`.

## Task 3: Confirm Kali can reach the Raspberry Pi

Run this on Kali:

```bash
ping -c 4 192.168.60.10
```

Expected behavior:
If routing between the lab subnets is configured, Kali receives replies from the Raspberry Pi.

If the command shows `Destination Host Unreachable`, `Network is unreachable`, or `100% packet loss`, record the exact result. Because the Raspberry Pi IP is reserved in `192.168.60.0/24`, failure is expected when no router connects the `192.168.50.0/24` and `192.168.60.0/24` networks.

## Task 4: Check Kali's ARP table

Run this on Kali:

```bash
arp -n
```

Expected behavior:
Kali shows a neighbor entry for `192.168.50.20` after a successful ping to the Mac. The Raspberry Pi may not appear in ARP if it is across a routed subnet or unreachable.

Record any entries for:

- `192.168.50.20`
- `192.168.60.10`
- `192.168.50.1`, if a lab router exists

## Task 5: Confirm the Mac can reach Kali

Run this on the Mac:

```bash
ping -c 4 192.168.50.10
```

Expected behavior:
The Mac receives replies from Kali with `0% packet loss`.

Record the result in `results.md`.

## Task 6: Check the Mac ARP table

Run this on the Mac:

```bash
arp -n 192.168.50.10
```

Expected behavior:
The Mac shows a neighbor entry for Kali after a successful ping.

Record whether the entry exists.

## Task 7: Confirm the Raspberry Pi can reach Kali

Run this on the Raspberry Pi console:

```bash
ping -c 4 192.168.50.10
```

Expected behavior:
If routing between the Raspberry Pi subnet and the Kali subnet is configured, the Raspberry Pi receives replies from Kali.

If the command fails, record the exact message and note that routing between `192.168.60.0/24` and `192.168.50.0/24` needs follow-up.

## Task 8: Check the Raspberry Pi IP address and ARP table

Run these on the Raspberry Pi:

```bash
ip addr
arp -n
```

Expected behavior:
The Raspberry Pi shows `inet 192.168.60.10/24` on its active interface. The ARP table may show a router or gateway entry if traffic crosses subnets.

Record the active interface name, IP address, and any relevant ARP entries in `results.md`.

## Task 9: Summarize pass or fail

Update `results.md` with:

- Which devices could reach each other
- Which commands failed
- Exact failure messages
- Whether a router is needed before later labs
- Any follow-up work required before running Level 1 labs
