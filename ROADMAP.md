# SRE Training Program — Master Roadmap

**Who this is for**: Vishweshwar Chippa — Principal SRE targeting Director/VP of Operations.  
**How to use**: Work phases in order. Infrastructure (5) and Leadership (7) tracks run in parallel with any phase.  
**Don't know where to start?** → [`1-phase-foundations/1.0-vocabulary/1.0.0-sre-mini-cookbook.md`](1-phase-foundations/1.0-vocabulary/1.0.0-sre-mini-cookbook.md)

---

## Folder Structure

```
Training/
├── 1-phase-foundations/         Phase 1: weeks 1–10 labs + vocabulary (1.0–1.11)
├── 2-phase-sre-practitioner/    Phase 2: SRE Core + Platform Engineering (2.0–2.6)
├── 3-phase-principal-sre/       Phase 3: Platform depth + Architecture + Capstone (3.1–3.6)
├── 4-phase-director/            Phase 4: Director Operating System + Strategy (4.1–4.5)
├── 5-track-infrastructure/      Parallel: VMware, Network, DB, Storage, Datacentre (5.1–5.7)
├── 6-track-technical-sre/       Parallel: FinOps, Zero Trust, SIEM, On-Call, Capacity (6.1–6.5)
├── 7-track-leadership-advanced/ Parallel: Board Comms, OKRs, Change Mgmt, Labor Law (7.1–7.4)
├── 00-program/                  Admin: training plan, glossary, progress log, resource library
├── job-search/                  Application tracker + company research
└── learning-path/               Curriculum navigation files
```

**File numbering scheme**: `{phase}.{topic}.{file}` — e.g., `2.1.3-triage-and-severity.md` = Phase 2, Topic 1 (Incident Mgmt), File 3. Subfolders use `.p` (playbook), `.t` (templates), `.r` (reference).

---

## Phase 1: SRE Foundations
**Goal**: Dev Lead → SRE Practitioner | **Duration**: 8 weeks | **Effort**: ~160h

### 1.0 Vocabulary (read before Week 1)
- [ ] SRE Mini Cookbook (~4h) → [`1-phase-foundations/1.0-vocabulary/1.0.0-sre-mini-cookbook.md`](1-phase-foundations/1.0-vocabulary/1.0.0-sre-mini-cookbook.md)

### Weekly Labs
| | # | Topic | Link | Est. |
|--|--|-------|------|------|
| - [ ] | 1.1 | Terraform & IaC | [`1-phase-foundations/1.1-terraform-iac/`](1-phase-foundations/1.1-terraform-iac/) | 16h |
| - [ ] | 1.2 | DevSecOps | [`1-phase-foundations/1.2-devsecops/`](1-phase-foundations/1.2-devsecops/) | 16h |
| - [ ] | 1.3 | Kubernetes | [`1-phase-foundations/1.3-kubernetes/`](1-phase-foundations/1.3-kubernetes/) | 16h |
| - [ ] | 1.4 | AWS + GitOps | [`1-phase-foundations/1.4-aws-gitops/`](1-phase-foundations/1.4-aws-gitops/) | 16h |
| - [ ] | 1.5 | Observability | [`1-phase-foundations/1.5-observability/`](1-phase-foundations/1.5-observability/) | 16h |
| - [ ] | 1.6 | Platform Engineering Lab | [`1-phase-foundations/1.6-platform-engineering-lab/`](1-phase-foundations/1.6-platform-engineering-lab/) | 16h |
| - [ ] | 1.7 | Interview Readiness | [`1-phase-foundations/1.7-interview-readiness/`](1-phase-foundations/1.7-interview-readiness/) | 16h |
| - [ ] | 1.8 | Certification | [`1-phase-foundations/1.8-certification/`](1-phase-foundations/1.8-certification/) | 16h |

### AI Track (runs in parallel with Labs 1.5–1.8)
| | # | Topic | Link | Est. |
|--|--|-------|------|------|
| - [ ] | 1.9 | AI Fundamentals | [`1-phase-foundations/1.9-ai-fundamentals/`](1-phase-foundations/1.9-ai-fundamentals/) | 16h |
| - [ ] | 1.10 | AI in Production | [`1-phase-foundations/1.10-ai-production/`](1-phase-foundations/1.10-ai-production/) | 16h |

### Progress Tracker
- Weekly check-in files → [`1-phase-foundations/1.11-weekly-tracker/`](1-phase-foundations/1.11-weekly-tracker/)

---

## Phase 2: SRE Practitioner
**Goal**: SRE → Senior SRE | **Duration**: 12 weeks | **Effort**: ~50h

