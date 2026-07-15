# Role 01 — Sr. Systems Development Manager, AWS Managed Operations (3132584) — TOP ★

> 🎯 **AWS MO charter is your bullseye.** "Reduce operational toil for AWS Region day-to-day operations" = your MART framework + 25M-msg-per-day + 36-month zero-Sev1 record. Verify Seattle/Bellevue option before applying.

## Job metadata
- **JD URL:** https://www.amazon.jobs/en/jobs/3132584/sr-systems-development-manager-aws-managed-operations-mo
- **Requisition ID:** 3132584
- **Team:** AWS Managed Operations (MO) — chartered April 2023
- **Location:** Herndon VA (per snippet) — likely also Seattle. **Verify Seattle availability up front.**
- **Posted base salary:** Not retrieved by automated fetch. M-band Sr SysDev Manager band typically $200K – $268K base + RSU.
- **Level:** M-band (L7-equivalent manager track)
- **Match score:** **92%**
- **Verdict:** **Apply this week** (after Seattle confirmation).

## What matched (Leadership Principle alignment)
- **"Reduce operational load and toil"** → ~25% Python toil reduction at T-Mobile (**Operational Excellence**)
- **"Day-to-day operations for AWS Regions; availability, reliability, latency"** → 99.99% across 4 platforms (**Deliver Results**)
- **"Build & lead a Systems Engineering team"** → 15-direct-reports onshore + offshore (**Hire and Develop**)
- **"Drive measurable Operational Excellence"** → **MART framework** adopted across T-Mobile notification ecosystem
- **Senior management business-acumen** → SAFe 4 PO/PM + DevOps certs + Product Owner depth
- **Strong technical depth on systems + DB** → TIBCO→Spring Boot, Oracle→MySQL→MongoDB migrations (**Ownership**)
- **"Long-term engineering projects to reduce toil"** → 6 zero-downtime migrations
- **Multi-region failover** → Macy's multi-DC failover for 60M customers

## Gaps
1. **No Go language** — AWS internal tooling is Go-heavy
2. **No prior AWS-internal Brazil / Pipelines / CloudFormation tooling experience**
3. **"AWS Region operations" implies physical/network-region scale** beyond app-level ops
4. **Possible Herndon VA-only requirement** (outside Atlanta + Seattle stated preference)

