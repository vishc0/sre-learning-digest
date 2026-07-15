# Charles Schwab — Interview Q&A Prep

## KEY BEHAVIORAL QUESTIONS

**Q: How have you managed platform reliability during a major merger or acquisition integration?**
"While not a merger per se, T-Mobile's acquisition of Sprint created integration requirements across notification systems — we had duplicate platforms serving the combined customer base. I led the consolidation: mapped every dependency, ran parallel delivery for 6 months, then cut over by customer segment. Zero customer-impacting outages during a 14-month integration. The principle: never cut over to the new system until it has earned the same trust as the old one, measured by real production metrics."

**Q: How do you approach security compliance in a regulated financial environment?**
"Compliance is a first-class SRE requirement, not an afterthought. In my framework: secrets in Vault, no static credentials anywhere, all deployments through CI/CD with mandatory security scans (Aqua, SonarQube), audit trails for every privileged operation. At T-Mobile I manage DND compliance for legally-mandated message governance — functionally similar to FINRA notification requirements. Results: zero critical vulnerabilities in production, clean Cybersecurity Syndicate reviews."

**Q: TIBCO migration — walk me through your approach.**
"TIBCO migrations are risk-heavy because the existing system is often undocumented and deeply integrated. My approach: 
1. Document everything first — every flow, every downstream consumer, every exception handler
2. Build the Spring Boot equivalent in parallel — don't modify the TIBCO flow
3. Shadow traffic — run both systems, compare outputs for 4-8 weeks
4. Migrate by consumer — cut over downstream systems one at a time
5. Keep TIBCO as hot standby for 3 months post-migration

That methodology produced zero downstream failures across 12 T-Mobile applications."

## QUESTIONS TO ASK
1. "What's the current state of the TD Ameritrade platform integration — are there active TIBCO systems still in the critical path?"
2. "How does Schwab's SRE organization relate to the fintech compliance teams for FINRA/SEC requirements?"
3. "Is this role focused on brokerage trading systems, or notification/customer engagement infrastructure?"
