# Role 01 — SRE Manager, Storage (Apple Services Engineering)

## Job metadata
- **JD URL:** https://jobs.apple.com/en-us/details/200620738-0836/site-reliability-engineering-manager-storage-apple-services-engineering
- **Requisition ID:** 200620738-0836
- **Team:** Apple Services Engineering (ASE) — Storage SRE
- **Location:** Cupertino, CA
- **Posted base salary:** **$216,600 – $325,500** (verified)
- **Posted:** Apr 24, 2026
- **Match score:** **88%** (highest of the 6 surfaced roles)

## Why this is your top Apple shot
Verified salary floor above the $200K bar, manager band sized to your scope (15 reports today), and the JD asks for SRE-leadership traits you've already demonstrated for 10 years.

## What matched (JD requirement → resume evidence)
- **"Deep knowledge of SRE principles — monitoring, alerting, error budgets, fault analysis"** → built MART (Monitoring/Alerting/Reporting/Troubleshooting) framework adopted across T-Mobile notification ecosystem; 99.99% availability across 4 platforms
- **"Lead teams spread across geographic regions"** → 15 direct reports onshore + offshore; structured on-call rotation, escalation, incident command
- **"Kubernetes, virtualization, containerization"** → led K8s migration of all 4 platforms over 12 months, zero SLA breach
- **"CI/CD pipelines, IaC (Terraform, Ansible)"** → GitLab CI/CD ownership; Bitbucket→GitLab migration; environment promotion gates with security scans
- **"Distributed systems at scale"** → 25M+ msgs/day across MongoDB / Cassandra / Redis distributed data plane
- **"Security best practices, compliance"** → Vault + CyberArk in production; Cybersecurity Syndicate reviews; zero critical vulnerabilities in production for 18 months

## Gaps
1. **Distributed *block* storage specialty** — your reliability domain is messaging/notifications, not block-storage internals
2. **Go preferred** — Python is your primary, no Go on resume
3. **Bare-metal / hardware-adjacent storage stack** — VM and K8s yes; storage hardware tier no

## Gap mitigation
1. Block storage → reframe Oracle→MongoDB and EMS→RabbitMQ migrations as "stateful data-plane reliability under sustained throughput." Optional 30-day Ceph or MinIO lab project documented in a GitHub repo to point to in the loop.
2. Go → ship one production tool in Go (rewrite a Python automation as a Go binary); add to resume in 60 days. In the interim, name-check Go in the cover letter as "the language I'm currently leveling up on."
3. Bare-metal → emphasize VM→PCF→K8s→AWS journey as evidence you've operated every layer; concede storage-hardware honestly and lean on leadership scope.

## Pre-application checklist
- [ ] Open live JD URL above and reconfirm $216,600 floor still posted
- [ ] Note any "Education & Experience" line items you can't speak to
- [ ] Update resume copy to use the tailored version below
- [ ] Apply via Apple careers (not aggregator)
- [ ] LinkedIn outreach to one Apple ASE engineer for referral

---

# TAILORED RESUME

## VISHWESHWAR CHIPPA
**SRE Manager | Distributed Storage & Stateful Systems Reliability | Apple Services Engineering**

Atlanta, GA → Open to relocate Cupertino, CA | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
SRE Manager with 21+ years operating large-scale distributed systems and stateful data planes at enterprise scale. At T-Mobile, lead a **15-person SRE team** managing 4 production notification platforms processing **25M+ messages/day** with **99.99% availability** over 36 months. Deep expertise in distributed-store reliability (MongoDB, Cassandra, Redis at production scale), zero-downtime stateful migrations (Oracle → MongoDB, EMS → RabbitMQ), Kubernetes at scale, and SRE-principle-driven leadership — the same disciplines Apple Services Engineering needs to scale ASE Storage.

---

## CORE COMPETENCIES (Storage SRE alignment)
Distributed Stateful Systems Reliability · Stateful Migration Leadership · SRE Manager (15 reports)
Kubernetes Orchestration at Scale · CI/CD + IaC Governance · Vault/CyberArk Security Operations
Splunk Observability Framework Authorship · ML Anomaly Detection in Production

---

