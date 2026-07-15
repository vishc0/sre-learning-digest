# Platform Stability Policy
## Director-Level Framework for Governing Velocity vs. Reliability

---

## Purpose of This Document

This document exists to answer one recurring question in a way that does not require the Director to be in every prioritization meeting:

> **When reliability conflicts with feature velocity, which wins, by how much, and who decides?**

If this question does not have a written, VP-signed answer, the answer is always "whoever argues loudest in the sprint planning meeting." That is not governance.

---

## Governing Principle

Feature velocity and platform stability are not opposites. They are complementary until they are not. The purpose of this policy is to define the point at which they diverge, and establish who makes the call.

**The metaphor**: Running a notification platform is like running a highway. You can have construction (new features) and traffic (reliability) on the same road. But when construction degrades traffic flow below the threshold your customers contracted for, construction stops until flow is restored.

---

## Service Tier Classification

Not all services are equal. Stability policy should be calibrated to service tier.

| Tier | Definition | Examples | SLO Target | Change Restrictions |
|---|---|---|---|---|
| Tier 1 — Mission Critical | Customer-facing, revenue-generating, contractual SLA exists | Notification delivery, payment processing, authentication | 99.95%+ | Strictest — Tier 3/4 changes require CAB |
| Tier 2 — Business Critical | Internal-facing critical functions, degradation visible to customers | Admin portals, reporting systems, batch processors | 99.9% | Moderate — peer review + SRE sign-off |
| Tier 3 — Supporting | Dev, test, internal tooling, non-critical pipelines | CI/CD pipelines, internal dashboards, staging environments | 99.5% | Light — standard PR + automated gates |
| Tier 4 — Non-Critical | Experimental, dev-only, non-SLA'd | Prototype services, data science workbenches | Best effort | Self-governed by team |

**Director responsibility**: Maintain this tier classification. Review it annually or after any new service launch. Escalate to VP when Tier 1 classification is disputed.

---

## Error Budget Policy (The Core Engine)

Error budgets convert SLO targets into a shared resource. When the budget is healthy, teams have freedom to move fast. When it is depleted, the platform is telling you something: slow down.

### Error Budget Calculation

```
Monthly error budget = (1 - SLO target) x minutes in month

For 99.95% SLO on a 30-day month (43,200 minutes):
Monthly error budget = 0.05% x 43,200 = 21.6 minutes of allowed downtime
```

### Error Budget Zones and Policy Response

| Zone | Error Budget Remaining | Policy State | Who Decides Changes |
|---|---|---|---|
| Green | >50% remaining | Normal operations | Standard change process applies |
| Yellow | 25–50% remaining | Cautious — SRE awareness required | SRE sign-off on all Tier 1 changes |
| Orange | 10–25% remaining | Restricted — reliability sprint triggered | Director approval for all Tier 1 changes; no Tier 4 |
| Red | <10% remaining | Freeze — non-critical deployments blocked | Director and VP approval for any Tier 1 change |
| Exhausted | 0% (SLO breach) | Emergency — reliability-only work | No feature deployments until next period |

### Policy Enforcement Mechanism

The error budget policy must be:
1. **Agreed in writing by product and engineering leadership** before the first enforcement
2. **Published and visible to all teams** (a dashboard, not a document in a drawer)
3. **Applied consistently** — the first waiver destroys the policy's authority

**Director rule**: If you need to grant an exception to an Orange/Red policy, do it in writing with explicit business justification and VP sign-off. Every exception is tracked. More than 2 exceptions in a quarter = policy is not working and needs revision.

---

## Feature Velocity vs. Stability: The Decision Framework

### When Velocity Wins
- Error budget is Green (>50%)
- Change is reversible (can be feature-flagged off)
- Automated rollback confirmed working
- No open Tier 1 incidents in the last 72 hours

### When Stability Wins
- Error budget is Yellow or below
- Open Tier 1 incidents or chronic reliability degradation
- Pending postmortem action items from a P0/P1 older than 2 weeks
- Upcoming peak traffic period (freeze calendar entry)
- Compliance audit in the next 30 days

### The "Reliability Sprint" Trigger

A reliability sprint is a time-boxed sprint where feature work is paused and the team focuses exclusively on reliability, debt, and postmortem action items.

**Trigger conditions** (any one is sufficient):
- Error budget <25% with more than 10 days remaining in the period
- 3 or more P1 incidents in a single month
- Postmortem action items older than 30 days from a Tier 1 P1
- CISO/audit flag on any Tier 1 system
- Director judgment that the team is operating in a chronic degraded state

**Director responsibility**: Call the reliability sprint. Do not wait for consensus. Communicate it to product leadership as a business decision, not an SRE request. Frame it as: "Our reliability indicators show we are operating outside acceptable risk. We are doing [X] weeks of reliability investment. Here is what we expect to come out of it."

---

## How Directors Set and Communicate This Policy to Product

