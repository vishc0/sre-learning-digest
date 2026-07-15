# Runbook 02: RBAC Misconfiguration — Overprivileged ServiceAccount

**Scenario**: Audit reveals payment-service SA has cluster-admin (or wildcard * permissions).

**Severity**: CRITICAL  
**MTTD**: 1-2 hours (requires manual audit)  
**Target MTTR**: 30 minutes (revoke permissions)

---

## Detection

**Alert**: `rbac-audit.py` identifies cluster-admin binding to user-managed SA.

```bash
python scripts/rbac-audit.py --kubeconfig ~/.kube/config --output json | \
  jq '.checks[] | select(.status=="CRITICAL")'

# Expected output:
{
  "check": "cluster_admin_sa",
  "status": "CRITICAL",
  "finding": "ServiceAccount 'payment-service' has ClusterRoleBinding to 'cluster-admin'",
  "namespace": "prod",
  "sa": "payment-service",
  "recommendation": "Delete ClusterRoleBinding immediately; use least-privilege Role instead"
}
```

---

## Triage

**Blast Radius**:
- Any pod using payment-service SA can: create/delete/modify ANY Kubernetes resource
- Can read/write all Secrets (including kube-system)
- Can modify RBAC (create new admin users, exfiltrate credentials)
- Can escape to other namespaces

**Confidence**: 100% (RBAC API is declarative, no ambiguity)

**Severity**: CRITICAL (assume SA is compromised; revoke immediately)

---

## Containment

### Step 1: Identify All Pods Using This SA

```bash
kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.serviceAccountName}{"\t"}{.metadata.namespace}{"\n"}{end}' | \
  grep "payment-service"

# Expected output:
# payment-service-abc123     payment-service     prod
# payment-service-def456     payment-service     prod
# payment-service-ghi789     payment-service     prod
```

### Step 2: Snapshot Current RBAC

```bash
kubectl get clusterrolebinding -o yaml > /tmp/crb-backup-$(date +%s).yaml
kubectl get rolebinding -A -o yaml > /tmp/rb-backup-$(date +%s).yaml

# Archive to S3 for forensics
aws s3 cp /tmp/crb-backup-*.yaml s3://incident-artifacts/rbac-backups/
```

### Step 3: Revoke cluster-admin Binding

```bash
# IMMEDIATELY delete the overprivileged binding
kubectl delete clusterrolebinding <binding-name>

# Example:
kubectl delete clusterrolebinding payment-service-admin

# Verify deletion
kubectl get clusterrolebindings | grep payment-service || echo "Deleted successfully"
```

---

## Eradication

### Step 1: Create Least-Privilege Role

```bash
kubectl apply -f - << EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: payment-service-least-privilege
  namespace: prod
rules:
# List pods (for discovery)
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
# Read ConfigMaps (for app config)
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]
# Read Secrets (ONLY if needed; otherwise remove)
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get"]
  resourceNames: ["payment-db-creds", "payment-api-key"]  # Allowlist specific secrets
# Leader election (if using)
- apiGroups: [""]
  resources: ["leases"]
  verbs: ["get", "create", "update"]
  resourceNames: ["payment-service-leader"]
EOF

# Verify role created
kubectl get role -n prod
```

### Step 2: Create RoleBinding

```bash
kubectl apply -f - << EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: payment-service-least-privilege
  namespace: prod
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: payment-service-least-privilege
subjects:
- kind: ServiceAccount
  name: payment-service
  namespace: prod
EOF

# Verify binding
kubectl get rolebinding -n prod
```

### Step 3: Test New Permissions (Dry-Run)

```bash
# As the payment-service SA, verify permissions work
kubectl auth can-i get pods --as=system:serviceaccount:prod:payment-service -n prod
# Expected: yes

kubectl auth can-i delete pods --as=system:serviceaccount:prod:payment-service -n prod
# Expected: no

kubectl auth can-i get secrets --as=system:serviceaccount:prod:payment-service -n prod
# Expected: yes (but only specific secrets)

kubectl auth can-i create clusterrolebindings --as=system:serviceaccount:prod:payment-service
# Expected: no (no cluster scope)
```

### Step 4: Verify Pods Still Function

```bash
# Restart one pod to verify new SA permissions are sufficient
kubectl delete pod payment-service-abc123 -n prod

# Wait for new pod to start
kubectl get pods -n prod -l app=payment-service -w

# Check pod logs (should be normal, no permission errors)
kubectl logs -f payment-service-abc123 -n prod | grep -i "permission\|denied\|unauthorized" || echo "Clean"
```

---

## Recovery

### Step 1: Rolling Update All Replicas

```bash
# Force all pods to restart (and use new SA with restricted permissions)
kubectl rollout restart deployment/payment-service -n prod

# Monitor rollout
kubectl rollout status deployment/payment-service -n prod --timeout=5m
```

### Step 2: Audit Logs for Abuse

```bash
# Check if any pod using payment-service SA created/modified RBAC while over-privileged
kubectl logs -n kube-apiserver <apiserver-pod> | \
  grep -i "clusterrolebinding\|rolebinding" | \
  grep "payment-service" | \
  head -20

# Or query CloudWatch Logs (if configured)
aws logs filter-log-events \
  --log-group-name /aws/eks/cluster/my-cluster/audit \
  --filter-pattern "payment-service" \
  --start-time $(($(date +%s) - 86400))000 \
  | jq '.events[] | select(.message | contains("ClusterRoleBinding"))'
```

### Step 3: Check for Credential Exfiltration

```bash
# If SA could read secrets, rotate all secrets in the namespace
kubectl get secrets -n prod -o name | while read secret; do
  echo "Rotating: $secret"
  # For actual rotation, trigger in external system (Vault, AWS Secrets Manager)
  # For Kubernetes secrets: delete and recreate
  kubectl delete "$secret" -n prod
done

# Recreate secrets (or they auto-renew if using external sync)
kubectl apply -f /path/to/secrets-manifests/
```

### Step 4: Review Other SAs

```bash
# Run audit script to check for similar RBAC issues
python scripts/rbac-audit.py --kubeconfig ~/.kube/config --output table

# Look for other CRITICAL findings and repeat this runbook
```

---

## Post-Incident Review

**Incident ID**: INC-2026-0611-002  
**Root Cause**: Developer granted cluster-admin for "convenience" 6 months ago; never reviewed.

**Timeline**:
- T+0: Audit script flags cluster-admin binding
- T+15min: On-call verifies, revokes immediately
- T+30min: Least-privilege role created
- T+45min: All pods restarted with new permissions
- T+60min: Audit logs reviewed; no abuse found
- T+90min: Incident closed

### Action Items

- [ ] Automate RBAC audit in CI/CD (fail build if cluster-admin detected) — 1 week
- [ ] Implement Gatekeeper policy to deny cluster-admin SA (warn-mode) — 2 weeks
- [ ] Quarterly RBAC review (check for privilege creep) — recurring
- [ ] Add "SA permissions audit" to security runbook template — 3 days

### What Went Well

✓ Audit identified problem  
✓ Least-privilege role was well-thought-out  
✓ No abuse detected (lucky, but process still sound)  

### What We'd Improve

✗ Why wasn't this caught during code review 6 months ago?  
→ **Fix**: Require security team sign-off on any RBAC changes  

---

**Signed**: On-call SRE  
**Date**: 2026-06-11
