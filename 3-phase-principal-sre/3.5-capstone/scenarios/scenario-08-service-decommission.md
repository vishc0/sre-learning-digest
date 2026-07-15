# Scenario 08 — Service Decommission: ShopCore Legacy Monolith

**System**: Shopping Cart (12 microservices on EKS + ShopCore legacy monolith)
**Event**: Product team declares ShopCore ready for decommission after 2-year strangler fig migration. ShopCore receives 50 rps; declared dependencies account for only 30 rps.
**SRE Role**: Principal SRE governing the decommission readiness gate and execution sequence

---

## 1. Concept — Decommission as the Most Irreversible Change in the SRE Toolkit

A deployment is reversible. A feature flag toggle is reversible. A DNS change is reversible within seconds. A service decommission is not reversible in any operational sense of the word.

When you decommission a service, the following sequence occurs. DNS records are removed — callers begin receiving NXDOMAIN or connection refused before they know the service is gone. Container images may be cleaned from the registry. The Kubernetes Deployment and Service manifests are deleted from the cluster. Databases may be dropped or archived to cold storage. IAM roles are revoked — any workload that used those roles for signing or cross-account access stops functioning. Secrets are rotated and the old versions destroyed.

Rolling any of that back is not a `kubectl rollout undo`. It is a recovery operation: re-image the container from the last-known-good tag (assuming it was not garbage-collected), re-apply manifests, re-register DNS, re-warm caches, re-hydrate any state that was not preserved. That sequence takes hours, not seconds. It requires a war room, not a single engineer at a keyboard.

The strangler fig pattern — migrating functionality incrementally to new microservices until the monolith has nothing left to do — is the correct architectural approach. ShopCore's two-year migration is complete. But declaring the migration complete is an engineering statement. Declaring ShopCore safe to remove is an SRE statement, and these are different things. Engineering correctness means the new services implement the right behavior. SRE readiness means no live caller is depending on the thing you are about to remove.

The 20 rps gap between observed traffic and declared dependencies is the entire problem. That gap is the signal that the engineering statement and the SRE statement have not converged yet.

---

## 2. SCI Calculation and What It Means for the Decommission

The **Shadow Coupling Index (SCI)** measures the fraction of inbound traffic to a service that has no documented upstream owner.

```
SCI = (observed_inbound_rps − declared_dep_rps) / total_observed_inbound_rps
```

For ShopCore:

```
SCI = (50 − 30) / 50
SCI = 20 / 50
SCI = 0.40
```

An SCI of 0.40 means 40% of ShopCore's inbound traffic originates from callers that no team has declared ownership of. These are shadow callers — services, scripts, batch jobs, internal tooling, monitoring probes, or legacy integrations that were never documented in the dependency registry and were not included in the migration plan.

The decommission is blocked. This is not a judgment call — it is a policy. An SCI above 0.0 means the blast radius of removing ShopCore is unknown. A known blast radius can be engineered around. An unknown blast radius cannot. If ShopCore is removed while SCI = 0.40, the 20 rps of shadow traffic will generate errors in systems that may have no circuit breaker, no fallback, and no on-call engineer aware that the dependency is gone.

SCI must equal 0.0, sustained for 72 consecutive hours, before a decommission Change Request can be opened. Any other policy is operational negligence.

---

## 3. Shadow Caller Investigation — Step-by-Step Methodology

Identifying the source of the 20 rps gap requires a systematic investigation across four data planes. Run all four in parallel — they each see different layers of the network stack and a caller may appear in one but not another.

**Step 1 — Distributed Tracing: Jaeger Span Source Analysis.**
Pull all spans in which ShopCore appears as a server-side span for any 24-hour window. For each span, extract the `peer.service` tag or the calling service identifier from the trace context. Group by caller. The declared 30 rps will appear here — every undiscovered caller should also appear as a service that is making spans without any corresponding entry in the dependency registry. Discrepancies between the trace source list and the declared dependency list are your shadow callers.

**Step 2 — Service Mesh: Istio Source Workload Report.**
If ShopCore is inside the Istio mesh, run: `istioctl proxy-config listeners <shopcore-pod> --port 8080` and correlate with Kiali's inbound traffic graph. Istio captures the source workload principal (SPIFFE ID) for every mTLS connection. This gives you the Kubernetes ServiceAccount identity of every caller — even if that caller has no tracing configured. Istio sees the network layer; Jaeger sees only the instrumented layer.

