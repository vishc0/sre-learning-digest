# Runbook 01: Container Escape / Compromised Pod

**Scenario**: Falco detects shell spawning inside a production pod.

**Severity**: HIGH  
**MTTD**: <1 second  
**Target MTTR**: 15 minutes (containment), 30 minutes (full eradication)

---

## Detection

**Alert**: `Alert: Unauthorized process spawned (shell) in container`

Falco Event Output:
  Time: 2026-06-11T14:32:47.123456Z
  Rule: Shell_Spawn_In_Container
  Container: payment-service-abc123
  Namespace: prod

**Expected**: This should NOT appear in normal operations.

### Step 1: Verify Alert

kubectl get pod payment-service-abc123 -n prod -o wide

### Step 2: Classify Severity

**Blast Radius**:
- Pod IP: 10.0.5.123
- Service account: payment-service (used by 3 replicas)
- Secret access: Can read prod namespace secrets
- Network policy: No egress restrictions

**Final Severity**: CRITICAL (high blast radius)

---

## Containment (First 5 Minutes)

### Step 1: Network Isolation

kubectl apply -f - << EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: isolate-payment-service-abc123
  namespace: prod
spec:
  podSelector:
    matchLabels:
      pod: payment-service-abc123
  policyTypes:
    - Ingress
    - Egress
  ingress: []
  egress:
    - to:
        - podSelector: {}
      ports:
        - protocol: UDP
          port: 53
EOF

### Step 2: Evict the Pod

kubectl delete pod payment-service-abc123 -n prod --grace-period=30

### Step 3: Cordon the Node

kubectl cordon node-05

---

## Eradication (Minutes 5-30)

### Step 1: Check Image for Vulnerabilities

aws ecr describe-image-scan-findings \
  --repository-name myrepo/payment-service \
  --image-id imageTag=v1.2.3 \
  --region us-east-1

### Step 2: Revoke Service Account Permissions

kubectl delete rolebinding payment-service-admin -n prod

### Step 3: Rotate All Secrets

kubectl get secrets -n prod -o name | xargs -I {} kubectl delete {}

### Step 4: Quarantine the Image Digest

Prevent new pods from using this image via ECR policy.

### Step 5: Uncordon the Node

kubectl uncordon node-05

---

## Recovery

### Step 1: Verify New Pod

kubectl get pods -n prod -l app=payment-service -o wide
kubectl logs payment-service-def456 -n prod | tail -20

### Step 2: Clean Up Isolation Policies

kubectl delete networkpolicy isolate-payment-service-abc123 -n prod

### Step 3: Deploy Fixed Image

kubectl set image deployment/payment-service \
  payment-service=docker.io/myrepo/payment-service:v1.2.4 \
  -n prod

kubectl rollout status deployment/payment-service -n prod --timeout=5m

---

## Post-Incident Review

**Incident ID**: INC-2026-0611-001  
**Duration**: 45 minutes

### Root Cause

Timeline:
- 14:32:47: Falco detects shell
- 14:33:00: On-call alerted
- 14:35:00: Pod isolated
- 14:40:00: Secrets rotated
- 14:50:00: Node uncordoned
- 15:00:00: Closed

**Root**: CVE-2024-1234 in libssl3 (RCE via compromised dependency)

### Action Items

- [ ] Scan all ECR images for CVE-2024-1234 (SLA: 24 hours)
- [ ] Add image scanning to CI/CD gate (Owner: Platform team, 1 week)
- [ ] Add alert for multiple shell spawns (Owner: SRE team, 3 days)
- [ ] Capture syscall traces to S3 before pod deletion (1 week)

### What Went Well

✓ Falco detected in <1 second  
✓ Auto-isolation prevented lateral movement  
✓ ReplicaSet auto-spawn ensured zero downtime  

### What We'd Improve

✗ Forensic data lost (pod terminated before capture)  
✗ No automated secret rotation  
✗ Image scanner lag (CVE not caught)  

---

**Signed**: On-call SRE  
**Date**: 2026-06-11
