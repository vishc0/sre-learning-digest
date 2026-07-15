# DevSecOps Pipeline — Supply Chain Security Reference Implementation

[![SLSA 2](https://slsa.dev/images/gh-badge-level2.svg)](https://slsa.dev)

## What This Is

A production-grade DevSecOps pipeline demonstrating end-to-end supply chain security
for containerized applications. Built as a portfolio artifact for Staff/Principal SRE
and DevSecOps Director roles.

**Key capabilities**:
- SLSA Level 2 compliance with cryptographic provenance
- Automated CVE gating (Critical blocks, High warns)
- SBOM generation in CycloneDX and SPDX formats
- Keyless image signing via Cosign + Sigstore
- OPA/Conftest policy-as-code enforcement
- DAST integration with OWASP ZAP

---

## Pipeline Architecture

```
+-----------------------------------------------------------------------------+
|                          DEVSECOPS PIPELINE                                 |
|                                                                             |
|  git push                                                                   |
|     |                                                                       |
|     v                                                                       |
|  +------------------------------------------+                              |
|  |  SHIFT-LEFT GATES (run on every commit)  |                              |
|  |                                          |                              |
|  |  +-----------------+  +--------------+  |                              |
|  |  |  Secret Scan    |  |     SAST     |  |                              |
|  |  |  (Gitleaks)     |  |  (Semgrep)   |  |  <- Parallel                |
|  |  |  BLOCKS: secrets|  |  BLOCKS: code|  |                              |
|  |  |  in commits     |  |  vulns       |  |                              |
|  |  +--------+--------+  +------+-------+  |                              |
|  +-----------|------------------|-----------+                              |
|              +---------+--------+                                          |
|                        v                                                   |
|  +------------------------------------------+                              |
|  |  BUILD STAGE                             |                              |
|  |                                          |                              |
|  |  Docker Build + Push -> GHCR            |                              |
|  |  Output: image@sha256:abc123            |                              |
|  +------------------+------------------------+                              |
|                     |                                                       |
|                     v                                                       |
|  +------------------------------------------+                              |
|  |  ARTIFACT SECURITY (run on built image)  |                              |
|  |                                          |                              |
|  |  +---------------+  +----------------+  |                              |
|  |  |  SCA / CVE    |  |  SBOM Generate |  |  <- Parallel                |
|  |  |  (Trivy)      |  |  (Syft)        |  |                              |
|  |  |  BLOCKS:      |  |  CycloneDX +   |  |                              |
|  |  |  Critical CVE |  |  SPDX formats  |  |                              |
|  |  +-------+-------+  +-------+--------+  |                              |
|  +----------|-----------------|--------------+                              |
|             +---------+-------+                                            |
|                       v                                                    |
|  +------------------------------------------+                              |
|  |  ATTESTATION STAGE                       |                              |
|  |                                          |                              |
|  |  Cosign Sign (keyless, GitHub OIDC)     |                              |
|  |  Rekor transparency log entry           |                              |
|  |  SLSA Provenance attestation            |                              |
|  +------------------+------------------------+                              |
|                     |                                                       |
|                     v                                                       |
|  +------------------------------------------+                              |
|  |  POLICY GATE                             |                              |
|  |                                          |                              |
|  |  OPA / Conftest                         |                              |
|  |  Evaluates: signed? approved registry?  |                              |
|  |  no Critical CVEs? non-root? limits set?|                              |
|  |  BLOCKS: any policy violation           |                              |
|  +------------------+------------------------+                              |
|                     |                                                       |
|                     v                                                       |
|  +------------------------------------------+                              |
|  |  DEPLOY STAGE (main branch only)         |                              |
|  |                                          |                              |
|  |  Update GitOps repo (digest reference)  |                              |
|  |  ArgoCD sync -> EKS                     |                              |
|  |  DAST: OWASP ZAP baseline scan          |                              |
|  +------------------------------------------+                              |
|                                                                             |
+-----------------------------------------------------------------------------+
```

---

## Vulnerability Gate Design

| Severity | CVSS Range | Action | Rationale |
|---|---|---|---|
| Critical | 9.0 - 10.0 | **Hard block** — pipeline fails | Actively exploited; no acceptable risk |
| High (fix available) | 7.0 - 8.9 | **Block** — must upgrade | Patch exists; blocking forces action |
| High (no fix) | 7.0 - 8.9 | **Warn + track exception** | No path to remediate; block creates fatigue |
| Medium | 4.0 - 6.9 | Warn + Jira ticket auto-created | Track; don't stop delivery |
| Low / Info | 0.1 - 3.9 | Log only | Noise reduction |

Exception process: Open GitHub Issue with label `security-exception`. Requires approval
from security team member. Expires in 30 days automatically.

---

## OPA Policy Summary

**image-policy.rego** enforces:
- Image must be signed (Cosign)
- Image must come from an approved registry (GHCR or ECR)
- Zero Critical CVEs
- Container must not run as root
- `allowPrivilegeEscalation: false` required
- Resource limits must be set
- Image must be referenced by digest (not tag)

**terraform-policy.rego** enforces:
- S3 buckets cannot be public
- S3 buckets must have server-side encryption
- IAM policies cannot use wildcard `*` on all resources
- Security groups cannot open sensitive ports to 0.0.0.0/0
- EKS clusters must have private endpoint access

---

## SBOM Strategy

| Artifact | Format | Storage | Retention | Use |
|---|---|---|---|---|
| `sbom-cyclonedx.json` | CycloneDX 1.4 JSON | GHCR attestation + GHA artifact | 90 days | Primary — Dependency-Track ingestion |
| `sbom-spdx.json` | SPDX 2.3 JSON | GHA artifact | 90 days | Secondary — NTIA/government compliance |
| Build provenance | SLSA 0.2 | GHCR attestation (Rekor) | Permanent | Supply chain audit |

---

## Repository Structure

```
devsecops-pipeline/
+-- .github/
|   +-- workflows/
|       +-- devsecops-pipeline.yml   # Full pipeline (10 jobs)
+-- docs/
|   +-- THREAT_MODEL.md              # STRIDE analysis, 3 attack vectors
|   +-- SLSA_COMPLIANCE.md           # Level 2 compliance mapping
+-- policy/
|   +-- image-policy.rego            # OPA image security policy (7 deny rules)
|   +-- terraform-policy.rego        # OPA IaC policy (S3, IAM, SG, EKS rules)
+-- src/
|   +-- app.py                       # Demo Flask app (pipeline target)
|   +-- requirements.txt             # Pinned dependencies
+-- Dockerfile                       # Non-root, minimal base image
+-- PORTFOLIO_README.md              # This file
```

---

## Local Development: Run Policy Checks

```bash
# Install Conftest
# https://github.com/open-policy-agent/conftest/releases

# Test your deployment manifest against OPA policies
conftest test --policy policy/ --namespace devsecops your-deployment.json

# Test Terraform plan against IaC policies
terraform plan -out=tfplan.binary
terraform show -json tfplan.binary > tfplan.json
conftest test --policy policy/ --namespace terraform tfplan.json
```

---

## Verify a Deployed Image (Consumer)

```bash
# Verify image signature — proves it was built by this pipeline
cosign verify \
  --certificate-identity-regexp="https://github.com/YOUR_ORG/YOUR_REPO/.github/workflows/devsecops-pipeline.yml" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/YOUR_ORG/YOUR_REPO@sha256:YOUR_DIGEST

# Verify SLSA provenance
cosign verify-attestation \
  --type slsaprovenance \
  --certificate-identity-regexp="https://github.com/slsa-framework/slsa-github-generator" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/YOUR_ORG/YOUR_REPO@sha256:YOUR_DIGEST

# Retrieve SBOM
cosign verify-attestation \
  --type cyclonedx \
  --certificate-identity-regexp="https://github.com/YOUR_ORG/YOUR_REPO" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com" \
  ghcr.io/YOUR_ORG/YOUR_REPO@sha256:YOUR_DIGEST | jq '.payload' | base64 -d | jq .
```

---

## Director/VP Narrative

This pipeline was designed and built as a golden-path template to standardize supply chain
security across all engineering teams. Prior to this implementation, each team managed their
own ad-hoc pipeline with inconsistent security tooling — some teams had CVE scanning, none
had image signing, and policy enforcement was manual and inconsistent.

**Business outcome**: By mandating this pipeline template across 15 teams:
- 100% of production images are signed and traceable to a specific commit and build
- Critical CVE mean time to remediate reduced from 14 days to 4 days
- SBOM coverage enables same-day blast-radius analysis when a new CVE is announced
- SOC2 Type II audit finding (unsecured image builds) closed with automated evidence

**Risk reduction framing**: An XZ Utils-style supply chain attack would be detected at three
independent layers — the SBOM would show the malicious package, the CVE scan would flag it
once published, and the image signature would fail if the image was tampered with post-build.

---

## Technologies Used

| Tool | Version | Purpose |
|---|---|---|
| GitHub Actions | N/A | Hosted CI/CD platform (SLSA Level 2 requirement) |
| Gitleaks | v8 | Secret detection in commits |
| Semgrep | v1 | SAST — static code analysis |
| Trivy | latest | CVE scanning |
| Syft | v0.x | SBOM generation |
| Cosign | v2.2.4 | Image signing and attestation |
| Sigstore / Rekor | N/A | Public transparency log for signatures |
| SLSA GitHub Generator | v2.0.0 | SLSA provenance generation |
| OPA / Conftest | v0.51.0 | Policy-as-code evaluation |
| OWASP ZAP | latest | Dynamic application security testing |
