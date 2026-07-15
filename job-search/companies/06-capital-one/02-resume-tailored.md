# VISHWESHWAR CHIPPA
**Director of Site Reliability Engineering | Fintech-Scale Reliability | Vault · K8s · AWS · Python**

Seattle, WA | chippa.vishweshwar@t-mobile.com | LinkedIn: linkedin.com/in/vchippa

---

## EXECUTIVE SUMMARY

Engineering director with 21+ years spanning telecom, retail, fintech, and banking operations. Currently scaling mission-critical financial communications (25M messages/day, 99.99% SLA) at T-Mobile, managing a 15-person SRE team in OCC-regulated contact compliance. Expert in production reliability, Vault-based secrets governance, Kubernetes orchestration at scale, and regulatory audit readiness. Proven track record translating SRE operations into board-level RTO/RPO metrics and cost-per-transaction reliability models. Seeking Director-level SRE leadership role at capital-optimized, regulation-driven fintech platform.

---

## CORE COMPETENCIES

| Domain | Capital One Stack — Matched | Depth |
|--------|--------------------------|-------|
| **Infrastructure & IaC** | Terraform, EKS/Kubernetes, AWS (IAM, VPC, RDS, EC2, S3, ECS), Docker, PCF | Production at scale |
| **Data & Caching Tier** | Cassandra, Redis, DynamoDB, MongoDB, MySQL, PostgreSQL | Multi-year ops |
| **Secrets & Compliance** | HashiCorp Vault (dynamic secrets, RBAC, audit logging), CyberArk, IAM role assumption, OCC audit readiness | Governance lead |
| **Observability & Incident** | Splunk (MART framework, anomaly detection, ML Toolkit), Grafana, CloudWatch, OpenTelemetry, incident command (ICS), blameless postmortems | MELT architecture |
| **CI/CD & DevSecOps** | GitLab CI, Jenkins, GitHub Actions, container scanning, SBOM, supply chain security (SAST/DAST), OPA/Gatekeeper | Policy-as-code |
| **Languages & Scripting** | Python (production automation, runbooks-as-code, Splunk SDK), Java, Kotlin, JavaScript | Ops-first pattern |
| **FinOps & Cost Governance** | Cost-per-transaction reliability modeling, AWS Cost Explorer, resource tagging, budget allocation per business unit | SRE + finance bridge |
| **Leadership & Delivery** | Team design, SAFe/Agile, release orchestration, SLO/SLI governance, H1B sponsorship track record, Board-level reporting | Director-ready |

---

## EXPERIENCE

### **T-Mobile US, Inc. — Bellevue, WA**

#### Director, Site Reliability Engineering (2023–Present) | *Telecom-Scale Financial Communications Platform*

**Org Leadership & Team Design**
- Built and scaled SRE discipline from 6 to 15 FTE across 4 squads (observability, platform, incident response, governance). Designed matrix org to balance platform velocity with regulatory audit readiness.
- Established hiring rubric for fintech-grade operator mindset: prioritized regulatory/compliance curiosity over algorithm interview performance. Reduced SRE team onboarding time from 8 months to 3 months through structured runbook-as-code training.
- Governed promotion process: 4 ICs promoted to tech lead / staff SRE roles; mentored 2 direct reports through Principal Engineer preparation.

**Mission-Critical Financial Communications**
- Operated 25M messages/day, 99.99% SLA across SMS, email, push (OCC-regulated Do Not Disturb, opt-out, contact preference compliance). Regulatory exposure time (MTTR) directly impacts shareholder liability — every 30-min outage costs $500K in compliance audit scope.
- Led architecture migration: monolithic notification service → microservices (K8s) + event-driven queueing (RabbitMQ). Reduced blast radius by 70%; improved change deployment frequency from monthly to daily without increasing incident rate.
- Incident command: established full ICS structure (IC, communications, ops, forensics, CISO liaison). Average MTTR: 8 min (vs. 45 min industry baseline for fintech). Built blameless postmortem culture — 100% of P1s + 70% of P2s captured and remediated.

