# Solutions: Exercise Set 5 — Integrated Scenarios

Complete worked solutions for all 4 integrated scenarios. Every sub-question shows full computation before stating the result.

---

## ALL FORMULAE (Reference)

```
CD = count(sync_hops)
Required_SLO = SLA^(1/CD)
SCS = SLO^CD / SLA  [valid range: 0.95–1.10]

LBH = (e2e_p99 - overhead) / CD

DG = Σ[tw × proximity_discount]  (1.0 direct, 0.5 one-hop)
BRI = affected% × criticality × tw
CC = Σ[P(cascade) × tw]  — P=0.9 no CB, 0.5 partial CB, 0 full CB
FLI = contained / total  [target >0.90]

EBV = normalized_errors / baseline
time_to_breach = remaining / (EBV × baseline_rate)

MTBI = period / count
achievable_SLO = MTBI / (MTBI + MTTR)

OCR = Σ(instrumented × tw) / Σ(tw)
OL = Δbudget_pp / SRE_hours
RCR = (response_hrs × freq) / fix_hrs
TAF = toil_growth / traffic_growth

SCV = freq × CSAI × failure_rate
MRI = DG × CD × (1 - FLI) × (2 - OCR)
EBR = min(MRI × 0.05, 0.80)
DSS = (1 - SCV_n) × (1 - MRI/10) × APR × budget_fraction

GEI = (new_deps × avg_tw) / (coverage × canary_hrs)
SLTD = (ramp_rps/min × lag_min) / pod_capacity
RDR = new_mode / old_mode  [target <0.10]

SCI = (observed - declared) / total_observed  [must = 0]
RIS = (RCR × OL) / MRI
SRMI = (FLI × OCR × APR/0.85) / (TAF × CC_max/10)
JRCS = SCS × FLI × OCR_path × (1 - CC_max/10)
```

---

## Shopping Cart System — Reference Numbers

| Service | Priority | tw | DG | Notes |
|---|---|---|---|---|
| Auth | P0 | 1.0 | 18 | CC_max contribution = 10.8 |
| Cart | P0 | 1.0 | 10 | — |
| Payment | P0 | 1.0 | — | — |
| Order Management | P0 | 1.0 | — | — |
| Inventory | P1 | 0.8 | 8 | — |
| Pricing | P1 | 0.8 | — | — |
| Product Catalog | P1 | 0.8 | — | — |
| Search | P1 | 0.8 | — | — |
| User Profile | P2 | 0.5 | — | — |
| Notification | P2 | 0.5 | — | — |
| Recommendation | P2 | 0.5 | — | — |
| Reviews | P3 | 0.3 | — | — |

**Checkout path**: CD=5, SLA=99.95%, error budget=21.6 min/month
**Browse path**: CD=2, SLA=99.5%, error budget=216 min/month
**System health**: OCR=0.457, APR=0.31, FLI=0.72, CC_max=10.8, TAF=0.62

---

## Scenario 1: Black Friday Reliability Audit

**Setup**: 2 weeks before Black Friday. Traffic expected at 4x baseline. All P0 services at 60% error budget consumed (day 18 of 30). System health: OCR=0.457, APR=0.31, FLI=0.72, CC_max=10.8, TAF=0.62.

---

### 1(a) SLTD for Auth Service

**Given**: Traffic ramp = 300 rps/min for 20 min (0 to 6,000 rps). Autoscaling lag = 3 min. Pod capacity = 150 rps/pod.

**Formula**: SLTD = (ramp_rps/min x lag_min) / pod_capacity

**Step 1** — Compute unserved traffic during autoscaling lag:

```
unserved_rps = ramp_rps/min × lag_min
             = 300 × 3
             = 900 rps
```

These 900 rps arrive before autoscaling can respond. Without pre-provisioned pods, they have no capacity to serve them.

**Step 2** — Compute SLTD:

```
SLTD = (300 × 3) / 150
     = 900 / 150
     = 6.0
```

**Step 3** — Interpret: pre-provision 6 pods (round up from 6.0) BEFORE the traffic ramp begins.

**Answer**: SLTD = 6.0. Pre-provision 6 Auth pods before the Black Friday traffic ramp.

**Why this matters operationally**: Without pre-scaling, the first 900 rps of the ramp hits Auth with no capacity. At 4x peak (6,000 rps through Auth), 15% of launch traffic fails in the opening 3 minutes — exactly when conversion matters most and when eyes are on dashboards. SLTD is not about total capacity — autoscaling will eventually catch up. It is about closing the gap window at the single most visible moment of the event.

**Key Insight**: SLTD converts the autoscaling lag into a concrete pod count. The number is not "how many pods total" — it is the minimum pre-provisioned count to bridge the gap between ramp start and scale-out completion.

---

### 1(b) SRMI Current State

**Formula**: SRMI = (FLI x OCR x APR/0.85) / (TAF x CC_max/10)

