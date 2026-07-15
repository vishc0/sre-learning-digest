# LexisNexis/RELX — Interview Q&A

Q: How does your experience align with legal and regulatory data platforms?
"Two alignment points: First, compliance operations. My DND platform at T-Mobile governs which customers can and cannot receive specific messages — enforcing opt-out and suppression rules with legal backing. Violating those rules has regulatory consequences. I've maintained zero violations over 10 years through code-enforced policy, not process-enforced. Second, AI responsibility. RELX's Responsible AI Principles resonate — I've deployed ML in production with human validation layers, not autonomous decision-making. My anomaly detection model flags patterns for human review; it doesn't take autonomous action."

Q: Tell me about your GenAI experience in SRE operations.
"I built an AI agent that answers natural language questions about our 4 platforms — 'how many messages did we send this week vs last week?' or 'which platform had the highest error rate yesterday?'. The agent queries our Splunk data layer and returns formatted answers. I also use Claude Code for code generation in our automation tooling. Beyond that, I've used AI for MongoDB query optimization — describing what data I want in natural language, getting optimized query structures back. These aren't demos — they're production tools my team uses daily."

Q: How do you handle data security in an observability context?
"Observability and security are in tension — comprehensive logging is great for debugging, catastrophic if it captures PII. My practice: define log classification tiers before any system goes to production. Tier 1: technical metrics (latency, error rates) — log everything. Tier 2: business events (message type, channel, timestamp) — log with care. Tier 3: customer data (content, identifiers) — never in logs. At T-Mobile, legal notifications required us to log the fact of delivery but never the content. Same principle would apply to LexisNexis legal data — log metadata, never substance."

QUESTIONS TO ASK: 1. Which LexisNexis business unit would this role support — Legal & Professional, Risk Solutions, or a shared platform? 2. What's the current state of the AI platform infrastructure — where does the SRE team contribute most? 3. Is the Alpharetta campus the primary hub for this role or does it span Alpharetta + Raleigh?
