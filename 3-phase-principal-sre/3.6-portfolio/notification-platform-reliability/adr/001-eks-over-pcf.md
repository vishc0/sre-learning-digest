# ADR 001: Kubernetes (EKS) Over Pivotal Cloud Foundry (PCF) for Notification Platform

**Status**: Accepted  
**Date**: 2023-Q3 (migration completed 2024-Q1)  
**Decision makers**: SRE Manager, Engineering Manager, Platform Architect  
**Stakeholders**: Notification platform team, infrastructure, security, finance

---

## Context

The notification platform was originally deployed on Pivotal Cloud Foundry (PCF), T-Mobile's enterprise PaaS standard at the time of platform inception. PCF provided a managed deployment target with buildpack-based deployment, service broker integrations for RabbitMQ and Redis, and centralized logging via the Loggregator system.

As the platform scaled from 3M to 25M messages/day and the team grew from 4 to 15 SREs, several constraints with PCF became migration drivers:

1. **Deployment window restrictions**: PCF ops team enforced 4-hour maintenance windows for platform updates. Any PCF version bump required coordination across 20+ teams. The notification platform could not deploy independently of the shared PCF upgrade cadence.

2. **Scaling granularity**: PCF scaled by instance count per application. There was no equivalent to Kubernetes HPA — scaling decisions required manual configuration changes through the CF CLI. Burst traffic from marketing campaigns required manual pre-scaling 30 minutes in advance.

3. **Networking rigidity**: PCF's internal networking relied on the Cloud Foundry router, which added latency and had limited support for connection-level traffic control. Implementing per-consumer rate limiting or circuit breakers required application-level code rather than infrastructure-level policy.

4. **Observability gaps**: PCF Loggregator had documented message loss under high log volume — exactly the condition a 25M msg/day platform creates. Structured log correlation between the broker, consumer, and downstream carrier required workarounds that increased engineering toil.

5. **Vendor trajectory**: VMware's acquisition of Pivotal and subsequent changes to PCF's product roadmap introduced long-term viability uncertainty. T-Mobile's enterprise architecture team made a strategic decision to consolidate on EKS for all new platform workloads.

---

## Decision

Migrate the notification platform from PCF to Amazon EKS (Elastic Kubernetes Service) with the following architectural commitments:

- **Deployment model**: Helm charts per service (notification-api, sms-consumer, push-consumer, email-consumer) with GitOps delivery via ArgoCD.
- **Scaling**: Kubernetes HPA on CPU + custom metrics (RabbitMQ queue depth via KEDA). No manual pre-scaling for campaigns.
- **Networking**: AWS VPC CNI plugin, Kubernetes NetworkPolicy for namespace isolation, NLB for the API layer.
- **Observability**: OpenTelemetry sidecar per pod, dual-export to Splunk (SIEM) and Prometheus (SLO alerting). See ADR-002 for the dual-export decision.
- **Secret management**: AWS Secrets Manager via External Secrets Operator (ESO). Eliminates hardcoded credentials in application config.

---

## Consequences

**Positive**:
- Deployment frequency increased from 2x/month to 8x/month (see DORA Metrics Baseline).
- Zero-downtime rolling deployments replaced 4-hour maintenance windows.
- Autoscaling eliminated manual campaign pre-scaling — KEDA scales consumers within 90 seconds of queue depth crossing threshold.
- SRE team has full control over the deployment lifecycle; no dependency on a shared PCF ops team.
- Cost reduction: EKS running right-sized Spot instances (for consumers) + On-Demand (for API) reduced compute cost by approximately 35% vs. PCF instance pricing at equivalent throughput.

**Negative / Costs accepted**:
- EKS requires more operational expertise than PCF. The team invested 3 months in Kubernetes training before migration. Two SREs obtained CKA certification.
- PCF's service broker made RabbitMQ and Redis provisioning trivially simple. EKS requires managing Helm charts for these services (or using AWS-managed equivalents). We chose to keep RabbitMQ on EKS (self-managed) for queue topology control — see ADR-003.
- The initial migration required a 6-month parallel-run period where both PCF and EKS received traffic. This added operational complexity and cost during the transition.

**Risks accepted**:
- EKS control plane is AWS-managed but cluster upgrades remain the team's responsibility. We committed to upgrading within 60 days of each new EKS release.
- The AWS us-east-1 dependency means a regional failure affects the platform. PCF's multi-datacenter deployment provided geographic redundancy. We mitigated this with a warm-standby deployment in us-west-2 (active-passive, not active-active).

---

## Alternatives Considered

**Stay on PCF**: Rejected. The deployment window and scaling constraints were hard blockers for reaching the 99.9% API availability SLO at growing traffic volumes.

**AWS ECS (Fargate)**: Evaluated. ECS would have reduced operational complexity (no node management) but limited our ability to run stateful workloads (RabbitMQ) in the same cluster and removed the ecosystem of Kubernetes operators we wanted (KEDA, External Secrets, cert-manager). The Kubernetes ecosystem investment was judged worth the additional complexity.

**Self-managed Kubernetes (kops on EC2)**: Rejected. EKS control plane management overhead is not a competitive advantage for the notification team. Delegating control plane operations to AWS was the right trade.

---

## Review Date

This ADR is reviewed annually or when: EKS is no longer the T-Mobile standard; platform traffic exceeds 100M messages/day (at which point multi-region active-active must be reassessed); or a significant PCF successor emerges with credible operational parity.
