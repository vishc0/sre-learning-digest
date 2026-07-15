# Building and Scaling Engineering Teams | Director Leadership Track

## Why This Separates Directors from ICs (What Interviewers Are Actually Testing)

Every senior IC has opinions about team structure. Directors are tested on whether they have made real decisions with real consequences — who to hire first, how to structure on-call when you have three people, what to do when your best engineer refuses to document anything. Interviewers at Director level are not asking "how would you build a team?" They are asking "what happened when you did, what broke, and what did you learn?" This module gives you the frameworks, the vocabulary, and the specific T-Mobile anchors to answer that question with precision.

---

## The Mental Model: The Org Chart Is an Architecture Diagram

Named framework: **The Reliability-to-Organization Mapping (ROM)**

Every principle you apply to system reliability maps directly to team design:

| System reliability principle | Team design equivalent |
|---|---|
| No single points of failure | No single-person knowledge holders |
| Observability before action | Diagnose team health before restructuring |
| SLOs define acceptable risk | Span-of-control thresholds define acceptable management load |
| Blameless postmortems | Blameless culture for organizational failures |
| Runbooks reduce MTTR | Documented norms reduce onboarding time |
| Toil reduction frees capacity | Process elimination frees senior IC cycles |
| Error budget as forcing function | Reliability investment as non-negotiable budget line |

When you walk into any Director-level interview and they ask how you build teams, this mapping is your opening frame. It signals that you think about people problems the way a systems engineer thinks about reliability problems — structurally, not motivationally.

---

## The Framework in Practice

### Phase 1: First 3 Hires — Shape Before Headcount

Most first-time Directors hire three generalists. This is the single most expensive mistake you can make because it sets the team's DNA wrong.

**The correct shape:**

**Hire 1 — The Anchor (Staff-level IC)**
This person has seen a mature SRE practice and can describe exactly what it looks like. Not someone who wants to build it from a book — someone who has lived in one. They write the first runbooks, the first SLO definitions, the first deployment checklist. If they cut corners, those corners become the team's permanent culture. Screen hard for: opinions about what good looks like, willingness to write documentation before building automation, and comfort setting standards alone.

**Hire 2 — The Operator (Senior SRE, on-call capable)**
You need someone who can hold a pager in week three while the Anchor is still building infrastructure. This is not a visionary hire. This is a reliable, calm-under-pressure engineer who can work from incomplete documentation. Most Directors get this wrong — they hire another builder. What you need is a runner. Screen for: incident history, alert hygiene opinions, comfort with ambiguity.

**Hire 3 — The Toolsmith (Senior SRE, automation-lean)**
By hire three you have enough toil to justify someone whose primary job is eliminating toil. Not a developer, not a pure ops person — someone who can own a small internal tool end-to-end and cares about the people who use it. Screen for: examples of self-initiated toil reduction, not just assigned automation work.

**What you do NOT hire at 0-3:**
- A manager (you are the manager)
- A TPM (adds process overhead before there is a process to manage)
- Someone whose primary value is tribal knowledge of a legacy system (you will build around their gaps indefinitely)

---

### Phase 2: Hires 4-10 — Specialization Without Silos

The failure mode from hire four to ten is hiring clones of the first three. The correct sequence:

```
Role              | Level  | Primary Responsibility          | Hire Order
------------------|--------|---------------------------------|------------
SRE Anchor        | Staff  | Technical bar + culture setter  | 1
SRE Operator      | Senior | On-call coverage, runbooks      | 2
SRE Toolsmith     | Senior | Toil automation, internal tools | 3
Platform SRE      | Senior | K8s, IaC, infrastructure depth  | 4
Observability SRE | Senior | Metrics pipeline, SLO framework | 5
DevSecOps SRE     | Senior | Security in CI/CD, compliance   | 6
SRE Generalist    | Senior | Domain coverage, on-call depth  | 7
SRE Generalist    | Senior | Domain coverage, on-call depth  | 8
Tech Lead         | Staff  | Team coordination, bar raising  | 9
Enablement SRE    | Senior | Docs, runbooks, internal tooling UX | 10
```

