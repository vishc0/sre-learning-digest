# STAR Story 06: MART Framework — Reactive Alerts to Proactive Observability
## Domain: Observability Engineering / Monitoring Strategy

---

## Situation

When I took over the SRE team, our observability stack was a collection of independently created Splunk dashboards and threshold-based alerts built by different engineers across five years. There was no taxonomy, no ownership model, and no connection between alerts and business outcomes. Engineers had created alerts for every component they worried about individually, but no one had ever asked: does this alert actually predict a customer-impacting event? The result was a monitoring system that felt comprehensive — we had hundreds of dashboards — but was operationally useless because there was no agreed-upon answer to the question "is the platform healthy right now?"

## Task

My task was to build a coherent observability framework that could answer three operational questions reliably: (1) Is the platform healthy right now? (2) Is it trending toward a problem? (3) If something is wrong, where do I look first? This needed to be done without replacing the existing Splunk investment, without requiring engineers to learn a new tool, and in a way that the framework itself could be maintained and evolved by the team without me personally.

## Action (IC Technical Depth)

I spent two weeks doing a monitoring audit before writing a line of SPL. I inventoried every dashboard and alert by asking three questions: Does this alert actually fire during incidents? When it fires outside of incidents, is there a real problem? Could an engineer use this to diagnose the problem, or does it just tell them something is wrong?

The audit revealed: 40% of alerts had never fired in 6 months. 35% of alerts that fired were noise (no corresponding incident or degradation). Only 25% of alerts were reliable signals. More importantly, there were entire failure modes — the RabbitMQ queue depth accumulation pattern, the Cassandra compaction latency drift — that had no detection at all.

I designed the MART framework around four tiers, deliberately ordered from real-time operational to strategic:

**M — Metrics**: A single "platform health" dashboard using four golden signals adapted for our context: message throughput (traffic), end-to-end delivery latency (latency), delivery failure rate (errors), and consumer queue depth (saturation). Each signal had a red/amber/green status tied to SLO thresholds. This answered "is the platform healthy right now" with a single screen.

**A — Alerts**: All alerts were rewritten to fire on SLO burn rate, not raw thresholds. Instead of "latency > 500ms," the alert became "current 1-hour burn rate would exhaust monthly error budget in less than 4 days." This meant alerts had business context built in — they told you not just that something was wrong, but how wrong relative to your commitments. I reduced the active alert count from 340 to 47. Every alert was assigned an owner and linked to a runbook.

**R — Reports**: Weekly automated Splunk report delivered to the SRE team and shared with product leads: SLO compliance for the week, top 5 error contributors, trend lines for each golden signal, and a "would we have made our SLO if this week's pattern held for a full month" calculation. This created a weekly ritual of shared situational awareness rather than everyone having their own incomplete view.

**T — Trends**: The MLTK anomaly detection layer (see STAR Story 03) — temporal baseline models on the three highest-risk failure patterns. These models don't alert on current state, they alert on trajectory: "this metric is deviating from its expected pattern for this time of day." This answered the "trending toward a problem" question 40-60 minutes before the problem became customer-visible.

I documented the framework in a single internal wiki page: what each tier answers, what the design decisions were, and how to add a new metric or alert within the framework. I ran a 2-hour workshop with the full SRE team to walk through the design decisions — not to train them on the tooling, but to transfer the reasoning so they could extend the framework without me.

## Result

MART went live in Q3 of Year 1 of my tenure:
- Active alert count: 340 → 47 (86% reduction), while coverage of actual failure modes improved
- Alert-to-incident correlation: 25% baseline → 88% after MART (alerts that fire are real problems)
- Mean Time to Detect: 47 minutes → under 8 minutes
- New-engineer onboarding: time to "able to go on-call independently" dropped from 8 weeks to 4 weeks (the Metrics dashboard gave them a shared mental model of platform health that threshold-based alerts never provided)
- Framework extended to 2 additional T-Mobile teams
- MART presented at internal engineering summit; engineering blog post (internal) documented it as a reusable pattern

