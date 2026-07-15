# Exercise Set 2: Blast Radius Terms — DG, BRI, CC, FLI, DSA

**Reference**: `00-shopping-cart-reference-system.md`
**Formulae used in this set**:
- `DG = Σ[tier_weight × proximity_discount(1.0 direct, 0.5 one-hop, 0.25 two-hop)]`
- `BRI = (affected_users/total) × journey_criticality × tier_weight_of_failing_service`
- `CC = Σ[P(dep_fails|X_fails) × tier_weight(dep)]` — P=0.9 no CB, 0.5 partial CB, 0 full CB
- `FLI = contained_failure_events / total_failure_events` [target >0.90]
- `DSA = Σ[1×tw_direct] + Σ[0.5×tw_transitive]`

**Before you begin**: These terms measure how bad a failure can get, not how likely it is. A service with DG=20 is not necessarily unreliable — it is highly connected. Whether that connection becomes a blast radius depends on circuit breakers (CC), containment (FLI), and operational practices.

---

## Section A: Concept Check

**A1.** A service has DG=5. Another has DG=15. Which is more dangerous to let fail? Does DG predict actual blast radius or just potential risk?

Think about this: DG uses proximity discounts (1.0, 0.5, 0.25). A service with DG=15 might reach many services two hops away, or it might have 15 direct high-tier neighbors. Does it matter which? What is the difference between potential blast radius and realized blast radius?

**A2.** FLI=0.65 is measured for an incident. What happened during this incident? What is the primary action item that should come out of the postmortem?

Work backward from the definition: FLI = contained_failure_events / total. If FLI=0.65, what fraction of failure events cascaded beyond their origin? The postmortem action item should address the mechanism of that cascade, not the root cause of the original failure.

**A3.** Two services have identical CC values. Service A is P0. Service B is P2. Does the CC value mean the same thing for both services? What additional context determines whether a CC value is acceptable?

CC measures cascade potential — it is a function of P(dep_fails) and tier_weight of dependents, not the tier of the service itself. Think: a P2 service with high-tier P0 dependents (everything depends on it) can have a very high CC. What does tier_weight of the failing service's dependents tell you that tier_weight of the failing service itself does not?

---

## Section B: Basic Formula Application

---

**B1. DG for Pricing Service**

Calculate DG for the Pricing Service using the reference system dependency graph.

Pricing's relationships:
- **Direct dependencies** (Pricing calls these): Product Catalog (P1, tw=0.8), Auth (P0, tw=1.0), external currency API (treat as P2, tw=0.5)
- **Direct callers** (these call Pricing): Cart (P0, tw=1.0), Search (P1, tw=0.8)

DG sums up all services in Pricing's immediate blast radius using proximity_discount=1.0 for direct relationships.

Note on DG interpretation: DG captures a service's gravitational pull on the system — the higher-tier the connected services, the higher the DG. Use tw × 1.0 for each direct dependency and each direct caller.

(a) Calculate DG(Pricing).

(b) Compare to Auth's DG=18 from the reference system. Given that Auth is the most connected service, where does Pricing rank by connectivity?

(c) If the currency API (P2) goes down and Pricing has no fallback, which downstream services are directly affected? Use the call graph.

---

**B2. BRI for Notification Incident**

An incident occurs: Notification Service (P2, tw=0.5) begins sending duplicate notifications. Every user who completed a purchase receives 3–5 copies of their order confirmation email. 8% of active users were affected during the 20-minute window.

Journey criticality for Notification = 0.3 (it does not block any journey — it is post-purchase async).

(a) Calculate BRI = (affected_users/total) × journey_criticality × tier_weight_of_failing_service.
Use: affected_users/total = 0.08, journey_criticality = 0.3, tw = 0.5.

(b) Using the BRI scale below, what SEV level does this incident warrant?

| BRI Range | SEV Level | Description |
|-----------|-----------|-------------|
| ≥0.50 | SEV-1 | Critical business impact; incident commander required |
| 0.20–0.49 | SEV-2 | Significant impact; SRE + engineering lead required |
| 0.05–0.19 | SEV-3 | Moderate impact; on-call handles |
| <0.05 | SEV-4 | Low impact; ticket for next business day |

(c) If the same bug caused 40% of users to be affected (a major deployment error), what would BRI be? Would the SEV change?

