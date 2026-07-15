# Scenario 07 — Incident-Driven Architecture Change

**System**: Shopping Cart Platform — Auth Service  
**Pattern**: Connection pool exhaustion → PgBouncer addition  
**SRE Concepts**: RCR, OL, MRI, RDR, CSD, RV, SRD, CC  
**Difficulty**: Principal

---

## 1. Concept: When Configuration Fixes Are Not Enough

SRE practice distinguishes between two categories of reliability failure. The first category responds to configuration changes: raise a timeout, increase a replica count, tune a rate limiter. The second category does not. It is caused by a structural pattern in the architecture itself — a pattern that will re-trigger the same incident class regardless of how carefully the system is operated. This second category is called **Structural Reliability Debt (SRD)**.

SRD is not the same as technical debt. Technical debt degrades code quality and developer velocity. Structural reliability debt degrades production stability and consumes error budget at a rate that no amount of alerting, runbook improvement, or on-call sharpness can offset. The signature of an SRD item is a repeating incident with the same root cause, arriving on a predictable cadence.

Auth Service presents a textbook SRD signature. Three SEV1 incidents in 90 days. All three share an identical root cause: PostgreSQL connection pool exhaustion at peak traffic. The arithmetic is deterministic: 8 pods × 50 HikariCP connections = 400 connection attempts; PostgreSQL `max_connections = 300`. At peak load, 100 connections are always refused. This is not a bug. It is an architectural ceiling that was never reconciled with the scale the system is expected to run at.

**The central challenge of incident-driven architecture change**: the recurrence pattern creates urgency and organizational pressure to move fast. But the proposed fix — adding PgBouncer as a connection proxy — is itself an architectural change with its own failure modes. Moving fast under pressure is precisely when teams introduce displacement risk: the original failure mode is eliminated, but a new failure mode of equal or greater severity is introduced in its place. SRE's role is to quantify the risk of the fix before it ships, not after.

---

## 2. Structural Reliability Debt: Definition and Identification

**SRD** is an architectural pattern that directly and repeatedly causes production incidents, where the root cause cannot be resolved without changing the architecture. SRD items are identified through postmortem pattern analysis: if three or more postmortems in a rolling 90-day window share the same root cause taxonomy, that root cause is an SRD candidate.

Auth Service qualifies. The postmortem action items for all three SEV1s read identically: "increase HikariCP pool size." That action item was closed each time. The incident recurred because the action item addressed a symptom, not the structural cause. Once an SRD item is identified, the SRE team must do two things: compute the cost of continuing to absorb the incidents (RCR), and compute the value of eliminating the root cause (OL).

---

## 3. Recovery Cost Ratio (RCR)

**Formula**: `RCR = (response_hours × frequency) / fix_hours`

Each SEV1 incident: 45-minute MTTR, 2 SREs engaged = 1.5 engineer-hours per incident. Three incidents in 90 days = 4.5 engineer-hours of incident response per quarter, not counting postmortem time, stakeholder communication, or the error budget consumed during each 45-minute outage window.

PgBouncer implementation cost: one engineer, 3 weeks. Assuming a standard 40-hour week: 120 engineer-hours.

```
RCR = (1.5 hrs × 3 incidents) / 120 hrs
RCR = 4.5 / 120
RCR = 0.038
```

An RCR below 1.0 means the fix costs more than the current incident cadence — in raw engineering hours. RCR = 0.038 looks like a weak justification, but this analysis is incomplete. RCR in raw hours ignores three factors that matter operationally: (1) the error budget cost of each incident, (2) the business revenue impact of a 45-minute Auth outage during peak traffic, and (3) the projected incident recurrence rate if nothing changes. At the current cadence, Auth produces 12 SEV1s per year. In year two, incident response alone consumes 18 engineer-hours — still less than the 120-hour fix. But PgBouncer, once deployed, has near-zero incremental cost. The fix is a capital investment; the incident cadence is an operating cost that compounds. Over a two-year horizon, RCR crosses 1.0 at month 14. The investment is justified; the break-even is not immediate.

**Takeaway**: RCR alone does not authorize an architecture change. It establishes the cost floor. The authorization comes from OL.

---

## 4. Operational Leverage (OL)

**Formula**: `OL = Δ(error_budget_consumption) / SRE_hours_invested`

Auth Service declared SLO: 99.990% availability. Monthly error budget: 4.38 minutes.