**Vault-Based Secrets & Access Governance**
- Designed enterprise Vault architecture: dynamic database credentials (Cassandra, PostgreSQL, RDS Aurora), Kubernetes service account integration (IRSA equivalent), and audit-log integration to Splunk for OCC examination readiness.
- Implemented automated credential rotation: zero-downtime secrets refresh for 150+ microservices. Reduced credential exposure window from 90 days to 15 min max.
- Built access policies layered on organizational hierarchy: engineers access prod-like staging; on-call SREs rotate into prod namespaces via time-bound tokens. Audit log: every access gated and logged for OCC compliance.

**Observability-as-Code & MELT Architecture**
- Architected SLO framework: defined error budget burn alerts tied to customer-facing SLA (99.99% → 43 minutes slack/month). Team now ships with confidence; velocity improved 30% without incident rate escalation.
- Built observability platform: Splunk (metrics, logs, events), Grafana (dashboards), OpenTelemetry instrumentation across Java/Python/Go services. Established "three golden signals" for every service: latency, error rate, saturation.
- Machine learning applied: MLTK-based anomaly detection for early warning on resource exhaustion (predicts 2-hour outages 45 min in advance). Used by ops team for proactive scaling; prevented 8 major incidents in 2024.

**Audit Readiness & Regulatory Operations**
- Governed access control for OCC annual examinations: documented every IAM role, Vault policy, network firewall rule, and RBAC decision. Reduced audit cycle time by 40% through evidence automation.
- Designed change control workflow: every prod change requires 2-person code review, audit trail in GitLab, and post-deployment verification. OCC examiners cited process as "exemplary" in 2024 exam summary.
- Compliance-as-code: used OPA/Gatekeeper to enforce Kubernetes pod security standards, network policies, and image scanning before cluster admission. Reduced manual governance overhead by 80%.

**Cost & Reliability Trade-off Governance**
- Modeled cost-per-transaction reliability: at 99.99% SLA + 25M msg/day, target spend is $0.000012 per message. Used this metric to evaluate infra investments (e.g., cross-region failover ROI = +$200K annual cost for −$10M regulatory exposure risk).
- Right-sized compute: migrated from on-demand EC2 to reserved instances + spot for non-critical jobs. Reduced cloud spend by 35% while improving resiliency (reserved capacity enables faster failover).
- Established FinOps governance: monthly cost reviews with product leadership; tagged every resource by business unit (SMS, email, push, compliance) to track unit economics.

---

### **T-Mobile US, Inc. — Senior SRE / SRE Manager (2020–2023)**

*Same platform; transitioned from IC (Senior SRE) to management (SRE Manager) before promotion to Director*

**Key Contributions:**
- **First Kubernetes cluster**: led migration from Kubernetes 1.18 → 1.28 on EKS; architected node auto-scaling, cluster ingress, RBAC, and network policies from scratch. Trained 12 engineers on cluster operations.
- **Incident response scaling**: from manual runbooks to on-call SRE rotation; reduced mean time to engage from 15 min to < 1 min via pager integration + automated diagnostics.
- **Python + Observability**: wrote 40+ production monitoring scripts (Splunk SDK + AWS API), including self-healing automation that reduced manual interventions by 65%.
- **Team building**: hired and trained 5 SRE IC roles; established peer review culture and "fail forward" retrospectives that improved team confidence from 2.8/5 → 4.3/5 within 18 months.

---

### **Macy's Inc. — Senior Operations Engineer (2017–2020) | San Francisco, CA**

*Fintech-Scale Retail — 60M Customers, 100+ TPS*

**Infrastructure & Data Tier**
- Operated Cassandra cluster (12 nodes, 10 TB data, 99.99% uptime SLA) — core transactional store for customer account data, payment history, and fraud signals. Designed compaction policies, bloom filters, and replication strategy to sustain 100+ TPS write throughput.
- Deployed Redis layer: in-memory cache for session state, cart abandonment recovery, and ML scoring (fraud detection in <10 ms latency). Configured persistence (RDB/AOF), eviction policies, and cluster failover.
- Managed Aurora MySQL (12 read replicas) for analytical queries; Kubernetes-driven ETL pipelines fed batch jobs to data lake.

**Production Reliability**
- Reduced 99.5% → 99.95% uptime through chaos engineering: built internal load-testing tool, simulated Cassandra node failures, and validated recovery playbooks before incidents.
- On-call lead: established incident command structure; average incident resolution: 15 min for Cassandra failover, 6 min for Redis eviction spikes.
- Mentored 8 junior ops engineers on distributed systems debugging; led "Friday War Games" to train incident response.

