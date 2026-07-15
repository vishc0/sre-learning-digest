# Phase 2: SRE Practitioner

**Duration**: 12 weeks  
**Entry point**: Junior/Mid SRE with on-call experience  
**Exit**: Can IC P2 incidents, write RCAs, define and monitor SLOs, participate in CAB, and own a problem record end-to-end

---

## What Phase 2 Builds

Phase 2 is where operational discipline is built. Phase 1 gave you observability and survival skills. Phase 2 gives you the frameworks that structure professional SRE work: how incidents are managed, how problems are tracked to root cause, how service levels are defined and measured, how changes are reviewed and released safely, and how environments are controlled.

By the end of Phase 2 you are not just responding to production — you are running it with intent. You have a framework for every major operational event, and you can articulate your reasoning in those frameworks to peers, managers, and stakeholders.

---

## Prerequisites

Before starting Phase 2, you should have:

- Phase 1 competency gates fully met, OR
- 2+ years of SRE experience in an on-call rotation
- Has participated in at least one P1 incident (not necessarily as IC — as a responder is sufficient)
- Has contributed to at least one postmortem document
- Comfortable with Kubernetes `kubectl` operations and basic observability tooling

---

## Reading Strategy for Phase 2

Each domain framework follows the same structure: chapters, then playbooks, then templates. Read in that order.

- **Chapters** give you the conceptual framework and decision logic
- **Playbooks** give you the step-by-step operational procedures
- **Templates** give you the artifacts you will produce (incident records, problem records, RFC documents)

Do not skip to the playbooks. The chapters are why the playbooks are written the way they are. Understanding the why means you can adapt the playbook to situations it does not explicitly cover.

---

## Week-by-Week Curriculum

### Weeks 1–3: Incident Management

**Framework**: `2-phase-sre-practitioner/2.1-incident-management/` — read all 10 chapters, then all playbooks

This is the most operationally immediate framework. Everything you do in an incident — how you declare severity, who you page, what you communicate, when you escalate, how you close — is covered here.

Read sequence:
1. `ch01` through `ch10` — read in order, do not skip chapters
2. `playbook/` — all playbooks in the folder
3. `templates/` — review all templates so you know what artifacts to produce
4. `references/` — as needed reference during actual incidents

**Textbook integration**: While reading incident-management chapters, also read:  
`2-phase-sre-practitioner/2.0-metrics-foundation/2.0.3-blast-radius-bri-cc-fli-dsa.md`

This chapter covers BRI (Blast Radius Index), CC (Call Complexity), and FLI (Fault Localization Index) — the quantitative layer that sits underneath your incident severity decisions. When you are deciding whether to page a director or call an all-hands, BRI gives you the number that justifies the decision.

**Cookbook pairing**:  
`1-phase-foundations/1.0-vocabulary/1.0.3-incident-management.md`

Read this before starting the framework chapters. It gives you the vocabulary map — the difference between MTTD, MTTR, MTTF, and MTBF, and why each one matters differently.

---

### Weeks 4–5: Problem Management

**Framework**: `2-phase-sre-practitioner/2.2-problem-management/` — all 8 chapters, then playbooks, then templates

If incident management is about stopping the bleeding, problem management is about not bleeding again. This framework covers root cause analysis, problem record lifecycle, known error management, and the process of driving a systemic fix from a pattern of incidents.

Key concepts this block:
- The difference between an incident and a problem (incidents are symptoms; problems are causes)
- Five Whys and fault tree analysis — when to use each, what each misses
- Known error database: how to manage issues you know about but have not yet fixed
- Problem closure criteria: what it means to actually solve a problem vs. closing a ticket

**Cookbook pairing**:  
`1-phase-foundations/1.0-vocabulary/1.0.3-incident-management.md` (postmortem section specifically)

---

### Weeks 6–7: Service Level Management

**Framework**: `2-phase-sre-practitioner/2.3-service-level-management/` — all 8 chapters, then playbooks, then templates

Service level management is the frame around which everything else in SRE is built. Your SLOs define what reliability means for your service. Your error budget determines how much operational risk you can carry. This framework takes you from "we should probably have SLOs" to "here is our complete SLM program."

Key concepts this block:
- SLI selection: what to measure, what not to measure, why availability alone is insufficient
- SLO setting: how to set a target that is both meaningful and achievable
- Error budget: what it is, how it burns, what happens when it is exhausted
- SLO review cadence: how frequently to review, what triggers a revision
- Reporting to stakeholders: how to communicate service health in terms non-engineers understand

**Textbook integration**: Read in parallel with this block:  
`2-phase-sre-practitioner/2.0-metrics-foundation/2.0.4-health-signals-ebv-apr-mtbi-ocr.md`

This chapter covers EBV (Error Budget Velocity), MTBI (Mean Time Between Incidents), and OCR (On-Call Rate) — the metrics that sit behind your SLO program and make "we are burning error budget faster than expected" into a quantifiable statement.

**Cookbook pairing**:  
`1-phase-foundations/1.0-vocabulary/1.0.2-sli-slo-error-budgets.md`

