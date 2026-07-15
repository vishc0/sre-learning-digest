# AT&T Dallas — Interview Q&A Prep

## RECRUITER SCREEN
**Q: Tell me about yourself.**
"I'm Vishweshwar Chippa, SRE Principal at T-Mobile for 10 years. I run 4 notification platforms — 25 million messages daily including legally-required communications — with 15 engineers. I've done every modernization AT&T is executing now: TIBCO to Spring Boot, VMs to Kubernetes, Oracle to MongoDB, all without downtime. I'm looking to bring that telecom domain expertise to AT&T in Dallas. I have an approved I-140, so the transfer is straightforward."

## HIRING MANAGER QUESTIONS

**Q: How have you managed compliance and regulatory notification requirements?**
"At T-Mobile, some of our messages have legal weight — fraud alerts, regulatory disclosures, data breach notifications. We treat these as a distinct delivery class with higher SLOs, separate monitoring, and mandatory audit trails. I built the suppression logic (DND domain) specifically to ensure we never suppress legally-required messages. I also implemented ML anomaly detection to flag abnormal suppression patterns that could indicate compliance risk. Zero compliance violations in 10 years."

**Q: How would you approach leading AT&T's notification platform modernization?**
"Start by mapping the current state — understand every upstream trigger, every downstream provider, every compliance obligation. Then define the target state — Kubernetes-native, cloud-hosted, observable. Then sequence migrations by risk: least critical first, build confidence, then tackle mission-critical. Parallel run every migration — old and new running simultaneously until the new one earns trust. That's how I did all 6 migrations at T-Mobile with zero customer impact."

**Q: How do you build a high-performing SRE team in a large enterprise?**
"Three things: ownership, visibility, and growth. Every engineer owns a platform — not as a job description but as pride of craft. Every platform's health is visible on a shared dashboard so poor health is never someone else's problem. Every engineer has a stretch project that's 20% above their current level. That combination created a team where incident response went from reactive firefighting to systematic reliability engineering."

## TECHNICAL QUESTIONS

**Q: How do you ensure 99.99% delivery for legally-required notifications?**
"Separate SLO class, dedicated monitoring, isolated delivery path. In production at T-Mobile:
- Legal messages bypass standard DND suppression logic entirely
- Dedicated retry queue with higher priority than marketing messages
- Delivery confirmation audit log written to immutable storage
- Real-time alert if delivery failure exceeds 0.01% for this message class
- Executive dashboard shows legal notification SLO separately from standard delivery"

**Q: What's your approach to on-call at scale for 4+ platforms?**
"Tiered ownership: each platform has a primary on-call owner. I'm the escalation path for Sev1 only. Runbooks are written for every known failure mode — on-call should spend 80% of time following a runbook, not improvising. Weekly on-call reviews identify any gaps in runbook coverage. Monthly postmortems eliminate the top-3 alert sources each month. Over 3 years this approach drove our Sev1 count to zero."

## QUESTIONS TO ASK
1. "Which notification platforms or product lines would this role focus on — consumer, FirstNet, enterprise?"
2. "What's the current state of the Kubernetes migration for the notification org?"
3. "How does AT&T structure SRE vs SWE responsibilities on the notification teams?"
