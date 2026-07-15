# Solutions: Exercise Set 2 — Blast Radius Terms (DG, BRI, CC, FLI, DSA)

---

## Formula Reference

```
DG  = Σ[tier_weight × proximity_discount]
      proximity: direct=1.0, one-hop=0.5, two-hop=0.25

BRI = (affected_users/total) × journey_criticality × tier_weight_of_failing_service
      SEV1 >0.70 | SEV2 0.30–0.70 | SEV3 0.10–0.30 | SEV4 <0.10

CC  = Σ[P(dep_fails|X_fails) × tier_weight(dep)]
      P: no CB=0.9, partial CB=0.5, full CB=0

FLI = contained_failure_events / total_failure_events   [target >0.90]

DSA = Σ[1×tw_direct] + Σ[0.5×tw_transitive]
```

---

## Section B — Guided Exercises

### B1: DG(Pricing Service)

**Approach**: DG measures how many "gravity units" of impact the Pricing service can exert across the system — both upstream (what it calls) and downstream (what calls it). Tally all nodes with their tier weight and proximity discount.

**Direct dependencies (Pricing calls these):**

| Dependency | Tier | tw | Proximity | Contribution |
|------------|------|-----|-----------|-------------|
| Product Catalog | P1 | 0.8 | direct (1.0) | 0.8 |
| Auth | P0 | 1.0 | direct (1.0) | 1.0 |
| External Pricing API | P2 | 0.5 | direct (1.0) | 0.5 |

**Direct callers (these call Pricing):**

| Caller | Tier | tw | Proximity | Contribution |
|--------|------|-----|-----------|-------------|
| Cart | P0 | 1.0 | direct (1.0) | 1.0 |
| Search | P1 | 0.8 | direct (1.0) | 0.8 |

**DG calculation:**

```
DG(Pricing) = 0.8 + 1.0 + 0.5 + 1.0 + 0.8
            = 4.1
```

**Answer**: DG(Pricing) = 4.1

**Key Insight**: DG=4.1 looks moderate, but Pricing includes a P0 dependency (Auth) and a P0 caller (Cart). When Pricing degrades, it directly impacts the most critical service in the platform. A DG score does not capture which nodes in the graph are highest-risk — always inspect the composition. Pricing should be operated with P0-equivalent change rigor because of who calls it, not just what its tier weight declares.

---

### B2: BRI — Notification Duplicate Bug

**Approach**: BRI quantifies blast radius as user impact × journey importance × service weight. A bug that sends duplicate notifications is noisy but not revenue-blocking.

**Given values:**
- Affected users: 8% of active users → 0.08
- Journey criticality: 0.3 (notification journey is low-criticality)
- Tier weight of failing service: Notification = P2 → tw = 0.5

**Step 1 — BRI calculation:**

```
BRI = (affected_users/total) × journey_criticality × tier_weight
    = 0.08 × 0.3 × 0.5
    = 0.012
```

**Step 2 — Severity mapping:**

```
BRI = 0.012 < 0.10 → SEV4
```

**Answer**: BRI = 0.012 → SEV4

**Key Insight**: BRI = 0.012 correctly classifies duplicate notifications as low-severity even though 8% of users are affected. The math captures what SREs know intuitively: annoying ≠ critical. The journey criticality factor (0.3) is the key moderating element — a 99% user-affecting bug in a P2 notification service is still not a SEV1 because no revenue is blocked and no orders fail. If this same bug occurred in the Checkout journey (criticality=1.0), BRI = 0.08 × 1.0 × 0.5 = 0.04, still SEV4. If it occurred in Cart (tw=1.0), BRI = 0.08 × 1.0 × 1.0 = 0.08, still SEV4. BRI rewards accurate tier assignment — do not tier-inflate services.

---

### B3: CC(Inventory) — Before and After Circuit Breakers

**Approach**: CC measures how likely it is that Inventory's failure cascades to its dependents. P(cascade)=0.9 with no CB, 0.5 with partial CB, 0 with full CB. Sum over all dependents weighted by tier.

**Inventory's key callers (services that call Inventory):**

