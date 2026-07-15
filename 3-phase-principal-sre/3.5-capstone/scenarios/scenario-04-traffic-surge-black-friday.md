# Scenario 04 — Traffic Surge: Black Friday

**Domain**: Capacity Engineering, Autoscaling, Surge Operations  
**System**: Shopping Cart Platform — 12 microservices  
**Key Services**: Checkout (CD=5, SLA 99.95%), Add-to-Cart (CD=3, SLA 99.9%), Browse (CD=2, SLA 99.5%)  
**Normal Peak**: Checkout 500 rps, Browse 2000 rps  
**Black Friday Target**: 8× normal — Checkout 4000 rps, Browse 16000 rps  
**Ramp Profile**: 0 → peak in 45 minutes starting at 06:00

---

## 1. Concept: Why Traffic Surges Are Categorically Different

Normal operational risk is stochastic — failures arrive without warning and SRE responds. Traffic surges are deterministic — the demand curve is known in advance, and failure to prepare is an engineering decision, not bad luck.

Autoscaling alone is insufficient for known surge events for three structural reasons. First, every autoscaling system has a *detection lag*: the HPA must observe elevated CPU, compute a scale recommendation, and trigger a node group expansion before a single new pod becomes ready. In this platform, that lag is 5 minutes total (2 min HPA detection + 2 min Karpenter node provisioning + 1 min pod startup). During a steep ramp, 5 minutes represents a substantial capacity deficit. Second, autoscaling is reactive: it responds to the traffic that has already arrived, not the traffic that is 60 seconds away. Third, autoscaling metrics — CPU, memory — are lagging indicators of saturation. By the time CPU signals the scaler, pods may already be dropping requests.

The three canonical failure modes during a surge are:

**Saturation before scale-out**: Traffic climbs faster than autoscaling can add capacity, creating a window where active pods are overloaded. Request latency spikes, then error rates climb, then SLA is breached — all before the new pods become ready.

**Cascade at saturation**: When one service saturates, it holds connections open, exhausting upstream thread pools and connection pools. The saturated service becomes a blocking dependency that drags down nominally healthy services. The shopping cart platform is particularly exposed here because Checkout (CD=5) has the most downstream hops and the tightest SLA.

**Alerting failure at 8× traffic**: Standard alerting thresholds calibrated at normal traffic generate noise during a surge. An alert that fires when error rate exceeds 0.1% is meaningful at 500 rps (0.5 errors/sec). At 4000 rps it generates constant paging even if the system is healthy. SREs silence these alerts and lose signal precisely when signal matters most.

---

## 2. SLTD Calculation — Checkout Service

**Formula**: `SLTD = (ramp_rate_rps/min × autoscaling_lag_min) / pod_capacity_rps`

**Inputs**:
- Ramp rate: 4000 rps over 45 minutes = **88.9 rps/min**
- Autoscaling lag: **5 minutes**
- Pod capacity: **200 rps per Checkout pod**

**Calculation**:

```
SLTD = (88.9 rps/min × 5 min) / 200 rps
     = 444.5 / 200
     = 2.22 pods
```

SLTD = 2.22 means that at any point during the ramp, autoscaling is structurally 2.22 Checkout pods *behind* where demand requires. Rounding up, **3 pods must be pre-provisioned above the autoscaling baseline** before the ramp begins. This is not a performance margin — it is the mathematical minimum to prevent saturation during the lag window.

If pre-provisioning is skipped, the platform will enter the ramp with a 444 rps capacity deficit that autoscaling physically cannot close until 5 minutes after the deficit appears. At a pod capacity of 200 rps, that deficit means existing pods must absorb 122% of rated load — sustained overload, not a spike.

---

## 3. CBI Before and After Pre-Scaling

**Formula**: `CBI = provisioned_capacity / observed_peak_demand`

**Without pre-scaling at normal provisioning**: At normal peak, Checkout runs at 500 rps. Assume 3 pods provisioned (600 rps capacity), giving CBI = 600/500 = 1.2 — a healthy 20% headroom for normal operations.

On Black Friday without intervention: peak demand is 4000 rps. With 3 pods, provisioned capacity is 600 rps. **CBI = 600/4000 = 0.15**. A CBI below 1.0 means the system is definitionally under-provisioned; 0.15 means the system has capacity for 15% of expected peak demand. This is not a degraded state — it is complete failure.

**CBI checkpoints for Black Friday**:

