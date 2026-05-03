# Expected Output

Exact interface names, MAC addresses, and latency values will vary. The examples below show the expected shape of successful and failed results.

## Kali IP address check

Command:

```bash
ip addr
ip route
```

Expected example:

`ip addr` example:

```text
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
    inet 192.168.50.10/24 brd 192.168.50.255 scope global eth0
```

`ip route` example:

```text
default via 192.168.50.1 dev eth0 proto static metric 100
```

## Kali to Mac ping

Command:

```bash
ping -c 4 192.168.50.20
```

Expected example:

```text
PING 192.168.50.20 (192.168.50.20) 56(84) bytes of data.
64 bytes from 192.168.50.20: icmp_seq=1 ttl=64 time=0.641 ms
64 bytes from 192.168.50.20: icmp_seq=2 ttl=64 time=0.522 ms
64 bytes from 192.168.50.20: icmp_seq=3 ttl=64 time=0.558 ms
64 bytes from 192.168.50.20: icmp_seq=4 ttl=64 time=0.549 ms

--- 192.168.50.20 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 0.522/0.568/0.641/0.044 ms
```

## Kali to Raspberry Pi ping when routed

Command:

```bash
ping -c 4 192.168.60.10
```

Expected example when routing is configured:

```text
PING 192.168.60.10 (192.168.60.10) 56(84) bytes of data.
64 bytes from 192.168.60.10: icmp_seq=1 ttl=63 time=1.21 ms
64 bytes from 192.168.60.10: icmp_seq=2 ttl=63 time=1.05 ms
64 bytes from 192.168.60.10: icmp_seq=3 ttl=63 time=1.12 ms
64 bytes from 192.168.60.10: icmp_seq=4 ttl=63 time=1.08 ms

--- 192.168.60.10 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 1.050/1.115/1.210/0.061 ms
```

## Kali to Raspberry Pi ping when not routed

Command:

```bash
ping -c 4 192.168.60.10
```

Expected example when routing is missing:

```text
PING 192.168.60.10 (192.168.60.10) 56(84) bytes of data.
From 192.168.50.10 icmp_seq=1 Destination Host Unreachable
From 192.168.50.10 icmp_seq=2 Destination Host Unreachable
From 192.168.50.10 icmp_seq=3 Destination Host Unreachable
From 192.168.50.10 icmp_seq=4 Destination Host Unreachable

--- 192.168.60.10 ping statistics ---
4 packets transmitted, 0 received, +4 errors, 100% packet loss, time 3066ms
```

## Kali ARP table

Command:

```bash
arp -n
```

Expected example:

```text
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.50.20            ether   aa:bb:cc:dd:ee:ff   C                     eth0
192.168.50.1             ether   11:22:33:44:55:66   C                     eth0
```

## Mac to Kali ping

Command:

```bash
ping -c 4 192.168.50.10
```

Expected example:

```text
PING 192.168.50.10 (192.168.50.10): 56 data bytes
64 bytes from 192.168.50.10: icmp_seq=0 ttl=64 time=0.612 ms
64 bytes from 192.168.50.10: icmp_seq=1 ttl=64 time=0.531 ms
64 bytes from 192.168.50.10: icmp_seq=2 ttl=64 time=0.544 ms
64 bytes from 192.168.50.10: icmp_seq=3 ttl=64 time=0.526 ms

--- 192.168.50.10 ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 0.526/0.553/0.612/0.034 ms
```

## Mac ARP table

Command:

```bash
arp -n 192.168.50.10
```

Expected example:

```text
? (192.168.50.10) at aa:bb:cc:dd:ee:ff on en0 ifscope [ethernet]
```

## Raspberry Pi IP address check

Command:

```bash
ip addr
ip route
```

Expected example:

`ip addr` example:

```text
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
    inet 192.168.60.10/24 brd 192.168.60.255 scope global eth0
```

`ip route` example:

```text
default via 192.168.60.1 dev eth0 proto static metric 100
```

## Raspberry Pi to Kali ping

Command:

```bash
ping -c 4 192.168.50.10
```

Expected example when routing is configured:

```text
PING 192.168.50.10 (192.168.50.10) 56(84) bytes of data.
64 bytes from 192.168.50.10: icmp_seq=1 ttl=63 time=1.18 ms
64 bytes from 192.168.50.10: icmp_seq=2 ttl=63 time=1.06 ms
64 bytes from 192.168.50.10: icmp_seq=3 ttl=63 time=1.09 ms
64 bytes from 192.168.50.10: icmp_seq=4 ttl=63 time=1.10 ms

--- 192.168.50.10 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 1.060/1.107/1.180/0.044 ms
```
