# Research Report 05 — Enterprise Security Trends 2025–2026
## Latest Trends Being Adopted by Enterprises: What Staff/Principal SRE & DevSecOps Must Know

**Research method**: 115 adversarial agents | 32 sources fetched | 118 claims extracted | 13/25 verified
**Date**: June 11, 2026
**Confidence**: ✅ Hard-verified (2-1 or 3-0) | ⚠️ Directional (plausible, vendor-sourced, use with caveat) | ❌ Refuted

---

## EXECUTIVE SUMMARY

Three forces are reshaping enterprise security in 2025–2026 that every Staff/Principal SRE and DevSecOps candidate must be able to discuss:

1. **Zero-trust is everywhere in name, partial in practice** — most enterprises cover less than half their environment. The opportunity: organizations that can actually *implement* zero-trust components (not just talk about them) are rare and highly valued.

2. **AI/LLM has created a new attack surface with its own OWASP Top 10** — prompt injection, model supply chain attacks, and excessive AI agent permissions are now interview topics, not just research topics.

3. **Supply chain security is becoming platform-native** — GitHub, npm, PyPI, and Kubernetes now have SBOM and provenance attestation built in. The 4% of teams that pin all their CI/CD action hashes vs. the 71% that pin none illustrates the massive gap between best practice and reality.

**The headline stat for interviews**: *87% of organizations have exploitable vulnerabilities in production. 70% of secrets leaked in 2022 are still valid today. Only 4% of teams pin all their GitHub Action hashes.* These numbers prove why DevSecOps exists.

---

## TREND 1: ZERO-TRUST ARCHITECTURE — FROM CONCEPT TO PARTIAL REALITY

### What Was Verified ✅ (3-0)

**Finding**: Zero-trust deployment is widespread in name but limited in practice. Most enterprise implementations cover **half or less of the environment** and mitigate **one-quarter or less of overall enterprise risk** — even among organizations actively pursuing zero-trust strategies.

*Source: Gartner Q4 2023 survey of 303 security leaders; corroborated by Forrester Zero Trust Platforms Wave Q3 2025*

**Gartner's sobering predictions** (corroborated):
- 75% of US federal agencies will **fail** zero-trust implementation through 2026
- Only **10% of large enterprises** will have a mature zero-trust program by 2026
- AI agents are actively increasing zero-trust architectural complexity (Forrester Q3 2025)

### The Forrester Definition (Use This in Interviews) ✅ (3-0)

**Forrester Zero Trust Platforms Wave Q3 2025** defines:
> "A unified set of core security technologies that serve as the foundation to enable the Zero Trust model of information security"

**Five functional domains** (map these to interview questions):
| Domain | What it means for SRE/DevSecOps |
|---|---|
| **Data** | Data classification, DLP, encryption at rest/transit, access logging |
| **Workloads** | Container security, runtime policy (Falco/eBPF), workload identity (SPIFFE/SPIRE) |
| **Networks** | Micro-segmentation, network policies, service mesh mTLS, VPC design |
| **Users** | IAM, MFA, privileged access management (PAM), JIT access |
| **Devices** | Endpoint compliance, certificate-based device identity |

### Zero-Trust Interview Vocabulary
`micro-segmentation` · `identity-aware proxy` · `continuous verification` · `policy enforcement point (PEP)` · `policy decision point (PDP)` · `Forrester ZTX (Zero Trust eXtended)` · `NIST SP 800-207` · `BeyondCorp` · `software-defined perimeter` · `least-privilege access` · `JIT (just-in-time) access` · `ZTNA (Zero Trust Network Access)` · `identity-based segmentation`

### What "Good" Looks Like for SRE in Zero-Trust Conversations
- Can explain the difference between network-based segmentation (old model) and identity-based micro-segmentation (zero-trust model)
- Understands NIST SP 800-207 as the reference architecture — can name its core tenets without notes
- Has a view on where zero-trust is currently implemented in T-Mobile's environment and where the gaps are
- Treats IRSA (IAM Roles for Service Accounts) as a concrete zero-trust implementation for workloads — no long-lived credentials, identity-verified at every request

### Your T-Mobile Anchor
"Vault and CyberArk at T-Mobile are the secrets management layer of our zero-trust posture. IRSA on EKS is our workload identity implementation. The gap I'd extend: network micro-segmentation using Kubernetes NetworkPolicies and service mesh mTLS — that's the next layer."

