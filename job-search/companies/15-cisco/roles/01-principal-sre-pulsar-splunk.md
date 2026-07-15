# Role 01 — Principal SRE — Apache Pulsar (Splunk) — TOP ★

> 🎯 **Two insider angles converge.** Splunk-owned BU + messaging SRE charter. You migrated TIBCO EMS → RabbitMQ at 25M msgs/day; Pulsar is the natural next-gen analog. Verified comp $200K – $250K base.

## Job metadata
- **JD URL:** https://www.splunk.com/en_us/careers/jobs/principal-site-reliability-engineer-31650.html
- **Team:** Splunk Data Stream Processor (DSP) — Apache Pulsar messaging group
- **Location:** San Jose, CA
- **Posted base salary:** ~$200K – $250K (matches floor)
- **Level:** Principal IC
- **Match score:** **10/10**
- **Verdict:** **Apply this week. Top pick.**

## What matched
- **Splunk-owned BU** → Cisco acquired Splunk in 2024; your **production Splunk MART framework + MLTK anomaly detection = direct product credential**
- **Apache Pulsar messaging SRE** → your TIBCO EMS → RabbitMQ migration is the closest analog; Pulsar is the next-gen evolution of the same primitives
- **Multi-cloud (AWS/GCP/Azure)** → AWS production at 25M msgs/day; Azure listed; multi-cloud reliability patterns
- **Messaging at scale** → 25M msgs/day is direct messaging-platform credential
- **Principal IC track** → 21 yrs, 10 yrs T-Mobile Principal SRE
- **JMS/SOA / event-driven systems** → Spring Boot, RabbitMQ, TIBCO EMS in production

## Gaps
1. **Pulsar specifics** (consumer groups, partitions, replay semantics) — RabbitMQ transfers conceptually but not 1:1
2. **Splunk-internal engineering tooling** — you're a customer, not internal dev
3. **DSP-specific stream-processing depth** — adjacent to your messaging work but distinct

## Gap mitigation
1. Pulsar specifics → "RabbitMQ → Pulsar mental model conversion is straightforward; consumer groups, partitions, replay — same primitives, different runtime. Two-week ramp."
2. Internal tooling → cite track record of fast onboarding to internal toolchains
3. DSP → frame as "messaging substrate that I have already operated in production, with stream-processing patterns I will absorb in onboarding"

## Pre-application checklist
- [ ] Open https://www.splunk.com/en_us/careers/jobs/principal-site-reliability-engineer-31650.html — verify still active
- [ ] Apply via Splunk careers (or Cisco careers under Splunk BU)
- [ ] LinkedIn outreach to Splunk DSP / Pulsar engineers
- [ ] Read 2 articles on Pulsar architecture before recruiter screen
- [ ] Lead with "I migrated TIBCO EMS → RabbitMQ at 25M msgs/day; Pulsar is the natural next step"

---

# TAILORED RESUME (Cisco/Splunk — full version)

## VISHWESHWAR CHIPPA
**Principal SRE | Splunk Production Operator | Messaging Platform Reliability at 25M msgs/day**

Atlanta, GA → Open to relocate **San Jose, CA** | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
Principal SRE with 21+ years operating large-scale messaging and notification platforms at enterprise scale, **with deep Splunk production credentials at a Cisco-acquired product**. At T-Mobile, lead a **15-person SRE team** managing 4 production messaging platforms processing **25M+ messages/day** with **99.99% availability over 36 consecutive months**. **Authored the MART (Monitoring/Alerting/Reporting/Troubleshooting) framework in Splunk** adopted across the notification ecosystem with **~40% MTTR reduction**, deployed **production ML anomaly detection (Splunk MLTK)** that recovers ~750K message deliveries monthly, and built a **production GenAI metrics agent** with Splunk telemetry backend. **Led TIBCO EMS → RabbitMQ zero-downtime migration** — direct analog to Pulsar messaging primitives.

---

## CORE COMPETENCIES (Cisco/Splunk Pulsar alignment)
**Splunk Production Operator** (built MART framework, MLTK anomaly detection, custom dashboards) · **Messaging Platform Reliability at 25M msgs/day**
TIBCO EMS → RabbitMQ Migration Leadership · Multi-Cloud Kubernetes (AWS production) · 15-Person SRE Team Leadership
6 Zero-Downtime Migrations · AI-Native SRE Practice (Production ML + GenAI)

---