The hire order is not arbitrary. Security at hire six instead of hire fifteen means you do not retrofit compliance controls into a platform that was built without them. Enablement at hire ten means by the time you have ten people, the documentation is still recoverable from tribal knowledge. After hire ten, it is not.

---

### Phase 3: The Embedded vs. Centralized Decision

This is not a philosophy question. It is a forcing function question based on your current organizational state.

**Centralized SRE — Own this structure when:**
- Organization is under 100 engineers
- Reliability standards are immature or inconsistent across product teams
- You are rebuilding after a bad on-call culture
- You need to establish baseline practices before distributing them

**Embedded SRE — Move here only when:**
- Each product team has genuine autonomy (their own deployments, their own SLOs)
- You have done the central work first — shared runbook templates, shared incident command framework, shared SLO definitions
- Each embedded SRE has a dotted-line reporting relationship to a central SRE manager for career development and performance calibration

**The Hybrid Model — The modern correct answer for most organizations:**

Central SRE team owns: platform infrastructure, SLO governance, incident command framework, tooling standards, on-call process design, and hiring bar.

Embedded SREs (two to three per product cluster) own: day-to-day reliability for their domain, SLO reporting, change management for their services, and weekly attendance at central SRE sync.

**The failure mode nobody documents:** Embedding SREs before doing the central work. Each SRE embeds into a product team with no shared framework. They invent their own runbooks, their own SLO definitions, their own alerting thresholds. Two years later you have fifteen different on-call processes and no way to staff-rotate without re-onboarding every person. This is an organizational reliability incident.

---

**Team Structure Decision Tree:**

```
Is your organization under 100 engineers?
├── YES → Centralized SRE. Build shared platform first.
└── NO → Is your reliability practice mature (documented SLOs, shared runbooks)?
    ├── NO → Centralized SRE. Establish baseline before distributing.
    └── YES → Is each product domain genuinely autonomous?
        ├── NO → Hybrid. Central platform + embedded reliability.
        └── YES (500+ engineers typical) → Embedded with dotted-line to central.
```

---

### When to Split a Team

Empirical triggers — any two together means split, not "consider splitting":

- Team is over ten engineers and standups exceed 45 minutes
- On-call load is carried unevenly (two people handle 70% of incidents)
- Two clear sub-domains exist that rarely share incidents
- Your Staff IC is spending more time coordinating than building
- Engineers describe their growth path as "unclear" in 1:1s

**How to split without creating silos:**

The failure mode: split cleanly and never have the teams talk again. Six months later, an incident spans both and no one knows who commands it.

The structure that prevents this:
- Weekly 30-minute joint sync between team leads — incident review plus shared metrics
- Shared on-call rotation at the platform layer
- Same postmortem template, same facilitation pattern
- Staff IC from each team reviews major architectural decisions from the other before commit

**How to communicate a split:**
1. Tell Staff ICs first — 48 to 72 hours before the team announcement. Give them time to process privately before questions go public.
2. Lead with why before what. Business reason, reliability reason, growth reason. Engineers accept structural change when the reasoning is honest.
3. Name the new structure explicitly: team names, leads, scope boundaries.
4. Within 30 days: give every person a clear answer to "what does this change for my career path?"
5. Answer the question they will all have but few will ask directly: "Was this because something went wrong?" Answer it directly. If yes, say so. If no, say so.

---

### When to Merge Teams

- Two teams share more than 60% of their on-call incidents
- Neither team has enough depth to staff its own on-call rotation
- Team culture has fragmented and a reset requires a single manager
- The domain boundary you drew 18 months ago no longer matches how the system actually works

---

## What Good Looks Like at Director Level

**Hiring:**
- Has a written philosophy on first-three hire shape, not just "hire good people"
- Writes JDs that describe actual scale and actual first-year milestones, not aspirational buzzwords
- Runs interview loops that simulate the job rather than test recall
- Has a two-thirds skill / one-third potential hire ratio and can defend it with examples

**Onboarding:**
- Has a documented 30-day plan with week-level milestones, not a checklist of tools to install
- Holds a day-30 conversation with specific questions — not a satisfaction survey
- Measures onboarding success by autonomous decision-making, not time-to-first-commit

**Culture:**
- Demonstrates blameless behavior publicly before installing blameless postmortem process
- Names and rewards cross-team risk flagging when it happens
- Defines ownership as "who knows the system is at risk" not "who is on the on-call rotation"