### 2.0 Metrics Foundation (read alongside frameworks)
- [ ] SRE Metrics Textbook (~8h) → [`2-phase-sre-practitioner/2.0-metrics-foundation/`](2-phase-sre-practitioner/2.0-metrics-foundation/)

### SRE Core Frameworks
| | # | Framework | Problem It Solves | Link | Est. |
|--|--|-----------|-------------------|------|------|
| - [ ] | 2.1 | Incident Management | Structured response — command hierarchy, comms, escalation | [`2-phase-sre-practitioner/2.1-incident-management/2.1.0-README.md`](2-phase-sre-practitioner/2.1-incident-management/2.1.0-README.md) | 8h |
| - [ ] | 2.2 | Problem Management | Preventing recurrence — postmortem to permanent fix | [`2-phase-sre-practitioner/2.2-problem-management/2.2.0-README.md`](2-phase-sre-practitioner/2.2-problem-management/2.2.0-README.md) | 4h |
| - [ ] | 2.3 | Service Level Management | Defining, measuring, governing reliability contracts | [`2-phase-sre-practitioner/2.3-service-level-management/2.3.0-README.md`](2-phase-sre-practitioner/2.3-service-level-management/2.3.0-README.md) | 6h |
| - [ ] | 2.4 | Availability & Continuity Management | Designing for failure — HA, DR, continuity at scale | [`2-phase-sre-practitioner/2.4-availability-continuity-management/2.4.0-README.md`](2-phase-sre-practitioner/2.4-availability-continuity-management/2.4.0-README.md) | 6h |

### Platform Engineering Foundations
| | # | Framework | Problem It Solves | Link | Est. |
|--|--|-----------|-------------------|------|------|
| - [ ] | 2.5 | Change & Release Management | Controlling change risk without slowing delivery | [`2-phase-sre-practitioner/2.5-change-release-management/2.5.0-README.md`](2-phase-sre-practitioner/2.5-change-release-management/2.5.0-README.md) | 5h |
| - [ ] | 2.6 | Environment Management | Eliminating environment drift — dev, staging, prod parity | [`2-phase-sre-practitioner/2.6-environment-management/2.6.0-README.md`](2-phase-sre-practitioner/2.6-environment-management/2.6.0-README.md) | 6h |

---

## Phase 3: Principal SRE
**Goal**: Senior SRE → Principal SRE | **Duration**: 12 weeks | **Effort**: ~50h

### Platform Engineering (continued)
| | # | Framework | Problem It Solves | Link | Est. |
|--|--|-----------|-------------------|------|------|
| - [ ] | 3.1 | Performance Engineering | Proactive capacity and latency management | [`3-phase-principal-sre/3.1-performance-engineering/3.1.0-README.md`](3-phase-principal-sre/3.1-performance-engineering/3.1.0-README.md) | 6h |
| - [ ] | 3.2 | Application Layer Taxonomy | Classifying apps to apply the right reliability pattern | [`3-phase-principal-sre/3.2-application-layer-taxonomy/3.2.0-README.md`](3-phase-principal-sre/3.2-application-layer-taxonomy/3.2.0-README.md) | 5h |

### Director-Level Frameworks (Principal introduction)
| | # | Framework | Problem It Solves | Link | Est. |
|--|--|-----------|-------------------|------|------|
| - [ ] | 3.3 | Architecture & Governance | Principles and review mechanisms so architecture doesn't drift | [`3-phase-principal-sre/3.3-architecture-principles-governance/3.3.0-README.md`](3-phase-principal-sre/3.3-architecture-principles-governance/3.3.0-README.md) | 6h |
| - [ ] | 3.4 | Application Portfolio Transformation | Managing a fleet — modernize, sustain, or retire | [`3-phase-principal-sre/3.4-application-portfolio-transformation/3.4.0-README.md`](3-phase-principal-sre/3.4-application-portfolio-transformation/3.4.0-README.md) | 6h |

### Applied Practice
- [ ] Capstone exercises and scenarios → [`3-phase-principal-sre/3.5-capstone/3.5.0-README.md`](3-phase-principal-sre/3.5-capstone/3.5.0-README.md)
- [ ] Portfolio projects (3 production-grade tools) → [`3-phase-principal-sre/3.6-portfolio/`](3-phase-principal-sre/3.6-portfolio/)

---

## Phase 4: Director of Operations
**Goal**: Principal SRE → Director/VP | **Duration**: Ongoing | **Effort**: ~80h

