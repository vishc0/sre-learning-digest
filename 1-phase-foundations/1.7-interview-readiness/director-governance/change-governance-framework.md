# Change Governance Framework — Director Level
## The CAB That Actually Works

---

## The Core Problem Directors Face

Most change governance frameworks fail in one of two ways:

1. **Too bureaucratic**: Every change requires a 3-day approval cycle. Teams route around the process. Shadow deployments happen on Friday afternoons. The CAB becomes a rubber stamp.
2. **Too loose**: "Move fast" culture means high-severity incidents are caused by unreviewed changes. Post-incident reviews trace 70% of P1s back to change events.

A Director-level change governance framework solves this by **tiering the risk**, not applying the same friction to all changes.

**The governing principle**: Friction should be proportional to blast radius. A typo fix in a non-critical config should not require the same process as a database schema migration on a platform serving 25M messages/day.

---

## Change Tier Model

### Tier 0 — Emergency Change (Incident Mitigation)
- **Definition**: Change required to restore service during an active P0 or P1 incident.
- **Authorization**: On-call Incident Commander can authorize. Post-change review within 48 hours.
- **Process**: Implement now. Document simultaneously or immediately after. No waiting.
- **Risk**: Higher implementation error rate accepted in exchange for faster MTTR.
- **Director action**: Aware in real-time via incident bridge. Receive 48-hour post-change review.

### Tier 1 — Standard Change (Pre-approved)
- **Definition**: Change that is pre-reviewed, well-understood, has automated rollback, and has been performed successfully ≥3 times.
- **Examples**: Feature flag toggle, routine scaling event, known-good config update from library, minor dependency version bump with passing tests.
- **Authorization**: Engineer self-approves via runbook + automated pipeline gate.
- **Process**: Automated checks pass → Deploy. Log entry in change record system.
- **Director action**: Not involved. Reviews trend data weekly.

### Tier 2 — Normal Change
- **Definition**: Planned change with known risk, not yet pre-approved, affecting non-critical services or non-peak windows.
- **Examples**: New feature deployment to non-Tier-1 service, database index addition, moderate config change.
- **Authorization**: Tech Lead or Staff Engineer peer review + SRE sign-off if availability impact possible.
- **Process**: PR review → automated test gates → deployment window scheduled → change logged.
- **Director action**: Not involved. Sees in weekly change summary.

### Tier 3 — Significant Change
- **Definition**: Change with elevated blast radius — Tier 1 service, data-layer change, cross-team dependency, architectural modification.
- **Examples**: Database schema migration on production, Kubernetes version upgrade, changes to authentication or authorization systems, network policy modifications.
- **Authorization**: CAB review required. At minimum: requesting engineer, SRE lead, security representative.
- **Process**: Change request submitted 72 hours before deployment window. CAB review (async or synchronous depending on complexity). Rollback plan reviewed. Deployment window confirmed.
- **Director action**: Informed. Signs off if change is highest-criticality. Available during deployment window for escalation.

### Tier 4 — Major Change
- **Definition**: Platform-level, multi-team, or compliance-impacting change. Risk score 9+ in risk register. Requires coordination across orgs.
- **Examples**: Cloud provider migration, data center failover test, RBAC model change, third-party integration removal, capacity architecture change.
- **Authorization**: Director sign-off required. CISO or VP Engineering awareness.
- **Process**: Formal RFC (Request for Change) document. CAB full review with ≥5 days lead time. Rollback plan + communication plan required. Post-implementation review scheduled at time of approval.
- **Director action**: Owns approval. Communicates to VP. Available throughout.

---

## CAB Structure That Actually Works

### What a CAB Is Not
- Not a committee that reviews all changes
- Not a bureaucratic gate that slows teams down
- Not a blame-assignment body when things go wrong

### What a CAB Is
- A **risk calibration group** that reviews Tier 3 and Tier 4 changes
- A **knowledge-sharing forum** where cross-team change impacts are surfaced
- A **policy governor** that ensures the change tier model is applied consistently

### Membership
| Role | Attendance Model | Why This Role |
|---|---|---|
| SRE Director / Lead | Standing member | Risk and availability perspective |
| Security Engineer | Standing member | Vulnerability and compliance perspective |
| Platform Engineering Lead | Standing member | Infrastructure dependency awareness |
| Database Lead | Standing member for Tier 4; ad hoc for Tier 3 | Data layer change awareness |
| Product Eng Lead | Ad hoc — attends for their team's changes | Accountability + blast radius ownership |
| Network / Infrastructure | Ad hoc — attends when network-adjacent | Routing, DNS, firewall change awareness |

**Quorum**: Minimum 3 standing members for Tier 3. All standing members for Tier 4.

