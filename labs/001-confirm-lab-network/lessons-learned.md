# Lessons Learned

## Reflection questions

- Which devices had the expected IP addresses?
- Which pings succeeded?
- Which pings failed?
- Did the ARP table show the neighbors you expected?
- Was the Raspberry Pi reachable from Kali, or is routing needed between subnets?
- What should be fixed before running Level 1 labs?

## Concepts reinforced

- `ip addr` confirms local interface addresses on Linux systems.
- `ping` confirms basic Layer 3 reachability when ICMP is allowed.
- `arp` shows local neighbor entries for devices on the same broadcast domain.
- Devices on different subnets usually need a router to communicate.
- A failed baseline connectivity check should be recorded before more advanced lab work begins.

## Notes

- This lab is a baseline check, not an attack lab.
- A failed ping does not always mean a device is offline. It can also indicate missing routing, firewall policy, wrong IP assignment, or disconnected cabling.
- Reproducible lab notes make later troubleshooting easier.
