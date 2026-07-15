# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose of This Repository

This is a personal training and interview-prep workspace for Vishweshwar Chippa, an SRE Manager / Principal SRE with 21+ years of experience. The goal is structured skill-building for DevSecOps and SRE roles at cloud-native organizations.

## Who This Is For

**Background**: IIT-BHU graduate, non-CS degree (Metallurgy). Self-taught technologist through on-the-job experience across telecom, retail, insurance, banking, and energy verticals. Strong delivery leadership, middleware architecture, and observability expertise. Currently at T-Mobile managing a 15-person SRE team on a 25M msg/day notification platform.

**Learning style**: Needs syntax scaffolding for scripting; understands architecture and systems thinking well. Explain code with context — *why* before *how*. Avoid assuming CS fundamentals (e.g., Big-O notation) but *do* assume deep operational and systems intuition.

## Current Skill Stack (Known Strengths)

- **Observability**: Splunk (expert — MART framework, ML/MLTK, dashboards), AppDynamics, Grafana
- **Platforms**: Kubernetes (EKS), AWS, Docker, PCF, RabbitMQ, Kafka-adjacent
- **Data stores**: Cassandra, Redis, MongoDB, MySQL
- **Languages**: Python (automation/monitoring), Java, Kotlin, JavaScript
- **Delivery**: SAFe, Agile, CI/CD, release orchestration, incident command, postmortems, SLO/SLI governance
- **Security**: Vault, CyberArk, IAM — conceptual and operational use
- **AI/ML**: Anomaly detection (Python + Splunk MLTK), GitHub Copilot workflows

## Training Focus Areas (DevSecOps/SRE Interview Prep)

Topics interviewers probe hardest for senior SRE/DevSecOps roles:

1. **Cloud-native IaC** — Terraform, Pulumi (hands-on resource authoring, state management, drift)
2. **Kubernetes deep-dives** — controllers, scheduling, RBAC, network policies, HPA/VPA, admission webhooks
3. **CI/CD security (DevSecOps)** — SAST/DAST integration, secrets scanning, supply chain (SBOM, Sigstore), policy-as-code (OPA/Gatekeeper)
4. **Observability as code** — SLO definitions, error budget burn alerts, OpenTelemetry instrumentation
5. **Incident command** — structured blameless postmortems, MTTR/MTTD metrics, chaos engineering basics
6. **Cloud security fundamentals** — IAM least-privilege, network segmentation, zero-trust, CSPM tools
7. **Platform engineering patterns** — golden paths, internal developer platforms, backstage
8. **Python scripting for SRE** — writing runbooks-as-code, automation scripts, operator patterns

## Program Structure: 10-Week Program

**Weekly schedule**: Weekdays 2-3 hrs, Weekends 5 hrs = ~20 hrs/week = 200 hrs total over 10 weeks.

| Week | Sprint | Primary Domain |
|---|---|---|
| 1 | Terraform Foundation | IaC — state, modules, first real apply |
| 2 | Supply Chain Security | SBOM/SCA/OPA/SAST/Cosign/SLSA |
| 3 | Kubernetes Internals | Control plane, RBAC, webhooks, IRSA, Karpenter |
| 4 | AWS Depth + GitOps | Organizations/SCPs, ArgoCD, FinOps, security services |
| 5 | Observability Translation | OTel, MELT, burn rate math, Prometheus, obs-as-code |
| 6 | Integration + Portfolio | 3 capstone projects → public GitHub |
| 7 | Interview Readiness | Mock interviews, STAR stories, Director/VP loops |
| 8 | Polish + Active Search | LinkedIn, certs, resume variants, active applications |
| 9 | AI Engineering Foundations | LLM ops, RAG, Bedrock, Azure OpenAI, AI platforms |
| 10 | AI Platform Engineering | Agents, MCP, AI observability, guardrails, multi-agent |

**Buffer**: 2 additional weeks exist for P1 incidents or slow weeks. Expected, not failure.

## Lab Environment

**Platform**: Windows 11 + WSL2 (confirmed installed). All lab commands run inside WSL2 terminal.

**Cloud**: AWS account is being set up for direct hands-on training. **All labs use real AWS resources** — not local simulators like LocalStack. Free tier + small paid resources (~$5–20/month during active training weeks).

**Lab command rules**:
- All commands assume WSL2 Ubuntu terminal — bash heredocs, `curl | sh`, `chmod`, `apt install` all work
- AWS CLI configured inside WSL2 with a dedicated IAM training user (least-privilege)
- `kubectl` and `eksctl` installed in WSL2
- Terraform CLI installed in WSL2
- Docker Desktop with WSL2 backend (or `docker` inside WSL2 directly)

