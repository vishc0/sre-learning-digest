# Phase 3: Principal SRE

**Duration**: 12 weeks  
**Entry point**: Senior SRE with 4+ years of SRE experience  
**Exit**: Can design reliability programs, lead architecture reviews, define SRE standards for an org, coach junior SREs, and present technical risk to VP-level audiences

---

## What Phase 3 Builds

Phase 3 is the shift from operational executor to operational designer. In Phase 2 you learned to run the frameworks. In Phase 3 you learn to build them, evaluate them, and defend them at the architectural and executive level.

The Principal SRE role is different from Senior SRE in one critical dimension: scope. A Senior SRE owns a service or a team's reliability. A Principal SRE owns a program — a set of standards, practices, and architectural decisions that other teams follow. That requires a different set of skills: systems thinking, architectural reasoning, cross-functional influence, and the ability to communicate technical risk to people who do not share your technical vocabulary.

Phase 3 builds all of that.

---

## Prerequisites

Before starting Phase 3, you should have:

- Phase 2 competency gates fully met, OR equivalent experience that covers all Phase 2 competency gates
- Has served as Incident Commander for at least one P1 incident
- Has designed at least one SLO program for a service or team (not just written an SLO — designed the program: SLIs selected, target justified, error budget policy defined, alerting configured)
- Has participated in architectural discussions — ARB, tech review, or equivalent
- Is comfortable reading and writing ADRs (Architecture Decision Records)

If you have not IC'd a P1 incident, do not start Phase 3 yet. P1 IC experience is not a reading exercise — it is the operational context that makes Phase 3 frameworks legible.

---

## Reading Strategy for Phase 3

Phase 3 frameworks are more interconnected than Phase 2. Performance engineering connects to architecture governance. Application taxonomy connects to portfolio transformation. Read each framework fully before starting the next, but expect cross-references and build on them.

The textbook becomes critical in Phase 3. The measurement framework (RIS, SRMI, JRCS) gives you the executive-communication layer that Principal SREs need to influence at the VP level. Do not skip the textbook chapters listed below.

---

## Week-by-Week Curriculum

### Weeks 1–2: Performance Engineering

**Framework**: `3-phase-principal-sre/3.1-performance-engineering/` — all 8 chapters, then playbooks, then templates

Performance engineering is the discipline of understanding how a system behaves under load — before, during, and after scaling events. It is distinct from monitoring: monitoring tells you what happened; performance engineering tells you what will happen and what to change before it does.

Key concepts this block:
- Performance modeling: how to predict system behavior before running a load test
- Load testing design: what to test, how much load to apply, what success and failure look like
- JVM performance: heap sizing, garbage collection tuning, thread pool configuration — why SREs who work on Java systems need this
- Latency analysis: p50/p90/p99/p99.9 — why the tail matters more than the mean
- Bottleneck identification: CPU, memory, I/O, network — how to find where the constraint lives
- Capacity planning: how to model headroom requirements and avoid surprise saturation

**Textbook integration**: Read in parallel:  
`2-phase-sre-practitioner/2.0-metrics-foundation/2.0.5-efficiency-terms-ol-rcr-taf.md`

This chapter covers OL (Operational Load), RCR (Resource Consumption Rate), and TAF (Traffic Amplification Factor) — the metrics that sit behind your capacity and performance decisions.

---

### Weeks 3–4: Application Layer Taxonomy

**Framework**: `3-phase-principal-sre/3.2-application-layer-taxonomy/` — all 8 chapters, then playbooks

Application layer taxonomy is the shared vocabulary for describing how applications are structured — tiers, components, interfaces, dependencies. Principal SREs need this because they work across multiple services and teams, and they need a consistent way to describe, compare, and reason about application architecture.

Key concepts this block:
- Application architecture patterns: monolith, microservice, event-driven, serverless — the reliability trade-offs of each
- Dependency mapping: direct vs. indirect dependencies, synchronous vs. asynchronous
- API contract analysis: how interface design creates or prevents reliability risk
- Data layer taxonomy: how storage patterns affect reliability (consistency, availability, partition tolerance)
- Service mesh concepts: how service mesh tools change the observability and control surface

