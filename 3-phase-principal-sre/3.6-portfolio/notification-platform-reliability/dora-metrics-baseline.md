# DORA Metrics Baseline — Notification Platform

**Measurement period**: Q4 2024 – Q1 2026 (18 months)  
**Team size**: 15 SREs + 8 application engineers  
**Note**: Numbers are sanitized composites — specific dates and exact production incident identifiers are omitted per information security policy. Directional accuracy is preserved.

---

## What DORA Metrics Measure

DORA (DevOps Research and Assessment) metrics are the four signals that correlate most strongly with engineering team performance and organizational outcomes. They were derived from surveying 32,000+ engineers across 6 years.

Think of them as the four gauges on your delivery dashboard:

| DORA Metric | What It Measures | Analogy |
|---|---|---|
| Deployment Frequency | How often you ship to prod | How often your assembly line produces a unit |
| Lead Time for Changes | Time from commit to prod | Time from design approval to unit on the floor |
| Change Failure Rate | % of deploys that cause an incident | Defect rate off the line |
| Mean Time to Restore (MTTR) | How fast you recover from failures | Time to clear a line stoppage |

---

## DORA Elite Performer Thresholds (2024 State of DevOps Report)

| Metric | Elite | High | Medium | Low |
|---|---|---|---|---|
| Deployment Frequency | On-demand (multiple/day) | 1x/week–1x/month | 1x/month–6x/year | < 6x/year |
| Lead Time | < 1 hour | 1 day – 1 week | 1 week – 1 month | > 6 months |
| Change Failure Rate | 0–5% | 5–10% | 10–15% | > 15% |
| MTTR | < 1 hour | < 1 day | < 1 week | > 6 months |

---

## Notification Platform Baseline

### Deployment Frequency

**Current**: 8 deployments/month to production (2x/week average)  
**Year 1 baseline**: 2 deployments/month  
**DORA classification**: **High** (approaching Elite for a regulated telecom platform)

**What drove improvement**:
- Migrated from PCF push-model deploys (4-hour maintenance windows) to EKS rolling deployments (zero-downtime, 12-minute average).
- Introduced feature flags (LaunchDarkly) to separate deploy from release — teams can deploy daily, activate features on a scheduled release cadence.
- Built a pre-prod staging environment that mirrors production traffic patterns, reducing "deploy and pray" behavior.

**Constraint**: Telecom regulatory requirements (SOX, CPNI) require change advisory board (CAB) approval for changes touching customer data schemas. These changes remain on a 2x/month cadence. All other changes are self-service.

---

### Lead Time for Changes

**Current**: 2.4 days average commit-to-production  
**Year 1 baseline**: 11 days  
**DORA classification**: **High**

**Breakdown of current 2.4-day lead time**:

| Stage | Average Duration | Notes |
|---|---|---|
| PR open to first review | 4 hours | SRE team SLA: 4-hour first review for all PRs |
| PR review to merge | 18 hours | Includes iteration time; complex PRs can be 36h |
| Merge to staging deploy | 22 minutes | Automated via GitHub Actions → ArgoCD |
| Staging validation | 6 hours | Automated test suite + 1-hour canary soak |
| Staging to production | 2 hours | Canary 5% → 25% → 100% with automated rollback gates |

**What drove improvement**:
- Eliminated manual approval gates in the CI pipeline for non-schema changes.
- Built automated integration tests against a RabbitMQ test cluster — previously, integration testing was manual and took 2–3 days.
- Introduced PR size guidelines (max 400 lines changed) — large PRs reviewed in batches were the biggest lead time contributor.

---

### Change Failure Rate (CFR)

**Current**: 4%  
**Year 1 baseline**: 18%  
**DORA classification**: **Elite**

**Definition used**: A deployment is a "failure" if it causes a P1 or P2 incident within 48 hours of the deploy, or if it requires an emergency rollback within 24 hours.

**What drove improvement**:
- Canary deployment pattern: 5% traffic to new version for 30 minutes before full rollout. Automated rollback if error rate on canary exceeds 2x baseline.
- Pre-production load testing with production-representative traffic profiles (anonymized message replay).
- Dependency version pinning in all Helm charts — stopped "surprise" library upgrades from breaking consumers.
- RabbitMQ schema compatibility checks in CI — prevents consumer code from being deployed before producer changes are stable.

**Notable outlier**: Two of the three failures in the current 18-month window were caused by upstream carrier API changes with no advance notice. These are tracked separately as "external-caused CFR" and do not reflect platform engineering quality.

---

### Mean Time to Restore (MTTR)

**Current**: 12 minutes (P1 incidents)  
**Year 1 baseline**: 47 minutes  
**DORA classification**: **Elite**

**Definition used**: Time from first PagerDuty alert firing to incident resolved (SLO burn rate returning below 1.0x).

**Breakdown of current 12-minute MTTR**:

| Phase | Average Duration | Improvement Driver |
|---|---|---|
| Alert to acknowledge | 2.5 minutes | PagerDuty escalation policy tuned; mobile alerts |
| Acknowledge to diagnosis | 4.5 minutes | Runbooks with pre-built Splunk queries |
| Diagnosis to mitigation | 3.0 minutes | Feature flags for instant disable; canary rollback is one kubectl command |
| Mitigation to resolved | 2.0 minutes | Automated SLO burn rate recovery confirmation |

**What drove improvement**:
- Runbooks were rewritten from prose to step-by-step with exact commands and expected outputs. Engineers no longer need tribal knowledge to diagnose.
- Splunk saved searches for every P1 alert pattern — the alert links directly to the relevant dashboard.
- "Undo button" principle: every deployment can be rolled back in under 3 minutes using Helm rollback. Every feature flag change is reversible in < 30 seconds.
- Game days: quarterly chaos engineering exercises (pod kill, queue saturation, carrier latency injection) build muscle memory for the most common failure modes.

---

## DORA Summary Table

| Metric | Year 1 Baseline | Current | DORA Tier | Change |
|---|---|---|---|---|
| Deployment Frequency | 2x/month | 8x/month | High | +300% |
| Lead Time | 11 days | 2.4 days | High | -78% |
| Change Failure Rate | 18% | 4% | Elite | -78% |
| MTTR (P1) | 47 min | 12 min | Elite | -74% |

---

## What These Numbers Mean for a Hiring Manager

A team that moves from the "Medium" DORA band to the "High/Elite" band while simultaneously scaling from 8M to 25M messages/day — without a Sev1 in 36 months — demonstrates that reliability and velocity are not in opposition. The constraint is engineering practice, not the platform.

The improvements above were not achieved by adding headcount. They were achieved by investing in:
1. Automated deployment gates (canary + rollback)
2. Runbooks that encode institutional knowledge
3. SLO-driven prioritization that gives the team permission to slow down when the budget demands it

This is the Director/VP SRE model: reliability is a system property you engineer, not a heroism property you hope for.
