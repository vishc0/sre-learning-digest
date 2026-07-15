# Resume: Vishweshwar Chippa — Director of SRE / Engineering Manager
## Tailored for Microsoft Azure Platform Group (IC6 / Director scope)

---

## EXECUTIVE SUMMARY

**Director of SRE and Engineering Organization** at T-Mobile with 21 years of production systems experience across telecom, retail, insurance, banking, and energy verticals. Currently leading a 15-person SRE organization managing a 25M msg/day notification platform (99.99% uptime SLA, zero Sev1 incidents in 2024–2025 fiscal year). Expertise spans Kubernetes orchestration (EKS / AKS-ready), large-scale observability (Splunk + OpenTelemetry transition), AI-native reliability practices (production GenAI agents, ML anomaly detection governance), and cross-functional delivery. Non-CS background (IIT-BHU Metallurgy) with demonstrated ability to translate complex systems thinking to non-technical stakeholders and build high-performing, inclusive teams in highly regulated environments. Seeking Director-level role to own SRE/Platform organization at Microsoft Azure, driving AI-native reliability and zero-trust infrastructure for enterprise cloud customers.

---

## CORE COMPETENCIES

**Engineering Leadership**: Org design (hiring, career ladders, retention), VP-level partnership, 0→1 SRE program scaling, incident command governance (blameless postmortems, SLO/SLI frameworks), team mentorship and talent development

**Observability & SRE**: Splunk (MART framework expert, ML/MLTK, advanced visualizations), Grafana, AppDynamics, OpenTelemetry instrumentation, SLO/SLI math, error budget burn-rate alerting, MTTR/MTTD optimization

**Cloud & Kubernetes**: AWS EKS (production scale), Kubernetes internals (controllers, RBAC, admission webhooks, HPA/VPA), AKS-pattern fluency (Managed Identity, Service Mesh, Event Hubs), Docker, multi-cloud architecture design

**AI-Native Reliability**: Production GenAI agent deployment and governance, ML anomaly detection (Python + Splunk MLTK), LLM prompt engineering for runbook automation, responsible AI safeguards for enterprise SRE

**DevSecOps & Infrastructure Security**: Vault, CyberArk, IAM least-privilege (IRSA), network segmentation, secrets scanning (GitLeaks, Vault), supply-chain security (SBOM, OPA), CI/CD hardening

**Data & Messaging at Scale**: Cassandra (multi-region), Redis, MongoDB, MySQL, RabbitMQ, Kafka-adjacent architectures, event-driven reliability patterns

---

## EXPERIENCE

### **T-Mobile (Telecom Services & Billing)**

#### Director of Reliability Engineering / SRE Manager (2023–Present) — *Notification Platform, 15-person team*

**Organization & Leadership:**
- Built SRE organization from 3 individuals to 15-person team across 4 regions (Kansas City, Denver, Charlotte, Austin) with intentional career-ladder design (IC1→IC5, Staff SRE track).
- Partnered with VP of Engineering on hiring, retention, and skill development; reduced team churn to <5% annually.
- Established blameless postmortem culture: 100% postmortem completion rate, avg time-to-publish 2 business days.
- Mentored 3 engineers to promotion (2 to Senior SRE, 1 to Staff); built internal "SRE Academy" curriculum (6-week onboarding bootcamp).

**AI-Native SRE — Production, Not Pilot:**
- Deployed production-grade GenAI agent (Claude API + LangChain) to automate runbook triage for the notification platform; reduces mean-time-to-resolution (MTTR) by 18% for Sev2/Sev3 incidents. Governance layer includes audit logging, hallucination detection, and human-in-loop validation for Sev1.
- Implemented ML anomaly detection (Python + Splunk MLTK) on 200+ metrics (throughput, latency, error rate); false-positive rate tuned to <3%, catching 94% of anomalies >2σ above baseline within 2 minutes.
- Designed responsible AI safeguards: model drift monitoring, explainability dashboards, quarterly model retraining review with cross-functional stakeholders.
- **Alignment to Azure AI Platform priorities (2026)**: These production patterns directly apply to Azure Monitor + Application Insights GenAI anomaly detection, Azure OpenAI API governance, and Copilot for Azure observability tooling.

