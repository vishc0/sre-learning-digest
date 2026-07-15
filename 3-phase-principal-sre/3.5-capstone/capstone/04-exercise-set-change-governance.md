# Exercise Set 4: Change Governance — SCV, MRI, CSD, RV, EBR, DSS

**Reference**: `00-shopping-cart-reference-system.md`
**Formulae used in this set**:
- `SCV = deploy_freq_per_week × mean_CSAI × failure_rate`
- `MRI = DG × CD × (1-FLI) × (2-OCR_weighted)`
- `CSD = Σ[tier_weight × depth_coeff(config=0.2, code=0.5, schema=1.5, API=2.0, coordinated=2.5)]`
- `RV = rollback time`; `window ≥ 3×RV`
- `EBR = min(MRI×0.05, 0.80)` — fraction of monthly budget that must be in reserve
- `DSS = (1-SCV_norm)×(1-MRI/10)×APR×budget_remaining_fraction`

**Before you begin**: Change governance terms exist because deployments are the leading cause of production incidents. The formulae in this set answer the question: "Given everything we know about this service and this change, how risky is deploying right now?" MRI is the master risk index — it synthesizes structural risk (DG, CD), containment risk (FLI), and observability risk (OCR). EBR protects the error budget before a change even starts. DSS tells you whether the monitoring posture is adequate to catch problems quickly.

---

## Section A: Concept Check

**A1.** MRI = 38.9 for the Auth Aurora database migration. The change is blocked. What are the 4 inputs to MRI, and which two are most responsible for the high score?

MRI = DG × CD × (1-FLI) × (2-OCR_weighted)

Given: Auth DG=18, Auth is on Checkout CD=5, FLI=0.72, OCR=0.457.

Calculate each factor's contribution. Which two have the most multiplicative effect? Now consider: if you could change only one input to get MRI below 10.0, which one would you change and by how much?

**A2.** EBR = 25% means the change requires 25% of the monthly error budget in reserve before it can proceed. Why does a *successful* change need budget in reserve? The change works perfectly — why does it consume budget just by existing?

Think about this: EBR reserves are not for the happy path. They are for the scenarios where the change partially fails, requires rollback, or reveals an unexpected dependency issue after deployment. What is the probability distribution of "change succeeds perfectly on first try" vs. "change succeeds but requires 1-2 rollback attempts"? The budget reserve is the SRE team's operational margin.

**A3.** The CAB asks for RV (rollback value — the measured rollback time). The engineer says "about 15 minutes." Is this acceptable? What should the engineer bring to the CAB?

RV is a measured value, not an estimate. "About 15 minutes" suggests it has never been timed. What is the risk of relying on an untimed rollback in a production incident at 2 AM? What documentation should the engineer bring instead?

Hint: The CAB needs to calculate window ≥ 3×RV. If RV is untested, the window calculation is meaningless — and the rollback plan is theater.

---

## Section B: Basic Formula Application

---

**B1. SCV — Cart Service**

Cart Service deployment history over the past week:
- 5 deployments total: 3 code updates (CSAI=0.5 each) and 2 config changes (CSAI=0.2 each)
- 1 rollback in the last 10 deployments (failure_rate = 1/10 = 0.10)

mean_CSAI = (3×0.5 + 2×0.2) / 5

SCV = deploy_freq_per_week × mean_CSAI × failure_rate

**(a)** Calculate mean_CSAI.

**(b)** Calculate SCV(Cart).

**(c)** Interpret the result. Using the SCV risk scale:

| SCV Range | Risk Level | Monitoring Requirement |
|-----------|-----------|------------------------|
| 0.00–0.10 | Low | Standard post-deploy monitoring 1 hr |
| 0.10–0.25 | Medium | Enhanced monitoring 2 hrs, on-call alert |
| 0.25–0.50 | High | 4-hr monitoring window, SRE approval required |
| >0.50 | Very High | CAB review, change freeze candidate |

