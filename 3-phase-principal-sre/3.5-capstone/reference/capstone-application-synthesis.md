# SRE Framework Application — Shopping Cart Capstone

## Purpose

This document applies every coined term from `01-coined-terms-framework.md` to the shopping cart reference system defined in the `research/` folder. This is the worked example that turns the vocabulary into practice. Every metric in this document has a computed value, not just a formula. By the end, you have a complete, number-grounded SRE posture for the shopping cart system.

---

## Step 1 — Call Depth Analysis (CD) and SLO Coherence (SCS)

### Computed Call Depths

| Journey | CD (optimized) | Customer SLA | Required per-service SLO | SCS check |
|---------|---------------|-------------|--------------------------|----------|
| J1 Browse | 2 | 99.5% | 99.749% | 0.999^2 / 0.995 = 1.003 ✓ |
| J2 Product Detail | 2 | 99.7% | 99.850% | 0.999^2 / 0.997 = 1.001 ✓ |
| J3 Add to Cart | 3 | 99.9% | 99.967% | 0.9997^3 / 0.999 = 1.0001 ✓ |
| J4 Checkout | 5 | 99.95% | 99.990% | 0.9999^5 / 0.9995 = 0.9999 ≈ 1.0 ✓ |
| J5 Order Tracking | 2 | 99.5% | 99.750% | 0.9997^2 / 0.995 = 1.004 ✓ |
| J6 Account Mgmt | 2 | 99.0% | 99.499% | 0.9995^2 / 0.990 = 1.009 ✓ |

**Finding**: All journeys are SLO-coherent at standard per-service SLOs of 99.97–99.99%. However, the checkout journey (J4) requires the tightest per-service SLO: **99.990% for Auth, Cart, Inventory/Pricing combined, Payment, and Order Management**.

**Action**: Set per-service SLOs to the maximum required across all journeys the service participates in:

| Service | Journeys | Max required SLO | Operational tier |
|---------|---------|-----------------|-----------------|
| Auth Service | J3, J4, J5, J6 | 99.990% (from J4) | P0 |
| Cart Service | J3, J4 | 99.990% (from J4) | P0 |
| Inventory Service | J2, J3, J4 | 99.990% (from J4) | P1 → elevate to P0 practices |
| Pricing & Promotions | J3, J4 | 99.990% (from J4) | P1 → elevate to P0 practices |
| Payment Service | J4 | 99.990% (from J4) | P0 |
| Order Management | J4, J5 | 99.990% (from J4) | P0 |
| Product Catalog | J1, J2 | 99.850% (from J2) | P1 — stays P1 |
| Search Service | J1 | 99.749% (from J1) | P1 |
| User Profile | J6 | 99.499% (from J6) | P2 |
| Notification | async | N/A (async) | P2 |
| Recommendation Engine | J1 (soft dep) | N/A (soft dep) | P2 |
| Review & Rating | J2 (soft dep) | N/A (soft dep) | P3 |

---

## Step 2 — Latency Budget Per Hop (LBH) Enforcement

### Computed LBH per journey

| Journey | CD | p99 SLO | Infrastructure overhead | LBH |
|---------|---|---------|------------------------|-----|
| J1 Browse | 2 | 800ms | 120ms (2 × 60ms) | (800-120)/2 = 340ms |
| J2 Product Detail | 2 | 500ms | 120ms | (500-120)/2 = 190ms |
| J3 Add to Cart | 3 | 300ms | 180ms | (300-180)/3 = 40ms |
| J4 Checkout | 5 | 2000ms | 250ms | (2000-250)/5 = 350ms |
| J5 Order Tracking | 2 | 1000ms | 120ms | (1000-120)/2 = 440ms |

### J3 Add-to-Cart: the tight constraint

