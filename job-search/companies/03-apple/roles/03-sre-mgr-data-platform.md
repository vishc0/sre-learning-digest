# Role 03 — SRE Manager, Apple Data Platform

## Job metadata
- **JD URL:** https://jobs.apple.com/en-us/details/200646432-0321/site-reliability-engineering-manager-apple-data-platform
- **Requisition ID:** 200646432-0321
- **Team:** Apple Data Platform — foundational data plane for Apple Services + AI/ML (lakehouse, embeddings, feature stores, inference-as-a-service)
- **Location:** Cupertino, CA (Seattle hub also referenced for Data Platform; verify on JD)
- **Posted base salary:** Not retrieved by automated fetch. Comparable Senior Manager Data SRE band runs **$183,400 – $316,900** (req 200493584). Mid-point ~$250K is well above $200K, but the **low end is borderline** — confirm the posted range on the live JD before applying.
- **Match score:** **85%**

## Why this role
Your AI-native SRE work — production ML anomaly detection in Splunk MLTK + GenAI metrics agent — is rare in the Apple SRE candidate pool. Data Platform powers Apple's AI/ML inference infrastructure, which is exactly where AI-SRE practice is most valuable.

## What matched
- **"Batch and real-time data processing, lakehouse, feature stores"** → built ML queries on MongoDB for daily / week-over-week metrics; designed real-time observability over event-driven data plane
- **"Data governance, compliance, scalable data management"** → SAFe governance, audit-readiness playbooks, vulnerability remediation, compliance audit trails
- **"SRE leadership of platform"** → 15 reports, MART framework adopted org-wide, 99.99% availability across 4 platforms
- **"AI/ML ecosystem reliability"** → production ML anomaly detection in Splunk MLTK; GenAI metrics agent answering natural-language platform queries

## Gaps
1. **No Hadoop / Spark / Flink / Iceberg in resume** — Apple Data Platform stack is heavily streaming-data-frameworks
2. **No production lakehouse (Databricks, Snowflake, Delta) experience**
3. **Inference-as-a-service / model-serving SRE not represented**

## Gap mitigation
1. Hadoop/Spark → reframe MongoDB pipelines as "batch + streaming over distributed store"; complete Databricks Spark fundamentals badge in 30 days; cite MART framework as transferable
2. Lakehouse → cover-letter angle: "I want to scale your lakehouse SRE, bringing my proven anomaly-detection-in-production playbook to your data plane"
3. Inference → mention GenAI metrics agent as evidence of model-in-production operability; describe the human-validation layer you built around the ML model

## Pre-application checklist
- [ ] Open live JD and confirm posted base range (must be ≥$200K floor for this to be worth pursuing)
- [ ] Confirm Cupertino vs. Seattle (both possible per JD pattern)
- [ ] Take Databricks Spark fundamentals badge (30-day prep) before submitting
- [ ] Write a 1-paragraph note in cover letter about your AI-SRE production playbook

---

# TAILORED RESUME

## VISHWESHWAR CHIPPA
**SRE Manager | Data Platform Reliability | AI-Native SRE Practice | Production ML Anomaly Detection**

Atlanta, GA → Open to relocate Cupertino, CA / Seattle, WA | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
SRE Manager with 21+ years operating large-scale data and notification platforms with an AI-native operations practice. At T-Mobile, lead a **15-person SRE team** managing 4 production platforms processing **25M+ messages/day** with **99.99% availability**. Built **production ML anomaly detection** (Python + Splunk MLTK) recovering ~750K message deliveries monthly, and a **GenAI leadership metrics agent** answering natural-language platform-health queries. Seeking SRE Manager role at Apple Data Platform to apply AI-augmented reliability engineering to the data plane that powers Apple Services and AI/ML.

---

## CORE COMPETENCIES (Data Platform alignment)
AI-Native SRE Practice (ML in production) · Distributed Data-Plane Reliability · 15-Person SRE Leadership
Observability Framework Authorship (MART) · Stateful Migration Leadership · SLO/SLI Governance at Scale
Compliance & Audit-Trail Design · Cross-Org Influence

---

