# Research Report 03 — Program Review, Gap Analysis & Risk Register
## Full Findings from the Comprehensive Program Audit

**Source**: 68KB agent review grounded in Training_Plan_Master.md (1,939 lines) and CLAUDE.md
**Date**: June 11, 2026
**Purpose**: Reference during any session where training content is being designed, adjusted, or generated

---

## PART A: GAP ANALYSIS — What Exists vs. What Was Needed

### Gap 1: Schedule Was Fiction → FIXED
**Original problem**: 30-day plan required 4–6 hrs/day. Actual availability: 2–3 hrs weekday, 5 hrs weekend (~20 hrs/week).
**Fix applied**: Redesigned as 8-week program. See `Training_Plan_Master.md` Section 3 for the rescaled sprint structure.
**Sprint map**:
| Week | Sprint | Primary Domain |
|---|---|---|
| 1 | Terraform Foundation | IaC — state, modules, first real AWS apply |
| 2 | Supply Chain Security | SBOM/SCA/OPA/SAST/DAST |
| 3 | Kubernetes Internals | Control plane, admission webhooks, RBAC, IRSA |
| 4 | AWS Depth + GitOps | IRSA deep dive, multi-account IAM, ArgoCD |
| 5 | Observability Translation | OTel Collector, MELT, burn rate math, SLO YAML |
| 6 | Integration + Portfolio | 3 capstone projects → public GitHub |
| 7 | Interview Readiness | Mock interviews + calibration applications |
| 8 | Polish + Active Search | LinkedIn + cert registration + top-tier apps |

**Buffer**: 2 extra weeks exist for P1 incidents. Use them — that's what they're for.

---

### Gap 2: All Labs Were Linux/Mac Only → FIXED
**Original problem**: Every lab used `curl | sh`, `brew install`, bash heredocs — none work in PowerShell.
**Fix applied**: WSL2 confirmed installed. All labs now target WSL2 Ubuntu bash. AWS account being set up for real infrastructure.
**Rule**: NEVER generate `brew install` or PowerShell-only commands for lab steps.

---

### Gap 3: No Resource Curation → FIXED
**Fix applied**: `resource-library.md` created with every domain's canonical textbook + primary course + supplementary reads + thought leaders. Research-backed (107-agent verification).

---

### Gap 4: No AI + Leadership Thread → PARTIALLY FIXED
**Status**: Staff/Principal lens tables exist in `Training_Plan_Master.md` Section 1 per domain. Agent framework not yet calibrated.
**What still needs to happen**: Each domain's concept guide must include a "Staff/Principal Lens" block covering:
- How a team lead *governs* this vs. how an IC *implements* it
- How AI changes this domain in 2026
- Executive communication script (how you explain this to a VP/CTO in 60 seconds)

---

### Gap 5: No Progress Measurement → FIXED
**Fix applied**: `progress-log.md` created with weekly confidence scoring (1–5 scale), timed drill ritual, decay check, and interview readiness meter.
**Weekly ritual**: Sunday evening, 30 minutes. Confidence calibration → timed drill → decay check → interview readiness meter.
**Threshold to interview**: CRITICAL gaps at 4+, MODERATE gaps at 3+.

---

### Gap 6: No H1B Strategy → FIXED
**Fix applied**: H1B guidance in CLAUDE.md, progress-log.md H1B tracker, and program_review.md memory file.
**Key facts**:
- H1B transfer portability: can start new job the day I-129 is FILED (not approved)
- Disclosure timing: after technical screen, before offer, never first
- Premium processing: ~$2,805, negotiate as part of offer at major employers
- Best sponsors: AWS, Google, Microsoft, Meta, Databricks, Snowflake, Verizon

---

### Gap 7: Agent Framework Not Gated → DOCUMENTED, NOT YET IMPLEMENTED
**Current state**: Agent prompts exist in Training_Plan_Master.md Section 6. Not yet restructured for textbook-workbook gating.
**Required sequence**: READ → 3-question comprehension check (2/3 to pass) → LAB with EXPECTED_OUTPUT at every step → CAPSTONE with ANSWER_KEY.md → proceed.
**When to implement**: When generating Week 1 content.

---

### Gap 8: Portfolio = Markdown Files, Not GitHub Repos → NOT YET DONE
**Required**: 3 public GitHub repositories with working code + ANSWER_KEY.md.
**Projects**:
1. `secure-iac-pipeline` — Terraform + OPA Conftest + GitHub Actions OIDC
2. `observable-sre-platform` — OTel Collector + Prometheus + Grafana + SLO burn rate alerts
3. `k8s-security-hardening` — OPA Gatekeeper + Falco + NetworkPolicies + intentional violations
**When**: Week 6 (Integration + Portfolio sprint).

