# Runbook: RabbitMQ Queue Backup / DLQ Alert

**Runbook ID**: NOTIF-RB-002  
**Alert name**: `NotificationQueueDepthHigh`, `NotificationDLQNonZero`  
**Severity**: Warning at DLQ > 100 messages; Critical at DLQ > 1,000 messages  
**Owner**: SRE Notification Team  
**Last validated**: Q1 2026

---

## What This Alert Means

**Queue backup**: Messages are accumulating in a primary queue faster than consumers can process them. If unchecked, the queue will grow until either consumers catch up, the broker runs out of memory, or messages expire and hit the DLQ.

**DLQ (Dead Letter Queue) alert**: Messages have failed processing and moved to the DLQ. A DLQ with any messages is a signal that needs investigation — these are messages that customers did not receive. Even a DLQ of 1 is worth a look; a DLQ of 1,000 is an incident.

**Analogy**: Think of RabbitMQ queues like baggage claim belts at an airport. The DLQ is the "unclaimed baggage" room. A few bags there is normal; a full room means the belt broke or no one showed up to collect. The bags do not disappear — they accumulate and eventually overflow.

---

## Queue Topology Reference

| Queue name | Priority | TTL | DLQ target | Normal depth |
|---|---|---|---|---|
| sms.high | High | 300s | sms.high.dlq | < 500 |
| sms.standard | Standard | 3600s | sms.standard.dlq | < 5,000 |
| push.high | High | 300s | push.high.dlq | < 1,000 |
| push.standard | Standard | 3600s | push.standard.dlq | < 10,000 |
| email.bulk | Bulk | 86400s | email.bulk.dlq | < 50,000 |

**Normal DLQ depth**: 0–10 messages (occasional transient consumer failures are expected and retry handles them).  
**Escalation threshold**: Any DLQ > 100 messages; any DLQ growing at > 50 messages/minute.

---

## Before You Start

**Check**: Is this a traffic spike or a consumer failure?

```bash
# Open Grafana Panel 4 (Consumer Throughput vs. Queue Depth)
# If consume rate is rising WITH queue depth → traffic spike, not a failure
# If consume rate is flat or dropping while queue depth rises → consumer problem
```

**Check**: Is there a scheduled campaign blast running?
- Check Slack **#marketing-campaigns** for any active mass-send campaigns.
- If a campaign blast is running, queue backup is expected — monitor that depth stays within bounds and consumers catch up within 15 minutes.

---

## Step 1: Identify Which Queue Is Affected

```bash
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqctl list_queues \
  name messages message_bytes consumers \
  --vhost notification \
  --formatter pretty_table
```

**EXPECTED_OUTPUT** (healthy example — DLQs at 0):
```
name                    messages   message_bytes   consumers
sms.high                143        28600           5
sms.high.dlq            0          0               1
sms.standard            2847       569400          5
sms.standard.dlq        0          0               1
push.high               891        178200          8
push.high.dlq           0          0               1
push.standard           12456      2491200         8
push.standard.dlq       0          0               1
email.bulk              45000      9000000         3
email.bulk.dlq          0          0               1
```

**Red flags**:
- Any DLQ with `messages > 100`
- Any primary queue with `consumers = 0` (no consumers attached)
- Any queue with `message_bytes` approaching 512MB (broker memory pressure)

---

## Step 2: Check Consumer Health

If a DLQ is growing, the corresponding consumer is likely failing.

```bash
# Identify which consumer handles which queue
# Convention: sms.high → sms-consumer pods; push.high → push-consumer pods

kubectl get pods -n notification -l app=sms-consumer -o wide
kubectl get pods -n notification -l app=push-consumer -o wide
kubectl get pods -n notification -l app=email-consumer -o wide
```

**EXPECTED_OUTPUT** (healthy):
```
NAME                              READY   STATUS    RESTARTS   AGE   NODE
sms-consumer-7d8f9b4c6-2xkpq     1/1     Running   0          2d    ip-10-0-1-45
sms-consumer-7d8f9b4c6-8mnrt     1/1     Running   0          2d    ip-10-0-1-46
```

