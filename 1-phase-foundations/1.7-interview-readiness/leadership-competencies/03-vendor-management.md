# Vendor Management: Evaluating, Negotiating, Governing | Director Leadership Track

---

## Why This Separates Directors from ICs (What Interviewers Are Actually Testing)

ICs evaluate tools on technical fit. Directors evaluate tools on business risk over a 3-year horizon. The interview question is never "which observability tool is best" — it is "walk me through a vendor decision where the technical winner was not the right choice, and how you made the call." Directors are also expected to protect the organization from contracts that look fine on day one and become traps by year three. If you cannot name the clauses you always negotiate and explain why, you are presenting as someone who signs what procurement puts in front of them.

The third signal interviewers look for: can this person manage the political dimension? Vendor decisions touch team loyalties, budget lines, and executive relationships. A Director who cannot navigate that without losing engineers or creating shadow IT is not operating at Director level.

---

## The Mental Model: The Three-Horizon Ownership Test

Every vendor decision is actually three simultaneous decisions collapsed into one:

**Horizon 1 (now)**: Does this solve the problem we have today, at a cost we can absorb?
**Horizon 2 (year 2-3)**: Does this decision give us more or less leverage as we scale?
**Horizon 3 (exit)**: When we eventually leave this vendor — and we will — what does that cost?

Most ICs optimize Horizon 1. Most procurement processes optimize Horizon 1 pricing. Directors hold all three simultaneously and make the decision that is acceptable across all three, not optimal at one.

The corollary: the cheapest year-one option is frequently the most expensive three-year option. Your job is to make that visible before the signature, not after.

---

## The Framework in Practice: Build vs. Buy vs. Open Source

### The 5 Questions (In Order — Do Not Skip Ahead)

**Question 1: Is this in our core differentiated value chain?**

If yes — strong bias toward build or open source with internal ownership. You do not outsource your moat. A notification platform that is your product's primary delivery mechanism is not a candidate for full vendor dependency. A time-tracking tool for internal HR absolutely is.

If no — continue to Question 2.

**Question 2: Is the vendor market mature enough to trust?**

Mature means: 5+ years of product investment by the market leader, multiple viable alternatives, established pricing norms, and a community that is not entirely dependent on one company's survival. Kubernetes passed this test around 2019. "AI-native observability" has not passed it yet in 2026.

If immature — bias toward open source foundation, because you will need to extend it regardless of what any vendor claims. If mature — continue.

**Question 3: What does switching cost look like in year 3?**

This question forces you to design your exit before you enter. Map: where does our data live, in what format, how do we get it out, and what breaks in our platform if we remove this tool. Tools that are deeply integrated into your deployment pipeline (Terraform Cloud, for example) have high switching cost. Tools that collect and display data with open APIs have lower switching cost.

High switching cost means the vendor knows it too. Price accordingly in negotiation and protect yourself contractually.

**Question 4: Do we have capacity to build AND maintain this over 3 years?**

Build cost in year 1 is always underestimated by 2-3x. Maintenance cost in years 2-3 is approximately 20-30% of build cost annually, plus the opportunity cost of engineering cycles that are not going toward differentiated work. If your platform team is already at capacity managing EKS, adding a build project for an observability stack is not a build decision — it is a decision to do neither well.

**Question 5: Can we buy and preserve exit rights contractually?**

If yes — buy with strong data portability and termination-for-convenience clauses. If the vendor will not accept these clauses, that is your answer about how they view the relationship and your leverage once you sign.

### The Honest TCO Model

Vendors present TCO comparisons that undercount build cost and overcount operational overhead of their competitors. Run your own model. For each path, add the costs vendors never include:

**Vendor TCO additions:**
- Integration engineering: plan 2-3x the vendor's estimate. Certified integrations are rarely certified for your specific stack version combination.
- New hire onboarding cost per engineer for a proprietary tool versus an open standard.
- Migration cost when you eventually switch. Budget for it now.
- Productivity loss during major upgrades — these are never zero-downtime for the team.
- Features on the roadmap that are promised but not shipped. If you bought the product partly for a Q3 feature, that feature is not in your TCO unless it shipped.

**Build TCO additions:**
- Apply the 3x rule to year-1 estimates without exception.
- Maintenance at 25% of build cost per year.
- Bus-factor risk: if the two engineers who built the internal tool leave, what is the reconstruction cost?
- Opportunity cost of what your best engineers did not build while building this.

