# Exercise Set 1: Structural Terms — CD, SCS, LBH

**Reference**: `00-shopping-cart-reference-system.md`
**Formulae used in this set**:
- `CD = count(sequential_sync_hops)`
- `Required_SLO = SLA^(1/CD)`
- `SCS = declared_SLO^CD / customer_SLA` [target 0.95–1.10]
- `LBH = (end_to_end_p99 - infra_overhead) / CD`

**Before you begin**: CD is about synchronous dependency. If Service A calls Service B and waits for the response before continuing, that is one synchronous hop. If A publishes to a queue and B consumes it independently, that is NOT a hop — async calls are outside CD.

---

## Section A: Concept Check

Answer these in 2–4 sentences each. They test understanding, not formula recall.

**A1.** Why does CD only count synchronous hops? What happens to async calls in the reliability model?

Think about this: if Service A calls Service B synchronously and B is down, what happens to the A→user transaction? Now contrast: if A publishes to a Kafka topic and B consumes it, what happens to the A→user transaction if B is down?

The answer reveals why async decoupling is a structural reliability tool, not just a performance optimization.

**A2.** What does SCS > 1.10 indicate? Is that a problem, or is the system over-engineered in a good way?

Hint: SCS compares the compound availability of declared SLOs against the customer SLA. If SCS is much greater than 1.0, the declared SLOs significantly exceed what the SLA requires. Think about what that means for error budget allocation and engineering effort.

**A3.** Why does LBH decrease when CD increases, even if the end-to-end p99 SLA stays the same?

LBH = (end_to_end_p99 - infra_overhead) / CD. If the numerator is fixed and CD grows, what happens to each service's latency budget? Now think about what that means for a service that normally has p99=300ms when its LBH drops to 80ms.

---

## Section B: Basic Formula Application

Work through each calculation step by step. Show your CD count before applying any formula.

---

**B1. Order Tracking Baseline**

The Order Tracking journey has SLA=99.5% and CD=2. The call chain is:
`Auth → Order Management`

(a) What per-service SLO does each service in this journey need to meet?
Apply: Required_SLO = SLA^(1/CD) = 0.995^(1/2)

(b) Auth currently declares 99.990% SLO. Order Management declares 99.990%. Calculate SCS.
Apply: SCS = (0.99990 × 0.99990) / 0.995

(c) If end-to-end p99 = 1000ms and infra_overhead = 100ms, what is LBH per service?

(d) Is Auth's MTBI-implied availability (30 days MTBI, 45 min MTTR) compatible with its declared 99.990% SLO? Use: achievable_SLO = MTBI/(MTBI+MTTR). Express MTBI and MTTR in the same unit.

---

**B2. Returns Portal — New Journey Design**

A proposed "Returns Portal" journey would chain the following services in sequence:
`API Gateway → Auth → Order Management → Inventory → Returns Service (new, P1)`

SLA = 99.0%.

(a) Count CD. Remember: count synchronous hops only. The API Gateway is hop 1, Auth is hop 2, etc.

(b) Apply Required_SLO = SLA^(1/CD). What SLO must each of the 5 services maintain?

(c) If end-to-end p99 = 3000ms and infra_overhead = 200ms, what is LBH?

(d) Auth currently achieves 99.990% and Order Management 99.990%. The Returns Service (new) has no history. If all 5 services declare 99.99%, what is SCS?

(e) Is this journey safe to add given the existing system? Consider: Auth is already in 3 other journeys. What happens to Order Tracking and Checkout if the Returns Portal adds load to Auth?

Hint for (e): CD formulas tell you about reliability arithmetic, not capacity. A service can be arithmetically safe but operationally strained.

---

**B3. Checkout SCS Sensitivity**

The Checkout journey has CD=5. Currently all 5 services declare 99.99% SLO. Customer SLA = 99.95%.

(a) Calculate SCS with all 5 services at 99.99%.
SCS = (0.9999^5) / 0.9995

(b) The Payment Service undergoes a reliability renegotiation and drops its declared SLO to 99.95% (due to known PSP dependency issues). Recalculate SCS.
New declared_SLO_compound = 0.9999^4 × 0.9995

(c) Is either SCS value in the target range of 0.95–1.10?

(d) The SRE team wants SCS to be exactly 1.05. Working backwards: if 4 services maintain 99.99%, what does the 5th service need to declare?
Set up: (0.9999^4 × x) / 0.9995 = 1.05. Solve for x.

---

## Section C: Intermediate Scenarios

These require combining multiple formula steps and applying judgment.

---

**C1. Checkout Expansion — Q2 Architecture Decision**