Current state: MTBI = 30 days, MTTR = 45 minutes. One incident per 30 days consumes 45 minutes of downtime against a 4.38-minute monthly budget. Error budget burn rate = 45 / 4.38 = **10.27×** the monthly budget per incident. Auth is operating in permanent error budget deficit. The SLO is not being met; it is a declared number that bears no relationship to actual availability.

Post-PgBouncer projection: connection pool exhaustion is eliminated as a failure mode. MTBI improves to 180 days (6× improvement). At that cadence, one incident per 180 days produces 45 minutes of downtime over a 6-month window, against a 6-month budget of 26.28 minutes. Budget consumption per incident = 45 / 26.28 = 1.71×. Still a budget burn event, but no longer a structural deficit.

```
Δ(error_budget_consumption) = (10.27× - 1.71×) = 8.56 budget-multiples eliminated per incident cycle
SRE_hours_invested = 120 hours (PgBouncer implementation)

OL = 8.56 / 120 = 0.071 budget-multiples per SRE-hour invested
```

OL quantifies the return on SRE investment in reliability engineering terms. Each hour spent on PgBouncer implementation reclaims 0.071 units of error budget burn rate. Over the 120-hour investment, the structural deficit is converted to a manageable overage. This is the authorization for the change.

---

## 5. Migration Risk Index (MRI) for PgBouncer Addition

PgBouncer sits directly in the critical path between Auth Service and PostgreSQL. Auth Service has a Dependency Grade (DG) of 18 — 18 services depend on Auth. Every one of those downstream services inherits the risk of the PgBouncer layer. The Cascade Coefficient (CC) of Auth is 10.8, meaning a full Auth outage propagates through 10.8× its own blast radius in downstream failures.

MRI captures the risk of introducing a new component into a high-DG path:

```
MRI components:
- DG of affected path: 18 (unchanged — PgBouncer is not a new dependency for callers)
- New component failure modes introduced: 3 (queue saturation, process crash, misconfiguration)
- Rollback complexity: Low (env var change, RV = 5 minutes)
- Change surface: Medium (3 touch points — see CSD below)

MRI rating: MEDIUM-HIGH
```

The MRI does not block the change. It determines the validation requirements before the change ships. A MEDIUM-HIGH MRI requires: staged rollout (one pod at a time), pre-production load testing under peak connection demand, and a documented rollback trigger threshold.

---

## 6. The Displacement Risk: PgBouncer's Own Failure Modes

PgBouncer eliminates in-process connection pool exhaustion. It does not eliminate the finite capacity of PostgreSQL. It relocates the queue. The new failure modes introduced are:

**PgBouncer queue saturation**: PgBouncer queues client connections when the server pool is exhausted. Under sustained overload, the queue fills and clients receive connection refused errors — identical in user impact to the original failure, but now at PgBouncer rather than PostgreSQL. Pre-validation: load test at 1.5× peak connection demand. Confirm PgBouncer queue depth metrics are observable before go-live.

**PgBouncer process crash**: PgBouncer is a single-threaded process. A crash removes all Auth-to-PostgreSQL connectivity instantly. This is a higher-severity failure mode than HikariCP exhaustion, which degrades gradually. Mitigation: deploy PgBouncer with a process supervisor (systemd or Kubernetes liveness probe with restart policy `Always`). Establish a mean time to restart baseline before go-live.

**Pool mode misconfiguration**: PgBouncer supports three pool modes: session, transaction, and statement. Auth Service uses PostgreSQL transactions. The correct mode is `transaction`. If deployed in `session` mode, each Auth request holds a server connection for the duration of the session rather than the transaction — the connection count behavior is identical to the current in-process pool, and the fix provides no benefit. This is the most likely misconfiguration vector. Pre-validation: verify pool mode in PgBouncer configuration file before deployment; add a startup assertion in Auth Service that confirms connection behavior matches expectations.

---

## 7. Change Surface Delta (CSD)

CSD captures the total surface area of a change — every file, configuration, and system component that must be modified or created.

| Touch Point | Change Type | Risk Level |
|---|---|---|
| Auth Service `application.yml` | JDBC URL changed from PostgreSQL direct to PgBouncer endpoint | Low — env var swap |
| PgBouncer deployment (new) | New Kubernetes Deployment + ConfigMap + Service | Medium — net-new component |
| PostgreSQL `pg_hba.conf` | Add PgBouncer host as authorized client | Low — additive change |

CSD = 3 touch points. Moderate surface. The highest-risk touch point is the PgBouncer deployment itself — a new component with no production history in this environment. Every other touch point is a modification to existing configuration.

---