**Open source TCO additions:**
- Do not assume free. Assume integration and configuration cost comparable to a mid-tier vendor.
- License change risk is real. HashiCorp's 2023 BSL change for Terraform was not hypothetical — it affected real adoption decisions. Evaluate the governance model of the open source project, not just the current license.
- Community dependency: if the top 3 contributors all work for one company, the project is one acquisition away from a pivot.

### Default Choices by Category

| Category | Default | Override Condition |
|---|---|---|
| Core product delivery logic | Build | Never outsource your differentiated capability |
| Observability (metrics/traces/logs) | Buy or OSS | OSS if you have a dedicated platform team; buy if you don't |
| Security tooling (SAST/DAST/secrets) | Buy | Build only if you are a security product company |
| Authentication/identity | Buy (Okta/Auth0) | Build only at Google-scale or regulatory requirement |
| Internal developer platform | OSS (Backstage) + owned plugins | Buy if you lack platform team capacity entirely |
| CI/CD orchestration | OSS (GitHub Actions, ArgoCD) | Buy if compliance requires vendor-backed support contracts |
| Incident management | Buy (PagerDuty, Incident.io) | Build only if existing tools cannot support your integration pattern |
| Kubernetes distribution | Managed cloud (EKS/GKE/AKS) | Self-manage only for air-gap, regulatory isolation, or extreme cost optimization at scale |

---

## Vendor Evaluation: The Process That Does Not Take 6 Months

### Week 1: Rapid Elimination (Desk Research + 30-Minute Demos)

You cannot evaluate 5 vendors equally. You eliminate to 2-3 in week 1, then evaluate deeply. Eliminate any vendor that hits one of these disqualifiers:

- No reference customer in your vertical at your scale. A Fortune 50 logo is not a reference for a Series B startup.
- Funding situation creates near-term viability risk. Seed-stage for mission-critical tooling is a risk profile most organizations cannot accept.
- Architecture requires your data to leave your environment when you have residency requirements. This is not negotiable.
- No API for the operations you need to automate. A tool your SREs cannot script around is a tool that becomes a bottleneck.
- Everything requires professional services to configure. You are buying a product, not a consulting engagement.

### The 10-Question Scorecard for Any SRE Tool

Use this for deep evaluation after rapid elimination. Score 1-5 on each dimension. Any score of 1 is a disqualifier unless formally documented.

**1. Technical Fit (weight: 30% for observability, 25% for security)**
Does the product do what we need it to do today, without workarounds that create maintenance burden?

**2. Operational Reliability**
What is their actual uptime over 24 months (not committed — actual)? Walk me through your last major outage. How long did it take to acknowledge? To resolve? What was the communication?

**3. Security and Compliance Posture**
SOC2 Type II current? ISO 27001? When was the last penetration test and can we see the summary under NDA? What is the CVE patch SLA for critical vulnerabilities?

**4. Data Architecture and Portability**
Where does our data go? Who can access it? What is the export format, and can we get everything out at end of contract at no additional cost?

**5. Commercial Reasonableness**
Is the pricing model transparent? Do we understand exactly what triggers overage charges? Are year-2 and year-3 rates committed in writing?

**6. Vendor Viability**
Funding stage, runway estimate, acquisition risk profile. Is this vendor likely to be acquired or shut down before our contract expires?

**7. Integration Completeness**
What can NOT be done via API? This is the question vendors hate, which is exactly why you ask it. What integrations are certified versus community-maintained versus aspirational?

**8. Support Quality**
How is P1 defined, and is it our definition or theirs? What does P1 response actually mean — an acknowledgment email or a named human engineer beginning active investigation? At what contract size do we get a named CSM?

**9. Roadmap Credibility**
Show me your roadmap from 12 months ago. What shipped? What slipped? The gap between promised and delivered is more predictive than the current roadmap.

**10. Team and Adoption Risk**
Will our SRE team actually use this tool, or will it sit at 20% adoption because the workflow is wrong for their practice? The most expensive tool is the one your team routes around.

### Reference Checks: The 3 Questions That Expose Vendor Weaknesses

Do not ask if they are happy with the product. Ask these:

**Question 1:** "Walk me through your last P1 incident involving this vendor. How long did it take them to acknowledge? How long to resolve? What was their communication like during the incident?"

Vendor behavior under pressure is the most predictive signal you have. Happy-path performance is table stakes.

**Question 2:** "When did they last raise your price, and by how much? Did you feel you received value for it, or did you feel held hostage?"

