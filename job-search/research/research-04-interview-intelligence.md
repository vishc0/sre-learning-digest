# Research Report 04 — Interview Intelligence
## Verbatim Interview Questions, Depth Levels & "What Good Looks Like" by Domain

**Source**: Training_Plan_Master.md Section 1 — Market Intelligence (synthesized from 110-agent research run)
**Date**: June 11, 2026
**Purpose**: Open this file when preparing mock interview answers. These are the actual questions interviewers ask at Staff/Principal SRE level at $180k+ companies.

---

## HOW TO USE THIS DOCUMENT

For each domain:
1. Read the verbatim interview questions — these are the exact phrasings used
2. Note the depth level — "architect" means draw the system; "hands-on" means walk through commands; "internals" means explain the mechanism without looking it up
3. Read "What Good Looks Like" — this is the bar you are aiming for, not the floor
4. Anchor your answer to T-Mobile experience wherever possible (see the STAR anchor column)

---

## DOMAIN A: Kubernetes Internals

### Verbatim Interview Questions
| Type | Question |
|---|---|
| Internals | "Walk me through what happens, component by component, when you run `kubectl apply` on a Deployment." |
| Internals | "How does the kube-scheduler decide which node gets a Pod? What factors does it weight?" |
| Admission Control | "What is the difference between a MutatingAdmissionWebhook and a ValidatingAdmissionWebhook? When would you build a custom one?" |
| Controllers | "If you needed to automate a Day-2 operation (e.g., rotate a secret when it expires), would you write a controller or use an operator framework? Why?" |
| Networking | "Explain how a request from Pod A reaches Pod B in a different namespace. Where does kube-proxy fit in vs. a CNI plugin like Cilium?" |
| Security | "What is the difference between a PodSecurityPolicy (deprecated), PodSecurity admission, and an OPA/Gatekeeper constraint? Why was PSP removed?" |
| Debugging | "A Pod is stuck in `Pending`. Give me your exact troubleshooting sequence — not just the commands, but the mental model." |
| Scale | "You're running 500 microservices on EKS. HPA is configured, but autoscaling is lagging 4 minutes behind traffic spikes. What do you investigate?" |

### Depth Level Expected
- **Architect**: Cluster topology decisions — multi-tenancy models, node pool strategy, cluster autoscaler vs. Karpenter
- **Hands-on debug**: Reading controller logs, `kubectl describe`, event chains, `crictl` for container runtime
- **Internals (explain, not code)**: etcd as source of truth, watch/reconcile loop, leader election, informer cache

### Key Vocabulary
`etcd` · `kube-apiserver` · `controller-manager` · `scheduler` · `kubelet` · `informer` · `reconcile loop` · `watch` · `admission webhook` · `mutating vs. validating` · `CRD` · `operator pattern` · `CNI` · `kube-proxy` · `iptables vs. eBPF dataplane` · `Karpenter` · `cluster autoscaler` · `RBAC` · `ServiceAccount` · `Pod Security Standards` · `OPA Gatekeeper` · `resource quotas` · `LimitRange` · `PriorityClass`

### What "Good" Looks Like at Staff/Principal
- Can draw the full control plane + data plane architecture from memory
- Knows *why* PSP was deprecated (security model was broken, not just "deprecated") and what replaced it
- Designs multi-tenant clusters with namespace isolation, RBAC, and resource quotas
- Understands the watch/reconcile loop deeply enough to explain eventual consistency as a feature
- Treats admission control as the "policy enforcement point" — analogous to a firewall for API objects

### Your T-Mobile STAR Anchor
"At T-Mobile, our EKS cluster runs the notification platform processing 25M messages/day. When we migrated from PCF to Kubernetes, I owned the cluster topology decisions — [expand with specifics]."

---

## DOMAIN B: AWS Services

### Verbatim Interview Questions
| Type | Question |
|---|---|
| Networking | "Explain the difference between a Security Group and an NACL. When would a misconfigured NACL cause intermittent failures that SGs alone wouldn't?" |
| IAM | "What is the difference between an IAM Role, an IAM Policy, and an SCP in AWS Organizations? Which takes precedence?" |
| EKS-Specific | "How do you grant a Kubernetes ServiceAccount access to an S3 bucket without storing AWS credentials in the cluster? Walk through IRSA." |
| Cost/Scale | "Your EKS cluster's data transfer bill tripled. Walk me through how you'd diagnose whether it's cross-AZ traffic, NAT Gateway inefficiency, or application misbehavior." |
| Storage | "You have a stateful workload on EKS that needs persistent storage. Compare EBS CSI driver vs. EFS CSI driver — when is each the right choice?" |
| Observability | "How would you ship container logs from EKS to both CloudWatch and your SIEM (Splunk) without running two separate log forwarders per node?" |
| Security | "What is VPC Flow Logs, what does it NOT capture, and how would you combine it with GuardDuty findings for an incident?" |
| Resilience | "Design a notification platform on AWS that handles 25M messages/day with <99.9% error budget consumption." |

