# Exercise Set 3: Health Signals and Efficiency — EBV, APR, MTBI, OCR, OL, RCR, TAF

**Reference**: `00-shopping-cart-reference-system.md`
**Formulae used in this set**:
- `EBV = traffic_normalized_error_rate / baseline_rate`; `Time_to_breach = remaining_budget / (EBV × baseline_rate)`
- `APR = actionable_alerts / total_alerts` [target >0.80]
- `MTBI = period / incident_count`; `achievable_SLO = MTBI/(MTBI+MTTR)`
- `OCR_weighted = Σ(instrumented×tier_weight) / Σ(tier_weight)`
- `OL = Δ(budget_pp_per_week) / SRE_hours`
- `RCR = (response_hrs × freq_per_year) / fix_hours` [fix if >0.50, defer if <0.50]
- `TAF = toil_growth_rate / traffic_growth_rate` [target <1.0]

**Before you begin**: These terms deal with signals and efficiency — how well the system communicates its state, and how efficiently the SRE team uses its time. High OCR means you can see failure. High APR means you can act on what you see. Low TAF means toil is not growing faster than the business. These three together determine whether SRE capacity scales with the platform or gets consumed by it.

---

## Section A: Concept Check

**A1.** EBV = 0.6 for the current period. What does this mean? Is it good or bad? What might explain it?

EBV = traffic_normalized_error_rate / baseline_rate. If EBV = 0.6, the current error rate is 60% of baseline. Think about what that means: is the system burning error budget faster than usual, slower than usual, or at the usual rate? What operational conditions could cause EBV < 1.0?

Consider: traffic drops during off-peak hours reduce absolute error count. A recent deployment fixed a latent bug. Traffic shifted from the error-prone checkout path to browse-heavy patterns.

**A2.** APR = 0.31. The on-call engineer handles 20 alerts per shift. How many are noise? What is the human cost over a week of on-call?

Calculate: if 31% of alerts are actionable, how many of the 20 are genuine? How many are noise?

