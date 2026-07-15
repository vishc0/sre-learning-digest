# Scenario 09 — Third-Party API Deprecation: Stripe v2 → v3 Migration

**System**: Shopping Cart (12 microservices on EKS)
**Event**: Stripe announces HTTP 410 Gone for all v2 Payment API calls in 90 days
**SRE Role**: Principal SRE governing a mandatory, externally-forced payment migration

---

## 1. Concept — When the Forcing Function Comes From Outside

Every migration the SRE team governs internally is a negotiated migration. The team sets the pace using MRI to measure risk, EBR to hold budget in reserve, and SSE to avoid compressing multiple high-risk changes into the same window. Internal migrations can be paused, slowed, or rescheduled when conditions are unfavorable. The SRE has authority over the timeline because the system being changed belongs to the organization.

Third-party API deprecation removes that authority. When Stripe announces that v2 API calls will return HTTP 410 Gone on day 90, the organization does not get a vote. The deadline is not a negotiation point. It is a constraint that arrives from outside the system boundary.

This changes the SRE's role fundamentally. In an internal migration, SRE governs the pace of change — slowing teams down when MRI is too high, holding budget when EBV rises, requiring OCR improvements before authorizing the next increment. In an externally-forced migration, the SRE's role shifts to a different question: can we complete this migration safely before the deadline forces an unsafe cutover?

The distinction matters operationally. An internally-governed migration that goes badly can be stopped. An externally-forced migration that goes badly cannot be stopped — if the deadline passes and migration is incomplete, the production system starts returning payment failures to customers automatically, without any human decision. The SRE is not managing risk in the normal sense. The SRE is racing a deadline while managing risk.

The Stripe v2 → v3 migration has three specific properties that make it more complex than a standard service upgrade:

**Schema discontinuity.** Stripe v3 uses a different request and response schema. This is not a version bump with backward-compatible field additions. The Payment Service must be rewritten to speak a different protocol, not updated to handle a new field.

**Authentication model change.** Stripe v3 uses a different authentication flow. Every environment — development, staging, production — requires credential rotation and new secret management configuration before a single v3 API call can be tested.

**Webhook format change.** Stripe v3 sends payment confirmation webhooks in a new format. This makes the migration scope larger than the Payment Service alone. Any service that consumes Stripe webhooks — Order Management, Notification Service — must also be updated before v3 can be declared complete.

SRE's job is to know all three of these properties before any code is written, because each one affects the migration's MRI, the SCW duration, and the feasibility of rollback.

---

## 2. The Stripe SLA Problem — SCS Below 1.0

Before computing any migration timelines, SRE must confront a structural problem that exists independent of the migration: Stripe's SLA does not support the checkout SLA.

Checkout SLA: **99.95%** (monthly error budget: 21.9 minutes)
Stripe's contractual SLA: **99.9%**
Payment Service dependency graph position: critical path, call depth CD=5

The SLO Coherence Score for this dependency relationship is:

```
SCS = Stripe_SLA / checkout_SLA
SCS = 0.999 / 0.9995
SCS = 0.9995
```

An SCS below 1.0 means the checkout SLA is mathematically unsupportable given Stripe's own reliability commitment. Even if every internal service performs perfectly, Stripe's 99.9% SLA allows 43.8 minutes of downtime per month. The checkout SLA permits only 21.9 minutes. Stripe alone can consume the entire checkout error budget and then exceed it — with no contract violation on their side.

This is not a migration risk. This is a pre-existing architectural risk that the migration makes visible. SRE must document this in the risk register before the migration begins, because it defines the baseline: the checkout SLA was already under-supported before v3 became relevant.

**What SRE documents in the risk register:**