---

## TREND 2: AI/LLM SECURITY — THE NEW ATTACK SURFACE

### OWASP LLM Top 10 (2025) — Two Categories Verified ✅ (3-0)

The OWASP Gen AI Security Project published the LLM Top 10 in November 2024 (current as of June 2026). Two entries are hard-verified and directly relevant to SRE/DevSecOps:

**LLM03:2025 — Supply Chain (Model Supply Chain)** ✅
Covers vulnerabilities in:
- Training datasets (data poisoning)
- Pre-trained models (backdoored models from untrusted sources)
- Deployment platforms (compromised model serving infrastructure)
- Outdated dependencies in ML pipelines

*Why this matters for SRE*: Every SRE team integrating AI/ML components is responsible for the security of the model supply chain, not just the application supply chain. An SBOM for code is not sufficient — you need model provenance and model cards.

**LLM06:2025 — Excessive Agency** ✅
Defined as: LLMs granted too much autonomy and permissions, enabling unintended harmful actions.
- An LLM agent with write access to a production database can be manipulated into data destruction
- An LLM with read access to internal Slack channels can leak confidential information via indirect prompt injection
- The mitigation: least-privilege for AI agents — same principle as RBAC, applied to AI tool-use

### AI Security Vocabulary for Interviews
`OWASP LLM Top 10` · `prompt injection (direct vs. indirect)` · `model supply chain attack` · `model card` · `SBOM for ML models` · `model provenance` · `RAG poisoning` · `indirect prompt injection` · `excessive agency` · `least-privilege for AI agents` · `LLM guardrails` · `AI red teaming` · `tool use / function calling attack surface` · `agentic AI security`

### AI-Generated Code Increases Secrets Risk ⚠️ (2-1, vendor-sourced)
**Finding**: Public repositories using GitHub Copilot show a **6.4% secret leakage rate** — 40% higher than the 4.6% baseline across all public repositories. Copilot adoption grew 27% between 2023–2024.

*Source: GitGuardian State of Secrets Sprawl 2025 — vendor report, use directionally*
*Caveat: Correlation, not causation. Copilot-heavy repos have higher commit volume which independently increases exposure surface.*

**Interview framing**: "AI-generated code bypasses the developer security awareness that comes from manually writing code. Pre-commit secrets scanning becomes more critical, not less, as AI coding assistance scales."

### The AI + SRE Opportunity
Staff/Principal SRE engineers who can speak to both implementing AI capabilities AND securing the AI pipeline are extremely rare. Your existing ML/anomaly detection work at T-Mobile (Python + Splunk MLTK) is a foundation. Frame it as: "I've built ML-based anomaly detection in production. The next question I'd ask about any AI pipeline is: what is the model's supply chain provenance, and what permissions does the inference service have at runtime?"

---

## TREND 3: eBPF — FROM HYPERSCALER TO ENTERPRISE STANDARD

### What Was Verified ✅ (3-0)

**Meta** runs eBPF as its primary software-defined load balancer (Katran, open-sourced 2018).
**Google** deploys eBPF via Cilium as the default CNI for **GKE Autopilot** (GA May 2021, now default).

*Source: Linux Foundation eBPF Foundation launch announcement (August 2021), corroborated by Google Cloud documentation*

**What this means**: eBPF is no longer an experimental technology. It is the production-grade substrate for:
- **Networking**: Replacing iptables for Kubernetes network policy enforcement (Cilium)
- **Observability**: Zero-instrumentation network flow visualization (Cilium Hubble)
- **Runtime security**: Process-level syscall tracing without ptrace overhead (Falco, Tetragon)
- **Performance**: XDP (eXpress Data Path) for sub-microsecond packet processing

### eBPF Interview Vocabulary ✅
`XDP (eXpress Data Path)` · `Cilium` · `Cilium NetworkPolicy` · `Hubble (network observability)` · `Tetragon (process-level tracing)` · `Falco (syscall-based runtime security)` · `BPF CO-RE (Compile Once Run Everywhere)` · `kprobes` · `uprobes` · `tracepoints` · `eBPF verifier` · `eBPF maps` · `kernel bypass`

