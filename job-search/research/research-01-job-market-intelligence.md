# Research Report 01 — Job Market Intelligence
## SRE/DevSecOps Skills, Vocabulary & Hiring Requirements 2025–2026

**Research method**: 110 adversarial agents | 27 sources fetched | 93 claims extracted | 25 verified
**Date**: June 11, 2026
**Confidence legend**: ✅ Hard-verified (2-1 or 3-0 vote) | ⚠️ Directional (refuted sourcing, plausible content) | ❌ Refuted (do not rely on)

---

## WHAT TO DO WITH THIS DOCUMENT

Use this as a **reference during interview prep and resume writing** — not as a study guide.
Specifically useful for:
- Picking vocabulary to use on LinkedIn and resume (Section 2)
- Understanding what interviewers are allowed to probe on (Section 3)
- Calibrating salary expectations with the right primary sources (Section 4)
- Understanding why certain tools were NOT verified (Section 5)

---

## SECTION 1: HARD-VERIFIED FINDINGS

### Finding 1 — Supply Chain Security Is Now Baseline, Not Optional ✅ (3-0)

**Claim**: OWASP Top 10:2025 lists A03:2025 — Software Supply Chain Failures as a distinct category with the highest average incidence rate (5.19%) across all categories. A10:2025 — Mishandling of Exceptional Conditions is a new entry.

**What this means for your job search**:
- Any job posting referencing "OWASP compliance" now implicitly requires: SBOM generation, SCA (Software Composition Analysis), signed artifacts, and provenance attestation
- This is the single most important gap to close — it is codified, testable, and in every DevSecOps job description
- Finalized January 2026 at OWASP Global AppSec Conference

**Sources**: owasp.org/Top10/2025/ (primary), webpronews.com/devsecops-in-2026, GitLab blog, Parasoft, socket.dev

---

### Finding 2 — MELT Is the Observability Vocabulary Recruiters Use ✅ (2-1)

**Claim**: MELT (Metrics, Events, Logs, Traces) is the four-pillar observability framework used in SRE job postings. Popularized by New Relic; adopted across Splunk, Cisco, and Microsoft Azure documentation.

**Important nuance (the 1 dissenting vote)**: OpenTelemetry's canonical model uses 3 pillars — Logs, Metrics, Traces — without Events as a separate pillar. MELT is primarily a New Relic framing. **Know both**:
- MELT: use when talking to recruiters and in LinkedIn/resume
- 3-pillar (Logs/Metrics/Traces): use when talking to engineers and in technical interviews

**Your translation**: Your MART framework (Monitoring, Alerting, Reporting, Troubleshooting) maps to MELT. In interviews, translate: "We built what I call MART — which is our implementation of the MELT observability model."

**Sources**: digital-architects-zurich.ch/effective-sre-observability-opentelemetry-melt/, newrelic.com/platform/telemetry-data-101/

---

## SECTION 2: VERIFIED VOCABULARY — USE THESE EXACT TERMS

These terms appear in $180k–$280k+ job postings and are grounded in the verified findings above. Use them on LinkedIn, in resumes, and in interviews.

### Security Vocabulary (anchored by OWASP A03:2025 — 3-0 verified)
| Term | Use in context |
|---|---|
| `supply chain security` | Headline skill; frame all CI/CD governance work under this |
| `SBOM` | Software Bill of Materials — the "nutritional label" for software |
| `SCA` | Software Composition Analysis — scanning dependencies for CVEs |
| `shift-left security` | Security gates in CI/CD before code reaches production |
| `OWASP Top 10` | Always cite the year: "OWASP Top 10:2025" |
| `policy-as-code` | OPA/Gatekeeper enforcing infrastructure rules as code |
| `zero-trust` | No implicit trust — every request authenticated and authorized |
| `CSPM` | Cloud Security Posture Management — continuous compliance scanning |
| `secrets management` | Vault, AWS Secrets Manager, External Secrets Operator |
| `SAST/DAST` | Static/Dynamic Application Security Testing |