| Caller | Tier | tw | CB State (before) | P(cascade) | Contribution |
|--------|------|-----|-------------------|-----------|-------------|
| Cart | P0 | 1.0 | None | 0.9 | 0.9 |
| Order Mgmt | P0 | 1.0 | None | 0.9 | 0.9 |
| Pricing | P1 | 0.8 | Partial | 0.5 | 0.4 |

**CC(Inventory) — No circuit breakers:**

```
CC = 0.9×1.0 + 0.9×1.0 + 0.5×0.8
   = 0.9 + 0.9 + 0.4
   = 2.2
```

**CC(Inventory) — After full CBs on Cart→Inventory and OM→Inventory:**

```
CC = 0×1.0 + 0×1.0 + 0.5×0.8
   = 0 + 0 + 0.4
   = 0.4
```

**Answer**: CC drops from 2.2 → 0.4. An 82% reduction in cascade coupling with two circuit breakers.

**Key Insight**: The two highest-contribution callers (Cart and Order Mgmt, both P0 tw=1.0) are also the most dangerous cascade paths — Inventory failure without CBs will reliably bring down the checkout flow. Adding full CBs on just those two connections drops CC from 2.2 to 0.4. This is the circuit breaker ROI principle: target the highest-weight caller paths first, and you get dramatic CC reduction with minimal engineering investment.

---

## Section C — Applied Problems

### C1: Cascade Analysis — Search → Pricing → Cart

**Approach**: When a multi-service cascade occurs, compute FLI (how many failures were contained), BRI (how severe was the impact), and then identify the circuit breaker placements that would prevent future recurrence.

**Incident timeline:**
- Search degrades → Pricing cannot get search-based data → Cart cannot get prices → Checkout fails

**FLI calculation:**

```
Total failure events:
  1. Search (original failure)
  2. Pricing (cascaded from Search)
  3. Cart (cascaded from Pricing)
  Total = 3 events

Contained failures = 1 (only Search was contained — the others propagated)

FLI_incident = contained / total
             = 1 / 3
             = 0.33
```

FLI = 0.33. Far below the 0.90 target. This incident had almost no containment.

**BRI calculation:**

```
Affected users = 25% of checkout attempts → 0.25
Journey criticality = checkout → 1.0 (highest)
Tier weight of origin failure = Search is P1 → tw = 0.8

BRI = 0.25 × 1.0 × 0.8
    = 0.20

Wait — cascade reached Cart (P0, tw=1.0). Use the highest-impact service in the chain.

BRI = 0.25 × 1.0 × 1.0
    = 0.25
```

BRI = 0.25 → SEV3 (0.10–0.30 range). (At the boundary of SEV2 if affected user fraction rises slightly.)

**Two circuit breaker placements to prevent recurrence:**

1. **CB on Pricing → Search**: Pricing should not fail if Search is degraded. Implement a CB that triggers when Search p99 > threshold, and returns cached or default pricing data. Pricing fails open gracefully.

2. **CB on Cart → Pricing**: Cart must be able to render items and accept add-to-cart even when Pricing is degraded. Implement a CB that triggers on Pricing error rate > threshold, and returns last-known or estimated price with a "price may vary" flag.

**Key Insight**: The cascade went three hops because no hop had a circuit breaker or graceful degradation. FLI=0.33 means the system has essentially no self-protection. A single Search degradation took down Checkout — a P0 journey. The fix is not to make Search more reliable. The fix is to ensure that Search's reliability is irrelevant to Cart's ability to function.

---

### C2: DSA(Inventory)

**Approach**: DSA (Dependency Surface Area) measures total exposure through both direct and transitive connections. Direct deps get full weight; transitive get 50% discount.

**Direct dependencies of Inventory:**

| Dependency | Tier | tw | DSA contribution (×1) |
|------------|------|-----|----------------------|
| PostgreSQL | P0 | 1.0 | 1.0 |
| Redis | P0 | 1.0 | 1.0 |
| Auth | P0 | 1.0 | 1.0 |
| Product Catalog | P1 | 0.8 | 0.8 |

```
DSA_direct = 1.0 + 1.0 + 1.0 + 0.8 = 3.8
```