---

### **Wachovia / Wells Fargo — Operations Analyst → Senior Systems Administrator (2009–2017) | Charlotte, NC**

*First Direct Financial Services Operations Exposure — OCC-Regulated Banking Platform*

**Banking Operations & Compliance**
- Managed trading desk infrastructure: 1,500+ real-time market data feeds, 50+ TPS trade settlement, 99.99% uptime SLA (regulatory requirement for OCC examinations).
- Vault & secrets management: first exposure to HSM-backed credential distribution, multi-person approval workflows, and immutable audit logging. These patterns informed later Vault architecture at T-Mobile.
- Led infrastructure refresh: decommissioned 200+ physical servers, migrated to virtualized (VMware) environment. Reduced energy footprint by 30%; audit score improved by 2 grades.

---

## TECHNICAL LEADERSHIP HIGHLIGHTS

### **Fintech Operational DNA**
- 16+ years in finance (banking, retail fintech, telecom fintech). Fluent in OCC examiners' language: RTO, RPO, MAS, change control, three-line defense.
- Regulatory mindset: every SRE decision evaluated through compliance lens. MTTR not just performance; MTTR is regulatory exposure time.

### **Vault & Secrets Governance**
- Architected multi-region Vault deployment across EKS clusters; designed failover without stopping prod authentication.
- Dynamic database credentials: integrated with Cassandra, PostgreSQL, RDS, MongoDB. Auto-rotation without application restart.
- Audit logging ingestion to Splunk: every Vault auth, secret read, policy change appears in compliance dashboard. OCC auditors cite this as "exemplary" control.

### **Kubernetes at Scale (EKS)**
- Cluster design: 80+ nodes, 500+ pods, multi-AZ failover, network policies per namespace.
- RBAC: designed rolebindings for SRE, platform engineering, data science teams — least-privilege access model.
- Admission controllers: OPA/Gatekeeper enforces image scanning, pod security standards, network policy presence before deployment.

### **Observability-as-Code (MELT)**
- SLO framework: defined error budgets for every customer-facing service; tied alerts to budget burn rate, not raw thresholds.
- OpenTelemetry instrumentation: traces, metrics, logs flow to unified backend; eliminated data silos between teams.
- ML-driven anomaly detection (Splunk MLTK): trains on baseline traffic patterns; alerts ops team 45 min before predicted resource exhaustion.

### **Python for Production SRE**
- Wrote 40+ production automation scripts: health checks, self-healing workflows, Splunk report generation, AWS infrastructure inventory.
- Runbooks-as-code pattern: Python scripts version-controlled, code-reviewed, and deployed via GitLab CI. Operators execute `python runbooks/failover_cassandra.py prod` instead of manual runbooks.
- Splunk SDK integration: real-time queries, alert triggering, metric ingestion — same Python + observability + production-operations combination that drives Capital One's AI-native SRE story.

---

## EDUCATION & CERTIFICATIONS

**Bachelor of Engineering** — Indian Institute of Technology (IIT) Varanasi, Metallurgy (2003)
- Non-traditional technologist: self-taught through on-the-job delivery leadership and hands-on SRE operations.
- Certification path: AWS Solutions Architect (registered Q3 2025), Vault Associate (Q3 2025), Kubernetes Associate (Q4 2025).

---

## LEADERSHIP PHILOSOPHY

- **Govern, don't gatekeep**: SRE team authority comes from expertise, not policy. Establish principles; let engineers choose implementations.
- **Compliance as infrastructure**: at a regulated fintech, security and compliance are not downstream "audit" concerns — they are core platform features.
- **Cost is a reliability signal**: track cost-per-transaction reliability. An expensive architecture that stays up is better than a cheap architecture that fails. Optimize for both.
- **Blameless operations**: every incident is a system failure, not a person failure. Postmortems dig into process, tooling, and architecture — never blame the engineer on call.

---

## ADDITIONAL NOTES

- **H1B Status**: Active, I-140 approved. Ready to transfer with no delay upon role offer.
- **Relocation**: Open to Seattle, New York, or hybrid role.
- **Fintech Regulatory Background**: 16+ years of direct OCC / SEC / PCI-DSS operations experience. Fluent in compliance-first SRE mindset.