### Director Operating System
| | # | Framework | Problem It Solves | Link | Est. |
|--|--|-----------|-------------------|------|------|
| - [ ] | 4.1 | Director Management Course | Running an ops org — 1:1s, planning, performance, executive presence | [`4-phase-director/4.1-director-management-course/4.1.0-README.md`](4-phase-director/4.1-director-management-course/4.1.0-README.md) | 20h |
| - [ ] | 4.2 | Director Operations Manual | Weekly rhythms, OKR cadence, reporting, stakeholder management | [`4-phase-director/4.2-director-operations-manual/4.2.0-README.md`](4-phase-director/4.2-director-operations-manual/4.2.0-README.md) | 10h |
| - [ ] | 4.3 | Operations Team Roles | Org design — structure, level, and staff an ops team | [`4-phase-director/4.3-operations-team-roles/4.3.0-README.md`](4-phase-director/4.3-operations-team-roles/4.3.0-README.md) | 8h |

### Strategic Frameworks
| | # | Framework | Problem It Solves | Link | Est. |
|--|--|-----------|-------------------|------|------|
| - [ ] | 4.4 | Build vs. Buy | When to build vs. procure — with governance and TCO analysis | [`4-phase-director/4.4-build-vs-buy/4.4.0-README.md`](4-phase-director/4.4-build-vs-buy/4.4.0-README.md) | 6h |
| - [ ] | 4.5 | Migration Projects | Large-scale migrations — planning, execution, cutover, risk | [`4-phase-director/4.5-migration-projects/4.5.0-README.md`](4-phase-director/4.5-migration-projects/4.5.0-README.md) | 8h |

---

## Track 5: Infrastructure Fluency
**When**: Parallel with any phase. P1 = before Director interviews. P2 = before VP interviews.

| | # | Topic | Link | Priority | Est. |
|--|--|-------|------|----------|------|
| - [ ] | 5.1 | Virtualization & VMware | [`5-track-infrastructure/5.1-virtualization-vmware/5.1.0-README.md`](5-track-infrastructure/5.1-virtualization-vmware/5.1.0-README.md) | P1 | 16h |
| - [ ] | 5.2 | Service Mesh | [`5-track-infrastructure/5.2-service-mesh/5.2.0-README.md`](5-track-infrastructure/5.2-service-mesh/5.2.0-README.md) | P1 | 12h |
| - [ ] | 5.3 | Network Operations | [`5-track-infrastructure/5.3-network-operations/5.3.0-README.md`](5-track-infrastructure/5.3-network-operations/5.3.0-README.md) | P1 | 16h |
| - [ ] | 5.4 | Database Reliability | [`5-track-infrastructure/5.4-database-reliability/5.4.0-README.md`](5-track-infrastructure/5.4-database-reliability/5.4.0-README.md) | P1 | 16h |
| - [ ] | 5.5 | Datacenter Operations | [`5-track-infrastructure/5.5-datacenter-operations/5.5.0-README.md`](5-track-infrastructure/5.5-datacenter-operations/5.5.0-README.md) | P1 | 12h |
| - [ ] | 5.6 | Bare Metal Management | [`5-track-infrastructure/5.6-bare-metal-management/5.6.0-README.md`](5-track-infrastructure/5.6-bare-metal-management/5.6.0-README.md) | P2 | 8h |
| - [ ] | 5.7 | Storage Architecture | [`5-track-infrastructure/5.7-storage-architecture/5.7.0-README.md`](5-track-infrastructure/5.7-storage-architecture/5.7.0-README.md) | P2 | 8h |

---

## Track 6: Technical SRE Depth
**When**: Phase 3–4. P1 = before Principal or Director interviews.

| | # | Topic | Link | Priority | Est. |
|--|--|-------|------|----------|------|
| - [ ] | 6.1 | FinOps for SRE | [`6-track-technical-sre/6.1-finops/6.1.0-README.md`](6-track-technical-sre/6.1-finops/6.1.0-README.md) | P1 | 12h |
| - [ ] | 6.2 | Zero Trust Security | [`6-track-technical-sre/6.2-zero-trust-security/6.2.0-README.md`](6-track-technical-sre/6.2-zero-trust-security/6.2.0-README.md) | P1 | 16h |
| - [ ] | 6.3 | SIEM/SOC Integration | [`6-track-technical-sre/6.3-siem-soc-integration/6.3.0-README.md`](6-track-technical-sre/6.3-siem-soc-integration/6.3.0-README.md) | P1 | 10h |
| - [ ] | 6.4 | On-Call Program Design | [`6-track-technical-sre/6.4-on-call-program-design/6.4.0-README.md`](6-track-technical-sre/6.4-on-call-program-design/6.4.0-README.md) | P1 | 12h |
| - [ ] | 6.5 | Capacity Planning | [`6-track-technical-sre/6.5-capacity-planning/6.5.0-README.md`](6-track-technical-sre/6.5-capacity-planning/6.5.0-README.md) | P1 | 10h |

