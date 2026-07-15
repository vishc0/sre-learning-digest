# Scenario 02 — Feature Flag-Gated Launch: "Buy Now" One-Click Checkout

**System**: Shopping Cart — 12 microservices, Checkout CD=5, SLA 99.95%  
**Monthly Error Budget**: 21.9 minutes | **Consumed**: 8 minutes (37%) | **Remaining**: 13.9 minutes  
**Feature**: Buy Now one-click checkout — new code path in Cart Service and Payment Service  
**Flag Platform**: LaunchDarkly | **Rollout Plan**: 1% → 5% → 25% → 100% over 5 days  
**Claim from Product**: "Tested in staging for 2 weeks"

---

## Section 1 — Concept: Feature Flag-Gated Launch from an SRE Perspective

A feature flag-gated launch is a controlled exposure mechanism. The feature ships to production — fully deployed, fully wired — but execution is governed by a runtime configuration switch rather than a code deployment. Traffic is progressively routed to the new code path while the baseline path remains available for immediate reversion. From an SRE perspective, this is not a deployment strategy; it is a **change exposure strategy**.

The critical distinction is that a feature flag decouples **deployment** from **activation**. In a trunk-based full deployment, the moment a service restarts with new code, 100% of traffic hits that code. Any miscalculation in load behavior, edge case handling, or downstream dependency response becomes immediately a production incident at full blast radius. A flag-gated rollout limits the blast radius to the cohort size at each increment, and that cohort can be snapped back to zero in seconds without a code rollback.

**What feature flags do not eliminate:**

- **State side effects**: if the new code path writes to a database, queue, or cache in a format incompatible with the baseline path, flag rollback does not undo that state. The data corruption persists.
- **Latent errors in small cohorts**: at 1% traffic, rare failure modes — those triggered by specific product combinations, account ages, or concurrent session states — may not surface until higher percentages.
- **Flag evaluation overhead**: every request must evaluate flag state, adding latency. This latency is negligible at low flag complexity but accumulates under high cardinality targeting rules.
- **Infrastructure coupling**: if the new code path provisions new infrastructure (a new queue, a new DynamoDB table, a new external API call), disabling the flag stops the code path but does not deprovision the infrastructure or cancel in-flight requests.

SRE's role in a flag-gated launch is not to bless the feature. SRE governs the **exposure cadence**, owns the **rollback threshold**, and enforces the **error budget gate**. The product team's confidence in the feature is an input to the conversation — not the decision.

---

## Section 2 — The Principal SRE's Assessment: Evaluating a Flag Launch Request

When a team brings a flag-gated launch request, a Principal SRE evaluates it in four sequential layers. Skipping layers creates blind spots that become incidents.

**Layer 1 — Change Volatility Assessment (SCV)**

The first question is: which services does this feature touch, and how does it change their volatility profile? Buy Now adds new logic to Cart Service (P0) and Payment Service (P0). Both services are on the critical path of the Checkout journey at CD=5. The Service Change Volatility (SCV) for this feature is high: two P0 services are receiving new code paths simultaneously, and those code paths interact with each other (Cart orchestrates the one-click order, Payment processes the charge). A failure in Cart's Buy Now path that causes a malformed payment request does not surface as a Cart error — it surfaces as a Payment error. Cross-service failure attribution is harder to diagnose under flag-gated partial exposure.

**Layer 2 — Error Budget Gate (EBR check)**

Before any rollout increment is approved, the remaining error budget must be sufficient to absorb a rollback-level event. This is not a courtesy check — it is a hard gate. With 13.9 minutes remaining, SRE must calculate the Error Budget Reservation requirement and verify that the current balance clears it.

**Layer 3 — Signal Threshold Readiness (RST)**

At 1% traffic, the cohort is too small to produce statistically valid error rate signals. SRE must calculate the Rollout Signal Threshold — the minimum rollout percentage at which the feature's error rate delta is distinguishable from baseline noise. Approving a gate advance before RST is reached is operationally meaningless: you cannot confirm the feature is healthy when you cannot hear the signal.

