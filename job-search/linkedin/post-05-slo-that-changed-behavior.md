# Post 5: SLOs That Changed Team Behavior

---

I spent two years writing SLOs nobody read. Then I wrote one that changed how an entire team made decisions.

The difference was not the math. It was the error budget.

Early SLOs at our shop looked like this: "Availability >= 99.9%." That number lived in a document. It got reviewed at quarterly business reviews. Engineers knew it existed the way they knew the fire extinguisher existed — important in theory, invisible in practice.

The shift happened when we reframed it: "You have 43 minutes of downtime budget this month. You have used 31. Do you want to ship this change on Thursday?"

Suddenly the SLO was a decision-making tool, not a compliance artifact. The team started asking about error budget before sprint planning. On-call engineers could tell you the remaining budget without looking it up. The SLO meeting went from a reporting exercise to an actual conversation about risk tolerance.

On a 25-million-message-per-day platform, that framing mattered. Some changes were worth spending budget. Some were not. The error budget created shared language between engineering, product, and leadership — "we are in the red, we do not ship features this week" is a sentence everyone could understand and act on.

The Director insight: an SLO that does not change behavior is not an SLO. It is a metric. The goal is not to measure reliability — it is to govern the tradeoff between reliability and velocity at every level of the organization.

What would change in your team if every sprint started with the error budget balance?

#SRE #SLO #Observability #ReliabilityEngineering #PlatformEngineering #EngineeringLeadership #DevOps
