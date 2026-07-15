# Notification Platform Reliability — SRE Portfolio Project

**Author**: Vishweshwar Chippa | SRE Manager / Principal SRE  
**Platform Scale**: 25M messages/day | 15-person SRE team  
**Stack**: AWS EKS, RabbitMQ, Cassandra, Redis, Splunk, OpenTelemetry  
**Outcome**: Zero Sev1 incidents over 36 consecutive months

---

## What This Project Demonstrates

This repository documents the reliability engineering practice behind a production notification platform processing 25 million messages per day at T-Mobile. It is not a toy example — the SLOs, runbooks, dashboards, and ADRs reflect the actual engineering decisions and operational patterns governing a platform that affects millions of T-Mobile customers daily.

Hiring managers reading this will find:

- **SLO-driven operations**: Three production SLOs with Sloth YAML definitions, error budget burn rate math, and a formal budget policy that governs feature freeze and rollback decisions.
- **Runbooks as code**: Two primary runbooks (high burn rate response, RabbitMQ DLQ backup) written to the standard that on-call engineers execute without tribal knowledge.
- **Architecture Decision Records**: Three ADRs capturing why EKS was chosen over PCF, why we run dual-export telemetry (Splunk + OpenTelemetry), and why RabbitMQ was retained over Kafka for this workload.
- **DORA baseline**: Real deployment frequency, lead time, change failure rate, and MTTR numbers (sanitized where needed) showing a high-performing delivery team.
- **Grafana dashboard design**: Four-panel JSON config translatable to any Grafana instance with a Prometheus or Splunk datasource.

---

## Platform Architecture Summary

```
                        ┌─────────────────────────────────────────────────────┐
                        │              AWS us-east-1                          │
                        │                                                     │
   Upstream Systems     │   ┌──────────────┐    ┌─────────────────────────┐  │
   (CRM, Billing,  ───► │   │  API Gateway │───►│  Notification Producer  │  │
    Campaign Mgr)       │   │  + WAF       │    │  (EKS Deployment x3)    │  │
                        │   └──────────────┘    └──────────┬──────────────┘  │
                        │                                  │                  │
                        │                         ┌────────▼────────┐        │
                        │                         │   RabbitMQ       │        │
                        │                         │  Cluster (x3)   │        │
                        │                         │  Queues:         │        │
                        │                         │  - sms.high      │        │
                        │                         │  - sms.standard  │        │
                        │                         │  - push.high     │        │
                        │                         │  - push.standard │        │
                        │                         │  - email.bulk    │        │
                        │                         │  DLQ per queue   │        │
                        │                         └────────┬────────┘        │
                        │                                  │                  │
                        │              ┌───────────────────┼──────────────┐  │
                        │              │                   │              │  │
                        │   ┌──────────▼──────┐  ┌────────▼──────┐      │  │
                        │   │  SMS Consumer   │  │  Push Consumer │      │  │
                        │   │  (EKS x5 pods)  │  │  (EKS x8 pods) │      │  │
                        │   └──────────┬──────┘  └────────┬──────┘      │  │
                        │              │                   │              │  │
                        │   ┌──────────▼───────────────────▼──────────┐  │  │
                        │   │          Downstream Carriers             │  │  │
                        │   │   (Twilio, FCM/APNs, SendGrid)          │  │  │
                        │   └──────────────────────────────────────────┘  │  │
                        │                                                  │  │
                        │   ┌────────────────────────────────────────────┐│  │
                        │   │              Data Layer                    ││  │
                        │   │  Cassandra (delivery state)                ││  │
                        │   │  Redis (dedup / rate limiting)             ││  │
                        │   │  S3 (DLQ archive / replay)                 ││  │
                        │   └────────────────────────────────────────────┘│  │
                        │                                                  │  │
                        │   ┌────────────────────────────────────────────┐│  │
                        │   │          Observability Layer               ││  │
                        │   │  OTel Collector (sidecar per pod)          ││  │
                        │   │  Splunk HEC (primary SIEM + alerting)      ││  │
                        │   │  Grafana + Prometheus (SLO burn dashboards)││  │
                        │   └────────────────────────────────────────────┘│  │
                        └─────────────────────────────────────────────────┘  │
                          └──────────────────────────────────────────────────┘
```

---

## Repository Contents

```
notification-platform-reliability/
├── PORTFOLIO_README.md           # This file — start here
├── slo-definitions.yaml          # Sloth-format SLO definitions (3 SLOs)
├── error-budget-policy.md        # What happens at 50/75/100% burn
├── dora-metrics-baseline.md      # Deployment frequency, MTTR, CFR, lead time
├── dashboards/
│   └── grafana-slo-dashboard.json  # 4-panel Grafana dashboard
├── runbooks/
│   ├── high-burn-rate.md         # Primary on-call response: SLO burn alert
│   └── queue-backup.md           # RabbitMQ DLQ escalation runbook
└── adr/
    ├── 001-eks-over-pcf.md       # Why we migrated from PCF to EKS
    ├── 002-dual-export.md        # Why Splunk + OTel dual-export telemetry
    └── 003-rabbitmq-vs-kafka.md  # Why RabbitMQ over Kafka for this workload
```

---

## Key Reliability Outcomes

| Metric | Baseline (Year 1) | Current (Year 3) |
|---|---|---|
| Sev1 incidents | 8/year | 0 (36 months) |
| MTTR (P1) | 47 min | 12 min |
| Deployment frequency | 2x/month | 8x/month |
| Change failure rate | 18% | 4% |
| SLO compliance | 97.2% | 99.7% |
| On-call alert noise | ~200/week | ~18/week |

---

## Why This Matters to Your Organization

A notification platform is a trust surface. When a bank's fraud alert, a carrier's network outage SMS, or a retailer's order confirmation fails to deliver — customers lose trust in the brand, not the notification vendor. Engineering reliability into this layer at 25M messages/day requires:

1. **SLO precision** — distinguishing carrier-caused failures from platform failures to protect the error budget from noise outside the team's control.
2. **Queue discipline** — RabbitMQ DLQ hygiene that prevents silent message loss while not hiding retry storms.
3. **Dual-export telemetry** — running OTel alongside Splunk means no vendor lock-in and the ability to migrate observability stacks without a production blind spot.

This portfolio documents how those three concerns were engineered and operationalized.

---

## Contact

LinkedIn: [linkedin.com/in/vchippa](https://linkedin.com/in/vchippa)  
Email: available on request  
GitHub: this repository