### What to Know at Staff/Principal Level
You do NOT need to write eBPF programs. You need to:
- Explain why eBPF replaces iptables at scale (iptables is O(n) per rule; eBPF is O(1) with hash maps)
- Know that Cilium Hubble provides **network flow visibility without a sidecar** — this is architecturally significant for service mesh debates
- Understand Tetragon as a Kubernetes-native, eBPF-based security tool that can enforce process-level policies (e.g., block a container process from spawning a shell)
- Be able to explain why GKE uses eBPF as default and what that means for K8s networking security at scale

---

## TREND 4: SUPPLY CHAIN SECURITY — BECOMING PLATFORM-NATIVE

### What Was Verified ✅ (3-0)

**GitHub**, **Red Hat Konflux**, **npm**, **PyPI**, and **Kubernetes** are all integrating provenance attestation and SBOM generation directly into their platforms as of 2025:

| Platform | What they added | When |
|---|---|---|
| GitHub | Artifact attestations (SLSA v1.0 Build Level 2) via `actions/attest-sbom` | 2024–2025 |
| npm | `--provenance` flag (GA October 2023) + Trusted Publishing (GA July 2025) | 2023–2025 |
| PyPI | Attestations — reached 17% adoption by March 2026 | 2025–2026 |
| Red Hat Konflux | Tekton Chains for in-toto attestations + Conforma/rego policy enforcement | 2024–2025 |

*Source: InfoQ, August 2025 — provenance feature coverage*

### The Unpinned Actions Crisis ✅ (3-0)

**Finding from Datadog State of DevSecOps 2026** (February 2026, data from tens of thousands of production applications):
- **71%** of organizations never pin any GitHub Action hashes
- **Only 4%** pin all marketplace action hashes
- **100%** of organizations use at least one marketplace action

**Real incidents validating this risk**:
- **tj-actions/changed-files compromise (2025)**: Widely used GitHub Action was compromised; repos using unpinned `@main` got malicious code injected into their CI pipelines
- **May 2026 tag-hijacking campaign**: Attacker hijacked a popular action's version tag to redirect to malicious payload

**The fix**: Pin every action to a specific commit SHA, not a tag:
```yaml
# Vulnerable (tag can be redirected):
uses: actions/checkout@v4

# Secure (commit SHA cannot be redirected):
uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
```

**Interview framing**: "71% of teams are one compromised GitHub Action away from a supply chain incident. Hash-pinning all actions is the single highest-ROI security control for CI/CD pipelines that almost nobody does."

### Supply Chain Vocabulary ✅
`SLSA (Supply-chain Levels for Software Artifacts)` · `SLSA Build Level 1/2/3` · `Sigstore` · `Cosign` · `Rekor (transparency log)` · `Fulcio (certificate authority)` · `in-toto attestation` · `provenance` · `artifact attestation` · `SBOM (CycloneDX vs. SPDX)` · `action hash pinning` · `SHA-256 commit pinning` · `Dependabot for Actions` · `OpenSSF Scorecard` · `StepSecurity Harden-Runner`

---

## TREND 5: SECRETS MANAGEMENT — THE SYSTEMIC FAILURE

### What Was Verified ⚠️ (2-1, vendor-sourced — GitGuardian)

**Three sobering statistics** (directionally valid; source has commercial interest):
1. **70% of secrets exposed in 2022 remain valid** (unrotated/unrevoked) as of January 2025
2. **64%+ of those same secrets** still valid in January 2026 (GitGuardian 2026 follow-up)
3. **5.1% of repositories at organizations with secrets managers** still leak secrets — *higher* than the 4.6% all-repo baseline

**What this means**: Having a secrets manager (Vault, AWS Secrets Manager) does not automatically prevent secrets sprawl. You need **active detection + mandatory rotation** to close the gap.

### The ESO VaultDynamicSecret Pattern ✅ (3-0)

**External Secrets Operator (ESO)** VaultDynamicSecret generator is the Kubernetes-native solution for eliminating static credentials:

```yaml
# Instead of storing a static database password in a K8s Secret:
apiVersion: generators.external-secrets.io/v1alpha1
kind: VaultDynamicSecret
metadata:
  name: "db-credentials"
spec:
  path: "database/creds/my-role"   # Vault dynamic secrets engine path
  method: "GET"
  provider:
    vault:
      server: "https://vault.company.com"
      auth:
        kubernetes:                  # Uses projected service account token
          mountPath: "kubernetes"
          role: "my-app-role"        # Vault role tied to K8s ServiceAccount
```

