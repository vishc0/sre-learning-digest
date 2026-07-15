# Kubernetes Security Incident Runbook | Week 6 Day 5

## Why This Matters (Interview Relevance + Business Impact)

Security incidents in Kubernetes clusters are not theoretical. In 2024, the CNCF Security Audit found
over-permissioned ServiceAccounts in 73% of production clusters audited. A single compromised pod
with a mounted service account token can pivot to cluster-admin in under 90 seconds.

**What interviewers probe at Staff/Principal/Director level:**
- Can you detect a container escape BEFORE the attacker reaches the node?
- Do you have runbooks practiced before the incident, not written during it?
- Can you explain your RBAC posture to a VP of Engineering in 2 minutes?
- Do your admission controls prevent the bad state from ever entering the cluster?

**Business impact at T-Mobile scale (25M msg/day notification platform):**
- One compromised notification-service pod can read customer PII from mounted secrets
- Cluster-admin ServiceAccount = attacker owns every namespace, every secret, every workload
- Unsigned image in prod = supply chain breach = SOC2 finding = customer trust damage

---

## Portfolio Context

This runbook was built as part of an 8-week SRE/DevSecOps interview preparation program.
It demonstrates the combination of **Kubernetes security depth** (technical IC skills) and
**incident command structure** (Director/VP leadership skills).

**Target audience for this portfolio artifact:**
- Hiring managers assessing Staff/Principal SRE candidates
- DevSecOps team leads evaluating security maturity
- Platform engineering leads evaluating runbook culture

---

## Repository Structure

```
k8s-security-runbook/
├── PORTFOLIO_README.md              # This file
├── runbooks/
│   ├── 01-compromised-pod.md        # Container escape via Falco detection
│   ├── 02-rbac-misconfiguration.md  # Over-permissioned ServiceAccount
│   ├── 03-image-integrity-failure.md # Unsigned image in production
│   ├── 04-secret-exfiltration.md    # Pod reading unauthorized secrets
│   └── 05-supply-chain-compromise.md # Known-malicious image hash in cluster
├── scripts/
│   └── rbac-audit.py                # Scans cluster for over-permissioned ServiceAccounts
├── falco-rules.yaml                 # Custom Falco detection rules for all 5 scenarios
├── gatekeeper-policies/
│   ├── 01-require-seccomp.yaml      # Blocks privileged containers (scenario 1)
│   ├── 02-deny-cluster-admin-sa.yaml # Blocks cluster-admin ServiceAccounts (scenario 2)
│   ├── 03-require-image-digest.yaml # Requires image digest (scenario 3)
│   ├── 04-deny-default-sa.yaml      # Denies default SA token automounting (scenario 4)
│   └── 05-allowed-registries.yaml   # Allowlist of trusted image registries (scenario 5)
└── director-narrative.md            # Org-level K8s security governance framing
```

---

## Incident Scenarios Covered

| # | Scenario | Detection Method | Severity | MTTD Target |
|---|----------|-----------------|----------|-------------|
| 1 | Compromised pod / container escape | Falco runtime rule | P0 / SEV1 | < 5 min |
| 2 | RBAC misconfiguration — cluster-admin SA | rbac-audit.py + OPA | P1 / SEV2 | < 30 min |
| 3 | Image integrity failure — unsigned image | Cosign + Gatekeeper | P1 / SEV2 | Pre-deploy |
| 4 | Secret exfiltration — unauthorized reads | Falco + audit log | P0 / SEV1 | < 5 min |
| 5 | Supply chain compromise — malicious hash | Cosign + Gatekeeper | P0 / SEV1 | Pre-deploy |

---

## Tools Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Runtime detection | Falco | eBPF-based syscall monitoring, custom rules |
| Admission control | OPA Gatekeeper | Policy enforcement at API server level |
| Image signing | Cosign (Sigstore) | Supply chain integrity |
| RBAC auditing | rbac-audit.py (custom) | Cluster-wide over-permission scan |
| Forensics | kubectl, crictl, stern | Post-incident log collection |
| Audit logging | AWS CloudTrail + K8s audit log | Control plane event trail |

---

## Skills Demonstrated

- Kubernetes security threat modeling (STRIDE applied to K8s)
- Falco rule authoring (syscall-level detection)
- OPA/Gatekeeper ConstraintTemplate authoring
- Python automation for RBAC posture assessment
- Incident command structure (Detection → Triage → Containment → Eradication → Recovery → Post-Incident)
- Blameless postmortem culture and SLO impact analysis
- Director-level governance framing (team readiness, not just tool readiness)

---

## Author

Vishweshwar Chippa — SRE Manager, T-Mobile
21 years in SRE/Platform Engineering across telecom, retail, banking, energy.
IIT-BHU Metallurgy | H1B active | Targeting Director/VP SRE roles.
