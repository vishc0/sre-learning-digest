# STAR Story 08: Incident Command — A Real P1 and What I Did Differently
## Domain: Incident Management / SRE Operations

---

## Situation

At 11:47 PM on a Tuesday, our on-call engineer paged a Sev1: notification delivery failure rate had crossed 15% across all channels — SMS, push, and email — simultaneously. The platform was processing a high-volume marketing campaign that had launched at 11 PM. 25 million messages per day meant that at 15% failure rate, we were dropping roughly 1.5 million notifications per hour. The initial hypothesis from the on-call engineer was that the RabbitMQ cluster was saturated — the marketing campaign had overloaded the message consumers.

## Task

I was the incident commander for this event. My responsibility was to direct the investigation, make the call on escalation, coordinate with product and marketing stakeholders about the campaign impact, decide whether to halt the campaign, and ensure the postmortem captured the systemic learning rather than just the fix.

## Action (IC Technical Depth)

I joined the war room (Zoom) within 4 minutes. My first action was not to look at any dashboard — it was to set up the incident channel structure. I assigned a scribe to document every action and decision in our incident log (timestamped, in Slack), a communications lead to handle stakeholder updates, and kept the technical investigation to two engineers plus myself. Too many people in a war room creates noise. I've learned to keep the bridge small and move observers to a separate update channel.

My second action was to challenge the initial hypothesis. The on-call engineer said "RabbitMQ is saturated" because queue depth was elevated. I asked: "Is queue depth elevated because producers are producing too fast, or because consumers are consuming too slowly?" That distinction matters — the fix is different. We pulled consumer throughput metrics from Splunk. Throughput was normal. Producers were feeding at normal rate. Queue depth was elevated not because we were overwhelmed — it was because consumers were processing messages and then... not acknowledging them. The messages were re-queuing.

That changed everything. This wasn't a saturation problem. This was a consumer error pattern. I asked the scribe to note the hypothesis pivot and the evidence for it. Simultaneously I pulled the deployment log: had anything changed in the last 2 hours? Yes. A dependency update had gone out at 10:15 PM — a logging library upgrade, considered low-risk, deployed via automated pipeline. I made the call to rollback immediately, without waiting to confirm the library was the cause. The failure rate was too high and the evidence of a recent change was sufficient. Rollback decision at 12:03 AM, 16 minutes after I joined the bridge.

Rollback completed at 12:19 AM. Failure rate began dropping immediately — 15% → 8% → 2% → baseline within 12 minutes. Incident resolved at 12:31 AM. Total customer-impacting duration: 44 minutes.

The postmortem is where I made the most deliberate decisions. The immediate cause was clear — the logging library dependency update had introduced a connection pooling change that caused Cassandra write acknowledgements to time out silently, causing consumers to re-queue messages instead of acknowledging delivery. But I refused to let the postmortem stop at "update caused bug, add testing." I pushed the team to the systemic level: why did a "low-risk" dependency update go out at 10:15 PM, 45 minutes before a major campaign launch? Who decided it was low-risk? What's the decision framework for deployment timing relative to scheduled high-traffic events?

The postmortem identified two systemic fixes: (1) a deployment blackout window 60 minutes before and after scheduled marketing campaigns above a volume threshold, and (2) a silent failure detection test — any dependency update now goes through a 5-minute integration test that specifically validates Cassandra write acknowledgement behavior, because that's a non-obvious failure mode.

## Result

- Incident duration: 44 minutes customer-impacting (low for a Sev1 of this complexity)
- Decision to rollback: 16 minutes from I joining the bridge, 32 minutes from first alert
- No repeat of this incident pattern in the following 24 months
- Deployment blackout windows implemented and respected (no exceptions to date)
- Silent failure detection test added to CI pipeline — has caught 3 subsequent dependency changes that would have caused similar behavior
- Postmortem presented at internal SRE community meeting as a model for systemic vs. symptomatic root cause analysis

