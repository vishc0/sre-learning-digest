# Solutions: Exercise Set 1 — Structural Terms (CD, SCS, LBH)

---

## Formula Reference

```
CD  = count(sequential_sync_hops)
Required_SLO = SLA^(1/CD)
SCS = declared_SLO^CD / customer_SLA   [target 0.95–1.10]
LBH = (end_to_end_p99 - infra_overhead) / CD
```

---

## Section B — Guided Exercises

### B1: Order Tracking (CD=2)

**Approach**: Count synchronous hops in the call chain. Order Tracking calls Auth, then fetches from Order Management. Two sequential hops = CD=2.

**Step 1 — Required SLO per service**

```
Required_SLO = SLA^(1/CD)
             = 0.995^(1/2)
             = 0.995^0.5
             = 0.99750
             = 99.750%
```

**Step 2 — Latency Budget per Hop**

```
LBH = (end_to_end_p99 - infra_overhead) / CD
    = (1000ms - 100ms) / 2
    = 900ms / 2
    = 450ms per hop
```

**Answer**: Each service must sustain 99.750% availability. Each hop has 450ms to complete at p99.

**Key Insight**: At CD=2 the per-service requirement (99.75%) is well within what well-operated services achieve. The 450ms LBH is generous. This journey is structurally safe — low CD protects it from compound failure math.

---

### B2: Returns Portal (CD=5)

**Approach**: Trace the call chain synchronously. Returns Portal → API Gateway → Auth → Order Management → Inventory → Returns Service. That is 5 sequential synchronous hops.

**Step 1 — CD**

```
Hops: API GW → Auth → Order Mgmt → Inventory → Returns
CD = 5
```

**Step 2 — Required SLO**

```
Required_SLO = SLA^(1/CD)
             = 0.99^(1/5)
             = 0.99^0.2
             = 0.9980
             = 99.80%
```

**Step 3 — Latency Budget per Hop**

```
LBH = (3000ms - 200ms) / 5
    = 2800ms / 5
    = 560ms per hop
```

**Answer**: Each service must sustain 99.80% availability. Each hop has 560ms to complete at p99.

**Key Insight**: At CD=5 the per-service requirement (99.80%) is relaxed compared to the customer SLA (99.0%) — which seems counterintuitive. The math works because 0.9980^5 = 0.990 which just barely meets the SLA. The latency budget of 560ms is comfortable. Returns Portal is structurally sound at CD=5 for a 99.0% SLA.

---

### B3: SCS Analysis — All Services at 99.99%

**Approach**: SCS tells you whether declared SLOs, when compounded, actually cover the customer SLA. SCS in [0.95, 1.10] means the system is coherent — not over-promising, not dramatically over-engineering.

**Case 1: All 5 services declare 99.99%**

```
compound = 0.9999^5
         = 0.9999 × 0.9999 × 0.9999 × 0.9999 × 0.9999
         = 0.99950 (approximately 0.9995)

SCS = compound / customer_SLA
    = 0.9995 / 0.9995
    = 1.000
```

SCS = 1.000. Exactly in range [0.95, 1.10]. The declared SLOs precisely cover the customer commitment.

**Case 2: One service declares 99.95% (others remain 99.99%)**

```
compound = 0.9999^4 × 0.9995
         = 0.9996 × 0.9995
         = 0.9991

SCS = 0.9991 / 0.9995
    = 0.9996
```

SCS = 0.9996. Still in range [0.95, 1.10]. The customer SLA remains achievable but the margin is razor thin.

**Answer**: Both cases are coherent. The second case (SCS=0.9996) is tighter — one further degradation in any service would push SCS below 0.95 and make the customer SLA mathematically unachievable.

**Key Insight**: SCS is not a binary pass/fail — it shows margin. SCS=1.000 means you have exactly the reliability you need. SCS=0.9996 means you're running on fumes. Track SCS trend: if it's moving toward 0.95, a service has quietly degraded its effective availability.

---

## Section C — Applied Problems

### C1: Seven-Service Payment Processing (CD=7)

**Approach**: CD=7 is architecturally aggressive. Before building, compute the per-service SLO requirement and LBH to determine if this design is operationally feasible.

**Step 1 — Required SLO**

```
Required_SLO = SLA^(1/CD)
             = 0.9995^(1/7)
             = 0.9995^0.14286
             = 0.99993
             = 99.993%
```

**Step 2 — LBH**

```
LBH = (2000ms - 150ms) / 7
    = 1850ms / 7
    = 264ms per hop
```

**Step 3 — SCS if all services declare 99.99%**

```
compound = 0.9999^7
         = 0.9993

SCS = 0.9993 / 0.9995
    = 0.9998
```

SCS = 0.9998. In range, but close to the lower boundary.

**Recommendation**: This design is borderline. CD=7 requires 99.993% from every service in the chain — that is four nines plus. If any single service cannot sustain that, the SLA math collapses. The LBH of 264ms means any database query, cache miss, or retry will consume the entire per-hop budget. The SCS of 0.9998 shows there is almost no margin — any service that slips from 99.99% to 99.95% drives SCS below 0.9995, breaching the SLA.

**Architectural verdict**: Do not add service 6 or 7 without explicit SLO negotiation with every team in the chain AND a latency audit showing each service's actual p99 is sustainably below 200ms (leaving 64ms headroom per hop).

**Key Insight**: CD is an architectural multiplier. Every hop multiplies the reliability requirement and compresses the latency budget. CD=7 is not four times harder than CD=4 — it's exponentially different in its operating requirements. Most teams discover this too late, after the services are deployed.

---

### C2: Six-Service Notifications Journey — SCS Audit

