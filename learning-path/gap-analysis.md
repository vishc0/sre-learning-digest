# Knowledge Gap Analysis — Director of Operations Training Program

This document consolidates all identified curriculum gaps across three domains: infrastructure and virtualization, technical SRE and DevOps, and leadership and management. Use this file to decide which parallel-track content to build next and in what order.

---

## P1 Priority Gaps — All Domains

| # | Gap | Domain | Est. Hours |
|---|-----|--------|-----------|
| 1 | Bare metal vs VM vs container decision framework | Infrastructure | 8h |
| 2 | Data center operations | Infrastructure | 12h |
| 3 | Network infrastructure for directors | Infrastructure | 16h |
| 4 | VMware operational management | Infrastructure | 12h |
| 5 | Cloud vs colo vs on-prem framework | Infrastructure | 6h |
| 6 | Carrier/ISP relationship management | Infrastructure | 6h |
| 7 | Terraform advanced patterns | Infrastructure | 8h |
| 8 | Database reliability engineering | Infrastructure | 16h |
| 9 | Observability tooling deep dives | Infrastructure | 12h |
| 10 | SIEM and SOC operations | Technical SRE | 12h |
| 11 | FinOps as a discipline | Technical SRE | 10h |
| 12 | On-call program design | Technical SRE | 8h |
| 13 | Capacity planning methodology | Technical SRE | 8h |
| 14 | Board-level communication | Leadership | 6h |
| 15 | Crisis communication (external) | Leadership | 6h |
| 16 | Labor law and HR for engineering managers | Leadership | 6h |
| 17 | Organizational change management | Leadership | 6h |
| 18 | OKR design and cascade | Leadership | 4h |

**Total P1 hours**: ~162h

---

## Domain 1: Infrastructure & Virtualization

A Director of Operations at an enterprise makes infrastructure decisions that affect cost, reliability, and team structure for years. The current training program covers cloud-native (Kubernetes, AWS) and software-layer (SRE, performance, change management) content well, but lacks grounding in physical and virtual infrastructure fundamentals that a Director must understand to make sound architectural decisions.

---

### Category 1: Physical Infrastructure & Data Center Operations

#### 1.1 Bare Metal vs Virtualization vs Containerization Decision Framework

- **Gap**: No decision framework for when to use bare metal servers vs VMware VMs vs containers vs cloud.
- **Why it matters for a Director**: Directors make (or approve) infrastructure strategy decisions. A Director who only knows containers cannot evaluate a colocation proposal, a bare metal performance argument, or a VMware licensing renegotiation.
- **Key concepts to cover**:
  - Bare metal: when raw performance/latency demands it (HFT, GPU workloads, network-intensive), hardware lifecycle (3-5 year refresh cycle), BIOS/UEFI management, IPMI/iDRAC remote management
  - VMware vSphere/ESXi: vCenter, vMotion, HA clusters, DRS, memory overcommit, VMDK management, snapshot performance impact, vSAN storage, NSX networking
  - VMware vs alternatives: comparison with KVM/libvirt, Hyper-V, Proxmox — when to use each
  - VMware Broadcom acquisition (2024) impact: license model change, 72-core minimum (April 2025), VCSP termination (January 2026), cost implications, customer migration pressure
  - Physical-to-virtual (P2V) migration and virtual-to-container (V2C) modernization paths
  - Total Cost of Ownership comparison: bare metal (capex-heavy) vs VM (opex-moderate) vs cloud (opex-variable)
  - Director decision criteria: workload type, compliance requirements, team skill set, vendor lock-in risk, cost at scale
- **Estimated learning time**: 8 hours
- **Priority**: P1 (critical)
- **Target location**: `5-track-infrastructure/`

---

#### 1.2 Data Center Operations

- **Gap**: No coverage of data center design, operations, and governance.
- **Why it matters for a Director**: Directors approve DC contracts, colocation agreements, and capital expenditure for physical infrastructure. A Director who cannot read a Tier classification or evaluate PUE cannot challenge vendor proposals or assess risk.
- **Key concepts to cover**:
  - Tier classification: Tier I (99.671%), Tier II (99.741%), Tier III (99.982%), Tier IV (99.995%) — Uptime Institute standards
  - Physical redundancy: power (N+1, 2N), cooling (CRAC/CRAH units), network (dual upstream providers)
  - Power management: UPS, PDU, generator runtime, power density limits (kW per rack)
  - Cooling: hot aisle/cold aisle containment, PUE (Power Usage Effectiveness) — target < 1.5 for modern DC
  - Physical security: mantrap, biometric access, camera, visitor policy
  - Colocation vs owned DC vs cloud: financial model, control tradeoffs, exit strategy
  - DCIM tools: Nlyte, Sunbird, ServiceNow ITOM
  - DC incident categories: power outage, cooling failure, network loss, physical security breach
- **Estimated learning time**: 12 hours
- **Priority**: P1 (critical)
- **Target location**: `5-track-infrastructure/`

---

#### 1.3 Network Infrastructure for Operations Directors

