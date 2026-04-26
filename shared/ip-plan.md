# IP Plan

## Current simple lab

| Network | Purpose | CIDR |
|---|---|---|
| Lab network | Basic sandbox | 192.168.50.0/24 |

## Future segmented lab

| Network | Purpose | CIDR | Gateway |
|---|---|---|---|
| Attacker | Kali and attack tooling | 192.168.50.0/24 | 192.168.50.1 |
| Internal | Client and target hosts | 192.168.60.0/24 | 192.168.60.1 |
| Servers | SIEM, AD, logging, vulnerable services | 192.168.70.0/24 | 192.168.70.1 |
| IoT | ESP8266 and IoT devices | 192.168.80.0/24 | 192.168.80.1 |

## Reserved addresses

| Device | Role | IP |
|---|---|---|
| pfSense or OPNsense | Router and firewall | 192.168.50.1 |
| Kali VM | Attacker | 192.168.50.10 |
| Mac host | Admin workstation | 192.168.50.20 |
| Raspberry Pi 1 | Linux target | 192.168.60.10 |
| Windows client | Endpoint | 192.168.60.20 |
| Wazuh | SIEM | 192.168.70.10 |
| Windows Server | Domain Controller | 192.168.70.20 |
| ESP8266 | IoT target | 192.168.80.10 |
