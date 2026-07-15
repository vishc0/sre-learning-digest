# Module 10: Stability, Risk, and Operational Governance | Director Leadership Track

---

## Why This Separates Directors from ICs (What Interviewers Are Actually Testing)

ICs manage incidents. Directors own the system that prevents them. ICs follow change process. Directors design it. ICs report SLO numbers. Directors use those numbers to make business decisions and have budget conversations.

When interviewers probe this domain at Director level, they are asking one question beneath all the surface questions: "Does this person have organizational risk ownership, or do they still think of reliability as a technical problem?" The answer is visible in every answer you give — whether you say "we had an outage" or "I owned the postmortem review and here is what changed in our process as a result."

---

## The Mental Model: The Three-Layer Ownership Stack

Name this framework. Use it in interviews. It maps every concept in this module.

```
Layer 3: STRATEGIC      — Stability as competitive moat (board, CTO, VP level)
Layer 2: ORGANIZATIONAL — Policy, process, cross-team agreements (Director level)
Layer 1: OPERATIONAL    — SLOs, error budgets, on-call, metrics (IC/Manager level)
```

Most ICs live in Layer 1. Strong senior managers reach Layer 2. Directors must operate across all three simultaneously — and know which layer a given conversation requires.

The most common Director failure mode: staying in Layer 1 during a Layer 2 or 3 conversation. Presenting MTTR numbers to a CTO who wants to know what the outage cost the business is a Layer 1 answer to a Layer 3 question.

---

## The Framework in Practice: How Directors Actually Work This

### Step 1 — Make Risk Visible Before It Becomes an Incident

Every risk that lives only in an engineer's head is the Director's personal liability. Every risk that is documented, scored, acknowledged by a VP, and has a mitigation plan is shared organizational risk.

This is not philosophical — it is career protection. If a risk you knew about materializes and you never documented it, that conversation goes badly for you. If you documented it, scored it, escalated it, and the VP chose to accept it, the conversation is: "We accepted this risk in Q3; here is what we are doing now."

### Step 2 — Design the Process, Do Not Run the Process

The change management anti-pattern: a Director who approves 80% of changes personally. This creates a bottleneck, trains the team to escalate instead of deciding, and burns the Director's calendar on low-value approvals.

The Director's actual job: design a tier model that makes 85% of changes pre-approvable, defines clear criteria for what requires human review, and puts the Director in the room only for Tier 4 (blast radius = major customer impact or irreversible data change).

### Step 3 — Govern SLO Policy at the Agreement Layer, Not the Metrics Layer

Engineers set the SLOs. Directors govern the policy that determines what happens when SLOs are breached. The policy must be co-signed by the product VP before it is enforced. The first enforcement is the moment the policy becomes real organizational infrastructure. If a Director has never enforced an error budget freeze, they have a document, not a policy.

### Step 4 — During a P1, Be the Communication Layer

The Director is not the most useful technical brain on a P1 bridge. The signal you have gone too technical: engineers are briefing you instead of fixing the problem. Redirect immediately. Your five jobs are: confirm IC and scribe are correct, send executive updates every 30 minutes in plain English, make the rollback call if it needs to be made, absorb VP questions away from the engineering team, and watch the clock for rabbit-holing.

### Step 5 — Close the Loop or It Did Not Happen

Postmortem items that are not tracked by the Director close at approximately 40% within 90 days. Postmortem items that appear on a weekly Director report close at approximately 85% within 90 days. The tracking is the governance. There is no enforcement mechanism more effective than "this item appears on my weekly report until it closes."

---

## What Good Looks Like at Director Level

**On risk:** You have a live risk register. You can speak to your top three open risks in any meeting without referring to a document. You have had the risk appetite conversation with your VP — in writing, with documented decisions. When a risk materializes, the postmortem references the risk register entry. Risk identification is part of your engineering team's routine, not a special activity.

**On change:** Change-induced incident rate is below 35% of P1s. Your CAB meets 30 minutes per week, not 90. Tier 1 and Tier 2 changes are fully self-service with automated gates. You have never personally approved a Tier 2 change in the past 6 months. Freeze periods are published 6 weeks in advance and are never a surprise to product teams.

