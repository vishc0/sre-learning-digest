# Audit Readiness Playbook — Director Level
## How to Prepare Your Team for Compliance Audits Without Panic

---

## The Director's Framing

Most teams fail audits not because they are insecure or non-compliant. They fail because they cannot **demonstrate** compliance. The auditor does not accept "we do this" — they require evidence.

The Director's job is to build the systems that produce evidence continuously, so that audit preparation is not a crisis sprint — it is a documentation exercise.

**Analogy from operations**: An audit is like an incident postmortem run by someone outside your organization. They are reading your logs. If your logs are clean, complete, and consistently formatted, the postmortem is fast and favorable. If your logs are gaps, overwrites, and tribal knowledge, you have a problem regardless of what actually happened.

---

## Audit Types Directors Will Face

| Audit Type | Who Runs It | What They Look For | Typical Frequency |
|---|---|---|---|
| SOC 2 Type II | External auditors (e.g., KPMG, Deloitte) | Continuous operation of controls over 3-12 months | Annual |
| ISO 27001 | External certification body | ISMS implementation and risk management program | Annual (initial) + surveillance |
| PCI DSS | Qualified Security Assessor (QSA) | Cardholder data environment controls | Annual |
| HIPAA | OCR or external auditor | PHI handling controls, access management | Variable — triggered by incident or contract |
| Internal Audit | Company's internal audit team | Policy compliance, change management, access reviews | Quarterly or annual |
| Customer Security Review | Enterprise customer's security team | Your security posture relative to their requirements | Per contract |
| FedRAMP | 3PAO (Third Party Assessment Organization) | Federal security controls (NIST SP 800-53) | Annual + continuous monitoring |

---

## The Audit-Ready Operating Model

### Principle: Evidence Is Created During Normal Operations, Not Before Audits

If you need to scramble before an audit, your normal operations do not produce evidence. Fix the process, not the audit prep.

The evidence that auditors want is almost identical to the evidence that Directors want for reliability governance:
- Who has access to what, and was that access reviewed?
- What changes were made, when, and who approved them?
- When did incidents occur, what happened, and what was done about it?
- Are policies written down and are they being followed?
- Are vulnerabilities being tracked and remediated on schedule?

If you already answer these questions continuously for operational purposes, audit preparation is a matter of presenting existing data — not creating new evidence.

---

## Core Control Areas Directors Own

### 1. Access Control and Privilege Management
**What auditors look for**: Who has privileged access? When was access last reviewed? How are accounts deprovisioned when people leave?

**Director governance actions**:
- Quarterly access review: every privileged account reviewed by the account owner's manager
- Automated deprovisioning: when HR records an offboard, all access is removed within 24 hours (with a control log proving it)
- Break-glass accounts: all emergency privileged accounts are logged, time-limited, and reviewed after use
- Principle of least privilege: documented in policy; spot-checked quarterly

**Evidence produced**: Access review tickets, offboarding checklists, audit logs of privileged access activity, break-glass usage log.

### 2. Change Management
**What auditors look for**: Is there a formal change process? Is it being followed? Are changes approved, tested, and documented?

**Director governance actions**:
- Change register with approval trail (see Change Governance Framework)
- Automated gate: no deployment to production without a passing CI run and a logged approval
- Separation of duties: the person who writes the code cannot be the sole approver of its production deployment
- Emergency change documentation: all Tier 0 (emergency) changes documented within 24 hours

**Evidence produced**: Change records with approvals, CI/CD logs, deployment audit trail, CAB meeting minutes.

### 3. Vulnerability Management
**What auditors look for**: Are vulnerabilities tracked? Is there a remediation timeline and is it being met?

**Director governance actions**:
- Vulnerability SLA policy (written, approved by CISO or VP):
  - Critical/P0: patch within 24 hours or document compensating control
  - High/P1: patch within 72 hours
  - Medium/P2: patch within 14 days
  - Low/P3: patch within 90 days
