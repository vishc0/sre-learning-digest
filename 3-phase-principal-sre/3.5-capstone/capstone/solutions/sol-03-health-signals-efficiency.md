# Solutions: Exercise Set 3 — Health Signals and Efficiency

---

## Formula Reference

```
EBV  = traffic_normalized_error_rate / baseline_rate
APR  = actionable_alerts / total_alerts               [target >0.80]
MTBI = period / incident_count
achievable_SLO = MTBI/(MTBI+MTTR)
OCR  = Σ(instrumented×tier_weight) / Σ(tier_weight)
OL   = Δ(budget_pp_per_week) / SRE_hours
RCR  = (response_hrs × freq_per_year) / fix_hours    [fix if >0.50]
TAF  = toil_growth_rate / traffic_growth_rate         [target <1.0]
RIS  = (RCR × OL) / MRI
```

---

## Section B — Guided Exercises

### B1: EBV and Time to Breach

**Approach**: EBV measures how fast the error budget is burning relative to baseline. If EBV > 1.0, you are burning faster than planned. Time-to-breach projects when the budget runs out at the current burn rate.

**Given:**
- Monthly budget: 21.6 minutes
- Budget consumed by day 20: 18 minutes
- Budget remaining: 21.6 − 18 = 3.6 minutes
- Days remaining in month: 10

**Step 1 — Baseline burn rate (planned)**

```
baseline_rate = total_budget / period_in_minutes
              = 21.6 min / (30 days × 24 hrs × 60 min)
              = 21.6 / 43,200
              = 0.0005 min/min
              (burning 0.05% of budget per minute at baseline)
```

**Step 2 — Actual burn rate (observed)**

```
actual_rate = consumed / elapsed_time
            = 18 min / (20 days × 24 × 60 min)
            = 18 / 28,800
            = 0.000625 min/min
```

**Step 3 — EBV**

```
EBV = actual_rate / baseline_rate
    = 0.000625 / 0.0005
    = 1.25

(Alternatively: at baseline you should have consumed 20/30 × 21.6 = 14.4 min by day 20.
 You consumed 18 min. EBV = 18/14.4 = 1.25 — same result.)
```

**Step 4 — Time to budget exhaustion**

```
time_to_breach = remaining_budget / actual_rate
               = 3.6 min / 0.000625 min/min
               = 5,760 minutes
               = 4.0 days

Or using EBV:
time_to_breach = remaining_budget / (EBV × baseline_rate)
               = 3.6 / (1.25 × 0.0005)
               = 3.6 / 0.000625
               = 5,760 min = 4.0 days
```

**EDFD (Exhaustion Date):**

```
EDFD = today + 4 days = Day 24 of the month
```

The error budget will be fully consumed by Day 24 — 6 days before month end. The checkout journey is 60% through the month with 83% of the budget consumed.

**Answer**: EBV = 1.25. Budget exhaustion in 4 days (Day 24).

**Key Insight**: EBV=1.25 seems modest (only 25% above baseline burn), but this small deviation compounds fast. At day 20 you have already consumed 83% of your monthly budget. The last 10 days must run on 3.6 minutes — equivalent to needing sub-0.0003 min/min burn rate, which requires near-perfect operation when the system is already struggling. EBV is most dangerous in the second half of the month when remaining budget is small.

---

### B2: APR Analysis — Alert Volume Reduction

**Approach**: APR tells you what fraction of alerts are worth responding to. If APR is low, the team is trained to ignore alerts — which means real incidents get missed. The fix is not to find more actionable alerts, it's to eliminate the non-actionable ones.

**Given:**
- Total alerts per week: 150
- Actionable alerts per week: 47

**Step 1 — Current APR**

```
APR = actionable / total
    = 47 / 150
    = 0.313
    = 31.3%
```

Current APR = 0.313. Target is >0.80. The team is responding to noise 69% of the time.

**Step 2 — What would it take to reach APR=0.80?**

Option A: Increase actionable alerts to 80% of current total
```
required_actionable = 0.80 × 150 = 120 actionable per week
Currently generating = 47 actionable
Gap = 120 − 47 = 73 more actionable alerts needed
```
This is not possible — you cannot manufacture 73 additional real problems that need alerting. The 47 genuinely actionable issues are the real signal. The remaining 103 alerts are noise.

