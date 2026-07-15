# SRE/DevSecOps Master Glossary — 2025-2026

## How to Use This Glossary

Rate every term on the 1–5 confidence scale below; revisit any term scored 1–2 before your next weekly review session. During Sunday calibration, sweep all terms in your two weakest domains and update scores. Before any interview, read every term in the TOP 60 table and verify you can answer a "tell me about a time you used X" question. Use the Level column (Know / Configure / Design / Build) to set your study depth — Know terms need a crisp 15-second definition; Build terms need a code or config example ready.

## Confidence Tracking Key

| Score | Meaning |
|---|---|
| 1 | Can spell it |
| 2 | Can define it |
| 3 | Can explain why it matters |
| 4 | Can explain tradeoffs + use in a STAR answer |
| 5 | Can teach it and handle follow-up questions |

---

## Domain 1: Kubernetes & Container Orchestration

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| Pod | Smallest deployable unit; one or more containers sharing network/storage | Asked in every K8s screen; know lifecycle states | Know | |
| ReplicaSet | Controller that ensures N identical pod copies are always running | Foundation for Deployment; know difference from Deployment | Know | |
| Deployment | Declarative spec for rolling out and updating ReplicaSets | Most common workload resource; know rollout/rollback commands | Configure | |
| StatefulSet | Manages pods with stable network identity and persistent storage | Used for Cassandra, Kafka, Redis on K8s — ties to your stack | Configure | |
| DaemonSet | Ensures one pod runs on every (or selected) node | Used for log agents, node exporters — common in observability | Configure | |
| Job / CronJob | Runs a pod to completion once or on a schedule | Batch processing, data cleanup; know ttlSecondsAfterFinished | Configure | |
| Namespace | Virtual cluster partition for multi-tenancy and access isolation | RBAC always scoped to namespace; know cluster-scoped exceptions | Configure | |
| ConfigMap | Stores non-secret configuration as key-value pairs or files | Decouple config from image; immutable ConfigMaps pattern | Configure | |
| Secret | Base64-encoded K8s object for sensitive config (not encrypted by default) | Interviewers probe: "why is Secret not really secret?" — know etcd encryption | Design | |
| ServiceAccount | Identity assigned to pods for API server authentication | Foundation for IRSA, Workload Identity; critical for zero-trust | Design | |
| RBAC | Role-based access control; defines who can do what to which resources | Staff role expectation: design cluster-wide RBAC strategy | Design | |
| ClusterRole / Role | RBAC policy scoped to cluster-wide or single namespace resources | Know difference; common interview: "when do you use ClusterRole?" | Design | |
| RoleBinding / ClusterRoleBinding | Binds a Role to a subject (user, group, ServiceAccount) | Pair with Role/ClusterRole; know aggregated ClusterRoles | Design | |
| Service (ClusterIP) | Internal virtual IP load-balancing traffic to matching pods | Foundation of K8s networking; understand kube-proxy modes | Know | |
| Service (NodePort) | Exposes service on every node's IP at a static port | Dev/test use only; not for production — know why | Know | |
| Service (LoadBalancer) | Provisions cloud LB; exposes service externally | AWS NLB/ALB integration via annotations; common in EKS | Configure | |
| Ingress | L7 HTTP routing rules managed by an Ingress Controller | NGINX, AWS ALB Ingress Controller; path/host-based routing | Configure | |
| Ingress Controller | Pod that watches Ingress objects and programs actual load balancer | Know NGINX vs AWS LB Controller tradeoffs in EKS | Design | |
| NetworkPolicy | Firewall rules restricting pod-to-pod and pod-to-external traffic | Zero-trust network segmentation; CNI must support it | Design | |
| CNI (Container Network Interface) | Plugin interface defining how pods get IP addresses and network | Calico, Cilium, AWS VPC CNI — know tradeoffs | Design | |
| Calico | CNI with eBPF dataplane and rich NetworkPolicy support | Common in regulated environments; used for micro-segmentation | Design | |
| Cilium | eBPF-based CNI with L7 policy, Hubble observability built in | Staff-level: Cilium replaces kube-proxy, enables deeper observability | Design | |
| etcd | Distributed KV store; the K8s control plane's source of truth | Know: encrypting secrets at rest in etcd is a CKS topic | Design | |
| kube-apiserver | Front door to the control plane; all K8s API calls go through here | Audit logging, admission webhooks attach here | Design | |
| kube-scheduler | Assigns pods to nodes based on resource requests, taints, affinities | Node affinity, taints/tolerations, topology spread constraints | Design | |
| kube-controller-manager | Runs all built-in controllers (ReplicaSet, Deployment, Node, etc.) | Know: each controller is a reconciliation loop — key concept | Design | |
| kubelet | Node agent; ensures containers described in PodSpec are running | Node Not Ready? Start with kubelet logs | Configure | |
| kube-proxy | Implements Service virtual IPs via iptables or IPVS rules | Cilium can replace kube-proxy entirely with eBPF | Know | |
| Taint / Toleration | Node taint repels pods; toleration on pod allows scheduling there | Dedicated node pools (GPU, spot); isolate noisy tenants | Configure | |
| Node Affinity | Rules guiding scheduler to prefer or require specific nodes | Use with topology spread for HA across AZs | Configure | |
| Pod Affinity / Anti-Affinity | Rules co-locating or separating pods relative to other pods | Anti-affinity spreads replicas across nodes/zones | Configure | |
| Topology Spread Constraints | Distributes pods evenly across topology domains (zones, nodes) | Replaces PodAntiAffinity for zone-level HA; newer pattern | Configure | |
| PodDisruptionBudget (PDB) | Minimum available pods guaranteed during voluntary disruptions | Critical for zero-downtime node drains; Staff must govern this | Design | |
| HPA (Horizontal Pod Autoscaler) | Scales pod count based on CPU, memory, or custom metrics | Know: custom metrics via Prometheus Adapter; KEDA for events | Configure | |
| VPA (Vertical Pod Autoscaler) | Adjusts CPU/memory requests/limits automatically over time | Use for right-sizing; know: do not use VPA + HPA on same metric | Design | |
| KEDA | Event-driven autoscaler; scales to zero based on queue depth etc. | Scales on SQS, Kafka, RabbitMQ — directly relevant to your stack | Configure | |
| Resource Requests / Limits | CPU/memory minimums (scheduling) and maximums (enforcement) | QoS classes: Guaranteed, Burstable, BestEffort — know impact | Design | |
| LimitRange | Sets default and max resource limits per namespace | Governance: prevents runaway pods consuming all node capacity | Configure | |
| ResourceQuota | Caps total resource consumption per namespace | Multi-tenant governance; pairs with LimitRange | Configure | |
| PersistentVolume (PV) | Cluster-level storage resource provisioned by admin or dynamically | Know static vs dynamic provisioning | Configure | |
| PersistentVolumeClaim (PVC) | Pod's request for storage; bound to a matching PV | Know access modes: RWO, ROX, RWX | Configure | |
| StorageClass | Defines storage provisioner and parameters for dynamic PV creation | EBS gp3 vs io2; know volume binding modes | Configure | |
| CSI (Container Storage Interface) | Standard plugin interface for storage drivers in K8s | EBS CSI driver, EFS CSI driver are the AWS implementations | Know | |
| Admission Controller | Plugin in API server pipeline that validates/mutates incoming requests | Foundation for policy-as-code; know mutating vs validating | Design | |
| MutatingWebhookConfiguration | Registers external webhook that modifies (mutates) API objects | Istio sidecar injection uses this; secrets injection via Vault | Design | |
| ValidatingWebhookConfiguration | Registers external webhook that accepts or rejects API objects | OPA Gatekeeper, Kyverno policy enforcement entry point | Design | |
| OPA Gatekeeper | Admission controller enforcing Rego policies as ConstraintTemplates | Staff expectation: write and govern cluster-wide policy library | Build | |
| Kyverno | K8s-native policy engine; policies are written as K8s resources | Alternative to Gatekeeper; simpler YAML syntax | Configure | |
| Helm | Package manager for K8s; bundles manifests into versioned charts | Know: values.yaml override, chart versioning, helmfile | Configure | |
| Helm Chart | Templated K8s manifest bundle with values substitution | Know chart structure: Chart.yaml, templates/, values.yaml | Configure | |
| Kustomize | Overlay-based manifest customization without templating | Built into kubectl; base + overlay pattern for env promotion | Configure | |
| Operator Pattern | Custom controller + CRD that encodes domain operational logic in code | Staff-level: design and explain; Build-level for principal roles | Build | |
| CRD (Custom Resource Definition) | Extends K8s API with custom object types | Foundation of Operator pattern; know how CR + controller interact | Design | |
| Controller Reconciliation Loop | Watch events → compare desired vs actual → act to converge state | Core concept behind all K8s controllers; explain in any interview | Design | |
| Finalizer | Marks resource for pre-deletion cleanup logic by a controller | Prevents dangling cloud resources when K8s objects are deleted | Design | |
| OwnerReference | Links child resource to owner; enables cascading deletion | Garbage collection mechanism; set by controllers | Know | |
| Init Container | Runs to completion before app containers start in a pod | Used for migrations, secret fetching, dependency checks | Configure | |
| Sidecar Container | Co-located container sharing pod network/storage with main app | Istio proxy, log shippers, secret agents are sidecars | Configure | |
| Istio | Service mesh: mTLS, traffic management, observability via sidecar | Staff: design mTLS policy; know Istio vs Cilium tradeoffs | Design | |
| Linkerd | Lightweight service mesh using Rust micro-proxy sidecars | Simpler than Istio; lower overhead; less feature-rich | Know | |
| mTLS (Mutual TLS) | Both client and server verify each other's certificates | Zero-trust service-to-service auth; Istio automates this | Design | |
| Service Mesh | Infrastructure layer providing traffic management, mTLS, observability | Interviewers ask: "when would you add a mesh vs not?" | Design | |
| EKS (Elastic Kubernetes Service) | AWS managed K8s control plane; you manage nodes | Know: managed node groups vs Fargate vs Karpenter | Configure | |
| Fargate for EKS | Serverless node model; AWS manages node lifecycle per pod | No node management; limited for DaemonSets; cost tradeoff | Design | |
| Karpenter | Node autoprovisioner; replaces Cluster Autoscaler for EKS | Creates right-sized nodes just-in-time; spot integration | Configure | |
| Cluster Autoscaler | Scales node groups based on pending pods and underutilization | Older pattern; Karpenter preferred on EKS; know both | Configure | |
| eksctl | CLI tool to create/manage EKS clusters via CloudFormation | Your primary cluster lifecycle tool during training | Configure | |
| IRSA (IAM Roles for Service Accounts) | Binds AWS IAM role to K8s ServiceAccount via OIDC | Critical: eliminates EC2 instance profile credential sharing | Design | |
| Pod Security Admission (PSA) | Built-in admission controller enforcing Pod Security Standards | Replaced PSP (deprecated); know Privileged/Baseline/Restricted | Configure | |
| Pod Security Policy (PSP) | Deprecated cluster-wide policy for pod security constraints | Removed in K8s 1.25; PSA is the replacement | Know | |
| Container Runtime Interface (CRI) | Standard interface between kubelet and container runtime | containerd is default; Docker shim removed in 1.24 | Know | |
| containerd | Industry-standard container runtime used by most K8s distros | Know: crictl commands for debugging vs docker commands | Configure | |

---

