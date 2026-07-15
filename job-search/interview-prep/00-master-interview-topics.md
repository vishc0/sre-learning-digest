# Master Pre-Interview Reading Checklist
## Director of Engineering / Sr. Engineering Manager / Principal SRE

**Target roles**: Director of Engineering, Sr. Engineering Manager, Principal SRE  
**Candidate**: Vishweshwar Chippa — SRE Manager, 21+ years, T-Mobile  
**Last updated**: 2026-06-24

---

> **How to use this file**: Read top to bottom once. Then use the "Read First (48h before interview)" callouts to triage by time. Every topic listed is a potential interview question or a framework you should be able to cite fluently. Do not memorize — internalize.

---

## 1. Management & Leadership (Director-Level)

The difference between a manager answer and a director answer: managers describe what they did to a team; directors describe how they designed the system the team operated in. Every answer should reveal systems thinking, not just action-taking.

### Topics

1. **Situational Leadership II (SLII) — Hersey/Blanchard quadrants**: Directing (S1), Coaching (S2), Supporting (S3), Delegating (S4). Know which quadrant maps to which employee development level (D1–D4). Be able to cite a real example of intentionally moving someone from S1 to S4.

2. **First 90 Days framework (Michael Watkins)**: STARS model — Start-up, Turnaround, Accelerated Growth, Realignment, Sustaining Success. Articulate which mode your last role was in and how that shaped your approach. Directors are expected to know this cold.

3. **Span of control decisions**: When to add a manager layer vs. flatten the org. Rule of thumb: 6–8 ICs per front-line manager, 4–6 managers per director. Know the exceptions and the cost of getting it wrong.

4. **Manager-of-managers vs. manager-of-ICs transition**: What changes in your job when you no longer have direct IC reports. The shift from tactical execution to organizational design, culture-setting, and capability building.

5. **OKR authoring and cascading**: Objective → Key Results → Initiatives. Know the difference between an output KR ("ship feature X") and an outcome KR ("reduce P95 latency by 40%"). Know how to cascade company OKRs to team OKRs without losing signal.

6. **Decision-making frameworks — DACI and RACI**: Driver, Approver, Contributor, Informed. When to use DACI vs. RACI. Be able to explain when ambiguous DACI causes delays and how you fixed it.

7. **Delegation ladder (7 levels)**: From "wait to be told" to "act and report periodically." Know how to consciously move people up the ladder and why defaulting to level 2–3 stunts team growth.

8. **Psychological safety — Amy Edmondson's research**: The four stages (Inclusion, Learner, Contributor, Challenger). What behaviors destroy it. What specific leader behaviors build it. Be ready for: "How do you create a culture where people raise problems early?"

9. **Double-loop learning vs. single-loop learning (Argyris)**: Single = fix the error. Double = question the assumption that caused the error. How postmortems should be double-loop, not single-loop.

10. **Radical Candor framework (Scott)**: Care Personally × Challenge Directly quadrant. Ruinous Empathy, Obnoxious Aggression, Manipulative Insincerity, Radical Candor. Know where your default is and how you correct for it.

11. **Operating cadence design**: What meetings exist at each level (weekly 1:1, team sync, skip-levels, org all-hands, leadership offsites). How to design a cadence that doesn't collapse under incident load. The "heartbeat model."

12. **Engineering strategy documents**: What is an Eng Strategy doc vs. a Tech Spec vs. an RFC. How to write a one-page strategy doc that aligns a 40-person org for a quarter. Format: context → principles → bets → anti-bets.

13. **Change management — Kotter's 8-step model**: Create urgency → Build coalition → Form vision → Communicate → Remove blockers → Create short-term wins → Consolidate gains → Anchor in culture. Know steps 1 and 8 — they're where most engineering leaders fail.

14. **Influence without authority**: Your peer team won't do what you ask unless you build credibility, frame problems in their language, and make their win visible. Be ready with a specific example of landing a cross-functional outcome without positional power.

15. **Organizational design patterns**: Functional, product-aligned, platform, matrix, stream-aligned (Team Topologies). Know when each is appropriate and the coordination cost of each.

16. **Team Topologies vocabulary**: Stream-aligned teams, Enabling teams, Complicated-subsystem teams, Platform teams. Interaction modes: Collaboration, X-as-a-Service, Facilitating. This is the vocabulary Directors use in 2025–2026.

17. **Leading through ambiguity**: How to give your team direction when the company strategy is unclear or shifting. "Commander's intent" model from military doctrine — tell people the outcome, not the steps.