## TECHNICAL SKILLS (mapped to JD)
**Distributed Data Plane:** MongoDB, Cassandra, Redis, MySQL — all in production at 25M-msg-per-day scale; partition heat maps, JVM tuning, repair scheduling
**Containers / Orchestration:** Kubernetes (EKS production), Docker, PCF, VM lineage
**CI/CD + IaC:** GitLab CI/CD (primary), GitHub Actions, infrastructure provisioning automation
**Security & Compliance:** Vault, CyberArk, IAM, TKE, Aqua, SonarQube, AppScan, Cybersecurity Syndicate reviews
**Observability:** Splunk (deep — built MART framework, MLTK anomaly detection, custom dashboards), AppDynamics, Grafana, DORA
**Languages:** Python (primary automation), Java, Kotlin, JavaScript; SQL/NoSQL
**Cloud:** AWS (EKS, Lambda, SQS/SNS, S3); Azure; multi-cloud reliability patterns

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 platforms · 25M+ msgs/day · **15 direct reports** · 99.99% availability · ~42 integrated systems

**Stateful & Distributed Reliability (ASE Storage alignment)**
- Operated **MongoDB, Cassandra, Redis** in production at T-Mobile scale; managed cluster health, partition strategy, JVM/GC tuning, repair scheduling — zero data-tier outages in last 18 months
- Led **Oracle → MySQL → MongoDB** zero-downtime migration with parallel-run pattern; shadow traffic for 8 weeks until output divergence < 0.001%
- Led **EMS → RabbitMQ** stateful messaging migration; managed queue depth, DLQ policies, consumer autoscaling
- Designed query patterns and ML queries for MongoDB to extract platform metrics (daily volumes, week-over-week comparisons) at scale

**SRE Leadership & Operating Model**
- Lead **15-person onshore + offshore SRE team**; established on-call rotation, escalation paths, incident command for 24/7 coverage
- Maintained **99.99% availability** and **zero customer-impacting Sev1s** over 36 consecutive months across 4 platforms
- Built **MART (Monitoring, Alerting, Reporting, Troubleshooting)** framework adopted across T-Mobile notification ecosystem; reduced MTTR by ~40%
- Defined error-budget policy and SLO governance; burn-rate alerting at 5% and 1% budget consumption

**Kubernetes + Cloud Migration**
- Architected and led **Kubernetes migration** for all 4 platforms over 12 months; zero SLA breach across legally-required message types
- Led **AWS migration** of primary notification platform including EKS, Lambda, SQS/SNS alignment

**Security & Compliance**
- Deployed Vault for secrets management across all 4 platforms; CyberArk for privileged access
- Implemented Aqua / SonarQube / AppScan in CI/CD; **zero critical vulnerabilities in production for 18 consecutive months**

**AI & Automation**
- Built ML anomaly detection in Python + Splunk MLTK; recovered ~750K message deliveries monthly from false-positive suppressions
- Developed GenAI metrics agent answering natural-language platform-health queries; eliminated ~8 hours/week manual reporting

### Macy's | Systems Specialist (Loyalty) | Oct 2012 – Dec 2015
60M customers · $5–7M/day transactions · 100+ TPS · multi-DC failover

### Asurion | Sr. System Design Engineer | Feb 2010 – Oct 2012
Java → TIBCO modernization; 3x throughput; international (EU/AU/JP) packaging

### Wachovia/Wells Fargo | Operations Lead | Feb 2009 – Feb 2010
### BP Global | Dev/Operations Lead | Jun 2005 – Feb 2009

---

## CERTIFICATIONS & EDUCATION
SAFe 4 PO/PM · SAFe 4 DevOps · SRE Foundation · TIBCO BW5
B.Tech (Metallurgy) — IIT-BHU, Varanasi | 2004

---

# TAILORED 30-SECOND PITCH

> "I'm Vishweshwar Chippa — SRE Principal at T-Mobile leading a 15-person team running 4 production platforms at 25 million messages a day with 99.99% availability for 3 years. The data tier is MongoDB, Cassandra, Redis at scale, and I've led the stateful migrations — Oracle to MongoDB, EMS to RabbitMQ — without losing a transaction. I've also led the Kubernetes migration of all 4 platforms over a year with zero SLA breach. The ASE Storage Manager role looks like a direct extension of what I do today, with Apple's scale on top. I have an approved I-140 so the H1B transfer is clean."

# COVER LETTER OPENER

> Dear Apple Services Engineering Hiring Team,
>
> The ASE Storage Manager role describes the work I have led at T-Mobile for a decade — distributed stateful systems at scale, zero-downtime migration of the data tier, SRE-principle-driven team leadership across geographies. I lead 15 SRE engineers across four production platforms processing 25 million messages daily, with 99.99% availability for 36 consecutive months and zero data-tier outages in the last 18. The stateful migrations I have led — Oracle to MongoDB, EMS to RabbitMQ, VM to Kubernetes to AWS — are the same class of work ASE Storage runs at Apple scale. I have an approved I-140 (June 2016 priority date), making any H1B transfer routine for your legal team.