## Domain 2: AWS Services

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| IAM (Identity and Access Management) | AWS service controlling who can do what to which AWS resources | Every AWS interview; know policies, roles, users, groups | Design | |
| IAM Policy | JSON document defining allowed/denied actions on resources | Know: identity-based vs resource-based; inline vs managed | Design | |
| IAM Role | AWS identity assumed by services, EC2, Lambda — no long-term keys | Foundation of least-privilege for AWS workloads | Design | |
| STS (Security Token Service) | Issues temporary credentials via AssumeRole API | Behind every IRSA, cross-account access, federated login | Design | |
| OIDC Provider | Trusted identity federation endpoint for IAM (e.g. EKS cluster) | Required to enable IRSA; ties K8s ServiceAccount to IAM Role | Design | |
| VPC (Virtual Private Cloud) | Isolated virtual network in AWS with your own IP address space | Know: subnets, route tables, IGW, NAT GW, VPC endpoints | Design | |
| Subnet (Public/Private) | Subdivisions of VPC CIDR; public has route to IGW, private does not | AZ-level HA: spread across 3 AZs minimum; EKS node placement | Design | |
| Internet Gateway (IGW) | Allows VPC resources to reach the public internet | Required for public subnets; not needed for private + NAT | Know | |
| NAT Gateway | Lets private subnet resources initiate outbound internet connections | Managed NAT; cost-driver — one per AZ for HA | Configure | |
| VPC Endpoint | Private connection to AWS services without traversing internet | Gateway endpoint (S3, DynamoDB free); Interface endpoint (cost) | Design | |
| Security Group | Stateful firewall rules attached to EC2, RDS, EKS node groups | Allow rules only; tracks connection state; Layer 4 | Configure | |
| Network ACL (NACL) | Stateless subnet-level firewall; rules evaluated in order | Know: stateless means you need both inbound + outbound rules | Know | |
| Route53 | AWS managed DNS service with health checks and routing policies | Failover, latency, weighted, geolocation routing policies | Configure | |
| ACM (Certificate Manager) | Manages SSL/TLS certs; auto-renews certs for AWS services | Free for AWS-managed services; used with ALB, CloudFront | Configure | |
| S3 (Simple Storage Service) | Object storage with 11 nines durability; buckets are global namespace | Versioning, lifecycle policies, bucket policies, replication | Configure | |
| S3 Bucket Policy | Resource-based IAM policy controlling access to S3 bucket | Block public access settings; cross-account access patterns | Design | |
| S3 Glacier | Long-term archival storage tier; retrieval takes minutes to hours | Lifecycle policy to move old logs; WORM compliance | Know | |
| EBS (Elastic Block Store) | Block storage attached to EC2/EKS nodes; zonal | gp3 default; io2 for high IOPS databases; know snapshot cost | Configure | |
| EFS (Elastic File System) | Managed NFS; multi-AZ shared filesystem for EKS RWX workloads | Used for shared config, ML datasets; more expensive than EBS | Configure | |
| ECR (Elastic Container Registry) | Managed Docker registry; integrated with EKS and IAM | Image scanning (Snyk integration), immutable tags, lifecycle | Configure | |
| EC2 (Elastic Compute Cloud) | Virtual machines in AWS; foundation of EKS node groups | Know instance families: compute/memory/storage optimized | Configure | |
| Auto Scaling Group (ASG) | Manages fleet of EC2 instances; integrates with EKS Cluster Autoscaler | Launch template, scaling policies, lifecycle hooks | Configure | |
| Launch Template | EC2 instance configuration template used by ASGs and EKS node groups | Replaces Launch Config; supports versioning | Configure | |
| ALB (Application Load Balancer) | L7 HTTP/HTTPS load balancer with path/host routing | AWS LB Controller creates ALBs from K8s Ingress objects | Configure | |
| NLB (Network Load Balancer) | L4 TCP/UDP load balancer; ultra-low latency, static IP | Used for non-HTTP workloads; EKS Service type=LoadBalancer | Configure | |
| CloudFront | CDN + DDoS protection (Shield Standard); edge caches content | WAF integration; Origins can be S3, ALB, API GW | Configure | |
| WAF (Web Application Firewall) | L7 rules blocking SQLi, XSS, rate limits at ALB/CloudFront | OWASP managed rule groups; custom rules via CDK/Terraform | Configure | |
| CloudWatch | AWS native monitoring: metrics, logs, alarms, dashboards | Know: metric math, composite alarms, CW Logs Insights queries | Configure | |
| CloudWatch Logs | Centralized log storage and query service for AWS workloads | Log groups, log streams, metric filters, retention policies | Configure | |
| CloudWatch Container Insights | Pre-built dashboards for EKS/ECS cluster metrics and logs | Node, pod, container metrics via ADOT/Fluent Bit | Configure | |
| AWS X-Ray | Distributed tracing service for AWS workloads | ADOT exports traces to X-Ray; know vs Jaeger/Zipkin | Know | |
| ADOT (AWS Distro for OpenTelemetry) | AWS-supported OTel collector with AWS-native backends | Your OTel-to-CloudWatch/X-Ray bridge in Week 5 labs | Configure | |
| RDS (Relational Database Service) | Managed MySQL/PostgreSQL/Oracle/SQL Server; automated backups | Multi-AZ for HA; Read Replicas for read scaling | Configure | |
| Aurora | AWS-proprietary MySQL/PostgreSQL-compatible distributed DB | 6-way replication, serverless v2, Global Database option | Know | |
| DynamoDB | Serverless NoSQL key-value and document DB; single-digit ms latency | Terraform remote state lock table; know on-demand vs provisioned | Configure | |
| ElastiCache | Managed Redis or Memcached; in-memory caching layer | Know: Redis cluster mode, eviction policies, AUTH tokens | Configure | |
| SQS (Simple Queue Service) | Managed message queue; at-least-once delivery | KEDA scales K8s pods on SQS queue depth — direct relevance | Configure | |
| SNS (Simple Notification Service) | Managed pub/sub messaging; fan-out to SQS, Lambda, HTTP | Know: SNS + SQS fan-out pattern for decoupling | Configure | |
| MSK (Managed Streaming for Kafka) | AWS managed Apache Kafka service | Know vs self-managed Kafka on EKS; IAM auth for MSK | Know | |
| Lambda | Serverless function; event-driven; max 15 min execution | Know: cold starts, memory/CPU correlation, Lambda@Edge | Know | |
| EventBridge | Serverless event bus; routes events between AWS services and SaaS | Replaces CloudWatch Events; rule-based routing to targets | Configure | |
| CloudTrail | Records all AWS API calls for audit and security analysis | Enabled by default 90 days; enable S3 trail for long-term audit | Configure | |
| Config (AWS Config) | Continuous compliance recorder; tracks resource config history | Config Rules + Conformance Packs; CSPM foundation on AWS | Configure | |
| GuardDuty | ML-based threat detection analyzing CloudTrail, VPC Flow, DNS logs | Findings: IAM credential theft, crypto mining, data exfiltration | Configure | |
| Security Hub | Aggregates findings from GuardDuty, Inspector, Macie, third-party | CSPM dashboard; integrates with SIEM; standards: CIS, FSBP | Configure | |
| Inspector | Automated vulnerability scanning for EC2 and container images | ECR image scanning in CI/CD pipeline; CVE prioritization | Configure | |
| Macie | ML-based PII/sensitive data discovery in S3 buckets | Compliance use case: find exposed PII before auditors do | Know | |
| KMS (Key Management Service) | Managed encryption key service; HSM-backed | Encrypt S3, EBS, Secrets Manager, etcd — know CMK vs AWS managed | Design | |
| Secrets Manager | Manages, rotates, and retrieves secrets; integrates with RDS | Preferred over SSM Parameter Store for secrets requiring rotation | Configure | |
| SSM Parameter Store | Hierarchical config and secrets store; SecureString uses KMS | Use for non-rotating config; Terraform reads via data source | Configure | |
| AWS Organizations | Manages multiple AWS accounts under one billing umbrella | SCPs restrict what accounts can do; used for account-level guardrails | Design | |
| SCP (Service Control Policy) | Max permission boundary for entire AWS accounts/OUs | Org-level guardrail; even Admins can't exceed SCP | Design | |
| Control Tower | Opinionated multi-account AWS setup with guardrails | Landing zone baseline; uses SCPs + Config rules | Know | |
| CloudFormation | AWS native IaC; JSON/YAML stacks | Know: drift detection, stack sets, change sets; Terraform competes here | Know | |
| CDK (Cloud Development Kit) | IaC using TypeScript/Python/Java; compiles to CloudFormation | Higher abstraction than raw CFN; constructs L1/L2/L3 | Know | |
| Terraform AWS Provider | HashiCorp-maintained provider for all AWS resource types | Your primary IaC tool for training; know provider versioning | Build | |
| Cost Explorer | Visualizes AWS cost and usage trends by service, tag, account | FinOps baseline; tag governance drives cost attribution | Configure | |
| Cost Allocation Tags | Key-value tags that appear in billing reports | Staff SRE must govern tagging strategy for cost attribution | Design | |
| Savings Plans | Flexible commitment discounts; applies across instance types | Compute Savings Plans most flexible; vs Reserved Instances | Know | |
| AWS Budgets | Alerts when cost or usage exceeds thresholds | Set $25 alert for training account; knows forecast alerts | Configure | |

---

## Domain 3: Azure Services

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| AKS (Azure Kubernetes Service) | Azure managed K8s; integrates with Entra ID and Azure Monitor | Many JDs mention AKS alongside EKS; know conceptual parallels | Know | |
| Azure Entra ID (AAD) | Microsoft's cloud identity provider; used for RBAC and SSO | OIDC federation for AKS similar to IRSA in EKS | Know | |
| Workload Identity (AKS) | Azure equivalent of IRSA; binds pod ServiceAccount to Azure identity | Replaces older pod-managed identity; key zero-trust pattern | Know | |
| Azure Container Registry (ACR) | Managed OCI registry; integrated with AKS and Azure DevOps | Geo-replication, image scanning; similar to ECR | Know | |
| Azure Monitor | Observability platform: metrics, logs, traces for Azure workloads | Container Insights for AKS; Log Analytics workspace backend | Know | |
| Log Analytics Workspace | Centralized log store for Azure Monitor using KQL query language | KQL syntax is different from SPL (Splunk); know the difference | Know | |
| Azure DevOps | Microsoft's CI/CD platform: Repos, Pipelines, Boards, Artifacts | Common in enterprises using Azure; Pipelines = GitHub Actions | Know | |
| Azure Pipelines | YAML-defined CI/CD; integrates with ACR, AKS, and Azure artifacts | Know: stages, jobs, steps pattern; similar to GitHub Actions | Know | |
| Azure Key Vault | Managed secrets, keys, and certificates service | CSI driver for K8s mounts Key Vault secrets as volumes | Know | |
| Azure Policy | Governance service enforcing compliance rules on Azure resources | Equivalent of AWS Config Rules + OPA for Azure resources | Know | |
| Defender for Cloud | CSPM + threat detection across Azure, AWS, GCP workloads | Multi-cloud security posture; replaces Azure Security Center | Know | |
| Azure Blob Storage | Object storage; equivalent to AWS S3 | Terraform remote state on Azure uses Blob Storage backend | Know | |
| Azure RBAC | Role assignments controlling access to Azure resources | Subscription, RG, resource scope; Built-in vs custom roles | Know | |
| Virtual Network (VNet) | Azure equivalent of AWS VPC; isolated network in Azure | Subnets, NSGs, peering; AKS nodes live in VNet | Know | |
| NSG (Network Security Group) | Azure L4 firewall rules for VNet subnets and NICs | Stateful; similar to AWS Security Group | Know | |
| ARM Templates | Azure native IaC in JSON; being replaced by Bicep | Know exists; Terraform Azure provider is more common in JDs | Know | |
| Bicep | Domain-specific language compiling to ARM templates | Microsoft-native IaC alternative to Terraform for Azure | Know | |
| Service Principal | Azure non-human identity for automation and CI/CD | Equivalent to AWS IAM Role; Terraform uses SP for auth | Know | |
| Managed Identity | Azure identity assigned to resources; no credential management | System-assigned vs user-assigned; equivalent to EC2 instance profile | Know | |

---