Where does Cart fall? What monitoring is required?

---

**B2. MRI — Inventory Schema Change**

A schema change is planned for the Inventory Service.

Given:
- DG(Inventory) = 8
- CD = 5 (Checkout journey, the most critical path Inventory is on)
- FLI = 0.72 (system-wide)
- OCR_weighted = 0.457 (system-wide)

**(a)** Calculate MRI = DG × CD × (1-FLI) × (2-OCR_weighted).

Work through each factor:
- DG: 8
- CD: 5
- (1-FLI): 1 - 0.72 = 0.28
- (2-OCR): 2 - 0.457 = 1.543

**(b)** Using the MRI approval tier table:

| MRI Range | Approval Tier | Requirements |
|-----------|--------------|-------------|
| 0–5 | Standard | Team lead sign-off |
| 5–15 | Enhanced | SRE approval + monitoring plan |
| 15–30 | Elevated | CAB review + rollback test |
| >30 | Critical | Executive sponsor + phased deployment |

What approval tier does this require?

**(c)** If FLI improves to 0.90 and OCR to 0.72 (after investments), recalculate MRI. Does the approval tier change?

---

**B3. CSD — Payment Service Update**

A Payment Service change involves three coordinated components:

| Component | Service | tw | Change Type | depth_coeff |
|-----------|---------|-----|------------|-------------|
| Payment code update | Payment | 1.0 | code | 0.5 |
| Payment schema change | Payment | 1.0 | schema | 1.5 |
| Order Management consumer update | Order Mgmt | 1.0 | code | 0.5 |

CSD = Σ[tier_weight × depth_coeff]

**(a)** Calculate CSD.

**(b)** Using the CSD deployment strategy table:

| CSD Range | Deployment Strategy |
|-----------|---------------------|
| 0–1.0 | Standard deploy (canary or blue-green) |
| 1.0–3.0 | Staged rollout with monitoring at each stage |
| 3.0–5.0 | Phased deploy: schema first (separate CR), then code |
| >5.0 | Architectural review required; split into separate CRs |

What deployment strategy does this require?

**(c)** Why must the schema change be deployed separately from the code changes? What failure mode occurs if schema and code are deployed simultaneously?

Hint: Think about what happens during the rollout window. If the new schema is deployed but the new code has not yet reached all pods, or if a rollback is needed — what state is the database in?

---

**B4. DSS — Cart Code Update**

Calculate DSS for a planned Cart code update under improved (target-state) conditions.

Given:
- SCV_cart = 0.10 (low change velocity)
- SCV_norm = SCV / SCV_max where SCV_max = 1.0 → SCV_norm = 0.10
- MRI = 3.45 (after OCR and FLI improvements)
- APR = 0.75 (after alert redesign, not yet at target 0.80)
- budget_remaining_fraction = 0.70 (70% of error budget remains this month)

DSS = (1-SCV_norm) × (1-MRI/10) × APR × budget_remaining_fraction

**(a)** Calculate DSS.

Work through each factor:
- (1 - SCV_norm) = 1 - 0.10 = 0.90
- (1 - MRI/10) = 1 - 3.45/10 = 0.655
- APR = 0.75
- budget_remaining = 0.70

**(b)** Using the DSS interpretation scale:

| DSS Range | Deployment Safety | Monitoring Requirement |
|-----------|------------------|------------------------|
| ≥0.50 | Safe to deploy | Standard 1-hr post-deploy |
| 0.30–0.49 | Conditional | Enhanced monitoring, pre-approved rollback |
| 0.10–0.29 | Risky | SRE on standby, 4-hr window |
| <0.10 | Do not deploy | Defer to next window |

What does this DSS indicate?

**(c)** Now calculate DSS under current (baseline) conditions: SCV_norm=0.10, MRI=17.34 (current, before improvements), APR=0.31, budget_remaining=0.70.

Compare the two DSS values. What does this tell you about the importance of making the investments before deploying significant changes?

---