---

## Director/VP Version (Leadership Framing)

"Monitoring maturity is one of the hardest things to build because the cost of bad monitoring is invisible — you can have hundreds of dashboards and zero operational insight. I redesigned our observability from first principles, organizing it around four tiers that answer distinct operational questions: is it healthy now, what's trending, when should I be alarmed, and what's the weekly pattern? The result was an 86% reduction in alerts with improved coverage, 8-minute detection, and — importantly — a framework that new engineers can navigate without tribal knowledge. Onboarding to on-call dropped from 8 weeks to 4. That's the leverage I was looking for: not a better dashboard, but a shared operational language."

## IC Version (Technical Depth)

"The design principle I anchored MART on was: every alert must have a business context. Raw threshold alerts tell you a metric crossed a line. SLO burn rate alerts tell you how fast you're consuming your customer-trust budget. I rewrote all 47 production alerts as burn rate calculations: 'at this rate, the monthly error budget exhausts in N days.' That framing changes the urgency calculus immediately — an alert that says 'latency > 500ms' might not feel urgent at 2 AM. An alert that says 'at current burn rate, we exhaust our monthly SLO budget in 11 hours' absolutely does. The MLTK trend tier used DensityFunction and StateSpaceForecast algorithms on 7-day and 4-hour rolling windows respectively — the design decision there was temporal segmentation by day-of-week and time-of-day, because Monday 2pm baseline is completely different from Saturday 2am baseline."

---

## 30-Second Version

"I audited 340 alerts and found only 25% were reliable signals. I rebuilt the observability framework as four tiers — Metrics, Alerts, Reports, Trends — each answering a different operational question. Reduced alerts from 340 to 47, improved alert reliability from 25% to 88%, and dropped MTTD to under 8 minutes. New-engineer on-call readiness dropped from 8 weeks to 4."

---

## 2-Minute Version

"When I inherited the monitoring stack, we had hundreds of dashboards and 340 active alerts. Engineers couldn't answer the simplest question: 'is the platform healthy right now?' Not because we lacked data — we had too much data. The problem was we had no organizing principle.

I ran a 2-week audit before touching anything. I asked three questions about every alert: does it fire during real incidents? When it fires outside incidents, is there a real problem? Can an engineer use it to diagnose, or does it just say 'something is wrong?' The results were sobering: 40% of alerts had never fired in 6 months. Only 25% were reliable signals.

I designed MART as four tiers, each answering a distinct question. Metrics answers 'is it healthy now' — four golden signals, one screen, red/amber/green tied to SLOs. Alerts answers 'when should I wake up' — SLO burn rate, not raw thresholds, 47 alerts down from 340, every alert linked to a runbook. Reports answers 'what's the weekly pattern' — automated Monday morning delivery to SRE and product leads, SLO compliance, trend lines. Trends answers 'what's coming' — MLTK anomaly detection, 40-60 minute early warning.

The cultural piece was as important as the technical piece. I ran a 2-hour team workshop on the design decisions — not tool training, but the reasoning. I wanted the team to be able to extend the framework without asking me. The test was: when a new engineer builds an alert, do they start by asking 'what threshold feels right' or do they ask 'what burn rate signals a real problem?' After the workshop, they were asking the right question.

Outcomes: 86% alert reduction, alert reliability from 25% to 88%, MTTD under 8 minutes, on-call onboarding from 8 weeks to 4. Framework was adopted by two other teams."

---

## Key Metrics to Remember
- Alert count: 340 → 47 (86% reduction)
- Alert reliability: 25% → 88% (alerts that fire = real problems)
- MTTD: 47 minutes → under 8 minutes
- On-call onboarding: 8 weeks → 4 weeks
- MART tiers: Metrics (healthy now?), Alerts (when to wake up?), Reports (weekly pattern?), Trends (what's coming?)
- Alert design principle: SLO burn rate, not raw threshold
- Adopted by 2 additional T-Mobile teams
- Framework documented in single wiki page, transferable without author present