(d) Why does journey_criticality matter in BRI? The Notification Service failing completely (not just sending duplicates) during Checkout would affect users who just paid. What journey_criticality value should apply to that scenario?

---

**B3. CC for Inventory Service**

Inventory Service (P1, tw=0.8) has the following services that call it:
- Cart (P0, tw=1.0): no circuit breaker on Cart→Inventory. P(Cart_fails | Inventory_fails) = 0.9
- Order Management (P0, tw=1.0): no circuit breaker. P(OM_fails | Inventory_fails) = 0.9
- Pricing (P1, tw=0.8): no circuit breaker. P(Pricing_fails | Inventory_fails) = 0.5

(a) Calculate CC(Inventory) with no circuit breakers.
CC = Σ[P(dep_fails|Inventory_fails) × tier_weight(dep)]
= (0.9 × 1.0) + (0.9 × 1.0) + (0.5 × 0.8)

(b) Circuit breakers are added to Cart→Inventory and Order Management→Inventory (full circuit breaker, P drops to 0). Pricing→Inventory remains unprotected. Calculate the new CC(Inventory).

(c) Compare to CC_max=10.8 for Auth. What does this comparison tell you about relative risk priority?

(d) If Inventory fails with the original CC (no circuit breakers), which service fails first and why does it fail faster than the others?

---

## Section C: Intermediate Scenarios

---

**C1. Cascade Incident Investigation**

An incident unfolds as follows:
1. Search Service begins throwing 503 errors (Elasticsearch OOM)
2. Pricing Service, which calls Search for price optimization, begins timing out and failing (no circuit breaker on Pricing→Search, P=0.9)
3. Cart, which calls Pricing for real-time item pricing, begins showing "Unable to load price" errors (no circuit breaker on Cart→Pricing, P=0.9)

Incident scope:
- 3 services experience failure events during the incident
- Only Search is the original failure; Pricing and Cart are cascades
- 25% of active users were browsing products or mid-add-to-cart when the incident occurred
- Journey criticality for Browse/Add-to-Cart combined = 0.6
- Search is P1 (tw=0.8)

**(a) Calculate FLI_incident**

FLI = contained_failure_events / total_failure_events

Contained events = failures that stayed within their origin service (Search failed and only Search was affected, with no cascades). In this incident, did any failure event stay contained?

If the original failure (Search) cascaded to Pricing and Cart: how many failure events were there total? How many were contained?

**(b) Calculate BRI for Search's original failure**

BRI = (0.25) × 0.6 × 0.8

**(c) Architectural improvements**

Name two architectural changes that would most improve FLI for future incidents of this type. For each change, state:
- What you add or change
- Which specific P(fail) value drops to 0
- Why FLI improves (fewer cascades = more contained events)

One change should address the Pricing→Search relationship. One should address the Cart→Pricing relationship.

**(d) After both changes, if Search fails again with the same root cause, recalculate FLI_incident.**

---

**C2. Should Inventory Be Operated as P0?**

The team is debating whether Inventory Service (P1, tw=0.8) should be elevated to P0 for operational purposes (on-call priority, change freeze periods, incident response SLA). Use DSA to make the case.

DSA = Σ[1 × tw_direct] + Σ[0.5 × tw_transitive]

**Inventory's direct dependencies** (services Inventory calls):
- PostgreSQL DB: treat as P0 equivalent, tw=1.0
- Redis Cache: treat as P0 equivalent, tw=1.0
- Auth (P0, tw=1.0)
- Product Catalog (P1, tw=0.8)

**Inventory's direct dependents** (services that call Inventory):
- Cart (P0, tw=1.0)
- Order Management (P0, tw=1.0)
- Pricing (P1, tw=0.8)

**Transitive dependents** (one hop beyond direct dependents):
- Cart's downstream: Payment (P0, tw=1.0)
- Order Management's downstream: Notification (P2, tw=0.5)
- Pricing has no additional downstream for this exercise

**(a) Calculate DSA(Inventory)_direct**

Include all direct dependencies and all direct dependents. Use tw × 1.0 for each.

DSA_direct = Σ(1 × tw) for all direct relationships

**(b) Calculate DSA(Inventory)_transitive**

