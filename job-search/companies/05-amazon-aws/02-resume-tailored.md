# Vishweshwar Chippa
## Director of Site Reliability Engineering | Distributed Messaging at Scale | 25M msg/day | AI-Native Operations

**Seattle, WA** | chippa.vishweshwar@t-mobile.com | linkedin.com/in/vishweshwar-chippa

---

## Executive Summary

Director-level SRE leader owning reliability, platform engineering, and incident command for **25M notifications/day** — a distributed messaging platform operating at **SNS/SQS-equivalent scale** — at T-Mobile. **21+ years** building production infrastructure across telecom BSS/OSS, retail, fintech, insurance, and energy. Leads an organization of **15 direct reports across 4 production platforms**, with a **36-month zero-Sev1 record**. Architect of multi-year platform roadmaps, SLO-based reliability governance, DevSecOps integration, and AI-native operations. Proven ability to translate platform risk into business language — protected $2.8M+ in annual revenue, avoided $3M+ in cloud overspend, and restored availability for 50M+ customers in 72 hours.

**Maps directly to L7 scope**: multi-team ownership, millions of customers downstream, multi-year technical roadmap, measurable business outcomes at Director scale.

---

## Technical Leadership (Customer Obsession · Ownership · Deliver Results)

- **Owns reliability for a 25M-notification/day messaging platform** — operating at the throughput, durability, and availability expectations of a mid-tier AWS managed service (SQS/SNS-equivalent). Leads org of 15 direct reports spanning SRE, platform, and observability disciplines across 4 production platforms serving 100+ upstream applications. Designed SLO governance framework (error budgets, burn-rate burn-down alerts, sliced by customer segment and service tier). **Result**: 99.95% availability YoY; $2.8M annual revenue protected through churn avoidance; zero Sev1 in 36 consecutive months.

- **Drives architectural decisions for a distributed messaging platform** processing 50K+ messages/second with 99.99% durability targets — equivalent to operating and evolving a RabbitMQ/SQS-scale message broker in production. Led multi-year migration from legacy ESB (TIBCO) to Kafka-adjacent stream topology. Made the architecture calls for message deduplication, dead-letter queue topology, producer backpressure, and consumer group scaling. **Result**: 40% end-to-end latency reduction; platform now underpins real-time fraud detection for fintech customers.

- **Leads org responsible for Kubernetes (EKS) platform governance** across 150+ microservices. Drove architectural decision to adopt IRSA (IAM Roles for Service Accounts) to eliminate static secrets cluster-wide — a supply chain security posture directly aligned with AWS Well-Architected Security Pillar. Established RBAC + network policy + admission webhook controls as org-wide standard. Led chaos engineering program (Gremlin-based failure injection) to validate blast radius assumptions before production events. **Result**: 99.9% EKS uptime; passed SOC2 Type II and PCI DSS audits with zero findings.

- **Owns multi-year platform engineering roadmap** for golden paths (GitOps via ArgoCD), canary release orchestration (Flagger + Istio), and FinOps governance (Kubecost + right-sizing). Built internal developer platform (IDP) reducing new-service onboarding from 2 weeks to 2 days — a force multiplier enabling 30+ teams to ship without platform bottlenecks. **Result**: $1.2M annual infrastructure cost savings; 30+ product teams adopted IDP in first year.

---

## Observability & Incident Command (Dive Deep · Bias for Action)

- **Owns observability-as-code program** integrating Splunk (expert — MART framework, MLTK anomaly detection), Grafana, and OpenTelemetry (OTel) distributed tracing across 150+ services. Defined org-wide MELT (Metrics + Events + Logs + Traces) taxonomy; implemented SLO-driven dashboards that surface error budget state to VP-level stakeholders. Built ML-based anomaly detection in Python + Splunk MLTK to catch latency degradation before customers page in. **Result**: Alert noise reduced 65%; MTTD improved 3x; on-call burnout measurably reduced.

- **Leads incident command program** responsible for P1/P2 resolution at platform scale. Facilitated 200+ blameless postmortems and built structured follow-through (root cause + action items + severity scoring + 30/60/90-day decay check). Mentored 15 on-call engineers in Incident Command System (ICS). Authored runbooks-as-code (Python + Ansible) that reduced human decision points during SEV escalations. **Result**: Sev1 escalation for 50M+ customer impact — led cross-functional war room, restored 99.5% availability in 72 hours; zero recurrence.

- **Drives DevSecOps integration across CI/CD pipeline**: embedded SAST/DAST (Checkmarx + OWASP ZAP), supply chain security (SBOM + Sigstore container signing), and policy-as-code enforcement (OPA Gatekeeper on EKS). Reduced critical CVE time-to-patch from 14 days to 2 days. **Result**: Zero breaches across fintech, healthcare, and telecom operating environments; security posture improvements funded by risk-avoidance business case I authored for VP approval.

---

## Data Systems & FinOps (Invent and Simplify · Frugality)

- **Architects multi-terabyte data platforms at scale**: Cassandra (comparable to DynamoDB for high-write, low-latency workloads) for real-time retail inventory; Redis for caching at 100K ops/sec; MySQL for banking-grade transactional workloads. Made multi-region replication, DR runbook, and consistency model decisions. **Result**: 99.99% query SLA; sub-100ms P99 latency at peak load; data tier has never been the incident root cause.

- **Owns FinOps program** with AWS Cost Explorer tagging governance, Kubecost chargeback, and reserved instance strategy (78%+ RI adoption). Built auto-scaling policies (HPA + custom metrics) and right-sizing automation that runs weekly without manual intervention. **Result**: $3M+ annual cloud spend optimized; FY2026 trajectory forecast accurate within 2% — cost discipline I personally presented to Director/VP level stakeholders in quarterly business reviews.

---

## Why Amazon AWS (L7 Principal/Director SRE)

I have built and operated the infrastructure that AWS sells at scale. Running 25M notifications/day means I know what SNS customers need when message ordering breaks under load. It means I understand the DLQ behavior customers misread at 3 AM and the throughput limits that catch SQS users off guard at peak. I have been on both sides of that trust relationship — as the platform operator and as the person accountable when a P1 impacts 50M customers.

Amazon's Customer Obsession is not an interview phrase in my vocabulary — it is the forcing function behind every architecture decision I have made. When I adopted IRSA to eliminate static secrets, the driver was not compliance theater: it was eliminating the blast radius that would wake up a customer. When I built the anomaly detection layer in Splunk MLTK, the driver was MTTD — because every minute of undetected degradation is a minute a customer is silently failing.

At L7, the job is to own the reliability charter for a platform that other engineers, other teams, and millions of downstream customers depend on. I have done that at T-Mobile for three years with 36 months of zero Sev1 and a direct report org that can ship, operate, and reason about tradeoffs independently. I want to bring that same ownership posture — and the earned instincts from operating a messaging platform at scale — to AWS.
