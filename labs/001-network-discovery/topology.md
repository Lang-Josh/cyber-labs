# Network Topology

## Devices

| Device | Role | IP Address | Notes |
|---|---|---|---|
| Kali | Attacker | TBD | Runs scan or attack tools |
| Target | Victim | TBD | Receives traffic |
| SIEM | Detection | TBD | Optional |

## Diagram

```mermaid
flowchart LR
  Kali[Kali Attacker] --> Switch[Lab Switch]
  Switch --> Target[Target Host]
  Target --> SIEM[SIEM Optional]
```
