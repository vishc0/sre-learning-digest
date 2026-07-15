# Resource Library — SRE/DevSecOps Training Program

**Status legend**: ⬜ Not started | 🔄 In progress | ✅ Complete

---

## DOMAIN E: Terraform / IaC

### Primary Textbook
| Resource | Type | Status | Notes |
|---|---|---|---|
| *Terraform: Up & Running* — Yevgeniy Brikman, O'Reilly, 3rd ed. 2022 | Book | ⬜ | Best in class. Read Chapters 1-5 for fundamentals; Ch 6-9 for modules and production patterns. |

### Primary Course
| Resource | Platform | Instructor | Status |
|---|---|---|---|
| HashiCorp Certified: Terraform Associate | KodeKloud | Mumshad Mannambeth | ⬜ |

### Supplementary
- HashiCorp Learn (developer.hashicorp.com/terraform/tutorials) — free official tutorials
- "Terraform Best Practices" by Anton Babenko — free on GitHub (github.com/antonbabenko/terraform-best-practices)
- OpenTofu documentation (opentofu.org) — Terraform fork gaining enterprise adoption; know both

### Thought Leaders
- Anton Babenko (LinkedIn, @antonbabenko) — Terraform module registry maintainer
- Yevgeniy Brikman (LinkedIn) — author of Terraform: Up & Running

---

## DOMAIN A: Kubernetes Internals (CKA Track)

### Primary Textbook
| Resource | Type | Status | Notes |
|---|---|---|---|
| *Kubernetes in Action* — Marko Luksa, Manning, 2nd ed. 2024 | Book | ⬜ | Chapter-by-chapter matches CKA curriculum. Best explanation of controllers and reconcile loops. |
| *The Kubernetes Book* — Nigel Poulton, 2024 ed. | Book | ⬜ | Faster read. Good for vocabulary building BEFORE the Luksa deep-dive. Start here. |

### Primary Course
| Resource | Platform | Instructor | Status |
|---|---|---|---|
| CKA — Certified Kubernetes Administrator | KodeKloud | Mumshad Mannambeth | ⬜ |
| killer.sh simulator | Included with CKA exam purchase | — | ⬜ | 2 free attempts included; mandatory exam prep |

### Supplementary
- kubernetes.io/docs — "Concepts" section, specifically: Admission Control, RBAC, Scheduling, Storage
- TechWorld with Nana (YouTube) — Kubernetes playlist — visual learner supplement for control plane

### Thought Leaders
- Kelsey Hightower (Google, @kelseyhightower) — K8s co-creator, talks/keynotes
- Liz Rice (Isovalent, @lizrice) — container security + eBPF

---

## DOMAIN C: DevSecOps / Supply Chain Security

### Primary Textbook
| Resource | Type | Status | Notes |
|---|---|---|---|
| *Container Security* — Liz Rice, O'Reilly, 2020 | Book | ⬜ | Container runtime security, namespaces, cgroups, capabilities. The foundation. |
| CISA "Defending CI/CD Environments" — free PDF, 2023 | Free guide | ⬜ | Government-produced; names specific attack patterns including PPE attacks |

### Primary Course
| Resource | Platform | Instructor | Status |
|---|---|---|---|
| DevSecOps Master Course | Udemy | Zeal Vora | ⬜ | Covers SAST/SCA/Trivy/OPA integration in pipelines specifically |
| CKS — Certified Kubernetes Security Specialist | KodeKloud | Mumshad Mannambeth | ⬜ | After CKA |

### Supplementary
- Snyk Learn (learn.snyk.io) — free, module-by-module, earns verifiable LinkedIn badges
- OWASP Top 10 — owasp.org/Top10 — verify current year numbering before citing in interviews
- CISA "Hacking the Supply Chain" — free PDF, 2023

### Thought Leaders
- Kim Lewandowski (Chainguard, @kimsterv) — Sigstore/SBOM/supply chain
- Liz Rice (Isovalent) — container security
- Ian Coldwater (Microsoft) — K8s security

---

## DOMAIN D: Observability / MELT / OpenTelemetry