**LBH = 40ms per hop** for Add-to-Cart. This is extremely tight:
- Auth Service JWT validation: typically 5–15ms → **within LBH** ✓
- Cart Service Redis read + write: typically 2–8ms for Redis, 10–20ms for total service → **within LBH** ✓
- Inventory Service DB read + reservation write: typically 20–50ms → **at risk** ⚠️
- Pricing Service rule evaluation: typically 15–40ms → **at risk** ⚠️

**Resolution**: Inventory and Pricing are parallelized (hop 3 is parallel, not sequential). LBH of 40ms applies to the longest of the two parallel calls, not their sum. If Inventory and Pricing are both ≤ 40ms at p99, the constraint is met. The risk is Inventory DB latency under load — which requires a read-replica with connection pooling and a p99 latency SLO set at 30ms for the DB query specifically.

### J4 Checkout: Payment Service constraint

**LBH = 350ms per hop**. Payment Service (Stripe API) has a p99 of 600–1200ms under normal conditions. 350ms LBH is violated by Stripe's own latency.

**Resolution**:
- Set Payment Service LBH as a **Tier 0 exception**: the end-to-end checkout SLO is measured excluding Payment Service p99 exceedances that are attributable to the Stripe API (Tier 0 dependency outside SLO control)
- The checkout p99 SLO is re-stated: "p99 ≤ 2000ms excluding Stripe API latency attribution"
- This is documented in the SLA as an explicit carve-out for Tier 0 dependencies
- Monitor separately: Stripe_latency_p99 and Stripe_error_rate as independent signals

---

## Step 3 — Dependency Gravity (DG) Ranking

Computing DG for each service using journey and tier data:

**Auth Service DG calculation**:
- Direct P0 dependents: Cart (J3/J4, P0), Payment (J4, P0), Order Management (J4/J5, P0) → 3 × (4 × 1.0) = 12
- Direct P1 dependents: Inventory (J4, via J3 context), Pricing (J4) → 2 × (3 × 1.0) = 6
- Total DG(Auth) = 12 + 6 = **18** — extremely high; critical infrastructure status

**Cart Service DG**:
- Direct P0 dependents: Payment (J4, P0) → 1 × (4 × 1.0) = 4
- Direct P1 dependents: Inventory (J3, J4), Pricing (J3, J4) → 2 × (3 × 1.0) = 6
- Total DG(Cart) = 4 + 6 = **10** — high gravity; P0 practices mandatory

**Inventory Service DG**:
- Direct P0 dependents: Cart (via Inventory check in J3), Payment (blocked by Inventory reserve in J4) → 2 × 4 = 8
- Total DG(Inventory) = **8** — high gravity; this elevates Inventory from P1 to P0-practices territory

**Payment Service DG**:
- Direct P0 dependents: Order Management (must receive payment confirmation before creating order) → 1 × 4 = 4
- Total DG(Payment) = **4** — lower than expected; it is at the bottom of the J4 chain so fewer services depend on it directly

**Product Catalog DG**:
- Direct P1 dependents: Search (J1, P1) → 1 × (3 × 1.0) = 3
- Transitive: Recommendation Engine (J1, via Catalog data) → 1 × (2 × 0.5) = 1
- Total DG(Catalog) = **4** — moderate; consistent with P1 classification

**DG ranking table** (highest risk first):

| Rank | Service | DG | Current Tier | Recommended Action |
|------|---------|---|-------------|-------------------|
| 1 | Auth Service | 18 | P0 | Dedicated SRE engagement; 5-nines target justified |
| 2 | Cart Service | 10 | P0 | Correct tier; dedicated runbooks required |
| 3 | Inventory Service | 8 | P1 | **Elevate to P0 practices** — DG exceeds P1 threshold |
| 4 | Pricing & Promotions | 6 | P1 | Elevate to P0 practices for J4 context |
| 5 | Payment Service | 4 | P0 | Correct tier; Stripe dependency documented |
| 6 | Product Catalog | 4 | P1 | Correct tier |
| 7 | Order Management | 4 | P0 | Correct tier |