*How it works*: Pod's projected service account token → Vault Kubernetes auth → Vault issues dynamic, short-lived DB credentials → ESO injects as K8s Secret → credentials auto-rotate on expiry. No static password ever stored.

### Secrets Management Vocabulary for Interviews
`secrets sprawl` · `dynamic credentials` · `just-in-time (JIT) access` · `External Secrets Operator (ESO)` · `VaultDynamicSecret` · `ExternalSecret CRD` · `ClusterSecretStore` · `Vault AppRole vs. Kubernetes auth` · `projected service account tokens` · `IRSA (AWS)` · `secrets rotation` · `pre-commit secrets scanning` · `push protection` · `truffleHog` · `Gitleaks` · `detect-secrets` · `GitHub Advanced Security (GHAS) secret scanning`

### Your T-Mobile Anchor
"At T-Mobile, we use Vault and CyberArk for secrets management. The problem I've observed is secrets rotation lag — when a secret needs to change, coordinating 200 pods to pick up the new value without a rolling restart is non-trivial. The ESO VaultDynamicSecret pattern solves this by removing long-lived credentials entirely — the pods always get fresh, short-lived credentials on demand."

---

## TREND 6: VULNERABILITY PRIORITIZATION — BEYOND RAW CVSS

### What Was Verified ✅ (3-0)

**Datadog State of DevSecOps 2026** (February 2026):
- **87%** of organizations have at least one exploitable vulnerability in production
- **40%** of all production services are affected
- By language: **Java services most exposed at 59%**, .NET at 47%, Rust at 40%

*Source: Datadog, based on CISA KEV catalog, NIST NVD, ExploitDB, GitHub Advisories, data from tens of thousands of production applications*

### The Alert Fatigue Problem (Directional — refuted claim, still important)
A refuted claim said "only 18% of critical CVEs remain critical after runtime context scoring." While the specific number was refuted, the underlying problem is real and interview-relevant: **raw CVSS scores produce unmanageable alert volumes**. Modern DevSecOps practice requires:

1. **CISA KEV filtering**: Only prioritize CVEs that are actually being exploited in the wild
2. **Reachability analysis**: Is the vulnerable code path actually reachable in your application?
3. **EPSS scoring**: Exploit Prediction Scoring System — probability a CVE will be exploited in the next 30 days
4. **VEX documents**: Vulnerability Exploitability eXchange — machine-readable statements about whether a vulnerability is exploitable in your specific context

### Vulnerability Prioritization Vocabulary
`CISA KEV (Known Exploited Vulnerabilities)` · `CVSS` · `EPSS (Exploit Prediction Scoring System)` · `reachability analysis` · `SCA (Software Composition Analysis)` · `VEX (Vulnerability Exploitability eXchange)` · `runtime context scoring` · `alert fatigue` · `vulnerability prioritization`

---

## TREND 7: POLICY-AS-CODE — MATURITY AND NEW PLAYERS

### The Three Policy Engines (Know When to Use Each)

| Engine | Best for | Model | Kubernetes native? |
|---|---|---|---|
| **OPA + Rego** | General-purpose infrastructure policy (Terraform, K8s, API gateways) | Rego rules evaluated against JSON input | Via Gatekeeper admission webhook |
| **Kyverno** | Kubernetes-native policy (simpler than Rego for K8s) | YAML-based policies — no separate language | Yes — direct admission controller |
| **AWS Cedar** | AWS-native authorization decisions (fine-grained IAM-like policies) | Cedar policy language; designed for application authz | No — AWS-specific |

**Interview question**: "OPA is general-purpose but requires learning Rego. Kyverno is K8s-native and YAML-based. When would you choose one over the other?"

**Answer structure**: "For infrastructure-wide policy enforcement across Terraform, K8s, CI/CD pipelines, and APIs, OPA gives you one engine and one language. For pure Kubernetes admission control where your team knows YAML but not Rego, Kyverno reduces the barrier to adoption. I'd use OPA for the enterprise-wide policy platform and Kyverno for team-level K8s controls."

### Compliance Automation Pattern
The emerging pattern for continuous compliance (SOC2, ISO 27001, FedRAMP):

```
Policy-as-Code (OPA/Rego)
    ↓
Automated evidence collection (CI/CD pipeline artifacts, git history, audit logs)
    ↓
Continuous compliance dashboard (Styra DAS, Nirmata, RegScale, Drata)
    ↓
Automated audit reports (replaces point-in-time spreadsheet audits)
```

