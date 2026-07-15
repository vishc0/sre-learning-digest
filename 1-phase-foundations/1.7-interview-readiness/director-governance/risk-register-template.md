# Risk Register — Director/VP SRE Template
## Owner: [Director Name] | Platform: [Platform Name] | Review Cadence: Quarterly

---

## How Directors Use a Risk Register (Not Just Fill One In)

A risk register is not a compliance form. It is the Director's primary tool for:

1. Making risk **visible** to stakeholders who need to make resource decisions
2. **Translating technical debt** into language a CFO or CTO can act on
3. Creating a **paper trail** that protects the team when a predicted risk materializes
4. Driving **prioritization conversations** with product and leadership from evidence, not opinion

**The Director's rule**: If a risk is on the register and leadership has acknowledged it, it is no longer solely your risk. If a risk is NOT on the register and it materializes, it is entirely your risk.

---

## Risk Appetite Statement (Complete This First)

Before populating the register, define your org's risk appetite. This is the governing statement that all register entries are measured against.

| Dimension | Appetite Statement | Threshold |
|---|---|---|
| **Availability** | We will not accept customer-facing unavailability exceeding X minutes/month for Tier 1 services | SLO breach = immediate escalation |
| **Security** | We will not operate with known P0/P1 CVEs unpatched beyond our stated SLA | P0: 24hr, P1: 72hr, P2: 14 days |
| **Change** | We will not ship changes to Tier 1 services without automated rollback capability | No rollback = no deploy |
| **Data integrity** | We will not accept data loss in customer transaction records | RPO = 0 for financial/transactional data |
| **Compliance** | We will not knowingly operate in violation of [SOC2/HIPAA/PCI] requirements | Violation triggers immediate freeze + escalation |

**Signed off by**: [VP Engineering Name], [CISO Name], [Date]

---

## Risk Register Table

| ID | Risk Title | Category | Description | Likelihood (1-5) | Impact (1-5) | Risk Score | Owner | Mitigation | Acceptance / Escalation | Status | Last Reviewed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R-001 | [Risk Name] | [Category] | [2-sentence plain-English description of what could go wrong and how it would manifest] | [1=rare, 5=likely] | [1=minor, 5=catastrophic] | L x I | [Name/Role] | [Specific action being taken to reduce likelihood or impact] | [Accept if score ≤ 8; Escalate to VP if ≥ 9; Escalate to CTO if ≥ 16] | [Open/Mitigating/Accepted/Closed] | [Date] |

### Risk Score Reference

| Score | Action Required |
|---|---|
| 1–4 | Accept. Document and monitor. No active mitigation required. |
| 5–8 | Mitigate. Assign owner and 90-day action plan. Report in quarterly review. |
| 9–15 | Escalate to VP level. Active mitigation with monthly status. Include in leadership risk briefing. |
| 16–25 | Immediate escalation to CTO/CISO. Stop-work consideration. Executive decision required. |

---

## Example Entries (T-Mobile Notification Platform Context)

| ID | Risk Title | Category | Description | L | I | Score | Owner | Mitigation | Status |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | Single-region EKS dependency | Availability | All notification platform workloads run in us-east-1 EKS cluster. Regional AWS outage would cause complete platform unavailability. | 2 | 5 | 10 | SRE Director | Multi-region architecture in H2 roadmap. Manual failover runbook exists for partial traffic routing. | Escalated — VP aware, funded in H2 |
| R-002 | Cassandra cluster on EOL version | Reliability | Cassandra 3.11 reaches community EOL in 6 months. No security patches after that date. Upgrade path requires 6-week migration. | 3 | 4 | 12 | Platform Lead | Upgrade project scoped and in Q3 planning. Interim: no new keyspaces on affected nodes. | Mitigating |
| R-003 | On-call rotation below sustainability floor | People | Current rotation: 6 engineers. Industry floor is 8 for 24x7 ops. One attrition event drops to 5 — burn risk. | 3 | 3 | 9 | SRE Manager | Headcount request in progress. Cross-training 2 engineers from adjacent team as backup rotation. | Escalated — in headcount review |
| R-004 | No DR drill in 12 months | Compliance | DR plan exists on paper but has not been tested. Last confirmed RTO measurement: 18 months ago. Audit finding risk. | 4 | 3 | 12 | SRE Director | DR drill scheduled for Q3. Runbooks under review. | Mitigating |
| R-005 | Secrets rotation frequency below policy | Security | 23% of service account credentials have not been rotated in >90 days, violating the stated 90-day rotation policy. | 3 | 4 | 12 | Security Lead + SRE | Automated rotation via Vault in progress. Manual rotation sweep for critical accounts initiated. | Mitigating |
| R-006 | Deployment pipeline lacks SBOM generation | DevSecOps | No software bill of materials generated at build time. Cannot demonstrate supply chain compliance for enterprise customer audits. | 2 | 3 | 6 | DevSecOps Lead | Syft integration in CI pipeline scoped for Q3. | Open — in planning |

---

## Risk Categories Reference

Use these standard categories for consistent filtering and reporting:

- **Availability** — failures that could cause customer-facing outages
- **Reliability** — degraded performance short of full outage
- **Security** — vulnerabilities, compliance gaps, credential exposure
- **People** — attrition risk, key-person dependency, skills gaps
- **Dependency** — third-party vendor, upstream service, cloud provider risks
- **Compliance** — audit requirements, regulatory obligations, policy violations
- **Data** — integrity, retention, backup, privacy risks
- **Change** — risks introduced by deployment, configuration change, or migration
- **Capacity** — growth-driven resource exhaustion risks

---

## How to Communicate Risk to Executives (Translation Table)

| What You Say (Technical) | What They Hear | What to Say Instead |
|---|---|---|
| "Our Cassandra is on EOL version 3.11" | "Some database version thing" | "Our primary database for customer notifications reaches end of community support in 6 months. After that, known vulnerabilities won't be patched. We're mid-upgrade." |
| "We have a single-AZ EKS deployment" | "Something about cloud" | "A single AWS infrastructure failure would take our notification platform completely offline. We're building redundancy — it's funded for Q3." |
| "Our error budget is at 80% for the month" | "Numbers" | "We've used 80% of our reliability cushion for the month with 10 days remaining. We're in a cautious deployment mode until the month resets." |
| "We have a 12-hour RTO" | "Jargon" | "If we have a complete platform failure, our current recovery capability is 12 hours. For a payment notification platform, our target is 2 hours. That gap is the risk we're closing." |
| "We're missing SBOM generation in our pipeline" | "Pipeline something" | "We can't currently produce a complete inventory of the software components we ship. Enterprise customers and auditors are starting to require this." |

---

## Quarterly Risk Review Checklist (Director)

- [ ] Review all open risks — status current?
- [ ] Any new risks to add from incidents in the last quarter?
- [ ] Any risks that escalated in score since last review?
- [ ] Confirm mitigations are progressing on plan
- [ ] Present top 3 risks to VP in quarterly leadership review
- [ ] Archive closed risks (keep for audit trail — never delete)
- [ ] Update risk appetite statement if org priorities have shifted
- [ ] Send risk summary to CISO if any security-category risks are score 9+

---

*Template version: 1.0 | Owner: Vishweshwar Chippa | Created: 2026-06-11*