Assume: 3 shifts per week, 20 alerts per shift, 45 minutes per alert triage (investigating, correlating, determining it's noise, documenting).

Calculate total engineer hours per week spent on noise. Now consider: what else could that time be spent on? (Postmortems, reliability investments, capacity planning — things that prevent future alerts.)

**A3.** MTBI = 60 days, MTTR = 2 hours for a service declaring 99.99% SLO. Calculate the MTBI-implied availability. What is the gap between declared and achievable?

Use: achievable_SLO = MTBI / (MTBI + MTTR). Express both in the same unit (minutes). MTBI = 60 days = 86,400 minutes. MTTR = 120 minutes.

The gap between declared SLO and achievable SLO is called the **SLO credibility gap**. It means the service's declared SLO is mathematically impossible given its actual failure frequency. What are the operational consequences of an SLO credibility gap? (Think: on-call targets, error budget policies, customer contracts.)

---

## Section B: Basic Formula Application

---

**B1. Error Budget Velocity — Checkout**

Given:
- Checkout error budget = 21.6 minutes/month
- At day 20 of a 30-day month, 18 minutes have been consumed
- Current error rate is 4× the traffic-normalized baseline (EBV = 4.0)
- Baseline error rate = 0.01% (1 error per 10,000 requests)

**(a) EBV**

EBV = current_traffic_normalized_error_rate / baseline_rate = 4.0 (given directly)

What does EBV=4.0 mean in operational terms? Is this a steady burn or a spike?

**(b) Remaining budget**

Budget consumed: 18 min. Total budget: 21.6 min. Remaining: ?

**(c) Time to breach**

Time_to_breach = remaining_budget / (EBV × baseline_rate)

The units here require care. Baseline_rate is in errors/request. EBV is dimensionless. The burn rate in budget-minutes-per-day must be derived from:

If baseline burn = (1 - SLA) × minutes_per_day = 0.0005 × 1440 = 0.72 min/day, then:
Current burn = EBV × baseline_burn = 4.0 × 0.72 = 2.88 min/day.

Time_to_breach = remaining_budget / current_burn = 3.6 min / 2.88 min/day = ?

Express your answer in hours. Is this enough time to respond?

**(d) At what point should the on-call have escalated?** What EBV threshold, if sustained for 24 hours, would consume the entire remaining 3.6 minutes in that window?

---

**B2. APR Improvement Calculation**

The on-call system fires 150 alerts in a week. Post-incident analysis determines that 47 of those alerts required direct action (page acknowledgment, investigation, and either a fix or a documented "not actionable" outcome).

**(a) Calculate APR** = 47 / 150

**(b) Target gap**: How many additional actionable alerts need to be correctly identified (without changing total alert volume) to reach APR=0.80?

Set up: (47 + x) / 150 = 0.80. Solve for x.

Note: x represents alerts that were previously classified as noise but are actually actionable — they represent real signal being missed, not just noise reduction.

**(c) Alternatively**: To reach APR=0.80 by reducing noise (keeping actionable constant at 47), how many total alerts would be allowable?

Set up: 47 / y = 0.80. Solve for y.

**(d) Which approach is safer?** Discuss: reducing total alert volume (suppression) vs. improving classification of existing alerts (tuning). Which risks missing real signals? Which is operationally faster to implement?

---

**B3. Auth MTBI-Implied Availability and SLO Gap**

Auth Service: MTBI = 30 days, MTTR = 45 minutes.

**(a) Convert to same unit and calculate achievable_SLO**

MTBI = 30 × 24 × 60 = 43,200 minutes
MTTR = 45 minutes

achievable_SLO = MTBI / (MTBI + MTTR)

**(b) SLO credibility gap**

Auth declares 99.990% SLO. What is the gap between declared and achievable?

Express the gap in:
- Percentage points
- Error budget minutes per month (monthly budget = 43,200 × (1 - declared_SLO))

**(c) Annual impact on Checkout**

Checkout error budget = 21.6 min/month = 259.2 min/year.

Auth MTTR = 45 min per incident. Auth incidents per year = 365 / 30 ≈ 12.

Each Auth incident that affects Checkout (assume all do): 45 min of Checkout downtime.

Total Auth-driven Checkout downtime per year = 12 × 45 = 540 minutes.

Checkout annual budget = 259.2 minutes.

What does this mean? Is the Checkout SLA mathematically achievable given Auth's current MTBI/MTTR?

**(d) What must change?** Given the current MTBI=30 days, what MTTR would Auth need to achieve to make declared 99.990% achievable?

Rearrange: achievable_SLO = MTBI / (MTBI + MTTR) = 0.99990
Solve: MTTR_required = MTBI × (1/0.99990 - 1) = 43200 × 0.0001 ≈ 4.32 minutes

Is a 4-minute MTTR realistic for Auth? What infrastructure changes would make it achievable?

---

**B4. OCR_weighted Calculation**

Calculate OCR_weighted from the current instrumentation state. Use partial credit for services that have some but not all signals instrumented.

Partial credit rule: if a service has k of 4 golden signals, its contribution = k/4.

| Service | Signals (of 4) | Partial Credit | tw | Weighted Contribution |
|---------|---------------|---------------|----|-----------------------|
| Auth | 2 | 0.50 | 1.0 | ? |
| Cart | 3 | 0.75 | 1.0 | ? |
| Payment | 4 | 1.00 | 1.0 | ? |
| Order Mgmt | 2 | 0.50 | 1.0 | ? |
| Inventory | 2 | 0.50 | 0.8 | ? |
| Pricing | 0 | 0.00 | 0.8 | ? |
| Product Catalog | 3 | 0.75 | 0.8 | ? |
| Search | 0 | 0.00 | 0.8 | ? |
| User Profile | 0 | 0.00 | 0.5 | ? |
| Notification | 1 | 0.25 | 0.5 | ? |
| Recommendation | 0 | 0.00 | 0.5 | ? |
| Reviews | 0 | 0.00 | 0.3 | ? |

**(a)** Fill in the weighted contribution column for each service (Partial Credit × tw).

**(b)** Sum all weighted contributions (numerator).

**(c)** Sum all tier_weights (denominator): Σ(tw) = 4×1.0 + 4×0.8 + 3×0.5 + 1×0.3 = ?

**(d)** Calculate OCR_weighted = numerator / denominator.

**(e)** If Pricing and Search are fully instrumented (0→4 signals each), recalculate OCR_weighted. How much does it improve?

**(f)** Why is OCR_weighted more useful than a simple count of instrumented services? What does the tier_weight do to the formula's incentive structure?

---

## Section C: Intermediate Scenarios

---

**C1. RCR Prioritization — Three Backlog Items**

The SRE team has three items competing for sprint capacity. Use RCR to prioritize them.

RCR = (response_hours × frequency_per_year) / fix_hours

Decision rule: RCR > 0.50 → fix it. RCR < 0.50 → defer. Higher RCR = higher priority.

**Item A: Kafka consumer lag in Notification Service**
- Frequency: weekly incident (52/year)
- Response: 1 SRE × 45 min = 0.75 hrs per incident
- Estimated fix: 40 hours (rewrite consumer group partition assignment logic)

**Item B: Auth slow queries at peak traffic**
- Frequency: monthly incident (12/year)
- Response: 2 SREs × 90 min each = 3 hrs per incident
- Estimated fix: 160 hours (index redesign + query optimization + load testing)

**Item C: Payment gateway retry storms**
- Frequency: bi-weekly (26/year)
- Response: 1 SRE × 30 min = 0.5 hrs per incident
- Estimated fix: 24 hours (implement exponential backoff with jitter)

**(a)** Calculate RCR for each item. Show formula.

**(b)** Rank by RCR, highest to lowest.

**(c)** Given 40 engineering hours available this sprint, which items can be fully addressed? Which items should not be started (starting a 160-hour fix in a 40-hour sprint without a plan is worse than deferring it).

**(d)** Item B has the highest operational severity (Auth slow queries affect Checkout). But RCR says defer. Does that mean it should never be fixed? What additional factor would you consider alongside RCR for an item affecting a P0 service?

Hint: RCR is a triage tool, not a veto. Business criticality and SLO exposure are inputs that RCR does not capture.

---

**C2. TAF — Which Toil Category is Driving Growth?**

Over the past 3 months, traffic grew 15%. Toil breakdown and growth rates:

| Toil Category | % of Total Toil | Growth Rate (3 months) |
|--------------|----------------|------------------------|
| Alert noise | 45% | 22% |
| Manual deployments | 30% | 8% |
| Support escalations | 25% | 10% |

**(a) Calculate overall TAF**

Overall toil growth rate = weighted average of category growth rates:
= (0.45 × 22%) + (0.30 × 8%) + (0.25 × 10%)

TAF = overall_toil_growth_rate / traffic_growth_rate = ? / 15%

**(b) Per-category TAF**

Calculate TAF for each category individually:
- Alert noise TAF = 22% / 15%
- Manual deployments TAF = 8% / 15%
- Support escalations TAF = 10% / 15%

Which category is above TAF=1.0? What does it mean that alert noise grows faster than traffic?

**(c) Impact of APR improvement**

If APR improves from 0.31 to 0.80 (alert redesign investment), alert noise toil drops from 45% of total to approximately 10% (noise alerts don't generate toil if they auto-resolve).

Recalculate overall TAF assuming alert noise growth drops to 0% (it cannot grow because it's already suppressed).

New overall toil growth = (0.10 × 0%) + (0.30 × 8%) + (0.25 × 10%) + (remaining 35% of toil with 0% growth) = ?

New TAF = new_growth / 15%

**(d)** What TAF value does the reference system currently show (0.62)? Is overall TAF < 1.0? Does that mean everything is fine? Use the per-category analysis to explain why TAF=0.62 still represents a problem for on-call engineers.

---

## Section D: Advanced — The Q2 Investment Portfolio

You are the Principal SRE preparing the Q2 investment recommendation. You have three candidate investments, each requiring 80 engineering hours. You must rank them and justify the order.

**Background metrics** (current state):
- OCR_weighted = 0.457
- APR = 0.31
- FLI = 0.72
- CC_max = 10.8
- TAF = 0.62
- MRI = 1.0 for operational changes (no service code changes)
- Checkout error budget = 21.6 min/month; quarterly budget = 64.8 min

---

**Investment A: OCR Improvement**
Instrument Pricing and Search with all 4 golden signals.
- Expected OCR improvement: 0.457 → 0.72
- Expected benefit: reduces MTTR by 15 min per incident (engineers can see failure earlier)
- Incidents expected next quarter: 3
- Total time saved: 3 × 15 min = 45 min/quarter
- As fraction of quarterly budget: 45/64.8 = 69.4% of quarterly budget saved

OL calculation:
- Δ(budget_pp_per_week) = (45 min / 13 weeks) / 21.6 min_per_month
  - 45 min saved over quarter = 3.46 min/month saved
  - As percentage points of budget: 3.46/21.6 = 0.16 pp/month — convert to weekly: 0.16/4.33 = 0.037 pp/week
- OL = Δ(budget_pp_per_week) / SRE_hours = 0.037 / 80 = **0.00046**

Note: OL is very small for Investment A because the error budget savings are modest — OCR helps you detect failure faster, but if FLI is low, failures cascade anyway.

---

**Investment B: APR Redesign**
Reduce alert noise; APR improves from 0.31 → 0.80.
- Expected TAF reduction: 0.62 → 0.40
- Expected MTTR reduction: 3 min/incident × 6 incidents/quarter = 18 min saved/quarter
- As fraction of quarterly budget: 18/64.8 = 27.8%

OL calculation:
- Δ(budget_pp_per_week): 18 min/quarter = 1.38 min/month = 0.064 pp/month = 0.015 pp/week
- OL = 0.015 / 80 = **0.000188**

RCR_B: Alert noise generates SRE labor. Estimate:
- 3 shifts/week × 20 alerts/shift × 69% noise × 45 min/alert = 62 SRE-hours/week × 52 weeks = 3,224 SRE-hours/year
- In practice, not every noise alert takes 45 min — use 15 min average for classification: 3 shifts/week × 20 × 0.69 × 15 min = 621 hrs/year
- RCR_B = 621 / 80 = **7.76**

---

**Investment C: Circuit Breakers on Auth Dependencies**
Full circuit breakers on Cart→Auth, Payment→Auth, Order Management→Auth.
- Expected FLI improvement: 0.72 → 0.90
- Expected CC_max reduction: 10.8 → 2.0
- Cascade incidents: 2/quarter = 8/year; each cascade: 2 SREs × 2 hrs = 4 SRE-hrs/incident
- 80% of cascade incidents eliminated: 8 × 0.80 = 6.4 incidents/year avoided × 4 hrs = 25.6 SRE-hrs/year
- Error budget impact: each cascade incident consumes ~8 min of Checkout budget
  - 8 × 0.80 × 8 min = 51.2 min/year eliminated = 4.27 min/month = 0.197 pp/month = 0.046 pp/week
- OL = 0.046 / 80 = **0.000575**

RCR_C:
- 8 cascade incidents/year × 4 SRE-hrs/incident = 32 SRE-hrs/year
- RCR_C = 32 / 80 = **0.40**

---

**(a) OL summary**

Fill in the OL for each investment. Which investment has the highest OL (budget efficiency per engineering hour)?

**(b) RCR summary**

Fill in RCR for each. Investment A was given: RCR_A = 12 hrs saved/year × 1 hr/incident / 80 = 0.15. Investment B = 7.76. Investment C = 0.40.

Which investments exceed the RCR > 0.50 threshold?

**(c) Calculate RIS for each investment**

RIS = (RCR × OL) / MRI. Use MRI = 1.0 for all.

Show all three RIS calculations.

**(d) Rank by RIS**

Which investment has the highest RIS? Does this ranking match your intuition? Why or why not?

Consider: a high RCR investment (Investment B — alert noise generates massive recurring labor) combined with a meaningful OL creates high RIS. Investment C (circuit breakers) has a strong OL but lower RCR. Investment A (instrumentation) has the lowest OL — visibility improvements pay off slowly unless failures are frequent.

**(e) Portfolio recommendation table**

| Investment | What It Does | RCR | OL | RIS | Priority | One-Line Rationale |
|-----------|-------------|-----|----|-----|----------|-------------------|
| A: OCR | Instrument Pricing + Search | 0.15 | 0.00046 | ? | ? | |
| B: APR | Alert redesign | 7.76 | 0.000188 | ? | ? | |
| C: CB | Circuit breakers on Auth | 0.40 | 0.000575 | ? | ? | |

Complete the table. Write one-line rationale for each priority ranking.

**(f) Strategic consideration**

RIS ranks investments by operational return-on-investment. But Investment C (circuit breakers) is a prerequisite for Investment A to have full effect — you cannot see the blast radius clearly with OCR improvements if the blast radius is still uncontrolled. Does this change your sequencing recommendation?

Write 2 sentences on how you would sequence the investments given both the RIS ranking and strategic dependencies.

---

*End of Exercise Set 3. Proceed to Exercise Set 4 (Change Governance) after completing all sections.*
