# Scenario 01 — Greenfield Service Addition: Wishlist Service

**System**: Shopping Cart (12 microservices on EKS)
**Event**: Engineering team proposes adding a new Wishlist Service to the Browse journey
**SRE Role**: Principal SRE conducting pre-production reliability assessment

---

## 1. Concept — What Greenfield Service Addition Means to an SRE

A greenfield service addition is not a feature release. A feature release modifies the behavior of a service that already exists in production with a known reliability baseline, established observability, and a measured error budget. A greenfield service has none of these. It has no history, no measured failure modes, no proven operator instincts, and no calibrated alert thresholds.

The engineering team's definition of "ready for production" is almost always scoped to functional correctness: does it do what the ticket says? The SRE's definition of production readiness is scoped to reliability contracts: can this service be placed on the critical path of a customer journey without degrading the SLA we have promised?

These are different questions. Answering one does not answer the other.

What makes greenfield addition specifically risky in ways that are not obvious:

**The trust inheritance problem.** When a new service joins an existing call chain, it inherits the trust of every service around it. If Browse was meeting its 99.5% SLA, and Wishlist is introduced into the Browse call chain, customers experience Browse SLA — not Wishlist SLA. The new service's immaturity is invisible to the customer until it causes a failure, at which point it is no longer a Wishlist problem. It is a Browse incident.

**The observability gap.** Every other service in the system has months or years of alerting calibration. Thresholds are tuned. Runbooks exist. On-call engineers have seen the failure modes. Wishlist has none of this. When it fails for the first time in production, the on-call engineer is diagnosing a service they have never seen fail before, without runbooks, without baseline metrics, in the middle of a customer-impacting incident.

**The cascading tail.** Greenfield services frequently have unoptimized code paths. A synchronous call to an unoptimized service on a hot path adds latency that is not just additive — it compounds across concurrent requests, increases queue depths in upstream services, and can trigger cascading timeouts if the latency budget is already tight.

**The dependency footprint.** New services introduce new dependency edges into the dependency graph. Each edge is a potential failure mode. A service with 5 dependencies that has never been load-tested under production traffic patterns has 5 untested failure modes, each of which can propagate upstream.

---

## 2. The Principal SRE's First 5 Questions

When a Principal SRE hears "we're adding a new service," these are the first five questions — before reading any design doc, before reviewing any code.

**Q1: Which customer journeys does this service join, and at what call depth?**
The journey and call depth determine the mathematical SLO the service must maintain. This is not negotiable. The number comes from the SLO coherence formula, not from a conversation.

**Q2: Is the service on the synchronous critical path, or is it an async enrichment?**
A service that is called synchronously blocks the request. Its latency and availability directly degrade the customer journey. An async service enriches data after the response is returned. The reliability requirements differ by orders of magnitude. The team's answer to this question determines whether the SRE engagement is a light review or a full PRR.

**Q3: What are the service's transitive dependencies, and what tier are they?**
Every dependency the new service takes on becomes a new failure mode in the call chain. A dependency on a P0 service is lower risk than a dependency on a P2 service, because P0 services already have rigorous SLOs. A dependency on a P2 service introduces a high-entropy node into a potentially low-entropy journey.

**Q4: What is the test coverage percentage, and what does the canary plan look like?**
Test coverage is not a proxy for quality — it is a proxy for known behavior space. Low coverage means more of the service's behavior is unknown. The canary plan determines how much production blast radius is available while the unknowns are discovered.

**Q5: What is the rollback plan if the service fails in production?**
The failure question is not whether the service will fail. All services fail. The question is whether the failure is recoverable without a customer SLA breach. A service with no graceful degradation path and no rollback mechanism is not production-ready regardless of its test coverage.

---

## 3. SRE Assessment Sequence

The assessment follows a fixed sequence. Order matters because each step constrains the next.

**Step 1 — Journey impact mapping.** Identify every customer journey the service touches. For each journey, record the current CD and the new CD after the service is added. A CD increase is a structural change to the reliability architecture — it requires re-derivation of all per-service SLOs on that journey.

**Step 2 — SLO coherence check.** Re-derive the required per-service SLO for the new service using the RIR formula. Verify that the derived SLO is achievable given the service's architecture. If the required SLO is 99.8% and the service has a single point of failure with no redundancy, the architecture must change before the service joins the call chain.

**Step 3 — Latency budget audit.** Determine the maximum latency budget per hop on the affected journeys using the LBH formula. Verify that the new service's p99 latency under load fits within the budget. If it does not, the service cannot be placed on the synchronous critical path.