**Reliability Engineering at Scale (Azure-Aligned Patterns):**
- Architected and operationalized MART framework (Metrics → Alerts → Runbooks → Triage) across the platform; drove SLO adoption from 2 services (2022) to 25 services (2025). Error-budget burn alerts prevent >95% of customer-impacting incidents before they occur.
- Implemented SLO governance: SLI definition standards, error-budget thresholds per service tier, quarterly SLO calibration reviews. Result: customer-reported downtime reduced from 180 min/year → 14 min/year (99.99% ↑ to 99.9975%).
- **Metrics**: 99.99% uptime SLA delivery for 25M msg/day; zero Sev1 incidents in FY2024–2025. Avg incident-resolution time: 8 min (Sev1), 18 min (Sev2).
- Monitoring stack: Splunk (core observability), AppDynamics (APM), Grafana (dashboards). Currently leading OpenTelemetry migration to consolidate vendor lock-in and enable multi-cloud observability portability. **Azure Monitor / Application Insights readiness**: KQL translation table created; metrics schema designed for Geneva protocol compatibility.

**Kubernetes & Cloud Migration Architecture (AKS/EKS Expertise):**
- Architected and deployed EKS clusters (3 prod, 2 staging) managing 80 microservices with 99.95% cluster uptime. RBAC policies enforce least-privilege; network policies segment prod/staging/dev traffic.
- Designed and implemented admission webhooks (custom validators) to prevent insecure resource specs (privileged pods, unsafe host mounts); enforcement rate 99.8%.
- **AKS cross-training completed**: Proficient in Managed Identity (equivalent to IRSA), Service Mesh (Istio/Linkerd patterns), Event Hubs (Kafka-compatible event architecture). Multi-cloud architecture strategy document completed and shared with AWS/Azure architecture teams.
- Implemented HPA + VPA for 40 services; auto-scaling SLA adherence 98.7%. Reduced unnecessary resource reservation by 22% via data-driven right-sizing.
- Kubernetes cost governance: Kubecost integration, chargeback model by team, quarterly capacity planning reviews. FY2025 K8s spend trending 15% below budget despite 30% traffic growth.

#### Senior Reliability Engineer (2021–2023) — *Notification Platform, IC5*

- Led incident response for 45 Sev2+ incidents; avg MTTR 22 min, all post-mortems published within 72 hours, zero repeat incidents.
- Designed first SLO framework for platform: 4 golden signals (latency, throughput, error rate, utilization), historical baseline analysis, burn-rate math. Adoption led to 60% fewer false-positive alerts.
- Built Splunk dashboards and ML models for demand forecasting (7-day ahead, 92% MAPE) and anomaly detection (threshold + ML hybrid approach).
- Mentored 2 junior SREs; both promoted to Mid-level within 18 months.

### **Dish Network (Media & Streaming)**

#### Platform Engineer, Observability (2019–2021) — *Streaming Infrastructure, IC4*

- Designed and deployed AppDynamics platform for 150+ microservices; instrumentation coverage 96% of transactions.
- Built real-time anomaly detection for streaming latency; reduced customer complaints by 35% via proactive notification to on-call engineer.
- Implemented distributed tracing (Spring Cloud Sleuth + ELK) for multi-tier request path visibility; reduced MTTR for cross-service issues by 40%.

### **Accenture (Professional Services) — Leadership Track**

#### Senior Consultant, Cloud Architecture (2016–2019) — *Enterprise Modernization, IC4*

- Led cloud migration engagements for 6 Fortune 500 clients (banking, insurance, retail); designed IaC (Terraform, CloudFormation) and CI/CD pipelines.
- Architected multi-region disaster recovery for critical banking systems (RTO 15 min, RPO 5 min); passed PCI-DSS audit with zero findings.
- Built and led a 12-person DevOps team for a year-long retail modernization project; delivered 3 Kubernetes clusters, 40 microservices, zero production incidents in first 6 months.

