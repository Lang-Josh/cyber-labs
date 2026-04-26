# Instructions

## Safety scope

Only scan the owned Linux target at `192.168.50.10` on your isolated lab network. Do not run these commands against public IP addresses, third-party networks, or production systems.

## Task 1: Confirm Nmap is available

Command:
```bash
nmap --version
```

Expected behavior:
Kali prints the installed Nmap version and enabled features.

## Task 2: Create a results directory

Command:
```bash
mkdir -p results/logs results/screenshots
```

Expected behavior:
The local output folders exist. This does not modify the target.

## Task 3: Run a basic TCP port scan

Command:
```bash
nmap 192.168.50.10 -oN results/logs/002-basic-tcp-scan.txt
```

Expected behavior:
Nmap scans the most common 1,000 TCP ports and reports any open ports.

## Task 4: Run service and version detection

Command:
```bash
nmap -sV 192.168.50.10 -oN results/logs/002-service-version-scan.txt
```

Expected behavior:
Nmap reports detected service names and version details when available.

## Task 5: Run safe default scripts against discovered services

Command:
```bash
nmap -sC -sV 192.168.50.10 -oN results/logs/002-default-scripts-scan.txt
```

Expected behavior:
Nmap runs default scripts intended for safe discovery and prints extra service details, such as SSH host key fingerprints or HTTP page titles.

## Task 6: Scan only the discovered open ports

Replace the port list with the ports you found in earlier scans.

Command:
```bash
nmap -sC -sV -p 22,80,139,445 192.168.50.10 -oN results/logs/002-focused-service-scan.txt
```

Expected behavior:
Nmap focuses on known open ports and returns cleaner, faster output.

## Task 7: Summarize findings

Update `results.md` with:

- Date and time of the scan
- Scanner IP
- Target IP
- Open ports
- Service names
- Version details, if detected
- Any unknown services that need follow-up

Do not attempt login, exploitation, password guessing, or configuration changes in this lab.