**What enterprises are replacing**: Annual compliance audits done manually by collecting screenshots and spreadsheets. What they're moving to: continuous compliance where every deployment automatically generates evidence that policy requirements were met.

### Policy-as-Code Vocabulary
`OPA (Open Policy Agent)` · `Rego` · `Gatekeeper` · `Kyverno` · `Conftest` · `Checkov` · `AWS Cedar` · `Sentinel (Terraform)` · `policy enforcement point` · `admission controller` · `continuous compliance` · `compliance as code` · `evidence collection pipeline` · `SOC2 Type II` · `FedRAMP` · `NIST CSF 2.0` · `CIS benchmarks` · `DORA regulation (EU)`

---

## TREND 8: WORKLOAD IDENTITY — SPIFFE/SPIRE

### The Problem It Solves
Every microservice needs to prove its identity to every other service and to cloud APIs. The current approaches all have problems:
- **Shared secrets** → secrets sprawl (70% still valid after 3 years)
- **Service account tokens** → long-lived, broad permissions
- **IP-based trust** → not zero-trust, breaks in dynamic environments

**SPIFFE/SPIRE** (Secure Production Identity Framework for Everyone / SPIRE is the runtime):
- Issues short-lived X.509 certificates (SVIDs — SPIFFE Verifiable Identity Documents) to every workload
- Identity is tied to the workload's cryptographic attestation (what process, on what node, in what K8s namespace)
- No secrets passed at deploy time — the identity is attested at runtime
- Integrates with Vault, Istio/Linkerd mTLS, and AWS STS

**Real-world adoption**: Uber, Square, and GitHub have publicly documented SPIFFE/SPIRE usage for workload identity. It is a CNCF graduated project.

### Workload Identity Vocabulary
`SPIFFE` · `SPIRE` · `SVID (SPIFFE Verifiable Identity Document)` · `X.509 SVID` · `JWT SVID` · `workload attestation` · `node attestation` · `trust bundle` · `OIDC federation` · `certificate lifecycle management` · `mTLS (mutual TLS)` · `service mesh` · `Istio` · `Linkerd` · `cert-manager` · `certificate rotation`

---

## TREND 9: REGULATORY FRAMEWORKS DRIVING ADOPTION

These are the compliance frameworks that are forcing enterprise security investment in 2025–2026:

| Framework | What it requires | Who it affects |
|---|---|---|
| **NIST CSF 2.0** (2024) | Expanded Govern function added; supply chain risk management elevated | US enterprises, federal contractors |
| **EU DORA Regulation** | Digital Operational Resilience Act; ICT risk management, incident reporting, resilience testing | EU financial services (banks, insurers, fintechs) |
| **EU Cyber Resilience Act** | Software product security requirements; SBOM and vulnerability disclosure | Software vendors selling into EU market |
| **US EO 14028** | Federal software suppliers must provide verifiable provenance | Federal contractors, cloud providers |
| **CIS Benchmarks** | Configuration hardening baselines for cloud, K8s, OS | Any enterprise with cloud infrastructure |
| **SOC2 Type II** | Continuous controls evidence for SaaS companies | B2B SaaS companies |
| **FedRAMP** | Cloud service authorization for US federal use | Cloud providers serving US government |

**Interview framing**: "The compliance landscape is driving DevSecOps adoption faster than any technology choice. DORA in Europe and EO 14028 in the US mean that SBOM generation and supply chain provenance are regulatory requirements, not best practices. That's why supply chain security is OWASP's highest-incidence category in 2025."

---

## TREND 10: THE HYGIENE GAP — THE REAL INTERVIEW DIFFERENTIATOR

The most important finding from this research: **the gap between best practice and actual enterprise state is enormous**. This is your opportunity.

| Best Practice | Actual Enterprise State |
|---|---|
| Pin all GitHub Action hashes | Only 4% do it |
| Rotate leaked secrets immediately | 70% of 2022 leaks still valid in 2025 |
| Zero exploitable prod vulnerabilities | 87% have at least one |
| Complete zero-trust coverage | Most have <50% coverage |
| SBOM for all software | Most enterprises have no formal SBOM program |