Read this first. It is the clearest possible explanation of SLO mechanics before you encounter the full framework's operational depth.

---

### Weeks 8–9: Availability and Continuity Management

**Framework**: `2-phase-sre-practitioner/2.4-availability-continuity-management/` — all 8 chapters (note: framework has 9 chapters, read all), then playbooks

This framework covers two related but distinct disciplines: availability engineering (keeping systems up) and continuity planning (getting systems back up when they fail at scale). Think of it as the difference between daily reliability work and disaster recovery.

Key concepts this block:
- Availability architecture patterns: redundancy, failover, geographic distribution
- Single point of failure identification and remediation
- Recovery objectives: RTO (Recovery Time Objective) and RPO (Recovery Point Objective) — how to define and test them
- Business continuity planning: what SREs own in a major outage vs. what the business owns
- Runbook design for continuity scenarios (different from incident runbooks)

---

### Week 10: Change and Release Management

**Framework**: `2-phase-sre-practitioner/2.5-change-release-management/` — all 8 chapters, then playbooks

Change management is the operational control that prevents accidental production failures. Every significant production modification — code deploy, configuration change, infrastructure change — should pass through a defined change process. This framework defines that process.

Key concepts this week:
- Change types: standard, normal, emergency — the risk profile and approval requirements for each
- CAB (Change Advisory Board): what it is, what it reviews, how to prepare an RFC for it
- Risk assessment: how to score a change's risk and present it to CAB
- Freeze windows and moratoriums: why they exist, how to navigate them
- Change failure rate: how to measure it and what it tells you about your change process

**Textbook integration**: Read in parallel:  
`2-phase-sre-practitioner/2.0-metrics-foundation/2.0.6-change-governance-metrics.md`

This chapter covers the quantitative layer of change governance — SCV (Single Change Volume), MRI (Mean Release Interval), CSD (Change Success Density), and related metrics. When you present at CAB, these are the numbers that make your risk assessment credible.

---

### Weeks 11–12: Environment Management

**Framework**: `2-phase-sre-practitioner/2.6-environment-management/` — all 8 chapters (note: framework has 10 chapters, read all), then playbooks

Environment management covers the discipline of keeping your non-production environments trustworthy, your production environment stable, and the promotion path between them controlled.

Key concepts this block:
- Environment taxonomy: dev, test, staging, pre-prod, prod — what each is for and what it is not for
- Environment drift: how environments diverge from each other and why it causes deployment failures
- Configuration management: what is environment-specific, what is universal, where secrets live
- Promotion gates: what must be true before code moves from staging to production
- Environment observability: monitoring non-production environments matters more than most teams think

**Cookbook pairing**:  
`1-phase-foundations/1.0-vocabulary/1.0.8-capacity-performance-cost.md`

Read this during or after Week 11. Environment management connects directly to capacity planning — how much headroom do you maintain, and in which environment, and why.

---

## Textbook Integration Summary

| Textbook Chapter | When to Read | What It Adds |
|-----------------|--------------|--------------|
| ch03 (BRI, CC, FLI, DSA) | Weeks 1–3 with incident-management | Quantifies incident severity and blast radius |
| ch04 (EBV, MTBI, OCR) | Weeks 6–7 with service-level-management | Quantifies error budget burn rate and on-call health |
| ch06 (SCV, MRI, CSD, RV) | Week 10 with change-release-management | Quantifies change risk and release velocity |
| ch09 (daily practice) | Weeks 1–12, ongoing | Live reference during incidents, CAB, postmortems |

Chapter 9 is not a chapter you read once — it is a reference you open during actual work. Keep it bookmarked.

---

## Phase 2 Competency Gates

You are ready for Phase 3 when you can do all of the following through demonstrated real-world practice, not just reading comprehension.

| Gate | What "done" looks like |
|------|----------------------|
| Incident Command (P2) | Can IC a P2 incident independently — declare severity, assemble the response team, run the bridge, make escalation decisions, and close the incident |
| Blameless Postmortem | Can facilitate a postmortem meeting that produces contributing factors and action items without devolving into blame or blame-adjacent language |
| SLO Dashboard | Can create and monitor an SLO dashboard that shows current burn rate, budget remaining, and alert thresholds |
| Problem Management | Can write a problem record, assign it correctly, track the root cause investigation, and drive it to closure with a verified fix |
| CAB Participation | Can review an RFC, articulate the risk level in terms that make sense to both technical and non-technical CAB members, and ask the questions that reveal hidden risk |
| DORA Reporting | Can measure and report DORA metrics for a team — not just know what they are, but produce the numbers |
| BRI Application | Can apply BRI scoring during a triage decision — take an incident's blast radius and use it to justify a severity level or escalation decision |

---

## What Phase 2 Does Not Cover

Phase 2 deliberately omits:
- Performance engineering at the system design level (that is Phase 3)
- Architecture review and governance (that is Phase 3)
- Application portfolio management (that is Phase 3)
- Executive communication and reporting (that is Phase 3–4)
- People management and org design (that is Phase 4)

You will feel operational in Phase 2 — and you will be. But operational execution without design thinking is a ceiling. Phase 3 removes that ceiling.
