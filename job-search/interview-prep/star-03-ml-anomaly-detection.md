# STAR Story 03: ML Anomaly Detection — Business Problem to Production Model
## Domain: AI/ML in Production / Observability Engineering

---

## Situation

Our notification platform was generating 40,000+ Splunk alerts per month. The engineering team had built threshold-based alerts over five years — CPU > 80%, queue depth > 10,000, latency > 500ms — and each threshold was set based on a single incident's context, never revisited. The result was chronic alert fatigue: engineers were paging out for conditions that were normal under high traffic loads, while genuinely anomalous behavior — slow drift in Cassandra read latency, gradual RabbitMQ queue depth accumulation — was invisible until it became a customer-visible outage. The business problem wasn't "our alerts are too loud." The business problem was "we're spending our alert budget on noise and missing the signals that actually matter."

## Task

My responsibility was to identify the highest-value monitoring gaps, propose a detection approach, and lead the implementation. I was not a data scientist — I was the SRE manager who understood both the operational failure modes and what Splunk MLTK could do. My task was to translate operational knowledge into detection models, get them into production, and validate that they actually reduced time-to-detect without increasing false positives.

## Action (IC Technical Depth)

I started with a postmortem data mining exercise. I exported every Sev1 and Sev2 postmortem from the past two years and categorized the "how we found it" field. Three categories emerged: (1) customer complaint — we found out from the service desk, (2) threshold alert — legitimate catch, (3) engineer noticed something "felt off" during a routine check. Category 3 was the most interesting. Engineers were noticing things that weren't triggering any alerts. When I asked them to describe what they noticed, it was always relative, not absolute: "the queue depth was higher than it usually is at this time on a Tuesday" or "Cassandra response times are trending up even though traffic is flat."

That told me the models needed to be temporal and relative, not static thresholds. I chose Splunk MLTK because we already had the data in Splunk and I didn't want to introduce a new toolchain that the team would have to operate.

I built three initial models:

**Model 1 — RabbitMQ Queue Depth Anomaly**: Used MLTK's `DensityFunction` algorithm on a 7-day rolling window of queue depth, segmented by time-of-day and day-of-week. The model scored each 5-minute interval against the expected distribution for that time slot. A score above 2 standard deviations triggered an alert. Training data: 90 days of queue depth metrics.

**Model 2 — Cassandra Read Latency Drift**: Used `StateSpaceForecast` to predict expected p99 latency for the next 30 minutes based on the past 4 hours of trend. If actual latency exceeded the 95% confidence interval of the forecast, alert fired. This caught slow compaction-driven degradation that threshold alerts missed entirely.

**Model 3 — Message Processing Rate Anomaly**: Cross-correlated message ingestion rate with processing confirmation rate. A widening gap (more messages ingested than confirmed processed) was a leading indicator of consumer lag, detected 20-30 minutes before queue depth alerts would fire.

I ran all three models in "shadow mode" for 45 days — they generated alerts into a Slack channel visible only to me and two senior engineers. We reviewed every alert manually, classified it as true positive, false positive, or unknown. After 45 days, Model 1 precision was 87%, Model 2 was 91%, Model 3 was 79% (too many false positives — I widened the detection window and re-ran for another 3 weeks). After tuning, all three exceeded 88% precision before I moved them to production on-call.

## Result

After MLTK models went live in production on-call:
- Alert volume: 40,000+/month → under 4,000/month (90% reduction)
- False positive rate: dropped from 73% to 19%
- Mean Time to Detect: 47 minutes average → under 8 minutes average
- Two Sev2s caught by the ML models in the first 6 months that would previously have been missed until customer-visible (both caught 40+ minutes before message delivery failure)
- Team confidence in alerts increased: engineers stopped ignoring pages, because the signal-to-noise ratio was now trustworthy

The MLTK framework I built became the observability template for two other T-Mobile teams. I presented the approach at an internal engineering summit and documented it as the MART framework (Metrics, Alerts, Reports, Trends).

---

## Director/VP Version (Leadership Framing)

"The business problem behind alert fatigue isn't volume — it's trust. When engineers stop believing their alerts, they start ignoring pages, and that's when real incidents become invisible. I reframed the project: instead of 'reduce noise,' the goal was 'rebuild trust in the monitoring system.' I used Splunk MLTK to build temporal anomaly detection models that fire based on deviation from expected baseline, not fixed thresholds. I validated them in shadow mode for 45+ days before putting them on-call. The outcome was a 90% reduction in alert volume, MTTD under 8 minutes, and — more importantly — engineers who actually respond to pages promptly because they trust the signal. That trust is an organizational asset you can't buy with tooling alone."

## IC Version (Technical Depth)

"I built three MLTK models: DensityFunction on RabbitMQ queue depth segmented by time-of-day and day-of-week, StateSpaceForecast on Cassandra p99 latency for 30-minute horizon predictions, and a cross-correlation model on ingestion-vs-confirmation rate spread for consumer lag early warning. The key design decision was using relative temporal baselines — 'higher than expected for Tuesday 2pm' — instead of static thresholds. I ran all models in shadow mode for 45+ days, manually classified every alert as TP/FP/unknown, and tuned until precision exceeded 88% before moving to production on-call. Model 3 needed two tuning cycles to get there — the detection window was too tight initially."

---

## 30-Second Version

"I mined two years of postmortems to find that engineers were catching anomalies by intuition — 'this feels higher than usual' — that no alert was catching. I built three Splunk MLTK models with temporal baselines instead of static thresholds, validated them in 45-day shadow mode, and deployed to on-call. Alert volume dropped 90%, MTTD dropped from 47 minutes to under 8 minutes."

---

## 2-Minute Version

"The problem wasn't the number of alerts. The problem was that engineers had stopped trusting alerts. When you page someone 80 times a week and 73% of those pages are noise, they start triaging by gut feel rather than genuine urgency. That's dangerous.

I went back to the postmortems and looked at the 'how we found it' field for every Sev1 and Sev2 in the past two years. The pattern I found was striking: the most experienced engineers were catching problems before any alert fired — but only because they'd seen the pattern before and recognized something felt off. That told me the detection logic needed to be temporal and relative, not static.

I built three Splunk MLTK models: queue depth anomaly on a 7-day rolling baseline segmented by time of day, Cassandra latency forecast with 30-minute lookahead, and a cross-correlation between message ingestion rate and processing confirmation rate to catch consumer lag early. None of these fire on absolute values — they all fire when something deviates from its own historical baseline.

Before putting any of them on-call, I ran 45 days of shadow mode — alerts visible only to me and two seniors, manually classified. Anything below 88% precision didn't graduate. One model needed two rounds of tuning.

Results: alert volume went from 40,000 per month to under 4,000. False positive rate from 73% to 19%. MTTD from 47 minutes to under 8. The thing that mattered most though was behavioral: engineers started responding to pages within 3 minutes instead of triaging them. The signal was trustworthy again. Two Sev2s in the first 6 months were caught by the models 40 minutes before they would have been customer-visible."

---

## Key Metrics to Remember
- Before: 40,000+ alerts/month, 73% false positive rate, 47-min MTTD
- After: under 4,000 alerts/month, 19% false positive rate, under 8-min MTTD
- Shadow validation: 45+ days before production deployment
- Precision threshold for production graduation: 88%
- Models: DensityFunction (RabbitMQ), StateSpaceForecast (Cassandra), cross-correlation (consumer lag)
- 2 Sev2s caught 40+ minutes early in first 6 months
- Framework adopted by 2 additional T-Mobile teams