**Step 1** — Compute the numerator:

```
APR/0.85 = 0.31 / 0.85 = 0.3647

FLI × OCR × (APR/0.85) = 0.72 × 0.457 × 0.3647
                        = 0.72 × 0.1666
                        = 0.1200
```

**Step 2** — Compute the denominator:

```
CC_max/10 = 10.8 / 10 = 1.08

TAF × (CC_max/10) = 0.62 × 1.08
                  = 0.6696
```

**Step 3** — Compute SRMI:

```
SRMI = 0.1200 / 0.6696
     = 0.179
```

**Answer**: SRMI = 0.179.

**Benchmark interpretation**: Best-practice target values (FLI=0.95, OCR=0.95, APR=0.85, TAF=0.40, CC_max=2.0) yield:

```
numerator   = 0.95 × 0.95 × (0.85/0.85) = 0.95 × 0.95 × 1.0 = 0.9025
denominator = 0.40 × (2.0/10)            = 0.40 × 0.20       = 0.0800
SRMI_target = 0.9025 / 0.0800            = 11.28
```

Current SRMI = 0.179 = 1.6% of target maturity.

**Black Friday readiness verdict**: NOT READY. Breaking down each driver:

- **CC_max=10.8**: A single Auth failure during the 4x traffic event cascades to Cart, Payment, and Order Management simultaneously. The cascade coefficient is the dominant denominator driver.
- **OCR=0.457**: The team is flying blind on 54% of weighted service capacity. During a high-stress event, missing signals delay detection and extend MTTR.
- **APR=0.31**: 69% of alerts during the event are noise — exactly when engineers cannot afford to triage false alarms.

**Key Insight**: SRMI below 1.0 means the system's safety mechanisms (containment, observability, alert quality) are collectively losing to the system's risk drivers (cascade potential, toil growth). A 4x traffic multiplier on a system with SRMI=0.179 amplifies every failure mode simultaneously.

---

### 1(c) Which CRs Can Proceed?

**Given**: Budget remaining = 40%. CR-1: MRI=2. CR-2: MRI=4.

**Formula**: EBR = min(MRI x 0.05, 0.80)

**Step 1** — Compute EBR for each CR:

```
CR-1: EBR = min(2 × 0.05, 0.80) = min(0.10, 0.80) = 10%
CR-2: EBR = min(4 × 0.05, 0.80) = min(0.20, 0.80) = 20%
```

**Step 2** — Check CR-1 against available budget:

```
Available = 40%
CR-1 EBR  = 10%
10% ≤ 40% → CR-1 CAN PROCEED
```

**Step 3** — Check CR-2 after CR-1 consumes its allocation:

```
Remaining after CR-1 = 40% - 10% = 30%
CR-2 EBR             = 20%
20% ≤ 30% → CR-2 CAN PROCEED (sequentially after CR-1)
```

**Step 4** — Compute final budget position:

```
Remaining after both = 40% - 10% - 20% = 10%
```

**Answer**: Both CRs can proceed. Order: CR-1 first, then CR-2. Budget after both: 10% remaining.

**Operational flag**: 10% remaining budget with 12 days left in the month is a tight position. Any incident before month-end will consume this buffer and breach the SLA. The Principal SRE should document this explicitly and recommend a soft change freeze for all non-emergency work until the new month resets the budget.

**Key Insight**: EBR is not what a change consumes during a successful deployment — it is the reserve held against rollback and remediation if the change causes an incident. After both CRs, the system has essentially no incident tolerance for the remainder of the month.

---

### 1(d) JRCS for Checkout

**Formula**: JRCS = SCS x FLI x OCR_path x (1 - CC_max/10)

**Step 1** — Determine SCS:

All services in the checkout path (CD=5) are declaring SLOs approximately consistent with achieving 99.95% compound availability. Assuming all services at 99.99% individual SLO:

```
Compound = 0.9999^5 = 0.9995
SCS = 0.9995 / 0.9995 = 1.00
```

SCS = 1.0 (coherent declarations).

**Step 2** — Determine OCR_path for checkout:

Auth and Order Management are partially instrumented; Cart and Payment are better covered; Payment is the highest-tw service and is fully instrumented, raising the path average above the system OCR. Estimated OCR_path = 0.60.

```
OCR_path = 0.60
```

**Step 3** — Compute JRCS:

```
JRCS = SCS × FLI × OCR_path × (1 - CC_max/10)
     = 1.0 × 0.72 × 0.60 × (1 - 10.8/10)
     = 1.0 × 0.72 × 0.60 × (1 - 1.08)
     = 1.0 × 0.72 × 0.60 × (-0.08)
     = 0.432 × (-0.08)
     = -0.035
```

**Answer**: JRCS = -0.035 (NEGATIVE).

