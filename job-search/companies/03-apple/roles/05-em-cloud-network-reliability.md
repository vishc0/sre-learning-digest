# Role 05 — Engineering Manager, Cloud Network Reliability

## Job metadata
- **JD URL:** https://jobs.apple.com/en-us/details/200642210-3956/engineering-manager-cloud-network-reliability
- **Requisition ID:** 200642210-3956
- **Team:** Apple Cloud Networking — powers iCloud, iTunes, Siri, Maps
- **Location:** **Sunnyvale, CA** (Bay Area — outside your stated Apple relocation set of Austin/Seattle/Cupertino, but commutable from Cupertino housing)
- **Posted base salary:** Not retrieved by automated fetch. Comparable Apple M3/M4 EM band in Bay Area runs **~$208K – $313K** (based on Sr EPM Apple Cloud Networking peer req). Reasonable assumption: floor ≥ $200K. **Confirm on live JD before applying** — CA law requires the range be posted.
- **Match score:** **82%**

## Why this role (with caveats)
Strong leadership + reliability scope match to your profile. Networking depth is the gap. Sunnyvale is the location caveat — you'd want to expand your acceptable list to "Bay Area" specifically for this requisition.

## What matched
- **"Lead and grow team focused on availability, performance, scalability, resiliency of global network services"** → 15 direct reports; 99.99% availability; near-zero Sev1 over 36 months
- **"Multi-cloud connectivity, global footprint"** → AWS migration of primary notification platform; 4 production platforms; ~42 integrated systems
- **"Visionary leader"** → 6 zero-downtime migrations; MART framework adoption org-wide; AI metrics agent deployed for leadership reporting
- **"Powers iCloud / Siri / Maps (high-availability services)"** → SMS / email / push delivery for legal and regulated communications via MoEngage / AJO / DND / MAT — high-availability bar

## Gaps
1. **Networking-specific depth (BGP, Envoy / Istio, SDN)** not on resume — this is the central skill the role hires for
2. **Sunnyvale not in your stated Apple relocation set** (Austin / Seattle stated)
3. **Salary range not posted-verified** by automated fetch

## Gap mitigation
1. Networking → reframe **APIGEE → MEG/TAG proxies migration** as "L7 traffic plane modernization" — that's the closest analog on your resume; mention Envoy/Istio concepts in cover letter and call out the upskill plan honestly. Be prepared for a deep technical screen on networking; this is a stretch role.
2. Location → for this single requisition, expand acceptable list to "Bay Area" (Cupertino housing makes Sunnyvale commutable). Mention I-140 portability removes timing risk.
3. Salary → ask recruiter directly on first call; do not advance without confirming ≥$200K floor.

## Pre-application checklist
- [ ] Confirm posted base range on live JD (≥$200K floor)
- [ ] Decide whether to expand relocation to include Bay Area / Sunnyvale
- [ ] Read 2–3 Envoy + Istio overview articles before recruiter call
- [ ] Recruiter screen: be honest about networking-depth gap; sell leadership scope

---

# TAILORED RESUME

## VISHWESHWAR CHIPPA
**Engineering Manager | Network & Cloud Reliability Leadership | Multi-System Availability at Scale**

Atlanta, GA → Open to relocate Bay Area (Cupertino / Sunnyvale) | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
Engineering Manager with 21+ years leading reliability of large-scale multi-system platforms. At T-Mobile, lead a **15-person SRE team** responsible for the availability, performance, and resiliency of 4 production notification platforms processing **25M+ messages/day**, integrated with **~42 downstream systems** including telecom-grade L7 traffic infrastructure. Maintained **99.99% availability** and **zero customer-impacting Sev1s over 36 consecutive months**. Led L7 traffic-plane modernization (APIGEE → MEG/TAG proxies), AWS cloud migration, and 6 zero-downtime platform migrations. Seeking Engineering Manager role with Apple Cloud Networking to apply multi-system reliability leadership at the scale that powers iCloud, Siri, and Maps.

---

## CORE COMPETENCIES (Cloud Network Reliability alignment)
Multi-System Reliability Leadership · 15-Person Engineering Team Management
L7 Traffic-Plane Modernization · Multi-Cloud Migration Leadership
Cross-Org Influence (42-System Integration) · Incident Command at Scale · SLO/SLI Governance

---