**On SLO governance:** Product VPs know their team's error budget balance. You have enforced at least one error budget freeze — and came to that conversation with an alternate shipping timeline, not just a "no." SLO policy is a shared OKR item, not an SRE-owned metric. Quarterly SLO review has standing attendees including at least one product VP.

**On incident governance:** You receive P1 notifications and join the bridge to confirm structure — then step back unless escalation is needed. Every P1 has a postmortem. Every postmortem has owner-assigned action items. Action items are tracked to closure. You can tell an interviewer: "Our MTTR trend over the last 4 quarters was..." with specific numbers.

**On audit readiness:** Evidence collection is part of normal operations. Access reviews happen quarterly without a scramble. The team knows three rules for auditor interaction. You have a named audit coordinator who is not you.

---

## What Bad Looks Like (Anti-Patterns That Derail Director Careers)

**Risk theater**: A risk register that is updated before board reviews and never touched otherwise. Risk items that never get closed or escalated. No documented risk appetite. Directors who say "we have a risk register" but cannot quote what is on it.

**CAB as rubber stamp**: A change advisory board where every change passes because rejection is socially difficult. High change-induced incident rate ignored because "we are moving fast." No change metrics. Directors who have never sent a change back.

**SLO policy without teeth**: Error budget policy that has exceptions for every major product launch. Product teams who have learned that the freeze policy negotiates. Directors who present SLO data to engineers but never use it in conversations with product VPs.

**Incident debugging Directors**: Directors who join P1 bridges and start asking "have you tried X?" This takes engineers off-task, signals distrust in the IC, and creates a culture where P1s escalate to Director immediately because the team expects the Director to lead technical resolution. The pattern compounds: engineers stop developing IC skills because the Director fills the role.

**Firefighting as identity**: Directors who measure their value by how many incidents they have personally resolved. This is the clearest signal to a hiring committee that the candidate has not made the leadership transition. The Director's reliability metric is: incidents are resolved without the Director, and the number of incidents is declining.

**Audit sprints**: A team that works 60-hour weeks assembling evidence before every audit. This means normal operations do not produce compliance artifacts. The audit exposes the gap between what the team claims their process is and what actually happens.

---

## Tools and Templates

### Template 1: Risk Register (Director-Maintained)

```
RISK REGISTER — [Platform Name]
Last updated: [Date] | Owner: [Director Name]
Risk Appetite Statement: We accept innovation and delivery risk. We do not accept 
compliance risk, data integrity risk, or risks that create customer-visible outages 
exceeding [X] minutes without documented VP acceptance.

SCORING: Likelihood (1-5) × Impact (1-5)
  Score 1-4:   Accept — monitor quarterly
  Score 5-8:   Mitigate — 90-day remediation plan required
  Score 9-15:  VP escalation — Director + VP agree on mitigation or acceptance
  Score 16-25: CTO/Immediate — escalate within 5 business days

ID     | Category     | Description                           | L | I | Score | Owner     | Mitigation                          | Status     | VP Acknowledged
-------|--------------|---------------------------------------|---|---|-------|-----------|-------------------------------------|------------|----------------
R-001  | Availability | Single-region database, no failover   | 3 | 5 | 15    | [Eng Lead] | Multi-AZ RDS migration Q3           | In Progress | Yes — [VP Name] [Date]
R-002  | People       | Only one engineer knows Kafka config  | 4 | 4 | 16    | [Manager]  | Runbook + cross-train by [Date]     | Open       | Escalation pending
R-003  | Security     | 3 P1 CVEs > 30 days unpatched         | 3 | 5 | 15    | [SRE Lead] | Patching sprint starts [Date]       | In Progress | Yes — [CISO] [Date]
R-004  | Dependency   | Third-party API no SLA contract       | 3 | 3 | 9     | [Director] | Contract renewal in Q2 — add SLA    | Monitoring | N/A
R-005  | Compliance   | Access review overdue 45 days         | 5 | 4 | 20    | [Director] | Access review scheduled [Date]      | Active     | Yes — [CISO] [Date]

RESIDUAL RISK STATEMENT:
After current mitigations, the following risks remain accepted by VP [Name] as of [Date]:
- [R-001]: Single-region risk until Q3 completion. Customer impact potential: up to 4hr outage.
- [R-004]: Dependency risk accepted pending Q2 contract cycle.
```

