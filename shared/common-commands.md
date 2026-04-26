# Common Commands

## Git

```bash
git status
git checkout -b branch-name
git add .
git commit -m "message"
git push -u origin branch-name
```

## Network checks

```bash
ip addr
ifconfig
ping TARGET_IP
traceroute TARGET_IP
```

## Nmap

```bash
nmap -sn 192.168.50.0/24
nmap -sV TARGET_IP
nmap -p- TARGET_IP
```

## Logs

```bash
sudo tail -f /var/log/auth.log
sudo tail -f /var/log/syslog
sudo tail -f /var/log/apache2/access.log
```
