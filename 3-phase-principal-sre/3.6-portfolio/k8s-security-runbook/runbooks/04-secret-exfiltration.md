# Runbook 04: Secret Exfiltration

**Scenario**: CloudWatch shows unusual "get secrets" API calls from a pod.

**Severity**: HIGH  
**MTTD**: 5-30 minutes  
**Target MTTR**: 15 minutes

---

## Detection

**Alert (CloudWatch Insights)**:

Unusual number of "get secrets" API calls from pod IP (10.0.5.99)

**OR (Falco Rule)**:

Secret API Key Read By Suspicious User
Container: auth-service-xyz
Secrets accessed: payment-db-password, stripe-api-key

---

## Triage

**Questions**:

1. Is this a known operation?
2. How many secrets accessed?
3. Exfiltrated to external IP?
4. Which SA/User initiated reads?

**Severity Assessment**:

50 reads + egress to external IP = CRITICAL
5 reads + no egress + normal SA = LOW

---

## Containment

### Step 1: Identify the Pod

kubectl get pods --all-namespaces -o wide | grep 10.0.5.99

### Step 2: Verify Service Account

kubectl get pod auth-service-xyz -n prod -o jsonpath='{.spec.serviceAccountName}'

### Step 3: Check Egress

Monitor network logs for outbound connections from pod IP.

### Step 4: Isolate the Pod

kubectl apply -f - << EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: isolate-auth-service-xyz
  namespace: prod
spec:
  podSelector:
    matchLabels:
      pod: auth-service-xyz
  policyTypes:
    - Egress
  egress:
    - to:
        - podSelector: {}
      ports:
        - protocol: TCP
          port: 5432
EOF

### Step 5: Revoke Pod Permissions

kubectl delete rolebinding auth-service-get-secrets -n prod

---

## Eradication

### Step 1: Rotate ALL Secrets

Assume all secrets readable by this SA were compromised.

kubectl patch secret payment-db-password -n prod --patch '{"metadata":{"annotations":{"rotation-time":"'$(date -u +%s)'"}}}'

Also rotate externally:
- Database passwords
- API keys (Stripe, etc.)
- SSH keys

### Step 2: List All Secrets Read

Query CloudWatch for all "get secrets" calls from auth-service SA during incident.

### Step 3: Update RBAC

Create least-privilege role: no "get secrets" unless explicitly allowlisted.

---

## Recovery

### Step 1: Restart Pod

kubectl rollout restart deployment/auth-service -n prod

### Step 2: Verify Access Denied

kubectl auth can-i get secrets --as=system:serviceaccount:prod:auth-service -n prod
# Expected: no

### Step 3: Monitor for Abuse

Alert if auth-service attempts "get secrets" again (should be denied).

---

## Post-Incident Review

**Incident ID**: INC-2026-0611-004  
**Root Cause**: Overprivileged RBAC ("get secrets *" allowall)

### Action Items

- [ ] Gatekeeper policy: deny "get secrets" without allowlist (1 week)
- [ ] CI/CD check: detect overprivileged RBAC in PR (3 days)
- [ ] CloudWatch dashboard: alert on secret reads >10/min (2 days)

### What Went Well

✓ CloudWatch alert triggered quickly  
✓ Isolation prevented further exfiltration  
✓ Comprehensive secret rotation  

### What We'd Improve

✗ Why was "get secrets *" granted?  
→ Fix: Require explicit resourceNames allowlist  

---

**Signed**: On-call SRE  
**Date**: 2026-06-11
