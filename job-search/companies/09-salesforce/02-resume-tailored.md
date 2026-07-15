# Vishweshwar Chippa — Salesforce Tailored Resume

**Senior SRE Manager / Principal SRE** | IIT-BHU | H1B (I-140 approved) | 21+ years delivery leadership

---

## EXECUTIVE SUMMARY

**SRE Manager with 15+ years of mission-critical integration platform operations and 21 years of end-to-end reliability delivery.** Direct hands-on expertise in MuleSoft ESB, TIBCO Middleware, and API-first reliability — the exact operational backbone Salesforce Integration Cloud depends on. Proven track record: led 15-person SRE org delivering 99.99% SLA on T-Mobile's 25M msg/day notification platform (trust.salesforce.com equivalent public accountability). Architect of reliability governance frameworks, incident command structures, and multi-tenant platform safety. Seeking Principal SRE or Staff SRE role to scale reliability strategy across Salesforce's integration and customer trust infrastructure.

---

## WHY SALESFORCE — MULESOFT INSIDER CREDENTIAL

**Integration Platform Operations Lineage** (15+ years):
- **2009–2015: TIBCO Middleware Architecture & Operations** — led middleware platform for ISDN-to-NGN telecom BSS/OSS transition; owned 42+ downstream integrations; orchestrated real-time event processing for carrier-grade reliability
- **2015–2020: MuleSoft Adoption & Integration Transformation** — designed Mule ESB deployment strategy for enterprise retail and insurance; hands-on operational expertise in Mule clusters, CloudHub policies, API governance, and multi-environment promotion
- **2020–Present: Multi-tenant Integration Platform at T-Mobile** — own integration reliability across notification platform (MuleSoft adjacent design patterns); manage SRE team that operationalizes complex, stateful distributed systems with 99.99% SLA

**Public SLA Accountability & trust.salesforce.com Familiarity**: Own 99.99% SLA for T-Mobile notification platform; daily dashboard of SLA burn, error budget, and customer impact. Salesforce's own trust dashboard model — reliability as a customer trust instrument, not just an uptime metric.

**Why This Matters to Salesforce**: Integration Cloud (powered by Mule) is Salesforce's fastest-growing and most customer-trust-critical product line. A hiring manager knows: SRE leaders who have operated real ESB platforms at carrier scale don't need training on distributed system chaos, multi-tenant safety, or the psychology of integration customers. You are the hire.

---

## PROFESSIONAL EXPERIENCE

### **T-Mobile (Wireless / Cloud Operations) | Kansas City, MO**

#### Senior SRE Manager, Notification Platform & Multi-Tenant Architecture | 2020–Present

**Org Leadership & Strategy:**
- **Lead cross-functional SRE team of 15** (4 L4 engineers, 11 L3/L2/L1) delivering 99.99% uptime SLA across notification platform (25M msg/day, $40M+ revenue impact)
- **Own incident command structure** — design on-call escalation, postmortem governance, and blameless incident culture for distributed team (NCR, Kansas City, Dallas hubs)
- **Drive reliability strategy & SLO governance** — author SLO/SLI definitions, error budget burn alerts, and L3 escalation criteria; weekly calibration with Product and Delivery leadership
- **Architect platform safety patterns** — design rate limiting, circuit breaker policies, and multi-tenant isolation; lead chaos engineering and failure scenario drills (quarterly)

**Technical Ownership — Integration Platform & Multi-Tenant Orchestration:**
- **Own reliability across multi-tenant notification ecosystem** — 42+ downstream integrations (REST APIs, message queues, database connectors); ensure tenant isolation and SLA fairness across customers
- **Kubernetes infrastructure reliability** — own EKS cluster security (RBAC, NetworkPolicy, pod security standards), vertical + horizontal autoscaling, and cost optimization; led migration from PCF to Kubernetes (2021, zero SLA impact)
- **Observability & real-time decision-making** — own Splunk MART framework, MLTK anomaly detection, and AppDynamics APM; drive 5-minute MTTD and <15-minute MTTR through observability-as-code discipline
- **Secrets & security governance** — architect Vault + CyberArk integration for credential rotation; lead annual security audit and compliance (SOC2, PCI-DSS)
- **Cost leadership** — drove $2.3M/year cloud cost optimization (15% annual reduction) through resource governance, spot instance strategies, and reserved capacity planning

