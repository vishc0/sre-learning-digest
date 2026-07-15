# STAR Story 02: Six Zero-Downtime Migrations — The Hardest One
## Domain: Platform Migration / Change Management

---

## Situation

Over three years at T-Mobile, I led six zero-downtime migrations for the notification platform: two Cassandra version upgrades, a RabbitMQ cluster topology change (adding a third node to a two-node cluster under live traffic), a PCF-to-EKS containerization migration, a Redis cache layer replacement, and a downstream API contract change affecting 12 consuming services. The hardest was the PCF-to-EKS migration — we were moving a stateful, high-throughput messaging platform off Pivotal Cloud Foundry onto Amazon EKS while keeping the system live at 25 million messages per day.

## Task

I was the technical lead and incident commander for the PCF-to-EKS migration. My responsibility was the migration strategy, risk mitigation plan, stakeholder communication, and the go/no-go decision at each phase gate. This was not a lift-and-shift — PCF and EKS have fundamentally different networking models, health check mechanisms, and secrets management approaches, so every service needed rework, not just repackaging.

## Action (IC Technical Depth)

I started by refusing to accept the original project timeline. The initial plan from the platform team was a 3-month cutover with a "maintenance window" for final switchover. I pushed back because a maintenance window on a 25M msg/day platform during business hours means real customers not receiving fraud alerts, marketing messages, and service notifications. I proposed a strangler-fig pattern instead — run both platforms in parallel with traffic splitting, not a hard cutover.

I designed a six-phase approach:
1. **Containerize without migrating** — rebuild all services as Docker images, run them on PCF first, verify behavior is identical. This decoupled container readiness from infrastructure readiness.
2. **Shadow traffic on EKS** — stand up EKS cluster, route a copy of incoming messages to EKS services without acting on them. Used this to validate processing behavior, latency profiles, and log output against PCF baseline.
3. **1% canary** — route 1% of live traffic to EKS, hold for 72 hours, monitor every SLI. I personally wrote the Splunk queries comparing EKS vs PCF error rates, latency percentiles, and message delivery confirmation rates in real time.
4. **Stepped ramp** — 5%, 20%, 50%, 80% over two weeks, with automated rollback triggers if any SLI crossed SLO threshold.
5. **PCF as cold standby** — at 100% EKS traffic, kept PCF provisioned but idle for two weeks. Used this period to prove we could tolerate a full EKS failure by failing back.
6. **PCF decommission** — only after 30 days of clean EKS operation.

The hardest technical problem was secrets management. PCF used credential injection via VCAP_SERVICES environment variable at runtime. EKS used Vault with Kubernetes auth. I had to refactor every service's secret retrieval pattern without changing business logic — I wrote the Vault integration library once, tested it exhaustively in shadow mode, and required every team to adopt it before their service could graduate to canary.

The hardest human problem was the product team. Two product managers wanted to launch new notification types during the migration. I held a steering committee meeting and explained the risk in terms they understood: "If we add new message types during a dual-stack migration, we are simultaneously testing the migration and validating new features on the same canary population. A failure gives us no clean signal — we can't tell if it's the migration or the new feature." They agreed to a feature freeze. That conversation required translating technical risk into business risk, not just saying "no."

## Result

PCF-to-EKS migration completed with zero customer-impacting incidents. Total migration duration: 11 weeks (vs. 3-month initial estimate with maintenance window risk). PCF infrastructure decommissioned, reducing monthly infrastructure cost by approximately $18,000/month. EKS also gave us autoscaling capability we didn't have on PCF — we subsequently handled a 3x traffic spike during a national emergency alert without manual intervention. All six migrations across my tenure were completed zero-downtime.

---

## Director/VP Version (Leadership Framing)

"I've led six zero-downtime migrations on a 25M msg/day platform. The principle I apply consistently is: the migration strategy has to be designed around the failure mode, not the success path. On our PCF-to-EKS migration, I replaced a proposed maintenance window with a 6-phase strangler-fig approach and a feature freeze, which required saying no to product leadership mid-execution. The outcome was zero customer impact, $18K/month cost reduction, and a platform that could autoscale — something PCF couldn't give us. More importantly, I now have a team that has run a large-scale live migration under production conditions. That's an organizational capability, not just a project outcome."

## IC Version (Technical Depth)

"The key technical insight was decoupling container readiness from infrastructure readiness. By containerizing services and running them on PCF first, I proved Docker behavior before introducing EKS networking unknowns. Then I ran shadow traffic on EKS — a copy of real messages, no customer impact — to establish a behavioral baseline before any traffic was routed live. I personally wrote the comparative Splunk queries that tracked EKS vs PCF SLIs in real time during ramp-up. The secrets management refactor was the ugliest part: I wrote the Vault/Kubernetes auth integration library once, tested it in shadow mode for two weeks, and made it the gate condition for canary graduation. No service went to 1% canary without clean Vault integration."

---

## 30-Second Version

"I led a PCF-to-EKS migration for a 25M msg/day platform using a six-phase strangler-fig approach instead of a maintenance window. I containerized first, ran shadow traffic, then ramped from 1% to 100% over two weeks with automated rollback triggers. Zero customer-impacting incidents. Cost savings of $18K/month. Completed in 11 weeks."

---

## 2-Minute Version

"The project was originally scoped as a 3-month effort ending with a maintenance window for the final switchover. I rejected that immediately — a maintenance window on a 25 million message per day platform means real customers missing fraud alerts and service notifications. I pushed for a strangler-fig approach: run both platforms simultaneously, shift traffic incrementally, never cut over hard.

I designed six phases: containerize without migrating, shadow traffic on EKS, 1% canary for 72 hours, stepped ramp to 100%, PCF as cold standby for 30 days, then decommission. Each phase had explicit go/no-go criteria tied to SLO burn rates, not gut feel.

The hardest technical problem was secrets management — PCF injected credentials via environment variables, EKS used Vault with Kubernetes auth. I wrote the Vault integration library once, ran it through two weeks of shadow traffic validation, and made it a hard gate before any service could go to canary.

The hardest human problem was a feature freeze. Two product managers wanted to launch new notification types mid-migration. I held a steering committee and explained: if we test the migration and new features on the same canary population, a failure gives us no clean signal. They agreed to hold.

Outcome: zero customer impact across the entire migration, $18K/month in PCF infrastructure savings, and we gained EKS autoscaling capability we later used to handle a 3x traffic spike without paging anyone. That spike used to be a Sev2. Now it's a non-event."

---

## Key Metrics to Remember
- 6 total zero-downtime migrations over 3 years
- PCF-to-EKS: 11 weeks, zero customer incidents
- Cost reduction: $18,000/month PCF decommission
- Platform scale: 25M messages/day throughout migration
- Traffic ramp: 1% → 5% → 20% → 50% → 80% → 100%
- Shadow traffic duration: 2 weeks before any live traffic
- Canary hold: 72 hours minimum at 1%
- Feature freeze: enforced for full migration duration
