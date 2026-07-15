# Decision-Making Frameworks for Directors | Director Leadership Track

## Why This Separates Directors from ICs (What Interviewers Are Actually Testing)

Interviewers at Director/VP level are not testing whether you know frameworks — every candidate who read a leadership book knows DACI. They are testing whether you have judgment about *when* to use which framework, whether you can make irreversible decisions cleanly when the data is incomplete, and whether you own your wrong calls before your manager finds out. The gap between a Senior Manager and a Director is not seniority — it is the demonstrated ability to operate under ambiguity without requiring upward permission on every decision that carries organizational risk.

At T-Mobile scale (25M msg/day, 15 reports, zero Sev1 in 36 months), you have already been making Director-level decisions. The job now is to name them, frame them, and demonstrate them in 45-minute conversations with VPs who will probe for the failure stories as hard as the win stories.

---

## The Mental Model: The Three-Axis Classifier

Before any framework, before any DACI or 6-pager, every decision gets classified on three axes. This is the habit that separates Directors from Managers — the brief but deliberate pause to categorize before acting.

**Axis 1: Reversibility (Type 1 vs. Type 2)**

| Type | Definition | Examples in SRE | Process Required |
|---|---|---|---|
| Type 1 | One-way door. High or impossible undo cost. | Platform migration, team reorg, vendor contract >12 months, deprecating a product line | Full DACI or 6-pager. Slow down deliberately. |
| Type 2 | Two-way door. Low undo cost. | Feature flag rollout, tooling change, process experiment, contractor hire | Decide in <48 hours. Observe. Adjust. |

The most common Director career derailment is applying Type 1 process to Type 2 decisions. It creates organizational constipation — engineers waiting weeks for approvals on decisions that could be reversed in an afternoon. Your team reads this as either indecisiveness or bureaucratic cover. Either reading is damaging.

The equally dangerous failure: treating a Type 1 decision as Type 2 because you are impatient or politically pressured. Platform migrations that skip proper review, reorgs announced without stakeholder alignment — these are the decisions that surface six months later in your skip-level as "Vishweshwar moved too fast."

**Axis 2: Blast Radius**

```
Team only (5-15 people)
  ↓
Org-level (50-200 people, adjacent teams)
  ↓
Customer-facing (external SLA impact, revenue risk)
  ↓
Regulatory or legal
```

The threshold rule: escalate to one level above your blast radius before acting. If the decision hits customers, your VP knows before you move. If it hits adjacent teams, those team's managers know before you announce. This is not about permission — it is about not surprising people who will need to explain your decision to their stakeholders.

**Axis 3: Cost of Delay (CoD)**

Borrowed from SAFe, used practically as a forcing function:

```
CoD = (Revenue impact + Engineering cost + Opportunity cost) per week of delay
```

If CoD exceeds the decision cost: decide now with 70% information.
If CoD is low: gather one more data point, time-boxed to one week maximum.

Amazon's formulation, which holds at every Director level: most decisions should be made with roughly 70% of the information you wish you had. If you wait for 90%, you are probably being slow. The caveat is Type 1 decisions — those warrant pushing toward 90%. The Director discipline is knowing which type you are in before applying the threshold.

---

## The Four Decision Types Directors Own

Directors make four categories of decisions, and each has different time horizons, stakeholders, and failure modes.

**1. Strategic Decisions**
Platform direction, build-vs-buy-vs-borrow, team charter scope, which technical debt to retire first. These are Type 1 or high-stakes Type 2. They require the 6-pager or at minimum a structured 1-pager with alternatives-rejected. Frequency: monthly. Horizon: 12-18 months.

**2. Operational Decisions**
Incident escalation thresholds, on-call policy changes, deployment freeze windows, capacity planning commitments. Mostly Type 2 but high CoD if delayed. The Director's role here is setting policy, not making individual calls — the failure mode is when Directors stay in individual operational decisions that TLs should own. Frequency: weekly. Horizon: 30-90 days.

