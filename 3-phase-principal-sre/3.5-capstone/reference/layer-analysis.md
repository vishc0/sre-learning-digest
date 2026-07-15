# Research: Layer-by-Layer Technical Analysis

## The Six Operational Layers of the Shopping Cart System

Every request a customer makes traverses six distinct technology layers. Failures at any layer manifest as customer-facing degradation. SRE ownership and tooling are different at each layer. This analysis maps what each layer contains, what can go wrong, how it is observed, and what the SRE team must own.

---

## Layer 1 — Business and User Experience Layer

**What it is**: The business metrics and user experience signals that measure whether the system is serving its commercial purpose.

**Components**:
- Conversion funnel metrics (browse → add-to-cart → checkout → purchase)
- Revenue per minute (GMV rate)
- Cart abandonment rate
- Session success rate by journey type
- Customer satisfaction signals (CSAT, support ticket volume)

**What goes wrong at this layer**:
- Conversion drop without availability signal (A/B test gone wrong, UX regression, price display bug)
- Revenue anomaly disconnected from technical incident (promotional pricing error, tax calculation bug)
- Funnel drop in a specific user segment (mobile-only users, specific geography, specific browser version)

**SRE ownership**: SRE does not own code at this layer, but SRE owns the metrics and alerts at this layer. A P1 incident declared from Layer 1 signals ("conversion rate dropped 40%") must be triaged by SRE even when no Layer 2–6 alert has fired.

**Key observability signals**:
- Real-time GMV rate (target: stable ± 15% vs. same-time-last-week baseline)
- Checkout success rate (target: > 97% of checkout attempts complete within 30 seconds)
- Add-to-cart success rate (target: > 99.5% of add-to-cart API calls succeed)
- Session duration trend (significant drop = performance regression detectable before technical metrics fire)

**SRE tooling at this layer**: Grafana dashboards fed by application events, not infrastructure metrics. Amplitude or Mixpanel for funnel analytics (not replaced by Prometheus). Splunk for log-derived business metrics when analytics tools are not available.

**Layer 1 SLI definition**: Business SLIs are defined as the numerator/denominator of user journey success. For the checkout journey: SLI = successful_checkout_completions / checkout_attempts_started. This is the signal closest to the customer's actual experience.

---

## Layer 2 — API and Service Interface Layer

**What it is**: The external-facing surface of the system — API contracts, authentication, routing, and rate limiting.

**Components**:
- API Gateway (Kong / AWS API Gateway)
- Authentication endpoints (JWT issuance, refresh)
- Rate limiting rules (per-user, per-IP, per-API-key)
- API contract versioning
- GraphQL / REST endpoint definitions
- Webhook delivery endpoints

**What goes wrong at this layer**:
- API contract breaking changes (a field removed from a response breaks mobile clients that were not upgraded)
- Rate limit misconfiguration (too aggressive: legitimate users throttled; too loose: DDoS vectors)
- Authentication service overwhelm during peak (login storm after a mass notification)
- API Gateway configuration drift (a routing rule changed in one region but not others)
- mTLS certificate expiry causing service-to-service authentication failures

**SRE ownership**: API Gateway configuration, rate limiting policy, certificate rotation automation. Product teams own their API contracts; SRE owns the gateway through which all traffic flows.

**Key observability signals**:
- API Gateway 4xx rate by endpoint (spikes indicate broken clients or contract violations)
- API Gateway 5xx rate by endpoint (spikes indicate upstream service failures)
- Token validation latency p99 (> 50ms indicates Auth Service pressure)
- Rate limit hit rate (if > 5% of requests are rate-limited, the limits may be misconfigured)
- Certificate expiry countdown (alert at 30 days, 7 days, 1 day)

**Layer 2 SLI definition**: API availability = (total_API_requests - 5xx_responses) / total_API_requests per endpoint per journey.

---

## Layer 3 — Application Service Layer

**What it is**: The microservices that implement business logic. This is where most SRE operational work happens.

**Components**: All 12 services in Tier 2 of the architecture (Auth, Cart, Catalog, Inventory, Pricing, Payment, Order Management, Notification, Search, Recommendation, User Profile, Reviews).

**What goes wrong at this layer**:

| Failure pattern | Example | Detection signal |
|----------------|---------|-----------------|
| Memory leak | Cart Service OOM after 6 hours of traffic | Pod memory trending up; eventual OOMKill event |
| Database connection pool exhaustion | Inventory DB connection pool saturated during flash sale | DB connection error rate; p99 latency spike |
| Cascading timeout | Payment Service times out; caller retries; cascading overload | Concurrent request count spike; thread pool exhaustion |
| Business logic bug | Promotion code applied twice in one order | Revenue loss detected at Layer 1; no technical alert fires |
| Dependency version mismatch | gRPC protocol version incompatibility after upgrade | Specific endpoint 502 rate spike |
| Circuit breaker misfire | Circuit breaker opens on transient errors during peak | Increased error rate → downstream degradation |