**Managing senior ICs:**
- Knows the difference between "does not want to be managed" and "does not want low-value management"
- Runs 1:1s with Staff ICs where the Director talks 30% of the time
- Provides air cover, organizational context, and sponsorship — not status check-ins

**Succession:**
- Maintains a running delta document for every Senior SRE on a Staff trajectory
- Runs the SPOF audit on people the same way they run it on systems, quarterly
- Has written Architecture Decision Records for every significant technical choice

---

## What Bad Looks Like (Anti-Patterns That Derail Director Careers)

**Hiring anti-patterns:**
- Hiring three generalists as your first three. Sets a culture of broad-but-shallow permanently.
- Hiring a manager before you have seven engineers. Adds management overhead to a team that needs builders.
- Writing JDs that describe the team you want to be, not the team you are. You will attract people who will be disappointed.
- Using interview loops that test knowledge recall ("what does a Kubernetes controller do?") instead of applied judgment ("we're seeing HPA not scaling when we expect it to — walk me through your investigation").

**Onboarding anti-patterns:**
- Giving a new hire two weeks of reading before any production exposure. By the time they touch a real system, their mental model is theoretical and wrong.
- Treating access provisioning as low-priority. An engineer who cannot access the systems on day one sends a specific organizational signal, and that signal compounds.
- Sink-or-swim onboarding framed as "we trust you to figure it out." This is not trust — it is the absence of a plan.
- No 30-day conversation. The most valuable signal about your team comes from someone who just saw it with fresh eyes. Most Directors let that signal expire.

**Culture anti-patterns:**
- Announcing a blameless postmortem process without demonstrating it yourself first. Engineers do not believe policies — they believe behaviors.
- Letting the on-call engineer write their own postmortem without a neutral facilitator. It will explain rather than learn.
- Tolerating "not my job" language in any form without immediate public correction.
- Using the threat of a difficult conversation to avoid a difficult conversation. When a resistant Staff IC blocks a correct decision because you find the conflict uncomfortable, every engineer on the team learns that resistance works.

**Attrition anti-patterns:**
- Waiting until a key person gives notice to start succession planning. By that point you are six to twelve months behind.
- Believing exit interview reasons. The stated reasons are almost never the actual reasons.
- Hiring at pace without onboarding at pace. Every new hire who ramps slowly pulls bandwidth from the engineers they were hired to relieve.

---

## Tools and Templates

### Job Description Framework That Attracts SREs (Not DevOps Engineers)

The difference between an SRE JD and a DevOps JD is not the technology list. It is whether the role has defined reliability ownership with measurable outcomes.

```
SECTION 1 — WHAT WE OWN (2-3 sentences, honest)
Specific scale, specific systems, current state — not aspirational.
Example: "25M message/day notification platform on EKS, 6 upstream product teams.
We own the SLO framework, on-call process, and platform infrastructure for all of them."

SECTION 2 — WHAT YOU WILL ACTUALLY DO (5-6 bullets)
First bullet is the hardest, most interesting thing.
Bad:  "Monitor production systems."
Good: "Own error budget burn rate alerting across 12 microservices; present
       burn rate trends in monthly engineering review with product leadership."

SECTION 3 — WHAT SUCCESS LOOKS LIKE (3 milestones)
Bad:  "Contribute to team goals."
Good: "Month 3: own on-call rotation independently.
       Month 6: shipped one toil-reduction automation.
       Year 1: led one postmortem as incident commander."

SECTION 4 — WHAT WE ARE LOOKING FOR (two-column: Required vs Preferred)
Required = things you will assess in the loop.
Preferred = genuine differentiators, not checkbox items.
Do not list "5 years of Kubernetes" as required if you will interview someone with 2.

SECTION 5 — HOW WE WORK (this is the differentiator section)
- On-call: rotation size, compensation model, escalation path
- Postmortem culture: blameless — name it explicitly
- Tech stack: what is actually in use, not what you aspire to use
- Growth: cert budget, conference sponsorship, learning time allocation
```

**Deliberate friction signals (these repel wrong candidates):**
- "Comfortable owning production incidents without a complete playbook"
- "Writes runbooks for work you just completed, not only work that is assigned"
- "Reviews and challenges existing SLO definitions — not just reports against them"