**3. People Decisions**
Promotion, PIP, team structure, hiring prioritization, contractor-to-FTE conversion. All Type 1. Every people decision has blast radius into morale, retention, and legal. The failure mode is decision debt — deferring the uncomfortable call (PIP, restructure) because the conversation is hard. If a people decision has been "in progress" for more than three weeks, you are not gathering information — you are avoiding discomfort. Frequency: as they arise. Horizon: permanent until undone.

**4. Vendor and Contract Decisions**
Tooling selection, contract renewals, SLA commitments to upstream providers. Type 1 when contract length exceeds 12 months or switching cost is high. The Director's value add here is the alternatives-rejected section — not the selection itself, but demonstrating that alternatives were genuinely evaluated, not dismissed as strawmen. Frequency: quarterly. Horizon: contract term.

---

## The Framework in Practice

### DACI for Cross-Team Decisions

DACI works. DACI also fails in predictable ways. The failure is always the same: two Approvers, or an undefined Approver.

```
DACI TABLE TEMPLATE

Decision:     [One sentence — what is being decided]
Deadline:     [Hard date — no open-ended review]
Reversibility: Type 1 / Type 2

Role          Person             Obligation
─────────────────────────────────────────────────────────────────────
Driver        [IC or TL]         Owns research, synthesis, and the written artifact
Approver      [One person only]  Makes the final call — cannot be shared
Contributors  [SME 1, SME 2]     Advisory input within 48-72 hour window
Informed      [Stakeholders]     Notified after decision is made, not during
```

The mechanics that matter:

Contributors get a time-boxed window — 48 to 72 hours for non-critical decisions. Their input is advisory. The Approver is not obligated to incorporate every input, but must acknowledge receipt. A common contributor objection is "I wasn't heard." The counter to this is a written acknowledgment of every contributor input with a one-line disposition: "incorporated," "considered but not adopted because X," or "out of scope for this decision."

If your VP and a peer Director both need to approve, you do not have a DACI problem — you have an escalation problem. Surface it explicitly: "I cannot close this at my level because two approvers are required. I need you and [VP2] to align on who owns this, then I'll execute."

**SRE Example — DACI in practice:**

```
Decision:     Adopt OpenTelemetry as the org-wide tracing standard; deprecate
              the existing AppDynamics agent instrumentation on new services.
Deadline:     June 25
Reversibility: Type 2 (new services only; existing services untouched)

Driver:       Staff SRE, Platform team
Approver:     Director of SRE (you)
Contributors: Lead SRE (AppDynamics subject matter), FinOps (cost
              impact), Security (agent approval process)
Informed:     Engineering VPs, AppDynamics vendor CSM
```

### The 1-Pager: Daily Currency at Director Level

The 1-pager is the most-used artifact at Director level. It is not a dumbed-down 6-pager — it is a precision instrument for decisions that are significant but not strategic. Use it for team-level decisions, process changes, tooling selection under $100K, and anything Type 2 with blast radius beyond your immediate team.

```
1-PAGER TEMPLATE

Title:         [Decision name — noun phrase, not question]
Date:          [Decision date, not start date]
Owner:         [Single name — not "the platform team"]
Review by:     [Hard date]
Reversibility: Type 1 / Type 2

CONTEXT (2 sentences)
  Why this decision exists now. What changed or what is breaking.

DECISION (1 sentence)
  What you are choosing. Active voice. No hedging.

ALTERNATIVES REJECTED
  • [Option A]: Rejected because [one-line reason]
  • [Option B]: Rejected because [one-line reason]
  Note: Never list alternatives without rejection reasons. That is a
  list, not a decision record.

RISKS ACCEPTED
  • [Risk 1]: [Likelihood] × [Impact] — mitigated by [specific action]
    or accepted because [explicit reasoning]
  • [Risk 2]: Same format.
  Note: This section is the differentiator. Omitting it signals the
  author hasn't thought the decision through.

SUCCESS METRIC
  How you will know this decision was correct in 30/60/90 days.
  One measurable indicator.

ESCALATION TRIGGER
  What specific event would cause you to reopen this decision.
  State it now so the team knows the threshold.
```

