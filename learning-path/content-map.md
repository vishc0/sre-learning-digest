# Content Map — All Training Materials by Phase and Layer

Use this map to find any piece of content by topic, phase, or audience. Every major file and folder in the Training library is mapped here. If you know what you want to learn, find it in the navigation table at the top of README.md. If you want to see everything available in a given phase, find your phase section below.

---

## Layer 1: Understand (Vocabulary, Concepts, Interview Prep)

### Source: 1-phase-foundations/1.0-vocabulary/

| File | Phase | Primary Audience | What It Covers |
|------|-------|-----------------|----------------|
| 1.0.0-sre-mini-cookbook.md | Phase 1–2 | Junior/Mid SRE | Compressed SRE vocabulary reference; use as a quick-reference dictionary |
| 1.0.1-reliability-foundations.md | Phase 1 | Junior SRE | What reliability means, why it matters, SRE vs. DevOps, core SRE concepts |
| 1.0.2-sli-slo-error-budgets.md | Phase 2 | Mid SRE | SLI/SLO/SLA mechanics, error budget calculation, error budget policies |
| 1.0.3-incident-management.md | Phase 2 | Mid SRE | Incident lifecycle, severity classification, IC role, MTTD/MTTR/MTBF |
| 1.0.4-observability-telemetry.md | Phase 1–2 | Junior/Mid SRE | Metrics/logs/traces, RED/USE/Four Golden Signals, alerting design |
| 1.0.5-distributed-systems-resilience.md | Phase 2–3 | Senior SRE | Failure modes, circuit breakers, bulkheads, retry patterns, chaos engineering |
| 1.0.6-kubernetes-platform-reliability.md | Phase 1 | Junior SRE | K8s reliability concepts, health probes, deployment strategies, EKS |
| 1.0.7-cicd-safe-release.md | Phase 1–2 | Junior/Mid SRE | CI/CD pipeline reliability, progressive delivery, feature flags, canary |
| 1.0.8-capacity-performance-cost.md | Phase 2–3 | Senior SRE | Capacity planning, performance budgets, cost allocation, right-sizing |
| 1.0.9-security-compliance-devsecops.md | Phase 1–2 | Junior/Mid SRE | Shift-left security, SAST/DAST, secrets management, compliance frameworks |
| 1.0.10-principal-leadership-communication.md | Phase 3–4 | Principal/Director | Executive communication, technical influence, cross-functional leadership |
| 1.0.11-ai-for-sre.md | Phase 3 | Principal SRE | AI tools in SRE practice, AIOps, where AI augments vs. where it falls short |
| 1.0.12-reliability-economics.md | Phase 3–4 | Principal/Director | Cost of unreliability, ROI framing for reliability investment, business case construction |
| 1.0.13-sre-enterprise-journey.md | Phase 2 | Mid SRE | How SRE programs grow in enterprise environments, organizational maturity |
| 1.0.14-enterprise-operational-realities.md | Phase 3 | Principal SRE | Enterprise-scale operational complexity, multi-team coordination, organizational friction |
| 1.0.15-interdisciplinary-sre-topics.md | Phase 3 | Principal SRE | SRE at the intersection of security, data, ML/AI systems, and compliance |
| 1.0.16-enterprise-architecture-patterns.md | Phase 3 | Principal SRE | Architecture patterns that appear in enterprise SRE: event-driven, saga, CQRS, strangler fig |
| 1.0.17-principal-sre-mastery-roadmap.md | Phase 2–3 | Mid-Principal SRE | Progression path from Senior to Principal SRE; competency model and development areas |

---

## Layer 2: Measure (Proprietary Reliability Metrics Framework)

### Source: 2-phase-sre-practitioner/2.0-metrics-foundation/

The textbook defines a proprietary reliability measurement framework. Each chapter introduces specific metrics; these are referenced throughout Phases 2–4. Chapter 9 is an ongoing daily-practice reference, not a one-time read.