### Primary Textbook
| Resource | Type | Status | Notes |
|---|---|---|---|
| *Observability Engineering* — O'Reilly, 2022 (ISBN 9781492076449, 2nd ed. 2024) | Book | ⬜ | **Chapter 7 confirmed: "Instrumentation with OpenTelemetry"** — covers automatic instrumentation, custom instrumentation, end-to-end strategy. Positions observability as a production excellence capability. Note: authorship details (Charity Majors, Liz Fong-Jones, George Miranda) were refuted by adversarial verification — confirm at O'Reilly before citing names. |
| *Google SRE Workbook* — Google, free PDF | Free book | ⬜ | sre.google/workbook — Chapters 5, 6, 7 on SLOs, toil elimination, on-call. MANDATORY. |

### Primary Course
| Resource | Platform | Instructor | Status |
|---|---|---|---|
| "Monitoring and Observability with OpenTelemetry" | Udemy | Jonah Kowall | ⬜ |

### Supplementary
- opentelemetry.io/docs/getting-started — official OTel getting started guide
- *Practical Monitoring* — Mike Julian, O'Reilly, 2017 — shorter; bridges AppDynamics → modern tooling
- Google SRE Book (original) — sre.google/sre-book — free PDF; read alongside Workbook

### Thought Leaders
- Charity Majors (Honeycomb CTO, @mipsytipsy) — observability philosophy
- Liz Fong-Jones (Honeycomb, @lizthegrey) — SRE + observability
- Austin Parker (Lightstep/ServiceNow) — OpenTelemetry

---

## DOMAIN B: AWS Architecture

### Primary Training Path — AWS-Direct (Confirmed Setup)
**Vishwe is setting up an AWS account specifically for training. All labs run on real AWS resources.**

| Resource | Platform | Cost | Status |
|---|---|---|---|
| **AWS Skill Builder** (skillbuilder.aws) | AWS official | Free tier available; ~$29/mo for full access | ⬜ | Start here — structured learning paths aligned to each AWS cert |
| **"AWS Cloud Practitioner Essentials"** | AWS Skill Builder | Free | ⬜ | If any AWS fundamentals feel shaky — skip if already comfortable |
| **"Architecting on AWS"** | AWS Skill Builder | Included in subscription | ⬜ | The official 3-day course condensed; covers VPC, IAM, EKS, S3 at architect depth |
| **AWS SAA-C03 Exam Prep** | AWS Skill Builder | Free official prep | ⬜ | Official AWS exam prep — use alongside Cantrill course |

### Primary Course (Deep Study)
| Resource | Platform | Instructor | Status |
|---|---|---|---|
| AWS Certified Solutions Architect Associate (SAA-C03) | learn.cantrill.io | Adrian Cantrill | ⬜ | ~$40 one-time. Most thorough SAA prep. Covers IRSA, VPC, multi-account in depth. Use alongside real AWS account. |
| SAA Practice Exams | tutorialsdojo.com | Jon Bonso (Tutorial Dojo) | ⬜ | Gold-standard practice bank. Predictive of actual exam difficulty. |

### AWS Services to Master Hands-On (Training Account)
| Service | Why | Lab Week |
|---|---|---|
| IAM (roles, policies, OIDC, SCPs) | Foundation of everything; IRSA depends on this | Week 1 |
| S3 + DynamoDB | Terraform remote state backend | Week 1 |
| EKS | Your primary production platform — go deep | Week 3 |
| ECR | Container image registry with native scanning | Week 2 |
| VPC (subnets, NACLs, SGs, endpoints, PrivateLink) | Every architecture question touches VPC | Week 4 |
| CloudWatch + Container Insights | Observability for EKS | Week 5 |
| ADOT (AWS Distro for OpenTelemetry) | OTel → CloudWatch bridge; know this cold | Week 5 |
| GuardDuty + Security Hub | Runtime threat detection + posture management | Week 4 |
| Secrets Manager + Parameter Store | Secrets management patterns | Week 2 |
| AWS Config | Drift detection + compliance rules | Week 4 |

### Cost Management for Training Account
- Set billing alert: $25/month hard limit
- Enable Cost Explorer — review weekly
- **EKS costs $0.10/hr for control plane** — always `eksctl delete cluster` after sessions
- Everything else (S3, DynamoDB, ECR, IAM, CloudWatch basic) is free tier or cents/month
- Estimated total training cost across 8 weeks: **$20–$40**

### Supplementary
- Stephane Maarek SAA-C03 course (Udemy) — for breadth sweep before exam
- AWS Well-Architected Framework — free, aws.amazon.com/architecture/well-architected — read Security Pillar + Reliability Pillar
- AWS documentation: IRSA setup guide; VPC endpoints guide; GuardDuty user guide
- AWS re:Post (repost.aws) — AWS's official community Q&A; better than Stack Overflow for AWS-specific issues

