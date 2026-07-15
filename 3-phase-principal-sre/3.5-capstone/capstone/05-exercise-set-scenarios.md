# Exercise Set 5: Integrated Scenarios — Full System Assessment

**Reference**: `00-shopping-cart-reference-system.md`
**Formulae used in this set**: All 25 formulae from the framework. This exercise set does not isolate individual terms — it requires you to select the right formula for the situation and combine them across sections of the framework.

**Before you begin**: These scenarios are designed to replicate the kinds of assessments you would perform in a Principal SRE or SRE Manager role. There are no single correct answers for the judgment questions — but there are wrong answers, and the wrong answers always share the same characteristic: they ignore what the data says. Let the numbers lead. Your judgment comes in when you decide what to do next.

**How to approach these scenarios**:
1. Read the full scenario before starting any calculations
2. Identify which formulae apply to each sub-question
3. Calculate first, interpret second — do not reason from intuition and then reverse-engineer the numbers
4. For judgment questions, state your reasoning explicitly and cite which metric most influenced your decision

---

## Scenario 1: Black Friday Reliability Audit

It is 2 weeks before Black Friday. Traffic is expected to reach 4× baseline (3,200 rps peak vs. 800 rps normal). You are the Principal SRE responsible for the shopping cart system. The VP Engineering wants a readiness report by end of day.

**Current state** (all figures as of day 18 of the current 30-day month):
- OCR_weighted = 0.457
- APR = 0.31
- FLI = 0.72
- CC_max = 10.8
- All 4 P0 services (Auth, Cart, Payment, Order Management) are at 60% error budget consumed
- Budget remaining: 40% of monthly allocation

---

**(a) Pre-provisioning calculation for Auth**

Auth is the highest-risk service under load. Current autoscaling configuration:
- Pod capacity: 150 rps/pod (at normal load)
- Current running pods: 6 (handling 800 rps baseline with headroom)
- Traffic ramp on Black Friday: 300 rps/minute increase for 20 minutes (0 to peak)
- Autoscaling lag: 3 minutes (time from "scale event triggered" to "new pods serving traffic")

During the autoscaling lag window of 3 minutes, traffic increases at 300 rps/minute × 3 min = 900 rps above current capacity.

To absorb this without pod saturation:
- Peak gap = 900 rps of unexpected traffic during scale lag
- Additional pods needed to absorb this gap = 900 / 150 = 6 additional pods pre-provisioned

(a-i) How many total pods must Auth have pre-provisioned before Black Friday traffic begins?
Current pods: 6. Add pods for baseline scale to 4× (3200 / 150 = 22 pods at peak). Add lag buffer of 6 pods. What is the pre-provision target?

(a-ii) What is the risk if pre-provisioning is not done and autoscaling handles it reactively? Think through: what happens to Auth during the 3-minute lag window when traffic is 2× capacity?

---

**(b) SRMI — System Readiness Index**

SRMI = (FLI × OCR × APR/0.85) / (TAF × CC_max/10)

Use current values: FLI=0.72, OCR=0.457, APR=0.31, TAF=0.62, CC_max=10.8.

Note on the formula: APR is normalized by 0.85 (the midpoint between current and target). CC_max is normalized by 10 (the practical maximum where cascade is certain). TAF is in the denominator — high toil growth penalizes readiness.

(b-i) Calculate SRMI.

(b-ii) Interpret the result using the SRMI scale:

| SRMI Range | Readiness Level | Interpretation |
|-----------|----------------|----------------|
| ≥2.0 | Ready | System can absorb a major incident without SLA breach |
| 1.0–1.99 | Marginal | System will handle normal load; major incident would breach SLA |
| 0.50–0.99 | Not Ready | Change freeze recommended; circuit breakers required before high-traffic events |
| <0.50 | Critical | High probability of SLA breach during elevated traffic |

(b-iii) Given SRMI, what is your Black Friday readiness recommendation?

---

**(c) Change queue — what can proceed before Black Friday?**

Two CRs are in queue for next week (6 days before end of month; budget window resets in 12 days):

**CR-1: Auth config update**
- MRI = 2.0 (config change to connection pool size — intended to help Black Friday capacity)
- EBR = min(2.0 × 0.05, 0.80) = 0.10 (10% of budget required in reserve)