**If a pod shows CrashLoopBackOff**:
```bash
# Get the reason for the crash
kubectl describe pod -n notification <pod-name>
kubectl logs -n notification <pod-name> --previous --tail=200
```

**Common crash causes**:

| Log pattern | Cause | Fix |
|---|---|---|
| `Cassandra NoHostAvailableException` | Cassandra node(s) down | Escalate to DBA on-call; scale down to remaining nodes |
| `AMQP connection closed` | RabbitMQ connection reset | Pod will auto-reconnect; if repeating every 30s, check RabbitMQ node health |
| `java.lang.OutOfMemoryError` | JVM heap exhausted | Increase pod memory limit in Helm values; force restart now |
| `Redis READONLY` | Redis failover in progress | Wait 60s for replica promotion; if stuck, restart the consumer pods |
| `Failed to decode message` | Bad message format in queue | Poison message — see Step 5 |

---

## Step 3: Scale Consumers (Traffic Spike Path)

If consumer pods are healthy but cannot keep up with volume (traffic spike or campaign blast):

```bash
# Check current HPA status
kubectl get hpa -n notification

# EXPECTED_OUTPUT:
# NAME                    REFERENCE                        TARGETS         MINPODS   MAXPODS   REPLICAS
# push-consumer-hpa       Deployment/push-consumer         72%/70% CPU     4         16        8

# If HPA is at max replicas and queue is still growing, manually check HPA constraints
kubectl describe hpa push-consumer -n notification
```

If HPA is maxed out (REPLICAS = MAXPODS):
```bash
# Temporarily increase the max replicas — requires SRE Manager approval if > 2x normal
kubectl patch hpa push-consumer -n notification \
  --type=merge \
  -p '{"spec":{"maxReplicas":24}}'

# Document this change in Slack #notification-incidents — revert after the spike
```

**Important**: RabbitMQ prefetch count must be reviewed if scaling beyond 2x normal. Prefetch count of 10 × 16 pods = 160 in-flight messages. At 24 pods, you have 240 in-flight. Verify the broker can sustain this:

```bash
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqctl list_channels \
  name prefetch_count messages_unacknowledged \
  --vhost notification \
  --formatter pretty_table
```

---

## Step 4: Inspect and Replay DLQ Messages

**Do not delete DLQ messages.** Every DLQ message is a notification a customer did not receive. Understand why before deciding what to do.

```bash
# Check how many messages are in the DLQ
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqctl list_queues \
  name messages \
  --vhost notification | grep dlq
```

**Inspect a sample of DLQ messages** (non-destructive peek):
```bash
# Peek at the first 5 messages in the sms.high.dlq without removing them
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqadmin \
  get queue=sms.high.dlq \
  count=5 \
  ackmode=peek_message \
  vhost=notification
```

**EXPECTED_OUTPUT** (example):
```json
{"routing_key": "sms.high", "payload": "{\"messageId\":\"msg-abc123\",\"recipient\":\"+1555XXXXXXX\",\"text\":\"Your verification code is 847291\",\"priority\":\"high\"}", "headers": {"x-death": [{"count": 3, "reason": "rejected", "queue": "sms.high", "time": "2026-01-15T14:23:07Z"}]}}
```

**The `x-death` header tells you why the message died**:
- `reason: expired` → Message exceeded TTL; the consumer was too slow or down when it arrived.
- `reason: rejected` → Consumer explicitly rejected the message (bad format or unrecoverable processing error).
- `reason: maxlen` → Queue hit its max length policy; broker discarded oldest messages.

**If messages are valid but the consumer was temporarily down (reason: rejected, count 1–3)**:
These are safe to replay. The consumer is healthy now and will process them.