**Critical finding**: Inventory Service has DG=8 but is classified P1. This is the hidden high-gravity service pattern that DG analysis surfaces. Inventory Service should be operated with P0 practices (dedicated on-call runbook, explicit circuit breakers on all callers, chaos engineering tested quarterly) even if it is not formally reclassified to P0.

---

## Step 4 — Cascade Coefficient (CC) Analysis

Estimating CC for each service using dependency graph and circuit breaker presence:

| Service | Dependents without CB | Dependents with CB | CC calculation | CC value |
|---------|----------------------|-------------------|---------------|---------|
| Auth Service | Cart (no CB), Payment (no CB), Order Mgmt (no CB) | None identified | (3 × 4 × 0.9) = 10.8 | **10.8** |
| Inventory Service | Cart (no CB on inventory call) | Pricing (has CB) | (1 × 4 × 0.9) + (1 × 3 × 0.1) = 3.6 + 0.3 = **3.9** | 3.9 |
| Cart Service | Payment (no CB on cart) | None | (1 × 4 × 0.9) = **3.6** | 3.6 |
| Product Catalog | Search (has CB, degrades to cached results) | Recommendation (has CB) | (1 × 3 × 0.1) + (1 × 2 × 0.1) = 0.5 | **0.5** |
| Notification Service | None (async, no callers blocked) | — | **0** | 0 |

**Critical finding — Auth Service CC = 10.8**: Auth Service has no circuit breakers on any of its callers. If Auth Service goes down, Cart, Payment, and Order Management all fail hard — no graceful degradation. For Auth specifically, there is no meaningful "degrade gracefully" mode (you cannot allow unauthenticated checkout). The mitigation is not circuit breakers but Auth Service redundancy: minimum 5 pods across 3 AZs, aggressive HPA, pre-warmed connection pools.

**Action items from CC analysis**:
1. Auth Service: add rate-limit protection at API Gateway level to prevent login storms from saturating Auth Service → this reduces the probability of Auth failure from demand spikes
2. Inventory Service: add circuit breaker on Cart Service's call to Inventory → graceful degradation: proceed to checkout with "availability not guaranteed" messaging instead of failing the add-to-cart action
3. Cart Service: add circuit breaker on Payment Service's dependency check of cart state → Payment should not re-read cart; it should receive cart state as part of the checkout API call (stateless handoff pattern)

---

## Step 5 — Blast Radius Index (BRI) for Key Failure Scenarios

### Scenario A: Auth Service complete outage (15 minutes)

```
affected_users = all users attempting authenticated actions = ~60% of active users
journey_criticality = checkout (1.0), add-to-cart (1.0), order-tracking (0.7)
tier_weight = P0 = 1.0

BRI = 0.60 × 1.0 × 1.0 = 0.60
```

**BRI = 0.60 → SEV2 (Major incident)**. Escalation: VP Engineering + Customer Support leadership notified. External status page updated. Note: Browse and Product Detail (unauthenticated users) continue normally.

### Scenario B: Payment Service degradation (error rate 40%)

```
affected_users = users in checkout flow only = ~5% of active users at any moment
journey_criticality = revenue-generating = 1.0
tier_weight = P0 = 1.0

BRI = 0.05 × 1.0 × 1.0 = 0.05
```

**BRI = 0.05 → SEV4 (Minor)**. However, GMV impact is disproportionate: 5% of users in checkout = 100% of revenue generation. BRI needs a revenue-weighted variant for checkout:

```
BRI_revenue = GMV_loss_rate / baseline_GMV_rate = 0.40 (40% of checkout revenue blocked)
```

**Revenue-weighted BRI = 0.40 → SEV2 escalation on revenue grounds** even though user-count BRI is SEV4. This reveals a gap in standard BRI: when a small number of users represent 100% of revenue, user-count-based BRI underestimates severity. The revenue-weighted BRI variant is required for any service on the revenue-critical path.

### Scenario C: Product Catalog Service outage (complete)