**Layer 4 — Rollback Velocity Verification (RV)**

The final question before approving any rollout increment: if something goes wrong right now, how fast can this be reversed? SRE must verify that the LaunchDarkly flag can be disabled in production in under 60 seconds, that the flag kill is operationally rehearsed (not theoretical), and that there is no state side effect that survives the flag kill.

---

## Section 3 — RST Calculation for Buy Now

**Formula**: `RST = min% where (feature_error_rate − baseline_error_rate) / σ_baseline ≥ 2`

This formula asks: at what cohort size does a 2-sigma deviation from baseline become detectable? Below RST, noise swamps signal. Above RST, a meaningful error rate increase will be statistically visible.

**Given values:**
- Total checkout volume: 50,000 transactions/day
- Baseline error rate: 0.05% (25 errors/day across all 50,000 transactions)
- Assume errors follow a Poisson distribution; σ_baseline ≈ √(n × p × (1−p))

**At 1% rollout (500 transactions/day):**

Expected baseline errors in cohort: 500 × 0.0005 = 0.25 errors/day  
σ_baseline at this cohort: √(500 × 0.0005 × 0.9995) ≈ √0.2499 ≈ 0.50

For a 2-sigma signal: feature_error_rate must exceed 0.25 + (2 × 0.50) = 1.25 errors/day in the cohort.  
That is (1.25 / 500) = **0.25% error rate** — five times the baseline — before the signal is detectable.

**At 5% rollout (2,500 transactions/day):**

Expected baseline errors: 2,500 × 0.0005 = 1.25 errors/day  
σ_baseline: √(2,500 × 0.0005 × 0.9995) ≈ √1.249 ≈ 1.12

2-sigma threshold: 1.25 + (2 × 1.12) = 3.49 errors/day = 0.14% error rate in cohort.

**At 25% rollout (12,500 transactions/day):**

Expected baseline errors: 12,500 × 0.0005 = 6.25 errors/day  
σ_baseline: √(12,500 × 0.0005 × 0.9995) ≈ √6.247 ≈ 2.50

2-sigma threshold: 6.25 + (2 × 2.50) = 11.25 errors/day = 0.09% error rate in cohort — now close to baseline.

**Conclusion:** RST is not met until approximately the 5%–10% rollout band. At 1%, the error signal is only detectable if the feature's error rate is five times the baseline — a catastrophic failure mode, not a subtle regression. The 1% gate is not a validation gate; it is a catastrophic failure check only. SRE must not treat a clean 1% observation as feature health confirmation.

---

## Section 4 — Error Budget Gate: Can This Rollout Proceed?

**Current state**: 8 minutes consumed, 13.9 minutes remaining.

**Error Budget Reservation (EBR) formula:**

`EBR = min(MRI × 0.05, 0.80)` — where MRI is the Migration Risk Index for this change.

For Buy Now, MRI is elevated: two P0 services modified, new cross-service interaction, new external code path affecting payment processing. A reasonable MRI for this change is 0.65 (high-risk change on critical path services). 

`EBR = min(0.65 × 0.05, 0.80) = min(0.0325, 0.80) = 0.0325`

EBR = 3.25% of monthly error budget must be held in reserve = 0.0325 × 21.9 = **0.71 minutes** reserved.

**Available budget for rollout**: 13.9 − 0.71 = **13.19 minutes**.

At current consumption of 37%, the rollout is within budget to proceed — the reservation is satisfied. However, the rollout proceeds **on condition**: if error budget consumption crosses 60% (13.14 minutes consumed) at any point during rollout, the next increment is blocked until the burn rate normalizes.

**EBV trigger for automatic rollout pause:**

Error Budget Velocity (EBV) = traffic_normalized_error_rate / baseline_rate.