**Filled Example — SRE context:**

```
Title:         Adopt PagerDuty as primary on-call routing; retire
               homegrown Slack-bot alerting
Date:          2026-06-11
Owner:         Vishweshwar Chippa
Review by:     2026-06-18
Reversibility: Type 2 (existing Slack-bot remains operational for 60
               days as fallback)

CONTEXT
  The homegrown Slack-bot alert router has no escalation path and
  no audit trail, creating compliance risk in our quarterly SLA
  reviews. Three P1 alerts in Q1 were acknowledged 12+ minutes late
  due to manual handoffs between onshore and offshore shifts.

DECISION
  Adopt PagerDuty for all on-call routing and escalation on the
  notification platform, effective the July 1 rotation cycle.

ALTERNATIVES REJECTED
  • Extend homegrown bot: Rejected — requires 3 sprint-weeks of
    engineering to add escalation; no audit trail without database
    work; does not solve offshore handoff gap.
  • OpsGenie (Atlassian): Rejected — 18% higher license cost per
    seat; migration complexity given existing Jira integration
    creates double-maintenance for 6 months.

RISKS ACCEPTED
  • Learning curve for offshore team: Accepted. Mitigation: recorded
    30-min onboarding session + PD sandbox environment for 2 weeks
    prior to go-live.
  • Vendor lock-in: Accepted for 12-month contract. Escalation
    trigger: if PagerDuty SLA drops below 99.9% for 2 consecutive
    months, re-evaluate.

SUCCESS METRIC
  Mean time to acknowledge (MTTA) drops from current 12 min to <3
  min within 30 days of go-live. Measured in PagerDuty reports,
  reviewed at next monthly ops review.

ESCALATION TRIGGER
  If MTTA does not improve by 50% within 30 days, or if offshore
  adoption rate is below 80% at day 14, reopen with escalation to
  VP Engineering.
```

### The 6-Pager: For Strategic Decisions Only

Use the 6-pager for: major investments, new program charters, platform migrations, strategic pivots, anything with cross-org blast radius or budget >$500K equivalent impact. Never for operational decisions — applying 6-pager rigor to operational questions is a Director anti-pattern (it signals you cannot calibrate process weight to decision weight).

**Structure:**

1. **Executive Summary** — The decision in one paragraph. Written last, placed first. If reviewers read only this, they should understand what you are deciding, why now, and what you need from them.
2. **Problem Statement** — What breaks or what opportunity is missed if you do not decide. Quantified: latency numbers, cost figures, error rates, team capacity burn.
3. **Goals and Non-Goals** — Non-goals are as important as goals. They prevent scope creep during review. "We are not solving X in this phase" is a gift to reviewers.
4. **Current State** — Narrative with data. Not a slide deck of metrics — a written story of where you are and why the current state is unsustainable or suboptimal.
5. **Proposed Solution with Alternatives** — Your recommendation plus at least two alternatives that were genuinely considered. The alternatives must not be strawmen. VP-level reviewers will identify strawman alternatives immediately, and it terminates your credibility on the document. Each rejected alternative gets a specific, honest rejection reason.
6. **FAQ** — Pre-populate the objections you know are coming. "Won't this require additional headcount?" "What happens if the vendor exits the market?" "Why now instead of after the platform migration?" Answering these before the room asks them is a signal of preparation and political awareness.

The discipline: Section 5's alternatives test your intellectual honesty. If you cannot write a genuinely competitive alternative and explain why you rejected it, you have not done the thinking.

---

## Decision Under Uncertainty: The Pre-Mortem

The pre-mortem is the highest-ROI technique in this module. It takes 20 minutes before a major decision and eliminates the category of failures that come from optimism bias.

**The script:**

