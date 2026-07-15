# Salesforce — Interview Q&A

Q: What operational challenges have you encountered running MuleSoft at enterprise scale?
"Three real ones from production: (1) Mule runtime memory management under high concurrency — flows with heavy DataWeave transformations can spike heap usage during traffic bursts; we added JVM monitoring to our Splunk dashboards and set proactive GC alerts. (2) Object store clustering in multi-node environments — replication lag during failover caused state inconsistencies; we worked around it with external Redis-backed state. (3) Connector retry logic — MuleSoft's default retry behavior can cause thundering herd problems on downstream APIs; we implemented custom backoff policies. These are the real production problems your SRE team should be monitoring."

Q: How do you approach SRE for an integration platform that many customers depend on?
"Same as multi-tenant SaaS: tenant isolation monitoring, tiered SLOs by customer tier, blast radius mapping per component, and synthetic canary transactions per integration pattern. For MuleSoft specifically, the integration patterns themselves need reliability classification — synchronous REST calls have different SLO profiles than async event-driven flows."

QUESTIONS TO ASK: 1. Is this role supporting MuleSoft infrastructure specifically or broader Salesforce platform engineering? 2. How does Salesforce's SRE org structure handle incidents that span multiple clouds (AWS + GCP)?