- **Gap**: Network fundamentals covered only superficially — no operational network management content.
- **Why it matters for a Director**: Network failures are the leading cause of customer-impacting outages. A Director who cannot read a BGP route table or evaluate a CDN proposal cannot assess risk or make sound vendor decisions.
- **Key concepts to cover**:
  - OSI model operational implications: where SRE tools observe (L4 vs L7), where failures manifest
  - BGP basics: why Directors need to understand BGP (multi-ISP, cloud peering, route flaps cause outages)
  - MPLS/SD-WAN: enterprise WAN design
  - Load balancing deep dive: L4 (HAProxy, NLB) vs L7 (ALB, nginx, Envoy), health check mechanics, sticky sessions
  - DNS architecture: authoritative vs recursive, TTL strategy for failover, split-horizon DNS, DNSSEC
  - CDN: origin shielding, edge caching, cache invalidation, CDN failover
  - Firewall governance: zone design, rule lifecycle management, change approval process
  - DDoS protection: Cloudflare/AWS Shield/Akamai, scrubbing center model, Director's role during a DDoS event
  - Network capacity: bandwidth planning, burst vs sustained, ISP contract terms
- **Estimated learning time**: 16 hours
- **Priority**: P1 (critical)
- **Target location**: `5-track-infrastructure/`

---

#### 1.4 Storage Systems

- **Gap**: No storage content — SRE deals with storage failures constantly but the taxonomy is not taught.
- **Why it matters for a Director**: Storage is the most expensive and least reversible infrastructure decision. Directors approve storage vendor contracts and must understand IOPS, RAID tradeoffs, and cloud storage cost models.
- **Key concepts to cover**:
  - Storage types: DAS, NAS (NFS/SMB — NetApp, EMC Isilon), SAN (Fibre Channel, iSCSI — Pure Storage, Dell EMC), Object Storage (S3, Azure Blob, Ceph)
  - Performance characteristics: IOPS, throughput, latency — NVMe vs SSD vs spinning disk
  - RAID levels: RAID 0/1/5/6/10 — data protection vs performance vs capacity
  - Kubernetes storage: PVC/PV lifecycle, storage classes, CSI drivers, stateful applications on K8s
  - Backup and recovery: RPO/RTO from storage perspective, snapshot vs backup vs replication
  - Cloud storage: EBS (block), EFS (file), S3 (object) — when each is appropriate, cost model
- **Estimated learning time**: 8 hours
- **Priority**: P2 (important)
- **Target location**: `5-track-infrastructure/`

---

#### 1.5 Hardware Lifecycle Management

- **Gap**: No content on hardware EOL, refresh cycles, and procurement governance.
- **Why it matters for a Director**: Hardware EOL creates security risk and cost escalation that Directors must anticipate in capital budget cycles.
- **Key concepts to cover**:
  - Server lifecycle: procurement, racking, provisioning, in-service, end-of-support, decommission
  - Vendor support tiers: standard support, extended support, post-EOL risk, CVE coverage implications
  - Firmware and BIOS management: update cadence, risk in production
  - Asset management: CMDB entries for physical hardware, serial numbers, warranty expiry
  - Refresh cycle planning: typical 3-5 year server refresh, cost modeling, capital budget cycles
  - EOL risk management: security risk, support cost escalation, failure rate increase
- **Estimated learning time**: 6 hours
- **Priority**: P2 (important)
- **Target location**: `5-track-infrastructure/`

---

### Category 2: Virtualization Deep Dives

#### 2.1 VMware Operational Management

- **Gap**: VMware is widely deployed in enterprise but no operational content exists in the training program.
- **Why it matters for a Director**: Most enterprise environments still run VMware at scale. Post-Broadcom acquisition, VMware licensing has become a board-level cost conversation. Directors must understand the operational model to evaluate migration proposals.
- **Key concepts to cover**:
  - vCenter management: cluster design, host profiles, resource pools, DRS rules
  - VM templates and golden images: versioning, patching, compliance
  - vMotion and HA: live migration mechanics, when it fails
  - Snapshots: performance impact, maximum snapshot depth, cleanup automation
  - VMware Tanzu: VMware's Kubernetes offering
  - Licensing model post-Broadcom: per-core subscription, 72-core minimum, cost impact at enterprise scale
  - VMware to Kubernetes migration: use cases, risk, approach
  - vSAN: hyperconverged storage, witness node, deduplication/compression
  - NSX-T: micro-segmentation, east-west firewall, overlay networking
- **Estimated learning time**: 12 hours
- **Priority**: P1 (critical — high relevance in enterprise)
- **Target location**: `5-track-infrastructure/`

---

#### 2.2 Cloud vs Colo vs On-Prem Decision Framework

- **Gap**: No framework for the fundamental infrastructure location decision.
- **Why it matters for a Director**: Infrastructure location is a multi-year, multi-million dollar commitment.
- **Key concepts to cover**:
  - Financial model comparison: TCO over 3 years (cloud vs colo vs on-prem)
  - Data sovereignty and compliance: which workloads must stay on-prem
  - Cloud exit cost: egress fees, data transfer costs, migration effort — often underestimated by 3-5x
  - Hybrid cloud patterns: AWS Outposts, Azure Arc, Google Anthos
  - Director decision framework: 5 questions to evaluate any infrastructure location proposal
  - Vendor lock-in assessment: which services create irreversible dependency
- **Estimated learning time**: 6 hours
- **Priority**: P1 (critical)
- **Target location**: `5-track-infrastructure/`

---

### Category 3: Network Operations