---

### Interview Loop Template

```
Interview    | Duration | Assessor          | Format                          | What You Test
-------------|----------|-------------------|---------------------------------|----------------------------
HM Screen    | 45 min   | You               | Behavioral + context            | Ownership language, failure honesty
Systems      | 60 min   | Staff IC          | System design                   | Failure-mode reasoning, observability instinct
Debugging    | 60 min   | Senior SRE        | Live debug (ambiguous signals)  | Methodology, hypothesis formation
Behavioral   | 45 min   | Cross-team 2-ppl  | STAR scenarios                  | Conflict under collaboration, specificity
Bar Raiser   | 30 min   | Skip-level        | Risk/judgment calibration       | What they see that you missed
```

**HM Screen questions that separate candidates:**
- "Walk me through the last incident you owned from detection to postmortem." (Tests: do they own outcomes or describe being present?)
- "What is the worst production decision you made, and what changed after?" (Tests: self-awareness and learning orientation)
- "What does your current on-call look like — how many alerts per week, how many are actionable?" (Tests: do they have opinions about alert quality, or do they just accept noise?)

**Systems interview signals that matter more than the design itself:**
- Do they ask about failure modes before designing the happy path?
- Do they mention observability without being asked?
- Do they reason about the cost of the SLO, not just how to achieve it?

**For Staff/Principal candidates — differentiated questions:**
- Ask them to critique a system design you present, not just build one
- "How would you coach a junior SRE who kept silencing the same alert?"
- "What is the right SLO for a new product team — and should it be different in year two?"
- "What would you deliberately NOT automate, and why?"

---

### 30-Day Onboarding Plan

```
Week 1 — Context, Not Tasks
Day 1:   Full access provisioned (all systems — do not let this drag into day 3)
Day 1:   Read team charter: what we own, current SLOs, on-call structure
Days 2-3: Shadow on-call — full shift with current on-call SRE
Days 3-4: Read last 5 postmortems. For each: what was the detection gap, what was the
          mitigation gap, what changed after?
Days 4-5: Architecture walkthrough — how data flows through the 3 most critical services
Day 5:   30-min check-in with hiring manager: what is confusing, what is clear, what
          is surprising?

Week 2 — First Real Ownership
- Own one runbook update (existing, not new) — forces reading and questioning docs
- Attend one production incident as observer — see incident command in real conditions
- Write one alert improvement proposal — forces understanding current coverage and gaps
- 30-minute 1:1 with every direct teammate (no agenda — relationship before crisis)

Week 3 — Supervised Autonomy
- Own one on-call shift with buddy available — first production ownership with safety net
- Ship one small automation or tooling improvement — first production contribution
- Present architecture understanding back to team — exposes knowledge gaps before
  they become production gaps

Week 4 — Independent Contribution
By day 30, the new hire should be able to:
- Handle a P2 incident without asking who to call
- Write a postmortem draft without a template prompt
- Name the team's top 3 SLO risks and what would cause each to breach
- Identify the one thing they would change about current on-call setup (and have an opinion)
```

**The Day-30 Director Conversation (not an HR survey — three specific questions):**
1. "What is the most important thing you learned that was not in the job description?"
2. "What gap in our runbooks surprised you most?"
3. "If you were staffing this team next, what skill would you add first?"

Their answers tell you more about your team's current state than a quarterly review. This conversation is a diagnostic, not a check-in.

**Onboarding into a broken platform (startup scenario):**
When you are onboarding someone and the platform does not exist yet, the framework shifts. Week one becomes: "shadow every conversation where a reliability decision gets made." Week two becomes: "own one decision that will affect production, document your reasoning before you make it." The milestone is not system access — it is having an opinion about an architectural choice with organizational impact.

---

### Retention Risk Assessment Template (Run Quarterly)

