# Solutions: Exercise Set 4 — Change Governance

---

## Formula Reference

```
SCV  = deploy_freq_per_week × mean_CSAI × failure_rate
       CSAI: config=0.2, code=0.5, schema/API=1.0, coordinated=2.0
       Stable <0.5 | Moderate 0.5-1.0 | High-risk >1.0

MRI  = DG × CD × (1-FLI) × (2-OCR_weighted)
       <1 notify | 1–3 CAB 2-approvers | 3–8 VP Eng | ≥8 BLOCKED

CSD  = Σ[tier_weight × depth_coeff]
       depth: config=0.2, code=0.5, schema=1.5, API-contract=2.0, coordinated=2.5

DSS  = (1-SCV_norm)×(1-MRI/10)×APR×budget_remaining_fraction
       >0.70 standard | 0.40–0.70 SRE bridge | 0.20–0.40 window | <0.20 block

EBR  = min(MRI×0.05, 0.80)   [fraction of monthly budget reserved for this change]

Window sizing: deployment_window ≥ 3 × rollback_time
```

---

## Section B — Guided Exercises

### B1: SCV(Cart)

**Approach**: SCV measures change velocity risk — combining how often a service deploys, what kind of changes are deployed, and how often those changes fail.

**Given:**
- Deploy frequency: 5 per week
- Change composition: 3 code deploys, 2 config deploys
- Failure rate: 1 failure in last 10 deploys = 10% = 0.10

**Step 1 — Mean CSAI**

```
CSAI values:
  Code:   0.5 (each of the 3 code deploys)
  Config: 0.2 (each of the 2 config deploys)

mean_CSAI = (3×0.5 + 2×0.2) / 5
           = (1.5 + 0.4) / 5
           = 1.9 / 5
           = 0.38
```

**Step 2 — SCV**

```
SCV = deploy_freq × mean_CSAI × failure_rate
    = 5 × 0.38 × 0.10
    = 0.19
```

**Answer**: SCV(Cart) = 0.19. Stable (< 0.5).

**Key Insight**: Cart deploys 5 times per week — high cadence — but the mixed change profile (mostly code, some config) and 10% failure rate keep SCV at 0.19. The failure rate is the most sensitive variable. If failure rate doubles to 20%, SCV = 0.38 (still stable but approaching the boundary). If a schema deploy gets added (CSAI=1.0), mean_CSAI rises to 0.52 and SCV = 5 × 0.52 × 0.10 = 0.26, still stable. Cart's SCV is healthy — the team is deploying frequently without accumulating velocity risk.

---

### B2: MRI(Inventory Schema Change)

**Approach**: MRI measures how risky it is to make a change to this service in the current system state. It combines the service's blast radius (DG), journey depth (CD), failure containment (FLI), and observability coverage (OCR).

**Shopping cart reference values:**
- DG(Inventory) = 8
- CD (checkout journey) = 5
- FLI = 0.72 → (1-FLI) = 0.28
- OCR = 0.457 → (2-OCR) = 1.543

**MRI calculation:**

```
MRI = DG × CD × (1-FLI) × (2-OCR_weighted)
    = 8 × 5 × 0.28 × 1.543
    = 8 × 5 × 0.432
    = 8 × 2.16
    = 17.3

Step-by-step:
  DG × CD       = 8 × 5       = 40
  40 × (1-FLI)  = 40 × 0.28  = 11.2
  11.2 × (2-OCR) = 11.2 × 1.543 = 17.3
```

**Answer**: MRI = 17.3 → BLOCKED (≥ 8).

**Approval decision**: This change cannot proceed under current system conditions regardless of approval level. Even VP Engineering cannot approve a blocked MRI.

**Why a P1 schema change is blocked:**

The MRI formula does not assess how critical the change is — it assesses how dangerous the current system state makes any change. Inventory has DG=8 (significant blast radius), the checkout journey is CD=5 deep, FLI=0.72 means 28% of failures propagate, and OCR=0.457 means the team cannot observe nearly half the call chain. Under these conditions, a schema change — which has the highest CSAI weight (1.5) and longest blast radius — is too risky.