### Template 2: Change Tier Policy (Director-Published)

```
CHANGE GOVERNANCE POLICY — [Platform Name]
Version: 1.0 | Owner: Director of SRE | Effective: [Date]

TIER 0 — EMERGENCY CHANGE
Definition: Active P1 incident, rollback or hotfix required immediately
Authorization: IC (Incident Commander) on the bridge
Process: Execute first, document within 2 hours, no pre-approval required
Retrospective: Mandatory postmortem includes change review section
Director involvement: Notification only; join bridge if >30 min duration

TIER 1 — PRE-APPROVED CHANGE
Definition: Change matches pre-approved template; automated testing gate passes
Examples: Dependency version bumps with green CI, config flag toggles, scaling adjustments within bounds
Authorization: Automated gate (green CI + automated test pass)
Lead time: None — self-service
Director involvement: Metrics review only; alert if failure rate >5% this week

TIER 2 — NORMAL CHANGE
Definition: Standard deployment, infrastructure change with known blast radius
Examples: New feature deployments, non-critical infra updates, database index additions
Authorization: Peer review (1 SRE) + SRE lead sign-off
Lead time: 24 hours
Director involvement: Weekly metrics only

TIER 3 — SIGNIFICANT CHANGE
Definition: Cross-team dependencies, stateful changes, changes to critical path
Examples: Database schema changes, API contract changes, shared infrastructure modification
Authorization: CAB review (SRE lead + affected team leads + on-call SRE)
Lead time: 72 hours; submitted to CAB tracking system
Director involvement: CAB chair reviews; Director notified, not required to attend

TIER 4 — MAJOR CHANGE
Definition: Irreversible or major blast radius; customer-visible risk; architecture change
Examples: Data migrations, load balancer changes, primary database changes, new AWS account structures
Authorization: Director sign-off + RFC document + VP awareness
Lead time: 5+ business days
Director involvement: Required. Director reviews RFC, signs off in change system.

FREEZE PERIODS:
Published 6 weeks in advance. Standard freezes: [Holiday blackout dates].
Platform-specific freezes: [High-traffic events — align with product calendar].
Emergency exception process: Director + VP approval; IC takes ownership of risk.

CHANGE METRICS (reviewed weekly by Director):
- Change volume by tier (trend week-over-week)
- Change failure rate by tier (target: <5% Tier 2, <2% Tier 3/4)
- Change-induced P1 rate (target: <35% of all P1s)
- CAB turnaround time (target: <48 hours Tier 3 decision)
```

### Template 3: Director P1 Checklist

