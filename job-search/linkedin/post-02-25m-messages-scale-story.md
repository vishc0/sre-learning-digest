# Post 2: 25M Messages/Day — Scale Story

---

We process 25 million messages a day. Here is what breaks at that scale that you would never predict.

Not the database. Not the message broker. Not the network.

The retry logic.

When your system is small, a retry is a safety net. When you are moving 25 million messages per day across a distributed notification platform, an exponential backoff misconfiguration becomes a traffic multiplier. One downstream service degrades. Retries kick in. Suddenly you have three times the intended load hitting a system that is already struggling. What started as a hiccup becomes a cascade.

We learned this at 2am on a Tuesday.

The fix was not hard technically — jitter in the backoff, circuit breaker thresholds, load-shed policies. The hard part was designing those policies before the incident, not during it. Because at 2am with an executive bridge open, you are not making your best engineering decisions.

The second thing that breaks at scale: observability assumptions. Dashboards built for 2 million messages/day look very different at 25 million. Alert thresholds that made sense at 10% traffic suddenly fire on normal variance at full load. You end up alert-fatigued exactly when you need your team sharpest.

The Director-level lesson: scale does not break systems. It amplifies every design assumption you made when the system was small. Review those assumptions before traffic forces you to.

What assumption in your current architecture are you most nervous about at 10x scale?

#SRE #DistributedSystems #Reliability #Scalability #PlatformEngineering #Observability #EngineeringLeadership