| Chapter | Phase | Primary Audience | Metrics/Concepts Introduced |
|---------|-------|-----------------|---------------------------|
| 2.0.1-reliability-contract-and-gap.md | Phase 2 | Mid SRE | Reliability contract, gap analysis between promised and delivered reliability |
| 2.0.2-structural-terms-cd-scs-lbh.md | Phase 2–3 | Senior SRE | Call Depth (CD), SLO Coherence Score (SCS), Latency Budget Hierarchy (LBH) |
| 2.0.3-blast-radius-bri-cc-fli-dsa.md | Phase 2 | Mid SRE | Blast Radius Index (BRI), Call Complexity (CC), Fault Localization Index (FLI), Dependency Surface Area (DSA) |
| 2.0.4-health-signals-ebv-apr-mtbi-ocr.md | Phase 2–3 | Senior SRE | Error Budget Velocity (EBV), Alert Precision Rate (APR), Mean Time Between Incidents (MTBI), On-Call Rate (OCR) |
| 2.0.5-efficiency-terms-ol-rcr-taf.md | Phase 3 | Principal SRE | Operational Load (OL), Resource Consumption Rate (RCR), Traffic Amplification Factor (TAF) |
| 2.0.6-change-governance-metrics.md | Phase 2–3 | Senior SRE | Single Change Volume (SCV), Mean Release Interval (MRI), Change Success Density (CSD), Rollback Velocity (RV) |
| 2.0.7-lifecycle-terms.md | Phase 3 | Principal SRE | Application lifecycle scoring; portfolio-level reliability maturity assessment |
| 2.0.8-composite-scores-ris-srmi-jrcs.md | Phase 3–4 | Principal/Director | Reliability Index Score (RIS), System Reliability Maturity Index (SRMI), Journey Risk and Complexity Score (JRCS) |
| 2.0.9-daily-practice.md | Phase 2+ (ongoing) | All SRE levels | Live operational reference; use during incidents, CAB reviews, postmortems, and 1:1s |

---

## Layer 3: Operate (Domain Frameworks)

All domain frameworks follow the same structure: `ch01/`–`chXX/` (chapters) → `playbook/` → `templates/` → `references/`. Read chapters before playbooks; playbooks before templates.

### SRE Core Tier — Phase 2

These four frameworks are the operational foundation of professional SRE practice. Phase 2 is built on them.

| Framework | Phase | Primary Audience | Scope |
|-----------|-------|-----------------|-------|
| 2-phase-sre-practitioner/2.1-incident-management/ | Phase 2 | Mid-Senior SRE | Incident lifecycle, IC role, severity classification, escalation, closure; 10 chapters |
| 2-phase-sre-practitioner/2.2-problem-management/ | Phase 2 | Mid-Senior SRE | RCA methodology, problem records, known error management, problem closure; 8 chapters |
| 2-phase-sre-practitioner/2.3-service-level-management/ | Phase 2 | Senior SRE | SLI/SLO design, error budget policy, SLO monitoring, stakeholder reporting; 8 chapters |
| 2-phase-sre-practitioner/2.4-availability-continuity-management/ | Phase 2–3 | Senior SRE | Availability architecture, SPOF remediation, RTO/RPO definition, BCP; 9 chapters |

### Platform Engineering Tier — Phase 2–3

These frameworks cover the disciplines that ensure systems are built and released reliably.

| Framework | Phase | Primary Audience | Scope |
|-----------|-------|-----------------|-------|
| 2-phase-sre-practitioner/2.5-change-release-management/ | Phase 2–3 | Senior SRE | Change types, RFC process, CAB, emergency change, change failure rate; 8 chapters |
| 2-phase-sre-practitioner/2.6-environment-management/ | Phase 2–3 | Senior/Principal SRE | Environment taxonomy, drift prevention, promotion gates, configuration management; 10 chapters |
| 3-phase-principal-sre/3.1-performance-engineering/ | Phase 3 | Principal SRE | Performance modeling, load testing, JVM tuning, latency analysis, capacity planning; 8 chapters |
| 3-phase-principal-sre/3.2-application-layer-taxonomy/ | Phase 3 | Principal SRE | Application architecture patterns, dependency mapping, API contract analysis, data layer; 8 chapters |

### Director/Leadership Tier — Phase 3–4

These frameworks cover strategic and organizational leadership for operations.

| Framework | Phase | Primary Audience | Scope |
|-----------|-------|-----------------|-------|
| 3-phase-principal-sre/3.3-architecture-principles-governance/ | Phase 3–4 | Principal/Director | Architecture principles, ARB, ADR, technical debt governance, reliability non-negotiables; 8 chapters |
| 3-phase-principal-sre/3.4-application-portfolio-transformation/ | Phase 4 | Director | Portfolio scoring, modernization patterns, dependency sequencing, risk stratification; 8 chapters |
| 4-phase-director/4.1-director-management-course/ | Phase 4 | Director | 10 modules covering the complete Director operating model; playbooks and templates included |
| 4-phase-director/4.2-director-operations-manual/ | Phase 4 | Director | Chapter-level director operating reference; 8 chapters covering job definition through 90-day plan |
| 4-phase-director/4.3-operations-team-roles/ | Phase 4 | Director | Team structure, role definitions, hiring framework, performance management for ops teams; 8 chapters |