18. **Engineering culture levers**: What a director actually controls — hiring bar, promotion criteria, incident culture, documentation norms, on-call fairness, postmortem quality. Know which levers have the highest ROI.

19. **Technical debt governance**: How to make tech debt visible to non-engineers (tech debt register, debt-to-velocity ratio). How to fund debt paydown without losing product velocity. The "20% time" model and its failure modes.

20. **Measuring engineering effectiveness**: Beyond velocity. Lead time for changes, deployment frequency, MTTR, change failure rate (DORA). Team health surveys. Cognitive load indicators. Be able to defend your choice of metrics.

21. **Managing high performers**: What happens when your best engineer is also your least collaborative. The "brilliant jerk" problem. How to coach without losing them. When to make the hard call.

22. **Skip-level meetings**: How to run them without undermining your managers. What questions to ask. What to do with what you hear. How to close the loop.

---

**Read First (48h before interview):** SLII quadrants, First 90 Days/STARS, Team Topologies vocabulary, OKR outcome vs. output distinction, Psychological safety behaviors.

---

## 2. Operational Excellence & SRE

Directors interviewing for SRE-aligned roles are expected to speak both the Google SRE language and the business language. Translate between them fluently.

### Topics

1. **DORA Four Key Metrics**: Deployment Frequency, Lead Time for Change, Change Failure Rate, Mean Time to Restore. Know the Elite/High/Medium/Low benchmarks (2023 State of DevOps report). Know which metric your current org sits at and what moved it.

2. **Error budget policy design**: What happens when a service burns 100% of its error budget in week 2 of the month? Written policy, not a conversation. Who freezes releases? Who can override? What's the escalation path?

3. **SLI/SLO/SLA hierarchy**: SLI = measurement. SLO = internal target. SLA = contractual commitment. How to choose the right SLI for a service (availability vs. latency vs. correctness vs. freshness). The "CUJ → SLI → SLO" design chain.

4. **Toil definition and toil budgeting**: Google's definition (manual, repetitive, automatable, scales with load, no enduring value). How to measure toil as a percentage of sprint capacity. The 50% toil ceiling and what to do when you're over it.

5. **Postmortem culture design**: Blameless vs. blame-aware. The five elements of a high-quality postmortem (timeline, contributing factors, action items with owners, detection gap, prevention). How to make postmortem action items actually close.

6. **On-call health indicators**: Mean time to acknowledge (MTTA), alert-to-ticket ratio, pages-per-engineer-per-week, percentage of alerts that are actionable. The "on-call misery index." How to use these to justify headcount.

7. **Alert fatigue root causes and remedies**: Alert noise ratio, lack of alert ownership, missing runbooks, poorly tuned thresholds. Specific tactics: alert ownership matrix, monthly alert review, automated alert deprecation after 90 days of no action.

8. **Incident command structure (ICS)**: Incident Commander, Communications Lead, Operations Lead. The five functions of ICS. How to scale from a 2-person incident to a 20-person incident without losing command.

9. **Runbook standards**: What a runbook must contain (trigger, symptoms, impact, diagnosis steps, mitigation, escalation, rollback). The difference between a runbook and a playbook. How to enforce freshness.

10. **Platform engineering vs. SRE**: Platform teams build the paved road. SRE teams ensure the system is reliable. The organizational tension between them. When to merge them and when to keep them separate.

11. **Chaos engineering maturity model**: Level 0 (no testing), Level 1 (gamedays), Level 2 (automated chaos in staging), Level 3 (automated chaos in production). Know how to pitch Level 2 to a skeptical VP.

12. **Observability pillars**: Metrics, Logs, Traces — and the fourth pillar: Events/Profiling. The difference between monitoring (known unknowns) and observability (unknown unknowns). How to explain this to a product VP.

13. **SRE book Chapter 3 — Risk**: Acceptable risk as a business decision. How to calculate availability (9s). The cost of an additional 9. Why 99.999% availability may be the wrong target for your service.

14. **Capacity planning process**: Traffic modeling, headroom targets (typically 20–30% above peak), capacity review cadence, provider lead times. How to integrate capacity planning with OKR cycles.

15. **Reliability roadmap construction**: How to prioritize reliability investments across a portfolio of services. The reliability investment matrix (criticality × current reliability gap). How to present this to engineering leadership.

16. **Graceful degradation patterns**: Circuit breakers, bulkheads, shed load, static fallback responses. Know when each applies. Be able to walk through a specific service where you implemented one.

17. **Deployment safety practices**: Feature flags, canary releases, blue/green deployments, progressive delivery. The difference between a canary (traffic split) and a feature flag (code path). When each is appropriate.

