# STAR Story 01: Zero Sev1 in 36 Months — Reliability Culture
## Domain: SRE Leadership / Reliability Engineering

---

## Situation

I manage a 15-person SRE team at T-Mobile responsible for a notification platform processing 25 million messages per day — SMS, push, and email delivery for customer-facing alerts, marketing campaigns, and operational triggers. When I took over the team, we had 4-6 Severity 1 incidents per year, reactive runbooks that were mostly tribal knowledge in the heads of 2-3 senior engineers, and no formal SLO framework. Alert fatigue was real — engineers were being paged 80+ times a week, most of it noise.

## Task

My responsibility was to transform the team from a reactive firefighting unit into a proactive reliability engineering organization. This meant redesigning the on-call model, building an observability framework, establishing SLOs with product accountability, and — critically — changing the culture so that preventing incidents was rewarded as much as resolving them.

## Action (IC Technical Depth)

I started by running a 90-day audit: I pulled every Sev1 and Sev2 postmortem from the past two years and categorized root causes. Three patterns dominated: (1) undetected queue depth buildup in RabbitMQ before message lag became customer-visible, (2) Cassandra read latency spikes during uncoordinated compaction windows, and (3) deployment-triggered failures from missing canary gates. Each had been "fixed" repeatedly — the fixes addressed symptoms, not systemic gaps.

I then built what I called the MART framework — a Splunk-based observability layer with four tiers: Metrics for baseline health, Alerts tuned to SLO burn rate rather than raw thresholds, Reports for weekly trend review, and Trend models using Splunk MLTK to detect anomalies before they became pages. I personally wrote the initial MLTK queries for RabbitMQ queue depth prediction and Cassandra compaction window detection. The anomaly models ran on a 7-day rolling window and would flag deviation 45-60 minutes before human-visible degradation.

Simultaneously, I restructured on-call: I eliminated single-engineer on-call, moved to paired rotations with a primary and a shadow, and required every engineer to have a runbook sign-off before going primary. I ran quarterly game days — tabletop simulations of previous incidents — so new engineers built pattern recognition without needing a live P1 to learn from.

The SLO piece was the hardest. I negotiated with product leadership to establish a 99.9% monthly availability target for the notification platform with a formal error budget policy. I wrote the policy document, got it signed at the VP level, and used it to block two releases in Year 1 when the error budget was depleted. That was uncomfortable, but it established credibility: SLO was not a suggestion.

## Result

36 months with zero Severity 1 incidents. Alert volume dropped from 80+ pages/week to under 12. On-call satisfaction scores (from team surveys) went from 3.2/5 to 4.6/5. Mean Time to Detect for anomalies improved from 47 minutes (human-noticed) to under 8 minutes (automated ML detection). Two engineers from my team were promoted to Staff SRE. The MART framework was adopted by two other teams at T-Mobile as a reference implementation.

---

## Director/VP Version (Leadership Framing)

"I inherited a team with a reactive reliability posture and a culture where the most experienced engineers were the most exhausted. Over 36 months I redesigned the team's operating model — shifting the reward system from heroic incident response to preventive engineering. I established formal SLO governance at the VP level, which gave the team the organizational authority to hold the line when product velocity threatened platform stability. The outcome was zero Sev1s over 36 months, but the real outcome was a team that can sustain that without me in the room. Two engineers were promoted to Staff. The framework we built was adopted org-wide. That's the multiplier effect I was going for."

## IC Version (Technical Depth)

"I built an ML-backed observability layer using Splunk MLTK — specifically, anomaly detection on RabbitMQ queue depth using a 7-day rolling baseline with deviation scoring. The model would fire at 2-sigma deviation, which gave us a 45-60 minute head start before message lag became customer-visible. I also redesigned the alert taxonomy: we stopped alerting on raw thresholds (CPU > 80%) and switched to SLO burn rate alerts — if we were burning 5x our hourly error budget, that fired. That change alone cut alert volume by 85% while improving signal quality. I wrote the initial detection models personally so I could explain every tuning decision to the team."

---

## 30-Second Version

"I ran a 90-day root cause audit, identified three systemic patterns behind our Sev1 history, and built ML-backed anomaly detection in Splunk to catch them before they became incidents. I also restructured on-call, established SLOs with real governance, and held the line when product wanted to ship into a depleted error budget. 36 months later: zero Sev1s, alert volume down 85%, two engineers promoted."

---

## 2-Minute Version

"When I took over the SRE team, we had 4-6 Sev1s a year and engineers who were paged 80+ times a week. The team was reactive — we were good at fighting fires but we weren't preventing them.

I started with a 90-day audit of every postmortem. Three patterns kept showing up: RabbitMQ queue depth buildup, Cassandra compaction timing, and canary-less deployments. Each one had been 'fixed' before, but the fixes were symptomatic. So I attacked the detection layer first.

I built what we call the MART framework — a Splunk observability stack where alerts are tied to SLO burn rates, not raw thresholds, and where MLTK anomaly models give us 45-60 minutes of early warning on the two most common failure patterns. I wrote the initial detection models myself so I could tune them properly and teach the team what to watch for.

On the culture side, I moved from solo on-call to paired rotations, required runbook sign-off before anyone went primary, and ran quarterly tabletop game days. And I negotiated SLO governance with product at the VP level — formal error budget policy, signed off, with two real-world enforcements in Year 1.

The result: 36 months, zero Sev1s. Alert noise dropped from 80 pages a week to under 12. Mean Time to Detect went from 47 minutes to under 8. Two staff promotions came out of the team. The framework got adopted by two other teams. The thing I'm most proud of is that the team can sustain this without me — that's the real test of whether you built a culture or just a dependency on yourself."

---

## Key Metrics to Remember
- 36 months: zero Sev1 incidents
- Alert volume: 80+/week → under 12/week (85% reduction)
- MTTD: 47 minutes → under 8 minutes
- On-call satisfaction: 3.2/5 → 4.6/5
- Team outcome: 2 Staff SRE promotions
- Platform scale: 25M messages/day
- MART framework: adopted by 2 additional teams
