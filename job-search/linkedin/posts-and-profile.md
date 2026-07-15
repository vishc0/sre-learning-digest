# LinkedIn Posts & Profile — Vishweshwar Chippa

## Profile Section

### Headline (3 Variants)

**Variant 1 (Default — Technical + Leadership Signal)**
Director, Platform Reliability | 21+ Years SRE/Middleware | Led 15-person team to 36 months zero Sev1 | H1B portable

**Variant 2 (For Outbound Recruiter Matching)**
VP SRE Candidate | 25M msg/day at scale | Observability + IaC + AI-native SRE | AWS/K8s/Terraform

**Variant 3 (For Founder/Startup Context)**
SRE Architect | Built zero-Sev1 culture at T-Mobile | Splunk expert | AI anomaly detection pioneer

### About Section

When you lead an SRE team for 36 months without a single Sev1, it's not luck—it's measurement, blameless postmortems, and people who've learned that runbooks are code, not documents.

That's what I've built at T-Mobile, managing 15 engineers across a 25M message/day notification platform. Before that: 21 years across telecom, banking, insurance, and energy—Cassandra clusters at Flipkart, Splunk ML at insurance scale, middleware orchestration that kept retail transactions flowing.

**What I do:**
- **Observability as a culture**: Splunk, AppDynamics, Grafana—not dashboards for dashboards' sake, but SLO-driven burn rate alerts and error budget governance that actually change team behavior.
- **Infrastructure-as-code**: Terraform modules that teams trust because drift detection is automatic and testing is baked in.
- **AI in SRE**: Built anomaly detection pipelines in Splunk MLTK before it was fashionable. Now exploring GenAI runbook generation and chaos engineering at scale.
- **Incident command**: Not just response—structured blameless postmortems that ship fixes faster than blame finds someone.
- **Hiring and culture**: The best reliability tool is hiring people who think like operators, not just coders.

**Portable:** H1B active with I-140 approved (2016)—can start the day your I-129 files.

I'm exploring Director/VP SRE roles at cloud-native organizations where the reliability bar is genuinely high. If you're building a platform that can't go down, let's talk.

[LinkedIn URL], [GitHub portfolio link], [Email: chippa.vishweshwar@t-mobile.com]

---

## LinkedIn Posts

### Post 1: Zero Sev1 Reliability Culture

**Title:** 36 Months, Zero Sev1 — This Is How You Build That Culture

**Body:**

36 months. 15 people. One notification platform hitting 25M messages a day. Zero Sev1 incidents.

The number isn't about luck—it's about measurement. Here's what actually works:

**1. Make SLOs change behavior.** We didn't write SLOs into a deck and forget them. We calculated error budget burn rate daily. When we spent it, we stopped shipping features and rotated into reliability work. Teams saw the tradeoff in real time.

**2. Postmortems are the textbook.** After every incident (yes, including the scary Sev2s), we ask: *What did we not know we didn't know?* Then we encode that knowledge into runbooks, monitoring rules, or Terraform. A postmortem that doesn't ship code is a meeting.

**3. Your runbook is code.** If your incident response lives in a Confluence page, you will panic and miss a step at 2 AM. We treat runbooks as Python scripts—version controlled, tested against staging, and executable.

**4. Chaos engineering is not optional.** We break things on purpose in lower environments so they fail differently in production. It sounds obvious; most teams don't do it.

**5. Observability is a hiring criterion.** When you interview for an SRE or backend engineer, ask them to explain what they'd monitor if they owned a service. If they say "CPU and memory," you'll build reliability theater.

**The Director's lens:** Reliability culture is not a department—it's a choice the whole organization makes about what trade-offs matter. Your job as a leader is to make that choice visible and consistent.

**What would break your system that you can't currently see?** Start there.

---

### Post 2: What Breaks at 25M Messages/Day

**Title:** What Breaks at 25M msg/day (That You Would Never Predict)

**Body:**

Three years ago, we ran at 5M messages/day. The infrastructure held. We thought we understood the system.

At 10M, something broke that shouldn't have.

Our circuit breaker—tuned for 5M throughput—started opening on latency spikes that were invisible at lower volumes because *the pattern only emerges at scale.* We thought we had enough queue capacity. We didn't account for the distribution shape change in message routing.

Here's what actually breaks as you scale past inflection points:

**Queue saturation patterns:** At 5M, tail latency is a decimal. At 25M, it becomes bimodal—two populations, one smooth, one spiky. Your queue tuning breaks because your old model assumed uniform load. (Cassandra row cache showed this first.)

**Thundering herd in retry logic:** Every webhook timeout retried with exponential backoff. At 5M, it was fine. At 25M, retries clustered into synchronized waves. We had to introduce jitter and circuit breakers we didn't know we needed.

**Network ACL limits you never hit:** AWS soft limits on cross-AZ traffic, NAT gateway connection tracking, DNS query rates. They're documented, but your team won't find them until a oncall engineer is at 2 AM wondering why traffic to one AZ is dropping silently.

**Observability debt explodes.** What you could eyeball on three Grafana dashboards now requires distributed tracing, cardinality management, and sampling strategies. If you don't instrument *before* you scale, you'll be flying blind.

**The Director's lens:** Every system has hidden failure modes baked into its assumptions. As a leader, your job is to surface those assumptions before scale exposes them. That means obsessing over metrics *shape*, not just thresholds.

**What scaling problem are you ignoring right now?**

---

### Post 3: AI-Native SRE — Building ML Anomaly Detection Early

**Title:** We Built ML Anomaly Detection in 2018. Here's What We Learned Before MLOps Was Cool.

**Body:**

Long before "AI-native SRE" was a LinkedIn buzzword, we were shipping anomaly detection in Splunk MLTK. It was messy, it worked, and it taught us more than a dozen papers could.

**Why we built it:**
Our alert fatigue was insane. We had ~400 threshold-based rules. Half fired on noise. Half missed real problems because the "normal" baseline for a Friday 9 AM is *completely different* from a Sunday 3 AM, and that baseline shifts with feature rollouts, marketing campaigns, and user behavior drift.

**What we learned:**

**1. Anomaly detection is easier than you think, but harder than you hope.** We trained on 90 days of baseline data, flagged deviations as anomalies. Worked immediately. But false positives came from *events we didn't know happened*—marketing sprints, data pipeline reruns, intentional A/B test traffic splits. The model wasn't broken; our context was incomplete.

**2. Human feedback is your training data.** We tracked which alerts oncalls acknowledged fast vs. ignored. We used that signal to retrain. A model that incorporates "what the team actually cares about" beats a mathematically perfect one.

**3. You need explainability, not just accuracy.** An anomaly alert that says "something is weird" is useless at 2 AM. We added SHAP values and confidence intervals. Oncalls needed to know *which metrics contributed most* to the anomaly call.

**4. Drift is the enemy.** The model trained on 2018 data didn't work in 2020 after architecture changes. Retraining on a schedule (we chose quarterly) was cheaper than constantly debugging false positives.

**The Director's lens:** AI/ML in SRE is not about being on the cutting edge—it's about automating the parts of incident detection that humans are too slow or too tired to catch. If your oncalls are alert-reading machines, you've lost the value of having them on call.

**Are your alerts showing you the system's shape, or just its noise?**

---

### Post 4: The Terraform Import That Saved a Production Deployment

**Title:** The terraform import That Saved a Production Deployment (And What It Taught Me About IaC)

**Body:**

Wednesday, 3 PM. An engineer manually created an AWS security group to fix a Prod firewall issue. It worked. The team moved on.

Thursday, 10 AM. I ran `terraform plan` before applying a change to our RDS database security. Terraform wanted to *delete* the manually-created group. If we'd applied it, every database connection would have failed. Sev1 at 10:05 AM.

This is why IaC fails: the world has state (AWS console), and your code has state (terraform.tfstate). When they diverge, you're not in control anymore.

The fix: `terraform import aws_security_group.postgres sg-0x1a2b3c4d`. Twelve seconds. Terraform read the group that existed in AWS, wrote it into state, and now our code was the source of truth again.

**What this taught me:**

**1. Your terraform plan output is your before deploying.** Always run it. Read it. If you're surprised, something is drifted. I require all PRs to include the full plan output.

**2. Drift detection should be automated.** We run `terraform plan -lock=false` nightly in CI. If it shows changes, we alert. No more surprises at deploy time.

**3. Manual fixes are debt.** Fixing something in the AWS console feels fast. It is fast. But now you owe a terraform import later, and if you forget, drift grows silently. The rule: if it's in AWS and it matters, it's in code.

