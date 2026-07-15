# Staff/Principal SRE & Senior DevSecOps — Training Program Master File
**For:** Vishweshwar Chippa | **Date:** June 11, 2026 | **Target:** $180k–$280k+ TC Roles

---

## TABLE OF CONTENTS

1. [Market Intelligence — What High-Comp Roles Actually Require](#section-1)
2. [Gap Analysis — Vishweshwar vs. Market Requirements](#section-2)
3. [30-Day Training Plan (Hybrid Agile-Waterfall Sprints)](#section-3)
4. [Certification Roadmap](#section-4)
5. [LinkedIn Optimization Strategy](#section-5)
6. [Content Creation Agent Framework](#section-6)

---

<a name="section-1"></a>
## SECTION 1: MARKET INTELLIGENCE — What High-Comp Roles Actually Require

> Reading guide: Each domain lists what interviewers actually ask, the expected depth level, vocabulary to deploy, and what "good" looks like at Staff/Principal level.

---

### Domain A: Kubernetes (Internals, Not Just Operations)

#### Interview Question Patterns

| Question Type | Verbatim Example |
|---|---|
| Internals | "Walk me through what happens, component by component, when you run `kubectl apply` on a Deployment." |
| Internals | "How does the kube-scheduler decide which node gets a Pod? What factors does it weight?" |
| Admission Control | "What is the difference between a MutatingAdmissionWebhook and a ValidatingAdmissionWebhook? When would you build a custom one?" |
| Controllers | "If you needed to automate a Day-2 operation (e.g., rotate a secret when it expires), would you write a controller or use an operator framework? Why?" |
| Networking | "Explain how a request from Pod A reaches Pod B in a different namespace. Where does kube-proxy fit in vs. a CNI plugin like Cilium?" |
| Security | "What is the difference between a PodSecurityPolicy (deprecated), PodSecurity admission, and an OPA/Gatekeeper constraint? Why was PSP removed?" |
| Debugging | "A Pod is stuck in `Pending`. Give me your exact troubleshooting sequence — not just the commands, but the mental model." |
| Scale | "You're running 500 microservices on EKS. HPA is configured, but autoscaling is lagging 4 minutes behind traffic spikes. What do you investigate?" |

#### Depth Level Expected

- **Architect/Design**: Cluster topology decisions (multi-tenancy models, node pool strategy, cluster autoscaler vs. Karpenter)
- **Hands-on Debug**: Reading controller logs, using `kubectl describe`, event chains, `crictl` for container runtime
- **Internals (explain, not necessarily code)**: etcd as source of truth, watch/reconcile loop, leader election, informer cache

#### Keywords/Vocabulary

`etcd`, `kube-apiserver`, `controller-manager`, `scheduler`, `kubelet`, `informer`, `reconcile loop`, `watch`, `admission webhook`, `mutating vs. validating`, `CRD`, `operator pattern`, `CNI`, `kube-proxy`, `iptables vs. eBPF dataplane`, `Karpenter`, `cluster autoscaler`, `RBAC`, `ServiceAccount`, `Pod Security Standards`, `OPA Gatekeeper`, `resource quotas`, `LimitRange`, `PriorityClass`

#### What "Good" Looks Like at Staff/Principal

- Can draw the full control plane + data plane architecture from memory
- Knows *why* PSP was deprecated and what replaced it without looking it up
- Can design a multi-tenant cluster with namespace isolation, RBAC, and resource quotas for a platform team
- Understands the watch/reconcile loop deeply enough to explain why eventual consistency is a feature, not a bug
- Has a mental model for admission control as the cluster's "policy enforcement point" — analogous to a network firewall but for API objects

---

### Domain B: AWS Services (Which Ones, At What Depth)

#### Interview Question Patterns

| Question Type | Verbatim Example |
|---|---|
| Networking | "Explain the difference between a Security Group and an NACL. When would a misconfigured NACL cause intermittent failures that SGs alone wouldn't?" |
| IAM | "What is the difference between an IAM Role, an IAM Policy, and an SCP (Service Control Policy) in AWS Organizations? Which takes precedence?" |
| EKS-Specific | "How do you grant a Kubernetes ServiceAccount access to an S3 bucket without storing AWS credentials in the cluster? Walk through IRSA." |
| Cost/Scale | "Your EKS cluster's data transfer bill tripled. Walk me through how you'd diagnose whether it's cross-AZ traffic, NAT Gateway inefficiency, or application misbehavior." |
| Storage | "You have a stateful workload on EKS that needs persistent storage. Compare EBS CSI driver vs. EFS CSI driver — when is each the right choice?" |
| Observability | "How would you ship container logs from EKS to both CloudWatch and your SIEM (Splunk) without running two separate log forwarders per node?" |
| Security | "What is VPC Flow Logs, what does it NOT capture, and how would you combine it with GuardDuty findings for an incident?" |
| Resilience | "Design a notification platform on AWS that handles 25M messages/day with <99.9% error budget consumption. What services, what failure modes?" |

#### Depth Level Expected

- **Deep**: EKS (IRSA, node groups vs. Fargate, add-on management), IAM (permission boundaries, IRSA, cross-account roles), VPC (routing, endpoints, PrivateLink), CloudWatch (Container Insights, custom metrics), S3 (lifecycle, encryption, bucket policies)
- **Working knowledge**: SQS, SNS, Lambda, RDS, ElastiCache, Route53, ACM, Secrets Manager, Parameter Store, ECR, GuardDuty, Security Hub, Config
- **Conceptual**: Organizations + SCPs, Control Tower, AWS WAF, Shield, Macie

#### Keywords/Vocabulary

`IRSA`, `OIDC provider`, `VPC endpoint`, `PrivateLink`, `NAT Gateway`, `Transit Gateway`, `SCP`, `permission boundary`, `resource-based policy`, `identity-based policy`, `CloudWatch Container Insights`, `OpenTelemetry Collector`, `ADOT`, `ECR image scanning`, `GuardDuty`, `Security Hub`, `AWS Config rules`, `Karpenter`, `Node termination handler`, `Cluster Autoscaler`, `OIDC`, `STS AssumeRole`

#### What "Good" Looks Like at Staff/Principal

- Designs AWS architectures with security and cost as first-class constraints, not afterthoughts
- Can explain IRSA without notes: the OIDC trust relationship, the ServiceAccount annotation, the token projection
- Knows which AWS services have native OpenTelemetry/ADOT support vs. which need sidecars
- Has a cost-optimization mental model for EKS: spot instance strategy, right-sizing, cross-AZ traffic reduction

---

### Domain C: DevSecOps / Supply Chain Security

#### Interview Question Patterns

| Question Type | Verbatim Example |
|---|---|
| SBOM | "What is an SBOM and why did the White House EO 14028 make it a federal requirement? What format would you use — SPDX or CycloneDX — and why?" |
| SCA | "Walk me through how a Software Composition Analysis scan differs from SAST. Which vulnerabilities does SCA catch that SAST misses?" |
| Sigstore | "How does Cosign signing of a container image protect against a supply chain attack? What is the difference between keyless signing and key-based signing?" |
| OWASP | "OWASP Top 10:2025 now lists A03 as supply chain/injection. How would you redesign a CI/CD pipeline to address the top 5 OWASP risks in your build?" |
| Policy-as-Code | "How is OPA Rego different from Kubernetes RBAC? Give me a scenario where RBAC alone is insufficient and you'd need OPA." |
| Shift-Left | "Your developers push directly to a feature branch. Design a shift-left security gate that catches secrets, vulnerable dependencies, and misconfigured IaC *before* the PR is merged." |
| Runtime | "What is the difference between Falco and Sysdig for runtime security? How does eBPF improve runtime security monitoring vs. ptrace-based approaches?" |
| Secrets | "A secret rotated in Vault. How do you ensure all 200 running pods get the new secret without a rolling restart causing a 5-minute outage?" |

#### Depth Level Expected

- **Architect/Design**: Full DevSecOps pipeline with gates, SBOM generation, SCA, SAST, container scanning, artifact signing, policy-as-code enforcement
- **Hands-on**: Writing OPA Rego rules, integrating Trivy or Grype into a GitHub Actions pipeline, using `cosign` CLI, generating SBOM with Syft
- **Conceptual-to-Working**: OWASP Top 10:2025, zero-trust principles, CSPM, DAST

#### Keywords/Vocabulary

`SBOM`, `SPDX`, `CycloneDX`, `Syft`, `Grype`, `Trivy`, `SCA`, `SAST`, `DAST`, `Cosign`, `Sigstore`, `Rekor`, `Fulcio`, `keyless signing`, `supply chain attack`, `SLSA framework`, `SLSA level 2/3`, `OPA`, `Rego`, `Gatekeeper`, `Conftest`, `shift-left`, `OWASP Top 10:2025`, `zero-trust`, `CSPM`, `Falco`, `eBPF`, `runtime security`, `secrets rotation`, `Vault Agent`, `External Secrets Operator`, `provenance attestation`

#### What "Good" Looks Like at Staff/Principal

- Can design a complete secure software supply chain: from developer commit to signed, scanned, attested artifact in production
- Knows SLSA framework levels and can map their current pipeline to SLSA level 2 vs. level 3
- Can write a basic OPA Rego policy without a reference (e.g., deny images from untrusted registries)
- Understands the attack vectors in SolarWinds-style supply chain attacks and can explain how SBOM + artifact signing would have mitigated it
- Treats secrets management as an architectural concern, not a DevOps afterthought

---

### Domain D: Observability / Telemetry (MELT, OpenTelemetry, SLO/Error Budgets)

#### Interview Question Patterns

| Question Type | Verbatim Example |
|---|---|
| MELT | "Explain the MELT framework. Where does distributed tracing fit — is it events, logs, or something else?" |
| OTel | "How does OpenTelemetry differ from OpenTracing and OpenCensus? Why did the CNCF consolidate them?" |
| SLOs | "Your SLO is 99.9% success rate over 28 days. You have consumed 80% of your error budget in 10 days. Walk me through your decision tree." |
| Cardinality | "What is metrics cardinality and why does it cause cost explosions in Prometheus/Datadog? Give a real example of a high-cardinality mistake." |
| Tracing | "What is the difference between sampling strategies in distributed tracing — head-based vs. tail-based sampling? When is tail-based essential?" |
| eBPF | "How can eBPF enable zero-instrumentation observability? What does Cilium Hubble provide that traditional metrics don't?" |
| Alerting | "What is the difference between a burn rate alert and a static threshold alert? Why do burn rate alerts have lower false-positive rates?" |
| Splunk-to-OTel | "Your team uses Splunk HEC today. How would you migrate to OpenTelemetry Collector without a 'rip and replace' and maintain SLA during the transition?" |

#### Depth Level Expected

- **Architect/Design**: Observability platform design (collector topology, sampling strategies, retention tiers, cost vs. coverage tradeoffs)
- **Hands-on**: Writing SLO YAML with `sloth` or `pyrra`, configuring OTel Collector pipelines, writing Prometheus recording rules, building Grafana dashboards from OTel data
- **Conceptual-to-Expert**: Splunk (already expert), Grafana, Prometheus, Jaeger/Tempo

#### Keywords/Vocabulary

`MELT`, `metrics/events/logs/traces`, `OpenTelemetry`, `OTLP`, `OTel Collector`, `instrumentation library`, `auto-instrumentation`, `trace context propagation`, `W3C TraceContext`, `span`, `exemplar`, `burn rate`, `error budget`, `SLO`, `SLI`, `SLA`, `multi-window multi-burn-rate alert`, `cardinality explosion`, `head-based sampling`, `tail-based sampling`, `Prometheus`, `remote_write`, `recording rules`, `alerting rules`, `Grafana Loki`, `eBPF`, `Cilium Hubble`, `sloth`, `pyrra`

#### What "Good" Looks Like at Staff/Principal

- Can articulate MELT vs. 3-pillar model and explain they are complementary frameworks, not competing
- Has designed SLO/error budget policies that changed team behavior (burn rate alerts that triggered freeze periods)
- Knows the math behind multi-window burn rate alerts (1h window + 6h window, fast vs. slow burn)
- Can design an OTel Collector pipeline with fan-out: same telemetry to Splunk HEC AND Prometheus remote_write
- Understands metrics cardinality as an economics problem, not just a technical one

---

### Domain E: IaC (Terraform, State, Modules, GitOps)

#### Interview Question Patterns

| Question Type | Verbatim Example |
|---|---|
| State | "What is Terraform state and why is it dangerous to store in a Git repository? What happens if two engineers run `terraform apply` simultaneously?" |
| Drift | "Production was manually changed by an on-call engineer during an incident. How do you detect the drift, and what is your process to reconcile without causing a second incident?" |
| Modules | "How do you design a Terraform module that 10 different teams can use for EKS clusters with different configurations, without code duplication?" |
| GitOps | "Explain the difference between GitOps (push model vs. pull model). Why is ArgoCD a pull-model, and why does that matter for security?" |
| Workspaces | "When would you use Terraform workspaces vs. separate state files per environment? What are the risks of workspaces for production vs. staging isolation?" |
| Testing | "How do you test Terraform code before merging? What tools and what layers of testing?" |
| Destruction | "A `terraform destroy` ran in production accidentally. How do you prevent this architecturally, not just with process?" |
| Import | "You have 50 AWS resources created manually. How do you bring them under Terraform management without rebuilding them?" |

#### Depth Level Expected

- **Architect/Design**: Module registry design, multi-account/multi-region state organization, remote state + `terraform_remote_state`
- **Hands-on**: Writing modules, state locking with DynamoDB, `terraform import`, `terraform plan` and diff reading, `terragrunt` patterns
- **GitOps**: ArgoCD or Flux architecture, ApplicationSet, image update automation

#### Keywords/Vocabulary

`remote state`, `S3 backend`, `DynamoDB state locking`, `state drift`, `terraform import`, `terraform refresh`, `module composition`, `registry`, `terragrunt`, `workspace`, `resource targeting`, `sentinel policies`, `OPA conftest`, `GitOps`, `ArgoCD`, `Flux`, `ApplicationSet`, `pull model`, `reconciliation loop`, `kustomize`, `Helm`, `CDKTF`, `Pulumi`, `drift detection`

#### What "Good" Looks Like at Staff/Principal

- Has designed a module library that reduced team toil by standardizing EKS, VPC, or RDS provisioning
- Can explain the state locking mechanism and a real race condition scenario without notes
- Knows the ArgoCD pull-model security advantage: no CI system needs cluster credentials
- Has a policy-as-code layer (Sentinel or Conftest) on top of Terraform to enforce compliance

---

### Domain F: CI/CD Pipeline Security

#### Interview Question Patterns

| Question Type | Verbatim Example |
|---|---|
| Secrets | "A developer accidentally committed an AWS secret key to a public GitHub repo. Walk me through your immediate response AND the architectural change to prevent recurrence." |
| Pipeline Security | "What is a poisoned pipeline execution attack (PPE)? How do you protect against it in GitHub Actions?" |
| Gate Design | "Design a quality gate strategy for a pipeline that builds a Java microservice. What checks run on every commit, every PR, and every merge to main?" |
| Artifact Integrity | "How do you ensure that the Docker image deployed to production is exactly the image that passed your security scan — not a different version?" |
| OIDC | "Why is using OIDC federation between GitHub Actions and AWS better than storing an AWS_ACCESS_KEY_ID as a GitHub secret?" |
| Dependencies | "How would you detect if a transitive dependency in your `pom.xml` or `requirements.txt` was compromised (e.g., a typosquatting attack)?" |
| Runner Security | "What are the security risks of self-hosted GitHub Actions runners vs. GitHub-hosted runners? When is each appropriate?" |
| Compliance | "Your pipeline must produce a compliance artifact proving that every deployment was code-reviewed, scanned, and approved. Design the audit trail." |

#### Depth Level Expected

- **Architect/Design**: End-to-end secure pipeline with secrets scanning, SAST, SCA, container scanning, signing, policy gates, audit logging
- **Hands-on**: GitHub Actions YAML authoring, Trivy integration, Cosign signing in pipeline, OIDC trust with AWS
- **Conceptual**: PPE attacks, supply chain attack models (SLSA), dependency confusion attacks

#### Keywords/Vocabulary

`GitHub Actions`, `OIDC federation`, `short-lived credentials`, `PPE (poisoned pipeline execution)`, `secrets scanning`, `gitleaks`, `trufflehog`, `SAST`, `Semgrep`, `SCA`, `Dependabot`, `Snyk`, `Trivy`, `Grype`, `container scanning`, `Cosign`, `artifact signing`, `digest pinning`, `SLSA`, `provenance`, `pipeline as code`, `branch protection rules`, `required status checks`, `CODEOWNERS`, `dependency confusion`, `typosquatting`, `supply chain`, `audit log`

#### What "Good" Looks Like at Staff/Principal

- Can name at least 3 real supply chain attacks (SolarWinds, XZ Utils, Log4Shell) and explain the pipeline controls that would have caught each
- Designs pipelines with "fail open vs. fail closed" intentionality — knowing when a scan failure should block vs. alert
- Understands OIDC federation deeply enough to write the GitHub Actions YAML trust policy without looking it up
- Has an opinion on centralized vs. federated pipeline security governance

---

### Domain G: Platform Engineering (Internal Developer Platforms, Golden Paths)

#### Interview Question Patterns

| Question Type | Verbatim Example |
|---|---|
| IDP Philosophy | "What is an Internal Developer Platform? How is it different from a CI/CD system or a Kubernetes cluster?" |
| Golden Paths | "What is a 'golden path' and why does it reduce cognitive load for developers without restricting flexibility?" |
| Backstage | "What problem does Backstage solve that a wiki or Confluence does not? What is the service catalog model?" |
| Self-Service | "Your 50 developer teams each need to provision a new microservice with its own Kubernetes namespace, ECR repo, GitHub repo, and monitoring dashboards. How do you build self-service provisioning?" |
| Paved Roads | "How do you balance standardization (paved roads) with the need for teams to diverge when their use case genuinely requires it?" |
| Metrics | "How do you measure the success of a platform team? What KPIs would you track for developer productivity?" |
| Toil Reduction | "Describe a time when you reduced developer toil by building a platform capability. What was the before/after measurement?" |
| Backstage Plugins | "How would you build a Backstage plugin that shows real-time SLO status for every service in the catalog?" |

#### Depth Level Expected

- **Architect/Design**: Platform as a product, IDP layers (infrastructure layer, orchestration layer, developer interface layer), self-service provisioning patterns
- **Conceptual-to-Working**: Backstage, Port, Humanitec, Crossplane for infrastructure abstraction
- **Metrics**: DORA metrics (deployment frequency, lead time, MTTR, change failure rate), SPACE framework

#### Keywords/Vocabulary

`Internal Developer Platform`, `IDP`, `golden path`, `paved road`, `cognitive load`, `Backstage`, `service catalog`, `software templates`, `scaffolding`, `Crossplane`, `Port`, `Humanitec`, `self-service provisioning`, `DORA metrics`, `deployment frequency`, `lead time for changes`, `MTTR`, `change failure rate`, `developer experience (DevEx)`, `platform as a product`, `platform team topology`, `Team Topologies`, `stream-aligned team`, `enabling team`, `platform team`

#### What "Good" Looks Like at Staff/Principal

- Frames platform engineering as a product problem, not an infrastructure problem
- Knows DORA metrics by heart and can cite their team's current baselines
- Has a clear opinion on the "paved road" philosophy: you build the fast lane, you don't mandate it
- Can design a Backstage service catalog integration from scratch, including the catalog-info.yaml schema

---

### Domain H: Incident Command & Reliability at Scale

#### Interview Question Patterns

| Question Type | Verbatim Example |
|---|---|
| Command Structure | "Walk me through your incident command structure. Who is the IC, who is the scribe, who is the comms lead? How do you hand off the IC role during a 6-hour incident?" |
| Postmortem | "Describe your blameless postmortem process. What makes a postmortem 'blameless' in practice, not just in theory?" |
| MTTR/MTTD | "Your MTTD for a P1 is 45 minutes. Walk me through a systematic approach to getting it under 10 minutes without more headcount." |
| Chaos Engineering | "What is chaos engineering and how is it different from load testing? What is your philosophy on running chaos experiments in production?" |
| Game Days | "How do you design a game day? Walk me through the last one you ran — scenario, participants, outcomes." |
| SLO Governance | "Who owns the SLO for a service — the SRE team, the product team, or both? How do you enforce error budget policies when a product team wants to override them?" |
| Toil Budget | "Google SRE recommends keeping toil below 50% of an SRE's time. How do you measure toil, and what do you do when you exceed the budget?" |
| Runbooks | "What is the difference between a runbook and a playbook? What makes a runbook actually usable during a P1 at 3am?" |

#### Depth Level Expected

- **Architect/Design**: Reliability program design (SLO framework, toil measurement, chaos engineering program, postmortem process)
- **Hands-on Leadership**: Incident command execution, escalation paths, war room facilitation, postmortem writing
- **Frameworks**: ICS (Incident Command System), Google SRE book principles, chaos engineering (Chaos Monkey, Gremlin, LitmusChaos)

#### Keywords/Vocabulary

`incident command`, `IC`, `scribe`, `comms lead`, `escalation matrix`, `P1/P2/P3`, `war room`, `blameless postmortem`, `5 Whys`, `action items`, `MTTD`, `MTTR`, `MTTI`, `chaos engineering`, `game day`, `failure injection`, `LitmusChaos`, `Gremlin`, `SLO`, `error budget`, `burn rate`, `toil`, `toil budget`, `runbook`, `playbook`, `on-call rotation`, `escalation`, `SLA breach`, `incident retrospective`, `DORA change failure rate`

#### What "Good" Looks Like at Staff/Principal

- Has a documented incident command model they've refined from real incidents, not just theory
- Can cite specific MTTD/MTTR improvements they drove with data (e.g., "reduced MTTD from 45m to 8m by implementing synthetic monitoring on the checkout flow")
- Treats the postmortem as a learning system with measurable follow-through, not a blame-avoidance ritual
- Has run chaos experiments and can articulate the hypothesis → experiment → learning cycle
- Owns SLO governance as a negotiation between reliability and product velocity

---

<a name="section-2"></a>
## SECTION 2: GAP ANALYSIS — Vishweshwar vs. Market Requirements

> Evidence basis: Resume content, CLAUDE.md skill inventory, and direct statements from the prompt about weak areas.

---

| Domain | What He Demonstrated | What Market Requires | Gap Severity | Bridge from Existing Experience |
|---|---|---|---|---|
| A. Kubernetes Internals | EKS operational use, deployment management, team leadership on K8s-hosted 25M msg/day platform | Control plane internals, admission webhooks, custom controllers, scheduler deep-dives | **MODERATE** | Operational depth on EKS gives intuition for scheduler behavior; needs to add vocabulary layer + specific internals |
| B. AWS Services | EKS, S3 (inferred), CloudWatch (inferred), IAM operational use | IRSA deep dive, multi-account IAM, VPC internals, GuardDuty/Security Hub, cost architecture | **MODERATE** | T-Mobile EKS work provides foundation; needs IRSA, SCPs, PrivateLink — gaps are breadth not fundamentals |
| C. DevSecOps / Supply Chain | Vault/CyberArk operational, CI/CD delivery governance, release orchestration | SBOM generation, SCA, SAST integration, Cosign/Sigstore, OPA Rego, SLSA framework | **CRITICAL** | CI/CD governance experience is a bridge; shift-left framing is already there; needs toolchain hands-on |
| D. Observability / Telemetry | Splunk expert (MART, MLTK), AppDynamics, Grafana, SLO/SLI governance | MELT vocabulary, OTel Collector design, burn rate alert math, cardinality management | **MINOR** | Strongest domain; needs vocabulary translation (Splunk → OTel/MELT) and burn rate alert formulas |
| E. IaC / Terraform | Acknowledged weak: no hands-on Terraform, no state management experience | Remote state, module design, drift handling, GitOps with ArgoCD | **CRITICAL** | Infrastructure change management from incident command translates to state/drift concepts; middleware config mgmt is a bridge |
| F. CI/CD Pipeline Security | Delivery governance, release orchestration, CI/CD management | Secrets scanning in pipeline, artifact signing, OIDC federation, PPE attack awareness | **CRITICAL** | Release governance = audit trail; delivery management = pipeline design — needs security layer added |
| G. Platform Engineering | Team leadership (15-person team), SAFe delivery, notification platform ownership | IDP philosophy, Backstage/catalog, golden paths, DORA metrics | **MODERATE** | Managing a platform team IS platform engineering — needs to reframe existing work with correct vocabulary + add tooling |
| H. Incident Command & Reliability | Expert: incident command, postmortems, SLO governance, T-Mobile scale reliability | Same — this is already strong; needs chaos engineering vocabulary | **MINOR** | Directly demonstrated; needs chaos engineering (LitmusChaos) and DORA metrics fluency added |

---

### Gap Severity Summary

| Severity | Domains | Priority |
|---|---|---|
| **CRITICAL** (blocks offer) | C (Supply Chain Security), E (Terraform/IaC), F (Pipeline Security) | Fix in Week 1 |
| **MODERATE** (differentiation) | A (K8s Internals), B (AWS), G (Platform Engineering) | Fix in Week 2 |
| **MINOR** (vocabulary gap) | D (Observability/MELT), H (Incident Command) | Refine in Weeks 3-4 |

---

<a name="section-3"></a>
## SECTION 3: 30-DAY TRAINING PLAN (Hybrid Agile-Waterfall Sprints)

> Format per day: LEARN (concept + analogy) → PRACTICAL (hands-on lab) → TEST (verification) → CERT/BADGE (if applicable)

---

### WEEK 1 (Days 1–7): Foundation Sprint — Close CRITICAL Gaps

**Sprint Goal:** Be able to articulate supply chain security, Terraform basics, and CI/CD security gates in an interview without notes.

---

#### Day 1: Supply Chain Security Mental Model + SBOM

**LEARN**
- Analogy: An SBOM is a nutritional label for software. Just as a food label lists every ingredient and its source, an SBOM lists every library, its version, its supplier, and its known vulnerabilities. The White House EO 14028 (2021) made this mandatory for federal software — the same way FDA mandates nutritional labels.
- OWASP Top 10:2025 A03 is now "Software and Data Integrity Failures" — covers both supply chain attacks and deserialization.
- Two formats: **SPDX** (Linux Foundation, ISO standard, more mature) vs. **CycloneDX** (OWASP, more tool ecosystem support in DevSecOps). Know both; prefer CycloneDX for DevSecOps contexts.
- SBOM ≠ security by itself. It is a *manifest* that enables SCA (Software Composition Analysis) tools to check for CVEs.

**PRACTICAL**
```bash
# Install Syft (SBOM generator) on your laptop — free, open source
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

# Generate a CycloneDX SBOM for a sample Docker image
syft nginx:latest -o cyclonedx-json > nginx-sbom.json

# Now scan that SBOM for vulnerabilities using Grype
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
grype sbom:nginx-sbom.json
```
- Goal: Read the output, understand what a HIGH CVE looks like in an SBOM context.
- Optional: Pull one of your T-Mobile service's Docker images (if accessible) and generate an SBOM for it.

**TEST — Can you answer these without notes?**
1. What is the difference between SBOM and SCA?
2. What is OWASP A03:2025 and what two attack categories does it cover?
3. A recruiter asks: "Do you have experience with SBOM?" — What is your 90-second STAR answer?

**CERT/BADGE:** No direct cert today. Note: `syft` and `grype` are Anchore open-source tools — put them in your LinkedIn Skills after you've used them.

---

#### Day 2: SCA, SAST, and Container Scanning — The Three Scan Types

**LEARN**
- Analogy: Think of a software delivery pipeline as a cargo manifest system.
  - **SAST** (Static Analysis Security Testing) = inspecting the cargo blueprint *before* it's built — reading source code for dangerous patterns (SQL injection, hardcoded secrets, unsafe deserialization).
  - **SCA** (Software Composition Analysis) = checking the parts manifest — are any of the components you're using recalled or under a safety advisory (CVE)?
  - **Container Scanning** = inspecting the sealed container *after* it's packed — are there vulnerabilities in the OS layer, not just your code?
- Key tools by category:
  - SAST: Semgrep (open source, fast), Checkmarx, Veracode
  - SCA: Snyk, Dependabot (GitHub native), OWASP Dependency-Check, Grype
  - Container Scanning: Trivy (Aqua Security, free), Snyk Container, ECR native scanning (Clair-based)
- **Trivy** is the Swiss Army knife: scans container images, filesystems, Git repos, Kubernetes clusters, and Terraform — know Trivy deeply.

**PRACTICAL**
```bash
# Install Trivy
brew install trivy  # Mac
# OR: https://aquasecurity.github.io/trivy/latest/getting-started/installation/

# Scan a container image
trivy image nginx:latest

# Scan a filesystem (your local repo)
trivy fs .

# Scan a Kubernetes cluster (if you have kubectl access)
trivy k8s --report summary cluster

# Generate output in table, JSON, or SARIF format
trivy image --format sarif --output results.sarif nginx:latest
```
- Goal: Understand severity levels (CRITICAL, HIGH, MEDIUM), what CVE-IDs look like, and what a SARIF report is (used by GitHub Security tab).

**TEST**
1. A developer says "I already have Dependabot. Why do I need Trivy?" — What is your answer?
2. What does SARIF stand for and why does it matter for GitHub integration?
3. Your team's container image has a CRITICAL CVE in the base OS layer. The code is not vulnerable. What is your recommendation?

**CERT/BADGE:** Snyk has a free "Snyk Learn" badge system — complete "Application Security Fundamentals" module (2 hours). Add badge to LinkedIn.

---

#### Day 3: OPA and Policy-as-Code — The Cluster Firewall

**LEARN**
- Analogy: OPA (Open Policy Agent) is to infrastructure decisions what a firewall is to network traffic. A network firewall enforces rules about *which packets are allowed*. OPA enforces rules about *which infrastructure changes are allowed* — "no container images from untrusted registries," "no Pods running as root," "no ingress rules without TLS."
- OPA + **Rego** (the policy language) + **Gatekeeper** (the Kubernetes admission webhook that runs OPA) are the trio.
- **Conftest** is OPA for CI/CD pipelines — you use it to check Terraform plans, Dockerfiles, Kubernetes manifests *before* they're applied.
- RBAC answers "can this *user/service* perform this *action*?" — OPA answers "is this *configuration* policy-compliant regardless of who submitted it?"

**PRACTICAL**
```bash
# Install OPA CLI
curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64_static
chmod 755 opa

# Write your first Rego policy (save as policy.rego)
cat > policy.rego << 'EOF'
package main

deny[msg] {
  input.spec.containers[_].securityContext.runAsRoot == true
  msg := "Container must not run as root"
}

deny[msg] {
  image := input.spec.containers[_].image
  not startswith(image, "ecr.us-east-1.amazonaws.com/")
  msg := sprintf("Image must be from approved ECR registry: %v", [image])
}
EOF

# Test the policy against a sample Kubernetes manifest
opa eval --input pod.json --data policy.rego "data.main.deny"
```
- Download a sample pod manifest from Kubernetes docs and intentionally add `runAsRoot: true` to trigger the deny.

**TEST**
1. Explain the difference between OPA Gatekeeper ConstraintTemplate and Constraint objects.
2. When would you use Conftest instead of Gatekeeper?
3. An interviewer says "how do you enforce that all Kubernetes Deployments must have resource limits?" — Describe the OPA policy approach.

**CERT/BADGE:** OPA does not have an official cert, but Styra (OPA's commercial maintainer) has free Styra Academy modules. Complete "OPA Foundations" and add to LinkedIn.

---

#### Day 4: Terraform Fundamentals — State, Locking, Remote Backend

**LEARN**
- Analogy: Terraform state is like a *reconciliation ledger* in accounting. When you apply infrastructure changes, Terraform writes down exactly what it created in the ledger (state file). The next time you run `terraform plan`, it compares your desired state (code) against the ledger (state) to calculate what needs to change. If two people edit the ledger simultaneously, you get accounting errors — that's why state locking with DynamoDB exists.
- The three ways state goes wrong:
  1. **Race condition**: Two engineers run `terraform apply` simultaneously (DynamoDB lock prevents this)
  2. **Drift**: Someone manually changes infrastructure; the state ledger no longer matches reality
  3. **State file corruption/loss**: Without remote state + versioning, your ledger is gone
- Remote state on S3 + DynamoDB locking is the standard answer for AWS. Know it cold.

**PRACTICAL**
```hcl
# Create a free-tier S3 bucket + DynamoDB table for Terraform state
# (Use AWS free tier — this costs $0)

# backend.tf
terraform {
  backend "s3" {
    bucket         = "vishweshwar-tfstate-dev"
    key            = "global/s3/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "vishweshwar-tfstate-lock"
    encrypt        = true
  }
}

# Create the S3 bucket and DynamoDB table manually first, then run:
# terraform init
# terraform plan
# terraform apply
```
- Exercise: Run two terminals simultaneously and try to run `terraform apply` from both. Observe the DynamoDB lock error.

**TEST**
1. What is `terraform.tfstate` and why should it never be committed to Git?
2. Explain `terraform import`. When would you use it?
3. What is `terraform refresh` and when is it dangerous?

**CERT/BADGE:** HashiCorp Terraform Associate exam prep starts here. Log this as Day 1 of cert prep.

---

#### Day 5: Terraform Modules + Hands-On EKS Module

**LEARN**
- Analogy: A Terraform module is like a reusable TIBCO process template (you have TIBCO experience). You define the process once with configurable parameters; different teams instantiate it with their own values. The module encapsulates complexity, exposes only the necessary knobs.
- Module design principles:
  - **Input variables**: what callers can customize
  - **Output values**: what the module exposes for other modules to consume
  - **Locals**: internal computed values, not exposed
  - **No hardcoded account IDs, regions, or environment names** in modules
- The Terraform Registry has community modules — the `terraform-aws-modules/eks/aws` module is the industry standard for EKS provisioning. Know how to read and use it.

**PRACTICAL**
```hcl
# Use the community EKS module (no actual deployment needed — just plan)
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "my-training-cluster"
  cluster_version = "1.29"

  cluster_endpoint_public_access = true

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    general = {
      min_size     = 2
      max_size     = 4
      desired_size = 2
      instance_types = ["t3.medium"]
    }
  }
}
```
- Goal: Run `terraform plan` against this (even without deploying) to see what it would create. Study the plan output — understand the dependency graph.

**TEST**
1. What is the difference between `terraform.tfvars` and `variables.tf`?
2. A module in your registry is at v1.5.0 but there's a v2.0.0 with breaking changes. How do you manage the upgrade across 10 teams?
3. What is `depends_on` in Terraform and when is it necessary vs. automatic?

---

#### Day 6: CI/CD Pipeline Security — GitHub Actions + OIDC + Secrets Scanning

**LEARN**
- Analogy: Using stored AWS credentials in GitHub Secrets is like leaving a master key under the doormat — it works, but anyone who finds the mat has permanent access. OIDC federation is like a temporary badge system: GitHub proves its identity to AWS ("I am this workflow, running from this repo, on this branch"), and AWS issues a *short-lived* credential that expires in 15 minutes.
- Poisoned Pipeline Execution (PPE) attack: An attacker submits a PR that modifies `.github/workflows/deploy.yml`, adding a step that exfiltrates secrets. Defense: require `pull_request_target` triggers to use read-only secrets for untrusted PRs.
- Secrets scanning tools: **gitleaks** and **truffleHog** scan Git history for accidentally committed secrets. GitHub has native secret scanning. Run these as pre-commit hooks.

**PRACTICAL**
```yaml
# .github/workflows/secure-deploy.yml
# Example: GitHub Actions with OIDC to AWS (no stored credentials)

name: Secure Deploy
on: [push]

permissions:
  id-token: write   # Required for OIDC
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # OIDC: exchange GitHub token for AWS credentials
      - name: Configure AWS Credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/GitHubActionsRole
          aws-region: us-east-1
          # No AWS_ACCESS_KEY_ID needed — OIDC provides short-lived credentials

      # Secrets scanning gate
      - name: Scan for secrets
        uses: gitleaks/gitleaks-action@v2

      # Container scan gate
      - name: Trivy container scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'myimage:latest'
          exit-code: '1'           # Fail the pipeline on CRITICAL
          severity: 'CRITICAL,HIGH'
```
- Practice: Create a free GitHub account, fork a sample repo, and add this workflow. Trigger it and observe the OIDC flow in the Actions log.

**TEST**
1. What is the `id-token: write` permission required for OIDC, and where is the trust relationship configured?
2. A developer asks why `gitleaks` is running on every push if secrets aren't in this PR. What do you tell them?
3. Describe a PPE attack in 3 sentences. What is your primary defense?

**CERT/BADGE:** GitHub Actions does not have an official cert. However, completing "GitHub Advanced Security" on GitHub Learning Lab earns a badge.

---

#### Day 7: Week 1 Integration — Build Your "Supply Chain Security" STAR Story

**LEARN**
Today is integration day, not new content. The goal is to build interview-ready narratives from the CRITICAL gap domains.

**PRACTICAL**
Write 3 STAR-method answers (Situation/Task/Action/Result) for:

1. **CI/CD Security Gate Design** — Using your T-Mobile delivery governance experience as the Situation, frame adding SBOM generation and container scanning as the Action. Even if not done yet, describe the design you would implement.

2. **Policy-as-Code for Kubernetes** — Using your EKS management experience, describe designing OPA Gatekeeper constraints to enforce image registry policies and resource limits.

3. **Supply Chain Security Architecture** — Describe a notification platform re-architecture (25M msg/day) where you added SBOM, artifact signing, and SCA gates to the CI/CD pipeline.

**TEST**
Record yourself answering these three questions on video. Review for:
- Are you using the vocabulary from Domains C and F naturally?
- Is each answer 2–3 minutes (not longer)?
- Do you anchor results with data (percentage, time, incident count)?

**CERT/BADGE:** No new cert. Review your Snyk Learn badge from Day 2 — post it on LinkedIn today with a note about your learning.

---

### WEEK 2 (Days 8–14): Core Skills Sprint — MODERATE Gaps + Deepen Strengths

**Sprint Goal:** Fill Kubernetes internals, AWS depth (IRSA, multi-account), Platform Engineering vocabulary, and translate Splunk expertise to OTel/MELT language.

---

#### Day 8: Kubernetes Control Plane Internals — The Watch/Reconcile Loop

**LEARN**
- Analogy: The Kubernetes control plane works like an air traffic control system. The **etcd** database is the flight plan registry — every aircraft's intended route is recorded there. The **kube-controller-manager** is the set of air traffic controllers, each responsible for one type of aircraft (Deployment controller, ReplicaSet controller, Node controller). Each controller constantly watches the registry for discrepancies between the intended route and the actual position, and issues correction commands. The **kube-scheduler** is the gate assignment system — when a new aircraft (Pod) arrives with no gate, the scheduler finds the best available gate (Node) based on capacity, constraints, and affinity rules.
- The reconcile loop: `observe current state → compare to desired state → act to close the gap`. This is how every Kubernetes controller works. It is also why Kubernetes is *eventually consistent* — the loop runs continuously, so it eventually converges.
- Key components: `kube-apiserver`, `etcd`, `kube-controller-manager`, `kube-scheduler`, `kubelet`, `kube-proxy`

**PRACTICAL**
```bash
# Read the source of truth — watch the etcd-level events
kubectl get events --watch -n default

# See the reconcile loop in action:
# 1. Create a deployment
kubectl create deployment test-app --image=nginx --replicas=3

# 2. Manually delete a Pod — watch the ReplicaSet controller reconcile
kubectl get pods -w &
kubectl delete pod <one-of-the-pods>
# Observe: new pod is created within seconds — that's the reconcile loop

# 3. See scheduler decisions
kubectl describe pod <pod-name> | grep -A 10 "Events:"
# Look for "Successfully assigned" — this shows scheduler decision
```

**TEST**
1. What happens, step by step, when you run `kubectl apply -f deployment.yaml`? (Name each component in sequence.)
2. Why is etcd the single point of truth for cluster state, and what happens if etcd becomes unavailable?
3. Explain the difference between a ReplicaSet and a Deployment controller.

---

#### Day 9: Kubernetes Admission Webhooks + RBAC Deep Dive

**LEARN**
- Analogy: Admission webhooks are the TSA security checkpoint for your Kubernetes API server. Every API request (create Pod, update Deployment, etc.) must pass through the checkpoint before it's admitted to the cluster. A **MutatingAdmissionWebhook** can *change* the request (inject a sidecar, add default resource limits). A **ValidatingAdmissionWebhook** can only *approve or reject* (enforce policy without modification). OPA Gatekeeper uses a validating webhook; Istio sidecar injection uses a mutating webhook.
- RBAC key objects: `Role` (namespaced), `ClusterRole` (cluster-wide), `RoleBinding` (binds a Role to a user/group/ServiceAccount in a namespace), `ClusterRoleBinding` (binds a ClusterRole cluster-wide).
- The ServiceAccount → token projection chain for IRSA: `ServiceAccount` → OIDC annotation → AWS IAM trust policy → short-lived credential.

**PRACTICAL**
```bash
# RBAC lab: Create a read-only user for a specific namespace
kubectl create namespace dev-team

# Create a Role (namespace-scoped)
cat <<EOF | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: dev-team
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch"]
EOF

# Create a ServiceAccount and bind the role
kubectl create serviceaccount dev-user -n dev-team
kubectl create rolebinding dev-user-binding \
  --role=pod-reader \
  --serviceaccount=dev-team:dev-user \
  -n dev-team

# Test the permissions
kubectl auth can-i list pods --as=system:serviceaccount:dev-team:dev-user -n dev-team
kubectl auth can-i delete pods --as=system:serviceaccount:dev-team:dev-user -n dev-team
```

**TEST**
1. A Pod needs to read ConfigMaps in its own namespace. What RBAC objects do you create?
2. What is the difference between `ClusterRole` and `Role`? When would you use `ClusterRoleBinding` with a `Role`?
3. How does OPA Gatekeeper's validating webhook get invoked by the API server?

---

#### Day 10: AWS IRSA + Multi-Account IAM — The Trust Relationship Chain

**LEARN**
- Analogy: IRSA (IAM Roles for Service Accounts) is like a corporate contractor badge system. A contractor (Kubernetes Pod) works for a specific project (ServiceAccount). The project manager (OIDC Provider) vouches for the contractor to the building security desk (AWS IAM). Security issues a temporary badge (short-lived credentials) that only opens the doors the project specifically needs. When the project ends, the badge expires automatically.
- The trust chain: EKS cluster creates an OIDC Provider → Pod is assigned a ServiceAccount → ServiceAccount is annotated with an IAM Role ARN → When Pod calls AWS, it exchanges its ServiceAccount JWT token with AWS STS → STS verifies the OIDC signature → Issues temporary credentials.
- Multi-account IAM: SCPs (Service Control Policies) in AWS Organizations are guardrails — they define what IAM policies in any account *cannot* allow. Even an IAM Admin in a member account cannot exceed SCP boundaries.

**PRACTICAL**
```bash
# Step 1: Check if your EKS cluster has OIDC enabled
aws eks describe-cluster --name <cluster-name> --query "cluster.identity.oidc.issuer"

# Step 2: Create IAM OIDC Provider (if not exists)
eksctl utils associate-iam-oidc-provider --cluster <cluster-name> --approve

# Step 3: Create IAM Role with trust policy for a ServiceAccount
# Trust policy (this is what makes IRSA work):
cat > trust-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Federated": "arn:aws:iam::ACCOUNT_ID:oidc-provider/OIDC_PROVIDER_URL"
    },
    "Action": "sts:AssumeRoleWithWebIdentity",
    "Condition": {
      "StringEquals": {
        "OIDC_PROVIDER_URL:sub": "system:serviceaccount:NAMESPACE:SERVICE_ACCOUNT_NAME"
      }
    }
  }]
}
EOF

# Step 4: Annotate the ServiceAccount
kubectl annotate serviceaccount \
  -n default my-service-account \
  eks.amazonaws.com/role-arn=arn:aws:iam::ACCOUNT_ID:role/MyRole
```

**TEST**
1. Explain IRSA to a developer who only knows "I need to give my app permission to read S3." Walk through the 4 steps.
2. What happens if the OIDC provider URL in the trust policy doesn't match the EKS cluster's OIDC URL?
3. A new account is added to your AWS Organization. You want to ensure it cannot disable CloudTrail. How do you enforce this?

---

#### Day 11: MELT Framework + OpenTelemetry Vocabulary Translation

**LEARN**
- You already speak Splunk fluently. Today is vocabulary translation, not learning from scratch.

| Your Splunk/Current Language | MELT/OTel Industry Language |
|---|---|
| Splunk search / index | Logs (L in MELT) |
| Grafana / AppDynamics metrics | Metrics (M in MELT) |
| Alert events | Events (E in MELT) |
| Distributed traces (APM) | Traces (T in MELT) |
| Splunk HEC forwarder | OTel Collector (OTLP exporter) |
| MART framework (your term) | Not industry-standard — translate to MELT |
| AppDynamics agent | OTel SDK / auto-instrumentation agent |
| Splunk MLTK anomaly detection | OTel + Prometheus recording rules + ML alerting |

- **OpenTelemetry** is the *standard* — vendor-neutral instrumentation. OTel SDK instruments your code. OTel Collector receives telemetry and fans it out to multiple backends (Splunk, Datadog, Prometheus, Jaeger). This is why OTel matters: you instrument once, send anywhere.
- **OTLP** (OpenTelemetry Protocol) is the wire format — like HTTP for telemetry data.

**PRACTICAL**
```yaml
# OTel Collector config: fan out to Splunk HEC AND Prometheus
# This is your "Splunk migration path" story

receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

exporters:
  splunk_hec:
    token: "YOUR_HEC_TOKEN"
    endpoint: "https://splunk.company.com:8088/services/collector"
    source: "otel"
    sourcetype: "otel:logs"

  prometheusremotewrite:
    endpoint: "http://prometheus:9090/api/v1/write"

service:
  pipelines:
    logs:
      receivers: [otlp]
      exporters: [splunk_hec]
    metrics:
      receivers: [otlp]
      exporters: [prometheusremotewrite]
```
- Install OTel Collector locally (Docker): `docker run -p 4317:4317 otel/opentelemetry-collector-contrib`

**TEST**
1. A recruiter asks about MELT. Translate your Splunk experience into MELT vocabulary in 90 seconds.
2. What is the difference between a Span and a Trace?
3. Why is the OTel Collector valuable even if your company is 100% Splunk today?

---

#### Day 12: SLO Math — Burn Rate Alerts + Error Budget Policies

**LEARN**
- You already manage SLOs. This is making the math explicit so you can discuss it in interviews.
- **Error budget** = (1 - SLO target) × time window. For 99.9% over 28 days = 0.1% × 28 × 24 × 60 = **40.3 minutes** of allowed failure.
- **Burn rate** = how fast you're consuming the error budget relative to normal. Burn rate of 1x = consuming at exactly the rate that will exhaust the budget at the end of the window. Burn rate of 14x = exhausting the 28-day budget in 2 days.
- **Multi-window multi-burn-rate alert** (Google SRE Workbook pattern):
  - Fast burn alert: 1h window, burn rate > 14x → page immediately
  - Slow burn alert: 6h window, burn rate > 6x → page immediately
  - This combination catches both sharp incidents AND slow degradation

**PRACTICAL**
```yaml
# Prometheus alerting rules for multi-window burn rate
# (Know this by heart — interviewers love this)

groups:
  - name: slo_burn_rate
    rules:
      # Fast burn: consuming 5% of 28-day budget in 1 hour
      - alert: SLOFastBurn
        expr: |
          (
            sum(rate(http_requests_total{status=~"5.."}[1h]))
            /
            sum(rate(http_requests_total[1h]))
          ) > (14 * 0.001)  # 14x burn rate for 99.9% SLO
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Fast burn: error budget exhausted in <2 days at current rate"

      # Slow burn: consuming 10% of 28-day budget in 6 hours
      - alert: SLOSlowBurn
        expr: |
          (
            sum(rate(http_requests_total{status=~"5.."}[6h]))
            /
            sum(rate(http_requests_total[6h]))
          ) > (6 * 0.001)  # 6x burn rate
        for: 15m
        labels:
          severity: warning
```

**TEST**
1. Your SLO is 99.5% over 30 days. What is your error budget in minutes?
2. Your fast-burn alert fires at 2am. Burn rate is 20x. What do you do in the first 5 minutes?
3. Why are burn rate alerts better than static threshold alerts for P1 detection?

---

#### Day 13: Platform Engineering — IDP, Golden Paths, DORA Metrics

**LEARN**
- Analogy: A platform team is like the highway department. They don't drive the trucks (features), but they build and maintain the roads (infrastructure, tooling, developer workflows). A **golden path** is the HOV lane — developers can take it and go faster, or they can take the local roads, but the golden path is optimized, safe, and well-maintained.
- An **Internal Developer Platform (IDP)** is the full system of paved roads: from "I want a new service" to "my service is running in production with monitoring, on-call rotation, and a deployment pipeline." Backstage is the UI layer of an IDP — the developer portal.
- **DORA metrics** (the four keys):
  1. **Deployment Frequency** — how often you deploy to production (Elite: multiple times/day)
  2. **Lead Time for Changes** — commit to production (Elite: <1 hour)
  3. **Change Failure Rate** — % of deployments that cause incidents (Elite: 0–15%)
  4. **Mean Time to Restore (MTTR)** — how fast you recover (Elite: <1 hour)
- Your existing work at T-Mobile maps directly to DORA. You likely have data for all four. Find and memorize your team's current DORA numbers.

**PRACTICAL**
```yaml
# Backstage catalog-info.yaml — the IDP service manifest
# Every service should have this file in its repo root

apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: notification-service
  description: T-Mobile notification platform — 25M msg/day
  annotations:
    github.com/project-slug: tmobile/notification-service
    grafana/dashboard-selector: "service=notification"
    pagerduty.com/service-id: "ABC123"
    backstage.io/techdocs-ref: dir:.
  tags:
    - notification
    - kafka
    - rabbitmq
spec:
  type: service
  lifecycle: production
  owner: sre-platform-team
  system: notification-platform
  dependsOn:
    - resource:rabbitmq-cluster
    - resource:cassandra-cluster
```
- Exercise: Write a `catalog-info.yaml` for your T-Mobile notification platform. This becomes a portfolio artifact.

**TEST**
1. What is the difference between a platform team and an SRE team in Team Topologies terminology?
2. Your deployment frequency is 2x per week. What would you do to move toward daily deployments?
3. A developer asks to use a non-standard container base image. How do you respond as a platform engineer?

**CERT/BADGE:** "Google Cloud Professional DevOps Engineer" study path (even if targeting AWS) has strong platform engineering content. Consider adding to study queue.

---

#### Day 14: Week 2 Integration — Build Portfolio Artifact #1

**PRACTICAL — Deliverable: Platform Engineering One-Pager**

Write a 1-page architecture description (Markdown) titled: "T-Mobile Notification Platform — Reliability Architecture" covering:
1. Service overview (25M msg/day, stack: RabbitMQ, Cassandra, Redis, EKS)
2. SLO definition and error budget policy
3. Observability stack (translate to MELT/OTel language)
4. Incident command structure
5. DevSecOps gates in the delivery pipeline (add what you'd add, not just what exists)

Save this as `C:\Work\Training\portfolio\notification-platform-reliability.md`

This document serves dual purpose:
- LinkedIn Featured section post: "Architecture deep-dive: How we designed reliability for a 25M msg/day platform"
- Interview talking point: "Let me show you the architecture doc I wrote..."

---

### WEEK 3 (Days 15–21): Integration Sprint — Connect Skills, Build Portfolio Artifacts

**Sprint Goal:** Connect the dots between domains. Build 3 portfolio artifacts. Practice system design interviews.

---

#### Day 15: Terraform + GitOps — ArgoCD Pull Model

**LEARN**
- The GitOps mental model: Git is the single source of truth for *both* application code *and* infrastructure state. Any change to production must flow through a Git commit. Rollback = revert the commit.
- ArgoCD operates on a **pull model**: ArgoCD runs inside the cluster, watches a Git repository, and reconciles the cluster state to match the repo. This is more secure than a CI system pushing to the cluster (which requires the CI system to hold cluster credentials).
- Analogy: Push model = you FedEx packages to the warehouse and give FedEx a key to the warehouse. Pull model = the warehouse sends a truck to pick up packages from your secure depot, and the warehouse already has its own key.

**PRACTICAL**
```bash
# Install ArgoCD in a local kind cluster (free, runs on your laptop)
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Create an Application pointing to a Git repo
cat <<EOF | kubectl apply -f -
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: notification-service
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/YOUR_USER/sample-app
    targetRevision: HEAD
    path: k8s/
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true   # ArgoCD will revert manual changes — drift correction
EOF
```
- Trigger a drift: manually change a Deployment's replica count with `kubectl scale`. Watch ArgoCD detect and correct the drift within 3 minutes.

---

#### Day 16: Chaos Engineering Fundamentals + LitmusChaos

**LEARN**
- Analogy: Chaos engineering is like fire drills. You don't wait for a fire to know whether your evacuation plan works. You run controlled drills to find the gaps before a real fire.
- The chaos engineering process: **Hypothesis → Experiment Design → Blast Radius Definition → Execution → Observation → Learning**
- Chaos ≠ random destruction. Every experiment has a hypothesis: "We believe the notification service will continue processing messages at >99.9% success rate when one RabbitMQ node is killed."
- Key tools: **LitmusChaos** (CNCF, free), **Gremlin** (commercial), **Chaos Monkey** (Netflix, AWS-specific).

**PRACTICAL**
```bash
# Install LitmusChaos in a Kubernetes cluster
kubectl apply -f https://litmuschaos.github.io/litmus/litmus-operator-v3.0.0.yaml

# Create a pod-delete experiment
cat <<EOF | kubectl apply -f -
apiVersion: litmuschaos.io/v1alpha1
kind: ChaosExperiment
metadata:
  name: pod-delete
spec:
  definition:
    scope: Namespaced
    image: "litmuschaos/go-runner:3.0.0"
    args: ["-c", "litmus-go -name pod-delete"]
    env:
      - name: TARGET_APP_LABELS
        value: "app=notification-service"
      - name: TOTAL_CHAOS_DURATION
        value: "60"  # Kill pods for 60 seconds
      - name: CHAOS_INTERVAL
        value: "10"
EOF
```
- Write a hypothesis before running the experiment. Measure your SLO during the chaos window.

---

#### Day 17: eBPF Fundamentals — Conceptual Mastery for Interviews

**LEARN**
- Analogy: Traditional monitoring tools are like reading a book through a library window — you can see some pages but not the full picture. eBPF is like being inside the library with X-ray vision — you can observe every system call, network packet, and CPU instruction without modifying the application or even restarting it.
- eBPF (extended Berkeley Packet Filter) allows you to run sandboxed programs in the Linux kernel — triggered by system calls, network events, kernel functions — without modifying kernel source code or loading kernel modules.
- **Why it matters for SRE**: Cilium uses eBPF for Kubernetes networking (replacing iptables, which doesn't scale past ~500 nodes). Falco uses eBPF for runtime security monitoring. Pixie uses eBPF for zero-instrumentation observability.
- Key vocabulary: `bpf()` syscall, eBPF programs, eBPF maps, verifier, JIT compiler, kernel hooks (kprobes, tracepoints, XDP), `bpftool`, Cilium, Hubble, Falco, Pixie, Tetragon.

**PRACTICAL**
- You do NOT need to write eBPF code at Staff/Principal level. You need to explain it architecturally.
- Install Cilium on a kind cluster and explore Hubble (the network observability UI that eBPF enables):
```bash
cilium install
cilium hubble enable --ui
cilium hubble port-forward &
# Open http://localhost:12000 — see real-time network flow visualization
```

---

#### Day 18: Terraform Advanced — Drift Detection + Sentinel Policy

**LEARN**
Today's focus: the scenarios that separate CRITICAL/HIGH roles from basic Terraform users.

**Drift Detection and Reconciliation Process:**
1. `terraform plan -refresh-only` — detect drift without planning changes
2. Review the diff carefully: is this drift from an emergency manual change or an unauthorized change?
3. If emergency change: document the drift, plan to codify it in Terraform within 24h
4. If unauthorized change: treat as a security incident AND reconcile via `terraform apply`
5. Prevention: use AWS Config Rules to detect out-of-band changes in real-time

**PRACTICAL**
```bash
# Detect drift
terraform plan -refresh-only

# Import a manually-created resource into Terraform state
# (Common scenario: someone manually created an S3 bucket during an incident)
terraform import aws_s3_bucket.incident_bucket my-incident-bucket-name

# Now write the resource configuration to match
cat >> main.tf << 'EOF'
resource "aws_s3_bucket" "incident_bucket" {
  bucket = "my-incident-bucket-name"
  # Add remaining configuration to match actual state
}
EOF
terraform plan  # Should show no changes if import was accurate
```

---

#### Day 19: Portfolio Artifact #2 — Secure CI/CD Pipeline Design Doc

Write a design document: "DevSecOps Pipeline Architecture for the T-Mobile Notification Platform"

Sections:
1. **Current State** (what exists today — CI/CD, deployment process)
2. **Threat Model** (what supply chain attacks are relevant for your stack)
3. **Target Architecture** (pipeline stages: commit → build → scan → sign → deploy → runtime)
4. **Gate Design**: what fails fast vs. what is advisory
5. **SBOM Strategy**: when generated, where stored, how linked to releases
6. **Artifact Signing**: Cosign + ECR, keyless signing via GitHub Actions OIDC
7. **Policy Gates**: OPA Conftest for Terraform, Gatekeeper for Kubernetes
8. **Audit Trail**: how every deploy is traceable to a reviewed, signed, scanned commit

Save as: `C:\Work\Training\portfolio\devsecops-pipeline-design.md`

---

#### Day 20: System Design Interview Practice — "Design a Reliable Notification Platform"

This is your strongest domain. Practice the full answer:

**Problem Statement**: "Design a notification platform that sends 25M messages/day with 99.9% delivery SLO, supports SMS, push, and email, and must handle a 10x spike during a T-Mobile major event (e.g., Super Bowl promotion)."

**Structure your answer (30 minutes):**
1. Clarifying questions (2 min): SLO type (delivery vs. send), message ordering requirements, retry semantics
2. High-level design (5 min): message intake → queue → processor → channel adapter → delivery
3. Scale design (8 min): RabbitMQ vs. Kafka for this use case, partition strategy, consumer group design
4. Reliability design (8 min): dead letter queues, retry with exponential backoff, idempotency keys
5. Observability design (5 min): MELT strategy, SLO definition, burn rate alerts
6. Security design (2 min): secrets management, API authentication, audit logging

This is where you WIN the interview — you have lived this problem.

---

#### Day 21: Portfolio Artifact #3 — Kubernetes Security Runbook

Write a runbook: "Kubernetes Security Incident Response — Container Escape Scenario"

Sections:
1. **Detection**: Falco alert signature for container escape
2. **Triage**: kubectl commands to identify the affected Pod, Node, and blast radius
3. **Containment**: How to cordon a Node, evict Pods, revoke ServiceAccount tokens
4. **Evidence Preservation**: What to collect before you delete anything
5. **Remediation**: Root cause (misconfigured SecurityContext? Vulnerable base image?)
6. **Prevention**: OPA Gatekeeper policies that would have blocked the vulnerable configuration

Save as: `C:\Work\Training\portfolio\k8s-security-incident-runbook.md`

---

### WEEK 4 (Days 22–30): Interview Readiness + LinkedIn Optimization

**Sprint Goal:** Polish narratives, activate LinkedIn, apply to 5 target roles with tailored positioning.

---

#### Day 22: Mock Interview #1 — Kubernetes + AWS Technical Deep Dive

Practice the following sequence (get a peer, use an AI, or record yourself):

1. "Walk me through the Kubernetes control plane, component by component." (8 min)
2. "How does IRSA work in EKS? Walk me through the trust chain." (5 min)
3. "A pod is in CrashLoopBackOff. Walk me through your diagnostic process." (7 min)
4. "Design a multi-tenant EKS cluster for 50 teams." (10 min)

**Evaluation rubric:**
- Used correct vocabulary without prompting?
- Drew architecture diagrams (on paper/whiteboard) without being asked?
- Cited T-Mobile experience for at least 2 answers?
- Answered "design" questions with tradeoffs, not just one right answer?

---

#### Day 23: Mock Interview #2 — DevSecOps + Supply Chain Security

1. "Design a secure software supply chain for a Java microservice from commit to production." (12 min)
2. "What is an SBOM and why does it matter for supply chain security?" (4 min)
3. "Write an OPA Rego policy that denies Pods running as root." (5 min — on paper)
4. "Walk me through the SolarWinds attack. How would SLSA level 3 have mitigated it?" (6 min)

---

#### Day 24: Mock Interview #3 — Incident Command + Reliability

1. "Describe your blameless postmortem process end-to-end." (6 min)
2. "Your SLO is 99.9%. You consumed 50% of error budget in 3 days. Walk me through your decision tree." (8 min)
3. "What is chaos engineering and how does it differ from load testing?" (4 min)
4. "Give me your best STAR story about improving reliability at scale." (8 min)

---

#### Day 25: LinkedIn Profile Overhaul (See Section 5 for full strategy)

Execute the complete LinkedIn optimization from Section 5. Estimated time: 4 hours.

Key tasks:
- [ ] Update headline (formula in Section 5)
- [ ] Rewrite About section
- [ ] Update Skills to the priority list
- [ ] Upload portfolio artifacts as Featured items
- [ ] Add Snyk Learn badge
- [ ] Set "Open to Work" for recruiters only

---

#### Day 26: Resume Tailoring — Staff SRE vs. DevSecOps Variants

Create two resume variants from your base:

**Variant A: Staff/Principal SRE**
- Lead with reliability metrics (MTTD, MTTR, SLO achievement, incident reduction)
- Emphasize scale (25M msg/day, 15-person team, platform ownership)
- Feature: Kubernetes, Splunk/observability, SLO governance, incident command

**Variant B: Senior DevSecOps Engineer**
- Lead with security posture improvements (vulnerability reduction, compliance achievements)
- Emphasize pipeline security, Vault/CyberArk, delivery governance
- Feature: CI/CD security, secrets management, policy enforcement, compliance

Add the following keywords to BOTH variants (they are currently missing):
- SBOM, SCA, supply chain security (even framed as "designed program to implement")
- MELT, OpenTelemetry, OTLP (translate Splunk work)
- DORA metrics (you have the data, add the vocabulary)
- Platform engineering, Internal Developer Platform (rename your team's work)
- OPA, policy-as-code (add as planned/in-progress if not yet implemented)

---

#### Day 27: Target Company Research + Role Mapping

Research 10 target companies in these categories:

| Category | Examples | What to Research |
|---|---|---|
| Hyperscalers/Cloud | AWS, Google Cloud, Azure | Staff/Principal SRE roles, interview process, Glassdoor |
| Big Tech | Meta, Apple, Netflix, Stripe | Site reliability engineering, their public engineering blogs |
| Fintech | Stripe, Plaid, Coinbase, Block | DevSecOps, compliance requirements, SRE culture |
| Telecom-adjacent | Verizon, AT&T, Comcast | Direct competitor knowledge advantage |
| Growth Tech | Databricks, Snowflake, HashiCorp | Platform engineering, IaC, DevSecOps alignment |

For each company, note:
1. Title variants they use (Staff vs. Principal vs. Senior)
2. Tech stack from job postings (what tools do they mention?)
3. Comp range (Levels.fyi, Glassdoor, LinkedIn Salary)

---

#### Day 28: Compensation Negotiation Prep

**Know your number:**
- Target: $180k–$280k+ TC
- T-Mobile current base (know this exactly)
- Market data: Levels.fyi for "Staff SRE" at target companies
- Competing offers: If you don't have one, use Levels.fyi data as your anchor

**Negotiation principles for your profile:**
1. Lead with scale and impact: "I manage reliability for a 25M message/day platform serving T-Mobile's entire subscriber base" — this is a Fortune 50 scale argument
2. Competing offers: Do not negotiate without one if you can get one
3. RSU vesting cliffs: Understand the equity component at each target company
4. Know your walk-away number before any offer call

---

#### Day 29: Application Sprint — Apply to 5 Roles

Apply to 5 specific roles with tailored cover letters and the correct resume variant. For each application:
1. Match resume keywords to job posting keywords (use a word cloud tool)
2. Customize the headline in your application email
3. Connect with the hiring manager or team lead on LinkedIn (before or after applying)
4. Note the application date, role, and expected timeline in a tracking spreadsheet

---

#### Day 30: Review, Retrospective, and Plan 31–60

**30-day retrospective:**
- What are the 3 topics you can now explain fluently that you couldn't on Day 1?
- What are the 3 topics that still feel weak?
- Have you completed all 3 portfolio artifacts?
- Is your LinkedIn profile active and receiving recruiter outreach?

**Plan Days 31–60 (post-30-day):**
- Begin CKA exam prep (3–4 weeks)
- Complete HashiCorp Terraform Associate exam (2 weeks)
- Build one end-to-end hands-on project: EKS cluster + ArgoCD + OPA Gatekeeper + Trivy + OTel Collector + Grafana — the full stack in one repo

---

<a name="section-4"></a>
## SECTION 4: CERTIFICATION ROADMAP

> Priority order based on: ROI for $180k–$280k roles, time to prepare given current skills, LinkedIn recruiter signal strength, and which gaps they address.

---

### Priority-Ordered Certification Plan

| Rank | Certification | Exam Code | Prep Time (Your Level) | Cost | Gap Addressed | Roles Unlocked |
|---|---|---|---|---|---|---|
| **1** | HashiCorp Terraform Associate | TA-003 | 3–4 weeks | $70.50 | CRITICAL: IaC gap | All DevSecOps, Platform Eng, SRE roles |
| **2** | CKA — Certified Kubernetes Administrator | CKA | 5–6 weeks | $395 | MODERATE: K8s internals | Staff/Principal SRE, Platform Eng |
| **3** | AWS Solutions Architect Associate | SAA-C03 | 4–5 weeks | $150 | MODERATE: AWS breadth | All cloud-native SRE/DevSecOps |
| **4** | CKS — Certified Kubernetes Security Specialist | CKS | 4–5 weeks (after CKA) | $395 | CRITICAL: K8s + security | Senior DevSecOps, Staff SRE with security emphasis |
| **5** | AWS Security Specialty | SCS-C02 | 5–6 weeks (after SAA) | $300 | CRITICAL: DevSecOps pipeline security | Senior DevSecOps, Cloud Security Eng |
| **6** | AWS Solutions Architect Professional | SAP-C02 | 6–8 weeks (after SAA) | $300 | MODERATE: AWS architecture depth | Principal SRE, Staff Platform Eng |
| **7** | CKAD — Certified Kubernetes Application Developer | CKAD | 2–3 weeks (after CKA) | $395 | LOW: already operational | Application platform roles |

---

### Certification Sequencing Detail

#### Phase 1 (Weeks 1–4): Terraform Associate
- **Why first**: Closes a CRITICAL gap, fastest prep, highest ROI for time invested
- **Study path**: HashiCorp Learn (free) → KodeKloud Terraform course → practice exams (Whizlabs or ExamTopics)
- **LinkedIn badge value**: HIGH — Terraform Associate is a top-searched keyword for DevSecOps recruiters
- **Roles it unlocks**: Every DevSecOps and Platform Engineering job posting lists Terraform; having the cert removes the "do you know Terraform?" objection

#### Phase 2 (Weeks 5–10): CKA
- **Why second**: Kubernetes is in every Staff/Principal SRE job description; CKA is the market-standard validation
- **Study path**: KodeKloud CKA course (Mumshad Mannambeth) → killer.sh simulator (included with exam) → hands-on labs daily
- **LinkedIn badge value**: VERY HIGH — CKA is the most-searched Kubernetes credential by recruiters
- **Roles it unlocked**: Specifically unlocks Staff SRE, Principal SRE, Platform Engineering, and eliminates K8s internals doubt in interviews
- **Exam format**: Performance-based (live cluster), 2 hours, 15–20 tasks — this is a real skills test, not multiple choice

#### Phase 3 (Weeks 11–15): AWS Solutions Architect Associate
- **Why third**: Validates AWS breadth; required prerequisite for AWS Security Specialty; short prep time given EKS/AWS operational experience
- **Study path**: Adrian Cantrill's SAA-C03 course (best depth) → Stephane Maarek (best breadth) → practice exams (Tutorial Dojo)
- **LinkedIn badge value**: HIGH — AWS certs are the most widely recognized cloud credentials
- **Note**: You may pass this faster than 4 weeks given your operational AWS experience

#### Phase 4 (Weeks 16–21): CKS (after CKA)
- **Why fourth**: CKS directly addresses the DevSecOps/security gap for Kubernetes; requires CKA as prerequisite
- **Study path**: KodeKloud CKS course → security-specific killer.sh labs → Falco, OPA Gatekeeper, network policies hands-on
- **LinkedIn badge value**: VERY HIGH for DevSecOps roles — CKS is rare and highly valued
- **Roles it unlocks**: Senior DevSecOps Engineer, Cloud Security Engineer (SRE-adjacent), Staff SRE with security scope

#### Phase 5 (Weeks 22–28): AWS Security Specialty
- **Why fifth**: The strongest signal for DevSecOps roles on the AWS side; validates supply chain security, IAM, GuardDuty, Security Hub knowledge
- **Study path**: Adrian Cantrill's Security Specialty → AWS whitepapers (IAM Best Practices, Well-Architected Security Pillar) → Tutorial Dojo practice exams
- **LinkedIn badge value**: HIGH — rare credential that validates security-specific depth

#### Phase 6 (Optional/Long-term): AWS Solutions Architect Professional + CKAD
- **AWS SAP**: Highest-value AWS cert for architecture roles; takes 6–8 weeks serious prep; unlocks Principal/Staff platform architect roles
- **CKAD**: Lower priority — you're not an application developer, but it completes the Kubernetes certification trifecta (CKA + CKAD + CKS)

---

### Cert ROI Summary Table

| Certification | Time Investment | Cost | Recruiter Signal | Gap Closed | Priority Score |
|---|---|---|---|---|---|
| Terraform Associate | 3–4 wks | $70 | High | CRITICAL | **1st** |
| CKA | 5–6 wks | $395 | Very High | MODERATE | **2nd** |
| AWS SAA | 4–5 wks | $150 | High | MODERATE | **3rd** |
| CKS | 4–5 wks | $395 | Very High | CRITICAL | **4th** |
| AWS Security Specialty | 5–6 wks | $300 | High | CRITICAL | **5th** |
| AWS SAP | 6–8 wks | $300 | Medium-High | MODERATE | **6th** |
| CKAD | 2–3 wks | $395 | Medium | LOW | **7th** |

---

<a name="section-5"></a>
## SECTION 5: LINKEDIN OPTIMIZATION STRATEGY

---

### Headline Formula

**Current problem**: Generic manager titles don't attract Staff/Principal-level recruiter searches.

**Formula**: `[Primary Role Target] | [Scale Signal] | [Top 3 Keywords Recruiters Search]`

**Recommended Headline:**
```
Staff SRE / Senior DevSecOps | 25M msg/day Platform | Kubernetes · Observability · Supply Chain Security
```

**Alternative (if currently job-searching actively):**
```
Staff SRE & DevSecOps Engineer | EKS · Splunk · Terraform | Open to Principal/Staff Roles
```

**Why this works:**
- "Staff SRE" matches the job title variants recruiters search
- "25M msg/day" is a scale signal that stops scrolling
- Three keyword clusters: Kubernetes (CKA tier), Observability (Splunk/OTel), Supply Chain Security (OWASP A03)

---

### About Section Structure

**Lead with impact, not biography.** Recruiters spend 8 seconds on About before deciding to read or close. Structure:

```
Paragraph 1 (Hook — 2 sentences):
I build reliability systems at scale. For 9 years at T-Mobile, I've owned the infrastructure 
reliability of a notification platform processing 25M messages per day for 100M+ subscribers — 
where a 10-minute outage affects real people in real emergencies.

Paragraph 2 (Breadth signal — 3-4 sentences):
My work spans three intersecting domains: SRE (SLO governance, incident command, chaos engineering), 
platform engineering (EKS-hosted microservices, developer tooling, golden paths), and DevSecOps 
(supply chain security, policy-as-code, secrets management). I lead a 15-person team and have driven 
reliability improvements reducing MTTD from [X] to [Y] minutes on a platform where every second matters.

Paragraph 3 (Unique angle — 2 sentences):
What makes my perspective distinctive: I came to reliability through systems thinking, not computer 
science theory. After 21 years across telecom, retail, insurance, banking, and energy, I know that 
the hardest reliability problems are organizational, not technical.

Paragraph 4 (Keyword-dense, scannable):
Technical domains: Kubernetes (EKS, CKA), Terraform, Splunk (MART/MLTK), OpenTelemetry, 
supply chain security (SBOM, SCA, Cosign), OPA/Gatekeeper, Python automation, CI/CD governance, 
RabbitMQ, Cassandra, Redis, Vault, CyberArk.

Paragraph 5 (CTA):
Currently exploring Staff SRE and Senior DevSecOps opportunities at companies where reliability is 
a competitive advantage. Open to conversations — reach me at [email].
```

---

### Skills Section — Priority Order

Feature these 15 skills in this exact order (most-searched first, strongest evidence first):

| Rank | Skill | Evidence Basis | Recruiter Search Volume |
|---|---|---|---|
| 1 | Kubernetes | EKS operational, T-Mobile platform | Very High |
| 2 | Site Reliability Engineering (SRE) | 9+ years, formal title | Very High |
| 3 | Splunk | Expert — MART, MLTK, dashboards | High (niche expert) |
| 4 | DevSecOps | Delivery governance, Vault, now building | High |
| 5 | Amazon EKS | Specific to T-Mobile platform | High |
| 6 | Terraform | Add after completing Associate cert | Very High |
| 7 | Python | Automation, MLTK, monitoring scripts | High |
| 8 | Incident Management | Formal IC role, postmortems, T-Mobile | High |
| 9 | CI/CD | Delivery governance, SAFe | Very High |
| 10 | Supply Chain Security | SBOM/SCA training — add after Week 1 | High (rising fast) |
| 11 | OpenTelemetry | Add after Week 2 OTel training | High |
| 12 | SLO/Error Budget Management | Documented T-Mobile governance | Medium-High |
| 13 | HashiCorp Vault | Operational Vault use | Medium-High |
| 14 | RabbitMQ | Core platform component | Medium (niche) |
| 15 | Platform Engineering | Reframe team leadership | High (rising fast) |

---

### Featured Section — What to Put There

Featured items appear above your experience — they are your "portfolio window."

**Recommended featured items (in order):**

1. **Architecture Article** (post on LinkedIn): "How We Designed Reliability for a 25M Message/Day Platform" — based on portfolio artifact from Day 14. This demonstrates Staff/Principal-level thinking publicly.

2. **GitHub Repository**: Link to a public GitHub repo with your Terraform module, OPA policies, or OTel Collector config from the training labs. Even a learning repo signals "I build things."

3. **Certification Badge**: Once you pass Terraform Associate, add the Credly badge directly to Featured.

4. **Technical Post**: "5 Things I Learned Implementing Supply Chain Security in a CI/CD Pipeline" — write after Week 1, post as a LinkedIn article. This signals current, relevant expertise.

5. **Snyk Learn Badge** (interim, before certs): Shows proactive skills development — recruiters notice this on active job-seekers.

---

### LinkedIn Learning Badges Strategy

LinkedIn Learning badges appear on your profile and are indexed by recruiters. Complete these in order and add each badge immediately:

1. **"DevSecOps Foundations"** (LinkedIn Learning, ~3 hours) — adds DevSecOps to verified skills
2. **"Kubernetes: Your First Project"** (LinkedIn Learning, ~4 hours) — adds Kubernetes badge
3. **"AWS Essential Training for Developers"** (LinkedIn Learning, ~5 hours) — adds AWS badge
4. **"Terraform Essential Training"** (LinkedIn Learning, ~3 hours) — bridges to cert
5. **Snyk Learn: "Application Security Fundamentals"** (Snyk, ~2 hours) — security-specific badge

**Pro tip**: LinkedIn Learning badges appear in the "Licenses & Certifications" section and are marked as verified. Recruiters using LinkedIn Recruiter filter by certifications — these show up in those filters even before you have the major certs.

---

### Activity Strategy

**Posting frequency**: 3x per week for the first 30 days to activate the algorithm, then 2x per week ongoing.

**Content mix (repeating rotation):**

| Post Type | Frequency | Example | Goal |
|---|---|---|---|
| Technical insight | 1x/week | "What I learned implementing OPA Gatekeeper on EKS — the gotchas nobody writes about" | Signal expertise to technical interviewers |
| Leadership/reliability story | 1x/week | "The postmortem that changed how my team thinks about incident ownership" | Signal Staff-level judgment |
| Learning milestone | 1x/week | "Passed Terraform Associate. Here are the 3 concepts I had to rebuild from scratch." | Signal active growth, attract recruiters |
| Industry commentary | As relevant | "OWASP Top 10:2025 lists supply chain security at A03. Here's what that means for SRE teams." | Position as thought leader |

**Content rules:**
- Always include 1 specific, concrete detail (a number, a tool name, a problem you solved)
- End with a question to drive comments ("What's your team's approach to X?")
- Use 3–5 hashtags: `#SRE #DevSecOps #Kubernetes #PlatformEngineering #OpenTelemetry`
- Never post job-seeking content (e.g., "looking for opportunities") — let your headline do that work silently

---

### "Open to Work" Strategic Use

**DO NOT use the public green banner.** It signals desperation and triggers lowball offers.

**Use instead**: "Share with recruiters only" setting in LinkedIn Open to Work.
- This makes your profile discoverable in LinkedIn Recruiter searches with the "Open to Work" filter
- Only recruiters using LinkedIn Recruiter can see it — not your current employer, not the general network
- Set your preferences: Job title = "Staff SRE, Principal SRE, Senior DevSecOps Engineer"; Location = Remote + specific metros; Start date = "In 3 months" (creates urgency without desperation)

**Recruiter InMail strategy**: When recruiters reach out via InMail:
- Respond within 24 hours (LinkedIn's algorithm rewards responsiveness and shows your profile more)
- Send a 3-sentence response: acknowledge the role, state your target TC range immediately, ask for a 20-minute call
- Do not accept or decline roles based on InMail alone — the 20-minute screen call is where you qualify them

---

<a name="section-6"></a>
## SECTION 6: CONTENT CREATION AGENT FRAMEWORK

> This section designs the orchestration of AI agents that produce, review, and publish your training content. Built for Claude Code or any agentic AI framework.

---

### System Overview

```
┌────────────────────────────────────────────────────────────────────┐
│                    CONTENT ORCHESTRATOR AGENT                       │
│              (Master scheduler + quality gate)                      │
└──────┬──────────────┬──────────────┬───────────────┬───────────────┘
       │              │              │               │
       ▼              ▼              ▼               ▼
 ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐
 │ CONCEPT  │  │   LAB    │  │  QUIZ &  │  │  LINKEDIN    │
 │  AGENT   │  │  AGENT   │  │ FLASHCARD│  │   CONTENT    │
 │          │  │          │  │  AGENT   │  │   AGENT      │
 └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬───────┘
      │              │              │               │
      └──────────────┴──────────────┴───────────────┘
                              │
                    ┌─────────▼──────────┐
                    │  ADVERSARIAL REVIEW │
                    │      AGENT          │
                    │  (debate + verify)  │
                    └─────────┬──────────┘
                              │
                    ┌─────────▼──────────┐
                    │  PUBLISHING AGENT  │
                    │  (format + deliver)│
                    └────────────────────┘
```

---

### Agent Definitions

#### Agent 1: Content Orchestrator

**Role**: Master scheduler, topic sequencer, dependency manager, quality gatekeeper

**What it produces**:
- Daily content brief: topic, depth level, target skill, dependencies (what the learner must know first)
- Quality gate decisions: approve/reject/revise content from downstream agents
- Progress tracking: what has been covered, what is pending, gaps in coverage
- Sequencing enforcement: ensures Lab Agent doesn't produce labs for concepts the Concept Agent hasn't covered

**Prompt pattern**:
```
You are the Content Orchestrator for Vishweshwar Chippa's SRE/DevSecOps training program.
Today is Day [X]. The learner has completed: [list of completed topics].
Current skill gaps (CRITICAL): Terraform, Supply Chain Security, CI/CD Pipeline Security.
Current skill gaps (MODERATE): Kubernetes internals, AWS IRSA, Platform Engineering.

Generate today's content brief for the following agents:
1. Concept Agent: Topic = [topic], Depth = [architect/hands-on/conceptual], Analogy domain = [middleware/operations/telecom]
2. Lab Agent: Build a lab for [topic] that runs on [laptop/AWS free tier/kind cluster], estimated time = [30/60/90 min]
3. Quiz Agent: Generate 5 questions escalating from conceptual to "debug this in prod"
4. LinkedIn Agent: Generate 1 post that demonstrates expertise in [topic] without sounding like studying

Quality gate: All content must pass the "T-Mobile anchor" test — can the learner connect this to their existing experience?
```

**Inputs**: Day number, completed topics list, upcoming interview dates
**Outputs**: Content briefs for all downstream agents, quality review decisions
**Feeds into**: All downstream agents

---

#### Agent 2: Concept Agent

**Role**: Technical explainer, analogy designer, vocabulary builder

**What it produces**:
- Concept explanations with real-world analogies anchored in middleware/operations/telecom experience
- Vocabulary tables: "industry term" → "your existing mental model equivalent"
- Depth-layered explanations: 30-second version, 2-minute version, 5-minute version
- STAR story scaffolds: how to frame this concept in a T-Mobile context

**Prompt pattern**:
```
You are the Concept Agent. Your learner is Vishweshwar Chippa:
- Middleware and systems thinking background (TIBCO, RabbitMQ, Cassandra)
- Splunk expert — use Splunk as the "known domain" for observability analogies
- Incident command expert — use incident management as the "known domain" for reliability concepts
- NOT a CS graduate — do not assume algorithmic or academic CS knowledge
- Needs: WHY before HOW, analogy before syntax, real-world before theory

Topic: [topic from Orchestrator brief]
Depth: [depth level]

Produce:
1. One paragraph analogy (use middleware/operations/telecom domain)
2. Vocabulary translation table (5-10 terms: market language → learner's existing mental model)
3. Three-depth explanation: 30-second / 2-minute / 5-minute versions
4. STAR story scaffold: "At T-Mobile, you can frame this as..." (fill with specific examples)
5. Two common interview questions and structuring guidance for answers
```

**Inputs**: Content brief from Orchestrator, learner profile (static)
**Outputs**: Concept guide (Markdown, saved to `Training/[domain]/[topic]-concept.md`)
**Feeds into**: Lab Agent (labs build on the concept), Quiz Agent (questions test the concept)

---

#### Agent 3: Lab Agent

**Role**: Hands-on exercise designer, environment builder, troubleshooting guide author

**What it produces**:
- Step-by-step lab instructions with exact commands (copy-paste ready)
- Environment setup guide (what tools to install, free tier constraints)
- Expected output at each step (so the learner knows if they're on track)
- Common failure modes and how to diagnose them
- "Stretch goal" variant for learners ahead of schedule

**Prompt pattern**:
```
You are the Lab Agent. Design a practical lab for:
Topic: [topic]
Learner level: operational expert, not a developer — needs working examples, not build-from-scratch
Environment constraint: laptop (Windows/Mac) + AWS free tier + free local tools (kind, Docker, Terraform CLI)
Time box: [30/60/90] minutes
Prerequisite: Learner has read [concept guide from Concept Agent]

Produce:
1. Environment setup (what to install — with exact commands)
2. Lab scenario (frame it as a real-world problem, not a tutorial exercise)
3. Step-by-step instructions (numbered, with exact commands and expected output)
4. Verification checkpoint: "You know you did this right when you see X"
5. Common failure: "If you see Y error, it means Z — fix it by..."
6. Cleanup instructions (free tier hygiene — avoid surprise AWS bills)
7. Stretch goal: one additional exercise for advanced practice

All code blocks must have inline comments explaining WHAT and WHY, not just HOW.
```

**Inputs**: Concept guide from Concept Agent, content brief from Orchestrator
**Outputs**: Lab guide (Markdown, saved to `Training/[domain]/[topic]-lab.md`)
**Feeds into**: Quiz Agent (lab experience informs scenario-based questions)

---

#### Agent 4: Quiz and Flashcard Agent

**Role**: Learning verification designer, retention system builder, interview simulation engine

**What it produces**:
- 5-question escalating quiz: concept → application → debug-in-prod progression
- 10 spaced-repetition flashcards (Anki format compatible)
- 1 "hostile interviewer" simulation: follow-up questions that probe the edges of knowledge
- "What you should be able to explain without notes" checklist

**Prompt pattern**:
```
You are the Quiz Agent. Generate assessment materials for:
Topic: [topic]
Learner has completed: [concept guide] + [lab]
Target role: Staff/Principal SRE and Senior DevSecOps ($180k-$280k)

Produce:
1. Five-question quiz (escalating difficulty):
   Q1: Recall — define [term] in your own words
   Q2: Application — given [scenario], what would you do?
   Q3: Design — design a [component/system] that satisfies [requirements]
   Q4: Debug — "you see [symptom] in production — what is your diagnostic process?"
   Q5: Trade-off — "compare [option A] vs. [option B] for [use case]"

2. Ten flashcards (front: question, back: answer):
   - 4 vocabulary/definition cards
   - 3 scenario/application cards
   - 2 "what's wrong with this" cards (show a misconfiguration or bad practice)
   - 1 "draw this architecture" card

3. Hostile interviewer simulation:
   Start with Q3 (Design), then probe: "Why not just use X instead?" / "What happens at 10x scale?" / "What would you do differently if you had to rebuild this today?"

4. "No-notes checklist": 5 things the learner should be able to explain from memory.
```

**Inputs**: Concept guide from Concept Agent, Lab guide from Lab Agent
**Outputs**: Quiz file (saved to `Training/[domain]/[topic]-quiz.md`), Flashcard file (saved to `Training/[domain]/[topic]-flashcards.md`)
**Feeds into**: Orchestrator (quiz results inform whether topic is "closed" or needs review)

---

#### Agent 5: LinkedIn Content Agent

**Role**: Thought leadership writer, personal brand builder, recruiter-magnet content creator

**What it produces**:
- 1 LinkedIn post per topic (250–400 words, technical but accessible)
- 1 LinkedIn article per domain (1000–2000 words, deep-dive, Featured section material)
- Hashtag recommendations
- Engagement hooks (ending questions, calls-to-action)
- Post scheduling recommendations

**Prompt pattern**:
```
You are the LinkedIn Content Agent for Vishweshwar Chippa, targeting Staff/Principal SRE and Senior DevSecOps roles.

Topic: [topic]
Learner's experience anchor: [specific T-Mobile or prior experience to reference]
Target audience: Technical recruiters and hiring managers at tech companies paying $180k-$280k+

Constraints:
- Write from first-person practitioner perspective, NOT as a student learning something new
- Frame as "here's what I learned from implementing this at scale" not "I just learned X"
- Include exactly ONE specific, concrete detail (a number, a tool name, a real problem)
- End with a question that invites comments from senior practitioners
- Do NOT use these overused LinkedIn phrases: "game-changer," "excited to share," "humbled," "blessed," "in today's fast-paced world"
- Use hashtags: #SRE #DevSecOps and 3 topic-specific tags

Produce:
1. Short-form post (250-300 words): hook, insight, specific detail, question
2. Hashtag set (5 tags, in order from most-searched to most-niche)
3. Best time to post: [day and time recommendation based on B2B tech audience]
4. One-line teaser for Stories/Feed preview
```

**Inputs**: Concept guide from Concept Agent, learner experience anchors (static profile)
**Outputs**: LinkedIn post drafts (saved to `Training/linkedin/[topic]-post.md`)
**Feeds into**: Adversarial Review Agent before publishing

---

#### Agent 6: Adversarial Review Agent

**Role**: Technical accuracy challenger, claim verifier, cliché detector, confidence calibrator

**What it produces**:
- Technical accuracy review: flags any factually incorrect or outdated claims
- Depth challenge: identifies where explanations are superficial vs. where they provide genuine depth
- Vocabulary audit: confirms correct use of industry terms
- Cliché/buzzword flag: catches generic statements that weaken credibility
- Confidence calibration: distinguishes "I know this" from "I learned this recently" vs. "I'm extrapolating"
- Suggested revisions with explanations

**Prompt pattern**:
```
You are the Adversarial Review Agent. Your job is to challenge and strengthen content before it reaches the learner or gets published. You are a senior Staff/Principal SRE with 15 years of experience at FAANG-tier companies. You do NOT give easy praise.

Review the following [concept guide / lab / quiz / LinkedIn post]:
[CONTENT]

Challenge on these axes:
1. TECHNICAL ACCURACY: Is every technical claim correct? Flag anything that is outdated, oversimplified, or wrong.
2. DEPTH: Would a Staff/Principal interviewer find this answer satisfying, or would they probe further? Where are the shallow spots?
3. VOCABULARY: Is every technical term used correctly in its industry-standard meaning?
4. CLAIMS WITHOUT EVIDENCE: Are there any assertions like "this is better" without explaining why?
5. REAL-WORLD VALIDITY: Would this actually work in a production environment at scale, or only in a tutorial?
6. LINKEDIN CREDIBILITY: (For posts only) Would a senior practitioner read this and think "this person knows their stuff" or "this person just learned this from a blog"?

For each issue found, provide:
- ISSUE: what is wrong
- SEVERITY: (blocks publication / weakens credibility / minor refinement)
- SUGGESTED FIX: specific rewrite recommendation

Final verdict: APPROVE / APPROVE WITH REVISIONS / REJECT AND REWRITE
```

**Inputs**: All content from Concept, Lab, Quiz, and LinkedIn agents
**Outputs**: Review report with specific issues and suggested fixes
**Feeds into**: Publishing Agent (only approved content proceeds)

---

#### Agent 7: Publishing Agent

**Role**: Final formatter, file organizer, delivery coordinator

**What it produces**:
- Final formatted Markdown files in the correct Training directory structure
- Daily digest email/notification: "Today's training materials are ready"
- LinkedIn post with correct formatting, hashtags, and scheduling recommendation
- Anki flashcard import file
- Progress tracker update: marks topic as complete in the master plan

**Directory structure maintained by Publishing Agent:**
```
C:\Work\Training\
├── CLAUDE.md
├── Training_Plan_Master.md        ← This file
├── portfolio\
│   ├── notification-platform-reliability.md
│   ├── devsecops-pipeline-design.md
│   └── k8s-security-incident-runbook.md
├── kubernetes\
│   ├── control-plane-concept.md
│   ├── control-plane-lab.md
│   ├── control-plane-quiz.md
│   └── control-plane-flashcards.md
├── terraform\
│   ├── state-management-concept.md
│   ├── state-management-lab.md
│   └── ...
├── devsecops\
│   ├── sbom-sca-concept.md
│   ├── sbom-sca-lab.md
│   └── ...
├── observability\
│   ├── melt-opentelemetry-concept.md
│   └── ...
├── aws\
│   ├── irsa-concept.md
│   └── ...
├── platform-engineering\
│   └── ...
├── interview-prep\
│   ├── mock-interview-k8s-aws.md
│   ├── mock-interview-devsecops.md
│   └── mock-interview-incident-command.md
└── linkedin\
    ├── supply-chain-security-post.md
    ├── slo-burn-rate-post.md
    └── ...
```

---

### Agent Orchestration Sequence (Daily Flow)

```
Day N morning:
┌─────────────────────────────────────────────────────────────────┐
│ Step 1: Orchestrator generates daily brief                      │
│   → Picks topic from Training Plan Master (Day N entry)         │
│   → Checks prerequisites (are prior topics complete?)           │
│   → Generates briefs for Concept, Lab, Quiz, LinkedIn agents    │
└──────────────────────────────┬──────────────────────────────────┘
                               │ (parallel execution)
                ┌──────────────┼──────────────────┐
                ▼              ▼                  ▼
       Concept Agent    Lab Agent           LinkedIn Agent
       (30 min)        (45 min)            (15 min)
                │              │                  │
                └──────────────┼──────────────────┘
                               │
                               ▼
                         Quiz Agent
                    (receives concept + lab)
                         (20 min)
                               │
                               ▼
                   Adversarial Review Agent
                   (reviews ALL four outputs)
                         (30 min)
                               │
                   ┌───────────┴──────────┐
                   ▼                      ▼
             APPROVED?              REJECTED?
                   │                      │
                   ▼                      ▼
           Publishing Agent      Returns to source agent
           (format + deliver)    with specific revision notes
                   │
                   ▼
         Files saved to Training\
         LinkedIn post queued
         Learner notified
```

---

### Content Debate Protocol

Before any technical content is published or used in interview prep, the Adversarial Review Agent runs a **structured debate**:

1. **Claim identification**: Extract all factual claims from the content
2. **Evidence check**: For each claim, identify: (a) source, (b) recency, (c) whether it holds at scale
3. **Red-team prompting**: "What would a senior FAANG engineer say is wrong about this?"
4. **Confidence rating**: CONFIRMED / LIKELY / UNCERTAIN / INCORRECT for each claim
5. **Vocabulary spot-check**: 5 randomly selected technical terms — are they used in industry-standard ways?

**Only content rated CONFIRMED or LIKELY proceeds to the learner.** UNCERTAIN content is flagged with a note: "Verify this against official documentation before using in an interview."

---

### Activation Instructions

To run this agent framework with Claude Code:

```bash
# In C:\Work\Training\, create a new session and run:
# "Run the Content Orchestrator for Day [X]. Generate today's training brief 
#  and then invoke the Concept Agent for [topic]."

# Claude Code will:
# 1. Read Training_Plan_Master.md to find Day X's topic
# 2. Read CLAUDE.md for learner profile
# 3. Generate the concept guide with analogies
# 4. Generate the lab instructions
# 5. Generate quiz questions
# 6. Generate a LinkedIn post draft
# 7. Run adversarial review on all content
# 8. Save approved content to the correct subdirectory
```

**Recommended daily session prompt:**
```
I'm starting Day [X] of my training plan. Read Training_Plan_Master.md and CLAUDE.md, 
then generate today's full training content package (concept guide, lab, quiz, and LinkedIn post) 
for the scheduled topic. Run adversarial review on all content before delivering it. 
Save all files to the appropriate Training subdirectory.
```

---

## APPENDIX: Quick Reference Tables

### Domain → Interview → STAR Anchor Quick Map

| Domain | Key Interview Question | T-Mobile STAR Anchor |
|---|---|---|
| Kubernetes | "Walk through what happens on kubectl apply" | EKS cluster for notification platform |
| AWS | "Explain IRSA" | EKS IRSA for RabbitMQ/Cassandra auth |
| DevSecOps | "Design a supply chain security pipeline" | Delivery governance → add security gates |
| Observability | "Design SLO + burn rate alerts" | 99.9% SLO on 25M msg/day platform |
| IaC | "How do you handle Terraform drift?" | Infrastructure change management during incidents |
| CI/CD Security | "Design a shift-left security gate" | Release governance pipeline → add scanning |
| Platform Eng | "What is a golden path?" | Internal tooling for 15-person SRE team |
| Incident Command | "Describe your postmortem process" | T-Mobile P1 incidents at subscriber scale |

### Vocabulary Cheat Sheet — Your Language → Market Language

| Your Current Language | Market/Recruiter Language |
|---|---|
| "MART framework" (Splunk) | "MELT framework" / "3-pillar observability" |
| "Splunk HEC" | "OTel Collector with Splunk exporter" |
| "AppDynamics traces" | "Distributed tracing" / "OpenTelemetry traces" |
| "Delivery governance" | "CI/CD pipeline security" / "shift-left security" |
| "SLO governance" | "Error budget management" / "SLO-based alerting" |
| "Kubernetes on EKS" | "EKS with managed node groups" / "Kubernetes at scale" |
| "Release orchestration" | "Deployment pipeline" / "GitOps" |
| "Vault/CyberArk management" | "Secrets management" / "zero-trust secrets architecture" |
| "Team incident command" | "Incident command system (ICS)" / "on-call culture" |
| "Platform migrations" | "Cloud-native migrations" / "lift-and-shift vs. re-architect" |

---

*Document generated: June 11, 2026 | Version 1.0 | Next review: July 11, 2026*
*Calibrated for: Staff SRE ($180k–$280k TC) and Senior DevSecOps Engineer roles at cloud-native organizations*