The engineering team has approved adding 2 new services to the Checkout journey over Q2:
- **Promotions Engine** (P1, tw=0.8): inserted at CD position 3, between Cart and Payment, applies coupon and discount logic
- **Compliance Logger** (P2, tw=0.5): inserted at CD position 6, after Order Management, records regulatory data synchronously before the transaction completes

New Checkout chain: `Auth → Cart → Promotions Engine → Payment → Order Management → Compliance Logger → [done]`

New CD = 7. Customer SLA remains 99.95%.

(a) What Required_SLO must each of the 7 services maintain?
Apply: 0.9995^(1/7)

(b) If all 7 services declare 99.99% SLO, what is SCS?

(c) End-to-end p99 budget = 2000ms, infra_overhead = 150ms. What is LBH per service?

(d) Currently, Payment Service p99 = 450ms (it calls an external PSP). With LBH from (c), is Payment compliant? What does non-compliance mean operationally?

(e) Should SRE approve this architecture? Write a 3-sentence recommendation addressing: the Required_SLO each service must hit, the LBH constraint on Payment specifically, and what condition must be met before the Compliance Logger can be added.

**Hint**: SCS in the acceptable range does not mean the architecture is safe. LBH violations are independent failure modes.

---

**C2. Inherited System Audit**

You inherit a legacy checkout journey with CD=6. The declared SLOs for the 6 services are:
- Service A: 99.999%
- Service B: 99.99%
- Service C: 99.99%
- Service D: 99.95%
- Service E: 99.90%
- Service F: 99.90%

Customer SLA = 99.95%.

(a) Calculate the compound declared availability:
0.99999 × 0.9999 × 0.9999 × 0.9995 × 0.9990 × 0.9990 = ?

(b) Calculate SCS = compound / 0.9995.

(c) Is SCS in the acceptable range? What does the value tell you?

(d) Services E and F both have 99.90% SLO. The team argues: "99.90% is still very good." Reframe this using Required_SLO. What SLO does each service actually need to maintain given CD=6 and SLA=99.95%?

(e) If Services E and F cannot improve to Required_SLO, what are the two structural options available to SRE? (Hint: one is architectural, one is contractual.)

---

## Section D: Advanced — Leadership Scenario

**D1. The CTO Presentation**

You are presenting to the CTO. The product team wants to add 4 microservices to the Checkout journey over the next 6 months, taking CD from 5 to 9. Their argument: "Each new service will maintain 99.99% SLO, so reliability won't suffer."

Known baseline:
- Current Checkout CD=5, all services at 99.99%, SLA=99.95%
- Checkout actual measured availability ≈ 99.62% (gap between declared and actual reflects operational reality)
- End-to-end p99 budget = 2000ms, infra_overhead = 200ms

**(a) Compound availability at CD=9 with all services at 99.99%**

Calculate: 0.9999^9

Compare to current: 0.9999^5

What is the delta? Express in minutes of error budget per month (monthly minutes = 43,200).

**(b) Required_SLO to maintain 99.62% actual availability at CD=9**

The team's implicit claim is that current reliability (99.62%) will be preserved. What per-service SLO would each of the 9 services need to achieve 99.62% compound?

Apply: x^9 = 0.9962. Solve for x. (Use x = 0.9962^(1/9))

Is this SLO achievable? What does it imply about the product team's argument?

**(c) LBH at CD=9**

LBH = (2000ms - 200ms) / 9

What is this in milliseconds? Payment Service currently operates at p99=450ms. Is it compliant?

**(d) SCS at CD=9 with all services at 99.99%**

SCS = 0.9999^9 / 0.9995

Is SCS in range? What does it indicate?

**(e) Executive Brief — CTO Recommendation**

Write using Format 1 (Executive Brief) from the framework style guide:

```
## Checkout Architecture: CD Expansion Risk

Recommendation: [one sentence — what you are recommending]

Why:
- [Bullet 1: compound availability math]
- [Bullet 2: LBH violation for Payment]
- [Bullet 3: structural principle — each hop adds blast radius]

Risks:
[Risk table or 2-bullet inline]

Next action: [one specific, concrete step]
```

Your recommendation should not be "never add services." It should be conditional — what conditions would you require before SRE approves a CD=7, CD=8, or CD=9 Checkout journey?

**Hint for the brief**: The product team is not wrong that each service at 99.99% is highly reliable individually. The argument fails at the system level. Your brief should make that distinction clear without being dismissive.

---

*End of Exercise Set 1. Proceed to Exercise Set 2 (Blast Radius Terms) after completing all sections.*