**Step 3 — API Gateway Access Logs.**
If ShopCore is accessed through an API Gateway (AWS ALB, Kong, NGINX), its access logs contain the originating IP or service identity for every request. Query the logs for the past 30 days grouped by `X-Forwarded-For`, `User-Agent`, or any custom header that identifies the calling service. Batch jobs and cron-triggered integrations often do not pass trace context but do pass identifiable User-Agent strings.

**Step 4 — AWS VPC Flow Logs.**
VPC flow logs capture every TCP connection at the network level, with source IP and destination IP. For the 20 rps of unknown traffic, the source IP will still appear in VPC flow logs even if no application-layer identifier is present. Map source IPs to EKS node pools, EC2 instances, or Lambda functions. This catches callers that bypass the service mesh (sidecar not injected, direct VPC routing, cross-account caller using a VPC peering path).

**Step 5 — Correlation and Ownership Resolution.**
Aggregate findings from all four sources. For each identified caller IP or service identity, resolve the owning team via the CMDB or service registry. Contact the team directly — "your service is calling ShopCore at X rps. This is undocumented. What is the call doing, and is this dependency handled by the migration?" Every shadow caller must either be migrated off ShopCore (preferred) or formally declared as a documented dependency (if migration is still in progress). Only then does that caller exit the shadow coupling count.

Repeat SCI measurement hourly. When the last shadow caller has migrated off and SCI has held at 0.0 for 72 consecutive hours, the decommission gate opens.

---

## 4. Dependency Gravity and the True MRI of Decommission

**Dependency Gravity (DG)** is the total set of services that depend on ShopCore. With SCI = 0.40, ShopCore's declared DG is the 30 rps of known callers. But ShopCore's true DG includes the shadow callers, and until the investigation is complete, true DG is partially unknown.

This distinction matters for the **Migration Risk Index (MRI)**. MRI quantifies the risk of a migration or decommission based on the size and maturity of the dependency surface being removed.

```
MRI = (true_DG_service_count × avg_caller_criticality_weight) / (known_migration_coverage_pct × decommission_validation_window_hours)
```

With SCI = 0.40 and only 30 rps of the 50 rps declared, `known_migration_coverage_pct` is 0.60 — you have confirmed migration coverage for only 60% of ShopCore's actual traffic. Even if all 30 rps of declared callers are fully migrated, the MRI denominator is constrained by the 0.60 coverage fraction, which inflates MRI proportionally.

As the shadow caller investigation resolves each caller — either migrating them off or declaring them — coverage climbs toward 1.0. The MRI drops. When coverage reaches 1.0 (all callers identified and migrated), the decommission is quantifiably lower risk than it was at the investigation start. MRI is the mechanism that translates "we found the shadow callers" into a number that a Change Advisory Board can evaluate.

---

## 5. The Decommission Readiness Gate

The readiness gate is a formal, measurable criterion. It is not a meeting or a vote.

**Gate criterion**: `SCI = 0.00` for 72 or more consecutive hours, measured by the SCI pipeline running at one-hour intervals.

The measurement methodology is as follows. Every hour, the observability pipeline queries ShopCore's inbound request rate from the service mesh telemetry (Prometheus, Istio metrics) and compares it against the declared dependency list, which is stored in the service registry and updated in real time as shadow callers are resolved. SCI is recomputed and logged. A single non-zero reading at any hour resets the 72-hour counter to zero.

Why 72 hours? Batch jobs, nightly ETL processes, weekly report generators, and monthly billing reconciliation jobs all have different call cadences. A batch job that runs once per day may not appear in a 1-hour or 4-hour observation window. 72 hours is sufficient to catch all daily-cadence callers. Weekly-cadence callers require a longer window — if the investigation reveals weekly batch callers, the gate extends to 168 hours (7 days) for those specific callers until they are confirmed migrated.

The 72-hour clean window also provides a forcing function for the shadow caller investigation team. When each shadow caller is migrated off, the window restarts. This creates a direct feedback loop: teams that drag their feet on migrating off ShopCore block the decommission gate for everyone.

---

## 6. Rollback Velocity — What RV Means for Decommission

**Rollback Velocity (RV)** is the speed at which the SRE team can reverse a change and restore the prior state. For a deployment, RV is measured in seconds — `kubectl rollout undo` restores the previous ReplicaSet. For a decommission, RV is measured in hours.

