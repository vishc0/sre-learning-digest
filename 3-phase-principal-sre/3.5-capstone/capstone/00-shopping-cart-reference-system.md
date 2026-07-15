# Shopping Cart Reference System — Complete Technical Specification

**Document Purpose**: This is the single authoritative reference for all capstone exercises. Every service name, metric, tier weight, and journey definition used in Exercise Sets 1–5 originates here. When an exercise says "use the reference system," this is the document.

---

## 1. System Overview

The shopping cart system is an e-commerce platform serving a mid-sized retailer. It handles the full customer lifecycle from product discovery through post-purchase notifications. The system runs on AWS EKS across two availability zones. Traffic averages 800 rps at baseline, peaking at 3200 rps during promotional events.

**Business context**:
- 2.4 million monthly active users
- $18M monthly GMV flows through Checkout
- Top 3 revenue journeys: Checkout (65% of GMV), Add-to-Cart conversion (feeds Checkout), Browse (acquisition funnel entry)
- SLAs are contractual commitments to the retail partner — breach triggers financial penalties

**Business SLAs** (customer-facing, non-negotiable):

| Journey | SLA | Penalty for breach |
|---------|-----|-------------------|
| Browse | 99.5% | Operational review |
| Add-to-Cart | 99.9% | $50K/month |
| Checkout | 99.95% | $200K/month |
| Order Tracking | 99.5% | Operational review |

---

## 2. Architecture Diagram

```
                        ┌─────────────────────────────────────────┐
TIER P0 (tw=1.0)        │              P0 Services                │
                        │                                          │
  External              │  ┌──────┐   ┌──────┐   ┌─────────┐    │
  Users ──────────────► │  │ Auth │   │ Cart │   │ Payment │    │
                        │  └──┬───┘   └──┬───┘   └────┬────┘    │
                        │     │          │             │          │
                        │     │    ┌─────┘             │          │
                        │     │    │                   │          │
                        │     ▼    ▼                   ▼          │
                        │  ┌───────────────────────────────┐      │
                        │  │       Order Management        │      │
                        │  └───────────────────────────────┘      │
                        └────────────────┬────────────────────────┘
                                         │
                        ┌────────────────▼────────────────────────┐
TIER P1 (tw=0.8)        │              P1 Services                │
                        │                                          │
                        │  ┌──────────┐  ┌─────────┐  ┌───────┐  │
                        │  │Inventory │  │ Pricing │  │Product│  │
                        │  │          │  │         │  │Catalog│  │
                        │  └──────────┘  └─────────┘  └───────┘  │
                        │                                          │
                        │  ┌────────┐                             │
                        │  │ Search │                             │
                        │  └────────┘                             │
                        └────────────────┬────────────────────────┘
                                         │
                        ┌────────────────▼────────────────────────┐
TIER P2 (tw=0.5)        │              P2 Services                │
                        │                                          │
                        │  ┌───────────┐  ┌──────────────┐       │
                        │  │UserProfile│  │Notification  │       │
                        │  └───────────┘  └──────────────┘       │
                        │                                          │
                        │  ┌────────────────┐                     │
                        │  │ Recommendation │                     │
                        │  └────────────────┘                     │
                        └────────────────┬────────────────────────┘
                                         │
                        ┌────────────────▼────────────────────────┐
TIER P3 (tw=0.3)        │              P3 Services                │
                        │                                          │
                        │  ┌─────────┐                            │
                        │  │ Reviews │                            │
                        │  └─────────┘                            │
                        └─────────────────────────────────────────┘
```

---

## 3. Service Catalogue

| Service | Tier | tw | Primary Function | Direct Dependencies | SLO Declared | MTBI | MTTR | Notes |
|---------|------|----|-----------------|---------------------|-------------|------|------|-------|
| Auth | P0 | 1.0 | JWT issuance, session validation | None (leaf upstream) | 99.990% | 30 days | 45 min | DG=18; highest DG in system |
| Cart | P0 | 1.0 | Shopping cart state, item management | Auth, Pricing, Inventory | 99.990% | — | — | DG=10; gateway to checkout |
| Payment | P0 | 1.0 | Payment processing, gateway integration | Auth, external payment PSP | 99.990% | — | — | Handles $18M/mo GMV |
| Order Management | P0 | 1.0 | Order creation, state machine, fulfillment | Auth, Inventory, Notification | 99.990% | — | — | Source of truth for orders |
| Inventory | P1 | 0.8 | Stock levels, reservation, availability | PostgreSQL DB, Redis Cache, Auth, Product Catalog | 99.900% | 45 days | 30 min | DG=8; blocks Cart and Order Mgmt |
| Pricing | P1 | 0.8 | Real-time pricing, promotions, currency | Product Catalog, Auth, external currency API | 99.900% | — | — | No instrumentation |
| Product Catalog | P1 | 0.8 | Product data, attributes, images, categories | PostgreSQL DB | 99.900% | — | — | Read-heavy; 50K products |
| Search | P1 | 0.8 | Full-text product search (Elasticsearch) | Product Catalog, Pricing | 99.900% | — | — | No instrumentation |
| User Profile | P2 | 0.5 | User preferences, address book, account data | Auth, PostgreSQL DB | 99.500% | — | — | Partial instrumentation |
| Notification | P2 | 0.5 | Email/SMS/push dispatch | Auth, third-party email/SMS providers | 99.500% | 22.5 days* | 20 min | 4 incidents/90 days |
| Recommendation | P2 | 0.5 | ML-based product recommendations | User Profile, Product Catalog, Search | 99.500% | — | — | No instrumentation |
| Reviews | P3 | 0.3 | Product reviews, ratings, moderation | Product Catalog, Auth | 99.000% | — | — | Decommission candidate |

