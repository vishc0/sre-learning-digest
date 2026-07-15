# Scenario 06 — Security Patch: Zero-Day CVE Response

**Series**: SRE Capstone — Principal-Level Scenarios
**Difficulty**: Principal (P0 consequence, hard external deadline, governance override)
**Domain**: Incident Response, Change Management, Risk Quantification, Security Operations

---

## 1. Scenario Brief

A critical CVE with CVSS score 9.8 has been disclosed in Eclipse Temurin JDK 17. The exploit is public and weaponized. Your shopping cart platform runs 12 microservices; 9 of them use Temurin JDK 17 as their base image:

| Tier | Services |
|------|----------|
| P0 | Auth, Payment |
| P1 | Cart, Order Management |
| P2 | Inventory, Pricing, User Profile |
| P3 | Search, Notification |

**Security team mandate**: All 9 services must be running the patched image within 4 hours of disclosure.
**Disclosure time**: 9:00 AM Tuesday (peak traffic window).
**Hard deadline**: 1:00 PM.

This is the scenario where SRE's normal governance — error budget gates, scheduled maintenance windows, mandatory canary periods — is overridden by an external hard deadline. The fundamental tension is not "patch or don't patch." The mandate is non-negotiable. The tension is **patch fast versus patch safely within the same window**. SRE's role is to maximize the probability that "fast" and "safely" are not mutually exclusive.

---

## 2. PPC — Patch Parallelism Ceiling

**Definition**: PPC is the maximum number of services that can be patched concurrently while preserving rollback feasibility for all of them within the remaining time window.

```
PPC = floor( (remaining_time - validation_window) / avg_rollback_time_per_svc )
```

**Applying the formula at T=0 (9:00 AM):**

- Remaining time: 240 minutes
- Validation window (final health check across all services): 30 minutes
- Usable working time: 240 − 30 = 210 minutes
- Average rollback time per service: 10 minutes

```
PPC = floor(210 / 10) = 21
```

PPC = 21 means you could theoretically roll back 21 services simultaneously and still finish within the window. With only 9 services to patch, PPC is not the binding constraint here. The binding constraint is **BRI** — the risk of a broken patch hitting all services simultaneously. PPC sets the upper bound; patch sequencing discipline sets the actual concurrency.

A working concurrency of 3 services per wave (explained in Section 3) keeps BRI manageable while still completing well inside the 4-hour window.

---

## 3. Patch Sequencing by Tier — Why P0 Goes Last

The instinct in a security emergency is to patch the highest-risk services first. This instinct is wrong during a zero-day response when the patch itself is unvalidated.

**The correct sequencing principle**: Use lower-tier services as a live validation environment for the patch before it touches P0 services. P2/P3 services carry lower blast radius; a patch failure there is recoverable without a P0 outage.

**Sequencing logic using Dependency Graph (DG)**:

Build the DG by service dependency, not service criticality. Patch leaves of the graph first (services with no inbound critical dependencies), then work toward the root nodes (P0 services).

```
[Notification] → no inbound deps    → patch Wave 1
[Search]       → no inbound deps    → patch Wave 1
[Inventory]    → feeds Pricing      → patch Wave 1
[Pricing]      → feeds Cart         → patch Wave 2
[User Profile] → feeds Auth         → patch Wave 2
[Order Mgmt]   → feeds Cart, Auth   → patch Wave 2
[Cart]         → feeds Payment      → patch Wave 3
[Auth]         → feeds all P0 flows → patch Wave 4 (last)
[Payment]      → terminal P0 node   → patch Wave 4 (last)
```

**Wave structure**:

| Wave | Services | Start | Rationale |
|------|----------|-------|-----------|
| Wave 1 | Search, Notification, Inventory | 9:00 AM | P3/P2 leaves; patch validation run |
| Wave 2 | Pricing, User Profile, Order Mgmt | 9:30 AM | P2/P1 after Wave 1 validates patch |
| Wave 3 | Cart | 10:00 AM | P1 after P2 confirms no breakage |
| Wave 4 | Auth, Payment | 10:30 AM | P0 last; full patch confidence established |

Each wave includes a 20-minute canary period and 10 minutes of post-wave validation before the next wave starts. Waves 1–3 are the patch validation mechanism. Wave 4 executes on confirmed, field-validated patch behavior.

---

## 4. BRI During Mass Patching — The Case Against Full Parallelism

**BRI (Blast Radius Index)** measures the proportion of the system exposed to a simultaneous failure. If a broken patch is deployed to all 9 services at once:

```
BRI = affected_services / total_services = 9 / 12 = 0.75
```

