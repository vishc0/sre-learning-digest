# Role 01 — Sr Manager DevOps People Leader, Cloud Operations Resilience Engineering (CORE) — TOP PICK

> 🎯 **Apply this week.** CORE team's charter ("resilience, availability, observability of foundational cloud infrastructure") is the same charter you've run at T-Mobile for a decade. Plano TX is posted. $204.9K+ floor verified.

## Job metadata
- **JD URL:** https://www.capitalonecareers.com/job/mclean/senior-manager-software-engineering-devops-people-leader/1732/89087260720
- **Requisition ID:** R1732 / 89087260720
- **Team:** Cloud Operations Resilience Engineering (CORE)
- **Locations posted:** McLean VA / **Plano TX** / Richmond VA
- **Posted base salary:** McLean $225.4K – $257.2K | **Plano $204.9K – $233.8K** | Richmond $204.9K – $233.8K
  - Plus LTI + bonus (Capital One total comp typically adds ~30–50% on top of base)
- **Level:** Senior Manager (M-track, people leader)
- **Match score:** **92%**
- **Verdict:** **Natural fit. Top pick.**

## What matched
- **15 direct reports running 4 production platforms** → exact people-leader scope CORE expects
- **99.99% availability over 36 months** → CORE mission of resilience and availability
- **AWS-native (EKS, Lambda, SQS, SNS) at 25M msgs/day** → Capital One is AWS-only; exact infrastructure match
- **Vault + CyberArk in production** → security-first DevOps muscle (Capital One's documented stack)
- **Splunk MART framework + ~40% MTTR cut** → observability deliverable
- **Python toil-reduction tooling + ML anomaly detection** → automation-first SRE expectation
- **Compliance audit trails + zero violations 10 years** → maps to PCI-DSS / SOX rigor

## Gaps
1. **Banking / PCI-DSS regulatory experience vs. telecom DND** — different specific regulations, same operational discipline
2. **No prior Capital One internal tooling exposure** — every internal-cloud team has bespoke tooling
3. **Resume light on Terraform / CDK depth** — Capital One is heavy on both

## Gap mitigation
1. Frame DND / legally-mandated message compliance and immutable audit trails as analogous to PCI/SOX controls. Concrete: "I run zero-violation compliance for 10 years across legally-mandated message classes; the discipline transfers directly to PCI-DSS and SOX requirements."
2. Internal tooling → cite track record of fast onboarding to internal toolchains across 6 zero-downtime migrations (TIBCO → Spring Boot, Bitbucket → GitLab, AWS migration); offer 30-day deep-dive commitment.
3. Terraform / CDK → in interview, narrate one Terraform module you own; reference your GitLab CI promotion-gate work as the IaC analog. If you've shipped IaC at T-Mobile (you have, given AWS migration), say so concretely.

## Pre-application checklist
- [ ] Open live JD on https://www.capitalonecareers.com/ and confirm Plano is still posted with $204.9K+ floor
- [ ] Submit application through Capital One careers portal (NOT aggregator)
- [ ] LinkedIn outreach to 1-2 Capital One CORE engineers in Plano
- [ ] If you know anyone who's left T-Mobile for Capital One, leverage that warm path
- [ ] Have your H1B / I-140 script ready (Capital One sponsors at 321+/year, this is routine for them)

---

# TAILORED RESUME (Capital One — full version, used by all CORE roles below with bullet swaps)

## VISHWESHWAR CHIPPA
**Senior Manager DevOps | Cloud Operations Resilience Engineering | AWS + Vault + CyberArk + GitLab in Production | 15-Person SRE Team Leadership**

Atlanta, GA → Open to relocate **Plano TX** | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
Senior Manager DevOps with 21+ years operating cloud-native, security-first platforms at enterprise scale. At T-Mobile, lead a **15-person onshore + offshore SRE team** managing 4 production platforms processing **25M+ messages/day** on **AWS + Kubernetes** infrastructure with **99.99% availability**, **zero customer-impacting Sev1 incidents over 36 consecutive months**, and **zero critical vulnerabilities in production for 18 consecutive months**. Stack mirrors Capital One's DNA: **Vault, CyberArk, GitLab CI/CD, AWS (EKS, Lambda, SQS, SNS), Python, MongoDB, Cassandra, Splunk**. Authored the MART observability framework adopted across the notification ecosystem; led 6 zero-downtime migrations including the full AWS migration of T-Mobile's primary notification platform.

---

## CORE COMPETENCIES (Capital One CORE alignment)
**Cloud Operations Resilience Engineering** · 15-Person SRE People Leadership · AWS-Native Operations
**Vault + CyberArk Production Operations** · GitLab CI/CD Governance · MART Observability Framework Authorship
Compliance-Aware Delivery (FCC + DND audit trails — PCI/SOX-transferable) · Zero-Downtime Migration Leadership

---

## TECHNICAL SKILLS (mapped to Capital One stack)
**Cloud (Capital One stack):** **AWS** (EKS, Lambda, SQS, SNS, S3, DynamoDB, Aurora); Kubernetes; Docker
**Security (Capital One stack):** **Vault (production deployment across 4 platforms)**, **CyberArk PAM**, IAM, TKE, Aqua, SonarQube, AppScan
**CI/CD (Capital One stack):** **GitLab CI/CD (primary)**, GitHub Actions; environment promotion gates; automated rollback
**Observability:** **Splunk** (deep — MART framework author, MLTK ML anomaly detection, custom dashboards), AppDynamics, Grafana, DORA
**Languages:** **Python (primary automation)**, Java, Kotlin, JavaScript; SQL/NoSQL
**Data Plane:** MongoDB, Cassandra, Redis, MySQL — distributed at production scale
**AI / ML:** Production ML anomaly detection (Splunk MLTK); GenAI metrics agent; GitHub Copilot + Claude Code workflows
**Compliance:** SAFe governance; immutable audit-trail design; zero-violation track record (transferable to PCI-DSS, SOX)

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 platforms · 25M+ msgs/day · **15 direct reports** · AWS + K8s + Vault + GitLab + Python · 99.99% availability · 36 months zero Sev1s

**Cloud Operations Resilience (CORE alignment)**
- Lead **15-person onshore + offshore SRE team** managing 4 production platforms; structured on-call rotation, escalation paths, incident command for 24/7 coverage
- Maintained **99.99% availability** and **zero customer-impacting Sev1s over 36 consecutive months**; near-zero MTTR-degrading incidents
- Authored **MART (Monitoring/Alerting/Reporting/Troubleshooting)** framework in Splunk — the resilience/observability discipline CORE hires for; **~40% MTTR reduction** for recurring incident classes
- Defined SLO / SLI / error-budget governance for 4 platforms; burn-rate alerting at 5% / 1% consumption

**AWS-Native Operations (Capital One stack alignment)**
- Operate 4 production platforms on **Kubernetes (EKS) + AWS** infrastructure; led the AWS migration of primary notification platform including EKS, Lambda, SNS/SQS alignment
- Right-sized cluster footprint; recovered ~30% over-provisioning via P95-driven request/limit tuning
- HPA + KEDA queue-driven scaling so capacity tracks actual message load; PodDisruptionBudgets and circuit breakers preventing cascading failures

**Security & Compliance Operations (Vault + CyberArk + GitLab — exact Capital One stack)**
- Deployed **Vault** for secrets management across all 4 platforms; **Vault Agent Injector** pattern (secrets injected as files into pods, never as environment variables); dynamic secrets for database credentials with automated rotation
- Implemented **CyberArk PAM** for privileged access control across SRE team and platform infrastructure
- Embedded **Aqua, SonarQube, AppScan** as mandatory promotion gates in **GitLab CI/CD**; **zero critical vulnerabilities in production for 18 consecutive months**
- Led **Cybersecurity Syndicate reviews** for all 4 platforms; quarterly cadence; closed all findings within remediation SLAs
- Compliance audit-trail design: zero-violation track record over 10 years on legally-mandated message governance — PCI-DSS / SOX-transferable discipline

**Python Automation & Toil Reduction**
- Built Python-based monitoring, triage, transition-tracking tools deployed across 4 platforms; **reduced manual toil by ~25%**
- Built **production ML anomaly detection** (Python + Splunk MLTK) for DND domain; **recovered ~750K message deliveries monthly** from false-positive suppressions
- Built **GenAI metrics agent** answering natural-language platform-health queries; eliminated ~8 hours/week manual reporting

**Migration & Platform Engineering**
- Led **6 zero-downtime migrations** with parallel-run + 8-week shadow-traffic methodology: TIBCO → Spring Boot, EMS → RabbitMQ, Oracle → MySQL → MongoDB, VM → PCF → Kubernetes → AWS, APIGEE → MEG/TAG, Bitbucket → GitLab — **all without customer-impacting SLA breach**
- Architected and led Kubernetes migration of all 4 platforms over 12 months; zero SLA breach across legally-required message types

### Macy's | Systems Specialist (Loyalty) | Oct 2012 – Dec 2015
60M customers · $5–7M/day · 100+ TPS · multi-DC failover · Redis/Cassandra at scale

### Asurion | Sr. System Design Engineer | Feb 2010 – Oct 2012
Java → TIBCO modernization; 3x throughput; international (EU/AU/JP) packaging

### Wachovia/Wells Fargo | Operations Lead | Feb 2009 – Feb 2010
Banking platform experience — TIBCO environments during merger pressure

### BP Global | Dev/Operations Lead | Jun 2005 – Feb 2009

---

## CERTIFICATIONS & EDUCATION
SAFe 4 PO/PM · SAFe 4 DevOps · SRE Foundation · TIBCO BW5
B.Tech (Metallurgy) — IIT-BHU, Varanasi | 2004

---

# TAILORED 30-SECOND PITCH

> "I'm Vishweshwar Chippa, SRE Principal at T-Mobile. I lead 15 engineers running 4 production platforms on AWS + Kubernetes at 25 million messages a day with 99.99% availability for 3 years and zero critical vulnerabilities in production for 18 months. The Capital One stack — Vault, CyberArk, GitLab CI/CD, AWS, Python — is my production stack today. The CORE team's charter for resilience, availability, and observability is exactly what I've run for a decade. Plano is my preferred relocation. Approved I-140."

# COVER LETTER OPENER

> Dear Capital One CORE Hiring Team,
>
> The Sr Manager DevOps People Leader role for Cloud Operations Resilience Engineering describes the work I have led at T-Mobile for the past decade — leading 15 SRE engineers operating 4 production platforms on AWS + Kubernetes at 25 million messages daily, with 99.99% availability and zero customer-impacting Sev1 incidents over 36 consecutive months. The Capital One stack — Vault deployed across all my platforms with the Vault Agent Injector pattern, CyberArk PAM in production, GitLab CI/CD with mandatory Aqua / SonarQube / AppScan gates, Python as primary automation language — is my production stack today. I authored the MART observability framework adopted across T-Mobile's notification ecosystem with ~40% MTTR reduction, and I led the full AWS migration of our primary notification platform. Plano is my preferred relocation. I have an approved I-140 (June 2016 priority date), making the H1B transfer routine.