**Key Insight**: This is the counterintuitive insight of MRI. The change's content matters less than the system's current safety posture. A schema change that would be routine in a healthy system (high FLI, high OCR) becomes blocked in this system. The path to unblocking is not to change the review process — it is to fix the system (raise FLI to ≥0.90, raise OCR to ≥0.70) until MRI drops below 8. Once FLI=0.90 and OCR=0.70: MRI = 8×5×0.10×1.30 = 5.2 → VP approval, no longer blocked.

---

### B3: CSD(Payment Three-Service Change)

**Approach**: CSD measures the total change surface — how deep the changes go and how many services are affected. High CSD signals coordination complexity and rollback difficulty.

**Change components:**
1. Payment service: code change (depth_coeff = 0.5)
2. Payment service: schema change (depth_coeff = 1.5)
3. Order Management: code change as consumer (depth_coeff = 0.5)

**Tier weights:**
- Payment: P0 → tw = 1.0
- Order Management: P0 → tw = 1.0

**CSD calculation:**

```
CSD = Σ[tier_weight × depth_coeff]
    = (1.0 × 0.5) [Payment code]
    + (1.0 × 1.5) [Payment schema]
    + (1.0 × 0.5) [OM consumer code change]

    = 0.5 + 1.5 + 0.5
    = 2.5
```

**Answer**: CSD = 2.5 → Small change (< 5). No expand-contract required.

**However — important caveat**: CSD = 2.5 is small, but two P0 services are touched. This means:
- Coordinated deployment sequence required (Payment schema first, then OM consumer)
- Rollback must be coordinated (cannot independently roll back one service)
- Testing must include end-to-end integration, not just unit tests

CSD tells you the scope. It does not replace judgment about coordination overhead.

**Key Insight**: CSD catches changes that look simple but aren't. A change classified as "small code update" that actually includes a schema migration (depth 1.5) is three times more complex than its label suggests. CSD makes the true depth visible so the change review board can require the right testing and deployment sequencing.

---

### B4: DSS — Deployment Safety Score

**Approach**: DSS is a composite score that tells you how safe it is to deploy right now, given SCV, MRI, alert quality, and remaining error budget. Low DSS = higher monitoring requirements and possibly a block.

**Given:**
- SCV = 0.10
- MRI = 3.45
- APR = 0.75
- Budget remaining = 70% = 0.70

**Step 1 — SCV normalization**

```
SCV_norm = min(SCV / 5, 1.0)
         = min(0.10 / 5, 1.0)
         = min(0.02, 1.0)
         = 0.02
```

**Step 2 — DSS**

```
DSS = (1 - SCV_norm) × (1 - MRI/10) × APR × budget_remaining_fraction
    = (1 - 0.02) × (1 - 3.45/10) × 0.75 × 0.70
    = 0.98 × 0.655 × 0.75 × 0.70

Step-by-step:
  0.98 × 0.655 = 0.642
  0.642 × 0.75 = 0.481
  0.481 × 0.70 = 0.337
```

**Answer**: DSS = 0.337 → Maintenance Window required (0.20–0.40 range).

**Deployment conditions required:**
- Scheduled maintenance window (specific time, communicated to stakeholders)
- SRE on-call available for 2 hours post-deploy
- Rollback procedure documented and tested
- 15-minute canary period before full rollout

**Key Insight**: DSS = 0.337 is largely driven by APR (0.75 — below target of 0.80) and MRI (3.45). Even with 70% budget remaining and low SCV, poor alert quality pulls DSS into the maintenance window band. This is intentional — if you cannot trust your alerts to detect a problem during deployment, you need extra human oversight. Fix APR first, and the same deployment would score: DSS = 0.98 × 0.655 × 0.85 × 0.70 = 0.382 — still in maintenance window, but closer to the SRE bridge threshold.

---

## Section C — Applied Problems

### C1: Three Change Requests — 28% Budget Remaining

**System state:**
- FLI = 0.72 → (1-FLI) = 0.28
- OCR = 0.457 → (2-OCR) = 1.543
- Budget remaining = 28%

**CR-A: Auth service config change**

```
DG(Auth) = 18, CD = 5

MRI = 18 × 5 × 0.28 × 1.543
    = 18 × 5 × 0.432
    = 18 × 2.16
    = 38.9
```