#### 3.1 Network Change Management

- **Gap**: Existing change management covers software changes well; network changes have a fundamentally different risk profile and are not addressed.
- **Why it matters for a Director**: Network changes are among the highest-risk changes in an operations calendar. The Facebook 2021 outage (BGP route withdrawal) is the canonical example.
- **Key concepts to cover**:
  - Network change risk: why a misconfigured BGP route advertisement can take down a company
  - Network CAB process: separate review track, vendor (ISP/carrier) coordination
  - Maintenance windows for network: carrier-side windows, customer notification requirements
  - Network rollback: less clean than software — BGP route withdrawal, spanning tree recalculation
- **Estimated learning time**: 4 hours
- **Priority**: P2 (important)
- **Target location**: `5-track-infrastructure/`

---

#### 3.2 Carrier and ISP Relationship Management

- **Gap**: No Director-level content on managing ISP/carrier relationships — especially critical in a telecom context.
- **Why it matters for a Director**: At T-Mobile scale, network connectivity is the product. Directors are the primary escalation point for ISP SLA violations and major circuit outages.
- **Key concepts to cover**:
  - ISP contract terms: bandwidth commitment, burst capacity, SLA (99.9% uptime), diversity requirement
  - Circuit types: MPLS private line, dedicated internet access (DIA), SD-WAN
  - Peering and transit: BGP peering agreements, paid transit vs settlement-free peering
  - ISP SLA management: measuring against contractual commitments, credit claims process
  - Redundancy: diverse ISPs, diverse physical paths (not just diverse vendors — separate conduit)
  - Telecom regulatory context: FCC reporting for network outages, NORS (Network Outage Reporting System)
- **Estimated learning time**: 6 hours
- **Priority**: P1 (critical — highly relevant for telecom context)
- **Target location**: `5-track-infrastructure/`

---

### Category 4: Infrastructure as Code Deep Dives

#### 4.1 Terraform Advanced Patterns

- **Gap**: Terraform is in the Phase 1 curriculum but no operational governance content exists.
- **Key concepts to cover**:
  - Terraform state management: remote state (S3/Terraform Cloud), state locking, state drift
  - Module design: reusable modules, versioning, module registry
  - Terraform in CI/CD: plan-then-apply pipeline, drift detection
  - Security: secrets in Terraform state (problem), Vault integration, AWS Secrets Manager
  - Terraform governance: policy-as-code with Sentinel or OPA/Conftest
  - Team workflow: PR-based infrastructure changes, plan review in MR
  - Director decisions: when to use Terraform vs CDK vs CloudFormation vs Pulumi
- **Estimated learning time**: 8 hours
- **Priority**: P1 (critical)
- **Target location**: `1-phase-foundations/1.1-terraform-iac/` (advanced content)

---

#### 4.2 Configuration Management

- **Gap**: No content on Ansible/Chef/Puppet/SaltStack — these tools remain widely used in enterprises alongside Kubernetes for managing long-lived VMs and bare metal.
- **Key concepts to cover**:
  - Ansible: playbook structure, inventory, idempotency, roles, Tower/AWX
  - When to use config management vs containers: long-lived VMs and bare metal still need it
  - Drift detection: how to detect when a managed server diverges from desired state
- **Estimated learning time**: 6 hours
- **Priority**: P2 (important)
- **Target location**: `5-track-infrastructure/`

---

#### 4.3 GitOps

- **Gap**: GitOps principles are in Phase 1 (Week 4) but no advanced governance content exists.
- **Key concepts to cover**:
  - ArgoCD: application sync, health status, drift detection
  - Flux CD: alternative GitOps tool
  - GitOps for Kubernetes: sync loops, reconciliation, self-healing
  - GitOps governance: who can merge to what branch, approval gates
  - Multi-cluster GitOps: managing multiple Kubernetes clusters with one GitOps tool
- **Estimated learning time**: 6 hours
- **Priority**: P2 (important)
- **Target location**: `1-phase-foundations/1.4-aws-gitops/` (advanced content)

---

### Category 5: Missing Platform Topics

#### 5.1 Service Mesh

- **Gap**: Service mesh (Istio, Linkerd, Cilium) is mentioned but not taught as an operational discipline.
- **Key concepts to cover**:
  - Service mesh purpose: mTLS between services, traffic management, observability
  - Istio architecture: control plane (istiod), data plane (Envoy sidecars), Ambient mode (GA 2024 — no sidecar injection)
  - Traffic management: VirtualService, DestinationRule, Gateway, canary deployments with Istio
  - Security: mTLS policy, authorization policies, certificate rotation, SPIFFE/SPIRE workload identity
  - Operational complexity: sidecars consume resources; when service mesh pays off (20+ microservices threshold)
  - Linkerd: simpler, faster, 163ms faster than Istio at p99; certificates rotate every 24 hours automatically
  - Director decision: when does service mesh complexity pay off vs when is it over-engineering?
- **Estimated learning time**: 8 hours
- **Priority**: P2 (important) — note: research suggests upgrading to P1 given 47% production cluster adoption in 2025
- **Target location**: `6-track-technical-sre/`

---

#### 5.2 Database Reliability Engineering