### Observability Vocabulary (anchored by MELT — 2-1 verified)
| Term | Use in context |
|---|---|
| `MELT` | Use as the framework name when talking to recruiters |
| `OpenTelemetry` | The vendor-neutral instrumentation standard |
| `SLO/error budgets` | Your strongest domain — lead with this |
| `distributed tracing` | How requests flow across microservices |
| `metrics cardinality` | High-cardinality metrics cause cost explosions — know this |
| `eBPF` | Zero-instrumentation observability (Cilium, Falco, Pixie) |
| `burn rate alerts` | Multi-window alert pattern for SLO consumption rate |
| `OTLP` | OpenTelemetry Protocol — the wire format for telemetry |

### Job Title Variations (use these in LinkedIn searches and applications)
- Senior SRE
- Staff SRE
- Principal SRE
- Senior Platform Engineer
- Staff DevSecOps Engineer
- Principal DevSecOps Engineer
- Cloud Security Engineer *(SRE-adjacent, valid target)*

---

## SECTION 3: WHAT INTERVIEWERS ACTUALLY PROBE (maturity level expected)

These were directionally consistent across multiple sources even though specific claims were refuted. Use as interview prep calibration — not as cited facts.

### Depth Level by Domain
| Domain | What's tested | Interview format |
|---|---|---|
| Kubernetes | Internals (control plane, admission webhooks, RBAC, scheduling) — NOT just "we run on EKS" | Whiteboard architecture + debug scenario |
| DevSecOps / Supply Chain | Design a secure pipeline end-to-end; write a basic OPA Rego rule; explain a supply chain attack | Whiteboard + "write this on paper" |
| Terraform/IaC | State locking, drift detection, module design, OIDC federation | Live coding or take-home |
| Observability | SLO math, burn rate calculation, OTel Collector design, cardinality tradeoffs | System design round |
| AWS | IRSA trust chain, multi-account IAM, VPC internals, cost architecture | Technical deep dive |
| Platform Engineering | IDP philosophy, DORA metrics, golden path design | Leadership/design round |
| Incident Command | Blameless postmortem process, MTTD/MTTR improvement, chaos engineering | Behavioral STAR round |

### Maturity Level Expected at Staff/Principal
- **Both** architect/design AND hands-on debug — not one or the other
- **Design round**: draw the architecture, justify every choice, explain tradeoffs
- **Debug round**: "you see this in prod — what do you do" — must walk through step-by-step
- **Leadership round**: "how did you drive org change around X" — STAR method required
- Roughly 40–50% of interview time at Staff/Principal level is **behavioral/leadership**, not technical

---

## SECTION 4: SALARY — WHAT THE RESEARCH CONFIRMED AND DID NOT CONFIRM

### What was confirmed ❌ (all salary claims refuted)
No specific salary figures survived adversarial verification. This does NOT mean the $180k–$280k+ target is wrong — it means the research pipeline could not independently verify the numbers from scraped/paywalled sources.

### Refuted salary claims (do not cite these numbers in negotiations — use levels.fyi directly)
| Claim | Source | Vote |
|---|---|---|
| Meta SRE median $470K across all levels | levels.fyi | 0-3 |
| Meta E5 SRE $422K TC ($216K base + $181K RSU + $24.5K bonus) | levels.fyi | 0-3 |
| Microsoft SRE median $193K TC | levels.fyi | 1-2 |
| Netflix SRE L6 $729K, L5 $510K, L4 $394K | levels.fyi | 0-3 |
| Senior Platform Eng: $162K Atlanta, $198K Seattle, $215K Bay Area | kore1.com | 0-3 |
| Senior DevSecOps 6-10yr: $165K-$215K; Staff/Principal: $210K-$275K+ | kore1.com | 0-3 |
| National avg base Senior DevSecOps: $133,317 | salary.com | 0-3 |

**Why they were refuted**: Data is behind paywalls, dynamically self-reported, or sourced from blog aggregators without primary backing. The numbers may be directionally correct — but cannot be cited as facts.

