# Topology

## Devices

| Device | Role | IP Address | Network | Notes |
| --- | --- | --- | --- | --- |
| Kali VM | Attacker | `192.168.50.10` | `192.168.50.0/24` | Runs confirmation commands |
| Mac host | Admin workstation | `192.168.50.20` | `192.168.50.0/24` | Hosts Kali VM |
| Raspberry Pi 1 | Linux target | `192.168.60.10` | `192.168.60.0/24` | Target for later Linux labs |
| pfSense or OPNsense | Router and firewall | `192.168.50.1` | `192.168.50.0/24` | Planned or optional router |

## Diagram

```text
                         Lab network

  Mac host                         Kali VM
  192.168.50.20  <------------->   192.168.50.10
       |
       | Ethernet or virtual network
       |
  Lab switch / router  <-------->  Raspberry Pi 1
  192.168.50.1 optional            192.168.60.10
```

## Network notes

- The Mac and Kali VM are expected on `192.168.50.0/24`.
- The Raspberry Pi is reserved as `192.168.60.10`, which is a different subnet from Kali and the Mac.
- If there is no router between `192.168.50.0/24` and `192.168.60.0/24`, pings to the Raspberry Pi may fail. Record that result instead of changing live network settings.
- This lab confirms baseline reachability only. It does not perform port scanning, exploitation, password guessing, or service enumeration.
