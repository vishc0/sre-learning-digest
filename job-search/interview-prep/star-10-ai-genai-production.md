# STAR Story 10: AI/GenAI in Production — Leadership Chat Agent and Anomaly Detection
## Domain: AI/ML Engineering / GenAI Leadership

---

## Situation

By 2024, T-Mobile's SRE organization was receiving growing pressure to demonstrate AI/GenAI capabilities in operational workflows. Two parallel tracks existed on my team: (1) the ML anomaly detection work using Splunk MLTK (established, proven — see STAR Story 03), and (2) a new initiative to build a GenAI-powered natural language interface for on-call engineers to query platform health without needing to write Splunk queries. The second initiative emerged from a specific pain point: junior engineers on the team could recognize that something was wrong on the Metrics dashboard, but they couldn't construct the Splunk queries needed to diagnose it. They were dependent on senior engineers for query authorship, which created a bottleneck at 2 AM during incidents.

## Task

My task on the anomaly detection work was to serve as the technical lead who translated operational domain knowledge into ML model design — I was not a data scientist, but I understood the failure modes deeply enough to specify what the models needed to detect, and I validated the models' output quality during the shadow period.

My task on the GenAI chat agent was broader: I proposed the initiative, defined the product requirements, led the integration design, and was responsible for the risk framework — specifically, what the agent could and could not do in a production context without human confirmation.

## Action (IC Technical Depth — Anomaly Detection)

I covered the MLTK anomaly detection work in detail in STAR Story 03. The leadership dimension here: the decision to use MLTK rather than building a standalone Python-based ML pipeline was deliberately about operational continuity. A Python pipeline would have required a new skill set, a new deployment footprint, and a new on-call responsibility. MLTK ran inside Splunk — a tool the team already owned and operated. The slightly lower model sophistication of MLTK vs. a custom sklearn model was worth the operational simplicity. I made that tradeoff explicitly and documented it.

The other leadership decision: I refused to let the models go to production on-call until they passed 45 days of shadow validation with manual TP/FP classification. Several engineers wanted to ship faster. I held the line. An untrusted AI alert layer would have made alert fatigue worse, not better. The value of an anomaly detection system depends entirely on the trust it earns. Trust is earned by shipping only after validation, not before.

## Action (IC Technical Depth — GenAI Chat Agent)

The GenAI chat agent was built using a RAG (Retrieval-Augmented Generation) architecture: a large language model with access to our Splunk search API, our runbook documentation, and a structured catalog of our platform's known failure modes. The architecture was:

1. **Engineer submits natural language query** — "Why is message delivery rate dropping on the push channel?"
2. **Query classifier** — LLM categorizes the query as diagnostic (retrieve current metrics), historical (search past incidents), or knowledge (retrieve runbook/documentation)
3. **Retrieval layer** — for diagnostic queries, the system generated a Splunk query, executed it, and returned results; for historical, it searched postmortem documents; for knowledge, it retrieved relevant runbook sections
4. **Response synthesis** — LLM synthesized retrieved context into a structured response: here's what I found, here's what it means, here's the runbook step that applies

The risk framework was the most important design decision. I classified all agent actions into three tiers:
- **Tier 1 (autonomous)**: Read-only queries — the agent could execute Splunk searches, retrieve dashboard data, pull postmortem history without any confirmation
- **Tier 2 (confirm-then-act)**: Configuration reads and state inspection — e.g., checking current consumer count, reading Kubernetes pod status. Allowed after one-click confirmation in Slack
- **Tier 3 (human-only, always)**: Any action that modifies state — scaling consumers, triggering rollbacks, changing configuration. The agent could not do these. It could only surface information and recommend. The action had to be taken by a human engineer.

I made Tier 3 an architectural constraint, not a policy. The agent had no write permissions to any production system. This was deliberate: GenAI systems hallucinate. The cost of a hallucination on a read query is a confusing answer. The cost of a hallucination on a write action is a production incident. The risk profile is asymmetric. We never gave the agent the ability to make things worse.

The agent was deployed to the team's Slack workspace in a private channel accessible to on-call engineers. We ran a 30-day pilot with all queries logged and manually reviewed weekly. Engineers were required to mark responses as helpful/not helpful and note any hallucinations.

## Result

**Anomaly Detection:**
- Alert volume: 40,000+/month → under 4,000/month
- MTTD: 47 minutes → under 8 minutes
- Precision: 88%+ across all production models
- (Full metrics in STAR Story 03)

