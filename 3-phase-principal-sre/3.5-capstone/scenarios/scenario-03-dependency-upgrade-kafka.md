# Scenario 03 — Dependency Upgrade: Kafka 2.8 to 3.5

**System**: Shopping Cart — 12 microservices  
**Change**: Apache Kafka (MSK) upgrade from 2.8 to 3.5  
**Affected services**: 6 (Order Management P0, Inventory Service P1, Notification Service P2, Analytics Pipeline, plus two internal consumer groups on shared topics)  
**Scenario class**: Infrastructure dependency upgrade — messaging backbone  
**Primary risk dimension**: Protocol coexistence, consumer group rebalance instability, irreversible log format migration

---

## 1. Why Kafka Upgrades Are Uniquely Risky

Most dependency upgrades — a library version bump, a database minor release — are reversible if something breaks. Kafka upgrades are not. They are infrastructure-layer changes to a stateful, distributed messaging substrate that sits beneath every asynchronous interaction in the system. Understanding why requires understanding what Kafka actually is to your services.

Kafka is not a queue you can swap. It is a distributed commit log. Every consumer group tracks an **offset** — a position in that log. The format of the log itself can change between major versions. In Kafka 3.x, the default log format version advances, and once a broker has written records in the new format, those records cannot be read by a 2.8 broker. This is the root cause of the irreversibility problem: **log format migration is a one-way door**.

### The Four Specific Risk Dimensions for 2.8 → 3.5

**1. ZooKeeper removal (KRaft mode).** Kafka 2.8 used Apache ZooKeeper for cluster metadata management — leader election, partition assignments, broker registrations. Kafka 3.5 supports KRaft (Kafka Raft Metadata) as the default, running the metadata quorum inside Kafka brokers themselves. This removes an entire distributed system dependency, but it also means your operational runbooks, monitoring, and alerting for the ZooKeeper ensemble are no longer valid. Every alert watching ZooKeeper node count, leader election time, and session expiry must be retired and replaced with KRaft quorum health equivalents.

**2. Consumer rebalance protocol change (incremental cooperative rebalancing).** In Kafka 2.8, the default consumer group protocol was **eager rebalancing**: when any consumer joins or leaves the group, all consumers stop consuming, revoke all their partition assignments, and renegotiate from scratch. In Kafka 3.5, **incremental cooperative rebalancing** is the default. Consumers incrementally transfer partition assignments, allowing unaffected partitions to continue being consumed during the transition. The risk during an upgrade is **mixed-protocol consumer groups** — a consumer group where some consumers are on 2.8 (eager) and some are on 3.5 (incremental cooperative) will fall back to the eager protocol, causing full consumption stalls across all partitions on every rebalance. The Service Compatibility Window (SCW) must be sized to ensure no mixed-protocol group exists in steady-state.

**3. Producer default changes (acks=all).** In Kafka 2.8, the default producer acknowledgment setting was `acks=1` — the leader broker acknowledges the write, but in-sync replicas (ISRs) are not required to confirm. In Kafka 3.5, the default is `acks=all` (equivalent to `acks=-1`). Any producer that relied on the default and did not explicitly configure `acks` will now wait for all ISRs to acknowledge before the produce call returns. This is safer but increases produce latency. Order Management Service (P0), as the primary producer of order events, must be audited for explicit `acks` configuration before the upgrade. An implicit reliance on the 2.8 default that silently becomes `acks=all` can cause latency regressions in the checkout path.

**4. Offset management and consumer group coordinator migration.** When a Kafka cluster is replaced rather than upgraded in-place (the recommended strategy for MSK), consumer group offsets stored in the `__consumer_offsets` internal topic on the old cluster are not automatically present on the new cluster. Each consumer group must either have its offsets exported and imported, or must accept a restart from the earliest or latest offset on the new cluster. An incorrect offset migration causes either message replay (duplicate processing) or message loss, depending on the direction of the error.

### What "Dependency Upgrade" Means in the SRE Context