**Interpretation**: A negative JRCS is the single most alarming finding in the entire framework. The (1 - CC_max/10) term goes negative when CC_max > 10.0. CC_max=10.8 means Auth's cascade coefficient exceeds the entire framework's safety scale. Even with FLI=0.72 and reasonable OCR, the cascade risk structurally overwhelms the checkout journey's safety margin.

This does not mean the journey definitely fails — it means that when Auth fails (which it will, given 4x traffic on a system at SRMI=0.179), the probability of full cascade to Cart, Payment, and Order Management exceeds the system's ability to contain it.

**Key Insight**: A negative JRCS is not a warning — it is a structural unsafety condition. The checkout journey must not be exposed to 4x Black Friday traffic without emergency circuit breaker deployment on Cart→Auth, Payment→Auth, and Order Mgmt→Auth before the event.

---

### 1(e) Black Friday Readiness Report to VP Engineering

> **Current checkout availability is 99.62% — already below our 99.95% SLA before Black Friday has started.**
>
> **Critical finding**: JRCS for the Checkout journey is -0.035. CC_max=10.8 means a single Auth failure during 4x traffic will cascade simultaneously to Cart, Payment, and Order Management. This is not a risk to be monitored — it is a structural condition that guarantees multi-service failure when Auth is stressed. SRMI=0.179 (1.6% of reliability maturity target) confirms the system has not been hardened for this event.
>
> **Three required actions before Black Friday**:
>
> 1. **Emergency circuit breaker sprint** (40 engineering hours, 5 business days): Deploy full circuit breakers on Cart→Auth, Payment→Auth, and Order Mgmt→Auth with tested fallback behaviors. This reduces CC_max from 10.8 to approximately 1.5 and makes JRCS positive. Without this, a single Auth degradation becomes a site-wide checkout outage.
>
> 2. **Pre-scale all P0 services** before traffic ramp: Auth requires 6 pre-provisioned pods minimum (SLTD=6.0). Cart, Payment, and Order Management require equivalent analysis. Pre-scaling must complete before the traffic ramp begins — autoscaling lag creates a 3-minute gap window that is unacceptable at event launch.
>
> 3. **Change freeze starting 7 days before Black Friday**: Current error budget position (40% remaining at day 18) leaves only 10% buffer after the two approved CRs. Any change-related incident in the final 12 days will breach the monthly SLA. No non-emergency changes after day 23.
>
> **Decision requested**: Approve the emergency circuit breaker sprint as P0 work, displacing current sprint scope. Without approval, the recommendation is to reduce Black Friday traffic targets to 2x baseline (not 4x) until CC_max is brought below 5.0.

---

## Scenario 2: Incident Investigation and Postmortem

**Setup**: 11 PM Tuesday. Cart p99 > 5,000ms. Payment 15% error rate. Search 8% error rate.

---

### 2(a) Suspicion Scores

**Formula**: suspicion = SCV x recency_factor

Recency factors: <24h = 1.0, <72h = 0.5, >72h = 0.1

**Given**:
- Cart: SCV=0.3, deployed 2 hours ago
- Payment: SCV=0.1, no recent changes (last deploy >1 week ago)
- Search: SCV=0.5, deployed 4 days ago

**Step 1** — Assign recency factors:

```
Cart:    2 hours ago  → <24h → recency = 1.0
Payment: >1 week ago  → >72h → recency = 0.1
Search:  4 days ago   → >72h → recency = 0.1
```

**Step 2** — Compute suspicion scores:

```
Cart:    suspicion = 0.3 × 1.0 = 0.30
Payment: suspicion = 0.1 × 0.1 = 0.01
Search:  suspicion = 0.5 × 0.1 = 0.05
```

**Step 3** — Rank:

```
1st: Cart    = 0.30
2nd: Search  = 0.05
3rd: Payment = 0.01
```

**Answer**: Investigate Cart first.

**Why recency changes everything**: SCV alone would rank Search highest (0.5 vs. 0.3 for Cart). The recency multiplier reverses the ranking. Cart's 2-hour-old deployment makes it 6x more suspicious than Search despite a lower base SCV. The framework multiplies rather than adds because deployment timing and inherent change risk are independent risk amplifiers — both must be present for suspicion to be high.

**Key Insight**: Alert loudness (Search at 8% errors sounds serious) and suspicion score are different things. Investigate in suspicion order, not alert order. The highest-alerting service may be a cascade victim, not the root cause.

---

### 2(b) FLI for the Incident

**Formula**: FLI = contained / total

**Given**: Cart is confirmed root cause. Circuit breaker states:
- Payment→Cart: partial CB (P=0.5)
- Search→Cart: no CB (P=0.9)

**Step 1** — Determine which failures cascaded:

```
Payment: partial CB (P=0.5) → cascade occurs → Payment is a cascade failure
Search:  no CB (P=0.9)      → cascade occurs → Search is a cascade failure
```

**Step 2** — Count failure events:

```
Total failure events = Cart (root cause) + Payment (cascade) + Search (cascade) = 3
Contained failures   = 1  (Cart only — the failure originated in Cart and was not caused by another service)
```

**Step 3** — Compute FLI:

```
FLI_incident = 1 / 3 = 0.333
```

**Answer**: FLI = 0.33 for this incident.

**Interpretation**: 67% of failure events are cascade. The Cart failure caused more collateral damage than the Cart failure itself. FLI=0.33 is far below the 0.90 target and below even the system's already-low baseline FLI=0.72.

**Primary postmortem action item**: Circuit breakers — not just the Cart bug fix. Fixing Cart eliminates the root cause but leaves the cascade paths open for the next incident, whatever causes it.

**Key Insight**: When FLI_incident < system_FLI_baseline, the incident's blast radius was worse than typical. This incident exposed exactly the cascade paths that circuit breakers would close. That is the postmortem insight.

---

### 2(c) BRI and Severity

**Formula**: BRI = affected% x criticality x tw

**Given**: 35% of active users affected (checkout and cart flows). Criticality = 1.0 (revenue-impacting). tw(Cart) = 1.0 (P0).

**Step 1** — Compute BRI:

```
BRI = 0.35 × 1.0 × 1.0
    = 0.35
```

**Step 2** — Map to severity:

```
BRI < 0.35   → SEV3 (team notification, no bridge)
BRI 0.35–0.70 → SEV2 (EM paged, bridge opened, CS notified)
BRI > 0.70   → SEV1 (VP/Director paged, executive bridge)
```

BRI = 0.35 lands on the SEV2 boundary. Escalate to SEV2.

**Answer**: BRI = 0.35 → SEV2.

**Actions**: Page Engineering Manager, open incident bridge, notify Customer Support lead. Do not page VP — BRI is below the 0.70 threshold for executive escalation.

**Key Insight**: BRI at exactly 0.35 is a boundary judgment. When BRI lands on a severity boundary, escalate to the higher severity. The cost of an unnecessary EM page is low; the cost of undertreating a SEV1-adjacent incident is high.

---

### 2(d) Postmortem RCR

**Formula**: RCR = (response_hrs x freq) / fix_hrs

**Given**: Cart incidents occurring 2x/month. Response: 2 SREs x 90 min = 3 hours per incident. Fix cost: 120 hours.

**Step 1** — Compute annual response cost:

```
Annual frequency        = 2 incidents/month × 12 months = 24 incidents/year
Response cost/incident  = 2 SREs × 1.5 hours            = 3 hours
Annual response cost    = 3 × 24                         = 72 hours
```

**Step 2** — Compute RCR:

```
RCR = 72 / 120 = 0.60
```

**Step 3** — Apply threshold:

```
RCR < 0.50   → Fix next quarter
RCR 0.50–1.0 → Fix this sprint
RCR > 1.0    → Fix immediately, pause other work
```

RCR = 0.60 → Fix this sprint.

**Answer**: RCR = 0.60 → Fix in current sprint.

**With cascade cost included**: Each incident triggers cascade to Payment and Search, each requiring approximately 1 additional SRE-hour for investigation and recovery:

```
Adjusted response/incident = 3 + 2 = 5 hours
Adjusted annual cost       = 5 × 24 = 120 hours
Adjusted RCR               = 120 / 120 = 1.00 → Fix immediately
```

The cascade-adjusted RCR crosses the immediate threshold. Fixing Cart is now break-even on hours in year one alone — and saves compounding cascade damage in subsequent years.

**Key Insight**: Incident RCR calculations that ignore cascade costs systematically underestimate the value of fixing root causes. Always add cascade response time when CC > 0.

---

### 2(e) Circuit Breakers and RDR Target

**Current CC(Cart path)**:

Callers of Cart that can cascade:

```
Payment→Cart: partial CB (P=0.5), tw=1.0 → contribution = 0.5 × 1.0 = 0.50
Search→Cart:  no CB (P=0.9),      tw=0.8 → contribution = 0.9 × 0.8 = 0.72

CC(Cart) = 0.50 + 0.72 = 1.22
```

**After full circuit breakers** on Payment→Cart and Search→Cart (P reduced to 0):

```
CC(Cart) = 0 × 1.0 + 0 × 0.8 = 0.0
```

Minor incidental callers contribute negligibly. Target CC(Cart) ≈ 0.0–0.2.

**RDR target at 90-day review**:

Formula: RDR = new_mode / old_mode, target < 0.10.

```
Pre-fix Cart incident rate  = 2.0 incidents/month

Post-fix (Cart bug fixed + circuit breakers deployed):
  Cart root-cause incidents: ~0.3/month residual (different failure modes remain)
  Cascade incidents:         0 (circuit breakers prevent cascade to Payment and Search)
  Total post-fix rate:       0.3 incidents/month

RDR = 0.3 / 2.0 = 0.15
```

