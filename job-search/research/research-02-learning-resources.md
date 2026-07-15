# Research Report 02 — Learning Resources
## Best Books, Courses, YouTube, Thought Leaders & Free Resources for SRE/DevSecOps 2025–2026

**Research method**: 107 adversarial agents | 25 sources fetched | 107 claims extracted | 18/25 verified
**Date**: June 11, 2026
**Confidence legend**: ✅ Hard-verified (2-1 or 3-0 vote) | ⚠️ Practitioner-recommended (not independently verified) | ❌ Refuted

---

## WHAT TO DO WITH THIS DOCUMENT

Use this as a **shopping list and study companion reference**. When you begin a new domain:
1. Check this document for the primary resource for that domain
2. Purchase/enroll before the first study session
3. Use as the "answer key" when Claude's concept guides leave gaps
4. Return to this doc when calibrating what to say in interviews ("who wrote X, which edition, what year")

---

## SECTION 1: FREE RESOURCES — ALL VERIFIED ✅

### Google SRE Book Series (sre.google/books/) — 3-0 Verified
Three books, all free, no paywall. The canonical baseline for SRE vocabulary.

| Book | Editors/Authors | Best chapters for your goals |
|---|---|---|
| **Site Reliability Engineering** | Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (O'Reilly) | Ch 2 (The Production Environment), Ch 4 (Service Level Objectives), Ch 13 (Emergency Response), Ch 14 (Managing Incidents), Ch 25 (Data Processing Pipelines) |
| **The Site Reliability Workbook** | Google SRE | **Ch 5 (Alerting on SLOs)** — the burn rate math chapter. Ch 6 (Eliminating Toil). Ch 7 (Managing Load). Case studies: Evernote, Home Depot, NYT. |
| **Building Secure & Reliable Systems** | Google | Part II (Designing Systems), Part III (Implementing Systems) |

**How to use**: Read the SRE book for vocabulary and mental models. Use the Workbook as the hands-on companion during Weeks 5 and 8 (Observability + Interview Readiness). Building Secure & Reliable Systems as reference during Week 2 (Supply Chain Security).

---

### AWS Well-Architected Framework — 3-0 Verified
URL: aws.amazon.com/architecture/well-architected

**Six pillars confirmed current as of 2026**:
1. Operational Excellence
2. Security ← **Read this first — directly maps to DevSecOps gaps**
3. Reliability ← **Read second — directly maps to SRE strengths**
4. Performance Efficiency
5. Cost Optimization
6. Sustainability *(added 2021, still current)*

**How to use**: Read Security Pillar + Reliability Pillar before Week 3 (AWS Depth). Reference during Week 4 interview prep for AWS architecture questions. Cite by name in interviews: "Based on the AWS Well-Architected Security Pillar..."

---

### OWASP Software Supply Chain Security Cheat Sheet — 3-0 Verified
URL: cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html

**Four threat categories confirmed**:
1. Source code threats (VCS exploits, malicious code injection)
2. Build environment threats (cache poisoning, compromised build accounts)
3. Dependency threats (vulnerable/compromised components — what SCA catches)
4. Deployment/runtime threats (compromised CI/CD accounts, misconfigurations)

**Key verified requirement**: "Both production and consumption of SBOMs should be automated, preferably as part of the organization's CI/CD process."

**How to use**: Read on Day 1 of Week 2 (Supply Chain Security). This is the ground truth for every SBOM/SCA interview question. Cite by name: "Per the OWASP Supply Chain Security Cheat Sheet..."

---

## SECTION 2: VERIFIED COURSERA / STRUCTURED PROGRAMS ✅

### Google Cloud SRE and DevOps Engineer Professional Certificate — 3-0 Verified
**URL**: coursera.org/professional-certificates/sre-devops-engineer-google-cloud
**Provider**: Google Cloud Training

**Confirmed courses within the program**:
- "Developing a Google SRE Culture" (8 hours confirmed)
- "Getting Started with Google Kubernetes Engine" (6 hours confirmed)

**Aligned to**: Google Cloud Professional Cloud DevOps Engineer certification exam

**How to use**: Enroll in "Developing a Google SRE Culture" during Week 5 (Observability). It provides the Google-native framing of SRE culture that appears in behavioral interview questions. GKE course supplements Week 3 (Kubernetes) if you want GCP-side perspective alongside EKS.

**Note**: Total program course count and hours were refuted — verify current structure at enrollment time.

---

### Google Cloud Security Engineer Professional Certificate — 2-1 Verified
**URL**: coursera.org/professional-certificates/google-cloud-security
**Provider**: Google Cloud

**Confirmed structure**: 14 courses, approximately 2 months at 10 hours/week
**Aligned to**: Professional Cloud Security Engineer certification exam

**How to use**: This is a long program — use selectively, not end-to-end. Relevant courses during Week 2 (Supply Chain Security) and Week 4 (AWS/Cloud Security). Extract the security architecture modules; skip GCP-specific product deep-dives unless you're targeting GCP roles.

---

### IBM Applied DevOps Engineering Professional Certificate — 3-0 Verified
**URL**: coursera.org/professional-certificates/ibm-applied-devops-engineering
**Instructors**: John Rofrano, Upkar Lidder, Alex Parker (all IBM)

**Confirmed content — Course 7**: "Application Security for Developers and DevOps Professionals"
- Covers OWASP principles including broken access controls and SQL injection
- Covers secure coding practices
- Maps directly to DevSecOps pipeline security domain

**How to use**: Enroll in Course 7 specifically during Week 2 (Supply Chain Security). You don't need to take the full 9-course program — extract Course 7 as a standalone unit.

---

### IBM Monitoring and Observability for Development and DevOps — 3-0 Verified
**URL**: coursera.org/learn/monitoring-and-observability-for-development-and-devops
**Instructor**: John Rofrano (IBM Top Instructor)
**Rating**: 4.6/5 stars | ~20,000 enrolled

**Confirmed Module 4**: "Automated Instrumentation with OpenTelemetry" — hands-on lab included

**How to use**: Take during Week 5 (Observability Translation). Module 4's OpenTelemetry lab is exactly what you need to be able to say "I have instrumented a service with OTel" in an interview. Budget 6-8 hours for the full course.

---

## SECTION 3: BOOKS — VERIFIED CONTENT

### Observability Engineering — Content 3-0 Verified, Authorship Uncertain ⚠️
**Publisher**: O'Reilly, 2022 (ISBN listed as 9781492076449; 2nd edition in 2024)
**Authors**: Listed as Charity Majors, Liz Fong-Jones, George Miranda — but authorship was **refuted** by adversarial verification (could not be independently confirmed from primary sources). Verify at O'Reilly before citing author names.

**Confirmed content — Chapter 7**: "Instrumentation with OpenTelemetry"
- Covers automatic instrumentation
- Covers custom instrumentation
- Covers end-to-end instrumentation strategy

**Core thesis (2-1 verified)**: Observable systems enable teams to "ship code swiftly and confidently, identify outliers and aberrant behaviors, and understand the experience of each and every user" — positioning observability as a production excellence capability, not a monitoring afterthought.

**How to use**: Primary textbook for Week 5 (Observability). Read Chapter 7 before the OTel Collector lab. The production excellence framing is directly quotable in Staff/Principal interviews.

---

### Platform Engineering: A Guide for Technical, Product, and People Leaders — Content 2-1 Verified ⚠️
**Authors**: Camille Fournier & Ian Nowland
**Publisher**: O'Reilly, 2024
**Note**: ISBN and exact publication date were refuted — verify at O'Reilly before ordering.

**Confirmed content**:
- "Cultivating a platform-as-product, developer-centric mindset" (explicit chapter)
- "Becoming a product manager for a platform team" (explicit chapter)
- Core thesis: Cloud computing enables applying agile/customer-centric principles to developer experience

**How to use**: Read during Week 6 (Platform Engineering vocabulary). Camille Fournier is also the author of *The Manager's Path* — this is the same person writing about platform engineering from a leadership perspective. The product-as-platform framing is exactly what Staff/Principal interviews test.

---

## SECTION 4: PRACTITIONER-RECOMMENDED BOOKS
*(Not independently verified by the research pipeline — based on practitioner consensus)*

| Book | Author | Domain | Why It Matters |
|---|---|---|---|
| *Terraform: Up & Running* 3rd ed. | Yevgeniy Brikman | Terraform/IaC | Chapter-by-chapter matches Terraform Associate exam; state management coverage is the best in print |
| *Kubernetes in Action* 2nd ed. | Marko Luksa | K8s Internals | Best explanation of controllers and the reconcile loop; CKA track-aligned |
| *The Kubernetes Book* 2024 ed. | Nigel Poulton | K8s Vocabulary | Faster read; use before Luksa for vocabulary orientation |
| *Team Topologies* | Skelton & Pais | Platform Engineering | Origin of "platform team," "stream-aligned team," "cognitive load" — cite by name in interviews |
| *Accelerate* | Forsgren, Humble, Kim | DORA Metrics | Source of the Four Keys (DORA); short read (200 pages); cite in every platform engineering answer |
| *An Elegant Puzzle* | Will Larson | Engineering Leadership | Best book on Staff/Principal engineering management; Larson is a CTO who was a senior IC |
| *The Manager's Path* | Camille Fournier | Career Positioning | Defines the career ladder IC→Staff→Manager→Director; use to calibrate your positioning |
| *Staff Engineer* | Will Larson | Staff Archetype | Free at staffeng.com; defines the four Staff engineer archetypes; read before LinkedIn rewrite |
| *Securing DevOps* | Julien Vehent | CI/CD Security | Older (2018) but foundational; pipeline security, secrets management, audit trails |
| *Container Security* | Liz Rice | DevSecOps | Container runtime security, namespaces, cgroups, capabilities — the technical foundation |
| *Designing Data-Intensive Applications* | Martin Kleppmann | Fintech/Systems | Textbook for distributed systems powering fintech — ACID vs BASE, consensus, replication |

---

## SECTION 5: VERIFIED THOUGHT LEADERS ✅ (3-0 Confirmed CNCF Ambassadors)

### Viktor Farcic — Upbound (Crossplane)
- **YouTube**: "DevOps Toolkit" channel
- **Content**: Cloud-native GitOps, Crossplane, platform engineering, IaC
- **CNCF Ambassador status**: Confirmed on cncf.io/people/ambassadors/
- **KubeCon presence**: Confirmed speaker at KubeCon NA 2024 + KubeCon Europe 2025
- **Follow for**: Platform engineering patterns, GitOps architecture, Crossplane + K8s integration

### Whitney Lee — Datadog, Senior Technical Advocate
- **YouTube**: Personal channel + "You Choose!" series + "Cloud Native Live" series
- **Content**: Kubernetes demonstrations, observability, cloud-native tooling
- **CNCF Ambassador status**: Confirmed on cncf.io/people/ambassadors/
- **CNCF Blog**: Active contributor confirmed August 2025
- **Follow for**: Observability tooling in practice, Kubernetes demos, accessible technical content

### Additional Practitioner-Recommended Thought Leaders
*(Not verified by this pipeline — practitioner consensus)*

| Person | Role | Platform | Follow for |
|---|---|---|---|
| Charity Majors | CTO, Honeycomb | X/@mipsytipsy, honeycomb.io/blog | Observability philosophy, Staff engineering culture |
| Liz Fong-Jones | Honeycomb | X/@lizthegrey | SRE + observability, OpenTelemetry |
| Kelsey Hightower | Google (retired) | X/@kelseyhightower | Kubernetes culture, cloud-native philosophy |
| Liz Rice | Isovalent/Cilium | X/@lizrice | Container security, eBPF |
| Kim Lewandowski | Chainguard | X/@kimsterv | Supply chain security, Sigstore, SBOM |
| Anton Babenko | AWS Hero | LinkedIn/@antonbabenko | Terraform modules, IaC best practices |
| Corey Quinn | LastWeekInAWS | X/@QuinnyPig | AWS cost optimization, cloud architecture |

---

## SECTION 6: YOUTUBE CHANNELS

### Confirmed Active (CNCF-verified)
- **DevOps Toolkit** (Viktor Farcic) — platform engineering, GitOps, Crossplane
- **Whitney Lee's channel** — K8s demos, observability, cloud-native tooling

### Practitioner-Recommended (not independently verified)
| Channel | Best for |
|---|---|
| TechWorld with Nana | Kubernetes visual explanations; control plane architecture; good starter series |
| KodeKloud | CKA/CKS/Terraform exam prep walkthroughs; mirrors the course content |
| AWS re:Invent (YouTube) | Annual conference talks; architecture deep-dives; the "Amazon.com high availability" talks are gold |
| CNCF (YouTube) | KubeCon sessions; OpenTelemetry project updates; free recordings |
| Honeycomb.io (YouTube) | Observability engineering; SLO culture |
| LeadDev (YouTube) | Staff/Principal engineering leadership; team management |

---

## SECTION 7: AI-SRE AND LEADERSHIP RESOURCES

### AI-SRE (AIOps)
| Resource | URL | What it contains |
|---|---|---|
| Awesome AI-SRE | github.com/agamm/awesome-ai-sre | Curated list of AIOps tools, papers, open source projects. Best single starting point. |
| PagerDuty AI Ops blog | pagerduty.com/blog | Current state of AI-assisted incident response in production |

### Staff/Principal Career Resources
| Resource | URL | What it contains |
|---|---|---|
| Staff Engineer Guide | staffeng.com | Will Larson's free book + case studies from Stripe, GitHub, Fastly Staff engineers |
| LeadDev | leaddev.com | Engineering leadership conference talks, free videos |
| ADPList | adplist.org | Free mentorship marketplace — search "SRE" or "DevSecOps" for a mentor |

---

## SECTION 8: SOURCES ACCESSED IN THIS RESEARCH

### Primary (official/direct)
- coursera.org/professional-certificates/sre-devops-engineer-google-cloud
- coursera.org/professional-certificates/google-cloud-security
- coursera.org/learn/monitoring-and-observability-for-development-and-devops
- coursera.org/professional-certificates/ibm-applied-devops-engineering
- cncf.io/people/ambassadors/
- sre.google/books/
- docs.aws.amazon.com/wellarchitected/latest/framework/
- cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html

### Secondary (corroborating)
- classcentral.com — course catalog and ratings
- amazon.com — book product pages (ISBN and page counts refuted; content descriptions confirmed)
- oreilly.com — book table of contents (chapter titles confirmed)
- staffeng.com/book/ — Will Larson's Staff Engineer guide
- github.com/agamm/awesome-ai-sre — AI-SRE curated list
- platformengineering.org — platform engineering community

---

## OPEN QUESTIONS FROM THIS RESEARCH

1. Which specific Udemy instructors for CKA, Terraform Associate, and AWS SAA have verifiable pass-rate data? (The research pipeline could not confirm Udemy-specific claims.)
2. Has the Google Cloud SRE/DevOps certificate been updated for 2025 to include AI operations/Gemini tooling?
3. Which books specifically for Kubernetes internals are most current for 2025 — Luksa 2nd edition vs. *Programming Kubernetes* by Hausenblas/Schimanski?

---

*Research run: June 11, 2026 | 107 agents | 25 sources | 107 claims | 18/25 verified*
*Refresh trigger: Check for new editions of primary textbooks quarterly; verify Coursera program structure before enrolling*
