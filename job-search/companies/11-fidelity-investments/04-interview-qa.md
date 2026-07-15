# Fidelity Investments — Interview Q&A

**Q: How is financial services SRE different from telecom SRE?**
"The operational principles are the same — SLOs, incident command, postmortem culture, capacity planning. The differences are in the compliance layer and the definition of 'mission-critical.' At T-Mobile, missing a legal notification has regulatory risk. At Fidelity, a failed trade confirmation has financial and regulatory risk. In both cases, I treat these message classes with separate SLOs, dedicated monitoring, immutable audit trails, and compliance-specific runbooks. The discipline transfers; I'd need to learn the specific financial regulations, but the operational framework I'd build is identical."

**Q: How do you handle a situation where a business stakeholder demands a change that increases reliability risk?**
"I quantify the risk and present it as a decision, not a veto. 'This change increases our Sev1 probability by X% based on similar changes in the past. If we proceed without the additional testing window, the risk window is Y days. If we add a 2-week canary period, the risk drops to Z%. Which do you want?' When stakeholders see the risk quantified, they almost always choose the safer path. If they still push forward, I document the decision, implement the change with extra monitoring, and have a rollback plan ready."

**Q: Tell me about your experience in a regulated environment.**
"T-Mobile operates under FCC regulations for notification delivery, with specific requirements around customer consent (DND/opt-out) and legal message delivery. I built the compliance layer: suppression governance with audit trails, ML anomaly detection for regulatory risk signals, separate message class handling for legally-required communications. Zero compliance violations in 10 years. The principles — document every decision, enforce policies in code not process, audit everything — apply directly to financial services regulation."

## QUESTIONS TO ASK
1. "What's the technology stack for Fidelity's customer notification infrastructure?"
2. "How far along is the mainframe modernization program, and would this role be involved in that work?"
3. "What does a SRE Director's day-to-day look like at Fidelity — more strategic or operational?"