RDR = 0.15 is above the 0.10 target. The fix is effective but not perfect — residual Cart instability exists from other root causes.

**Recommendation**: Set a 90-day RDR review. If RDR > 0.10 at 90 days, investigate the residual 0.3/month failure modes as a separate workstream. The circuit breakers are independently valuable regardless of residual Cart rate — they prevent cascade from any future Cart failure, not just this one bug.

**Key Insight**: RDR separates "did we fix this specific bug" from "did we fix the service's reliability." RDR = 0.15 at 90 days means the bug was fixed but the service has other failure modes. That is useful signal for prioritizing the next reliability investment.

---

## Scenario 3: Loyalty Points Service Integration

**Setup**: Loyalty Points service to be inserted in Checkout between Payment and Order Management. It calls Auth (P0, tw=1.0) and a third-party loyalty API (P2, tw=0.5). Test coverage: 70%. Canary plan: 6 hours.

---

### 3(a) New CD and Required SLO per Service

**Current checkout path**: API Gateway → Auth → Cart → Payment → Order Management (CD=5)

**New checkout path**: API Gateway → Auth → Cart → Payment → Loyalty Points → Order Management (CD=6)

**Formula**: Required_SLO = SLA^(1/CD)

**Step 1** — Compute required SLO at CD=6:

```
Required_SLO = 0.9995^(1/6)

Using logarithm approximation:
ln(0.9995)    = -0.00050012
÷ 6           = -0.000083353
e^(-0.000083353) ≈ 0.999917

Required_SLO = 99.9917% ≈ 99.992%
```

**Step 2** — Compare to prior requirement at CD=5:

```
Prior (CD=5): 0.9995^(1/5) = e^(-0.0001) ≈ 99.990%
New  (CD=6):  0.9995^(1/6)              ≈ 99.992%
Delta:        +0.002 percentage points per service
```

**Answer**: New CD=6. Required per-service SLO = 99.992% (up from 99.990% at CD=5).

**Why the 0.002pp gap matters**: Auth's MTBI-implied availability is approximately 99.896% (based on MTBI/MTTR analysis from prior exercises). Auth already fails to meet the CD=5 requirement of 99.990%. Adding Loyalty Points tightens the required SLO for every existing service in the path — including Auth, which was already non-compliant. Inserting Loyalty Points makes checkout SLA compliance structurally harder before the new service even has a reliability track record.

**Key Insight**: Adding one hop to a CD=5 path raises the required SLO per service by only 0.002pp in absolute terms, but that shift matters because it moves the compliance bar for every existing service — including those already below the prior bar.

---

### 3(b) GEI for Loyalty Points

**Formula**: GEI = (new_deps x avg_tw) / (coverage x canary_hrs)

**Given**: new_deps=2 (Auth and loyalty API), avg_tw=(1.0+0.5)/2=0.75, coverage=0.70, canary_hrs=6.

**Step 1** — Compute numerator:

```
new_deps × avg_tw = 2 × 0.75 = 1.50
```

**Step 2** — Compute denominator:

```
coverage × canary_hrs = 0.70 × 6 = 4.20
```

**Step 3** — Compute GEI:

```
GEI = 1.50 / 4.20 = 0.357
```

**Step 4** — Interpret:

```
GEI < 1.0 → LOW risk: standard canary sufficient
GEI 1–2   → MODERATE risk: extended canary (2 weeks) required
GEI > 2.0 → HIGH risk: phased rollout with VP approval
```

GEI = 0.357 → LOW. Standard 6-hour canary is sufficient.

**Answer**: GEI = 0.357 → Low integration risk. Proceed with standard 6-hour canary.

**Sensitivity check — shortened canary**:

```
If canary_hrs = 2:
GEI = 1.50 / (0.70 × 2) = 1.50 / 1.40 = 1.071 → MODERATE
```

Shortening to 2 hours flips GEI from LOW to MODERATE, requiring a 2-week extended canary instead. The 6-hour canary is the minimum duration that keeps GEI in the acceptable range for this coverage level. Do not allow the team to shorten it.

**Key Insight**: GEI reveals that canary duration is the most controllable lever for new service integration risk. Coverage is hard to increase quickly; dependency count is fixed by design. Duration is the dial the SRE controls on the day.

---

### 3(c) New LBH at CD=6

**Formula**: LBH = (e2e_p99 - overhead) / CD

**Given**: Checkout p99 SLA = 2,000ms. Infrastructure overhead = 150ms.

**Step 1** — Compute LBH at CD=6:

```
LBH = (2000 - 150) / 6
    = 1850 / 6
    = 308ms per hop
```

**Step 2** — Compare to prior LBH at CD=5:

```
Prior LBH (CD=5) = (2000 - 150) / 5 = 1850 / 5 = 370ms per hop
New LBH  (CD=6) = (2000 - 150) / 6 = 1850 / 6 = 308ms per hop
Delta            = -62ms per hop
```