### Director Management Course — Module Detail

| Module | Phase | Topic |
|--------|-------|-------|
| 4.1.1-directors-role.md | Phase 4 | Role boundaries, accountability vs. responsibility, what Directors own |
| 4.1.2-executive-communication.md | Phase 4 | Communicating up/across/down, risk framing, the 15-minute executive briefing |
| 4.1.3-budgeting-and-financial-management.md | Phase 4 | Budget ownership, headcount business case, cost center management |
| 4.1.4-managing-senior-managers.md | Phase 4 | Manager-of-managers dynamics, delegation, accountability without micromanagement |
| 4.1.5-org-design-and-people-strategy.md | Phase 4 | Team topologies, span of control, org design for operational effectiveness |
| 4.1.6-vendor-management.md | Phase 4 | Vendor accountability, QBR structure, escalation, evaluation criteria |
| 4.1.7-partnership-management.md | Phase 4 | Internal and external partner relationships, negotiated commitments, mutual accountability |
| 4.1.8-governance-risk-and-compliance.md | Phase 4 | Audit engagement, risk committee participation, compliance without friction |
| 4.1.9-people-leadership-and-culture.md | Phase 4 | Culture design, psychological safety, accountability culture |
| 4.1.10-directors-complete-operating-system.md | Phase 4 | Integration of all modules into a unified operating model |

---

## Structured Curriculum (Hands-on Labs)

### Source: 1-phase-foundations/

All weeks are Phase 1 content. They are the hands-on operational counterpart to the Phase 1 cookbook reading.

| Week | Content Directory | Phase | What It Covers |
|------|------------------|-------|----------------|
| Week 1 | 1-phase-foundations/1.1-terraform-iac/ | Phase 1 | Terraform state management, modules, remote backend (S3/DynamoDB), drift detection, IaC security |
| Week 2 | 1-phase-foundations/1.2-devsecops/ | Phase 1 | Security scanning, pipeline security, shift-left, DevSecOps toolchain |
| Week 3 | 1-phase-foundations/1.3-kubernetes/ | Phase 1 | K8s fundamentals, pod lifecycle, deployments, kubectl operations, EKS |
| Week 4 | 1-phase-foundations/1.4-aws-gitops/ | Phase 1 | AWS core services — EC2, EKS, S3, VPC, IAM, CloudWatch |
| Week 5 | 1-phase-foundations/1.5-observability/ | Phase 1 | Observability tooling — Splunk, Datadog, metrics, logs, traces, alerting |
| Week 6 | 1-phase-foundations/1.6-platform-engineering-lab/ | Phase 1 | Backstage, IDP concepts, DORA metrics, self-service engineering |
| Week 7 | 1-phase-foundations/1.7-interview-readiness/ | Phase 1–2 | Chaos engineering, fault injection, game days, resilience testing |
| Week 8 | 1-phase-foundations/1.8-certification/ | Phase 1→2 | Certification prep, capstone exercise, Phase 1 exit assessment |

---

## Capstone and Scenarios

### Source: 3-phase-principal-sre/3.5-capstone/

| Content | Phase | What It Is |
|---------|-------|-----------|
| 3-phase-principal-sre/3.5-capstone/scenarios/ | Phase 2–3 | Scenario-based exercises requiring multi-framework application; used as Phase 3 capstone |
| 3-phase-principal-sre/3.5-capstone/reference/ | Phase 2+ (ongoing) | Reference documents for scenario context; remain useful throughout Phase 3–4 |

---

## Job Search and Interview Preparation

### Source: job-search/

| Content | Phase | What It Is |
|---------|-------|-----------|
| job-search/ | Phase 3–4 | Director-level interview prep, LinkedIn content, company research frameworks, behavioral question banks |

Run job-search content in parallel with Phase 3 and throughout Phase 4. The Director interview tests the operating model built in Phase 4 — preparation and study reinforce each other.

---