**Cookbook pairing**:  
`1-phase-foundations/1.0-vocabulary/1.0.16-enterprise-architecture-patterns.md`

Read this after completing the framework chapters. It applies the taxonomy to enterprise-scale architecture decisions.

---

### Weeks 5–7: Architecture Principles and Governance

**Framework**: `3-phase-principal-sre/3.3-architecture-principles-governance/` — all 8 chapters, then playbooks, then templates

Architecture governance is the discipline of ensuring that architectural decisions — across teams, across time — remain coherent and aligned with reliability principles. The Principal SRE role frequently sits in or near the ARB (Architecture Review Board), either as a technical reviewer or as a reliability advocate.

Key concepts this block:
- Architecture principles: what they are, how they are written, how they are enforced
- Architecture Review Board: how ARBs function, what makes an ARB effective vs. bureaucratic
- ADR (Architecture Decision Record): how to write one that is useful six months later
- Technical debt governance: how to make technical debt visible and manageable at the architectural level
- Reliability non-negotiables: how to define and defend the architectural constraints that must not be traded away for delivery speed

**Textbook integration**: Read in parallel:  
`2-phase-sre-practitioner/2.0-metrics-foundation/2.0.1-reliability-contract-and-gap.md`  
`2-phase-sre-practitioner/2.0-metrics-foundation/2.0.2-structural-terms-cd-scs-lbh.md`

Ch01 covers the reliability contract between a system and its consumers — the Principal SRE's conceptual foundation for every ARB discussion. Ch02 covers Call Depth (CD), SLO Coherence Score (SCS), and Latency Budget Hierarchy (LBH) — the structural metrics that let you reason about a multi-service architecture's reliability in quantitative terms.

**Cookbook pairings**:  
`1-phase-foundations/1.0-vocabulary/1.0.10-principal-leadership-communication.md`  
`1-phase-foundations/1.0-vocabulary/1.0.12-reliability-economics.md`

Read these during Weeks 5–7. Executive communication and reliability economics are the two skills that separate a Principal SRE who can influence architectural decisions from one who can only comment on them.

---

### Weeks 8–10: Application Portfolio Transformation

**Framework**: `3-phase-principal-sre/3.4-application-portfolio-transformation/` — all 8 chapters, then playbooks

Application portfolio transformation is how organizations systematically modernize, rationalize, and improve their application landscape. This is Phase 3's most strategically complex framework — it requires thinking about dozens of applications simultaneously, scoring their reliability maturity, and making prioritization decisions.

Key concepts this block:
- Portfolio scoring frameworks: how to assess the reliability maturity of an application
- Modernization patterns: lift-and-shift, re-platform, re-architect, retire — the reliability implications of each
- Dependency sequencing: how to determine the order in which applications should be transformed
- Risk stratification: which applications carry the most portfolio-level risk and why
- Business value alignment: how reliability investment decisions connect to business outcomes

**Textbook deep dive**: Read during Weeks 8–10:  
`2-phase-sre-practitioner/2.0-metrics-foundation/2.0.7-lifecycle-terms.md` — portfolio-level lifecycle scoring  
`2-phase-sre-practitioner/2.0-metrics-foundation/2.0.8-composite-scores-ris-srmi-jrcs.md` — executive-level composite scoring

The composite scores in Ch08 (RIS — Reliability Index Score, SRMI — System Reliability Maturity Index, JRCS — Journey Risk and Complexity Score) are the quantitative tools for portfolio transformation decisions. When you recommend retiring or re-architecting an application, these scores give you the evidence.

**Cookbook pairing**:  
`1-phase-foundations/1.0-vocabulary/1.0.14-enterprise-operational-realities.md`  
`1-phase-foundations/1.0-vocabulary/1.0.15-interdisciplinary-sre-topics.md`

