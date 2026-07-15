# Strategic Planning, Roadmaps, and OKRs | Director Leadership Track

## Why This Separates Directors from ICs

Interviewers at VP and above are not testing whether you understand roadmaps. They are testing whether you have made real prioritization calls under constraint, communicated strategy to skeptical audiences, and held the line when pushed. An IC who has never owned a budget or defended a roadmap to a CFO will describe planning as a process. A Director describes it as a series of difficult trades. The difference is visible in the first two minutes of an interview answer.

The second thing interviewers are testing: whether you build planning infrastructure that outlives you, or whether you are the single point of failure. A Director who has no roadmap artifact, no OKR discipline, and no quarterly ritual is a Director whose team loses direction the week they go on vacation.

---

## The Mental Model: Three Horizons, Five Inputs, One North Star

The mistake engineers make when stepping into Director roles is treating a roadmap like a project plan — a sequential list of things to do. Platform roadmaps are layered bets across time, not a Gantt chart.

**The Three-Horizon Model**

- **Horizon 1 (0-6 months)**: Committed delivery. Named owners. You keep promises here. If this slips, your credibility slips.
- **Horizon 2 (6-12 months)**: Directional commitment. You have a plan, resources are rough-sized, dependencies are identified. You will defend this publicly but reserve the right to reprioritize.
- **Horizon 3 (12-18 months)**: Strategic intent. No owner yet. This horizon signals to engineers where to build skills, and to product where to make bets. If Horizon 3 does not scare you slightly, you are not thinking ambitiously enough.

**The Five-Input Model**

Every roadmap built from a single source — usually "what product asked for" — fails within two quarters. Directors synthesize five inputs:

1. Business objectives — what does your VP's VP care about this year?
2. Technical debt register — what is currently costing your team 20% of sprint capacity?
3. Incident and reliability data — post-incident action items that never got scheduled; recurring pages; SLO miss trends.
4. Team capability gaps — where is your team behind the market?
5. Platform user feedback — internal engineering teams are customers. Treat them that way.

**The North Star Rule**

Every roadmap needs a single sentence with a single number that everyone on your team can recite without looking. If it takes two sentences, it is not a north star — it is a paragraph. Example: "Reduce time-to-production for new services from 3 weeks to 3 days while maintaining 99.95% reliability."

---

## The Framework in Practice

### Building the Roadmap: Step by Step

**Step 1: Run the five-input survey before opening a slide deck.**

Schedule 30-minute sessions with three tech leads, two product partners, and two dependent-team leads. Ask each: what is breaking, what is too slow, and what are you afraid of in the next 6 months? You are gathering signal, not commitments.

**Step 2: Pull objective data — do not rely on memory.**

Review the last 6 months of incidents. Count recurring failure modes. Calculate what percentage of sprint capacity went to unplanned work. Check SLO trend lines. This data becomes your justification layer for every Horizon 1 item.

**Step 3: Populate Horizon 1 from commitments that already exist.**

Regulatory deadlines, architecture decisions already made, on-call contract improvements your team promised at the last all-hands. These are not new ideas — they are obligations. Slot them first. Whatever capacity remains is what you actually have for new work.

**Step 4: Populate Horizon 2 from the highest-impact, highest-confidence items from your input survey.**

Rough-size each initiative: S (one person, one sprint), M (two people, one quarter), L (a team, two quarters). Do not over-invest in sizing precision at Horizon 2 — you will be wrong. The size is directional, not contractual.

**Step 5: Write the "What We Are Not Doing" section.**

This is the most underrated section of any roadmap. It demonstrates that your list is the result of intentional tradeoffs, not random prioritization. Every item in this section should have a one-line reason: wrong time, wrong team size, already covered by another initiative, not aligned with company direction.

**Step 6: Assign confidence tags.**

High confidence (greater than 80 percent): technical approach is known, staffing is confirmed, dependencies are owned. Medium confidence (50-80 percent): known unknowns exist. Low confidence (less than 50 percent): approach is still being defined or a significant external dependency is unresolved. Present these tags openly — they turn roadmap reviews from debates about dates into productive conversations about what needs to be unblocked.

