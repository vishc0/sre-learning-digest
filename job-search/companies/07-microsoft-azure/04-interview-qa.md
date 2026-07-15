# Microsoft Azure — Interview Q&A Prep

## RECRUITER SCREEN

**Q: Tell me about yourself.**
"I'm Vishweshwar Chippa, currently SRE Principal at T-Mobile. I manage four production notification platforms processing 25 million messages daily with a team of 15. Over the past 10 years I've maintained 99.99% availability and led six major zero-downtime platform migrations, including a full Kubernetes and cloud migration. What's unique is that I've built AI into my SRE practice — anomaly detection, natural language metrics agents, and AI-assisted tooling for the team. I'm targeting Principal SRE roles at Microsoft because Azure's direction with AI-driven reliability aligns with work I'm already doing."

**Q: Why Microsoft?**
"Microsoft's commitment to growth mindset culture resonates with how I operate — I've reskilled from TIBCO middleware to Spring Boot to Kubernetes to AI tooling over 10 years. Azure's scale and the opportunity to apply AI to reliability engineering at cloud scale is exactly where I want to take my career. Plus, Microsoft's approach to responsible AI principles mirrors how I've built ML tooling in production — with constraints, observability, and human validation in the loop."

## HIRING MANAGER SCREEN

**Q: Describe a time you influenced without authority.**
"During our TIBCO-to-Spring-Boot migration, I had no authority over the 42 downstream teams whose integrations we were changing. Without buy-in, we'd have caused cascading failures post-migration. I built a voluntary integration test group, created a shared contract document for each integration, and ran joint testing sessions. All 42 teams participated. Migration went live with zero downstream failures. The lesson: show stakeholders exactly what they risk if they don't engage — then make engagement easy."

**Q: Tell me about a time you failed and what you learned.**
"Early in our Kubernetes migration we underestimated the impact of a pod autoscaler configuration change. During a high-volume event, the scaler throttled too aggressively and we had a 45-minute message delivery degradation — below SLO. I owned the postmortem completely. The fix was adding load-test gates to our release pipeline specifically for autoscaler configs. We've never had an autoscaler-related incident since. The lesson: migrate infra config changes with the same rigor as code changes."

**Q: How do you balance reliability with developer velocity?**
"I use SLO burn rate as the arbiter. If we're burning error budget slowly, velocity gets priority — teams deploy freely. If burn rate accelerates, I institute a feature freeze and a reliability sprint. The key is making the budget visible to everyone, not just the SRE team. When developers can see the burn rate on a shared dashboard, they self-regulate. I've found that transparency beats gatekeeping every time."

## TECHNICAL QUESTIONS

**Q: How would you build an observability strategy for a platform migrating from on-prem to Azure?**
"Three-phase approach: 
Phase 1 — Instrument before migrating. Deploy Azure Monitor agents alongside existing Splunk setup. Run both in parallel so you have baseline comparisons.
Phase 2 — Define SLOs before cutover. If you don't know what 'healthy' looks like in metrics form, you can't know when migration breaks something.
Phase 3 — Create synthetic canary transactions that run the full path — from intake through processing through delivery — and alert if any step degrades. This catches infrastructure issues before users report them.
I applied this pattern at T-Mobile for our Kubernetes migration — ran parallel observability for 8 weeks before cutting over."

**Q: How do you handle a situation where your SLO is met but users are complaining?**
"This means your SLO is wrong. Users experiencing pain that metrics don't capture is a measurement gap, not a performance gap. I'd run a user journey analysis — trace actual user complaints through the system and find which metric correlates. At T-Mobile we had a case where our SLO tracked delivery latency but not suppression false positives. Users were getting 'message not delivered' when actually it was suppressed incorrectly. We added a suppression accuracy SLO, which led to the ML anomaly detection work."

## QUESTIONS TO ASK
1. "How does the Azure SRE organization approach the integration of AI tooling into operational workflows? Are there specific initiatives I'd be contributing to?"
2. "What's the breakdown between IC track and people management track for Principal SRE at IC5/IC6?"
3. "How does this team's SRE work connect to external Azure customer SLAs?"