| Item | Detail |
|------|--------|
| Risk | Stripe SLA (99.9%) is insufficient to support checkout SLA (99.95%) |
| SCS | 0.9995 — structurally below 1.0 |
| Likelihood | High — Stripe incidents consume checkout budget by design |
| Impact | High — Stripe outage exceeds checkout budget before any internal failure |
| Mitigation | Circuit breaker with graceful degradation (allow checkout to complete with payment queued); SLA renegotiation with Stripe; or Stripe redundancy via secondary processor |
| Residual | Medium — circuit breaker eliminates cascade; SLA gap remains unless secondary processor added |

The v3 migration does not change this SCS. Stripe's v3 SLA is the same as v2: 99.9%. After migration, SCS remains 0.9995. The risk register entry does not close at migration completion.

---

## 3. EDFD Calculation — When Budget Math Forces Cutover

The External Deprecation Forcing Date (EDFD) is the date at which the remaining error budget, consumed at the current degradation rate, would be exhausted. EDFD is not the same as the Stripe deadline. EDFD is when *budget math* forces the team to cut over, which may be earlier than the official deadline if v2 degradation begins before day 90.

**Given conditions:**
- Stripe begins degrading v2 reliability at day 60 (reduced engineering investment as sunset approaches)
- v2 API returns occasional HTTP 299 Deprecated warnings with a 0.1% probability of causing checkout errors
- That 0.1% error rate on the checkout journey translates to approximately 0.2 minutes per day of error budget consumed
- Error budget consumed so far this month: 7 minutes
- Monthly error budget: 21.9 minutes
- Remaining budget: 21.9 − 7.0 = **14.9 minutes**

**EBR reservation** (budget held in reserve for migration itself):

SRE holds 30% of monthly error budget in reserve for any migration of this risk level.

```
EBR_reserved = 0.30 × 21.9 = 6.57 minutes
```

Budget available for v2 degradation to consume before forced cutover:

```
Available_budget = 14.9 − 6.57 = 8.33 minutes
```

**EDFD from the point v2 degradation begins (day 60):**

```
EDFD = day_60 + (Available_budget / daily_EBV_burn_from_degradation)
EDFD = day_60 + (8.33 / 0.2)
EDFD = day_60 + 41.6 days
EDFD ≈ day 101 (from today)
```

However, day 90 is the hard Stripe deadline. Since EDFD is day 101 and the deadline is day 90, there appears to be 11 days of slack in budget terms. But this assumes v2 degradation stays flat at 0.2 minutes/day and does not accelerate as Stripe invests less in v2 maintenance. If EBV from v2 degradation doubles to 0.4 min/day in the final 30 days:

```
EDFD_accelerated = day_60 + (8.33 / 0.4) = day_60 + 20.8 = day 81
```

At accelerated degradation, EDFD moves 9 days *before* the Stripe deadline. The team has no slack and may be forced into an incomplete v3 migration under budget pressure. This is the signal EDFD is designed to surface: it converts an abstract deadline into a concrete budget-derived forcing function that the SRE can track in real time.

**Practical use of EDFD:** At day 60, when v2 degradation begins, SRE begins measuring actual EBV from v2 errors daily. If observed EBV exceeds 0.2 min/day for three consecutive days, EDFD is recalculated and the migration schedule is accelerated accordingly.

---

## 4. SCW During Migration — Service Compatibility Window

The Service Compatibility Window is the duration during which the Payment Service must support both v2 and v3 simultaneously. v2 serves production traffic. v3 is being validated in staging and, once partial traffic migration begins, in production.

**Migration ramp plan:**
- Days 1–30: v3 integration built and tested in staging
- Day 30: v3 receives 10% of production checkout traffic (canary)
- Day 45: v3 at 50% if canary metrics are clean
- Day 60: v3 at 100%; v2 decommission begins
- Day 90: v2 sunset (Stripe enforces HTTP 410)

SCW begins when v3 first receives production traffic (day 30) and ends at v2 sunset (day 90).

```
SCW = day_90 − day_30 = 60 days
```

During this 60-day window, the Payment Service codebase must route traffic to v2 or v3 based on a feature flag, maintain separate authentication credentials for both, handle both request schemas in the outbound client, and process both response schemas inbound. The webhook consumers (Order Management, Notification Service) face the same dual-format requirement for the SCW duration.