### Thought Leaders
- Corey Quinn (LastWeekInAWS.com, @QuinnyPig) — AWS cost/architecture commentary
- Adrian Cantrill (learn.cantrill.io) — AWS training
- AWS Heroes program (aws.amazon.com/developer/community/heroes/) — practitioner experts by specialty

---

## DOMAIN F: CI/CD Pipeline Security

### Primary Textbook
| Resource | Type | Status | Notes |
|---|---|---|---|
| *Securing DevOps* — Julien Vehent, Manning, 2018 | Book | ⬜ | Older but foundational. Pipeline security, secrets management, audit trails. |

### Primary Course
| Resource | Platform | Instructor | Status |
|---|---|---|---|
| GitHub Actions — The Complete Guide | Udemy | Maximilian Schwarzmüller | ⬜ | Pipeline mechanics |
| GitHub Advanced Security learning path | GitHub (free) | — | ⬜ | Security gates; earns a free badge |

### Supplementary
- Gitleaks official docs (github.com/gitleaks/gitleaks) — secrets scanning configuration
- TruffleHog docs — another secrets scanner; know both
- GitHub docs: "Security hardening for GitHub Actions" — official best practices for PPE defense

---

## DOMAIN G: Platform Engineering

### Primary Textbook
| Resource | Type | Status | Notes |
|---|---|---|---|
| *Team Topologies* — Skelton and Pais, IT Revolution, 2019 | Book | ⬜ | MANDATORY. The vocabulary of "platform team," "stream-aligned team," "cognitive load" comes from here. Cite it by name in interviews. |
| *Accelerate* — Forsgren, Humble, Kim, IT Revolution, 2018 | Book | ⬜ | The source of DORA metrics. Short read (200 pages). Cite it when naming the Four Keys. |

### Primary Course
| Resource | Platform | Status |
|---|---|---|
| Platform Engineering on Kubernetes | Linux Foundation / CNCF (free) | ⬜ |

### Supplementary
- Backstage official docs (backstage.io) — catalog-info.yaml schema, plugin development
- Evan Bottcher's "What I Talk About When I Talk About Platforms" — martinfowler.com — the defining blog post on platform engineering philosophy
- DORA reports — dora.dev — annual State of DevOps reports; cite recent year in interviews

### Thought Leaders
- Kaspar von Grünberg (Humanitec) — IDP patterns
- Evan Bottcher (martinfowler.com) — platform engineering philosophy
- Manuel Pais (co-author Team Topologies) — Team Topologies blog/talks

---

## DOMAIN H: Incident Command & Reliability at Scale

### Primary Textbook
| Resource | Type | Status | Notes |
|---|---|---|---|
| *Google SRE Workbook* — Google, free PDF | Free book | ⬜ | sre.google/workbook — already in Domain D list. Chapters 5-7 specifically for incident management. |
| *Incident Management for Operations* — Rob Schnepp, O'Reilly | Book | ⬜ | ICS framework applied to IT operations |

### Primary Course
| Resource | Platform | Status |
|---|---|---|
| Introduction to Incident Management | PagerDuty University (free) | ⬜ | Short modules; earns certificate |

### Supplementary
- learningfromincidents.io — case studies used by Staff/Principal SREs at Slack, AWS, Etsy
- LitmusChaos docs (litmuschaos.io) — CNCF chaos engineering framework

---

## LEADERSHIP + AI TOPICS (Staff/Principal Lens)

### Books
| Resource | Status | Why |
|---|---|---|
| *An Elegant Puzzle* — Will Larson, Stripe Press, 2019 | ⬜ | Best book on engineering management at Staff/Principal level. Written by a CTO who was a senior IC. |
| *The Manager's Path* — Camille Fournier, O'Reilly, 2017 | ⬜ | Defines the career ladder from IC to Staff to Manager to Director; calibrate your positioning |
| *Staff Engineer* — Will Larson, free online at staffeng.com | ⬜ | Defines the Staff engineer archetype; read before writing your LinkedIn About section |

### Courses/Resources
| Resource | Status |
|---|---|
| staffeng.com — Will Larson's Staff Engineer guide + case studies | ⬜ |
| LeadDev.com — engineering leadership conference talks (free videos) | ⬜ |
| ADPList.org — free mentorship; search SRE or DevSecOps for a mentor | ⬜ |

