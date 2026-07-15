# LexusNexus SRE Tools

Related architecture reference: [`platform-architecture.md`](./platform-architecture.md)
Interview prep reference: [`interview-prep-principal-sre.md`](./interview-prep-principal-sre.md)
AI opportunities reference: [`ai-sre-opportunities.md`](./ai-sre-opportunities.md)

This document outlines the Site Reliability Engineering (SRE) tools commonly used (or recommended) for running reliable, scalable, and secure production systems at **LexusNexus**.

> Note: The repository currently has no existing tool inventory files, so this list is a practical SRE baseline stack.

## 1) Monitoring & Observability

### Prometheus
- **Purpose:** Metrics collection and time-series monitoring.
- **Used for:** Service health, resource usage, custom application metrics, SLO tracking.

### Grafana
- **Purpose:** Dashboards and visualization.
- **Used for:** Real-time and historical dashboards for latency, error rate, traffic, capacity, and business KPIs.

### Alertmanager
- **Purpose:** Alert routing and deduplication.
- **Used for:** Sending alerts to Slack, email, PagerDuty, and handling silences/escalations.

### OpenTelemetry
- **Purpose:** Standardized telemetry collection (metrics, logs, traces).
- **Used for:** Distributed tracing and correlation between services.

### Jaeger / Tempo
- **Purpose:** Trace storage and analysis.
- **Used for:** Root-cause analysis of latency spikes and cross-service failures.

## 2) Logging & Log Analytics

### Elasticsearch + Kibana (ELK)
- **Purpose:** Centralized log indexing and search.
- **Used for:** Troubleshooting incidents, finding patterns, and audit visibility.

### Fluent Bit / Fluentd / Logstash
- **Purpose:** Log collection and shipping.
- **Used for:** Aggregating logs from containers, VMs, and apps into a central platform.

## 3) Incident Response & On-call

### PagerDuty
- **Purpose:** On-call scheduling and incident escalation.
- **Used for:** Paging responders for critical alerts and managing incident workflows.

### Opsgenie (alternative)
- **Purpose:** Alerting and incident management.
- **Used for:** Team-specific escalation chains and on-call automation.

### Slack / Microsoft Teams
- **Purpose:** Real-time collaboration.
- **Used for:** Incident war rooms, alert notifications, and communication updates.

### Statuspage
- **Purpose:** External incident communication.
- **Used for:** Publishing service health and planned/unplanned outage updates.

## 4) Infrastructure as Code (IaC) & Configuration

### Terraform
- **Purpose:** Provisioning cloud infrastructure as code.
- **Used for:** Repeatable and version-controlled environments (network, compute, storage, IAM).

### Ansible
- **Purpose:** Configuration management and automation.
- **Used for:** Server bootstrap, patching, and operational runbooks.

### Helm
- **Purpose:** Kubernetes package management.
- **Used for:** Managing versioned app deployments to Kubernetes clusters.

## 5) Containerization & Orchestration

### Docker
- **Purpose:** Container packaging and runtime.
- **Used for:** Consistent app execution across environments.

### Kubernetes
- **Purpose:** Container orchestration.
- **Used for:** Auto-scaling, self-healing, rolling deployments, and service discovery.

### Argo CD / Flux
- **Purpose:** GitOps continuous delivery for Kubernetes.
- **Used for:** Declarative deployments and drift detection/reconciliation.

## 6) CI/CD & Release Engineering

### GitHub Actions / Jenkins / GitLab CI
- **Purpose:** Build, test, and deployment pipelines.
- **Used for:** Automated quality gates, artifact builds, and safe releases.

### SonarQube
- **Purpose:** Code quality and static analysis.
- **Used for:** Enforcing quality and maintainability standards pre-release.

### Artifact Repository (Nexus / Artifactory)
- **Purpose:** Binary/package storage.
- **Used for:** Versioned artifacts and dependable deploy inputs.

## 7) Reliability Engineering Practices (Tool-supported)

### Error Tracking (Sentry)
- **Purpose:** Application error monitoring.
- **Used for:** Exception aggregation, release health, and regression detection.

### Feature Flags (LaunchDarkly / Unleash)
- **Purpose:** Progressive delivery.
- **Used for:** Safe rollouts, canary exposure, and fast rollback without full redeploy.

### Load & Performance Testing (k6 / JMeter)
- **Purpose:** Performance validation.
- **Used for:** Capacity planning, pre-release stress testing, and bottleneck discovery.

## 8) Security & Compliance (DevSecOps-aligned)

### Vulnerability Scanning (Trivy / Clair)
- **Purpose:** Image and dependency scanning.
- **Used for:** Detecting CVEs in containers and software dependencies.

### Secrets Management (HashiCorp Vault / Cloud KMS)
- **Purpose:** Secure secret storage and rotation.
- **Used for:** API keys, credentials, encryption keys, and lease-based access.

### Policy as Code (OPA/Gatekeeper)
- **Purpose:** Guardrails and compliance automation.
- **Used for:** Enforcing deployment and runtime policies in Kubernetes.

## Suggested Core Stack for LexusNexus

If LexusNexus wants a focused, high-value starting point:
1. **Prometheus + Grafana + Alertmanager** for monitoring/alerting
2. **OpenTelemetry + Jaeger** for tracing
3. **ELK (or Loki stack)** for centralized logs
4. **PagerDuty + Slack** for incident operations
5. **Terraform + Kubernetes + Helm** for infrastructure/platform consistency
6. **GitHub Actions + Argo CD** for CI/CD and GitOps delivery
7. **Sentry + k6** for app reliability and performance readiness

---

If you want, I can also create a second file (`tooling-standards.md`) mapping each tool to:
- owner team,
- alert severity,
- SLO impact,
- deployment environment,
- and operational runbook links.