**PCC (Protocol Coexistence Cost)** for this 60-day window represents the engineering and operational burden of maintaining two live API versions. The specific costs are:

- Dual secret rotation cycles (v2 credentials expire; v3 credentials must be provisioned fresh)
- Parallel observability: two sets of dashboards (v2 error rate, v3 error rate) must be maintained
- Dual runbooks: on-call engineers must know how to diagnose both v2 and v3 failures during SCW
- Increased cognitive load on incident response: when a payment failure occurs during SCW, the first diagnostic question is always "is this a v2 issue, a v3 issue, or a routing issue?"

PCC is the cost of not completing the migration faster. Every week of SCW duration is a week of double operational overhead. The migration plan should minimize SCW to the shortest window that allows safe validation of v3, not the most comfortable window for engineering.

---

## 5. Migration Risk Assessment — MRI for Payment Service v3

The Migration Risk Index for the Payment Service v3 migration is computed as:

```
MRI = DG × (1 − OCR) × (1 − FLI) × CD_weight
```

Where `CD_weight = CD / max_CD_in_system`. With checkout at CD=5 and maximum observed CD in the shopping cart system at 6:

```
CD_weight = 5 / 6 = 0.833
```

**Baseline MRI (current OCR = 0.457):**

```
MRI_baseline = 4 × (1 − 0.457) × (1 − 0.72) × 0.833
MRI_baseline = 4 × 0.543 × 0.28 × 0.833
MRI_baseline = 4 × 0.127 = 0.507
```

An MRI above 0.4 requires mandatory OCR improvement before migration authorization. At 0.507, the Payment Service cannot be migrated in its current observability state. The SRE team must require the Payment Service team to raise OCR to at least 0.75 before v3 migration can proceed.

**Revised MRI after OCR improvement to 0.95 (as specified in the migration plan):**

```
MRI_revised = 4 × (1 − 0.95) × (1 − 0.72) × 0.833
MRI_revised = 4 × 0.05 × 0.28 × 0.833
MRI_revised = 4 × 0.0117 = 0.047
```

At MRI = 0.047, the migration is low-risk by index. The OCR improvement from 0.457 to 0.95 reduces MRI by a factor of 10. This is why SRE mandates observability improvements before migrations, not during them: the MRI reduction is significant, and the work to improve OCR takes time that must be budgeted into the migration window.

With a 90-day hard deadline, the sequence is: days 1–15 (OCR improvement to 0.95), days 15–30 (v3 integration built in staging), days 30–90 (production ramp and cutover). The OCR work is not optional and it is not parallel to the v3 integration work — it is a prerequisite gate that must close before the migration is authorized.

---

## 6. The Rollback Window — Asymmetric Reversibility

In a standard service migration, rollback is always available. A new deployment can be reverted. A feature flag can be toggled. The SRE governance model assumes that if a migration goes badly, the team can stop and return to the previous state.

The Stripe v2 → v3 migration has a rollback window that closes permanently on day 90. Before day 90, if v3 integration fails in production, the Payment Service can be rolled back to v2 and checkout continues operating. After day 90, v2 returns HTTP 410 Gone, rollback to v2 means payment failures for all customers, and the team has no safe fallback.

This asymmetry changes SRE governance in a specific way as the deadline approaches.

**Rollback Velocity (RV) by phase:**

| Phase | Days Remaining | RV (ability to roll back safely) | Governance implication |
|-------|---------------|----------------------------------|----------------------|
| Pre-canary | 60–90 | High — full rollback possible in minutes | Standard canary controls apply |
| Canary (10–50%) | 30–60 | Medium — rollback possible but disruptive at scale | Require explicit SRE sign-off before advancing canary |
| Late canary (50–90%) | 15–30 | Low — rollback increasingly disruptive; v2 degrading | Mandatory daily MRI review; no canary pausing allowed |
| Final approach | 0–15 | Critical-low — rollback window closing; v2 unreliable | All hands; no discretionary changes in Payment or adjacent services; SSE enforced |

