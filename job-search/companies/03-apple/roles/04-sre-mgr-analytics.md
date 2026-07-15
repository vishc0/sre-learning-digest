# Role 04 — SRE Manager, Analytics (Apple Services Engineering)

> ⚠️ **POSTING STATUS UNCERTAIN.** Direct fetch returned 404 on 2026-05-07 — this requisition may have been pulled within the last 24–48 hours. **Confirm with a recruiter or via the live Apple careers search before tailoring an application.** Tailored materials below assume the JD as indexed; revise once you confirm the live posting.

## Job metadata
- **JD URL (last known):** https://jobs.apple.com/en-us/details/200592602/site-reliability-engineering-manager-sre-analytics
- **Requisition ID:** 200592602
- **Team:** Apple Services Engineering — Analytics (Apple Music, TV+, App Store data)
- **Location:** Cupertino, CA (per indexed listing)
- **Posted base salary:** Not retrieved. Apple analytics-SRE manager band ≈ **$200K – $315K** based on peer reqs. Confirm on live JD.
- **Match score:** **84%**

## Why this role
Observability + analytics-platform reliability is a direct extension of your MART framework work. The Apple Music / TV+ / App Store data plane is at the scale where your Splunk + ML production experience compounds.

## What matched
- **"Configure, tune, fix multi-tiered systems for performance, stability, availability"** → MART framework reduced MTTR ~40% across 4 platforms
- **"Exabytes of data, tens of thousands of jobs"** → 25M+ msgs/day; ML queries on MongoDB for daily / week-over-week metrics
- **"Bare-metal and cloud computing platforms"** → VM → PCF → Kubernetes → AWS migration leadership
- **"Analytics enabling features in Apple Music, TV+, App Store"** → Adobe AJO / AEP / CJA, MoEngage at production scale — customer-engagement analytics at adjacent scale
- **"Hadoop, Spark, Flink, Kubernetes, AWS"** → K8s + AWS strong; Hadoop / Spark / Flink absent (see Gaps)

## Gaps
1. **No Hadoop / Spark / Flink production experience**
2. **Posting status uncertain** (404 on retry)
3. **Apple Music / TV+ / App Store domain unfamiliar**

## Gap mitigation
1. Hadoop/Spark → 30-day Spark Structured Streaming course; reframe MART as "Splunk MLTK is my anomaly-detection-on-streaming-data pattern; transfers to Spark Structured Streaming"
2. Posting → recruiter confirmation before any application work; if delisted, do not apply (capacity to other roles)
3. Domain → cover letter pivots to "I run Adobe AJO / AEP at production scale at T-Mobile — same customer-engagement analytics primitives at Apple's scale"

## Pre-application checklist
- [ ] **First: recruiter check that this requisition is still open**
- [ ] If open: confirm posted base range on live JD (must be ≥$200K floor)
- [ ] Take Spark Structured Streaming course before submitting
- [ ] LinkedIn outreach to one Apple Analytics SRE engineer

---

# TAILORED RESUME

## VISHWESHWAR CHIPPA
**SRE Manager | Analytics & Observability Platform Reliability | Splunk Authority | AI-Native SRE**

Atlanta, GA → Open to relocate Cupertino, CA | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
SRE Manager with 21+ years operating analytics and notification platforms at enterprise scale. At T-Mobile, lead a **15-person SRE team** managing 4 production platforms processing **25M+ messages/day** with **99.99% availability**. Authored the **MART (Monitoring/Alerting/Reporting/Troubleshooting) framework** in Splunk that reduced MTTR by ~40% across the notification ecosystem, built **production ML anomaly detection** in Splunk MLTK, and operate Adobe AJO / AEP / CJA — customer-engagement analytics at adjacent scale to Apple Music / TV+ / App Store. Seeking SRE Manager role with Apple Services Engineering Analytics.

---

## CORE COMPETENCIES (Analytics SRE alignment)
Observability Framework Authorship · Splunk Deep Expertise · ML Anomaly Detection in Production
15-Person SRE Leadership · Multi-Tiered Systems Performance Tuning · SLO/SLI Governance at Scale
Customer-Engagement Analytics Operations (Adobe AJO/AEP/CJA in production)

---