### **Ericsson & Telecom Ops (Early Career, 2003–2016)**

#### Middleware Architect / Senior Delivery Engineer (2011–2016)
- Designed and operated mission-critical TIBCO, RabbitMQ, and Kafka messaging infrastructure for telecom BSS/OSS platforms.
- Led 15-person delivery team for 5-year telecom infrastructure modernization; delivered on time, under budget, zero billing outages.

#### Sr. Operations Engineer, Telecom Carrier Grade Systems (2006–2011)
- Managed 24/7 operations for carrier-grade systems (telecom switches, billing engines); Sev1 incident count <1/month across 50 production systems.

#### Operations Support Engineer (2003–2006)
- Foundation work: on-call rotation, ticket triage, escalation management.

---

## CERTIFICATIONS & LEARNING (Active)

- **Certified Kubernetes Administrator (CKA)** (2024, in progress) — exam scheduled Q3 2026
- **Terraform Associate (AWS)** (KodeKloud track, in progress) — comprehensive IaC and state management
- **AWS Solutions Architect Associate (SAA-C03)** (2025 certification target)
- **Observability Engineering (in progress)** — OpenTelemetry instrumentation, MELT framework, vendor-agnostic metrics translation
- **Microsoft Azure Fundamentals & AKS Deepdive** (self-paced, 2025) — Managed Identities, Service Mesh, Event Hubs, Azure Monitor/Application Insights

---

## EDUCATION & BACKGROUND

**B.Tech, Metallurgical Engineering**, Indian Institute of Technology (IIT-BHU), Varanasi, India (2003)
- Self-taught technologist: systems thinking learned through production incident response and architecture design, not formal CS curriculum
- Non-traditional path: strength in translating complex systems to non-technical stakeholders (CFOs, CMOs, board-level execs)

---

## KEY DIFFERENTIATORS FOR MICROSOFT AZURE

| Microsoft Priority (2026) | Your Credential | Evidence |
|---|---|---|
| **SRE Organization Scaling** | Built 3→15 person SRE team from scratch; 100% postmortem completion rate | Mentored 3 engineers to promotion; established SRE Academy curriculum |
| **AI-Native Reliability** | Production GenAI agents + ML anomaly detection deployed at 25M msg/day scale | 18% MTTR improvement; 94% anomaly catch rate (<3% false positives) |
| **Kubernetes at Enterprise Scale** | 80 microservices on EKS; admission webhooks, RBAC, HPA/VPA, cost governance | Kubecost integration; 98.7% auto-scaling SLA; 15% spend under budget |
| **Multi-Cloud Portability** | AKS architecture study completed; OpenTelemetry migration in progress | KQL translation table; Geneva protocol compatibility validated; Managed Identity fluency |
| **SLO/SLI Governance** | Built and scaled MART framework from 2→25 services; error-budget math operationalized | 99.9975% uptime vs. 99.99% SLA; zero Sev1 incidents in 2 years |
| **Observability Modernization** | Splunk expert (MART, MLTK); leading transition to vendor-agnostic OTel + Azure Monitor | Dashboards, ML models, KQL syntax fluency |
| **Incident Command & Postmortems** | Zero-repeat-incident track record; VP-level partnership on incident governance | 45 Sev2+ incidents; 100% postmortem completion; avg 22 min MTTR |
| **Mentorship & Diversity** | Built inclusive career ladders; mentored 3→promotion; active in SRE community | Established promotion pathways; "SRE Academy" on-ramp curriculum |

---

## LINKS & ARTIFACTS

- **GitHub Portfolio**: [3 capstone SRE/DevSecOps projects — under construction for public release by Q2 2026]
- **Splunk MART Framework Whitepaper** (internal): Methodology document for cross-functional SRE adoption
- **Open-source contributions**: [Forthcoming — currently drafting OTel instrumentation examples for messaging platforms]

---

**Last updated**: June 2026 | **Targeting**: Director of Reliability Engineering / Engineering Manager (Azure Platform Group, IC6)