```
DIRECTOR P1 CHECKLIST
(Run this mentally in the first 5 minutes of every P1)

PHASE 1 — 0-5 MINUTES (Join bridge, confirm structure)
[ ] Named IC confirmed on bridge? (If not, name one immediately)
[ ] Named scribe confirmed? (Taking timeline notes)
[ ] Severity correct? P1 criteria met? (Do not dilute severity; do not under-declare)
[ ] Cross-team bridge triggered if needed? (Dependencies pulled in?)
[ ] War room link shared in main Slack channel?

PHASE 2 — 0-15 MINUTES (Communication layer)
[ ] First stakeholder update sent? (Template: "P1 declared at [TIME]. Customer impact: [what is broken]. Team is investigating. Next update in 30 minutes.")
[ ] VP notified directly? (Text or Slack DM — do not assume they see the channel)
[ ] Rollback option confirmed with IC? ("Do we have a known-good rollback state? What is rollback time?")
[ ] Step back from technical thread — let IC run the bridge

PHASE 3 — 15-60 MINUTES (30-minute update cadence)
[ ] 30-minute update sent? ("Status: investigating [hypothesis]. No resolution yet. Next update in 30 min.")
[ ] Is the IC still working a single hypothesis or have they branched? (If 20+ minutes on same hypothesis with no progress — prompt the IC to branch)
[ ] Are there any VP/Exec questions landing on the engineering team directly? (Intercept — answer or hold)
[ ] Recovery timeline to business? ("We estimate resolution within [X] hours based on [what we know]")

PHASE 4 — RESOLUTION
[ ] Resolution confirmed by metrics, not by team declaration alone? (SLO or key metric back to baseline)
[ ] Customer impact timeline documented? (Exact start, degradation period, full recovery)
[ ] Postmortem scheduled within 48 hours?
[ ] Recovery time granted to on-call team? (No major changes for 24 hours post-resolution)
[ ] All-clear communication sent to stakeholders?

PHASE 5 — 24-72 HOURS POST-INCIDENT
[ ] Postmortem draft reviewed before team meeting?
[ ] Action items have named owners and dates? (Not "team" or "SRE" — a person's name)
[ ] Action items entered in tracking system?
[ ] Risk register updated if new risk exposed?
[ ] VP summary sent? (3-5 sentences: what happened, customer impact, what changes)
[ ] Incident added to weekly reliability report?

WHAT NOT TO DO:
- Do not ask "have you tried X?" on the bridge — this is IC territory
- Do not make the rollback call without confirming with IC first (they have context you do not)
- Do not send speculative root cause to executives before postmortem confirms
- Do not skip recovery time for the on-call engineer
- Do not let a P1 close without a scheduled postmortem
```

### Template 4: Monthly Reliability Scorecard (Executive Version)

```
PLATFORM RELIABILITY SCORECARD — [Month Year]
Platform: [Name] | Director: [Name] | Prepared for: VP Engineering

CUSTOMER EXPERIENCE SUMMARY
[One sentence. Example: "Customers experienced no service outages this month; 
one 12-minute degraded notification delivery period on [Date]."]

SLO STATUS
Service               | SLO Target | Actual  | Status  | Trend
----------------------|------------|---------|---------|--------
Notification Delivery | 99.95%     | 99.97%  | GREEN   | Stable
API Availability      | 99.9%      | 99.88%  | YELLOW  | Improving
Message Processing    | 99.5%      | 99.72%  | GREEN   | Stable

ERROR BUDGET REMAINING (end of month)
Service               | Monthly Budget | Consumed | Remaining | Policy Trigger
----------------------|----------------|----------|-----------|---------------
Notification Delivery | 21.9 min       | 6 min    | 73%       | None
API Availability      | 43.8 min       | 52 min   | -19%      | Orange zone — reliability sprint active

INCIDENT SUMMARY
P1 incidents this month: [N]
  - Change-induced: [N] ([%] of total — target <35%)
  - Infrastructure failure: [N]
  - Dependency failure: [N]
MTTD this month: [X] minutes (target: <[Y])
MTTR this month: [X] minutes (target: <[Y])
Trend vs. last month: [Better/Worse/Stable]

DEPLOYMENT HEALTH
Deployments this month: [N]
Rollbacks: [N] ([%])
Change failure rate: [%] (target: <5%)

TOP 3 RISKS (current, as of this month)
1. [Risk description — one sentence] — [Mitigation status]
2. [Risk description — one sentence] — [Mitigation status]
3. [Risk description — one sentence] — [Mitigation status]

POSTMORTEM ACTIONS
Open action items from postmortems: [N]
  - On track: [N]
  - Overdue: [N] — [brief description of what is late and why]
Items closed this month: [N]

NEXT MONTH FOCUS
[2-3 bullets: what changes, what reliability work is planned, what risk is being addressed]
```

### Template 5: Compliance Readiness Checklist