---

## What Good Looks Like at Director Level

- You can present the roadmap in three different formats in one day: a 15-minute CTO conversation, a 30-minute engineer working session, and a two-paragraph email to a PM — and the content is consistent but the framing is entirely different.
- You have a "What We Are Not Doing" section and you can defend every item in it.
- Your OKRs have baselines. If you do not have a baseline, you do not have a KR — you have an aspiration.
- You run a quarterly planning session with an agenda circulated 48 hours in advance, and the session produces committed owners, not just a list of ideas.
- Your 30-60-90 in a new role is structured around listening, not doing. The first tangible change you make is small, visible, and low-risk — designed to signal how you lead, not to prove how much you know.
- When requirements change mid-roadmap, you notify stakeholders within 72 hours with options, not apologies.

---

## What Bad Looks Like

**Anti-pattern 1: The Project Mindset Director.** Treats the platform as a project with a finish line. Delivers the migration, then argues headcount back down to maintenance mode. The platform degrades. Incidents increase. Two years later they are fighting for resources to fix what was not maintained.

**Anti-pattern 2: The Consensus Roadmap.** Runs a vote on priorities. The loudest engineers win. The roadmap reflects whoever showed up to the planning meeting, not actual business value. When asked to defend a priority, they say "the team decided."

**Anti-pattern 3: The Theater OKR Director.** Writes OKRs like: "Complete 5 runbooks." "Attend 3 SRE conferences." "Publish a reliability dashboard." Hits all three. Nothing improves. Gets surprised when executives question the team's impact at mid-year review.

**Anti-pattern 4: The First-90-Days Executor.** Joins a new role and starts making changes in week two. Offends the engineers who have been managing the technical debt for three years. Breaks trust with the informal leaders the team actually turns to. Has the right answers technically and the wrong approach politically. Gets managed out at 18 months when the organizational friction catches up.

**Anti-pattern 5: The Single-Audience Communicator.** Sends the same roadmap deck to engineers, PMs, and the CFO. Engineers want to know the technical rationale. PMs want to know what they can promise their users and when. The CFO wants to know the risk and the cost. One deck fails all three audiences.

---

## Tools and Templates

### Roadmap One-Pager (Filled for T-Mobile Context)

```
TEAM: Notification Platform SRE     OWNER: Vishweshwar Chippa     DATE: Q3 2026

NORTH STAR:
"Reduce service onboarding time from 3 weeks to 3 days
 while sustaining 99.95% reliability on 25M daily messages."

HORIZON 1 — COMMITTED (Q3-Q4 2026)
  EKS upgrade to 1.30        | Priya    | Zero prod incidents        | AWS SA sign-off
  Secrets rotation (Vault)   | Marcus   | 100% vault coverage        | CyberArk renewal
  SLO dashboard v2           | Team     | MTTD under 5 min on P1s    | Grafana 10 upgrade
  On-call runbook audit      | Leads    | 100% runbooks reviewed     | Q3 retro findings

HORIZON 2 — PLANNED (Q1-Q2 2027)
  Internal developer portal  | 2 engineers | Reduce onboarding 3wk → 3d
  SBOM pipeline              | 1 engineer  | Compliance + supply chain posture
  Cost attribution tooling   | 1 engineer  | FinOps pressure; charge-back by team

HORIZON 3 — INTENT (Q3-Q4 2027)
  AI-assisted runbook generation integrated with PagerDuty
  eBPF-based observability to replace current sidecar model
  Multi-region active-active evaluation for notification platform

NOT ON THIS ROADMAP (and why):
  Microservices migration: premature given team size and current traffic pattern
  Build internal CI/CD: GitHub Actions covers the need at current scale
  On-prem Kubernetes: not aligned with cloud-first mandate
```

---

### OKR Writing Card (Filled Example)

