# Error Budget Policy — Notification Platform

**Version**: 2.1  
**Owner**: SRE Notification Team  
**Reviewed**: Quarterly (last reviewed Q1 2026)  
**Audience**: Engineering leadership, product managers, on-call SREs

---

## What Is an Error Budget?

An error budget is the maximum allowed unreliability for a given SLO over a rolling 30-day window.

Think of it like a compliance margin in a regulated process: you have a specified tolerance for defects. When that tolerance is consumed, you stop the line — not to punish the team, but because shipping more changes into a degraded system makes the problem worse.

**Formula:**  
`Error Budget = 1 - SLO Target`

| SLO | Target | Monthly Budget (minutes) | Budget at 25M msg/day |
|---|---|---|---|
| SMS Delivery Success Rate | 99.5% | 216 minutes | ~43,200 failed messages |
| Push Latency P95 | 99.0% | 432 minutes | latency window violations |
| API Availability | 99.9% | 43.8 minutes | ~2,160 failed requests |

---

## Burn Rate Explained

**Burn rate** measures how fast you are consuming budget relative to normal.

- Burn rate 1.0 = consuming budget exactly in proportion to time (you will use exactly 100% by end of month)
- Burn rate 2.0 = consuming budget twice as fast (you will exhaust it in 15 days)
- Burn rate 14.4 = you will exhaust the monthly budget in 2 hours (critical threshold — page now)

Sloth generates two burn rate alert windows per SLO:
- **Fast burn**: 1h window at burn rate 14.4 — catches sudden spikes
- **Slow burn**: 6h window at burn rate 6.0 — catches sustained degradation

---

## Policy Thresholds and Required Actions

### Threshold 1: 50% Budget Consumed

**State**: Yellow. Team is aware and monitoring.

**What triggers this**: Burn rate exceeds 1.0 for a sustained period mid-month, or a single incident consumed ~50% in a short window.

**Required actions (within 24 hours)**:
1. SRE lead reviews the incident or trend causing consumption.
2. Post-incident review (PIR) opened if consumption was event-driven.
3. Product Manager notified — feature release schedule reviewed.
4. No deployment freeze yet, but all upcoming deployments require an SRE sign-off on rollback plan.
5. Capacity review: verify autoscaling limits, queue depth trends, downstream carrier health.

**Leadership action**: Engineering Manager reviews with team at next standup. No escalation required unless trend is accelerating.

---

### Threshold 2: 75% Budget Consumed

**State**: Orange. Feature velocity governed by reliability risk.

**What triggers this**: Sustained burn or a second incident in the same window.

**Required actions (within 4 hours of crossing threshold)**:
1. **Feature freeze for risky changes**: No deployments of new features to production without explicit SRE Manager approval. Bug fixes and security patches are exempt.
2. All in-flight Jira stories touching the notification pipeline are paused for impact assessment.
3. On-call SRE moves to heightened readiness (15-min PagerDuty acknowledgement SLA instead of 30-min).
4. SRE Manager and Engineering Manager hold a joint review within 24 hours to assess root cause and remaining budget.
5. Upstream teams (CRM, billing) are notified of degraded reliability posture via a status page update.
6. Chaos engineering and load testing scheduled for the current sprint are cancelled.

**Leadership action**: Engineering Manager escalates to Director of Engineering. VP Engineering is briefed if the platform serves any regulatory-adjacent notification (fraud alerts, network outages).

---

### Threshold 3: 100% Budget Consumed (Exhausted)

**State**: Red. Reliability contract with upstream systems is breached.

**What triggers this**: The platform has exceeded its allowable failure rate for the 30-day window.

**Required actions (immediate)**:

1. **Full feature freeze**: No production changes of any kind except emergency patches approved by the SRE Manager + Engineering Manager jointly.
2. **Incident bridge opened**: War room Slack channel activated. SRE Manager takes incident command.
3. **Rollback assessment**: Last 3 deployments reviewed for contribution to budget burn. Rollback executed if a deployment is implicated.
4. **Upstream notification**: All upstream system owners (CRM, billing, campaign) receive a formal communication within 2 hours. No SLA commitments made until budget is restored.
5. **Postmortem initiated**: Blameless postmortem document opened within 4 hours. Postmortem must be completed within 5 business days.
6. **Recovery gate**: Feature freeze remains in place until budget burn rate drops below 1.0 for 72 consecutive hours AND the root cause postmortem is in draft review.

**Leadership action**: VP Engineering and product leadership briefed. If regulatory notifications (fraud alerts, 911-adjacent) were affected, Legal and Compliance are looped in within 24 hours.

---

## Budget Restoration

The error budget resets on a rolling 30-day window — it does not reset on a calendar month boundary.

When the burn rate drops below 1.0 and stays there:
- At 72 hours sustained recovery: feature freeze can be lifted with SRE Manager approval.
- At 7 days sustained recovery: return to normal deployment cadence.
- At next monthly review: retrospective assessment of whether the SLO target is correctly calibrated or needs adjustment.

---

## SLO Target Review Cadence

SLO targets are not static. They are reviewed:
- **Quarterly**: SRE team reviews actual burn vs. target, adjusts if target is consistently trivial (burn never reaches 10%) or consistently punishing (burn exceeds 75% monthly).
- **Post-major-incident**: If a single incident consumes more than 30% of any budget, the SLO definition is reviewed for accuracy (are we measuring the right signal?) not just tightened.
- **Platform architecture change**: Any change to downstream carrier integration, queue topology, or consumer scaling model triggers an SLO review.

---

## Who Owns This Policy

| Role | Responsibility |
|---|---|
| SRE Manager | Enforces thresholds, approves exceptions, escalates at 75%+ |
| On-Call SRE | Monitors burn rate dashboards, escalates to SRE Manager at 50% |
| Engineering Manager | Owns feature freeze enforcement with product teams |
| Product Manager | Owns sprint adjustment when feature freeze is invoked |
| Director of Engineering | Briefed at 75%; approves emergency exceptions to feature freeze |