Renewal behavior reveals the real commercial relationship. Vendors who treat customers fairly at renewal are vendors worth keeping.

**Question 3:** "If you were evaluating this again today, would you choose them? If yes, what would give you pause? If no, what would it take to stay?"

The hesitation in answering this question is the answer. Reference customers who have not thought critically about this have not been tested.

Always ask for: one reference who went through a P1 incident with the vendor. One reference who negotiated a renewal. These two calls are worth more than ten happy-customer calls.

### Proof of Concept Design: What to Test, What to Ignore

**The fundamental rule:** The POC must run against real or real-representative data. Synthetic data does not have the cardinality, edge cases, or traffic patterns of production. Vendor performance claims on synthetic data are marketing, not engineering.

**Write success criteria before the POC starts.** Not after. Criteria defined post-POC are shaped by what the vendor demonstrated, not by what you actually need.

Example POC success criteria for an observability tool on a 25M msg/day platform:

```
1. Ingest rate: sustain 300K events/sec without data loss for 4 continuous hours
2. Query latency: trace correlation across 8 service hops returns in < 10 seconds
   at 30 days of data
3. Alert fidelity: detect a 5% error rate increase within 3 minutes with < 5%
   false positive rate on the prior 7-day baseline
4. Integration: complete Kafka consumer lag integration without professional services
   in < 2 business days
5. Usability: an SRE with no prior exposure builds a functional SLO dashboard in < 2 hours
```

Pass/fail is binary per criterion. Partial credit only if accepted by stakeholders before the POC ends, in writing.

**What to ignore during the POC:** their demo dashboard, the marketing case study, any feature that is promised for next quarter rather than available today, and any benchmark that was not run on your data.

### Evaluating AI Vendors Specifically

The AI tooling market in 2025-2026 has vendors for every category claiming AI-native differentiation. The evaluation framework that applies to observability or security vendors still applies, plus these specific probes:

**Model transparency:** "What was your model trained on? Is it a general-purpose foundation model or domain-specific? What is the validation dataset?" A general LLM claiming observability-specific anomaly detection is a marketing claim, not an engineering claim.

**False positive rate in production:** AI alert systems with high false positive rates train humans to ignore alerts. This is measurably worse than no AI. Ask for false positive rate data from production deployments at scale, not lab benchmarks.

**Explainability:** "AI detected anomaly" is not operationally useful if you cannot see why. Explainability is not optional for SRE tooling. The on-call engineer at 2am needs to understand the reasoning, not just the conclusion.

**Feedback loop design:** Does operator feedback (this was a false positive; this alert was correct) train the model? How often is the model retrained? Who triggers retraining when traffic patterns shift significantly?

**Data privacy architecture:** Where does your data go for model inference? Is inference happening on-premises, in your VPC, or in the vendor's shared cloud? For sensitive operational data, this is a compliance question, not just a preference.

**Pricing model for AI features:** AI features are frequently consumption-priced in ways that become nonlinear at scale. Get the exact pricing formula for AI feature consumption at your data volumes before signing.

---

## Contract Negotiation: The 5 Clauses Directors Always Get

### The Sequence: Terms Before Price

Never negotiate price and contract terms simultaneously. Start with terms — frame them as legal and compliance requirements, not preferences. "Our legal team requires X" removes the negotiation from the commercial team and puts it where it belongs: as a contractual baseline, not a line item to trade.

Then anchor on price at 25-30% below list. Not because you expect that price, but because anchoring forces the vendor further down than they planned.

### Clause 1: SLA With Real Teeth

The default vendor SLA is written to protect the vendor. "99.9% uptime with credits up to 10% of monthly fees" sounds meaningful until you calculate it. On a $1.2M/year contract, a 10% monthly credit is $10,000 for an 8-hour outage. Calculate what 8 hours of downtime costs your platform and compare.

What to negotiate:
- SLA definition: "availability" means your users can use the product, not "our infrastructure shows green." This distinction matters enormously for multi-tenant SaaS where their infrastructure is up but your tenant is degraded.
- Credit percentage: push for 25-50% of monthly fee per breach, not 10%.
- Automatic credit trigger: you should not have to file a ticket to claim SLA credits. Automatic credit on breach removes vendor friction from the compensation process.
- P1 definition must be jointly defined, not vendor-unilateral.
- Read every exclusion clause. "Force majeure" and "customer-caused" are often broad enough to cover most real incidents. Push back on any exclusion that could plausibly apply to a realistic failure scenario.

