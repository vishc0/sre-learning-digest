# Module 9: Motivation, Culture, and Psychological Dynamics | Director Leadership Track

---

## Why This Separates Directors from ICs (What Interviewers Are Actually Testing)

ICs deliver work. Managers deliver through individuals. Directors deliver through teams over time — meaning they must sustain engagement across people with different career stages, different motivations, and different breaking points. Interviewers at Director level are not asking whether you can motivate a team in a good quarter. They are asking whether you have the vocabulary, the systems, and the personal discipline to hold a team together through uncertainty, failure, reorgs, and burnout. The question behind every motivation question is: *do you understand people accurately, or do you manage on assumptions?*

---

## The Mental Model: The Motivation Stack

Think of motivation as a stack, not a dial. The base of the stack is hygiene — compensation, stability, fair treatment. Hygiene does not create engagement; it prevents disengagement. You cannot motivate a senior engineer with a raise if what they need is ownership. Once hygiene is satisfied, motivation lives in five drivers:

```
DRIVER          | WHAT IT SOUNDS LIKE                     | YOUR LEVER
----------------|------------------------------------------|---------------------------
Autonomy        | "I own something real"                  | Domain assignment
Mastery         | "I'm growing at the edge of my ability" | Stretch work routing
Purpose         | "My work connects to something that matters" | Impact narration
Belonging       | "I am seen accurately and valued here"  | Recognition precision
Fairness        | "Rewards match contributions"           | Calibration transparency
```

The Motivation Stack failure mode: treating all five as interchangeable. Giving someone more purpose talk when what they actually need is autonomy produces confusion, not engagement. The diagnostic skill — figuring out which driver is actually low — is what separates Directors from managers who apply generic motivation tactics.

---

## The Framework in Practice: Diagnosing and Acting on the Stack

**Step 1: Diagnose which driver is depleted**

In a 1:1, ask: "When was the last time you were genuinely energized at work? What were you doing?"

The answer maps directly to the driver. "I was debugging the consumer lag issue and figured out the root cause before anyone else" = mastery. "I finally shipped the alerting framework I designed" = autonomy + purpose. "The CTO mentioned my name in the all-hands" = belonging. "I got the promo I'd been working toward for two years" = fairness.

Then ask the inverse: "Is there anything about your current work that's starting to feel like maintenance rather than growth?" The gap between those two answers is where you work.

**Step 2: Match intervention to driver**

| Driver Depleted | Wrong Intervention | Right Intervention |
|---|---|---|
| Autonomy | Give them more interesting tickets | Give them a domain they own end-to-end |
| Mastery | Give them praise for current work | Route stretch work they cannot fully do yet |
| Purpose | Tell them the company vision | Show them the specific line from their work to user/business outcome |
| Belonging | Throw them a team lunch | Name their specific contribution in the right room at the right time |
| Fairness | Say "I appreciate everything you do" | Be explicit about how decisions are made and where they stand |

**Step 3: Narrate the connection**

Recognition that sticks names the action, the judgment, and the consequence.

Hollow: "Great job on that incident."

Specific: "During the RabbitMQ cascade on Tuesday, you read the consumer lag pattern in Splunk 40 minutes before any alert fired and pre-scaled before anyone asked you to. That's not junior instinct — that's someone who has internalized the system well enough to see around corners. That call prevented an SLA breach."

The formula: **specific action + specific judgment demonstrated + specific consequence prevented or enabled.**

---

## What Good Looks Like at Director Level

- You know each engineer's primary motivation driver without having to look at notes
- You route work deliberately — stretch assignments are not random, they are matched to who needs mastery right now
- Recognition is specific enough that the person knows you actually understood what was hard
- 1:1s surface problems before they become attrition — you are not surprised when someone is close to leaving
- You have a different management posture for each person based on what they actually need, not a uniform approach
- When you give difficult feedback, the person leaves the room with clarity about what to change, not a wound to process
- You publicly model receiving feedback — you ask for it, and you respond to it visibly