**Step 4 — Dependency gravity assessment.** Enumerate all dependencies of the new service. For each dependency, assess its tier and its SLO. Compute the GEI to quantify the combined exposure from dependency breadth and canary maturity.

**Step 5 — Observability gap analysis.** Verify that the service emits the four required signal types before production: request rate, error rate, latency distribution (p50/p95/p99), and saturation (CPU, memory, connection pool utilization). A service that does not emit these signals cannot be safely canary-monitored.

**Step 6 — PRR gate evaluation.** Run the Production Readiness Review against the specific pass/fail criteria for the service tier. The Wishlist Service, because it joins the Browse journey's synchronous call chain, is treated as a P1 service for PRR purposes.

**Step 7 — Canary plan review.** Confirm the canary duration, traffic percentage ramp schedule, automated rollback triggers, and who is on-call during the canary window. The canary is not a courtesy — it is the SRE's primary mechanism for discovering unknown failure modes in a controlled blast radius.

---

## 4. Formulae Applied — Wishlist Service Numbers

### 4.1 Call Depth Change (Browse Journey)

Before Wishlist: `Browse CD = 2` (API Gateway → Product Catalog → Search)
After Wishlist: `Browse CD = 3` (API Gateway → Product Catalog → Wishlist → Search, or parallel path that adds one synchronous hop)

This is a structural change. Every formula below uses the new CD of 3.

### 4.2 RIR — Reliability Inheritance Requirement

The RIR formula derives the minimum SLO the Wishlist Service must maintain to preserve the Browse journey SLA.

```
RIR = consumer_SLO ^ (1 / (CD_existing + 1))
```

Browse SLA = 99.5% = 0.995
CD after adding Wishlist = 3
CD_existing for the formula = the new total CD = 3

```
RIR = 0.995 ^ (1 / (3 + 1))
RIR = 0.995 ^ 0.25
RIR = 0.99875
```

The Wishlist Service must maintain **99.875% availability** to allow the Browse journey to meet its 99.5% SLA. This is the floor. The SRE does not negotiate this number — it is derived from the contract.

### 4.3 SCS — SLO Coherence Score (Before and After)

SCS measures whether the per-service SLOs actually multiply out to produce the customer SLA.

```
SCS = per_service_SLO ^ CD / customer_SLA
```

Assume before Wishlist, all Browse journey services were at 99.75% SLO, CD=2:
```
SCS_before = 0.9975 ^ 2 / 0.995 = 0.995006 / 0.995 = 1.000006
```
Score of ~1.0 means the math is coherent — the per-service SLOs produce exactly the customer SLA.

After Wishlist (CD=3), if Wishlist is provisioned at 99.875% and the other services remain at 99.75%:
```
SCS_after = (0.9975 × 0.9975 × 0.99875) / 0.995
SCS_after = 0.99376 / 0.995 = 0.9987
```
A score below 1.0 means the system is under-provisioned relative to its SLA commitment. The SRE must raise per-service SLOs, reduce CD, or accept that the Browse SLA will be missed. In this case, Wishlist must run at 99.9%+ to restore SCS to ≥1.0.

### 4.4 GEI — Greenfield Exposure Index

```
GEI = (new_transitive_deps × avg_dep_tier_weight) / (test_coverage_pct × canary_duration_hours)
```

Wishlist dependencies: Product Catalog (P1, weight=0.6), User Profile (P2, weight=0.8), Recommendation Engine (P2, weight=0.8), Redis (P0-infra, weight=0.2), Postgres (P1, weight=0.6).

Tier weights reflect entropy: P0=0.2 (highly controlled), P1=0.6 (moderate), P2=0.8 (higher entropy), P3=1.0 (lowest maturity).

```
avg_dep_tier_weight = (0.6 + 0.8 + 0.8 + 0.2 + 0.6) / 5 = 3.0 / 5 = 0.60
new_transitive_deps = 5
test_coverage_pct = 0.72
canary_duration_hours = 48

GEI = (5 × 0.60) / (0.72 × 48)
GEI = 3.0 / 34.56
GEI = 0.087
```

GEI interpretation: values below 0.1 are acceptable for P1 services. At 0.087, Wishlist is just inside the threshold, but only because the 48-hour canary provides meaningful exposure time. If the team had proposed a 24-hour canary, GEI would be 0.174 — above threshold, requiring either extended canary or reduced dependency count. This is the quantitative argument for holding the team to 48 hours minimum.