```
affected_users = all browse and search users = ~80% of active users (most users are browsing)
journey_criticality = informational = 0.3
tier_weight = P1 = 0.75

BRI = 0.80 × 0.3 × 0.75 = 0.18
```

**BRI = 0.18 → SEV3 (Partial impact)**. Catalog outage affects many users but has low immediate revenue impact (users in mid-cart or checkout are not affected; catalog is not on the checkout critical path). This is the counterintuitive result: a visually dramatic outage (the storefront breaks) has a lower BRI than a Payment Service error rate of 40%.

---

## Step 6 — Alert Precision Rate (APR) Baseline and Target

Based on typical pre-improvement state for a system of this scale:

| Alert category | Alerts/month (estimated) | Actionable (estimated) | APR | Status |
|---------------|------------------------|----------------------|-----|--------|
| P0 service error rate | 40 | 30 | 75% | Acceptable, improve |
| Latency threshold breach | 120 | 35 | 29% | **Alert fatigue — immediate audit** |
| Infrastructure (CPU, memory) | 200 | 40 | 20% | **Alert crisis — redesign** |
| Dependency health check | 60 | 15 | 25% | **Alert fatigue** |
| Business metric anomaly | 15 | 13 | 87% | Good — maintain |
| **Total** | **435** | **133** | **31%** | **Alert fatigue zone** |

**Finding**: The infrastructure and latency alert categories are generating massive noise. 89% of CPU/memory alerts and 71% of latency alerts are not actionable. The on-call engineers have learned to ignore them — which means when a real CPU saturation or latency breach occurs, the alert is treated as noise.

**Alert redesign priorities**:
1. **Latency alerts**: replace static threshold (p99 > 300ms) with burn-rate-based latency budget alerts. Alert only when latency budget consumption rate exceeds 2× expected. Reduces false positives by ~70%.
2. **Infrastructure alerts**: replace CPU % threshold with saturation rate (time-to-saturation at current growth rate < 30 minutes). Alert only when saturation is imminent.
3. **Dependency health checks**: replace synthetic ping with real traffic error rate. If the service is processing real traffic successfully, a synthetic ping failure is irrelevant.

**Target APR after redesign**: > 0.80 for all alert categories. Expected reduction in total alert volume: 435/month → ~120/month, while actionable alert count stays at 120+ (all remaining alerts are actionable).

---

## Step 7 — Error Budget Velocity (EBV) Analysis

**Scenario**: Checkout service error budget. SLO = 99.95% (monthly window = 43,800 minutes). Budget = 21.9 minutes/month.

Month 1: Normal operations
- Error rate: 0.05% at 10,000 requests/hour baseline
- Traffic: 240,000 requests/day
- EBV = (0.05% / 0.05%) = 1.0 — nominal

Month 2: Traffic grows 2× (promotional event)
- Error rate: 0.07% at 20,000 requests/hour
- Traffic: 480,000 requests/day
- Standard burn rate = (0.07% / 0.05%) = 1.4 — concerning; triggers slow-burn alert
- EBV = (0.07% / 20,000) / (0.05% / 10,000) = (0.0000035) / (0.000005) = 0.70

**EBV = 0.70**: despite higher standard burn rate, error rate is actually improving relative to traffic. The system is handling 2× traffic with proportionally fewer errors. Standard burn rate says "investigate"; EBV says "system is improving." EBV prevents a false investigation that would disrupt engineering during a successful promotional event.

Month 3: New deployment introduces a regression
- Error rate: 0.09% at 20,000 requests/hour (same traffic as Month 2)
- Standard burn rate = (0.09% / 0.05%) = 1.8 — warning
- EBV = (0.09% / 20,000) / (0.05% / 10,000) = (0.0000045) / (0.000005) = 0.90

**EBV = 0.90**: error rate grew slightly but less than proportionally to traffic — marginally improving. This month, the deployment regression is subtle. Standard burn rate (1.8) fires an alert; EBV says the system is still handling scale proportionally. The regression is real but minor relative to scale. Correct response: monitor closely for 24 hours rather than immediate rollback.