```
OBJECTIVE:
  Engineering teams ship to production faster with less fear.

KEY RESULT 1:
  Median deployment frequency moves from 2/week to 8/week per service
  Measured by: GitHub deploy event API, aggregated weekly
  Owned by: Platform tooling lead
  Cadence: Weekly automated report

KEY RESULT 2:
  P95 rollback time drops from 45 minutes to under 5 minutes
  Measured by: Incident timeline data in ServiceNow
  Owned by: On-call program lead
  Cadence: Monthly review at incident retrospective

KEY RESULT 3:
  Developer confidence score on "I can deploy safely on a Friday" moves
  from 3.1 to 4.0 on quarterly pulse survey
  Measured by: 5-question anonymous survey sent by eng-ops
  Owned by: Director
  Cadence: Quarterly

CONFIDENCE CHECK:
  [x] All KRs have a baseline
  [x] All KRs ladder to company OKR: "Accelerate product delivery velocity"
  [x] 60-70% achievable, not sandbagged
  [x] No KR is a pure activity
  [x] Team can recite the Objective without looking
```

---

### Quarterly Planning Session Agenda

```
QUARTERLY PLANNING — Q[N] — Duration: 3 hours
Facilitator: Director   Required: All tech leads, Staff+ engineers, key PMs
Pre-work (circulated 1 week prior):
  - Last quarter OKR actuals
  - Incoming stakeholder requests (compiled by Director)
  - Technical debt register (updated by leads)
  - Team capacity for the quarter (PTO, on-call rotations, known spikes)

PART 1 — RETROSPECTIVE (45 min)
  Wins: what went well and why — not a highlight reel, a causal analysis (15 min)
  Misses: for each miss, classify it:
    Planning failure (we committed to something we could not deliver)
    Execution failure (we could have delivered but did not)
    External dependency failure (outside our control — name the owner)
  One process change based on retrospective — decision made in the room (10 min)

PART 2 — CONTEXT SETTING (30 min)
  Company and org OKRs for the quarter — Director presents (10 min)
  Top 3 external pressures: compliance, customer asks, leadership priorities (10 min)
  Capacity reality check: confirmed headcount, PTO blocks, on-call load (10 min)

BREAK (10 min)

PART 3 — CANDIDATE INITIATIVES (45 min)
  Each tech lead presents top 1-2 candidates (pre-submitted, 3 min each)
  Director presents top stakeholder requests
  No debate yet — this is input gathering
  All items captured on shared board

PART 4 — PRIORITIZATION (30 min)
  Place each item on impact/effort matrix as a group
  Director facilitates; no one person drives placement
  Identify must-do items: compliance, reliability SLA, contractual
  Explicitly identify items NOT doing this quarter — state the reason aloud

PART 5 — COMMITMENT (20 min)
  Director calls the final list — this is not a committee vote
  For each committed item: named owner, success metric, key dependency
  For each deferred item: reason stated aloud so the team hears the logic

CLOSE (10 min)
  OKR draft circulated within 3 business days
  Roadmap artifact updated within 1 week
  Mid-quarter checkpoint scheduled at week 6 (not end of quarter — too late)
```

**On the person who dominates planning sessions**: Do not manage this in the room. Before the session, reach out to that person and give them a role — facilitating the retrospective section, for example. People who dominate usually do so because they feel unheard. Give them a structured outlet. If it persists across sessions, address it in a 1:1 after: "I need every voice in the room. When you drive the conversation, I lose signal from the rest of the team. I need your help managing that."

---

## Decision Matrix

| Situation | Action |
|---|---|
| Request fits Horizon 1 capacity | Accept, assign owner, add to roadmap |
| Request is high-value but Horizon 1 is full | Constraint Redirect — offer a trade explicitly |
| Request is unclear in value | Ask for a one-page business case before scheduling a conversation |
| Request conflicts with company direction | Direct No with rationale and alternative |
| Request comes from a peer who outranks you politically | Horizon Move — "strong Horizon 2 candidate, bring a use case to Q planning" |
| Request comes from your manager and you disagree | Private disagreement process — never in public |
| Mid-roadmap requirement change | 48-hour impact assessment, 72-hour stakeholder notification, formal re-plan in next sprint |
| OKR is at 30% at mid-quarter | Assess: execution problem or planning problem? Adjust only if the external condition has materially changed — not because it is hard |
| Technical debt vs. feature work | Debt that creates incident risk goes on Horizon 1 as reliability work, not a backlog item. Debt that is inconvenient but not risky goes to Horizon 2. |