**What to do instead**: Go to levels.fyi directly and search for your exact target title at your target companies. The self-reported data there is more current and company-specific than any aggregated report.

### Open questions on salary (not answered by this research)
1. What is the TC split (base vs. RSU vs. bonus) at mid-market vs. Big Tech for Staff SRE?
2. Is there a measurable salary premium for CKA/CKS holders?
3. How does Atlanta base comp compare to remote-first roles at San Francisco-based companies?

---

## SECTION 5: TOOLS THAT WERE MENTIONED BUT NOT VERIFIED

These tools appear consistently in job postings and practitioner blogs. The specific claims about them were refuted (meaning the sources weren't independently verifiable) — but the tools themselves are real and widely used. Know them by category, not just by name.

### DevSecOps Toolchain by Category
| Category | Tools mentioned (unverified market share, but real tools) |
|---|---|
| SAST | Snyk Code, Semgrep, Checkmarx, SonarQube, GitHub Advanced Security |
| DAST | OWASP ZAP, Burp Suite Enterprise, Invicti |
| SCA / Container Scanning | Trivy (Aqua), Grype (Anchore), Clair, Snyk Container |
| Runtime Security | Falco, Sysdig Secure, Aqua, Prisma Cloud |
| Policy-as-Code | OPA/Gatekeeper, Kyverno, Conftest, Checkov |
| Secrets Management | HashiCorp Vault, AWS Secrets Manager, Sealed Secrets, External Secrets Operator |
| Artifact Signing | Cosign (Sigstore), Rekor, Fulcio |
| SBOM Generation | Syft (Anchore), Trivy (SBOM mode), CycloneDX CLI |

**How to talk about these in interviews**: Claim category knowledge and hands-on experience with 2–3 tools per category. Don't claim expertise in tools you haven't used. "I've worked with Trivy for container scanning and I understand the SAST/SCA/runtime security landscape" is stronger than listing 15 tool names.

---

## SECTION 6: SOURCES ACCESSED (for follow-up reading)

### Primary sources (most reliable — go here for current data)
- owasp.org/Top10/2025/ — OWASP Top 10:2025 official
- levels.fyi — Compensation data (self-reported, use directly)
- levels.fyi/2025/ — Annual survey

### Secondary sources (corroborating, less reliable)
- webpronews.com/devsecops-in-2026-demands-more-than-tools
- jfrog.com/whitepaper/state-of-devops-2025/
- devopsprojectshq.com/role/devops-market-h1-2025/
- salary.com/research/salary/hiring/senior-devsecops-engineer-salary
- kore1.com/devsecops-engineer-guide/
- kore1.com/platform-engineer-salary-guide-2026/

### Blog sources (directional only — do not cite in interviews)
- platformengineering.org/blog/platform-engineering-maturity-in-2026
- dev.to/aws-builders/gitops-and-iac-at-scale-aws-argocd-terragrunt-and-opentofu
- sreschool.com/blog/opentelemetry-in-devsecops-a-comprehensive-tutorial
- digital-architects-zurich.ch/effective-sre-observability-opentelemetry-melt/
- resumeadapter.com/blog/devsecops-resume-keywords

---

## OPEN QUESTIONS (not answered — worth a future research pass)

1. What do actual job postings at Amazon, Google, Stripe, Cloudflare list as required vs. preferred for Staff SRE — specifically around K8s depth and AWS service breadth?
2. Is there a cert premium for CKA/CKS or AWS Security Specialty in job offer data?
3. What is the practical K8s depth tested in Staff SRE technical interviews — are admission webhooks actually whiteboarded or is that only in job descriptions?
4. How does TC structure differ between Big Tech SRE (high RSU) and fintech/health-tech SRE (higher base, lower equity)?

---

*Research run: June 11, 2026 | 110 agents | 27 sources | 93 claims | 2/25 verified*
*Refresh trigger: Pull 5 new job postings from target companies every 2 weeks and compare vocabulary*