A BRI of 0.75 means 75% of the platform fails simultaneously. Auth and Payment are included. This is a complete platform outage caused not by the CVE, but by the remediation itself.

The sequenced wave approach reduces BRI at each decision point:

| Point in time | Max concurrent at risk | BRI |
|--------------|----------------------|-----|
| Wave 1 only | 3 services (P3/P2) | 3/12 = 0.25 |
| Wave 2 only | 3 services (P2/P1) | 3/12 = 0.25 |
| Wave 3 only | 1 service (Cart) | 1/12 = 0.08 |
| Wave 4 only | 2 services (Auth, Payment) | 2/12 = 0.17 |

Peak BRI under sequenced approach: **0.25** — compared to **0.75** under full parallelism. The sequenced approach reduces worst-case blast radius by 67% while adding only 90 minutes to the execution timeline, well within the 4-hour mandate.

---

## 5. EBR Override — Security Exception Authority Chain

Forced out-of-cycle deployments consume error budget. Nine simultaneous forced deploys during peak traffic represent a significant **EBR (Error Budget Reservation)**. Under normal governance, a service already at error budget exhaustion cannot deploy. Security patches are the one exception.

**Override authority chain**:

1. Security team declares the CVE mandates emergency patching (timestamp and ticket number required)
2. SRE Lead acknowledges: "EBR gates are suspended for CVE-XXXX-XXXXX remediation"
3. CTO or designee countersigns the override — this is an executive risk acceptance, not an SRE decision
4. SRE documents: which services had exhausted budgets at override time, what their EBV looked like entering the patch window, and the ticket number authorizing the bypass

The override is not a blanket suspension of observability. EBV monitoring continues throughout. The override means SRE cannot *block* the deployment on budget grounds — it does not mean SRE stops watching the budget. A service whose error rate spikes during patching still triggers an immediate rollback of that specific service's patch (see Section 7).

**Post-incident documentation requirement**: The override and all associated EBR consumption must appear in the postmortem. This is how the organization accounts for invisible reliability debt created during emergency response.

---

## 6. The 4-Hour Execution Timeline

| Time | Action | Owner | Gate |
|------|--------|-------|------|
| 9:00 AM | Wave 1 deploys (Search, Notification, Inventory) | SRE + Release | EBV baseline captured |
| 9:10 AM | Canary validation — 10% traffic, error rate watch | SRE | EBV < 2x baseline |
| 9:20 AM | Wave 1 full rollout | Release | No EBV breach |
| 9:30 AM | Wave 2 deploys (Pricing, User Profile, Order Mgmt) | SRE + Release | Wave 1 confirmed stable |
| 10:00 AM | Wave 3 deploys (Cart) | SRE + Release | Wave 2 confirmed stable |
| 10:30 AM | Wave 4 deploys Auth (canary only, 5% traffic) | SRE Lead | Wave 3 confirmed stable |
| 10:45 AM | Auth full rollout; Payment canary begins | SRE Lead | Auth EBV clean |
| 11:00 AM | Payment full rollout | SRE Lead | Payment EBV clean |
| 11:00–11:30 AM | Final validation: all 9 services health-checked | SRE | All green |
| 12:00 PM | Security team sign-off; incident declared complete | Security + SRE | Formal closure |

**Failure scenario at 10:45 AM**: Auth canary shows elevated 5xx rates. EBV spikes past 2x baseline. Immediate action:
- Roll back Auth patch only (10 minutes)
- Payment canary does not proceed while Auth is in rollback
- Engage image team: is this the patch or a config conflict?
- If rollback restores Auth health: investigate patch compatibility before re-attempt
- Hard decision point: if Auth patch cannot complete by 12:30 PM (allowing 30-minute buffer), escalate to CTO for extended window or compensating control (WAF rule, network segmentation) while patch is re-validated

The timeline has a 60-minute buffer before the 1:00 PM hard deadline. That buffer exists specifically to absorb one P0 rollback-and-retry cycle.

---

## 7. EBV Monitoring During Patch — Rollback Thresholds

**EBV (Error Budget Velocity)** is the rate at which error budget is being consumed, measured as a multiple of the baseline consumption rate.

For each service being patched, SRE captures a 15-minute EBV baseline before the wave begins. During and after patching, the following thresholds apply:

| EBV Multiple | Meaning | Action |
|-------------|---------|--------|
| 1.0–1.5x | Normal variance | Continue |
| 1.5–2.0x | Elevated — watch closely | Halt next wave until stable |
| 2.0x+ | Patch causing degradation | Immediate rollback of this service |
| 5.0x+ | Severe degradation / cascade risk | Rollback + P0 page regardless of tier |