**Answer**: New LBH = 308ms per hop (down from 370ms). Every service on the checkout path loses 62ms of latency headroom.

**Impact on existing services**:

| Service | Estimated p99 | Prior headroom (370ms) | New headroom (308ms) | Status |
|---|---|---|---|---|
| Auth | ~280ms | 90ms | 28ms | TIGHT |
| Cart | ~150ms | 220ms | 158ms | OK |
| Payment | ~200ms | 170ms | 108ms | OK |
| Order Mgmt | ~220ms | 150ms | 88ms | OK |

Auth at 280ms has only 28ms of headroom under the new LBH. Under 4x Black Friday traffic, Auth latency typically degrades. Any p99 regression above 308ms breaches the new tighter LBH — and Auth was previously 90ms below budget.

**Key Insight**: Adding Loyalty Points does not slow down Auth. But it shrinks Auth's latency headroom from 90ms to 28ms. The same Auth performance that was safely within budget at CD=5 becomes a near-breach at CD=6.

---

### 3(d) SCS with Loyalty Points at 99.99% Individual SLO

**Formula**: SCS = SLO^CD / SLA

**Step 1** — Compute compound availability at CD=6, all services at 99.99%:

```
Compound = 0.9999^6

ln(0.9999) = -0.00010001
6 × (-0.00010001) = -0.00060006
e^(-0.00060006) ≈ 0.99940

Compound = 99.940%
```

**Step 2** — Compute SCS:

```
SCS = 0.99940 / 0.9995
    = 0.99990
    ≈ 1.000
```

SCS = 1.000 is within the valid range [0.95, 1.10].

**Answer**: SCS ≈ 1.000 → Coherent SLO declarations.

**Hidden shortfall**: From part (a), the required SLO per service is 99.992%, not just 99.99%. If all 6 services achieve only 99.99%:

```
Compound at 99.99% × 6 = 0.9999^6 = 0.99940 = 99.940%
SLA required             =           0.9995   = 99.950%
Gap                      = 0.010pp below SLA
```

SCS can read 1.000 (internally coherent) while the compound availability still misses the SLA by 0.010pp. The system is breaching its customer commitment even when all services hit their declared SLOs — because those SLOs were set for CD=5, not CD=6.

**Key Insight**: SCS tells you whether declarations are internally consistent. It does not tell you whether the compound outcome meets the SLA. Always verify both: SCS within [0.95, 1.10] AND compound availability >= SLA.

---

### 3(e) MRI for Future Loyalty Changes

**Formula**: MRI = DG x CD x (1 - FLI) x (2 - OCR)

**Step 1** — Compute DG for Loyalty Points service:

Direct dependencies Loyalty calls (proximity=1.0):
- Auth: P0, tw=1.0 → contribution = 1.0 × 1.0 = 1.0
- Loyalty API: P2, tw=0.5 → contribution = 0.5 × 1.0 = 0.5

Callers of Loyalty that depend on it (proximity=0.5, one-hop):
- Order Management: P0, tw=1.0 → contribution = 1.0 × 0.5 = 0.5

```
DG(Loyalty) = 1.0 + 0.5 + 0.5 = 2.0
```

**Step 2** — Compute MRI using system health values and new CD=6:

```
MRI = DG × CD × (1 - FLI) × (2 - OCR)
    = 2.0 × 6 × (1 - 0.72) × (2 - 0.457)
    = 2.0 × 6 × 0.28 × 1.543
    = 12.0 × 0.28 × 1.543
    = 3.36 × 1.543
    = 5.18
```

**Answer**: MRI = 5.18 → VP Engineering approval required (MRI range 3–8 requires VP sign-off).

**Why a low-DG service still triggers VP approval**: Loyalty's DG=2.0 is modest — 3 connections total. But the system multipliers (FLI=0.72, OCR=0.457, CD=6) amplify the MRI significantly. The governance framework correctly identifies that the system's health state — not just the service's individual footprint — determines deployment risk. A service inserted into a fragile, under-observed, high-cascade system requires more scrutiny regardless of how small it appears on its own.

**Key Insight**: MRI is a function of system health as much as service footprint. Improving OCR from 0.457 to 0.90 would reduce this same MRI from 5.18 to approximately 2.0 — below the VP approval threshold. Investment in observability directly reduces governance overhead for future changes.

---

### 3(f) Three SRE Approval Conditions for Loyalty Points

Before approving Loyalty Points for production, all three conditions must be verified in writing:

**Condition 1 — Canary gate (GEI condition)**:
Loyalty Points must sustain >= 99.992% SLO and < 308ms p99 latency during the full 6-hour canary at >= 5% of checkout traffic, with no SLO breach, before any traffic increment. The canary duration must not be shortened below 6 hours — doing so raises GEI from 0.357 to 1.071 and changes the approval tier from standard to extended canary.