---

## People Scenarios

### Scenario 1: Executive asks you to add a major initiative to an already-full Horizon 1.

**Script**:
"I want to make this happen. Here is the honest constraint: Horizon 1 is committed at capacity — I have [X] engineers and we are already carrying [Y] and [Z]. If we add this now, one of three things happens: we delay [existing initiative] by one quarter, we reduce scope on [initiative] to make room, or we phase this new work with a smaller version starting in Q4. Which trade makes more sense from your position? I can run any of these — I just want to make the trade visible before we commit."

### Scenario 2: An engineer on your team comes to planning session with an initiative that is technically interesting but low business value.

Do not dismiss it in the room. "I want to think about where this fits. Can you write a one-paragraph case for which internal team benefits from this, and what that benefit looks like in measurable terms? If the case is strong, I will fight to get this into Horizon 2." Most low-value requests die at the business case stage. The engineer feels respected. The planning session stays focused.

### Scenario 3: Your manager has a pet project that does not fit your roadmap priorities.

Private conversation, before the roadmap goes public.

**Script**:
"I want to talk through [initiative] with you before I finalize the roadmap. I have a concern: our current capacity is committed to [X and Y], and adding [pet project] would mean slipping one of those. I want to understand what you are optimizing for here — is this a strategic priority I am underweighting, or is there a way to phase it that would still give you what you need? I want to support it. I want to make sure I understand the tradeoff correctly before I commit."

This accomplishes three things: it respects their input, it exposes the real tradeoff, and it forces a conversation about priority rather than a unilateral decision by either party.

### Scenario 4: Peer Director's team is creating a dependency that will block your Horizon 1 item.

**Script** (in a direct 1:1, not in a group setting):
"I want to surface a dependency before it becomes a problem. [Your initiative] is blocked by [their deliverable] in Q4. I am not asking you to reprioritize — I am asking if we can agree on an interface date so I can plan against it. If [their deliverable] slips, I need 3 weeks' notice to re-plan my side. Can we set that as a formal check-in between our teams?"

This is not political. It is logistics. Peer Directors who get this right build reputation as people who are easy to work with.

---

## The 30-60-90 Day Plan for a New Director Role

### Philosophy Before the Template

The 30-60-90 is not a to-do list. It is a trust-building arc. New Directors who start executing before listening are dangerous — they fix the wrong things, offend the engineers who have been managing the technical debt for three years, and break trust with the informal leaders the team actually turns to for decisions.

The output of your first 30 days is not a deliverable. It is relationships and a clear picture of reality.

**What to avoid in the first 90 days:**
- Making structural changes to team or process before you have done your first full 1:1 cycle
- Dismissing existing architecture decisions in public — you do not have full context yet
- Overclaiming in your 30-day readout — be honest about what you do not know yet
- Missing your first committed deliverable — whatever you say you will ship in days 31-60, ship it. This is the trust anchor.
- Trying to establish yourself by being the most technical person in the room. You are not there to be the best engineer. You are there to build the best team.

---

### 30-60-90 Template (Filled for SRE Director Joining a Startup)