Rollback is per-service. A Wave 2 service breaching 2.0x EBV does not roll back Wave 1 services — it halts Wave 3 advancement until the breach is resolved. This is the SRE discipline: contain the failure to the service that triggered it.

Monitoring tooling must be pre-staged before 9:00 AM: dashboards open, alert routing confirmed, on-call bridge active. The **APR (Alert Precision Rate)** problem during mass deployments is real — CI/CD pipelines generate high alert volumes during simultaneous releases, and alert fatigue causes genuine signals to be missed. Pre-stage service-specific EBV dashboards so SRE engineers are watching metrics, not alert queues.

---

## 8. Post-Patch Debt — Restoring Normal Governance

Nine forced out-of-cycle deployments in a single morning dramatically spike **SCV (Service Change Volatility)**. SCV measures the frequency of service changes relative to the baseline cadence. A normal Tuesday might see 1–2 planned deployments; this morning produced 9 emergency deployments at irregular intervals.

High SCV means the system is harder to reason about for the next 24–48 hours. Correlation between failures and recent changes becomes ambiguous.

**Post-patch retrospective must address**:

1. **EBR accounting**: For each service that was at budget exhaustion when the override occurred, document the budget consumed and schedule a reliability sprint to rebuild it
2. **SCV normalization window**: No additional deployments to patched services for 48 hours unless critical. The system needs a settling period
3. **Change freeze recommendation**: Communicate to engineering leads that patched services are in a heightened monitoring state and voluntary changes should defer to Thursday
4. **MRI (Migration Risk Index) reset**: The forced migration altered the baseline MRI for all 9 services. Recalculate MRI incorporating the new base image version, patch history, and any anomalies observed during rollout
5. **Process improvement**: Did the 4-hour window work? Were the wave boundaries correct? Was the PPC formula adequate? Feed findings back into the incident response runbook

---

## 9. The Parallel Risk: The Patch Itself May Be Broken

The 2021 Log4Shell response is the definitive case study. The initial patch (Log4j 2.15.0) was released under emergency conditions and itself contained a vulnerability that required a second patch (2.16.0) within days. Organizations that mass-deployed 2.15.0 to all services simultaneously had to repeat the entire exercise.

**Patch validation step** — built into every wave transition:

Before promoting a patched image from Wave N to Wave N+1, run a structured validation checklist:

1. **Functional smoke test**: Does the service start, respond to health checks, and handle a representative request set correctly?
2. **Security validation**: Does the CVE scanner report the specific CVE as remediated in the new image? (Do not rely on image tag alone — scan the running container)
3. **Regression baseline**: Does the service's EBV and latency profile match pre-patch baseline within 10%?
4. **Dependency compatibility**: Does the new JDK version introduce any behavioral changes visible in the service's integration tests? (Temurin 17 minor version updates occasionally change TLS cipher preference ordering — confirm with Auth and Payment before Wave 4)

The wave structure is itself the primary protection against a broken patch. If the patch is broken, it will manifest in Wave 1 services (P3/P2 — Search, Notification, Inventory) before it ever reaches Auth or Payment. **This is the engineering justification for the P0-last sequencing**: P2/P3 services are sacrificial validators in the best sense — they absorb the discovery cost of a broken patch at low blast radius.

**FLI (Failure Locality Index)**: A broken patch discovered in Wave 1 has FLI near 0 — the failure does not propagate to P0 services because those services have not yet been patched. A broken patch discovered after full parallel deployment has FLI near 1.0 — every service fails simultaneously and cascades are inevitable.

The 4-hour window is tight but not impossible to execute safely. The wave structure is the mechanism that makes "fast" and "safe" compatible goals rather than opposing ones.

---

## Summary — Key Formulas Applied

| Metric | Value | Interpretation |
|--------|-------|---------------|
| PPC | 21 | Far exceeds 9 services; not the binding constraint |
| BRI (parallel) | 0.75 | Unacceptable; 75% platform outage if patch is broken |
| BRI (sequenced, peak) | 0.25 | Acceptable; 3 P2/P3 services maximum at risk per wave |
| EBV rollback threshold | 2.0x baseline | Per-service; triggers immediate rollback, not full halt |
| Timeline buffer | 60 minutes | One P0 rollback-and-retry cycle absorbed |
| SCV impact | High | 48-hour normalization window required post-patch |

The zero-day scenario is the acid test of SRE maturity. Anyone can deploy fast. The discipline is deploying fast while preserving the ability to recover — and using the structure of the deployment itself as the mechanism for validating an unproven patch before it reaches the services the business cannot afford to lose.