```
PRE-MORTEM PROTOCOL

Setup: "Assume it's 12 months from today. This decision failed
       catastrophically. The post-mortem report is being written.
       What are the three most likely causes of failure?"

Step 1: Write three specific failure causes. Not vague — specific.
        Wrong: "The team didn't adopt it."
        Right: "The offshore team in Bangalore did not receive
                structured onboarding. They continued using the old
                process. The migration never reached >60% adoption,
                and we maintained two parallel systems for 18 months
                at double the operational cost."

Step 2: For each cause, answer:
        - Is this cause preventable now? If yes, prevent it or
          change the decision.
        - If not preventable, is it an acceptable risk? If yes,
          name it explicitly in the risks-accepted section.
        - What metric would serve as an early warning?

Step 3: In your presentation of the decision, use this language:
        "We ran a pre-mortem. The three ways this fails are X, Y, Z.
        We are mitigating X through [specific action]. We are
        accepting Y because [explicit reasoning]. We are monitoring Z
        using [specific metric with threshold]."
```

This language pattern does three things in an executive conversation: it signals rigor, it demonstrates you are not blindly optimistic, and it pre-frames the monitoring cadence so your VP is not surprised when you surface early warning signals in your next 1:1.

---

## What Good Looks Like at Director Level

- **Classifies before deciding.** Type 1 or Type 2 is stated explicitly in every written decision record. This habit, visible in your artifacts, signals Director-caliber thinking without you having to claim it.
- **Single Approver, enforced ruthlessly.** Never allows two approvers to coexist in a DACI. Surfaces the ambiguity explicitly and forces resolution upward rather than proceeding with unclear authority.
- **Recommends when escalating.** Every escalation to the VP arrives as "I recommend X, here is my reasoning, here is specifically what I cannot resolve at my level and need you to decide."
- **Names accepted risks explicitly.** Every 1-pager and 6-pager has a risks-accepted section. Omitting it is not confidence — it is incomplete thinking.
- **States escalation triggers at decision time.** Before implementing, declares: "The specific condition that would cause me to reopen this is Y." This prevents endless second-guessing while creating a legitimate re-evaluation path.
- **Comes to the manager before the manager comes to them.** When a decision is going wrong, surfaces it with containment action already scoped. Does not wait to be discovered.
- **Creates decision artifacts.** Decisions are documented. Not as bureaucracy — as organizational memory and credibility signals.

---

## What Bad Looks Like (Anti-Patterns That Derail Directors)

**Failure 1: Escalating questions instead of recommendations.**
"I need your guidance on whether we should migrate to OpenTelemetry" is a manager move. "I recommend we adopt OpenTelemetry for new services in Q3. The decision I cannot resolve at my level is the budget reallocation from the AppDynamics contract — that requires your sign-off with FinOps" is Director behavior. VPs who receive the first pattern long enough begin to make the decisions themselves, which means the Director becomes a project manager.

**Failure 2: Consensus conflation.**
Alignment means stakeholders understand the decision and their role in it. Consensus means everyone agrees. Directors who require consensus on Type 2 decisions are avoiding accountability — if everyone agreed, no one person is accountable when it fails. Seek input. Own the decision. Communicate clearly. Consensus is appropriate only when the decision legitimately cannot proceed without cross-functional commitment (a Type 1 decision with multi-team blast radius).

**Failure 3: Decision debt.**
Any decision that has been on your list for more than two weeks without resolution is not awaiting more information — it is awaiting your willingness to have a hard conversation. People decisions (PIP, structural change, underperformer feedback) accumulate fastest. Directors carrying more than three unresolved decisions for more than two weeks are read as avoidant by their managers and their teams simultaneously.

**Failure 4: Reopening closed decisions without threshold.**
If you stated at decision time what would cause you to revisit, and that condition has not been met, you do not reopen. Directors who re-examine closed decisions every time new information arrives — without a pre-stated threshold — destroy team execution velocity. The team stops trusting that decisions are real.