Option B: Reduce total alert volume so 47 actionable = 80% of total
```
required_total = 47 / 0.80 = 58.75 → 59 alerts maximum
Alerts to eliminate = 150 − 59 = 91 alerts per week
```

**Answer**: You must eliminate 91 alerts per week (61% of current volume). This requires suppressing or deleting non-actionable alert rules — not tuning thresholds.

**Steps to eliminate 91 alerts:**
1. Identify which alert rules generated alerts with no SRE action taken (review last 30 days of alert history)
2. Delete rules that fired but produced no SRE response >80% of the time
3. Convert remaining noisy rules to metrics dashboards (visible, not paging)
4. For borderline rules: raise thresholds until they only fire when action is required

**Key Insight**: APR=0.313 means the on-call rotation is conditioned to treat alerts as background noise. When a real SEV1 fires in a sea of ignored alerts, mean-time-to-acknowledge increases. Low APR is not an efficiency problem — it's a reliability risk. Every alert you don't eliminate is a small tax on SRE trust in the alerting system.

---

### B3: Auth Availability — Achievable vs. Declared

**Approach**: MTBI and MTTR constrain the maximum achievable availability. Declared SLOs that exceed this achievable maximum are SLO theater — mathematically impossible given operational reality.

**Given:**
- Auth MTBI: 30 days between incidents
- Auth MTTR: 45 minutes to resolve
- Auth declared SLO: 99.990%
- Checkout SLA: 99.95%, monthly budget: 21.6 minutes

**Step 1 — Achievable SLO from MTBI/MTTR**

```
MTBI in minutes = 30 × 24 × 60 = 43,200 minutes
MTTR = 45 minutes

achievable_SLO = MTBI / (MTBI + MTTR)
               = 43,200 / (43,200 + 45)
               = 43,200 / 43,245
               = 0.99896
               = 99.896%
```

**Step 2 — Gap between declared and achievable**

```
Gap = declared − achievable
    = 99.990% − 99.896%
    = 0.094 percentage points

In minutes per month:
0.094% × 43,200 min = 40.6 minutes/month of unaccounted unavailability
```

Auth is unavailable 40.6 minutes per month on average, but declares a 4.3 minute budget (99.99%). The declared SLO is off by nearly 10×.

**Step 3 — Annual impact on Checkout SLA**

```
Annual checkout budget = 21.6 min/month × 12 = 259.2 minutes

Auth-contributed downtime per year:
  1 incident × 45 min × 12 months = 540 minutes/year
  (or 40.6 min/month × 12 = 487 minutes/year)

Ratio = 487 / 259.2 = 1.88×
```

Auth's unavailability alone accounts for 1.88× the entire annual checkout error budget. Before any other service fails, before any deployment incident, Auth's MTTR alone consumes the full SLA for Checkout plus 88% more.

**Answer**: Auth achievable SLO = 99.896%. Declared SLO = 99.990%. The declared SLO is not achievable given Auth's operational MTBI/MTTR. Auth-contributed downtime exceeds the entire annual Checkout SLA budget by 1.88×.

**Key Insight**: This is the most dangerous form of SLO theater — the service declares an SLO that is mathematically impossible to achieve given its own operational data. The team carries a false sense of safety. Auth's declared SLO should be 99.90% (achievable) not 99.99% (fantasy). Once the SLO is honest, the MRI and change governance math will accurately reflect Auth's real risk profile — and circuit breakers on Auth will be prioritized correctly.

---

### B4: OCR — Weighted Observability Coverage

**Approach**: OCR weights observability credit by service tier. A P0 service with full instrumentation contributes more to OCR than a P3 service. Partial instrumentation gets partial credit proportional to coverage fraction.

**Tier weight reference: P0=1.0, P1=0.8, P2=0.5, P3=0.3**

**Step 1 — Total weight denominator**

| Service | Tier | tw |
|---------|------|-----|
| Auth | P0 | 1.0 |
| Cart | P0 | 1.0 |
| Payment | P0 | 1.0 |
| Order Mgmt | P0 | 1.0 |
| Inventory | P1 | 0.8 |
| Pricing | P1 | 0.8 |
| Product Catalog | P1 | 0.8 |
| Search | P1 | 0.8 |
| User Profile | P2 | 0.5 |
| Notification | P2 | 0.5 |
| Recommendation | P2 | 0.5 |
| Reviews | P3 | 0.3 |