MRI = 38.9 → BLOCKED (≥ 8).

Note: Even a config-only change (depth=0.2) does not reduce MRI — MRI measures the system's current risk posture, not the change depth. CSD would be small (1.0 × 0.2 = 0.2) but MRI still reflects Auth's DG=18 and the system's low FLI/OCR.

EBR check: `min(38.9 × 0.05, 0.80) = min(1.945, 0.80) = 80% of budget`. Available = 28%. Even if not blocked by MRI, the EBR (80%) far exceeds available budget (28%). Doubly blocked.

**Decision: CR-A REJECTED. Reasons: MRI=38.9 (blocked tier) and EBR=80% exceeds available 28%.**

---

**CR-B: Notification service code change**

```
DG(Notification) = 3, CD = 1 (notification is not in the main checkout chain)

MRI = 3 × 1 × 0.28 × 1.543
    = 3 × 1 × 0.432
    = 1.30
```

MRI = 1.30 → CAB approval, 2 approvers required.

```
EBR = min(1.30 × 0.05, 0.80)
    = min(0.065, 0.80)
    = 0.065 = 6.5% of budget
```

Available budget: 28% > 6.5% required → **CAN PROCEED**.

**Decision: CR-B APPROVED. CAB with 2 approvers. EBR=6.5%, well within 28% available.**

---

**CR-C: Product Catalog schema change**

```
DG(Product Catalog) = 6, CD = 3 (Browse journey)

MRI = 6 × 3 × 0.28 × 1.543
    = 6 × 3 × 0.432
    = 7.78
```

MRI = 7.78 → VP Engineering approval required (3–8 range). Not blocked by tier alone.

```
EBR = min(7.78 × 0.05, 0.80)
    = min(0.389, 0.80)
    = 0.389 = 38.9% of budget
```

Available budget: 28% < 38.9% required → **BLOCKED by budget**.

**Decision: CR-C REJECTED. Reason: EBR=38.9% exceeds available budget of 28%. Defer to next budget window.**

**Processing order:**
```
CR-B  → APPROVED (proceed this week)
CR-A  → REJECTED (blocked by MRI — resubmit when FLI and OCR improve)
CR-C  → REJECTED (budget — resubmit at start of next month with 100% budget available)
```

**Key Insight**: Budget as a change gate is not bureaucracy — it is a forcing function that prevents teams from consuming the entire error budget on changes in the second half of the month. By day 28 with 28% budget, any change that requires more than 28% EBR must wait. This protects the remaining budget for genuine incidents.

---

### C2: SCW (Safe Change Window) and RV Analysis

**Approach**: The deployment window must be at least 3× the rollback time to ensure the team has enough time to detect a problem AND execute a full rollback before the window closes.

**Given rollback times:**
- Service A: 8 minutes
- Service B: 15 minutes
- Service C: 10 minutes
- No data migration required

**Step 1 — Maximum rollback time across the change set**

```
RV = max(8, 15, 10) = 15 minutes
```

**Step 2 — Minimum required window**

```
window_minimum = 3 × RV
               = 3 × 15
               = 45 minutes
```

**Step 3 — Evaluate proposed window (45 minutes)**

```
Proposed window = 45 minutes
3 × RV = 45 minutes
45 ≥ 45 → EXACTLY meets minimum (no margin)
```

**Step 4 — Evaluate actual RV = 22 minutes**

Correction: if the actual measured rollback time during testing was 22 minutes (not the 15-minute estimate):

```
Required window = 3 × 22 = 66 minutes
Proposed window = 45 minutes
45 < 66 → INSUFFICIENT
```

**Decision: Window is insufficient. The team cannot safely deploy in a 45-minute window when rollback takes 22 minutes.**

**Corrective action:**

```
Option A: Extend window to 90 minutes
  max_RV at 90min = 90/3 = 30 minutes
  Actual RV = 22 minutes < 30 minutes → SUFFICIENT

Option B: Reduce rollback time to ≤ 15 minutes
  Requires pre-staging rollback artifacts and testing the rollback procedure
  If RV = 15min: required window = 3 × 15 = 45min → original window works
```