### Depth Level Expected
- **Deep**: EKS (IRSA, node groups vs. Fargate, add-on management), IAM (permission boundaries, IRSA, cross-account roles), VPC (routing, endpoints, PrivateLink), CloudWatch (Container Insights, custom metrics)
- **Working knowledge**: SQS, SNS, Lambda, RDS, ElastiCache, Route53, ACM, Secrets Manager, ECR, GuardDuty, Security Hub, Config
- **Conceptual**: Organizations + SCPs, Control Tower, AWS WAF, Shield, Macie

### Key Vocabulary
`IRSA` · `OIDC provider` · `VPC endpoint` · `PrivateLink` · `NAT Gateway` · `Transit Gateway` · `SCP` · `permission boundary` · `resource-based policy` · `identity-based policy` · `CloudWatch Container Insights` · `ADOT` · `ECR image scanning` · `GuardDuty` · `Security Hub` · `AWS Config rules` · `Karpenter` · `OIDC` · `STS AssumeRole`

### What "Good" Looks Like at Staff/Principal
- Designs AWS architectures with security and cost as first-class constraints
- Can explain IRSA without notes: OIDC trust relationship, ServiceAccount annotation, token projection
- Knows which AWS services have native ADOT/OTel support vs. which need sidecars
- Has a cost-optimization mental model for EKS: spot instance strategy, cross-AZ traffic reduction

### Your T-Mobile STAR Anchor
"The last design I owned: migrating from PCF to EKS on AWS while maintaining 99.99% uptime for 25M daily messages. The IRSA setup for RabbitMQ/Cassandra authentication was [expand]."

---

## DOMAIN C: DevSecOps / Supply Chain Security

### Verbatim Interview Questions
| Type | Question |
|---|---|
| SBOM | "What is an SBOM and why did the White House EO 14028 make it a federal requirement? SPDX or CycloneDX — why?" |
| SCA | "Walk me through how SCA differs from SAST. Which vulnerabilities does SCA catch that SAST misses?" |
| Sigstore | "How does Cosign signing of a container image protect against a supply chain attack? Keyless vs. key-based signing?" |
| OWASP | "OWASP Top 10:2025 now lists A03 as supply chain. How would you redesign a CI/CD pipeline to address the top 5 OWASP risks in your build?" |
| Policy-as-Code | "How is OPA Rego different from Kubernetes RBAC? Give me a scenario where RBAC alone is insufficient." |
| Shift-Left | "Your developers push to a feature branch. Design a shift-left security gate that catches secrets, vulnerable dependencies, and misconfigured IaC before the PR is merged." |
| Runtime | "What is the difference between Falco and Sysdig for runtime security? How does eBPF improve runtime monitoring vs. ptrace-based approaches?" |
| Secrets | "A secret rotated in Vault. How do you ensure all 200 running pods get the new secret without a rolling restart causing a 5-minute outage?" |

### Depth Level Expected
- **Architect**: Full DevSecOps pipeline with gates, SBOM, SCA, SAST, container scanning, artifact signing, policy enforcement
- **Hands-on**: Write OPA Rego rules; integrate Trivy into GitHub Actions; use `cosign` CLI; generate SBOM with Syft
- **Conceptual to working**: OWASP Top 10:2025, zero-trust, CSPM, DAST

### Key Vocabulary
`SBOM` · `SPDX` · `CycloneDX` · `Syft` · `Grype` · `Trivy` · `SCA` · `SAST` · `DAST` · `Cosign` · `Sigstore` · `Rekor` · `Fulcio` · `keyless signing` · `supply chain attack` · `SLSA framework` · `SLSA level 2/3` · `OPA` · `Rego` · `Gatekeeper` · `Conftest` · `shift-left` · `OWASP Top 10:2025` · `zero-trust` · `CSPM` · `Falco` · `eBPF` · `runtime security` · `secrets rotation` · `Vault Agent` · `External Secrets Operator` · `provenance attestation`