## Section C: Intermediate Scenarios

---

**C1. Three Change Requests — Budget Gate Analysis**

It is the last week of the month. Error budget remaining = 28% (the month has been rough — 72% consumed by day 22).

Three CRs are in queue. Evaluate each for approval.

**CR-A: Auth Config Change**
- Auth DG=18, CD=5 (Checkout), FLI=0.72, OCR=0.457
- Change type: config change (depth=0.2)
- This is a single-service change

Step 1: Calculate MRI(Auth_config_change) = 18 × 5 × (1-0.72) × (2-0.457)

Step 2: Calculate EBR = min(MRI × 0.05, 0.80)

Step 3: Compare EBR to budget_remaining = 0.28. Can this CR proceed?

Step 4: What approval tier does MRI indicate?

---

**CR-B: Notification Service Code Update**
- Notification DG=3 (estimated — it has few callers; it is async and downstream)
- CD=1 (Notification is not on any synchronous journey — it's post-purchase async)
- FLI=0.72, OCR=0.457
- Change type: code update (depth=0.5)

Step 1: Calculate MRI(Notification_code) = 3 × 1 × (1-0.72) × (2-0.457)

Step 2: Calculate EBR = min(MRI × 0.05, 0.80)

Step 3: Compare EBR to budget_remaining = 0.28. Can this CR proceed?

Step 4: Note that CD=1 here because Notification is not synchronously in any customer journey. What does that tell you about the system design benefit of making Notification async?

---

**CR-C: Product Catalog Schema Change**
- Product Catalog DG=6 (it has several services calling it: Search, Recommendation, Reviews; and it depends on PostgreSQL)
- CD=3 (Browse journey: Search → Product Catalog → PostgreSQL, treating the browse path; or more precisely Search is on the Browse journey, and it calls Product Catalog)
- FLI=0.72, OCR=0.457
- Change type: schema (depth=1.5)

Step 1: Calculate MRI(ProductCatalog_schema) = 6 × 3 × (1-0.72) × (2-0.457)

Step 2: Calculate EBR = min(MRI × 0.05, 0.80)

Step 3: Compare EBR to budget_remaining = 0.28. Can this CR proceed?

---

**Sequencing Decision**

Given budget = 28% and the three EBR values calculated above:
- Which CRs can proceed, and in what order?
- Which CR should be deferred to next month?
- If the team argues "CR-A is just a config change, it's low risk," how do you respond using only the numbers?

---

**C2. Payment API Version Upgrade — Deployment Window Planning**

The team wants to deploy a new Payment API version that changes the transaction response format. Existing consumers (Order Management and Notification) must both be updated before or immediately after Payment.

**Rollback timing from staging tests**:
- Payment API rollback: 22 minutes (measured 3 times, consistent)
- Order Management consumer rollback: 18 minutes (if Payment rolled back, OM must be rolled back too)
- Total synchronized rollback: 22 min (they run in parallel)

RV = 22 minutes (the governing constraint — slowest single-service rollback)

**Window calculation**:
Required window ≥ 3 × RV = 3 × 22 = 66 minutes

**(a)** The team requests a 45-minute window. Is this sufficient? Why or why not?

**(b)** The team requests a 90-minute window instead. What is the maximum allowable RV for a 90-minute window?

Rearrange: window ≥ 3 × RV → RV ≤ window/3 → RV ≤ 90/3 = ? minutes

**(c)** What does the 3×RV rule protect against? Walk through the failure scenario: deploy happens at minute 0, problem is detected at minute X, rollback is initiated, rollback completes at minute Y. What happens if Y > window?

**(d)** The SCW (Safe Change Window) also needs to be calculated. Given:
- Payment deploy: 8 min
- Order Mgmt consumer upgrade: 15 min (can run in parallel after Payment is live)
- Notification consumer upgrade: 10 min (can run in parallel after Payment is live)
- No data migration

SCW = maximum of the parallel paths = max(Payment alone + parallel upgrades, ...)
= 8 min (Payment) + max(15, 10) min (parallel consumer upgrades) = 8 + 15 = 23 min

Is 23 minutes a realistic estimate? What risks are not captured in the SCW calculation?

---

## Section D: Advanced — Full CAB Simulation

You are the SRE chair of the Change Advisory Board (CAB). The following CR is under review.

**CR-2024-Q4-089: Search Service Elasticsearch 7.x → 8.x Upgrade**

Background: Elasticsearch 7.x reached EOL. The upgrade to 8.x involves significant breaking changes to the query API. Both Pricing and Product Catalog consume the Search query API and require consumer updates.

**Input data**:

| Parameter | Value |
|-----------|-------|
| Search DG | 7 (estimated from dependency count) |
| Journeys affected | Browse (CD=2), Add-to-Cart (CD=3) |
| Use CD | 3 (most critical affected journey) |
| FLI (system) | 0.72 |
| OCR_weighted | 0.457 |
| Search SCV | 3 deploys/week, mean_CSAI=1.2, failure_rate=0.20 |
| Change footprint | See CSD table below |
| Rollback time (staging) | 35 minutes (ES index rollback + service restart) |
| Window requested | 90 minutes |
| Browse error budget | 216 min/month |
| Budget consumed | 60% (day 20 of 30) |
| Budget remaining | 40% = 86.4 min |

**CSD Input Table**:

| Component | Service | tw | Change Type | depth_coeff |
|-----------|---------|-----|------------|-------------|
| ES schema change | Search | 0.8 | schema | 1.5 |
| Search API contract change | Search | 0.8 | API | 2.0 |
| Pricing consumer update | Pricing | 0.8 | code | 0.5 |
| ProductCatalog consumer update | Product Catalog | 0.8 | code | 0.5 |

---

**(a) SCV(Search)**

SCV = deploy_freq × mean_CSAI × failure_rate = 3 × 1.2 × 0.20

What risk level does this represent?

**(b) MRI for the Elasticsearch upgrade**

MRI = DG × CD × (1-FLI) × (2-OCR_weighted)
= 7 × 3 × (1-0.72) × (2-0.457)

What approval tier does MRI indicate?

**(c) CSD**

CSD = Σ[tw × depth_coeff] for all 4 components.

Calculate from the CSD table above.

What deployment strategy does CSD require?

**(d) Window sufficiency**

RV = 35 minutes (measured in staging).
Required window = 3 × RV = ?
Requested window = 90 minutes.

Is 90 minutes sufficient? What must be verified about the staging rollback time before accepting it as the production RV?

**(e) EBR and budget gate**

EBR = min(MRI × 0.05, 0.80)

Budget remaining = 40%. Is budget sufficient to absorb EBR?

**(f) DSS**

DSS = (1-SCV_norm) × (1-MRI/10) × APR × budget_remaining_fraction

Use: SCV_norm = SCV/1.0 = SCV value from (a); MRI from (b); APR = 0.31 (current); budget_remaining = 0.40.

Note: if MRI/10 > 1, cap (1-MRI/10) at 0 — DSS cannot be negative. What does DSS=0 mean operationally?

**(g) CAB decision**

Based on all calculations above, issue one of three verdicts: **Approve / Approve with Conditions / Reject**

For each verdict option, list the specific conditions that would apply or the specific reasons for rejection.

Consider all of these factors in your verdict:
- MRI approval tier
- Window sufficiency
- Budget sufficiency
- DSS value
- SCV risk level
- Strategic urgency (Elasticsearch 7.x is EOL — deferring is not costless)

**(h) What must change in the next sprint for this CR to pass CAB next month?**

List 3 specific, measurable actions. For each, state what the action changes and which formula input it improves.

Example structure: "Action: [what]. Improves: [which formula input]. New value: [what it becomes]."

---

*End of Exercise Set 4. Proceed to Exercise Set 5 (Integrated Scenarios) after completing all sections.*
