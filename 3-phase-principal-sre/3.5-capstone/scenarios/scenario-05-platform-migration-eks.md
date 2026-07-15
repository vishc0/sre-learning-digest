# Scenario 05 — Platform Migration: EKS 1.27 → 1.30 (Blue-Green Cluster Strategy)

**Domain**: Platform Engineering / SRE  
**System**: Shopping Cart — 12 microservices  
**Starting State**: FLI=0.72, OCR_weighted=0.457, 5 P0 services  
**Risk Class**: CRITICAL — highest-risk change class in the SRE framework

---

## 1. Why Platform Migration Is the Highest-Risk Change Class

Most changes in the SRE framework affect one service at a time. A dependency update, a new feature flag, a database schema migration — each has bounded blast radius. Platform migration is categorically different because it applies simultaneously to every service running on the platform.

When you upgrade EKS from 1.27 to 1.30, you are not upgrading one microservice. You are replacing the substrate that all 12 microservices depend on. Every Kubernetes API call, every admission webhook, every network policy, every ingress rule — all of them execute against the new control plane simultaneously. There is no such thing as a partial platform upgrade. You cannot upgrade Auth while leaving Checkout on the old version.

This simultaneity is what makes platform migration the highest-risk class:

- **Change Surface Delta (CSD)** is maximized — all 12 services × all manifests × all deprecated API removals
- **SLO Coherence Score (SCS)** is invalidated for all services simultaneously — no prior SLO baseline exists for the green cluster
- **Observability Coverage Ratio (OCR)** drops to zero on the green cluster until the full monitoring stack is reinstalled and validated
- **Failure Locality Index (FLI)** must be revalidated — a misconfigured network policy on green can cascade across all 12 services simultaneously

Between Kubernetes 1.27 and 1.30, three beta API groups were promoted to stable and their beta versions removed from the API server. The most impactful removal for this system is `networking.k8s.io/v1beta1` Ingress, which was promoted to `networking.k8s.io/v1` in 1.22 and its beta removed in 1.25. Any manifest still referencing the v1beta1 API will be rejected by the green cluster's API server on first apply — silently breaking the service deployment without a clear error in the CI pipeline unless a specific gate is in place.

**Why blue-green is the only safe approach for major version jumps**: An in-place upgrade of a 12-service production cluster leaves no clean rollback path. If the upgrade fails at service 7, you have a partially upgraded cluster in an undefined intermediate state. Blue-green means the old cluster (blue) continues serving 100% of production traffic while the new cluster (green) is built, validated, and loaded. Traffic shifts are discrete, measured decisions — not a point of no return.

---

## 2. SSE — Simultaneous SLO Exposure

**Formula**: `SSE = (services_in_cutover / total_services) × avg(1 − SLO_margin_remaining)`

SSE governs the pacing of traffic shifts. It answers the question: at this moment, how much SLO margin is being simultaneously consumed across the system by services in an active cutover state?

During a cluster migration, all 12 services are in cutover state during any traffic shift. The number of `services_in_cutover` is always 12 for a full cluster blue-green. What varies is the SLO margin remaining as traffic load increases on the green cluster.

Assume each service enters the migration with an average SLO margin of 18% remaining (conservatively — some services have been running hot). At 50% traffic shift:

```
services_in_cutover = 12
total_services = 12
avg(1 − SLO_margin_remaining) = avg(1 − 0.18) = 0.82

SSE = (12/12) × 0.82 = 0.82
```

At 50% shift, SSE = **0.82** — dangerously above the "high" threshold of 0.25. This is why naive thinking ("we'll just cut over at 50% and watch for problems") fails. Half the traffic to an unvalidated cluster means full SLO exposure for all services simultaneously.

**At what traffic percentage does SSE exceed 0.25?**

SSE exceeds 0.25 as soon as any production traffic hits the green cluster, because all 12 services are simultaneously in cutover (`services_in_cutover / total_services = 1.0`). The constraint equation resolves to:

```
0.25 = 1.0 × avg(1 − SLO_margin_remaining)
→ avg(SLO_margin_remaining) must be ≥ 0.75 before first shift
```

This means services must hold at least 75% of their error budget before the first traffic shift to green. Any service below that threshold must be remediated first.