- **Gap**: Databases are the most common single point of failure in production systems but the training program has no dedicated database reliability content.
- **Key concepts to cover**:
  - Database HA patterns: PostgreSQL streaming replication, Patroni/Pacemaker failover, Oracle RAC, MySQL Group Replication
  - CloudNativePG, Zalando postgres-operator: Kubernetes-native PostgreSQL HA
  - Connection pooling: PgBouncer, ProxySQL — why it matters for K8s (connection churn)
  - Database migrations in production: zero-downtime schema changes, expand-contract pattern
  - NoSQL operational patterns: MongoDB replica sets, Cassandra repair, Redis Sentinel vs Cluster
  - Database incident response: split-brain, replication lag, connection exhaustion, lock contention
  - Cassandra operational patterns (2025): consistent hashing ring awareness, compaction strategy tuning, read repair scheduling — directly applicable to T-Mobile DND platform
  - Chaos engineering for databases: Gremlin, Chaos Monkey — fault injection for real availability validation
  - Database SLOs: query latency percentiles (p50/p95/p99), transaction success rate, replication lag, backup recovery time (tested, not estimated), connection pool exhaustion rate
  - Director decisions: when to use managed DB (RDS/Aurora) vs self-managed, distributed SQL (CockroachDB, YugabyteDB) decision criteria
- **Estimated learning time**: 16 hours
- **Priority**: P1 (critical)
- **Target location**: `6-track-technical-sre/`

---

#### 5.3 Observability Tooling Deep Dives

- **Gap**: Observability concepts are covered but tool-specific operational knowledge and cost governance are not taught.
- **Why it matters for a Director**: Splunk ingest costs can exceed $1M/year at enterprise scale. Directors must understand the tooling well enough to govern cost, evaluate consolidation proposals, and make build-vs-buy decisions.
- **Key concepts to cover**:
  - Splunk: SPL query language, data models, index management, licensing model (ingest-based), Splunk Enterprise vs Cloud
  - Datadog: APM traces, log management, dashboards, monitors vs composite monitors, cost management
  - Prometheus/Grafana: metrics collection, PromQL, recording rules, alerting rules, Thanos for long-term storage
  - OpenTelemetry: collector architecture, auto-instrumentation, exporter configuration
  - Distributed tracing: Jaeger/Tempo — trace sampling strategy, storage cost
  - Cost management: Splunk ingest licensing costs at scale, Datadog metrics billing, strategies to control costs
  - Director decisions: observability stack consolidation vs best-of-breed, total cost modeling
- **Estimated learning time**: 12 hours
- **Priority**: P1 (critical)
- **Target location**: `6-track-technical-sre/`

---

### Infrastructure Gap Summary

| # | Gap | Priority | Est. Hours | Category |
|---|-----|----------|-----------|----------|
| 1 | Bare metal vs VM vs container decision framework | P1 | 8h | Infrastructure |
| 2 | Data center operations | P1 | 12h | Infrastructure |
| 3 | Network infrastructure for directors | P1 | 16h | Networking |
| 4 | VMware operational management | P1 | 12h | Virtualization |
| 5 | Cloud vs colo vs on-prem framework | P1 | 6h | Infrastructure |
| 6 | Carrier/ISP relationship management | P1 | 6h | Networking |
| 7 | Terraform advanced patterns | P1 | 8h | IaC |
| 8 | Database reliability engineering | P1 | 16h | Platform |
| 9 | Observability tooling deep dives | P1 | 12h | Observability |
| 10 | Storage systems | P2 | 8h | Infrastructure |
| 11 | Hardware lifecycle management | P2 | 6h | Infrastructure |
| 12 | Network change management | P2 | 4h | Networking |
| 13 | Configuration management (Ansible) | P2 | 6h | IaC |
| 14 | GitOps (advanced governance) | P2 | 6h | IaC |
| 15 | Service mesh (Istio/Linkerd) | P2 | 8h | Platform |

---

## Domain 2: Technical SRE & DevOps

---

### Category 1: Security Operations (SecOps)

#### 1.1 SIEM and SOC Operations

- **Gap**: DevSecOps covers security scanning in CI/CD pipeline but no coverage of security operations as an ongoing discipline.
- **Why it matters for a Director**: Directors of Operations often have a SOC as a peer or direct report. You must understand what they do to govern the relationship and handle incident handoffs cleanly.
- **Key concepts to cover**:
  - SIEM architecture: Splunk Enterprise Security, Microsoft Sentinel, QRadar, Sumo Logic Security
  - Use case development: correlation rules, behavioral analytics
  - Alert triage: SOC L1/L2/L3 analyst model, alert fatigue, MTTA from a security perspective
  - Security incident coordination: when a security event is also an operational incident — who leads?
  - Threat intelligence integration: IOC feeds, TTP mapping (MITRE ATT&CK)
  - SOAR (Security Orchestration, Automation, Response): playbook automation, case management
  - Vulnerability management lifecycle: scan → triage → remediation SLA → verification
  - Director's SIEM obligation: providing log sources, access review, audit response
- **Estimated learning time**: 12 hours
- **Priority**: P1
- **Target location**: `6-track-technical-sre/`

---

#### 1.2 Zero Trust Architecture Implementation

