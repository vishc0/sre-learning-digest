# Runbook: High SLO Burn Rate Alert

**Runbook ID**: NOTIF-RB-001  
**Applies to**: All three notification platform SLOs (SMS delivery, push latency, API availability)  
**Alert name**: `SMSDeliveryBurnRate`, `PushLatencyBurnRate`, `NotificationAPIAvailabilityBurnRate`  
**Severity**: Critical (page) or Warning (ticket) — see alert labels  
**Owner**: SRE Notification Team  
**Last validated**: Q1 2026 (validated during game day — procedure confirmed correct)

---

## What This Alert Means

You are consuming your monthly error budget faster than sustainable. The alert fires on two conditions:

| Alert window | Burn rate threshold | Meaning |
|---|---|---|
| 1-hour | 14.4x | You will exhaust the monthly budget in ~2 hours at current rate |
| 6-hour | 6.0x | You will exhaust the monthly budget in ~5 days at current rate |

**Critical (page)**: Either threshold is breached.  
**Warning (ticket)**: 6-hour burn rate is between 3.0 and 6.0 (slow degradation).

Do NOT acknowledge and go back to sleep. Even a warning-level burn rate can compound into a full budget exhaustion by end of month if unchecked.

---

## Before You Start

**Do not** open the dashboard and start changing things. Diagnosis before action.

**Check first**: Is there a known maintenance window or planned deployment in progress?  
- Check Slack #deployments for activity in the last 30 minutes.  
- Check the Grafana deployment annotations (blue vertical lines on the SLO dashboard).  
- If a deployment is in progress, notify the deployer immediately and assess rollback.

**Gather context (2 minutes)**:
- Which SLO is burning? (SMS / Push / API)
- What is the burn rate right now? (1h window vs. 6h window)
- When did the burn start? (Check the time series on Panel 2)

---

## Step 1: Open the SLO Dashboard

**URL**: `https://grafana.internal/d/notif-slo/notification-platform-slo`

**What to look for**:
- Panel 1 (Error Budget Remaining): What percentage is left?
- Panel 2 (Burn Rate): When did the burn rate spike? Is it still rising or leveling off?
- Panel 3 (Queue Depth): Are DLQs growing?
- Panel 4 (Consumer Throughput): Is consume rate dropping while queue depth rises?

**Decision point**:
- If DLQs are growing AND consume rate is dropping → go to **Step 3: Queue Investigation**
- If DLQs are flat AND API error rate is high → go to **Step 4: API Error Investigation**
- If DLQs are flat AND push latency is the burning SLO → go to **Step 5: Latency Investigation**

---

## Step 2: Check for Recent Deployments

A deployment 15–45 minutes before the burn started is the most common cause.

```bash
# Check Helm release history for all notification services
helm history notification-api -n notification --max 5
helm history notification-sms-consumer -n notification --max 5
helm history notification-push-consumer -n notification --max 5
```

**EXPECTED_OUTPUT** (example — dates will vary):
```
REVISION  UPDATED                   STATUS     CHART                       APP VERSION  DESCRIPTION
5         2026-01-15 14:23:07 UTC   deployed   notification-api-2.4.1      2.4.1        Upgrade complete
4         2026-01-10 09:11:44 UTC   deployed   notification-api-2.4.0      2.4.0        Upgrade complete
```

**If a recent deployment exists**:
```bash
# Check error rate of current vs. previous revision in Splunk (saved search)
# Saved search name: "notification_deployment_error_comparison"
# OR check the canary rollback status:
kubectl get rollout notification-api -n notification
```

**If current revision is causing errors — rollback immediately**:
```bash
helm rollback notification-api -n notification
# This reverts to the previous revision. Takes ~60 seconds for pods to restart.
```

**EXPECTED_OUTPUT after rollback**:
```
Rollback was a success! Happy Helming!
```

Monitor burn rate on Panel 2 for 5 minutes. If burn rate drops below 1.0, the deployment was the cause — proceed to post-incident. If burn rate does not drop, continue investigation.

---

## Step 3: Queue Investigation (DLQ Growing)

If Panel 3 shows DLQ depth growing, consumers are failing silently.

```bash
# Check consumer pod status
kubectl get pods -n notification -l app=sms-consumer
kubectl get pods -n notification -l app=push-consumer
```

**EXPECTED_OUTPUT** (healthy):
```
NAME                              READY   STATUS    RESTARTS   AGE
sms-consumer-7d8f9b4c6-2xkpq     1/1     Running   0          2d
sms-consumer-7d8f9b4c6-8mnrt     1/1     Running   0          2d
```

**If pods show CrashLoopBackOff or high RESTARTS**:
```bash
# Get logs from a failing pod
kubectl logs -n notification <pod-name> --previous --tail=100
```

Look for:
- `connection refused` → RabbitMQ connection lost
- `Cassandra timeout` → Cassandra write latency spike
- `Redis timeout` → Redis unavailable (dedup/rate limit layer)
- `OutOfMemoryError` / `OOM kill` → Pod memory limit too low (HPA may be needed)

**If RabbitMQ connection is the issue**:
```bash
# Check RabbitMQ cluster health
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqctl cluster_status
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqctl list_queues name messages consumers
```

**EXPECTED_OUTPUT** (healthy):
```
Cluster status of node rabbit@rabbitmq-0
Disk Nodes: rabbit@rabbitmq-0, rabbit@rabbitmq-1, rabbit@rabbitmq-2
Running Nodes: rabbit@rabbitmq-0, rabbit@rabbitmq-1, rabbit@rabbitmq-2
Alarms: []
```

