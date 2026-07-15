# Principal SRE Framework Design — Shopping Cart System

## How a Principal SRE Thinks About This Project

A Principal SRE does not start with tools, dashboards, or runbooks. They start with three questions that cut across everything:

1. **What did we promise the customer?** — This is the SLA. Every technical decision either supports or undermines it.
2. **What is the minimum architecture that can keep that promise?** — This is the reliability floor. Everything below it is a structural risk.
3. **How do we govern change so the floor never drops?** — This is the SRE operating model.

Everything else — observability, incident management, on-call design, change gating — is execution of the answers to those three questions. A Principal SRE's job is to ensure those answers are always current, always grounded in measurement, and always visible to engineering leadership.

---

## The Project-Level Reliability Contract

For the shopping cart, the customer SLAs are:

| Journey | SLA (availability) | SLA (latency p99) | Revenue criticality |
|---------|-------------------|-------------------|---------------------|
| Checkout | 99.95% | 2000ms | Direct (every second of downtime = lost GMV) |
| Add to Cart | 99.90% | 300ms | Gate (blocks checkout funnel) |
| Browse / Search | 99.50% | 800ms | Indirect (conversion funnel entry) |
| Order Tracking | 99.50% | 1000ms | Service (customer satisfaction) |
| Account Mgmt | 99.00% | 2000ms | Low (infrequent, non-revenue) |

**The reliability contract is not a list of uptime targets. It is a mathematical constraint on the entire architecture.** Once the SLAs and call depths are known, the required per-service SLO for every service on every critical path is derivable — not negotiable.

---

## The Three-Layer SRE Operating Model

### Layer A — Architecture Governance (Principal SRE leads)

The Principal SRE owns the architecture reliability constraints. No service is added to, or removed from, the call chain of any P0 journey without Principal SRE approval. No new dependency with DG > 6 is created without a formal reliability review. The Principal SRE computes SLO Coherence Score (SCS) quarterly for all journeys and presents findings in the reliability review board.

**Principal SRE's standing agenda**:
- Call Depth audit: are any journeys drifting toward higher CD than planned?
- Dependency Gravity review: are any services accumulating unexpected DG?
- SLO coherence check: is the math still sound — do per-service SLOs produce the customer SLA?
- Migration Risk Index: what changes are in flight, and what is their combined MRI?

### Layer B — Operational Excellence (SRE team executes)

The SRE team owns the operational health of P0 and P1 services. This means: error budget accounting, alert quality (APR), on-call health (page load, MTBI, MTTR), toil management (TAF), and reliability investment prioritization (OL, RCR). The SRE team does not own the application code but owns the operational standards every service must meet.

**SRE team's standing agenda**:
- Error budget review (monthly): which services consumed budget? Why?
- Alert quality review (quarterly): APR per alert category; tune or retire low-precision alerts
- Toil review (quarterly): TAF per toil category; automation sprint planning
- RCR ranking: top 5 recurring incident classes by RCR; fix or accept decision

### Layer C — Delivery Safety (SRE embedded in delivery)

Every change to the shopping cart system passes through an automated CR gate before reaching production. The gate computes MRI, checks EBR, validates layer-specific gates (G1.1–G6.6), and returns an approval requirement. SRE does not review every CR — but SRE designed the gate and owns the thresholds.

**SRE's delivery safety tools**:
- CI/CD gate: automated MRI calculation; EBR check; layer gate validation
- Canary deployment: all P0 service changes start at 5% traffic; SRE monitors EBV during canary
- Feature flag governance: all new features behind flags; rollout governed by Rollout Momentum Score
- Deployment annotation: every production change creates a Grafana annotation for correlation

---

## The Shopping Cart Reliability Floor — Current State vs. Target

### Current State (before framework implementation)

| Metric | Current Value | Classification |
|--------|-------------|---------------|
| Checkout actual availability | ~99.62% | Below SLA (target 99.95%) |
| OCR_weighted | 45.7% | Critical |
| APR (overall) | 31% | Alert fatigue zone |
| FLI (system) | 72% | Moderate — cascade risk present |
| TAF (overall) | 0.62 | Acceptable, borderline |
| Auth Service DG | 18 | Critical infrastructure |
| Auth MTBI-implied availability | 99.96% | Below declared SLO (99.990%) |
| CD for Checkout (optimized) | 5 | High — architectural investment needed |

### Target State (12-month horizon)

| Metric | Target | Key investment |
|--------|--------|---------------|
| Checkout actual availability | > 99.92% | Auth/Inventory hardening + CD reduction |
| OCR_weighted | > 0.95 | Instrumentation sprint |
| APR (overall) | > 0.80 | Alert redesign |
| FLI (system) | > 0.90 | Circuit breaker audit |
| TAF (overall) | < 0.50 | Deployment automation |
| CD for Checkout | 4 (via API GW JWT) | API Gateway JWT authorizer |

### The Reliability Investment Portfolio

The Principal SRE maintains a reliability investment portfolio — a ranked, justified list of engineering investments, each with computed OL (Operational Leverage) and RCR (Recovery Cost Ratio). The portfolio is the answer to: "how should we allocate reliability engineering time?"

