# STAR Story 04: 25M Messages/Day Platform — Scale Design and Tradeoffs
## Domain: Distributed Systems Design / Platform Architecture

---

## Situation

The T-Mobile notification platform I manage processes 25 million messages per day across three channels: SMS, push notification, and email. The platform serves customer-facing use cases including fraud alerts (latency-critical — must deliver within seconds), marketing campaigns (burst-heavy — millions of messages in a short window), and operational notifications like bill pay confirmations and service outage alerts. These three traffic types have fundamentally different SLO requirements and failure behaviors. Fraud alerts failing silently is a compliance and customer trust issue. Marketing burst failures are a revenue issue. Operational notifications failing means customers think their service is broken when it isn't.

## Task

When I took over as SRE Manager, the platform was handling peak load through manual scaling — on-call engineers would provision additional message consumers before known campaign events. Unknown spikes caused degradation. My task was to assess the platform's scaling model, identify the architectural gaps, and lead the engineering work to make the system self-managing at scale without compromising SLO differentiation between message priority classes.

## Action (IC Technical Depth)

The first design problem I identified was that all three message types were on the same RabbitMQ queues with the same consumer configuration. A marketing campaign burst would saturate the consumers and starve fraud alert processing. The system had no priority differentiation — it was treating "your account may be compromised" and "here's a 10% off coupon" as equivalent work.

I proposed and implemented queue segregation by priority class: a dedicated queue and consumer pool for P1 (fraud/security), P2 (operational/transactional), and P3 (marketing/promotional). Each pool had independent autoscaling, independent SLOs, and independent circuit breakers. The key design decision was resource reservation: P1 consumers were always provisioned at minimum capacity — they never scaled to zero — while P3 consumers could scale to zero overnight and back to full capacity in under 90 seconds during campaign launch.

The second problem was EKS pod autoscaling. Standard Kubernetes HPA scales on CPU and memory, but our message consumers were I/O-bound, not CPU-bound. A consumer could be at 5% CPU while its queue had 500,000 messages backed up. I implemented KEDA (Kubernetes Event-Driven Autoscaling) with a RabbitMQ queue depth trigger: scale out when queue depth per consumer exceeds 1,000 messages, scale in when queue depth drops below 100. This gave us queue-aware autoscaling that responded to actual workload, not CPU proxy metrics.

The third problem was circuit breaking. When downstream SMS and push delivery APIs were degraded, our platform would continue consuming messages from RabbitMQ and failing to deliver them — messages were lost without retry. I implemented Resilience4j circuit breakers on all outbound delivery calls with a dead-letter queue pattern: failed messages went to DLQ with a retry schedule of 1 min, 5 min, 15 min, 60 min before being flagged for manual review. This meant P1 messages would always be attempted, even if delivery was slow, and nothing was silently dropped.

The fourth problem was the burst pattern for marketing campaigns. Campaign teams would schedule mass notifications for "9 AM Monday" — and every scheduling system would fire simultaneously, creating a thundering herd. I worked with the campaign platform team to implement rate-limited ingestion with a backpressure signal: if the notification platform's inbound queue exceeded a high watermark, we'd return a 429 to the campaign platform and they'd back off. This was a cross-team architectural negotiation, not just a technical change on our side.

## Result

After the redesign:
- Zero priority inversion incidents — P1 fraud alerts have never been delayed by P3 campaign bursts since implementation
- EKS pod count during campaign peaks: scales from ~20 consumers to 180+ in under 4 minutes (KEDA-driven), with no manual intervention
- KEDA autoscaling handled a 3x unplanned traffic spike (national emergency alert) without any manual response or degradation
- DLQ retry pattern eliminated silent message loss: we now have full visibility into every delivery failure with retry audit trail
- Campaign team SLA improved: 95% of marketing messages delivered within 4 minutes of scheduled send time (was 72% before queue isolation)

---

## Director/VP Version (Leadership Framing)