### AI-in-SRE Resources
| Resource | Status | Why |
|---|---|---|
| "AI-Assisted Incident Response" — PagerDuty blog series | ⬜ | Current state of AIOps in production |
| GitHub Copilot for Infrastructure (GitHub blog) | ⬜ | How AI changes IaC and pipeline authoring |
| Honeycomb blog — Charity Majors on AI and observability | ⬜ | The Staff/Principal lens on AI-assisted debugging |

---

## FINANCE / TELECOM / RETAIL SECTOR FUNCTIONAL KNOWLEDGE

*(Added per user request — covers high-paying sectors' core systems)*

### Financial Services
| Resource | Status | Why |
|---|---|---|
| *Designing Data-Intensive Applications* — Martin Kleppmann, O'Reilly, 2017 | ⬜ | The textbook for understanding distributed systems that power fintech — ACID vs BASE, consensus, replication |
| "Payment Systems in the US" — Carol Coye Benson (free online) | ⬜ | ACH, wire transfer, card rails — understand what you're building reliability for |
| PCI-DSS quick reference guide — PCI Security Standards Council (free) | ⬜ | Every fintech SRE interview asks about compliance constraints |
| FIX Protocol overview (wikipedia + FIX Trading Community) | ⬜ | Capital markets trading systems vocabulary |

### Telecom (Your Domain — Needs Market Language)
| Resource | Status | Why |
|---|---|---|
| GSMA Intelligence reports (gsma.com) — free summaries | ⬜ | Industry vocabulary: MNO, MVNO, BSS/OSS, network slicing, 5G SA core |
| "Telecommunications: An Introduction" — 4th ed, Bates | ⬜ | Reference for RAN, core network, IMS stack vocabulary — know what surrounds your notification work |
| 3GPP overview (3gpp.org — specifications summary pages) | ⬜ | Standards that define the 4G/5G stack — useful for T-Mobile context in interviews |

### Retail / E-commerce
| Resource | Status | Why |
|---|---|---|
| "Designing Distributed Systems" — Burns, O'Reilly, free PDF | ⬜ | Covers retry patterns, circuit breakers — the patterns behind Macy's loyalty platform architecture |
| AWS re:Invent talks: "Amazon.com's approach to high-availability" (YouTube) | ⬜ | The gold standard for retail-scale reliability patterns |
| Google SRE case studies — sre.google/case-studies | ⬜ | Real-world reliability stories from search, ads, and retail-adjacent infrastructure |

### Healthcare / Insurance
| Resource | Status | Why |
|---|---|---|
| HIPAA Security Rule overview — HHS.gov (free) | ⬜ | If targeting health tech SRE roles, HIPAA compliance vocabulary is baseline |
| HL7 FHIR overview — hl7.org | ⬜ | Healthcare data interoperability standard; appears in health tech platform engineering |

---

## VERIFIED COURSERA / STRUCTURED CERTIFICATE PROGRAMS
*(Adversarially verified by 107-agent research workflow, June 2026)*

### SRE + DevOps Track
| Program | Provider | Platform | Verified Content | Status |
|---|---|---|---|---|
| **Google Cloud SRE and DevOps Engineer Professional Certificate** | Google Cloud Training | Coursera | Includes "Developing a Google SRE Culture" (8 hrs) + "Getting Started with Google Kubernetes Engine" (6 hrs). Aligned to Google Cloud Professional Cloud DevOps Engineer exam. | ⬜ |
| **IBM Applied DevOps Engineering Professional Certificate** | IBM | Coursera | Course 7 confirmed: "Application Security for Developers and DevOps Professionals" — covers OWASP Top 10, secure coding. Instructors: John Rofrano, Upkar Lidder, Alex Parker. | ⬜ |

### Cloud Security Track
| Program | Provider | Platform | Verified Content | Status |
|---|---|---|---|---|
| **Google Cloud Security Engineer Professional Certificate** | Google Cloud | Coursera | 14 courses, ~2 months at 10 hrs/week. Prepares for Professional Cloud Security Engineer exam. Direct URL: coursera.org/professional-certificates/google-cloud-security | ⬜ |

### Observability / OpenTelemetry
| Course | Provider | Platform | Verified Content | Status |
|---|---|---|---|---|
| **Monitoring and Observability for Development and DevOps** | IBM / John Rofrano | Coursera | 4.6/5 stars, ~20,000 enrolled. Module 4: "Automated Instrumentation with OpenTelemetry" lab confirmed. Covers OTel + container tracing in Kubernetes. Direct URL: coursera.org/learn/monitoring-and-observability-for-development-and-devops | ⬜ |

---

## FREE AUTHORITATIVE REFERENCES
*(All verified as freely available — no paywall)*

### Google SRE Book Series — sre.google/books/
| Book | Editors / Authors | Best For | Status |
|---|---|---|---|
| *Site Reliability Engineering* | Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy | Foundational SRE concepts: SLOs, toil, error budgets, postmortems | ⬜ |
| *The Site Reliability Workbook* | Google SRE | Hands-on companion — case studies from Evernote, Home Depot, NYT. **Chapters 5-7 mandatory for SLO math and burn rate alerts.** | ⬜ |
| *Building Secure & Reliable Systems* | Google | Security + reliability intersection — complements DevSecOps track | ⬜ |

### AWS Well-Architected Framework — aws.amazon.com/architecture/well-architected
**Six pillars (verified current as of 2026)**: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.
- Read: Security Pillar + Reliability Pillar first
- Reference during: AWS SAA study + IRSA and VPC deep-dive

### OWASP Software Supply Chain Security Cheat Sheet
URL: cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html
**Four verified threat categories**:
1. Source code threats (VCS exploits, malicious code injection)
2. Build environment threats (cache poisoning, compromised accounts)
3. Dependency threats (vulnerable/compromised components)
4. Deployment/runtime threats (compromised CI/CD, misconfigurations)
**Key verified recommendation**: SBOM generation AND consumption must be automated within CI/CD pipelines.

---

## VERIFIED PLATFORM ENGINEERING BOOK (2024)
| Resource | Authors | Publisher | Verified Content | Status |
|---|---|---|---|---|
| *Platform Engineering: A Guide for Technical, Product, and People Leaders* | Camille Fournier & Ian Nowland | O'Reilly, 2024 | Covers "platform-as-product, developer-centric mindset" and "product management for platform teams" as explicit topics. Thesis: cloud computing enables applying agile/customer-centric principles to developer experience. | ⬜ |

> **Note**: ISBN and exact publication date were refuted in adversarial verification — verify at O'Reilly before ordering. Camille Fournier is also author of *The Manager's Path* — this is the same person, now focused on platform engineering specifically.

---

## VERIFIED THOUGHT LEADERS (CNCF-CONFIRMED, 2025)

| Person | Company/Role | Platform | What to Follow |
|---|---|---|---|
| **Viktor Farcic** | Upbound (Crossplane) | YouTube: "DevOps Toolkit" channel | Cloud-native GitOps, Crossplane, platform engineering — CNCF Ambassador, KubeCon speaker |
| **Whitney Lee** | Datadog, Senior Technical Advocate | YouTube + "You Choose!" series + "Cloud Native Live" | Kubernetes, observability, cloud-native demos — CNCF Ambassador, CNCF Blog contributor |

> Both confirmed on cncf.io/people/ambassadors/ and in KubeCon NA 2024 + KubeCon Europe 2025 session listings.

### AI-SRE Resources (Free, Curated)
| Resource | URL | What It Contains |
|---|---|---|
| Awesome AI-SRE | github.com/agamm/awesome-ai-sre | Curated list of AIOps tools, papers, and projects — the best single starting point for AI-assisted operations |
| Staff Engineer Guide | staffeng.com | Will Larson's free guide + real case studies from Staff engineers at Stripe, GitHub, Fastly |

---

## Community Resources

| Community | Purpose | Access |
|---|---|---|
| CNCF Slack (slack.cncf.io) | #kubernetes, #opentelemetry, #opa technical questions | Free, self-invite |
| SRE Weekly (sreweekly.com) | Current SRE/DevSecOps news | Free newsletter |
| learningfromincidents.io | Incident case studies | Free |
| ADPList.org | Free mentorship — search SRE/DevSecOps | Free |
| Exponent.dev | Mock interviews with practitioners | $12-19/month |
| Levels.fyi | Compensation calibration | Free |
| Gremlin Community (gremlin.com/community) | Chaos engineering practitioners | Free |

---

*Last updated: June 11, 2026 | Review monthly for version/edition changes*