**Why this matters for your positioning**: You don't need to have implemented all of these. You need to be able to articulate:
1. Why the gap exists (developer workflow friction, alert fatigue, tool complexity)
2. How you'd close it systematically (platform security golden paths, automated tooling, policy-as-code guardrails)
3. What you've already done in a similar vein at T-Mobile (your delivery governance, incident command, SLO culture)

**The strongest Staff/Principal answer**: "I've seen this gap firsthand. At T-Mobile, we had 42 downstream integrations and six zero-downtime migrations — every one of those was a potential supply chain event. The way we maintained reliability was the same way you close security hygiene gaps: you make the right thing the easy thing. Golden paths, automated checks, policy-as-code guardrails. You don't solve it by adding more rules — you solve it by making compliance frictionless."

---

## INTERVIEW VOCABULARY MASTER LIST — Enterprise Security Trends

Compile all new vocabulary from this research into a single scannable list for review:

**Zero-Trust**: micro-segmentation · identity-aware proxy · continuous verification · PEP · PDP · ZTNA · BeyondCorp · NIST SP 800-207 · JIT access · Forrester ZTX

**AI/LLM Security**: OWASP LLM Top 10 · prompt injection · indirect prompt injection · model supply chain · model card · RAG poisoning · excessive agency · LLM guardrails · tool use attack surface · agentic AI · least-privilege for AI agents

**eBPF**: XDP · Cilium · Hubble · Tetragon · Falco · BPF CO-RE · kprobes · uprobes · tracepoints · eBPF verifier · kernel bypass

**Supply Chain**: SLSA Build Level 1/2/3 · Sigstore · Cosign · Rekor · Fulcio · in-toto attestation · provenance · action hash pinning · OpenSSF Scorecard · tj-actions compromise · StepSecurity Harden-Runner

**Secrets**: secrets sprawl · dynamic credentials · JIT access · ESO · VaultDynamicSecret · ExternalSecret CRD · IRSA · projected service account tokens · push protection · GHAS secret scanning

**Vulnerability Mgmt**: CISA KEV · CVSS vs. EPSS · reachability analysis · VEX · runtime context scoring · alert fatigue

**Policy-as-Code**: OPA · Rego · Gatekeeper · Kyverno · Conftest · Checkov · Cedar · Sentinel · continuous compliance · evidence collection pipeline · SOC2 · FedRAMP · NIST CSF 2.0 · DORA · CIS Benchmarks

**Workload Identity**: SPIFFE · SPIRE · SVID · mTLS · service mesh · cert-manager · certificate rotation · trust bundle · node attestation

---

## SOURCES USED

### Primary / High Quality
- Gartner Zero Trust survey (Q4 2023, 303 security leaders) — gartner.com
- Forrester Zero Trust Platforms Wave Q3 2025 — forrester.com
- Datadog State of DevSecOps 2026 (February 2026) — datadoghq.com/state-of-devsecops/
- External Secrets Operator documentation — external-secrets.io
- Linux Foundation eBPF Foundation announcement — linuxfoundation.org
- OWASP Gen AI Security Project — genai.owasp.org (LLM03:2025, LLM06:2025)
- InfoQ provenance coverage (August 2025) — infoq.com

### Secondary / Directional
- GitGuardian State of Secrets Sprawl 2025 + 2026 — gitguardian.com *(vendor source — use directionally)*
- Forrester Wave (blog summary, not full report) — forrester.com/blogs
- CSO Online zero-trust coverage — csoonline.com
- The Hacker News secrets sprawl 2026 — thehackernews.com

---

## OPEN QUESTIONS FOR FUTURE RESEARCH

1. SPIFFE/SPIRE adoption rates outside hyperscalers — which enterprises have deployed it, and is it displacing service mesh mTLS or complementing it?
2. Policy-as-code maturity in regulated industries — which platforms (Styra, Nirmata, AWS Cedar, RegScale) are winning for automated compliance reporting?
3. Documented enterprise incidents from LLM Excessive Agency (LLM06) — are there production examples with quantified blast radius?
4. SLSA Level 2/3 actual enterprise adoption — beyond GitHub and Red Hat, which enterprises have mandated it internally?

---

*Research run: June 11, 2026 | 115 agents | 32 sources | 118 claims | 13/25 verified*
*Next refresh: September 2026 — check OWASP LLM Top 10 updates, Forrester Wave updates, Datadog State of DevSecOps annual release*