**Failure 5: Applying Type 1 process to Type 2 decisions.**
The 6-pager review cycle for a tooling change that can be rolled back in four hours. This signals either indecisiveness or bureaucratic self-protection. Both are read as weak by VPs and as friction by engineers.

**Failure 6: Confidence miscalibration in either direction.**
Presenting uncertain decisions as certain destroys credibility on the first wrong call. Excessive hedging on decisions you should own makes VPs feel they are doing your job. The calibrated pattern: "My confidence on outcome is [moderate/high/low]. Here is specifically what I am uncertain about and how I am tracking it."

---

## Tools and Templates

### Decision Log (How Directors Track and Communicate)

```
DECISION LOG — [Team/Platform Name]
Updated: [Date] | Owner: [Director Name]

──────────────────────────────────────────────────────────────────────
ID    Date        Decision                  Type  Status     Review By
──────────────────────────────────────────────────────────────────────
D-01  2026-06-11  PagerDuty adoption        T2    Decided    2026-07-11
D-02  2026-06-03  OTel for new services     T2    In Review  2026-06-18
D-03  2026-05-20  SLO reduction for batch   T1    Decided    2026-08-20
D-04  2026-06-09  TL promotion — [name]     T1    Pending    2026-06-25
──────────────────────────────────────────────────────────────────────

For each row:
- "In Review" = open for contributor input, deadline stated
- "Decided" = closed, documented, escalation trigger on file
- "Pending" = not yet decided; if >2 weeks, flag to self as debt
```

The decision log is shared with your team at a monthly cadence, not hidden. Transparency about what has been decided and what is pending reduces the ambient anxiety of "I don't know what's happening" that accumulates in teams under Directors who decide in private.

### DACI Table Template (Reusable)

```
Decision:      ___________________________________
Decision By:   [Hard date — required field]
Reversibility: Type 1 / Type 2
Approver:      [One person — if empty, decision is not ready to run]

Role           Person(s)          Input Deadline    Notes
─────────────────────────────────────────────────────────────────────
Driver         [name]             N/A               Owns artifact
Approver       [one name]         N/A               Final call
Contributor    [name 1]           [date]            Advisory
Contributor    [name 2]           [date]            Advisory
Informed       [list]             N/A               Post-decision
```

---

## Decision Matrix: When to Use Which Approach

| Situation | Approach | Why |
|---|---|---|
| Team-level, Type 2, <$100K impact | 1-pager, decide in 48 hrs | Low CoD, high reversibility |
| Cross-team, Type 2, 3+ stakeholders | DACI, 1-pager, 72-hr contributor window | Alignment needed, not consensus |
| Strategic, Type 1, budget or platform scope | 6-pager, full DACI, VP review | Irreversible, blast radius requires rigor |
| Operational, recurring, policy-level | Documented policy, not per-incident decision | Eliminate repeated decision-making |
| Incomplete data, high CoD | Decide at 70%, state uncertainty explicitly, monitor | Cost of waiting exceeds cost of being wrong |
| Two approvers exist | Stop. Surface the ambiguity. Force resolution upward | Proceeding with split authority is always worse |
| Decision has been pending >2 weeks | Treat as decision debt, force close this week | You are avoiding discomfort, not awaiting data |

---

## People Scenarios: Scripts for Specific Situations

### Scenario 1: Presenting a Decision to Your VP

```
Structure: Situation → Complication → Resolution → Ask

"Here's where we are: [current state in 2 sentences, quantified].
The complication: [what breaks or what costs accrue if we don't act,
and the weekly CoD].
I'm recommending [specific action, one sentence].
The alternatives I considered were [X] and [Y]. I rejected X because
[reason]. I rejected Y because [reason].
The risks I'm accepting are [A] and [B] — I've mitigated A through
[specific], and I'm monitoring B with [specific metric].
What I need from you: [specific — budget approval, air cover with
team Z, or 'nothing, I'm informing you'].
I'm acting on this [date] unless you direct otherwise."
```

