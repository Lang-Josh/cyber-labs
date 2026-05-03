# Hardware

## Required systems

The available devices come from `shared/hardware-inventory.md`.

| Hardware | Lab role | Expected IP | Notes |
| --- | --- | --- | --- |
| Mac running macOS | Admin workstation and Kali host | `192.168.50.20` | Used to manage the lab and host the Kali VM |
| Kali Linux VM on Mac | Attacker | `192.168.50.10` | Primary system for later lab commands |
| Raspberry Pi 5 8GB | Linux target | `192.168.60.10` | Owned lab target — direct console access via keyboard and monitor |
| Monitor | Raspberry Pi display | N/A | Connected directly to Raspberry Pi |
| Keyboard | Raspberry Pi input | N/A | Connected directly to Raspberry Pi |
| Ethernet switch | Lab network switching | N/A | Connects physical lab devices |
| Ethernet cables | Network links | N/A | Connect Mac, Raspberry Pi, and switch as needed |

## Optional systems

- pfSense or OPNsense router at `192.168.50.1`
- Managed switch for future VLAN labs
- Mini PC for future always-on lab services

## Safety notes

- Use only owned lab devices.
- Do not SSH into devices during this lab unless a separate instruction explicitly allows it.
- Assign static IP addresses before running the validation tasks.
- Do not change firewall rules, router settings, or switch settings as part of this lab.