## Domain 4: Terraform & IaC

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| HCL (HashiCorp Configuration Language) | Declarative language used to write Terraform configs | Syntax: resource, data, variable, output, locals blocks | Configure | |
| Provider | Plugin that maps Terraform to a specific cloud/service API | Version pinning providers is required for production stability | Configure | |
| Resource | Terraform block declaring a real infrastructure object to manage | Core building block; every AWS/K8s object is a resource | Configure | |
| Data Source | Read-only query to fetch existing infrastructure state | Fetch existing VPC, AMI, SSM param without managing it | Configure | |
| Variable | Parameterizes a Terraform module; accepts input values | Type constraints, validation blocks, sensitive flag | Configure | |
| Output | Exposes values from a module or root config for use elsewhere | Cross-module data flow; remote_state reads outputs | Configure | |
| Locals | Named expressions computed within a module for reuse | Avoid repetition; DRY principle in HCL | Configure | |
| Module | Reusable package of Terraform resources with defined interface | Public registry modules vs internal; inputs/outputs contract | Design | |
| terraform init | Downloads providers and modules; initializes backend | First command in any workflow; idempotent | Configure | |
| terraform plan | Shows proposed changes without applying them | Dry run; pipe to file for apply; -out flag for GitOps | Configure | |
| terraform apply | Executes planned changes and updates state | Always plan before apply; use -auto-approve only in CI | Configure | |
| terraform destroy | Removes all resources tracked in state | Run at end of every training session to avoid cost | Configure | |
| terraform import | Brings existing resources under Terraform management | Know: imports resource into state, does not write config | Configure | |
| terraform state | Commands for inspecting and manipulating state file directly | mv, rm, list — use carefully; state is your source of truth | Design | |
| State File | JSON file recording every managed resource and its current config | Never edit manually; remote backend required for teams | Design | |
| Remote Backend | Stores state file in shared, durable storage (S3, TFC, GCS) | S3 + DynamoDB lock table is the standard AWS pattern | Configure | |
| State Locking | Prevents concurrent modifications to state during apply | DynamoDB provides the lock for S3 backend | Design | |
| State Drift | Difference between state file and actual infrastructure reality | Drift detection: terraform plan; fix with import or refresh | Design | |
| Workspace | Named state isolation within a single config directory | Use sparingly; modules + separate state files preferred at scale | Design | |
| terraform fmt | Formats code to canonical HCL style | Required in CI lint step; enforce in pre-commit hook | Configure | |
| terraform validate | Checks syntax and config validity without accessing APIs | Fast check in CI before plan; catches type errors | Configure | |
| terraform taint (deprecated) | Marked resource for forced replacement on next apply | Replaced by -replace flag: terraform apply -replace=aws_instance.x | Know | |
| -replace flag | Forces recreation of a specific resource on next apply | Current way to taint; know both old and new syntax | Configure | |
| count | Meta-argument to create multiple resource instances by number | Simple repetition; use for_each when keys matter for stability | Configure | |
| for_each | Meta-argument creating resources from a map or set | Preferred over count; resource addresses are stable | Configure | |
| dynamic block | Generates repeated nested blocks from a collection | Used for ingress rules, tags, policy statements | Configure | |
| depends_on | Explicit dependency when implicit graph doesn't capture it | Use sparingly; prefer implicit references | Configure | |
| lifecycle block | Controls create_before_destroy, prevent_destroy, ignore_changes | prevent_destroy for prod state buckets; ignore_changes for ASG | Design | |
| terraform graph | Outputs DOT-format dependency graph of resources | Debug dependency order; visualize with Graphviz | Know | |
| Sentinel | HashiCorp policy-as-code for Terraform Enterprise/Cloud | Enforces compliance before apply in enterprise TFC | Know | |
| OPA with Terraform | Open Policy Agent evaluating terraform plan JSON output | conftest tool; enforcement in CI pipeline | Design | |
| Checkov | SAST tool scanning Terraform/CloudFormation for misconfigs | Integrates into CI; checks CIS benchmarks, HIPAA, PCI | Configure | |
| tfsec | Static analysis tool scanning Terraform for security issues | Similar to Checkov; often run alongside in CI | Configure | |
| Terragrunt | Thin wrapper adding DRY remote state config and dependencies | Popular in large multi-account orgs; generates backend configs | Design | |
| Terraform Cloud (TFC) | HashiCorp-managed collaborative Terraform platform | Remote runs, VCS integration, policy enforcement, cost estimate | Know | |
| Terraform Registry | Public/private catalog of modules and providers | Public modules: quick start; always pin module versions | Configure | |
| atlantis | Self-hosted GitOps-style Terraform PR automation | PRs trigger plan; merge triggers apply; comments in PR | Design | |
| CDK for Terraform (CDKTF) | IaC using Python/TS/Java that synthesizes to Terraform JSON | Higher abstraction; emerging pattern; know vs Pulumi | Know | |
| Pulumi | IaC using full programming languages (Python, TS, Go) | True imperative IaC; state in Pulumi Cloud or self-hosted | Know | |
| drift detection | Identifying when actual infrastructure diverges from desired state | terraform plan output; automated via scheduled pipelines | Design | |
| immutable infrastructure | Pattern of replacing resources rather than patching them in place | create_before_destroy enables this; blue-green uses it | Design | |
| GitOps for IaC | Storing all IaC in Git; apply only triggered from Git events | atlantis, Spacelift, TFC VCS integration implement this | Design | |

---

## Domain 5: DevSecOps & Supply Chain Security

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| SAST (Static Application Security Testing) | Analyzes source code for vulnerabilities without executing it | Semgrep, Checkmarx, Snyk Code; runs in CI on every PR | Configure | |
| DAST (Dynamic Application Security Testing) | Tests running application by sending attack traffic | OWASP ZAP, Burp Suite; runs against staging environment | Know | |
| SCA (Software Composition Analysis) | Identifies vulnerabilities in open-source dependencies | Snyk, Dependabot, OWASP Dependency-Check; SBOM generators | Configure | |
| SBOM (Software Bill of Materials) | Machine-readable inventory of all components in a software artifact | SPDX or CycloneDX format; EO 14028 requires SBOM for federal | Design | |
| SPDX | Linux Foundation open standard for SBOM interchange format | ISO 5962 standard; generated by syft, Trivy, Snyk | Know | |
| CycloneDX | OWASP SBOM standard; lighter than SPDX; tool-friendly JSON/XML | Generated by syft, cdxgen; supports VEX (vuln exploitability) | Know | |
| Syft | CLI tool generating SBOM from container images and filesystems | Generate SBOM in CI; pair with Grype for vuln matching | Configure | |
| Grype | CLI vulnerability scanner consuming SBOMs or scanning images directly | Pair with syft; integrates into CI gates | Configure | |
| Trivy | All-in-one scanner: CVEs, misconfigs, secrets, SBOM in images/repos | Most popular in K8s; built into many CI platforms | Configure | |
| Snyk | Commercial SCA + container + IaC scanner with developer UX | Common in JDs; free tier for open-source; CI plugin | Configure | |
| CVE (Common Vulnerabilities and Exposures) | Unique identifier for known security vulnerabilities | Know: CVSS score, severity tiers; base vs exploitability | Know | |
| CVSS (Common Vulnerability Scoring System) | 0-10 numerical scoring of vulnerability severity | v3.1 standard; base score ≠ environmental score | Know | |
| Sigstore | Keyless code signing ecosystem using OIDC and transparency logs | Cosign + Fulcio + Rekor; supply chain signing standard | Design | |
| Cosign | CLI tool for signing and verifying container images (Sigstore) | Sign in CI; verify at admission webhook before deploy | Configure | |
| Fulcio | Sigstore CA issuing short-lived certs tied to OIDC identity | No long-term key management; certificate is the signature | Know | |
| Rekor | Sigstore immutable transparency log for signed artifacts | Append-only ledger; verify signature provenance offline | Know | |
| SLSA (Supply chain Levels for Software Artifacts) | Framework of four levels for supply chain security hardening | L1: provenance; L2: hosted build; L3: hardened; L4: two-party | Design | |
| Provenance | Signed metadata describing how, where, and by whom artifact was built | SLSA requirement; generated by GitHub Actions OIDC + slsa-github-generator | Design | |
| in-toto | Framework for supply chain policy and step attestations | SLSA builds on in-toto attestation format | Know | |
| OWASP Top 10 | Ten most critical web application security risks | Interviewers assume you know A01–A10; A03 injection most common | Know | |
| OWASP A03 (Injection) | SQL/NoSQL/command injection from untrusted input | Most common critical finding in app security reviews | Know | |
| OWASP A05 (Security Misconfiguration) | Default credentials, open S3 buckets, missing security headers | Terraform/K8s misconfiguration scanning catches this | Know | |
| OWASP A09 (Security Logging Failures) | Missing audit logs makes breach detection impossible | SRE relevance: structured logging + SIEM coverage | Know | |
| Policy as Code | Expressing compliance rules as machine-executable code | OPA Rego, Kyverno YAML, Sentinel HCL — all policy as code | Design | |
| OPA (Open Policy Agent) | General-purpose policy engine using Rego language | K8s admission, Terraform plan, API authz — one engine | Design | |
| Rego | OPA's query language for writing policies | Know: allow rules, deny rules, violation rules; structural style | Build | |
| conftest | CLI running OPA/Rego policies against structured config files | Test Terraform plans, K8s manifests, Dockerfiles in CI | Configure | |
| Gatekeeper | OPA-based K8s admission controller using ConstraintTemplates | ConstraintTemplate (Rego) + Constraint (config) pattern | Design | |
| ConstraintTemplate | CRD defining a policy in Rego; generates a new CRD type | One template = one policy class; parameterized per Constraint | Build | |
| Kyverno Policy | K8s-native policy written as K8s YAML resource | Mutate, Validate, Generate, Verify Image policy types | Configure | |
| Secrets Scanning | Detecting hardcoded credentials in source code or git history | detect-secrets, truffleHog, gitleaks, GitHub secret scanning | Configure | |
| gitleaks | Open-source tool scanning git repos for secrets | Pre-commit hook + CI gate; configurable rule patterns | Configure | |
| detect-secrets | Yelp's tool detecting secrets using entropy and pattern matching | Used as pre-commit hook; baseline file for suppressing FPs | Configure | |
| truffleHog | Deep git history scanner finding high-entropy strings and patterns | Use for one-time audit of full repo history | Know | |
| DORA Metrics | Four metrics: deployment frequency, lead time, MTTR, change fail rate | Google DevOps research; interviewers ask you to define all four | Design | |
| Deployment Frequency | How often code is deployed to production per time period | Elite: multiple per day; High: weekly; Medium: monthly | Know | |
| Lead Time for Changes | Time from commit to production deployment | Measures CI/CD pipeline efficiency; target: <1 hour for elite | Know | |
| Change Failure Rate | Percentage of deployments causing production incidents | Target <5% for elite; tracked in incident system | Know | |
| MTTR (Mean Time to Restore) | Average time to restore service after a production failure | Key SRE metric; ties to on-call, runbooks, automation | Design | |
| Shift Left Security | Moving security checks earlier in SDLC (IDE → PR → CI) | Core DevSecOps principle; reduces cost of fixing vulns | Design | |
| IaC Scanning | Static analysis of Terraform/CloudFormation for security misconfigs | Checkov, tfsec, Snyk IaC; runs in CI alongside SAST | Configure | |
| Container Image Scanning | CVE + misconfiguration scan of Docker image layers | Trivy, Snyk, ECR native scanning; part of CI pipeline gate | Configure | |
| Binary Authorization | Google/GKE policy requiring signed images before deploy | Equivalent: Kyverno verifyImages or Cosign + admission webhook | Know | |
| Admission Webhook for Policy | Validates every K8s resource against security policies before creation | Gatekeeper and Kyverno both implement via this mechanism | Design | |
| VEX (Vulnerability Exploitability eXchange) | Document stating whether CVE is exploitable in your specific context | Reduces alert fatigue; CycloneDX supports VEX in SBOM | Know | |
| CSPM (Cloud Security Posture Management) | Continuous compliance checking of cloud resource configurations | Prisma Cloud, Wiz, Defender for Cloud, AWS Security Hub | Design | |
| Wiz | Agentless CSPM + CWPP scanning cloud environments via APIs | Very common in JDs 2024-2026; know: graph-based risk correlation | Know | |
| Prisma Cloud | Palo Alto CSPM + runtime protection for cloud and containers | Common in enterprise; covers IaC scan, CSPM, CWPP, DSPM | Know | |
| CWPP (Cloud Workload Protection Platform) | Runtime security for containers and VMs | Falco is open-source CWPP; pairs with CSPM | Know | |
| Falco | Open-source runtime security using eBPF syscall monitoring | K8s threat detection; rules alert on unexpected syscalls | Configure | |
| eBPF (Extended Berkeley Packet Filter) | Kernel-level programmable hooks for networking and security | Powers Cilium, Falco, Pixie; no kernel module needed | Know | |
| Zero Trust | Security model: never trust, always verify; least-privilege everywhere | mTLS, RBAC, network policy, IRSA all implement zero-trust | Design | |
| Least Privilege | Grant only permissions needed; revoke when not needed | IAM policy design principle; audited by Access Analyzer | Design | |
| AWS IAM Access Analyzer | Identifies overly permissive policies and external access | Generates least-privilege policy recommendations | Configure | |

