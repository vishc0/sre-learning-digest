# Runbook 03: Image Integrity Failure — Unsigned or Tampered Image

**Scenario**: Gatekeeper policy rejects unsigned image; deployment fails. OR: Cosign verification fails on signed image.

**Severity**: HIGH  
**MTTD**: At admission time (immediate)  
**Target MTTR**: 5 minutes (approve image OR rebuild)

---

## Detection

**Alert (Gatekeeper)**: 

error message: "Image 'docker.io/myrepo/payment-service:v1.2.3' rejected: no valid signature found"

OR (Cosign direct check):

cosign verify docker.io/myrepo/payment-service:v1.2.3@sha256:d3f5a6b9c2e...
# Expected: FAILED — invalid signature

**Alert (Registry Policy)**:

ECR scan found CRITICAL CVE in image

---

## Triage

**Is this expected?**

- Was a new image just built? (Check deployment/image tag)
- Is the signing key in place? (Check Cosign config)
- Is this a known-bad image? (Check CVE database)

**Root Cause Assessment**:

1. Image built but not signed (CI/CD process failure)
2. Image tampered after push (supply chain attack)
3. Signing key rotated (Cosign keyless verification issue)
4. Known CVE in image (ECR scanning caught it)

---

## Containment

### Option A: Image Build Failed (No Signature)

**Action**: Block the deployment. Rebuild with signing.

```bash
# Check current image in deployment
kubectl get deployment payment-service -n prod -o jsonpath='{.spec.template.spec.containers[0].image}'
# Expected: docker.io/myrepo/payment-service:v1.2.3 (or with @sha256)

# If Gatekeeper rejected it, the pod is NOT running
kubectl get pods -n prod -l app=payment-service
# Expected: Pending, Events show "ConstraintTemplate deny: no valid signature"

# Action: Trigger rebuild in CI/CD
# In GitHub Actions / GitLab CI:
git push --force-with-lease origin fix/rebuild-and-sign
# CI/CD should:
# 1. Build image
# 2. Sign with Cosign: cosign sign --key cosign.key <image>@<digest>
# 3. Push signed image to ECR
```

### Option B: Image Tampered (Signature Invalid)

**Action**: Investigate the image. Do not deploy.

```bash
# Verify cosign signature
cosign verify --key cosign.pub docker.io/myrepo/payment-service:v1.2.3

# Expected: FAILED with "invalid signature"

# Possible causes:
# 1. Image was modified in transit (registry vulnerability)
# 2. Signing key was compromised (need key rotation)
# 3. Wrong key being used (verify key source)

# Action: Quarantine the image
aws ecr put-image-scan-findings-config \
  --repository-name myrepo/payment-service \
  --image-scan-findings-config scanOnPush=true

# And: Revoke signing key, generate new one
# cosign generate-key-pair
```

### Option C: Known CVE (ECR Scan)

**Action**: Rebuild with patched base image. Do not deploy.

```bash
# Check scan findings
aws ecr describe-image-scan-findings \
  --repository-name myrepo/payment-service \
  --image-id imageTag=v1.2.3

# Expected: CRITICAL findings (e.g., CVE-2024-1234)

# Action: Update Dockerfile base image
# FROM alpine:3.18  →  FROM alpine:3.19 (or latest patched version)

# Rebuild and sign
docker build -t docker.io/myrepo/payment-service:v1.2.4 .
docker push docker.io/myrepo/payment-service:v1.2.4
cosign sign --key cosign.key docker.io/myrepo/payment-service:v1.2.4@<digest>
```

---

## Eradication

### Step 1: Fix the Root Cause

**If unsigned**: Sign the image

```bash
# Cosign keyless signing (recommended for production)
cosign sign --keyless docker.io/myrepo/payment-service:v1.2.3@sha256:d3f5a6b9c2e...
# Requires OIDC provider (GitHub, Google, etc.)

# Or: Cosign with key file
cosign sign --key cosign.key docker.io/myrepo/payment-service:v1.2.3@sha256:d3f5a6b9c2e...
```

**If tampered**: Generate new signing key + rebuild

```bash
cosign generate-key-pair
# Prompts for password, stores cosign.key and cosign.pub

# Update CI/CD to use new key
# Rebuild all recent images with new signature
```

**If CVE found**: Patch base image + rebuild

```bash
# Update Dockerfile
sed -i 's/FROM alpine:3.18/FROM alpine:3.19/g' Dockerfile

# Rebuild with higher tag
docker build -t docker.io/myrepo/payment-service:v1.2.4 .
docker push docker.io/myrepo/payment-service:v1.2.4
cosign sign --key cosign.key docker.io/myrepo/payment-service:v1.2.4@<digest>
```

### Step 2: Update Deployment

```bash
# Roll out the new, signed image
kubectl set image deployment/payment-service \
  payment-service=docker.io/myrepo/payment-service:v1.2.4 \
  -n prod

# Monitor rollout
kubectl rollout status deployment/payment-service -n prod --timeout=5m
```

### Step 3: Verify Admission

```bash
# New pod should be admitted by Gatekeeper
kubectl get pods -n prod -l app=payment-service -o wide
# Expected: pods in Running state (not Pending)

# Check for admission webhooks logs
kubectl logs -n gatekeeper system-gatekeeper-audit -f | grep "payment-service"
# Expected: "constraint matched" and "audit: ALLOW" (warn-mode) or silent (deny-mode)
```

---

## Recovery

### Step 1: Verify New Image Is Signed

```bash
cosign verify docker.io/myrepo/payment-service:v1.2.4@sha256:new-digest

# Expected: Certificate found in "transparencyLog"
# OR: "Subject CN verified"
```

### Step 2: Scan New Image for CVEs

```bash
aws ecr describe-image-scan-findings \
  --repository-name myrepo/payment-service \
  --image-id imageTag=v1.2.4

# Expected: No CRITICAL findings (or acceptable risk list)
```

### Step 3: Update ECR Policy

```bash
# Enforce image signing for this repository
cat > /tmp/ecr-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "ecr:BatchGetImage",
      "Condition": {
        "StringLike": {
          "aws:imageTag": "v1.2.3"
        }
      }
    }
  ]
}
EOF

aws ecr set-repository-policy \
  --repository-name myrepo/payment-service \
  --policy-text file:///tmp/ecr-policy.json
```

---

## Post-Incident Review

**Incident ID**: INC-2026-0611-003  
**Root Cause**: CI/CD signing step skipped when developer force-pushed directly to ECR.

**Timeline**:
- T+0: Gatekeeper rejects unsigned image at deployment time
- T+5min: Deployment fails, incident paged
- T+15min: Root cause identified (missing cosign step)
- T+20min: Image re-signed, deployment retried
- T+30min: Pods healthy, incident closed

### Action Items

- [ ] Make Cosign a required step in CI/CD gate (SLA: fail build if not signed) — 3 days
- [ ] Add image registry to allowed list (only docker.io/myrepo) — 1 day
- [ ] Document signing key rotation procedure — 1 week
- [ ] Set up transparency log monitoring (Rekor integration) — 2 weeks

### What Went Well

✓ Gatekeeper caught the issue before deployment  
✓ Admission control worked as intended  
✓ Fast diagnosis and remediation  

### What We'd Improve

✗ Why can developer push directly to ECR without signature?  
→ **Fix**: Require all image pushes to be signed; enforce in ECR policy  

---

**Signed**: On-call SRE  
**Date**: 2026-06-11