- Automated scanning: container images scanned at build time; results in CI pipeline
- SCA (Software Composition Analysis): dependency vulnerabilities tracked and assigned owners
- Monthly vulnerability summary report: open count by severity, trend, top items by age

**Evidence produced**: Scan results, remediation tickets with open/close dates, trend reports, exception log for accepted risks.

### 4. Incident Management and Response
**What auditors look for**: Is there a documented incident response process? Is it tested? Are incidents tracked and closed with root cause?

**Director governance actions**:
- Incident response plan: written, current, accessible (not buried in a wiki that nobody knows exists)
- Incident register: all P0 and P1 incidents logged with: date, duration, customer impact, root cause summary, corrective actions
- Postmortem completion rate: all P0/P1s receive a completed postmortem within 72 hours
- Tabletop exercise: annual at minimum, semi-annual for high-compliance environments

**Evidence produced**: Incident tickets, postmortem documents, tabletop exercise records, incident response plan with revision history.

### 5. Backup and Recovery
**What auditors look for**: Do backups exist? Are they tested? Is the RTO/RPO achievable?

**Director governance actions**:
- Backup policy: written, specifying frequency, retention, and scope per data class
- Backup test cadence: restores tested quarterly; results documented
- DR drill: full recovery exercise at least annually; results and findings documented
- RTO/RPO defined per service tier and reviewed annually against actual drill results

**Evidence produced**: Backup job logs, restore test records, DR drill results, RTO/RPO documentation.

### 6. Security Awareness and Training
**What auditors look for**: Have engineers received security training? Is training tracked?

**Director governance actions**:
- Annual security training completion tracked by HR or LMS system
- Phishing simulation results tracked and acted on (not just run)
- Security training completion rate: target 100% before audit; >95% is acceptable

**Evidence produced**: LMS completion reports, phishing simulation results, training completion attestations.

---

## Pre-Audit Checklist (Director Runs This 90 Days Out)

### 90 Days Before Audit
- [ ] Identify audit scope: which systems, which controls, which time period?
- [ ] Assign a single internal audit coordinator (not the Director — delegate to a Senior SRE or Security Lead)
- [ ] Run a gap assessment against the audit framework — use last year's findings as a starting point
- [ ] Stand up the evidence collection tracker (see template below)
- [ ] Identify any known gaps and estimate closure time — can they be closed before audit, or will they require a remediation plan?
- [ ] Communicate to VP: here is our readiness assessment, here are the gaps, here is the plan

### 60 Days Before Audit
- [ ] Access review cycle complete — quarterly review done, results documented
- [ ] Vulnerability backlog reviewed — any items that exceed SLA need a documented exception or emergency remediation
- [ ] Change register is current and complete — spot check 10 recent changes for documentation quality
- [ ] All P0/P1 postmortems from the audit period are complete — no open postmortems without a closed or tracked status
- [ ] DR documentation is current — last drill recorded, RTO/RPO targets documented

### 30 Days Before Audit
- [ ] Evidence packages assembled for each control area
- [ ] Internal walkthrough with the audit coordinator — simulate the auditor's questions
- [ ] Any identified gaps: document as accepted risks or remediation-in-progress with executive sign-off
- [ ] Prepare team briefing: who talks to the auditor, about what, and what they do not speculate on
- [ ] Confirm audit logistics: auditor access, meeting schedules, document sharing portal

### During the Audit
- [ ] Single point of contact for auditor document requests (the coordinator, not engineers)
- [ ] Engineers available for technical questions on scheduled windows — not pulled ad hoc
- [ ] Daily debrief between Director and coordinator: what was asked, what was provided, any red flags
- [ ] Do not speculate: if auditor asks something the coordinator does not know, the answer is "let me confirm and get back to you today"
- [ ] No new evidence creation after the audit starts — only produce what exists; do not backfill

---

## Evidence Collection Tracker Template