**AWS Training Account Setup** (do once before Week 1):
- Create AWS account or use existing; enable MFA on root
- Create IAM user `training-admin` with AdministratorAccess (scoped to training account only — never production)
- Configure AWS CLI: `aws configure` with training-admin credentials
- Set a billing alert at $25/month — training should stay well under this
- Enable AWS Cost Explorer to track spend by service
- Regions: use `us-east-1` for all labs unless a topic specifically requires multi-region

**AWS services used across the 8-week program** (know what you're provisioning):
- Week 1 (Terraform): S3 bucket + DynamoDB table (remote state) — ~$0
- Week 3 (K8s): EKS cluster — ~$0.10/hr for control plane; use `eksctl delete cluster` after each session
- Week 4 (GitOps): ECR, IAM roles for IRSA — ~$0
- Week 5 (Observability): CloudWatch, ADOT collector — minimal cost
- Week 6 (Portfolio): Full stack — budget ~$5 for the week; tear down after
- **Always run `terraform destroy` or `eksctl delete cluster` at end of each session**

## Textbook-Workbook Learning Model

Every topic follows this gated sequence — do NOT deliver all artifacts at once:

1. **READ**: Concept guide (with analogy + vocabulary translation table)
2. **THINK**: 3-question comprehension check — must pass 2/3 before lab unlocks
3. **TEST**: Lab with `EXPECTED_OUTPUT` at every major step (this IS the answer key)
4. **PROJECT**: Capstone with `ANSWER_KEY.md` available immediately (not hidden)
5. **PROCEED**: Only after learner confirms lab completion + can explain tradeoffs in 3 min

**Canonical resources** (use these as primary references, not self-contained Claude explanations):
- Terraform: *Terraform: Up & Running* (Brikman, 3rd ed.) + KodeKloud Terraform Associate
- K8s: *Kubernetes in Action* (Luksa, 2nd ed.) + KodeKloud CKA
- Observability: *Observability Engineering* (Majors/Fong-Jones) + Google SRE Workbook (free)
- AWS: Adrian Cantrill SAA-C03 course
- Full list: see `resource-library.md`

## Target Roles & Compensation

- **Target titles**: Director of SRE, VP of Platform Engineering, Director of DevSecOps, Head of Site Reliability
- **Phase 1** (now): Startup/mid-size (Series B–D, 50–500 people) — land the Director title
- **Phase 2** (18–36 months): FAANG/enterprise Director with title already on resume
- **Target comp Phase 1**: $200K–$270K base + equity
- **Target comp Phase 2**: $280K–$380K base | $450K–$600K total comp

## H1B Status (Affects Job Search Strategy)

- H1B active, I-140 approved (2016). **Transfer portability**: can start new job the day I-129 is FILED.
- Disclose H1B status AFTER technical screen, BEFORE offer — never as first disclosure.
- Negotiate premium processing coverage (~$2,805) as part of offer package.
- Phase 1 companies: verify Series B+ minimum, 18+ months runway, H1B history before first call.
- Best Phase 2 sponsors: AWS, Google, Microsoft, Meta, Adobe, Capital One, Salesforce.
- See `job-search/01_Application_Tracker.md` for active pipeline status.

## File Layout

```
Training/
├── CLAUDE.md                    # This file — read first in every session
├── Training_Plan_Master.md      # Full program: market intel, gap analysis, 8-week plan, cert roadmap
├── resource-library.md          # Canonical books, courses, YouTube per domain (research-backed)
├── session-start-prompt.md      # Paste this at start of EVERY Claude session
├── progress-log.md              # Weekly confidence scores, calibration interview debrief
│
├── research/                    # Multi-agent research outputs — reference during training
│   ├── README.md
│   ├── research-01-job-market-intelligence.md
│   ├── research-02-learning-resources.md
│   ├── research-03-program-review-and-gap-analysis.md
│   ├── research-04-interview-intelligence.md
│   └── research-05-enterprise-security-trends.md
│
├── learning/                    # Skill-domain labs, concepts, flashcards (one folder per domain)
│   ├── cloud-labs/              # Terraform + Azure + AKS hands-on labs
│   ├── kubernetes/              # K8s internals, RBAC, webhooks
│   ├── devsecops/               # Supply chain, SAST/DAST, OPA
│   ├── observability/           # OTel, MELT, SLO burn rate
│   ├── aws/                     # AWS deep-dives, IRSA, GitOps
│   └── platform-engineering/   # IDP, golden paths, Backstage
│
├── sre-framework/               # Generic SRE reference (not T-Mobile-specific)
│   ├── concepts/                # 16 topic guides: SLO, incident mgmt, K8s, CI/CD, etc.
│   ├── ai-agents/               # AI adoption, workforce transformation docs
│   └── platform-teams/         # Platform team org patterns
│
├── job-search/                  # All job application execution (was: JobSearch/)
│   ├── 00_README.md
│   ├── CLAUDE.md
│   ├── 00_Master_Resume.md
│   ├── 01_Application_Tracker.md
│   └── companies/               # 17 target companies × 4-5 docs each
│       └── 01_LexisNexis_RELX/
│           └── dnd-research/    # Merged from DNDSREFrameworkV2/LexusNexus/
│
├── Resume/                      # Source .docx resume files (5 variants)
│
├── dnd-platform/                # T-Mobile DND platform ops reference (was: DNDSREFrameworkV2/)
│   ├── grafana/                 # RabbitMQ Grafana dashboard JSONs
│   ├── rabbitmq/                # RMQ cluster state exports
│   ├── onenote-exports/         # OneNote knowledge captures
│   ├── deployment-checklists/
│   ├── usecases/
│   ├── cache-clear/
│   └── metrics.md               # Prometheus metrics dump
│
└── reference/                   # Passive reference material (PDFs, tutorials)
    ├── tutorials/               # SRE tutorial PDFs (was: SRE Tutorials/)
    ├── AI_Learning_Roadmap_90DayPlan.pdf
    └── Expanded_Leadership_Playbook.pdf
```

**Old folder names → new locations** (for muscle memory):
- `Teraform/` → `learning/cloud-labs/`
- `SREFRamework/` → `sre-framework/`
- `DNDSREFrameworkV2/` → `dnd-platform/` + `sre-framework/concepts/`
- `SRE Tutorials/` → `reference/tutorials/`
- `JobSearch/` → `job-search/` (kept as-is, original still present)

## Updated Folder Structure (July 2026)

The folder structure in the "File Layout" section above reflects the original design. The actual current structure is:

```
Training/
├── CLAUDE.md, README.md, session-start-prompt.md, progress-log.md
├── 00-program/          ← planning docs: training-plan-master.md, resource-library.md, glossary.md, etc.
├── learning-path/       ← curriculum navigation: 4 phases, 3 gap analyses, content-map, quick-start
├── concepts/            ← knowledge library: 13+ domain frameworks across 6 tiers
│   ├── [existing frameworks at root: incident-management, problem-management, etc.]
│   ├── sre-core/        ← Tier 1 index
│   ├── platform-engineering/ ← Tier 2 index
│   ├── director-level/  ← Tier 3 index
│   ├── infrastructure/  ← Tier 4: VMware, Network, DB Reliability, Service Mesh, Datacenter
│   ├── technical-sre/   ← Tier 5: FinOps, Zero Trust, On-Call, SIEM, Capacity, Multi-Cloud
│   ├── leadership-advanced/ ← Tier 6: Board Comms, OKRs, Change Mgmt, Labor Law, P&L
│   ├── cookbook/        ← vocabulary and mental models
│   └── textbook/        ← proprietary SRE metrics
├── weeks/               ← Weeks 1-10 lab content + tracker
├── SRECapstone/         ← exercises, scenarios, solutions
├── ToolsPortfolio/      ← 3 portfolio projects
└── job-search/          ← application tracker, company research
```

Note: Existing domain framework folders (incident-management/, problem-management/, etc.) remain at concepts/ root to preserve cross-references. Tier subfolders (sre-core/, platform-engineering/, director-level/) are navigation indexes only. New gap-fill frameworks live inside their tier subfolders.

## Working With Claude in This Repo

- **Every session**: Paste `session-start-prompt.md` at start. This gives Claude current week, completed topics, today's goal.
- Lead every explanation with a real-world analogy — priority: middleware (TIBCO/RabbitMQ) → incident command → delivery governance → physical/operational analogies. Never lead with CS theory.
- Provide vocabulary translation tables: industry term → learner's existing mental model equivalent.
- Three depths for every concept: 30-second version, 2-minute version, 5-minute version.
- Frame interview answers using STAR method anchored to T-Mobile experience.
- Drills escalate: concept check → scenario → "debug this in prod" → trade-off discussion.
- When writing scripts or IaC, include inline comments explaining WHAT and WHY each block achieves.
- Include Staff/Principal leadership lens on every topic: how does a team lead govern this vs. how an IC implements it? How does AI change this domain?
- Include sector functional knowledge where relevant: fintech compliance, telecom BSS/OSS, retail reliability patterns.

## Progress Tracking

- Confidence scale: 1=read it, 2=can define, 3=can explain why, 4=can explain tradeoffs, 5=can teach it
- **Interview threshold**: CRITICAL gaps at 4+, MODERATE gaps at 3+ before top-tier applications
- **Forcing function**: First calibration application by Week 6, regardless of readiness
- Weekly ritual: Sunday evening, 30 min — confidence calibration + timed drill + decay check
- Track all progress in `progress-log.md`