**Transitive dependencies (through Inventory's callers):**

Cart depends on Auth and Product Catalog (Inventory's caller brings these into transitive scope).
Order Management depends on Notification service.

```
Transitive through Cart: Auth (tw=1.0), Product Catalog (tw=0.8)
  — but Auth is already a direct dep, count once
  New transitive: Product Catalog already counted
  Net new transitive: 0 (all already in direct scope)

Transitive through Order Mgmt: Notification (P2, tw=0.5)
  DSA_transitive from OM path: 0.5 × 0.5 = 0.25

Additional transitive surface from Cart callers bringing new paths:
  Estimate unique transitive additions ≈ 0.5 × (1.0 + 0.5) = 0.75

DSA_transitive ≈ 0.25 + 0.75 = 1.0 (order of magnitude estimate)
```

```
DSA(Inventory) = DSA_direct + DSA_transitive
               = 3.8 + 1.0
               ≈ 4.8
```

**Answer**: DSA(Inventory) ≈ 4.8

**Should Inventory be operated as P0?** Yes.

DSA = 4.8 means Inventory has significant exposure surface — multiple P0 direct dependencies and transitive reach through high-criticality callers. More importantly: Inventory's callers include Cart and Order Management, both P0. When Inventory fails, P0 services fail. The correct operational tier for any service is max(its_declared_tier, the_tier_of_its_highest-tier_caller). Inventory's declared tier (P1) understates its operational criticality.

**Key Insight**: DSA reveals hidden complexity. A service with DSA=4.8 is not a simple service even if it is declared P1. DSA is a better guide for change review requirements than tier weight alone — use DSA to override tier-based routing when a lower-tier service has unusually high surface area.

---

## Section D — Advanced Capstone: Auth Failure Cascade

### D(a): FLI Without Circuit Breakers

**Incident: Auth fails, no CBs anywhere**

```
Events:
  1. Auth (original failure)
  2. Cart cascades (calls Auth, no CB)
  3. Payment cascades (calls Auth, no CB)
  4. Order Mgmt cascades (calls Auth, no CB)

Total events = 4
Contained = 1 (Auth only)

FLI = 1/4 = 0.25
```

FLI = 0.25. The system has 25% containment — far below the 0.90 target. Three of four failure events propagated.

---

### D(b): BRI at Peak

**Given: Auth fails at checkout peak, 55% of users affected**

```
BRI = (affected_users/total) × journey_criticality × tier_weight(Auth)
    = 0.55 × 1.0 × 1.0
    = 0.55
```

BRI = 0.55 → SEV2 (0.30–0.70 range).

At peak this could escalate to SEV1 if checkout revenue impact exceeds the 0.70 BRI threshold (e.g., if 72%+ of users are affected during a traffic spike).

---

### D(c): New CC(Auth) After Circuit Breakers on Main Dependents

**After adding full CBs on Cart→Auth, Payment→Auth, Order Mgmt→Auth:**

These three callers now contribute 0 to CC. Remaining callers of Auth (smaller services):

```
Remaining callers (estimate):
  Search:       P1, tw=0.8, no CB → P=0.9 → 0.9×0.8 = 0.72
  User Profile: P2, tw=0.5, no CB → P=0.9 → 0.9×0.5 = 0.45

CC(Auth) after CBs on 3 main callers = 0.72 + 0.45 = 1.17
```

Previous CC(Auth) without any CBs = 0.9×1.0 + 0.9×1.0 + 0.9×1.0 + 0.9×0.8 + 0.9×0.5 = 0.9+0.9+0.9+0.72+0.45 = 3.87

**CC drops from 3.87 → 1.17 with three circuit breakers.** A 70% reduction.

---

### D(d): FLI With Circuit Breakers

**With full CBs on Cart, Payment, and Order Mgmt paths:**

```
Events:
  1. Auth (original failure)
  CBs on Cart, Payment, OM fire — cascades stopped

Contained = 1 (Auth only — cascade stopped at CB boundary)
Total = 1

FLI = 1/1 = 1.00
```

FLI = 1.00. Perfect containment. The three circuit breakers completely prevent cascade propagation. This is the target state: failures occur (Auth is not made more reliable), but they are fully contained.

---

### D(e): JRCS Before and After

**JRCS formula:**
```
JRCS = SCS × FLI × OCR_path × (1 - CC_max/10)
```

**Current state (before CBs):**

```
SCS = 1.0 (assumed coherent)
FLI = 0.72 (system-wide)
OCR_path = 0.70 (estimated for checkout path)
CC_max = 10.8 (Auth's cascade coupling, system max)

JRCS = 1.0 × 0.72 × 0.70 × (1 - 10.8/10)
     = 1.0 × 0.72 × 0.70 × (1 - 1.08)
     = 1.0 × 0.72 × 0.70 × (-0.08)
     = NEGATIVE (-0.040)
```

JRCS is negative. Checkout is not systemically safe. CC_max > 10 means cascade risk exceeds the safety margin built into the formula — the journey will cascade on any Auth failure.

**After CBs (estimated new state):**

```
SCS = 1.0 (unchanged)
FLI = 0.90 (improved from 0.72, after CBs raise containment)
OCR_path = 0.70 (unchanged)
CC_max = 1.17 (new Auth CC after CBs)

JRCS = 1.0 × 0.90 × 0.70 × (1 - 1.17/10)
     = 1.0 × 0.90 × 0.70 × 0.883
     = 0.556
```

JRCS = 0.556. The journey moves from negative (systemically unsafe) to 0.556 (healthy positive). A completely different risk profile from three circuit breakers.

---

### D(f): Investment Brief for Circuit Breaker Implementation

```
PROPOSAL: Circuit Breakers on Cart→Auth, Payment→Auth, Order Mgmt→Auth

WHAT IT FIXES:
  - CC(Auth): 3.87 → 1.17 (70% cascade coupling reduction)
  - FLI during Auth incidents: 0.25 → 1.00 (full containment)
  - JRCS(Checkout): negative → 0.556 (systemically safe)

COST:
  - Engineering effort: 40 hours (1 engineer, 1 sprint week)
  - Implementation pattern: standard CB library (Resilience4j / go-breaker)
  - Testing: 8 hours chaos testing in staging

WHAT IT PREVENTS:
  - Auth fails approximately 12 times per year (MTBI=30d estimate)
  - Without CBs: each Auth failure cascades → 3 cascade-incidents per Auth failure
  - 12 Auth failures × 3 cascades = 36 cascade-incidents prevented per year
  - Each cascade-incident: 2 SREs × 2 hours response = 4 SRE-hours
  - 36 incidents × 4 SRE-hours = 144 SRE-hours/year eliminated

ROI CALCULATION:
  - Fix cost: 40 hours (one-time)
  - Annual savings: 144 SRE-hours
  - Payback period: 40/144 = 3.3 months

ADDITIONAL VALUE (not counted above):
  - SLA breach prevention: current cascade rate is the primary driver of
    SEV1/SEV2 SLA breaches; eliminating cascades likely prevents 2-3 SLA
    breach months per year
  - Customer trust: checkout cascade during Auth failure is the highest-
    visibility incident type

DECISION REQUIRED: Engineering sprint allocation — 40 hours, next sprint.
RISK IF DEFERRED: Next Auth failure incident will cascade. MTBI=30d.
```

---

## Quick Reference — Key Answers

| Exercise | Formula | Result | Decision |
|----------|---------|--------|----------|
| B1 DG(Pricing) | Σ tw×prox | 4.1 | Operate as P0-equivalent due to P0 caller |
| B2 BRI(Notification dup) | 0.08×0.3×0.5 | 0.012 | SEV4 |
| B3 CC(Inventory) no CB | 0.9×1.0+0.9×1.0+0.5×0.8 | 2.2 | Needs CBs |
| B3 CC(Inventory) with CB | 0+0+0.5×0.8 | 0.4 | Safe |
| C1 FLI (cascade) | 1/3 | 0.33 | Far below 0.90 target |
| C1 BRI (checkout) | 0.25×1.0×1.0 | 0.25 | SEV3 |
| C2 DSA(Inventory) | 3.8+1.0 | 4.8 | Operate as P0 |
| D(a) FLI no CB | 1/4 | 0.25 | Unacceptable |
| D(b) BRI peak Auth | 0.55×1.0×1.0 | 0.55 | SEV2 |
| D(c) CC after 3 CBs | 0.72+0.45 | 1.17 | 70% reduction |
| D(d) FLI with CBs | 1/1 | 1.00 | Perfect containment |
| D(e) JRCS before | negative | -0.040 | Systemically unsafe |
| D(e) JRCS after | 0.90×0.70×0.883 | 0.556 | Safe |