---

## Director/VP Version (Leadership Framing)

"The incident itself was resolved in 44 minutes — faster than average for that failure class. But what I'm most proud of is what the postmortem produced. The easy answer was 'bad library update, add more testing.' The systemic answer was 'why are we doing dependency updates 45 minutes before a high-volume campaign?' The real gap was governance, not testing coverage. I pushed the team to that level because symptomatic fixes give you the illusion of learning without the substance. The two systemic changes — deployment blackout windows and silent failure detection — are what prevented recurrence. That's the incident command mindset I try to bring: use every P1 as an investment in the system, not just a fire to put out."

## IC Version (Technical Depth)

"The diagnostic pivot was the key moment. The on-call engineer's hypothesis was saturation — high queue depth usually means overload. I asked him to check consumer throughput, not just queue depth. Throughput was normal, which meant the queue depth wasn't caused by consumers being slow — it was caused by messages being re-queued rather than acknowledged. That's a completely different failure mode with a different fix. If we'd treated it as saturation, we would have scaled out consumers, which would have amplified the problem. The rollback decision was made before we had definitive proof that the library was the cause — the deployment timeline correlation plus the failure pattern signature was sufficient evidence to act. At a 15% failure rate on 25M msg/day, you don't wait for certainty."

---

## 30-Second Version

"We had a 15% notification failure rate at midnight during a major campaign. On-call said 'saturation.' I challenged the hypothesis, found consumers were re-queuing messages rather than being overwhelmed, correlated it to a dependency update 45 minutes earlier, and called the rollback at minute 16 of the bridge. Resolved in 44 minutes. Postmortem found the systemic issue was deployment timing governance, not testing coverage. Blackout windows implemented, zero recurrence."

---

## 2-Minute Version

"It was 11:47 PM, 15% failure rate across all channels, major campaign running. First thing I did when I joined the bridge: set the room structure. Scribe documenting every action timestamped in Slack, communications lead for stakeholder updates, two engineers on investigation plus me. Small bridge, clear roles. I've seen war rooms turn into chaos when 15 people are all pulling in different directions.

On-call engineer said 'RabbitMQ saturated' because queue depth was high. I asked him to check consumer throughput before we concluded that. Throughput was normal. Messages were being processed by consumers but not acknowledged — they were re-queuing. This wasn't saturation. This was a consumer error pattern. Completely different root cause, completely different fix. If we'd scaled consumers for saturation, we would have made it worse.

I pulled the deployment log immediately. Library update at 10:15 PM, 45 minutes before the campaign started. I called the rollback at 12:03 AM — 16 minutes into the bridge — without waiting for confirmation the library was the cause. At 15% failure on 25M messages per day you don't wait for certainty. You act on sufficient evidence and monitor.

Rollback complete at 12:19. Failure rate dropped from 15% to baseline in 12 minutes. Total customer impact: 44 minutes.

The postmortem was where I made the most deliberate investment. The easy call was 'bad library, more testing.' I pushed the team to a harder question: why was a dependency update going out 45 minutes before a major campaign? What governance exists for deployment timing around high-traffic events? The answer was: none. We had a process gap, not just a testing gap.

We implemented deployment blackout windows 60 minutes either side of campaigns above a volume threshold. We added a silent failure detection test to the CI pipeline. That test has caught 3 subsequent changes that would have caused the same behavior. Zero recurrence in 24 months."

---

## Key Metrics to Remember
- Alert to bridge: on-call paged at 11:47 PM
- Hypothesis pivot: saturation → re-queue error pattern (within 8 minutes)
- Rollback decision: 16 minutes from joining bridge, 32 minutes from first alert
- Customer-impacting duration: 44 minutes
- Root cause: logging library update silently broke Cassandra write acknowledgement
- Systemic fixes: deployment blackout windows + silent failure detection test in CI
- CI test impact: caught 3 subsequent problematic changes before production
- Recurrence: zero in 24 months