## Cross-Reference: Cookbook Topics to Domain Frameworks

Use this table to find the framework that operationalizes the concept you read about in the cookbook.

| Cookbook Topic | Corresponding Domain Framework |
|----------------|-------------------------------|
| Incident management vocabulary | 2-phase-sre-practitioner/2.1-incident-management/ |
| SLI/SLO/error budget mechanics | 2-phase-sre-practitioner/2.3-service-level-management/ |
| Postmortem and RCA | 2-phase-sre-practitioner/2.2-problem-management/ |
| Observability and telemetry | 1-phase-foundations/1.5-observability/ + 2-phase-sre-practitioner/2.0-metrics-foundation/2.0.4-health-signals-ebv-apr-mtbi-ocr.md |
| Distributed systems resilience | 2-phase-sre-practitioner/2.4-availability-continuity-management/ |
| Kubernetes reliability | 1-phase-foundations/1.3-kubernetes/ + 2-phase-sre-practitioner/2.6-environment-management/ |
| CI/CD and safe release | 2-phase-sre-practitioner/2.5-change-release-management/ |
| Capacity and performance | 3-phase-principal-sre/3.1-performance-engineering/ + 2-phase-sre-practitioner/2.0-metrics-foundation/2.0.5-efficiency-terms-ol-rcr-taf.md |
| Security and DevSecOps | 1-phase-foundations/1.2-devsecops/ |
| Principal leadership and communication | 4-phase-director/4.1-director-management-course/4.1.2-executive-communication.md |
| AI for SRE | Not yet mapped to a domain framework |
| Reliability economics | 4-phase-director/4.1-director-management-course/4.1.3-budgeting-and-financial-management.md + 2-phase-sre-practitioner/2.0-metrics-foundation/2.0.8-composite-scores-ris-srmi-jrcs.md |
| Enterprise architecture patterns | 3-phase-principal-sre/3.3-architecture-principles-governance/ + 3-phase-principal-sre/3.2-application-layer-taxonomy/ |

---

## Cross-Reference: Textbook Metrics to Operational Use Cases

| Metric | When You Use It | Which Framework It Supports |
|--------|----------------|----------------------------|
| BRI (Blast Radius Index) | During incident severity triage | 2-phase-sre-practitioner/2.1-incident-management/ |
| CC (Call Complexity) | When analyzing service dependency risk | 3-phase-principal-sre/3.2-application-layer-taxonomy/ |
| FLI (Fault Localization Index) | During postmortem scope-setting | 2-phase-sre-practitioner/2.2-problem-management/ |
| DSA (Dependency Surface Area) | During architecture review | 3-phase-principal-sre/3.3-architecture-principles-governance/ |
| EBV (Error Budget Velocity) | During SLO review and error budget governance | 2-phase-sre-practitioner/2.3-service-level-management/ |
| APR (Alert Precision Rate) | When auditing alerting quality | 2-phase-sre-practitioner/2.1-incident-management/ |
| MTBI (Mean Time Between Incidents) | During reliability trend reporting | 2-phase-sre-practitioner/2.3-service-level-management/ |
| OCR (On-Call Rate) | During on-call health review | 4-phase-director/4.3-operations-team-roles/ |
| OL (Operational Load) | During capacity planning | 3-phase-principal-sre/3.1-performance-engineering/ |
| RCR (Resource Consumption Rate) | During cost and capacity review | 3-phase-principal-sre/3.1-performance-engineering/ |
| TAF (Traffic Amplification Factor) | During load test design | 3-phase-principal-sre/3.1-performance-engineering/ |
| SCV (Single Change Volume) | During CAB risk assessment | 2-phase-sre-practitioner/2.5-change-release-management/ |
| MRI (Mean Release Interval) | During DORA/delivery metrics reporting | 2-phase-sre-practitioner/2.5-change-release-management/ |
| CSD (Change Success Density) | During change process maturity review | 2-phase-sre-practitioner/2.5-change-release-management/ |
| RIS (Reliability Index Score) | During portfolio scoring | 3-phase-principal-sre/3.4-application-portfolio-transformation/ |
| SRMI (System Reliability Maturity Index) | During org-level reliability maturity review | 3-phase-principal-sre/3.4-application-portfolio-transformation/ |
| JRCS (Journey Risk and Complexity Score) | During transformation prioritization | 3-phase-principal-sre/3.4-application-portfolio-transformation/ |