An application code change affects one service. A dependency upgrade affects every service that shares that dependency. The SRE distinction is the **blast radius asymmetry**: a bad code deploy to Notification Service (P2) harms only notification delivery. A bad Kafka upgrade harms Order Management (P0), Inventory (P1), Notification (P2), and Analytics simultaneously. This is why the frameworks in this capstone — MRI, FLI, DG, CSD — weight infrastructure-layer changes far more heavily than application-layer changes. The change surface is not just wider; the failure mode is correlated across all dependent services rather than isolated.

---

## 2. Protocol Coexistence Cost (PCC) Calculation

Running two Kafka clusters in parallel — the existing 2.8 cluster and the new 3.5 cluster — generates **Protocol Coexistence Cost (PCC)**: operational overhead from duplicate monitoring, duplicate alert routing, split consumer group management, and engineer hours spent validating both clusters daily.

**Formula:**

```
PCC = (dual_version_ops_hours/day × cost_rate) × coexistence_days
```

**Inputs from the scenario:**
- Dual-version monitoring requires 3 engineer-hours per day (alert review, lag validation on both clusters, replication offset checks)
- Blended senior SRE cost rate: $150/hour (fully loaded)
- Required coexistence period: 4 weeks (28 days) for a safe incremental migration
- Forced hard cutover engineering cost: 40 hours at the same rate

**PCC over the full coexistence period:**

```
PCC = (3 hours/day × $150/hour) × 28 days
PCC = $450/day × 28 days
PCC = $12,600
```

**Hard cutover cost:**

```
Hard cutover cost = 40 hours × $150/hour = $6,000
```

**Decision threshold:** Hard cutover becomes cheaper than incremental migration when:

```
(3 × $150) × coexistence_days = $6,000
$450 × coexistence_days = $6,000
coexistence_days = 13.3 days
```

After approximately 13 days of dual-version operation, the forced hard cutover is cheaper in pure engineering labor. However, PCC is an economic model, not a safety model. Hard cutover of Kafka — cutting all consumers over simultaneously rather than topic by topic — dramatically increases MRI and eliminates the ability to abort and roll back individual consumer groups. The PCC calculation justifies the question; risk framework answers it. For this upgrade, the 28-day incremental plan is retained because MRI is high enough to demand the slower, safer path. Paying the additional $6,600 in operational overhead is the correct decision given the P0 blast radius.

---

## 3. Change Surface Delta (CSD) for the Kafka Upgrade

CSD quantifies the total change footprint across all affected services. A messaging protocol upgrade has a distinct `change_depth_coefficient` from an application library bump. The coefficient reflects how deeply the change penetrates service internals.

**Formula:**

```
CSD = Σ[tier_weight × change_depth_coefficient]
```

**Tier weights for the shopping cart:**
- P0 (Order Management): tier_weight = 3.0
- P1 (Inventory Service): tier_weight = 2.0
- P2 (Notification Service): tier_weight = 1.5
- Analytics Pipeline (no SLO, batch): tier_weight = 0.5
- Internal consumer group A (shared topic reader, P1-adjacent): tier_weight = 2.0
- Internal consumer group B (audit log consumer, P2-adjacent): tier_weight = 1.5

**Change depth coefficients for a Kafka protocol upgrade:**

A Kafka upgrade requires changes at three depths: client library version bump (shallow, coefficient 1.0), producer/consumer configuration review and potential override (medium, adds 0.5 per service), and consumer group offset migration with validation (deep, adds 1.0 per consumer). Services that are both producers and consumers carry the full additive coefficient.

| Service | Role | Library Bump | Config Review | Offset Migration | Total Coefficient | Tier Weight | CSD Contribution |
|---------|------|-------------|--------------|-----------------|-------------------|-------------|-----------------|
| Order Management (P0) | Producer + Consumer | 1.0 | +0.5 | +1.0 | 2.5 | 3.0 | 7.5 |
| Inventory Service (P1) | Producer | 1.0 | +0.5 | — | 1.5 | 2.0 | 3.0 |
| Notification Service (P2) | Consumer | 1.0 | +0.5 | +1.0 | 2.5 | 1.5 | 3.75 |
| Analytics Pipeline | Consumer | 1.0 | — | +1.0 | 2.0 | 0.5 | 1.0 |
| Consumer Group A | Consumer | 1.0 | +0.5 | +1.0 | 2.5 | 2.0 | 5.0 |
| Consumer Group B | Consumer | 1.0 | +0.5 | +1.0 | 2.5 | 1.5 | 3.75 |