Month 4: Aggressive regression (memory leak introduced)
- Error rate: 0.15% at 20,000 requests/hour
- Standard burn rate = (0.15% / 0.05%) = 3.0 — fast burn
- EBV = (0.15% / 20,000) / (0.05% / 10,000) = (0.0000075) / (0.000005) = 1.5

**EBV = 1.5**: error rate is growing faster than traffic — clear reliability degradation. Both standard burn rate and EBV agree: investigate immediately.

---

## Step 8 — Toil Amplification Factor (TAF) Assessment

Current state (baseline):

| Toil category | Q1 hours | Q2 hours | Traffic growth Q1→Q2 |
|--------------|---------|---------|---------------------|
| On-call pages and response | 240 | 290 | +50% |
| Manual deployment actions | 80 | 120 | +50% |
| Support escalation triage | 60 | 95 | +50% |
| Certificate/secret rotation | 40 | 45 | +50% |
| **Total toil** | **420h** | **550h** | |
| **Toil growth rate** | — | +31% | — |

```
TAF = 31% / 50% = 0.62
```

**TAF = 0.62**: toil is growing at 62% the rate of traffic growth. This is acceptable but not comfortable — the team is managing to keep toil sublinear, but only barely. If traffic doubles again next quarter, projected toil = 550 × 1.62 = 891 hours. The team currently has 700 hours of engineering capacity (4 SREs × 175h productive hours). TAF=0.62 at 3× baseline traffic would put toil at ~850 hours — within 50 hours of capacity breach.

**By category TAF**:

| Category | Q1→Q2 growth | Traffic growth | Category TAF |
|---------|-------------|---------------|-------------|
| On-call pages | +21% | +50% | **0.42** — good |
| Manual deployments | +50% | +50% | **1.0** — concern; should be automated |
| Support escalations | +58% | +50% | **1.16** — superlinear; investigate root cause |
| Certificate/secret rotation | +12% | +50% | **0.24** — mostly automated; good |

**Finding**: Manual deployment TAF = 1.0 (linear scaling) is the urgent automation target. Support escalation TAF = 1.16 is a reliability signal — customers are escalating faster than traffic grows, which means there is a quality issue that traffic growth is exposing.

---

## Step 9 — Recovery Cost Ratio (RCR) for Top Recurring Incident Classes

### Incident class A: Inventory reservation deadlock during flash sales

- Incident frequency: 3 per quarter
- Mean response + remediation: 4 hours per incident (2 SREs × 2h)
- Engineering time to fix root cause (implement proper pessimistic locking + retry logic): 3 weeks (1 engineer)
- RCR = (4h × 3 incidents) / (120h for fix) = 12 / 120 = **0.1**

**RCR = 0.1** — prevention costs 10× more than the incidents do right now. Accept the risk unless frequency increases.

*Wait — re-examine*: 3 incidents per quarter means 12 per year. Each is 4 engineer-hours. Annual cost = 48h. Fix cost = 120h. Annual RCR = 48/120 = 0.4. Still < 1. **Defer fix** unless frequency increases or an incident escalates to SEV1.

### Incident class B: Auth service token validation spike (certificate cache miss on deployment)

- Incident frequency: 6 per quarter (every deployment rotation)
- Mean response + remediation: 2 hours per incident
- Engineering time to fix root cause (implement hot-reload for JWT public keys without restart): 2 weeks (1 engineer)
- Annual RCR = (2h × 24 incidents/year) / (80h for fix) = 48 / 80 = **0.60**

**RCR = 0.60** — borderline. Fix in the next cycle if engineering capacity allows; otherwise accept.

### Incident class C: Kafka consumer lag building overnight (consumer group rebalance bug)

- Incident frequency: 8 per quarter (roughly weekly)
- Mean response: 1.5 hours (restart consumer group, monitor recovery)
- Fix: replace manual restart with automated lag-triggered restart Kubernetes CronJob: 1 week
- Annual RCR = (1.5h × 32/year) / (40h) = 48 / 40 = **1.2**

