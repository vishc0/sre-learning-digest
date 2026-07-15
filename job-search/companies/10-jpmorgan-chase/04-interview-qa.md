# JPMorgan Chase — Interview Q&A

Q: How do you ensure notification reliability for mission-critical financial alerts?
"Same framework as my legally-required telecom notifications: separate SLO class, dedicated delivery path, immutable audit trail, ML anomaly detection for abnormal patterns. For JPM specifically, transaction alerts have a compliance dimension — a missed fraud alert has regulatory implications. I'd add a compliance validation layer that confirms every mandatory notification delivered, with escalation if delivery confirmation doesn't arrive within SLO window."

Q: How do you build SRE culture in a large financial institution?
"Start with visibility. When SLOs and error budgets are invisible, reliability is just a feeling. I'd build dashboards that show every team their SLO health in real time. Then connect reliability to business outcomes — a 1% delivery failure rate on fraud alerts is not an SRE metric, it's a risk management metric. When business stakeholders understand reliability in their language, SRE investment gets funded. Third: blameless postmortem culture — this is hardest in regulated industries where there's fear of documentation, but it's essential."

Q: Tell me about your banking experience.
"At Wachovia during the First Union merger I was Operations Lead, responsible for building new TIBCO environments while the existing infrastructure was under active M&A integration pressure. The lesson that shaped my whole career: when systems are changing, documentation and clear ownership become more important, not less. I applied that lesson every time T-Mobile underwent a major platform change — always document, always define an owner, always have a rollback plan."

QUESTIONS TO ASK: 1. What are the primary SLO challenges for JPMorgan's customer notification infrastructure? 2. How does the Plano campus SRE organization relate to New York headquarters from a platform ownership perspective?