## Gap mitigation
1. Lead Python automation story heavily; position Go as "next language to ramp on, idiomatic in 4 weeks." If you ship a Go binary in the next 60 days, mention it concretely.
2. Cite 6 zero-downtime migrations **including AWS migration of T-Mobile primary notification platform** — proves AWS hands-on. Mention CloudFormation/CDK familiarity (you've worked with comparable patterns).
3. Reframe 25M msgs/day as a "regional control-plane analog" — same fan-out, retry, DLQ, observability primitives that AWS Region operations face. Add Macy's multi-DC failover for 60M customers as additional regional-scale evidence.
4. **First recruiter call: ask whether Seattle/Bellevue is an option for this req.** If Herndon-only and you can't relocate East Coast, redirect to Role 4 (Seattle confirmed).

## Pre-application checklist
- [ ] First recruiter call: confirm Seattle/Bellevue option for this req
- [ ] If Herndon-only: decide whether you can relocate East Coast (or pivot to Role 4)
- [ ] Open https://www.amazon.jobs/en/jobs/3132584/ — verify still active
- [ ] Apply via Amazon careers portal
- [ ] LinkedIn outreach to 2 AWS MO engineers (Seattle and Herndon)
- [ ] Prep Leadership Principle stories: 1 each for Operational Excellence, Ownership, Deliver Results, Hire and Develop, Invent and Simplify (Apple Q&A file 04 has good baseline structure)

---

# TAILORED RESUME (Amazon AWS — full version)

## VISHWESHWAR CHIPPA
**Sr. Systems Development Manager | AWS Operational Excellence | Notification Platform Reliability at 25M msgs/day**

Atlanta, GA → Open to relocate **Seattle, WA** (preferred) or Herndon, VA | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
Sr. Systems Development Manager with 21+ years operating large-scale, business-critical platforms with operational excellence as a first-class engineering discipline. At T-Mobile, lead a **15-person SRE team** managing 4 production notification platforms processing **25M+ messages/day** on **AWS + Kubernetes** infrastructure with **99.99% availability over 36 consecutive months** and **zero customer-impacting Sev1 incidents**. Authored the **MART operational excellence framework** adopted across the notification ecosystem with **~40% MTTR reduction**, led **6 zero-downtime platform migrations** including the full AWS migration of T-Mobile's primary notification platform, and shipped **production ML anomaly detection** plus a **GenAI metrics agent** in operations. Seeking Sr SysDev Manager role with AWS Managed Operations to apply OpEx-driven SRE leadership at AWS Region scale.

---

## CORE COMPETENCIES (AWS MO alignment)
**Operational Excellence at Scale** · 15-Person SRE Team Leadership · AWS-Native Operations
**Toil Reduction (Python automation, ~25% reduction)** · Zero-Downtime Migration Leadership (6 programs)
SLO/SLI/Error-Budget Governance · Splunk Observability Authorship · Multi-DC / Multi-Region Failover

---

## TECHNICAL SKILLS (mapped to Amazon)
**Cloud:** **AWS (EKS, Lambda, SQS, SNS, S3, DynamoDB, Aurora)** in production at 25M-msg-per-day; Azure; multi-cloud reliability patterns
**Compute / Containers:** Kubernetes (EKS production), Docker, PCF, VM lineage; HPA + KEDA queue-driven scaling
**Observability:** **Splunk (deep — built MART framework, MLTK anomaly detection, custom dashboards)**, AppDynamics, Grafana, DORA metrics
**Languages:** Python (primary automation), Java, Kotlin, JavaScript; **Go (currently leveling up — committed to ship one production tool in 60 days)**
**Security:** Vault (production), CyberArk, IAM, Aqua, SonarQube, AppScan
**Data Plane:** MongoDB, Cassandra, Redis, MySQL — distributed at production scale
**CI/CD:** GitLab CI/CD (primary), GitHub Actions; environment promotion gates with security scans

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 platforms · 25M+ msgs/day · **15 direct reports** · 99.99% availability · 36 months zero Sev1s · ~42 integrated systems

**Operational Excellence Leadership (AWS MO alignment)**
- Authored **MART (Monitoring/Alerting/Reporting/Troubleshooting) framework** adopted across T-Mobile notification ecosystem; **~40% MTTR reduction** for recurring incident classes
- Maintained **99.99% availability** and **zero customer-impacting Sev1s over 36 consecutive months** across all 4 platforms
- Defined SLO/SLI/error-budget governance; burn-rate alerting at 5% / 1% consumption
- Conducted 30+ postmortems; eliminated recurring-incident classes through systemic root-cause work — equivalent to AWS COE (Correction of Errors) discipline at smaller scope

**Ownership: 4 Platforms, 15 People, 25M Msgs**
- Lead **15-person onshore + offshore SRE team**; structured on-call rotation, escalation paths, incident command for 24/7 coverage
- Operated 4 production platforms (MoEngage, DND, AJO, MAT) at 25M+ messages/day with no escalation gaps
- Cross-org influence: built integration test working group across 42 connected systems during TIBCO → Spring Boot migration with no formal authority over downstream teams; zero downstream failures at cutover

**Deliver Results: 6 Zero-Downtime Migrations**
- Led **6 zero-downtime migrations** with parallel-run + 8-week shadow-traffic methodology: **TIBCO → Spring Boot, EMS → RabbitMQ, Oracle → MySQL → MongoDB, VM → PCF → Kubernetes → AWS, APIGEE → MEG/TAG, Bitbucket → GitLab** — all with zero customer-impacting SLA breach
- Architected and led **Kubernetes migration** of all 4 platforms over 12 months; zero SLA breach across legally-required message types
- Led **AWS cloud migration architecture** for primary notification platform: EKS, Lambda, SQS/SNS alignment

**Invent and Simplify: AI in Operations**
- Built **production ML anomaly detection** (Python + Splunk MLTK) on the DND domain; **recovered ~750K message deliveries monthly** from false-positive suppressions
- Built **GenAI metrics agent** answering natural-language platform-health queries for leadership; eliminated ~8 hrs/week manual reporting
- Implemented **GitHub Copilot + Claude Code workflows** for SRE team of 15; reduced routine coding toil by ~25%

**Hire and Develop the Best**
- Built and scaled SRE team from 4 to 15 engineers over 6 years
- Authored internal SRE onboarding checklist + playbook; new hires ramp to full productivity in 4 weeks (down from 12)
- Identified one engineer who joined as deployment engineer; gave stretch project; now leads Kubernetes platform independently

**Security & Compliance Operations**
- Deployed Vault for secrets across all 4 platforms with Vault Agent Injector pattern; CyberArk PAM for privileged access
- Embedded Aqua / SonarQube / AppScan as mandatory promotion gates in GitLab CI/CD; **zero critical vulnerabilities in production for 18 consecutive months**

### Macy's | Systems Specialist (Loyalty) | Oct 2012 – Dec 2015
60M customers · $5–7M/day transactions · 100+ TPS · multi-DC failover; high-availability across 12 platform components

### Asurion | Sr. System Design Engineer | Feb 2010 – Oct 2012
Java → TIBCO modernization; 3x throughput; international (EU/AU/JP) packaging

### Wachovia/Wells Fargo | Operations Lead | Feb 2009 – Feb 2010
TIBCO environments during merger pressure; pre-CI/CD deployment automation

### BP Global | Dev/Operations Lead | Jun 2005 – Feb 2009
Real-time trading integrations replacing file-based processing; centralized logging framework

---

## CERTIFICATIONS & EDUCATION
SAFe 4 PO/PM · SAFe 4 DevOps · SRE Foundation · TIBCO BW5
B.Tech (Metallurgy) — IIT-BHU | 2004

---

## KEY METRICS SNAPSHOT
| Metric | Value |
|--------|-------|
| Platform message volume | 25M+ msgs/day |
| Platform availability | 99.99% (3 years) |
| Customer-impacting Sev1s (36 months) | 0 |
| MTTR improvement (MART framework) | ~40% |
| Critical security vulnerabilities (production, 18 months) | 0 |
| Zero-downtime migrations | 6 |
| Team size | 15 (onshore + offshore) |
| Integrated systems | ~42 |
| Toil reduction (Python automation) | ~25% |
| Message deliveries recovered (ML anomaly detection) | ~750K/month |

---

# TAILORED 30-SECOND PITCH

> "I'm Vishweshwar Chippa, SRE Principal at T-Mobile. For the past 10 years I've run 4 production notification platforms processing 25 million messages a day across SMS, email, and push, integrating with 42 systems. I've led 6 major zero-downtime migrations — including a full Kubernetes and AWS migration — while maintaining 99.99% availability. I have 15 engineers reporting to me, I've built AI-driven anomaly detection and a GenAI metrics agent in production, and I've established the MART observability framework that cut MTTR ~40%. I have an approved I-140, so the H1B transfer is straightforward. I'm looking to bring that operational excellence and scale experience to a Sr SysDev Manager role at AWS Managed Operations."

# COVER LETTER OPENER

> Dear Amazon AWS Managed Operations Hiring Team,
>
> The Sr Systems Development Manager role for AWS Managed Operations describes the work I have led at T-Mobile for a decade — driving operational excellence at scale, reducing toil, building reliability frameworks, and leading the engineering team responsible for day-to-day operations of mission-critical platforms. I have run 4 production notification platforms at 25 million messages daily on AWS + Kubernetes, with **99.99% availability and zero customer-impacting Sev1 incidents over 36 consecutive months**. I authored the MART observability framework adopted across the notification ecosystem with ~40% MTTR reduction, deployed production ML anomaly detection in Splunk MLTK, built a GenAI metrics agent live for leadership, and led 6 zero-downtime migrations including the full AWS migration of our primary notification platform. I lead 15 SRE engineers onshore and offshore. The Operational Excellence and Ownership Leadership Principles are not buzzwords for me — they are how I have operated for years. I have an approved I-140 (June 2016 priority date), making the H1B transfer routine. I'd welcome the chance to discuss how my experience translates to AWS Managed Operations.
