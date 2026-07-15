# Role 06 — Manager, SRE — Information Security

> ⚠️ **POSTING STATUS UNCERTAIN.** Direct fetch returned 404 on 2026-05-07 — this requisition may have been pulled. **Confirm via recruiter or live Apple careers search before tailoring an application.** Tailored materials below assume the JD as indexed; revise once you confirm the live posting.

## Job metadata
- **JD URL (last known):** https://jobs.apple.com/en-us/details/200624759-3278/manager-site-reliability-engineering-information-security
- **Requisition ID:** 200624759-3278
- **Team:** Information Security — SRE
- **Location:** Not retrieved
- **Posted base salary:** Not retrieved. Apple InfoSec Manager band typically ≥$200K base in CA/WA. Confirm on live JD.
- **Match score:** **80%** (lowest of the 6, but still pursue-worthy)

## Why this role
The intersection of SRE leadership and Information Security maps cleanly to your T-Mobile work: Vault + CyberArk in production, Cybersecurity Syndicate reviews, vulnerability remediation programs, and zero critical vulnerabilities in production for 18 consecutive months. You are not a pure-play security engineer — but you are a security-aware SRE leader, which is what InfoSec SRE rolls hire for.

## What matched
- **InfoSec SRE leadership** → Cybersecurity Syndicate reviews; vulnerability remediation programs across 4 platforms; **zero critical vulnerabilities in production for 18 months**
- **Production secrets / privileged access management** → **Vault deployed and operationalized** across all 4 platforms; **CyberArk PAM** for privileged access control
- **Security scanning in CI/CD** → Aqua container scanning + SonarQube static analysis + AppScan in GitLab pipelines as mandatory promotion gates
- **SRE leadership scope** → 15 reports, MART framework, 99.99% availability, on-call command for Sev1/Sev2
- **Compliance posture** → SAFe governance; immutable audit trails for legally-required notifications; zero compliance violations in 10 years
- **Incident command** → defined runbooks, postmortem culture, root-cause elimination — directly transferable to security incident response

## Gaps
1. **Not pure-play security engineer** — security is a stripe across your work, not the headline
2. **Posting status uncertain** (404 on retry)
3. **No SIEM-as-product experience** (you use Splunk for ops, not as a SOC primary)
4. **No specific Apple-style threat-modeling / red-team exposure**

## Gap mitigation
1. Reframe → "I run security-by-default in a regulated comms platform" with Vault / CyberArk / Aqua / SonarQube / AppScan evidence; cite the 18-month zero-critical-vulnerability streak as the headline number
2. Posting → recruiter confirmation before any application work; if delisted, redirect effort to roles 01–03
3. SIEM → emphasize Splunk depth (MART, MLTK, custom dashboards) as cross-applicable to security analytics; Splunk-as-SIEM is a small extension of Splunk-as-observability
4. Threat modeling → mention OWASP / STRIDE awareness in cover letter; complete a focused threat-modeling refresh in 30 days if you advance to loop

## Pre-application checklist
- [ ] **First: recruiter check that this requisition is still open**
- [ ] If open: confirm posted base range on live JD (must be ≥$200K floor)
- [ ] Refresh threat-modeling fundamentals (OWASP Top 10, STRIDE)
- [ ] LinkedIn outreach to one Apple InfoSec engineer

---

# TAILORED RESUME

## VISHWESHWAR CHIPPA
**SRE Manager | Information Security Operations | Vault + CyberArk in Production | Compliance-Aware Reliability**

Atlanta, GA → Open to relocate per role | Chippa.Vishweshwar@gmail.com | 516-915-0046
H1B active · I-140 Approved (June 2016) · AC21 portable

---

## PROFESSIONAL SUMMARY
SRE Manager with 21+ years operating large-scale platforms with security as a first-class engineering requirement. At T-Mobile, lead a **15-person SRE team** managing 4 production platforms processing **25M+ messages/day** with **99.99% availability** and **zero critical vulnerabilities in production for 18 consecutive months**. Deployed Vault and CyberArk in production across all 4 platforms; embedded Aqua / SonarQube / AppScan as mandatory CI/CD gates; led Cybersecurity Syndicate reviews; built immutable audit trails for legally-required messages with zero compliance violations in 10 years. Seeking InfoSec SRE Manager role at Apple to apply security-aware SRE leadership at Apple's privacy-and-security bar.

---

## CORE COMPETENCIES (InfoSec SRE alignment)
Security-First SRE Operations · Vault + CyberArk Production Deployment · CI/CD Security Gating
Cybersecurity Syndicate Review Leadership · Vulnerability Remediation Program Ownership
Compliance Audit-Trail Design · 15-Person SRE Team Leadership · Incident Command at Scale

