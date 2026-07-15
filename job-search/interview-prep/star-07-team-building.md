# STAR Story 07: Team Building — Hiring, Growing, and Restructuring the 15-Person Team
## Domain: Engineering Leadership / Talent Development

---

## Situation

When I became SRE Manager for the T-Mobile notification platform team, I inherited a team of 9 engineers with a bimodal skill distribution: 3 senior engineers who had been on the platform for 5+ years and held all the tribal knowledge, and 6 junior-to-mid engineers who were competent but not growing because the senior engineers were the bottleneck for every non-trivial decision. There was no formal career development, no structured skill-building, and no knowledge transfer program. Two of the three senior engineers were flight risks — they'd been passed over for staff promotions twice and were quietly interviewing elsewhere. Over 18 months I grew the team from 9 to 15, promoted two engineers to Staff SRE, reduced key-person dependency from 3 critical people to a distributed model, and built a structured growth program that's still running.

## Task

My task was threefold: retain the senior engineers who were flight risks, create a growth path for mid-level engineers so they were developing toward staff rather than stagnating, and hire for cultural and technical fit with a team that was moving from reactive operations to proactive platform engineering. I had full hiring authority and direct influence over T-Mobile's promotion process for my team.

## Action (IC Technical Depth)

The first thing I did was have a direct conversation with each of the two senior engineers who I believed were at risk of leaving. Not a retention conversation — a career conversation. I asked each of them: what does Staff SRE look like to you? What problems do you want to be solving in two years? The answers were telling. One wanted architectural ownership — he wanted to be the person who designed the observability framework, not just operated it. The other wanted to lead a meaningful project end-to-end, not just be the most experienced person in the room.

I gave them both what they needed — real ownership, not just responsibility. The observability engineer became the technical lead and primary author of the MART framework. The other became the migration lead for our PCF-to-EKS migration. I framed both as Staff-caliber work in their promotion narratives, with documented outcomes. Both were promoted to Staff SRE within 12 months. Neither left. That's a retention story, but the mechanism was genuine career investment, not counter-offers.

For the mid-level engineers, I built a structured growth program I called the "On-Call Ladder." I'd found that the bottleneck to growth was that junior engineers didn't have enough surface area with the platform to develop intuition — they were always supervised, always deferring to seniors. The On-Call Ladder had four levels: L1 could page out without diagnosis, L2 could diagnose and escalate with context, L3 could resolve independently with runbook, L4 could resolve independently without runbook and write the postmortem. Progression was gated by demonstrated capability, not time. Each level had a specific set of platform components the engineer had to demonstrate comfort with.

I also started weekly "production archaeology" sessions — 30-minute team meetings where we'd pull a random recent event from Splunk (page, anomaly, deployment) and walk through what happened, what signals were visible, and what the right response would have been. This transferred senior knowledge systematically rather than through osmosis. Within 6 months, the ratio of incidents escalated to senior engineers dropped from 70% to under 30%.

For hiring: I changed the interview process to include a 45-minute "production scenario" exercise rather than whiteboard algorithms. Candidates were given a Splunk dashboard with an ongoing degradation pattern and asked to narrate their diagnostic approach. This screened for operational intuition over CS theory fluency — which is what SRE work actually requires. I hired 6 engineers over 18 months; 5 are still on the team, 1 was a culture mismatch that I identified and resolved within 90 days.

## Result