**CR-2: Search indexing optimization**
- MRI = 4.0 (code change to Elasticsearch query patterns)
- EBR = min(4.0 × 0.05, 0.80) = 0.20 (20% of budget required in reserve)

Budget remaining = 40%.

(c-i) Can CR-1 proceed? Show: EBR vs. budget_remaining.

(c-ii) If CR-1 proceeds first, budget remaining drops by EBR amount. Can CR-2 then proceed?

(c-iii) Should CR-1 proceed at all, given it is modifying Auth 6 days before Black Friday? Use SRMI and MRI to frame your recommendation. Note: the change is intended to help — but changes that fail make things much worse.

---

**(d) JRCS — Checkout Journey Confidence**

JRCS = SCS × FLI × OCR_path × (1-CC_max/10)

For JRCS, use:
- SCS: Checkout CD=5, all services declaring 99.99%, SLA=99.95% → SCS = 0.9999^5 / 0.9995
- FLI = 0.72
- OCR_path: average OCR of services on the Checkout path (Auth, Cart, Payment, Order Management). From the reference system, their partial credits are: Auth=0.50, Cart=0.75, Payment=1.00, Order Mgmt=0.50. OCR_path = (0.50+0.75+1.00+0.50)/4 = 0.6875
- CC_max = 10.8 → cap at 10 for formula: (1-10/10) = 0

(d-i) Calculate JRCS. Note what happens when CC_max ≥ 10.

(d-ii) What does JRCS=0 mean for the checkout journey on Black Friday? Is the mathematical result telling you the system will definitely fail, or something more nuanced?

(d-iii) What single investment would most improve JRCS before Black Friday? (Look at which factor drives it to zero.)

---

**(e) Black Friday Readiness Report to VP Engineering**

Write 3 bullets: current state, risks, recommendations.

Format requirements:
- Current state bullet: cite SRMI and JRCS values; state plainly whether the system is ready
- Risks bullet: name the top 2 risks with quantified consequences (use BRI or error budget numbers)
- Recommendations bullet: 3 specific actions, each with a "by when" and an "owned by"

This is an executive-facing artifact. No jargon that the VP would not understand. Lead with the conclusion.

---

## Scenario 2: Incident Investigation and Postmortem

At 11 PM on a Tuesday, three alerts fire within 90 seconds of each other:
- Cart Service: p99 latency > 5,000ms (normal: 300ms)
- Payment Service: error rate 15% (normal: 0.1%)
- Search Service: error rate 8% (normal: 0.2%)

No customer-facing alerts have fired yet, but at these error rates they will breach SLA within minutes.

---

**(a) Triage — which service to investigate first?**

Use suspicion_score = SCV × recency_factor to prioritize investigation order.

recency_factor: 1.0 if deployed within 6 hours, 0.7 if deployed within 24 hours, 0.5 if deployed within 72 hours, 0.3 if no recent deployment.

| Service | Last Deployment | SCV | recency_factor | suspicion_score |
|---------|----------------|-----|---------------|----------------|
| Cart | 2 hours ago | 0.30 | 1.0 | ? |
| Payment | No recent change | 0.10 | 0.3 | ? |
| Search | 4 days ago | 0.50 | 0.3 | ? |

(a-i) Calculate suspicion_score for each service.

(a-ii) Which service should be investigated first? Does this match your intuition?

(a-iii) If you are wrong about the first investigation (Cart is not the root cause), what do you check next? Write the decision tree for the first 15 minutes of this incident.

---

**(b) Root cause confirmed — FLI calculation**

Cart Service is confirmed as the root cause. A new deployment introduced a database connection leak that exhausted the connection pool after 2 hours of traffic (which is why the alert fired at 11 PM, 2 hours after the 9 PM deployment).

Cascade analysis:
- Payment Service: has a partial circuit breaker on its Cart dependency (P=0.5). Cart failure → Payment degrades (counts as a cascade failure event)
- Search Service: has no circuit breaker on its Cart dependency (why Search calls Cart: it uses Cart to check item availability for search result ranking). P=0.9. Cart failure → Search fails

Total failure events: Cart (1 original) + Payment (1 cascade) + Search (1 cascade) = 3 total
Contained events: 0 (the original failure cascaded to both dependents)

(b-i) Calculate FLI_incident.

