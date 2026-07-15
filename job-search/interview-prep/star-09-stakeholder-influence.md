# STAR Story 09: Stakeholder Influence — Changing a Technical Decision Without Authority
## Domain: Influence / Cross-Functional Leadership

---

## Situation

T-Mobile's platform engineering team proposed migrating the notification platform's service-to-service authentication from a shared secret model (static API keys rotated quarterly) to a mutual TLS (mTLS) implementation as part of a broader zero-trust initiative. The proposal was presented to engineering leadership with an implementation timeline and a recommended approach: issue certificates from T-Mobile's internal PKI to every service, implement mTLS at the application layer in each service, and rotate certificates annually. I was not on the architecture committee that made this decision — I was invited to a review meeting as the SRE stakeholder for the notification platform.

My concern was not with zero-trust principles or mTLS broadly. My concern was specific: the proposed implementation put certificate management logic inside each application service, meaning every service team would need to implement certificate loading, validation, and rotation independently. On a platform with 23 microservices and 6 different engineering teams, this was a distributed secrets management problem being solved 23 different ways. The failure mode — a certificate expiry going unnoticed on one service — would produce the same kind of silent delivery failure we'd already experienced. The committee's recommendation was about to be approved.

## Task

My task was to change the technical decision from a position of no formal authority. I was an SRE manager, not the architect. The proposal had already received positive signals from the VP of Platform Engineering. I needed to make a compelling case for an alternative approach — service mesh with mTLS at the infrastructure layer — without making the proposing team feel attacked, without undermining the VP's implicit endorsement, and without letting perfect be the enemy of good.

## Action (IC Technical Depth)

I did not object in the meeting. I asked a question instead: "What's our operational model for certificate expiry detection across 23 services on 6 different teams?" The architect paused. He said the plan was for each team to set calendar reminders for annual rotation. I asked a follow-up: "If one service's certificate expires and that service can no longer authenticate, what's the user-visible behavior?" The answer: silent delivery failure on that message path. I asked one more: "How long would it take us to diagnose that the cause was an expired certificate versus a code defect?" He acknowledged it would probably take 30+ minutes given current tooling.

I said: "I think the mTLS direction is right. My concern is operational — I'd like to propose an alternative implementation for the team's consideration before we finalize." I offered to write up the comparison before the next architecture review meeting. The VP agreed. That gave me a week.

I prepared a two-page comparison document — not a critique of the proposed approach, but a side-by-side analysis of two implementation patterns against five evaluation criteria: implementation cost, operational complexity, failure mode visibility, rotation automation, and incident blast radius. The criteria were not chosen arbitrarily — I anchored each one to an incident from our own postmortem history. Operational complexity was anchored to the dependency update incident (STAR Story 08). Certificate expiry visibility was anchored to a historical event at another team where a Redis TLS cert expiry had caused a 3-hour silent failure before anyone diagnosed it.

The alternative I proposed was Istio service mesh with mTLS at the sidecar proxy layer. Services wouldn't know about certificates at all — the infrastructure would manage issuance, rotation, and validation transparently. Certificate rotation would become an infrastructure-layer event, not a per-application code change. Istio's certificate authority would rotate certificates every 24 hours automatically, eliminating the annual manual rotation problem entirely.

The document ended with a recommended path: pilot the service mesh approach on two services (both owned by my team, so I was volunteering my own team for the change work), gather operational data for 60 days, then decide on the broader rollout approach. I wasn't asking them to abandon their proposal. I was offering to carry the proof-of-concept risk myself.

I shared the document with the platform architecture team two days before the review meeting — not as a surprise, but to give the proposing architect time to read it and respond. He came back with two concerns, both legitimate. I incorporated responses to both in a revised version. When we went to the review meeting, the conversation was collaborative rather than adversarial.

The committee adopted the service mesh recommendation with my team's pilot as the proof-of-concept.

## Result