## TECHNICAL SKILLS (mapped to JD)
**Data Plane:** MongoDB, Cassandra, Redis, MySQL — distributed at production scale; ML queries on MongoDB; partition heat maps, JVM tuning
**AI / ML:** **Splunk MLTK anomaly detection in production**; **GenAI metrics agent in production**; GitHub Copilot + Claude Code workflows for team of 15
**Streaming / Event-Driven:** RabbitMQ, Spring Boot, TIBCO EMS (legacy); HPA + KEDA queue-driven scaling on K8s
**Cloud:** AWS (EKS, Lambda, SQS, SNS, S3); Azure
**Observability:** **Splunk (deep — built MART framework, MLTK integration, custom dashboards)**, AppDynamics, Grafana, DORA
**Languages:** **Python (primary — built ML models, AI agents, automation)**, Java, Kotlin, JavaScript
**CI/CD + IaC:** GitLab (primary), GitHub Actions
**Security & Compliance:** Vault, CyberArk, IAM, TKE, AppScan, SAFe governance, audit-trail design

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 platforms · 25M+ msgs/day · **15 direct reports** · production ML in observability stack

**AI-Native SRE Practice (Data Platform alignment)**
- Built and deployed **ML anomaly detection model** in Python + Splunk MLTK for the DND (Do Not Disturb) compliance domain; flags abnormal message-suppression patterns; **recovered ~750K message deliveries monthly** from false-positive suppressions
- Built **GenAI leadership metrics agent** answering natural-language queries about 4-platform health in real time; eliminated ~8 hours/week of manual reporting; runs in production with human-validation layer (the agent surfaces, humans decide)
- Implemented GitHub Copilot + Claude Code workflows for SRE team of 15; reduced routine coding toil by ~25%
- Use ML queries on MongoDB to extract intelligent platform metrics (volume comparisons, week-over-week trend analysis)

**Data-Plane Reliability**
- Operated MongoDB, Cassandra, Redis in production at 25M-msg-per-day scale; managed cluster health, query patterns, JVM tuning
- Led **Oracle → MySQL → MongoDB** zero-downtime migration with parallel-run pattern (8 weeks of shadow-traffic comparison before cutover)
- Led **EMS → RabbitMQ** stateful messaging migration; managed queue depth, DLQ policies, consumer autoscaling

**SRE Leadership & Operating Model**
- Lead **15-person onshore + offshore SRE team**; structured on-call rotation, escalation paths, incident command for 24/7 coverage
- Maintained **99.99% availability** and **zero customer-impacting Sev1s** over 36 consecutive months
- Authored **MART (Monitoring/Alerting/Reporting/Troubleshooting)** framework adopted across T-Mobile notification ecosystem; ~40% MTTR reduction
- Defined SLO governance for 4 platforms; burn-rate alerting at 5% / 1% budget consumption

**Compliance & Audit Trails**
- Built immutable audit trails for legally-mandated message delivery; zero compliance violations in 10 years
- Designed log classification tiers — Tier 1 (technical metrics), Tier 2 (business events), Tier 3 (customer data — never logged) — applicable directly to Apple privacy posture

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

> "I'm Vishweshwar Chippa. I lead a 15-person SRE team at T-Mobile and I've put AI into production in the operations layer — an ML anomaly detection model in Splunk MLTK that recovers about 750,000 message deliveries a month, and a GenAI agent that answers natural-language questions about platform health for leadership. The data plane I run — MongoDB, Cassandra, Redis at 25 million messages a day with 99.99% availability — is the same primitives Apple Data Platform relies on. The Apple Data Platform SRE Manager role is where my AI-SRE practice and my data-plane reliability work converge. I have an approved I-140."

# COVER LETTER OPENER

> Dear Apple Data Platform Hiring Team,
>
> The Data Platform SRE Manager role asks for someone who can scale reliability across the foundational data plane that powers Apple Services and AI/ML — including inference-as-a-service. I have done this work at T-Mobile for a decade, and crucially I have done it with AI-native SRE practice that is still uncommon in the field: a production ML anomaly detection model in Splunk MLTK that recovers ~750,000 message deliveries monthly, and a GenAI metrics agent answering natural-language platform-health queries with a human-validation layer. I lead 15 engineers, run four platforms at 25 million messages daily with 99.99% availability for 36 consecutive months, and have led the stateful migrations (Oracle → MongoDB, EMS → RabbitMQ) that prove I can move the data tier without losing a transaction. I have an approved I-140.