### What "Good" Looks Like at Staff/Principal
- Can design a complete secure software supply chain: developer commit → signed, scanned, attested artifact in production
- Knows SLSA framework levels; can map a pipeline to SLSA level 2 vs. 3
- Can write a basic OPA Rego deny policy without a reference
- Understands SolarWinds-style attack vectors; can explain how SBOM + signing would have mitigated it
- Treats secrets management as an architectural concern, not a DevOps afterthought

### Your T-Mobile STAR Anchor
"My delivery governance program at T-Mobile — managing 42 downstream integrations and six zero-downtime migrations — is exactly the CI/CD governance foundation I would extend with security gates. Specifically [expand with: what SBOM strategy you would add, why it matters for T-Mobile's compliance posture]."

---

## DOMAIN D: Observability / Telemetry (MELT, OpenTelemetry, SLO/Error Budgets)

### Verbatim Interview Questions
| Type | Question |
|---|---|
| MELT | "Explain the MELT framework. Where does distributed tracing fit — is it events, logs, or something else?" |
| OTel | "How does OpenTelemetry differ from OpenTracing and OpenCensus? Why did the CNCF consolidate them?" |
| SLOs | "Your SLO is 99.9% success rate over 28 days. You have consumed 80% of your error budget in 10 days. Walk me through your decision tree." |
| Cardinality | "What is metrics cardinality and why does it cause cost explosions in Prometheus/Datadog? Give a real example of a high-cardinality mistake." |
| Tracing | "What is the difference between head-based vs. tail-based sampling? When is tail-based essential?" |
| eBPF | "How can eBPF enable zero-instrumentation observability? What does Cilium Hubble provide that traditional metrics don't?" |
| Alerting | "What is the difference between a burn rate alert and a static threshold alert? Why do burn rate alerts have lower false-positive rates?" |
| Splunk→OTel | "Your team uses Splunk HEC today. How would you migrate to OTel Collector without a 'rip and replace' while maintaining SLA?" |

### Depth Level Expected
- **Architect**: Observability platform design — collector topology, sampling strategies, retention tiers, cost vs. coverage tradeoffs
- **Hands-on**: Write SLO YAML with `sloth` or `pyrra`, configure OTel Collector pipelines, write Prometheus recording rules
- **Expert (already strong)**: Splunk, Grafana, AppDynamics

### Key Vocabulary (Your Translation Table)
| Your Current Language | Market Language |
|---|---|
| MART framework | MELT framework / 3-pillar observability |
| Splunk HEC | OTel Collector with Splunk HEC exporter |
| AppDynamics traces | Distributed tracing / OpenTelemetry traces |
| Splunk MLTK anomaly detection | ML-based alerting / AIOps |
| Alert events | Events (E in MELT) / deployment markers |

**Full vocabulary**: `MELT` · `metrics/events/logs/traces` · `OpenTelemetry` · `OTLP` · `OTel Collector` · `auto-instrumentation` · `trace context propagation` · `W3C TraceContext` · `span` · `exemplar` · `burn rate` · `error budget` · `SLO/SLI/SLA` · `multi-window multi-burn-rate alert` · `cardinality explosion` · `head-based sampling` · `tail-based sampling` · `recording rules` · `Grafana Loki` · `eBPF` · `Cilium Hubble` · `sloth` · `pyrra`

### The Burn Rate Math (Know This Cold)
- **Error budget for 99.9% SLO over 28 days** = 0.1% × 28 × 24 × 60 = **40.3 minutes** of allowed failure
- **Burn rate 14x** = exhausting 28-day budget in 2 days → **fast burn alert: 1h window, >14x**
- **Burn rate 6x** = exhausting budget in ~4.7 days → **slow burn alert: 6h window, >6x**
- These two alerts together cover both sharp incidents AND slow degradation

### What "Good" Looks Like at Staff/Principal
- Articulates MELT vs. 3-pillar as complementary, not competing
- Has designed SLO/error budget policies that changed team behavior
- Knows the multi-window burn rate math without looking it up
- Can design an OTel Collector pipeline with fan-out: same data to Splunk HEC AND Prometheus

### Your T-Mobile STAR Anchor
"We maintain 99.99% uptime across 25M messages/day. My MART framework — the Splunk-based monitoring, alerting, reporting, and troubleshooting system I built — is my implementation of the MELT model. Specifically, the burn rate calculation that drives our SLO governance shows [expand with actual numbers if safe to share]."

---

## DOMAIN E: IaC (Terraform, State, Modules, GitOps)