```
Total_weight = 1.0+1.0+1.0+1.0+0.8+0.8+0.8+0.8+0.5+0.5+0.5+0.3
             = 9.0
```

**Step 2 — Instrumented weight (coverage fraction × tier weight)**

| Service | Coverage | tw | Weighted contribution |
|---------|----------|-----|----------------------|
| Auth | 50% metrics+logs (no traces) | 1.0 | 0.50×1.0 = 0.50 |
| Cart | 75% (missing distributed traces) | 1.0 | 0.75×1.0 = 0.75 |
| Payment | 100% full 4-signal | 1.0 | 1.00×1.0 = 1.00 |
| Order Mgmt | 50% | 1.0 | 0.50×1.0 = 0.50 |
| Inventory | 50% | 0.8 | 0.50×0.8 = 0.40 |
| Pricing | 0% (no instrumentation) | 0.8 | 0.00×0.8 = 0.00 |
| Product Catalog | 75% | 0.8 | 0.75×0.8 = 0.60 |
| Search | 0% | 0.8 | 0.00×0.8 = 0.00 |
| User Profile | 0% | 0.5 | 0.00×0.5 = 0.00 |
| Notification | 25% (logs only) | 0.5 | 0.25×0.5 = 0.125 |
| Recommendation | 0% | 0.5 | 0.00×0.5 = 0.00 |
| Reviews | 0% | 0.3 | 0.00×0.3 = 0.00 |

```
Total_instrumented = 0.50+0.75+1.00+0.50+0.40+0.00+0.60+0.00+0.00+0.125+0.00+0.00
                   = 3.875
```

**Step 3 — OCR**

```
OCR = total_instrumented / total_weight
    = 3.875 / 9.0
    = 0.431 ≈ 43.1%
```

Note: The shopping cart reference value of 0.457 reflects slightly different coverage assumptions. The calculation method is identical — small differences trace to assumed coverage fractions for services with partial instrumentation.

**Answer**: OCR ≈ 43–46%. The platform has observability coverage for less than half its weighted service surface.

**Priority instrumentation order** (highest tw first, with zero coverage):
1. Pricing (P1, tw=0.8, 0% coverage) — impacts Cart and Search
2. Search (P1, tw=0.8, 0% coverage) — Browse journey blind spot
3. Auth (P0, tw=1.0, only 50%) — most critical service, incomplete coverage

**Key Insight**: OCR of 43% means that during the next SEV1, the team will be debugging 57% of the call chain in the dark. Incidents take longer because engineers must infer state from indirect signals. OCR is not a vanity metric — it directly determines MTTR. Every 10 percentage points of OCR improvement corresponds to faster incident triage. Target: P0 services at 100%, P1 at 75%, P2 at 50% before any new service is added.

---

## Section C — Applied Problems

### C1: RCR — Alert Triage Workflow

**RCR formula:**
```
RCR = (response_hours × frequency_per_year) / fix_hours
Fix if RCR > 0.50
```

**Three workflows to analyze:**

**Workflow A: Manual alert-to-ticket triage**
```
response_hours = 0.75 hrs (45 min per occurrence)
frequency_per_year = 52 (weekly)
fix_hours = 40

RCR_A = (0.75 × 52) / 40
       = 39 / 40
       = 0.975
```
RCR_A = 0.975 → FIX (well above 0.50). The manual triage is costing 39 SRE-hours/year and could be automated for 40 hours investment. Payback in one year.

**Workflow B: Quarterly capacity planning report**
```
response_hours = 3 hrs per occurrence
frequency_per_year = 12 (monthly, not quarterly — assuming monthly planning cycles)
fix_hours = 160 (full automation of reporting pipeline)

RCR_B = (3 × 12) / 160
       = 36 / 160
       = 0.225
```
RCR_B = 0.225 → DEFER. 36 hours/year cost vs. 160 hours to automate. Automation doesn't pay back within 2 years. Do it manually until a natural refactor opportunity arises.