**Recommended: Extend window to 90 minutes.** Rollback time reduction requires engineering work (pre-staging, scripting) that may not be available before the planned deployment date.

**Key Insight**: The 3×RV rule exists because detection takes time. A deployment issue may not manifest immediately — it might take 15-20 minutes for error rates to rise enough to trigger alerts, and SREs need time to assess before rolling back. The 3×RV window gives the team: 1× to detect the problem, 1× to decide and initiate rollback, 1× to execute the rollback. Skimping on window size means the team may be mid-rollback when the window closes — an even worse state than no rollback.

---

## Section D — Advanced: Search Elasticsearch Upgrade CAB

**Context:** Search service (P1, tw=0.8) upgrading Elasticsearch. The change touches schema, config, API contract, and has consumer service updates.

**Given:**
- SCV_current(Search): 3 deploys/week, mean_CSAI=1.2, failure_rate=0.20
- MRI inputs: DG=7, CD=3, FLI=0.72, OCR=0.457
- CSD components: Elasticsearch schema, API contract update, config change, Search consumer changes
- RV = 35 minutes
- Proposed window = 90 minutes
- Budget remaining = 40%
- APR = 0.31

### D(a): SCV

```
SCV = deploy_freq × mean_CSAI × failure_rate
    = 3 × 1.2 × 0.20
    = 0.72
```

SCV = 0.72 → Moderate risk (0.5–1.0 range). Not high-risk, but above stable.

---

### D(b): MRI

```
MRI = DG × CD × (1-FLI) × (2-OCR)
    = 7 × 3 × 0.28 × 1.543
    = 7 × 3 × 0.432
    = 9.07
```

MRI = 9.07 → BLOCKED (≥ 8). Just over the block threshold.

The change is blocked. VP Engineering approval cannot override a blocked MRI.

---

### D(c): CSD

**Change components and depth coefficients:**

| Component | Service | tw | Depth | Coeff | CSD contribution |
|-----------|---------|-----|-------|-------|-----------------|
| Elasticsearch schema migration | Search | 0.8 | schema | 1.5 | 0.8×1.5 = 1.20 |
| API contract version bump | Search | 0.8 | API-contract | 2.0 | 0.8×2.0 = 1.60 |
| Config changes (index settings) | Search | 0.8 | config | 0.2 | 0.8×0.2 = 0.16 |
| Consumer service code update | Product Catalog (P1) | 0.8 | code | 0.5 | 0.8×0.5 = 0.40 |

```
CSD = 1.20 + 1.60 + 0.16 + 0.40
    = 3.36
```

CSD = 3.36 → Small change (< 5). Despite the number of components, each is at a single service.

Note: If the consumer updates span multiple services (e.g., both Product Catalog and Recommendation), CSD would add additional terms.

---

### D(d): Window Sufficiency

```
Required window = 3 × RV
               = 3 × 35
               = 105 minutes

Proposed window = 90 minutes
90 < 105 → INSUFFICIENT
```

The 90-minute window must be extended to at least 105 minutes. Recommended: 120 minutes (provides 15-minute buffer above minimum).

---

### D(e): EBR and Budget Gate

```
EBR = min(MRI × 0.05, 0.80)
    = min(9.07 × 0.05, 0.80)
    = min(0.454, 0.80)
    = 0.454 = 45.4% of budget

Available budget = 40%
45.4% > 40% → BLOCKED by budget
```

Even if MRI were below 8, this change would be blocked by the budget gate.

---

### D(f): DSS

```
SCV_norm = min(SCV/5, 1.0) = min(0.72/5, 1.0) = 0.144

DSS = (1 - 0.144) × (1 - 9.07/10) × 0.31 × 0.40
    = 0.856 × 0.093 × 0.31 × 0.40

Step-by-step:
  0.856 × 0.093 = 0.0796
  0.0796 × 0.31 = 0.0247
  0.0247 × 0.40 = 0.0099
```

DSS = 0.010 → BLOCK (< 0.20).

---

### D(g): CAB Decision

**REJECT. Four simultaneous block conditions:**

