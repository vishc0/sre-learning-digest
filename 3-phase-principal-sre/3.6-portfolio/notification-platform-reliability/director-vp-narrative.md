# Director/VP Narrative — Notification Platform Reliability

**For use in**: Executive interviews, VP/Director-level screening calls, portfolio walk-throughs  
**Delivery format**: 2 minutes spoken; this document is the prep text, not the script

---

## Paragraph 1: What Was Built and Why It Mattered

I manage the SRE function for T-Mobile's notification platform — a system that processes 25 million messages per day across SMS, push, and email channels. These are not marketing messages. They are 2FA codes, network outage alerts, fraud notifications, and customer account actions. When this platform fails silently, a customer cannot complete a purchase, a fraud alert does not reach someone whose account is being compromised, and a technician does not receive a dispatch order. The stakes are regulatory and reputational, not just operational. When I took over the team, the platform was generating eight Sev1 incidents per year, deployment took four hours in a maintenance window, and the on-call engineer was receiving approximately two hundred alerts per week — most of them noise. The team was skilled but exhausted, and the reliability posture was driven by heroism rather than engineering. My job was to change the substrate, not just the outcomes.

## Paragraph 2: How the Engineering Practice Was Built and What Changed

Over three years, the team moved from Pivotal Cloud Foundry to EKS with zero-downtime rolling deployments, instrumented the platform with dual-export telemetry so that SLO burn rates drive alert decisions rather than threshold counts, and rewrote every runbook from prose into executable step-by-step procedures with expected outputs. We defined three production SLOs, formalized an error budget policy that gives the team permission to pause feature work when reliability is at risk, and ran quarterly chaos engineering exercises to build muscle memory for the failure modes we are most likely to see at 3am. The results are in the DORA metrics: deployment frequency went from two to eight per month, MTTR dropped from 47 to 12 minutes, change failure rate dropped from 18% to 4%, and we have had zero Sev1 incidents in 36 consecutive months. The platform now runs at 99.7% SLO compliance — above target — while simultaneously scaling from 8M to 25M messages per day. The point I want to make to your organization is not that these numbers are impressive in isolation. It is that they were achieved through engineering practice changes, not headcount increases. The same 15-person team that was overwhelmed at 8M messages is now operating confidently at 25M. That is the leverage point: invest in the practice, and the scale follows.

---

## Interview Bridge Phrases

Use these to connect the narrative to interview questions:

- "The SLO framework I built here is directly applicable to your platform because..." (tailor to the company's product)
- "The error budget policy is the mechanism I used to have the feature-vs-reliability conversation with product leadership without it being a subjective debate."
- "The DORA improvement from medium to elite band happened because we treated deployment as a reliability investment, not a delivery tax."
- "Zero Sev1s in 36 months at this scale is not luck — it is the compounded result of runbooks that work, alerts that fire accurately, and a team that practices failure response before it happens."

---

## The One-Sentence Version (for cold introductions)

"I led the SRE function for T-Mobile's 25M-message-per-day notification platform from 8 Sev1s per year to zero over 36 months, while doubling deployment frequency and tripling throughput — through an SLO-driven engineering practice built on EKS, OpenTelemetry, and a formal error budget policy."