## TECHNICAL SKILLS (mapped to JD)
**Observability:** **Splunk (deep — MART framework author, MLTK integration, custom dashboards, SLO burn-rate calculations)**, AppDynamics, Grafana, DORA
**Analytics Platforms (production):** Adobe Journey Optimizer (AJO), Adobe Experience Platform (AEP), Customer Journey Analytics (CJA), Campaign Manager, MoEngage
**Data Plane:** MongoDB, Cassandra, Redis, MySQL — distributed at production scale; ML queries for trend analysis
**Cloud / Compute:** AWS (EKS, Lambda, SQS, SNS, S3); Kubernetes (production at 25M-msg-per-day); Docker; PCF; VM lineage
**Streaming Adjacency:** RabbitMQ, Spring Boot, TIBCO EMS (legacy); event-driven patterns
**Languages:** Python (primary — built ML models, AI agents), Java, Kotlin, JavaScript
**Security:** Vault, CyberArk, IAM, Aqua, SonarQube, AppScan
**Currently leveling up:** Spark Structured Streaming (30-day course in progress)

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 platforms · 25M+ msgs/day · **15 direct reports** · MART framework adopted org-wide · 99.99% availability

**Observability & Analytics Reliability (ASE Analytics alignment)**
- Authored **MART (Monitoring/Alerting/Reporting/Troubleshooting)** framework in Splunk; adopted across T-Mobile notification ecosystem; **~40% MTTR reduction**
- Built **15+ real-time Splunk dashboards** tracking SLOs, message volumes, anomaly alerts, platform health across 42 downstream systems
- Built and deployed **ML anomaly detection** in Python + Splunk MLTK for the DND domain; recovered ~750K message deliveries monthly
- Built **GenAI metrics agent** answering natural-language platform-health queries; eliminated ~8 hours/week of leadership reporting

**Customer-Engagement Analytics at Production Scale**
- Operate **Adobe Journey Optimizer (AJO)** as primary notification orchestration platform; journey reliability, SLO definition, operational governance
- Operate **Adobe Experience Platform (AEP)** for customer data integration and identity management; manage data quality, ingestion reliability, downstream journey triggers
- Use **Customer Journey Analytics (CJA)** as primary reporting layer for platform metrics; built custom CJA dashboards for executive tracking
- Pattern: customer-engagement analytics at adjacent scale to Apple Music / TV+ / App Store

**SRE Leadership & Operating Model**
- Lead **15-person onshore + offshore SRE team**; on-call rotation, escalation, incident command for 24/7 coverage
- Maintained **99.99% availability** and **zero customer-impacting Sev1s** over 36 months
- Defined SLOs for 4 platforms; burn-rate alerting at 5% / 1% budget consumption

**Multi-Tiered Systems Tuning (JD language match)**
- Right-sized Kubernetes cluster footprint (recovered ~30% over-provisioning)
- Tuned MongoDB query patterns and JVM behavior for 25M-msg-per-day throughput
- Implemented PodDisruptionBudgets and circuit breakers preventing cascading failures

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

> "I'm Vishweshwar Chippa, SRE Principal at T-Mobile. I authored the observability framework — MART — that our entire notification ecosystem runs on, and I built an ML anomaly detection model in Splunk MLTK that runs in production recovering about 750,000 message deliveries a month. I also operate Adobe AJO and AEP — customer-engagement analytics at adjacent scale to Apple Music and TV+. I lead 15 engineers, 25 million messages a day, 99.99% availability for 3 years. The Apple Analytics SRE Manager role is where observability authorship, AI-SRE practice, and customer-data analytics converge. Approved I-140."

# COVER LETTER OPENER

> Dear Apple Services Engineering Hiring Team,
>
> The Analytics SRE Manager role asks for someone who can lead reliability for the multi-tiered analytics platforms behind Apple Music, TV+, and the App Store. The work I have led at T-Mobile is functionally adjacent: I authored the MART observability framework that our 4-platform notification ecosystem runs on, I built and deployed an ML anomaly-detection model in Splunk MLTK that runs in production at 25 million messages a day, and I operate Adobe AJO and AEP — customer-engagement analytics at scale. I lead 15 SRE engineers, maintain 99.99% availability across 36 consecutive months, and I am currently leveling up Spark Structured Streaming to close the streaming-frameworks gap relative to Hadoop/Spark/Flink. I have an approved I-140 (June 2016 priority date).