The SRE governance model shifts from "gate each increment carefully" to "do not allow any condition that would force us into the final 15-day window with incomplete migration." The worst outcome is arriving at day 75 with v3 at 30% traffic and an unresolved defect that would require a rollback — at that point, rolling back to v2 is disruptive but possible, but the team has 15 days to fix a defect under budget pressure with a degrading v2 API. That is the scenario that produces an SLA breach.

The SRE prevents this by setting a hard trigger: if v3 canary cannot reach 50% traffic by day 60, an incident is declared, leadership is escalated, and the migration is treated as a P0 program-level risk regardless of the current P-severity of any individual defect.

---

## 7. EBV During v2 Degradation — The Early Warning Signal

Error Budget Velocity (EBV) measures how quickly the error budget is being consumed relative to the normal baseline. An EBV of 1.0 means budget is being consumed at exactly the expected rate. An EBV above 1.0 means the budget is being consumed faster than normal — the budget will run out before the end of the month at the current burn rate.

As Stripe reduces engineering investment in v2 after the sunset announcement, v2 reliability is expected to decline gradually. The EBV signal from this degradation is the primary early warning indicator for the migration timeline.

**EBV interpretation thresholds:**

| EBV | Condition | Action |
|-----|-----------|--------|
| 1.0–1.1 | Normal — v2 performing within SLA | Monitor; no migration acceleration |
| 1.1–1.3 | Elevated — v2 beginning to degrade | Recalculate EDFD; accelerate v3 staging validation |
| Above 1.3 (sustained 3 days) | Warning — v2 unreliable; budget burn accelerating | Mandatory EDFD recalculation; SRE escalation; canary timeline compressed |
| Above 2.0 (any single day) | Critical — v2 SLA failing | Emergency session; evaluate early cutover if v3 is at ≥70% traffic |

If EBV rises above 1.3 consistently (three or more consecutive days), the EDFD calculation must be rerun with the observed EBV as the daily burn rate rather than the projected 0.2 min/day. As shown in section 3, a doubling of EBV moves EDFD from day 101 to day 81 — inside the Stripe deadline. An EBV above 1.3 is the operational signal that the migration schedule has become critical, regardless of what the calendar says.

This is also the case where EDFD serves its most important function: it converts a subjective sense of urgency ("v2 seems to be getting flaky") into a specific, calendar-derived deadline ("at this burn rate, we must complete v3 cutover by day 81, not day 90"). Numbers create accountability; feelings do not.

---

## 8. Webhook Format Migration — Expanded Blast Radius

The scope of the Stripe v3 migration is not limited to the Payment Service. Stripe v3 sends webhooks in a new format. Any service that processes Stripe webhooks must be updated before v3 can operate at 100% of production traffic.

**Services affected beyond Payment Service:**

**Order Management Service** receives payment confirmation webhooks to transition orders from "payment pending" to "payment confirmed" state. If Order Management still expects v2 webhook format and v3 webhooks arrive, orders will not transition. Customers complete checkout but orders remain in pending state indefinitely. This is a silent failure — no errors are generated, no alerts fire, but orders are not fulfilled. The impact is discovered through support tickets, not monitoring.

**Notification Service** receives payment confirmation webhooks to trigger the payment receipt email. If the v3 webhook format is not handled, customers who pay successfully receive no email confirmation. Again, this is silent: no errors, no alerts, no SLA breach visible in the metrics — only a support ticket spike 24–48 hours later.

**Webhook router** (if one exists as an intermediary) must be updated to parse v3 event types and route them to the correct downstream consumers. If the router is a shared infrastructure component, its update is a dependency that blocks both Order Management and Notification Service from being v3-ready.

**Consequence for SCW:** The SCW for the Payment Service (60 days, as computed in section 4) is the minimum SCW. The effective SCW for the migration is determined by the last service to be v3-compatible. If Order Management is ready at day 45 but Notification Service is delayed to day 55, the effective SCW end is day 55 — 5 days of additional dual-format operation for Order Management with no benefit.

