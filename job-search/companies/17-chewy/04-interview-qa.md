# Chewy — Interview Q&A

Q: How did you handle 100+ TPS for the Macy's loyalty file processing?
"The challenge was that each transaction required reward calculation, offer evaluation, and database write — all before generating the summary file for Citi. We optimized in three stages: parallel processing using JMS queuing so multiple transactions processed simultaneously; Redis caching for frequently-used offer rules to eliminate DB round-trips; and partitioned file generation by customer segment so we could process in parallel batches. We sustained 100+ TPS with sub-2-second latency at P95 during peak sale events."

Q: How do you approach SRE for seasonal retail load (like Super Bowl pet product sales)?
"Exactly like a planned incident — we know it's coming, so we prepare. 60-90 days out: run load tests at 2x projected peak. 30 days out: complete any infrastructure scaling and validate autoscaling behavior. 1 week out: freeze non-critical deployments. During peak: enhanced monitoring, on-call staffing augmented, runbooks pre-staged. Post-peak: thorough retrospective on what we didn't predict. The worst retail incidents happen when teams treat a predictable peak as a surprise."

QUESTIONS TO ASK: 1. What's Chewy's current infrastructure state — AWS-native or hybrid? 2. How does SRE work with fulfillment and logistics systems — is there a platform team boundary?