---

## Domain 6: CI/CD & Pipeline Security

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| CI (Continuous Integration) | Automatically build and test code on every commit | Every JD assumes CI exists; know trigger events and gates | Configure | |
| CD (Continuous Delivery) | Automated pipeline to production-ready state; deploy on demand | Delivery = ready to deploy; Deployment = auto-deploys | Know | |
| CD (Continuous Deployment) | Every passing build automatically deploys to production | Know: CD Delivery vs CD Deployment distinction | Know | |
| Pipeline as Code | CI/CD pipeline defined in version-controlled YAML/HCL/Groovy | Jenkinsfile, .github/workflows, .gitlab-ci.yml | Configure | |
| GitHub Actions | GitHub's native CI/CD platform using YAML workflow files | Triggers: push, PR, schedule, workflow_dispatch; OIDC for AWS | Configure | |
| GitHub Actions OIDC | Keyless AWS auth in Actions using JWT; no stored secrets | Best practice for AWS credential management in GitHub CI | Design | |
| GitLab CI | GitLab's CI/CD with .gitlab-ci.yml; stages, jobs, runners | Runner registration, shared vs project runners, caching | Configure | |
| Jenkins | Self-hosted CI/CD with Groovy pipelines; very common legacy | Shared libraries, multibranch pipeline, Jenkinsfile | Configure | |
| Jenkinsfile | Groovy DSL defining Jenkins pipeline; stored in repo root | Declarative (preferred) vs scripted pipeline syntax | Configure | |
| ArgoCD | GitOps CD controller for K8s; syncs cluster to Git repo state | Pull model; App of Apps pattern; health status tracking | Design | |
| Argo Rollouts | Progressive delivery controller: canary, blue-green, analysis | Integrates with Prometheus for automated rollback | Design | |
| Flux | CNCF GitOps toolkit for K8s; pull-based CD | HelmRelease, Kustomization CRDs; multi-tenancy via GitRepository | Design | |
| GitOps | Operations model using Git as single source of truth for infra | Declarative, versioned, auditable; ArgoCD/Flux implement it | Design | |
| Pull-based GitOps | Agent in cluster pulls desired state from Git; cluster initiates | More secure than push-based; no external push access needed | Design | |
| Push-based GitOps | External CI pipeline pushes changes directly to cluster | Less secure; kubectl apply from CI; legacy pattern | Know | |
| Blue-Green Deployment | Two identical environments; switch traffic between them | Zero-downtime; instant rollback; double the resource cost | Design | |
| Canary Deployment | Route small % of traffic to new version; gradually increase | Argo Rollouts automates; Istio/Flagger enable traffic splitting | Design | |
| Rolling Update | Replace pods incrementally; default K8s Deployment strategy | maxSurge, maxUnavailable params control rollout speed | Configure | |
| Feature Flags / Toggles | Runtime switches to enable/disable features without deploying | LaunchDarkly, Flagsmith; decouple deploy from release | Know | |
| Branch Protection | GitHub/GitLab rules requiring PR reviews and CI pass before merge | Required status checks; signed commits; linear history | Configure | |
| CODEOWNERS | File mapping directories to required reviewers in GitHub/GitLab | Enforce security team review on infra/policy changes | Configure | |
| Signed Commits | Git commits with GPG/SSH signature proving author identity | Required in secure supply chains; GitHub shows Verified badge | Configure | |
| Dependency Update Automation | Automated PRs for dependency upgrades (Renovate, Dependabot) | Reduces CVE exposure lag; know merge strategy options | Configure | |
| Renovate | Dependency update bot with flexible batching and scheduling | More configurable than Dependabot; mono-repo aware | Configure | |
| Dependabot | GitHub-native dependency update and security alert tool | Auto-PRs for package upgrades; security alerts on CVEs | Configure | |
| Pipeline Gate | CI step that fails the pipeline when quality/security check fails | Must-fail on critical CVE, failed SAST, missing SBOM | Design | |
| Artifact Registry | Versioned storage for build artifacts: jars, images, Helm charts | ECR, GCR, Nexus, Artifactory; immutable artifacts required | Configure | |
| Immutable Artifacts | Build once; same artifact promoted through all environments | No rebuilds per env; Cosign signs the artifact digest | Design | |
| Pre-commit Hooks | Local Git hooks running checks before commit is created | gitleaks, terraform fmt, detect-secrets; enforced via pre-commit tool | Configure | |
| pre-commit (tool) | Framework managing and installing pre-commit hook scripts | .pre-commit-config.yaml; hooks run on changed files only | Configure | |
| Hermetic Build | Build fully isolated with pinned deps; reproducible bit-for-bit | SLSA L2+ requirement; no internet access during build | Know | |
| Build Provenance | Signed attestation of what built an artifact and from what source | GitHub Actions OIDC + slsa-github-generator produces this | Design | |
| SLSA Build Levels | L1: signed provenance; L2: hosted builder; L3: tamper-resistant | Each level adds supply chain trust; L3 recommended for production | Design | |
| Tekton | K8s-native CI/CD pipeline framework using CRDs | Cloud-native CI in cluster; used in some GitOps platforms | Know | |
| Spinnaker | Netflix-originated CD platform for cloud deployments | Legacy enterprise use; complex; mostly replaced by ArgoCD | Know | |
| Semantic Versioning | MAJOR.MINOR.PATCH versioning with defined bump rules | Every release artifact should follow semver; automate via CI | Configure | |
| Container Image Tag Immutability | Tag once; never overwrite same tag with different image | ECR and Docker Hub support immutable tags; enforce in policy | Design | |

---

## Domain 7: Observability & Telemetry

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| Observability | Ability to understand internal system state from external outputs | Three pillars: metrics, logs, traces (MELT includes events) | Design | |
| MELT | Metrics, Events, Logs, Traces — four observability signal types | More complete than "three pillars"; events often missed | Design | |
| Metrics | Numeric measurements aggregated over time (counters, gauges, histograms) | Prometheus format; OTLP export; cardinality is the cost driver | Design | |
| Logs | Timestamped text or structured records of discrete events | Structured > unstructured; JSON logs for machine parsing | Configure | |
| Traces | End-to-end records of request paths across distributed services | Spans + context propagation; W3C TraceContext header standard | Design | |
| Events | Discrete occurrences with rich context; between logs and metrics | OTel semantic conventions define event structure | Know | |
| Span | Single unit of work in a distributed trace with start/end timestamps | Parent-child relationships form a trace tree | Know | |
| Trace Context | Headers propagating trace ID and span ID across service calls | W3C traceparent/tracestate headers are the standard | Design | |
| OpenTelemetry (OTel) | CNCF standard for instrumentation, collection, and export of signals | Vendor-neutral; SDK + Collector + Protocol (OTLP) | Design | |
| OTLP (OpenTelemetry Protocol) | Wire protocol for sending OTel signals to backends | gRPC and HTTP/Protobuf; replace all vendor-specific agents | Design | |
| OTel Collector | Vendor-neutral agent/gateway receiving, processing, and exporting signals | Receiver → Processor → Exporter pipeline; deploy as DaemonSet or sidecar | Configure | |
| OTel SDK | Language library for auto or manual instrumentation of apps | Java agent, Python SDK, Go SDK; auto-instrumentation preferred | Configure | |
| Auto-instrumentation | OTel SDK capturing traces/metrics automatically via bytecode injection | Java agent, Node.js require hook; no code changes needed | Configure | |
| Prometheus | Pull-based metrics system with PromQL query language | De facto K8s metrics standard; /metrics endpoint scraping | Configure | |
| PromQL | Prometheus query language for metric selection and aggregation | rate(), increase(), histogram_quantile() — know these functions | Configure | |
| Alertmanager | Prometheus component routing alerts to PagerDuty, Slack, email | Inhibition, silences, grouping; know routing tree structure | Configure | |
| Grafana | Visualization platform for metrics, logs, traces from multiple sources | Dashboards, alerting, Loki integration; panels and variables | Configure | |
| Loki | Grafana's log aggregation system indexed by labels only | Very cost-efficient; query with LogQL; pairs with Promtail | Configure | |
| Tempo | Grafana's distributed tracing backend; uses object storage | Completes the Grafana LGTM stack (Loki, Grafana, Tempo, Mimir) | Know | |
| Mimir | Grafana's horizontally scalable Prometheus backend | Long-term metric storage; multi-tenant; replaces Cortex/Thanos | Know | |
| Thanos | HA and long-term storage extension for Prometheus | Sidecar model vs Receiver model; object store backend | Know | |
| Jaeger | Open-source distributed tracing system (CNCF) | Older tracing backend; being replaced by OTel-native backends | Know | |
| Zipkin | Twitter-originated distributed tracing; predates OTel | Legacy; know exists; B3 propagation headers | Know | |
| Splunk | Enterprise log management, SIEM, and observability platform | Your expert domain; SPL, MART, MLTK, dashboards | Design | |
| SPL (Splunk Processing Language) | Splunk's search and analytics query language | Your strongest observability tool; search, stats, eval, rex | Design | |
| SLI (Service Level Indicator) | Specific metric measuring user-visible service behavior | Request success rate, latency P99, throughput — quantified | Design | |
| SLO (Service Level Objective) | Target threshold for an SLI over a time window | "99.9% requests < 200ms over 30 days" — be this specific | Design | |
| SLA (Service Level Agreement) | Contractual commitment to customers; SLO with consequences | SLOs internal; SLAs external; SLO should be tighter than SLA | Design | |
| Error Budget | Amount of allowable unreliability before SLO is violated | 100% − SLO target over window; budget remaining = headroom | Design | |
| Error Budget Burn Rate | How fast you're consuming error budget vs the allowed rate | 1x = exact pace; >1x = consuming faster than allowed | Design | |
| Burn Rate Alert | Fires when error budget depletes faster than allowed threshold | Multiwindow alerts: fast burn (1hr/5min) + slow burn (6hr/30min) | Build | |
| Alerting on Burn Rate | Alerting on rate of SLO violation rather than raw thresholds | Dramatically reduces alert noise vs threshold-based alerting | Design | |
| Toil | Repetitive, manual, automatable work with no enduring value | Keeping toil <50% of SRE time is a team health metric | Design | |
| Four Golden Signals | Latency, Traffic, Errors, Saturation — Google's SRE monitoring framework | Universal alert coverage; USE/RED are derived from these | Design | |
| USE Method | Utilization, Saturation, Errors — for resource-level monitoring | Brendan Gregg; apply to CPU, disk, network interfaces | Design | |
| RED Method | Rate, Errors, Duration — for service-level monitoring | Weaveworks pattern; apply to microservices and APIs | Design | |
| Cardinality | Number of unique label value combinations in a metric | High cardinality (user ID in labels) explodes Prometheus storage | Design | |
| Histogram | Metric type bucketing observations for percentile calculation | histogram_quantile(0.99,...) — the right way to measure P99 | Design | |
| Summary | Metric type computing quantiles client-side; not aggregatable | Avoid in distributed systems; histogram is preferred | Know | |
| P50/P95/P99 Latency | Percentile latency: 50th/95th/99th percent of requests | P99 = worst experience for 1 in 100 users; alert on P99 | Design | |
| Exemplar | Sample trace linked to a specific metric data point | Connects a high-latency metric spike to the specific trace | Know | |
| Structured Logging | Logs as key-value pairs (JSON) rather than free-form text | Enables log parsing, filtering, and metric extraction | Configure | |
| Log Correlation | Linking logs, metrics, and traces via shared trace/span ID | Inject trace_id into all log records for drill-down | Design | |
| Fluent Bit | Lightweight log forwarder; common K8s DaemonSet | EKS → CloudWatch Logs via Fluent Bit DaemonSet | Configure | |
| Fluentd | Heavier log collector/aggregator; more plugin ecosystem | Often replaced by Fluent Bit for resource efficiency | Know | |
| OpenMetrics | Standard extending Prometheus exposition format | Emerging standard; OTel ingests OpenMetrics | Know | |
| ADOT (AWS Distro for OpenTelemetry) | AWS-supported OTel distribution for AWS backends | X-Ray, CloudWatch, AMP — all reachable via ADOT | Configure | |
| AMP (Amazon Managed Prometheus) | AWS managed Prometheus-compatible metrics backend | Remote write from self-managed Prometheus to AMP | Configure | |
| AMG (Amazon Managed Grafana) | AWS managed Grafana workspace with AWS SSO integration | Visualize AMP, CloudWatch, X-Ray in one place | Configure | |
| SLO as Code | Defining SLOs in version-controlled YAML/configuration | OpenSLO spec; Nobl9, Sloth, slok/sloth for Prometheus | Design | |
| Nobl9 | SLO management platform with multi-source metric integration | Manages SLOs across Prometheus, Datadog, Splunk | Know | |
| Datadog | Commercial APM, metrics, logs, security in one platform | Common competitor to Splunk; agent-based; APM tracing | Know | |
| New Relic | Commercial observability platform with full-stack coverage | Know: NRQL query language exists; similar tier to Datadog | Know | |
| Dynatrace | Commercial observability with AI-driven automatic baselining | Davis AI engine; similar tier to Datadog in enterprise | Know | |
| AppDynamics | Cisco APM platform; your existing expertise | Business transactions, JVM agent, flow maps | Design | |