### 4.5 LBH — Latency Budget Per Hop

Browse journey has a p99 latency SLA of 800ms (from the framework document). With CD=3, each synchronous hop receives an equal budget share as a starting point:

```
LBH = total_journey_latency_budget / CD
LBH = 800ms / 3 = 266ms per hop
```

The Wishlist Service must demonstrate p99 latency ≤ 266ms under production-representative load before it is placed on the synchronous Browse path. If load testing shows p99 at 380ms, the service cannot join the synchronous path until the code is optimized. The alternative is to make the Wishlist call async and return a cached wishlist state, removing it from the synchronous CD count.

---

## 5. The Production Readiness Review (PRR) Gate

The PRR is a structured pass/fail gate. Every criterion below must be met before the service is approved for production canary. There are no partial passes.

### Tier 1 — Hard Blockers (any failure = no production)

| Criterion | Requirement | Wishlist Status |
|-----------|-------------|-----------------|
| Circuit breaker implemented | All synchronous dependencies wrapped | Must verify |
| Graceful degradation defined | Browse journey continues if Wishlist returns 503 | Must be architected |
| Rollback plan documented | Canary rollback automated, < 5 min | Must be in runbook |
| Secret management | All credentials via Secrets Manager or Vault | Must verify |
| Load test completed | p99 latency ≤ LBH (266ms) at 2× peak Browse traffic | Must run |
| Dependency health checks | All 5 dependencies have health check probes | Must verify |

### Tier 2 — Gating Conditions (failure requires waiver from Principal SRE)

| Criterion | Requirement |
|-----------|-------------|
| Test coverage | ≥ 80% (Wishlist is at 72% — gap of 8 points requires waiver or remediation) |
| Runbook exists | At least 3 known failure modes documented with resolution steps |
| On-call trained | At least 2 engineers trained on the service before canary starts |
| Alerting configured | Rate, error, latency, saturation alerts all set before canary |
| Dependency SLO contracts | Formal SLO agreement from User Profile and Recommendation Engine (both P2) |

### Tier 3 — Recommendations (failure noted but does not block)

- Chaos test for Redis failure mode (simulate Redis unavailability and verify Browse degrades gracefully)
- Rate limiting on all inbound calls
- Structured logging with correlation IDs matching the Browse journey trace format

Note on the 72% test coverage gap: this is a Tier 2 condition, not a Tier 1 blocker, because test coverage measures known behavior, not operational readiness. However, the Principal SRE should require a waiver acknowledgment from engineering leadership, documented in the PRR record, stating that the team accepts the elevated risk of undiscovered edge cases.

---

## 6. Monitoring Strategy During Canary Rollout

The canary window is 48 hours at 5% Browse traffic, increasing to 25% at hour 24 if no alerts fire, and to 100% at hour 48 if the service remains within all thresholds.

### Primary Signals (alert = auto-rollback)

| Signal | Threshold | Rationale |
|--------|-----------|-----------|
| Wishlist error rate | > 0.1% over any 5-minute window | RIR requires 99.875% — any sustained error rate above 0.1% threatens this |
| Wishlist p99 latency | > 266ms | LBH for Browse CD=3 journey |
| Browse journey error rate | Increase > 0.05% vs. pre-canary baseline | Canary must not degrade the host journey |
| Browse journey p99 latency | Increase > 50ms vs. pre-canary baseline | Latency regression is an early failure signal before errors appear |

### Secondary Signals (alert = human escalation, not auto-rollback)

| Signal | Threshold | Why Human Decision |
|--------|-----------|-------------------|
| Wishlist connection pool saturation | > 70% | May indicate load spike, not failure — needs context |
| Redis cache miss rate | > 40% | Could be cold cache after deploy, or a real misconfig |
| User Profile dependency error rate | > 0.2% | Could be upstream issue unrelated to Wishlist canary |
| Wishlist pod restart count | > 2 in any 10-minute window | OOMKill or crash loop — needs investigation, not blind rollback |

### Canary Dashboard Requirements

The on-call engineer must be able to see, on a single dashboard without drilling down: Wishlist request rate, error rate, p50/p95/p99 latency, pod count, and the Browse journey error rate and latency delta versus the control group. If these are not on a single panel before canary starts, canary does not start.

---

## 7. SLO Coherence Re-evaluation — Browse Journey After Wishlist

With CD increased from 2 to 3, all per-service SLOs on the Browse journey must be re-derived to maintain SCS ≥ 1.0.

