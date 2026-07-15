# Phase 1: SRE Foundations

**Duration**: 10 weeks  
**Entry point**: Dev Lead or Senior Software Engineer with no SRE background  
**Exit**: Ready for on-call rotation; can contribute to postmortems and basic observability work

---

## What Phase 1 Builds

Phase 1 is about operational fluency, not operational mastery. By the end of these 10 weeks you should be able to function in an SRE team — you will not yet be running incidents, but you will be able to participate in them, read the dashboards, write the runbooks, and understand why things are structured the way they are.

The goal is **survival and contribution**, not leadership. Leadership starts in Phase 2.

---

## Prerequisites

Before starting Phase 1, you should have:

- 3+ years of software development experience (any language, any stack)
- Comfort with a Linux terminal — you do not need to be an expert, but you should not be afraid of it
- Basic networking knowledge: what a DNS lookup does, what a TCP connection is, what HTTP status codes mean
- A development environment you can run containers in (Docker Desktop or WSL2 equivalent)

---

## Week-by-Week Curriculum

### Week 1: Terraform and Infrastructure as Code

**Lab content**: `1-phase-foundations/1.1-terraform-iac/`

What you are building: the foundational skill for managing cloud infrastructure reproducibly. Every production system an SRE is responsible for was built with some form of IaC. You need to be able to read it, run it, and fix it when it drifts from intended state.

Key skills this week:
- Terraform state: what it is, why it matters, what happens when it is lost or corrupted
- Remote state: S3 backend + DynamoDB locking — the production-safe pattern
- Modules: writing reusable infrastructure units, input variables, output values
- `terraform plan` / `apply` / `destroy` — the three-command lifecycle
- Drift detection: what it is and why SREs care more than developers do
- IaC security: secrets in state files (the problem), Vault integration (the solution)

**Paired reading**: `1-phase-foundations/1.0-vocabulary/1.0.7-cicd-safe-release.md`

Read this before the lab. It gives you the reliability context — IaC is not just a developer convenience, it is a reliability and repeatability guarantee for the systems you will be responsible for.

---

### Week 2: DevSecOps — Supply Chain Security and Pipeline Security

**Lab content**: `1-phase-foundations/1.2-devsecops/`

What you are building: an understanding of how code moves from a developer's laptop to production, and where security and reliability risks enter that pipeline.

Key skills this week:
- CI/CD pipeline anatomy: stages, gates, artifacts, environments
- Software Bill of Materials (SBOM): what it is, why regulators care, tools (Syft, Grype)
- SAST (Semgrep) and DAST: where each runs in the pipeline
- Container image scanning: vulnerability tiers, when to block a deployment
- Secrets scanning: why secrets in code is a P1 waiting to happen
- Policy-as-code: OPA/Rego basics — gate a pipeline with a policy rule
- Supply chain: Cosign/Sigstore for artifact signing and provenance
- Shift-left security: what it means, why SREs care about it

**Paired reading**: `1-phase-foundations/1.0-vocabulary/1.0.9-security-compliance-devsecops.md`

Read this first. It maps DevSecOps concepts to SRE reliability concerns — the two disciplines overlap more than most people expect.

---

### Week 3: Kubernetes Fundamentals and Pod Lifecycle

**Lab content**: `1-phase-foundations/1.3-kubernetes/`

What you are building: the operational mental model for how Kubernetes manages workloads. You are not learning to write YAML from scratch — you are learning to read it, debug it, and understand what Kubernetes is doing and why.

Key skills this week:
- Cluster anatomy: nodes, control plane, etcd, API server
- Pod lifecycle: Pending → Running → Succeeded/Failed/CrashLoopBackOff
- Workload types: Deployment, DaemonSet, StatefulSet, Job, CronJob — when to use which
- Service types and how traffic reaches a pod
- Health probes: liveness, readiness, startup — why they matter for reliability
- Deployment strategies: rolling update, blue/green, canary — the reliability trade-offs of each
- Basic `kubectl` operations: get, describe, logs, exec, port-forward, rollout
- RBAC basics: ServiceAccounts, Roles, RoleBindings — who can do what to which resource
- Admission webhooks: what they are and why they matter for security and policy enforcement
- IRSA (IAM Roles for Service Accounts): the production-safe way to give pods AWS permissions

**Paired reading**: `1-phase-foundations/1.0-vocabulary/1.0.6-kubernetes-platform-reliability.md`

---

### Week 4: AWS Core Services and GitOps