The last line is the critical Director move. It shifts the default from "pending VP approval" to "proceeding unless you stop me." Managers ask for permission. Directors inform and proceed.

### Scenario 2: Your Decision Is Wrong — With Your Manager

```
Come to them before they come to you. Every time, without exception.

"I want to give you a clear picture before you hear this elsewhere.
[Decision] is not producing the outcome I projected.
The specific gap: [metric — was X, projected Y, actual Z].
The assumption that failed: [specific, not vague — 'I assumed
offshore adoption would track onshore adoption curves. It has not,
because the training delivery approach was asynchronous and
synchronous cadence is needed for Bangalore time zone'].
I am already [doing / will complete by Friday] [specific corrective
action].
Updated trajectory: [new estimate, banded — best case X, likely Y,
worst case Z].
What I need from you: [specific ask or 'nothing — I'm informing you
and will update in our next 1:1']."
```

VPs can absorb Directors being wrong. They cannot absorb Directors who are surprised by their own decisions going wrong, or who lead with blame displacement (the data, the team, the timeline). The former is human. The latter is a leadership failure.

### Scenario 3: Your Decision Hurt Your Team

```
To your team, in a team meeting or written communication:

"I made the call on [decision]. The assumptions I was working from
were [X and Y]. What I did not account for well enough was [Z —
specific: the impact on the rotation schedule, the additional
context-switching, the missed OKR].
The cost to the team was [specific — three weekend on-call
escalations, the missed Q2 launch window].
I own that.
Here is what I am changing in how I make similar decisions going
forward: [specific process change — not a platitude].

Example of a process change that lands:
'I'm adding a two-day hold on any commitment I make to external
stakeholders that requires weekend on-call coverage. Before I agree
to any external deliverable date, I will do an explicit capacity
check with the rotation leads.'"

The "specific process change" is non-negotiable. "I'll be more
careful" is not a process change. It is a deflection.
```

### Scenario 4: Pushing Back on Executive Direction

```
"I want to make sure you have my honest read, because that's what
you need from me.
My concern with [directive] is [specific risk, quantified where
possible].
If we proceed, here is what I would want in place to mitigate:
[specific safeguard].
Alternatively, [option B] reaches [same goal] with [lower risk
profile].
You have more context than I do on [the strategic priority /
the political dynamic / the board-level constraint]. If that changes
the calculus, tell me and I'll execute.
Otherwise, my recommendation is [clear statement, one sentence]."
```

This script accomplishes four things simultaneously: demonstrates loyalty (I will execute your call), demonstrates competence (I identified the risk), gives the executive an out, and lands a clear recommendation. It does not require agreement to be effective.

---

## How to Talk About This in Interviews

### Exact Phrases That Signal Director-Level Thinking

- "I classified it as a Type 2 decision, which meant I needed to decide in 48 hours, not 48 days."
- "I ran a pre-mortem before we committed. The three ways it could fail were X, Y, Z. We mitigated X, accepted Y, and put Z on the monitoring dashboard."
- "I brought my VP the recommendation with the risk I was accepting, not just the question. The specific ask I had for him was air cover with the infrastructure team, not the decision itself."
- "We used DACI with a hard 72-hour contributor window and a single approver. I enforced that — we had a contributor who wanted extended review time, and I acknowledged his input in writing and proceeded."
- "When I realized the assumption had failed, I went to my manager before the weekly status update. I led with the specific metric gap and the corrective action already in motion."

### Phrases to Avoid

- "We took it to the team and got everyone aligned" — sounds like consensus, not decision-making.
- "We didn't have enough data to decide at the time" — sounds like you waited for certainty. Frame as: "We made the call at 70% information because the cost of delay was exceeding the risk of being wrong."
- "I escalated it to my VP" — without the recommendation, this sounds like abdication. Always pair with: "I escalated with a recommendation."

### STAR Framing for Decision-Making Questions

The interview question is typically: "Tell me about a time you made a decision with incomplete information and were wrong" or "Tell me about a difficult decision that had significant organizational impact."