---

## What Bad Looks Like (How Directors Fail Here)

- Applying the same management style to everyone — the "fair" manager who treats everyone identically ends up being effective for no one
- Confusing retention with engagement — someone staying is not the same as someone thriving
- Generic recognition: "Thanks for all your hard work" said in a team Slack becomes noise after the third occurrence
- 1:1s as status updates — you learn nothing about the person, only about the ticket
- Waiting for disengagement to become visible before acting — by the time an engineer is obviously checked out, you are already six months behind
- Giving feedback only in performance cycles — feedback should never be a surprise in a review
- Punishing the person who surfaces a problem — this teaches the entire team to hide problems
- Narrating uncertainty with false confidence — "everything is fine" when it isn't destroys credibility irreversibly

---

## Tools and Templates

### Tool 1: The 1:1 Question Library (20 Questions)

Use one or two per session. Never work through the list top-to-bottom. Rotate based on what you are trying to understand.

**Opening / surface what they won't volunteer:**
1. "What's the hardest part of your week that nobody else saw?"
2. "What problem are you thinking about at 2am that you haven't brought to me yet?"
3. "What are you proud of this week that didn't get enough recognition?"
4. "What's something you're working on that you think I don't fully understand?"
5. "If you were me, what would you change about how this team is run?"

**Surface hidden blockers:**
6. "What's the one thing I could remove from your plate that would make you 30% more effective?"
7. "Who on the team — or outside it — is making your work harder than it needs to be?"
8. "What decision are you waiting on that's slowing you down?"
9. "Is there anything you've been avoiding because you think it will cause conflict?"

**Career and motivation signals:**
10. "When was the last time you were genuinely energized at work? What were you doing?"
11. "Is there anything about your current work that's starting to feel like maintenance rather than growth?"
12. "Where do you want to be in two years, and are we giving you work that moves you toward that?"
13. "Is there a domain or technology you want to go deeper on that we haven't given you a chance to touch?"

**Team dynamics:**
14. "Who on the team do you think is underutilized?"
15. "Is there tension on the team I should know about that you'd be comfortable sharing?"
16. "How do you think new team members experience joining this team?"

**How they see you:**
17. "Is there anything I've done recently that frustrated you or felt wrong? I'd rather hear it directly."
18. "Do you feel like I understand what you actually do well enough to represent you to leadership?"
19. "Is there a type of support you need from me that you're not getting?"
20. "If you could redesign your role on this team from scratch — what would you keep, remove, and add?"