| Checkpoint | Target CBI | Required Checkout Pods | Rationale |
|---|---|---|---|
| 72h before | 1.0 | 20 pods (4000 rps / 200 rps) | Confirm full-peak capacity is achievable |
| 24h before | 1.3 | 26 pods | 30% headroom for demand estimation error |
| 6h before | 1.5 | 30 pods | Pre-warm all pods; absorb SLTD gap |
| 1h before | 1.5+ maintained | 30+ pods | Freeze autoscaling min-replicas; no scale-down allowed |

A CBI of 1.5 at event start means the system can absorb 50% more traffic than forecasted peak before saturation. Given that Black Friday traffic forecasts historically deviate ±20-30%, a CBI of 1.5 is the minimum defensible target, not a conservative one.

---

## 4. LBH Under Load — Latency SLO Verification

**Formula**: `LBH = (p99_SLO_ms − infrastructure_overhead_ms) / CD`

Assume Checkout's p99 SLO is 800ms with 50ms infrastructure overhead (load balancer, service mesh, DNS). At normal load: `LBH = (800 - 50) / 5 = 150ms per hop`. Each of Checkout's 5 hops has a 150ms budget.

At 8× traffic with pods above 80% CPU, empirical behavior in most runtimes (JVM, Python WSGI) produces p99 latency that grows non-linearly — often doubling when CPU crosses 80% and doubling again above 90%. If average pod CPU reaches 85% at peak: effective p99 per hop rises to approximately 250-300ms. Aggregate p99 = 5 × 275ms = 1375ms. The 800ms SLO is breached by 72%.

LBH is useful not just as a static calculation but as a *triage signal*: the service whose LBH is smallest relative to observed per-hop latency is the service that will breach the SLO first. During the ramp, if Auth (CD contribution = 1 hop, 150ms budget) reports p99 of 140ms at 4× load, Auth is the leading indicator of cascade risk, not Checkout itself.

---

## 5. The Pre-Scale Plan

**72 hours before**: Run a load test at 100% of projected peak. Validate that all services reach CBI ≥ 1.0 under test load. Identify any service that cannot reach target pod count due to node group limits or resource quotas. Fix provisioning blockers — do not defer to event day.

**24 hours before**: Set HPA `minReplicas` to 80% of CBI 1.3 target counts across all services. Freeze all non-critical deployments. Enable surge-mode alert profiles (see Section 6). Confirm Karpenter node pools have sufficient pre-warmed capacity. Target CBI ≥ 1.3.

**6 hours before**: Raise `minReplicas` to full CBI 1.5 target counts. Verify pod readiness probes are passing for all pre-provisioned pods. Brief on-call rotation — primary and secondary confirmed. Activate war room channel. Disable scale-down policies for the event window. Target CBI ≥ 1.5.

**1 hour before**: Final CBI audit across all 12 services. Confirm circuit breakers are armed on Auth and Inventory. Verify EBV baseline is logged for comparison during the event. No changes to running services after this checkpoint. Declare the system event-ready.

---

## 6. Alert Reconfiguration for Surge Events

Standard alerting thresholds are calibrated for steady-state traffic. At 8× volume, absolute-count-based thresholds fail in two ways: they generate noise (benign proportional errors trigger pages) or they are silenced wholesale (on-call disables the alert, losing real signal).

**APR (Alert Precision Rate) degradation at 8×**: If an alert fires correctly 90% of the time at 500 rps, the same threshold at 4000 rps will fire on proportional errors — errors that exist because traffic exists, not because reliability degraded. APR collapses toward noise.

The correct approach is to switch to *rate-normalized* thresholds during the surge window and restore them afterward. Instead of alerting on "error count > 10/min," alert on "error rate > 0.05%." This is a temporary threshold, time-boxed to the event window, documented in the runbook, and reverted automatically via a scheduled config change.

**EBV handles this structurally**: EBV = (current_error_rate) / (baseline_error_rate × traffic_multiplier). An absolute alert would fire during a clean 8× surge; EBV would read approximately 1.0 and stay silent. EBV will alert only when errors grow faster than traffic — the only condition that actually signals a reliability problem.

---

## 7. EBV During Surge — Signal vs. Noise

**Scenario A — Proportional errors (not alarming)**:  
Error rate triples, traffic triples. EBV = (3× errors) / (3× traffic) = **1.0**. The system is degrading proportionally with load. Latency may be rising, but error behavior is not worsening. Monitor LBH; do not page.