---

### Gap 9: Cert Timeline Disconnected → NOTED
**Problem**: Terraform Associate listed for "Weeks 1–4" but only ~12 hours of Terraform in the plan. Exam requires 30+ hours of prep.
**Fix**: Don't register for Terraform Associate until Week 6 at earliest. KodeKloud course + practice exams = ~30 hours total needed.

---

### Gap 10: No Spaced Repetition → PARTIALLY ADDRESSED
**Fix applied**: Decay check in weekly ritual (Sunday). Review one topic from 2 weeks ago. If confidence dropped >1 point, add to revisit queue.
**Not yet built**: Anki deck setup guide. Add to Week 1 setup.

---

## PART B: BLIND SPOTS IDENTIFIED

### Blind Spot 1: H1B Constraints (CRITICAL)
See Gap 6 above. The full H1B strategy is now documented.

**H1B Sponsor Reliability Table**:
| Company | H1B Sponsor History | Transfer Friendly | Notes |
|---|---|---|---|
| AWS (Amazon) | Excellent | Yes | Top H1B filer; robust legal team |
| Google Cloud | Excellent | Yes | Top 5 H1B sponsor |
| Microsoft Azure | Excellent | Yes | Well-established process |
| Meta | Good | Yes | Active sponsor; executive transfers common |
| Netflix | Variable | Sometimes | Smaller H1B volume; slower |
| Stripe | Variable | Sometimes | Has sponsored; verify per role |
| Databricks | Good | Yes | Growing sponsor, Series G+ |
| Snowflake | Good | Yes | Public company; established program |
| HashiCorp/IBM | Variable | Variable | Post-IBM acquisition uncertainty |
| Coinbase | Inconsistent | Sometimes | Crypto sector variability |
| Verizon | Good | Yes | Telecom sector familiar with H1B |
| Comcast | Good | Yes | Large enterprise; established |

---

### Blind Spot 2: Cognitive Load Reality
Managing a 15-person SRE team on a 25M msg/day platform. A single P1 incident wipes out 2 study days. No recovery mechanism in original plan.
**Mitigation**: 2 buffer weeks in the 8-week program. Build the "incident contingency" mindset: a week with a P1 is Week 1 of the buffer, not failure.

---

### Blind Spot 3: The "Boil the Ocean" Trap
8 domains + 5 certifications + LinkedIn + portfolio + applications. This is a 6-month program, not 30 days.
**Mitigation**: Hard-freeze the domain list. New ideas go to a "backlog" section, not the active sprint.

---

### Blind Spot 4: Technology Decay Risk
| Item at risk | Decay speed | How to check |
|---|---|---|
| OWASP Top 10 version/numbering | Annual | owasp.org/Top10 |
| Kubernetes version in lab examples | 3x/year | kubernetes.io/releases |
| Terraform exam code TA-003 | Post-IBM acquisition | hashicorp.com/certifications |
| OpenTofu vs Terraform adoption | Quarterly | opentofu.org + job postings |
| CKA curriculum | Annually | training.linuxfoundation.org |
| Coursera program structures | Semester | Verify at enrollment |

---

### Blind Spot 5: Tutorial Hell Risk
Following numbered lab steps produces "I did the lab" confidence, not "I can debug this in prod" competence. Labs must include intentional break scenarios — not just working examples.
**Fix**: Every lab must have a "what if it breaks" section. The K8s security hardening project has 5 intentional violations for exactly this reason.

---

### Blind Spot 6: Interview Process Reality
Real Staff/Principal SRE interview loops at target companies:
- **FAANG/hyperscaler**: Phone screen (30 min) → system design (60 min) → infra/SRE deep dive (60 min) → coding/scripting in Python or Bash — NOT algorithmic (45 min) → behavioral/leadership STAR (45 min) → culture/cross-functional (30 min)
- **Take-home projects**: Databricks, Stripe, some growth tech — 3–5 hour take-home for Staff roles
- **Calibration-first strategy**: Apply to 3 non-top-tier companies at Week 6 BEFORE applying to dream companies at Week 9

---

### Blind Spot 7: Certification Collector Trap
Risk: studying for 7–8 months, accumulating certs, never applying.
**Forcing function**: First application submission by Week 6, regardless of readiness. Interview feedback calibrates remaining study priorities better than any training plan.

---