```
Portfolio (Q1 Priority):
┌────────────────────────────────────────────────────┬─────┬────────────────────┐
│ Investment                                          │ OL  │ Justification      │
├────────────────────────────────────────────────────┼─────┼────────────────────┤
│ API Gateway JWT validation (CD: 5→4)               │ 15+ │ Structural fix     │
│ Kafka consumer watchdog automation                  │ 18  │ RCR=1.2, do now    │
│ Auth Service pod scaling (3→5)                     │ 12  │ MTBI improvement   │
│ Pricing + Search observability (OCR gap)           │ 10  │ Blind spot fix     │
│ Alert redesign (latency + infra categories)        │ 8   │ APR: 31%→80%      │
│ Inventory circuit breaker (FLI improvement)        │ 6   │ CC reduction       │
│ SLO recalibration (MTBI-based, no theater)         │ n/a │ Governance fix     │
└────────────────────────────────────────────────────┴─────┴────────────────────┘
```

---

## The Nine Operational Scenarios

A Principal SRE must have a consistent mental model and decision framework for every type of change that touches the shopping cart. Nine scenarios cover the full lifecycle:

| Scenario | File | Core SRE concern |
|---------|------|-----------------|
| Greenfield service addition | scenario-01-greenfield-service.md | Does the new service meet the reliability bar required by its consumers? |
| Feature flag-gated launch | scenario-02-feature-flag-launch.md | Is the rollout rate safe given current error budget? |
| Dependency version upgrade | scenario-03-dependency-upgrade.md | What is the compatibility surface and what fails silently? |
| Traffic surge / scaling event | scenario-04-traffic-surge.md | Does provisioned capacity outrun elasticity response time? |
| Platform / cluster migration | scenario-05-platform-migration.md | How do we maintain SLO continuity during full cluster rebuild? |
| Security patch / zero-day | scenario-06-security-patch.md | How do we patch 9 services across 4 hours without outage? |
| Incident-driven architecture change | scenario-07-incident-driven-change.md | How do we fix structural reliability debt without creating new risk? |
| Service decommission | scenario-08-service-decommission.md | How do we retire a service without orphaning callers? |
| Third-party API change | scenario-09-third-party-api-change.md | How do we maintain SLA when an external provider forces a breaking change? |

Each scenario has a dedicated textbook document covering: concept, Principal SRE assessment sequence, applicable coined terms with computed values, decision gates, monitoring plan, and exit criteria.

---

## Cross-Scenario Principles

These principles apply across every scenario. A Principal SRE invokes them regardless of which specific scenario is in play.

### Principle 1 — Measure before and after, not just during

Every change to the shopping cart must have a pre-change baseline captured and a post-change validation window defined. The validation window length is proportional to MRI:
- MRI < 3: 48-hour validation window
- MRI 3–8: 2-week validation window
- MRI > 8: 4-week validation window

### Principle 2 — Error budget is the change gate, not a postmortem

Error budget consumption gates whether a change can proceed. If the checkout journey has consumed > 70% of its monthly error budget by day 15, no further P0 service changes are allowed in that window — regardless of urgency (security patches are the only exception). This converts error budget from a reporting metric into an operational lever.

### Principle 3 — Rollback velocity determines the maintenance window, not the calendar

Every planned change must declare its Rollback Velocity (RV) before the maintenance window is scheduled. The window length must be ≥ 3× RV. If the rollback for a change would take 2 hours, the maintenance window is at minimum 6 hours. This prevents the most common maintenance failure: running out of time to rollback cleanly.

### Principle 4 — New services inherit reliability debt if they don't meet the RIR

When a new service is added to any critical journey, it must meet the Reliability Inheritance Requirement (RIR) — the minimum reliability bar derived from the SLO requirements of its consumers. A service that enters a call chain without meeting RIR creates SLO incoherence immediately. RIR is non-negotiable for P0 journeys; it can be waived for P2/P3 with documented risk acceptance.

### Principle 5 — The cascade is always the real incident

When incidents cascade, the root cause is the failure of blast radius containment, not the originating failure. The FLI for the incident is the signal: FLI < 0.90 for an incident means the real finding is a circuit breaker or bulkhead gap, not whatever the originating failure was. Postmortems for cascading incidents must have an FLI-improvement action item, not just a root-cause fix.

---

## How a Principal SRE Communicates Reliability to Leadership

### To the CTO (weekly)

> "Checkout availability this week: 99.87%. SLA is 99.95%. We are 0.08 points below target. Root cause: Auth Service had two incidents totaling 22 minutes of checkout impact. MTBI-implied availability for Auth is 99.96% — our declared SLO is 99.990%. We have SLO theater on Auth. Recommendation: fund the API Gateway JWT validation investment (removes Auth from checkout critical path; 1 sprint, 4× OL). Without it, we cannot close this gap."

### To the VP Engineering (monthly)

> "Shopping cart reliability portfolio: three high-ROI investments are unfunded. Kafka watchdog (RCR=1.2, RV=1 week) would eliminate the weekly Notification consumer lag incident, saving 48 SRE hours/year. Inventory circuit breaker (FLI improvement: 72%→85%) would prevent 30% of checkout cascade incidents. Alert redesign (APR: 31%→80%) would reduce on-call page volume by 60%, freeing 2 SRE-days/week for proactive work. Total investment: 6 engineer-weeks. Annual return: 200+ SRE hours and elimination of 3 recurring incident classes."

### To the on-call SRE (during incident)

> "Checkout error rate is 3%. EBV is 2.8 — we are burning budget at 2.8× expected rate. Current budget consumed this window: 12 of 21.9 minutes (55%). If this continues for 30 more minutes, we breach SLA. BRI for current failure: 0.35 (SEV2). Declare SEV2 now. Escalate to Engineering Manager. Cascade risk: CC for Auth is 10.8 — if Auth is involved, expect Cart and Order Management to follow. Check circuit breaker status on Cart → Auth call before declaring root cause."