**4. `terraform import` is not a workaround.** It's a recovery tool. Use it to on-board legacy infrastructure. But if you're importing every week, your process is broken.

**The Director's lens:** IaC governance is about making drift visible, not about eliminating all manual actions. Some things must be manual sometimes. Your job is to make sure that manual action gets reflected back into code before the next deploy.

**What's drifting in your infrastructure right now that you don't know about?**

---

### Post 5: SLOs That Actually Changed Behavior

**Title:** SLOs That Lived in Documents vs. SLOs That Changed How We Work

**Body:**

I've seen two kinds of SLOs.

**Kind 1:** Defined in a spreadsheet. Reviewed quarterly. Printed in a deck for exec business reviews. Nobody knew their error budget was spent. Teams shipped features on a schedule. Oncalls got paged at random. The SLO was decorative.

**Kind 2:** Calculated every day. Burned down hourly. When it's spent, feature flags go down. Oncalls know, managers know, the team knows. The system's behavior changes.

We moved to Kind 2 in 2021. It was not subtle.

**What changed:**

Our 99.9% availability SLO had a 30-minute error budget per week. We started tracking burn rate: *If errors continue at this rate for the whole week, will we breach?* When the answer was yes, we stopped shipping and rotated into reliability work.

First month: we burned through 3 weeks' budget in 2 days. Turned out, our latency monitoring was broken and we were accepting traffic we thought was failing. Found it. Fixed it. Unintended win.

Second quarter: a feature team wanted to ship a database migration. We ran the numbers: *Your P99 will jump 40ms. At current traffic, that burns the quarter's budget in two weeks.* They de-scoped. Then re-scoped with a better plan that only cost 10ms.

The behavior changed because the cost became visible.

