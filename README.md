# Cyber Labs

A personal cybersecurity lab knowledge base built and maintained by a three-entity team: you, Codex, and Claude Code. Labs are reproducible, structured, and tied directly to certification exam topics.

---

## System design

```
┌─────────────────────────────────────────────────────────────────┐
│                          YOU                                     │
│                                                                  │
│  • Describe lab from exam chapter                                │
│  • Trigger agents via terminal prompts                           │
│  • Review and merge PRs on GitHub                                │
│  • Run labs on physical hardware                                 │
│  • Save real outputs back to repo                                │
└────────────┬───────────────────────────────┬────────────────────┘
             │                               │
     prompt Codex                    prompt Claude Code
             │                               │
             ▼                               ▼
┌────────────────────┐           ┌───────────────────────┐
│       CODEX        │           │      CLAUDE CODE       │
│                    │           │                        │
│  Reads:            │           │  Reads:                │
│  • AGENTS.md       │           │  • CLAUDE.md           │
│  • .codex/notes.md │           │  • shared/             │
│  • shared/         │           │  • templates/          │
│  • templates/      │           │  • agent-handoff/      │
│  • agent-handoff/  │           │    codex-to-claude.md  │
│    claude-to-codex │           │                        │
│                    │           │  Does:                 │
│  Does:             │           │  • Reviews PRs         │
│  • Creates labs    │           │  • Checks commands     │
│  • Writes files    │           │  • Checks outputs      │
│  • Commits branch  │           │  • Checks safety       │
│  • Opens PR        │           │  • Leaves PR comments  │
│  • Creates issues  │           │  • Updates handoff     │
└────────┬───────────┘           └───────────┬───────────┘
         │                                   │
         │         ┌─────────────┐           │
         └────────►│   GITHUB    │◄──────────┘
                   │             │
                   │  • master   │
                   │  • branches │
                   │  • PRs      │
                   │  • issues   │
                   │  • comments │
                   └──────┬──────┘
                          │
                          │ source of truth
                          ▼
          ┌───────────────────────────────┐
          │         REPO STRUCTURE        │
          │                               │
          │  AGENTS.md   CLAUDE.md        │
          │  .mcp.json   .codex/          │
          │                               │
          │  shared/                      │
          │    ip-plan.md                 │
          │    hardware-inventory.md      │
          │    common-commands.md         │
          │    credentials.example.md     │
          │                               │
          │  templates/lab-template/      │
          │    (11 files)                 │
          │                               │
          │  labs/                        │
          │    001-network-discovery/     │
          │    002-service-enumeration/   │
          │    003-.../                   │
          │                               │
          │  agent-handoff/               │
          │    codex-to-claude.md         │
          │    claude-to-codex.md         │
          │                               │
          │  detections/  diagrams/       │
          │  scripts/     results/        │
          └───────────────────────────────┘
                          │
                          │ you run labs against
                          ▼
          ┌───────────────────────────────┐
          │         PHYSICAL LAB          │
          │                               │
          │  Mac (host)                   │
          │    └─ Kali VM (attacker)      │
          │                               │
          │  Raspberry Pi (target)        │
          │  ESP8266 (IoT target)         │
          │  Alfa adapter (wireless)      │
          │  Switch                       │
          │                               │
          │  Future:                      │
          │    Managed switch (VLANs)     │
          │    Mini PC (SIEM/AD/targets)  │
          │    pfSense (firewall/routing) │
          └───────────────────────────────┘
```

---

## Lab cycle

```
Exam chapter
    │
    ▼
You describe lab ──► Codex builds files ──► PR opened on GitHub
                                                    │
                                           Claude reviews PR
                                                    │
                                           PR comments posted
                                                    │
                                           You merge to master
                                                    │
                                        You run lab on hardware
                                                    │
                                        Real outputs saved to repo
                                                    │
                                              Repeat
```

---

## How the agents coordinate

GitHub is the only thing both agents touch directly. They never call each other and share no memory. They coordinate exclusively through:

- GitHub issues — one per lab, used to define requirements and assign work
- GitHub PRs — Codex opens them, Claude reviews and comments, you merge
- agent-handoff/ files — structured notes passed between agents between sessions
- AGENTS.md and CLAUDE.md — standing instructions each agent reads automatically

---

## Repo structure

| Folder | Purpose |
|---|---|
| labs/ | Finished and in-progress labs |
| templates/ | Reusable lab template all labs must follow |
| shared/ | IP plan, hardware inventory, common commands |
| scripts/ | Deploy, reset, and evidence collection scripts |
| detections/ | Wazuh, Sigma, and Sysmon detection content |
| diagrams/ | Network and lab diagrams |
| agent-handoff/ | Coordination notes between Codex and Claude Code |
| results/ | Top-level results storage |

---

## Each lab includes

- Goal and difficulty
- Hardware required
- Network topology
- Setup steps
- Step-by-step instructions with commands
- Expected outputs
- Results template
- Cleanup steps
- Lessons learned