### Clause 2: Data Portability

"Upon termination or expiration, Vendor shall provide a complete export of all Customer data in [CSV/JSON/open format] within 30 days at no additional charge. Export shall include all configurations, historical data for the full contractual retention period, and all metadata required to reconstruct the operational state."

The trap to close: vendors often offer export at an additional cost, or exclude historical data beyond 12 months from base export. If you have a 24-month retention contract and discover 13-24 month export costs $40K, you are paying a hostage fee. Close this gap in the contract, not at exit.

### Clause 3: Price Lock With Cap

"Annual price increases shall not exceed the lesser of 5% or CPI for the contract term. Any increase requires 90-day written notice."

Multi-year commitments without price caps are not multi-year commitments — they are multi-year revenue guarantees for the vendor. Year-2 and year-3 pricing must appear in the contract as specific numbers or a specific formula, not "subject to prevailing rates."

### Clause 4: No Auto-Renewal Without Affirmative Action

"This agreement shall not auto-renew unless Customer provides written confirmation at least [45] days before expiration. Auto-renewal shall not be triggered by inaction."

The trap: vendor sends the renewal invoice to Finance. Finance pays it as a recurring vendor. You discover 60 days after the fact that you are committed to another year at full price. Set a calendar reminder 120 days before every contract end date. Your contract register — even if it is a spreadsheet — must track auto-renewal opt-out deadlines.

### Clause 5: Termination for Convenience

"Customer may terminate this agreement with 30 days written notice. In multi-year agreements, Customer owes fees only through the termination date, not the full remaining term."

Vendors will resist this clause. The negotiation trade is: they get termination-for-convenience protection in exchange for a stronger price commitment or an enhanced SLA. Frame it: "We are committing to a 3-year term. In exchange for that commitment, we need the right to exit if the product materially fails to meet our needs. That is reasonable risk management, not a commitment to leave."

### Pricing Leverage: When You Have It and How to Create It

**Your leverage is highest:**
- Before signature — this is the only leverage window that is always available
- Q4 for calendar-year vendors (AE quota pressure is real)
- When you have two viable alternatives and the vendor knows it
- When you are a reference customer they want — logo value, vertical credibility, speaking opportunity

**Your leverage is lowest:**
- After signature and deep integration
- During mid-migration when you need an extension
- In a single-vendor situation with no credible alternative

**How to create leverage when you have none:**
Run a competitive evaluation — not necessarily to switch, but to have a real quote from a competitor. Even a quote creates leverage. "We are making sure our stack is right for the next 3 years" is a true statement that signals competition without misrepresentation.

### Common Negotiation Trades

| You Give | You Get |
|---|---|
| 2 or 3-year commitment | Year-over-year price cap at CPI or hard percentage |
| Case study and reference call rights | 5-10% discount |
| Annual prepay instead of monthly | 5-8% discount |
| Named logo on their website | Upgraded support tier at no additional cost |
| Beta program participation | Roadmap influence and early feature access |

---

## Vendor Relationship Management

### The QBR That Gets Real Information

Most QBRs are vendor presentations. The agenda is theirs, the data is theirs, and you leave with a roadmap slide and no actionable information. Flip the agenda:

```
QBR Agenda — [Vendor Name] — Q[X] [Year]

Block 1: We present (30 minutes)
  - How we use the product today versus 12 months ago
  - Incidents and operational impact — data, not anecdote. Bring numbers.
  - Features we rely on most; features we pay for but never use
  - Our platform roadmap for the next 12 months and where we need the vendor to grow

Block 2: Vendor responds (20 minutes)
  - Response to our incident data — not defense, response
  - Roadmap alignment: what on our list ships in the next 2 quarters?
  - Honest answer on gaps — what is not on the roadmap and why

Block 3: Joint commitments (20 minutes)
  - Specific product commitments from vendor with dates (write them down during the meeting)
  - Our commitments — beta participation, reference calls, feedback sessions
  - Escalation path review — confirm current contacts and escalation triggers

Block 4: Renewal framing (10 minutes, for QBRs 6+ months before renewal)
  - "Here is what we would need to see to expand" — sets the anchor early
  - Surface any commercial issues before they become renewal-time surprises
```

The goal is arriving at renewal knowing exactly where you stand on leverage. Surprises at renewal mean you managed the relationship passively.

### The Escalation Path Map

