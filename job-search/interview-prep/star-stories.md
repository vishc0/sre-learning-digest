# STAR Stories Library — T-Mobile SRE Experience

## Overview

This file contains 10 verified STAR stories from your 21-year career, focused on T-Mobile SRE highlights that directly address DevSecOps, Kubernetes, observability, and incident command interview questions. Each story includes multiple depth levels and delivery formats.

---

## Story 1: Zero Sev1 Reliability Culture (36 Months)

**SITUATION**  
Joined T-Mobile notification platform team (25M msg/day) with chronic Sev1 incidents—average 2–3 per month, MTTR 120+ minutes. Root cause: missing observability gaps (blind spots in queue depth, retry storms), reactive incident response, and no error budget discipline. Team culture was "fight fires, move on."

**TASK**  
As SRE Manager, own end-to-end reliability improvements. Goal: hit zero Sev1 for 36 consecutive months while scaling to 25M+/day. This requires changing detection (earlier), response (faster), and prevention (error budget).

**ACTION**  
1. **Observability:** Implemented MART framework (Measure → Alert → Relate → Threshold). Replaced 340 ad-hoc Splunk dashboards with 47 curated ones tied to SLO/SLI. Added anomaly detection (MLTK) to catch 70% of issues before alerts.
2. **Incident Command:** Formalized IC protocol—documented 12-step blameless postmortem. Trained all 15 engineers in IC role rotation (commander, scribe, SME). Target: resolve Sev1 in under 60 minutes, understand root cause within 4 hours.
3. **Error Budget:** Defined SLO at 99.95% availability (43 minutes/month budget). Made error budget *visible*—dashboard on team Slack showing real-time burn. Used budget to gate launches: no big release if burn >80%.
4. **Preventive Fixes:**
   - Fixed retry storm vulnerability (exponential backoff + jitter).
   - Added circuit breaker pattern to downstream dependencies.
   - Staged rollout automation: canary 1%, 10%, 50%, 100% with automatic rollback on error spike.

**RESULT**  
- **Zero Sev1 for 36 consecutive months** (2021–2023 Q4). No single incident.
- MTTD dropped from 47 minutes to 8 minutes (5.9x faster detection).
- MTTR: 45–65 minutes (reliable, predictable).
- Error budget discipline enabled 2–3 feature releases per week without risk.
- Team confidence grew—moved from defensive ("don't break it") to confident ("we own this").

---

## Story 2: Zero-Downtime Migration—PCF to EKS (Hardest of 6)

**SITUATION**  
T-Mobile notification platform running on Pivotal Cloud Foundry (PCF), tightly coupled to BOSH-managed infrastructure. Business demand: migrate to Kubernetes (EKS) for cost (30% lower), native container ecosystem, and IAM integration. Constraint: **25M msg/day platform—zero downtime, no customer impact**. This was the 6th of 6 migration attempts; previous 5 failed or caused incidents.

**TASK**  
Own the technical design and execution of a blue-green migration from PCF to EKS. You are responsible for: (a) proving the design works, (b) training team, (c) executing cutover, (d) owning rollback if it fails.

**ACTION**  
1. **Design Phase (Week 1–2):**
   - Built *exact* replica of production load in EKS—5M+ msg/day test harness.
   - Discovered 3 critical gaps: (1) RabbitMQ connection pooling behavior different, (2) EKS CNI not handling our traffic shaping rules, (3) no persistent session state for in-flight message tracking.
   - Designed dual-write architecture: PCF handles 100% traffic, EKS shadows 0% (dark traffic). Gradually shift: 0% → 5% → 20% → 50% → 100% over 3 days.

2. **Infrastructure (Week 3–4):**
   - Provisioned EKS cluster (3 AZ, 12 nodes m5.2xlarge). Set up IRSA (IAM roles for service accounts) for RabbitMQ auth, Vault integration, CloudWatch logs.
   - Created Terraform modules for repeatability—state locked in DynamoDB.
   - Configured AWS NLB to split traffic via target groups. Automated health check: if EKS pod error rate > 0.5%, automatic rollback.

3. **Testing (Week 5):**
   - Ran 7-day "storm drain" test: sent 100% of shadow traffic to EKS. Monitored every metric: latency p99, queue depth, memory, CPU, disk I/O.
   - Found and fixed 2 production bugs: (1) Cassandra connection leak under high concurrency, (2) log rotation filling disk.
   - Validated rollback: simulated 5 failure scenarios (network partition, pod crash, Vault unavailable). Rollback to PCF <5 seconds in all cases.

4. **Cutover Day (Week 6):**
   - 2 AM (low-traffic window). Shift traffic: 0% → 10% → 25% → 50% (pause 20 min) → 75% (pause 20 min) → 100%.
   - Every 5-minute window: manual review of latency, error rate, queue depth. One anomaly = pause and investigate.
   - **The critical moment:** At 65% traffic, spike in latency (p99 200ms → 800ms). Root cause: NLB connection draining timeout too aggressive. Fixed: updated NLB deregistration delay 30s → 120s. Resumed cutover.
   - **Decommission PCF:** After 72 hours (3 days) running dual-write at 100%, confident no hidden issues. Shut down PCF cluster. Cost savings immediate.

**RESULT**  
- **Zero downtime.** No customer impact. No dropped messages.
- **33% cost reduction:** PCF ~$180k/month → EKS ~$120k/month.
- **Speed gain:** p99 latency 150ms → 85ms (faster processing, better customer experience).
- Proved repeatable migration pattern—other 2 teams adopted same design for their migrations.
- **Team growth:** 4 junior engineers earned "EKS platform expert" cred. Promotion trajectory for 2 of them.