If EBV > 2.0 during any rollout increment — meaning the feature is burning error budget at more than twice the baseline rate — the rollout is automatically paused. At the current baseline of 25 errors/day across 50,000 transactions, an EBV of 2.0 corresponds to 50 errors/day system-wide, or approximately 0.10% error rate. Any SLO burn rate alert firing during rollout is treated as an EBV > 2.0 signal until proven otherwise.

---

## Section 5 — BRI During Rollout: Quantifying Blast Radius

**Formula**: `BRI = (affected_users / total_users) × journey_criticality × tier_weight`

For the Checkout journey: journey_criticality = 1.0 (highest, direct revenue impact). Cart and Payment are both P0: tier_weight = 1.0.

| Rollout % | Affected Users (of 50K) | BRI Calculation | BRI Score |
|-----------|------------------------|-----------------|-----------|
| 1% | 500 | (500/50,000) × 1.0 × 1.0 | 0.010 |
| 5% | 2,500 | (2,500/50,000) × 1.0 × 1.0 | 0.050 |
| 25% | 12,500 | (12,500/50,000) × 1.0 × 1.0 | 0.250 |
| 100% | 50,000 | (50,000/50,000) × 1.0 × 1.0 | 1.000 |

A BRI of 0.25 at 25% rollout means one in four checkout users is exposed to a potential Buy Now failure. Given that Payment Service is P0 and a failure in the Buy Now payment path could cascade to order creation failures in Order Management (also P0), the effective blast radius at 25% is not just 25% of users — it is 25% of users on a CD=5 journey where a failed payment may leave an orphaned cart state, a duplicate charge attempt, or an unfulfillable order. SRE must ensure the 25% gate includes explicit verification that no cross-service state corruption is occurring.

---

## Section 6 — Rollout Cadence with SRE Gates

Each increment requires a formal go/no-go before the next percentage is enabled in LaunchDarkly.

**Gate 0 → 1% (Day 0, Hour 0)**

Go criteria: EBR satisfied (confirmed above). Flag kill rehearsed in production within 24 hours. Monitoring dashboards active and verified to capture Buy Now-specific metrics. Latency budget per hop (LBH) baseline established for Cart and Payment before flag enable. No active P0/P1 incidents on any checkout-path service.

**Gate 1% → 5% (Day 1, minimum 24 hours at 1%)**

Go criteria: Zero error rate delta detectable at 1% (acknowledging RST limitations — any signal at 1% is a stop signal). p99 latency for Cart and Payment within 10% of pre-rollout baseline. EBV < 2.0 for the observation window. No LaunchDarkly SDK errors or flag evaluation failures in application logs.

**Gate 5% → 25% (Day 2, minimum 24 hours at 5%)**

Go criteria: RST is now in range — error rate signal is statistically valid. Feature error rate must be within 1-sigma of baseline error rate (not just below 2-sigma alert threshold, but actively comparable). Payment success rate for Buy Now cohort ≥ Payment success rate for standard checkout. Order Management receiving well-formed order payloads from Buy Now path (spot-check 100 orders). EBV < 1.5. Error budget consumed < 55% of monthly total.

**Gate 25% → 100% (Day 4, minimum 48 hours at 25%)**

Go criteria: Feature error rate statistically indistinguishable from baseline across a 48-hour window including at least one peak traffic period. No data anomalies in inventory deduction, payment ledger, or order state for Buy Now orders. p99 latency at 25% matches p99 at baseline (no latency regression from additional Buy Now logic). Error budget consumed < 65% of monthly total. Explicit sign-off from SRE lead and an on-call engineer confirmed for the 100% window.

---

## Section 7 — Monitoring Plan

**Metrics required before flag enable:**

- `buy_now_checkout_error_rate` — separate from standard checkout error rate; must be tagged by LaunchDarkly cohort
- `buy_now_payment_success_rate` — Payment Service must instrument Buy Now payment attempts distinctly
- `buy_now_cart_latency_p99` — Cart Service latency for the new code path specifically
- `buy_now_order_creation_success` — Order Management order creation rate for Buy Now-sourced orders
- `feature_flag_evaluation_errors` — LaunchDarkly SDK errors; a spiking flag evaluation failure rate means traffic is falling back to default (potentially all-off or all-on depending on flag configuration)