**1:1 cadence rules:**
- Weekly 30-minute format: 10 minutes theirs (one question, mostly listening), 10 minutes blockers, 10 minutes one longer topic
- Monthly: one 1:1 entirely for career — no status, no blockers
- Skip-level (talking to your team's team): open with "I'm here to listen, not to evaluate. Nothing said here goes to your manager in a way that identifies you." Ask questions 14-16, then questions 6-9. Never use a skip-level to gather performance data — that poisons it
- What NOT to do: surprise negative feedback in a 1:1, status-update-only sessions, skipping 1:1s during busy weeks (this is exactly when they matter most)

---

### Tool 2: The SBI Feedback Template

**S = Situation**: specific time, place, context — not "lately" or "often"
**B = Behavior**: observable action only — not interpretation, not character
**I = Impact**: what actually happened as a result, in specific terms

**Filled example for a defensive senior engineer:**

"I want to give you some direct feedback. I'm doing it now because I think you're capable of better than what I've been seeing, and you deserve to hear it from me directly — not in a performance review.

**Situation**: In the last three sprint planning sessions — specifically Tuesday, the week before, and two weeks ago — during technical proposal discussions.

**Behavior**: When another engineer proposed an approach you disagreed with, you cut them off before they finished their point. I saw it most clearly on Tuesday when [name] was walking through the caching proposal.

**Impact**: After that moment, the other engineers in the room stopped contributing. We spent the next 20 minutes on your counter-proposal without hearing what [name] was going to say. We may have made a better decision with the full information.

What's your read on how those conversations are landing with the team?"

**The last question is not optional.** It opens the floor before you prescribe a fix. If they already know, you are co-designing the solution, not delivering a verdict.

**Closing SBI**: "What I'm asking for going forward is specific: in the next planning session, let other engineers finish their point before you respond. Can you do that?" Get a specific yes, not a vague acknowledgment.

**Feedback medium rules:**
- Verbal first for negative feedback — writing creates a record before you know the full story
- Written to confirm after the conversation: "Following up on what we discussed Tuesday — [agreed change]"
- Never written-only for critical feedback — it removes your ability to read the reaction and adjust
- Follow-up at the next 1:1: "I wanted to check in on what we talked about last week." The follow-up is what separates feedback from change.

---

### Tool 3: Motivation Assessment Tool

Run this diagnostic quarterly for each direct report. Takes 10 minutes in a 1:1.

```
DRIVER          | SIGNAL QUESTIONS TO ASK              | LOW SIGNAL TO WATCH FOR
----------------|--------------------------------------|--------------------------------
Autonomy        | "Do you feel like you own your work  | Waits to be told what to do;
                |  or are you executing someone else's  | no initiative on domain decisions
                |  decisions?"                         |
----------------|--------------------------------------|--------------------------------
Mastery         | "Are you learning anything you        | Executes perfectly but never
                |  couldn't do three months ago?"       | volunteers for new problems
----------------|--------------------------------------|--------------------------------
Purpose         | "Can you draw a line from what you   | "It doesn't really matter, I
                |  shipped last month to something that | just close tickets"
                |  actually mattered?"                 |
----------------|--------------------------------------|--------------------------------
Belonging       | "Do you feel like people here know   | No spontaneous sharing; only
                |  what you're actually capable of?"   | engages when directly addressed
----------------|--------------------------------------|--------------------------------
Fairness        | "Does the distribution of rewards    | Watches promotions of peers
                |  and recognition here make sense     | closely; brings up comp without
                |  to you?"                            | being asked
```

Score each 1-3 (1 = depleted, 3 = satisfied) in your notes. If two or more drop to 1 simultaneously, you have an attrition risk. Act within two weeks.

---

### Tool 4: Psychological Safety Checklist (4-Stage Model)

The four stages of psychological safety, in order of development:

**Stage 1 — Inclusion safety**: "I can be myself here without fear of rejection"
- Signal: People share personal context, admit when they don't know something, ask basic questions
- Killer: Any response to a question that implies the person should have known better

**Stage 2 — Learner safety**: "I can ask questions and make mistakes without punishment"
- Signal: Engineers flag problems early; incidents get surfaced before they escalate
- Killer: Any reaction to a mistake that focuses on blame before learning

**Stage 3 — Contributor safety**: "I can offer ideas and push back without being dismissed"
- Signal: Engineers bring proposals without being asked; disagree with you openly
- Killer: Consistent overriding of technical judgment without explanation

**Stage 4 — Challenger safety**: "I can challenge the status quo, including leadership direction, without retaliation"
- Signal: An engineer tells you a direction you set is wrong, and is right, and you say so
- Killer: Any visible consequence for being right when it was inconvenient

**Director behaviors that accidentally kill psychological safety:**

| Behavior | What You Think It Does | What It Actually Does |
|---|---|---|
| Answering your own question in a meeting | Moves things forward | Teaches people not to answer your questions |
| Saying "great point" to everything | Signals openness | Signals you're not actually evaluating |
| Skipping postmortems when you're busy | Saves time | Signals incidents are managed, not learned from |
| Not pushing back when leadership is wrong | Picks battles wisely | Teaches your team that hierarchy beats truth |
| Sharing 1:1 content without permission | Surfaces problems | Teaches people never to be honest in 1:1s |

**Blameless postmortem as culture-building (not just process):**

The postmortem is not the artifact. The postmortem is the evidence — visible to the team — that you believe the system failed, not the person. Every postmortem where you redirect from person to system teaches the team that surfacing information is safe. Every postmortem where someone feels blamed undoes months of trust-building.

Opening the meeting: "Before we start: I want to name that incident reviews have sometimes felt like a search for someone to blame. That is not what I'm doing. If the system allowed a human to make a mistake, the system failed. I need everyone honest in this room. What's said here stays here unless it becomes a documented action item."

Facilitation: Ask "walk me through exactly what happened, in order, from the first signal." When you hit a gap: "What information did you have at that moment? What options did you see?" — this removes hindsight bias from the conversation.

When someone deflects to blame: "I hear that. Let's come back to the system design that made that the path of least resistance."

Every action item: one owner, one date, one measurable done-state. No action item assigned to "the team."

---

### Tool 5: Difficult Period Communication Scripts

**Company instability (layoffs nearby, bad earnings):**

"I want to be straight with you about where we are. [Specific uncertain thing — headcount, budget, org structure] is genuinely not decided yet. I don't know the answer and I won't pretend I do. What I can tell you is [specific certain things — your team's mandate, a funded project, a commitment you personally have made]. In uncertain periods, I try to make sure you're working on things that matter regardless of how the uncertainty resolves."

What not to say: "Everything is fine" when it isn't. "I can't share anything." "Don't worry about it." Each of these teaches your team you will not tell them the truth when it is inconvenient.

**After a major incident (rebuilding confidence without glossing over):**

"What we went through last week was hard and I don't want to paper over it. [Specific thing that failed]. At the same time, I want to name what I actually saw from this team: [specific person] caught the consumer lag signal before any alert fired. [Specific person] managed the customer escalation thread for six hours straight. The incident exposed a gap in [specific system], not a gap in this team. The postmortem action items are concrete. Let's close them."

Do not hold a pep talk that doesn't acknowledge the failure — engineers are not children, and they know when something went wrong. The confidence rebuild comes from naming the failure accurately and then naming what comes next.

**During a reorg (keeping people focused when everything feels uncertain):**

"I know what's circulating. Here's what I actually know: [specific facts]. Here's what I don't know yet: [specific uncertainties]. My intention is to tell you what I know as soon as I know it. In the meantime, the work on [specific project] is real and funded, and I need your focus there. I would rather have you ask me a direct question than speculate in Slack."

**Technical debt spiral (demoralized by the codebase):**

"I hear you on the state of the codebase. I'm not going to pretend it's in better shape than it is. What I want to do is carve out real capacity — not a 20% aspirational bucket, actual sprint slots — to address [specific highest-pain area]. I want you to own the proposal for what we fix first and why. That means you're setting the direction on this, not just executing a cleanup list I hand you."

**When you are demotivated as a Director:**

This one is not in most management books. Directors are allowed to have off quarters. What you owe your team is that your demotivation does not become their problem. Three practices:

1. Separate your state from your signals — your team reads your affect as organizational data. If you walk into a meeting visibly discouraged, they conclude something is wrong with the team.
2. Find one thing in the quarter that is genuinely yours to build — something that matters to you independent of org politics. This is your anchor.
3. Be honest with your own manager: "I'm in a lower-energy period. I need [specific thing]." Directors who cannot ask for what they need model exactly the behavior they are trying to eliminate in their teams.

---

## Decision Matrix: When to Do X vs. Y

| Situation | Do This | Not This | Why |
|---|---|---|---|
| Engineer is disengaged | Ask "what would make this worthwhile again?" | "I've noticed you seem disengaged" | Accusatory frame produces defensiveness, not honesty |
| High performer seems stretched thin | Name specific behavior; ask about bandwidth before assuming | Wait until they tell you | By the time they tell you, attrition risk is already high |
| Team conflict | Separate conversations first, then joint | Jump straight to mediation | You need unfiltered individual perspective before facilitating |
| Giving feedback | SBI + specific ask + follow-up date | Annual review surprise | Feedback at the point of behavior is information; months later is a verdict |
| Reorg uncertainty | Separate certain from uncertain; name both | False confidence or total silence | Engineers are more resilient to truth than to finding out you hid it |
| Someone is burned out | Remove actual work; don't just offer support | "Everyone is under pressure" | The framing makes their burnout a personal weakness |
| Your own mistake | Acknowledge specifically, in the same forum | Minimize, explain, deflect | Explanation reads as excuse; costs more trust than the mistake |
| Engineer has ego problem | Redirect to "ask the best questions" frame | Try to humble them | You cannot shrink a strong ego; you can channel it |

---

## People Scenarios

**Scenario 1: The one that saves someone from quitting**

An engineer who has been on your team for three years is slow to respond, stopped bringing ideas, and says "sure, I'll take it" to everything. These are checked-out signals, not burned-out signals.

"I want to be honest with you about something. I feel like we've drifted. I'm not sure I'm giving you what you need right now, and I think that's on me to fix. Can you help me understand what would make this feel worthwhile again?"

If they give a vague answer: "If you could redesign your role on this team from scratch — what would you keep, what would you remove, what would you add?"

If after that conversation you sense they have a better opportunity and are coasting: "If you've decided this isn't where you want to build, I'd rather help you land well somewhere great than watch us both waste the next six months. I'm not pressuring you — I'm just telling you I'd rather be a good exit for you than a frustrated manager." This is counterintuitive but often re-engages people because it signals you respect their autonomy more than your headcount.

**Scenario 2: Critical feedback to a defensive person**

"I'm giving you this feedback directly because I think you're capable of better than what I've been seeing, and you deserve to hear it from me — not in a performance cycle."

[Deliver the SBI]

If they get defensive: "I don't need you to agree with me right now. I need you to think about it. Can we revisit this in our 1:1 next week?" Then follow up. The follow-up is what separates feedback-givers from change-makers.

**Scenario 3: Building trust with a burned team (90-day sequence)**

Days 1-30: Listen only. In the first team meeting: "I've read the docs. But I want to understand what it's actually like to be on this team. I'll be scheduling 1:1s with each of you. My only goal is to listen. Nothing you tell me will be used against you." Then follow through exactly — this is the entire test.

Days 30-60: Deliver one visible win they asked for. "I heard you about [specific thing]. I went and talked to [person]. It's done." Do not try to score ten small wins. One specific, visible win changes the belief from "they say things" to "they do things."

Days 60-90: Name the dysfunction honestly. "I've noticed we don't surface problems early because historically surfacing them hasn't felt safe. I want to change that. Here's how I want us to handle [specific problem type] going forward."

**Scenario 4: Your own public mistake**

The notification platform had a degradation. Your call to delay the rollback by 30 minutes was wrong. You need to address this with the team.

"I made a wrong call on Thursday. I told the team to hold on the rollback while we gathered more data. We lost 30 minutes we shouldn't have. The right call was to roll back at 11:15 when [specific signal] appeared. Going forward, our rollback threshold is [specific criterion] — we do not wait for additional confirmation past that point. I've updated the runbook."

Then stop. Do not add "but the data was ambiguous at the time." The explanation reads as excuse.

---

## How to Talk About This in Interviews

**What they're actually asking when they ask motivation questions:**

"Tell me about a time you motivated a struggling team" = can you diagnose what's actually wrong or do you apply generic tactics?

"How do you handle a high performer who's checked out?" = do you have the courage to have direct conversations and the skill to do it without pushing people further away?

"How do you build psychological safety?" = do you understand it as a specific set of behaviors or do you treat it as a vibe?

**Phrases to use:**
- "I diagnose the motivation driver first before intervening — autonomy, mastery, purpose, belonging, and fairness require different responses."
- "Recognition that sticks names the specific action, the judgment it demonstrated, and the consequence it prevented or enabled."
- "Psychological safety is not a feeling you create — it's a set of behaviors you demonstrate consistently, especially when it's expensive to do so."
- "The 1:1 is for the engineer, not for me. If I'm talking 50% of the time, it's not a 1:1, it's a status update with audience."

**What to avoid:**
- "I believe in open communication" — says nothing
- "I try to keep morale high" — no mechanism
- "I give people autonomy" — what does that actually mean in practice?

**STAR framing anchored to T-Mobile:**

Situation: "We had a 36-month zero-Sev1 streak and a platform handling 25M messages per day. The team had delivered well and was starting to plateau — the challenge shifted from capability to sustained engagement."

Task: "I needed to keep a high-performing team growing through a period with no major fires, no big launches, and organizational uncertainty around headcount."

Action: "I ran quarterly motivation diagnostics in 1:1s — specifically looking at which of the five drivers had gone flat. For three engineers, mastery was low — they were executing well but not growing. I routed them to the chaos engineering program we were building, which was at the edge of their capability. For two others, purpose had dropped — they couldn't see the connection between their platform work and end-user outcomes. I started sharing anonymized customer impact data from the notification platform in team meetings: X million messages delivered for [specific campaign], Y revenue events triggered."

Result: "Attrition on the team over that period was zero. More importantly, the engineers who went through the chaos engineering stretch became the people I relied on for architectural decisions — it compounded."

---

## T-Mobile Anchors

**Your zero-Sev1 streak is a culture artifact, not just an ops metric.** Thirty-six months without a Sev1 on a 25M msg/day platform does not happen by accident. It is the result of a team where psychological safety is high enough that problems surface before they become incidents. Name that in interviews: "The streak is evidence that my team feels safe surfacing signals early."

**Six zero-downtime migrations** require a team that runs toward hard problems, not away from them. That is mastery driver satisfied — people who have done a zero-downtime migration of a production platform at that scale have had their growth needs met. Name the mastery dimension when you talk about these.

**Managing 15 people onshore and offshore** means you have navigated belonging and fairness across time zones, cultures, and visibility gaps. Offshore engineers are at perpetual risk of purpose depletion — their work is real but the connection to outcome is often invisible. If you have practices for narrating impact across geographies, name them.

**The platform you run is the connective tissue for customer-facing notifications at T-Mobile.** That is purpose at scale. If your engineers know that, and if they can point to a specific moment where their infrastructure decision shaped a customer interaction, you have satisfied the purpose driver at a level most teams never reach. Make sure they know it.

---

## Drills

**Drill 1 — Motivation Diagnosis**
Prompt to use with Claude: "I have an engineer, 8 years of experience, has been on the team for 3 years. Last 6 months: execution is flawless, no complaints, but they've stopped bringing proposals to architecture discussions and stopped volunteering for new projects. They respond to everything with 'sure, I can take that.' Which motivation driver is likely depleted? What is my diagnostic question for the next 1:1? What is my intervention if I'm right?"

**Drill 2 — SBI Practice**
Prompt to use with Claude: "Give me a scenario where a senior engineer on my SRE team is consistently making architectural decisions in isolation without consulting peers, which is creating integration problems downstream. I need to give them feedback using the SBI model. They have a history of reacting defensively when given feedback. Write the full script for the conversation including the opening, the SBI, the question I ask before prescribing a fix, the specific change I'm asking for, and the close."

**Drill 3 — Difficult Period Communication**
Prompt to use with Claude: "My company just announced a hiring freeze and there are rumors of a 10% RIF in Q2. My team is a 15-person SRE function. I need to communicate to them at the next team meeting. Some things are certain: our platform's budget is protected for this fiscal year. Some things are uncertain: headcount for new hires, the RIF scope and timeline, whether my VP's org is affected. Write the script for what I say in the team meeting — including what I say I know, what I say I don't know, and how I close in a way that keeps people focused without lying."

---

*This module is a practitioner reference. Return to it before a hard conversation, not after. The frameworks are stable. The scripts are starting points. The discipline is: specific behavior, specific language, specific follow-through. Generality is where leadership intentions go to die.*