```bash
# Move DLQ messages back to the primary queue for retry
# NOTE: This uses the shovel plugin. Verify shovel is enabled:
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmq-plugins list | grep shovel

# One-time replay: move all DLQ messages to sms.high for retry
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqadmin \
  publish \
  exchange=amq.default \
  routing_key=sms.high \
  vhost=notification \
  -- < /dev/null   # Placeholder: in practice, use the shovel or a replay script

# Preferred method: use the DLQ replay script (avoids manual shovel config)
# Script location: s3://notification-ops-scripts/dlq-replay.sh
aws s3 cp s3://notification-ops-scripts/dlq-replay.sh /tmp/dlq-replay.sh
chmod +x /tmp/dlq-replay.sh
/tmp/dlq-replay.sh --queue sms.high.dlq --target sms.high --vhost notification --count 500
```

**EXPECTED_OUTPUT**:
```
Replaying 500 messages from sms.high.dlq to sms.high
Progress: 500/500
Replay complete. sms.high.dlq depth: 0
```

**Monitor after replay**: Watch Panel 4 to confirm consume rate absorbs the replayed messages. If consumer failures spike after replay, there are poison messages in the DLQ — see Step 5.

---

## Step 5: Handling Poison Messages

A poison message is one that always causes the consumer to fail, regardless of how many times it is retried. Common causes: malformed payload, schema version mismatch, or a recipient ID that no longer exists.

**Identify poison messages** (they will have a high `x-death count`):
```bash
# Inspect DLQ for messages with death count > 3 (these are likely poison)
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqadmin \
  get queue=sms.high.dlq \
  count=50 \
  ackmode=peek_message \
  vhost=notification | python3 -c "
import sys, json
for line in sys.stdin:
    try:
        msg = json.loads(line)
        death_count = msg.get('headers', {}).get('x-death', [{}])[0].get('count', 0)
        if death_count > 3:
            print(f'Poison message (death count {death_count}): {msg[\"routing_key\"]} / {msg[\"payload\"][:100]}')
    except:
        pass
"
```

**Disposition of poison messages**:
1. Archive to S3 (for audit — never delete without archiving):
   ```bash
   # The DLQ archive Lambda runs every 5 minutes and archives DLQ messages to S3.
   # Verify archive is current before any manual deletion.
   aws s3 ls s3://notification-dlq-archive/$(date +%Y/%m/%d)/ --region us-east-1
   ```
2. Open an engineering ticket for the malformed message format — this is a producer bug.
3. After archive confirmation, purge the poison message:
   ```bash
   # Purge only after confirming archive. This is irreversible for the queue.
   # Prefer targeted removal using the management API over bulk purge.
   kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqadmin \
     delete queue name=sms.high.dlq vhost=notification
   # WARNING: This deletes ALL messages in the DLQ. Only do this after full S3 archive.
   ```

---

## Step 6: RabbitMQ Broker Health Check

If the queue backup is widespread (multiple queues affected simultaneously), the broker itself may be under pressure.

```bash
# Check broker memory and disk alarms
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmqctl status | grep -A5 alarms

# Check per-node memory usage
kubectl exec -n rabbitmq rabbitmq-0 -- rabbitmq-diagnostics memory_breakdown
```

**Memory alarm**: RabbitMQ will stop accepting publishes when memory exceeds the `vm_memory_high_watermark` (default: 40% of system RAM). If this alarm fires, all producers are blocked — immediate escalation to infrastructure team.

**Disk alarm**: RabbitMQ will stop accepting publishes when free disk drops below 50MB (default). Check EBS volume utilization for the RabbitMQ nodes.

```bash
kubectl exec -n rabbitmq rabbitmq-0 -- df -h /var/lib/rabbitmq
```

---

## Resolution Criteria

The alert is resolved when:
- All DLQs are at 0 (or below 10 for standard queues)
- Primary queue depths are within normal thresholds (see topology table above)
- Consumer throughput is at or above baseline (Panel 4 showing normal msg/s)
- No pod restarts in the last 15 minutes

---

## Post-Incident Requirements

- Any DLQ event that affected > 1,000 messages: open a PIR ticket.
- Any DLQ event involving fraud alerts, 2FA codes, or network outage notifications: immediate Engineering Manager notification regardless of message count.
- DLQ replay events must be documented in the incident Slack thread with: message count replayed, time of replay, confirmation of archive.