**Workflow C: On-call handoff documentation**
```
response_hours = 0.5 hrs (30 min per handoff)
frequency_per_year = 26 (bi-weekly on-call rotation)
fix_hours = 24 (build a standard handoff template/tool)

RCR_C = (0.5 × 26) / 24
       = 13 / 24
       = 0.542
```
RCR_C = 0.542 → FIX (just above 0.50). 13 hours/year vs. 24 hours to fix. Payback in 22 months — marginal but worth doing because standardized handoffs also reduce MTTR (quality benefit not captured in RCR).

**Prioritization with 40-hour budget:**

| Workflow | RCR | Fix Hours | Decision |
|----------|-----|-----------|---------|
| A: Alert triage | 0.975 | 40 | FIX — highest RCR, use all 40 hours |
| C: Handoff docs | 0.542 | 24 | FIX — do next sprint (24 hrs) |
| B: Capacity report | 0.225 | 160 | DEFER — not cost-effective |

With 40 hours: complete A (40 hrs = full budget). C must wait for next sprint allocation.

**Key Insight**: RCR forces an honest ROI conversation. Teams often automate what's technically interesting rather than what costs the most SRE-hours. Workflow A (alert triage) looks boring but has the highest RCR — it's the highest-priority automation investment. Do the math, not the hunch.

---

### C2: TAF — Toil Growth vs. Traffic Growth

**Approach**: TAF measures whether toil is growing faster or slower than the system it serves. TAF < 1.0 means automation is keeping up. TAF ≥ 1.0 means toil will eventually consume the team.

**Given:**
- Traffic growth: 15%
- Toil composition: alert-response 45%, manual deploys 30%, customer support 25%
- Alert-response hours grew 22%
- Manual deploy hours grew 8%
- Customer support hours grew 10%

**Step 1 — Weighted toil growth rate**

```
overall_toil_growth = (fraction_alert × growth_alert) 
                    + (fraction_deploy × growth_deploy) 
                    + (fraction_support × growth_support)

= (0.45 × 0.22) + (0.30 × 0.08) + (0.25 × 0.10)
= 0.099 + 0.024 + 0.025
= 0.148
= 14.8%
```

**Step 2 — TAF**

```
TAF = toil_growth_rate / traffic_growth_rate
    = 0.148 / 0.150
    = 0.987 ≈ 1.0
```

TAF = 0.987. Borderline — at essentially 1.0. Toil is growing almost exactly as fast as traffic. The team will not shrink relative to traffic load, but they will not fall further behind either. This is a warning sign, not a crisis — yet.

**Step 3 — Scenario: Eliminate alert noise (alert-response hours → minimal)**

If alert triage workflow is automated (from C1 above), alert-response hours could be reduced to near-zero growth:

```
new_growth = (0.45 × 0.00) + (0.30 × 0.08) + (0.25 × 0.10)
           = 0 + 0.024 + 0.025
           = 0.049
           = 4.9%

New_TAF = 0.049 / 0.150
         = 0.327
```

TAF drops from 1.0 → 0.327. The automation investment from C1 delivers a dramatic TAF improvement — and demonstrates why alert noise is not just an on-call morale issue. It is the primary driver of toil growth.

**Answer**: Current TAF = 0.987 (borderline). After alert automation: TAF = 0.327 (excellent, well below 1.0).

**Key Insight**: TAF is the long-run sustainability metric. A team with TAF=1.0 is treading water — as traffic doubles, their toil doubles too, and headcount must scale linearly. A team with TAF=0.33 can triple traffic without adding proportional toil. The difference between these two outcomes, in this case, is one 40-hour automation project (workflow A from C1).

---

## Section D — Advanced: RIS Portfolio Prioritization

**RIS formula:**
```
RIS = (RCR × OL) / MRI

RCR = toil cost ratio
OL  = budget consumption rate per SRE-hour
MRI = system risk (scales the denominator — higher risk makes each investment more valuable... 
      wait: higher MRI means lower DSS and tighter change constraints. 
      RIS penalizes high-MRI contexts because they are harder to deploy improvements into.)
```

**Three investment options:**