## PART C: RISK REGISTER

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Schedule slip from P1 incidents | HIGH | HIGH | 2 buffer weeks exist; use them without guilt |
| R2 | Content accuracy decay over time | MEDIUM | MEDIUM | Monthly version audit; OWASP check quarterly |
| R3 | Scope creep — adding domains/certs | HIGH | MEDIUM | Hard freeze domain list; backlog file for new ideas |
| R4 | Studying but never applying | MEDIUM | HIGH | Week 6 forcing function for first 3 applications |
| R5 | H1B transfer processing delays | MEDIUM | HIGH | Premium processing negotiation; prefer established sponsors |
| R6 | Technology shift (OpenTofu, K8s changes) | MEDIUM | MEDIUM | Bi-weekly job posting scan; monthly refresh check |
| R7 | Context loss between Claude sessions | HIGH | MEDIUM | `session-start-prompt.md` — paste at every session start |
| R8 | False confidence from studying | HIGH | HIGH | Weekly confidence calibration ritual; timed drills without notes |
| R9 | LinkedIn posts signal "student" not "practitioner" | MEDIUM | MEDIUM | Practitioner-voice rule: "I implemented X at T-Mobile" not "I just learned X" |
| R10 | Burnout alongside demanding day job | MEDIUM | HIGH | Recognize P1 weeks as buffer weeks; protect weekends during high-incident periods |

---

## PART D: CAPSTONE PROJECT SPECIFICATIONS (Answer Keys)

### Project 1: Secure IaC Pipeline
**Stack**: Terraform + OPA Conftest + GitHub Actions + OIDC (no stored AWS credentials)
**What it proves**: Can design and implement a secure CI/CD pipeline with policy gates
```
secure-iac-pipeline/
├── .github/workflows/
│   ├── plan.yml          # Runs on PR: terraform plan + OPA Conftest + Checkov
│   └── apply.yml         # Runs on merge: terraform apply with OIDC
├── modules/
│   ├── vpc/              # Reusable VPC module
│   └── s3-secure/        # S3 with encryption + versioning enforced
├── environments/
│   ├── dev/
│   └── prod/             # Requires manual approval gate
├── policies/
│   └── deny-public-s3.rego    # OPA policy: no public-read buckets
├── README.md
└── ANSWER_KEY.md         # Expected pipeline output at each step; what errors mean
```

### Project 2: Observable SRE Platform
**Stack**: OTel Collector + Prometheus + Grafana + Python app with OTel SDK
**What it proves**: Can instrument a service, configure MELT telemetry, implement SLO burn rate alerts
```
observable-sre-platform/
├── app/
│   ├── main.py           # Python app with OTel instrumentation
│   └── Dockerfile
├── otel-collector/
│   └── config.yaml       # Fan-out: Splunk HEC + Prometheus remote_write
├── prometheus/
│   ├── prometheus.yml
│   └── slo-alerts.yml    # Multi-window burn rate rules (14x/1h + 6x/6h)
├── grafana/dashboards/
│   └── slo-dashboard.json
├── docker-compose.yml
└── ANSWER_KEY.md         # Screenshots/descriptions of working dashboard + alert behavior
```

### Project 3: Kubernetes Security Hardening
**Stack**: kind cluster + OPA Gatekeeper + Falco + NetworkPolicies
**What it proves**: Can implement K8s security controls and identify policy violations
```
k8s-security-hardening/
├── cluster/kind-config.yaml
├── gatekeeper/
│   ├── constraint-templates/    # 5 ConstraintTemplates
│   └── constraints/             # 5 Constraints (no-root, resource-limits, approved-registries, required-labels, no-hostNetwork)
├── falco/falco-rules.yaml
├── network-policies/namespace-isolation.yaml
├── test-namespaces/
│   ├── compliant/               # Manifests that pass all policies
│   └── violations/              # 5 intentionally broken manifests to fix
└── ANSWER_KEY.md                # Exact error messages for each violation + expected Falco alert output
```

---

## PART E: CONTENT FRESHNESS PROTOCOL

| Review type | Frequency | What to check |
|---|---|---|
| Version audit | Monthly | K8s version in labs; Terraform version; exam codes |
| OWASP check | Quarterly | Top 10 page for version updates |
| Job market scan | Bi-weekly | 5 new postings from target companies; new vocabulary appearing? |
| Cert curriculum | Before exam registration | Linux Foundation / HashiCorp official exam pages |
| Compensation data | Monthly | levels.fyi for Staff SRE at target companies |

**Freshness trigger for Claude sessions**: "Check Training_Plan_Master.md for version numbers or exam codes that may have changed since [last review date]."

---

*Source: 68KB program review agent | June 11, 2026 | Grounded in Training_Plan_Master.md (1,939 lines)*