```
For each person on your team, answer these 5 questions:

1. Growth trajectory
   - What is the last meaningful new scope they received?
   - Is their current work building toward their stated next-level goal?
   - Red flag: no new scope in 6+ months, or scope that is narrowing not expanding

2. Peer recognition
   - Are they known outside this team? (other teams, skip-level, cross-org)
   - Have you named them in rooms they were not in this quarter?
   - Red flag: high performer who is invisible to organizational leadership

3. Work quality satisfaction
   - What percentage of their week is reactive vs proactive?
   - Are they building anything they would put in a portfolio?
   - Red flag: self-reports 70%+ reactive week over 2+ consecutive months

4. Compensation signal
   - Is their compensation still competitive for their market-adjusted level?
   - Have they received a meaningful increase in the last 12 months?
   - Red flag: top-performing Senior with flat comp while market has moved

5. Manager relationship
   - Can they disagree with you and remain safe?
   - Do they know what you actually think of their work?
   - Red flag: they give you only good news; no friction in 1:1s usually means no trust

Risk classification:
0-1 red flags = monitor, no action
2 red flags = active retention conversation in next 1:1
3+ red flags = treat as high attrition risk; retention plan within 30 days
```

**The three real reasons senior engineers leave (not what exit interviews say):**

1. **Invisible work.** Their best contributions were not named, credited, or visible to the organization. They leave when they believe their work matters more at the next company than at this one. Exit interview says: "better opportunity." Real reason: you never made them feel consequential.

2. **Stagnant trajectory.** They have been doing the same type of work for 18 months. Not necessarily the same tasks — the same level of challenge. Exit interview says: "professional development." Real reason: you kept giving them work they were already good at instead of work that required growth.

3. **Loss of respect for organizational decisions.** They have watched leadership make decisions they believe are wrong — technically, culturally, or strategically — and received no evidence that their perspective was heard or considered. Exit interview says: "culture fit." Real reason: they stopped believing the organization's decision-making was sound.

**When a key person gives notice — the first 24 hours:**

The instinct is to counter-offer. The data says counter-offers retain people for an average of 90 days before they leave anyway. Do not lead with counter-offer.

The protocol:
- Hour one: "Tell me what led to this decision. I want to understand, not retain." Then listen without defending.
- Hour two to 24: Assess whether the underlying driver is fixable in your current organization. If yes, make a genuine structural change proposal — not a compensation patch.
- If the decision is firm: transition conversation immediately. "What would make your last 30/60/90 days the best possible handoff?" This protects your team and preserves the relationship.
- Within 48 hours: tell your team yourself, in your own words, before they hear it another way.

---

## Decision Matrix

| Situation | Signal | Action | Timeline |
|---|---|---|---|
| Hire 1 | You have funding and a charter | Staff Anchor — reject the urge to hire a generalist | Before anything else |
| Embedded vs centralized | Under 100 engineers | Centralized. No exceptions. | Day 1 of building |
| Team split | 2+ empirical triggers present | Split with joint sync infrastructure | 30-60 days to execute |
| Team merge | 60%+ shared incident load | Merge under single manager | Announce 2 weeks out |
| Potential vs skill hire | On-call is understaffed today | Skill hire — potential hires cannot hold a pager in 3 months | Immediate |
| Potential vs skill hire | Staff IC can absorb mentorship | Potential hire — up to 1/3 of team | Evaluated per hire |
| Staff IC resisting | They are wrong and blocking | 1:1 with data + org implication; make the call, document it | Within 1 week |
| Staff IC resisting | Your management adds no value | Change what you offer them; don't call it a resistance problem | Within 2 weeks |
| Key person gives notice | Firm decision | No counter-offer lead; listen first, transition second | Hour 1 |
| Retention risk score 3+ | Assessment triggered | Retention plan; structural change offer, not just comp patch | 30 days |

---

## People Scenarios (Scripts Included)

### Scenario 1: The Staff IC Who Refuses 1:1s

They say: "I do not need weekly 1:1s. I will Slack you if I need something."

What they mean: Your 1:1s are status updates. They get no value from them.

Director script:
"You are right that we do not need a status check-in. Let me change the format. Once a month, 45 minutes. I talk 30% of the time. The agenda: where the organization is going that you do not know yet, what risks I am seeing, what you are seeing that I am missing, and what is in your way that I can remove. No status updates. You can cancel it if it stops being useful."

Most Staff ICs who refuse 1:1s will accept this format. If they still refuse, that is a different signal — one about trust, not format.

---

### Scenario 2: The Senior IC Who Is Wrong and Resistant