### The Setup Conversation (Do This Before You Need the Policy)

Do not introduce the error budget policy during a conflict. Introduce it during a period of stability, ideally in a joint planning session with product leadership.

The framing:

> "I want to propose a shared framework for how we make deployment decisions when reliability is under stress. Right now we're in a good state. I want to use that to agree on a process so that when we're in a stressed state, we have a shared framework rather than a disagreement."

Get the product VP to agree to the principle before the first enforcement. Make it a shared framework, not an SRE policy imposed on product.

### The Enforcement Conversation (When You Have to Use It)

Key principles for the enforcement conversation:
1. **Come with data, not feelings**: error budget metrics, incident count, SLI trends
2. **Come with an alternate timeline**: "no, not this week" is a rejection; "not this week, and here's when" is a partnership
3. **Acknowledge the business cost**: "I understand this feature has been in development for [X] weeks. That effort is not wasted. Here is when it can deploy."
4. **Reference the shared agreement**: "This is the policy our VPs agreed to. I am applying it as written."

### The SLO/Error Budget Briefing Template (For Quarterly Business Reviews)

```
PLATFORM RELIABILITY SUMMARY — [Quarter] [Year]

HEADLINE METRIC: [Platform Name] achieved [X]% availability against [Y]% target.
Error budget consumed: [N]% of quarterly budget used.
Status: [Within target / Slightly above target / Exceeded target]

INCIDENTS
P0: [N] incidents | Average duration: [M] minutes | Change vs. last quarter: [+/-N]
P1: [N] incidents | Average duration: [M] minutes | Change vs. last quarter: [+/-N]
Change-induced incidents: [N]% of total

SLO TREND
[Sparkline or table: monthly SLO attainment for last 4 quarters]

TOP RELIABILITY INVESTMENTS THIS QUARTER
1. [Initiative — impact in plain English]
2. [Initiative — impact in plain English]
3. [Initiative — impact in plain English]

RISKS FOR NEXT QUARTER
1. [Risk — mitigation plan]
2. [Risk — mitigation plan]

WHAT WE NEED TO MAINTAIN THIS TRAJECTORY
[Specific asks: headcount, budget, architectural changes, product partnership on reliability debt]
```

---

## The Stability-vs-Innovation Balance: How Directors Make the Call

**The tension**: Product wants to move fast. The platform has scars from the last time someone moved too fast. Where is the line?

**The Director's answer**: The line is the error budget. It is not a judgment call — it is a measurement.

The more important question is: **how do you build a culture where product teams internalize this, rather than fighting it every sprint?**

The answer is co-ownership:
- Product VP and SRE Director co-own the error budget burn rate as a shared OKR
- Product PMs receive the same error budget dashboard that SRE engineers do
- Postmortem action items that originate from product-owned code are assigned to product teams, not SRE
- When a product team ships a release that improves reliability, they receive credit for it

When product teams own a piece of the reliability metric, they stop being the adversary of the reliability policy and start being its advocate.

---

## How to Handle a Team That Has Been Shipping Fast and Breaking Things

This is a culture and process problem, not just a technical one.

### Step 1: Diagnose Before You Prescribe
Before introducing process, understand why the team has been breaking things:
- Is it testing gaps? (no unit/integration tests, no staging environment)
- Is it deployment frequency without deployment safety? (deploying 10x/day without feature flags or automated rollback)
- Is it ownership fragmentation? (nobody knows who owns what — so nobody feels accountable for reliability)
- Is it incentive misalignment? (they are measured on features shipped, not on reliability)

### Step 2: Make the Cost Visible
Most teams that ship fast and break things have never seen the full cost of what they're doing. Show them:
- Hours of on-call engineer time consumed by their incidents (in FTE-hours)
- Revenue or SLA credit impact of their P1s
- Customer escalations traced to their service
- Error budget consumed by their deployments

Present this data without blame. "Here's what happened" not "here's what you did." The goal is awareness, not punishment.

### Step 3: Build the Safety Net Before Adding Friction
Do not add process friction before providing the safety tooling. The sequence is:
1. Give the team automated testing infrastructure (if they don't have it)
2. Give the team feature flags and rollback capability (if they don't have it)
3. Add deployment gates that enforce testing (automated friction, not manual process)
4. Then, if needed, add a change tier requirement for their services

If you add process without tooling, you will slow the team without making them safer. They will route around the process.

### Step 4: Create a Reliability Owner on the Team
The most effective change is giving one engineer on that team an explicit reliability mandate. Not "everyone is responsible for reliability" (which means nobody is). One named person who owns the error budget, attends SRE postmortems, and is the reliability liaison.

This creates internal pressure that is more effective than external governance.

---

*Policy version: 1.0 | Owner: Vishweshwar Chippa | Last reviewed: 2026-06-11*
*Requires sign-off from: VP Engineering, VP Product before enforcement*