**Lab content**: `1-phase-foundations/1.4-aws-gitops/`

What you are building: working knowledge of the AWS services that appear in most enterprise SRE environments, plus the GitOps operational model for Kubernetes deployments.

Key skills this week:
- EC2: instance types, security groups, key pairs, AMIs
- EKS: what managed Kubernetes looks like, how it differs from self-managed
- S3: buckets, objects, access control, versioning — artifacts, state, and backups
- VPC: subnets, routing tables, NAT gateways, security groups vs. NACLs
- IAM: roles, policies, IRSA — the foundation of secure cloud access
- CloudWatch basics: metrics, alarms, log groups
- GitOps model: Git as the source of truth for infrastructure and application state
- ArgoCD: application sync, health status, drift detection — how GitOps works in practice
- Multi-account IAM and SCPs: what AWS Organizations brings to enterprise security governance

**Paired reading**: `1-phase-foundations/1.0-vocabulary/1.0.6-kubernetes-platform-reliability.md` (EKS sections)

---

### Week 5: Observability — Metrics, Logs, Traces, and Alerting

**Lab content**: `1-phase-foundations/1.5-observability/`

What you are building: the ability to see what a system is doing and reason about it. Observability is the core SRE skill. Without it, you are guessing. With it, you are investigating.

Key skills this week:
- The three pillars: metrics (what is happening), logs (what happened), traces (how it happened)
- Metrics taxonomy: counters, gauges, histograms, summaries — what each measures and when to use it
- Alerting design: symptom-based vs. cause-based, alert fatigue, actionable alerts
- Splunk: search queries, dashboards, saved searches, alert configuration
- Datadog: metrics explorer, log management, APM basics, monitors
- OpenTelemetry: what it is, why it matters, how it unifies the three pillars
- Reading a flame graph and understanding where latency lives
- Observability-as-code: SLO definitions and burn rate alert math

**Paired reading**: `1-phase-foundations/1.0-vocabulary/1.0.4-observability-telemetry.md`

Read this before the lab week. Observability has a vocabulary (RED, USE, the Four Golden Signals) that makes the tooling make sense.

---

### Week 6: Platform Engineering and Internal Developer Platforms

**Lab content**: `1-phase-foundations/1.6-platform-engineering-lab/`

What you are building: an understanding of how platform teams reduce cognitive load for developers, and why this matters for reliability.

Key skills this week:
- What an Internal Developer Platform (IDP) is and why organizations build them
- Backstage: software catalog, templates, TechDocs, plugins — and the real cost of building it (3–5 dedicated engineers Year 1)
- DORA metrics: Deployment Frequency, Lead Time for Changes, Change Failure Rate, Time to Restore, Rework Rate (the 5th metric added in 2025) — how to measure and improve each
- Team Topologies: stream-aligned teams, platform teams, enabling teams — the organizational pattern behind effective platform engineering
- Golden paths: how platform teams make the right way the easy way
- Self-service provisioning and why it reduces toil

**Paired reading**: `1-phase-foundations/1.0-vocabulary/1.0.7-cicd-safe-release.md`

---

### Week 7: Interview Readiness and Leadership Communication

**Lab content**: `1-phase-foundations/1.7-interview-readiness/`

What you are building: the ability to articulate your SRE knowledge in interview and stakeholder contexts, and the leadership communication patterns that separate a contributing SRE from a senior one.

Key skills this week:
- STAR method for behavioral questions anchored to your operational experience
- SRE interview question patterns: the "walk me through an incident" question, the "design an SLO" question, the "debug this system" question
- Vocabulary translation: map SRE jargon to your existing operational experience so you can speak it fluently under pressure
- Leadership competencies: influence without authority, operational decision-making under ambiguity, cross-functional coordination
- Director-track foundations: what Principal SRE and Director-level roles expect that Senior SRE roles do not
- Mock interview practice: time yourself, answer out loud, record and review

**Domain Framework Preview** (read the README of each — do not read full chapters yet):

- `2-phase-sre-practitioner/2.1-incident-management/README.md`
- `2-phase-sre-practitioner/2.3-service-level-management/README.md`

These two README files give you a preview of what Phase 2 is built on. You are not ready for the full frameworks yet — but you should understand what they are and why they exist before Phase 2 starts.

---

### Week 8: Certification Prep, Capstone, and Phase Transition

**Lab content**: `1-phase-foundations/1.8-certification/`

What you are building: synthesis of everything in Phase 1, plus the foundation for Phase 2 entry.