**Alert thresholds:**

| Alert | Threshold | Action |
|-------|-----------|--------|
| Buy Now error rate | > 2× baseline for 5 minutes | Page on-call; pause rollout |
| EBV | > 2.0 for 10 minutes | Automatic flag kill via LaunchDarkly API |
| Cart p99 latency | > 110% of pre-rollout baseline | Warn; hold current increment |
| Payment success rate delta | > 1% below baseline | Page on-call; pause rollout |
| LaunchDarkly SDK error rate | > 0.1% of evaluations | Immediate investigation; flag behavior undefined |

**EBV trigger for automatic flag kill**: configure a Terraform-managed alert in the observability stack that calls the LaunchDarkly API `PATCH /api/v2/flags/{projectKey}/{featureKey}` with `{"on": false}` when EBV > 2.0 persists for more than 10 minutes. This is not a human decision — it is an automated circuit breaker. The on-call engineer is paged simultaneously but the flag kill does not wait for human acknowledgment.

---

## Section 8 — Rollback Plan and Residual Error State

**Rollback Velocity (RV)**: The LaunchDarkly flag kill, when triggered (manually or automatically), propagates to SDK clients within the SDK polling interval. For server-side SDKs, the default streaming connection means flag state changes propagate in under 500 milliseconds. The effective RV for this feature is **sub-60 seconds** from decision to full flag-off across all Cart and Payment service instances — assuming no custom polling interval has been set above the default.

**Residual error state after rollback:**

Disabling the flag stops new Buy Now requests. It does not resolve:

1. **In-flight transactions**: any Buy Now request already in Cart or Payment at the moment of flag kill will complete on the new code path. These must be allowed to resolve (success or failure) before declaring rollback complete.
2. **Payment pre-authorizations**: if Buy Now pre-authorizes a payment card before the flag kill, that authorization remains in the payment gateway. Cancellation logic must be verified — does the standard checkout cancel path handle Buy Now pre-authorizations correctly, or does a separate cleanup be required?
3. **Orphaned cart state**: if Buy Now modifies cart state before a payment failure and flag kill occurs mid-transaction, the user's cart may be in an inconsistent state. The Cart Service must be verified to handle this scenario gracefully, ideally with a compensating transaction or a cart state reset on next page load.
4. **Order Management partial records**: any Buy Now order that reached Order Management before flag kill will appear in the order ledger. These orders are real and must be fulfilled or cancelled — they do not disappear with the flag.

---

## Section 9 — Common Failure Patterns in Feature Flag Launches

**Pattern 1: Flag Not Respected by All Clients**

The LaunchDarkly flag is enabled at 5%, but a subset of Cart Service instances are running an older SDK version that does not receive the streaming update correctly. Those instances fall back to the flag's default state. If the default is `on`, those instances run Buy Now for all traffic. If the default is `off`, those instances run zero Buy Now traffic. In either case, the actual traffic distribution no longer matches the intended 5%, and the EBV calculation is based on a false denominator. Detection: monitor LaunchDarkly SDK evaluation counts per service instance and compare against expected traffic distribution.

**Pattern 2: Error Masking by Retry Logic**

Payment Service has a client-side retry with exponential backoff on transient failures. A Buy Now payment request fails on the first attempt (due to a bug in the one-click payload format), retries successfully on the second attempt, and is logged as a success. The error is masked. Error rate metrics show green. The actual failure rate is hidden in retry counters that are not surfaced in the primary SLO dashboard. Detection: monitor retry rate as a leading indicator alongside error rate; a rising retry rate with a flat error rate is a masking signal.

**Pattern 3: State Pollution Between Cohorts**

