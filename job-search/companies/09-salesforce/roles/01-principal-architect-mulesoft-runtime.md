# Role 01 — Principal Engineer/Architect, MuleSoft Runtime Manager (JR329590) — TOP ★

> 🎯 **95% match — your MuleSoft insider credential is the unfair advantage.** Almost no other SRE candidate has MuleSoft on their resume. Salary band $197K – $401K.

## Job metadata
- **JD URL:** https://careers.salesforce.com/en/jobs/jr329590/principal-engineer-or-architect-mulesoft-runtime-manager/
- **Requisition ID:** JR329590
- **Team:** MuleSoft Anypoint Runtime Manager (ARM) / Universal Management Platform — 40+ microservices, 8+ AWS regions
- **Location:** San Francisco / Bellevue
- **Posted base salary:** $197,300 – $365,200 (CA std band) / $237,700 – $401,400 (SF/NYC tier)
- **Level:** Principal IC (Architect track)
- **Posted:** 2026-03-13
- **Match score:** **95%**
- **Verdict:** **Apply this week. Top pick.**

## What matched
- **MuleSoft on resume** → insider credential. You operate MuleSoft alongside APIGEE in production at T-Mobile
- **K8s + AWS + microservices reliability at 25M msgs/day** → direct match to ARM Control Plane scope
- **6 zero-downtime migrations** → modernization muscle
- **Multi-region availability** → AWS migration of T-Mobile primary notification platform; ~42 integrated systems
- **40+ microservices, 8+ AWS regions, K8s** → your scope of operation today
- **Lead architecture/evolution** → 21 years of architecture decisions including MART framework authorship

## Gaps
1. **Salesforce-internal MuleSoft engineering tooling** — no exposure
2. **Architect-level FedRAMP / Protected B environments** specifically
3. **DataWeave / Mule Runtime internals** — you're an enterprise consumer, not an internals expert

## Gap mitigation
1. Frame your MuleSoft enterprise-customer perspective as the rare credential — internal Salesforce candidates can't bring that voice
2. Cite Vault + CyberArk + Cybersecurity Syndicate reviews as FedRAMP-adjacent compliance discipline
3. Concede internals honestly; commit to deep-dive in onboarding; lean on architecture patterns + reliability primitives that transfer

## Pre-application checklist
- [ ] Open https://careers.salesforce.com/en/jobs/jr329590 — verify still active
- [ ] Apply via Salesforce careers
- [ ] LinkedIn outreach to 2-3 MuleSoft Anypoint engineers (SF + Bellevue)
- [ ] Prep 2-3 specific MuleSoft operational pain stories you've hit at T-Mobile (memory mgmt under high concurrency, object store clustering replication lag, connector retry thundering herd)

---

# TAILORED RESUME (Salesforce — full version)

## VISHWESHWAR CHIPPA
**Principal Engineer / Architect | MuleSoft Production Operator | Customer-Engagement Platform Reliability at 25M msgs/day**

Atlanta, GA → Open to relocate **San Francisco, CA / Bellevue, WA** | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
Principal Engineer / Architect with 21+ years operating large-scale integration and notification platforms at enterprise scale, **with a credential rare among Salesforce architecture candidates: production operation of MuleSoft alongside APIGEE for T-Mobile's notification platform at 25M msgs/day**. Lead a **15-person SRE team** managing 4 production platforms with **99.99% availability over 36 consecutive months** and **zero customer-impacting Sev1 incidents**. Authored the MART observability framework adopted across the notification ecosystem with **~40% MTTR reduction**, led **6 zero-downtime migrations**, and shipped **production ML anomaly detection (Splunk MLTK)** plus a **GenAI metrics agent**. Seeking Principal Architect role with MuleSoft Runtime Manager to apply enterprise-customer perspective directly inside Salesforce's integration platform team.

---

## CORE COMPETENCIES (MuleSoft / Salesforce alignment)
**MuleSoft Production Operations** · APIGEE / L7 Traffic Plane · Integration Platform Reliability
Architect-Track Principal Scope · 25M-Msg-per-Day Multi-Region AWS · 6 Zero-Downtime Migrations
**MART Observability Framework Authorship** · AI-Native SRE Practice · 15-Person SRE Team Leadership

---

## TECHNICAL SKILLS (mapped to Salesforce / MuleSoft)
**Integration Platforms (production):** **MuleSoft (production operator)**, APIGEE, MEG/TAG proxies, Spring Boot, RabbitMQ, TIBCO EMS (legacy)
**Cloud / Compute:** **AWS multi-region (EKS, Lambda, SQS, SNS, S3)**; Kubernetes (production at 25M-msg-per-day); Docker; PCF
**Observability:** **Splunk (deep — built MART framework, MLTK anomaly detection, custom dashboards)**, AppDynamics, Grafana, DORA metrics
**AI / ML:** Production ML anomaly detection (Splunk MLTK); production GenAI metrics agent; GitHub Copilot + Claude Code workflows
**Languages:** Python (primary automation), Java, Kotlin, JavaScript; SQL/NoSQL
**Data Plane:** MongoDB, Cassandra, Redis, MySQL, Oracle — distributed at production scale
**Security:** Vault, CyberArk, IAM, Aqua, SonarQube, AppScan; Cybersecurity Syndicate review cadence
**CI/CD:** GitLab CI/CD (primary), GitHub Actions

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 platforms · 25M+ msgs/day · **15 direct reports** · multi-region AWS · 99.99% availability · 36 months zero Sev1s

