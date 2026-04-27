# Hardware Inventory

## Current hardware

- Mac running macOS
- Kali Linux VM on Mac
- Raspberry Pi 5 8GB
- Raspberry Pi power supply
- Raspberry Pi case and active cooler
- MicroSD card and reader
- Monitor (connected to Raspberry Pi)
- Keyboard (connected to Raspberry Pi)
- Ethernet switch
- Ethernet cables
- Alfa USB WiFi adapter
- ESP8266 boards
- Dupont wires

## Planned upgrades

- Managed switch
- Mini PC for always-on lab services
- pfSense or OPNsense firewall box
- External SSD for VM snapshots and logs

## Lab roles

| Hardware | Role |
|---|---|
| Mac | Admin workstation and Kali host |
| Kali VM | Attacker |
| Raspberry Pi | Linux target — direct console access via keyboard and monitor |
| Mini PC | VM host, SIEM, AD, vulnerable targets |
| Managed switch | VLANs and port mirroring |
| pfSense or OPNsense box | Firewall, routing, segmentation |
| Alfa adapter | Wireless labs |
| ESP8266 | IoT labs |