**SRE ownership at this layer**: SRE does not own application code but owns:
- Production Readiness Review gate (service must pass PRR before any feature goes live)
- SLO definitions per service
- Circuit breaker configuration standards
- Resource requests/limits standards (CPU/memory)
- Probe configuration standards (liveness, readiness, startup)
- Error budget review cadence

**Four golden signals per service**:

| Signal | Metric name (example) | Alert threshold |
|-------|----------------------|----------------|
| Traffic | `http_requests_total{service="cart"}` by method | Traffic drops > 40% vs. baseline: page |
| Errors | `http_request_errors_total{service="cart"}` / total | Error rate > 1% for 5 min: warn; > 5%: page |
| Latency | `http_request_duration_seconds{quantile="0.99", service="cart"}` | p99 > 300ms for 5 min: warn; > 500ms: page |
| Saturation | CPU usage, memory usage, active_connections / max_connections | CPU > 80% for 10 min: warn; > 95%: page |

**Layer 3 SLI definition**: Service availability SLI = (successful_requests) / (total_requests) where "successful" means HTTP 2xx/3xx for the service's own errors, and the SLO window aligns with the journey SLA.

---

## Layer 4 — Middleware and Integration Layer

**What it is**: The messaging, eventing, and integration infrastructure that connects services asynchronously.

**Components**:
- Kafka event bus (order events, inventory events, analytics events)
- Dead Letter Queue (DLQ) for failed message processing
- Saga orchestration (distributed transaction coordination for checkout)
- Webhook fan-out for third-party integrations
- gRPC between services (internal API calls)
- Service mesh (Istio) traffic policies

**What goes wrong at this layer**:

| Failure pattern | Impact | Detection |
|----------------|--------|----------|
| Consumer lag buildup | Notification delays, analytics falling behind | Kafka consumer group lag metric |
| DLQ accumulation | Silent data loss if DLQ not monitored | DLQ depth metric; alert if DLQ > 0 for > 10 min |
| Saga timeout (distributed transaction) | Checkout payment taken but order not created | Saga state machine timeout counter |
| Message schema mismatch | Consumer fails to deserialize new message format | Consumer error rate; DLQ spike |
| Istio sidecar crashloop | All traffic to affected pod fails silently | Sidecar restart count; upstream error rate |
| Back-pressure not propagated | Upstream floods downstream beyond its capacity | Queue depth + consumer lag trending together |

**SRE ownership**: SRE owns the Kafka cluster health, consumer lag alerting, DLQ monitoring policy, and saga monitoring. Service teams own their producer/consumer implementations; SRE audits them during PRR.

**Critical observability gap at this layer**: most engineering organizations monitor Kafka broker health (topic replication, broker availability) but not consumer lag per consumer group per topic. A consumer group that is 500,000 messages behind a real-time topic is functionally unavailable for its business purpose — but no broker-level alert fires. Consumer lag alerting is one of the highest-ROI observability investments at this layer.

**Layer 4 SLI definition**: messaging SLI = (messages_successfully_delivered_within_SLA_window) / (total_messages_produced). For the Notification Service, the SLI is: what fraction of order confirmation emails were delivered within 60 seconds of the order being created.

---

## Layer 5 — Container and Infrastructure Layer

**What it is**: The Kubernetes platform, container runtime, compute, storage, and networking that services run on.

**Components**:
- EKS control plane (API server, etcd, scheduler, controller manager)
- EC2 worker nodes (instance types, autoscaling groups)
- Pod scheduling (resource requests/limits, node affinity, taints/tolerations)
- Persistent Volume Claims (for stateful services)
- Network policies (Calico or Cilium)
- Cluster autoscaler / Karpenter

**What goes wrong at this layer**:

| Failure pattern | Impact | Detection |
|----------------|--------|----------|
| Node NotReady | Pods evicted; services lose capacity | Node condition alert |
| Resource contention | Pods CPU-throttled or OOMKilled | Throttled_cpu_seconds; OOMKill events |
| PVC stuck Pending | Stateful pods cannot start | PVC status alert |
| etcd latency spike | K8s API server slow; deployments stall | etcd_request_latencies_summary |
| Karpenter over-provision delay | Scale-out takes > 3 minutes during traffic spike | Node provisioning time metric |
| Network policy blocking service | Service-to-service calls failing silently | Network policy log + service error rate correlation |

**SRE ownership**: Platform Engineering team owns EKS cluster health; product SRE teams own their pod configurations (resource requests, probes, PDBs). When a pod is OOMKilled, the Platform team alerts the product team — the product team owns fixing the memory limit. When the node is NotReady, Platform team owns the fix.

**Key cluster SLOs**:
- Pod scheduling latency p99 < 30 seconds (time from pod creation to Running)
- Node replacement time p99 < 5 minutes (time from node failure to replacement node Ready)
- Control plane API server availability > 99.9%
- PVC provisioning latency p99 < 60 seconds