"The platform was architected as a single-tier system treating a fraud alert and a marketing coupon as equivalent workloads. That's a common scaling antipattern — you optimize for average load rather than worst-case priority conflicts. I led the redesign to introduce priority class segregation, queue-aware autoscaling with KEDA, and circuit-breaking with dead-letter retry. The result was a platform that handles a 3x unplanned spike without a page, that has never let a fraud alert be delayed by a marketing burst, and where we have full audit visibility into every delivery failure. The more important business outcome was that the campaign team now trusts the platform enough to schedule high-value campaigns without pre-calling us. That trust has a real revenue value."

## IC Version (Technical Depth)

"The core technical insight was that HPA on CPU was the wrong autoscaling signal for an I/O-bound message consumer. I replaced it with KEDA using a RabbitMQ queue depth trigger: scale out at 1,000 messages per consumer, scale in at 100. This gave us queue-aware scaling that responds to actual backlog, not CPU proxy. I also segregated queues by priority class — P1 consumers always provisioned at minimum, P3 consumers can scale to zero — and implemented Resilience4j circuit breakers on all outbound calls with a DLQ retry schedule. The rate-limiting backpressure with the campaign platform was a cross-team negotiation: I had to convince their engineering team that a 429 response from us was a feature, not a failure."

---

## 30-Second Version

"The platform was treating fraud alerts and marketing promotions as equal workloads. I implemented priority class queue segregation, replaced CPU-based autoscaling with KEDA queue-depth triggers, added circuit breakers with dead-letter retry, and negotiated rate-limiting backpressure with upstream campaign systems. The platform now handles 3x unplanned spikes without manual intervention and has never let a fraud alert be delayed by marketing traffic."

---

## 2-Minute Version

"When I looked at the platform architecture, the first thing I noticed was that all three message types — fraud alerts, operational notifications, marketing campaigns — were on the same queues with the same consumers. A marketing campaign burst could starve fraud alert processing. That's a compliance risk, not just a performance issue.

I redesigned around priority classes. Three separate queue and consumer pools, each with independent SLOs and independent autoscaling. P1 consumers — fraud and security — are always warm, minimum provisioned, never scale to zero. P3 consumers — marketing — can scale to zero overnight.

The autoscaling was a deeper problem. Kubernetes HPA scales on CPU, but message consumers are I/O-bound. CPU was at 5% while queues were backed up with 500,000 messages. I implemented KEDA with a RabbitMQ queue depth trigger — scale out when the backlog per consumer exceeds 1,000, scale in below 100. That change alone let us handle a 3x traffic spike from a national emergency alert without anyone being paged.

I also added circuit breakers with dead-letter retry on all outbound delivery calls. Before that, delivery failures were silent drops. Now every failure has a retry schedule — 1 minute, 5 minutes, 15 minutes, 60 minutes — and after that it's visible to the ops team. Nothing disappears.

The hardest part was the backpressure negotiation with the campaign platform team. Their system was creating thundering herd effects — everything scheduled for '9 AM Monday' fires simultaneously. I had to convince their engineering team to respect a 429 response from us as a legitimate flow control signal, not an error. That was a cross-team architectural conversation, not a code change.

The outcomes: P1 messages have never been delayed by P3 bursts since implementation, 3x spikes handled without manual intervention, and campaign delivery SLA improved from 72% to 95% within 4 minutes of schedule."

---

## Key Metrics to Remember
- Platform scale: 25M messages/day, 3 channels (SMS, push, email)
- Priority classes: P1 (fraud/security), P2 (operational), P3 (marketing)
- KEDA trigger: scale out at 1,000 messages/consumer, scale in at 100
- Autoscaling range: 20 → 180+ consumers in under 4 minutes
- 3x unplanned spike handled without manual intervention
- Campaign delivery SLA: 72% → 95% within 4 minutes
- DLQ retry schedule: 1m, 5m, 15m, 60m before manual review
- Zero priority inversion incidents since implementation