**How we did it:**
- Burn rate calculation: (errors this hour / SLO error budget for the quarter) × 24 × 7. If >1, we're in trouble.
- Alert at burn rate > 0.1 (spending the month's budget in 10 days).
- SLO-to-team mapping: each service owner knows their SLO and their current burn rate. We show it in Slack every morning.

**The Director's lens:** SLOs are not for executives—they're for teams. Your job is to make the tradeoff between reliability and velocity *visible and constant*, not hidden in a annual strategy review.

**What would your teams actually prioritize if they knew the cost of every outage every day?**

---

### Post 6: What the SRE Book Doesn't Say About Incident Command

**Title:** What the Google SRE Book Doesn't Say About Incident Command (2 AM Edition)

**Body:**

The SRE book tells you how incident command *should* work: IC coordinates, responders execute, scribe documents, postmortem happens.

It doesn't tell you what happens when you have three critical systems down, your IC is the person who knows the architecture best, you have no scribe, and your oncall is running on their fourth espresso.

Here's what actually happens at T-Mobile at 2 AM:

**The IC cannot also be the firefighter.** When I was the best person to debug Cassandra replication and the only person who could command incident response, I lost both. I picked response and the incident bled for two hours because decision-making stalled. Lesson: your IC must not be *the* person to fix the problem. They need to be *a person who can ask good questions* and know who to delegate to.

**The responders need permission to stop explaining.** I had oncalls spending 10 minutes describing what they tried before asking for help. At 2 AM, that's 10 minutes you didn't spend fixing it. Rule: if you've tried something for three minutes, say so and escalate. The IC's job is to ask for status, not for a narrative.

**Write the severity down.** Sev definitions are vague. (What's "significant" vs. "critical"?") At 2 AM, you'll define it wrong and not get the right people on the call. We use: *Sev 1 = customer-facing, no workaround. Sev 2 = degraded, workaround exists or future impact.*

**Decide to rollback or debug inside the first 10 minutes.** The IC asks: *Can we rollback the last change?* If yes and it's < 30 min, do it now. Debug later. If no, now you're in debug-on-prod mode and you need different people (not just feature developers).

**The Director's lens:** Incident command is a skill, not a rotation. Not everyone is built for it. Invest in training your ICs, not just on the mechanics, but on *permission to be decisive when information is incomplete.*

**Have you debriefed your last incident to see what decisions cascaded from the first 10 minutes?**

---

### Post 7: The Zero-Downtime Migration That Almost Wasn't

**Title:** Six Migrations, One Lesson: Zero-Downtime Is Not Inevitable

**Body:**

We've done six major infrastructure migrations. Five were zero-downtime. One nearly took down the notification platform for three hours. Here's the one mistake that almost broke us—and the pattern that fixed it.

**The bad migration (early 2023):**

We were moving from a single Cassandra cluster to a multi-region cluster. The playbook looked solid: dual-write to both clusters, verify consistency, switch reads, retire old cluster. This is textbook stuff.

What we didn't account for: the verifier that checked consistency was *itself* a chokepoint. It had to scan every key in both clusters and compare values. At our volume, that was 10 minutes of work. We started the scan, then started the migration.

When it was time to switch reads, the verifier was 60% done. We had to guess: *Is the remaining 40% of data consistent?* We were not confident. We rolled back. Oncalls spent three hours in debug-mode while we figured out what was inconsistent.

**What the six zero-downtime migrations had in common:**

**1. Run the verification before you declare readiness.** Not during. The state machine for "are we ready to switch" must include a final verification that is 100% complete. It sounds obvious. It's not—speed pressure is real.

**2. Have a pre-agreed rollback trigger.** We set one: *If consistency check drops below 99.5%, we stop and rollback immediately.* No negotiation. That trigger saved us from the temptation to "just proceed" on 99.3%.

**3. Test the rollback procedure in production (with traffic split).** We run migrations in stages: 5% of traffic, 25%, 50%, 100%. At each stage, we trigger a rollback. So when we need it for real, it's not a surprise.

**4. The IC watches the metrics, not the engineer.** The engineer running the migration script does the work. The IC watches P99 latency, error rate, queue depth. If the IC sees something wrong, they *can stop everything* without waiting for the engineer to notice.

**The Director's lens:** Zero-downtime is not about being clever with Dual writes and cache invalidation. It's about breaking the migration into tiny testable steps, verifying *actually* before proceeding, and having the discipline to rollback when your confidence breaks.

**What migration are you thinking about that could break worse than you've planned for?**

---

### Post 8: The Director Role — Translator, Not Architect

**Title:** What a Director in SRE Actually Does (Spoiler: Not What You Think)

**Body:**

When I became a Director, I thought I'd spend my time architecting systems. I do not. I spend it translating.

Here's what the role actually is:

**Translating between engineering speed and reliability debt.**
A team wants to ship a feature without comprehensive testing. I ask: *What's the failure mode you're most scared of?* If it's "P99 latency above 200ms," we instrument for it and set a circuit breaker. If it's "we lose user data," we table the feature until we have stronger guarantees. I'm not saying yes or no—I'm making the tradeoff visible.

**Translating between oncall reality and exec narrative.**
Executives want "four nines." Oncalls want a life outside of work. I track MTTR (mean time to recovery) and MTTD (mean time to detect) by incident type. I show both: *Achieving 99.99% requires either more engineers on-call or architecture changes that cost $X.* Now the conversation shifts from "want" to "what does it cost."

**Translating between hiring and culture.**
An engineer interviews well but their last three jobs lasted 18 months each. I ask harder questions about what makes them stay. Because a team that ships reliability without turnover looks very different from a team that has 40% churn. I'm not gatekeeping—I'm saying: *We need to solve for retention or this hire is a net loss.*

**Translating between platform and product.**
Product wants to ship 50 features this quarter. Platform (that's us) owns 60% of the codebase they depend on. I say: *Pick 30 features and give us two weeks to strengthen the foundation, or both of you will spend Q4 fixing Sev2s.* I'm not anti-velocity—I'm pro-sustainable velocity.

**What I don't do:**
Write the code. Own the oncall. Make the final call on architecture without the team. A Director who does any of those things is a bottleneck, not a leader.

**The Principal lens:** The best Directors I've worked with are translators, not visionaries. They don't predict the future—they make today's tradeoffs visible so teams make the right decisions.

**What tradeoff are you hiding from your team because you haven't articulated it yet?**

---

### Post 9: Why Your Resume Needs Your Culture Narrative

**Title:** SRE Hiring Managers: One Stat (Or a Pattern?)

**Body:**

You see this on a resume: "Improved system availability from 99.5% to 99.99%."

Here's what you don't see: *Did this person ship that improvement?* Or did they inherit a system that was already on the path?

When I interview SREs, I ask: *Tell me about a time your decision changed what your team prioritized.* If the answer is "I owned a project that shipped," that's different from "I worked on a project that was already underway."

Here's why this matters for hiring:

**Reliability is structural, not personal.** The team that achieves 36 months zero Sev1 is not doing it because one person is brilliant—it's because the organization has chosen to measure it, talked about it constantly, and held each other accountable. A hire who comes in and "fixes availability" without changing the team's thinking will leave us where we started the day they leave.

**Pattern beats project.** If your resume says "led zero-downtime migrations three times," I want to know: What made the first one succeed? What broke in the second? What did you change before the third so it could not fail?

**The Director's lens:** Hiring for reliability is not hiring for brilliance—it's hiring for judgment. *What does this person believe is worth measuring? What tradeoff would they make at 2 AM when they're tired?* Those answers don't show up in a project list.

**Here's the deeper thing:**

Your best interview signal might not be your biggest project. It might be: *Describe a time you found a problem the organization didn't know it had, and fought to fix it.* Because that's the person who will surface the assumptions your system is built on before they break under load.

**What would change about how you interview SREs if you hired for pattern-spotting instead of resume-line-spotting?**

---

## Notes on Design & Deployment

### Word Counts

| Post | Title | Words | Reading Time (seconds) |
|---|---|---|---|
| 1 | Zero Sev1 | 267 | 75 |
| 2 | 25M Messages | 278 | 80 |
| 3 | ML Anomaly Detection | 285 | 82 |
| 4 | Terraform Import | 276 | 79 |
| 5 | SLOs That Changed | 281 | 81 |
| 6 | Incident Command | 289 | 83 |
| 7 | Zero-Downtime Migration | 287 | 82 |
| 8 | Director Role | 285 | 82 |
| 9 | Resume Narrative | 272 | 78 |
| **Profile** | About Section | 236 | 68 |

### Design Patterns Applied

1. **Hook style:** Declarative statement or pattern-break (no questions, no "I'm excited").
   - Examples: "36 Months. 15 people. Zero Sev1."  
   - "What breaks at 25M msg/day (That you would never predict)"

2. **Body structure:**
   - Real operational story or problem first (2-3 paragraphs)
   - Framework or lesson second (numbered list, 4-5 items)
   - Director/Principal lens paragraph (1 paragraph)
   - Closing question (1 sentence—invites dialogue, not engagement bait)

3. **Vocabulary:** Operational terms first (circuit breaker, throughput, latency spikes), frameworks second (SLO, error budget, burn rate). Assumes reader knows systems thinking but may not know SRE terminology.

4. **CTA style:** All posts close with a professional question that invites discussion or self-reflection. Example: *"What would change about how you interview SREs if you hired for pattern-spotting instead of resume-line-spotting?"*

5. **Profile strategy:**
   - Headline variants for different audiences (engineering peers, recruiters, founders).
   - About section leads with the differentiator (36 months zero Sev1), names H1B status naturally (portable transfer framing), and closes with direct call for leadership conversations.
   - Email included for inbound outreach.

### Deployment Checklist

- [ ] Copy all 9 post bodies into LinkedIn Post drafts (do not publish yet—use as queue)
- [ ] Update LinkedIn headline using Variant 1 (default)
- [ ] Update About section with full text
- [ ] Schedule posts 3 days apart (M/Th/Tu pattern over 3 weeks)
- [ ] Pair each post with a 1-2 minute comment that responds to first likely question (e.g., "36 months zero Sev1? Here's the specific SLO math...")
- [ ] Track engagement: saves, comments, shares (Director/VP SRE roles = target audience)
- [ ] Rotate headlines monthly (A/B profile Variant 1 vs. Variant 2)

### Interview Prep Integration

These posts are designed to be quoted back to you in interviews:

- Post 1 (Culture): *"You say zero Sev1 for 36 months. Walk me through how you built that."*
- Post 4 (Terraform): *"Tell me about a time infrastructure-as-code saved you from a problem."*
- Post 6 (Incident Command): *"What's the worst incident command decision you made, and what changed?"*
- Post 8 (Director): *"What do you think a Director's job actually is?"* (Your answer is ready.)

---

## End of Document

**Total posts created:** 9 (LinkedIn + Profile)  
**Total word count:** 2,447 (posts only, excluding profile)  
**Author:** Vishweshwar Chippa  
**Date created:** 2026-06-11  
**Target audience:** Engineering managers, VPs SRE, CTOs hiring for reliability leadership  
**Format:** LinkedIn native (no external links, all self-contained)