**Layer 5 SLI definition**: infrastructure SLI = (pod_uptime_percentage across all P0 service pods). Target: 99.99% (infrastructure should not be the reliability bottleneck for P0 services).

---

## Layer 6 — Network and Physical Layer

**What it is**: The underlying network infrastructure — VPC, subnets, routing, DNS, inter-AZ traffic, CDN edges.

**Components**:
- AWS VPC (Virtual Private Cloud)
- Subnets (public, private, database)
- Route 53 (DNS, health checks, failover routing)
- NAT Gateway (outbound internet for private subnet services)
- Transit Gateway (if multi-account or multi-VPC)
- AWS PrivateLink (for secure service-to-service within AWS)
- CloudFront edge nodes
- Direct Connect (if applicable)

**What goes wrong at this layer**:

| Failure pattern | Impact | Detection |
|----------------|--------|----------|
| AZ network partition | All pods in affected AZ unreachable | AZ health metric; Route 53 health checks |
| NAT Gateway saturation | All outbound internet calls from private subnets fail | NAT Gateway connection error count |
| DNS resolution failure | Service discovery fails; service-to-service calls fail | DNS query failure rate |
| VPC flow log showing packet loss | Silent packet drops between services | VPC flow logs + NetFlow analysis |
| CDN origin pull storm | CDN cache miss during cold start; origin overwhelmed | CDN origin request rate vs. cache hit rate |
| Route 53 health check misconfiguration | Traffic routed to unhealthy endpoint | Health check state + error rate correlation |

**SRE ownership**: Network layer is owned by the Networking/Platform team. Product SRE teams observe network-layer failures through their service error rates but cannot fix them — escalation path to Networking must be documented in runbooks.

**Key insight**: network layer failures are the hardest to diagnose because they often produce ambiguous symptoms at Layer 3 (service error rates rise, but the error is "connection refused" or "timeout" rather than an application error). Correlating service error rate with VPC flow logs and DNS query failure rate is the diagnostic pattern that separates expert SRE from junior SRE.

**Layer 6 SLI definition**: network SLI = (successful inter-service network calls) / (total inter-service network calls). Measured via service mesh (Istio) telemetry rather than network-layer tooling.

---

## Cross-Layer Failure Analysis — The Checkout Journey

When checkout fails, the failure can originate at any of the six layers. Here is the diagnostic decision tree:

```
Checkout failure detected (Layer 1 signal: checkout success rate drops)
      │
      ├── Is the API Gateway returning errors?
      │   YES → Layer 2 failure (gateway config, rate limiting, auth)
      │   NO  → continue
      │
      ├── Is a specific service returning errors?
      │   YES → Layer 3 failure (application bug, crash, OOM)
      │         → Which service? → Check error rate by service label
      │   NO  → continue
      │
      ├── Is Kafka consumer lag growing?
      │   YES → Layer 4 failure (async processing backlog; Notification is delayed)
      │         → Does checkout block on Notification? → If yes, architectural bug
      │   NO  → continue
      │
      ├── Are pods OOMKilled or evicted?
      │   YES → Layer 5 failure (resource limits too low, node pressure)
      │   NO  → continue
      │
      ├── Is inter-AZ latency elevated?
      │   YES → Layer 6 failure (network partition, AZ degradation)
      │   NO  → escalate to AWS Support
```

This decision tree is the checkout journey runbook template. Each decision point maps to a specific metric query that the on-call engineer runs. The time from alert to correct layer identification is a major component of MTTD.

---

## Observability Requirements by Layer

| Layer | Primary signal type | Tooling | Who monitors | Key gap if absent |
|-------|-------------------|---------|-------------|------------------|
| L1 Business | Business events, funnel rates | Grafana (business metrics) + Amplitude | SRE + Product | Silent revenue loss not detected |
| L2 API/Interface | Request counts, error codes, latency | API Gateway metrics + Prometheus | SRE | Auth failures look like service failures |
| L3 Application | Golden signals per service | Prometheus + Grafana + Jaeger | SRE + Dev team | Can't isolate which service is failing |
| L4 Middleware | Consumer lag, DLQ depth, saga state | Kafka JMX + Prometheus | SRE | Async failures invisible; data loss silent |
| L5 Container/Infra | Node status, pod events, resource usage | K8s metrics server + Prometheus | Platform SRE | OOMKills look like random crashes |
| L6 Network | Packet loss, DNS failure, AZ health | VPC flow logs + Route 53 health | Networking team | Network partitions look like service failures |

**The critical observation**: without L4 (middleware) observability, the Notification Service failure mode (Kafka consumer stopped processing) would be invisible until customers email support asking where their order confirmation is. This is the "silent failure" class that causes customer dissatisfaction without triggering any operational alert.