**Scenario B — Super-proportional errors (alarming)**:  
Error rate quadruples, traffic has only tripled. EBV = 4/3 = **1.33**. Errors are growing 33% faster than traffic. This is a saturation signal — a service is not scaling with demand. EBV > 1.1 should trigger investigation; EBV > 1.25 should trigger an incident. The EBV threshold for paging during a surge event is explicitly higher than normal (1.25 vs. 1.05) because minor super-proportionality is expected during rapid ramp, but the signal is structurally cleaner than any absolute threshold.

---

## 8. Cascade Risk at Saturation

**CC (Cascade Coefficient)** measures how many downstream services are exposed when a given service saturates.

Auth is called by every service in the checkout flow (authentication on every request). If Auth saturates, Checkout, Add-to-Cart, and 6 of the 12 services experience held connections waiting on Auth responses. CC(Auth) ≈ 0.75 (9 of 12 services impacted). Inventory is called only by Checkout and Add-to-Cart; CC(Inventory) ≈ 0.17.

Auth is the higher-priority circuit breaker target. Before the event, the Auth circuit breaker must be configured to: open after 5 consecutive 500ms timeouts (not 5xx errors alone — slow Auth is as dangerous as failed Auth), return a cached token for read-only operations during open-circuit state, and alert when the circuit opens (not when individual requests fail).

Inventory's circuit breaker should degrade gracefully: if Inventory is unreachable, Add-to-Cart continues with an optimistic "in stock" response and reconciles post-order. This is a pre-agreed degraded mode, not an error condition.

**BRI (Blast Radius Index)** at Auth saturation: with CC(Auth) = 0.75, a full Auth outage affects 9 services. If those 9 services collectively represent 85% of user-facing revenue operations, BRI is HIGH. Auth must be treated as a Tier-0 dependency requiring dedicated pre-scaling, independent of its own traffic volume.

---

## 9. Toil During Black Friday

**TAF (Toil Amplification Factor)** = toil actions during event / toil actions during normal peak.

At normal peak: on-call handles 3-5 manual scaling actions per shift. On Black Friday without preparation: manual pod restarts, manual HPA overrides, manual threshold silencing, manual war-room updates — estimated 30-40 actions per shift. **TAF ≈ 8-10×**, matching the traffic multiplier. This is the signal that preparation was insufficient: when TAF tracks traffic, automation has not kept pace with scale.

Manual actions that must be automated before the event:
- Pre-scaling HPA `minReplicas` to event-day targets (scripted, executed at T-6h)
- Alert threshold switching (scheduled ConfigMap update at T-1h, reverts at T+6h)
- Circuit breaker arming (Helm values updated pre-event, not manually during)
- War-room status updates (automated Slack bot posting CBI and EBV every 15 minutes)

After automation, target TAF ≤ 2 during the event window. Residual manual actions should be judgment calls only — not mechanical repetition.

---

## 10. Post-Surge Review — 48-Hour Checklist

The post-surge review has one purpose: confirm the framework held, and identify where it did not. Measurements drive the next year's preparation.

**Capacity**:
- [ ] Record actual peak rps per service vs. forecast. Was the 8× estimate accurate?
- [ ] Record minimum observed CBI per service during the ramp. Did any service drop below 1.0?
- [ ] Record SLTD actual vs. calculated. Did the 3-pod pre-provision absorb the lag gap?

**Reliability**:
- [ ] Pull EBV timeseries for the full event window. Identify any EBV spikes > 1.1 and correlate with specific services and timestamps.
- [ ] Review error budget consumption during the event for all three SLA tiers (99.95%, 99.9%, 99.5%).
- [ ] Confirm no SLA was breached. If any was: document the breach window, calculate error budget impact, and file a P1 remediation item.

**Alerting**:
- [ ] Review APR during the event window. How many pages fired? How many were actionable?
- [ ] Confirm surge-mode thresholds reverted automatically at T+6h.
- [ ] Identify any alert that should have fired but did not (false negative review is as important as false positive review).

**Cascade and Toil**:
- [ ] Record TAF for the event window. If TAF > 2, identify each manual action and assign an automation ticket.
- [ ] Review circuit breaker open/close events. Did any circuit open unexpectedly? Did any fail to open when it should have?
- [ ] Update the pre-scale plan with actual pod counts required. Adjust the next-event CBI targets accordingly.

The goal of the post-surge review is not to declare victory or assign blame. It is to narrow the delta between the model and observed behavior so that next year's SLTD calculation starts from better inputs.

---

*Scenario 04 of the SRECapstone Framework — Traffic Surge Operations*