**GenAI Chat Agent:**
- Pilot period: 30 days, 340 queries logged
- Response accuracy rate: 91% (marked helpful by on-call engineer)
- Hallucination rate: 4% (14 of 340 queries — all Tier 1 read-only, no production impact)
- Most frequent query type: "what's the current queue depth trend for the last 4 hours" — Splunk syntax that junior engineers previously needed senior help to construct
- Measurable outcome: incidents requiring senior escalation for diagnostic query authorship dropped from ~35% to under 10% during the pilot period
- Agent is now in production use on the notification platform SRE team

---

## Director/VP Version (Leadership Framing)

"I led two distinct AI/ML initiatives: a validated anomaly detection layer that reduced MTTD by 83%, and a GenAI chat agent that democratized Splunk query authorship for junior on-call engineers. The leadership decisions on both were the same: validate rigorously before trusting operationally, and be explicit about what the AI can and cannot do autonomously. On the chat agent, I made Tier 3 — any write action — architecturally impossible for the agent, not just policy-constrained. GenAI systems make mistakes. The cost of a read-query mistake is a confusing answer. The cost of a write-action mistake is a production incident. I treat that risk asymmetry as a design constraint, not a configuration option. The outcome is an AI system the team trusts because they know its failure modes."

## IC Version (Technical Depth)

"The GenAI chat agent used a RAG architecture with three retrieval sources: Splunk search API, postmortem documents, and runbook catalog. I built a query classifier layer to route queries to the appropriate retrieval path rather than mixing diagnostic and knowledge retrieval in a single RAG call — that separation improved answer precision significantly. The risk framework was architecturally enforced: the agent had read-only IAM permissions to Splunk, read-only Kubernetes API access, and no write access to any system. The 4% hallucination rate in the pilot was entirely in Tier 1 read queries — wrong or misleading interpretations of metric data, not dangerous actions. All were caught by the 'mark helpful/not helpful' feedback loop and used to tune the synthesis prompt."

---

## 30-Second Version

"I led two AI/ML production deployments: MLTK-based anomaly detection that reduced MTTD from 47 minutes to under 8, and a RAG-based GenAI chat agent that lets junior on-call engineers query platform health in natural language instead of Splunk syntax. The agent is architecturally read-only — no write permissions to any production system by design. Pilot: 91% response accuracy, 4% hallucination rate, senior escalation for diagnostic queries dropped from 35% to under 10%."

---

## 2-Minute Version

"I've run two AI/ML initiatives in production, and the leadership story behind both is the same: validate rigorously before trusting operationally, and be explicit about the failure modes before you ship.

The anomaly detection work used Splunk MLTK — temporal baseline models, 45-day shadow validation period, 88% precision threshold before going on-call. The key decision was to use MLTK rather than a custom Python pipeline. Slightly less model sophistication, but it runs inside Splunk, which the team already owns and operates. Simpler to maintain, simpler to troubleshoot. I made that tradeoff explicitly.

The GenAI chat agent was newer and riskier. The problem it solved was real: junior on-call engineers could see something was wrong on the dashboard but couldn't write the Splunk queries needed to diagnose it. That's a 2 AM dependency on senior engineers. I built a RAG-based agent with natural language query input, Splunk retrieval for diagnostics, postmortem search for historical patterns, and runbook retrieval for action guidance.

The risk framework was the most important design decision. I classified all agent actions into three tiers: read-only queries autonomous, configuration inspection with one-click confirmation, and write actions — scaling, rollback, configuration changes — architecturally impossible for the agent. No write permissions. Ever. GenAI systems hallucinate. The cost of a hallucination on a read query is a confusing answer. The cost of a hallucination on a write action is a production incident. That risk asymmetry is a design constraint, not a setting.

Pilot results: 340 queries, 91% helpful response rate, 4% hallucination rate, all read-only, no production impact. Senior escalation for Splunk query authorship dropped from 35% to under 10%. The agent is in production. The team trusts it because they know exactly what it can and can't do."

---

## Key Metrics to Remember
- Anomaly detection: 40,000+ → under 4,000 alerts/month, 47 min → under 8 min MTTD
- GenAI pilot: 340 queries, 91% helpful, 4% hallucination (all read-only)
- Escalation reduction: 35% → under 10% for diagnostic query authorship
- Architecture: RAG with Splunk API + postmortem docs + runbook catalog
- Risk tiers: Tier 1 autonomous (read), Tier 2 confirm-then-act (state inspection), Tier 3 human-only (all writes)
- Architectural enforcement: agent has zero write permissions to any production system
- Key principle: hallucination on read = confusing answer; hallucination on write = production incident
- Shadow validation: 45 days for ML models, 30-day pilot for GenAI agent