---

### Weeks 11–12: Capstone and Scenario Integration

**Content**: `3-phase-principal-sre/3.5-capstone/` — all scenarios, case studies, and reference documents

The capstone phase integrates everything from Phases 1–3 into realistic scenario-based exercises. These are not test questions — they are operational scenarios that require you to apply multiple frameworks simultaneously, make decisions under ambiguity, and produce the artifacts that a Principal SRE would produce.

Structure for these two weeks:

- Work through each scenario in `3-phase-principal-sre/3.5-capstone/scenarios/` in the order they are provided
- For each scenario, identify which frameworks apply and what artifacts you would produce
- Write your reasoning — not just your conclusion, but the decision logic
- Compare your approach to the reference documents in `3-phase-principal-sre/3.5-capstone/reference/`

The capstone is also your Phase 3 exit assessment. If you can work through the scenarios and produce defensible artifacts, you are ready for Phase 4.

**Cookbook pairing**:  
`1-phase-foundations/1.0-vocabulary/1.0.11-ai-for-sre.md`

AI tools are increasingly part of the SRE toolkit. This cookbook chapter covers where AI augments SRE practice and where it does not — a critical perspective for a Principal SRE who will be asked to evaluate and recommend AI tooling.

---

## Textbook Integration Summary

| Chapter | When to Read | What It Adds |
|---------|--------------|--------------|
| ch01 (reliability contract) | Weeks 5–7 with architecture-governance | Foundation for every ARB-level reliability discussion |
| ch02 (CD, SCS, LBH) | Weeks 5–7 with architecture-governance | Structural metrics for multi-service reliability reasoning |
| ch05 (OL, RCR, TAF) | Weeks 1–2 with performance-engineering | Quantifies efficiency and capacity decisions |
| ch07 (lifecycle terms) | Weeks 8–10 with portfolio-transformation | Portfolio-level lifecycle scoring |
| ch08 (RIS, SRMI, JRCS) | Weeks 8–10 with portfolio-transformation | Executive-level composite reliability scores |
| ch09 (daily practice) | Ongoing | Live reference; keep it open |

---

## Phase 3 Competency Gates

You are ready for Phase 4 when you can do all of the following through demonstrated real-world practice or scenario-based defense of your decisions.

| Gate | What "done" looks like |
|------|----------------------|
| Reliability program design | Can design a full reliability program for a new service: SLI selection → SLO target → error budget policy → monitoring configuration → runbook set → on-call schedule → review cadence |
| Executive risk communication | Can present a reliability risk assessment to a VP or executive audience in 10 minutes or less, in business terms, with a clear recommendation and a defined ask |
| Architecture Review Leadership | Can lead an ARB session — not just attend one. Can prepare the agenda, facilitate the technical discussion, and produce a written decision record |
| RIS Scoring | Can score an application using the Reliability Index Score (RIS) framework from the textbook, and defend the score in a peer review |
| SPOF Analysis | Can identify single points of failure in a 10-service dependency graph and prioritize remediation by risk, not by ease |
| Load Test Design | Can design a load test with explicit hypothesis, load profile, and success/failure criteria, then interpret the results against SLO thresholds |
| SRE Coaching | Can coach a Senior SRE through their first P1 IC experience — not by taking over, but by guiding their decision-making in real time |
| ADR Authoring and Defense | Can write an Architecture Decision Record and defend it in an ARB session when challenged |

---

## What Phase 3 Does Not Cover

Phase 3 deliberately omits:
- People management and direct report relationships (that is Phase 4)
- Budget ownership and financial accountability (that is Phase 4)
- Vendor and partner management (that is Phase 4)
- Executive reporting cadences and operating rhythm (that is Phase 4)
- Org design and headcount planning (that is Phase 4)

Phase 3 gives you the technical credibility and strategic thinking that Director-level roles require. Phase 4 gives you the management operating system that Director-level roles demand. Both are necessary. Neither is sufficient alone.