## TECHNICAL SKILLS (mapped to JD)
**Cloud:** AWS (EKS, Lambda, SQS, SNS, S3, DynamoDB); Azure; multi-cloud reliability patterns
**Compute / Containers:** Kubernetes (EKS production), Docker, PCF, VM lineage
**L7 Traffic Plane:** APIGEE, MEG/TAG proxies, Spring Boot, RabbitMQ; **currently leveling up Envoy + Istio concepts**
**Observability:** **Splunk (deep — built MART framework, MLTK anomaly detection, custom dashboards)**, AppDynamics, Grafana, DORA
**Languages:** Python (primary automation), Java, Kotlin, JavaScript
**Security:** Vault, CyberArk, IAM, TKE, Aqua, SonarQube, AppScan
**Data Plane:** MongoDB, Cassandra, Redis, MySQL — distributed at scale

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 platforms · 25M+ msgs/day · **15 direct reports** · ~42 integrated systems · 99.99% availability

**Multi-System Reliability Leadership (Cloud Network alignment)**
- Lead **15-person SRE team** responsible for availability, performance, scalability of 4 production platforms with **~42 downstream system integrations** — equivalent operational complexity to a multi-service network plane
- Maintained **99.99% availability** and **zero customer-impacting Sev1s over 36 months** across all platforms
- Authored MART framework adopted across T-Mobile notification ecosystem; ~40% MTTR reduction
- Built integration test working group across 42 connected systems during TIBCO → Spring Boot migration with no formal authority over downstream teams; zero downstream failures at cutover

**L7 Traffic Plane & Migration Leadership**
- Led **APIGEE → MEG/TAG proxies migration** — rebuilt 12+ API contracts; managed traffic-plane transition without customer-facing degradation
- Led **AWS cloud migration** for primary notification platform: EKS, Lambda, SQS/SNS alignment
- Architected and led **Kubernetes migration** for all 4 platforms over 12 months; zero SLA breach across legally-required message types
- Pattern: 6 zero-downtime platform migrations including TIBCO → Spring Boot, EMS → RabbitMQ, Oracle → MongoDB, VM → PCF → Kubernetes → AWS

**SRE Operating Model & On-Call Command**
- Structured on-call rotation, escalation paths, incident command for 24/7 coverage across 4 platforms
- Established postmortem culture eliminating recurring-incident classes; defined error-budget policy with burn-rate alerting at 5% / 1% consumption
- Implemented PodDisruptionBudgets and circuit breakers preventing cascading failures across services

**Visionary Initiatives**
- Built **production ML anomaly detection** in Python + Splunk MLTK; recovered ~750K message deliveries monthly
- Built **GenAI metrics agent** for leadership reporting; eliminated ~8 hours/week manual data aggregation
- Implemented GitHub Copilot + Claude Code workflows for SRE team of 15

### Macy's | Systems Specialist (Loyalty) | Oct 2012 – Dec 2015
60M customers · $5–7M/day · 100+ TPS · multi-DC failover

### Asurion | Sr. System Design Engineer | Feb 2010 – Oct 2012
### Wachovia/Wells Fargo | Operations Lead | Feb 2009 – Feb 2010
### BP Global | Dev/Operations Lead | Jun 2005 – Feb 2009

---

## CERTIFICATIONS & EDUCATION
SAFe 4 PO/PM · SAFe 4 DevOps · SRE Foundation · TIBCO BW5
B.Tech (Metallurgy) — IIT-BHU | 2004

---

# TAILORED 30-SECOND PITCH

> "I'm Vishweshwar Chippa, SRE Principal at T-Mobile. I lead 15 engineers running 4 production platforms integrated with 42 downstream systems at 99.99% availability for 3 years. I led the L7 traffic-plane modernization — APIGEE to MEG/TAG proxies — and the full cloud migration to AWS. The Apple Cloud Networking EM role is leadership of the same kind of multi-system reliability work, at the scale that powers iCloud, Siri, and Maps. I am honest that networking-stack depth — BGP, Envoy, Istio — is a stretch for me; my edge is leadership scope and reliability discipline at large multi-system scale. Approved I-140 makes the H1B transfer clean."

# COVER LETTER OPENER

> Dear Apple Cloud Networking Hiring Team,
>
> The Cloud Network Reliability EM role asks for a leader who can scale a team responsible for global network services availability and resiliency. I have led that work at T-Mobile for a decade — 15 SRE engineers, 4 production platforms with ~42 downstream integrations, 99.99% availability and zero customer-impacting Sev1s for 36 consecutive months. I led the L7 traffic-plane migration (APIGEE to MEG/TAG proxies) and the cloud migration to AWS. I want to be straightforward: networking-stack depth (BGP, Envoy/Istio, SDN) is a stretch relative to my resume; my edge is leadership scope, multi-system reliability discipline, and a track record of zero-downtime migrations across 6 platforms. I have an approved I-140 (June 2016 priority date), making any H1B transfer routine.