```
30-60-90 DAY PLAN
Role: Director of SRE
Company: [Startup — Series B, 150 engineers, 3 product lines]
Start Date: [Date]
Reporting To: VP Engineering

NORTH STAR FOR FIRST 90 DAYS:
Earn trust, understand the real constraints, and produce one tangible
win that signals how I lead.

============================================================
DAYS 1-30: LISTEN AND MAP
Goal: Understand before changing.
Rule: No structural changes. No public opinions on architecture yet.
============================================================

WHO TO MEET AND WHAT TO ASK:

Every direct report (45 min each):
  - What is the one thing that makes your job harder than it should be?
  - What is the team proud of that I should know about?
  - What do you wish the previous leader had done differently?
  - Where do you want to be in 18 months?
  Output: Written notes per person. Know their win, frustration, career goal.

Every key peer Director (30 min each):
  - Where does your team depend on mine, and where are the friction points?
  - What should I know about this org that is not in the wiki?
  Output: Dependency and trust map. Know where my team helps or blocks theirs.

VP Engineering (weekly structured 1:1):
  - What does success in this role look like at 6 months?
  - What are the top 3 things you need from this team this quarter?
  - What decisions are mine, and which do you want to stay involved in?
  Output: Aligned on expectations before I make any public commitments.

Technical lead on each product team that depends on my platform:
  - What is the most painful thing about working with the platform today?
  - What would make you recommend us to a new engineer joining your team?
  Output: Customer pain list — 3 specific complaints with context.

WHAT TO REVIEW:
  Last 6 months of production incidents — looking for patterns, not blame
  Last quarter's OKRs — what was committed, what was delivered, why did we miss
  Current on-call rotation and paging load by engineer
  All architecture decision records (ADRs) that exist
  Open Jira/Linear backlog — what has been sitting unscheduled for 3+ months
  Any existing roadmap or planning documents

DAYS 1-30 OUTPUT:
  State of the Platform document — 2 pages, shared with manager and team.
  This is not a critique. It is a reflection of what you heard.
  Structure: What is working, what is fragile, what is unclear, what I need to learn more about.
  Tone: Curious, not corrective.

============================================================
DAYS 31-60: DIAGNOSE AND PRIORITIZE
Goal: Surface the real problems and begin making visible decisions.
============================================================

PRODUCE:
  Technical debt register v1: top 5 items with estimated impact if unaddressed
  Process gap list: top 2 team process problems with proposed fix
  Preliminary roadmap draft: shared with team for feedback before finalizing
  OKR draft for next quarter: reviewed by manager before team presentation
  Customer pain list: three specific, actionable items from internal users

DO:
  Make one visible, low-risk improvement — ship it.
    This could be: an on-call runbook gap you fill, a recurring manual task you automate,
    an alert that fires too often that you tune with the team.
    Purpose: demonstrate you can execute, not just observe.
  Establish 1:1 cadence with every direct report — calendar invites sent, agenda template shared.
  Meet with key stakeholders: product leads, FinOps, security team.
  Identify the two informal leaders on your team: who do people go to when
    they have a hard question? Invest time with these people specifically.

DAYS 31-60 OUTPUT:
  First version of team roadmap — circulated for feedback, not announced as final.
  First OKR draft — manager has reviewed and agreed on direction.
  One thing shipped. One person on the team has seen you deliver.

============================================================
DAYS 61-90: COMMIT AND LEAD
Goal: Set direction publicly and begin executing.
============================================================

PRODUCE:
  Final roadmap — published, not just circulated. Three-horizon structure.
  Signed-off OKRs — team can recite the Objective without looking.
  Q[N] plan with named owners and success metrics for every committed item.
  Development plan started for one engineer on your team.
    They should know you are invested in their growth before day 90.

ESTABLISH:
  Team rituals: incident review, retrospective, demo cadence, quarterly planning.
    These are on the calendar before day 90, not being discussed.
  On-call health metric: baseline paging load per engineer established.
    You will use this to defend on-call sustainability in the next headcount ask.

PRESENT:
  90-day findings readout to manager — structured, honest, forward-looking.
  What you found, what you are committing to, what you need from them.
  One named risk — the thing that, if it breaks, ends your tenure early —
    with a mitigation plan and a communication plan.

DAYS 61-90 OUTPUT:
  A team that knows where it is going.
  A manager who trusts your judgment.
  One win visible to the organization.
  One person who has seen you invest in their career.
```

---

## How to Talk About This in Interviews

**Question: "Walk me through how you build a roadmap."**

Avoid: listing process steps. Avoid: "I work with stakeholders to align on priorities" — this is noise.

Use: "I start with five inputs — business objectives, technical debt, incident data, team capability gaps, and internal customer feedback. I synthesize those into a three-horizon structure where Horizon 1 is committed delivery, Horizon 2 is directional, and Horizon 3 is strategic intent. The section I spend the most time on is what we are explicitly not doing and why — that is where the real prioritization thinking is visible."

**Question: "Give me an example of an OKR you wrote that actually worked."**