Document this in your internal runbook, not in the vendor's portal:

```
Tier 1: Your on-call to vendor support ticket
  Expected: Response within [SLA tier hours]
  
Tier 2: Your SRE lead to vendor CSM (direct phone/Slack)
  Trigger: Tier 1 unresponsive within [X hours], or recurring issue pattern
  
Tier 3: You (Director) to vendor Account Executive
  Trigger: Tier 2 unresponsive, P1 in progress beyond [X hours], or
  pattern of failures threatening SLA compliance
  
Tier 4: Your VP/CTO to vendor VP Customer Experience
  Trigger: SLA breach creating business impact, pattern of failures
  over 30-day window, commercial dispute
  
Nuclear: Legal to legal
  Trigger: SLA credits not honored, data breach notification SLA missed,
  contractual violation
```

Directors keep the AE and CSM's cell phone numbers in their contacts. The vendor portal is for tickets. The phone is for when production is down and the ticketing system is also down.

### Managing a Vendor That Is Underperforming Against SLA

**Step 1: Quantify before you escalate.** Pull the incident log. Calculate actual uptime versus committed uptime. Calculate credits owed under the current SLA. This number is your opening statement, not a complaint.

**Step 2: Set the tone in writing before the call.** Email to AE and CSM: "Over the past 90 days, we have experienced [X] incidents totaling [Y hours] of impact. Under our current SLA, we are owed $[Z] in credits. Before our call on [date], I want to ensure we're aligned on the data and that you've had time to review our incident log."

**Step 3: On the call, separate the technical problem from the commercial problem.** "The technical problem is [root cause pattern]. The commercial problem is that the SLA structure is not creating sufficient incentive to resolve the root cause. I need both addressed." Give them a timeline to address each.

**Step 4: Document the outcome.** Follow every vendor conversation with a written summary of what was agreed. "Per our discussion, Vendor X commits to [specific fix] by [date] and will apply $[amount] in SLA credits to our next invoice." This documentation is your leverage at renewal and your protection if you need to exit.

### Renewal Leverage: Building It 6 Months Out

**9 months before renewal:** Run competitive evaluation. Get pricing from 1-2 competitors. Calculate actual migration cost. You now know your true BATNA.

**6 months before renewal:** QBR with renewal framing as described. Signal that you are evaluating without misrepresenting. "We are making sure our platform stack is right for the next 3 years."

**3 months before renewal:** Make an ask larger than your actual need. You want 15% reduction and better SLA? Ask for 25% reduction and SLA plus premium support at no cost. Leave room to land where you actually needed.

**1 month before renewal:** Final negotiation. You have competitive quotes, documented incident history, and stated requirements. If the vendor's fiscal year end aligns, their AE has quota pressure. Use it.

---

## Sunsetting a Vendor

### The Migration Pattern: Not a Cutover, a Traffic Migration

Sunsets fail as single cutover events. Run them as phased traffic migration:

**Phase 1: Parallel Run (weeks 1-6).** New vendor receives all data. Old vendor remains primary for all decisions. Validate that the new vendor produces equivalent output. Do not make production decisions using the new tool yet. Identify every gap — features the old vendor has that the new one does not.

**Phase 2: Selective Primary (weeks 7-12).** New vendor primary for non-critical use cases. Old vendor primary for production alerts and decisions. Team builds operational muscle memory with the new tool. Update all on-call runbooks.

**Phase 3: Primary Swap (week 13).** New vendor primary for all use cases. Old vendor passive/warm standby. Begin 30-day observation window. No rollback after this window unless there is a critical unresolvable failure.

**Phase 4: Decommission (weeks 14-16).** Export all historical data before shutdown — every organization that skips this step regrets it 18 months later during a compliance review or post-incident investigation. Store in cold storage (S3 with lifecycle policy) for the contractual retention period. Cancel subscription explicitly and confirm in writing. Remove agents and collectors from production systems.

### Communication Timing and Scripts

**To the vendor (3 months before intended exit):** "We're conducting a platform review and have decided to consolidate our [observability/security/incident management] tooling. We plan to conclude our use of [Product] at contract end on [date]. We want to ensure a clean exit and are requesting information on the data export process."

Do not give more notice than your contract requires. Early notice gives the vendor time to mobilize retention efforts, which is fine — but it also gives them time to make the offboarding process difficult if they are motivated to do so.

