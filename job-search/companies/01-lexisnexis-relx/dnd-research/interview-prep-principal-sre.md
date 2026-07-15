# Principal SRE / SRE Manager Interview Prep (LexusNexus)

This guide captures likely interview questions and the kinds of answers typically expected for a **Principal SRE** or **SRE Manager** role in a platform-heavy enterprise like LexusNexus.

> Note: This is a practical prep guide based on common SRE hiring patterns and the architecture/tooling context documented in this workspace.

## What interviewers are usually validating

1. **Systems reliability depth:** Can you design and operate reliable services at scale?
2. **Leadership effectiveness:** Can you build teams/processes that sustain reliability over time?
3. **Business alignment:** Can you translate reliability into customer and revenue impact?

## Core Questions You Can Expect (with Typical Strong Answers)

### 1) How do you define and implement SLOs?
**What they expect to hear:**
- Clear distinction between **SLI**, **SLO**, and **SLA**
- Business-aligned reliability targets
- Error budget policy tied to release decisions

**Strong answer pattern:**
- Pick user-critical SLIs (availability + latency)
- Set SLOs based on business tolerance and user impact
- Track error budget burn rates
- Use error budget as a deployment/release gate
- Recalibrate SLOs with product maturity

---

### 2) What are your golden signals for a platform?
**What they expect:**
- Operational clarity and observability maturity

**Strong answer:**
- Latency, traffic, errors, saturation
- Journey-level views (login, checkout, notification delivery)
- Layered dashboards (edge/API/service/DB/dependency)

---

### 3) How do you reduce alert fatigue?
**What they expect:**
- Signal quality discipline

**Strong answer:**
- Alert only on user-impacting conditions and SLO risk
- Use multi-window burn-rate alerting
- Remove noisy/non-actionable alerts
- Track and reduce false positive rate and page volume

---

### 4) Walk us through a Sev-1 incident you led.
**What they expect:**
- Structured incident leadership under pressure

**Strong answer structure (STAR):**
- Situation and business impact
- Immediate stabilization action
- Role clarity (IC/comms/ops)
- Root-cause analysis and mitigation
- Postmortem actions with owners and deadlines

---

### 5) How would you design high availability across regions?
**What they expect:**
- Architecture tradeoff fluency

**Strong answer:**
- Choose active-active vs active-passive by consistency needs and cost
- Define service-tiered RTO/RPO
- Add automated health checks and failover workflows
- Validate through regular game days

---

### 6) How do you handle unreliable third-party dependencies?
**What they expect:**
- Resilience patterns and defensive design

**Strong answer:**
- Timeouts, retries (with exponential backoff + jitter)
- Circuit breakers and bulkheads
- Graceful degradation and fallback modes
- Dependency-specific SLIs/SLOs and escalation criteria

---

### 7) How do you approach capacity planning?
**What they expect:**
- Predictive operations and risk control

**Strong answer:**
- Forecast from trends + seasonality + business events
- Set explicit headroom policies for critical services
- Run load/stress tests before peak periods
- Tie autoscaling thresholds to observed saturation

---

### 8) Which reliability KPIs do you report?
**What they expect:**
- Outcome-based reliability management

**Strong answer:**
- SLO attainment
- Error budget burn
- MTTA / MTTR
- Change failure rate
- Incident recurrence rate
- Toil percentage

---

### 9) What does a blameless postmortem look like in practice?
**What they expect:**
- Culture + rigor

**Strong answer:**
- Focus on system conditions, not blame
- Accurate timeline and contributing factors
- Prioritized corrective actions
- Action ownership and closure tracking

---

### 10) How do you split ownership between Product teams and SRE?
**What they expect:**
- Clear operating model

**Strong answer:**
- Platform SRE: shared runtime, observability, reliability guardrails
- Product teams: service correctness and feature-level ownership
- Embedded SRE: co-own SLOs, readiness, resilience tests
- Formal RACI and escalation boundaries

---

### 11) How do you improve release reliability?
**What they expect:**
- Safe delivery and change risk control

**Strong answer:**
- Progressive delivery (canary/blue-green)
- Automated rollback criteria
- Performance and reliability gates in CI/CD
- Change windows based on risk and supportability

---

### 12) How do you prioritize reliability work vs feature delivery?
**What they expect:**
- Senior-level prioritization and influence

**Strong answer:**
- Use objective signals (error budget, incidents, customer impact)
- Convert reliability debt into quantifiable business risk
- Reserve explicit roadmap capacity for reliability
- Present tradeoff options with impact/cost/timeline

---

### 13) How do you lead and grow SRE teams? (Manager track)
**What they expect:**
- People leadership and organizational design

**Strong answer:**
- Define role ladder and expectations by level
- Coach on incident leadership and system design
- Build sustainable on-call practices
- Hire for collaboration + systems thinking + ownership

---

### 14) How do you manage executive communication during incidents?
**What they expect:**
- High-quality stakeholder communication

**Strong answer:**
- Predictable update cadence (e.g., every 15–30 min)
- Separate technical and executive channels
- Clear statements: impact, mitigation, ETA confidence, risk
- One source of truth for timeline and decisions

---

### 15) What would your 30-60-90 day plan be?
**What they expect:**
- Strategic onboarding and early impact

**Strong answer:**
- **First 30 days:** map services, SLO baseline, incident review, top risks
- **60 days:** reduce alert noise, improve runbook quality, dependency hardening plan
- **90 days:** measurable gains (e.g., MTTR down, fewer noisy pages, improved SLO attainment)

## Answer Style Interviewers Reward

- Use metrics and outcomes (before/after)
- Explain tradeoffs (reliability, latency, cost, delivery speed)
- Keep answers concrete (tools + process + result)
- Frame reliability in business terms (customer trust, revenue, risk)

## High-ROI Prep Checklist

- Prepare **3 incident stories**:
  1. Major Sev-1 outage
  2. Chronic reliability issue fixed over time
  3. Near-miss prevented by controls

- Prepare **2 leadership stories**:
  1. Cross-team conflict alignment
  2. Process/system improvement with measurable impact

- Prepare **1 architecture narrative**:
  - End-to-end reliability model for edge, services, data, and dependencies

- Prepare your metric snapshots:
  - MTTR, MTTA, change failure rate, SLO attainment, incident recurrence

## Suggested One-Minute Positioning Statement

“I bring a hybrid reliability leadership model: strong platform engineering fundamentals, embedded partnership with product teams, and disciplined incident/postmortem operations. I focus on measurable outcomes—improving SLO attainment, reducing MTTR and change failure rate, and creating sustainable on-call systems while enabling faster and safer delivery.”

## Related Documents in This Workspace

- [`tools.md`](./tools.md)
- [`platform-architecture.md`](./platform-architecture.md)