- Istio service mesh deployed on notification platform services over 6 months
- Certificate rotation: annual manual → automated every 24 hours (zero human action required)
- mTLS coverage: all 23 services, uniform implementation, no per-service certificate management code
- Certificate expiry monitoring built into Istio's control plane: any anomaly surfaces in Splunk within 2 minutes
- The proposing architect and I subsequently co-presented the implementation at an internal engineering summit — the relationship was stronger after the process than before
- T-Mobile platform engineering adopted Istio as the standard service mesh for all new platform deployments following the pilot

---

## Director/VP Version (Leadership Framing)

"I changed a technical direction I had no authority to override, and I did it by making the proposing team's proposal better rather than replacing it. The key moves: I asked clarifying questions in the room to surface the operational gap without attacking the proposal, I volunteered my own team to carry the proof-of-concept risk, and I gave the proposing architect two days to engage with my document before the review meeting so he wasn't surprised. The outcome was a better technical decision and a stronger cross-team relationship. The architect and I co-presented the final implementation at an internal summit. That's the version of influence I try to practice — the goal is the best outcome, not winning the argument."

## IC Version (Technical Depth)

"The technical argument for service mesh over application-layer mTLS is operational manageability: when certificates live in application code, you have 23 implementations of certificate loading and rotation logic, each with its own failure modes. When certificates live in the sidecar proxy, you have one implementation, one failure mode, and one monitoring integration point. Istio's SPIFFE-based certificate authority rotates every 24 hours by default — that eliminates the annual manual rotation risk entirely. The Istio control plane also provides a real-time certificate validity API that we integrated directly into our Splunk monitoring — certificate anomalies surface in under 2 minutes versus the 30+ minute diagnostic time the alternative would have produced."

---

## 30-Second Version

"The platform engineering team proposed application-layer mTLS with annual manual certificate rotation across 23 services. I saw a future silent failure pattern in that design. Instead of objecting in the meeting, I asked operational questions that surfaced the gap, then wrote a two-page comparison document proposing Istio service mesh as an alternative, volunteered my own team for the pilot, and gave the proposing architect two days to engage before the review. Committee adopted the service mesh approach. The architect and I co-presented it at the summit."

---

## 2-Minute Version

"The platform team proposed mTLS with certificates managed inside each application service — 23 services, 6 teams, annual rotation via calendar reminders. I could see the failure mode: one expired certificate produces a silent delivery failure, and we'd be debugging it for 30+ minutes before anyone thought to check certificate validity. But I had no authority to block the proposal — the VP had already signaled support.

I didn't object in the meeting. I asked operational questions. 'What's our operational model for expiry detection across 23 services?' Calendar reminders. 'If a certificate expires, what's the user-visible behavior?' Silent failure. 'How long to diagnose certificate expiry versus code defect?' Thirty-plus minutes. I asked for time to write up a comparison before the decision was finalized. The VP agreed.

I spent the week writing a two-page document — not a critique, a side-by-side against five operational criteria, each anchored to our own postmortem history. I proposed Istio service mesh: mTLS at the sidecar layer, certificates invisible to application code, Istio CA rotating every 24 hours automatically. I volunteered my own team for the 60-day pilot so I was carrying the implementation risk, not just proposing work for others.

I shared the document with the proposing architect two days early. He came back with two concerns. I incorporated both into the revised version. By the time we were in the review meeting, it was a collaborative conversation, not a debate.

Committee adopted the service mesh approach. Six months later: all 23 services on Istio, certificate rotation automated, certificate anomalies surfacing in Splunk in under 2 minutes. Zero certificate-related incidents. The architect and I co-presented the implementation at an internal engineering summit. The relationship was stronger for the process."

---

## Key Metrics to Remember
- Scope: 23 microservices, 6 engineering teams
- Alternative proposed: Istio service mesh (application-unaware mTLS)
- Certificate rotation: annual manual → automated every 24 hours
- Certificate anomaly detection: 30+ minutes → under 2 minutes in Splunk
- Pilot: 2 services, 60 days, carried by my own team
- Adoption: T-Mobile platform engineering standard for all new deployments
- Relationship outcome: co-presentation with proposing architect at engineering summit
- Influence mechanism: questions in room → written comparison → early sharing → collaborative revision