---

## Domain 8: SRE Fundamentals

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| SRE (Site Reliability Engineering) | Engineering discipline applying software practices to operations | Your career; know Google SRE book chapter structure | Design | |
| Reliability | Probability a system performs its function for a specified period | Quantified via SLOs; not "up/down" binary | Design | |
| Availability | Percentage of time a system is operational and serving traffic | 99.9% = 8.7 hrs/yr downtime; 99.99% = 52 min/yr | Design | |
| Incident | Unplanned disruption or degradation of service quality | P1/P2 severity tiers; know your incident criteria | Design | |
| Incident Command System (ICS) | Structured roles: IC, comms lead, ops lead, scribe during P1 | Your lived experience; formalize with NIMS ICS terminology | Design | |
| Incident Commander (IC) | Single decision-maker coordinating all incident response tracks | No technical work by IC; delegates and drives resolution | Design | |
| Blameless Postmortem | Structured analysis of incident focusing on systems, not people | Timeline, contributing factors, action items; no blame | Design | |
| Timeline (postmortem) | Chronological sequence of events during an incident | Detection → Response → Mitigation → Resolution sequence | Design | |
| Contributing Factor | System or process condition that enabled the incident | Not root cause (singular); systems have multiple factors | Design | |
| Action Items (postmortem) | Concrete improvements with owner and due date | Must be SMART; tracked in Jira/ServiceNow; reviewed next PI | Design | |
| On-Call Rotation | Scheduled engineer responsibility for incident response | Rotation fairness, escalation policy, runbook coverage | Design | |
| Runbook | Step-by-step procedure for common operational tasks | Automating runbooks reduces toil; link from alert bodies | Design | |
| Runbook Automation | Converting manual runbook steps into executable code/API calls | Reduces MTTR; Ansible, Python scripts, AWS SSM documents | Design | |
| MTTD (Mean Time to Detect) | Average time from incident start to first alert firing | Reduced by better SLO alerting and synthetic monitoring | Design | |
| MTTR (Mean Time to Restore) | Average time from detection to service restoration | Reduced by runbooks, automation, blameless practice | Design | |
| MTTF (Mean Time to Failure) | Average operating time between failures | Reliability metric; MTBF (between failures) is equivalent | Know | |
| MTBF (Mean Time Between Failures) | Average time from one failure recovery to next failure start | Higher is better; improved by reliability engineering | Know | |
| Change Management | Process controlling production changes to reduce risk | CAB, change freeze, rollback plan requirements | Design | |
| Change Failure Rate | % of deployments requiring emergency fix or rollback | DORA metric; target <5% for elite organizations | Design | |
| Deployment Frequency | How often production deployments occur | DORA metric; proxy for engineering velocity | Know | |
| Lead Time for Changes | Time from code commit to code running in production | Measures CI/CD pipeline efficiency | Know | |
| Chaos Engineering | Deliberately injecting failures to find weaknesses proactively | Chaos Monkey, LitmusChaos, Gremlin; Game Days | Design | |
| Game Day | Structured exercise simulating failures to test readiness | Planned; involves full response team; validates runbooks | Design | |
| LitmusChaos | CNCF chaos engineering platform for K8s | ChaosExperiments as CRDs; pod kill, node drain experiments | Configure | |
| Synthetic Monitoring | Scripted transactions probing production endpoints continuously | Detects issues before users; Checkly, Datadog Synthetics | Configure | |
| Real User Monitoring (RUM) | Capturing actual user browser/app performance metrics | Complements synthetic; shows geographic and device variation | Know | |
| Capacity Planning | Forecasting future resource needs to prevent saturation | DBRM: demand, baseline, resource, model — structured approach | Design | |
| Saturation | Metric showing how "full" a resource is; queue depth building | Key golden signal; CPU saturation ≠ CPU utilization | Design | |
| Toil | Manual, repetitive, automatable work scaling with load | Google SRE target: <50% toil; track and report quarterly | Design | |
| Error Budget Policy | Document defining consequences and actions at error budget thresholds | When budget is at 50%: caution; at 0%: freeze features | Design | |
| SLO Window | Time period over which SLO compliance is measured | Rolling 30-day window most common; calendar windows simpler | Design | |
| Alerting Philosophy | Principle that alerts should be actionable, not informational | Alert on SLO burn rate; not raw thresholds | Design | |
| Reliability Roadmap | Planned improvements to system reliability prioritized by impact | Backed by postmortem action items and toil reduction | Design | |
| Graceful Degradation | System continues serving reduced functionality during partial failure | Feature flags, circuit breakers, fallback responses | Design | |
| Circuit Breaker | Stops calling a failing dependency; returns fallback immediately | Resilience4j, Hystrix patterns; prevents cascade failures | Design | |
| Bulkhead Pattern | Isolates failures in one component from cascading to others | Thread pool isolation; K8s namespace resource quotas | Design | |
| Retry with Backoff | Retrying failed calls with exponential delay and jitter | Prevents thundering herd on recovery; always add jitter | Design | |
| Thundering Herd | Burst of concurrent requests overwhelming a recovering service | Caused by cache miss + retry storm; jitter prevents it | Design | |
| Backpressure | Mechanism to slow producers when consumers are overwhelmed | RabbitMQ prefetch, Kafka consumer pause, queue depth limits | Design | |
| Rate Limiting | Caps requests per time window to protect service capacity | Token bucket algorithm; implemented at gateway/LB layer | Configure | |
| Timeout | Maximum wait time before abandoning a downstream call | Set timeouts shorter than upstream timeout (Hystrix-style) | Configure | |
| Dead Letter Queue (DLQ) | Queue receiving messages that failed all retry attempts | RabbitMQ dead letter exchange; SQS DLQ; investigate and replay | Configure | |
| Observability vs Monitoring | Monitoring checks known states; observability explores unknown states | Key distinction interviewers probe at Staff level | Design | |
| Cognitive Load | Mental effort required to operate a system | High cognitive load causes incidents; SRE reduces it | Know | |
| SRE Team Topologies | Embedded, consulting, enabling, platform SRE models | Know which model your team is; tradeoffs of each | Design | |

---

## Domain 9: Platform Engineering

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| Platform Engineering | Building internal products (IDPs) that let developers self-serve infra | Emerging discipline; replaces "DevOps team as gatekeeper" | Design | |
| IDP (Internal Developer Platform) | Self-service portal and toolchain for developers to deploy and operate apps | Backstage is the most common IDP foundation | Design | |
| Backstage | CNCF open-source framework for building developer portals | Software catalog + scaffolding + plugins; Spotify origin | Design | |
| Software Catalog (Backstage) | Registry of all services, libraries, APIs with ownership metadata | catalog-info.yaml in every repo; discovery + ownership | Design | |
| Golden Path | Opinionated, supported way to build and deploy a specific workload type | Reduces cognitive load; not mandated but well-maintained | Design | |
| Scaffolding | Template-based generation of new service with all standards built in | Backstage Software Templates; cookiecutter; copier | Configure | |
| Software Templates (Backstage) | Parameterized templates creating repos with golden path built in | Actions: fetch:template, publish:github, catalog:register | Configure | |
| TechDocs | Backstage plugin rendering Markdown docs alongside service catalog | Docs-as-code; MkDocs backend; in-portal documentation | Configure | |
| Crossplane | K8s-based universal control plane for provisioning cloud resources | Composition + CompositeResourceDefinition; GitOps for infra | Design | |
| Composition (Crossplane) | Crossplane resource combining managed resources into one abstraction | Developer requests an "App"; Crossplane creates RDS + S3 + IAM | Design | |
| KubeVela | OAM-based application platform for K8s; appfile-centric | Open Application Model standard; alternative to Crossplane | Know | |
| Flux + Helm + Kustomize | Standard GitOps toolchain for platform teams managing many clusters | Layered approach: Flux syncs, Kustomize overlays, Helm charts | Design | |
| App of Apps (ArgoCD) | Root ArgoCD Application managing all other ArgoCD Applications | Bootstrap pattern for managing many apps from one ArgoCD repo | Design | |
| ApplicationSet (ArgoCD) | Generates multiple ArgoCD Applications from templates and generators | Matrix, list, git, cluster generators; multi-cluster deployments | Design | |
| GitOps Tenancy | Pattern giving each team their own Git path managed by platform | Namespace-per-team; Flux tenancy; Kyverno policies enforce | Design | |
| Multi-Tenancy | Safely running multiple teams/workloads on shared K8s clusters | Namespace isolation, RBAC, NetworkPolicy, quotas, LimitRange | Design | |
| Cluster Fleet Management | Operating and governing many K8s clusters at scale | ACM, Fleet, ArgoCD multi-cluster; upgrade orchestration | Design | |
| ACM (Advanced Cluster Management) | Red Hat tool for managing fleet of K8s clusters | Policy propagation, lifecycle, observability across clusters | Know | |
| Cluster API | K8s-native way to provision and lifecycle-manage K8s clusters | CAPI providers: AWS CAPI, Azure CAPI; clusters as CRDs | Know | |
| Service Level (Platform) | Contractual reliability commitment the platform team offers developers | Platform SLOs: pipeline success rate, provisioning time P95 | Design | |
| Paved Road | Similar to golden path; the well-maintained, easy-to-follow route | Reduce cognitive load; dev teams opt-in not forced | Know | |
| Developer Experience (DevEx) | Quality of the tools and processes developers use daily | Measured by SPACE framework; platform team's primary metric | Design | |
| SPACE Framework | Satisfaction, Performance, Activity, Communication, Efficiency — DevEx | GitHub research; replaces lines-of-code productivity metrics | Know | |
| Cognitive Load (Platform) | Mental overhead placed on developers by platform complexity | Platform engineering goal: reduce developer cognitive load | Design | |
| Onboarding Time | Time for a new developer to first production deployment | Key platform metric; golden path reduces this dramatically | Know | |
| SLA to Developers | Platform team commitment: provisioning, pipeline, uptime guarantees | Treat developers as customers; define and measure | Design | |
| FinOps in Platform | Platform team embedding cost awareness into developer workflows | Show cost per namespace/team; chargeback/showback models | Design | |
| Chargeback | Billing teams for actual cloud resource usage | Finance integration; requires tag governance | Know | |
| Showback | Showing teams their costs without actually charging them | First step before chargeback; changes behavior | Know | |
| Port | Commercial IDP platform alternative to Backstage | SaaS option; faster time to value; less flexible | Know | |
| Cortex | Commercial service catalog and developer portal | Competing with Backstage; scorecard-based maturity tracking | Know | |

---