```
AUDIT READINESS CHECKLIST
90 days out:
[ ] Audit scope confirmed with compliance team (which controls, which systems)
[ ] Gap assessment complete (what evidence exists vs. what will be requested)
[ ] Evidence tracker document created and shared with audit coordinator
[ ] Audit coordinator named (not the Director — an SRE lead or engineering manager)
[ ] VP briefed on gap areas and remediation timeline

60 days out:
[ ] Access review complete and documented (who has access to what, when reviewed)
[ ] Vulnerability backlog reviewed — P0/P1 CVEs patched or have accepted risk documentation
[ ] Change register current (all Tier 3/4 changes for audit period documented with approvals)
[ ] All postmortems from audit period written and action items tracked
[ ] Runbooks exist and are current for key procedures auditors will ask about

30 days out:
[ ] Evidence packages assembled by control area (access, change, incident, vulnerability)
[ ] Internal walkthrough with team — simulate auditor questions
[ ] Team briefed on three rules: (1) answer only what is asked, (2) do not speculate, (3) be honest about gaps with remediation plan
[ ] Single point of contact designated for auditor requests during audit
[ ] VP briefed on remaining gaps and what documentation exists for accepted risk

During audit:
[ ] All auditor requests routed through designated coordinator
[ ] Director available for escalations but not managing document flow
[ ] No new evidence creation — only existing documentation
[ ] Daily debrief with coordinator on open requests

Six controls Directors must be able to speak to without referring to notes:
1. How access is provisioned and reviewed (frequency, who approves, where documented)
2. How changes are approved (tier model, who signs off on major changes)
3. How incidents are managed and reviewed (IC model, postmortem process)
4. How vulnerabilities are tracked and patched (SLA by severity, who owns)
5. How secrets and credentials are managed (vault, rotation frequency)
6. How the team ensures audit trails (what is logged, where, retention period)
```

---

## Decision Matrix: When to Do X vs Y

| Situation | Do This | Not This | Why |
|---|---|---|---|
| Risk identified by engineer | Document in register, score it, schedule mitigation | Verbally acknowledge, move on | Undocumented risk is Director liability |
| Risk score 9-15 | Escalate to VP within 5 days with mitigation options | Handle internally without VP awareness | VP needs to accept or fund mitigation |
| Change-induced P1 rate hits 45% | Stop Tier 2 pre-approvals, review tier criteria, add gates | Add more CAB meetings | The process is wrong, not the velocity |
| Error budget exhausted | Enforce freeze with alternate timeline | Negotiate exceptions | First enforcement makes policy real |
| P1 bridge, IC has been on one hypothesis 25 minutes | Ask IC directly: "Do you want to branch?" | Suggest technical alternatives yourself | IC maintains bridge control |
| Product VP resists error budget freeze | Enforce with shared OKR reference + alternate timeline | Escalate to CTO as first move | Preserve the VP relationship; show you came with a solution |
| Audit in 30 days, gaps exist | Document accepted risk for gaps, brief VP, prepare gap explanation | Scramble to create evidence | Fake evidence is worse than a gap with a plan |
| Postmortem has a clear human error trigger | Frame as process gap that allowed human error to have impact | Avoid naming the action at all | Blameless means systemic, not invisible |

---

## People Scenarios: Scripts for Difficult Situations

### Scenario 1: Engineer Who Thinks All Change Control Is Bureaucracy

The engineer is not wrong about bad change control. They are wrong about the solution.

Script:
"I hear you — I have worked under change processes that were pure friction with no safety benefit. Here is what I want to know: in the last 6 months, how many of our P1s were change-induced? [Get number.] And what tier were those changes? [Get tier.] If we are seeing failures in Tier 1 or Tier 2, the problem is the gate criteria, not the process. Let us review the criteria together. I will commit to a 30-day review — if the data shows our gates are adding friction without reducing failure rate, we change the gates. What I am not willing to do is remove the gates without data showing they are net negative. Fair?"

This gives them agency in the solution and anchors the conversation to data. It also signals: you are not defending process for process's sake.

### Scenario 2: Product VP Pushing Back on Error Budget Freeze

The VP is in the middle of a product commitment cycle. They see the error budget policy as the SRE team blocking delivery.