This week's structure:
- Certification preparation (CKA, Terraform Associate, AWS SAA — depends on your target role)
- Capstone exercise from `3-phase-principal-sre/3.5-capstone/` — a scenario-based exercise that pulls together observability, Kubernetes, AWS, and incident basics
- Self-assessment against Phase 1 competency gates (see below)
- Review gaps, return to the relevant week's content where needed
- Begin `job-search/` if you are actively looking — the Phase 1→2 transition is a natural inflection point

**Paired reading**: `1-phase-foundations/1.0-vocabulary/1.0.5-distributed-systems-resilience.md` (finish if not complete)

---

### Week 9: AI Engineering Foundations for SRE

**Lab content**: `1-phase-foundations/1.9-ai-fundamentals/`

What you are building: the baseline AI literacy that is now expected at Senior SRE and above. AI tooling is embedded in every domain — observability, incident management, capacity planning. This week gives you the conceptual foundation before Week 10 goes hands-on.

Key skills this week:
- LLM fundamentals: what a large language model is, how tokens work, why context window size matters for operational tools
- Prompt engineering for SRE use cases: writing prompts for runbook generation, incident summaries, log analysis
- RAG (Retrieval-Augmented Generation): how to ground AI output in your actual runbooks and documentation
- AI-assisted incident management: how AIOps tools use ML for anomaly detection, noise reduction, and correlation
- Bedrock and Azure OpenAI: the managed LLM APIs most enterprises use
- Cost awareness: AI API costs at scale, prompt caching strategies, token optimization

**Paired reading**: `1-phase-foundations/1.0-vocabulary/1.0.11-ai-for-sre.md`

Read this first — it gives you the critical perspective on where AI genuinely augments SRE practice vs. where it is hype.

---

### Week 10: AI Platform Engineering and LLMOps

**Lab content**: `1-phase-foundations/1.10-ai-production/`

What you are building: hands-on experience running AI in production-like conditions, including the reliability patterns that distinguish a production AI system from a prototype.

Key skills this week:
- Multi-agent systems: how AI agents collaborate to execute complex operational workflows
- MCP (Model Context Protocol): how AI models interact with external tools and data sources
- AI observability: monitoring for model drift, hallucination rate, output consistency — SLOs for AI systems
- LLMOps: the operational discipline for LLM-based systems (distinct from MLOps for traditional ML)
- Guardrails: how to implement content safety and output validation for production AI
- Vector databases: how embeddings-based search works — the retrieval layer of RAG systems
- AI cost governance: prompt caching, model routing, tier selection — the FinOps layer for AI workloads

**Paired reading**: `1-phase-foundations/1.0-vocabulary/1.0.11-ai-for-sre.md` (return after Week 9 with practical context)

---

## Phase 1 Competency Gates

You are ready for Phase 2 when you can do all of the following. These are not theoretical — demonstrate them through real work or lab exercises.

| Gate | What "done" looks like |
|------|----------------------|
| On-call contribution | Can acknowledge, assess severity, and escalate a P2 incident — know who to page and what information to provide |
| SLO basics | Can write a basic SLO (target, measurement window, error budget) for a service you own or work on |
| Runbook authoring | Can write a runbook for a known failure mode — one that another engineer could follow without asking you questions |
| Observability query | Can open Splunk or Datadog and write a query that identifies a latency anomaly or error spike in a service you are responsible for |
| DORA literacy | Can explain all five DORA metrics and state your current team's approximate position on each |
| Kubernetes operations | Can perform a Kubernetes rolling deployment, watch it succeed, and roll it back if it fails — using `kubectl` |
| IaC literacy | Can read a Terraform plan, identify what will change in production, and articulate the reliability risk of each change |
| AI awareness | Can explain what a RAG system is, what hallucination means, and name two SRE use cases where AI augments (not replaces) human judgment |

If you cannot hit one or two of these, do not try to power through to Phase 2. Return to the specific week that covers that skill, do the lab, and re-evaluate.

---

## What Phase 1 Does Not Cover

Phase 1 deliberately omits:
- Full incident command (that is Phase 2)
- SLO design beyond basics (that is Phase 2)
- Root cause analysis methodology (that is Phase 2)
- Change management and CAB process (that is Phase 2)
- Performance engineering (that is Phase 3)
- Director-level people management (that is Phase 4)

You will feel the pull to jump ahead. Resist it. The frameworks in Phase 2 assume Phase 1 competency. Reading Phase 2 content without that foundation makes it feel abstract when it should feel immediately applicable.