```
CSD = 7.5 + 3.0 + 3.75 + 1.0 + 5.0 + 3.75 = 24.0
```

A CSD of 24.0 is high. For context, a typical single-service library upgrade with no protocol implications produces a CSD of 1.5 to 3.0. The Kafka upgrade CSD of 24.0 reflects the infrastructure-wide penetration of the change. Any CSD above 15.0 triggers a mandatory Principal SRE review and a two-week minimum migration runway per the shopping cart SRE operating model.

---

## 4. Migration Risk Index (MRI) Calculation

**Formula:**

```
MRI = DG × CD × (1 - FLI) × (2 - OCR_weighted)
```

**Dependency Gravity (DG):** Kafka is not one service — it is infrastructure shared by 6 services. DG for infrastructure-layer components is computed as the sum of the DG values of all dependent services. Using the established DG values for the shopping cart: Order Management DG = 8, Inventory DG = 5, Notification DG = 3, Analytics DG = 1, Consumer Group A DG = 4, Consumer Group B DG = 2. Infrastructure-level Kafka DG = 8 + 5 + 3 + 1 + 4 + 2 = **23**.

**Call Depth (CD):** The upgrade requires coordinated changes across all 6 services simultaneously in the migration window. Effective CD for coordination = **6** (one "hop" per coordinated service change).

**Failure Locality Index (FLI):** FLI measures how contained a failure is. If Kafka fails during upgrade, all 6 dependent services are immediately affected. There is no locality — the failure is fully correlated. FLI = **0.05** (near-zero; a Kafka outage during migration has near-total blast radius).

**OCR_weighted (On-Call Readiness):** The migration requires a dedicated incident commander, a Kafka specialist, and service owners for all 6 affected services on standby. With that full team present: OCR_weighted = **1.8** (high readiness — full coverage, pre-briefed runbooks, comms bridge open).

```
MRI = 23 × 6 × (1 - 0.05) × (2 - 1.8)
MRI = 23 × 6 × 0.95 × 0.2
MRI = 23 × 6 × 0.19
MRI = 26.22
```

An MRI of 26.22 is in the extreme-risk band for the shopping cart (threshold for mandatory Change Advisory Board escalation: MRI > 15). The OCR term is doing meaningful work here — without the full team on standby, OCR_weighted drops to 1.3, pushing MRI to 47.4. This quantifies what experienced engineers already know intuitively: Kafka upgrades must not be attempted with a skeleton crew.

---

## 5. The Service Compatibility Window (SCW) Problem

The **Service Compatibility Window** is the period during which producers on 2.8 must write to brokers on 3.5, and consumers on 3.5 must read from brokers that may still carry 2.8-format log segments. The SCW is not a choice — it is a mathematical consequence of the migration topology.

In the blue-green migration approach (two clusters, topic-by-topic consumer migration), the SCW for each topic begins when the first consumer is pointed at the 3.5 cluster and ends when the last producer has been migrated off the 2.8 cluster for that topic. For the `order-events` topic (Order Management produces, Notification and Consumer Group A consume), the SCW spans the time between migrating Notification Service to 3.5 and migrating Order Management's producer to 3.5. If Notification migrates on Day 3 of the migration window and Order Management migrates on Day 7, the SCW for `order-events` is 4 days.

**Incremental cooperative rebalancing and the SCW.** The new rebalance protocol in 3.5 is not backward-compatible with eager consumers in the same consumer group. If a consumer group has 3 consumers and one is migrated to a 3.5 client library (incremental cooperative) while two remain on 2.8 (eager), the group coordinator falls back to eager rebalancing for the entire group on every rebalance event. The SCW must therefore be minimized by migrating all consumers within a single consumer group together in one operation, not individually. Partial consumer group migrations are not safe.

**Practical implication:** Consumer groups must be treated as atomic migration units. For Notification Service, which runs 4 consumer instances across two availability zones, all 4 instances must be redeployed with the 3.5 client library in the same deployment window. A rolling restart that leaves 2 instances on 2.8 and 2 on 3.5 creates exactly the mixed-protocol failure condition described above.

