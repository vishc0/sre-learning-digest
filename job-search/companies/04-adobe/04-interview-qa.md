# Adobe — Interview Q&A Prep

## RECRUITER SCREEN
**Q: Tell me about yourself.**
"I'm Vishweshwar Chippa. Here's the headline: I run Adobe Journey Optimizer in production at T-Mobile. 25 million messages a day through AJO, along with AEP and CJA. I'm an enterprise operator of Adobe's own products. Beyond that, I lead 4 platforms, 15 engineers, 99.99% availability over 3 years. I'm looking to bring that production AJO experience to Adobe's SRE organization. I have an approved I-140."

**Q: Why Adobe specifically?**
"Because I'm already working in Adobe's product ecosystem daily. When I talk to your SRE team about what an enterprise operator needs — what breaks under load, what monitoring is missing, what journey reliability looks like at 25M msgs/day — that's not theory. That's my Monday morning. I can contribute domain expertise that's genuinely rare."

## BEHAVIORAL + PRODUCT KNOWLEDGE QUESTIONS

**Q: What are the biggest reliability challenges you've seen operating AJO at scale?**
"Three things stand out from production experience:
1. Journey re-entry logic under high concurrency — when 100K profile updates hit simultaneously, journey branch execution can queue-back in ways that create latency spikes. We mitigate with upstream rate limiting and Splunk alerts on journey queue depth.
2. AEP identity stitching latency — if a profile update hasn't propagated before journey trigger, the wrong profile version is used. We added a short TTL cache warmup before trigger evaluation.  
3. Suppression sync lag — AJO's DND integration can lag during platform updates; we built a secondary validation layer in our DND platform to catch any window gaps.
These are the kinds of failure modes I'd want to instrument and address from inside Adobe's SRE team."

**Q: How have you used CJA for platform observability?**
"We built custom CJA dashboards tracking message delivery rates, channel preference adherence, journey completion rates by segment, and comparison of weekly/daily volumes. CJA is excellent for the business-level view — journey funnel analysis, attribution of message-to-conversion — but for real-time operational alerting we still rely on Splunk. The gap I'd love to help close is tighter integration between CJA analytics and SRE operational signals."

**Q: Tell me about a production incident on AJO and how you resolved it.**
"We had an event where journey suppression was not applying correctly during an AJO platform update window — messages that should have been held were being sent. We identified it through our Splunk DND monitoring layer (not AJO's own tooling) within 8 minutes. Containment: paused journey execution for affected segments. Root cause: a timing gap during AJO's own DND rule sync during platform maintenance. Resolution: added pre-journey trigger validation in our upstream platform to re-check suppression state. This led to our ML anomaly detection build for the DND domain."

## TECHNICAL QUESTIONS

**Q: How would you approach SRE for a SaaS platform like AJO where you share infrastructure with many customers?**
"Multi-tenant SRE requires a different mental model than owned infrastructure. You need:
1. Tenant isolation monitoring — can I tell if ONE customer's usage is degrading all others?
2. SLO per tenant tier — enterprise customers (T-Mobile, large banks) have different expectations than SMBs
3. Blast radius mapping — for every component, what's the worst-case blast radius per tenant?
4. Canary tenant strategy — can I test a change against a subset of tenants before full rollout?

From the customer side at T-Mobile, we've experienced all four of these challenges with AJO at different times."

## QUESTIONS TO ASK
1. "Which AJO or AEP engineering team would this SRE role be embedded with? I want to understand if it's the journey execution layer, the AEP ingestion layer, or the delivery infrastructure."
2. "How does Adobe's SRE organization incorporate enterprise customer feedback into reliability priorities?"
3. "What's the mix between AWS and Azure for AJO's production infrastructure today?"