```
STAR Template — Director Level

Situation: Set the context in 2 sentences. State the stakes
           quantitatively (msg/day, team size, CoD).

Task:      What specifically you were responsible for deciding.
           Name the decision type (Type 1 / Type 2 framing signals
           sophistication without you having to state it overtly).

Action:    Walk through your classification → framework selection →
           the alternatives you considered and rejected (and why) →
           the risks you named explicitly → how you communicated.
           Include the pre-mortem if you ran one.
           If you were wrong: what you found out, how you surfaced it,
           what the corrective action was, what structural change you
           made.

Result:    Quantified outcome. Then: what you changed in how you make
           similar decisions. The process change is the signal
           interviewers at VP level are listening for — it
           demonstrates you learn systematically, not accidentally.
```

---

## T-Mobile Anchors

Your T-Mobile experience maps directly to each concept. The job is translating what you did into Director vocabulary:

| What you did at T-Mobile | Director vocabulary |
|---|---|
| Zero Sev1 in 36 months | "I set incident escalation thresholds using CoD framing — the weekly cost of running below SLO calibrated our response posture without over-rotating to false positives." |
| 6 zero-downtime migrations | "Each migration was classified as a Type 1 decision. We used 6-pager structure for the three largest, 1-pager for the others. Each included an explicit reversal condition and a pre-mortem." |
| 15 direct reports, offshore + onshore | "The DACI failures I've seen most often involve offshore contributors getting an inadequate window. I standardized on 72-hour windows with asynchronous input mechanisms to account for timezone spread." |
| 25M msg/day platform reliability | "SLO decisions — where to set the threshold, how to respond to burn rate alerts — are recurring operational decisions that I converted to policy. The goal was eliminating per-incident decision-making under pressure." |
| Managing through incidents in real-time | "Incident command at this scale forced me to get fast at the Type 1 vs. Type 2 classification. Almost every in-incident decision is Type 2 — you can roll back, you can try a different path. The Type 1 moment is the customer communication after 15 minutes. That one you slow down for." |

The STAR story that lands best: the 6 zero-downtime migrations. Pick the one with the highest organizational risk (the one where, if it failed, the impact was most visible). Walk through the pre-mortem, the alternatives-rejected section, how you communicated to your manager, and — if there was a moment where the assumptions partially failed — how you surfaced that and corrected.

---

## Drills

**Drill 1 — Decision Classification Practice**

Prompt to use with Claude:
> "Give me 10 decisions a Director of SRE would face in the first 90 days at a Series B startup building from scratch. For each one, I will classify it as Type 1 or Type 2, estimate the CoD, and state which framework I'd use. Push back on any classification that seems off."

Goal: Build the habit of automatic classification. Do this until it takes less than 30 seconds per decision.

**Drill 2 — 1-Pager Speed Drafting**

Prompt to use with Claude:
> "Give me a real SRE decision scenario: a vendor selection, a platform migration, or a team process change. I will write the 1-pager in 15 minutes using the template. You will then evaluate: Is the alternatives-rejected section genuinely competitive or strawmen? Is the risks-accepted section specific or vague? Does the escalation trigger have a measurable threshold?"

Goal: Build the habit of explicit risk-naming and genuine alternatives evaluation. The evaluator role should be adversarial — if the alternatives look like strawmen, say so directly.

**Drill 3 — Interview Simulation on Being Wrong**

Prompt to use with Claude:
> "Ask me the following question as a VP of Engineering conducting a Director-level interview: 'Tell me about a decision you made that turned out to be wrong, and walk me through exactly how you handled it.' After I answer, evaluate: Did I lead with the assumption that failed, or with deflection? Did I state what I would do differently as a specific process change or a platitude? Did the STAR structure include quantified stakes? What is missing from a VP-level answer?"

Goal: The being-wrong story is the highest-signal answer in any Director interview. Rehearse until the specific process change at the end is instinctive and precise.