Browse SLA: 99.5%. Three services on synchronous path: Product Catalog, Wishlist, and one routing layer. For the SCS to equal 1.0 with CD=3:

```
per_service_SLO ^ 3 = 0.995
per_service_SLO = 0.995 ^ (1/3) = 0.99833
```

Every service on the Browse synchronous path now requires a minimum SLO of **99.833%**. Before Wishlist was added, the required per-service SLO with CD=2 was:

```
0.995 ^ (1/2) = 99.75%
```

The Browse journey's addition of Wishlist has increased the required per-service SLO for every participating service from 99.75% to 99.833%. This affects Product Catalog (P1) and the API Gateway layer, not just Wishlist. The Principal SRE must inform the Product Catalog team that their SLO target has increased as a consequence of this architecture change.

---

## 8. Common Failure Patterns — First 30 Days

Based on operational experience with greenfield service introductions, four failure patterns account for the majority of incidents.

**Pattern 1 — Latency cliff under burst traffic.** The service performs acceptably during load tests run at steady-state traffic. On day 3 or 4, a Browse traffic burst (sale event, marketing email, social media spike) arrives. The service has not been tested at burst, its connection pool to Postgres or Redis is undersized for burst concurrency, and p99 latency spikes from 180ms to 900ms within 60 seconds. Browse journey p99 exceeds 800ms. SLA breach. Prevention: load test at 3× peak, not 2×. Size connection pools for burst, not average.

**Pattern 2 — Dependency failure propagation.** User Profile (P2) or Recommendation Engine (P2) has a brief outage. The Wishlist Service has no circuit breaker on these dependencies, so requests hang waiting for timeouts rather than failing fast. Browse requests pile up waiting for Wishlist. Upstream timeout cascades. Prevention: circuit breaker on every outbound dependency call, with a defined fallback response (empty wishlist, not an error).

**Pattern 3 — Silent data corruption.** The service returns 200 OK with subtly wrong data — wrong user's wishlist, duplicate items, missing items. No alert fires because error rate is 0% and latency is nominal. Customers notice after hours or days. Prevention: data validation at write boundaries, read-back verification on writes, anomaly detection on wishlist item counts per user.

**Pattern 4 — Alert threshold miscalibration.** The team sets error rate alert at 1% because "that's what we used in the load test." Under production traffic, a 0.3% error rate affecting high-value Browse users triggers enough customer contacts to create a P1 incident. The alert fires only at 1%. On-call had no signal. Prevention: set initial thresholds conservatively (0.1% error rate) and relax them only after 14 days of production baseline data is collected.

---

## 9. Exit Criteria — Declaring Production Maturity at Day 30

At the end of the 30-day observation window, the Principal SRE conducts a maturity assessment. The service is declared production-mature when all of the following are true.

**SLO performance.** The service has maintained its derived SLO (99.875%) over the full 30-day window, measured from production telemetry. Error budget consumption must be less than 50% of the monthly allocation.

**Incident record.** No P1 or P0 incidents caused by the Wishlist Service during the 30-day window. P2 incidents are acceptable if they were resolved within SLA and resulted in a runbook update.

**Alert calibration complete.** All Tier 1 and Tier 2 alert thresholds have been reviewed against 30 days of production baseline data and adjusted if necessary. The adjusted thresholds are documented and reviewed by the SRE team.

**Runbook coverage.** At least five failure modes are documented with confirmed resolution steps. Each runbook entry must have been validated — either through a real incident or a controlled chaos test.

**Dependency SLO contracts active.** Formal SLO agreements are in place with all P2 dependencies (User Profile, Recommendation Engine). The SRE team is receiving alerting on those upstream SLOs.

**Browse journey SCS verified.** The SLO Coherence Score for the Browse journey is computed from 30 days of production data and is ≥ 1.0. If it is below 1.0, the service is not mature — it is under-performing relative to its reliability contract.

**OCR ≥ 0.9.** Observability Coverage Ratio for the service has reached at least 90%, meaning the four required signal types (rate, error, latency, saturation) are populated with production-calibrated thresholds and have fired at least once (in test or real conditions) to confirm the alerting pipeline is functional.

When all nine criteria are met, the Principal SRE signs off on the PRR closure record and the service transitions from monitored onboarding to standard operational cadence.

---

*Document version: 1.0 | Scenario class: Greenfield Addition | System: Shopping Cart EKS | Author: SRECapstone Program*
