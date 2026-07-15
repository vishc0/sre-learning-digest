# ADR 003: RabbitMQ Over Apache Kafka for the Notification Delivery Pipeline

**Status**: Accepted  
**Date**: 2021-Q1 (original platform design); reaffirmed 2024-Q1 (EKS migration review)  
**Decision makers**: Principal SRE, Engineering Manager, Platform Architect  
**Stakeholders**: Notification platform team, upstream integration teams (CRM, billing, campaign)

---

## Context

When the notification platform was initially designed, the team evaluated both RabbitMQ and Apache Kafka as the message broker layer. This ADR documents the original decision and its 2024 reaffirmation, since the EKS migration was an explicit opportunity to re-evaluate.

This decision matters because it affects: message routing complexity, consumer scaling behavior, dead-letter handling, delivery semantics (at-least-once vs. exactly-once), and operational tooling.

**The core tension**: Kafka is the industry default for high-throughput streaming at scale and is increasingly the "safe" choice for SRE-adjacent engineers. RabbitMQ is less fashionable but better suited to the specific routing, acknowledgement, and dead-letter requirements of a notification delivery pipeline.

Choosing the less-fashionable tool is a defensible engineering decision if the reasoning is documented — which is the purpose of this ADR.

---

## The Workload Profile

Before the decision, the team characterized the workload:

| Characteristic | Value | Implication |
|---|---|---|
| Peak throughput | 25M messages/day (~290 msg/s peak ~900 msg/s) | Both Kafka and RabbitMQ handle this comfortably |
| Message size | 200–2000 bytes (notification payloads) | Small; both handle this |
| Routing requirements | 5 channels × 2 priorities = 10 logical lanes | Complex; see below |
| Delivery semantics | At-least-once, with DLQ for final failure handling | Both support this |
| Consumer model | Push (broker pushes to consumers) | RabbitMQ native; Kafka requires poll loop |
| Dead-letter requirements | Per-queue DLQ with TTL-based expiry | RabbitMQ native; Kafka requires manual implementation |
| Message TTL | High-priority: 300s; Standard: 3600s; Bulk: 86400s | RabbitMQ native per-message TTL; Kafka TTL is per-topic only |
| Replay requirement | Replay DLQ messages on demand (not always) | RabbitMQ: shovel/replay; Kafka: consumer group offset reset |
| Ordering requirement | None (notifications are independent) | Kafka's ordering guarantee is not needed |

---

## Decision

**Retain RabbitMQ** as the notification platform message broker.

**Key factors**:

### 1. Per-Message TTL and Dead-Letter Routing

Notification messages have strict TTL requirements: a 2FA code that expires in 5 minutes should not be delivered 10 minutes later — it would confuse the user and potentially create a security issue. RabbitMQ supports per-message TTL natively. When a message expires, it routes to the configured DLQ automatically.

Kafka's TTL model is per-topic/partition and is based on log retention time — it cannot expire individual messages before the log retention window. Implementing per-message TTL in Kafka requires application-level logic in every consumer, which distributes what should be infrastructure behavior into application code.

### 2. Push vs. Poll Consumer Model

RabbitMQ's push model (broker delivers messages to subscribed consumers) aligns naturally with the notification workload: consumers are always ready and should process messages as fast as they arrive. The push model also enables per-consumer prefetch count tuning, which allows the team to control in-flight message pressure without changing consumer code.

Kafka's poll model requires consumers to call `poll()` on a loop. For notification delivery, this adds artificial latency (the poll interval) and requires careful tuning of `max.poll.records` and `max.poll.interval.ms` to balance throughput against consumer group rebalancing timeouts. At 290 msg/s peak, this tuning is manageable — but it is operational complexity that provides no benefit for the workload.

### 3. Routing Topology Flexibility

The notification platform routes messages based on channel (SMS/push/email), priority (high/standard/bulk), and in some cases, carrier affinity (some carriers have dedicated processing queues for rate-limit compliance). This is a classic enterprise messaging routing problem.

RabbitMQ exchanges (direct, topic, headers) are purpose-built for this. A single topic exchange with routing keys like `sms.high`, `push.standard`, `email.bulk` provides the entire routing topology without any application-level routing logic.

Kafka's partitioning model routes by key hash within a topic. Implementing 10 logical lanes in Kafka requires 10 topics (or complex partition key conventions), each with its own consumer group. Consumer group management at 10+ topics creates operational overhead that grows with new notification channels.

### 4. Operational Familiarity

At the time of original design, the T-Mobile operations team had 4 years of RabbitMQ operational experience. The team knew how to tune memory watermarks, manage cluster split-brain scenarios, and interpret the management UI. Kafka operations expertise was limited to one engineer.

Operational familiarity is a legitimate factor in platform decisions. A platform you understand and can operate confidently at 3am is more reliable than a platform that is theoretically superior but requires specialized expertise the team does not have.

---

## Why Not Kafka?

Kafka's advantages over RabbitMQ for this workload are: better throughput above ~50,000 msg/s; built-in log retention for replay (useful for stream processing, less critical for notification delivery); and the consumer offset model (useful when consumers need to independently re-read history — not a notification platform requirement).

None of these advantages are relevant at 25M messages/day with a notification delivery workload. The disadvantages (poll model, per-topic TTL only, complex routing topology) add engineering cost that is not justified.

**The 2024 reaffirmation**: At the EKS migration review, the team evaluated replacing RabbitMQ with Amazon SQS or MSK (managed Kafka). SQS was rejected because it lacks per-message DLQ routing flexibility and the fan-out model requires SNS integration complexity. MSK was rejected for the same reasons as self-managed Kafka. The conclusion: RabbitMQ on EKS, maintained by the team, continues to be the correct choice.

---

## Consequences

**Positive**:
- Per-message TTL and DLQ routing work exactly as designed, with no application-level workarounds.
- Consumer scaling via KEDA (queue-depth-based HPA) integrates directly with RabbitMQ metrics via the `rabbitmq_prometheus` plugin — no custom adapter needed.
- Routing topology changes (new channel, new priority tier) require only exchange/binding configuration changes, not code deploys.
- Operational team is expert in RabbitMQ failure modes (memory alarms, disk alarms, partition handling, connection storms).

**Negative / Costs accepted**:
- RabbitMQ is not a log store. If a consumer needs to replay historical messages beyond the DLQ window, it cannot. The platform maintains an S3 archive of all DLQ messages and a separate event store (Cassandra) for notification state — replay requires querying the event store and re-publishing, not native broker replay.
- RabbitMQ's high-availability mode (classic mirrored queues or quorum queues) requires careful configuration. Quorum queues (the modern choice) require a 3-node cluster for fault tolerance. This is a hard minimum that cannot be reduced without losing HA guarantees.
- The broader industry trend toward Kafka means that RabbitMQ operational expertise is harder to hire for. New SRE onboarding requires deliberate RabbitMQ training. This is tracked as a team capability risk.

**Risks accepted**:
- If the platform scales beyond 5,000 msg/s sustained throughput, this decision should be re-evaluated. At that point, Kafka's throughput advantages become materially relevant and the routing complexity delta becomes manageable.

---

## Review Triggers

Re-evaluate this decision if:
- Platform throughput exceeds 5,000 msg/s sustained
- A new notification channel requires stream processing semantics (e.g., real-time ML scoring of message content)
- T-Mobile standardizes on MSK for all event-driven workloads and the team inherits Kafka expertise organically
- RabbitMQ Streams (the Kafka-compatible extension added in RabbitMQ 3.9) matures to production-readiness and provides a migration path with retained operational familiarity