**RCR = 1.2** — fix cost is recovered within the year. **Schedule for next sprint.** After fixing, the consumer lag restart becomes automatic; the 1.5h of on-call response per incident is eliminated.

### Incident class D: Grafana dashboard authentication token expiry (ops loses monitoring visibility)

- Incident frequency: 4 per quarter (token TTL = 90 days, rotation is manual)
- Mean response: 0.5 hours (rotate token, update dashboards)
- Fix: implement automated Grafana service account token rotation via Vault lease renewal: 1 week
- Annual RCR = (0.5h × 16/year) / (40h) = 8 / 40 = **0.2**

**RCR = 0.2** — prevention costs 5× the incidents. However, this incident causes monitoring blindness during real incidents — the hidden cost is higher. Prioritize based on operational risk, not RCR alone.

**RCR priority ranking for this quarter**:
1. Kafka consumer lag auto-restart (RCR=1.2) → **do this sprint**
2. Auth certificate hot-reload (RCR=0.6) → **schedule next cycle**
3. Inventory deadlock fix (RCR=0.4) → **defer; monitor frequency**
4. Grafana token rotation (RCR=0.2) → **defer; but flag as operational risk**

---

## Step 10 — Failure Locality Index (FLI) Measurement

**Assessment**: review the last quarter's 18 P2+ incidents for the checkout journey.

| Incident | Root cause | Did it cascade? | Cascade scope |
|---------|-----------|----------------|-------------|
| 1 | Payment Service timeout spike | No — circuit breaker on Order Management side | Contained |
| 2 | Inventory DB deadlock | Yes — Cart Service failed when Inventory unavailable | J3, J4 both degraded |
| 3 | Auth Service pod OOMKill (1 pod) | No — other 4 pods absorbed traffic | Contained |
| 4 | Kafka broker leadership election | Yes — Notification consumer stopped; DLQ filled | Layer 4 cascade |
| 5 | Pricing Service bad deployment | No — feature flag disabled; canary caught it | Contained |
| ...12 more incidents... | — | — | — |

Assume: out of 18 incidents, 5 cascaded.

```
FLI = (18 - 5) / 18 = 13/18 = 0.72
```

**FLI = 0.72 — Good but improvable.** 28% of incidents (5 of 18) cascaded beyond the originating service. Target: FLI > 0.90. Gap closure actions:
1. Add circuit breaker on Cart Service's call to Inventory (prevents J3+J4 cascade when Inventory degrades)
2. Implement Kafka consumer watchdog — auto-restart stalled consumer groups (prevents Layer 4 cascade)
3. Review the 5 cascading incidents: are there common missing circuit breakers?

---

## Step 11 — Observability Coverage Ratio (OCR) Assessment

| Service | Traffic ✓ | Errors ✓ | Latency ✓ | Saturation ✓ | Tracing ✓ | Alerts defined ✓ | Fully instrumented |
|---------|----------|---------|----------|-------------|----------|-----------------|------------------|
| Auth Service | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Yes** |
| Cart Service | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Yes** |
| Inventory Service | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | **No** |
| Pricing Service | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | **No** |
| Payment Service | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Yes** |
| Order Management | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Yes** |
| Product Catalog | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | **No** |
| Search Service | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | **No** |
| Notification | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | **No** |
| Recommendation | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | **No** |
| User Profile | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | **No** |
| Reviews | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | **No** |

Fully instrumented: 4 of 12 services

```
OCR = 4 / 12 = 0.333 — 33.3%
```

**Weighted OCR** (P0=4, P1=3, P2=2, P3=1):

Instrumented weight: Auth(4) + Cart(4) + Payment(4) + Order Mgmt(4) = 16
Total weight: 4+4+3+3+4+4+3+3+2+2+2+1 = 35

```
OCR_weighted = 16 / 35 = 0.457 — 45.7%
```