## Domain 10: Networking & Security

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| OSI Model | Seven-layer network model: Physical, Data, Network, Transport, Session, Presentation, Application | L4 = TCP; L7 = HTTP; know which layer controls what | Know | |
| TCP/IP | Fundamental internet protocol suite; connection-oriented reliable transport | Three-way handshake; SYN, SYN-ACK, ACK | Know | |
| UDP | Connectionless transport protocol; no guaranteed delivery | DNS, QUIC, video streaming; lower latency than TCP | Know | |
| DNS | Translates domain names to IP addresses | A, CNAME, MX, TXT records; TTL; Route53 in AWS | Configure | |
| CIDR | IP address range notation: base address + prefix length | /16 = 65K IPs; /24 = 256 IPs; VPC and subnet sizing | Configure | |
| BGP (Border Gateway Protocol) | Internet routing protocol exchanging paths between networks | AWS Direct Connect, Transit Gateway use BGP | Know | |
| TLS (Transport Layer Security) | Cryptographic protocol securing network communications | TLS 1.3 preferred; certificate chain, cipher suites | Design | |
| mTLS (Mutual TLS) | Both sides present and verify certificates; stronger than TLS | Service mesh zero-trust; Istio automates cert management | Design | |
| PKI (Public Key Infrastructure) | System for managing digital certificates and keys | CA hierarchy: root → intermediate → leaf certs | Design | |
| X.509 Certificate | Standard format for public key certificate with identity | Common Name, SAN, validity period, issuing CA | Know | |
| JWT (JSON Web Token) | Compact signed token for identity and claims passing | Header.Payload.Signature; verify signature, check expiry | Configure | |
| OAuth 2.0 | Authorization delegation framework for API access | Authorization Code flow, Client Credentials flow | Know | |
| OIDC (OpenID Connect) | Identity layer on top of OAuth 2.0; adds user identity | ID token + access token; used in IRSA, GitHub Actions | Design | |
| SAML 2.0 | XML-based federation protocol for enterprise SSO | Older than OIDC; used in enterprise identity providers | Know | |
| Zero Trust Network | No implicit trust based on network location; always authenticate | BeyondCorp model; verify every request, device, user | Design | |
| Service Mesh | Infrastructure managing mTLS, traffic policy, observability at L7 | Istio, Linkerd; sidecar or eBPF implementations | Design | |
| API Gateway | Manages API traffic: auth, rate limiting, routing, transforms | Kong, AWS API GW, Apigee; North-South traffic pattern | Configure | |
| Ingress (Networking) | Inbound traffic entering a K8s cluster or network | Managed by Ingress Controller or API Gateway | Configure | |
| Egress (Networking) | Outbound traffic leaving a K8s cluster or network | Control via NetworkPolicy; egress gateway for auditing | Design | |
| Network Policy (K8s) | Firewall rules restricting pod communication at L3/L4 | Ingress + egress rules; default-deny baseline required | Design | |
| eBPF Networking | Kernel-level packet processing without kernel modules | Powers Cilium; L7 policy, connection tracking, XDP | Know | |
| IPsec | Network-layer encryption for VPN tunnels | AWS VPN connections use IPsec; Site-to-Site VPN | Know | |
| Transit Gateway | AWS hub for connecting VPCs and on-premises networks | Hub-and-spoke model; route tables per attachment | Know | |
| VPC Peering | Direct connection between two VPCs; non-transitive | Simple; doesn't scale to many VPCs; use TGW instead | Know | |
| PrivateLink | AWS private connectivity to services without internet exposure | VPC endpoint interface backed by NLB; no public IP | Configure | |
| DDoS (Distributed Denial of Service) | Overwhelming a service with traffic to cause unavailability | AWS Shield Standard (free); Shield Advanced for L7 | Know | |
| WAF Rules | L7 rules filtering HTTP requests at ALB/CloudFront | SQL injection, XSS, rate limiting, geoblocking | Configure | |
| Firewall | Network device or rules allowing/blocking traffic by policy | Stateful (SG) vs stateless (NACL); know the difference | Know | |
| Port Scanning | Probing ports to discover running services | nmap tool; indicator of reconnaissance; monitored in SIEM | Know | |
| SIEM (Security Information and Event Management) | Centralized security event collection, correlation, and alerting | Splunk, Sentinel, Chronicle; you have Splunk expertise | Design | |
| SOC (Security Operations Center) | Team monitoring and responding to security events | Tier 1 triage → Tier 2 investigation → Tier 3 response | Know | |
| Secrets Management | Storing, rotating, and injecting secrets securely into workloads | Vault, AWS Secrets Manager, CyberArk — know tradeoffs | Design | |
| Vault (HashiCorp) | Secrets management with dynamic credentials and PKI | Dynamic DB creds, K8s auth, PKI secrets engine | Design | |
| CyberArk | Enterprise PAM (privileged access management) solution | Your operational background; PAM vs secrets management | Know | |
| PAM (Privileged Access Management) | Controls and audits access to privileged accounts | Break-glass accounts, session recording, just-in-time access | Know | |
| Encryption at Rest | Data encrypted when stored on disk or object storage | KMS CMK for EBS, S3, etcd; mandatory in regulated industries | Design | |
| Encryption in Transit | Data encrypted while moving across networks (TLS) | Enforce TLS 1.2+; disable weak ciphers | Design | |
| RBAC (General) | Access control based on roles mapped to permissions | Principle of least privilege; regular access reviews | Design | |
| ABAC (Attribute-Based Access Control) | Access decisions based on attributes of user, resource, environment | More flexible than RBAC; used in AWS tag-based policies | Know | |
| Network Segmentation | Dividing network into isolated zones limiting lateral movement | DMZ, VPC subnets, K8s namespaces + NetworkPolicy | Design | |
| Lateral Movement | Attacker pivoting from compromised host to other systems | Prevented by network segmentation and zero-trust | Know | |

---

## Domain 11: AI/ML Engineering

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| LLM (Large Language Model) | Neural network trained on text; generates contextual text responses | GPT-4, Claude, Gemini; foundation for AI-powered tooling | Know | |
| RAG (Retrieval-Augmented Generation) | Combines LLM with real-time document retrieval for grounded answers | Used in internal knowledge bots; reduces hallucination | Know | |
| Vector Database | Stores high-dimensional embeddings for semantic similarity search | Pinecone, Weaviate, pgvector; enables RAG retrieval | Know | |
| Embedding | Numerical vector representation of text for semantic comparison | text-embedding-3-small (OpenAI); stored in vector DB | Know | |
| Fine-Tuning | Further training a pretrained LLM on domain-specific data | Expensive; prefer RAG for most operational use cases | Know | |
| Prompt Engineering | Crafting inputs to LLMs to elicit desired outputs | Few-shot, chain-of-thought, system prompt patterns | Know | |
| MLOps | DevOps practices applied to machine learning lifecycle | Model versioning, serving, monitoring, retraining pipelines | Know | |
| Feature Store | Centralized registry of ML features for training and serving | Feast, Tecton; prevents training-serving skew | Know | |
| Model Registry | Versioned storage for trained ML models with metadata | MLflow, W&B, SageMaker Model Registry | Know | |
| Model Serving | Deploying ML models to serve predictions via API | TorchServe, Triton, SageMaker Endpoints, BentoML | Know | |
| Model Drift | Degradation in model accuracy as real-world data changes | Monitor feature distributions; trigger retraining pipeline | Know | |
| Data Drift | Statistical change in input feature distributions over time | Evidently AI, Arize, WhyLabs detect drift | Know | |
| Inference Latency | Time to return a prediction from a deployed model | P99 latency SLO for ML APIs; GPU vs CPU trade-off | Know | |
| Kubeflow | K8s-native ML platform for pipelines, training, serving | Pipelines = Argo Workflows under the hood | Know | |
| MLflow | Open-source ML lifecycle: tracking, registry, deployment | Experiment tracking, model versioning, serving flavors | Know | |
| SageMaker | AWS managed ML platform end-to-end | Training, HPO, model registry, endpoints, pipelines | Know | |
| A/B Testing (ML) | Serving two model versions to user segments; comparing metrics | Shadow deployment → canary → full traffic shift | Know | |
| MLTK (Splunk ML Toolkit) | Splunk extension for predictive analytics and anomaly detection | Your existing expertise; showcase in portfolio | Design | |
| Anomaly Detection | Identifying unusual patterns deviating from baseline behavior | MLTK DBSCAN, OCSVM; Splunk + Python custom models | Design | |
| GitHub Copilot | AI coding assistant integrated into VS Code/JetBrains/CLI | Your current workflow tool; prompt best practices matter | Configure | |
| AI-assisted Operations | Using LLMs to assist with incident triage, runbook generation, postmortems | Emerging space; know use cases and limitations | Know | |
| Prompt Injection | Attack where malicious input hijacks LLM behavior | Security risk in AI-powered internal tools | Know | |
| LLM Guardrails | Mechanisms preventing harmful or off-topic LLM outputs | Constitutional AI, RLHF, content filters | Know | |
| GPU Operator (K8s) | K8s operator automating GPU driver and plugin lifecycle | NVIDIA GPU Operator; required for ML workloads on K8s | Know | |
| Vertical Scaling (ML) | Adding more GPUs/memory to a single node for large models | Different from K8s VPA; model sharding at extreme scale | Know | |

---

## Domain 12: FinOps & Cost Engineering

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| FinOps | Financial operations discipline applying engineering to cloud cost | Cultural movement: finance + engineering collaboration | Design | |
| FinOps Framework | CNCF FinOps Foundation phases: Inform, Optimize, Operate | Three phases iterative; maturity assessment tool available | Know | |
| Unit Economics | Cost per meaningful business unit (cost per transaction, per user) | Staff SRE should define unit economics for their platform | Design | |
| Showback | Reporting cloud costs to teams without billing them | First step; requires tag governance to attribute costs | Know | |
| Chargeback | Billing internal teams for their cloud resource consumption | Requires commitment; changes team behavior most effectively | Know | |
| Tagging Strategy | Consistent labels on all cloud resources for cost attribution | team, env, app, cost-center tags minimum; enforce via SCP | Design | |
| Rightsizing | Matching instance/pod size to actual resource utilization | VPA recommendations; Compute Optimizer for EC2 | Configure | |
| AWS Compute Optimizer | Analyzes CloudWatch metrics to recommend right-size for EC2/ECS | EC2, Lambda, EBS, ECS recommendations; free service | Configure | |
| Reserved Instances (RI) | Commitment to use specific instance type; 30-72% discount | 1-year or 3-year; Standard vs Convertible flavors | Know | |
| Savings Plans | Flexible compute spend commitment; applies across families | Compute Savings Plans most flexible; Compute vs EC2 plans | Know | |
| Spot Instances | Spare AWS capacity at up to 90% discount; interruptible | 2-min interruption notice; Karpenter spot integration | Configure | |
| Spot Interruption | AWS reclaiming spot instance with 2-minute notice | Handle via SIGTERM; drain K8s node gracefully | Configure | |
| Karpenter Spot | Karpenter provisioning spot nodes with automatic fallback | Spot-to-on-demand fallback; diversified instance type pool | Configure | |
| Cost Allocation | Distributing total cloud cost to teams/apps/projects | Requires tagging + blended cost splitting for shared services | Design | |
| Idle Resource Detection | Finding unused EBS volumes, stopped EC2, unattached EIPs | AWS Trusted Advisor + Cost Explorer; automated cleanup | Configure | |
| Data Transfer Cost | Charges for moving data between AZs, regions, internet | Often invisible; cross-AZ traffic adds up in K8s | Design | |
| Egress Cost | Cost of data leaving AWS to internet | CDN (CloudFront) reduces egress; VPC endpoints reduce NAT cost | Design | |
| Cost per Request | Unit metric dividing infrastructure cost by request volume | Directly attributable; correlates with performance SLOs | Design | |
| FinOps Maturity | Crawl → Walk → Run stages of FinOps practice adoption | Know where your org is; describe plan to advance | Know | |
| Cloud Cost Anomaly Detection | Automated alerting on unexpected cost spikes | AWS Cost Anomaly Detection; Slack alert integration | Configure | |
| Kubecost | K8s cost monitoring tool breaking down cost by namespace/pod | Open-source; integrates with Grafana; per-workload cost | Configure | |
| OpenCost | CNCF open standard for K8s cost monitoring | Open-source spec; backed by same team as Kubecost | Know | |
| Resource Efficiency | Ratio of used to provisioned CPU/memory across cluster | Low efficiency = wasted spend; VPA + KEDA improve it | Design | |
| Waste Identification | Finding over-provisioned or unused cloud resources | Process: tag → measure → rightsized → alert on anomaly | Design | |