- **Gap**: Zero Trust is listed as an architecture principle but no operational implementation guidance exists.
- **Key concepts**:
  - Identity-centric access and the BeyondCorp model
  - Microsegmentation implementation
  - SASE (Secure Access Service Edge)
  - PAM (Privileged Access Management): CyberArk, HashiCorp Vault
  - Certificate lifecycle management
  - Mutual TLS at scale; SPIFFE/SPIRE workload identity
  - Istio Ambient mode as the 2025-standard deployment model for mTLS
- **Estimated learning time**: 8 hours
- **Priority**: P1 (upgraded from P2 — 47% of Kubernetes production clusters now run a service mesh in 2025)
- **Target location**: `6-track-technical-sre/`

---

#### 1.3 Compliance Automation

- **Gap**: Compliance is mentioned in governance modules but no tooling-level content exists.
- **Key concepts**:
  - Policy-as-code: OPA/Rego, AWS Config Rules, Azure Policy
  - Compliance scanning: Checkov, Prisma Cloud, Wiz
  - SOC 2 continuous compliance and evidence automation
  - Drift detection for compliance controls
- **Estimated learning time**: 6 hours
- **Priority**: P2
- **Target location**: `6-track-technical-sre/`

---

### Category 2: FinOps & Cloud Cost Engineering

#### 2.1 FinOps as a Discipline

- **Gap**: Budget management is in the Director course but no dedicated FinOps content exists for cloud cost optimization.
- **Why it matters**: Cloud costs are typically the 2nd or 3rd largest line item in an operations budget. A Director who cannot optimize cloud spend is leaving 20–40% of cloud budget on the table.
- **Key concepts**:
  - FinOps lifecycle: Inform → Optimize → Operate
  - FinOps Maturity Model: Crawl (basic visibility) → Walk (chargeback, anomaly detection) → Run (unit economics, automated optimization, AI cost governance)
  - Reserved Instances vs Savings Plans vs On-Demand vs Spot — decision model
  - Right-sizing: analyzing CPU/memory utilization to identify over-provisioned resources
  - Kubernetes cost: cost per namespace/team, Kubecost, OpenCost, KubeGreen
  - Data transfer costs: the most commonly missed cloud cost category (egress fees)
  - Unit economics: tying technology spend to business outcomes — cost per message delivered, cost per API call
  - Showback vs chargeback: allocating cloud costs to business units
  - AI cost governance: managing LLM/GPU spend — jumped from 31% to 98% of FinOps teams in two years
  - FOCUS specification: the emerging cloud-agnostic cost data standard
  - FinOps tooling: AWS Cost Explorer, CloudHealth, Apptio Cloudability
- **Estimated learning time**: 10 hours
- **Priority**: P1 (upgraded from P2 — FinOps is now a Director core competency, not a Finance-adjacent skill)
- **Target location**: `6-track-technical-sre/`

---

### Category 3: On-Call Program Design

#### 3.1 On-Call Program as an Operational System

- **Gap**: On-call is referenced throughout the program but no dedicated content exists on designing and governing the on-call program as a system.
- **Why it matters**: On-call load is the #1 retention risk for SRE teams. A Director who cannot design a healthy on-call program will lose engineers.
- **Key concepts**:
  - On-call rotation design: minimum team size (5 engineers), primary/secondary/escalation tiers
  - Escalation policy design: time-to-escalate, whom to escalate to at each tier
  - On-call compensation: industry models (incident pay vs on-call retainer vs salary premium)
  - Pager load thresholds: alert volume targets, actionable vs noise alert ratio
  - Alert quality program: alert lifecycle (create → validate → tune → deprecate), alert ownership
  - Runbook coverage requirement: no service enters on-call rotation without 100% runbook coverage
  - On-call health metrics: pages per engineer per night, MTTA trend, alert-to-action ratio
  - Director's on-call governance: monthly review of on-call health dashboard, intervention criteria
- **Estimated learning time**: 8 hours
- **Priority**: P1
- **Target location**: `6-track-technical-sre/`

---

### Category 4: Capacity Planning

#### 4.1 Capacity Planning Methodology

- **Gap**: Capacity is referenced in the performance engineering module but no dedicated capacity planning methodology exists.
- **Key concepts**:
  - Demand forecasting: trend-based, seasonality patterns, business-driven (user growth, new products)
  - Capacity models: working set size × safety factor, Little's Law for queue-based capacity
  - USL (Universal Scalability Law): when adding resources stops helping
  - Kubernetes capacity: node sizing, pod packing, HPA vs VPA vs KEDA
  - Database capacity: connections, IOPS, storage growth rate
  - Network capacity: bandwidth utilization, 80% rule for link saturation
  - Capacity planning cadence: quarterly capacity review, annual capacity plan, trigger-based interim reviews
  - Director's capacity governance: approving capacity investments, communicating capacity risk to VP
- **Estimated learning time**: 8 hours
- **Priority**: P1
- **Target location**: `6-track-technical-sre/`

---

### Category 5: Multi-Cloud and Cloud Architecture

#### 5.1 Multi-Cloud Strategy and Operations