---

## TECHNICAL SKILLS (mapped to JD)
**Secrets / PAM:** **Vault (production deployment across 4 platforms)**, **CyberArk PAM** for privileged access, IAM, TKE, dynamic database credentials
**Security Scanning in CI/CD:** **Aqua** (container), **SonarQube** (static analysis), **AppScan** (DAST) — all as mandatory promotion gates in GitLab CI/CD
**Observability / Splunk-as-Security:** **Splunk (deep — MART framework author, MLTK anomaly detection, custom dashboards, SLO burn-rate calculations)** — directly extensible to SIEM patterns
**Cloud / Compute:** AWS (EKS, Lambda, SQS, SNS); Kubernetes (production at 25M-msg-per-day); Docker; PCF
**Languages:** Python (primary — built ML anomaly detection, AI agents, automation), Java, Kotlin, JavaScript
**Compliance:** SAFe governance, immutable audit-trail design, log classification tiers (technical / business / customer-data — never logged)
**Currently leveling up:** Threat modeling refresh (OWASP Top 10, STRIDE)

---

## PROFESSIONAL EXPERIENCE

### T-Mobile | SRE Principal · DevSecOps · Product Owner | *Dec 2015 – Present*
4 platforms · 25M+ msgs/day · **15 direct reports** · Cybersecurity Syndicate compliant · 99.99% availability

**Information Security Operations (InfoSec SRE alignment)**
- Deployed and operationalized **Vault** for secrets management across all 4 platforms; integrated **Vault Agent Injector pattern** so secrets are injected as files into pods via init containers, not environment variables
- Implemented **CyberArk PAM** for privileged access control across the SRE team and platform infrastructure
- Embedded **Aqua container scans, SonarQube static analysis, AppScan DAST** as mandatory promotion gates in GitLab CI/CD; **zero critical vulnerabilities in production for 18 consecutive months**
- Led **Cybersecurity Syndicate reviews** for all 4 platforms; quarterly cadence; closed all findings within remediation SLAs
- Designed **dynamic Vault secrets** for database credentials with automated rotation; eliminated static credentials from deployment pipelines

**Compliance & Audit-Trail Design**
- Governed compliance-aware notification delivery for legally-mandated messages; built immutable audit trails for regulatory requirements; **zero compliance violations in 10 years**
- Designed log classification tiers — Tier 1 (technical metrics, log everything), Tier 2 (business events, log with care), Tier 3 (customer data, never in logs) — directly applicable to Apple privacy posture
- Passed internal audit on DND domain with zero findings after self-identifying gap and implementing immutable suppression-decision logging

**SRE Leadership & Operating Model**
- Lead **15-person onshore + offshore SRE team**; on-call rotation, escalation, incident command for 24/7 coverage
- Maintained **99.99% availability** and **zero customer-impacting Sev1s** over 36 consecutive months
- Authored **MART (Monitoring/Alerting/Reporting/Troubleshooting)** framework adopted across notification ecosystem; ~40% MTTR reduction
- Built **Splunk MLTK ML anomaly detection** in production; pattern is directly transferable to security-event anomaly detection

**Security-Adjacent Migrations**
- Led **Bitbucket → GitLab** migration consolidating CI/CD security tooling
- Led 6 zero-downtime platform migrations including **APIGEE → MEG/TAG proxies** (L7 traffic plane); zero security regressions across all transitions

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

> "I'm Vishweshwar Chippa, SRE Principal at T-Mobile. Security has been a stripe across my work for a decade — I deployed Vault and CyberArk in production for all 4 of my platforms, embedded Aqua, SonarQube, and AppScan as mandatory CI/CD gates, and we've had zero critical vulnerabilities in production for 18 months. I lead Cybersecurity Syndicate reviews. I'm not a pure-play security engineer — but I'm a security-aware SRE leader of 15 engineers running platforms at 99.99% availability, which is exactly what an InfoSec SRE Manager role hires for. Approved I-140."

# COVER LETTER OPENER

> Dear Apple Information Security Hiring Team,
>
> The InfoSec SRE Manager role asks for an SRE leader who treats security as a first-class engineering requirement. That has been my operating model at T-Mobile for a decade. I deployed Vault and CyberArk in production across 4 platforms; I embedded Aqua, SonarQube, and AppScan as mandatory promotion gates in GitLab CI/CD; we have had zero critical vulnerabilities in production for 18 consecutive months; I lead the Cybersecurity Syndicate reviews; and I built immutable audit trails for legally-required notifications with zero compliance violations in 10 years. I lead 15 SRE engineers across 4 platforms at 99.99% availability for 36 consecutive months. I have an approved I-140 (June 2016 priority date), making any H1B transfer routine.