Include one-hop transitive services with 0.5 discount:
DSA_transitive = Σ(0.5 × tw_transitive)

Include: Payment (via Cart) and Notification (via Order Management).

**(c) Total DSA(Inventory) = DSA_direct + DSA_transitive**

**(d) For comparison**: DSA(Reviews) would be very low — it has one direct dependent (Product Catalog) and no transitive reach to P0 services.

Calculate DSA(Reviews) using: Reviews calls Product Catalog (tw=0.8) and Auth (tw=1.0). Reviews is called by no services (it's a leaf from the consumer side).

**(e) Based on DSA, write a 2-sentence recommendation** on whether Inventory should be operated with P0 practices, citing the specific DSA values as evidence.

---

## Section D: Advanced — The Circuit Breaker Investment Case

You are presenting to VP Engineering. You need to justify 40 engineering hours of investment in circuit breakers. The argument must be quantitative.

**Setup**:
- Auth CC_max = 10.8 (current, no circuit breakers on any consumer)
- Auth callers without circuit breakers: Cart (P0, tw=1.0, P=0.9), Payment (P0, tw=1.0, P=0.9), Order Management (P0, tw=1.0, P=0.9)
- FLI_system = 0.72
- The incident you are modeling: Auth connection pool exhaustion causing cascades to Cart, Payment, and Order Management

**(a) FLI_incident without circuit breakers**

In this Auth failure scenario:
- Auth fails (1 original failure event)
- Cart, Payment, Order Management all fail (3 cascade events) — P=0.9 each, treat as certain for incident modeling

Total failure events = 4 (Auth + 3 cascades)
Contained events = ? (how many stayed within their origin?)

Calculate FLI_incident.

**(b) BRI for this incident**

55% of active users were in checkout or cart flows during the incident.
Journey criticality = 1.0 (this is the checkout path — highest criticality).
Auth is P0, tw=1.0.

Calculate BRI.

At this BRI, what SEV level? What is the operational consequence of a SEV-1 at 2 AM?

**(c) CC(Auth) after circuit breakers**

Full circuit breakers are implemented on:
- Cart→Auth: P drops from 0.9 to 0
- Payment→Auth: P drops from 0.9 to 0
- Order Management→Auth: P drops from 0.9 to 0

Recalculate CC(Auth). What services (if any) remain without circuit breakers?

**(d) FLI_incident after circuit breakers**

With the same Auth failure:
- Auth fails (1 failure event)
- Cart, Payment, Order Management: circuit breakers open, services degrade gracefully (continue operating with cached/fallback responses). These do NOT count as failure events.

Calculate FLI_incident after circuit breakers.

**(e) JRCS improvement**

JRCS = SCS × FLI × OCR_path × (1-CC_max/10)

Calculate JRCS in two scenarios:
- **Before**: SCS=1.0, FLI=0.72, OCR_path=0.70 (Auth + Cart + Payment + OM partially instrumented), CC_max=10.8
- **After**: SCS=1.0, FLI=0.90 (improved from circuit breakers), OCR_path=0.70, CC_max=1.5 (residual CC from remaining callers)

What is the percentage improvement in JRCS?

**Hint for JRCS**: The (1-CC_max/10) term penalizes systems where a single failure can cascade massively. At CC_max=10.8, this term is (1-1.08) = negative — which is unphysical and means the system is at maximum cascade risk. Cap CC_max at 10.0 for the formula: (1-10/10) = 0. After improvement to CC_max=1.5: (1-0.15) = 0.85.

**(f) Investment Brief**

Write 4 lines:
1. What you are proposing (specific technical change)
2. What it costs (40 engineering hours, estimated 2-sprint delivery)
3. What it prevents (use BRI and FLI numbers from above)
4. ROI statement: compare engineering hours invested to expected incident response hours saved per year

For the ROI: Auth fails ~12× per year (MTBI=30 days). Each incident without circuit breakers: 2 SREs × 3 hours = 6 SRE-hours. With circuit breakers, Auth failures are degraded, not down: incident response drops to 1 SRE × 30 min = 0.5 SRE-hours.
Annual savings = 12 × (6 - 0.5) = 66 SRE-hours saved vs. 40 hours invested.

---

*End of Exercise Set 2. Proceed to Exercise Set 3 (Health Signals and Efficiency) after completing all sections.*