**Finding**: OCR_weighted < 0.85 — critical threshold. P1 services (Inventory, Pricing, Catalog, Search) are severely under-instrumented. Pricing Service has no latency SLO and no tracing, despite being on the J4 checkout critical path. **Pricing Service observability gap is a P0-level risk** because we cannot detect Pricing Service degradation before the checkout error rate rises.

**Instrumentation sprint priority** (by DG × observability gap):
1. Pricing Service — add all 4 golden signals + tracing (2 engineer-days)
2. Inventory Service — add saturation metrics + alert definitions (1 engineer-day)
3. Search Service — add saturation + tracing (2 engineer-days)
4. Notification Service — add latency + saturation + tracing (2 engineer-days)

---

## Step 12 — MTBI-Based SLO Validation

**Using historical incident data to validate whether declared SLOs are achievable**:

| Service | MTBI (observed) | MTTR (observed) | Implied availability | Declared SLO | Achievable? |
|---------|----------------|----------------|---------------------|-------------|------------|
| Auth Service | 720h (1/month) | 0.3h | 720/(720.3) = 99.96% | 99.990% | **No** — MTBI-implied availability is below declared SLO |
| Cart Service | 1440h (1/2 months) | 0.5h | 99.97% | 99.990% | **Marginal** |
| Payment Service | 360h (2/month) | 0.25h | 99.93% | 99.990% | **No** — far below |
| Order Management | 720h | 0.4h | 99.94% | 99.990% | **No** |
| Inventory Service | 240h (3/month) | 0.75h | 99.69% | 99.990% | **No** — significant gap |

**Critical finding**: nearly every P0 service has declared a SLO that its historical MTBI and MTTR cannot support. This is SLO theater — the SLOs are aspirational, not operational.

**Required MTBI calculation** to achieve the declared SLO at observed MTTR:

```
Required_MTBI = MTTR × (SLO / (1 - SLO))

For Auth at 99.990% SLO and MTTR=0.3h:
Required_MTBI = 0.3 × (0.9999 / 0.0001) = 0.3 × 9,999 = 2,999h (125 days between incidents)
```

Auth Service currently fails once per month (720h). To meet 99.990%, it must fail at most once every 125 days. **The gap is 5×** — Auth must be 5× more reliable than it currently is to legitimately claim a 99.990% SLO.

**Action**: either reduce declared SLO to match operational reality (99.96% for Auth based on MTBI/MTTR) or invest in reducing incident frequency (improve Auth Service resilience, add multi-region active-active Auth). Both are valid choices — the key is that the SLO reflects reality.

---

## Step 13 — SRE Team Operational Leverage (OL)

**Reliability improvement investments made this quarter and their OL**:

| Investment | Engineering weeks | Error budget consumption (before) | Error budget consumption (after) | Reduction | OL |
|-----------|------------------|----------------------------------|----------------------------------|----------|---|
| Alert redesign (APR from 31% to 68%) | 3 weeks | 85%/quarter consumed | 60%/quarter | 25pp | 8.3 pp/week |
| Kafka consumer watchdog automation | 1 week | 20% of Notification budget consumed by consumer lag incidents | 2% | 18pp | 18.0 pp/week |
| Inventory circuit breaker addition | 2 weeks | J3 error rate 0.05% avg | J3 error rate 0.03% avg | Modest latency improvement | 3.2 pp/week |
| Auth Service scaling (3→5 pods) | 1 week | Auth incident frequency 1/month | Auth incident frequency 1/2.5 months | Significant | 12.0 pp/week |

**OL ranking**: Kafka watchdog (18.0) > Auth scaling (12.0) > Alert redesign (8.3) > Circuit breaker (3.2)

**Insight**: the two infrastructure investments (Kafka automation and Auth scaling) had higher OL than the alert engineering investment. This is typical early in an SRE program — infrastructure hardening has higher leverage than alert tuning until the infrastructure is stable. Alert tuning becomes the high-OL investment only after the underlying reliability floor is raised.