## TECHNICAL SKILLS (mapped to Splunk DSP / Pulsar)
**Messaging (Pulsar Analog):** **RabbitMQ (production primary; migrated from TIBCO EMS)**, Spring Boot, JMS, SOA patterns; consumer groups + partitions + replay semantics (transferable to Pulsar)
**Splunk (Cisco-owned product):** **MART framework authorship**, **MLTK production ML anomaly detection**, custom dashboards, SLO burn-rate calculations, GenAI metrics agent on Splunk backend
**Cloud / Compute:** **AWS multi-region (EKS, Lambda, SQS, SNS, S3)** in production at 25M-msg-per-day; Azure; **multi-cloud reliability patterns**; Kubernetes; Docker
**Languages:** Python (primary automation), Java, Kotlin, JavaScript; SQL/NoSQL
**Observability:** Splunk (deep), AppDynamics, Grafana, DORA metrics
**AI / ML:** Production ML anomaly detection (Splunk MLTK); production GenAI metrics agent; GitHub Copilot + Claude Code workflows
**Security:** Vault, CyberArk, IAM, Aqua, SonarQube, AppScan
**CI/CD:** GitLab CI/CD (primary), GitHub Actions

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 messaging platforms · 25M+ msgs/day · **15 direct reports** · 99.99% availability · 36 months zero Sev1s

**Splunk Production Operator (Cisco/Splunk Direct Match)**
- **Authored MART (Monitoring/Alerting/Reporting/Troubleshooting) framework** in Splunk; adopted across T-Mobile notification ecosystem covering 4 platforms + ~42 integrated systems; **~40% MTTR reduction** for recurring incident classes
- Built **production ML anomaly detection** in Splunk MLTK on the DND domain; **recovered ~750K message deliveries monthly** from false-positive suppressions
- Built **production GenAI metrics agent** answering natural-language platform-health queries on Splunk telemetry backend; eliminated ~8 hrs/week leadership reporting
- 15+ real-time Splunk dashboards tracking SLOs, message volumes, anomaly alerts, platform health for executive visibility
- Splunk SLO burn-rate calculations + custom alerting at 5% / 1% budget consumption

**Messaging Platform Reliability (Pulsar Direct Analog)**
- Operate 4 production messaging platforms — Adobe AJO (notification orchestration), MoEngage (engagement), DND (suppression service), MAT (delivery) — across SMS, email, push channels at **25M+ messages/day**
- **Led TIBCO EMS → RabbitMQ zero-downtime migration** — same primitives Pulsar uses (consumer groups, partitions, replay, DLQ); managed queue depth, autoscaling, replay semantics
- Designed fan-out architecture: API gateway → SQS fanout queues per channel → EKS-hosted Spring Boot microservices per channel
- Authored circuit-breaker and DLQ-depth alerting; eliminated cascading-failure incidents

**Multi-Cloud Operations**
- AWS production at 25M-msg-per-day on EKS + Lambda + SQS/SNS
- Multi-cloud reliability patterns (AWS + Azure + on-prem)
- Led full **AWS migration** of T-Mobile primary notification platform

**Principal IC + Team Leadership**
- Lead **15-person onshore + offshore SRE team**; structured on-call rotation, escalation paths, incident command for 24/7 coverage
- Maintained **99.99% availability** and **zero customer-impacting Sev1s over 36 consecutive months**
- Led **6 zero-downtime migrations** with parallel-run + 8-week shadow-traffic methodology

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

> "I'm Vishweshwar Chippa, SRE Principal at T-Mobile. Two angles converge for this role: I run Splunk in production at 25 million messages a day — your acquired product is my daily tool, and I authored our MART framework + MLTK anomaly detection on top of it. And I migrated TIBCO EMS → RabbitMQ zero-downtime at 25M msgs/day, which is the closest analog to Pulsar messaging primitives. The Principal SRE Pulsar role at Splunk DSP is direct match. Approved I-140."

# COVER LETTER OPENER

> Dear Splunk DSP / Cisco Hiring Team,
>
> The Principal SRE for Apache Pulsar role describes work I have shipped at scale on adjacent technologies — and at the same observability product Cisco acquired in 2024. I run Splunk in production at T-Mobile across 4 messaging platforms at 25 million messages daily; I authored the MART (Monitoring/Alerting/Reporting/Troubleshooting) framework on Splunk that became our ecosystem-wide observability platform with ~40% MTTR reduction; I deployed production ML anomaly detection in Splunk MLTK that recovers ~750,000 message deliveries monthly; and I built a GenAI metrics agent on top of Splunk telemetry. On the messaging side, I led the TIBCO EMS → RabbitMQ zero-downtime migration at T-Mobile — same primitives Pulsar uses (consumer groups, partitions, replay, DLQ semantics). The role is the convergence of two insider angles I bring genuinely: Splunk customer at production scale + messaging SRE leadership at carrier scale. I have an approved I-140 (June 2016 priority date).