SRE must treat the webhook migration as a parallel workstream with its own timeline, its own MRI assessment, and its own PRR gate. The overall migration is not complete until all three services (Payment, Order Management, Notification) have passed their individual PRR gates and are running v3 webhooks in production.

---

## 9. Post-Migration Validation — 30-Day Observation Window

Once v3 is live at 100% traffic and v2 has been decommissioned, the migration is operationally complete but not declared stable. A 30-day observation window is required before the migration is closed in the risk register.

**Validation criteria:**

**MTBI stability.** Compute MTBI for the Payment Service for the 90 days preceding migration and the 30 days following. MTBI should be equal to or greater than pre-migration baseline. A declining MTBI (more frequent incidents) after v3 cutover indicates that the new integration has introduced instability that was not visible during the canary window.

**MTTR unchanged.** Measure median MTTR for payment-related incidents during the 30-day window. If MTTR has increased, the v3 integration has introduced failure modes that on-call engineers cannot yet diagnose efficiently. This signals a runbook gap — the team has not yet documented the v3-specific failure modes and their resolutions.

**SCS recomputed.** After v3 is live, recompute SCS using Stripe v3 SLA. Stripe's v3 SLA is the same as v2 (99.9%), so SCS remains 0.9995. This confirms that the structural risk documented before migration (section 2) has not changed. The risk register entry remains open.

```
SCS_post_migration = 0.999 / 0.9995 = 0.9995
```

**Error budget recovery.** Confirm that EBV has returned to 1.0 or below within 7 days of v3 full cutover. If EBV remains elevated after v3 is at 100%, the source of budget burn is no longer v2 degradation — it is a v3 integration defect. This requires immediate investigation.

**EDFD status after migration.** Once v3 is live at 100%, the EDFD concept becomes undefined for this migration. There is no longer a deprecation forcing function. The formula `EDFD = today + (EBR_reserved / daily_EBV_burn_from_deprecation_errors)` requires a non-zero deprecation error burn rate in the denominator. With v2 decommissioned, deprecation error burn is zero. EDFD collapses to undefined — which is the correct state. A defined EDFD is a signal of ongoing external pressure. An undefined EDFD is a signal that the external pressure has been resolved.

The 30-day observation window closes when MTBI is stable, MTTR is unchanged, EBV is at 1.0, and the risk register entry for the Stripe SLA gap has been updated to reflect that the migration risk (v2 sunset) is closed, while the structural risk (SCS < 1.0) remains open for a separate workstream.

---

## Summary — Key Numbers at a Glance

| Metric | Value | Derived From |
|--------|-------|-------------|
| Checkout SLA | 99.95% | System contract |
| Stripe SLA (v2 and v3) | 99.9% | Vendor contract |
| SCS | 0.9995 | 0.999 / 0.9995 |
| Monthly error budget | 21.9 min | System contract |
| Budget consumed this month | 7.0 min | Current state |
| EBR reserved for migration | 6.57 min | 30% × 21.9 |
| Remaining usable budget | 8.33 min | 14.9 − 6.57 |
| EDFD (at 0.2 min/day v2 burn) | Day 101 from today | 8.33 / 0.2 from day 60 |
| EDFD (at 0.4 min/day burn) | Day 81 from today | 8.33 / 0.4 from day 60 |
| SCW | 60 days | Day 30 to day 90 |
| MRI (baseline OCR 0.457) | 0.507 | Formula — above threshold |
| MRI (improved OCR 0.95) | 0.047 | Formula — low risk |
| Services requiring v3 updates | 3 | Payment, Order Mgmt, Notification |
| Rollback window close | Day 90 | Stripe v2 sunset |

---

*Document version: 1.0 | Scenario class: Third-Party API Deprecation | System: Shopping Cart EKS | Author: SRECapstone Program*