### Verbatim Interview Questions
| Type | Question |
|---|---|
| State | "What is Terraform state and why is it dangerous to store in Git? What happens if two engineers run `terraform apply` simultaneously?" |
| Drift | "Production was manually changed by on-call during an incident. How do you detect the drift, and reconcile without causing a second incident?" |
| Modules | "How do you design a Terraform module that 10 different teams can use for EKS clusters with different configurations, without code duplication?" |
| GitOps | "Explain push model vs. pull model GitOps. Why is ArgoCD a pull-model, and why does that matter for security?" |
| Testing | "How do you test Terraform code before merging? What tools, what layers of testing?" |
| Destruction | "A `terraform destroy` ran in production accidentally. How do you prevent this architecturally, not just with process?" |
| Import | "You have 50 AWS resources created manually. How do you bring them under Terraform management without rebuilding them?" |

### Key Vocabulary
`remote state` · `S3 backend` · `DynamoDB state locking` · `state drift` · `terraform import` · `terraform refresh` · `module composition` · `terragrunt` · `workspace` · `resource targeting` · `sentinel policies` · `OPA conftest` · `GitOps` · `ArgoCD` · `Flux` · `ApplicationSet` · `pull model` · `reconciliation loop` · `kustomize` · `Helm` · `drift detection`

### What "Good" Looks Like at Staff/Principal
- Designed a module library that reduced team toil for EKS/VPC/RDS provisioning
- Can explain state locking and a real race condition scenario without notes
- Knows ArgoCD pull-model security advantage: no CI system needs cluster credentials
- Has a policy-as-code layer (Conftest or Sentinel) on top of Terraform for compliance

### Your T-Mobile STAR Anchor
"My incident management experience — handling manual changes during outages, then reconciling them into the config baseline — is exactly the Terraform drift reconciliation problem. I've done this manually; Terraform makes it systematic."

---

## DOMAIN F: CI/CD Pipeline Security

### Verbatim Interview Questions
| Type | Question |
|---|---|
| Secrets | "A developer committed an AWS secret key to a public GitHub repo. Walk through your immediate response AND the architectural change to prevent recurrence." |
| Pipeline Security | "What is a poisoned pipeline execution attack (PPE)? How do you protect against it in GitHub Actions?" |
| Gate Design | "Design a quality gate strategy for a pipeline that builds a Java microservice. What checks run on every commit, every PR, and every merge to main?" |
| Artifact Integrity | "How do you ensure the Docker image deployed to production is exactly the image that passed your security scan?" |
| OIDC | "Why is using OIDC federation between GitHub Actions and AWS better than storing an AWS_ACCESS_KEY_ID as a GitHub secret?" |
| Compliance | "Your pipeline must produce a compliance artifact proving every deployment was code-reviewed, scanned, and approved. Design the audit trail." |

### Key Vocabulary
`GitHub Actions` · `OIDC federation` · `short-lived credentials` · `PPE (poisoned pipeline execution)` · `secrets scanning` · `gitleaks` · `trufflehog` · `Semgrep` · `SCA` · `Dependabot` · `Trivy` · `Cosign` · `artifact signing` · `digest pinning` · `SLSA` · `provenance` · `branch protection rules` · `required status checks` · `CODEOWNERS` · `dependency confusion` · `supply chain`

### Real Supply Chain Attacks to Know (for name-dropping)
1. **SolarWinds (2020)**: Build system compromise; malicious code injected into signed updates. SBOM + build provenance would have enabled faster detection.
2. **XZ Utils (2024)**: Social engineering into an open source project; backdoor in a widely-used compression library. SCA scanning catches the compromised version.
3. **Log4Shell (2021)**: Critical CVE in a transitive dependency. SCA + SBOM would have identified every affected service in minutes.

---

## DOMAIN G: Platform Engineering

### Verbatim Interview Questions
| Type | Question |
|---|---|
| IDP Philosophy | "What is an Internal Developer Platform? How is it different from a CI/CD system or a Kubernetes cluster?" |
| Golden Paths | "What is a 'golden path' and why does it reduce cognitive load without restricting flexibility?" |
| Self-Service | "Your 50 developer teams each need to provision a new microservice with its own K8s namespace, ECR repo, GitHub repo, and dashboards. How do you build self-service provisioning?" |
| Metrics | "How do you measure the success of a platform team? What KPIs?" |
| Toil Reduction | "Describe a time you reduced developer toil by building a platform capability." |