| Control Area | Evidence Type | Location | Coverage Period | Status | Owner |
|---|---|---|---|---|---|
| Access Management | Quarterly access review records | [Link to ticketing system] | [Audit period dates] | Complete / In progress / Gap | [Name] |
| Change Management | Change register with approvals | [Link to ITSM] | [Audit period dates] | | |
| Vulnerability Management | Scan results + remediation tickets | [Link to scan tool] | [Audit period dates] | | |
| Incident Response | P0/P1 incident tickets + postmortems | [Link to wiki/ITSM] | [Audit period dates] | | |
| Backup/Recovery | Backup job logs + restore test records | [Link] | [Audit period dates] | | |
| Security Training | LMS completion report | [Link to HR system] | [Audit period dates] | | |
| DR | DR drill results + RTO/RPO documentation | [Link to wiki] | [Last drill date] | | |
| Policy Documentation | Current versions of all applicable policies | [Link to policy library] | [Last review date] | | |

---

## How to Brief Your Team Before an Auditor Interview

Brief engineers on three rules:

**Rule 1: Answer the question that was asked. Do not elaborate.**
"Do you log privileged access?" Answer: "Yes. Logs are in [system], retained for [period], reviewed quarterly." Do not volunteer information about gaps in adjacent controls.

**Rule 2: When you don't know, say so and offer to follow up.**
"I'm not the right person to speak to that specific control — let me connect you with [name] who owns it." Never speculate. Speculation creates findings.

**Rule 3: If you are asked about a gap, be honest.**
Auditors are experienced at detecting evasion and it creates trust problems. If a control is not in place, the correct answer is: "We identified this gap in [month]. Here is our remediation plan and timeline." A known gap with a plan is a finding. A known gap hidden from an auditor can be a major finding.

---

## How Directors Communicate Audit Outcomes to Leadership

### Pre-Audit Readiness Briefing (VP Level)
```
AUDIT READINESS SUMMARY — [Audit Type] [Date]
Overall readiness: [Green / Yellow / Red]
Audit period: [Dates]
Auditor: [Firm / Team]

CONTROL STATUS
[Green controls]: [N] controls — fully evidenced
[Yellow controls]: [N] controls — evidence in progress, expected complete by [date]
[Red controls / gaps]: [N] items — [description of gap and remediation plan]

KEY RISKS
[Any gaps that may generate audit findings, with mitigation plan]

WHAT I NEED FROM YOU
[Any sign-off, resource, or escalation needed before audit date]
```

### Post-Audit Results Briefing
```
AUDIT RESULTS SUMMARY — [Audit Type] [Date Completed]
Result: [No findings / N minor findings / N major findings / N critical findings]

FINDINGS SUMMARY
[List each finding with: severity, description in plain English, owner, remediation deadline]

WHAT WE ARE DOING
[Remediation plan with owners and dates for each finding]

WHAT THIS MEANS
[Plain language assessment: are we compliant? Are there contractual or regulatory consequences?]

TIMELINE TO FULL REMEDIATION
[Date by which all findings are expected closed]
```

---

## Security Governance for Directors Who Are Not Security Engineers

You own the security posture of your platform. You do not need to be a security engineer to govern it well. You need to:

1. **Know your attack surface**: what services are internet-facing, what data classes they handle, what credentials they use
2. **Own the vulnerability metrics**: track open CVE counts by severity the same way you track SLO metrics
3. **Enforce the patch SLA**: treat a CVE that has breached SLA the same way you treat an SLO breach — with urgency and escalation
4. **Partner with the CISO, not resist them**: bring security into postmortems; invite the CISO team to your quarterly reliability review
5. **Make security a shared OKR with the CISO team**: "CISO team and SRE co-own: zero P0 CVEs unpatched beyond SLA"
6. **Establish a security champion on your team**: one engineer with a security focus who bridges SRE and security, attends both teams' planning sessions

The CISO's biggest fear about engineering teams is that they will deploy without thinking about security consequences. The best way to address that fear is to demonstrate that your team tracks, prioritizes, and remediates security issues with the same discipline they apply to reliability.

---

*Playbook version: 1.0 | Owner: Vishweshwar Chippa | Created: 2026-06-11*