The decommission rollback sequence:

1. Re-identify the last-known-good container image tag for ShopCore (must be pinned and preserved in the registry — do not allow garbage collection until 30 days post-decommission)
2. Re-apply Kubernetes manifests (Deployment, Service, ConfigMap, ServiceAccount, NetworkPolicy)
3. Re-register DNS entries (Route 53 records, Istio VirtualService, API Gateway routing rules)
4. Re-issue IAM role bindings and Vault policies
5. Re-warm the ShopCore application cache (Redis or in-memory) to avoid a cold-start latency spike
6. Validate that inbound traffic is flowing correctly and SCI is returning to its pre-decommission pattern

This sequence, executed by a competent SRE team under incident conditions, takes 2 to 4 hours. During those 2 to 4 hours, every shadow caller that was missed during the investigation is generating errors in production.

The maintenance window for a decommission hard-removal must be sized accordingly. A 30-minute maintenance window is sufficient for a deployment. A decommission hard-removal requires a minimum 4-hour window, with a rollback decision gate at the 30-minute mark and a go/no-go decision gate before the database archival step — which is the point of no return.

---

## 7. Staged Decommission — The Correct Sequence

Instant removal is not an acceptable decommission strategy for a service that was receiving 50 rps. The correct approach is a three-phase staged decommission.

**Phase 1 — Traffic Drain (0% → Dark Mode → Offline).**
Before the decommission CR is opened, the remaining declared callers (30 rps) are migrated to the appropriate microservices. Traffic is drained gradually: 100% → 75% → 50% → 25% → 5% → 0%, with 72 hours of observation at each step below 25% to confirm no latency or error regression in the downstream microservices. When inbound rps reaches 0, ShopCore enters dark mode: it is still running, still accessible, but receiving no declared traffic. SCI is measured continuously.

**Phase 2 — Soft Removal (30-Day 410 Window).**
ShopCore's application code is modified to respond `HTTP 410 Gone` to all inbound requests. The service remains running and reachable on the network. Its DNS entries remain active. This is not a cost-saving measure — it is a shadow caller trap. Any caller that was missed during the investigation phase will now receive a structured, logged 410 response rather than a connection refused error. The 410 response body includes: `{"error": "shopcore_decommissioned", "migration_docs": "<url>", "contact": "<sre-team>"}`.

The 30-day 410 window is the safety net. Shadow callers that run on monthly billing cycles, quarterly report jobs, or ad hoc manual processes that were not running during the 72-hour SCI gate will surface here. Every 410 hit is logged with the caller's source identity. The SRE team reviews the 410 log weekly. Any new caller discovered during this window is routed to the appropriate microservice — the fix is made in the caller, not in ShopCore.

**Phase 3 — Hard Removal.**
After 30 days of zero new 410 callers (or all discovered callers have been migrated), the hard removal proceeds: manifests deleted, DNS deregistered, IAM roles revoked, databases archived, container image tagged as `archived-<date>` and retained for 90 days in cold storage before final deletion. This is the irreversible step. The Change Request for Phase 3 requires Principal SRE sign-off and is not a self-service operation.

---

## 8. CSD, DSA Cleanup, and the FLI Effect After Decommission

**Change Surface Delta (CSD)** measures how much of the system's operational surface area is altered by a change. Decommissioning ShopCore is a large negative CSD — it removes a substantial portion of the operational surface. This is one of the few cases in SRE where a large CSD is desirable.

**Dependency Surface Area (DSA)** quantifies all the dependencies ShopCore itself owned: its database connections, its Redis cluster, its downstream API calls to payment processors and inventory services (before migration), its Vault paths, its IAM roles, its CloudWatch log groups, its Prometheus scrape targets. After hard removal, every one of these connections no longer requires monitoring, alerting, or incident response. The SRE team's operational burden decreases.

**Failure Locality Index (FLI)** measures how contained failures are within the system. A high FLI means failures stay local to the originating service. A low FLI means failures propagate across service boundaries — cascades.

Before decommission, ShopCore's FLI contribution is low. A failure in ShopCore cascades to its shadow callers (who have no circuit breakers on an undocumented dependency), which cascade to their own callers, producing a distributed cascade from a single monolith failure. ShopCore's position in the dependency graph — as an undocumented hub — is an inherent FLI liability.