### Key Vocabulary
`Internal Developer Platform` · `IDP` · `golden path` · `paved road` · `cognitive load` · `Backstage` · `service catalog` · `software templates` · `scaffolding` · `Crossplane` · `DORA metrics` · `deployment frequency` · `lead time for changes` · `MTTR` · `change failure rate` · `developer experience (DevEx)` · `platform as a product` · `Team Topologies` · `stream-aligned team` · `enabling team`

### DORA Four Keys (Memorize These)
1. **Deployment Frequency** — how often you deploy to production (Elite: multiple times/day)
2. **Lead Time for Changes** — commit to production (Elite: <1 hour)
3. **Change Failure Rate** — % of deployments causing incidents (Elite: 0–15%)
4. **Mean Time to Restore (MTTR)** — recovery speed (Elite: <1 hour)

### Your T-Mobile STAR Anchor
"Managing a 15-person SRE team responsible for 42 downstream integrations is platform engineering. I own the internal tooling, the deployment patterns, the observability standards — that's a platform team. The vocabulary is new; the work is what I've been doing."

---

## DOMAIN H: Incident Command & Reliability at Scale

### Verbatim Interview Questions
| Type | Question |
|---|---|
| Command Structure | "Walk through your incident command structure. Who is the IC, scribe, comms lead? How do you hand off the IC role during a 6-hour incident?" |
| Postmortem | "Describe your blameless postmortem process. What makes it 'blameless' in practice, not just theory?" |
| MTTR/MTTD | "Your P1 MTTD is 45 minutes. Give me a systematic approach to getting it under 10 minutes without more headcount." |
| Chaos Engineering | "What is chaos engineering and how is it different from load testing? Your philosophy on chaos in production?" |
| SLO Governance | "Who owns the SLO for a service — SRE, product, or both? How do you enforce error budget policies when product wants to override?" |
| Toil Budget | "Google SRE recommends keeping toil below 50% of SRE time. How do you measure toil? What do you do when you exceed the budget?" |

### Key Vocabulary
`incident command` · `IC` · `scribe` · `comms lead` · `escalation matrix` · `P1/P2/P3` · `blameless postmortem` · `5 Whys` · `MTTD` · `MTTR` · `MTTI` · `chaos engineering` · `game day` · `failure injection` · `LitmusChaos` · `Gremlin` · `SLO` · `error budget` · `burn rate` · `toil` · `toil budget` · `runbook` · `playbook` · `DORA change failure rate`

### What "Good" Looks Like at Staff/Principal
This is your strongest domain. Your advantage:
- 99.99% uptime over 36 months on a 25M msg/day platform → *cite this in every answer*
- Zero Sev1 over 36 months → *this is exceptional; lead with it*
- Six zero-downtime migrations → *this demonstrates chaos engineering done right in practice*
- Structured postmortem culture → *frame this as SRE book-aligned*

**The gap**: You need chaos engineering vocabulary (LitmusChaos, game days, hypothesis-driven experiments) and DORA metrics numbers from your own team.

---

## CROSS-DOMAIN: STAR ANCHOR MAP

| Domain | T-Mobile Anchor | How to Start the Answer |
|---|---|---|
| Kubernetes | EKS cluster for notification platform | "At T-Mobile, our EKS cluster runs 25M messages/day across SMS, email, and push..." |
| AWS | VM → PCF → K8s → AWS migration | "When I led the migration from PCF to EKS on AWS, the key design decision was..." |
| DevSecOps | Delivery governance on 42 downstream integrations | "My CI/CD governance program at T-Mobile manages 42 downstream systems. Adding security gates means..." |
| Observability | Splunk MART framework, MLTK anomaly detection | "I built what we call MART — Monitoring, Alerting, Reporting, Troubleshooting — using Splunk. In MELT terms, that's..." |
| IaC | Manual incident config changes → need reconciliation | "Managing infrastructure state during incidents — that's the Terraform drift problem, and I've done it manually for years..." |
| CI/CD Security | Release orchestration, delivery governance | "My delivery governance covers the audit trail side. What I'm adding is the security gate layer: SBOM, SCA, artifact signing..." |
| Platform Eng | 15-person SRE team, internal tooling | "Running a platform team of 15, I own the developer-facing tools, the deployment patterns, the monitoring standards — that's an IDP..." |
| Incident Command | 99.99% uptime, zero Sev1 in 36 months | "In 36 months, zero Sev1s on a platform processing 25M messages/day. Here's how our incident command structure works..." |

---

*Source: Training_Plan_Master.md Section 1 (1,939 lines) | June 11, 2026*
*Use alongside `research-01-job-market-intelligence.md` for vocabulary verification*