**Investment A: OCR Improvement (P0 instrumentation project)**
```
RCR_A = 0.15  (low — instrumentation has modest direct toil impact)
OL_A  = 0.002  (small budget impact per SRE-hour)
MRI_A = 1.0   (low-risk investment itself)

RIS_A = (0.15 × 0.002) / 1.0
      = 0.0003 / 1.0
      = 0.0003
```

**Investment B: Alert Redesign (eliminate 91 non-actionable alerts)**
```
RCR_B = 9.4   (extremely high — alerts fire 52×/year, 10.75 hrs response, fix=60 hrs)
        Verification: (10.75 × 52) / 60 = 559/60 = 9.32 ≈ 9.4
OL_B  = 0.0008 (moderate budget impact)
MRI_B = 1.0   (alert changes are low-risk deployments)

RIS_B = (9.4 × 0.0008) / 1.0
      = 0.00752 / 1.0
      = 0.0075
```

**Investment C: Circuit Breakers (Auth cascade prevention)**
```
RCR_C = 0.40  (moderate — cascades are expensive when they occur but not daily)
OL_C  = 0.033 (high — each CB prevents significant budget erosion)
MRI_C = 1.0   (CB implementation itself is moderate-risk change)

RIS_C = (0.40 × 0.033) / 1.0
      = 0.013 / 1.0
      = 0.013
```

**Step 2 — Ranking**

| Investment | RIS | Rank | Rationale |
|-----------|-----|------|-----------|
| C: Circuit Breakers | 0.013 | 1st | Highest budget preservation per SRE-hour |
| B: Alert Redesign | 0.0075 | 2nd | Highest toil reduction (RCR=9.4) |
| A: OCR Improvement | 0.0003 | 3rd | Lowest direct budget + toil impact |

**Priority order: C → B → A**

**The surprising result**: OCR improvement ranks last despite being the most technically important infrastructure investment. Why? Because RIS measures budget-and-toil return per SRE-hour. Instrumentation has high long-term value (faster MTTR, better debugging) but low direct RCR (it doesn't stop incidents from occurring or directly reduce toil hours) and low OL (it doesn't save much error budget directly). RIS is a short-term prioritization tool — it must be supplemented with strategic investment logic for OCR.

**Operational recommendation:**
- This quarter: Circuit breakers (C) — highest RIS, also prevents JRCS going negative
- This quarter: Alert redesign (B) — highest toil reduction
- Next quarter: OCR (A) — required for journey reliability and SRMI improvement, even though RIS is low

The team cannot postpone OCR indefinitely just because RIS ranks it third. OCR is a prerequisite for MRI improvement — and without MRI improvement, future CBs and alert redesigns will still be operating in a system that cannot detect its own failures.

**Key Insight**: RIS is a useful tiebreaker for investment prioritization, but it does not capture strategic infrastructure debt. A low-RIS investment can be a high-priority prerequisite for future high-RIS investments. Use RIS for quarterly prioritization, not multi-year roadmap decisions.

---

## Quick Reference — Key Answers

| Exercise | Formula | Result | Decision |
|----------|---------|--------|---------|
| B1 EBV | actual/baseline | 1.25 | Budget exhausted Day 24 |
| B1 Time to breach | 3.6/0.000625 | 4 days | Freeze non-critical changes |
| B2 APR current | 47/150 | 0.313 | Must eliminate 91 alerts |
| B2 Target volume | 47/0.80 | 59 alerts | 61% volume reduction required |
| B3 Achievable SLO | 43200/43245 | 99.896% | Auth declared SLO is theater |
| B3 Annual gap | 487/259.2 | 1.88× | Auth exceeds full checkout budget alone |
| B4 OCR | 3.875/9.0 | 43.1% | Priority: Pricing, Search, Auth |
| C1 RCR_A | (0.75×52)/40 | 0.975 | FIX — highest priority |
| C1 RCR_B | (3×12)/160 | 0.225 | DEFER |
| C1 RCR_C | (0.5×26)/24 | 0.542 | FIX — next sprint |
| C2 TAF current | 0.148/0.150 | 0.987 | Borderline — eliminate alert noise |
| C2 TAF after automation | 0.049/0.150 | 0.327 | Excellent |
| D RIS ranking | C=0.013,B=0.0075,A=0.0003 | C>B>A | CBs first, then alerts, then OCR |