---

## 6. Rollback Reality: Why Kafka RV Is Not Minutes

For most service changes, **Rollback Velocity (RV)** is measured in minutes: redeploy the previous container image, restore the previous feature flag state, or revert the configuration map. Kafka version rollback is categorically different.

Kafka 3.5 brokers write log segments in a newer internal format. Once records exist on disk in the new format, a 2.8 broker cannot read them. A rollback from 3.5 to 2.8 therefore requires one of two options: (1) restore the entire MSK cluster from a snapshot taken before the 3.5 upgrade began, or (2) accept that all records written to the 3.5 cluster are unreadable on the restored 2.8 cluster and treat them as lost. Neither option has an RV of minutes. Snapshot restoration for a production MSK cluster with 100GB of data across 6 brokers takes 45–90 minutes in typical scenarios, and during that window all Kafka-dependent services are degraded. Treated as lost records means replaying from a source-of-truth system if one exists, or accepting data loss if not.

**What this means for migration strategy:** Because rollback is expensive and slow, forward progress must be validated at every step before proceeding. The migration must not advance to the next consumer group until the current group has been validated for 24 hours. The maintenance window for each consumer group migration must include explicit go/no-go gates. If a no-go decision is reached after a consumer group has already been migrated, the response is to halt further migration — not to roll back what has already been done. In practice, this means the 3.5 cluster runs with partial migration state (some consumer groups on 3.5, others still on 2.8 via mirror) until the go-forward decision is made with full leadership awareness.

**Error Budget Reservation (EBR) before upgrade begins:** Given the high rollback cost, the EBR for this migration must be calculated conservatively. Order Management (P0) has a 99.95% monthly availability SLO, which translates to approximately 21.9 minutes of allowable downtime per month. The migration must not begin unless at least 15 minutes of error budget remain for the current calendar month. Any migration that begins with less than 15 minutes of remaining budget cannot afford even a brief Kafka disruption without breaching the SLA.

---

## 7. Consumer Lag Alert Reconfiguration Using APR Logic

Standard consumer lag alerts fire when a consumer group falls more than N messages behind the producer offset. During a Kafka upgrade, consumer lag spikes are expected at multiple points: when consumer groups are paused for migration, when incremental cooperative rebalancing redistributes partition assignments, and when consumer instances restart with the new client library. Without adjusting thresholds, these expected events generate false-positive alerts, flooding the on-call engineer and reducing **Alert Precision Rate (APR)**.

APR is the fraction of alerts that represent real actionable incidents versus total alerts fired. During normal operations, the target APR for consumer lag alerts is above 0.85. During a migration window, unmodified lag alerts will produce APR near 0.20 — meaning 4 out of 5 pages are noise. This is operationally dangerous: high alert volume during a complex migration causes alert fatigue precisely when the on-call engineer needs to detect a genuine rebalance storm or offset regression.

**Reconfiguration approach:**

Before each consumer group migration window begins, the on-call SRE must execute the following alert modifications:

1. **Suppress the standard lag alert** for the specific consumer group being migrated. Use Prometheus alertmanager inhibition rules or CloudWatch composite alarm suppression tied to the migration maintenance window label.
2. **Activate a replacement alert** that fires only if consumer lag for the group has not returned to baseline within 45 minutes of the migration window end time. This alert has no false positives — a 45-minute non-recovery is genuinely anomalous.
3. **Add a rebalance duration alert** specific to the migration: fire if a single consumer group rebalance event takes longer than 90 seconds. Normal rebalances under incremental cooperative rebalancing complete in under 15 seconds. A 90-second threshold filters out normal rebalancing while catching genuine stuck rebalances.
4. **Restore original alert thresholds** within 30 minutes of completing the migration window and confirming consumer lag has returned to baseline.

This alert lifecycle must be documented in the migration runbook and executed as a checklist item — not as an ad-hoc decision made under time pressure during the window itself.

---

## 8. Migration Strategy: Blue-Green Kafka, Low-DG First

The recommended approach is a **blue-green Kafka migration**: stand up the 3.5 MSK cluster in parallel with the existing 2.8 cluster, use MSK Replicator (or MirrorMaker 2) to replicate all topics from 2.8 to 3.5 in real time, then migrate consumer groups topic by topic to read from the 3.5 cluster. Producers are migrated last, after all consumers for their topics have been validated on 3.5.