If a RabbitMQ node is down: escalate to the infrastructure team (pager: #infra-oncall). This is beyond the notification SRE team's blast radius.

**To temporarily drain the DLQ (use only after root cause is identified)**:
```bash
# Inspect DLQ — do NOT delete messages without saving them first
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqctl list_queues name messages
# DLQ messages are also archived to S3 automatically — verify before any delete action
aws s3 ls s3://notification-dlq-archive/$(date +%Y/%m/%d)/ --region us-east-1
```

---

## Step 4: API Error Investigation (5xx Rate High)

Check whether errors are coming from the API pods themselves or from a downstream dependency.

```bash
# Check API pod logs for 5xx patterns
kubectl logs -n notification -l app=notification-api --tail=200 | grep -E '"status":5[0-9][0-9]'
```

**Common 5xx root causes and remediation**:

| Log pattern | Root cause | Remediation |
|---|---|---|
| `Cassandra host unavailable` | Cassandra node down or slow | Check Cassandra metrics; if a node is down, reduce replication factor temporarily or scale down the affected AZ |
| `Redis connection pool exhausted` | Redis max connections hit | Increase `maxmemory-clients` in Redis config or scale Redis; check for connection leaks in consumer code |
| `RabbitMQ publish timeout` | RabbitMQ publish queue backed up | Check RabbitMQ queue depth; may need to scale consumers |
| `Downstream carrier timeout` | Twilio/FCM having an incident | Check vendor status pages; if external, errors are carrier_fault=true and do NOT consume error budget |

```bash
# Check carrier health (these are external status pages — verify manually)
# Twilio: https://status.twilio.com
# Firebase/FCM: https://status.firebase.google.com
# APNs: https://developer.apple.com/system-status/
```

**If carrier is the cause**: Update the `carrier_fault` label in the metrics pipeline to correctly tag these failures. They should not consume your SLO error budget.

---

## Step 5: Latency Investigation (Push P95 Degraded)

Push latency breaches usually come from one of three sources: consumer pod CPU saturation, downstream FCM/APNs latency, or Redis slowdown (dedup layer adds latency).

```bash
# Check consumer pod resource utilization
kubectl top pods -n notification -l app=push-consumer
```

**EXPECTED_OUTPUT** (healthy):
```
NAME                               CPU(cores)   MEMORY(bytes)
push-consumer-6f9b8d7c-abcd1       142m         384Mi
push-consumer-6f9b8d7c-efgh2       138m         391Mi
```

If CPU is above 800m (near the 1000m limit) for most pods, the consumer is CPU-bound:
```bash
# Trigger HPA scale-out manually if autoscaler is lagging
kubectl scale deployment push-consumer -n notification --replicas=12
# Standard is 8 replicas; 12 is the maximum before RabbitMQ prefetch needs tuning
```

**Check Redis latency** (dedup layer):
```bash
kubectl exec -n redis redis-master-0 -- redis-cli --latency-history -i 5
```

If Redis P99 latency is above 10ms, the dedup check is adding latency to every message. Options:
1. Increase Redis memory allocation (contact infra team)
2. Temporarily increase the dedup TTL to reduce key lookup volume

---

## Step 6: Communication

When burn rate is above 14.4x (critical):

1. Post to Slack **#notification-incidents** immediately:
   ```
   :alert: SLO BURN RATE ACTIVE
   SLO: [SMS / Push / API]
   Burn rate: [current 1h burn rate]
   Budget remaining: [% from Panel 1]
   Status: Investigating
   IC: @[your name]
   ```

2. If burn rate is sustained above 6.0x for more than 30 minutes, notify:
   - Engineering Manager (Slack DM)
   - Upstream team leads if API availability SLO is burning (CRM, billing teams may be seeing errors)

3. Every 15 minutes until resolved, post a status update in **#notification-incidents**.

---

## Step 7: Declare Resolution

The incident is resolved when burn rate drops below 1.0 and has been below 1.0 for 10 consecutive minutes.

```bash
# Confirm burn rate via Prometheus query
# Run this in Grafana Explore or via promtool:
# sum(rate(notification_sms_delivery_total{status="failed",carrier_fault="false"}[1h])) 
# / 
# sum(rate(notification_sms_delivery_total{carrier_fault="false"}[1h])) 
# / (1 - 0.995)
# Should return a value < 1.0
```

Post resolution to Slack **#notification-incidents**:
```
:white_check_mark: RESOLVED
SLO: [name]
Duration: [start time to end time]
Root cause: [one sentence]
Budget consumed this incident: [% of monthly budget]
PIR required: [yes/no — yes if > 10% budget consumed]
```

---

## Escalation Path

| Situation | Escalate to | How |
|---|---|---|
| Burn rate > 14.4x, cause not found in 20 min | SRE Manager | PagerDuty escalation + Slack DM |
| RabbitMQ node down | Infrastructure on-call | PagerDuty team: infra-oncall |
| Cassandra node down | DBA on-call | PagerDuty team: dba-oncall |
| Carrier outage affecting regulated notifications (fraud alerts) | Engineering Manager + Legal | Slack + phone |
| Budget > 75% consumed this month | Engineering Manager | Slack DM immediately |

---

## Post-Incident Requirements

- If budget consumed > 5% in a single incident: open a Post-Incident Review (PIR) Jira ticket within 4 hours.
- PIR must be completed within 5 business days.
- PIR template: `https://wiki.internal/templates/pir`
- All PIRs are blameless. The goal is system improvement, not attribution.