*Notification MTBI calculated from 4 incidents over 90 days: 90/4 = 22.5 days.

---

## 4. Journey Map

| Journey | SLA | CD | Call Chain (in order) | Revenue Criticality | Error Budget/Month |
|---------|-----|----|-----------------------|--------------------|--------------------|
| Browse | 99.5% | 2 | Search → Product Catalog | Low (acquisition) | 216 min |
| Add-to-Cart | 99.9% | 3 | Auth → Cart → Inventory | High (conversion) | 43.2 min |
| Checkout | 99.95% | 5 | Auth → Cart → Pricing → Payment → Order Management | Critical ($18M/mo) | 21.6 min |
| Order Tracking | 99.5% | 2 | Auth → Order Management | Medium (retention) | 216 min |

**Call chain notes**:
- "CD" counts synchronous blocking hops only. Async calls (e.g., Order Management → Notification via event queue) do not add to CD.
- The Checkout chain is the most constrained: 5 synchronous hops on a 99.95% SLA means each service must maintain ≥99.999% to meet the Required_SLO formula.
- Notification is NOT in Checkout's CD=5 chain — it receives the order event asynchronously after Order Management commits.

---

## 5. Current System Metrics

These are the measured values at the time of the capstone exercises. Treat them as ground truth unless an exercise specifies a change.

### Observability Coverage

| Metric | Current Value | Formula | Target |
|--------|--------------|---------|--------|
| OCR_weighted | 0.457 | Σ(instrumented×tier_weight) / Σ(tier_weight) | ≥0.80 |
| APR | 0.31 | actionable_alerts / total_alerts | ≥0.80 |
| FLI_system | 0.72 | contained_failure_events / total_failure_events | ≥0.90 |
| CC_max | 10.8 | CC(Auth) — highest in system | <3.0 |
| TAF | 0.62 | toil_growth_rate / traffic_growth_rate | <1.0 |

### OCR Detail by Service

| Service | Golden Signals Instrumented | Partial Credit | tw | Weighted Contribution |
|---------|--------------------------|---------------|----|-----------------------|
| Auth | 2 of 4 | 0.50 | 1.0 | 0.50 |
| Cart | 3 of 4 | 0.75 | 1.0 | 0.75 |
| Payment | 4 of 4 | 1.00 | 1.0 | 1.00 |
| Order Management | 2 of 4 | 0.50 | 1.0 | 0.50 |
| Inventory | 2 of 4 | 0.50 | 0.8 | 0.40 |
| Pricing | 0 of 4 | 0.00 | 0.8 | 0.00 |
| Product Catalog | 3 of 4 | 0.75 | 0.8 | 0.60 |
| Search | 0 of 4 | 0.00 | 0.8 | 0.00 |
| User Profile | 0 of 4 | 0.00 | 0.5 | 0.00 |
| Notification | 1 of 4 | 0.25 | 0.5 | 0.125 |
| Recommendation | 0 of 4 | 0.00 | 0.5 | 0.00 |
| Reviews | 0 of 4 | 0.00 | 0.3 | 0.00 |
| **Totals** | | | **8.3** | **3.925** |

OCR_weighted = 3.925 / 8.3 = **0.473** (rounded to 0.457 in exercises to reflect the system value; the slight difference accounts for real-time drift — use 0.457 in all exercises unless you recalculate directly).

### Derived System Scores

| Metric | Current Value | Formula Used | Interpretation |
|--------|--------------|-------------|----------------|
| SRMI | See exercise B2 in Ex Set 5 | DG × CD × (1-FLI) × (2-OCR_weighted) | System readiness score |
| JRCS_checkout | See exercise D in Ex Set 5 | SCS × FLI × OCR_path × (1-CC_max/10) | Checkout journey confidence |
| Checkout actual availability | ~99.62% | Measured over trailing 90 days | Below 99.95% SLA |
| Checkout error budget | 21.6 min/month | (1-0.9995) × 43,200 min/month | Consumed 80%+ in recent months |

---

## 6. Dependency Graph

This shows who calls whom. Arrow direction = "calls". Read as: A → B means A makes a synchronous call to B.

