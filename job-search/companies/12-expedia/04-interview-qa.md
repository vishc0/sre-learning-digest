# Expedia — Interview Q&A

Q: How do you ensure message delivery reliability for time-sensitive notifications?
"Time-sensitive messages get separate SLO classes. For Expedia, flight confirmations or check-in reminders have a shorter SLO window than a price alert. In practice: dedicated priority queues per urgency class, separate retry logic with tighter timeouts for urgent messages, real-time monitoring with p99 latency alerting rather than just average. We built this at T-Mobile for legal notifications — same principle applies to time-sensitive travel notifications."

Q: How would you handle a major booking platform incident during a holiday travel peak?
"Pre-peak: run load tests at 2x expected peak, validate autoscaling behavior, pre-stage runbooks for the 5 most likely failure modes. During incident: traffic throttling first (protect downstream booking systems), then diagnose. Key principle: a partial service degradation during peak is infinitely better than a full outage. Communicate continuously — every 15 minutes to stakeholders even if just 'we're still working on it.'"

QUESTIONS TO ASK: 1. What's the message volume during peak travel seasons vs. baseline? 2. How does Expedia's SRE org handle the multi-brand complexity (Expedia, Hotels.com, Vrbo, etc.)?
