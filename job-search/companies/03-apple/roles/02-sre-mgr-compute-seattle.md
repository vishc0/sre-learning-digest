# Role 02 — SRE Manager, Compute (Apple Services Engineering) — Seattle

## Job metadata
- **JD URL:** https://jobs.apple.com/en-us/details/200602617/site-reliability-engineer-sre-manager-apple-services-engineering
- **Requisition ID:** 200602617
- **Team:** ASE Compute — VMs / containers / clusters powering Apple Services
- **Location:** Seattle, WA
- **Posted base salary:** Not retrieved by automated fetch. Apple ASE Manager band in Seattle ≈ **$216K – $325K** (based on peer ASE Manager req with verified band). **Confirm on live JD before applying** — WA law requires the range be posted.
- **Match score:** **86%**

## Why this role
Seattle is in your stated relocation set. ASE Compute = K8s + cloud + bare-metal compute orchestration, which is your strongest stack alignment after observability.

## What matched
- **"Massive clusters hosting VMs, containers, infrastructure that scales to Apple Services demand"** → led K8s migration of 4 platforms; AWS EKS / Lambda / SQS / SNS in production; 25M msgs/day on K8s
- **"Constant uptime, scale seamlessly"** → 99.99% across 36 months; zero customer-impacting Sev1s
- **"SRE manager leading a team"** → 15 reports; on-call command for Sev1/Sev2; postmortem culture
- **"Cloud + bare-metal compute"** → VM → PCF → Kubernetes → AWS migration leadership (every layer)
- **"Communication, cross-functional"** → Cybersecurity Syndicate reviews; AI metrics agent for leadership; integration test working group across 42 systems

## Gaps
1. **Apple-internal compute tooling** (likely internal orchestrators / Pie equivalents) — no exposure
2. **Go preferred** at ASE — you're Python-primary
3. **Hypervisor / KVM / kernel-level VM internals** — not on resume

## Gap mitigation
1. Internal tooling → cite track record of fast onboarding to internal toolchains (TIBCO → Spring Boot, Bitbucket → GitLab, AWS migration); offer 30-day deep-dive commitment in the loop
2. Go → see Role 01 mitigation; ship one Go tool in 60 days; mention the upskill in cover letter
3. Hypervisor → reframe Docker + K8s container-runtime experience as "compute substrate"; concede VM internals honestly

## Pre-application checklist
- [ ] Open live JD and capture WA-mandated salary range (must be on page)
- [ ] Confirm Seattle is correct location (not "Seattle preferred, Cupertino acceptable")
- [ ] LinkedIn outreach to one ASE Compute engineer in Seattle
- [ ] Tailored resume below ready to upload

---

# TAILORED RESUME

## VISHWESHWAR CHIPPA
**SRE Manager | Compute Platform Reliability | Kubernetes + Cloud + VM at Scale | Seattle Target**

Atlanta, GA → Open to relocate Seattle, WA | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
SRE Manager with 21+ years operating compute infrastructure across the full stack — VMs, containers, Kubernetes, cloud-native — at enterprise scale. At T-Mobile, lead a **15-person SRE team** managing 4 production platforms processing **25M+ messages/day** on Kubernetes (EKS) + AWS infrastructure with **99.99% availability** over 36 consecutive months. Led the entire compute-layer journey: VM → PCF → Kubernetes → AWS, with zero SLA breach across legally-required message types. Seeking SRE Manager role at Apple Services Engineering in Seattle to apply compute-platform reliability leadership at Apple's scale.

---

## CORE COMPETENCIES (ASE Compute alignment)
Compute Substrate Reliability (VM, Container, Kubernetes, Cloud) · 15-Person SRE Team Leadership
Zero-Downtime Compute Migrations · Cluster Lifecycle & Capacity Management
Splunk Observability Authorship · Cross-Org Incident Command · CI/CD + IaC Governance

---

## TECHNICAL SKILLS (mapped to JD)
**Compute / Containers:** Kubernetes (EKS production at 25M-msg-per-day scale), Docker, PCF, VM lineage; HPA + KEDA queue-driven scaling
**Cloud:** AWS (EKS, Lambda, SQS, SNS, S3, DynamoDB, Aurora); Azure
**Observability:** Splunk (deep — built MART framework, MLTK anomaly detection), AppDynamics, Grafana, DORA metrics
**CI/CD + IaC:** GitLab CI/CD (primary), GitHub Actions, environment promotion gates, automated rollback
**Security:** Vault (production), CyberArk, IAM, TKE, Aqua, SonarQube, AppScan
**Languages:** Python (primary automation), Java, Kotlin, JavaScript; SQL/NoSQL
**Data Plane:** MongoDB, Cassandra, Redis, MySQL — distributed at scale

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 platforms · 25M+ msgs/day · **15 direct reports** · Kubernetes + AWS production · 99.99% availability