- **Gap**: AWS is covered in labs; Azure and GCP are not. Multi-cloud is a Director-level decision topic.
- **Key concepts**:
  - Multi-cloud vs multi-region single cloud: when each is appropriate
  - Cloud provider comparison: AWS vs Azure vs GCP for operations workloads
  - Cloud-agnostic SLOs: OpenTelemetry as the abstraction layer, unified backends (Grafana + Thanos, Datadog, Dynatrace)
  - Multi-cloud incident runbooks: which cloud's control plane is authoritative, DNS failover across providers
  - Cost vs resilience trade-offs: multi-cloud adds 20-40% operational overhead — which workloads justify it?
  - Vendor lock-in assessment: which services create irreversible dependency per cloud
  - Director decisions: how to evaluate a cloud consolidation vs multi-cloud argument
- **Estimated learning time**: 10 hours
- **Priority**: P2
- **Target location**: `6-track-technical-sre/`

---

### Category 6: AI Operations

#### 6.1 MLOps and AI Infrastructure Reliability

- **Gap**: `1-phase-foundations/1.0-vocabulary/1.0.11-ai-for-sre.md` covers AI-assisted SRE but no content exists on operating AI/ML workloads reliably.
- **Key concepts**:
  - ML pipeline reliability: training pipeline failures, model serving outages, feature store latency
  - GPU infrastructure: GPU scheduling in Kubernetes (NVIDIA device plugin), GPU memory management
  - AI system SLOs: hallucination rate, output consistency rate, retrieval precision (for RAG), guardrail pass-through rate, data drift rate — these are not yet standardized; Directors must design from first principles
  - LLMOps: LangSmith, Langfuse, Evidently AI for LLM observability; vLLM, Ollama for inference
  - Model drift detection, training-serving skew, feature store staleness
  - AI cost explosion: 98% of FinOps teams now manage AI spend (up from 31% in 2024)
  - Director decisions: build vs buy for AI infrastructure, GPU capacity planning
- **Estimated learning time**: 10 hours
- **Priority**: P2
- **Target location**: `1-phase-foundations/1.10-ai-production/` (advanced content) or `6-track-technical-sre/`

---

### Category 7: Developer Experience and Platform Maturity

#### 7.1 Platform Engineering Maturity Model

- **Gap**: Platform engineering week covers Backstage but no maturity model exists for evaluating the overall IDP.
- **Key concepts**:
  - Platform maturity stages: ad-hoc tooling → shared scripts → internal platform → product platform
  - Platform as a product: platform team as internal product team with internal customers
  - Team Topologies vocabulary: stream-aligned, platform, enabling, complicated-subsystem teams
  - Backstage reality check: 3-5 dedicated engineers Year 1, 2-3 to maintain — this is the most common Director mistake to scope it as a weekend project
  - Alternative IDPs: Port, Cortex, OpsLevel — growing market share vs Backstage build cost
  - Platform metrics: DORA for the platform team, developer satisfaction (SPACE framework)
  - AI + platform quality relationship: DORA 2025 shows AI adoption only boosts performance when platform quality is already high
- **Estimated learning time**: 8 hours
- **Priority**: P2
- **Target location**: `6-track-technical-sre/`

---

### Technical SRE Gap Summary

| # | Gap | Priority | Est. Hours |
|---|-----|----------|-----------|
| 1 | SIEM and SOC operations | P1 | 12h |
| 2 | FinOps as a discipline | P1 | 10h |
| 3 | On-call program design | P1 | 8h |
| 4 | Capacity planning methodology | P1 | 8h |
| 5 | Zero Trust architecture implementation | P1 | 8h |
| 6 | Multi-cloud strategy and operations | P2 | 10h |
| 7 | Compliance automation | P2 | 6h |
| 8 | MLOps and AI infrastructure reliability | P2 | 10h |
| 9 | Platform engineering maturity model | P2 | 8h |

---

## Domain 3: Leadership & Management

---

### Category 1: Executive Presence and Communication

#### 1.1 Board-Level Communication

**Gap**: Executive communication covers VP reporting but not board-level presentations.

**Why it matters**: A VP of Operations presents to the board quarterly in most enterprises. Director-level staff prepare this content and must understand the format, audience, and risk of getting it wrong.

**Key concepts**:

- Board composition and what board members care about: risk, compliance, ROI, competitive position
- Translating operational metrics to board language: not "MTTR improved 15%" but "we reduced customer impact time by 15%, reducing estimated revenue impact by $X"
- Board risk reporting: operational risk materiality threshold — what rises to board level vs stays at executive level
- Board presentation format: 3–5 slides, executive summary first, appendix with supporting detail
- Pre-board alignment: CEO/CFO alignment before the board sees it, handling questions you were not asked

**Priority**: P1 | **Estimated**: 6h | **Target location**: `7-track-leadership-advanced/`

---

#### 1.2 Crisis Communication (External Facing)

**Gap**: Stakeholder management covers internal communication well but no external crisis communication content exists.

**Key concepts**:

- Media/PR coordination during a major outage: who speaks, what can be said, what cannot
- Customer-facing status pages: what to say and when (vs internal bridge communication)
- Regulatory reporting obligations: FCC network outage reports (Form 480, timing requirements), SEC 8-K for publicly traded companies, state PUC notifications
- Social media response: how to handle Twitter/X during a visible outage
- Post-incident public statement: format, timing, what to include and exclude
- Legal coordination: what you must not say during an incident (admission of liability, financial estimates)

**Priority**: P1 | **Estimated**: 6h | **Target location**: `7-track-leadership-advanced/`

---

### Category 2: Financial and Business Acumen