**Traffic shift schedule that keeps SSE < 0.15 throughout**:

To hold SSE < 0.15 with all 12 services in cutover, services must maintain `avg(SLO_margin_remaining) > 0.85` throughout every shift window. This dictates a minimum 72-hour observation window between shifts, with rollback triggered if any P0 service drops below 85% margin.

| Shift Step | Traffic to Green | Required avg SLO Margin | Observation Window |
|------------|-----------------|------------------------|-------------------|
| 1          | 2%              | ≥ 85%                  | 24 hours          |
| 2          | 5%              | ≥ 85%                  | 24 hours          |
| 3          | 10%             | ≥ 85%                  | 48 hours          |
| 4          | 25%             | ≥ 87%                  | 72 hours          |
| 5          | 50%             | ≥ 90%                  | 72 hours          |
| 6          | 75%             | ≥ 92%                  | 48 hours          |
| 7          | 100%            | ≥ 95%                  | Blue decommission gate |

---

## 3. MRI — Migration Risk Index

**Formula**: `MRI = DG × CD × (1 − FLI) × (2 − OCR_weighted)`

Using the highest-risk service (Auth) for DG, Checkout for CD as the most change-dense service:

```
DG = 18 (Auth)
CD = 5 (Checkout)
FLI = 0.72
OCR_weighted = 0.457

MRI = 18 × 5 × (1 − 0.72) × (2 − 0.457)
    = 90 × 0.28 × 1.543
    = 90 × 0.432
    = 38.9
```

An MRI of **38.9** is in the extreme-risk band. The SRE framework defines MRI > 8 as requiring pre-migration remediation before traffic shift authorization. MRI > 20 requires a formal migration readiness review with engineering leadership sign-off.

**To bring MRI below 8**, the remediation targets are ordered by leverage:

1. **Reduce DG**: Auth's dependency graph score of 18 reflects deep coupling. Prior to migration, dependency hardening (circuit breakers, async fallbacks for non-critical paths) can reduce effective DG. Target: DG ≤ 12.
2. **Improve FLI**: At 0.72, failures are only moderately contained. Network policy hardening on the green cluster — enforcing namespace isolation before any service deploys — can improve FLI to ≥ 0.85. Target: FLI ≥ 0.85.
3. **Improve OCR**: At 0.457, less than half the service behavior is observable. Full observability stack deployment on green (see Section 5) must bring OCR_weighted to ≥ 0.85 before first shift. Target: OCR ≥ 0.85.

With remediation (DG=12, FLI=0.85, OCR=0.85):
```
MRI = 12 × 5 × (1 − 0.85) × (2 − 0.85)
    = 60 × 0.15 × 1.15
    = 60 × 0.1725
    = 10.35
```

Further hardening to FLI=0.90 and OCR=0.90 yields:
```
MRI = 12 × 5 × 0.10 × 1.10 = 6.6
```

MRI = 6.6 clears the threshold. The required pre-migration work is: DG hardening on Auth, network policy isolation on green, and full observability bootstrap before any traffic shift authorization.

---

## 4. The Deprecated API Problem

Kubernetes 1.30 rejects any manifest referencing removed API versions at the API server level. The manifest apply fails with `no matches for kind "Ingress" in version "networking.k8s.io/v1beta1"`. This failure is silent in pipelines that only check exit codes from `helm upgrade --dry-run` against the old cluster.

**Identification strategy before cutover**:

Run `kubeval` or `pluto` against all 12 Helm chart rendered outputs, targeting the 1.30 API schema. Pluto is preferred because it maintains a deprecation database keyed by Kubernetes version:

```bash
helm template ./charts/auth | pluto detect - --target-versions k8s=v1.30.0
```

Run this against all 12 charts in CI. Any deprecated API hit blocks the pipeline.

**CI gate**: Add a `deprecated-api-scan` job to the pre-merge pipeline that runs before any chart diff or deployment job. The gate must execute against the rendered manifest output (not the raw chart templates), because some deprecated API references are injected by Helm library charts or external chart dependencies — they do not appear in `values.yaml`.

