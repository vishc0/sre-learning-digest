# Amazon AWS — Interview Q&A Prep
## Recruiter Screen → Hiring Manager → Loop (Behavioral + Technical)

---

## RECRUITER SCREEN (Phone, 30 min)

**Q: Tell me about yourself.**
"I'm Vishweshwar — currently SRE Principal at T-Mobile where I run 4 notification platforms processing 25 million messages daily. I have 15 engineers, and over the last 10 years I've kept those systems at 99.99% availability through six major platform migrations. I'm an approved I-140 holder, so the H1B transfer is completely clean — no lottery, no new filing. I'm exploring Amazon because the operational excellence culture and the scale of distributed systems problems aligns directly with what I've been solving at T-Mobile."

**Q: Why Amazon?**
"Two reasons. First, the Leadership Principles — particularly Operational Excellence and Ownership — aren't just words to me. I've lived them. I built a monitoring framework adopted across our team, I own postmortems, I don't wait for someone else to fix recurring incidents. Second, AWS is where platform reliability happens at the scale that I want to grow into. T-Mobile's 25M messages is meaningful — but AWS operates at internet scale, and I want to test and grow my capabilities there."

**Q: What's your visa situation?**
"I'm on H1B. I have an approved I-140 with a priority date of June 2016, which makes me AC21-portable. For Amazon, a transfer is straightforward — your legal team files a transfer petition, I'm portable day one. No lottery, no new cap filing, no risk. I've done this successfully before."

**Q: What are you looking for in your next role?**
"SRE Principal or SRE Manager at L6 or L7. I want to operate at larger scale, grow my AI-in-SRE practice, and build teams that are genuinely excellent at reliability engineering. I'm open to either IC or people management — I currently lead 15 people so I'm comfortable with both tracks."

---

## HIRING MANAGER SCREEN — BEHAVIORAL (LP-BASED)

**Q: Tell me about a time you demonstrated Operational Excellence.**
*STAR:* "At T-Mobile, we had recurring Sev2 incidents caused by a MongoDB query pattern that degraded under high load. The team was treating each as a one-off — triage, fix, repeat. I stopped the cycle and ran a proper postmortem asking 'why does this keep happening?' The root cause was that our DBA queries hadn't been reviewed since we went from 5M to 25M msgs/day. I built a structured monitoring layer in Splunk specifically for MongoDB query latency patterns — the MART framework — and established a quarterly capacity review process. We've had zero repeats of that class of incident in 18 months."

**Q: Tell me about a time you showed Ownership beyond your scope.**
*STAR:* "When we began migrating from TIBCO to Spring Boot, the downstream teams hadn't updated their integration contracts. I had no formal authority over those teams but I knew that silent dependency failures would cause production incidents post-migration. I proactively set up an integration test working group, ran joint testing sessions, and created a shared runbook for 42 connected systems — all outside my direct org. The migration went live with zero downstream failures."

**Q: Tell me about a time you Invented and Simplified.**
*STAR:* "Our leadership team was asking for weekly platform health reports. The process required pulling data from 4 Splunk dashboards, merging them into Excel, and formatting a slide deck — 8 hours of manual work weekly. I built an AI-powered chat agent that could answer natural language queries about platform health in real time. 'How many SMS messages did we send yesterday?' Answer: immediate, from the model. The weekly reporting ritual went from 8 hours to 15 minutes of review."

**Q: Tell me about Hiring and Developing the Best.**
*STAR:* "I've built and scaled the T-Mobile notification SRE team from 4 to 15 engineers over 6 years. My practice is to identify the 1-2 engineers with the highest ceiling, give them a stretch project with full ownership, and debrief weekly. One engineer who joined as a deployment engineer is now leading our Kubernetes platform independently. I also authored our internal SRE onboarding checklist and playbook so new hires ramp to full productivity in 4 weeks instead of 12."

---

## TECHNICAL INTERVIEW QUESTIONS

**Q: Design a notification system that must deliver 25M messages per day across SMS, email, and push.**
"I'd design it around three principles: channel isolation, idempotent delivery, and observable pipelines.
- Intake: API gateway (APIGEE or AWS API Gateway) → SQS fanout queues per channel
- Processing: EKS-hosted Spring Boot microservices per channel; circuit breakers per downstream provider
- Delivery: SNS for push, SES/third-party for email, Twilio/carrier APIs for SMS — each with retry queues
- Idempotency: message IDs stored in Redis with TTL to prevent duplicates on retry
- Observability: CloudWatch metrics + Splunk for business-level tracking; alert on DLQ depth
- DND/suppression: MongoDB-based suppression list with near-real-time sync; ML anomaly detection for abnormal patterns

This is essentially what I run in production at T-Mobile."

**Q: How do you approach SLO definition for a notification platform?**
"I define SLOs from the user's perspective, not the system's. For notifications:
- Delivery SLO: 99.9% of messages delivered within 60 seconds of trigger event
- Critical path SLO (legal/financial): 99.99% delivery, 30-second window
- Suppression accuracy: < 0.1% false-positive DND suppression

Then I instrument Splunk to track these in near real-time with burn-rate alerts at 5% and 1% budget consumption. We review SLO burn monthly and adjust capacity or code when we're trending toward budget exhaustion."

**Q: Walk me through how you handle a Sev1 production incident.**
"I follow a strict runbook:
1. Declare and bridge — assemble on-call lead, platform owner, comms lead within 5 minutes
2. Contain first — throttle traffic, activate failover, or roll back if possible, BEFORE diagnosing
3. Diagnose in parallel — Splunk queries for error spike pattern, pod health in Kubernetes, DB latency
4. Communicate every 15 minutes — to stakeholders, never silent
5. Resolve and validate — confirm metrics return to SLO range before declaring recovery
6. Postmortem within 48 hours — 5-whys, systemic fix, owner assigned, due date set

We've had zero Sev1s in 36 months because every Sev2 gets the same postmortem treatment."

---

## QUESTIONS TO ASK THE INTERVIEWER
1. "Which specific team or product would this Principal SRE role be supporting? I want to understand the blast radius."
2. "How does Amazon's COE (Correction of Errors) process work at the Principal level — do Principals own the COE document or review them?"
3. "What does success look like in the first 90 days for this role?"
4. "How does this team handle the tension between velocity and reliability — what mechanisms exist to slow down deploys when SLO burn rate is elevated?"