---

## Track 7: Leadership Advanced
**When**: Phase 4 and alongside Director interview prep.

| | # | Topic | Link | Priority | Est. |
|--|--|-------|------|----------|------|
| - [ ] | 7.1 | Board & Executive Communications | [`7-track-leadership-advanced/7.1-board-communications/7.1.0-README.md`](7-track-leadership-advanced/7.1-board-communications/7.1.0-README.md) | P1 | 8h |
| - [ ] | 7.2 | OKR Design & Governance | [`7-track-leadership-advanced/7.2-okr-design/7.2.0-README.md`](7-track-leadership-advanced/7.2-okr-design/7.2.0-README.md) | P1 | 8h |
| - [ ] | 7.3 | Organizational Change Management | [`7-track-leadership-advanced/7.3-organizational-change-management/7.3.0-README.md`](7-track-leadership-advanced/7.3-organizational-change-management/7.3.0-README.md) | P1 | 10h |
| - [ ] | 7.4 | Labor Law for Managers | [`7-track-leadership-advanced/7.4-labor-law-for-managers/7.4.0-README.md`](7-track-leadership-advanced/7.4-labor-law-for-managers/7.4.0-README.md) | P1 | 6h |

---

## Program Summary

| # | Phase / Track | Duration | Effort | Content |
|---|---------------|----------|--------|---------|
| 1 | SRE Foundations | 8 weeks | 160h | 10 labs + AI track + vocab |
| 2 | SRE Practitioner | 12 weeks | ~50h | 6 frameworks |
| 3 | Principal SRE | 12 weeks | ~50h | 4 frameworks + capstone |
| 4 | Director of Operations | Ongoing | ~80h | 5 frameworks |
| 5 | Infrastructure Fluency | Parallel | ~88h | 7 frameworks |
| 6 | Technical SRE Depth | Parallel | ~60h | 5 frameworks |
| 7 | Leadership Advanced | Parallel | ~40h | 4 frameworks |
| **Total** | | **~32 weeks** | **~528h** | **41 frameworks + 10 labs** |

---

## Quick Reference — Operational Documents

Most-reached-for documents when doing real work.

| Document | Path |
|----------|------|
| Incident Command Playbook | [`2-phase-sre-practitioner/2.1-incident-management/playbook/2.1.p3-incident-command-playbook.md`](2-phase-sre-practitioner/2.1-incident-management/playbook/2.1.p3-incident-command-playbook.md) |
| Postmortem Playbook | [`2-phase-sre-practitioner/2.1-incident-management/playbook/2.1.p5-postmortem-playbook.md`](2-phase-sre-practitioner/2.1-incident-management/playbook/2.1.p5-postmortem-playbook.md) |
| SLO Definition Template | [`2-phase-sre-practitioner/2.3-service-level-management/templates/2.3.t4-slo-definition-template.md`](2-phase-sre-practitioner/2.3-service-level-management/templates/2.3.t4-slo-definition-template.md) |
| Change Risk Assessment Template | [`2-phase-sre-practitioner/2.5-change-release-management/templates/2.5.t1-change-risk-assessment-template.md`](2-phase-sre-practitioner/2.5-change-release-management/templates/2.5.t1-change-risk-assessment-template.md) |
| On-Call Program Audit Playbook | [`6-track-technical-sre/6.4-on-call-program-design/playbook/6.4.p2-on-call-program-audit-playbook.md`](6-track-technical-sre/6.4-on-call-program-design/playbook/6.4.p2-on-call-program-audit-playbook.md) |
| Director Weekly VP Status Template | [`4-phase-director/4.1-director-management-course/templates/4.1.t4-weekly-vp-status-template.md`](4-phase-director/4.1-director-management-course/templates/4.1.t4-weekly-vp-status-template.md) |
| Migration Cutover Checklist | [`4-phase-director/4.5-migration-projects/templates/4.5.t3-migration-cutover-checklist-template.md`](4-phase-director/4.5-migration-projects/templates/4.5.t3-migration-cutover-checklist-template.md) |
| Build vs. Buy Decision Template | [`4-phase-director/4.4-build-vs-buy/templates/4.4.t1-build-vs-buy-decision-template.md`](4-phase-director/4.4-build-vs-buy/templates/4.4.t1-build-vs-buy-decision-template.md) |
| SRE Metrics Cheatsheet | [`2-phase-sre-practitioner/2.0-metrics-foundation/reference/2.0.r1-all-25-terms-formulae-cheatsheet.md`](2-phase-sre-practitioner/2.0-metrics-foundation/reference/2.0.r1-all-25-terms-formulae-cheatsheet.md) |
