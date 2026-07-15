# Role 03 — Principal Engineer, Platform (Device Finance)

> **JD reads like it was written for you.** AI/LLM-assisted incident summaries, RCA drafts, runbook automation, security-by-default, Vault, GitLab, K8s, AWS, Java/Spring Boot, MongoDB, Oracle. ONE caveat: confirm whether this is Principal IC (you'd lose the 15 reports) or Principal-with-team.

## Job metadata
- **URL:** https://careers.t-mobile.com/principal-engineer-platform/job/1D12E4F97A123671866569B191B72B85
- **Req ID hash:** `1D12E4F97A123671866569B191B72B85`
- **Location:** Not surfaced (Bellevue likely)
- **Posted base salary:** Not surfaced. Principal Engineer band ~$190K – $270K (Levels.fyi, Bellevue/Seattle T-Mobile).
- **Team:** Device Finance Platform Engineering
- **Level:** Principal IC (likely — confirm)
- **Match score:** **88%**
- **Verdict:** **Natural fit. Confirm IC vs. people-leader scope before applying.**

## What matched
- **"Generate AI/LLM-assisted incident summaries, RCA drafts, runbook suggestions"** → you have shipped a GenAI metrics agent + use Claude Code/Copilot for runbook automation
- **"Security & compliance: threat modeling, secrets/identity, RBAC/ABAC, SOX/PCI, secure SDLC, AI/AIOps guardrails"** → Vault + CyberArk in production, Cybersecurity Syndicate reviews, vulnerability remediation, zero critical vulnerabilities for 18 months
- **"Steward Oracle DB and MongoDB"** → both in production at 25M-msg-per-day scale
- **"10+ years platform-scale cloud-native; 5+ leading architecture across teams"** → 10 yrs T-Mobile; lead architecture across 4 platforms
- **"Java/Spring Boot microservices, distributed systems, REST/gRPC"** → exact stack
- **"3+ years CI/CD with GitLab/GitHub, IaC, Kubernetes, AWS"** → exact stack
- **"Enable AI/ML and dev tooling: model serving, AI agents, golden paths"** → MART = your golden path

## Gaps
1. **Domain is Device Finance / OFSLL** (Oracle Financial Services Lending and Leasing) — you haven't run consumer financing platforms specifically
2. **Principal IC vs. Principal-with-team** — your current Principal is *with* people management; this might require giving up the 15 reports
3. **Customer-facing financial regulations (Reg Z, Reg E)** — you've operated FCC-regulated comms, not consumer-finance regulated platforms

## Gap mitigation
1. Frame platform-engineering muscle as domain-portable. AJO/MoEngage migrations + Oracle production experience transfer; OFSLL specifics learnable in 60 days.
2. **Critical: ask the hiring chain whether Principal IC is fixed or whether Principal-with-team is in scope.** Decide before applying whether you want to give up people leadership for IC depth (legitimate trade depending on career goal).
3. Reg Z / Reg E → reframe FCC + DND compliance as "regulated-platform DNA"; commit to picking up consumer-finance specifics in onboarding.

## Internal-application strategy
- **Career-decision question first:** if this is Principal IC only, do you want it? Going from Principal+people-management to Principal-IC is a real trade. Sometimes valuable (depth, technical leadership), sometimes regretful (loss of leverage).
- **Manager conversation:** different from Roles 01/02 — this isn't a step up in title, it's a domain shift. Frame as "I want to broaden my platform credentials."
- **Backchannel:** find one of the existing Principal Engineers on the team. Ask: "Is this IC-only? What does the next 18 months look like?"

## Pre-application checklist
- [ ] Decide: are you OK with potentially losing the 15 reports for an IC role?
- [ ] Confirm IC vs. people-leader scope with hiring chain
- [ ] Manager conversation complete
- [ ] Posted salary range confirmed
- [ ] If IC: prep deep-technical loop (system design, AI/LLM-augmented ops, security)

---

# TAILORED TALKING POINTS

## Lead with this

> "I have shipped what this JD describes — production AI/LLM-augmented operations, security-by-default platforms, Java/Spring Boot microservices on Kubernetes/AWS with GitLab CI/CD, Oracle and MongoDB stewardship at 25M-msg-per-day scale. I run a 15-person SRE team at 99.99% availability for 36 consecutive months with 18 months of zero critical vulnerabilities. The Principal Engineer Platform charter for Device Finance reads like my next 5 years."

## Top resume bullets to emphasize

- Built and deployed **production GenAI metrics agent** (natural-language platform-health queries) and **Splunk MLTK ML anomaly detection** — direct evidence of "AI/LLM-augmented operations"
- Implemented **Claude Code + GitHub Copilot workflows** for SRE team of 15; ~25% routine-toil reduction
- Operate **Oracle and MongoDB** in production at 25M-msg-per-day; led Oracle → MongoDB zero-downtime migration with 8-week shadow-traffic validation
- Run **Vault + CyberArk** in production; Cybersecurity Syndicate review cadence; **zero critical vulnerabilities in production for 18 months**
- **Java / Spring Boot / Kubernetes / AWS / GitLab CI/CD** as primary stack across 4 platforms
- Authored **MART (Monitoring/Alerting/Reporting/Troubleshooting) framework** — the "golden path" pattern this JD asks for
- Led **6 zero-downtime migrations** including TIBCO → Spring Boot, EMS → RabbitMQ, VM → PCF → Kubernetes → AWS

## Key questions to ask the hiring chain

1. **"Is this Principal IC only, or is Principal-with-team in scope?"** (most important question)
2. "What's the relationship between this Principal Engineer and the Director of Engineering for Device Finance?"
3. "What are the top 3 platform problems this role is hired to solve in year 1?"
4. "Reg Z / Reg E exposure — how much regulatory-domain depth is expected vs. learnable?"

## Hiring-manager pitch

> "I'm SRE Principal at T-Mobile, 10 years in. I lead 15 engineers running 4 platforms at 25M messages a day, 99.99% availability for 3 years, with production AI in the operations layer — ML anomaly detection in Splunk MLTK and a GenAI metrics agent live today. The Principal Engineer Platform charter reads like an exact match — Java/Spring Boot, Kubernetes, AWS, Vault, GitLab, Oracle, MongoDB, AI/LLM-augmented ops. Before I apply I want to understand: is this Principal IC, or does Principal-with-team fit the charter? And what would year 1 look like to you?"