#### 2.1 P&L Ownership

**Gap**: Budget management module covers department-level budget but not P&L responsibility or the shift from cost center to value center.

**Key concepts**:

- Revenue-generating vs cost-center org: how Operations shifts to a profit center model
- Chargeback model: charging business units for SRE services
- Reliability ROI presentation to CFO: quantifying the value of avoided incidents
- Business case for SRE investment: the financial argument for platform reliability spending
- Reading the company income statement: how operational costs affect margins

**Priority**: P2 | **Estimated**: 6h | **Target location**: `7-track-leadership-advanced/`

---

#### 2.2 Contract Negotiation

**Gap**: Vendor management module covers vendor relationships but not negotiation tactics at operational depth.

**Key concepts**:

- Negotiation principles: BATNA, zone of possible agreement (ZOPA)
- Multi-year contract negotiation: when to commit to 3 years, expected discount structure
- SLA penalty negotiation: pushing vendors for meaningful remedies (not 10% monthly credit caps)
- MSA vs SOW structure: which terms belong in which
- Contract renewal negotiation: how to use competitive quotes and timing as leverage

**Priority**: P2 | **Estimated**: 6h | **Target location**: `7-track-leadership-advanced/`

---

### Category 3: People Leadership Depth

#### 3.1 Labor Law and HR for Engineering Managers

**Gap**: People leadership covers management practices but not the legal and HR framework managers operate within. Getting this wrong creates legal exposure for the company and the manager personally.

**Key concepts**:

- At-will employment vs employment contracts: implications for termination decisions
- Performance improvement plans (PIPs): legal purpose, documentation requirements, common pitfalls
- Protected classes and discrimination: what you can and cannot consider in hiring, promotion, and termination decisions
- Wage and hour: exempt vs non-exempt classification, on-call pay obligations for hourly employees
- FMLA and ADA: manager obligations when an employee has a medical situation
- Hostile work environment: definition, manager reporting obligation, investigation process
- HR business partner role: when and how to engage HR as a manager

**Priority**: P1 | **Estimated**: 6h | **Target location**: `7-track-leadership-advanced/`

---

#### 3.2 Organizational Change Management

**Gap**: No content exists on managing people through organizational change — reorgs, layoffs, major process changes.

**Key concepts**:

- Kotter's 8-step model for leading change
- ADKAR model: Awareness, Desire, Knowledge, Ability, Reinforcement
- Resistance to change: why engineers resist process changes and how to address root causes
- Communication sequencing during a reorg: who hears what, in what order, through which channel
- Layoff process: how a Director is informed, what they can and cannot share before announcement, how to handle the team immediately after
- Survivor syndrome: the team members left after a layoff and how to stabilize and retain them

**Priority**: P1 | **Estimated**: 6h | **Target location**: `7-track-leadership-advanced/`

---

#### 3.3 Coaching and Mentoring at Scale

**Gap**: People leadership covers 1:1s and feedback but not structured coaching methodology for developing senior engineers and managers.

**Key concepts**:

- GROW model: Goal, Reality, Options, Will/Way forward — the standard coaching framework
- Coaching vs mentoring vs sponsorship: different relationships with different appropriate uses
- Situational leadership: adapting your style to the employee's competence/commitment level
- Stretch assignment design: how to design an assignment that develops without overwhelming

**Priority**: P2 | **Estimated**: 6h | **Target location**: `7-track-leadership-advanced/`

---

### Category 4: Strategy and Organizational Design

#### 4.1 OKR Design and Cascade

**Gap**: Metrics tracking is well-covered but objective-setting methodology is not. Metrics tell you what is happening; OKRs tell you what you are trying to change.

**Key concepts**:

- OKR structure: Objective (qualitative, inspiring) + Key Results (quantitative, time-bound)
- OKR cascade: company → department → team → individual alignment
- Common OKR mistakes: too many OKRs, key results that are tasks not outcomes, 100% hit rate (set too easy)
- OKR cadence: annual objectives with quarterly key results
- OKR for an operations team: reliability OKRs differ from product OKRs — what good looks like in practice
- Grading OKRs: 0.7 as the target score

**Priority**: P1 | **Estimated**: 4h | **Target location**: `7-track-leadership-advanced/`

---

#### 4.2 Industry Analysis and Technology Strategy

**Gap**: Architecture principles are internal-facing. No content exists on how Directors track and act on industry trends to inform investment decisions.

**Key concepts**:

- Gartner Hype Cycle: how to interpret it for technology investment decisions
- Technology radar: ThoughtWorks radar methodology, building a company-internal radar
- Analyst relations: Gartner/Forrester briefings, what analysts are looking for
- Conference participation: KubeCon, SREcon, PlatformCon — Director participation strategy and ROI

**Priority**: P3 | **Estimated**: 4h | **Target location**: `7-track-leadership-advanced/`

---

### Leadership Gap Summary

| # | Gap | Priority | Est. Hours |
|---|-----|----------|-----------|
| 1 | Board-level communication | P1 | 6h |
| 2 | Crisis communication (external) | P1 | 6h |
| 3 | Labor law and HR for engineering managers | P1 | 6h |
| 4 | Organizational change management | P1 | 6h |
| 5 | OKR design and cascade | P1 | 4h |
| 6 | P&L ownership | P2 | 6h |
| 7 | Contract negotiation | P2 | 6h |
| 8 | Coaching and mentoring at scale | P2 | 6h |
| 9 | Industry analysis and technology strategy | P3 | 4h |

