# Incident Director Checklist
## What Your Job Is When Production Is Down

---

## The Core Reframe

When a P1 is declared, your instinct as someone who came up through engineering is to **go fix it**. That instinct is wrong at Director level.

Your job is not to diagnose. Your job is to ensure the right people are diagnosing, that the organization is informed, that decisions can be made, and that the incident is closed in a way that improves the system.

**Analogy**: You are the Incident Commander in a fire department structure, not the firefighter. The IC does not hold the hose. The IC ensures the right crews are on the right floors, that the building manager has been notified, that resources are not duplicated, and that everyone has a clear exit if conditions change.

---

## Severity Trigger Reference

| Severity | Trigger | Director Involvement |
|---|---|---|
| P0 | Complete platform outage, revenue impact confirmed, customer-facing | Immediately notified. Owns executive communication. Present on bridge. |
| P1 | Significant degradation, subset of customers impacted, SLO at risk | Notified within 15 minutes. Monitors bridge. Escalates if needed. |
| P2 | Single service degraded, no customer impact confirmed | Optional — reviews post-incident summary next day. |
| P3 | Minor issue, no customer impact, resolved without escalation | Sees in weekly reliability digest. Not involved. |

---

## Director Incident Checklist

### Phase 1: First 5 Minutes (Notification)
- [ ] Confirm severity classification with on-call engineer or Tech Lead — do not accept the first severity declaration as final without a quick sanity check
- [ ] Confirm the Incident Commander (IC) is identified and on the bridge — if not, designate one immediately
- [ ] Confirm a scribe / timeline tracker is on the bridge — if not, assign one (even an SRE manager works)
- [ ] Identify whether this incident crosses team boundaries — if yes, activate the federated IC protocol
- [ ] Note the time: you will use this in executive communication

### Phase 2: First 15 Minutes (Stabilization)
- [ ] Confirm customer impact is being quantified (how many customers, what functionality, since when)
- [ ] Begin stakeholder notification chain:
  - VP Engineering (always for P0/P1)
  - VP Product (if product is customer-facing)
  - CISO (if security-adjacent)
  - Customer Success lead (if enterprise customers impacted)
  - Public communications lead (if there is social media risk)
- [ ] Draft first stakeholder update: **[Time] [Service] is degraded. We have [N] engineers engaged. Customer impact: [Description]. Next update in 30 minutes.**
- [ ] Confirm the technical team has a clear working hypothesis — if they are more than 15 minutes in with no hypothesis, this is a signal to ask the IC to time-box the current direction and consider parallel tracks
- [ ] Ask: "Do we have a rollback option?" — not "should we rollback?" — just confirm the option exists and someone is prepared to execute it

### Phase 3: 15–60 Minutes (Active Response)
- [ ] Send stakeholder update every 30 minutes: impact, current status, working theory (in plain English), ETA if known
- [ ] Monitor for rabbit-holing — if the same team has been investigating the same hypothesis for >20 minutes without progress, ask the IC to consider branching
- [ ] Watch for resourcing gaps — are there teams that should be pulled in who haven't been? Common gap: database team, networking team, third-party vendor.
- [ ] Make the rollback call if needed: "What is the risk of rolling back vs. the risk of continuing?" — this is a Director decision, not an IC decision
- [ ] Track decision log: every major decision made on the bridge should be time-stamped (this feeds the postmortem)
- [ ] Protect the technical team from leadership distraction — if VPs start asking questions on the bridge that are pulling engineers off the investigation, redirect them to you

### Phase 4: Resolution
- [ ] Confirm customer impact has ended — do not close the incident until monitoring confirms recovery, not just when the engineer says "I think it's fixed"
- [ ] Confirm the immediate fix is stable — what is the watch window? (typically 15–30 minutes of clean metrics post-fix)
- [ ] Send resolution notification to all stakeholders: **[Time] [Service] is restored. Customer impact lasted [duration]. Immediate cause: [plain English]. Post-incident review within 48 hours.**
- [ ] Confirm the on-call engineer is not left alone post-incident — assign a second engineer to monitor for the next 2 hours if the incident was significant
- [ ] Schedule the postmortem: within 48–72 hours while details are fresh
- [ ] Grant recovery time: engineer who drove the incident response should not be on-call the following night (non-negotiable policy, not manager discretion)

### Phase 5: Post-Incident (24–72 Hours)
- [ ] Attend or review the postmortem within 48 hours of the incident
- [ ] Confirm the postmortem follows blameless format (see postmortem guide)
- [ ] Review the action items — are they real changes or are they cover stories?
- [ ] Communicate outcomes to VP: incident summary, root cause summary, specific changes being made, timeline for those changes
- [ ] Update the risk register if this incident revealed a gap that belongs there
- [ ] Check: does this incident expose a gap in the change governance framework?

