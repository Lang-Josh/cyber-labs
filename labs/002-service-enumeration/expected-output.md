# Expected Output

Your exact output may differ depending on the target image and enabled services. The examples below show the expected shape of the results.

## Basic TCP scan

Command:
```bash
nmap 192.168.50.10 -oN results/logs/002-basic-tcp-scan.txt
```

Example output:
```text
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-25 14:00 EDT
Nmap scan report for 192.168.50.10
Host is up (0.0012s latency).
Not shown: 996 closed tcp ports (reset)
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 2.41 seconds
```

## Service and version scan

Command:
```bash
nmap -sV 192.168.50.10 -oN results/logs/002-service-version-scan.txt
```

Example output:
```text
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-25 14:05 EDT
Nmap scan report for 192.168.50.10
Host is up (0.0011s latency).
Not shown: 996 closed tcp ports (reset)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.52 ((Ubuntu))
139/tcp open  netbios-ssn Samba smbd 4.X - 4.Y
445/tcp open  netbios-ssn Samba smbd 4.X - 4.Y
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.73 seconds
```

## Default scripts scan

Command:
```bash
nmap -sC -sV 192.168.50.10 -oN results/logs/002-default-scripts-scan.txt
```

Example output:
```text
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.9p1 Ubuntu 3ubuntu0.6
| ssh-hostkey:
|   256 SHA256:EXAMPLEKEYFINGERPRINT ECDSA
|_  256 SHA256:EXAMPLEKEYFINGERPRINT ED25519
80/tcp  open  http        Apache httpd 2.4.52 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
139/tcp open  netbios-ssn Samba smbd 4.X - 4.Y
445/tcp open  netbios-ssn Samba smbd 4.X - 4.Y
```

## Results checklist

- `results/logs/002-basic-tcp-scan.txt` exists.
- `results/logs/002-service-version-scan.txt` exists.
- `results/logs/002-default-scripts-scan.txt` exists.
- `results/logs/002-focused-service-scan.txt` exists.
- `results.md` contains a concise table of discovered services.