## 8. Rollback Architecture and Rollback Velocity (RV)

**Rollback design**: Auth Service connects to PgBouncer via an environment variable (`DB_HOST`). To bypass PgBouncer, change `DB_HOST` from the PgBouncer service endpoint back to the PostgreSQL service endpoint and trigger a rolling restart of Auth Service pods.

**RV = 5 minutes**: time for a rolling restart of 8 Auth pods at a 30-second interval.

**Post-rollback behavior**: HikariCP connection pools are cold on startup. Each Auth pod requires approximately 2 minutes to warm its connection pool to steady-state performance. During this window, Auth latency will be elevated as connections are established. This is not a failure; it is expected behavior. The runbook must document this so the on-call engineer does not interpret elevated latency post-rollback as a rollback failure and trigger a second intervention.

**Rollback trigger**: if PgBouncer introduces a new connection failure mode that is not queue saturation (i.e., a crash or misconfiguration causing hard errors), rollback immediately. If the issue is queue saturation (soft degradation), engage the PgBouncer queue depth runbook before escalating to rollback.

---

## 9. RDR Tracking Plan

**Formula**: `RDR = post_change_incident_rate_new_mode / pre_change_incident_rate_original_mode`

**Original failure mode**: PostgreSQL connection refused errors (`FATAL: remaining connection slots are reserved`) appearing in Auth Service logs during peak traffic windows. Incident rate pre-change: 1 per 30 days.

**New failure mode**: PgBouncer queue saturation errors (`ERROR: no more connections allowed`) or PgBouncer process unavailability. These are distinct error strings and can be differentiated in Splunk without ambiguity.

**90-day monitoring window**: begin on PgBouncer go-live date. Sample the following metrics weekly:
- Auth Service error rate by error type (PostgreSQL connection refused vs. PgBouncer queue saturation)
- PgBouncer active connections and queue depth at peak traffic
- Auth MTBI (rolling)

**RDR interpretation**:
- `RDR < 0.10`: original failure mode is effectively eliminated; new mode is rare. Success.
- `0.10 ≤ RDR < 0.50`: partial displacement. PgBouncer is providing benefit but a new failure pattern is emerging. Investigate queue depth tuning.
- `RDR ≥ 0.50`: displacement is significant. PgBouncer has introduced a new failure class at a rate comparable to the original. Re-evaluate the architecture decision.

**Success declaration criteria** (30-day observation window post go-live):
1. Zero connection pool exhaustion incidents of original failure mode type
2. PgBouncer queue depth peaks below 80% of configured maximum during peak traffic
3. Auth MTBI trend line is improving (no new SEV1s in 30-day window)
4. RDR measured at day 30 < 0.10

---

## 10. Structural Reliability Debt: Broader Framework

SRD items share a common taxonomy. They are identified by postmortem pattern analysis, not by individual incident review. The process:

1. **Pattern query**: pull all postmortems from the last 90 days. Group by root cause taxonomy. Any root cause appearing 3+ times is an SRD candidate.
2. **Structural test**: ask whether the root cause can be resolved without changing the architecture. If yes, it is a configuration debt item, not SRD. If no, it is SRD.
3. **Prioritization**: rank SRD items by `(incident_frequency × MTTR × CC)`. Higher values represent greater operational drag. Auth Service scores: `(1/30 days × 45 min × 10.8) = 16.2`. This is the operational drag index — how much operational capacity this SRD item consumes per day.
4. **Remediation planning**: every SRD item requires an MRI assessment before remediation is approved. The fix is an architecture change; architecture changes have their own failure surface and must be treated as migration events with CSD, RV, and RDR tracking built in from the start.

The discipline of SRD management is what separates reactive SRE practice from proactive reliability engineering. Reactive practice treats each incident as an independent event. Proactive practice sees the pattern, names the structural cause, quantifies the cost, and engineers the removal — accepting the short-term migration risk in exchange for the long-term elimination of the failure class.

Auth Service's SRD item is connection multiplexing architecture mismatch: a system designed for 2 pods operating at 25 connections each, running at 8 pods at 50 connections each, against a database configured for a world that no longer exists. PgBouncer is not a workaround. It is the correct architectural layer for decoupling application connection demand from database connection capacity. The MRI is real, the RV is adequate, and the OL justifies the investment. The change ships — with a tracking plan, a rollback architecture, and a 90-day RDR window that will tell you whether the problem was solved or displaced.

---

*SRECapstone Scenario 07 — Principal Level | Connection Pool Architecture | PgBouncer Migration Pattern*