Context: Your Staff SRE insists on an architectural approach that you and two other senior engineers have assessed as fragile. They have blocked the decision for three weeks.

Director script (1:1 setting):
"I want to have this conversation directly. I have heard your concerns about [approach]. I have also heard the counter-arguments from [others]. I have assessed both and I am making a call: we are going with [correct approach]. I want to give you the chance to tell me what would change your mind — what evidence or reasoning would move you. If there is something I have not considered, I want to hear it today. But I also want to be clear: if we cannot reach alignment, I will make the decision and document that it was mine. That does not mean your concern was wrong — it means organizations need someone to make calls when alignment is not available."

What you must not do: let this go another week. Every day this is unresolved, the rest of the team is observing that resistance works.

---

### Scenario 3: The Team That Has a Blame Culture

Context: You have inherited a team where engineers delay reporting incidents because previous leadership used incidents as performance evidence.

Director script (team meeting, week 2):
"I want to name something I have noticed in the postmortems I have read. The language is often passive — things 'went down,' alerts 'were missed.' I want us to change that not because I want to assign blame, but because passive language hides the system conditions that caused the problem, and if we cannot name them, we cannot fix them. Starting with the next postmortem, I am going to facilitate it myself. I am also going to share my own example — a decision I made recently that I would make differently. The goal is: by the time someone else facilitates, they have seen what blameless actually looks like, not just been told it is safe."

This takes three to four cycles before engineers believe it. Do not expect the first postmortem to be different — expect the fourth to be.

---

### Scenario 4: Announcing a Team Split

Context: You are splitting a 12-person team into two teams of six.

Staff IC conversation (72 hours before announcement):
"I want to talk with you before I announce this to the team. I am splitting the team into two — Platform SRE and Product SRE. I want you to lead Platform SRE. Here is why I am doing this: [specific reliability reasoning, not headcount reasoning]. I want to give you a few days to think about this and ask me anything you want privately before it goes to the team. What questions do you have?"

Team announcement structure:
1. Why first (reliability rationale, growth rationale)
2. What second (new structure, named leads, scope boundaries)
3. What stays the same (shared postmortem process, shared on-call at platform layer, joint weekly sync)
4. Direct answer to the unspoken question: "This is not because something went wrong. This is because we have grown to the point where two distinct domains need focused leadership."

---

### Scenario 5: The New Hire Who Is Not Ramping

Context: A senior SRE at week 5 has not yet held an independent on-call shift, and their runbook contribution was surface-level.

Director conversation:
"I want to have a direct conversation because I care about your success here. At week five, based on our onboarding plan, I expected you to be ready for an independent on-call shift. You are not there yet, and I want to understand why. Is the platform more complex than we set you up for? Are the runbooks insufficient? Is there something about the on-call process that does not make sense yet? I am asking because the answer changes what we do next — and because I would rather have this conversation now than wait until you are in a high-stakes incident without the foundation."

The Director failure mode here: waiting until week ten to have this conversation, then treating it as a performance issue when it is an onboarding design failure.

---

## How to Talk About This in Interviews

**The framing that works:**

You have been building SRE teams for years in an environment that required Director-scope decisions without the Director title. The interview requires you to name the framework, not just describe the story.

**Phrases that signal Director-level thinking:**
- "The first decision I make when building a team is about shape, not headcount — specifically, what the first three roles need to accomplish structurally before the fourth hire can be effective."
- "I treat team topology the same way I treat system architecture — I look for single points of failure, unclear ownership boundaries, and insufficient observability into team health."
- "The embedded vs. centralized decision is not a philosophy question. It is a question about whether you have done the central work first. If you have not, embedding distributes fragility."
- "I measure onboarding success by whether someone can make an autonomous production decision by day 30 — not by whether they have completed the access provisioning checklist."

**What to avoid:**
- "I hire A-players and let them figure it out." (Signals you do not have a real framework)
- "Culture is everything." (True but unactionable — say what you actually do to install culture)
- "My team has very low attrition." (This is a result, not a strategy — explain the three drivers and what you do about each)

**STAR framing anchor for "tell me about building a team from scratch":**

