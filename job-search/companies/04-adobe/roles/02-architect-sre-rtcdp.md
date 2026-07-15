# Role 02 — Architect, Site Reliability Engineering (RTCDP / AEP)

> Pair-application with R158063 (Role 01). RTCDP is the platform under AJO; you've been the enterprise consumer. IC architect track — different from the L40 EM role above.

## Job metadata
- **URL:** https://careers.adobe.com/us/en/job/R166444/Architect-Site-Reliability-Engineering
- **Requisition ID:** R166444
- **Team:** Real-Time CDP / Adobe Experience Platform SRE
- **Location:** San Jose, CA
- **Posted base salary:** **$208K – $302K base** (Glassdoor capture of Adobe-posted CA range)
- **Level:** Architect / Senior Technical Lead (IC, Principal-equivalent)
- **Match score:** **90%**
- **Verdict:** **Natural fit (IC architect track).**

## What matched
- **"RTCDP reliability, scalability, operational excellence at global scale"** → you operate AEP (RTCDP's foundation) in production
- **Kafka-based AEP pipeline** → you run event-driven messaging (RabbitMQ, EMS, Spring Boot streams) at 25M/day
- **Multi-cloud Kubernetes (AKS+EKS)** → led full K8s migration of 4 platforms
- **SLO/SLI governance** → MART framework, 40% MTTR reduction
- **Observability architecture** → custom Splunk dashboards / leadership SLO views
- **Incident command at enterprise scale** → 36 months zero customer-impacting Sev1s

## Gaps
1. **"Architect" IC track** — no direct reports in scope; you're a people leader currently
2. **Native Kafka/Spark depth lighter** than core SRE candidates (your streaming is RabbitMQ/EMS)
3. **Datadog/ArgoCD not in resume** (Splunk/Grafana strong, but Adobe-specific tools missing)

## Gap mitigation
1. Position the IC architect role as "player-coach" pivot; emphasize hands-on architecture decisions you've owned (MART framework design, Kubernetes migration architecture, Vault deployment patterns)
2. Translate RabbitMQ + EMS pub/sub experience to Kafka semantics in interview (consumer groups, partitions, replay)
3. Volunteer Datadog/ArgoCD ramp plan; cite Splunk MLTK as proxy for observability tooling agility

## Resume strategy
**Use the full tailored resume from [Role 01](01_Sr_EM_Adobe_Journey_Optimizer.md)** with these adjustments:
- Replace headline with "Architect | Adobe Experience Platform Operator | RTCDP Reliability"
- Move AEP/RTCDP bullets to top
- De-emphasize "15 direct reports" framing; emphasize technical-leadership and architecture decisions
- Add Kafka-equivalence bullet for messaging stack

## 30-second pitch
> "I'm Vishweshwar Chippa, SRE Principal at T-Mobile. I run Adobe Experience Platform in production for customer data integration and identity management feeding 25 million daily journeys through AJO. The Architect SRE role for RTCDP is the platform layer I'm already on top of as an enterprise customer. I've architected the K8s migration, MART observability framework, and Vault deployment for 4 production platforms. Approved I-140."

## Cover letter opener
> Dear Adobe RTCDP Hiring Team,
>
> The Architect SRE role for Real-Time CDP describes the platform I've been operating as an enterprise customer for years. At T-Mobile I run Adobe Experience Platform for customer data integration, identity stitching, and profile-based triggers feeding 25 million daily customer journeys through AJO. I have architected and led the Kubernetes migration of all 4 of our notification platforms over 12 months with zero SLA breach, authored the MART observability framework adopted across the notification ecosystem, and shipped production ML anomaly detection in Splunk MLTK. The IC Architect track is the depth path I want to take next. I have an approved I-140.

## Pre-application checklist
- [ ] Decide: pursue this OR Role 01 (people-manager track) — apply to both is acceptable, they're different teams
- [ ] Open live JD, confirm posted band ≥$200K
- [ ] LinkedIn outreach to AEP/RTCDP engineers