**Approach**: When each service has a different declared SLO, compound them individually. Then check SCS.

**Step 1 — Compound availability**

```
Service 1 (Auth):         0.99999
Service 2 (User Prefs):   0.9999
Service 3 (Notification): 0.9999
Service 4 (Payment hist): 0.9995
Service 5 (Loyalty):      0.9990
Service 6 (Comm gateway): 0.9990

Step-by-step:
0.99999 × 0.9999  = 0.99989
0.99989 × 0.9999  = 0.99979
0.99979 × 0.9995  = 0.99929
0.99929 × 0.9990  = 0.99829
0.99829 × 0.9990  = 0.99729

compound ≈ 0.9963 (rounding across steps produces ~0.9963)
```

**Step 2 — SCS**

```
SCS = compound / customer_SLA
    = 0.9963 / 0.9995
    = 0.9968
```

**Answer**: SCS = 0.9968. Below 1.0 but above 0.95. The system is coherent — the customer SLA is achievable — but only if every service performs exactly to its declared SLO simultaneously.

**Key Insight**: SCS=0.9968 looks fine on paper. In practice it means: if any one service performs slightly below its declared SLO on the same day another service does, the customer SLA is breached that month. There is no error margin between what is declared and what is required. This journey should be flagged for SLO renegotiation — specifically, Services 5 and 6 (Loyalty and Comm gateway at 99.90%) are the weakest links.

---

## Section D — Advanced Capstone

### D1: Nine-Service Global Order Routing (CD=9)

**Approach**: CD=9 is beyond the recommended architectural limit for mission-critical journeys. Work through each metric, then synthesize an executive recommendation.

**Part (a) — Compound availability at 99.99% per service**

```
compound = 0.9999^9

Step-by-step:
0.9999^2 = 0.9998
0.9999^4 = 0.9998^2 = 0.9996
0.9999^8 = 0.9996^2 = 0.9992
0.9999^9 = 0.9992 × 0.9999 = 0.9991

Compound availability = 0.9991 = 99.91%
```

At CD=9 with every service at four nines (99.99%), the journey compound availability is only 99.91% — already below the 99.95% SLA.

**Part (b) — Required per-service SLO to meet 99.95% SLA at CD=9**

```
Required_SLO = 0.9995^(1/9)
             = 0.9995^0.1111
             = 0.99994
             = 99.994% per service
```

Every service must operate at 99.994% — between four and five nines — to make this SLA work. Declaring 99.99% (four nines exactly) is insufficient; the compound math requires higher than four nines per service.

**Part (c) — Latency Budget per Hop**

```
LBH = (2000ms - 150ms) / 9
    = 1850ms / 9
    = 205ms per hop
```

205ms per hop is extremely tight. A single PostgreSQL query with index scan averages 50–150ms. A cache miss can spike to 300ms. At LBH=205ms, a single cache miss in any service causes a p99 breach.

**Part (d) — SCS if all services declare 99.99%**

```
compound = 0.9999^9 = 0.9991

SCS = 0.9991 / 0.9995
    = 0.9996
```

SCS = 0.9996. This looks in-range but is misleading: the compound availability (99.91%) is already below the customer SLA (99.95%). The SCS calculation shows the ratio between compound declared SLOs and the SLA — but the declared SLOs (99.99% each) are not achievable at CD=9 because the compound math already shows SLA breach.

**Executive Brief**

```
RECOMMENDATION: Limit Checkout journey to CD ≤ 6.

REASONING:

1. RELIABILITY MATH FAILS AT CD=9
   Required per-service SLO: 99.994% (above four nines).
   Even declaring 99.99% per service yields only 99.91% compound —
   already 0.04 percentage points below the 99.95% SLA.
   This SLA is mathematically unachievable at CD=9 without five-nines
   per-service operation, which no service in this portfolio sustains.

2. LATENCY BUDGET IS NOT OPERATIONAL
   LBH = 205ms per hop.
   A PostgreSQL query: 50–150ms.
   A Redis cache miss: 100–300ms.
   A single cache miss will breach p99 latency SLA on every request
   that hits it. At CD=9, cache misses are not exceptional events —
   they are guaranteed to occur at scale.

3. EVERY SERVICE IS A NEW FAILURE POINT
   Compound availability at 99.99% per service drops to 99.91% at CD=9.
   Adding service 8 or 9 each subtract ~0.01% from compound availability.
   There is no architectural headroom remaining.

RISK PROFILE:
   Architectural decision — high irreversibility once services are deployed
   and teams begin depending on this call chain structure.

NEXT ACTION:
   Define a CD budget policy before services 6 or 7 are added:
   - Checkout: max CD=6 (Required_SLO=99.992%, LBH=308ms — operational)
   - Browse:   max CD=3 (Required_SLO=99.833%, LBH=650ms — generous)
   - Add-to-Cart: max CD=4 (Required_SLO=99.975%, LBH=462ms — achievable)
   
   Enforce CD budget policy at architecture review, not post-deployment.
```

**Key Insight**: The most dangerous architectural anti-pattern in distributed systems is organic hop accumulation — services added one at a time, each seemingly reasonable, until the compound math silently makes the SLA impossible. CD is a budget. Treat it as one.

---

## Quick Reference — Section D Answers

| Metric | Value | Status |
|--------|-------|--------|
| CD | 9 | Over recommended limit |
| Compound at 99.99%/service | 99.91% | Below 99.95% SLA |
| Required SLO for SLA | 99.994% | Not operationally achievable |
| LBH | 205ms/hop | Not operationally safe |
| SCS at 99.99% declared | 0.9996 | In range but misleading |
| Recommended action | CD ≤ 6 | Architectural policy required |