Situation: "T-Mobile notification platform serving 25M messages per day, 15-person SRE team — but the relevant scenario is when I inherited a team with no structured on-call process, no SLO definitions, and a postmortem culture that was blame-oriented because of previous leadership."

Task: "I needed to install structure without invalidating the work the team had already done — and I needed to do it while maintaining operational continuity on a zero-downtime platform."

Action: "First 30 days: diagnostic only. I attended every incident, read every postmortem from the previous six months, and made a list of every practice I observed — then categorized it: safety risks that needed immediate correction, reliability risks that needed team involvement to fix, and cultural patterns that required trust before I could change them. First structural change was in safety risks — I framed each one as a 'this creates risk when we are under pressure' conversation, not a 'this was wrong' conversation. The postmortem culture reset started with me: I publicly named a decision I made in week three that I would make differently, and I facilitated the next two postmortems myself to demonstrate the behavior before asking the team to trust the process."

Result: "36 months zero Sev1, six zero-downtime migrations. More importantly, the team now initiates postmortem conversations rather than avoiding them — which is the leading indicator I actually care about."

---

## T-Mobile Anchors

| This Module's Concept | Your T-Mobile Evidence | How to Frame It |
|---|---|---|
| First 3 hire shape | You have a 15-person team with defined roles — walk back to describe how the shape was established | "When I look at how our team reached its current structure, the decisions that mattered most were the first specialization decisions..." |
| Embedded vs centralized | 6 product teams, centralized SRE function | "We run a centralized model with informal embeds — I have SREs who have deep context in specific product domains but maintain their primary accountability to the SRE function..." |
| Team splitting | 15 people — you have operated at the threshold | "At 15, we are organized in sub-domains. The forcing function for how I think about team structure is when coordination cost exceeds collaboration benefit..." |
| Onboarding | 15-person team means you have onboarded many people — name a specific example | Use the "most valuable thing I learned was what the new hire told me in the day-30 conversation" framing |
| Blameless culture | 36 months zero Sev1 is a cultural outcome, not just a technical one | "Zero Sev1 for 36 months is partly technical rigor, but it is also that the team reports early because they do not fear the postmortem..." |
| Succession | 6 zero-downtime migrations = someone planned for people not being available | "Every migration we ran was staffed as if the primary person could be unavailable — that discipline came from treating people SPOFs the same way we treat system SPOFs..." |
| Senior IC management | Principal SRE role — you manage yourself as a senior IC and manage others at that level | "The deal I make with Staff-level engineers is explicit: I give you context before it is public, air cover when you make a correct but unpopular call, and sponsorship in rooms you are not in. In exchange, I need you to write down the decisions you make and why..." |

---

## Drills

**Drill 1: The Hiring Architecture Problem**

Prompt for Claude:
"I am a Director of SRE being hired at a 60-person startup. They have two engineers doing ops work with no formal SRE function. I have budget for three hires in year one and six hires in year two. Walk me through my hiring sequence, the JD for each role, and the two organizational risks I need to name explicitly in my first 90-day plan."

What to practice: Speaking to hire shape with reasoning, not just headcount. Connecting each hire to a specific reliability gap.

---

**Drill 2: The Underperforming Staff IC Scenario**

Prompt for Claude:
"My Staff SRE has strong technical opinions and has been with the company for four years. In the last six months, they have blocked three architectural decisions — two they were right about, one they were wrong about. The team is starting to route around them. I need to have a direct conversation. Roleplay as the Staff IC with those behaviors and let me practice the Director conversation."

What to practice: Separating the "they are sometimes right" dynamic from the "routing around them is now a team culture problem" dynamic. Delivering direct feedback without removing the IC's sense of authority.

---

**Drill 3: The Day-30 Onboarding Conversation**

Prompt for Claude:
"I just ran a 30-day onboarding check-in with a new Senior SRE. They told me: (1) the runbooks are outdated and no one updates them, (2) the on-call alert volume is so high that they cannot tell signal from noise, and (3) they were surprised how much of the team's time is in reactive work. Roleplay as me and respond to this new hire — address each concern, be honest about what is a known issue vs. what is news, and outline what changes as a result of this conversation."

What to practice: Using onboarding feedback as a diagnostic tool rather than a reassurance exercise. Committing to specific changes vs. explaining why things are the way they are.