**MuleSoft Production Operations (Salesforce alignment)**
- Operate **MuleSoft** in production at T-Mobile alongside APIGEE for the notification platform integration layer; my team uses MuleSoft daily to orchestrate integrations across 4 notification platforms and ~42 downstream systems
- Operational pain patterns I have hit and fixed at scale: **Mule runtime memory management under high concurrency** (DataWeave-heavy flows + JVM GC alerts in Splunk), **object store clustering replication lag** during failover (mitigated with external Redis-backed state), **connector retry thundering herd** on downstream APIs (custom backoff policies)
- Led **APIGEE → MEG/TAG proxies migration** — rebuilt 12+ API contracts; managed L7 traffic-plane transition without customer-facing degradation

**Integration Platform Reliability at Scale**
- Lead **15-person onshore + offshore SRE team** managing 4 production platforms processing 25M+ messages/day across **multi-region AWS** infrastructure
- Maintained **99.99% availability** and **zero customer-impacting Sev1s over 36 consecutive months**
- Authored **MART (Monitoring/Alerting/Reporting/Troubleshooting) framework** adopted across T-Mobile notification ecosystem; ~40% MTTR reduction
- Defined SLO/SLI/error-budget governance for 4 platforms; burn-rate alerting at 5% / 1% consumption

**6 Zero-Downtime Migrations (Architect-Grade Modernization)**
- Led 6 zero-downtime migrations with parallel-run + 8-week shadow-traffic methodology: TIBCO → Spring Boot, EMS → RabbitMQ, Oracle → MongoDB, VM → PCF → Kubernetes → AWS, **APIGEE → MEG/TAG (L7 traffic plane)**, Bitbucket → GitLab — all with zero customer-impacting SLA breach
- Architected and led Kubernetes migration of all 4 platforms over 12 months; zero SLA breach across legally-required message types

**AI-Native SRE Practice (production)**
- Built **production ML anomaly detection** (Python + Splunk MLTK); recovered ~750K message deliveries monthly
- Built **production GenAI metrics agent** answering natural-language platform-health queries; eliminated ~8 hrs/week leadership reporting
- Implemented **GitHub Copilot + Claude Code workflows** for SRE team of 15; reduced routine coding toil ~25%

**Security & Compliance Operations**
- Deployed Vault for secrets across all 4 platforms; CyberArk PAM for privileged access
- Embedded Aqua / SonarQube / AppScan in GitLab CI/CD; **zero critical vulnerabilities in production for 18 consecutive months**
- Cybersecurity Syndicate review cadence — corporate-grade security posture (FedRAMP-adjacent discipline)

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

> "I'm Vishweshwar Chippa, SRE Principal at T-Mobile. I run MuleSoft in production alongside APIGEE for our notification platform — I'm a Salesforce enterprise customer of MuleSoft, and I'm the candidate who has lived its operational pain points at scale. I've hit and fixed Mule runtime memory issues under concurrency, object store clustering replication lag, and connector retry thundering herd patterns. I lead 15 SRE engineers, run 4 platforms at 25 million messages a day on multi-region AWS with 99.99% availability for 3 years, and I've shipped 6 zero-downtime migrations including the L7 traffic-plane modernization. The Principal Architect MuleSoft Runtime Manager role is the chance to bring the enterprise-customer voice directly inside Salesforce's integration platform team. Approved I-140."

# COVER LETTER OPENER

> Dear Salesforce MuleSoft Hiring Team,
>
> The Principal Engineer/Architect role for MuleSoft Runtime Manager describes the platform I have been operating as an enterprise customer for years. At T-Mobile I run MuleSoft alongside APIGEE for our notification platform integration layer — orchestrating integrations across 4 production platforms and ~42 downstream systems at 25 million messages daily on multi-region AWS. I have lived MuleSoft's operational pain points at scale: Mule runtime memory under DataWeave-heavy concurrency, object store clustering replication lag during failover, connector retry thundering herd on downstream APIs — and I have shipped fixes for each. I led 15 SRE engineers, maintain 99.99% availability for 36 consecutive months, and shipped 6 zero-downtime platform migrations including the APIGEE-to-MEG/TAG L7 traffic-plane transition. I authored the MART observability framework adopted across our notification ecosystem with ~40% MTTR reduction. I have an approved I-140 (June 2016 priority date), making the H1B transfer routine. I would welcome the chance to bring the MuleSoft enterprise-customer perspective directly inside the Anypoint Platform engineering team.