---

## Domain 13: Data & Messaging

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| Apache Kafka | Distributed commit log for high-throughput event streaming | Topics, partitions, consumer groups, offsets — your domain | Design | |
| Kafka Topic | Named stream of records; divided into partitions | Partition count drives parallelism; cannot reduce partitions | Design | |
| Kafka Partition | Ordered, immutable log; unit of parallelism in Kafka | Key-based routing ensures ordering within partition | Design | |
| Consumer Group | Set of consumers sharing partition assignment for a topic | Each partition assigned to exactly one consumer in group | Design | |
| Kafka Offset | Position of a record in a partition; consumer checkpoint | Auto-commit vs manual commit; know lag implications | Design | |
| Consumer Lag | How far behind consumers are relative to latest offset | Alert on lag >N; KEDA scales consumers on lag | Design | |
| Kafka Schema Registry | Service enforcing Avro/Protobuf/JSON Schema for topics | Schema evolution: backward, forward, full compatibility | Design | |
| Avro | Binary serialization format with schema; used with Kafka | Compact; schema required for deserialization | Know | |
| Protobuf | Google binary serialization format; language-neutral | Faster than JSON; used in gRPC and high-throughput Kafka | Know | |
| RabbitMQ | AMQP message broker with exchanges, queues, and bindings | Your expert domain; T-Mobile notification platform | Design | |
| AMQP | Advanced Message Queuing Protocol; RabbitMQ's core protocol | Exchange types: direct, fanout, topic, headers | Design | |
| Exchange (RabbitMQ) | Routing component receiving messages and routing to queues | Direct routing: exact key; Topic: pattern matching | Design | |
| Queue (RabbitMQ) | Buffer storing messages until consumed | Durable vs transient; lazy queues for large backlogs | Design | |
| Binding (RabbitMQ) | Rule connecting exchange to queue with optional routing key | Defines which messages flow to which queues | Design | |
| Dead Letter Exchange (DLX) | Catches messages that expire, are rejected, or exceed TTL | Configure per-queue; audit DLQ regularly for errors | Design | |
| Shovel (RabbitMQ) | Plugin copying messages between queues/clusters | Used for cross-cluster migration and bridge patterns | Know | |
| Federation (RabbitMQ) | Connects RabbitMQ nodes/clusters across WAN | Lower coupling than clustering; used for geo-distribution | Know | |
| Quorum Queues | RabbitMQ HA queues using Raft consensus protocol | Replace mirrored queues; default for HA in modern RabbitMQ | Design | |
| Mirrored Queues (deprecated) | Older RabbitMQ HA via queue mirroring; replaced by quorum | Know exists; recommend migration to quorum queues | Know | |
| at-least-once delivery | Message delivered one or more times; duplicates possible | Idempotent consumers required; most queue systems default | Design | |
| exactly-once delivery | Message delivered precisely once; no duplicates, no loss | Kafka transactions + idempotent producer; complex to achieve | Design | |
| Idempotent Consumer | Consumer safe to call multiple times with same message | Required for at-least-once delivery systems | Design | |
| Backpressure | Signal from consumer to slow down producer rate | Prefetch count in RabbitMQ; Kafka pause/resume in consumer | Design | |
| Redis | In-memory data structure store: cache, session, queue, pub/sub | Your stack; know: eviction policies, persistence, clustering | Design | |
| Redis Cluster | Distributed Redis with automatic sharding across nodes | 16384 hash slots; node failure handled by replicas | Design | |
| Redis Sentinel | HA monitor promoting replica to primary on failure | Simpler than Cluster; no sharding; for single-shard HA | Know | |
| Redis Streams | Redis data type for append-only log with consumer groups | Kafka-like semantics in Redis; consumer groups + XACK | Know | |
| Cassandra | Distributed wide-column NoSQL; no single point of failure | Your stack; ring topology, consistent hashing, replication factor | Design | |
| Consistent Hashing | Token ring data distribution strategy in Cassandra | Enables linear scale-out; vnodes distribute load evenly | Design | |
| Replication Factor (Cassandra) | Number of copies of each data row across nodes | RF=3 minimum for production; LOCAL_QUORUM for consistency | Design | |
| Quorum Read/Write | Cassandra consistency requiring majority of replicas to agree | LOCAL_QUORUM common in multi-DC; balances speed and safety | Design | |
| Compaction (Cassandra) | Merging SSTables and removing tombstones on disk | STCS vs TWCS vs LCS; wrong strategy = performance problems | Design | |
| MongoDB | Document database storing JSON-like BSON documents | Your stack; Atlas, change streams, aggregation pipeline | Configure | |
| MySQL | Relational database; SQL standard with ACID guarantees | Your stack; know: replication, slow query log, index types | Configure | |
| Connection Pooling | Reusing database connections to reduce connection overhead | HikariCP in Java; pgBouncer for PostgreSQL | Configure | |
| CDC (Change Data Capture) | Streaming database changes as events to downstream consumers | Debezium on Kafka; enables event-driven architectures | Know | |
| Debezium | Open-source CDC platform for MySQL, PostgreSQL, MongoDB | Kafka Connect source connector; captures row-level changes | Know | |

---

## Domain 14: GitOps & Source Control

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| Git | Distributed version control system; tracks file history | Every engineer must know; branching, merging, rebasing | Configure | |
| Branch Strategy | Policy for creating, naming, and merging feature branches | Trunk-based development preferred for CI; GitFlow for releases | Design | |
| Trunk-Based Development | Short-lived branches merged frequently to main | Enables continuous integration; no long-lived feature branches | Design | |
| GitFlow | Branching model with main, develop, feature, release, hotfix branches | Heavier; used for versioned software with release cadence | Know | |
| Pull Request (PR) | Code review mechanism before merging branch to main | Required: branch protection, status checks, CODEOWNERS | Configure | |
| Code Review | Human review of code changes for quality and security | Security team review for infra changes via CODEOWNERS | Design | |
| Merge vs Rebase | Merge preserves history; rebase creates linear history | Rebase before merge keeps log clean; squash for noisy PRs | Know | |
| Squash Merge | Combines all PR commits into one merge commit | Cleaner history; loses granular commit context | Know | |
| Git Tag | Immutable reference to a specific commit; used for releases | Semantic version tags: v1.2.3; trigger release pipelines | Configure | |
| GitOps | Using Git as single source of truth for infrastructure state | Declarative + versioned + automatically reconciled | Design | |
| ArgoCD | K8s GitOps controller syncing cluster state to Git | App, Project, ApplicationSet; health and sync status | Design | |
| Flux | CNCF GitOps toolkit; Kustomization + HelmRelease CRDs | Multi-tenancy via GitRepository per team | Design | |
| Drift Detection (GitOps) | ArgoCD/Flux detects divergence between cluster and Git | Out-of-sync status triggers alert; auto-sync option | Design | |
| Self-Healing (GitOps) | Automatic revert of manual changes to match Git state | ArgoCD sync policy: automated with prune + self-heal | Design | |
| Multi-Cluster GitOps | Managing multiple K8s clusters from one Git repo | ArgoCD ApplicationSet, Flux fleet; critical for Staff SRE | Design | |
| Mono-Repo | Single Git repository containing multiple services or components | Better for atomic cross-service changes; needs CI scoping | Know | |
| Poly-Repo | Separate Git repositories per service | More autonomy per team; harder cross-repo changes | Know | |
| Git Submodule | Reference to another Git repository embedded within a repo | Avoid for application code; use package managers instead | Know | |
| Signed Tags | GPG-signed release tags proving release authenticity | Required in regulated supply chains; GitHub shows Verified | Configure | |
| Branch Protection Rules | GitHub rules: require PR, status checks, signed commits | Configure per-org as default branch policy | Configure | |
| CODEOWNERS | Maps file paths to required reviewers in GitHub PRs | security/ → @security-team; infra/ → @platform-team | Configure | |
| GitHub Actions | GitHub CI/CD using YAML workflows triggered by Git events | on: [push, pull_request, schedule] events | Configure | |
| GitHub OIDC | Keyless AWS authentication from GitHub Actions | No stored secrets; JWT from GitHub used to assume IAM role | Design | |
| Renovate Bot | Automated dependency update PRs with flexible scheduling | Configures automerge for minor/patch updates in safe domains | Configure | |
| Pre-commit Framework | Git hook manager for running checks before commit | .pre-commit-config.yaml; language-agnostic hook runner | Configure | |
| Semantic Release | Automated versioning and changelog from conventional commits | conventional commits format: feat:, fix:, chore: | Configure | |
| Conventional Commits | Standard commit message format: type(scope): description | feat, fix, docs, chore, refactor; enables tooling automation | Configure | |
| Inner Source | Applying open-source collaboration practices inside an organization | Forking, PRs, issues — same workflow for internal code | Know | |

---

## Domain 15: Compliance & Governance

| Term | Plain-English Definition | JD/Interview Context | Level | My Score |
|---|---|---|---|---|
| SOC 2 | AICPA standard for service organization security controls | Type I (design) vs Type II (operating effectiveness over time) | Know | |
| SOC 2 Type II | Audit verifying controls operated effectively over 6-12 months | Common customer requirement; requires continuous evidence | Know | |
| PCI DSS | Payment Card Industry Data Security Standard | 12 requirements; cardholder data isolation; your banking experience | Know | |
| HIPAA | US healthcare data privacy and security standard | PHI protection; covered entities + business associates | Know | |
| GDPR | EU general data protection regulation | Data subject rights, consent, breach notification 72hr | Know | |
| CCPA | California Consumer Privacy Act; US equivalent of GDPR | Data deletion, opt-out of sale; SaaS companies must comply | Know | |
| FedRAMP | US federal cloud security authorization program | ATO (Authority to Operate); controls mapped to NIST 800-53 | Know | |
| NIST CSF | National Institute of Standards cybersecurity framework | Identify, Protect, Detect, Respond, Recover functions | Know | |
| NIST 800-53 | Federal information security controls catalog | Basis for FedRAMP, StateRAMP; 20 control families | Know | |
| CIS Benchmarks | Prescriptive security configuration guides for OS/cloud/K8s | CIS K8s Benchmark, CIS AWS Foundations; Checkov maps to these | Configure | |
| ISO 27001 | International information security management system standard | ISMS certification; risk management framework | Know | |
| DORA (EU regulation) | Digital Operational Resilience Act for EU financial services | Not to be confused with DORA metrics; ICT risk management | Know | |
| Compliance as Code | Expressing compliance requirements as executable rules | Checkov, AWS Config Rules, OPA policies automate audits | Design | |
| Audit Trail | Immutable log of all system and user actions | CloudTrail, K8s audit logs, DB audit logs; required for SOC2 | Design | |
| Evidence Collection | Gathering proof that controls are operating as designed | Screenshots, API responses, automated reports for auditors | Design | |
| Control | A safeguard or countermeasure reducing information security risk | Technical, administrative, or physical; mapped to frameworks | Know | |
| Risk Assessment | Identifying, analyzing, and evaluating information security risks | Likelihood × Impact matrix; formal process in ISO 27001 | Know | |
| Data Residency | Requirement that data stays within a specific geography | AWS regions per country; data sovereignty laws | Know | |
| Data Classification | Categorizing data by sensitivity: Public, Internal, Confidential, Restricted | Drives encryption, access control, and retention policy | Design | |
| Data Retention Policy | Rules for how long data is stored before deletion | S3 lifecycle policies, DB purge jobs; legal hold exception | Configure | |
| WORM (Write Once Read Many) | Storage where data cannot be modified or deleted | S3 Object Lock; regulatory compliance for financial records | Know | |
| Encryption Key Rotation | Periodically replacing encryption keys to limit exposure | AWS KMS automatic rotation; annual for CMKs | Configure | |
| Access Review | Periodic audit of user and service account permissions | Quarterly RBAC review; remove stale access; SOC 2 requirement | Design | |
| Separation of Duties | No single person can perform a critical operation alone | CI/CD: developer cannot deploy to prod without peer approval | Design | |
| Immutable Audit Log | Log that cannot be deleted or modified; tamper-evident | CloudTrail with S3 Object Lock; CloudWatch Logs retention | Design | |
| Change Approval Process | Formal gate before production changes are implemented | CAB (Change Advisory Board), GitOps PR approval, emergency CAB | Design | |
| Governance Risk Compliance (GRC) | Integrated framework for managing governance, risk, and compliance | ServiceNow GRC, Archer; maps controls to frameworks | Know | |
| Threat Modeling | Structured analysis of potential threats to a system | STRIDE model: Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation | Design | |
| STRIDE | Threat modeling categories: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation | Microsoft model; apply to each system component | Know | |
| Penetration Testing | Authorized simulated attacks to find exploitable vulnerabilities | Annual requirement for PCI DSS; internal or third-party | Know | |
| Vulnerability Management | Process of identifying, prioritizing, and remediating CVEs | CVSS-based prioritization; SLA by severity tier | Design | |
| SLA by Severity (Vuln) | Remediation time commitment per CVE severity | Critical: 24-72hr; High: 7-14 days; Medium: 30-90 days | Design | |
| Policy Enforcement Point | Where compliance policy is technically enforced | OPA admission webhook, SCP, bucket policy, WAF rule | Design | |
| Attestation | Signed statement confirming a claim about a system or artifact | SLSA provenance, build attestations, compliance declarations | Design | |
| SBOM for Compliance | Using SBOM to prove component inventory for auditors | EO 14028 mandates SBOM for federal software suppliers | Design | |