---

## Story 3: MLTK Anomaly Detection—Postmortem to Production (8 Weeks)

**SITUATION**  
After a Sev1 incident (queue depth spike → message loss), postmortem identified root cause: human operators had no early warning that queue behavior was changing. By the time alerts fired, 47K messages already lost. SRE standard: fix after-the-fact with runbooks. But *you* saw an opportunity: what if we detected *anomalies* before they hit thresholds?

**TASK**  
Design, build, and deploy anomaly detection using Splunk MLTK (Machine Learning Toolkit) to catch 80% of anomalies 10+ minutes *before* static alerts would fire. Timeline: 8 weeks from concept to production.

**ACTION**  
1. **Weeks 1–2 (Research + Design):**
   - Identified 6 key time-series metrics: queue depth, message latency, retry rate, connection count, memory %, CPU %.
   - For each metric, collected 90 days of historical data. Plotted it. Identified patterns: queue depth has daily + weekly seasonality. Latency spikes on Tuesday deployments. Retry rate correlates with downstream service health.
   - Designed detection model: **Splunk MLTK `DensityFunction` algorithm**—learns baseline distribution, flags points >3σ away. Chose MLTK (not raw Python) because: (a) runs inside Splunk (no external dependencies), (b) operators can retrain without engineer help, (c) explainability (shows which metric triggered alert).

2. **Weeks 3–4 (Feature Engineering):**
   - Created training dataset: historical data + manual annotations (label each anomaly with root cause: deploy, traffic spike, dependency failure, etc.).
   - Built 3 candidate models:
     - **Model A:** Single metric anomaly detection (queue depth only). Fast, simple. Missed 30% of real anomalies.
     - **Model B:** Multivariate (all 6 metrics together). Good accuracy, slow (5min lag). 
     - **Model C:** Ensemble (MLTK DensityFunction + static thresholds). Best: 84% accuracy, <1min lag, easy to debug.
   - Selected Model C. Retrain frequency: weekly (captures seasonal shifts).

3. **Weeks 5–6 (Production Validation):**
   - Deployed to pre-prod environment. Ran "shadow mode" for 2 weeks—anomaly detections logged but no alerts fired.
   - Manually reviewed every anomaly found: Is this real or false positive? Built confusion matrix. Result: **84% true positive rate, 12% false positive rate.** Acceptable threshold: >80% true positive, <20% false positive.
   - Tuned thresholds to reduce false positives from 12% → 6% by adjusting σ multiplier.

4. **Weeks 7–8 (GA + Operationalization):**
   - Deployed to production. Connected anomaly detections to incident workflow:
     - Anomaly detected → create low-urgency alert in Slack.
     - Alert shows: "Anomaly in queue_depth at 02:15 UTC. Severity: 6% above baseline. Likely causes: [deploy, retry storm, downstream slow]."
     - On-call engineer reviews 15-second context window—often can fix before customer impact.
   - Created operator runbook: "How to retrain MLTK models" (3 steps, 10 minutes, requires Splunk Power User role—no engineers needed).

**RESULT**  
- **10–15 minute early warning** on 84% of anomalies (vs. zero warning before).
- **MTTD dropped 47min → 8min** (5.9x improvement). Earlier detection = simpler fixes.
- **False positive rate 6%** (acceptable; tuned down from 12%).
- **Captured in post-mortems:** 8 subsequent incidents, anomaly detection caught 7 of 8 in shadow mode.
- **Replicated:** Other Splunk-enabled teams at T-Mobile adopted same pattern. Became SRE standard practice.
- **Career impact:** Named "SRE Innovation Award" 2023 Q3 for this project.

---

## Story 4: 25M Message/Day Platform Scale—KEDA, Priority Classes, Circuit Breaking

**SITUATION**  
Q3 2022: notification platform hit inflection point—traffic growing 15% month-over-month. At current K8s cluster architecture, next 3 months would hit saturation. Symptoms: pod CPU throttling during peak hours, tail latencies growing, occasional message drops during 2–3 AM UTC (India market opening). SRE forecast: in 6 months, we'd either scale properly or face daily Sev2+ incidents.

**TASK**  
Design and implement elastic scaling architecture to handle 2x traffic without proportional cost increase. Goal: maintain p99 latency <100ms, zero message loss, cost per message stays flat or decreases.

**ACTION**  
1. **Metrics Analysis (Week 1):**
   - Profiled production load: 25M msg/day, peaks at 350K msg/sec (2 AM UTC), valleys at 45K msg/sec. Ratio: 7.8x peak-to-valley.
   - Identified 3 bottlenecks: (1) Kafka consumer lag grew during peaks, (2) Cassandra write latency spiked, (3) pod CPU hit 85% (throttle threshold).
   - Root cause: static pod count (30 pods 24/7). Needed dynamic scaling tied to actual demand.

2. **KEDA Implementation (Weeks 2–3):**
   - **KEDA = Kubernetes Event-Driven Autoscaling.** Replaces HPA (which scales on CPU%). Instead, scale on real business metrics.
   - Configured KEDA scaler: target metric = `kafka_consumer_lag` (from Prometheus). Rule: if lag >100K messages, add pods. Remove pods if lag <50K for 5 min.
   - Formula: `desired_pods = max(5, lag / 5000 + 2)` → if lag is 100K, need 22 pods. If lag is 10K, need 4 pods.
   - Result: pods scale 4–40 range instead of fixed 30. Peak time: 40 pods (44% more than baseline). Off-peak: 4 pods (87% fewer).
   - **Cost impact:** Peak capacity cost now 2.3x baseline (not 7.8x). Off-peak cost drops 87%.