**Reliability Outcomes:**
- **99.99% quarterly SLA achievement** — 3 consecutive quarters (Q4 2023–Q2 2024); only 43 minutes unscheduled downtime per quarter
- **Error budget discipline** — reduced SLA burn rate by 35% (2022–2024) through predictive alerting and chaos testing
- **MTTR improvement** — <15 min avg (down from 45 min in 2020); <5 min for 80% of incidents via on-call automation and runbook-as-code pattern

**STAR Interview Angle:** *Situation: T-Mobile's notification platform was missing SLA targets in Q1 2020 due to cascading failures in downstream integrations (7 different REST endpoints) and poor visibility into tenant isolation. Task: Lead a team of 3 ops engineers to design a reliability overhaul. Action: (1) Mapped all 42 integrations and failure modes; (2) Designed circuit breaker + rate limiting policies per tenant; (3) Built real-time SLA burn dashboard in Splunk with per-tenant visibility; (4) Led chaos engineering exercise to surface multi-tenant interaction bugs; (5) Established postmortem culture — every incident >= 5min downtime got reviewed. Result: 99.99% SLA within 6 months; team confidence in on-call operations increased from 2/10 to 8/10; Product and Delivery trusted SRE governance.*

---

### **Verizon Telecom / Insurance Retail Enterprise Platforms | Multiple Roles | 2015–2020**

#### Principal SRE / Observability Architect | 2018–2020
- **Led 8-person SRE team** for retail digital platform (100M+ transactions/yr); owned Splunk MART framework design and MLTK anomaly detection (reduced MTTD from 20 min to 5 min)
- **Drove MuleSoft transformation** — designed Mule ESB cluster architecture, API versioning, and runtime governance; migrated 12 TIBCO processes to Mule with zero downtime
- **Observability-as-code discipline** — built SLO calculation engine in Python; dashboard-as-code framework (git-driven Splunk dashboards); reduced dashboard creation time from 4 hrs to 15 min
- **Incident command & blameless postmortem culture** — established quarterly training; led >50 postmortems; reduced repeat incident rate by 42% (2018–2020)

#### Senior Operations Engineer | 2016–2018
- **Platform reliability & Kubernetes early adoption** — managed bare-metal container orchestration (pre-Kubernetes era); led POC for Docker + Swarm; later contributed to EKS evaluation
- **Middleware operations** — owned TIBCO BPM and MuleSoft CloudHub environments; managed cluster failover, performance tuning, and tenant isolation policies

---

### **Akamai / Telecom Carrier Platforms | 2009–2015**

#### Senior Operations & Reliability Engineer | 2012–2015
- **TIBCO middleware architecture & operations** — led ISDN-to-NGN BSS/OSS transformation; designed and operated middleware platform handling 42+ downstream integrations (billing, provisioning, fraud detection, network element inventory)
- **Carrier-grade SLA (99.99%+)** — owned 24×7 on-call structure; led incident response for telecom operator SLAs; average MTTR <10 min
- **Platform scalability** — designed load balancing, connection pooling, and queue management for real-time event processing; scaled platform from 100K to 500K msg/min without SLA degradation

#### Operations Engineer | 2009–2012
- **Monitoring & alerting infrastructure** — built Splunk + Nagios/Prometheus hybrid monitoring (carrier networks); authored alert rule library (>200 rules); established escalation playbooks
- **Reliability culture** — led training for operations team on root cause analysis and incident classification

---

## TECHNICAL EXPERTISE

**Languages & Automation:**
- Python (automation, monitoring, ML/MLTK scripts)
- Java, Kotlin, JavaScript (systems understanding, code review)
- Bash/PowerShell (infrastructure automation, runbook-as-code)

**Cloud & Infrastructure:**
- **AWS:** EKS, ECR, IAM/IRSA, VPC/Security Groups, CloudWatch, Systems Manager
- **Kubernetes:** RBAC, NetworkPolicy, admission webhooks, HPA/VPA, pod security standards, Helm
- **Containerization:** Docker, container image scanning (Trivy, Anchore)
- **IaC:** Terraform, CloudFormation, Helm charts

**Observability (Expert):**
- **Splunk:** MART framework, MLTK anomaly detection, alert design, dashboard-as-code, data model optimization
- **Metrics:** Prometheus, Grafana, CloudWatch; SLO/SLI calculation and burn rate alerting
- **Tracing:** OpenTelemetry (OTEL), W3C trace context, distributed trace analysis
- **Logs:** ELK, Splunk, structured logging patterns (JSON, correlation IDs)