**To your team:** Name the sunk cost explicitly and separate skill from tool. "The dashboards we've built represent years of knowing what to measure. That knowledge transfers. We're rebuilding in the new platform, and the people who built those dashboards are leading the migration because they know the domain best."

Give resistors ownership roles in the migration. The engineer who knows the old tool most deeply is the highest-value migration lead, not an obstacle.

**To stakeholders:** Frame as risk reduction and capability improvement, not cost cutting (even if it is partly cost cutting). "This migration addresses [specific risk: vendor viability, pricing trajectory, technical capability gap] and improves [specific capability]. Timeline is [X weeks], with zero production impact by design."

### When the Vendor Fights Back

Vendors have retention playbooks. When you signal exit, expect: executive escalation (their CRO calling your VP), emergency discounts that somehow appear only when you announce you are leaving, roadmap promises for features you requested 18 months ago that are now "coming in Q2."

**The Director's response:** "I appreciate the engagement. These concessions would have changed our evaluation if they had been available when we raised these issues [X months ago]. At this point, the migration is planned and the team has been committed. If the terms and roadmap had been different 6 months ago, we might be having a different conversation."

The meta-point: retention offers at exit reveal what the vendor could have offered all along. This is information you will use in the next contract negotiation with any vendor.

---

## What Good Looks Like at Director Level

A Director who manages vendors well does the following without being asked:

Maintains a contract register with auto-renewal dates and alerts set 120 days out. Runs a competitive evaluation every 18-24 months for every mission-critical vendor, not to switch but to maintain leverage and market awareness. Holds QBRs where the Director's team presents first and the vendor responds to the Director's data. Knows the SLA credits owed by every vendor in the past 12 months and whether they were collected. Can articulate the exit path from every tool in the stack and the approximate cost of executing it. Enforces a tiered governance model for tool adoption that prevents sprawl without creating a bottleneck. Documents every vendor negotiation outcome in writing within 24 hours of the conversation.

---

## What Bad Looks Like (Anti-Patterns That Derail Directors)

**Signing the vendor's standard contract without red-lining.** This tells you the Director has not done this before or does not understand the 3-year horizon. The standard contract is written by the vendor's legal team to maximize vendor protection.

**Evaluating only in good times.** A Director who has never asked a vendor "walk me through your last major outage" does not know who they are in a relationship with.

**Letting the team make vendor decisions without Director-level commercial oversight.** Engineers pick tools on technical merit. That is correct and appropriate. Commercial terms, lock-in risk, and 3-year TCO require a Director-level lens.

**Avoiding the tool consolidation conversation because it is politically hard.** Tool sprawl compounds. Twelve observability tools at a 200-person company is not a technical problem — it is a leadership problem.

**Treating the roadmap as a delivery commitment.** "It is on the roadmap" is a statement of intent. Building operational dependency on unshipped features is how teams get stranded.

**Losing track of auto-renewal dates.** This is operational negligence at Director level. It is a calendar reminder and a spreadsheet.

---

## Tools and Templates

### RFP Section Structure (Rapid Version for SRE Tools)

```
Section 1: Company and Product (1 page max)
  - Founding year, ownership, funding stage
  - 12-month roadmap: specific, not marketing
  - Reference customer count in your vertical and scale band

Section 2: Technical Architecture
  - System component diagram (actual, not marketing)
  - Data flow: where does our data go, who can access it
  - Multi-tenancy model
  - API completeness: what CANNOT be done via API
  - DR posture: RTO/RPO, last test date

Section 3: Operational Characteristics
  - Actual uptime data: 24 months, not committed SLA
  - Describe your last outage: duration, root cause, customer impact
  - Maintenance window frequency and customer control options
  - Agent/collector resource overhead on monitored hosts

Section 4: Security and Compliance
  - SOC2 Type II, ISO 27001 currency
  - Penetration test frequency and last summary (NDA)
  - Data residency options
  - Breach notification SLA (contractual, not policy)

Section 5: Commercial
  - Pricing formula at our current and 2x scale
  - Overage mechanics: hard cap or surprise bill?
  - Year 2 and year 3 rates in writing
  - What is NOT included in base price

Section 6: References
  - 3 customers: same vertical, similar scale
  - 1 customer who experienced a P1 with the vendor
  - 1 customer who negotiated a renewal
```

### Contract Red Flags Checklist

Before signing any enterprise software contract, verify:

```
[ ] SLA credits are automatic, not request-triggered
[ ] SLA credit percentage is >= 25% of monthly fee for P1 breach
[ ] "Availability" is defined as customer-observable, not infrastructure-observable
[ ] Data export is included at no cost for full retention period
[ ] Annual price increase cap is specified as a number, not "market rates"
[ ] Auto-renewal requires affirmative action, not inaction
[ ] Termination for convenience clause exists for customer
[ ] Change of control clause gives customer termination right on acquisition
[ ] "Force majeure" definition is narrow enough to exclude routine failures
[ ] Subprocessor list is disclosed and change notification is required
[ ] Professional services requirements are identified and scoped before signing
[ ] P1 support definition specifies "human engineer begins investigation" not "ticket acknowledged"
```

### Vendor Scorecard (10-Question, Weighted)

| Dimension | Weight (Obs) | Weight (Sec) | Score (1-5) | Weighted |
|---|---|---|---|---|
| Technical Fit | 30% | 25% | | |
| Operational Reliability | 20% | 15% | | |
| Security/Compliance | 10% | 30% | | |
| Commercial Reasonableness | 20% | 15% | | |
| Vendor Viability | 10% | 10% | | |
| Data Architecture/Portability | 5% | 10% | | |
| Integration Completeness | 5% | — | | |
| Support Quality | 5% | 5% | | |
| Roadmap Credibility | 5% | 5% | | |
| Team Adoption Risk | 5% | 5% | | |
| **Weighted Total** | | | | |

Any dimension scoring 1 requires formal written documentation of why the gap is being accepted. This documentation protects you when the vendor fails on that dimension later.

---

## Decision Matrix: When to Do X vs. Y

| Situation | Do This | Not This |
|---|---|---|
| 5 vendors, all claiming same capability | Eliminate to 2-3 in week 1 on disqualifiers; deep eval remaining | Evaluate all 5 equally; you do not have the cycles |
| Vendor acquisition announced | Invoke change-of-control clause review immediately; negotiate retention terms | Wait to see how it plays out; the leverage window closes |
| Team has strong loyalty to incumbent tool | Give loyal engineers ownership of the migration evaluation | Mandate the new tool without process; creates shadow IT |
| Vendor underperforming against SLA | Quantify credits owed, send written notice, set remediation timeline | Absorb the impact informally; this becomes the new normal |
| Build vs. buy unclear | Run the 5-question framework in order; do not jump to cost comparison | Start with TCO comparison; vendors control TCO narratives |
| Multi-year vs. annual decision | Multi-year only with price cap clause and termination for convenience | Multi-year for price alone without contractual protections |

---

## People Scenarios

### Scenario 1: Your Senior SRE Is an Internal Vendor Advocate

One of your most senior engineers has been cultivated by a vendor's account team. They are now openly advocating for that vendor's position in internal discussions and sharing internal evaluation details with the account team.

**Script:**
"I appreciate your depth on [Vendor X] — that expertise is genuinely valuable and I want to use it. I need to set one boundary: all commercial conversations — pricing, terms, renewal positioning — go through me. If [Vendor X] starts a commercial conversation with you, route it to me the same day. That is not about limiting your relationship with them. It is about making sure our negotiating position stays coherent. Your technical assessment of their product is exactly what I want from you. The commercial piece is mine."

Then use the relationship. The engineer with a strong vendor relationship often has escalation access that bypasses normal support queues. That is an operational asset.

### Scenario 2: Executive Is Pushing a Vendor You Have Not Evaluated

Your CTO attended a conference and is enthusiastic about a vendor. They have implied that you should move forward with evaluation. The vendor has reached out saying "your CTO suggested we connect."

**Script to CTO:**
"I'm glad [Vendor X] is on your radar — I'll prioritize getting them into our evaluation cycle. To make sure we do this right and protect us commercially, I want to run them through our standard evaluation process. It will take 4-6 weeks. Should I keep you posted on what we find, or would you prefer to be briefed at the end?"

You have validated the CTO's interest, framed the evaluation as due diligence protection (not resistance), and bought the time you need to evaluate without political pressure compressing the process.

### Scenario 3: Team Resisting a Vendor Sunset

You have made the decision to sunset a tool the team has used for 3 years. The team's objections are real: dashboards represent years of work, the new tool has a known gap in one area, and three engineers have certifications in the old tool that will be worth less.

