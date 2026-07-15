# State Street — Interview Q&A

Q: You come from telecom — how do you think about financial services SRE differently?
"Financial services adds two layers that telecom partially addresses but doesn't fully match: (1) Every transaction has regulatory accountability — not just delivery confirmation but immutable record of what happened, when, by what system. At T-Mobile I built this for legal notifications; the discipline is the same. (2) The cost of failure is bidirectional — a failed trade confirmation can hurt the customer AND create regulatory liability for State Street. That dual accountability shapes every SLO decision I'd make here."

Q: Tell me about your banking experience.
"At Wachovia (now Wells Fargo) I was Operations Lead during the merger with First Union — building TIBCO environments under M&A pressure, maintaining uptime while the system map was changing weekly. That experience taught me that operational stability during organizational chaos requires documented systems, clear ownership, and runbooks that work even when the person who wrote them isn't available. Same principles apply at State Street during any platform transition."

QUESTIONS TO ASK: 1. What's the primary reliability challenge in State Street's custody and servicing infrastructure? 2. How does the SRE org relate to the trading desk from an SLO perspective?