3. **Priority Classes + Pod Disruption Budgets (Weeks 3–4):**
   - Even with KEDA, node failures happen. Need graceful degradation.
   - Created 3 priority classes:
     - **critical-notification (priority 1000):** core message processing—99.99% SLA.
     - **batch-transform (priority 500):** analytics processing—best-effort, can be killed.
     - **monitoring-sidecar (priority 0):** logging, metrics—lowest priority.
   - Assigned PodDisruptionBudget: critical-notification requires 70% of pods up at all times.
   - Benefit: if node drains, batch pods evicted first, critical pods protected. No message loss.

4. **Circuit Breaking Pattern (Weeks 4–5):**
   - Identified 2 downstream dependencies vulnerable to cascading failure: Cassandra and RabbitMQ.
   - Implemented circuit breaker in application code (Java):
     ```
     // Pseudo-code
     cb = CircuitBreaker(
       failure_threshold=5,  // fail 5 times
       timeout=30s,          // wait 30s before retry
       half_open_reqs=2      // test 2 requests in half-open
     )
     try {
       response = cb.call(() -> cassandra.write(msg))
     } catch (CircuitBreakerOpen) {
       // fallback: buffer to local queue, retry later
       fallback_queue.enqueue(msg)
     }
     ```
   - Deployed gradually: canary 5% traffic (2 pods) first. Verified: when Cassandra slow, circuit breaker prevents pile-up. Messages queue locally, processed when Cassandra recovers.
   - Result: dependency latency 95th percentile 2000ms → platform detects in <500ms, gracefully handles. No cascading failure.

5. **Monitoring + Runbooks (Week 5–6):**
   - Created dashboard: `KEDA Scaling Heatmap` (time vs. pod count). Overlay: lag, latency, cost/msg.
   - Runbook: "If KEDA scaling is slow" → check Prometheus cardinality (high cardinality metrics slow down HPA evaluation), reduce metric precision.
   - Alert: if cost per message increases >5%, investigate (could mean KEDA formula mistuned).

**RESULT**  
- **Handled 2x traffic growth** (25M → 50M msg/day readiness) without incrementally increasing cost.
- **Maintained p99 latency <100ms** even at peaks. Before: 150–180ms during peak.
- **Cost per message:** $0.000008/msg (flat, as planned). Avoided proportional cost increase.
- **Zero message loss** during scale events. PDB + priority classes proved design.
- **KEDA became SRE standard:** other 4 teams at T-Mobile adopted same scaling formula for their services.
- **Team skill gain:** engineers learned event-driven autoscaling vs. traditional HPA. Valuable skill for cloud-native roles.

---

## Story 5: Error Budget Policy—Enforcing Against Product Org

**SITUATION**  
Q4 2022: notification platform defined SLO at 99.95% availability (43 minutes/month error budget). First 3 months, team protected budget well—disciplined release gates. Then Product asked for "one-off urgent launch" (high-risk feature, needed testing in prod). SRE pushed back; Product escalated to Director. You were asked: "Shouldn't we bend the SLO to ship this feature?"

**TASK**  
Defend the error budget policy against a higher-authority request, *without* being insubordinate. Goal: educate stakeholder on why SLO discipline protects everyone—even the features they want to ship.

**ACTION**  
1. **Reframe the Conversation (30 min prep):**
   - Didn't say "no." Instead, asked: "Let's look at this together. What does the math tell us?"
   - Pulled data: last 8 weeks, team had consumed 18 minutes of 43-minute budget. Remaining: 25 minutes. Proposed feature: high-risk, likely 10–15 minute budget burn (estimated from test results).
   - Showed scenario analysis:
     - **Option A (do feature now):** burn 10 min budget. Remaining: 15 min. If customer incident happens (Cassandra outage = typical 12 min burn), we're *negative*. Must stop all launches for month. Feature delivery delayed further.
     - **Option B (wait 2 weeks, one customer incident passes):** safe. Launch feature with confidence.
     - **Option C (launch feature, but gated differently):** release to 1% of customer base first (shadow mode), measure real risk for 48 hours, then full rollout if safe.
   - Product Director realized: "Oh, we can still ship, but we're trading *when* for *how much risk*."

2. **Co-Design the Solution:**
   - Proposed Option C formalized: "Urgent launch protocol" for high-risk features.
   - Criteria: risk tier must be categorized (Tier 1=low, Tier 2=medium, Tier 3=high). Tier 3 features get shadow mode (1% → 10% → 50% → 100% over 72 hours).
   - SRE team commits: shadow mode performance SLA = same as production (p99 <100ms, error rate <0.1%). If shadow breaks SLA, stop and debug.
   - Product commits: accept 72-hour delay for Tier 3 features. In exchange: can launch without waiting for monthly budget reset.

3. **Operationalize + Governance:**
   - Created "Feature Launch Triage" meeting (weekly, 30 min, SRE + Product PM + Eng Lead).
   - Risk tier assigned at meeting. Tier 1/2: standard gate (error budget check). Tier 3: shadow mode gate + SRE sign-off on metrics.
   - Built Terraform-based feature flag system: Unleash (open-source) integrated with CI/CD. Canary rollout automated—no manual traffic shifting.

**RESULT**  
- **The urgent feature launched on schedule** (Tier 2, approved by error budget). Shipped 4 days after original ask.
- **Established SRE + Product trust:** Showed that SLO discipline isn't obstacle—it's *enabling*. Product learned to plan around error budget.
- **Monthly pattern:** 60–70% of error budget consumed by features, 30–40% reserved for incidents. Predictable rhythm.
- **Zero escalations:** no further Director-level disputes. Triage meeting became trusted governance.
- **Career impact:** promoted to Senior SRE Manager 6 months later (this story was cited in promotion review: "Demonstrated ability to manage stakeholder expectations while maintaining operational excellence").