18. **SRE team topologies**: Embedded SRE vs. central SRE vs. consulting SRE. The "CRE" (Customer Reliability Engineering) model. The engagement model that scales and the one that creates bottlenecks.

19. **Reliability as a product**: SRE teams that publish internal SLOs for their platforms, maintain public status pages, run "reliability office hours." How this changes the relationship between SRE and development teams.

20. **Incident metrics trending**: Not just MTTR but: incident recurrence rate (same root cause twice = systemic failure), blast radius trend, customer-impacting vs. internal-only ratio. How to present these in a QBR.

21. **Toil elimination ROI calculation**: Engineer-hours consumed by toil × hourly cost × recurrence = annual toil cost. Automation build cost / annual toil cost = payback period. Be able to do this math on a whiteboard.

22. **Game days and fire drills**: How to run them. What makes a game day valuable vs. theater. How to tie game day outcomes to reliability roadmap priorities.

---

**Read First (48h before interview):** DORA metrics with benchmarks, error budget policy design, SLI/SLO/SLA chain, toil definition and budgeting, incident command structure.

---

## 3. Technical Domain Knowledge (Platform/Infrastructure)

At Director/Principal level, you are not expected to write the code. You are expected to make the architecture decision, explain the trade-off in business terms, and know when you're being sold a wrong answer.

### Topics

1. **Kubernetes architecture at scale**: Control plane components (API server, etcd, scheduler, controller manager). Why etcd is the single point of truth and the single point of failure. HPA vs. VPA vs. KEDA. Node group strategy. Know when to use managed K8s (EKS/GKE) vs. self-managed.

2. **Service mesh trade-offs**: Istio vs. Linkerd vs. Cilium. What a service mesh buys (mTLS, traffic shaping, observability) and what it costs (complexity, latency, operational burden). When NOT to use one.

3. **Messaging architecture decisions**: When to use RabbitMQ (task queues, low-volume, routing complexity), when to use Kafka (event streaming, high-throughput, replay, audit log). The wrong answer: "we'll just use whichever." The right answer: model the message pattern first.

4. **Event-driven architecture patterns**: Event sourcing, CQRS, Saga pattern for distributed transactions. Know the failure modes of each. Be able to explain why Saga without compensating transactions is dangerous.

5. **Multi-region architecture trade-offs**: Active-active vs. active-passive vs. pilot-light. RPO/RTO as business decisions, not engineering decisions. The cost of active-active (data synchronization, conflict resolution, 2x infrastructure spend).

6. **API gateway patterns**: Edge gateway vs. backend-for-frontend (BFF) vs. service-to-service gateway. Rate limiting strategies. API versioning approaches (URL versioning vs. header versioning vs. content negotiation).

7. **Data platform architecture**: Lambda architecture (batch + speed layers) vs. Kappa architecture (streaming only). When each is appropriate. The operational cost of running two stacks in Lambda vs. the replay complexity in Kappa.

8. **Security architecture decisions**: Zero-trust model (never trust, always verify). mTLS in service-to-service. Secret management (Vault, AWS Secrets Manager). RBAC vs. ABAC. Know where the attack surface is in a K8s cluster.

9. **FinOps architecture levers**: Right-sizing vs. spot instances vs. reserved capacity. The "buy vs. commit vs. spot" decision framework. How architecture decisions (stateful vs. stateless, session affinity) constrain cost optimization.

10. **Build vs. buy vs. borrow decisions**: The three-part test — (1) Is this a differentiator? (2) Do we have the expertise to maintain it? (3) What is the total cost of ownership? Internal platform teams often answer #1 wrong.

11. **GitOps and IaC maturity**: From ad-hoc Terraform to fully declarative GitOps (ArgoCD/Flux). The drift problem. The state locking problem. How to migrate a team from manual deployment to GitOps without halting delivery.

12. **Observability tooling decisions**: Prometheus + Grafana vs. Datadog vs. New Relic vs. OpenTelemetry. The vendor lock-in risk. The "OpenTelemetry first, backend second" principle. How to frame the build-vs-buy for observability.

13. **Database selection criteria**: OLTP vs. OLAP vs. HTAP. Relational vs. document vs. time-series vs. graph. Know when to pick each and what makes it hard to migrate later. The "read-your-writes" consistency requirement as a selection driver.

14. **CDN and edge architecture**: What belongs at the edge (auth tokens, A/B flags, static assets) vs. what must stay in origin (personalization, write operations). Edge computing trade-offs (Cloudflare Workers, Lambda@Edge).

15. **Platform engineering investment calculus**: How to justify a developer platform team to a CFO. Developer tax (manual steps × developer count × cost per hour). Golden path ROI. Time-to-production as the metric that moves executives.