- Team grew from 9 to 15 (6 new hires in 18 months)
- 2 Staff SRE promotions (both previously flight-risk)
- Key-person dependency: incidents requiring senior escalation dropped from 70% to under 30%
- On-call onboarding: 8 weeks to independent → 4 weeks to independent
- Team engagement scores (internal survey): 3.8/5 → 4.6/5 over 18 months
- 0 attrition in the 18-month period (notable in T-Mobile's competitive engineering market)
- Weekly "production archaeology" sessions: still running, now facilitated by two mid-level engineers who were L2 when I started the program

---

## Director/VP Version (Leadership Framing)

"The team I inherited had a critical structural problem: all the knowledge lived in three people, and those three people were flight risks. I treated that as an organizational risk, not a talent problem. I solved it by identifying what each senior engineer needed to feel invested — real architectural ownership and project leadership — and then creating the org structures that let them do that work. Simultaneously I built a knowledge transfer system so the platform's operational understanding was distributed, not concentrated. The outcome wasn't just retention: it was a team that now runs more reliably with 15 people than it used to with 9, because the knowledge is spread and the growth path is clear. Zero attrition in 18 months in a competitive market tells you the model worked."

## IC Version (Technical Depth)

"The On-Call Ladder was the most technically rigorous thing I built for the team. I defined four progression levels with explicit platform components mapped to each level — L1 could page out and say 'queue depth high on rabbit cluster 2,' L2 could say 'queue depth high, consumer lag increasing, I think it's a slow consumer on service X, I'm escalating with that context,' L3 could resolve it with a runbook, L4 could resolve it, update the runbook, and write a postmortem with systemic recommendations. Progression was demonstrated, not assumed. I assessed each engineer's ladder level every quarter and mapped it explicitly to their career level. That mapping made promotion conversations concrete — here's what Staff SRE looks like in operational terms, here's where you are, here's the gap."

---

## 30-Second Version

"I inherited a 9-person team where 3 senior engineers held all the knowledge and were flight risks. I gave them real ownership — architectural and project leads — and both were promoted to Staff within 12 months. I built an On-Call Ladder for mid-level growth and weekly production archaeology sessions to distribute knowledge. Team grew to 15, zero attrition in 18 months, senior escalation dependency dropped from 70% to 30%."

---

## 2-Minute Version

"The team I inherited had a structural problem more than a talent problem. Three senior engineers held the platform knowledge, and they were flight risks — passed over for staff twice, quietly interviewing. Six mid-level engineers were competent but not growing because every decision went through those three people. That's fragile.

I started with direct career conversations, not retention conversations. I asked each senior engineer what Staff SRE looked like to them and what problems they wanted to be solving in two years. One wanted architectural ownership — I made him the technical lead for the MART framework. The other wanted to lead a meaningful project — I made him the migration lead for PCF-to-EKS. I supported both cases through T-Mobile's promotion process with documented outcomes. Both were promoted within 12 months. Neither left.

For the mid-level engineers, I built what I called the On-Call Ladder — four progression levels with explicit capability gates, from 'can page out' to 'can resolve independently and write the postmortem.' Progress was demonstrated, not assumed. I ran quarterly assessments and mapped each level explicitly to career level. That made promotion conversations concrete.

I also started weekly production archaeology sessions — 30 minutes, we pull a recent event from Splunk and walk through what happened and what the ideal response would have been. This transferred senior knowledge systematically. Within 6 months, incidents requiring senior escalation dropped from 70% to under 30%.

For hiring, I changed the interview format to a production scenario exercise — candidates narrate through a degradation pattern on a Splunk dashboard. That screens for operational intuition, which is what SRE work actually needs.

Outcomes over 18 months: team from 9 to 15, 2 Staff promotions, zero attrition, senior escalation dependency cut in half, engagement scores up from 3.8 to 4.6."

---

## Key Metrics to Remember
- Team growth: 9 → 15 over 18 months
- Staff SRE promotions: 2 (both previously flight-risk)
- Attrition: 0 in 18-month period
- Senior escalation dependency: 70% → under 30% of incidents
- On-call onboarding: 8 weeks → 4 weeks
- Engagement scores: 3.8/5 → 4.6/5
- Production archaeology: weekly, still running, now peer-facilitated
- Hiring: 6 engineers hired, 5 retained (1 culture mismatch identified in 90 days)
- On-Call Ladder: 4 levels (page out → diagnose → resolve with runbook → resolve independently + postmortem)