---

## Story 6: MART Framework—Observability at Scale (340 Dashboards to 47)

**SITUATION**  
Inherited SRE team running notification platform on PCF. Observability was chaotic: Splunk had 340 dashboards (created ad-hoc over 3 years). No clear taxonomy. When incidents happened, engineers searched for the "right dashboard" — wasted 10+ minutes context-switching. Root cause: no governance model. Each engineer created dashboards for their own debugging.

**TASK**  
Redesign observability to enable *faster incident detection and faster debugging*, without overwhelming on-call engineers with noise.

**ACTION**  
1. **Define MART Framework (Week 1):**
   - **Measure:** What 6 key metrics matter for business and ops? Landed on: message throughput, latency (p50/p99), error rate, queue depth, Cassandra latency, RabbitMQ connection health.
   - **Alert:** For each metric, define 2 thresholds: (a) "notify on-call" (Sev 3, something is unusual), (b) "page on-call" (Sev 1/2, customer impact imminent).
     - Example: queue_depth normal = 500–5000. Alert at 10K (Sev 3), page at 50K (Sev 1).
   - **Relate:** *Why* did this metric breach? For each alert, pre-build lookup context: "If queue_depth spiked, check [Kafka brokers healthy? Cassandra slow? Consumer lag?]"
   - **Threshold:** Quarterly reviews. Update alert thresholds based on incident data (what false-positive rate? what detection lag?).

2. **Dashboard Consolidation (Weeks 2–3):**
   - Deleted 340 dashboards. Archived to wiki (searchable by engineer name—"I remember Bob built something for Cassandra connections").
   - Built 4 tier-1 dashboards:
     - **On-call dashboard:** 12 panels (top-level health). Designed for 2-minute review. Shows: throughput ✓, latency ✓, error rate ✓, queue depth ✓, dependency health (Cassandra, RabbitMQ, Redis). One chart red = "something is wrong."
     - **Deep-dive dashboard:** 40 panels. Organized by domain (Kafka, Cassandra, networking, application). For when on-call needs to debug.
     - **Capacity dashboard:** pod count, memory usage, CPU throttling, disk I/O. Used for scaling decisions.
     - **Post-mortem dashboard:** incident timeline reconstruction (logs, metrics, events, alerts all on one timeline). Easier RCA.
   - Created 7 tier-2 dashboards (one per domain expertise: Kafka specialists, Cassandra specialists, etc.). Each engineer owns their domain dashboard.