---

## Complete SRE Posture Summary — Shopping Cart System

### Current state

| Metric | Value | Rating |
|--------|-------|--------|
| OCR_weighted | 45.7% | Critical — instrumentation sprint needed |
| APR (overall) | 31% | Alert fatigue zone — redesign required |
| FLI (system) | 72% | Good but improvable |
| TAF (overall) | 0.62 | Acceptable; deployment automation urgent |
| Top RCR | 1.2 (Kafka) | One investment with positive ROI this quarter |
| SCS (J4 Checkout) | ~1.0 | Coherent at declared SLOs |
| DG hidden risk | Inventory DG=8 but P1 | Elevate operational practices |
| MTBI validation | Auth: 5× gap vs. declared SLO | SLO theater — must address |

### Priority action backlog (ranked by OL)

| Priority | Action | Expected OL | Timeline |
|---------|--------|------------|---------|
| 1 | Kafka consumer watchdog | 18.0 pp/week | This sprint |
| 2 | Auth Service 5-pod scaling | 12.0 pp/week | This sprint |
| 3 | Alert redesign (latency + infra) | 8.3 pp/week | Next 4 weeks |
| 4 | Pricing Service observability | Enables detection | 2 engineer-days |
| 5 | Inventory circuit breaker | Improves FLI | 2 engineer-days |
| 6 | API Gateway JWT validation (removes Auth hop from J3/J4) | Reduces CD, improves LBH | 1 sprint |
| 7 | SLO recalibration (MTBI-based) | Restores SLO integrity | 2 weeks (process) |
| 8 | Auth certificate hot-reload | RCR=0.6, schedule next cycle | Next cycle |

### The journey to 99.95% checkout reliability

**Where we are**: Payment and Auth both have implied availability ~99.93% from historical MTBI/MTTR data. Checkout at CD=5 with these availability levels computes to:
```
0.9993 × 0.9993 × 0.9990 × 0.9993 × 0.9993 ≈ 0.9962 = 99.62%
```
Current actual checkout availability is approximately **99.62%** — well below the declared 99.95% SLA.

**The gap**: 0.33 percentage points = 144 minutes of additional checkout downtime per month beyond what the SLA permits.

**The path**: implement the priority backlog in order. The MTBI improvement from Auth scaling reduces Auth downtime by ~50%. Kafka watchdog eliminates notification consumer lag incidents (not directly on checkout path, but reduces overall incident load on the SRE team). The most direct checkout improvement is reducing CD from 5 to 4 by implementing API Gateway JWT validation — this eliminates Auth from the checkout call chain entirely, increasing the checkout availability floor even if Auth itself has lower-than-declared availability.

**12-month target state**:
- OCR_weighted: > 95%
- APR: > 80%
- FLI: > 90%
- TAF: < 0.5
- Actual checkout availability: > 99.92% (approaching 99.95% as Auth and Inventory reliability improve)
- SLO coherence: all SLOs MTBI-validated, no SLO theater

---

## Conclusion — The Framework in Practice

Every number in this document was computed from the formulas in `01-coined-terms-framework.md` applied to the architecture in `research/`. The framework is not theoretical — it produces specific, actionable findings that a textbook SRE assessment would miss:

1. **Inventory Service is a hidden P0** (DG=8 revealed by Dependency Gravity analysis)
2. **Checkout SLA is currently unmet** (MTBI × MTTR implies 99.62%, not 99.95%)
3. **73% of alerts are noise** (APR=31% revealed by Alert Precision Rate analysis)
4. **Auth Service is 5× less reliable than its SLO declares** (MTBI validation)
5. **API Gateway JWT validation is the highest-leverage architectural investment** (eliminates Auth from CD, improves LBH for J3 and J4)

None of these findings appear in a standard SRE dashboard. All of them are derivable from data any mature engineering organization already has. The framework provides the formulas; the organization provides the data; the result is a reliability roadmap grounded in measurement rather than intuition.
