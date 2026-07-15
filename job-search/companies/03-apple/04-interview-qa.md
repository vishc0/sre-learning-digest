# Apple — Interview Q&A

## RECRUITER SCREEN
Q: Tell me about yourself.
"I'm Vishweshwar Chippa, SRE Principal at T-Mobile. I lead a 15-person team running 4 production platforms at 25 million messages daily. The data infrastructure I operate — Cassandra, Redis, RabbitMQ, Kubernetes — aligns with Apple Services Engineering. I've maintained 99.99% availability over 3 years with zero Sev1s. I have an approved I-140. I'm interested in SRE Manager roles at Apple Austin or the Databases SRE Manager position in Seattle."

## TECHNICAL QUESTIONS (ASE FOCUS)

Q: How do you approach Cassandra operations at production scale?
"Four areas: (1) Compaction strategy — I tune compaction based on read/write ratio; STCS for write-heavy, TWCS for time-series. (2) Read repair and consistency levels — we use LOCAL_QUORUM for most reads, LOCAL_ONE for high-velocity message delivery tracking where eventual consistency is acceptable. (3) Capacity management — keyspace-level monitoring for disk usage, partition heat maps for hot-partition detection, JVM heap monitoring for GC pressure. (4) Repair scheduling — incremental repair on a rolling schedule to keep anti-entropy manageable without impacting write throughput. We've had zero Cassandra-related outages since implementing this practice."

Q: How do you manage distributed systems failure at scale?
"Assume failure — don't design for success. Every component has a defined failure mode and a fallback behavior. For notifications: if the primary delivery path fails, there's a retry queue; if the retry queue fills, there's a DLQ with alerting; if DLQ grows beyond threshold, there's a human escalation path. No silent failures anywhere. In Kubernetes, I use PodDisruptionBudgets and circuit breakers to prevent cascading failures. The goal: any single component failure degrades gracefully, never catastrophically."

Q: Describe your experience managing distributed cache (Redis) at scale.
"At T-Mobile we use Redis for DND suppression state caching and offer rule caching. Key practices: cluster mode with at least 3 shards + replicas for HA; memory eviction policy set to allkeys-lru for cache use cases; AOF disabled for performance (we can rebuild from source of truth); TTL on all keys (no unbounded memory growth). For the suppression cache specifically, we monitor hit rate — if it drops below 95%, something is wrong with the cache warming process."

## BEHAVIORAL QUESTIONS

Q: How do you approach SRE team building? (For SRE Manager role)
"I hire for ownership mentality over specific tech skills. The best SRE I ever hired had never used Splunk — but they had a pattern of noticing problems before they became incidents and feeling personal responsibility for them. Tech skills are teachable in 3 months; ownership mentality is years in the making. Once hired, I give every engineer a clear platform they own — not shared responsibility, but specific ownership. They set the SLOs, they own the runbooks, they own the postmortems. That structure creates excellence."

Q: Tell me about a zero-downtime migration that required precise execution.
"Our TIBCO-to-Spring-Boot migration was our highest-risk. TIBCO was processing legal notification messages that could not be lost. I ran both systems in parallel for 8 weeks — TIBCO processing all messages, Spring Boot receiving shadow traffic and comparing outputs. When Spring Boot output matched TIBCO output for 8 consecutive weeks with zero divergence, I cut over 10% of traffic, then 25%, then 50%, then 100% over 4 weeks. We had TIBCO on hot standby for 3 months post-cutover. Zero messages lost."

## QUESTIONS TO ASK
1. "Which Apple Services team would this SRE Manager role be embedded with — iCloud specifically, or the broader ASE infrastructure?"
2. "How does Apple's SRE organization handle the tension between Apple's secrecy culture and the need for cross-team incident coordination?"
3. "For the Databases SRE Manager role in Seattle: what's the current team size and composition?"