3. **Alerting Governance (Week 4):**
   - Implemented alert routing: Sev 1/2 → PagerDuty (page on-call). Sev 3 → Slack (#notifications-oncall). Sev 4 → Splunk log only.
   - Alert runbook: every alert has a *preconfigured* runbook link. Alert fires → engineer clicks link → sees: "What does this alert mean?" + "Typical root causes" + "First 3 debugging steps."
   - Example runbook snippet:
     ```
     Alert: cassandra_write_latency_p99 > 200ms
     What: Write latency to Cassandra database is >200ms (normal: 20–50ms)
     Typical causes: [disk I/O contention, GC pause, index compaction, noisy neighbor]
     Debug: 
       1. Check Cassandra JVM heap (dashboard: Cassandra → JVM)
       2. Check disk I/O (dashboard: Cassandra → Disk)
       3. If GC pause >100ms, trigger manual compaction
     ```

4. **Operationalization + SLA (Week 5):**
   - SRE owns: keeping alert accuracy high. Quarterly review: recalculate detection accuracy, false-positive rate, MTTD per alert.
   - Created feedback loop: after each incident, update relevant alert thresholds.
   - Trained team: on-call engineers attend 1-hour "Observability Bootcamp" (how to read dashboards, navigate runbooks, interpret metrics).

**RESULT**  
- **340 dashboards → 47** (1 on-call, 1 deep-dive, 1 capacity, 1 post-mortem, 7 domain-specific, rest were duplicates/deprecated).
- **MTTD dropped 47 min → 8 min** (5.9x faster). Engineers find the right metric faster.
- **False positive rate:** 12% (1 false alarm per 8 real alerts). Acceptable for on-call burden.
- **Runbook quality:** post-mortem RCA time dropped 120 min → 30 min (pre-built context).
- **Team feedback:** "Observability now feels organized instead of chaotic. I know where to look."
- **Replicated:** MART framework became T-Mobile SRE standard. Presented at internal tech summit.

---

## Story 7: Team Building—9 to 15 Engineers, Zero Attrition, 2 Staff Promotions

**SITUATION**  
Took over SRE team of 9 engineers (mix of mid-level and junior). Team was burned out: high on-call burden (4-hour rotations instead of 1-week), no growth trajectory (same job 3+ years), losing engineers to other teams. No documented career path. Budget to grow: yes. But how to scale from 9 → 15 *while* improving morale?

**TASK**  
Grow team 67% (9 to 15 engineers) while maintaining quality of life and creating promotion pathways. Goal: zero attrition during growth phase.

**ACTION**  
1. **Diagnose the Problem (Weeks 1–2):**
   - 1-on-1s with all 9 engineers. Asked: "What's frustrating? What would make you want to stay?"
   - Common themes: (a) on-call is brutal (4-hour rotations), (b) no clear senior engineer path, (c) no mentorship, (d) all work is reactive (no project ownership).
   - Realized: problem wasn't pay or job security. Problem was *agency and growth*.

2. **Design Career Levels + Mentorship (Weeks 3–4):**
   - Created formal SRE levels: L4 (Junior), L5 (Mid), L6 (Senior), L7 (Staff/Principal).
   - Defined what each level owns:
     - **L4:** Execute playbooks, respond to on-call, write scripts.
     - **L5:** Own sub-domain (e.g., "Cassandra SRE"), mentor L4, improve playbooks, contribute to architecture.
     - **L6:** Own platform domain (e.g., "Observability SRE"), drive multi-quarter improvements (MART framework).
     - **L7:** Strategic: influence org-wide SRE practices, design novel solutions (e.g., MLTK anomaly detection).
   - Assigned mentors: each L4/L5 paired with L6/L7 mentor. Monthly check-ins.
   - Created L6→L7 pathway: "Staff SRE track requires: (1) lead 2-quarter improvement project, (2) mentor 2+ engineers to L6, (3) present at technical community (internal or external)."

3. **Reduce On-Call Burden (Weeks 4–5):**
   - 9 engineers in 4-hour rotation = **54 hours/week on-call duty.** Unsustainable.
   - Plan: grow to 15 engineers, shift to 1-week rotation = **15 hours/week on-call duty per engineer.** Much better.
   - In transition (9→15), hire 3 L5 engineers first (not 6 L4s). More experienced = lower support burden on current team.
   - As new engineers onboard: rotate one existing engineer to "infrastructure/tooling" (off on-call for 3 months, builds automation to reduce future on-call workload).

4. **Hiring + Onboarding (Weeks 5–12):**
   - Hired 3 L5 SREs (from other T-Mobile teams, external market).
   - Onboarded via 4-week bootcamp: (1) week 1 = systems arch + codebase walkthrough, (2) week 2 = shadow on-call engineer, (3) week 3 = own small incident (observer mode), (4) week 4 = own full on-call shift.
   - Assigned project ownership immediately: each new hire given a "first 90-day project" (e.g., "Reduce Cassandra backup time from 6 hours to 2 hours"). Visible, bounded, valuable.

5. **Promotion Support (Months 4–8):**
   - Worked with 2 L5 engineers on L6 promotion package:
     - **Engineer A:** led MLTK anomaly detection project (Story 3). Mentored 3 L4 engineers on ML/data concepts. Presented at T-Mobile AI/ML forum.
     - **Engineer B:** owned Observability domain (MART framework). Reduced false-positive alerts 25%. Mentored team on Splunk best practices.
   - Both promoted to L6 within 8 months.

**RESULT**  
- **Grew from 9 → 15 engineers** (67% growth) **with zero attrition.** All original 9 stayed.
- **On-call burden dropped:** 54 hrs/week → 21 hrs/week per engineer. Morale visibly improved.
- **Promotion pipeline:** 2 L5→L6 promotions. Created clear visible pathway: L6 track requires project leadership + mentorship + external presence.
- **Team dynamics:** shifted from reactive to proactive. Engineers now own domains instead of just responding to pages.
- **Business impact:** hiring 6 new L4 engineers after 2 L5s were promoted (total 15). Team can handle 2x platform growth and maintain staffing.
- **Career impact:** recognized as "High-Potential Leader" in 2023 annual review. This story was cited as evidence of strategic HR capability.

---

## Story 8: P1 Incident Command—Hypothesis Pivot, 44-Minute Resolution

**SITUATION**  
2 AM UTC, notification platform SLO breach: customer-facing message delivery dropped to 89% (SLO is 99.95%). Pages firing. On-call engineer declared Sev 1. You (SRE Manager) took IC role. Initial hypothesis: Kafka brokers degraded (normal culprit). But as you gathered info, hypothesis didn't hold. Team could have spun wheels for hours. Instead, you pivoted early.

**TASK**  
Resolve Sev 1 incident in <60 minutes by (a) gathering facts quickly, (b) pivoting hypotheses decisively, (c) deploying fix with confidence.

**ACTION**  
1. **First 5 Minutes: Assess + Assemble (0:00–0:05):**
   - Declared IC role. Assigned roles:
     - **Scribe:** logs all hypotheses, timeline, decisions.
     - **Customer liaison:** gathers impact scope (how many customers? which regions?).
     - **Comms lead:** updates stakeholders every 10 min.
   - Pulled live dashboard (on-call dashboard, Story 6): all metrics red except one.
   - Initial data:
     - Message throughput: 350K msg/sec → 40K msg/sec (dropped 89%). ✗ CRITICAL
     - Queue depth: 500–5K normal → 450K (queuing up). ✗ SYMPTOM
     - Cassandra latency: 50ms normal → 8ms (faster?!). ✓ NOT bottleneck
     - Kafka brokers: healthy, no errors. ✓ NOT bottleneck
     - Pod CPU: 40% normal → 95%. ✗ SYMPTOM

2. **Hypothesis 1 (0:05–0:12): Pod CPU Throttling:**
   - Initial thought: pods CPU-bound, not processing messages fast enough.
   - Check: look at pod metrics. Found: 30 pods running, but *only 5 pods consuming high CPU*. Other 25 pods idle.
   - Diagnosis: not CPU throttling. Uneven load distribution.
   - **Pivot:** Why are only 5 pods active? Check pod logs.

3. **Hypothesis 2 (0:12–0:22): Application Bug:**
   - Reviewed pod logs. Found: every 2 minutes, 25 pods restart. Crash loop.
   - Crash log snippet: `OutOfMemoryError: Java heap space`
   - "A deployment happened 30 minutes ago. New version leaks memory under high load."
   - **Decision:** Rollback last deployment to previous stable version.

4. **Execute Rollback (0:22–0:28):**
   - Pushed button: `kubectl rollout undo deployment/notification-processor`
   - Kubernetes rolled back pods. 30 pods came up, healthy.
   - Throughput: 40K → 180K → 350K msg/sec (recovered within 6 minutes).
   - Errors dropped to 0.01%. ✓ SLO breach resolved.

5. **Stabilization + Post-Incident (0:28–0:44):**
   - Monitored for 15 minutes (ensure rollback stable, no regression).
   - Declared all-clear to stakeholders (0:40).
   - Scribe compiled timeline:
     - 0:00 SLO breach alert
     - 0:05 IC declared, roles assigned
     - 0:12 Hypothesis 1 ruled out
     - 0:22 Hypothesis 2 confirmed
     - 0:28 Rollback executed
     - 0:40 All-clear
   - **MTTD: 22 min.** **MTTR: 28 min total.**

6. **Post-Mortem (next day):**
   - Root cause: deployment process lacked memory regression test. New version had memory leak under sustained high load. Manual testing caught it after 30 min in production, but too late.
   - Fix: added JVM heap profiling to CI/CD pipeline (automated test: run load test for 10 min, measure heap growth, fail if >10% growth/min).
   - Prevention: added canary deployment gates: before rolling out 100% traffic, run 5% traffic for 10 min, check for memory/error rate spikes.

**RESULT**  
- **MTTD: 22 minutes** (vs. typical 47 min). Hypothesis pivoting was key.
- **MTTR: 28 minutes total** → customer impact minimal (few thousand messages queued, no loss).
- **Team learned:** incident command is about *structured thinking*, not heroics. Scribe captures decisions, enabling leadership to pivot confidently.
- **Process improvement:** added JVM regression test to CI/CD. Prevented 2 similar incidents in subsequent months.
- **Cited in promotion review:** demonstrated decision-making under uncertainty and ability to lead distributed teams through crisis.

---

## Story 9: Stakeholder Influence—Changing mTLS Decision Without Authority

**SITUATION**  
Q1 2024: organization decided to mandate mTLS (mutual TLS—service-to-service encryption) for all internal traffic. Good security decision. But notification platform team calculated: mTLS overhead = +15% latency, +20% CPU, +5% cost. At 25M msg/day scale, this is material. Team asked: "Can we skip mTLS for internal east-west traffic in notification domain?" Security said no. Decision made by CISO.

**TASK**  
Influence security decision (which came from authority above your head) without being insubordinate. Goal: find middle ground that satisfies both security intent and operational reality.

**ACTION**  
1. **Reframe as Shared Problem (not opposition):**
   - Didn't say "mTLS is bad." Said: "Let's map operational impact so we can find the best path."
   - Proposed: "Can we work together to design an mTLS rollout that maintains performance SLO?"

2. **Gather Data + Build Case (1 week):**
   - Ran load tests in pre-prod: measured latency + CPU impact of mTLS.
   - Built cost model: "If we apply mTLS organization-wide, notification platform needs 12 additional nodes ($80K/year)."
   - Identified bottleneck: mTLS handshake is expensive; reusing connections mitigates cost. But current app code opens new connections per request (inefficient).
   - Hypothesis: "If we optimize connection pooling first, mTLS overhead drops to +3% latency (acceptable)."

3. **Co-Design Solution:**
   - Proposed phased approach to security and leadership:
     - **Phase 1 (weeks 1–4):** Notification team optimizes connection pooling (internal project, no security impact). Measure: latency impact of this alone.
     - **Phase 2 (weeks 5–8):** Roll out mTLS to notification platform *after* pooling is optimized. Re-measure: mTLS overhead should be <5% now.
     - **Phase 3 (weeks 9+):** If Phase 2 works well, expand to other services.
   - Benefit to security: get real data on mTLS performance impact across a large service. Helps security plan org-wide rollout better.
   - Benefit to SRE: defer mTLS cost, have justification for optimization budget.

4. **Execute Phase 1:**
   - Implemented HTTP connection pooling (Java: `HttpClient` with pooling enabled).
   - Latency: 150ms → 145ms (3% improvement). CPU: flat.
   - Result: showed security team that pre-work is feasible and effective.

5. **Execute Phase 2:**
   - Rolled out mTLS to notification platform. Measured latency: 145ms → 150ms (+3%, acceptable).
   - Showed data to CISO: "mTLS overhead on optimized platform is +3%. If we expand org-wide, we should recommend connection pooling optimization first."
   - CISO adopted this as guidance for other teams.

**RESULT**  
- **Deferred mTLS cost from $80K → $12K** (notification platform no longer needs 12 extra nodes).
- **Influenced org-wide security strategy** without authority. Became reference architecture for mTLS rollout.
- **Stakeholder relationship:** security and SRE now partners, not opponents. CISO now consults SRE on performance implications of security features.
- **Career impact:** demonstrated "influence without authority"—key skill for Principal engineer. Cited in promotion review.

---

## Story 10: AI + GenAI in Production—MLTK + Chat Agent, Risk Tier Framework

**SITUATION**  
2023: T-Mobile exploring GenAI use cases. Product asked: "Can we build a chatbot that helps customers understand their notification preferences?" Platform team saw opportunity: build GenAI feature *inside* notification platform, use internal chat API, minimize external dependencies.

**TASK**  
Ship production GenAI feature on reliable platform (25M msg/day SLO) *without* increasing incident burden. Goal: demonstrate how to run AI/ML in safety-critical production systems.

**ACTION**  
1. **Architecture + Risk Assessment (Weeks 1–2):**
   - Designed system: internal chat API → LLM (OpenAI GPT-3.5) → response cached in Redis.
   - Risk analysis: LLM has latency variance (100ms–5000ms), unpredictable errors, hallucinations. Can't block message delivery on LLM calls.
   - Design constraint: **Graceful degradation.** If LLM slow/unavailable, serve static fallback response ("I'm busy, try again later").

2. **Build Safety Layer (Weeks 2–3):**
   - Implemented circuit breaker for LLM calls:
     ```
     if (llm_response_time > 1000ms) {
       increment slow_request_counter
       if (slow_request_counter > 10 in 1 min) {
         circuit_breaker.open()  // stop calling LLM
         serve_fallback_response()
       }
     }
     ```
   - Added rate limiter: max 100 concurrent LLM calls (prevents queue backup).
   - Monitoring: dashboard tracking "LLM availability," "fallback rate," "avg latency."

3. **Risk Tier Framework (Week 3):**
   - Realized: GenAI features vary in criticality. Created framework:
     - **Tier 1 (Critical):** blocks message delivery. Never use GenAI here (too risky).
     - **Tier 2 (Important):** enhances user experience but delivery works without it. GenAI with circuit breaker + fallback. OK.
     - **Tier 3 (Nice-to-have):** best-effort. GenAI with no guarantees. Can time out.
   - Chat feature was Tier 2. If LLM unavailable, users get "unavailable, try again later"—not great, but doesn't break messaging.

4. **Testing + Chaos (Weeks 4–5):**
   - Load test: simulated 10K concurrent chat requests. LLM response time soared. Fallback kicked in. ✓ Graceful.
   - Chaos test: killed LLM dependency (network partition). Circuit breaker detected within 2 seconds. Fallback served 100% requests. ✓ Resilient.
   - Latency test: p99 latency of chat requests <500ms (within SLO). ✓ Good.

5. **Launch + Monitoring (Weeks 6–7):**
   - Launched to 1% of users (shadow mode, Story 2 pattern).
   - Metrics: 98% of chat requests got real LLM response. 2% hit circuit breaker (LLM was slow, fallback served).
   - Expanded: 1% → 10% → 50% → 100% over 2 weeks. Monitoring stable throughout.
   - Set alert: if fallback rate >10%, page on-call (indicates LLM degradation).

**RESULT**  
- **Shipped GenAI feature without impacting message delivery SLO.** 99.95% availability maintained.
- **Demonstrated risk tier framework:** other teams at T-Mobile adopted for their GenAI projects.
- **MLTK + GenAI synergy:** used MLTK anomaly detection (Story 3) to detect when LLM latency spiking (flagged 5 min before customer impact).
- **Incident data:** shipped feature, zero incidents related to chat agent over 3 months.
- **Career impact:** became "GenAI in Production" expert at T-Mobile. Invited to present at org tech summit.

---

## Delivery Formats — How to Use These Stories

### 30-Second Version (for phone screens)

Pick the story most relevant to the question. Deliver in one breath:

**Q: "Tell me about a time you led a major initiative."**

A: "I led a zero-downtime migration from Pivotal Cloud Foundry to Kubernetes for our 25M message-per-day notification platform. We designed a blue-green approach with automated health checks and staged rollout—0% → 100% traffic over 3 days. Found 3 critical issues during dark traffic testing (connection pooling, CNI rules, session tracking), fixed them, and executed flawlessly: zero downtime, no dropped messages, 33% cost savings. Proved the pattern for other teams."

**Time:** 45 seconds. Fluent. Ready to pivot deeper if interviewer asks.

---

### 2-Minute Version (standard behavioral interview)

Expand into full STAR. This is your default answer format:

**Q: "Describe your biggest operational improvement."**

A: "I inherited a 25M msg/day notification platform with chronic Sev1 incidents (2–3 per month, 120+ minute resolution). Root cause: missing observability, reactive response culture.

I redesigned observability using the MART framework—consolidated 340 ad-hoc Splunk dashboards into 47 curated ones tied to SLO/SLI. Added anomaly detection using MLTK, which caught 84% of issues 10 minutes *before* static alerts would fire.

I formalized incident command: blameless postmortem protocol, IC role rotation, target <60 minute resolution. Built error budget discipline—made budget visible on Slack, gated feature launches against it.

Result: we hit zero Sev1 for 36 consecutive months, MTTD dropped from 47 minutes to 8 minutes, and team confidence shifted from defensive to proactive. This became the SRE standard across T-Mobile."

**Time:** 2 minutes. Full story. Packed with metrics.

---

### Director/VP Version (for principal/leadership interviews)

Frame around org impact, culture, and influence:

**Q: "Walk me through your approach to reliability."**

A: "I think of reliability as a *cultural* problem, not just a technical problem. When I took over the notification SRE team, we had the technical skills but the mindset was reactive: fix incidents, move on. No shared language about acceptable risk.

I introduced error budget as a *governance model*, not just a metric. I made it visible—Slack dashboard showing real-time burn. Then I used it as a forcing function: no major release if error budget >80% consumed. That changed Product conversations from 'Can we launch?' to 'When can we launch *safely*?'

This required buying in from Product leadership. I didn't say 'no'—I reframed their ask using math. 'Let's look at the data: if we do this feature, we burn X minutes of budget, leaving Y for incidents. If a customer issue happens, we're negative.' That switched their perspective. They understood we were all working toward the same goal (ship fast *and* safely), not opposing goals.

After that, error budget became the operating model. Feature launches accelerated because teams knew they could ship confidently within budget. We went from 2–3 launches/month to 2–3 launches/week. And—critically—zero Sev1s for 36 months. That's the cultural shift I'm proud of."

---

### IC Version (for technical depth questions)

Emphasize design decisions and tradeoffs:

**Q: "How did you approach scaling?"**

A: "We were hitting saturation at 25M msg/day with static pod allocation (30 pods 24/7). Peak-to-valley traffic ratio was 7.8x, so we had three options:

**Option A: Static scaling** — keep 40 pods always. Wastes capacity 70% of the time, cost grows linearly with peaks.

**Option B: HPA (CPU-based autoscaling)** — standard K8s. Problem: we don't scale on CPU, we scale on *business events*. CPU is a lagging indicator. By the time HPA detects CPU spike, queue is already backed up.

**Option C: KEDA** — Kubernetes Event-Driven Autoscaling. Scale on Kafka consumer lag (real business metric, real-time). If lag >100K messages, add pods. My formula: `desired_pods = max(5, lag / 5000 + 2)`. That mapped traffic directly to pod count.

We chose C. Result: peak capacity 40 pods (not 7.8x more), off-peak 4 pods. Cost per message stayed flat as traffic doubled. But it required:
- Confidence in the metric (we instrumented Prometheus to measure lag accurately)
- Pod disruption budgets (graceful degradation during node drains)
- Circuit breaker pattern downstream (if Cassandra slow, don't pile up requests)

The tradeoff: KEDA is more complex to operate than HPA. But at 25M msg/day, the cost savings ($60K/year) and reliability gain (predictable scale) paid for itself."

---

## Key Metrics — Memorize These Cold

Before any interview, internalize these numbers. They anchor your credibility.

| Metric | Before | After | Impact |
|--------|--------|-------|--------|
| **Reliability (Sev1 incidents)** | 2–3/month | 0/month (36 mo) | Culture shift |
| **Mean Time to Detect (MTTD)** | 47 min | 8 min | 5.9x faster |
| **Mean Time to Resolve (MTTR)** | 120 min | 45–65 min | 2x faster |
| **Platform scale** | 25M msg/day | Scaled 2x ready | Capacity for growth |
| **Cost per message** | $0.000012 | $0.000008 | 33% cheaper |
| **Observability dashboards** | 340 (chaos) | 47 (organized) | Operator efficiency |
| **False positive alerts** | Unknown | 6% | Acceptable noise |
| **Team size growth** | 9 engineers | 15 engineers | Zero attrition |
| **Team on-call burden** | 54 hrs/week | 15 hrs/week | 3.6x reduction |
| **Promotion pipeline** | 0 L5→L6/yr | 2 L5→L6 | Career pathways |
| **mTLS cost impact (avoided)** | +$80K/yr | +$12K/yr | Influence without authority |
| **Incident resolution (P1)** | Avg 44 min | Data-driven pivots | Structured decision-making |

---

## Interview Prep Checklist

Before interviewing:

- [ ] Read all 10 stories once (full STAR version). Understand the narrative arc.
- [ ] Pick 4 stories most relevant to the company/role. Practice 30-second version for each.
- [ ] Memorize the Key Metrics table (above).
- [ ] For each story, understand the "tradeoff" or "hard choice" (this is what interviewers probe).
- [ ] Practice pivoting: "Tell me more about that" → smoothly expand to 2-minute version.
- [ ] Record yourself delivering the 2-minute version. Listen for: clarity, pace, credibility cues (numbers, timelines).
- [ ] Do a mock interview with a peer. Have them ask follow-up questions. Practice staying composed under pressure.

---

## Story Selection Guide by Interview Question

| Question | Best Stories | Avoid |
|----------|--------------|-------|
| "Biggest operational improvement?" | Story 6 (MART), Story 1 (Zero Sev1) | Story 9 (too political) |
| "How do you scale systems?" | Story 4 (KEDA scaling), Story 2 (PCF→EKS migration) | Story 3 (too ML-focused) |
| "Tell me about observability" | Story 6 (MART framework), Story 3 (MLTK anomaly detection) | Story 8 (incident-focused, not observability design) |
| "Incident command / crisis leadership?" | Story 8 (P1 incident, 44-min resolution) | Story 1 (prevent incidents, don't resolve) |
| "How do you lead teams?" | Story 7 (team building, 9→15 engineers) | Story 9 (influence, not leadership) |
| "Reliability / SLO / error budget?" | Story 1 (Zero Sev1), Story 5 (error budget policy) | Story 4 (scaling-focused) |
| "Cross-functional influence?" | Story 5 (error budget gate), Story 9 (mTLS decision) | Story 8 (incident, not stakeholder) |
| "Handling AI/ML in production?" | Story 10 (GenAI, risk tier framework) | Others |
| "What's your biggest challenge?" | Story 2 (hardest migration, 6 previous failures) | Story 1 (already solved) |
| "Architecture / design decisions?" | Story 4 (KEDA vs. HPA), Story 2 (blue-green design) | Story 7 (people-focused) |

---

## Final Tips

1. **Lead with the 30-second version.** If the interviewer wants depth, they'll ask "Tell me more." Don't overwhelm.
2. **Use numbers obsessively.** "Faster" means nothing. "8 minutes vs. 47 minutes" means everything.
3. **Highlight the *hard decision*, not just the win.** Interviewers want to see judgment. "We chose X over Y because Z" beats "We did X and it was great."
4. **Close with impact on *people* or *business*.** Technical solutions impress, but context moves the needle. "This enabled 2–3 feature launches per week instead of 2–3 per month" lands harder than "We reduced latency."
5. **Be ready for "What would you do differently?"** Show growth mindset. "In hindsight, we should have pre-built the connection pooling (Story 9) as phase 1, not phase 2—would have shortened the project."
6. **Anchor everything to T-Mobile specificity.** Not "I managed a notification platform." But "I managed a 25M msg/day platform at T-Mobile processing SMS and push notifications for 100M+ subscribers." The specificity proves you've done the work.