---

## Top 60 Must-Know Terms (Flash Card List)

| Rank | Term | Domain | Level | One-Line Definition | Why It Appears in Staff/Principal JDs |
|---|---|---|---|---|---|
| 1 | SLO (Service Level Objective) | Observability/SRE | Design | Target threshold for a service metric over a time window | Every Staff SRE JD; cornerstone of reliability engineering |
| 2 | Error Budget | SRE | Design | Allowable unreliability before SLO is violated | Defines the reliability contract; enables dev/ops tradeoff decisions |
| 3 | IRSA (IAM Roles for Service Accounts) | K8s/AWS | Design | Binds AWS IAM role to K8s pod via OIDC federation | Required for secure AWS access from EKS; appears in 80%+ of K8s+AWS JDs |
| 4 | OPA/Gatekeeper | DevSecOps | Build | Policy-as-code engine enforcing rules at K8s admission | Staff SRE expected to own policy governance; Rego writing expected |
| 5 | GitOps | CI/CD | Design | Git as single source of truth; automated reconciliation | Appears in nearly every cloud-native SRE JD since 2022 |
| 6 | ArgoCD | CI/CD/GitOps | Design | K8s-native GitOps CD controller syncing cluster to Git | De facto standard; ApplicationSet for multi-cluster management |
| 7 | Terraform Remote State | IaC | Design | Shared state backend with locking for team-safe applies | S3 + DynamoDB pattern; appears in all IaC-heavy JDs |
| 8 | SBOM (Software Bill of Materials) | DevSecOps | Design | Machine-readable inventory of software components | EO 14028 mandate; appears in all supply chain security JDs |
| 9 | Sigstore/Cosign | DevSecOps | Design | Keyless container image signing via OIDC transparency log | Supply chain signing is now baseline expectation in 2025+ JDs |
| 10 | OpenTelemetry (OTel) | Observability | Design | CNCF standard for vendor-neutral instrumentation and signal collection | Replacing all vendor agents; appears in every modern observability JD |
| 11 | Burn Rate Alert | Observability | Build | Alert firing when error budget depletes faster than allowed rate | Multi-window burn rate alerting is the Staff-level alerting standard |
| 12 | Admission Webhook | K8s | Design | HTTP endpoint called by API server to validate/mutate resources | Foundation of policy enforcement; appears in advanced K8s JDs |
| 13 | RBAC (K8s) | K8s | Design | Roles and bindings controlling K8s API access | Universal K8s security requirement; governance ownership at Staff level |
| 14 | NetworkPolicy (K8s) | K8s | Design | Pod-level firewall rules for micro-segmentation | Zero-trust K8s network; required in regulated-industry JDs |
| 15 | Chaos Engineering | SRE | Design | Deliberate failure injection to find system weaknesses | Game Day facilitation is a Staff SRE leadership expectation |
| 16 | Blameless Postmortem | SRE | Design | Incident analysis focused on systems, not people | Cultural ownership question in every SRE manager/Staff interview |
| 17 | DORA Metrics | DevSecOps | Design | Four metrics measuring software delivery performance | Referenced in 70%+ of DevOps/SRE JDs; define all four fluently |
| 18 | HPA + KEDA | K8s | Configure | K8s horizontal scaling; KEDA adds event-driven scaling | Queue-based scaling (KEDA on SQS/Kafka/RabbitMQ) = your lived stack |
| 19 | Karpenter | K8s/AWS | Configure | K8s node autoprovisioner replacing Cluster Autoscaler on EKS | Preferred EKS autoscaling; appears in EKS-specific JDs |
| 20 | Trivy | DevSecOps | Configure | All-in-one scanner for CVEs, misconfigs, secrets, SBOM | Most widely referenced open-source scanner in 2024-2026 JDs |
| 21 | Helm | K8s | Configure | K8s package manager bundling manifests as versioned charts | Universal K8s packaging tool; governance of chart lifecycle at Staff level |
| 22 | Operator Pattern | K8s | Build | Custom controller encoding operational domain logic in code | Distinguishes Staff/Principal K8s engineers from intermediate |
| 23 | Service Mesh / mTLS | K8s/Networking | Design | Infrastructure providing mTLS + traffic policy between services | Zero-trust service auth; Istio vs Cilium decision is Staff-level |
| 24 | Secrets Scanning | DevSecOps | Configure | Detecting hardcoded credentials in source code and git history | Pre-commit hook + CI gate; required in secure SDLC JDs |
| 25 | Terraform Modules | IaC | Design | Reusable IaC packages with defined input/output interfaces | Module governance is Staff IaC ownership responsibility |
| 26 | SLSA Framework | DevSecOps | Design | Levels of supply chain security from provenance to hermetic builds | Increasingly required in security-conscious JDs; know L1-L3 |
| 27 | EKS + IRSA + Karpenter | AWS/K8s | Design | Secure, auto-scaling EKS cluster architecture | Stack combination appears in most AWS-native SRE roles |
| 28 | PodDisruptionBudget | K8s | Design | Guarantee minimum available pods during voluntary node disruptions | Zero-downtime operations governance; required in HA system JDs |
| 29 | Error Budget Policy | SRE | Design | Document defining actions when error budget crosses thresholds | Bridges SLO governance and engineering velocity decisions |
| 30 | Rego (OPA) | DevSecOps | Build | Policy language for OPA; evaluates JSON-structured data | Writing Rego policies is a differentiator for Staff security-focused SRE |
| 31 | Observability vs Monitoring | Observability | Design | Monitoring checks known states; observability explores unknown | Definitional question in every Staff observability interview |
| 32 | Four Golden Signals | Observability | Design | Latency, Traffic, Errors, Saturation | Google SRE book standard; expected memorized definition |
| 33 | Crossplane | Platform Eng | Design | K8s-based universal cloud resource provisioner via CRDs | Emerging IDP infrastructure tool; appears in platform engineering JDs |
| 34 | Backstage | Platform Eng | Design | CNCF developer portal and software catalog framework | Appears in 60%+ of platform engineering JDs since 2023 |
| 35 | Falco | DevSecOps | Configure | eBPF-based runtime security monitoring for K8s syscalls | Runtime threat detection; pairs with admission control |
| 36 | CSPM | DevSecOps | Design | Cloud security posture management: continuous compliance checking | Wiz, Prisma Cloud appear in >50% of DevSecOps JDs |
| 37 | Structured Logging | Observability | Configure | Machine-parseable JSON logs with consistent key-value schema | Baseline engineering practice; enables log-to-metric pipelines |
| 38 | SLI (Service Level Indicator) | SRE | Design | Specific metric quantifying user-visible service behavior | Define SLI precisely; interviewers distinguish SLI/SLO/SLA fluency |
| 39 | VPC + Subnets + NAT | AWS | Design | Network isolation, AZ resilience, outbound internet architecture | AWS networking baseline; appears in every AWS infrastructure JD |
| 40 | KMS + Encryption at Rest | AWS | Design | AWS key management encrypting data in EBS, S3, etcd, Secrets Manager | Security hygiene baseline; required in regulated industry JDs |
| 41 | Canary Deployment | CI/CD | Design | Routing small traffic percentage to new version before full rollout | Progressive delivery pattern; Argo Rollouts implementation |
| 42 | StatefulSet | K8s | Configure | K8s workload resource for pods requiring stable identity and storage | Cassandra, Kafka, Redis on K8s — directly relevant to your stack |
| 43 | CRD + Controller Loop | K8s | Design | Custom API types + reconciliation controller implementing operator pattern | Core K8s extensibility; every operator is a CRD + controller |
| 44 | Terraform Plan → Apply | IaC | Configure | Two-phase IaC workflow: review proposed changes, then execute | Demonstrates IaC operational discipline; GitOps gate in CI |
| 45 | GitHub Actions OIDC | CI/CD | Design | Keyless AWS authentication from GitHub Actions using JWT tokens | Security best practice eliminating stored secrets in CI |
| 46 | OWASP Top 10 | DevSecOps | Know | Ten most critical web application security risk categories | Baseline security vocabulary; A03 injection most common probe |
| 47 | Quorum Queues (RabbitMQ) | Messaging | Design | RabbitMQ HA queues using Raft consensus; replaces mirrored | Your RabbitMQ expertise; demonstrate modern HA understanding |
| 48 | Consumer Lag (Kafka) | Messaging | Design | Distance between latest offset and consumer position | KEDA scales consumers on lag; operational alerting metric |
| 49 | Toil | SRE | Design | Manual, repetitive, automatable work that scales linearly with load | Google SRE definition; track and report reduction as Staff metric |
| 50 | Multi-tenancy (K8s) | K8s/Platform | Design | Safe operation of multiple teams on shared cluster infrastructure | Namespace isolation, RBAC, quotas, NetworkPolicy governance |
| 51 | Shift Left Security | DevSecOps | Design | Embedding security checks early in SDLC (IDE → PR → CI) | Core DevSecOps cultural and tooling principle |
| 52 | Incident Commander | SRE | Design | Single decision-maker coordinating all tracks during a P1 incident | Your lived role; formalize with ICS terminology for interviews |
| 53 | P99 Latency | Observability | Design | 99th percentile request duration; worst experience for 1 in 100 users | Alert metric; histogram_quantile(0.99,...) in PromQL |
| 54 | IAM Least Privilege | AWS/Security | Design | Grant only minimum permissions required; revoke when not needed | Universal security principle; IAM Access Analyzer enforces | 
| 55 | Graceful Degradation | SRE | Design | System serves reduced functionality during partial failure | Circuit breaker, feature flags, fallback — Staff design pattern |
| 56 | Kubernetes Audit Logs | K8s/Compliance | Design | API server log of every request for security and compliance | SOC 2 audit trail requirement; policy violation detection | 
| 57 | Zero Trust | Security | Design | Never implicitly trust any network, device, or identity | Cultural and architectural principle underpinning all security work |
| 58 | Cost per Unit (FinOps) | FinOps | Design | Infrastructure cost divided by business transaction volume | Staff SRE bridges engineering and finance; unit economics fluency |
| 59 | Immutable Artifacts | CI/CD | Design | Build once, sign, promote same artifact through all environments | Supply chain security + reproducibility; Cosign + ECR pattern |
| 60 | SRE Team Topology | SRE | Design | Embedded vs platform vs consulting SRE model selection | Staff SRE expected to articulate org model and tradeoffs |