| Gate | Value | Threshold | Status |
|------|-------|-----------|--------|
| MRI | 9.07 | < 8 to approve | BLOCKED |
| EBR | 45.4% | ≤ budget (40%) | BLOCKED |
| Window | 90min | ≥ 105min required | INSUFFICIENT |
| DSS | 0.010 | ≥ 0.20 to proceed | BLOCKED |

No single condition is borderline. All four independently block this change. The Elasticsearch upgrade cannot proceed in the current system state.

---

### D(h): Conditions for Next Month Approval

**What must change to make this change approvable?**

**Condition 1: Reduce MRI below 8**

```
Current MRI = 7 × 3 × 0.28 × 1.543 = 9.07

Required: MRI < 8

Path: Improve FLI to ≥ 0.85 (circuit breakers) and OCR to ≥ 0.70

Verification:
  New (1-FLI) = 0.15
  New (2-OCR) = 1.30
  New MRI = 7 × 3 × 0.15 × 1.30 = 4.1 → CAB (1–3 range, with 2 approvers)
  
Actually: 7×3=21, 21×0.15=3.15, 3.15×1.30=4.1
Wait: 4.1 is in the 3-8 range = VP Eng approval, not CAB.
For CAB (1-3): need MRI < 3 → harder target.
VP approval (3-8): FLI=0.85, OCR=0.70 → MRI=4.1 is achievable and approvable.
```

**Condition 2: Submit at start of budget window**

```
At day 1: budget_remaining = 100%
EBR = 45.4% of budget
100% > 45.4% → PASSES budget gate
```

Start the change at the beginning of the monthly budget window, not mid-month.

**Condition 3: Extend deployment window or reduce rollback time**

```
Option A: Window = 120 minutes → 3×35 = 105 < 120 → sufficient
Option B: Reduce RV to ≤ 30 minutes → 3×30 = 90 = proposed window → sufficient
         (Pre-stage rollback artifacts, script the rollback procedure, test in staging)
```

**Summary of pre-conditions for approval next month:**

1. Circuit breakers implemented on Search's highest-risk caller paths → FLI improves to ≥0.85
2. P0 and P1 service observability completed → OCR improves to ≥0.70 → MRI drops to 4.1
3. Schedule at day 1 of the new budget month → EBR=45.4% fits within 100% budget
4. Extend window to 120 minutes OR reduce RV to ≤30 minutes through rollback scripting

**Key Insight**: MRI=9.07 is not a permanent block — it is a signal about system state. The path to approval is to fix the system, not to negotiate with the change review board. Teams that understand this design the right sequence: (1) fix FLI and OCR first, (2) then the Elasticsearch upgrade becomes a routine VP-approved change, not a CAB escalation.

---

## Quick Reference — Key Answers

| Exercise | Formula | Result | Decision |
|----------|---------|--------|---------|
| B1 SCV(Cart) | 5×0.38×0.10 | 0.19 | Stable |
| B2 MRI(Inventory schema) | 8×5×0.28×1.543 | 17.3 | BLOCKED |
| B3 CSD(Payment) | 0.5+1.5+0.5 | 2.5 | Small — coordination required |
| B4 DSS | 0.98×0.655×0.75×0.70 | 0.337 | Maintenance window |
| C1 MRI(Auth config) | 18×5×0.28×1.543 | 38.9 | BLOCKED + EBR exceeds budget |
| C1 MRI(Notification) | 3×1×0.28×1.543 | 1.30 | APPROVED — CAB |
| C1 MRI(ProdCat schema) | 6×3×0.28×1.543 | 7.78 | EBR 38.9% > 28% — budget block |
| C2 Required window | 3×22min | 66min | 45min insufficient — extend to 90min |
| D SCV(Search) | 3×1.2×0.20 | 0.72 | Moderate |
| D MRI(Search) | 7×3×0.28×1.543 | 9.07 | BLOCKED |
| D CSD(Search) | 1.20+1.60+0.16+0.40 | 3.36 | Small |
| D Window | 3×35=105 > 90 | Insufficient | Extend to 120min |
| D EBR | min(0.454,0.80)=45.4% > 40% | Budget block | Start next month |
| D DSS | 0.856×0.093×0.31×0.40 | 0.010 | BLOCK |