**Compute Substrate at Scale (ASE Compute alignment)**
- Architected and led **Kubernetes migration** for all 4 platforms over 12 months; maintained 99.99% SLA throughout
- Operated production EKS clusters at 25M-msg-per-day load; HPA for CPU-driven pods, KEDA for queue-depth-driven scaling so capacity tracks actual message load
- Right-sized cluster footprint after profiling actual P95 CPU/memory; recovered ~30% over-provisioning
- Implemented PodDisruptionBudgets and circuit breakers to prevent cascading failures across services

**Compute Migration Lineage**
- Led full compute-substrate journey across the platform: **VM → PCF → Kubernetes → AWS** — zero customer-impacting SLA breach across all transitions
- Built parallel-run / shadow-traffic patterns for every migration: 8-week observation, output-divergence comparison, gradual cutover (10% → 25% → 50% → 100%)

**SRE Manager Operating Model**
- Lead **15-person onshore + offshore SRE team**; structured on-call rotation, escalation paths, incident command for 24/7 coverage
- Maintained **zero customer-impacting Sev1s over 36 months** via disciplined postmortem culture and systemic root-cause elimination
- Authored MART (Monitoring/Alerting/Reporting/Troubleshooting) framework adopted across T-Mobile notification ecosystem; ~40% MTTR reduction
- Defined SLOs for 4 platforms; burn-rate alerting at 5% and 1% budget consumption

**Cross-Org Influence**
- Built 42-system integration-test working group during TIBCO → Spring Boot migration with no formal authority over downstream teams; zero downstream failures at cutover
- Presented platform health, risk assessments, and architectural decisions to senior leadership monthly

**Security & Compliance Operations**
- Deployed Vault for secrets across all 4 platforms; CyberArk PAM for privileged access
- Aqua / SonarQube / AppScan in CI/CD; **zero critical vulnerabilities in production for 18 months**

**AI & Automation**
- Built ML anomaly detection in Python + Splunk MLTK; recovered ~750K message deliveries monthly
- Developed GenAI metrics agent for leadership reporting

### Macy's | Systems Specialist (Loyalty) | Oct 2012 – Dec 2015
60M customers · $5–7M/day · 100+ TPS · multi-DC failover

### Asurion | Sr. System Design Engineer | Feb 2010 – Oct 2012
### Wachovia/Wells Fargo | Operations Lead | Feb 2009 – Feb 2010
### BP Global | Dev/Operations Lead | Jun 2005 – Feb 2009

---

## CERTIFICATIONS & EDUCATION
SAFe 4 PO/PM · SAFe 4 DevOps · SRE Foundation · TIBCO BW5
B.Tech (Metallurgy) — IIT-BHU | 2004

---

# TAILORED 30-SECOND PITCH

> "I'm Vishweshwar Chippa, SRE Principal at T-Mobile. I lead 15 engineers operating 4 production platforms on Kubernetes and AWS at 25 million messages a day with 99.99% availability for 3 years running. I've led the entire compute-substrate journey — VMs to PCF to Kubernetes to AWS — without missing an SLA. The ASE Compute Manager role in Seattle is a clean extension of what I run today, at Apple's scale, in a city I'd be glad to relocate to. Approved I-140, so the H1B transfer is straightforward."

# COVER LETTER OPENER

> Dear Apple Services Engineering Hiring Team,
>
> The ASE Compute Manager role asks for someone who has led compute-platform reliability at scale across VMs, containers, and clusters. That has been my full-time work at T-Mobile for the last decade — leading 15 SRE engineers operating four production platforms on Kubernetes and AWS at 25 million messages daily, with 99.99% availability over 36 consecutive months. I led the entire substrate migration: VM to PCF to Kubernetes to AWS, with zero customer-impacting SLA breach. Seattle is at the top of my relocation list. I have an approved I-140 (June 2016 priority date), making the H1B transfer straightforward.