**Condition 2 — Cascade containment (CC condition)**:
Two circuit breakers must be implemented, tested under simulated failure, and verified in staging before go-live:
- Loyalty→Auth: If Auth is unreachable, allow the transaction to proceed and validate loyalty eligibility asynchronously. Do not fail the checkout for Auth unavailability within the Loyalty call path.
- Loyalty→loyalty_api: If the third-party loyalty API fails, skip points calculation and complete checkout without points. Do not propagate a third-party API failure to the customer-facing checkout flow.

Both fallback behaviors must be load-tested at simulated failure conditions in staging before approval is granted.

**Condition 3 — Instrumentation (OCR condition)**:
Full four-signal golden signal instrumentation (latency, traffic, errors, saturation) must be deployed and verified producing live data in the monitoring system before go-live. Loyalty Points is being added to the highest-criticality path (CD=6, P0-adjacent). An uninstrumented service on this path directly degrades OCR_path for checkout and removes the team's ability to distinguish Loyalty-caused latency from Auth or Payment latency during future incidents.

**Key Insight**: These three conditions correspond directly to the three weakest system health metrics — FLI (Condition 2 improves cascade containment), OCR (Condition 3 adds observability), GEI (Condition 1 enforces deployment rigor). Approval conditions should always be designed to improve system health, not just gate the deployment.

---

## Scenario 4: Reviews Service Decommission

**Setup**: Reviews (P3, tw=0.3) is being decommissioned. Declared callers: Product Catalog only. 60-day observed traffic: Product Catalog 45 rps, Recommendation 12 rps, Search 8 rps, unknown caller 3 rps.

---

### 4(a) SCI Calculation

**Formula**: SCI = (observed - declared) / total_observed

**Step 1** — Compute total observed traffic:

```
total_observed = 45 + 12 + 8 + 3 = 68 rps
```

**Step 2** — Identify declared traffic:

```
declared = 45 rps (Product Catalog — the only documented caller)
```

**Step 3** — Compute SCI:

```
SCI = (68 - 45) / 68
    = 23 / 68
    = 0.338
```

**Answer**: SCI = 0.338. Decommission BLOCKED.

**What this means**: 33.8% of all traffic to Reviews has no documented owner. Three undocumented callers (Recommendation at 12 rps, Search at 8 rps, unknown at 3 rps) account for 34% of all Reviews traffic. Decommissioning now would immediately break these callers with no notification, no migration plan, and no owner tickets.

**Key Insight**: SCI converts "we think only Product Catalog calls this" into "33.8% of actual traffic is unexplained." This is the entire value of the metric — it replaces assumption with measurement before a destructive action is taken.

---

### 4(b) What Must Happen Before SCI = 0

The decommission gate requires SCI = 0. Five sequential steps are required:

**Step 1 — Identify all undocumented callers**:
Pull service mesh logs, distributed tracing (Jaeger, X-Ray, or equivalent), and API gateway access logs for the 60-day observation window. Identify the source service IDs for Recommendation (12 rps), Search (8 rps), and the unknown 3 rps caller. The unknown caller must be identified by IP address, service account, or trace header before proceeding to Step 2.

**Step 2 — Notify each caller team**:
Create tickets for the Recommendation team, Search team, and unknown caller's team (once identified). Notification must include: service name calling Reviews, current rps volume, decommission target date, and whether the migration path is to Reviews v2 or a full dependency removal.

**Step 3 — Migrate or remove each dependency**:
Each caller team either updates their integration to the Reviews v2 endpoint, or removes the Reviews dependency entirely from their service. The SRE team tracks progress against the target date and escalates blockers.

**Step 4 — Verify traffic cessation**:
Monitor Reviews v1 traffic in real-time. Each undocumented caller's traffic must reach 0 rps and remain at 0 rps. Use the same monitoring that produced the 60-day baseline. A single rps from any previously-undocumented caller restarts the verification clock.

**Step 5 — Re-run SCI check**:
After all callers have stopped calling Reviews v1 (including Product Catalog migrating to v2):

```
observed_on_v1 = 0 rps (all callers migrated or removed)
declared       = 0 rps (Product Catalog now on v2, no longer calls v1)
```

If Reviews v1 receives 0 rps for 30+ consecutive days, SCI is effectively 0. Proceed to decommission.

**Key Insight**: The five steps are linear and each gates the next. Skipping Step 1 (identifying the unknown caller) makes Steps 2 through 5 impossible to complete correctly.

---

### 4(c) Unknown 3 rps Caller Not Identified After 5 Days

**SRE recommendation**: Do not decommission on the original timeline. Extend by minimum 2 weeks.

**Reasoning**:

3 rps may appear trivial but the caller is unknown — which means:

