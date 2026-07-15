# STAR Story Library — Master Index
## Vishweshwar Chippa | SRE Manager / Principal SRE | T-Mobile

---

## How to Use This Library

Each file contains:
- Full STAR story (Situation, Task, Action, Result)
- Director/VP version (leadership framing — use for Director/VP-level interviews)
- IC version (technical depth — use for Principal/Staff SRE interviews)
- 30-second version (phone screen, "quick background" prompts)
- 2-minute version (standard behavioral interview answer)
- Key metrics table (memorize before every interview)

**Read-aloud test**: Every 2-minute version should clock 1:45 to 2:15 at normal conversational pace. Practice with a timer.

**When to use which version**: Match the interviewer's level. VP Engineering = Director version. Staff SRE technical screen = IC version. "Tell me about yourself" opener = 30-second version.

---

## Story Index

| # | File | Domain | Core Theme | Key Metric |
|---|------|--------|------------|------------|
| 01 | star-01-zero-sev1-reliability-culture.md | SRE Leadership | Reliability culture, MART framework | 36 months, zero Sev1 |
| 02 | star-02-zero-downtime-migrations.md | Platform Migration | Strangler-fig migration, risk management | 6 migrations, zero downtime |
| 03 | star-03-ml-anomaly-detection.md | AI/ML in Production | MLTK temporal models, shadow validation | MTTD 47 min → under 8 min |
| 04 | star-04-25m-msg-platform-scale.md | Distributed Systems | KEDA, priority classes, circuit breaking | 3x spike, zero manual intervention |
| 05 | star-05-error-budget-policy.md | SLO Governance | Policy enforcement, product/SRE alignment | First enforcement, no exceptions |
| 06 | star-06-mart-framework-observability.md | Observability | 4-tier observability framework design | 340 → 47 alerts, 86% reduction |
| 07 | star-07-team-building.md | Eng Leadership | Retention, growth ladder, hiring | 0 attrition, 2 Staff promotions |
| 08 | star-08-incident-command-p1.md | Incident Management | Hypothesis-driven diagnosis, systemic postmortem | Resolved in 44 min, zero recurrence |
| 09 | star-09-stakeholder-influence.md | Influence | Changing decision without authority | Istio adoption org-wide |
| 10 | star-10-ai-genai-production.md | AI/GenAI | RAG agent, risk tier framework | 91% accuracy, 4% hallucination rate |

---

## Cross-Reference: Common Interview Questions

### "Tell me about your biggest technical achievement"
Primary: Story 01 (zero Sev1) or Story 03 (ML anomaly detection)
Secondary: Story 04 (platform scale design)

### "Tell me about a time you influenced without authority"
Primary: Story 09 (Istio/mTLS decision)
Secondary: Story 05 (error budget enforcement with product)

### "Tell me about a difficult stakeholder conversation"
Primary: Story 05 (error budget enforcement)
Secondary: Story 09 (architecture committee)

### "How do you build engineering culture?"
Primary: Story 01 (reliability culture, MART framework)
Secondary: Story 07 (team building, On-Call Ladder)

### "Tell me about a time you managed risk"
Primary: Story 02 (zero-downtime migration strategy)
Secondary: Story 08 (rollback decision under uncertainty)

### "How do you think about AI/ML in production?"
Primary: Story 10 (both ML and GenAI initiatives)
Secondary: Story 03 (MLTK anomaly detection specifically)

### "Tell me about your incident command approach"
Primary: Story 08 (P1 command, hypothesis pivot)
Secondary: Story 01 (systematic prevention vs. heroic response)

### "How do you scale systems?"
Primary: Story 04 (KEDA, priority classes, backpressure)
Secondary: Story 02 (PCF-to-EKS, strangler-fig)

### "Tell me about talent development"
Primary: Story 07 (team building, On-Call Ladder)
Secondary: Story 01 (two Staff promotions from reliability work)

### "How do you approach observability?"
Primary: Story 06 (MART framework)
Secondary: Story 03 (anomaly detection as observability evolution)

---

## Platform Metrics — Memorize These

These numbers anchor every story to operational reality. Know them cold.

| Metric | Value |
|--------|-------|
| Daily message volume | 25 million messages/day |
| Channels | SMS, push, email |
| Team size | 15 engineers |
| Sev1 record | Zero in 36 months |
| Alert reduction | 340 → 47 (86% reduction) |
| MTTD improvement | 47 minutes → under 8 minutes |
| Migration record | 6 migrations, zero downtime |
| Alert volume reduction | 40,000+/month → under 4,000/month |
| On-call onboarding | 8 weeks → 4 weeks |
| PCF cost savings | $18,000/month after decommission |
| Staff promotions | 2 during tenure |
| Attrition (18-month period) | Zero |
| Error budget events | 2 policy enforcements, zero exceptions |
| GenAI pilot accuracy | 91% helpful response rate |

---

## Interview Preparation Ritual (Before Every Interview)

1. Read the index table — confirm all 10 stories are fresh
2. Read the Key Metrics table — these are your anchors
3. For each story you expect to use, read the version that matches the interviewer level
4. Run through the 30-second version aloud for each story you'll use — this sets fluency
5. Time one 2-minute version aloud — recalibrate pacing if needed

**Depth test**: If an interviewer asks "tell me more about X" — you should be able to go 2 levels deeper on any story. Practice the IC version even if you expect to interview at Director level. Credibility comes from depth you don't need to use.