---

## Director Communication Templates

### Initial Stakeholder Notification (P0/P1)
```
[TIME] INCIDENT NOTIFICATION — [Service Name]
Severity: [P0/P1]
Status: Active investigation
Customer impact: [Plain English description. How many customers. What is affected.]
Team engaged: [N engineers on bridge]
Current working theory: [One sentence, plain English — "We believe the issue is in X"]
Next update: [Time, typically 30 minutes]
IC: [Name]
Director contact: [Your name, phone/Slack]
```

### 30-Minute Update
```
[TIME] INCIDENT UPDATE — [Service Name] — Update [#N]
Status: [Still investigating / Identified cause / Deploying fix]
Customer impact update: [Any change from last update]
What's happening: [One paragraph, plain English, no jargon]
Current action: [What the team is doing right now]
Rollback status: [Available / In progress / Complete]
ETA for resolution: [Best estimate, or "Not yet estimable — next update in 30 min"]
```

### Resolution Notification
```
[TIME] INCIDENT RESOLVED — [Service Name]
Service restored at: [Time]
Total customer impact duration: [Start to resolution time]
Customers affected: [Estimate if available]
Root cause summary: [2-3 plain English sentences — no jargon]
Immediate fix applied: [What was done]
Post-incident review: Scheduled for [Date/Time]
Action items to prevent recurrence: [2-3 items, owner named]
Director contact for questions: [Your name]
```

### Executive Post-Incident Summary (for VP / C-suite)
```
INCIDENT SUMMARY — [Service Name]
Date: [Date]
Duration: [Total minutes/hours of customer impact]
Severity: [P0/P1]

CUSTOMER IMPACT
[2 sentences: who was affected and what they experienced]

BUSINESS IMPACT
Revenue impact: [Estimate or N/A]
SLA credits triggered: [Yes/No — estimated value if yes]
Customer escalations: [Number of enterprise/VIP customer contacts]

WHAT HAPPENED
[3-4 sentences, plain English narrative of the failure]

WHAT WE FIXED
[Immediate fix — 1 sentence]

WHAT WE'RE CHANGING
1. [Specific action item — owner — deadline]
2. [Specific action item — owner — deadline]
3. [Specific action item — owner — deadline]

CONFIDENCE ASSESSMENT
Likelihood of recurrence before changes are complete: [Low/Medium/High]
Rationale: [One sentence]
```

---

## What Directors Should NOT Do During an Incident

| Temptation | Why It Hurts | What to Do Instead |
|---|---|---|
| Jump on the bridge and start debugging | You pull senior engineers into briefing you instead of fixing | Assign one engineer as your update liaison. Let them brief you at 30-min intervals. |
| Ask "why didn't the alert catch this?" during the incident | It creates defensiveness and pulls attention to blame | Note the question. Ask it in the postmortem. |
| Give engineers a deadline for resolution | Arbitrary deadlines cause shortcuts and missed steps | Ask for a confidence-weighted estimate. Share it with stakeholders as a range. |
| Approve experimental fixes under pressure | "Let's try X, maybe it'll work" leads to making things worse | Require a hypothesis and expected evidence of success before any change |
| Run the bridge yourself without an IC | You cannot manage the room and manage stakeholders simultaneously | Always have an IC. You are the escalation layer, not the bridge lead. |
| Skip the recovery time policy | Engineers who are exhausted make worse decisions in the next incident | Enforce it. If coverage is a concern, that's a staffing risk to surface. |

---

## Fast Decision Frameworks for Directors During Incidents

### When to Rollback (vs. continue forward)
Rollback when:
- No hypothesis for root cause after 20 minutes
- Customer impact is worsening, not stable
- The change that preceded the incident was made in the last 4 hours
- Rollback time is shorter than estimated fix time

Continue forward when:
- Rollback would cause data loss or worse customer impact
- Root cause is confirmed and fix is low-risk
- The issue is environmental (cloud provider, dependency) and rollback does not help

### When to Escalate Severity
Escalate P1 to P0 when:
- Revenue impact exceeds [your threshold — e.g., $50K/hour]
- VIP/enterprise customers are directly impacted
- Regulatory or compliance data is at risk
- Multiple simultaneous platform failures (systemic vs. isolated)

### When to Page Additional Leadership
- You have been on the bridge for 60 minutes with no mitigation in sight: page VP Engineering
- The incident involves potential security breach or data exposure: page CISO immediately (not after resolution)
- Media or customer social media attention is confirmed: page Communications lead
- A vendor is involved and SLA remedies are needed: page Vendor Manager

---

*Checklist version: 1.0 | Owner: Vishweshwar Chippa | Created: 2026-06-11*