Script:
"I want to make sure we are aligned on the same goal here. We both signed the error budget policy in Q1 specifically for this situation. Our API availability budget is exhausted — we have used all of this quarter's downtime allowance already, and the quarter is not over. If we continue deploying features at the current rate and have another incident, we are now borrowing against next quarter. The policy says freeze until budget recovers or we complete the reliability sprint. Here is what I can offer: we can run a two-week reliability sprint starting [date], which gets us back to orange zone, and then your feature release can proceed on [specific date]. That is a [X]-week delay. The alternative — continuing as-is — means we are one bad deploy away from a P1 that delays your roadmap by longer than [X] weeks. Which path do you want?"

Key moves: reference the shared agreement, come with an alternative timeline, frame the cost of the alternative.

### Scenario 3: A Postmortem That Keeps Circling Toward Blame

This happens when someone made a clear mistake and the team is skirting around it.

Script (in the room):
"I want to name what I am noticing. We keep coming back to the fact that [action X] happened. In a blameless postmortem, that is important data — but what we are trying to understand is: what conditions made it possible for [action X] to have the impact it did? If our process had caught this before it reached production, we would not be here. So let us ask: what was missing in the system that would have prevented [action X] from causing a P1? That is the action item. The action item is never a person — it is the guard rail, the review step, the alert, the runbook that was missing."

### Scenario 4: Executive Asking for Root Cause During Active P1

The CTO texts you directly: "What is happening? What is the root cause?"

Script:
"We have [specific customer impact] affecting [scope]. Our team is actively investigating. We have two current hypotheses and are working both in parallel. We have a rollback option ready if needed. I will send you an update in 30 minutes or sooner if we have resolution. Is there anything you need from me right now that is not an update?"

The last question is important — it surfaces whether they need to communicate to their chain and what specifically they need from you.

---

## How to Talk About This in Interviews

### Exact Phrases That Land at Director Level

"I own the risk register — I can tell you right now what our top three open risks are and which ones have VP acceptance."

"The error budget policy we have is not theoretical — I enforced it for the first time in Q3 and that is when it became real. The product VP was not happy in the moment, but after the reliability sprint cleared the budget, the relationship actually improved because we had a shared mechanism instead of a personal argument."

"During P1s my job is to be the communication layer and the decision authority, not the most technical person on the bridge. The signal I watch for is whether the IC is being interrupted by my questions — if they are, I have gone too far into the technical lane."

"I think about change governance in four tiers. The goal is for 85% of changes to be pre-approvable with automated gates, so that human review concentrates on the 15% that actually carry blast radius."

"When I present reliability to executives, I do not show SLO percentages. I show customer minutes of impact and what we changed to prevent the next occurrence. The number they care about is the business impact number."

### What to Avoid

Do not say "we maintain a risk register" — say what is on it.

Do not say "we have an SLO policy" — say when you last enforced it and what happened.

Do not say "I run the CAB" — that signals you are in the process, not above it. Say "I designed the tier model and I review the metrics."

Do not say "blameless postmortems" without explaining how you actually run one — every Director says the phrase. Demonstrate the behavior by describing a specific postmortem you ran.

### STAR Frame: Incident Governance

**Situation**: "We had a P1 in Q2 that exposed a gap in our incident communication process — executive stakeholders were getting updates directly from engineers on the bridge, which was pulling engineers off the investigation."

**Task**: "My job was to fix the communication model without adding overhead during incidents, and to ensure the team trusted I was handling the executive layer so they could focus on resolution."

**Action**: "I implemented a structured stakeholder update template — three sentences every 30 minutes, sent by me, not the IC. I briefed the engineering team: any executive question that lands on you during a P1, forward it to me. I absorbed all executive queries for the next three P1s personally to prove the model worked."

**Result**: "IC mean resolution time dropped by 22% in the subsequent quarter. Post-incident surveys from engineers showed a 40-point NPS improvement on the question 'do you feel supported during incidents.' The CTO noted in a QBR that executive communication during P1s was a strength of the team."

---

## T-Mobile Anchors: How Vishweshwar's Experience Maps

