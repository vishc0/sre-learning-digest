# Executive Presentation Template: Director/VP Round Interview

**Purpose**: This is a complete speaker notes document for a 30-45 minute executive round interview. Structure is designed for SRE/DevSecOps Director or Principal Engineer roles. Each slide is written as what you actually *say*, not bullet points.

**Key insight**: This is not a demo. This is a conversation starter where you demonstrate organizational thinking, not technical depth. The interviewer already knows you're technically competent (they saw your skills round). This round answers: "Would I trust this person to lead my team? Do they think like leadership?"

---

## Slide 1: Opening Statement (2 minutes)

**WHAT TO SAY:**

"Thanks for having me. I'd like to start by explaining what I've learned works in SRE leadership, and then show you a specific case where I applied it. The core insight is this: SRE teams exist to solve business problems through reliability, not to be gatekeepers of uptime. I've spent the last eight years running teams that think backwards from business impact — not forwards from infrastructure."

[Pause. Let them absorb.]

"I'll walk through a framework I built at T-Mobile for governing 25 million notifications a day across a 15-person team, touch on three mistakes I see Directors make, and then I want to hear from you about what your team is struggling with right now. That will tell me whether my experience translates here."

**WHAT NOT TO SAY:**

- ❌ Don't lead with Splunk dashboards or Kubernetes architecture. That signals you're still thinking like an IC.
- ❌ Don't say "I've always wanted to work for [company]." Say what problem you're solving, not where you want to work.
- ❌ Don't claim expertise in areas you haven't led a team through (e.g., "I'm great at mentoring" if you've never done 1-on-1s at scale).
- ❌ Don't use technical jargon in the first 30 seconds. Enterprise leadership despises window-dressing.

**TIME BUDGET:** 2 minutes. If they interrupt with a question, answer it and reset to Slide 2. Don't fight it — responsiveness > following a script.

---

## Slide 2: The Problem Statement (3 minutes)

**WHAT TO SAY:**

"Before I describe what we built, I want to set the context. When I took over the SRE team at T-Mobile, we had three systemic issues that I see everywhere:

**First, alert fatigue was killing morale.** We had 47,000 alerts per week, and the on-call engineer was responding to pings every 45 seconds. That's not reliability. That's chaos. The engineers I recruited weren't staying because they didn't feel like engineers — they felt like alarm responders. So we had retention at 62%.

**Second, the business didn't trust our SLOs.** We had four different SLO definitions floating around: what Ops said, what the platform said, what billing said, and what Engineering thought. When a product manager asked 'Am I within my error budget?' nobody could answer with certainty. That kills agility.

**Third, we had zero leverage on security.** Every deployment went through three manual security gates. Nobody owned the gates — they just existed. We couldn't ship a hotfix in under four hours. For a 25M message-per-day platform, that's a business risk, not a security feature.

Here's what I noticed: every team was working hard, but the system was misaligned. The incentives were wrong."

**WHAT NOT TO SAY:**

- ❌ Don't blame individual engineers ("My predecessor hired the wrong people").
- ❌ Don't claim you fixed everything. Say what you improved and what's still hard.
- ❌ Don't spend time on numbers that don't matter to an executive (alert fatigue doesn't need to be 47K — could be 10K. The fact that it's high is what matters).
- ❌ Don't make it sound like a blame game against other teams. DevSecOps is inherently cross-team — own the misalignment.

**TIME BUDGET:** 3 minutes. If they ask "How did you measure alert fatigue?" answer briefly (Splunk logs + alert telemetry) and move on. Don't get pulled into the weeds.

---

## Slide 3: The 30/60/90 Day Plan (5 minutes)

**WHAT TO SAY — This is where most candidates fail. Read carefully.**

"I want to be explicit about what I'd do in my first 90 days here, but I want to be even more explicit about what I'd *not* do without talking to you first.

**Days 1-30: Listen and measure.** I'd spend the first two weeks in 1-on-1s with every engineer on the team. Not performance reviews — just 'What's your biggest frustration right now?' I'd also do a walk-through of the incident log for the last three months. Not to judge — to calibrate. Here's what I'm looking for: Are engineers burnt out? Are incidents driven by toil, architecture, or external factors? What's actually keeping your business up at night?

By day 20, I'd have a shared Slack channel where I synthesize patterns: 'I'm hearing three things — 43% of your unplanned work is secrets rotation, 31% is cluster scaling, and 26% is unclear ownership.' That transparency is my credibility.

By day 30, I'd propose **one** thing we're going to improve together. Not five things. One. And I'd let the team vote on what it is. This matters because I don't know your constraints yet — maybe hiring is frozen, maybe the next quarter is locked. I pick *their* highest-leverage problem, not mine.

**Days 31-60: Build trust, not infrastructure.** I'd run a blameless postmortem on the last major incident using a structured format. I'd publicly give one example of where I was wrong in my first two weeks. I'd get one small win — maybe automating a toil task that takes three hours a week. Publicly celebrate the person who did it.

I'd also start weekly sync with the platform team, the security team, and the product org. Not to assign blame. To align incentives. 'Here's our error budget. Here's where we're spending it. What can we change in the contract between us?'

**Days 61-90: Charter the direction.** Once I understand your constraints and your team's energy, we draft the north star. Not a roadmap — a direction. Something like: 'Our goal is that by Q4, every deployment is encrypted end-to-end, every engineer has a runbook generator, and zero unplanned incidents are due to secrets.' That gives people clarity without a false sense of being able to predict timelines.

**Here's what I'm NOT doing without talking to your leadership first:**

- Recommitting to a roadmap that was set before I arrived. Not because I distrust it — because I don't know if it was set with full information.
- Reorganizing the team. I've seen too many new leaders hire fast and fire faster. I'd rather have strong engineers in the wrong org structure than lose people before I understand what I'm working with.
- Proposing a new technology stack. K8s, Terraform, Datadog — these are expensive to migrate. I'd audit what you have, understand why it was chosen, and only recommend change if the business impact is clear.
- Making hiring decisions. I'd ask you who you've lost and why. That tells me what we need.

**The question I'm really answering in the first 90 days is: Is this fixable, and where do I have leverage?** That's an honest assessment, not a roadmap fantasy."

**WHAT NOT TO SAY:**

- ❌ Don't present a detailed 90-day roadmap with specific projects and timelines. That screams "I didn't listen to the team."
- ❌ Don't say "I'll hire aggressively." Startups love this; enterprises hate it. Enterprises are hearing "you're understaffed" as an implicit criticism of current leadership.
- ❌ Don't commit to specific tech migrations without saying "if the business impact is clear." You don't know their constraints yet.
- ❌ Don't skip the "what I'm NOT doing" section. It's the signal that you're self-aware. Self-aware executives are trustworthy.
- ❌ Don't treat this as a script. If they ask "What if the team votes for something impossible?" then answer that — it shows you're thinking.

**TIME BUDGET:** 5 minutes. If they interrupt with "How would you handle the case where..." then *that's the interview now*. Answer the scenario and come back to the narrative if it makes sense. Flexibility > rigid structure.

---

## Slide 4: Case Study — The SLO Alignment Example (8 minutes)

**WHAT TO SAY:**

"Let me ground this in something concrete. At T-Mobile, SLOs were a mess. I'll walk through how we fixed it, but more importantly, I'll show you the leadership decisions, not the technical ones.

**The problem**: Product management wanted 99.99% uptime. Platform engineering said 99.95% was achievable. Billing said they needed 99.99% to meet SLA contracts. We had three different numbers, and when an engineer made a deployment decision, they didn't know which standard they were being measured against.

**The first mistake we made**: We tried to solve it technically. We proposed a complex tiered SLO architecture — different SLOs for different customer tiers. It was smart. It was also wrong. Because the real problem wasn't the math. The problem was that nobody owned the conversation.

**Here's what actually worked**: I scheduled a 90-minute meeting with Product, Billing, Platform, and a customer success manager. No slides. Just the question: 'What does uptime mean to our business?' 

Product said: 'Our customers will churn if we're down for more than 5 minutes, more than once a month.'

Billing said: 'Our SLA contract says 99.99%, but actually, we've never been audited on it. What we really need is predictability and a way to communicate outages clearly.'

Customer success said: 'Honestly, most outages are under 30 seconds and customers don't notice. What drives complaints is unclear communication.'

**The insight**: They weren't arguing about a number. They were using the number to argue about *trust*. Product didn't trust Platform to care about their customers. Billing didn't trust us to communicate. So we solved the trust problem first.

**Here's what we committed to:**

One: A single SLO — 99.95% for the platform. That's our contract. No tier nonsense.

Two: A clear definition of what uptime means — response time under 500ms for 95% of requests, error rate under 0.1%. Published on the wiki. Everyone sees it. 

Three: A bi-weekly sync — 30 minutes, Product and Platform together, looking at the previous two weeks. 'How close are we to budget? Where are we spending it?' This is not a meeting to assign blame. It's a meeting to keep everyone on the same page.

Four: When we burn 50% of the month's error budget, we lock down new features. Not forever — but until we buy back the budget. This is not me being strict. This is an agreement everyone made.

**The results:**

- Retention stayed at 85%. (Not incredible, but it stopped declining.)
- We shipped a security hotfix in 2 hours instead of 4 because everyone knew we had budget.
- We reduced deployments from five a week to three a week, but each one was more intentional. We weren't shipping to patch over systemic issues.
- Alert fatigue dropped. Because now every alert was tied to a budget impact.

**But here's what I want you to notice**: The technical change was trivial. We didn't build new monitoring. We didn't rewrite the platform. We changed the *conversation*. That's what leadership is — changing how your team thinks about a problem so that their intelligence can actually solve it.

**The hard part**: This took three months to stabilize. There were two moments where Product wanted to bend the SLO for a special customer. I said no. Not because I don't care about customers — but because breaking the contract destroys the trust we just built. That's a decision that only a leader can make. And it's lonely. But it's what prevents your team from burning out."

**WHAT NOT TO SAY:**

- ❌ Don't spend 50% of this section on the technical architecture (SLO math, percentile calculations, etc.). That's not what an executive cares about. They care about the outcome.
- ❌ Don't present this as a victory lap. Say what you learned and what still didn't work. "We still have alert fatigue in the edge cases" signals that you're honest.
- ❌ Don't claim you did this solo. Name the people who helped — even if it's just "my tech lead pushed back on my first draft and they were right."
- ❌ Don't say "I changed the team's culture." Say "We changed the conversation." Culture is something that unfolds over time; conversations are intentional.
- ❌ Don't use this to brag about shipping speed or uptime metrics. Use it to show how you made tradeoffs transparent.

**TIME BUDGET:** 8 minutes. If they ask "How did you measure the impact on retention?" answer it (we tracked signup cohorts), but don't go deep. The story is done. Move on.

---

## Slide 5: Three Mistakes I See Directors Make (4 minutes)

**WHAT TO SAY:**

"I've interviewed at six companies over the last two years, and I've debriefed with directors at most of them after deciding not to take the job. Three patterns emerged that I think are worth naming:

**Mistake #1: Mistaking technical excellence for leadership.**

I see Directors who can architect a platform beautifully but can't tell you whether their team is happy. They measure success by uptime and feature velocity, not by whether people are staying. The best technical leader I know is my peer at Amazon — incredibly sharp — and they explicitly said to me: 'My job is not to be the smartest person in the room. My job is to hire people smarter than me and get out of their way.' That's the shift. Once you're a Director, your technical chops are table stakes. Your leverage is people.

**Mistake #2: Trying to boil the ocean.**

New Directors often inherit a list of problems and try to solve them all at once. 'We're going to move to Kubernetes, implement observability-as-code, and adopt OPA all in Q1.' That's not ambition. That's organizational overload. The teams I respect have a clear thesis — 'This quarter, we're reducing toil by 30%. Everything else is secondary.' That gives people permission to say no.

**Mistake #3: Confusing alignment with obedience.**

This one kills morale. I see Directors who say 'Here's the roadmap,' and they expect the team to execute it like robots. What they're actually saying is: 'I don't trust your judgment.' Smart engineers leave that. What works is saying 'Here's the constraint and the goal. What's your idea for how to solve this?' Then you might disagree. But the team knows they were heard.

**These aren't random observations.** I'm naming them because I want you to know I'm thinking about how to lead *your* team differently. If you see me making these mistakes, I hope you'll call me out."

**WHAT NOT TO SAY:**

- ❌ Don't name specific companies or people. Keep it generic ("I've seen this at three places").
- ❌ Don't position yourself as a crusader who's going to fix all the broken directors out there. That's arrogant.
- ❌ Don't make it sound like these are moral failings. Say 'I see this pattern' not 'I hate directors who do this.'
- ❌ Don't skip the last sentence. Saying "I want you to call me out" is vulnerability. Vulnerability is trust-building.

**TIME BUDGET:** 4 minutes. If they ask "How would you avoid mistake #1?" give a one-sentence answer: "I measure the health of my team every month — engagement survey, retention tracking, promotion velocity. That's where I spend my attention." Then move on.

---

## Slide 6: Your Platform as a Multiplier (5 minutes)

**WHAT TO SAY:**

"One of the biggest shifts in SRE over the last five years is that SRE is not a centralized constraint anymore. It's a capability multiplier.

What I mean: Five years ago, the mental model was 'SRE says yes or no to deployments.' Now, the model is 'SRE makes it so easy for product engineers to deploy safely that they never want to go around you.'

At T-Mobile, we built this by thinking backwards from product engineering. What do they need to ship? They need to know: Is this safe? Will it break anything? Can I get this out in 15 minutes if there's a P1?

So we built four things:

**One: Deployment orchestration that's not a gate.** It's a guide. You define your change. The system tells you: 'This touches these services. Their current error budget is X. Your change has a Y% chance of triggering an incident based on historical patterns.' Then you decide. Not us. If you push anyway and it breaks, we help you fix it fast. But the decision was yours. That's ownership.

**Two: Automated security scanning that runs in CI.** Not a gate. A feedback loop. 'You're shipping a secret key. Here's why that's bad. Here's how to fix it.' By the time the PR reaches our gate, there are zero surprises.

**Three: Observability that's built into every service at deploy time.** Product engineers don't have to ask us for dashboards. They auto-generate. They don't have to ask us for alerts. We deploy smart defaults based on the SLO. They can customize, but most don't because the defaults are good.

**Four: A runbook generator that creates triage steps from your recent incidents.** 'The last time this service had a spike, you did X and Y. Want me to bake that into the runbook?' It's not perfect, but it's better than blank pages.

**The magic**: Product teams love this because they feel faster. They're not waiting for SRE to review. We love it because we're not drowning in tickets. And the platform gets more reliable because we're pushing intelligence to the edge, not concentrating it in a gate.

**The business impact**: Deployment frequency went from 2 per week to 5 per week. Mean time to recovery went from 45 minutes to 12 minutes. And nobody hates SRE anymore. That last one matters because morale drives retention drives knowledge drives reliability."

**WHAT NOT TO SAY:**

- ❌ Don't spend time on the technical stack (Spinnaker, ArgoCD, Falco, etc.). An executive doesn't care.
- ❌ Don't present this as "We automated all the gatekeeping." That's jargon. The idea is "We made it easy for engineers to make safe decisions."
- ❌ Don't claim 100% automation. Real world: 15% of deployments still need manual review. Say that.
- ❌ Don't frame this as SRE "giving up power." Frame it as "shifting from approval to leverage."

**TIME BUDGET:** 5 minutes. If they ask "How do you prevent engineers from shipping bad code?" answer: "The automation catches it. If it gets through, we have rapid rollback. And we debrief — 'Why did this slip past our checks?' Then we improve the checks. We treat engineers as partners, not adversaries."

---

## Slide 7: Security, Compliance, and SRE (4 minutes)

**WHAT TO SAY:**

"DevSecOps is a buzzword that actually describes a real shift. It's not 'embed security in CI/CD.' It's 'make security the default path, not the friction path.'

Here's the model I've built: Security is not a gate. It's a guardrail.

**What that means in practice:**

We have three levels of policy:

**Level 1 — Stop.** These are non-negotiable. You cannot deploy code with hardcoded secrets. You cannot open a port to 0.0.0.0 without an exception. These are automatic blocks, not reviews. 

**Level 2 — Require review.** You're shipping a new external API. Our security team reviews the auth model. Takes 2–4 hours. This is not a veto. It's a check. We've never said no — we've said 'change this' and the engineer makes the change.

**Level 3 — Feedback.** You're using a third-party library with a CVE that's 18 months old but not in your execution path. We flag it. You have 30 days to patch. If you don't, it escalates to Level 2.

**The business value:** Compliance becomes a data problem, not a people problem. We run a scan every night. Our compliance dashboard shows: 'You have 147 images in ECR. 144 are compliant. Here are the three you should patch.' Nobody has to read a checklist. The system is the checklist.

**The team impact:** Engineers understand policy is about protecting the business, not gatekeeping. We had zero complaints about security slowing deployments in the last year because the auto-checks run in seconds and the policy reviews are proportional to risk.

**The hard part:** This requires partnership with your security team. If they're adversarial, this doesn't work. I've spent time building trust with security. I ask them: 'What incidents keep you up at night?' Then I point engineering problems at those. When you show security that you care about their actual risks, not just passing audits, they become your allies."

**WHAT NOT TO SAY:**

- ❌ Don't position yourself as the person who will teach security teams how to think. That's arrogant. You're a partner.
- ❌ Don't claim you've eliminated security friction. Say you've shifted it — from high-friction gates to low-friction automation.
- ❌ Don't use technical security vocabulary (CVE scoring, CVSS, supply chain verification). An executive wants to hear "we've reduced risk and sped up shipping."
- ❌ Don't make it sound like you're security-lite. Emphasize that you've accelerated security, not weakened it.

**TIME BUDGET:** 4 minutes. If they ask "What if an engineer argues against a Level 1 block?" answer: "That's a conversation with the security team and the VP of Engineering. It's rare, and the answer is usually 'find a different approach.' But we don't stone-wall. We think together."

---

## Slide 8: Questions I Ask You (3 minutes)

**WHAT TO SAY:**

"Before we wrap, I want to ask you three things. Not because I have an agenda — because the answers will tell me whether I can be effective here.

**Question 1: When your team has a serious incident — let's say a data leak or a deployment that broke something critical — what happens next?** 

I'm listening for: Do you do a blameless postmortem? Or do you look for a person to fire? Does leadership participate? Do you actually change things based on what you learn? Because if the culture is blame-based, no amount of technical brilliance will fix morale. And retention will stay low.

**Question 2: What's the last time a manager or leader on this team told you they were wrong about something?**

I'm listening for: Can they name a specific example? Or do they say 'It happens' without details? Humility from leadership is rare. But it's everything. It gives engineers permission to take risks and admit mistakes.

**Question 3: If I were to talk to your best engineer right now and ask 'What would make your life better?' what would they say?**

I'm listening for: Do you know the answer? Can you articulate it? Because if you can, it tells me that leadership is listening. And if you say 'I'd have to ask,' that's actually honest and I respect it.

These aren't trick questions. They're filters. I'm trying to figure out: Is this a place where I can lead well? Because I can be effective in a lot of environments, but I'm most effective in places where leadership is self-aware."

**WHAT NOT TO SAY:**

- ❌ Don't ask questions where you have a 'right answer' that you're fishing for. That's manipulative.
- ❌ Don't ask about their technical stack or roadmap. You already know that. You're probing leadership health.
- ❌ Don't ask more than three questions. You're not interviewing them. They're still interviewing you.
- ❌ Don't ask 'What's your biggest challenge?' That's too broad. Get specific.

**TIME BUDGET:** 3 minutes. If they give an answer and then ask "Does that make sense?" you've got them thinking. That's good.

---

## Slide 9: Closing (1 minute)

**WHAT TO SAY:**

"I know this was a lot. Let me land on one thing: I'm not here because I need a job. I'm here because I think there's a problem I can help solve. I've done this three times — taken a burned-out team and made it functional, taken a siloed platform and made it a multiplier, taken a security bottleneck and made it a safety net. I know how to do that. And I know it takes patience and partnership. If that sounds like something you need, I'm interested."

[Pause. Let them respond.]

**WHAT NOT TO SAY:**

- ❌ Don't oversell. You've done the work. Let it speak.
- ❌ Don't ask "Do you have any other questions?" That's weak. Let them decide.
- ❌ Don't thank them profusely. Professional and clear is stronger than gratitude.

**TIME BUDGET:** 1 minute max.

---

## Slide 10: Adaptations for Different Contexts

### If This Is A Startup (Series B–D)

**Change Slide 2 (Problem Statement):**
- De-emphasize process and organizational alignment. Emphasize speed and leverage.
- "We had one engineer and they were drowning. I needed to give them 10x leverage."
- Replace SLO discussion with "How do we know we're not leaking money to downtime?"

**Change Slide 4 (Case Study):**
- Use the same SLO example but frame it as "How we went from 40% engineering time on firefighting to 10%."
- Add a line about how this freed up engineering to build new features.

**Change Slide 6 (Platform as Multiplier):**
- Keep this section. Startups desperately need platform thinking. But tone it as "We built a platform because we couldn't hire fast enough. Here's the leverage we got."

**De-emphasize Slide 7 (Security):**
- Don't lead with compliance and policy. Lead with "How we made security a non-negotiable part of the developer experience without slowing us down."
- Mention SOC 2 prep, not HIPAA audit trails.

**Add to Slide 8 (Questions):**
- "What's your growth trajectory? Are we hiring 10 engineers or 100 in the next year?" — This tells you whether the platform scales.

### If This Is An Enterprise (Fortune 500)

**Emphasize Slide 2 (Problem Statement):**
- Add a line about regulatory and compliance context. "We had to ship securely while meeting [HIPAA/PCI/SOX] requirements."
- Frame alert fatigue as "Our on-call burden was unsustainable, and it was a retention risk."

**Expand Slide 4 (Case Study):**
- Add a section about cross-team governance. "We had to align Product, Platform, Security, and Finance. Here's how we built the forum for that conversation."
- Mention working with an Enterprise Architecture team, if relevant.

**Enhance Slide 6 (Platform as Multiplier):**
- Add a line about compliance automation. "We built observability that automatically generates audit trails for compliance reviews. It saves Finance three person-weeks per audit."
- Mention integration with Enterprise governance tools (ServiceNow, Splunk, etc., if relevant).

**Expand Slide 7 (Security and Compliance):**
- This becomes a full story, not a brief mention.
- Add: "We reduced audit findings by 60% by shifting from manual checklist reviews to automated compliance scanning."
- Mention work with CISO/Chief Risk Officer, not just security ops.

**Change Slide 8 (Questions):**
- "How does your security org measure the effectiveness of your controls?" — Shows whether security is strategic.
- "What's your incident command maturity?" — Enterprise cares about structured incident response.
- "How do you handle cross-org dependencies?" — Enterprise is all about dependencies.

---

## Rehearsal Protocol: Six Calibration Questions

**You should be able to answer these cold, in a parking lot, without notes.** Each answer should be 45–60 seconds.

### 1. "Your team is burning out on on-call. What do you do first?"

**Your answer should:**
- NOT start with "I'll hire more people." (Fixes the symptom, not the cause.)
- Start with: "I need to understand what's actually driving the load. Is it alert fatigue, incident complexity, or coverage gaps?"
- Show a sequence: Measure → Root cause → Targeted fix.
- Name something you'd change in the first two weeks.

**Red flags you're failing:**
- You're thinking operationally (shift schedules) instead of strategically (why are we burning out?).
- You're not naming the root cause.

---

### 2. "Tell me about a time you disagreed with your leadership. How did you handle it?"

**Your answer should:**
- Be specific. Name the situation.
- Show that you tried to understand their perspective first. "I asked why they were pushing this direction..."
- Show that you made an argument based on data or team impact. Not emotion.
- Show the outcome: Either they convinced you, or you convinced them, or you found a third path.
- End with: "What I learned is..."

**Red flags you're failing:**
- You sound bitter. "They never listen to their team."
- You sound arrogant. "I was right and they were wrong."
- You don't name a real example.

---

### 3. "A director-level peer on your org is making a decision you think is bad for the company. How do you engage?"

**Your answer should:**
- Start with: "I'd ask to understand their constraints first."
- Show that you assume they have information you don't. "Maybe they're under pressure I'm not seeing."
- Show that you'd make your concerns clear. "I'd lay out the risks as I see them."
- Show that you'd escalate if needed. "If we can't align, I'd bring in our boss and let them decide."
- Show deference. "They're my peer, not my subordinate. I can't make them change. I can only influence."

**Red flags you're failing:**
- You sound political. "I'd lobby their skip-level manager."
- You sound passive. "I'd just do what they want."
- You don't name a real example.

---

### 4. "What's something you're not good at, and how are you working on it?"

**Your answer should:**
- Be honest. Not a strength in disguise. ("I'm a perfectionist" doesn't count.)
- Be specific. "I'm not great at writing documentation. I tend to skip it and assume people will ask questions."
- Show self-awareness. "I know this slows down onboarding and creates bottlenecks."
- Show you're working on it. "I'm using a template-driven approach and I'm pairing with my tech lead on docs. We review every Friday."
- Show progress. "It's better. Not perfect."

**Red flags you're failing:**
- You pick something that's not actually a weakness for a director role.
- You don't name a concrete strategy for improvement.
- You sound defensive.

---

### 5. "What's the difference between an SRE director and a strong IC SRE who got promoted?"

**Your answer should:**
- Show that you've thought about this shift.
- "An IC thinks about making the system better. A director thinks about making the *team* better. At some point, my leverage is through other people, not my own keyboard."
- Give an example of a decision you made that shows this shift. "I chose not to own the incident investigation. I assigned it to an engineer and coached them through it. That took longer, but now two people know how to do the triage instead of one."
- Show that you still code or do deep technical work, but it's intentional. "I'll jump in for the hard incident or code review, but it's 10% of my time, not 50%."

**Red flags you're failing:**
- You sound like an IC trying to act like a director.
- You imply that directors don't code or don't do technical work.
- You don't show examples.

---

### 6. "If you took this role and in 18 months your org had higher churn, lower deployment velocity, and worse morale, what would that tell you?"

**Your answer should:**
- Not start with "That would never happen."
- Start with: "That would tell me I got something wrong."
- Show humility. "Maybe I inherited a problem that's deeper than I thought. Maybe my approach didn't land with this team. Maybe I'm not the right leader for this place."
- Show you'd course-correct. "I'd ask people — not my boss. I'd ask the engineers. 'What am I doing wrong? What do you need?' And I'd listen."
- Show you'd escalate if needed. "If it's a culture mismatch and I can't fix it, it's better to know in 18 months than pretend it'll improve in year three."

**Red flags you're failing:**
- You're defensive.
- You blame external factors without owning your part.
- You don't show willingness to change or leave.

---

## Final Notes on Delivery

**Tone:** Conversational, not a TED talk. This is a two-person chat, not a presentation. Use "I" and "we," not "one might argue."

**Pauses:** Pause after every major claim. Give them room to interrupt. If they do, answer and come back to the narrative. Rigidity reads as brittleness.

**Specificity:** Every story should have a number, a name (or "my team"), and a decision. Not vague. Executives test for vagueness.

**Self-awareness:** Name something that didn't work. Something you'd do differently. This is what separates leaders from bullshitters.

**Authenticity:** You don't have to like the company or the role. You have to be honest about what you can do and what you need. Honesty is more impressive than enthusiasm.

---

**Last thing:** This template is yours to adapt. If your experience is different, use it. If you've never done SLOs, use something you have done (incident command, capacity planning, security alignment). The structure is the point — not the content. The structure says: "I think like a leader, not an IC."

Good luck.