**Script:**
"I hear three separate concerns. The first is the dashboard investment — that work represents our institutional knowledge of what matters operationally, and I do not want to lose that. You are leading the migration of those dashboards because you know them best. The second is the [specific capability gap] — that is a legitimate technical gap, and I want you to document it precisely so we can track when the new tool closes it and hold the vendor accountable. The third is the certifications — those skills are portable across tools in the same domain, and I would support adding [new tool certification] to your development plan."

You have named each concern separately, given ownership to the resistors, and documented the gap so it becomes a vendor accountability item rather than an unresolved objection.

---

## How to Talk About This in Interviews

### What Interviewers Are Actually Asking

When they ask "tell me about a vendor decision you made," they are testing: did you evaluate rigorously, did you negotiate commercially, did you manage the relationship over time, and did you protect the organization from lock-in. They are not testing product knowledge.

### Phrases That Signal Director-Level Thinking

"We ran a parallel evaluation against two vendors, and the technical winner was not the right choice because of the lock-in profile at our scale."

"I always negotiate data portability and a price cap before anything else. Price is secondary to terms."

"At renewal, I came in with 12 months of incident data and credit calculations. The negotiation was factual, not emotional."

"We moved through the POC with written success criteria defined before the POC started. That protected both sides."

"The QBR I run has the vendor responding to our data, not presenting their data to us."

### Phrases to Avoid

"We went with the industry standard" — this signals you followed, not decided.
"The team preferred X" — this signals the decision was delegated.
"We evaluated their demo and it looked good" — this signals no rigor.
"The pricing was competitive" — this signals year-1 thinking, not 3-year thinking.

### STAR Frame (T-Mobile Anchor)

**Situation:** Managing observability tooling for a 25M msg/day notification platform, evaluating whether to expand with primary vendor or consolidate with a newer entrant.

**Task:** Evaluate 3 vendors, negotiate a commercially sound contract, and maintain zero-downtime operations through the transition.

**Action:** Ran a 6-week evaluation using a weighted scorecard. Defined POC success criteria before the POC started. Asked each reference for a P1 incident story and a renewal experience story. Negotiated a 3-year contract with a 5% annual price cap, automatic SLA credits at 30% of monthly fee per breach, and explicit data portability language covering the full retention period.

**Result:** Selected a vendor that scored lower on year-1 pricing but significantly higher on reliability history and commercial terms. 18 months later, when the alternative vendor was acquired by a PE firm, we had no exposure.

---

## T-Mobile Anchors

Your 21 years contain the raw material for every vendor scenario in this module. The framing work is naming what you have already done:

**The 36-month zero-Sev1 record** is the output of operational discipline — which includes the observability tooling decisions that made it possible. Frame your tooling decisions as contributors to that record.

**The 25M msg/day platform** is the scale context that makes your vendor evaluations credible at Director interviews. When you say "we evaluated the pricing model at our event volume," you are speaking from real operational scale.

**The 6 zero-downtime migrations** are vendor sunset stories waiting to be told. Each migration had a parallel run period, a primary swap moment, and a decommission step. Name the pattern.

**The 15-person team** gave you the people scenarios — engineers with deep tool expertise who needed to be managed through transitions, vendors who cultivated internal champions, and the political work of consolidating tooling across a team with strong technical opinions.

If you have evaluated an observability vendor (AppDynamics, Grafana, Splunk), an incident management tool (PagerDuty, VictorOps), or any infrastructure vendor contract — those are your STAR stories. The negotiation details may be under NDA but the decision framework and outcome are yours to tell.

---

## Drills

**Drill 1: The Vendor Evaluation Simulation**
Prompt Claude with: "I'm evaluating three observability vendors for a 25M msg/day Kubernetes-based notification platform. The vendors are Datadog, Grafana Cloud, and Honeycomb. Run me through the 10-question scorecard for each, and help me design a POC with written success criteria. Push back on any criteria that is too vague to be testable."

**Drill 2: The Negotiation Role-Play**
Prompt Claude with: "Play the role of a Datadog account executive. I am negotiating a 2-year renewal for a $400K/year contract. I want a 15% price reduction, a 5% annual cap, automatic SLA credits at 30% of monthly fee, and explicit data portability language. Push back the way a real AE would, and I will practice the Director negotiation responses."

**Drill 3: The Build vs. Buy Decision**
Prompt Claude with: "We are considering building an internal incident management tool versus buying PagerDuty. We have a 6-person platform team, 200 microservices, and strong Kafka/Python expertise. Run me through the 5-question build vs. buy framework and give me the honest TCO model for both paths, including the costs that are typically undercounted."