**25M msg/day notification platform = auditable change governance evidence.** Any change governance policy you built for that platform at that scale is Director-level evidence. Name the tier model. Name the change-induced incident rate you achieved. "We reduced change-induced P1s from X% to Y% by implementing a pre-approval tier for dependency bumps with automated test gates" is a complete Director answer.

**Zero Sev1 in 36 months = risk register story.** This does not happen by luck at 25M msg/day. It happens because someone made risk visible and managed it. The story is: what risks were on your register, what did you do to mitigate them, and which VP conversations did you have? The 36-month number is meaningless without the governance story behind it.

**6 zero-downtime migrations = change governance at the Tier 4 level.** A zero-downtime database migration or platform migration is a Tier 4 change with a full RFC, Director sign-off, rehearsal, and rollback plan. Walk through one migration as a change governance story: how did you define success, what was the rollback criteria, who was on the bridge, what was the stakeholder communication.

**15 direct reports onshore/offshore = reliability scorecard translation.** Managing reliability across time zones means the reliability scorecard must communicate without real-time conversation. The executive one-pager you present monthly is the same artifact you used to align offshore leads on priorities without 3am calls.

**SLO/SLI governance for telecom platform.** Telecom has regulatory reliability requirements (FCC, carrier-grade SLAs). If you have had conversations with compliance or legal about reliability commitments, that is the Director-level audit readiness story. Frame it: "We had regulatory reliability commitments for carrier-grade delivery. Here is how I built the governance model that ensured we could demonstrate compliance in any audit."

---

## Drills: Three Practice Exercises

### Drill 1: Risk Register Stress Test

Prompt to use with Claude:
"I am a VP of Engineering at a Series C startup. We have a 12-person SRE team, a single-region production deployment, and we are three months from a SOC 2 Type 2 audit. I am interviewing you for Director of SRE. I want you to walk me through what you would do in the first 60 days to understand and document our risk posture. I will ask follow-up questions and challenge your approach."

What to practice: naming the risk register methodology, explaining the risk appetite conversation, framing audit readiness as a 90-day runway not a 30-day sprint, and presenting residual risk in business language.

### Drill 2: Error Budget Enforcement Role Play

Prompt to use with Claude:
"You are the SRE Director. I am the VP of Product. We are two weeks from launching the highest-priority feature of the year — board-level visibility. Our SRE team has just told me the error budget is exhausted and the change freeze policy kicks in. I do not think this policy should apply to this situation. Play out this conversation with me and push back realistically."

What to practice: referencing the shared agreement without sounding bureaucratic, offering an alternative timeline with specifics, making the business case for reliability as risk mitigation, and not escalating to the CTO as a first move.

### Drill 3: Executive P1 Communication

Prompt to use with Claude:
"Simulate a P1 in progress. Every 5 minutes of simulated time, I will tell you what the IC is reporting. You write the stakeholder update you would send to the CTO and VP of Product — exactly the words, nothing else. Then tell me what Director action you took in that 5-minute window. Start the scenario: a database failover has failed to complete, notification delivery is at 40% of normal volume, and the IC has been working the problem for 15 minutes with no resolution."

What to practice: 3-sentence executive update format, correct framing of uncertainty without speculation, rollback decision trigger, and the specific language that keeps executives informed without flooding engineers with escalations.

---

## Closing Frame: The One Thing That Separates Directors

When everything else is equal between two Director candidates — the technical background, the scale of experience, the leadership polish — the question that separates them is this:

"Tell me about a time you owned a risk that materialized."

The IC answer: "We had an incident and I helped resolve it."

The Director answer: "The risk was documented in our register. We had scored it at a 12. I had escalated it to the VP in Q2 and presented two mitigation options. The VP accepted the risk with a Q4 mitigation commitment. It materialized in Q3. Because the risk was documented and accepted, the postmortem conversation was about accelerating the mitigation timeline, not about who missed what. The mitigation was complete by Q4 as originally planned. That is what owning risk looks like — not preventing every outcome, but ensuring every outcome was a known possibility with a documented response."

That answer gets you to the offer.