The 1.27 → 1.30 removal list for this system includes:
- `networking.k8s.io/v1beta1` Ingress → must be `networking.k8s.io/v1`
- `policy/v1beta1` PodDisruptionBudget → must be `policy/v1`
- `batch/v1beta1` CronJob → must be `batch/v1`

All 12 service charts must be audited, updated, and validated against the 1.30 API server before green cluster provisioning is marked ready.

---

## 5. Green Cluster Observability Bootstrap

The green cluster starts with OCR_weighted = 0. No scrape configs, no alert routing, no dashboards, no log forwarding. This is not a gap that can be tolerated at any point during traffic shift. Shifting traffic to an unmonitored cluster is operationally equivalent to flying blind — an incident on green will not produce alerts, and MTTR will be measured in hours rather than minutes.

**Minimum OCR_weighted before first traffic shift**: Using the MRI threshold analysis from Section 3, OCR_weighted must reach ≥ 0.85 before traffic shift authorization. This is not a soft recommendation — it is a hard gate enforced by the migration readiness checklist.

**Observability bootstrap sequence** (must complete in order, each step validated before proceeding):

1. Deploy Prometheus operator and scrape configs for all 12 service endpoints
2. Validate that all 12 services appear in Prometheus targets with `up=1`
3. Deploy Grafana with dashboard provisioning — verify all golden signal dashboards load with live data
4. Configure Alertmanager with PagerDuty routing — send a test alert, confirm receipt
5. Deploy Fluent Bit with log forwarding to the same log aggregation backend as blue
6. Validate log ingestion by generating a known log line and confirming it appears in the aggregation backend
7. Recompute OCR_weighted: if < 0.85, identify which services are missing coverage and remediate before proceeding

Steps 1-7 must complete before the green cluster receives any production traffic. The observability bootstrap is estimated at 6-8 hours for an experienced SRE. Plan accordingly — it is not a parallel-to-traffic-shift activity.

---

## 6. Traffic Shift Schedule with SSE at Each Step

The detailed shift schedule from Section 2 expanded with SSE calculations at each step, assuming SLO margin is actively maintained at the minimum required threshold:

| Step | Traffic % | services_in_cutover | avg(1−SLO_margin) | SSE   | Go Criteria                          |
|------|-----------|--------------------|--------------------|-------|--------------------------------------|
| 0    | 0%        | 0                  | —                  | 0.000 | OCR ≥ 0.85, MRI < 8, CI green       |
| 1    | 2%        | 12                 | 0.13               | 0.130 | All P0 error budgets > 85%           |
| 2    | 5%        | 12                 | 0.13               | 0.130 | No P0 alerts on green, 24hr clean    |
| 3    | 10%       | 12                 | 0.14               | 0.140 | Latency p99 within 5% of blue        |
| 4    | 25%       | 12                 | 0.13               | 0.130 | All SLIs tracking within tolerance   |
| 5    | 50%       | 12                 | 0.10               | 0.100 | 72hr clean window, no budget burn    |
| 6    | 75%       | 12                 | 0.08               | 0.080 | Blue cluster on standby, RV tested   |
| 7    | 100%      | 12                 | 0.05               | 0.050 | Blue decommission gate (Section 8)   |

SSE remains below 0.15 at every step by enforcing the error budget reservation before each shift. Any step where the go criteria are not met holds at the current percentage and extends the observation window.

---

## 7. RV — Rollback Velocity

Route 53 weighted routing can be adjusted to send 100% traffic back to the blue cluster in under 60 seconds — that is the DNS propagation time for a weight change. However, RV is not the DNS change time. RV is the time from rollback decision to restored service state for all affected users.

**Full rollback sequence and time accounting**:

| Action | Time | Notes |
|--------|------|-------|
| Route 53 weight updated (green=0, blue=100) | ~60 seconds | DNS TTL must be pre-reduced to 60s before any traffic shift |
| DNS propagates to CDN edge nodes | 60-120 seconds | Depends on CDN TTL settings |
| In-flight requests to green complete or timeout | Up to 30 seconds | Depends on service timeout config |
| Session state on green (cart, auth tokens) | Variable | Must be backed by shared Redis — not green-local |
| Users with green DNS cached re-resolve | Up to TTL seconds | TTL must have been lowered before shift began |