After successful decommission (all shadow callers migrated to services that have circuit breakers, retry policies, and fallback behavior), the system's FLI improves. The 12 microservices each have bounded, documented failure modes. There is no longer a monolith at the center of undiscovered call chains. Compute the FLI delta as:

```
FLI_delta = (cascade_paths_removed) / (total_failure_propagation_paths_before_decommission)
```

With 20 rps of shadow callers (say, from 4 undiscovered services, each with their own downstream callers), removing ShopCore from the graph eliminates those 4 undocumented cascade paths. If the system had 20 total failure propagation paths before decommission, and 4 of them ran through ShopCore's shadow caller relationships:

```
FLI_delta = 4 / 20 = 0.20
```

The system's effective FLI improves by 20% — failures that previously could propagate through ShopCore's shadow coupling now have nowhere to propagate because the hub is gone and its former callers are using microservices with proper resilience patterns.

---

## 9. Post-Decommission Observability — 30-Day Watch Window

After Phase 2 (soft removal) activates, the SRE team operates a 30-day post-decommission observability protocol. This is not optional. Missing a shadow caller during this window is the difference between a managed incident (caller gets a 410, SRE gets alerted, caller is migrated in days) and an unmanaged incident (caller gets connection refused at 3 AM, team has no runbook, ShopCore rollback is initiated).

**Signal 1 — 410 Error Log Review (weekly).**
The ShopCore 410 response handler logs every inbound request with: timestamp, source IP, source service identity (from mTLS SPIFFE ID or X-Forwarded-For), request path, and request volume. The SRE team reviews this log every Monday morning during the 30-day window. Any new caller that appears after Phase 2 activation is treated as a P2 incident: the caller is identified, the owning team is contacted, and the caller is migrated within 5 business days.

**Signal 2 — Error Rate Spike in Downstream Microservices.**
If a shadow caller was missed and is now receiving 410s instead of valid responses, it may respond by retrying aggressively, timing out, or failing in a way that produces errors in its own error rate. A sudden unexplained error rate spike in any of the 12 microservices during the 30-day window is a signal that a shadow caller has been disrupted. The investigation starts by cross-referencing the spike timestamp with the ShopCore 410 log.

**Signal 3 — Support Ticket Volume for Specific Flows.**
Business flows that relied on ShopCore but whose callers were missed — order history, account summary, legacy checkout — will generate customer-facing errors. Support ticket volume for these specific flows is an SRE signal. A spike in support tickets for "order history not loading" or "checkout error" during the 30-day window triggers an immediate investigation of whether a ShopCore shadow caller is responsible.

**Signal 4 — BRI (Blast Radius Index) Monitoring.**
During the 30-day window, the SRE team maintains a live BRI estimate: if a shadow caller is discovered at any point in the window, how many customers are affected by its failure? BRI is computed as the caller's downstream customer journey coverage × the error rate the caller is now experiencing. A high-BRI discovery (a caller serving >10% of checkout traffic that nobody knew about) escalates immediately to a P1 and triggers the ShopCore rollback procedure.

At the end of the 30-day window with zero new callers discovered and no error rate anomalies, Phase 3 hard removal proceeds. The decommission is complete.

---

## Summary — Decommission Decision Gate Checklist

| Gate | Criterion | Method |
|------|-----------|--------|
| SCI = 0.00 | 72+ consecutive hours of zero shadow traffic | Hourly SCI pipeline |
| MRI acceptable | All callers declared; migration coverage = 100% | Service registry + trace audit |
| RV understood | Team confirms 2–4 hr rollback window; maintenance window sized ≥ 4 hrs | CR planning |
| Phase 2 active | 410 response deployed; logging confirmed | Smoke test from each declared caller |
| 30-day watch complete | Zero new callers; zero unexplained error rate spikes | Post-decommission observability protocol |
| Phase 3 approved | Principal SRE sign-off; database archival approved by data governance | Change Advisory Board |

No step in this sequence is optional. The most dangerous decommission is the one that skips Phase 2 because "we're confident we got all the callers." Confidence is not the same as evidence. The 410 window converts confidence into evidence.

---

*Document version: 1.0 | Scenario class: Service Decommission | System: Shopping Cart EKS + ShopCore Monolith | Author: SRECapstone Program*