Lead with the baseline/target/method formula and contrast it with the theater version explicitly: "Most teams write OKRs that are activity lists — complete five runbooks, attend three conferences. I write KRs as: this metric moves from this baseline to this target, measured by this system, owned by this person. The test I use is: if we hit all three KRs and the business is no different, did we write the wrong KRs?"

**Question: "How would you build your 30-60-90 for this role?"**

The answer interviewers want is one that demonstrates you know the first 30 days are about learning, not doing. "The first 30 days I make no structural changes. I meet every direct report with four questions. I review the last six months of incidents. I map the informal leadership structure — not the org chart. The output of day 30 is a written State of the Platform document that I share with the team and my manager. Day 31 is when I start diagnosing."

**Exact phrases that signal Director-level thinking:**
- "We tagged each initiative with a confidence level so the roadmap conversation became about what to unblock, not a debate about dates."
- "I put a 'what we are not doing' section on every roadmap — it is the most important section for credibility."
- "The test for a real OKR: if you hit it and nothing in the business improved, it was the wrong KR."
- "The first 30 days are listening days. The cost of moving too fast in a new role is higher than the cost of moving too slow."

**Phrases to avoid:**
- "I align stakeholders on priorities" — empty
- "We use OKRs to drive accountability" — cliche
- "I believe in transparency" — tells them nothing
- "My roadmap is agile and flexible" — signals you do not make hard calls

---

## T-Mobile Anchors

| Framework Element | Your T-Mobile Evidence |
|---|---|
| Five-input model | You have incident data (36 months, zero Sev1), SLO history, and active on-call data. You have been doing input synthesis informally — now name it. |
| Technical debt register | 6 zero-downtime migrations implies you have been managing debt deliberately. Build the artifact retroactively for interview use. |
| OKR baseline/target | Your platform has concrete metrics: 25M msg/day, MTTD numbers, deployment frequency. Use these as example baselines in every OKR conversation. |
| 30-60-90 listening model | When you joined T-Mobile in your current role or when you expanded scope — what did the first 90 days look like? Even if informal, reconstruct it as a structured story. |
| Quarterly planning | Your team runs sprints and retros. The gap is the Director-level framing: connecting team work to company OKRs and communicating that chain explicitly. |
| Saying no | You have managed a 15-person team with 4 production platforms. You have said no to work many times. Identify two specific examples — one where you used a trade, one where you moved something to the next quarter — and prepare the STAR framing. |

---

## Drills

**Drill 1 — Roadmap Construction**

Prompt to Claude: "I am a new Director of Platform Engineering at a Series B company. My team has 8 engineers, one legacy deployment system that takes 4 hours to run, two open security findings from last quarter's audit, and a product team that wants a feature-flagging service built from scratch. Build a 3-horizon roadmap with a north star, confidence tags on every Horizon 1 item, and a 'what we are not doing' section."

What to look for in your answer: Does the north star have a number? Does Horizon 1 reflect what already exists (the security findings, the legacy system) before adding new work? Is the feature-flagging service in Horizon 2 rather than Horizon 1, and is there a rationale?

**Drill 2 — OKR Rewrite**

Prompt to Claude: "Critique this OKR and rewrite it. Objective: Improve platform reliability. KR1: Publish 10 new runbooks. KR2: Upgrade Kubernetes to latest version. KR3: Complete disaster recovery test."

What to look for: The rewrite should have baselines. The objective should be inspiring and outcome-oriented, not task-oriented. The KRs should describe a state of the world after success, not a list of activities. The measurement method and owner should be explicit.

**Drill 3 — Interview Simulation**

Prompt to Claude: "Interview me as a VP of Engineering at a Series B startup. Ask me three questions about strategic planning, roadmaps, and OKRs back to back, then give me direct feedback on whether I sounded like a Director or a senior IC. Flag any answers that were too tactical, too vague, or that used filler phrases."

Target in your answer: You should spend 40% of each answer on framing and rationale, 40% on specific evidence from your experience, and 20% on the broader principle. If the answer is all evidence with no framework, you sound like an IC. If it is all framework with no evidence, you sound like someone who read a management book.