---

**Read First (48h before interview):** K8s at scale (architecture, EKS specifics), Kafka vs. RabbitMQ decision framework, multi-region trade-offs with RPO/RTO framing, build-vs-buy three-part test, FinOps architecture levers.

---

## 4. Financial & Business Acumen

Directors who can't speak finance get bypassed in budget season. Learn to walk into a budget conversation with data, not requests.

### Topics

1. **Headcount modeling**: HC = FTEs + contractors. How to build a hiring plan that shows ramp cost (new hire is ~25% effective in month 1, ~50% in month 3, ~75% in month 6). How to present headcount as a bet on output, not a cost request.

2. **Total cost of ownership (TCO)**: Infrastructure + labor + tooling + opportunity cost. How to compute TCO for a platform decision. How to use TCO to kill a pet project that feels cheap but isn't.

3. **Cost of downtime calculation**: Revenue per minute × MTTR + customer churn cost + SLA penalty cost + reputational cost. Know how to run this for your primary service. This number justifies reliability investment better than any SLO argument.

4. **ROI framing for engineering investment**: (Benefit - Cost) / Cost × 100. But also IRR and payback period for multi-year investments. Know how to present a 3-year ROI for a platform rebuild vs. maintain decision.

5. **Budget variance management**: What to do when you're running 15% over forecast in Q3. Levers: delay hiring, freeze discretionary spend, re-prioritize roadmap. How to communicate variance without losing credibility.

6. **CapEx vs. OpEx distinction**: Why cloud spend is OpEx (immediate P&L hit) and why that matters to a CFO. How reserved instances convert OpEx to CapEx-like behavior. How to use this in a budget conversation.

7. **Contractor vs. FTE cost model**: Contractor is typically 1.5–2x FTE fully-loaded cost at spot rate but zero ramp, zero benefits, zero severance. When each is the right tool. The risk of contractor dependency for core capabilities.

8. **FinOps maturity model (FOCUS framework)**: Inform → Optimize → Operate. The three personas: Practitioner, Executive, Business. Know where your org sits and what the next step looks like.

9. **Unit economics for platform teams**: Cost per deployment, cost per service onboarded, cost per alert handled. How to use unit economics to show platform team efficiency rather than just headcount.

10. **Budget cycle navigation**: Annual planning (HC, infrastructure commitments, tooling) vs. quarterly re-forecast vs. monthly actuals. When to ask for budget vs. when to re-allocate. How to build contingency into a plan without sandbagging.

11. **Infrastructure cost attribution**: Chargeback vs. showback. How tagging strategy enables cost visibility. How to present a showback dashboard to engineering leads without it becoming a blame session.

12. **Business case writing**: Structure — executive summary, problem statement, options considered, recommendation, financial model, risks, ask. Know how to write one in two hours and what makes it fail at the CFO review.

---

**Read First (48h before interview):** Cost of downtime calculation (run it for your primary service), headcount modeling with ramp curve, ROI framing structure, CapEx vs. OpEx in cloud context.

---

## 5. People Leadership & Talent

The most common Director interview question category, and the one most candidates underestimate. Prepare specific stories, not generic principles.

### Topics

1. **Structured hiring design**: Job leveling rubrics, interview loop design (who interviews for what), calibration sessions, offer alignment. How to prevent the "everyone likes them but no one can say why" debrief failure mode.

2. **Interview bias mitigation**: Structured vs. unstructured interviews (structured interviews 2x more predictive). Anchoring bias in debrief. The "brilliant jerk" halo. How to design a loop that surfaces these.

3. **Performance calibration process**: Relative calibration sessions, performance distribution (not necessarily forced), criteria-based ratings vs. gut-based ratings. How to defend a rating when a peer manager disagrees.

4. **PIP design and execution**: When to PIP vs. when to manage out. The legal purpose of a PIP (documentation) vs. the development purpose (course correction). How to run a PIP conversation without destroying the relationship.

5. **High-performer retention tactics**: Recognition cadence, scope expansion, technical leadership tracks, compensation equity reviews. The "stay interview" — what to ask and when. The cost of losing a 9 (replaces with a 6 on average at 1.5x salary cost and 6 months ramp).

6. **Attrition analysis**: Voluntary vs. involuntary. Regrettable vs. non-regrettable. Leading indicators (eNPS, 1:1 sentiment, skip-level feedback). How to build an attrition dashboard that shows you the problem 60 days before the resignation.