**Meeting cadence**: Weekly 30-minute standing CAB for Tier 3 submissions. Async review via shared document for Tier 3 changes with no controversy. Emergency CAB (ad hoc) for Tier 4 when timeline is compressed.

### CAB Review Questions (Use This as the Agenda)
1. What is the blast radius if this change fails? (How many customers affected? How long to detect?)
2. What is the rollback plan, and how long does rollback take? Has it been tested?
3. What automated testing validates this change before it reaches production?
4. What is the deployment window, and why was it chosen? (Avoid high-traffic periods for Tier 3+)
5. Who is the change owner during the deployment window, and how are they reachable?
6. Is there a communication plan for impacted teams and customers?
7. Has a similar change caused incidents before? What's different this time?

---

## Change Freeze Policy

### Freeze Types
| Freeze Type | Trigger | Scope | Duration |
|---|---|---|---|
| Error Budget Freeze | Error budget >80% consumed | No Tier 3 or Tier 4 changes | Until budget resets or Director exception granted |
| Incident Freeze | Active P1 or P0 incident | No non-Tier-0 changes | Until incident closed + 24-hour stability window |
| Holiday/Peak Freeze | Pre-defined high-traffic periods | No Tier 3 or Tier 4 changes | Per published freeze calendar |
| Compliance Freeze | Audit period | Changes to audit-scope systems require CISO approval | Per audit schedule |

### Freeze Calendar (Example)
- Jan 1–2: New Year
- Nov 25 – Dec 2: Thanksgiving/Cyber Monday (adjust per industry)
- Dec 24 – Jan 2: Year-end holiday
- [Add company-specific peak periods: quarterly earnings, major product launches, regulatory reporting dates]

### How to Manage Freeze Exceptions
All freeze exceptions must be:
1. Requested in writing (Slack + ticket) by the requesting engineer's manager
2. Reviewed by the Director (or delegate)
3. Documented with: business justification, rollback plan, approval chain
4. Tracked as an exception in the change register

**Director rule**: If you grant an exception and the change causes an incident, you own that outcome. Grant exceptions on evidence, not pressure.

---

## Change Metrics Directors Track

| Metric | What It Measures | Target | Alert Threshold |
|---|---|---|---|
| Change volume by tier | Are changes being tiered correctly? | Tier 1 > 60% of total changes | Tier 3+ > 20% = tiering problem |
| Change-induced incidents | % of incidents triggered by changes | <30% of P1s attributed to change | >50% = change process failure |
| CAB review cycle time | Time from Tier 3 submission to approval | <24 hours for standard Tier 3 | >72 hours = bureaucracy problem |
| Rollback execution rate | % of Tier 3+ changes that required rollback | Track trend, no hard target | Rising trend = change quality problem |
| Freeze violations | Changes deployed during freeze without exception | 0 | Any = process failure, investigate |
| Pre-approved change adoption | % of Tier 1 changes using standard runbooks | >80% | <60% = runbook library needs work |

---

## How Directors Govern Change Without Being in Every Review

The Director should never be reviewing Tier 1 or Tier 2 changes. The Director's job is:

1. **Design the tier model** — calibrate what belongs in each tier for your specific platform and risk profile
2. **Staff the CAB correctly** — right people with authority and context
3. **Review metrics weekly** — not individual changes, but trend data
4. **Audit tier classification quarterly** — randomly sample 10 changes and verify they were tiered correctly
5. **Own Tier 4 changes directly** — those are the ones with organizational consequences
6. **Make freeze exceptions the exception** — protect the policy by not becoming its first violator

---

## Change Request Template (Tier 3 and Tier 4)

```
CHANGE REQUEST: [Change Title]
ID: CR-[YYYY-MM-DD-NNN]
Tier: [3 / 4]
Requested by: [Name, Team]
Submitted: [Date]
Requested deployment window: [Date, Time, Duration]

DESCRIPTION
What is changing and why? (2-3 sentences, plain English)

IMPACT
Services affected: [List]
Expected customer impact during change: [None / Degraded / Full impact]
Blast radius if change fails: [Describe worst case]

ROLLBACK
Rollback procedure: [Link to runbook]
Rollback execution time: [Estimate]
Rollback tested in non-production: [Yes / No — if No, explain why not]

VALIDATION
Automated tests confirming change is safe: [Link to CI results]
Monitoring that confirms change is healthy post-deploy: [Specific alerts / dashboards]
Health check criteria (how do you know the change succeeded): [Define]

COMMUNICATION PLAN
Teams notified: [List]
Customer communication required: [Yes / No — if Yes, who owns it?]
On-call engineer assigned for deployment window: [Name]

CAB APPROVAL
Approved by: [Names, dates]
Conditions / notes: [Any special instructions]
```

---

*Framework version: 1.0 | Owner: Vishweshwar Chippa | Created: 2026-06-11*
