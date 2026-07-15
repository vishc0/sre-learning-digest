# Amazon AWS — Per-Role Index

**Research date:** 2026-05-08 | **7 roles tracked**

> **Strategic note:** Amazon hires laterally at L6 Manager (M-band) and L7 Principal Engineer. **L7 PE is brutally hard to enter laterally** — bar is "industry-recognized in your domain." Your bullseye is **M-band Sr SysDev Manager** (Roles 1, 4, 5) — manager track at Sr Manager / Director-equivalent scope.

## Priority ranking

| Rank | Title | Req ID | Location | Level | Match % | Verdict |
|------|-------|--------|----------|-------|---------|---------|
| 🎯 **1** | Sr. Systems Development Manager, AWS Managed Operations | **3132584** | Herndon VA / verify Seattle | M-band/L7 | **92%** | Apply this week (verify Seattle option) |
| 2 | Sr. Systems Development Manager, Managed Operations | 2805245 | Seattle/Herndon | M-band/L7 | 88% | Apply alongside #1 |
| 3 | Systems Development Manager, Managed Operations | 2918092 | Not retrieved | M-band/L6 | 82% | Stretch (only if Sr opens don't land) |
| 4 | Sr. Manager, Software Development - AWS Insights & Enterprise Tools | 1361120 | **Seattle** | M-band/L7 | 78% | Natural fit (cleanest Seattle option) |
| 5 | Sr Manager, Software Development, AWS GenAI Security | 3094971 | Seattle (implied) | M-band/L7 | 70% | Stretch but viable |
| 6 | Principal Engineer, Amazon (Multiple Locations) | 2741847 | Multi (Seattle option) | L7 IC | 45% | Stretch (long-shot, no public brand) |
| 7 | Sr. Principal Engineer, AWS Infrastructure Services | 10393965 | Not retrieved | L8 | 25% | **Skip** (Distinguished feeder) |

## Top finding

**AWS Managed Operations (MO)** — chartered April 2023 to reduce operational toil for AWS Region day-to-day operations — has 3 active reqs (Roles 1, 2, 3). The team's published charter ("operational excellence at AWS Region scale, reduce toil") is a sentence-level match for your **MART framework + 25M-msg-per-day + 36-month zero-Sev1 record**. Your Operational Excellence Leadership Principle alignment is unfaked.

**Caveat:** Verify Seattle/Bellevue location availability for Role 1 (Herndon-only is outside your stated relocation set).

## Per-role analysis

### Role 1 — Sr. Systems Development Manager, AWS Managed Operations (3132584) — TOP ★
**URL:** https://www.amazon.jobs/en/jobs/3132584/sr-systems-development-manager-aws-managed-operations-mo
**Inferred band:** $200K – $268K base + RSU (Sr SysDev Mgr Bay/Sea band)

**What matched (Leadership Principle alignment):**
- "Reduce operational load and toil" → ~25% Python toil-reduction story (Operational Excellence)
- "Day-to-day operations for AWS Regions; availability, reliability, latency" → 99.99% across 4 platforms (Deliver Results)
- "Build & lead a Systems Engineering team" → 15-direct-reports leadership (Hire and Develop)
- "Drive measurable Operational Excellence" → MART framework adopted org-wide
- Senior management business-acumen → SAFe certs + Product Owner depth
- Strong technical depth on systems + DB → TIBCO→Spring Boot, Oracle→MySQL→MongoDB migrations (Ownership)

**Gaps:** No Go (AWS internal tooling is Go-heavy); no prior AWS-internal Brazil/Pipelines/CloudFormation experience; "AWS Region operations" implies physical/network scale beyond app-level; possible Herndon VA-only

**Mitigation:** Lead Python automation heavily; position Go as "next language to ramp on, idiomatic in 4 weeks"; cite 6 zero-downtime migrations including AWS migration of T-Mobile primary notification platform; reframe 25M msgs/day as a regional control-plane analog; ask up-front whether Seattle/Bellevue is an option

→ **Full tailored resume + pitch in [01_Sr_SysDev_Mgr_MO_3132584.md](01_Sr_SysDev_Mgr_MO_3132584.md)**

---

### Role 2 — Sr. Systems Development Manager, Managed Operations (2805245)
**URL:** https://www.amazon.jobs/en/jobs/2805245/sr-systems-development-manager-managed-operations
Sister req to Role 1 — same MO charter, possibly different sub-team.

**What matched:** Same MO charter; MART framework = OpEx muscle; 36 months zero Sev1 = the bar AWS expects; 6 zero-downtime migrations = "long-term engineering projects to reduce toil"; multi-region failover from Macy's

**Mitigation:** Apply to both 3132584 and 2805245; let recruiter triage. Lead with the MART → OpEx one-pager.

---

### Role 3 — Systems Development Manager, Managed Operations (2918092)
Junior peer to Roles 1 & 4 — likely L6 entry M-band.

**Verdict:** Use only as fallback. Negotiate to L7 during loop calibration if performance warrants. Position as "ready to step in fast and deliver Sr. Manager scope from day 1."

---

### Role 4 — Sr. Manager, Software Development - AWS Insights & Enterprise Tools (1361120) — Seattle confirmed
**URL:** https://www.amazon.jobs/en/jobs/1361120/sr-manager-software-development-aws-insights-enterprise-tools
**Team:** AWS Cloud Insights & Optimization (cost/usage/performance products)
**Location:** **Seattle, WA confirmed**

**What matched:** "Translate complex requirements into project plans" → SAFe Product Owner + 12-week release cycles; on-call rotation → on-call leadership decade; "authoritative provider of cloud insight" → custom Splunk dashboards, DORA metrics, MART; day-to-day engineering team management → 15-person team; "Ownership, autonomy, deliver results" → 4 platforms / zero Sev1 / 6 migrations

**Gaps:** No prior SaaS product P&L ownership for external customers; internal AWS billing/usage data model unfamiliar; no public AWS speaking/blogging history

**Mitigation:** Reframe 4 internal T-Mobile platforms as multi-tenant products with internal SLAs/customers; pitch first 90 days reading internal Wiki + MWAA cost references; offer to publish internal-first blog on MART within 6 months

---

### Role 5 — Sr Manager, Software Development, AWS GenAI Security (3094971)
**URL:** https://www.amazon.jobs/en/jobs/3094971/sr-manager-software-development-aws-genai-security
**Team:** AWS Security — GenAI service protection (Bedrock, Q Business, Q Developer, SageMaker)

**What matched:** GenAI services tooling → leadership chat agent + Splunk MLTK ML anomaly detection; building/managing engineers + leaders → 15 reports onshore + offshore; pre-release tool building → Copilot/Claude Code internal toolchain; Vault + CyberArk → security-conscious foundation

**Gaps:** No application security or pentesting background; Bedrock/SageMaker only consumed at toy scale, not as service operator; no prior security org leadership

**Mitigation:** Frame Cybersecurity Syndicate reviews + AppScan + SonarQube + vulnerability remediation as security delivery; volunteer first 6 months learning AppSec patterns; pitch AI/ML literacy as the rare skill; bring GenAI agent demo to loop

---

### Role 6 — Principal Engineer, Amazon (2741847) [Stretch]
**URL:** https://amazon.jobs/en/jobs/2741847/principal-engineer-amazon-multiple-locations-usa
**Posted base salary:** **$180,100 - $311,200** (verified — only confirmed band in this batch)

**Verdict:** Apply only as long-shot. Amazon L7 PE is "industry-recognized in distributed systems" — typically requires AWS-internal tenure or external SoS/keynote-level visibility. Your strength is leadership/delivery; PE community is IC-only.

**Action:** Build technical brand (LinkedIn long-form posts on MART) in next 90 days regardless. Be honest in any loop — claim Sr. Manager / Sub-org SRE leadership, not Bar Raiser-grade L7 PE.

---

### Role 7 — Sr. Principal Engineer, AWS Infrastructure Services (10393965) — SKIP
L8 / Distinguished Engineer feeder. Out of band; defer 5+ years out.

---

## Recommended action order
1. **Apply Role 1 (3132584) and Role 2 (2805245) in parallel** — same MO charter, let recruiter triage. Confirm Seattle availability before applying.
2. **Apply Role 4 (1361120)** — confirmed Seattle, cleaner observability/Splunk fit.
3. **Apply Role 5 (3094971)** — stretch but the GenAI agent demo is a real differentiator.
4. **Hold Role 3 (2918092)** as fallback; only apply if L7 reqs go cold.
5. **Skip Roles 6 and 7** unless you build technical brand in next 90 days.

## Networking targets
- LinkedIn: AWS Managed Operations engineers and managers (Seattle + Herndon)
- Amazon Operational Excellence community (look for AWS staff who speak at re:Invent on OpEx)
- Universal gap: no Go. Frame Python aggressively, commit to Go ramp in onboarding plan.