7. **Succession planning**: Identifying 9-box talent (performance × potential). Building "ready now / ready in 1 year / ready in 3 years" succession maps. How to develop a successor without telegraphing your own departure.

8. **Coaching vs. mentoring vs. sponsoring distinction**: Coaching = ask questions to unlock their answer. Mentoring = share your experience. Sponsoring = use your political capital to open doors. Directors are expected to do all three, on purpose, not accidentally.

9. **Difficult conversation framework (SBI model)**: Situation, Behavior, Impact. How to deliver feedback that doesn't trigger defensiveness. How to follow up after the conversation. The "24-hour rule" for difficult feedback.

10. **Team health metrics**: eNPS, engagement survey response rate, 1:1 completion rate, internal mobility rate. How to build a team health dashboard and what to do when one indicator goes red.

11. **Remote/hybrid team management**: Async communication norms, timezone-fair meeting design, documentation culture as a first-class requirement (not optional), loneliness as a retention risk.

12. **Org design for growth**: When to split a team (Conway's Law — team structure drives architecture). When to merge teams (reducing coordination cost). The pain of splitting a team that shares a codebase.

---

**Read First (48h before interview):** SBI feedback model (practice it out loud), coaching vs. mentoring vs. sponsoring distinction, structured hiring loop design, attrition leading indicators.

---

## 6. Strategy & Communication

Directors who cannot communicate strategy are not Directors for long. This section is about translating between engineering reality and business intent — in both directions.

### Topics

1. **OKR writing quality bar**: A well-formed Objective is inspirational, time-bound, and qualitative. A well-formed Key Result is measurable, outcome-based, and unambiguous. The failure mode: KRs that are actually tasks ("complete migration of X") rather than outcomes ("95% of traffic runs on new platform").

2. **Wardley Mapping basics**: Genesis → Custom-built → Product → Commodity evolution axis. How to map your platform components on this axis. Why it matters for build-vs-buy decisions. You don't need to be an expert — know the vocabulary and the genesis/commodity distinction.

3. **Product thinking for platform teams**: Jobs-to-be-done framework applied to internal platform. Developer experience as a product. Platform NPS. The "paved road" metaphor and how to make developers choose it over the dirt road.

4. **Roadmap communication to executives**: The "Now / Next / Later" roadmap format (vs. Gantt). How to present a roadmap as a set of bets with confidence levels, not a commitment schedule. How to handle "why is X not on the roadmap" without losing credibility.

5. **Stakeholder mapping**: Power × Interest grid. High power / high interest = manage closely. High power / low interest = keep satisfied. Low power / high interest = keep informed. Know where each of your key stakeholders sits and what they need from you.

6. **Executive communication — BLUF format**: Bottom Line Up Front. State the answer, then the evidence, then the options. The mistake: leading with context when the executive wants the recommendation. One page or fewer. Three bullets or fewer.

7. **Running effective steering committees**: Purpose (decision vs. update vs. alignment), cadence, participants, pre-reads, decision documentation. The failure mode: steering committees that inform but never decide.

8. **Engineering brand building**: Tech blog, conference talks, open source contributions, internal tech talks. How to use engineering brand as a recruiting lever. How to sponsor engineers to build their public profile.

9. **Cross-functional alignment techniques**: Joint OKRs, shared success metrics, co-located planning, "pre-mortems" with partner teams. How to get product, security, and finance aligned on an engineering initiative before it starts.

10. **SAFe (Scaled Agile Framework) vocabulary**: PI Planning, ART (Agile Release Train), Enabling Epic, Feature vs. Story, Program Increment, Innovation and Planning (IP) iteration. Know enough to navigate the process and spot where it creates waste.

11. **Narrative construction for change**: The "problem → aspiration → path" structure. How to write a one-page narrative (Amazon-style) that aligns a leadership team on a direction. The difference between a narrative and a deck.

12. **Metrics storytelling**: How to present a dashboard that tells a story vs. one that dumps data. The "so what / now what" test for every metric slide. How to avoid metric theater (tracking what's easy vs. what matters).

---

**Read First (48h before interview):** BLUF communication format (practice it), OKR quality bar (outcome vs. output), Now/Next/Later roadmap format, stakeholder power-interest grid.

---

## 7. Soft Skills & Behavioral

Behavioral questions are not soft. They are the most predictive part of a Director-level interview. Every answer here needs a specific, named story — not a generic principle.

### Topics to Have Stories For

1. **Managing conflict between two senior engineers on a technical direction**: Specifically a conflict where you had to intervene, not mediate from the sideline. What did you do when one was right and the other was more senior?

2. **Delivering feedback that changed someone's trajectory**: Positive or corrective. The SBI model in action. What happened after. How you followed up.

3. **Managing up when you disagreed with a VP-level decision**: Not just "I raised concerns." You disagreed, you made your case, the decision went against you, and you either changed the outcome or committed to the direction. What was the conversation?

4. **Influence without authority — cross-functional win**: You needed a team you don't manage to change their behavior or prioritize your work. How did you make it happen without escalation?

5. **Building a team from scratch or rebuilding a broken one**: Hiring sequencing, culture setting, the first 30 days as the leader. What went wrong and how you corrected it.

6. **Leading through a major incident as the commander**: Not "I helped" — you were in the chair. What decisions did you make? What did you communicate to whom? What happened after?

7. **A project that failed and what you did**: Not a project that "faced challenges." One that failed. What was your role? What did you own? What would you do differently?

8. **Prioritizing ruthlessly when resources were constrained**: You had three critical things and one team. How did you decide? Who was unhappy and how did you handle it?

9. **Leading a major platform migration under pressure**: Zero-downtime or near-zero. Timeline pressure from business. Team that was stretched thin. What did you do to make it work?

10. **A difficult conversation with a peer manager**: They were blocking your team. You couldn't escalate without burning the relationship. How did you handle it?

11. **Handling a high performer who was also toxic to team culture**: You couldn't afford to lose their output. You also couldn't let the behavior continue. What did you actually do?

12. **Changing a culture that was resistant to change**: Blameful postmortems, hero culture, no documentation. Specific actions you took. Timeline. Leading indicators that it was working.

13. **Communicating bad news up the chain**: A project missed, an incident with business impact, a hire that didn't work out. How did you frame it, what did you own, what was the outcome?

14. **Building a relationship with a skeptical stakeholder**: They didn't trust engineering. Or they thought your team was the problem. How did you turn it.

15. **Advocating for your team in budget or headcount conversations**: You went into a room, made the case, and either won or lost. What was your argument? What was the result?

---

### Behavioral Answer Quality Bar

A Director-level STAR answer must:
- Take 2–3 minutes to deliver, not 30 seconds
- Include a specific number, timeline, or scale indicator
- Show systems thinking ("I designed the process" not "I did the thing")
- Name what you would do differently
- End with the outcome and the learning, not just the outcome

---

**Read First (48h before interview):** Review your STAR story library. Pick the 5 stories that are most versatile (apply to 3+ question types). Practice them out loud until they are conversational, not recited.

---

## 8. Industry & Trends (2025–2026)

A Director who doesn't know what's happening in the industry sounds like a manager. Have a point of view on each of these — not just awareness.

### Topics

1. **AIOps maturity in enterprise**: Using ML for alert correlation (Moogsoft, BigPanda), anomaly detection, predictive incident prevention. The gap between the marketing claim and the production reality. Where it actually works today vs. where it's still vapor.

2. **Platform engineering as an organizational pattern**: CNCF Platform Engineering whitepaper (2024). Internal Developer Portals (Backstage). The "paved road" vs. "guardrails" debate. The 2025 Gartner prediction that 80% of large orgs will have a platform team by 2026.

3. **GenAI in operations**: AI-assisted runbooks, LLM-powered incident summarization (PagerDuty Copilot, Datadog Bits AI), code-to-infra generation (Pulumi AI). The risk: AI-generated runbooks that are confidently wrong. The opportunity: 10x faster triage.

4. **FinOps maturity acceleration**: FOCUS specification (cloud billing normalization standard). FinOps Foundation maturity model. Unit economics as the next evolution beyond tagging/chargeback. Cloud cost as a product metric, not just an infrastructure metric.

5. **Security shift-left and DevSecOps**: SBOM (Software Bill of Materials) as a compliance requirement. Supply chain security (SLSA framework). Policy-as-code (OPA/Gatekeeper). The engineering leader's job: make secure the default path, not the extra step.

6. **OpenTelemetry standardization**: OTel becoming the dominant observability data standard. Vendor backends decoupling from instrumentation. The transition from proprietary agents to OTel collectors. What this means for your observability tooling decisions.

7. **SRE at scale — the Google/Netflix evolution**: SRE is becoming a platform/product discipline, not just an operations discipline. "Reliability engineering" embedded in product teams vs. central SRE. The debate is not settled and your point of view matters.

8. **Kubernetes operator pattern maturity**: Database operators, messaging operators, workflow operators. When operators reduce operational burden vs. when they add hidden complexity. The enterprise adoption curve in 2025.

9. **AI-assisted coding impact on engineering orgs**: GitHub Copilot, Cursor, Claude Code changing developer productivity. Implications for team size, skill mix, code review practices, and how you measure engineering output. Directors need a position on this.

10. **Zero-trust networking as an operational reality**: BeyondCorp model in enterprise. The NIST SP 800-207 framework. mTLS at service mesh level. The identity perimeter replacing the network perimeter. The SRE implication: identity is now a reliability dependency.

11. **eBPF and the future of observability**: eBPF-based tracing (Cilium, Falco, Pixie) without instrumentation changes. What this means for observability overhead and the "no-touch" visibility pitch. Early adopter stage — but Directors should know the direction.

12. **Incident response automation**: Automated remediation workflows (PagerDuty Process Automation, Shoreline.io). The risk of automated remediation making incidents harder to understand. The design principle: automate detection and notification first, remediation only for known, safe, reversible actions.

---

**Read First (48h before interview):** GenAI in operations (have an opinion), Platform Engineering CNCF framing, FinOps FOCUS spec, AI-assisted coding impact on org design, security shift-left vocabulary (SBOM, SLSA).

---

## 9. Must-Know STAR Story Categories

These are the 15 interview story buckets that a Sr. Manager / Director / Principal SRE candidate must have prepared before walking in. Every story must be real, specific, and deliverable in 2–3 minutes.

| # | Story Category | What the Interviewer Is Actually Testing |
|---|---------------|------------------------------------------|
| 1 | **Leading a team through a major platform migration under time pressure** | Execution under pressure, risk management, stakeholder communication |
| 2 | **Building an on-call culture from a reactive/heroic model to a sustainable one** | Systems thinking, culture change, data-driven leadership |
| 3 | **Hiring a key role — defining the bar, running the loop, making the call** | Hiring judgment, leveling, bias awareness |
| 4 | **Turning around a low-performing engineer — before and after** | Coaching, feedback quality, patience + decisive action |
| 5 | **Handling a P0/Sev1 incident as incident commander** | Incident command, communication, post-incident follow-through |
| 6 | **Delivering a project that was significantly behind schedule** | Recovery planning, stakeholder management, scoping decisions |
| 7 | **Convincing leadership to fund a reliability/platform investment** | Business case, ROI framing, executive communication |
| 8 | **Navigating a major org change (reorg, layoff, team merger)** | Change management, protecting your team, managing ambiguity |
| 9 | **Building cross-functional alignment on a contested technical decision** | Influence, facilitation, decision documentation |
| 10 | **Scaling a system 10x — architecture decisions and trade-offs made** | Technical judgment, architecture at scale, build vs. buy |
| 11 | **Eliminating significant operational toil — the before/after/ROI** | Toil quantification, automation strategy, team capacity reclamation |
| 12 | **A postmortem that actually changed something** | Postmortem quality, systemic thinking, follow-through |
| 13 | **Managing a conflict between two senior people on your team** | Conflict resolution, fairness, decisive mediation |
| 14 | **A situation where you had to tell your manager they were wrong** | Managing up, principled disagreement, commitment after disagreement |
| 15 | **Your biggest leadership failure and what you learned** | Self-awareness, growth mindset, honesty under pressure |

---

### Mapping Stories to Common Director Interview Questions

| Common Question | Best Story Categories to Use |
|-----------------|------------------------------|
| "Tell me about your leadership style" | #2, #3, #4, #15 |
| "How do you handle technical debt?" | #1, #7, #11 |
| "Describe a time you led through ambiguity" | #6, #8, #9 |
| "How do you build reliability culture?" | #2, #5, #12 |
| "Tell me about a failure" | #15 (primary), #6 (secondary) |
| "How do you influence without authority?" | #9, #14, #7 |
| "What's your approach to scaling teams?" | #3, #4, #8 |

---

**Read First (48h before interview):** Pull up your STAR library. Verify stories #1, #5, #7, #15 are sharp — they're asked in 90%+ of Director interviews. Practice #15 (failure story) until it doesn't feel uncomfortable. That discomfort is what makes it sound authentic.

---

## 10. Pre-Interview Day Checklist

### 72 Hours Before

- [ ] Research the company's current tech stack from their engineering blog, GitHub org, and job postings
- [ ] Read the last 3 earnings call transcripts or investor updates — what is the business betting on?
- [ ] Find the interviewer's LinkedIn and GitHub. What have they shipped? What do they care about?
- [ ] Read any recent news: layoffs, product launches, acquisitions, outages (status page history)
- [ ] Identify the company's primary SLO concerns: read reviews on Glassdoor, Blind, HN threads
- [ ] Pull up the job description and map every bullet to a STAR story or knowledge area you can speak to
- [ ] Review your five most versatile STAR stories out loud — not silently

### 48 Hours Before

- [ ] Run your "cost of downtime" calculation for your most critical service — have this number ready
- [ ] Review your DORA metrics for your current team — have the numbers, not approximations
- [ ] Refresh on SLII quadrants and have one example per quadrant
- [ ] Review Team Topologies vocabulary (stream-aligned, enabling, platform, complicated-subsystem)
- [ ] Reread your failure story (#15) and practice saying it without hedging
- [ ] Write out 3 specific questions you want to ask each interviewer (role, not generic)
- [ ] Confirm logistics: format (panel vs. serial), total time, any take-home component

### 24 Hours Before

- [ ] Sleep. Not review — sleep.
- [ ] Lay out physical materials: resume, notebook, pen
- [ ] Confirm video/audio setup if virtual; test camera, mic, background
- [ ] Set your opening statement: 90-second "who I am, why I'm here, what I bring" — practiced, not memorized

### Day Of

- [ ] Arrive (or log in) 10 minutes early
- [ ] Have water nearby
- [ ] When you don't know something: "I haven't faced that exact situation, but here's how I'd think about it" — do not pretend
- [ ] After each answer: pause. Let silence work for you. Directors think before they speak.

---

### Company Research Questions (Answer Before You Walk In)

1. What does the company's engineering org look like? (size, structure, reporting lines)
2. What is the stated engineering strategy or platform vision? (engineering blog, CTO talks)
3. What are the primary reliability risks for their product? (downtime history, customer complaints)
4. What has changed in the last 12 months? (reorg, new leadership, product pivot, M&A)
5. What is the on-call culture like? (Glassdoor engineering reviews, job postings for SRE roles)
6. What does the tech stack tell you about their maturity? (K8s? Monolith? Microservices? Data platform?)
7. Who are their key engineering leaders and what is their background? (LinkedIn)
8. What does the business care about most? (revenue growth, cost reduction, compliance, scale)
9. What does the role actually solve? (read between the lines — what broke or was missing?)
10. What would success in this role look like at 6 months and 18 months?

---

### Questions to Ask the Interviewer (Director-Appropriate)

Ask exactly these questions — or adapt them. Never ask questions answered on the company website. Never ask about salary in a technical/leadership round.

**About the role and org:**
1. "What does success in this role look like at 90 days versus 12 months? How would you measure it?"
2. "What is the biggest reliability or operational challenge the team is facing right now that this role is expected to own?"
3. "How does engineering collaborate with product on reliability prioritization — specifically when reliability investment competes with feature delivery?"
4. "What does the current on-call rotation look like? How many engineers are in it, and what is the alert volume per week?"

**About culture and leadership:**
5. "What's something about how this engineering org works that might surprise someone coming from the outside?"
6. "What does the team need from this leader that the previous person in this role wasn't providing?"
7. "How does the org handle blameless postmortems in practice — not policy, but what actually happens?"

**About strategy and direction:**
8. "What is the platform/infrastructure investment priority for the next two PI cycles?"
9. "Where is the org on the DORA maturity curve, and what is the target for 12 months out?"
10. "What is the most important architectural decision being debated right now? What are the camps?"

**Closing question (always ask this last):**
11. "Based on our conversation today, is there anything about my background or approach that you'd want me to address or that you see as a gap for this role?"

---

**Read First (48h before interview):** Memorize the 4 company research questions and the 4 questions to ask about the role. Have them written in your notebook before you walk in. The "closing question" (#11) is mandatory — it gives you a chance to address the doubt before it becomes a rejection.

---

## Quick Reference: Frameworks by Situation

| Situation | Framework to Cite |
|-----------|-------------------|
| Employee development conversation | SLII quadrants + delegation ladder |
| New role / first 90 days | STARS model (Watkins) |
| Reliability investment pitch | Cost of downtime + error budget ROI |
| Org design question | Team Topologies |
| Budget ask | TCO + ROI + payback period |
| Technical trade-off | Build-vs-buy three-part test |
| Feedback delivery | SBI model |
| Stakeholder alignment | Power-interest grid + BLUF |
| Change management | Kotter's 8 steps (cite steps 1 and 8) |
| Cross-functional conflict | DACI + Radical Candor |
| Capacity planning | DORA benchmarks + headroom target |
| Exec communication | BLUF + "so what / now what" |
| Postmortem quality | Double-loop learning |
| Team culture assessment | Psychological safety stages |

---

*End of master checklist. Estimated reading time: 60–90 minutes. Estimated preparation time to internalize: 3–5 focused sessions.*
