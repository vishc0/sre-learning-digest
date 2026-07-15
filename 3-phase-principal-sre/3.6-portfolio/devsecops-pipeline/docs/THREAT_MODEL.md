# Supply Chain Threat Model
## DevSecOps Pipeline — Portfolio Project
**Author**: Vishweshwar Chippa
**Date**: 2025-06
**Version**: 1.0

---

## Threat Modeling Methodology

Using STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure,
Denial of Service, Elevation of Privilege) focused on the CI/CD supply chain.
Attack vectors mapped to MITRE ATT&CK for Enterprise (Initial Access, Execution,
Persistence via supply chain techniques).

---

## Attack Surface Overview

```
Developer Workstation -> GitHub (Source) -> GitHub Actions (Build) -> GHCR (Registry) -> EKS (Runtime)
         |                    |                    |                    |                  |
    [Secret leak]     [Branch bypass]      [Build injection]    [Image tamper]    [Runtime escape]
```

---

## Attack Vector 1: Malicious Dependency Injection (SolarWinds Pattern)

**Description**: An attacker compromises an upstream package (e.g., a PyPI package your
`requirements.txt` depends on) and publishes a malicious version. Your pipeline pulls the
new version on next build, injecting malicious code without any developer action.

**Real examples**: SolarWinds Orion (2021), XZ Utils (2024), event-stream (npm, 2018).

**Attack flow**:
1. Attacker identifies a popular dependency in your SBOM (e.g., `flask`, `requests`)
2. Attacker compromises the maintainer account (credential stuffing or phishing)
3. Attacker publishes a malicious patch version
4. Your pipeline pins `flask>=3.0` (not pinned to exact version) and pulls the malicious version
5. Malicious code executes at container startup — data exfiltration, cryptominer, backdoor

**Likelihood**: Medium (requires upstream compromise, but happens multiple times per year)
**Impact**: Critical (malicious code runs in production with app privileges)

**Mitigations implemented in this pipeline**:

| Mitigation | Implementation | Where in Pipeline |
|---|---|---|
| Dependency pinning | `requirements.txt` uses exact versions (`flask==3.0.3`) | Dockerfile / src |
| Hash verification | `pip install --require-hashes` in production builds | Dockerfile |
| SCA scanning | Trivy scans all dependencies against CVE databases | sca-scan job |
| SBOM generation | Syft generates a manifest of all dependencies | sbom job |
| Dependency review | GitHub Dependency Review Action on PRs | PR gate |

**Residual risk**: A zero-day malicious package that is not yet in any CVE database will
pass the CVE scan. Mitigation: behavioral analysis at runtime (Falco) + SBOM drift detection.

---

## Attack Vector 2: Build System Compromise (Codecov Pattern)

**Description**: An attacker gains access to the CI/CD system itself (GitHub Actions runner,
build server, or CI configuration) and injects malicious steps into the build process.
The resulting artifact appears legitimate — correct source, correct binary — but contains
a backdoor inserted during the build phase.

**Real examples**: Codecov bash uploader (2021), CircleCI breach (2023).

**Attack flow**:
1. Attacker compromises a GitHub Actions secret (leaked in logs, misconfigured scope)
2. OR: Attacker submits a PR to a fork that modifies the pipeline YAML
3. OR: Attacker compromises a third-party GitHub Action used in the pipeline
4. Build step exfiltrates secrets, modifies the binary, or adds a malicious layer to the image
5. Malicious image passes CVE scan (no known CVE) and gets deployed

**Likelihood**: Medium (CI secrets are frequently misconfigured)
**Impact**: Critical (attacker controls the build outputs)

**Mitigations implemented in this pipeline**:

| Mitigation | Implementation | Where in Pipeline |
|---|---|---|
| Pinned action versions | All `uses: action@v4` — never `uses: action@main` | All jobs |
| Minimal permissions | `permissions: contents: read` default; scoped up per job | Workflow level |
| No self-hosted runners | GitHub-hosted runners only (SLSA Level 2 requirement) | Workflow config |
| Secret scanning | Gitleaks scans all commits | secret-scan job |
| Keyless image signing | Signing identity is the GitHub OIDC workflow, not a secret | sign job |
| PR protection | Branch protection + required status checks | GitHub settings |
| Isolated build environment | Each job runs in a fresh ephemeral runner | GitHub Actions arch |

**Residual risk**: A compromised GitHub Actions itself (GitHub infrastructure breach).
Mitigation: out of scope for a single team — rely on GitHub's own security posture and
audit logging.

---

## Attack Vector 3: Registry Tampering (Image Substitution Attack)

**Description**: An attacker gains write access to the container registry and replaces
a legitimate image with a malicious one, keeping the same tag. The deployment pipeline
deploys the malicious image, which passes tag-based checks but was never scanned or signed.

**Attack flow**:
1. Attacker compromises a registry credential (leaked PAT, misconfigured IAM policy)
2. Attacker pushes a malicious image with the same tag as the current production image
3. Deployment pipeline reads `image: myapp:latest` and deploys the malicious image
4. The malicious image was never scanned, never signed, never policy-checked
5. OPA policy check is bypassed because it ran against the ORIGINAL image, not this replacement

**Likelihood**: Low-Medium (requires registry credential compromise)
**Impact**: Critical (full application compromise in production)

**Mitigations implemented in this pipeline**:

| Mitigation | Implementation | Where in Pipeline |
|---|---|---|
| Digest-based references | Images referenced as `@sha256:...` not `:latest` | OPA policy, deploy job |
| Image signing | Cosign signature is bound to the specific digest | sign job |
| Signature verification at deploy | Admission webhook (Kyverno/OPA) verifies signature | Cluster-level |
| OPA image allowlist | Only images from approved registries are admitted | policy-gate job |
| GHCR immutable tags | GitHub Packages supports immutable image tags | Registry config |

**Residual risk**: If the cluster-level admission webhook is misconfigured or bypassed,
a tampered image could still deploy. Mitigation: audit all Kubernetes admission webhook
configurations quarterly.

---

## Residual Risk Summary

| Risk | Likelihood | Impact | Residual after mitigations |
|---|---|---|---|
| Zero-day malicious package | Low | Critical | Medium — SBOM enables rapid identification |
| GitHub Actions infrastructure breach | Very Low | Critical | Low — out of team's control surface |
| Cluster admission webhook misconfiguration | Low | High | Low — quarterly audit process |
| Developer machine compromise | Medium | High | Medium — branch protection limits blast radius |

---

## Recommendations for Production Enhancement

1. **Private Rekor instance**: For regulated environments, run an internal Rekor so
   signatures are not published to the public transparency log.
2. **Dependency-Track integration**: Connect Syft SBOM output to Dependency-Track for
   continuous CVE monitoring of deployed SBOMs (not just build-time scanning).
3. **Runtime behavioral analysis**: Deploy Falco to detect anomalous container behavior
   that a supply chain attack might trigger at runtime.
4. **SLSA Level 3 upgrade**: Move to `slsa-github-generator` hermetic builds to prevent
   pipeline script forgery of provenance documents.