(b-ii) What does FLI_incident = 0 mean? Can FLI ever be 0 in a well-architected system, or does this value indicate a design problem?

---

**(c) BRI calculation**

At the time of the incident:
- 35% of active users were in checkout or cart flows
- Journey criticality = 1.0 (checkout path — highest criticality)
- Cart is P0, tw = 1.0

(c-i) Calculate BRI = (0.35) × 1.0 × 1.0

(c-ii) What SEV level? (Use the BRI/SEV table from Exercise Set 2.)

(c-iii) At this BRI and SEV level, who must be paged? What is the SRE incident commander's first action?

---

**(d) Postmortem — RCR for Cart incidents**

Post-incident analysis reveals that Cart incidents (connection pool issues) occur approximately twice per month.

| Parameter | Value |
|-----------|-------|
| Frequency | 2 incidents/month = 24/year |
| Response | 2 SREs × 90 min each = 3 SRE-hours/incident |
| Fix | Rewrite connection pool management = 120 hours |

(d-i) Calculate RCR = (response_hours × freq_per_year) / fix_hours

(d-ii) Does RCR say fix it or defer? What does the threshold (0.50) mean in plain language?

(d-iii) At 2×/month frequency, how many SRE-hours per year are consumed by this recurring issue?
Annual cost = 24 incidents × 3 hrs = ? hours/year.

Compare to fix cost of 120 hours. How many years of incidents does the fix pay back in the first year?

---

**(e) Circuit breaker proposal — CC and RDR targets**

The proposed fix includes circuit breakers on Payment→Cart and Search→Cart.

Current CC(Cart):
- Payment depends on Cart: P(Payment_fails|Cart_fails) = 0.5 (partial CB already), tw=1.0 → contributes 0.5 × 1.0 = 0.50
- Search depends on Cart: P(Search_fails|Cart_fails) = 0.9 (no CB), tw=0.8 → contributes 0.9 × 0.8 = 0.72

CC(Cart)_current = 0.50 + 0.72 = 1.22

After circuit breakers added to both:
- Payment→Cart: full CB, P drops to 0
- Search→Cart: full CB, P drops to 0

(e-i) Calculate CC(Cart) after circuit breakers.

(e-ii) For the 90-day post-fix review, the team sets a target using RDR:
RDR = new_cascade_mode_rate / old_cascade_mode_rate [target <0.10]

Old cascade rate: 2 incidents/month where both Payment and Search cascaded = effectively 4 cascade events/month (2 per incident).

Target: RDR < 0.10 means new cascade rate should be less than 10% of old cascade rate.

New cascade event target = 0.10 × 4/month = 0.4 cascade events/month.

Is this achievable if the circuit breakers work correctly? What scenario would still generate cascades despite full circuit breakers?

---

## Scenario 3: New Service Integration

The product team wants to add a "Loyalty Points" service to the Checkout journey. It would sit between Payment (hop 4) and Order Management (hop 5). Requirements as submitted:
- Loyalty Points calls Auth (P0, tw=1.0) and a third-party loyalty API (treat as P2, tw=0.5)
- 70% test coverage
- Team wants a 6-hour canary deployment
- Declared SLO: 99.99%

---

**(a) New Checkout CD and Required_SLO**

Current Checkout chain: Auth → Cart → Pricing → Payment → Order Management (CD=5)
Proposed chain: Auth → Cart → Pricing → Payment → **Loyalty Points** → Order Management (CD=6)

(a-i) What is the new CD?

(a-ii) Apply Required_SLO = SLA^(1/CD) = 0.9995^(1/6)

What per-service SLO must Loyalty Points (and every other service) maintain?

(a-iii) Loyalty Points is declaring 99.99%. Is this above or below Required_SLO? What is the margin?

---

**(b) GEI — Gateway Entry Integration Score**

GEI = (new_deps × avg_tier_weight) / (test_coverage × canary_hours)

Loyalty Points is new and has 2 dependencies:
- Auth (P0, tw=1.0)
- Third-party loyalty API (P2, tw=0.5)

new_deps = 2
avg_tier_weight = (1.0 + 0.5) / 2 = 0.75
test_coverage = 0.70 (70%)
canary_hours = 6

(b-i) Calculate GEI.

(b-ii) Using the GEI risk scale:

| GEI Range | Integration Risk | Requirement |
|-----------|----------------|-------------|
| 0–0.25 | Low | Standard integration review |
| 0.25–0.50 | Moderate | SRE review + runbook required |
| 0.50–1.0 | High | Extended canary (24+ hrs), circuit breaker required |
| >1.0 | Very High | Phased rollout only; feature flag required |

What risk level? What requirements does this trigger?

(b-iii) The team argues 6 hours is sufficient because the service is simple. What does GEI tell you? What specific concern does the avg_tier_weight highlight?

---

**(c) LBH for the new CD=6 checkout path**

End-to-end p99 budget = 2000ms (unchanged from current Checkout SLA).
Infra overhead = 200ms.

LBH = (2000 - 200) / 6

(c-i) Calculate LBH per service.

(c-ii) Current p99 latencies from the reference system:
- Auth: ~80ms
- Cart: ~120ms
- Pricing: ~200ms
- Payment: ~450ms (PSP dependency)
- Order Management: ~150ms

Each of these must fit within LBH. Which service violates LBH? What are the options?

(c-iii) For Loyalty Points specifically: the third-party loyalty API SLA is 500ms p99. Does Loyalty Points fit within LBH? What must be done if it does not?

---

**(d) SCS with Loyalty Points at 99.99%**

SCS = declared_SLO^CD / customer_SLA

All 6 services declare 99.99% (including Loyalty Points). Customer SLA = 99.95%.

SCS = 0.9999^6 / 0.9995

(d-i) Calculate SCS.

(d-ii) Is it in the acceptable range (0.95–1.10)?

(d-iii) Compare to current SCS (Exercise Set 1 calculated 0.9999^5 / 0.9995). What is the direction of change?

---

**(e) MRI for future Loyalty Points changes**

Once Loyalty Points is deployed, future changes to it will be evaluated with:

MRI = DG × CD × (1-FLI) × (2-OCR_weighted)

Estimate DG(Loyalty Points): it has 2 direct dependencies (Auth, loyalty API) and 0 direct callers that we know of (other than Order Management receiving it in sequence). For the initial deployment: DG ≈ 3.

Use: DG=3, CD=6 (it is now in Checkout), FLI=0.72 (system current), OCR=0.457 (system current).

(e-i) Calculate MRI(Loyalty Points future change).

(e-ii) What approval tier does this require for any future changes to Loyalty Points?

(e-iii) If the team expected "simple service, easy changes," what does MRI tell them about the operational reality of deploying on the Checkout journey?

---

**(f) SRE approval conditions**

Write 3 specific, measurable conditions under which SRE will approve the Loyalty Points integration. For each condition, state:
- The condition (what must be true)
- The formula or metric that verifies it
- The target value required for approval

Structure: "SRE will approve Loyalty Points when: [condition 1], [condition 2], [condition 3]."

Your conditions must address: latency (LBH compliance for Payment and Loyalty Points), canary duration (GEI-driven), and circuit breaker requirement (for the loyalty API dependency).

---

## Scenario 4: Service Decommission

Reviews Service (P3, tw=0.3) is being decommissioned. The architecture docs declare one caller: Product Catalog.

Before decommission, the SRE team runs a 60-day shadow coupling audit using service mesh telemetry.

**Observed traffic over 60 days**:

| Caller | Observed rps |
|--------|-------------|
| Product Catalog | 45 rps |
| Recommendation | 12 rps |
| Search | 8 rps |
| Unknown service | 3 rps |

**Declared callers from architecture docs**: Product Catalog only.

Total observed traffic = 45 + 12 + 8 + 3 = 68 rps
Declared traffic = 45 rps (Product Catalog)

---

**(a) SCI — Shadow Coupling Index**

SCI = (observed_rps - declared_rps) / total_observed_rps

(a-i) Calculate SCI.

(a-ii) Target: SCI must = 0 before decommission is safe. What does SCI > 0 mean for the decommission plan?

(a-iii) Which callers are undeclared? What is the risk if Reviews is decommissioned while these callers are still active?

---

**(b) What must happen before SCI reaches 0?**

List the steps for each undeclared caller:

For Recommendation (12 rps):
- Step 1: Identify which feature in Recommendation is calling Reviews
- Step 2: Determine if the call is critical or vestigial
- Step 3: If critical: implement alternative data source. If vestigial: remove the call and deploy.