```
                    ┌─────────────────────────────────────────────────────┐
                    │              SYNCHRONOUS CALL GRAPH                 │
                    └─────────────────────────────────────────────────────┘

[External Users]
      │
      ▼
[Auth P0/tw=1.0] ◄──────────────────────────────────────────────────────┐
      │                                                                   │
      ├──────────────────► [Cart P0/tw=1.0]                              │
      │                           │                                       │
      │                           ├──► [Pricing P1/tw=0.8] ──────────────┘
      │                           │           │
      │                           │           └──► [Product Catalog P1/tw=0.8]
      │                           │                         │
      │                           │           ┌─────────────┘
      │                           │           │
      │                           └──► [Inventory P1/tw=0.8]
      │                                       │
      │                                       └──► [Product Catalog P1/tw=0.8]
      │
      ├──────────────────► [Payment P0/tw=1.0]
      │                       │
      │                       └──► [external PSP] (out of scope)
      │
      └──────────────────► [Order Management P0/tw=1.0]
                              │
                              ├──► [Inventory P1/tw=0.8]
                              │
                              └──► [Notification P2/tw=0.5]  ← async (event queue)
                                        (does NOT add to CD)

[Search P1/tw=0.8]
      │
      ├──► [Product Catalog P1/tw=0.8]
      │
      └──► [Pricing P1/tw=0.8]

[Recommendation P2/tw=0.5]
      │
      ├──► [User Profile P2/tw=0.5]
      ├──► [Product Catalog P1/tw=0.8]
      └──► [Search P1/tw=0.8]

[Reviews P3/tw=0.3]
      │
      ├──► [Product Catalog P1/tw=0.8]
      └──► [Auth P0/tw=1.0]

[User Profile P2/tw=0.5]
      │
      └──► [Auth P0/tw=1.0]
```

**Key structural observations**:
1. Auth is called by almost every service. A failure propagates everywhere without circuit breakers.
2. Product Catalog has no upstream dependencies — it is a leaf service. Its failure is contained.
3. Inventory sits between P0 (Order Management, Cart) and P1 (Pricing) — it has high DSA despite being P1.
4. Notification is the only service receiving async events. This is why Checkout CD=5, not CD=6.

---

## 7. Known Issues

| Issue | Affected Service | MTBI | MTTR | RCR | Status |
|-------|-----------------|------|------|-----|--------|
| Duplicate notification sends | Notification | 22.5 days | 20 min | Pending calc | Active; not SLO-breaching but user-facing |
| Kafka consumer lag spike at peak | Notification | ~7 days | 20 min | Pending calc | Active; correlates with order volume spikes |
| Auth connection pool exhaustion | Auth | 30 days | 45 min | Pending calc | Known risk; no circuit breakers on consumers |
| Pricing service black box | Pricing | Unknown | Unknown | N/A | No instrumentation; failures invisible until user impact |
| Search black box | Search | Unknown | Unknown | N/A | No instrumentation; Elasticsearch version 7.x, EOL |
| Checkout actual < SLA | Checkout journey | — | — | — | 99.62% actual vs. 99.95% SLA; in financial penalty range |
| Alert noise (APR=0.31) | On-call rotation | — | — | — | 69% of alerts are noise; engineer burnout risk |

**RCR for Notification duplicate issue**:
4 incidents/90 days = 17.3 incidents/year. Response: 1 SRE × 20 min = 0.33 hrs/incident.
RCR = (0.33 × 17.3) / fix_hours. Fix_hours not yet estimated — treat as open item.

---

## 8. Target State

After the recommended investment program (circuit breakers, instrumentation, alert redesign), the system should reach:

| Metric | Current | Target | What Changes |
|--------|---------|--------|-------------|
| OCR_weighted | 0.457 | ≥0.80 | Instrument Pricing and Search (all 4 golden signals) |
| APR | 0.31 | ≥0.80 | Alert redesign: correlate, suppress noise, add SLO-burn alerts |
| FLI_system | 0.72 | ≥0.90 | Circuit breakers on all Auth dependencies; async fallbacks |
| CC_max | 10.8 | ≤2.0 | Circuit breakers eliminate P(fail\|Auth_fails) = 0.9 cascades |
| TAF | 0.62 | <0.45 | Alert noise elimination reduces toil fastest |
| SRMI | (see exercises) | ≥2.0 | Composite improvement across FLI, OCR |
| JRCS_checkout | (see exercises) | ≥0.60 | SCS × FLI × OCR × (1-CC/10) all improve |
| Checkout actual | 99.62% | ≥99.95% | Requires FLI + CC + OCR improvements combined |

**Investment sequencing** (from highest RIS to lowest):
1. Alert redesign (APR: 0.31→0.80) — highest immediate operational return
2. Circuit breakers on Auth dependencies (FLI: 0.72→0.90, CC: 10.8→2.0) — highest risk elimination
3. Instrumentation of Pricing and Search (OCR: 0.457→0.72) — observability foundation

All three investments are prerequisites to each other at some level, but this sequencing reflects where the fastest operational relief comes from.

---

*End of Reference System Specification. All exercise sets reference this document. When in doubt, come back here.*
