# Cisco — Interview Q&A

Q: How deeply have you used Splunk and what advanced capabilities have you built?
"Beyond dashboards and basic alerts: (1) MART framework — custom Splunk application with correlated monitoring across 4 platforms, automated alerting with dynamic thresholds, real-time reporting for leadership, and integrated troubleshooting guides. (2) ML anomaly detection — used Splunk's MLTK to build a model detecting abnormal message suppression patterns in our DND domain; runs in production, recovers ~750K message deliveries monthly from false positives. (3) SLO burn-rate monitoring — custom calculation in Splunk tracking error budget consumption in real-time with predictive alerting before budget exhaustion. (4) Python + Splunk SDK integration for automated incident enrichment."

Q: How do you approach multi-cloud reliability?
"Treat cloud providers as unreliable dependencies, not trusted infrastructure. Design blast radius by cloud zone, not just availability zone. For our T-Mobile platforms: primary workloads on AWS EKS, with circuit breakers that activate if AWS health events are detected. The key observability requirement: you need unified monitoring that works regardless of which cloud layer is having issues — which is exactly the value Splunk provides in a multi-cloud architecture."

QUESTIONS TO ASK: 1. How has Cisco integrated Splunk into its own internal SRE operations? 2. What's the SRE charter for Cisco's cloud-delivered networking products?