**Total RV for full rollback**: 3-5 minutes under ideal conditions (TTL pre-reduced, Redis shared, no green-local session state). Up to 15-20 minutes if TTL was not pre-reduced.

The DNS TTL for all shopping cart endpoints must be reduced from the default (typically 300-3600 seconds) to 60 seconds at least one TTL cycle before the first traffic shift. This is a pre-migration task that must be completed 24 hours before Step 1 of the shift schedule.

Session state is the critical dependency: any session data stored in green-local cache (not the shared Redis layer) is lost on rollback. The migration readiness checklist must verify that all 5 P0 services use the shared session backend, not green-local storage.

---

## 8. Post-Migration Validation Checklist

The blue cluster is decommissioned only after all of the following are complete. Blue decommission is irreversible — maintain blue for a minimum of 7 days at 0% traffic before teardown.

**SCS Recomputation on Green**

SLO Coherence Score must be recomputed against green cluster data, not carried over from blue. Blue cluster SLOs were validated against blue cluster infrastructure; green cluster introduces different hardware profiles, different network paths, and potentially different performance characteristics. SCS must be reestablished with a minimum of 72 hours of green-only production data before decommission authorization.

```
SCS checklist:
- [ ] All 12 services have ≥ 72hr of SLO data on green
- [ ] No P0 service has burned more than 10% of monthly error budget during migration
- [ ] SLI baselines for green cluster documented and committed to runbooks
- [ ] Alert thresholds reviewed and adjusted for green cluster p99 baselines
```

**Full Decommission Gate**:

- [ ] All traffic routing to green (Route 53 weights: green=100, blue=0) for ≥ 7 days
- [ ] No P0 incidents on green during 7-day validation window
- [ ] OCR_weighted on green ≥ 0.85 (recomputed with green cluster data)
- [ ] SCS revalidated — all 12 services with ≥ 72hr green baseline
- [ ] All deprecated API manifests confirmed removed from chart repositories
- [ ] Helm chart versions tagged and committed: green cluster deployment state is source of truth
- [ ] Runbooks updated to reference green cluster endpoint URLs
- [ ] PagerDuty escalation policies updated to green cluster alert sources
- [ ] Blue cluster EKS node groups scaled to 0 (cost stop, not deletion) — hold for 7 additional days
- [ ] Blue cluster VPC, IAM roles, and Route 53 health checks deleted after final hold period
- [ ] Post-migration MRI recomputed — document final values as new baseline

---

## 9. Why OCR Must Be Reconfigured on Green — The 48-Hour Blindspot

The observability stack for the blue cluster took months to build correctly. Scrape configs were tuned, alert thresholds were calibrated to production traffic patterns, log parsing rules were validated against real error messages. None of that configuration is automatically present on the green cluster.

If SRE shifts traffic to green without reinstalling and validating the observability stack, the following occurs:

- Prometheus scrape targets reference blue cluster service endpoints — green services are not scraped
- Alerts that fire on green cluster anomalies route to dead endpoints or simply never fire
- Dashboards display blue cluster metrics while green runs unmonitored
- Log forwarding is absent — incidents produce no searchable log trail

The window between first traffic shift and full observability validation on green is the highest-risk period of the entire migration. Infrastructure incidents have the highest probability of occurrence during the first 24-48 hours of a new cluster receiving production load. This is precisely when you need monitoring most — and it is precisely when OCR = 0 if the bootstrap was skipped or rushed.

The 48-hour blindspot is not theoretical. It is the documented failure mode in post-mortems from EKS upgrades across the industry: team shifts traffic, confidence is high because nothing looks wrong, an anomaly develops overnight, and it is discovered manually by a customer complaint at 6am because the alert never fired.

The mitigation is architectural, not procedural: the observability bootstrap (Section 5) is a hard gate in the migration checklist, not a best-effort recommendation. No traffic shifts until OCR_weighted ≥ 0.85 on green cluster, verified by automated validation — not by human assertion.

---

*Scenario 05 of the SRECapstone series. Prerequisites: Scenario 00 (SRE Framework Design). Related: Scenario 03 (Dependency Graph Analysis), Scenario 04 (Error Budget Management).*