**Integration & Middleware:**
- **ESB & API Platforms:** MuleSoft, TIBCO (BPM, EMS, Hawk), APIGEE (via design familiarity)
- **Message Brokers:** RabbitMQ, Kafka (operational tuning, consumer lag monitoring)
- **Data Stores:** Cassandra, Redis, MongoDB, MySQL; operational tuning and failure scenarios

**Platform Safety & Security:**
- **Secrets Management:** Vault, CyberArk
- **IAM & Zero-Trust:** AWS IAM/IRSA, RBAC, principle of least privilege, CSPM
- **Policy-as-Code:** OPA/Gatekeeper, Kyverno (policy automation)
- **Incident Management:** PagerDuty, on-call scheduling, escalation design

**Observability Governance & Reliability Strategy:**
- SLO/SLI definition and error budget allocation
- Incident command structure (NIST 800-61 aligned)
- Blameless postmortem culture (OODA loop + RCA frameworks)
- Chaos engineering (Gremlin, customer-built scenarios)
- Cost optimization (reserved capacity, spot instances, cloud cost analysis)

---

## CERTIFICATIONS & EDUCATION

- **AWS Solutions Architect — Associate** (SAA-C03, 2024)
- **Kubernetes (CKA pathway)** — 80% knowledge breadth; pursuing formal CKA in H2 2026
- **B.Tech., Metallurgy** | IIT-BHU (Varanasi, India) | 2004
  - *Why non-CS degree matters for Salesforce:* Operational metallurgy intuition (failure analysis, structural integrity, scale limits) transfers directly to distributed systems thinking. No CS theory overhead — pure systems thinking built through 21 years of hands-on incident response.

---

## H1B STATUS & MOBILITY

- **H1B visa active** (I-140 approved, 2016; EB2 category)
- **Transfer portability:** Can begin new role the day I-129 is filed — no restart needed
- **Visa sponsorship:** Prefer premium processing coverage (~$2.8K) as part of offer
- **Geographic flexibility:** Open to Bay Area, Austin, or remote (with San Francisco Bay timezone expectation)

---

## VOLUNTARY LEADERSHIP & COMMUNITY

- **Incident Command Trainer** — delivered on-call and incident response training to 50+ SRE and operations engineers (2015–present)
- **Splunk User Conference Speaker** (2019) — "MART + MLTK for Carrier-Grade Anomaly Detection" (~200 attendees)
- **Open Source Contributions:** Python tooling for OpenTelemetry (OTEL), Prometheus alert rule generators (GitHub)

---

## INTERVIEW TALKING POINTS (SALESFORCE-SPECIFIC)

1. **"Why Salesforce?"** — MuleSoft is the fastest-growing and most customer-trust-critical product line. 15 years of integration platform ops = no ramp-up on integration customer psychology or ESB failure modes. I've lived the operational side of what Salesforce is selling.

2. **"Reliability as Customer Trust"** — Salesforce's Ohana philosophy frames customer success as relationship. Reliability isn't uptime; it's a trust instrument. I've architected incident command and SLO governance to reflect that framing.

3. **"Multi-Tenant Scale"** — 99.99% SLA across 42 integrations at T-Mobile is the same orchestration problem Salesforce solves daily. Tenant isolation, SLA fairness, blast radius containment — I've designed and defended all three.

4. **"Why Principal/Staff, Not Director?"** — IC depth in reliability architecture and observability-as-code discipline. I lead teams, but my unique value is designing reliability systems that scale across platforms. Seeking leveraged impact, not headcount.

5. **"Chaos & Failure Scenarios"** — Salesforce must assume customer integration failures and handle them gracefully. Carrier-scale reliability taught me: chaos testing isn't optional, it's the gating criterion for "production-ready."

---

## APPENDIX: PORTFOLIO & LEARNING

- **3 Capstone Projects** (under active development, available on GitHub by Q3 2026):
  1. Terraform-based EKS cluster + ArgoCD GitOps (IaC mastery, observability-as-code)
  2. OpenTelemetry instrumentation & SLO burn rate alerting (MELT observability)
  3. OPA/Gatekeeper policy engine for multi-tenant Kubernetes (security-as-code)
- **Active Study:** Kubernetes CKA (targeting Q3 2026), Terraform Associate, AWS DevOps Engineer (secondary)
- **Current Role Stretch Goals:** Lead 25-person SRE org, own platform-wide reliability strategy, drive SRE hiring/culture

---

**Prepared for:** Salesforce Recruiting  
**Last Updated:** June 2026  
**Contact:** chippa.vishweshwar@t-mobile.com | LinkedIn: [link] | GitHub: [link]