---

## Master Gap Summary — All Domains

| # | Gap | Domain | Priority | Est. Hours | Target Folder |
|---|-----|--------|----------|-----------|---------------|
| 1 | Bare metal vs VM vs container framework | Infrastructure | P1 | 8h | 5-track-infrastructure/ |
| 2 | Data center operations | Infrastructure | P1 | 12h | 5-track-infrastructure/ |
| 3 | Network infrastructure for directors | Infrastructure | P1 | 16h | 5-track-infrastructure/ |
| 4 | VMware operational management | Infrastructure | P1 | 12h | 5-track-infrastructure/ |
| 5 | Cloud vs colo vs on-prem framework | Infrastructure | P1 | 6h | 5-track-infrastructure/ |
| 6 | Carrier/ISP relationship management | Infrastructure | P1 | 6h | 5-track-infrastructure/ |
| 7 | Terraform advanced patterns | Infrastructure | P1 | 8h | 1-phase-foundations/1.1-terraform-iac/ |
| 8 | Database reliability engineering | Infrastructure | P1 | 16h | 6-track-technical-sre/ |
| 9 | Observability tooling deep dives | Infrastructure | P1 | 12h | 6-track-technical-sre/ |
| 10 | SIEM and SOC operations | Technical SRE | P1 | 12h | 6-track-technical-sre/ |
| 11 | FinOps as a discipline | Technical SRE | P1 | 10h | 6-track-technical-sre/ |
| 12 | On-call program design | Technical SRE | P1 | 8h | 6-track-technical-sre/ |
| 13 | Capacity planning methodology | Technical SRE | P1 | 8h | 6-track-technical-sre/ |
| 14 | Zero Trust architecture implementation | Technical SRE | P1 | 8h | 6-track-technical-sre/ |
| 15 | Board-level communication | Leadership | P1 | 6h | 7-track-leadership-advanced/ |
| 16 | Crisis communication (external) | Leadership | P1 | 6h | 7-track-leadership-advanced/ |
| 17 | Labor law and HR for engineering managers | Leadership | P1 | 6h | 7-track-leadership-advanced/ |
| 18 | Organizational change management | Leadership | P1 | 6h | 7-track-leadership-advanced/ |
| 19 | OKR design and cascade | Leadership | P1 | 4h | 7-track-leadership-advanced/ |
| 20 | Storage systems | Infrastructure | P2 | 8h | 5-track-infrastructure/ |
| 21 | Hardware lifecycle management | Infrastructure | P2 | 6h | 5-track-infrastructure/ |
| 22 | Network change management | Infrastructure | P2 | 4h | 5-track-infrastructure/ |
| 23 | Configuration management (Ansible) | Infrastructure | P2 | 6h | 5-track-infrastructure/ |
| 24 | GitOps (advanced governance) | Infrastructure | P2 | 6h | 1-phase-foundations/1.4-aws-gitops/ |
| 25 | Service mesh (Istio/Linkerd) | Infrastructure | P2 | 8h | 6-track-technical-sre/ |
| 26 | Multi-cloud strategy and operations | Technical SRE | P2 | 10h | 6-track-technical-sre/ |
| 27 | Compliance automation | Technical SRE | P2 | 6h | 6-track-technical-sre/ |
| 28 | MLOps and AI infrastructure reliability | Technical SRE | P2 | 10h | 6-track-technical-sre/ |
| 29 | Platform engineering maturity model | Technical SRE | P2 | 8h | 6-track-technical-sre/ |
| 30 | P&L ownership | Leadership | P2 | 6h | 7-track-leadership-advanced/ |
| 31 | Contract negotiation | Leadership | P2 | 6h | 7-track-leadership-advanced/ |
| 32 | Coaching and mentoring at scale | Leadership | P2 | 6h | 7-track-leadership-advanced/ |
| 33 | Industry analysis and technology strategy | Leadership | P3 | 4h | 7-track-leadership-advanced/ |

**Total P1**: 19 gaps, ~162 hours  
**Total P2**: 13 gaps, ~90 hours  
**Total P3**: 1 gap, 4 hours  
**Grand total**: 33 gaps, ~256 hours of content to build

---

## Recommended Build Sequence

Build P1 content in this order to maximize coverage of the most Director-critical gaps first:

1. **Batch 1** — Infrastructure core (parallel): bare metal/VM/container framework, data center operations, cloud vs colo decision framework → `5-track-infrastructure/`
2. **Batch 2** — Network and VMware (parallel): network for directors, ISP/carrier management, VMware operational management → `5-track-infrastructure/`
3. **Batch 3** — Platform reliability (parallel): database reliability engineering, observability tooling deep dives → `6-track-technical-sre/`
4. **Batch 4** — Security and cost (parallel): SIEM/SOC operations, FinOps, Zero Trust → `6-track-technical-sre/`
5. **Batch 5** — Operations design (parallel): on-call program design, capacity planning → `6-track-technical-sre/`
6. **Batch 6** — Leadership (parallel): board communication, crisis communication, labor law, org change management, OKRs → `7-track-leadership-advanced/`