- **Criticality unknown**: A compliance auditing service, billing reconciliation job, or executive dashboard could call Reviews at low steady-state volume but fail critically if Reviews disappears. Low rps does not mean low criticality.
- **Blast radius unknown**: Breaking it could trigger a financial reconciliation failure, a compliance reporting gap, or an executive-visible dashboard outage — none of which would be traceable to the Reviews decommission without post-incident forensics.
- **Failure mode unknown**: Unlike a service that returns errors immediately, the caller might cache Reviews responses and fail silently for hours or days after decommission, making root cause analysis extremely difficult.

**Action plan when the 5-day window closes without identification**:

1. **Extend timeline by 2 weeks** — document the extension with the reason. Do not miss the gate; push the gate.
2. **Escalate to platform engineering** — enable distributed tracing (or increase trace sampling rate) specifically on the Reviews v1 endpoint to capture caller identity on every request.
3. **Zombie services registry** — if the caller remains unidentified after 2 more weeks, add Reviews v1 to a monitored zombie services registry with an automated alert if traffic deviates from the 3 rps baseline.
4. **Do not hard-delete Reviews v1** — deprecate (stop taking new feature work, disable on-call coverage for non-P0 issues), but leave the service running until SCI=0 is achieved and verified.

The SCI gate exists precisely for this situation. Timeline pressure never justifies bypassing a gate whose entire purpose is to prevent silent breakage of undocumented dependencies.

**Key Insight**: The worst outcome is not a delayed decommission — it is a decommission that breaks an unknown production caller at 3 AM and takes two hours to trace back to the Reviews removal. The gate is cheaper than the incident.

---

### 4(d) Observation Period After SCI = 0

**Minimum observation period**: 30 days of confirmed SCI=0 before executing the decommission.

**Why 30 days (not 7, not 14)**:

The 30-day window covers three specific risk patterns that shorter windows miss:

**Risk 1 — Monthly billing and reporting cycles**: Some services call Reviews only at month-end to generate reports, reconcile data, or produce compliance artifacts. A 7-day or 14-day observation would miss these callers entirely. Reviews handles product review data — a monthly content audit or catalog refresh job could be a low-frequency but critical caller.

**Risk 2 — Scheduled jobs and cron processes**: Jobs running on weekly or monthly schedules would not appear in a single week's traffic sample. The 30-day window captures at least one full monthly cycle, catching monthly scheduled callers that the daily traffic view misses.

**Risk 3 — Weekend vs. weekday patterns**: Traffic to Reviews may be lower during business hours (when engineers are writing code) and higher on weekends (when customers browse and submit reviews). A weekday-only observation window produces a biased sample and misses weekend-driven traffic patterns.

**After 30 days of confirmed SCI=0**:

Execute the decommission during a planned maintenance window with:
- Rollback procedure documented: if any service reports unexpected errors in the 7 days following decommission, Reviews v1 can be restored from the last known good state.
- Post-decommission monitoring alert in place: 7-day watch for any services reporting 503 or connection-refused errors correlating with the Reviews v1 DNS removal.
- Decommission record: document the date, final SCI verification, all callers migrated or removed, and the approving SRE. This becomes the evidence trail if a future incident ever traces back to the Reviews removal.

**Key Insight**: The 30-day observation period is not bureaucratic caution — it is the minimum window to observe the full monthly call pattern of any caller. Decommissioning after 30 days of silence gives high confidence that no monthly caller was missed. Decommissioning after 7 days does not.

---

## Summary: What the Integrated Scenarios Teach

These four scenarios share a common pattern: the framework converts intuition into defensible numbers.

| Scenario | Key Finding | How the Framework Surfaces It |
|---|---|---|
| Black Friday | System is architecturally unsafe for 4x traffic | JRCS = -0.035; SRMI = 0.179 (1.6% of target maturity) |
| Incident | Root cause was the recent deployment, not the loudest alert | Suspicion(Cart)=0.30 vs. Suspicion(Search)=0.05 |
| Integration | Adding 1 service raises the required SLO for every existing service | CD=5→6 raises Required_SLO from 99.990% to 99.992% per hop |
| Decommission | 34% of traffic has no documented owner | SCI = 0.338; 3 undocumented callers identified |

In each case, the answer was not obvious before the calculation. That is what the framework is for.

**The integrated view**: all four scenarios operate on the same system with OCR=0.457, FLI=0.72, CC_max=10.8. These three numbers appear in every scenario as amplifiers of every other risk. The most leveraged improvement in this system is not fixing any individual service — it is raising OCR, FLI, and reducing CC_max. Doing so would:

- Make JRCS positive (Black Friday safe)
- Improve FLI_incident for future Cart failures (Incident)
- Reduce MRI for Loyalty Points below the VP approval threshold (Integration)
- Have no effect on SCI (Decommission) — SCI is a process gate, not a health metric

The framework is an X-ray. The scenarios are what you see when you hold the system up to the light.