**Sequence: low-DG services first.**

The MRI framework dictates migrating the lowest-DG consumers first. A failure in a low-DG service during migration causes minimal cascade impact and generates learning about the 3.5 cluster behavior before higher-DG services are exposed.

| Migration Order | Service | DG | Role | Consumer Group |
|----------------|---------|-----|------|---------------|
| 1 | Analytics Pipeline | 1 | Consumer | `analytics-all-topics` |
| 2 | Consumer Group B (audit) | 2 | Consumer | `audit-log-consumer` |
| 3 | Notification Service (P2) | 3 | Consumer | `notification-order-events` |
| 4 | Consumer Group A | 4 | Consumer | `internal-consumer-a` |
| 5 | Inventory Service (P1) | 5 | Producer migration | N/A (consumer of own topic) |
| 6 | Order Management (P0) | 8 | Producer migration | `order-mgmt-consumer` |

Analytics Pipeline is migrated first: DG = 1, no SLO, batch workload. Failure here does not affect any customer journey. Consumer Group B is migrated second: DG = 2, audit log consumer — delay is acceptable, data loss is not, so offset migration must be verified. Notification Service (P2) migrates third — this is the first SLO-bearing consumer group in the sequence and the first real test of the 3.5 cluster under production load for a critical service. Order Management consumer and producer migration is last because P0 cannot afford the risk of being the canary.

Producer migration for Order Management happens only after all consumers of its topics have been validated on 3.5 for at least 24 hours. The `acks` configuration for Order Management must be explicitly set to `acks=1` in the producer configuration before migration if the current behavior relies on the 2.8 default. This prevents the silent latency regression from the `acks=all` default change.

---

## 9. Post-Upgrade Validation: 72-Hour Checklist per Consumer Group

For each consumer group migrated to the 3.5 cluster, the following validation checks must pass continuously for 72 hours before that group is considered stable and the migration proceeds to the next group.

**Offset integrity:** Consumer group committed offset on the 3.5 cluster must advance monotonically. Any stall in committed offset advance (lag increasing without corresponding producer slowdown) indicates a consumer stuck in rebalance or a deserializer incompatibility. Alert threshold: lag increase of more than 500 messages with no corresponding producer backpressure event, sustained for more than 2 minutes.

**Rebalance frequency:** Normal rebalance frequency for a stable consumer group is zero to one rebalance per 6 hours (triggered by routine deployments or instance replacements). More than 3 rebalances in a 6-hour window indicates a consumer group stability problem — typically a consumer that is slow to heartbeat under the new protocol or a misconfigured `session.timeout.ms` value.

**End-to-end message latency:** For Notification Service, measure time from order event produce timestamp to notification delivered event. Expected p99 latency: under 3 seconds. A p99 above 5 seconds after migration indicates either consumer lag accumulation or a downstream processing regression introduced by the client library upgrade.

**Dead letter queue (DLQ) rate:** Any increase in DLQ message rate above baseline (pre-migration average) indicates a deserialization failure, a schema incompatibility between producer (still on 2.8 format) and consumer (on 3.5 client), or an application-level processing error surfaced by the new message format handling. DLQ rate must remain within 5% of baseline.

**KRaft quorum health (cluster-level, continuous):** The 3.5 cluster's KRaft metadata quorum must maintain 3/3 active voters throughout the migration. A quorum with fewer than 3 voters (one controller node degraded) is a cluster health risk that must pause all further migration activity until resolved.

---

## Summary: What This Scenario Teaches

Kafka upgrades are the canonical example of a change where the **cost of the safe path is real but the cost of the fast path is potentially catastrophic**. The PCC calculation shows the economic pressure to cut the migration short; the MRI of 26.22 shows why that pressure must be resisted. The RV analysis is the most important lesson: when rollback is measured in hours rather than minutes, each forward step must be treated as irreversible. The blue-green topology with low-DG-first sequencing is not a Kafka-specific pattern — it is the general SRE approach to any infrastructure migration where rollback is expensive. Kafka makes the stakes undeniable.
