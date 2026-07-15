# Runbook 05: Supply Chain Compromise — Known-Bad Image Digest in Production

**Scenario**: Security advisory: image digest XYZ has backdoor. You have 10 pods running this image.

**Severity**: CRITICAL  
**MTTD**: Immediate (external alert)  
**Target MTTR**: 15 minutes (nuke all instances)

---

## Detection

**Alert (External)**:

CISA Advisory: Docker image digest sha256:d3f5a6b9c2e1f8... contains backdoor
Affects: myrepo/payment-service versions v1.0.0 — v1.2.3
Action: Immediately remove from production

**Alert (Internal)**:

Falco rule: "Known-Bad Image Digest Detected"
Container: payment-service-abc123
Digest: d3f5a6b9c2e1f8g7h4i9j0k1l2m3n4o5p6q7r8s9

---

## Triage

**Questions**:

1. Which deployments use this image?
2. How many pods are running it?
3. Is this digest in ANY production registry?
4. What was deployed by which digest version?

**Find All Instances**:

kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{.spec.containers[*].image}{"\n"}{end}' | \
  grep "d3f5a6b9c2e1f8"

# Expected:
docker.io/myrepo/payment-service:v1.2.3@sha256:d3f5a6b9c2e1f8
docker.io/myrepo/payment-service:v1.2.2@sha256:d3f5a6b9c2e1f8
docker.io/myrepo/payment-service:v1.2.1@sha256:d3f5a6b9c2e1f8

**Count Impact**:

kubectl get pods --all-namespaces -o json | \
  jq '[.items[] | select(.spec.containers[].image | contains("d3f5a6b9c2e1f8"))] | length'

# Expected: 10 pods affected

---

## Containment (Minutes 0-5)

### Step 1: Identify Deployment Name

kubectl get pods --all-namespaces -o wide | grep "d3f5a6b9c2e1f8"

# Expected:
payment-service-abc123     prod        Running   10.0.5.123
payment-service-def456     prod        Running   10.0.5.234
auth-service-ghi789        prod        Running   10.0.6.345

### Step 2: Quarantine Image in Registry

Prevent ANY new deployment from using this digest.

ECR policy:

aws ecr put-image-scan-findings-config \
  --repository-name myrepo/payment-service \
  --image-scan-findings-config scanOnPush=true

Also: Tag digest as QUARANTINED in ECR

aws ecr tag-resource \
  --resource-arn arn:aws:ecr:us-east-1:123456789012:repository/myrepo/payment-service \
  --tags quarantined=true

### Step 3: Apply Gatekeeper Deny Policy (Immediate)

kubectl apply -f - << EOF
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredImageDigest
metadata:
  name: deny-known-bad-digest
spec:
  match:
    kinds:
      - apiGroups: ["apps"]
        kinds: ["Deployment", "StatefulSet", "DaemonSet"]
  parameters:
    blockedDigests:
      - d3f5a6b9c2e1f8g7h4i9j0k1l2m3n4o5p6q7r8s9
EOF

# This prevents new pods from being created with the bad digest

---

## Eradication (Minutes 5-15)

### Step 1: Delete All Affected Pods

# Force immediate deletion (no graceful termination)
kubectl delete pods -A --field-selector metadata.name in (payment-service-abc123,payment-service-def456,auth-service-ghi789)

# Expected: Pods terminate immediately; ReplicaSets auto-spawn replacements

### Step 2: Force Deployment Rollout with Safe Image

Update deployments to use patched image (e.g., v1.2.4)

kubectl set image deployment/payment-service \
  payment-service=docker.io/myrepo/payment-service:v1.2.4 \
  -n prod

kubectl set image deployment/auth-service \
  auth-service=docker.io/myrepo/auth-service:v1.1.0 \
  -n prod

### Step 3: Wait for New Pods to Start

kubectl rollout status deployment/payment-service -n prod --timeout=5m
kubectl rollout status deployment/auth-service -n prod --timeout=5m

# Expected: All pods in "Running" state with new digest

### Step 4: Verify NO Old Pods Running

kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{.spec.containers[*].image}{"\n"}{end}' | \
  grep "d3f5a6b9c2e1f8"

# Expected: No output (digest completely removed)

---

## Recovery

### Step 1: Verify New Pods Are Healthy

kubectl logs -f payment-service-xyz -n prod | head -50

# Expected: Normal app startup logs, no errors

### Step 2: Run Smoke Tests

# If your app has a health endpoint:
kubectl exec -it payment-service-xyz -n prod -- curl http://localhost:8080/health

# Expected: HTTP 200 OK

### Step 3: Remove Gatekeeper Policy (After Patched)

Once all bad images are gone, remove the temporary block:

kubectl delete constraint deny-known-bad-digest

### Step 4: Update Image Policy

Ensure future deployments enforce signed images ONLY:

kubectl apply -f gatekeeper-policies/03-require-image-digest.yaml

---

## Post-Incident Review

**Incident ID**: INC-2026-0611-005  
**Root Cause**: Compromised upstream dependency in myrepo/payment-service:v1.2.1—v1.2.3

**Timeline**:
- T+0: CISA alert published
- T+2min: Alert ingested, all instances identified
- T+5min: Gatekeeper policy applied, bad digest quarantined
- T+10min: All bad pods deleted, replacements spawning
- T+15min: Rollout complete, verification passed
- T+20min: Incident closed

### Action Items

- [ ] Publish incident report to DevSecOps team (1 day)
- [ ] Audit all images for similar compromises (24 hours)
- [ ] Implement SBOM scanning in CI/CD (next release cycle)
- [ ] Set up Rekor transparency log monitoring (1 week)

### What Went Well

✓ Fast containment (bad digest in production <5 min)  
✓ Gatekeeper prevented new deployments of bad image  
✓ Zero downtime (ReplicaSets auto-spawned replacements)  

### What We'd Improve

✗ No automated supply chain scanning  
→ Fix: Integrate Syft + Grype in CI/CD for SBOM + CVE scanning  

---

**Signed**: On-call SRE + Security Team  
**Date**: 2026-06-11