At 25% rollout, Buy Now users share the Redis cart cache with standard checkout users. The Buy Now code path writes a new field (`buy_now_session_token`) to the cart object. The standard checkout code path does not expect this field and, depending on deserialization strictness, may fail silently, log warnings, or produce incorrect cart totals for non-Buy Now users. State pollution crosses the flag boundary — non-Buy Now users are affected by a flag they are not part of. Detection: monitor error rates for both the Buy Now cohort and the standard checkout cohort simultaneously during rollout; a rising standard checkout error rate during a Buy Now flag increment is the signature of state pollution.

**Pattern 4: Gradual Data Corruption**

Buy Now creates a slightly different order record structure — perhaps omitting a field that Order Management considers optional but that downstream reconciliation jobs treat as required. At 1% and 5%, the volume of corrupt records is small enough that the reconciliation job processes them without visible error (or logs errors that are not alerted on). By 100%, the reconciliation backlog is large enough to cause visible failures in payment settlement or inventory adjustment, days after the rollout completed. Detection: instrument downstream jobs (reconciliation, inventory sync, payment ledger) with record-format validation that fires immediately on malformed inputs, not on job failure. Catching schema drift at the point of record creation, not at the point of downstream processing, is the only reliable prevention.

---

## Section 10 — Staging vs. Production Validation: Why Two Weeks of Staging Does Not Reduce RST

The RST is a statistical threshold derived from production traffic volume, production error distribution, and production noise characteristics. Staging validation does not alter any of these parameters.

**Staging cannot replicate production in four specific ways:**

First, **traffic volume and distribution**: staging typically runs at a fraction of production volume, with synthetic or replayed traffic that does not capture the full distribution of user behavior, device types, account ages, and concurrent session patterns. The rare conditions that trigger edge case failures — a cart with 47 items, a payment account with an expired card on file from a previous failed transaction, a concurrent session from two devices — are underrepresented or absent in staging.

Second, **real dependency behavior**: payment gateways, fraud detection services, and third-party inventory feeds in staging are either mocked, pointed at sandbox environments, or run at reduced capacity. A Buy Now payment flow that works against a Stripe sandbox may fail against the production Stripe API under specific response timing conditions that the sandbox does not simulate.

Third, **production data state**: staging databases are typically anonymized snapshots or synthetic datasets. Production accounts carry years of accumulated state — subscription histories, loyalty point balances, address books, stored payment methods — that create interaction patterns staging cannot reproduce.

Fourth, **infrastructure behavior at scale**: a Cart Service pod in staging handles tens of requests per minute. In production, it handles thousands. The new Buy Now code path may introduce a memory allocation pattern, a connection pool contention point, or a database query that performs acceptably at low concurrency and degrades nonlinearly at production load.

**Two weeks of staging testing provides confidence that the feature is functionally correct under controlled conditions.** It does not provide confidence that it is operationally stable under production conditions. RST is the mechanism for acquiring that production confidence incrementally, with a controlled blast radius. The staging duration is an input to the feature's functional readiness assessment — it has no bearing on the statistical signal threshold that governs production rollout. A feature that has been in staging for two weeks and one that has been in staging for two days both require the same RST to be met before a gate advance is approved. RST is a production measurement, not a staging measurement.

---

## Summary: The Principal SRE's Verdict on This Rollout

The Buy Now rollout may proceed under the following conditions: EBR is satisfied (confirmed — 13.9 minutes remaining clears the 0.71-minute reservation). Flag kill is rehearsed and automated circuit breaker is wired. Monitoring instrumentation for Buy Now-specific metrics is in place before flag enable. The 1% gate is treated as a catastrophic failure check only — not a health confirmation. No gate advance before RST is reached at the 5%–10% band. Error budget consumption is checked at every gate; if it crosses 60%, the next increment is blocked. The product team's two weeks of staging testing is noted and is not a factor in any RST or gate calculation.

The feature is not approved because it is well-tested. It is approved because the error budget can absorb the exposure, the rollback velocity is acceptable, the blast radius is bounded, and the signal threshold will be reachable before the exposure becomes material. Those are SRE's criteria — not staging duration.