For Search (8 rps):
- Similar analysis. Note: Search calls Reviews likely for product rating signals used in ranking.

For Unknown (3 rps):
- This is the highest-risk caller. What process would you follow to identify a service generating 3 rps to Reviews that is not in the architecture docs?

---

**(c) Unknown caller — SRE recommendation at day 5**

You have been investigating the unknown 3 rps caller for 5 days. The traffic is consistent, not declining, and you cannot attribute it to any known service in the mesh. The product team is asking to proceed with the decommission on schedule.

Write SRE's recommendation in 3 sentences:
1. What you know from the data (cite SCI)
2. What the risk is of proceeding (cite specific failure mode)
3. What you recommend (specific action and timeline)

---

**(d) Observation period after SCI=0**

After all callers are identified and migrated, SCI drops to 0. How long must SCI=0 be observed before decommission proceeds?

The framework does not prescribe an exact duration, but you can derive a reasonable answer from:
- Traffic patterns: if the unknown caller was a batch job, what is its maximum recurrence interval?
- Confidence interval: how long must you observe to be statistically confident there are no more hidden callers?
- MTBI reference: Notification has MTBI=22.5 days. A batch job calling Reviews might run monthly.

Write your recommendation for observation duration, with reasoning. The answer is not "forever" — it is a specific, justified duration.

---

*End of Exercise Set 5 — Integrated Scenarios.*

---

## Capstone Completion Checklist

Before considering the capstone complete, verify that you have:

### Exercise Set 1 (Structural Terms)
- [ ] Calculated CD for at least 3 journeys
- [ ] Applied Required_SLO formula in both directions (CD given → SLO required; SLO given → verify sufficiency)
- [ ] Calculated SCS and interpreted both in-range and out-of-range values
- [ ] Applied LBH and identified a specific service that violates it
- [ ] Written an executive brief in Format 1 style

### Exercise Set 2 (Blast Radius)
- [ ] Calculated DG for at least 2 services
- [ ] Calculated BRI and mapped to SEV level
- [ ] Calculated CC before and after circuit breaker changes
- [ ] Calculated FLI for an incident and identified the cascade mechanism
- [ ] Calculated DSA and used it to justify a tier reclassification
- [ ] Written a circuit breaker investment brief

### Exercise Set 3 (Health Signals and Efficiency)
- [ ] Calculated EBV and time-to-breach
- [ ] Calculated APR and the human cost of noise
- [ ] Applied MTBI achievable_SLO and identified a credibility gap
- [ ] Calculated OCR_weighted with partial credit
- [ ] Applied RCR to a multi-item prioritization
- [ ] Calculated TAF by category and identified the driving factor
- [ ] Ranked investments using RIS

### Exercise Set 4 (Change Governance)
- [ ] Calculated SCV for a service with mixed change types
- [ ] Calculated MRI and mapped to an approval tier
- [ ] Calculated CSD and determined deployment strategy
- [ ] Verified a change window against 3×RV
- [ ] Calculated EBR and applied the budget gate
- [ ] Calculated DSS and interpreted the deployment safety signal
- [ ] Completed a full CAB simulation (all formulae applied to one CR)

### Exercise Set 5 (Integrated Scenarios)
- [ ] Applied SRMI to assess Black Friday readiness
- [ ] Applied JRCS to a specific journey
- [ ] Used suspicion_score to triage a multi-service incident
- [ ] Calculated FLI for an incident and traced the cascade mechanism
- [ ] Applied GEI to a new service integration decision
- [ ] Calculated SCI for a decommission safety check
- [ ] Written a VP-level readiness report (3-bullet format)

### Cross-Cutting
- [ ] Every formula has been applied at least once with real numbers
- [ ] No formula has been applied mechanically without interpreting the result
- [ ] At least 3 "should we do this?" questions have been answered with "it depends on [specific metric]" rather than a blanket yes or no
- [ ] At least 1 recommendation has been reversed after calculating the metric (intuition was wrong; the math said otherwise)

---

*This capstone is part of "SRE: The Missing Layer — A Framework for Reliability Engineering." Solutions to all exercises are in a separate solutions file. Do not consult solutions until you have completed each section independently.*
