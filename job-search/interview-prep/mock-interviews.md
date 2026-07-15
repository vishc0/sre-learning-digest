# Mock Interview System — Director/VP SRE | Week 7

## Why This Matters

Week 7 is not study time — it is performance time. The difference between a $220K Director offer and a $180K Senior IC offer is often not technical depth; it is whether you sound like someone who runs a function vs. someone who executes tasks within one. Every question in a Director/VP loop is a test of one thing: "Does this person think in systems of people and risk, or in systems of code and config?"

Interviewers at Director level are not grading you on whether you know the exact Kubernetes scheduler algorithm. They are grading whether you can hold a conversation about tradeoffs, org design, and business continuity without needing a whiteboard. Your T-Mobile story — zero Sev1 incidents in 36 months, 25M msg/day platform, 15-person team — is your credential. This week, you learn to deploy it precisely.

## Analogy

Think of this week as a tabletop incident drill, except the incident is the interview itself. In an actual P1, you do not improvise for the first time when production is down. You have runbooks. You have practiced communication. You have a known escalation path. The mock interview system here is your runbook for the conversation.

In RabbitMQ terms: your T-Mobile stories are pre-loaded messages in a persistent queue. The interviewer's questions are consumers. Your job this week is to make sure every consumer gets exactly the right message, routed correctly, with no dead-letter queue.

## Vocabulary Translation Table

| Their Term | Your Existing Mental Model |
|---|---|
| "Tell me about a time you scaled a team" | Post-incident capacity review — what broke, what you added, why |
| "How do you set SLOs?" | SLA negotiation with internal customers — same thing, internal contract |
| "What's your philosophy on toil?" | Queue depth management — reduce what clogs the pipeline |
| "How do you handle underperformers?" | Incident triage — is it a person issue, a process issue, or a tooling issue? |
| "What's your hiring bar?" | Reliability bar — what failure rate is acceptable in your team? |
| "How do you earn executive trust?" | Change management — show the blast radius before you push the button |
| "What's your AI strategy?" | Automation pipeline — what gets automated, what stays human-in-the-loop |
| "What does good SRE culture look like?" | Blameless postmortem culture — psychological safety + accountability |

---

## 30-Second Version

You have three interviews to prepare for: startup speed round, enterprise director loop, and CTO philosophy screen. Each requires a different gear. The foundation is the same: your T-Mobile story, told at the right altitude for the audience.

## 2-Minute Version

Director/VP interviews test four things simultaneously: technical credibility (can you talk to your ICs), leadership judgment (can you make hard calls), business translation (do you speak P&L and risk), and cultural fit (does your operating style match their stage). Most senior SRE candidates fail not because they are unqualified but because they pitch IC depth in a Director seat. This guide re-trains your default register from "here is how I built X" to "here is why I chose X, what it cost, and what I would do differently at 3x the scale."

## 5-Minute Version

The three failure modes at Director-level interviews:

**Failure Mode 1 — IC Gravity.** You get a systems design question and spend 12 minutes explaining implementation details. The interviewer wanted to know how you would staff the team, how you would communicate progress to the CTO, and what you would stop doing to make room for it. Fix: every technical answer ends with "and here is how I would govern this across a team of N people."

**Failure Mode 2 — Story Recycling.** You use the same T-Mobile story for five different questions. The interviewer notices. Fix: you need at least eight distinct stories mapped to eight competencies. This guide provides the mapping.

**Failure Mode 3 — Philosophy Vacuum.** When asked "what is your philosophy on SRE?" you recite the Google SRE book. It sounds borrowed. Fix: your philosophy comes from 21 years of operational scar tissue, not from a book. Part 4 of this guide drafts it in your voice.

---

## Director/VP Lens

**As a Director/VP, you are being assessed on:**
- Span of control: can you lead 4–6 managers, not just 15 ICs?
- Budget ownership: have you owned headcount and tooling budgets?
- Cross-functional authority: can you influence product, infra, and security without direct authority?
- Talent pipeline: do you have a hiring philosophy and a development track record?
- Risk communication: can you translate "error budget burn rate" into "business risk" for a VP of Engineering?

**What an IC implements vs. what a Director governs:**

| Domain | IC Implements | Director Governs |
|---|---|---|
| SLO | Writes the PromQL query | Sets the SLO policy and review cadence |
| Incident response | Runs the incident | Owns the postmortem culture and MTTR trend |
| Kubernetes | Configures the cluster | Decides cluster topology and ownership model |
| Hiring | Passes the interview | Defines the hiring bar and pipeline |
| Tooling | Builds the dashboard | Decides build vs. buy and deprecation schedule |
| AI adoption | Uses Copilot | Sets the AI strategy and guardrails for the team |

---

# PART 1: MOCK INTERVIEW SCRIPTS

---

## Interview A — Startup/Series C (45 min)

**Context:** Series C, 120-person company, first dedicated SRE Director hire. Currently 3 SREs embedded in product teams. Platform is AWS-native, Kubernetes, moving from manual deploys to GitOps. Engineering VP is the interviewer for the technical portion.

---

### Section A1: Recruiter Pre-Screen (10 min) — 5 Questions + Model Answers

---

**Q1. "Walk me through your background in 2 minutes."**

Model Answer:

"I am an SRE Manager at T-Mobile currently running a 15-person team that owns a notification platform processing 25 million messages per day on Kubernetes on AWS. Before T-Mobile I spent 21 years across telecom, banking, and retail building the operational backbone — middleware, observability, incident command — before that was called SRE. What drew me to this role is that you are at the stage where the reliability function needs to be built correctly the first time. I have done that before from scratch and I want to do it again with more scope."

Why this works: it anchors seniority (21 years), quantifies scale (25M msg/day), signals self-awareness about the company stage (Series C needs a builder), and ends with forward intent not backward credential.

---

**Q2. "Why are you leaving T-Mobile?"**

Model Answer:

"T-Mobile gave me an extraordinary operational education. What I am looking for now is a role where I own the reliability strategy end-to-end — the architecture decisions, the team shape, the tooling philosophy — not just the execution layer within a larger org. At a Series C, the decisions I make in year one become the foundation the company builds on. That is the scope I am ready for."

Why this works: no negativity about current employer, frames the move as a pull not a push, signals ambition calibrated to the stage.

---

**Q3. "What is your compensation expectation?"**

Model Answer:

"I am targeting Director-level total compensation in the range of $230K to $270K depending on the equity structure and stage. I am flexible on cash-equity split if the equity has strong mechanics. I would also want to discuss H1B transfer support — I have an approved I-140 and the transfer is straightforward, but premium processing coverage, around $2,800, is something I factor in."

Why this works: gives a range not a single number, introduces H1B proactively but after establishing value, frames it as a logistics item not a liability.

---

**Q4. "Have you built an SRE practice from scratch before?"**

Model Answer:

"Not from zero headcount, but I have built from operational chaos. When I joined the notification platform team, we had no SLO framework, alert fatigue was severe, and on-call was unsustainable. Within 18 months I built the SLO governance model, reduced alert volume by 60%, and established the blameless postmortem process. The team went from reactive firefighting to proactive reliability engineering. At your stage, that is effectively the same challenge — the tooling exists but the culture and governance do not yet."

---

**Q5. "How do you think about SRE at a 120-person company vs. a company like T-Mobile?"**

Model Answer:

"At scale, SRE is about governance, consistency, and preventing entropy across hundreds of teams. At 120 people, SRE is about setting defaults — the paved road, the golden path — that product engineers will actually use because it makes their lives easier, not because policy forces them. The tactical work is different but the principle is the same: make reliability the path of least resistance."

---

### Section A2: HM Technical Screen (35 min) — 8 Questions + Model Answers

---

**Q1. "We have 3 SREs embedded in product teams. How would you restructure this in the first 90 days?"**

Model Answer (IC + Director framing):

"First, I would not restructure in 90 days — I would observe. The embedded model exists for a reason. I would spend the first 30 days doing structured listening: how is on-call burden distributed, where is the toil concentrated, what does each product team actually need from SRE. In days 31-60, I would identify the two or three platform capabilities that every team needs but no one owns — usually observability, incident coordination, and deployment standards. In days 61-90, I would propose a hybrid model: a small platform SRE function that owns shared tooling, with the embedded SREs becoming the interface layer. I would not do a big-bang reorganization because reliability during a reorg is an oxymoron."

Director lens addition: "I would also establish a reliability council in month two — product engineering leads, myself, and the CTO — meeting monthly to review error budget burn and prioritize reliability investment. That council is how you scale SRE influence without scaling headcount."

---

**Q2. "How would you decide whether to use PagerDuty vs. building your own alerting pipeline?"**

Model Answer:

"Build vs. buy for on-call tooling is a solved problem — always buy. On-call tooling is not a competitive differentiator. PagerDuty, Opsgenie — both work. The decision I would make in the first month is which one, and then standardize it. The real question underneath your question is: how do you decide what to build vs. buy as an SRE function? My rule is: if the problem is in your value chain — observability queries, runbook logic, SLO definitions — build it. If the problem is commodity infrastructure — alerting pipelines, secrets management, certificate renewal — buy it or use cloud-native."

---

**Q3. "We are moving from manual deploys to GitOps. What reliability risks does that introduce?"**

Model Answer:

"Three risks in roughly this order of probability. First, blast radius expansion — GitOps makes it easy to deploy often, which is good, but without progressive delivery controls like canary or blue-green, you go from one manual mistake per week to automated mistakes per hour. Second, secret sprawl — when you move to Git-driven deployments, secrets management becomes critical; if engineers start putting secrets in manifests because it is the easy path, you have a compliance and security debt that compounds. Third, runbook rot — your incident runbooks assume the old deployment model; the first time something goes wrong with a GitOps deploy, the team will not know where to look. I would front-load runbook updates before the rollout, not after."

---

**Q4. "Describe how you would instrument a new service for observability from day one."**

Model Answer:

"The framework I use maps to MELT: Metrics, Events, Logs, Traces. For a new service on Kubernetes, I start with: one, the four golden signals as Prometheus metrics exposed on a /metrics endpoint — latency, traffic, errors, saturation. Two, structured logging in JSON to a central aggregator, with trace IDs in every log line so you can correlate. Three, distributed tracing via OpenTelemetry SDK — I would have them instrument the service in the language-native OTel SDK before it ever hits production. Four, a synthetic probe — a simple health check that fires every 60 seconds from outside the cluster. The synthetic is what catches the 3am 'service is up but not responding correctly' class of incident. I have caught two significant silent failures with synthetics that metrics completely missed."

---

**Q5. "How do you set SLOs for a new service when you have no historical data?"**

Model Answer:

"You borrow and negotiate. First, if the service has a predecessor or a comparable service in the industry, you start with its SLO as a baseline. Second, you negotiate with the product team and the business stakeholders: what does a bad user experience look like, and how often is acceptable? For a notification delivery service, for example, a message delivered more than 30 seconds late is functionally a failure for an SMS alert. That 30-second threshold becomes your latency SLO. Third, you set conservative targets for the first 60 days — 99% availability, not 99.9% — because you need to observe the natural error rate before you can commit to a number. The worst thing you can do is set a 99.9% SLO on day one and burn your error budget in week one because you did not account for the deployment noise."

---

**Q6. "A product engineer comes to you and says 'SRE is slowing us down.' How do you handle it?"**

Model Answer:

"I start by assuming they are right. If a product engineer feels that SRE is friction, then somewhere SRE is imposing a process that does not justify its cost. I schedule a 30-minute conversation — not a review, a conversation — and ask them to walk me through the last three times they felt blocked. Usually it is one of three things: the deployment checklist is too long, the on-call escalation path is unclear, or a reliability gate caught something that felt like a false positive. I fix the specific thing first. Then I look at whether it is a pattern. SRE is a service function. If our customers — the product engineers — are complaining about the service, that is a signal, not a confrontation."

Director lens addition: "At the leadership level, I also track 'SRE NPS' informally — I ask engineering managers in our monthly 1:1s: is SRE making your team faster or slower? That question, asked regularly, prevents the friction from becoming resentment."

---

**Q7. "What is the first metric you look at when you join a new company as an SRE Director?"**

Model Answer:

"Mean time to detect, MTTD. Not MTTR — MTTR is a lagging indicator of how well you respond after something goes wrong. MTTD tells me how good your observability is, how well your alerts are tuned, and whether your on-call team is overwhelmed with noise. If MTTD is high — say, customers are detecting issues before your monitoring does — that tells me within 30 days where the investment needs to go. At T-Mobile when I took over, our MTTD for notification delivery failures was 8 minutes. Customers were getting complaint calls before our alerts fired. We fixed that to under 90 seconds by adding synthetic probes and tightening alert thresholds. That 90-second MTTD is now a KPI I report to the VP of Engineering quarterly."

---

**Q8. "How would you build a 12-person SRE team from the current 3-person team over 18 months?"**

Model Answer:

"I would phase it in three stages. Stage one, months one to six: hire two senior SREs whose job is platform — shared observability, deployment standards, incident tooling. Do not hire junior until the platform is stable, because junior engineers need a functional platform to learn on. Stage two, months seven to twelve: hire four mid-level SREs aligned to product domains — payments, user services, data pipeline. Each one works with the embedded SRE already there and inherits their context. Stage three, months thirteen to eighteen: evaluate whether you need a Site Reliability Engineer Manager to own the team operationally while I focus on the Director-level function. By month 18, the team shape is: two platform SREs, six product-aligned SREs, one SRE Manager, one staff/principal SRE who owns architecture. Total: ten plus the three originals equals thirteen. I said twelve — one role I keep open as a flex hire depending on where the growth is."

Director lens addition: "Hiring plan at this pace also requires a sourcing strategy, not just job postings. I would establish a referral pipeline from the existing team in month two, and a college recruiting track for entry-level in month six. At 120 people, your employer brand is strong enough to attract from good programs if you invest in it."

---

## Interview B — Enterprise Director Loop (60 min)

**Context:** Large enterprise, 400-person engineering org, VP Engineering role open, current team has 3 SRE managers and 25 SREs. Platform is multi-cloud (AWS + Azure), 200 microservices, SOC2 and PCI compliance required.

---

### Section B1: System Design Round (20 min) — "Design observability for a 200-service platform"

**Prompt:** "You have 200 microservices, mixed AWS and Azure, some greenfield and some 10-year-old Java monoliths. Design an observability platform that gives you meaningful signal."

Model Answer Structure (speak this aloud in about 6 minutes, then expect follow-ups):

**Start with requirements clarification (always do this — it signals Director thinking):**
"Before I draw architecture, let me validate scope. Are we designing for external-customer-facing SLOs or internal engineering efficiency or both? Do we have a central SRE team that owns the platform, or is this distributed? What is the current state — are we starting from nothing or refactoring something? And is there a cost ceiling?"

**Assume: both internal and external SLOs, central SRE team, mixed current state, $500K/year observability budget.**

**The three-layer design:**

Layer 1 — Collection. Every service emits OpenTelemetry (OTel) — structured logs, metrics, traces via a language-native OTel SDK. For the legacy Java monoliths where code changes are expensive, instrument via the OTel Java agent attached at JVM startup — zero code change required. Deploy an OTel Collector as a DaemonSet on every Kubernetes node and as a sidecar on legacy VMs. The collector handles batching, retry, and routing. This is the only point where you standardize signal format before it hits storage.

Layer 2 — Storage. Three purpose-built stores. Metrics: Prometheus remote-write to a managed Prometheus or Cortex cluster — you want long-term retention of aggregated metrics at 15-day granularity for SLO burn rate reporting. Logs: centralized to Elasticsearch or Splunk depending on existing team expertise — given my background, I would evaluate Splunk seriously here because its alerting and ML capabilities reduce the analyst burden. Traces: Tempo or Jaeger, retained for 7 days because trace volumes are large and 7 days covers your longest incident investigation window. All three stores write to S3 cold storage after retention, because you will need it for the next PCI audit.

Layer 3 — Presentation and alerting. A single Grafana instance with role-based dashboards — executive layer shows SLO burn rates by business capability, not service. Engineering layer shows golden signals per service. On-call layer shows alert triage boards. All SLO alerts route to PagerDuty. Runbooks are linked directly from the alert. Every runbook is reviewed quarterly — this is a governance requirement, not a nice-to-have.

**Follow-up likely: "How do you onboard a new service?"**

"The golden path: you give engineers a service template repository — Terraform module plus Kubernetes manifest template plus OTel SDK already wired in. They clone, they configure service name and business domain, they deploy. The OTel collector picks it up automatically. On day one of a new service, I have metrics, logs, and traces. The only manual step is writing the initial SLO definition, and I make that a required field in the service registration PR template."

**Follow-up likely: "How do you handle the legacy Java monoliths?"**

"JVM agent instrumentation for traces and metrics. Log parsing is messier — I would deploy Fluentbit as a sidecar log shipper with a structured parsing rule for each monolith. Yes, it is per-application configuration. Yes, it is toil. I schedule one legacy onboarding per sprint for the first 6 months until the full estate is covered. I do not boil the ocean — I start with the three services that cause the most on-call pages."

---

### Section B2: Leadership Round (20 min) — Org Design, Hiring, Conflict Resolution

---

**Q1. "How do you structure an SRE org of 25 people across 200 services?"**

Model Answer:

"I would use a federated model with a central platform team. The central platform team — about six people — owns the shared observability stack, incident coordination tools, deployment standards, and chaos engineering capability. They are the 'SRE infrastructure' team. The remaining 19 SREs are organized into product-aligned pods — typically three to four SREs per pod, each pod aligned to a business domain like payments, identity, or data. Each pod has a lead SRE who reports to an SRE manager. I would have three SRE managers reporting to me, each managing roughly three pods plus the platform team.

The benefit of the federated model over a fully centralized or fully embedded model is that you get standardization from the center and context from the edge. The failure mode of this model is when the central platform team builds things no one uses because they are too abstracted from real product problems. I prevent this by requiring every platform team member to rotate through on-call for a product domain for one quarter per year. You cannot build good platform tooling if you have never been woken up at 3am by the alerts it generates."

---

**Q2. "Tell me about a time you had to let someone go. What was the process?"**

Model Answer (STAR format, T-Mobile anchored):

"Situation: I had a senior SRE on my team who had been a high performer two years prior but had been missing deliverables for eight months. The team had noticed. On-call rotations were being quietly redistributed to cover for them.

Task: I needed to either rehabilitate the performance or make a change, and I needed to do it without destroying team morale or creating a liability.

Action: I started with a structured 1:1 conversation — not a PIP, a conversation. I asked directly: what has changed, is there something outside work affecting you, what support do you need? The answer was burnout compounded by a mismatch between their skills and where the team's technical work had moved. We tried a role adjustment for 60 days — reduced on-call exposure, more architectural work. It did not close the gap. I initiated a Performance Improvement Plan in partnership with HR, with specific measurable outcomes over 90 days. At the end of the 90 days, the outcomes were not met. I made the call to part ways. I managed the transition so the team's on-call coverage was stable before the last day.

Result: The team's overall performance improved within 60 days of the change. Two team members told me in 1:1s that they had been waiting for it and felt that management was now credible. The lesson I took forward: delayed action on a performance issue is not kindness — it is a leadership failure that the whole team pays for."

---

**Q3. "How do you manage conflict between SRE and a product engineering team that thinks reliability gates slow them down?"**

Model Answer:

"Conflict between SRE and product is usually a symptom of misaligned incentives, not a people problem. Product is measured on feature velocity. SRE is measured on availability. If those measurements are not connected at the leadership level, conflict is structural.

My resolution process: First, I get the data. I pull the last quarter's deployment frequency, change failure rate, and MTTR by team. I want to show whether the reliability gates are correlated with better outcomes, not just assert it. Second, I bring the product engineering director into a joint review — not a debate, a review. We look at the data together. Third, we renegotiate the gates. Usually there are two or three gates that are genuinely bureaucratic — left over from an old incident that no longer applies — and removing them reduces friction by 40% without increasing risk. Fourth, I establish a shared metric: change failure rate. Both teams are accountable. Suddenly product is invested in reliability, because their deployment success rate is on their scorecard too."

---

### Section B3: Technical Depth Round (20 min) — K8s + Terraform + DevSecOps

---

**Q1. "An EKS node is OOMKilled repeatedly. Walk me through your diagnosis."**

Model Answer (speak as if briefing your team lead):

"OOMKill means the kernel killed a container because it exceeded its memory limit. I check five things in order. One: `kubectl describe pod <pod>` — look at the last state, confirm it is OOMKilled not CrashLoopBackOff for a different reason. Two: check the container's memory limit in the deployment spec — is there a limit set, and is it realistic? I have seen limits set to 256Mi on a Java service that needs 1Gi. Three: `kubectl top pod` to see current memory consumption versus the limit. Four: look at the application logs for OOM signals — Java heap dumps, Python memory errors — to understand whether this is a leak or a workload growth problem. Five: check for memory pressure at the node level with `kubectl describe node` — if the node is at 90% memory, the scheduler may be packing too many pods. The fix depends on diagnosis: if it is a limit misconfiguration, adjust the limit and set a Request equal to the observed baseline. If it is a memory leak, that is a code fix. If it is node pressure, it is a scheduling or cluster autoscaler configuration issue."

Director lens: "At the governance level, I require memory limits and requests on every pod in our admission policy — enforced by OPA Gatekeeper. An OOMKill on a production service is usually a code review or deployment review failure, not just an ops issue. I review OOMKill frequency in my weekly reliability metrics."

---

**Q2. "Your Terraform state file is corrupted in S3. What do you do?"**

Model Answer:

"First, do not panic and do not run terraform apply. A corrupted state file means Terraform does not know what it owns, and running apply could create duplicates or destroy live resources. My recovery process: One, immediately enable state locking if it is not already locked — DynamoDB lock prevents concurrent writes while you are in recovery. Two, check S3 versioning — every production state bucket should have versioning enabled. Restore the most recent valid version of the state file from S3 version history. Three, run `terraform plan` with the restored state and compare the output against what you know is deployed. You are looking for drift — resources that exist in AWS but are not in the state. Four, use `terraform import` to bring any drifted resources back into state. Five, write the incident postmortem: how did the state get corrupted, what is the guard rail that prevents this? Usually the answer is a missing state lock or someone manually edited the state file. The fix is: state locking mandatory, state file access restricted to Terraform role only, human hands never touch the state file directly."

---

**Q3. "How do you prevent secrets from being committed to Git in a DevSecOps pipeline?"**

Model Answer:

"Defense in depth across three layers. Layer one is prevention at the developer workstation: pre-commit hooks using tools like detect-secrets or gitleaks. These run before `git commit` and block the push if they find entropy patterns or known secret formats — AWS access keys, API tokens. Layer two is enforcement in the CI pipeline: the same gitleaks scan runs in the pipeline as a mandatory gate. The pipeline fails if secrets are detected. This catches anyone who bypasses or disables the pre-commit hook. Layer three is policy: OPA or Checkov policy that validates Kubernetes manifests and Helm charts do not contain plaintext secrets — all secrets must reference a Kubernetes Secret object or an external secrets manager. The Kubernetes Secrets themselves are backed by AWS Secrets Manager or Vault via the External Secrets Operator. The developer never writes a secret value directly — they write a reference to the secret path. If you want the belt-and-suspenders addition: enable AWS CloudTrail and set an alert if anyone reads the production secrets path from outside the CI/CD service account. That gives you detection even if prevention fails."

---

## Interview C — Executive/CTO Screen (30 min)

**Context:** Series B company, CTO is a former SWE architect, now 3 years in executive role. Evaluating whether to hire a VP SRE or keep reliability embedded in engineering. This is a philosophy and strategic conversation.

---

**Q1. "Why does a company our size need a VP of SRE?"**

Model Answer:

"You probably do not need the title — you need the function. The question is whether reliability as a capability has an owner with organizational authority. Right now, reliability work is distributed: product engineers handle it when it breaks, platform engineers handle some of it systematically. What you are missing is someone whose job it is to ask: what is the cost of unreliability to the business, how much are we investing in prevention vs. firefighting, and what does the reliability roadmap look like 18 months out? That is a Director or VP function. The alternative — keeping it distributed — works until you have a major incident that reveals that no one owns the postmortem culture, no one tracks MTTR as a business metric, and no one had authority to push back on the feature release that caused it."

---

**Q2. "What is your view on AI replacing SRE engineers?"**

Model Answer:

"AI will replace a class of SRE tasks: log triage, runbook execution, alert correlation, first-level incident diagnosis. These are pattern-matching tasks with bounded state spaces, and LLMs are genuinely good at them. What AI will not replace in the near term is the judgment layer: deciding which SLO to set given business constraints, managing the human dynamics of an incident when the CTO is in the bridge call, making the build-vs-buy call on a new observability tool, convincing a VP of Product that the reliability investment needs to happen before the next feature launch. Those require contextual authority and organizational trust. My job as a Director is to automate everything below my judgment threshold and keep pushing that threshold up. An AI-augmented SRE team of eight can do what a non-augmented team of fifteen can do — I have been building toward that ratio for the last 18 months."

---

**Q3. "Tell me about the biggest reliability mistake you ever made."**

Model Answer:

"The biggest one was a mistake of omission. Early in my time at T-Mobile, I inherited an alerting configuration from the previous team and did not audit it for the first six months because we were not having incidents. Then we had an incident — a RabbitMQ queue depth buildup that took down notification delivery for 11 minutes — and the postmortem revealed that we had had the precursor signals in Splunk for four hours. The alert existed, but the threshold was set so high it never fired. Eleven minutes of outage that should have been a two-minute ops task.

What I changed: I built a quarterly alert audit into our operating rhythm. Every alert gets reviewed: is the threshold calibrated to current traffic? Is the runbook still accurate? Is someone actually trained to respond to it? That audit process has caught three potential incidents in the 18 months since. The mistake was treating inherited configuration as trustworthy. The lesson is: trust is earned, not inherited — in people and in systems."

---

**Q4. "How do you think about the relationship between security and reliability?"**

Model Answer:

"They are the same function with different threat models. Reliability engineering asks: what are all the ways this system can fail, and how do we prevent them? Security engineering asks the same question about adversarial failures specifically. The tooling is different but the discipline is identical — failure mode analysis, defense in depth, blast radius minimization. At the Director level, I break down the organizational wall between them because the wall creates gaps. The classic gap is: the security team patches a kernel vulnerability, the SRE team does not know about the rolling restart, and the rolling restart triggers an incident because pod disruption budgets were not configured. If security and SRE have a shared change calendar and a shared blast radius review, that incident does not happen. I run a joint weekly review — 30 minutes, security lead and SRE lead, reviewing the upcoming change calendar together."

---

**Q5. "What does your ideal SRE team culture look like?"**

Model Answer:

"It looks like a team where the 3am page is never a surprise. Not because nothing goes wrong, but because the team has modeled the failure modes in advance, written the runbook, and practiced the response in a game day. The cultural marker I look for is: when something goes wrong, does the team's first instinct to ask 'who broke it?' or 'what failed?' Blameless postmortem culture is not a process — it is a belief that systems fail before people do. You get to blameless culture by demonstrating it at the top. Every time I run a postmortem, I look for the process failure first. The human mistake is usually the last link in a chain that started with missing safeguards. When you find the chain, you fix the chain. That is the culture I build and the culture I would bring here."

---

**Q6. "How do you make the case for reliability investment to a board or CFO?"**

Model Answer:

"I translate reliability into two numbers they already understand: revenue impact and insurance cost. Revenue impact: if the platform processes X transactions per minute and the average order value is Y, then one minute of downtime costs X times Y. I calculate that number once, write it on the wall, and refer back to it every time I am asking for headcount or tooling budget. Insurance cost: the alternative to investing in reliability is not zero cost — it is incident cost. I track engineering hours spent on incidents per quarter. At T-Mobile, the notification platform team was spending roughly 30% of engineering capacity on reactive incident work in the year I inherited it. I reduced that to under 8% in 18 months. The 22% delta — roughly 3 FTE equivalents — was the ROI of the reliability investment. That is the conversation that gets a CFO to nod."

---

**Q7. "What is the most important thing you look for when hiring a senior SRE?"**

Model Answer:

"Calibrated pessimism. I want someone who reads a new architecture diagram and immediately starts asking 'what fails first?' Not because they are negative — because that is the job. The best SREs I have hired have an almost allergic reaction to confidence in systems they have not yet broken. They ask about failure modes in design reviews. They write chaos tests before the service is in production. They treat documentation as a reliability artifact, not an afterthought. The second thing I look for is communication under pressure. In a technical interview, I often ask candidates to explain a complicated failure they debugged. I am less interested in the solution than in how they communicated during the incident. If they can tell me clearly what they knew, what they did not know, and how they communicated uncertainty to stakeholders, I know they can function in a real P1. You can teach Kubernetes. You cannot teach calmness under pressure and intellectual honesty."

---

**Q8. "Where do you see SRE as a discipline in five years?"**

Model Answer:

"SRE in five years looks like platform engineering with a reliability lens built in. The IC work of writing runbooks, building dashboards, and triaging alerts will be largely AI-assisted. The role that survives is the reliability architect — someone who designs systems for failure, sets the organizational standards, and owns the risk conversation with the business. The team structure shifts: fewer reactive responders, more people who build internal developer platforms that make reliability the default for product teams. The metric that replaces 'number of incidents' is 'percentage of engineers who shipped without needing SRE intervention because the platform handled it.' That is the five-year vision I am building toward, and it is why I invest in golden paths and internal platform capabilities rather than just adding on-call headcount."

---

# PART 2: DIRECTOR/VP QUESTION BANK

Eight domains, five Director-level questions each, with model answers.

---

## Domain 1: Org Design and Team Structure

**Q1. "How do you decide between embedded SRE and a central SRE team model?"**

Answer: Embedded model maximizes product context but creates inconsistency and isolation — each SRE reinvents the wheel. Central model maximizes standardization but creates ivory tower syndrome — the central team builds things for a customer they do not really understand. The right answer is almost always federated: a small central platform team (3–5 people) owning shared tooling and standards, with domain-aligned SREs who report to SRE management but work closely with product teams. Decision trigger: if you have more than 3 product teams and more than 8 SREs, start building the platform function.

**Q2. "How large should an SRE team be relative to the engineering org?"**

Answer: The Google model suggests 10% of engineering for embedded SRE. In practice, modern tooling allows 6–8%. For a 100-person engineering org, 7–10 SREs is right. The ratio degrades if you have large amounts of legacy infrastructure — legacy doubles the toil load. The ratio improves if you have a mature internal developer platform. I track the ratio quarterly and treat it as a risk indicator, not a target.

**Q3. "How do you handle the 'SRE as bottleneck' anti-pattern?"**

Answer: The bottleneck appears when SRE approval is required for deploys. Fix: move from gatekeeping to guardrailing. SRE writes the policy — deployment must pass automated reliability checks. SRE does not approve individual deploys. The policy runs in the pipeline. SRE reviews the policy quarterly. This scales infinitely and removes the bottleneck while maintaining the standard.

**Q4. "What does the career ladder for an SRE look like?"**

Answer: SRE I (operational execution) → SRE II (independent investigation) → Senior SRE (design and cross-team influence) → Staff SRE (org-wide reliability architecture) → Principal SRE (company-wide technical strategy, external influence). The IC track goes to Principal. The management track diverges at Senior: SRE Tech Lead → SRE Manager → Director → VP. I make both tracks explicit and equivalent in compensation at the Staff/SRE Manager level. People should not feel forced into management to grow financially.

**Q5. "How do you maintain technical credibility as a Director without being an IC?"**

Answer: Three practices. One: I stay on the on-call rotation for a reduced but consistent shift — one week per quarter. This keeps my debugging skills sharp and gives me credibility in the postmortem room. Two: I own one technical project per quarter — a tool, a policy, a proof-of-concept — end to end. I present it to the team. Three: I read every postmortem personally and ask technical follow-up questions in the review. My team knows I can go deep if needed. That knowledge is the credibility.

---

## Domain 2: Incident Management and Postmortems

**Q1. "What is your incident severity model?"**

Answer: I use a four-tier model aligned to customer impact, not technical failure. P0: customer-facing revenue impact, all hands. P1: customer-facing degradation or compliance breach, SRE lead + product owner. P2: internal system degradation, SRE on-call. P3: monitoring gap or risk identified, no current customer impact. The key principle: severity is defined by customer impact, not by how scary the technical failure looks. A database failover that customers never noticed is P3. A 5% error rate on checkout is P1 even if the root cause looks simple.

**Q2. "What makes a postmortem actually useful vs. ceremonial?"**

Answer: A useful postmortem has three properties. One, it identifies contributing factors in the system, not blame in the person. Two, it produces action items with owners and due dates, and those action items are tracked. Three, it is reviewed at the next incident or within 30 days — whichever comes first — to verify the action items closed. The ceremonial postmortem has the write-up but not the tracking. I require action item closure rates in my quarterly reliability review. If action items from postmortems are not closing, either the items are wrong or the team is too busy to fix things, and both are signals I need to act on.

**Q3. "How do you handle an incident where the root cause is a vendor?"**

Answer: Same postmortem process, different action item category. You cannot fix your vendor's code, but you can: harden your blast radius (circuit breakers, fallback behavior), improve your detection (synthetic monitors, vendor status page integration), establish SLA credit processes, and evaluate the build-vs-buy decision for next cycle. I document vendor incidents separately in a vendor reliability register and review it quarterly with procurement. Vendors with persistent SLA misses get put on a 90-day improvement plan or a replacement evaluation.

**Q4. "How do you measure the effectiveness of your incident management program?"**

Answer: Four metrics, reviewed monthly. MTTD (mean time to detect) — target is improving trend. MTTR (mean time to recover) — absolute target depends on SLO but I want quarter-over-quarter improvement. Repeat incident rate — if the same class of incident occurs twice in 90 days, the postmortem action items failed; this is a leading indicator of postmortem quality. On-call alert-to-page ratio — what percentage of alerts actually required a human response? If it is above 30%, you have alert fatigue. Below 10% and you may be missing signals.

**Q5. "Tell me about a time you improved MTTR significantly."**

Answer (T-Mobile anchored): "When I joined the notification platform team, MTTR for queue depth incidents was averaging 45 minutes. The diagnostic process was entirely manual — engineer SSHed in, ran queries, correlated logs across three systems. I built a runbook-as-code framework in Python that automated the first five diagnostic steps: check queue depth across all RabbitMQ nodes, pull the last 100 error logs, check consumer health, verify upstream producer rate, compare to baseline. The runbook ran in 90 seconds and produced a structured report. Average MTTR dropped to 12 minutes within 60 days. The remaining 12 minutes is human decision time — and that is appropriate. I do not want to automate the decision, only the diagnosis."

---

## Domain 3: SLO/SLI Governance

**Q1. "How do you establish SLOs for services that have never had them?"**

Answer: Four-step process. One, identify the user journey, not the service — what does the user experience? Two, identify the measurable signal that represents that experience — latency at the 95th percentile, error rate, availability. Three, set a target based on historical data or, if no data exists, negotiate a draft target with the product team and revisit in 60 days. Four, define the error budget — if the SLO is 99.5% availability, the error budget is 0.5% of the reporting window. The error budget is the forcing function for reliability investment decisions. If you burn the budget, you pause feature work and focus on reliability. If you have budget remaining, you can take calculated risks.

**Q2. "How do you handle a team that consistently burns their error budget?"**

Answer: I treat chronic error budget burn as a staffing and architecture signal, not a discipline problem. If a team burns their budget every quarter, one of three things is true: the SLO is unrealistic for the current architecture (wrong target), the team does not have the reliability investment to meet the target (resource problem), or the team is deploying features too fast without reliability work (incentive problem). I diagnose which one it is before prescribing anything. If it is a resource problem, I make the case to leadership: here is the cost of unreliability, here is the investment required to close the gap. That is a budget conversation, not a team performance conversation.

**Q3. "What is your error budget burn rate alert strategy?"**

Answer: I use a multi-window burn rate alert — Google's alerting approach from the SRE Workbook. Short window (1 hour at 14x burn rate) catches fast-burning incidents. Medium window (6 hours at 6x burn rate) catches sustained degradation. Long window (3 days at 3x burn rate) catches slow leaks. Three separate alerts, three separate severities. The short window is P1 — page immediately. The medium window is P2 — notify the team. The long window is a weekly review item. Most teams start with just a raw budget-remaining alert, which only fires when you are almost out of budget — too late to be useful.

**Q4. "How do you get product management to care about error budgets?"**

Answer: You make them share ownership of the budget. In my model, the SRE team does not own the error budget alone — the product team co-owns it. Their sprint planning includes a budget review: how much budget do we have this sprint, how risky are the planned releases, do we need to slow down? When product managers see that a high-velocity sprint is burning 40% of the monthly error budget in a week, they start asking their engineers better questions. The budget becomes a shared resource, like engineering capacity or infrastructure cost. People protect shared resources they can see.

**Q5. "What is the relationship between SLOs and on-call load?"**

Answer: Direct and often ignored. If your SLO is too tight — say 99.99% on a service that is naturally 99.9% reliable — you will page your on-call team for every minor fluctuation because the alert thresholds have to be tight to detect budget burn in time. This creates alert fatigue and on-call burnout. The right SLO is the minimum reliability level that makes the customer happy, not the maximum achievable reliability. I audit the correlation between SLO tightness and on-call page volume quarterly. Any service where on-call pages are correlated with SLO burn at greater than 80% is a candidate for SLO re-evaluation.

---

## Domain 4: Kubernetes and Platform Engineering

**Q1. "How do you govern Kubernetes access across a 200-service platform?"**

Answer: RBAC with a least-privilege baseline, enforced via GitOps. Every team gets a namespace. Every namespace has a RoleBinding that grants namespace-level access to the team's CI/CD service account and read-only access to the team members. No one gets cluster-admin in production except the SRE platform team, and that access is time-bound and audited. Admission webhooks via OPA Gatekeeper enforce policies at the API server level: no privileged containers, all pods must have resource limits, all images must come from the internal registry. The policies are stored in Git and reviewed quarterly. Violations alert to the security Slack channel and are reviewed weekly.

**Q2. "How do you manage cluster upgrades across a fleet without causing incidents?"**

Answer: Blue-green cluster upgrades when budget allows, rolling node upgrades when not. Before any upgrade: run the Kubernetes upgrade compatibility matrix against all deployed manifests and Helm charts, identify any deprecated API versions, and require teams to fix deprecations in the sprint before the upgrade window. The upgrade window is scheduled during low-traffic hours with a 30-minute rollback window. Every cluster upgrade has a dedicated on-call engineer for 24 hours post-upgrade. I have seen more incidents in the 8-hour window after an upgrade than during the upgrade itself — the delayed failures from changed scheduler behavior or admission webhook incompatibilities. The 24-hour watch catches those.

**Q3. "What is your pod disruption budget strategy?"**

Answer: Default rule: every deployment with more than one replica gets a PodDisruptionBudget of maxUnavailable=1 for stateless services and minAvailable=51% for stateful services. This prevents cluster maintenance operations from taking down entire deployments. The failure mode I watch for is PDB deadlock: if every service has maxUnavailable=0, the cluster cannot drain nodes for maintenance. I require teams to set realistic PDBs in their deployment templates and I test them quarterly with a controlled node drain in staging. Any PDB that blocks a drain gets escalated to the team for review.

**Q4. "How do you handle a misconfigured admission webhook that is blocking all deployments?"**

Answer: This is a high-severity incident — it blocks every team. Immediate response: identify the webhook with `kubectl get validatingwebhookconfigurations` and `kubectl get mutatingwebhookconfigurations`. Check the `failurePolicy` field — if it is set to `Fail`, a webhook service outage blocks all deployments. Short-term fix: patch the `failurePolicy` to `Ignore` to restore deployment capability while you debug the webhook itself. Medium-term fix: restore the webhook service, test it, switch policy back to Fail. Long-term fix: require all production webhooks to have a `namespaceSelector` that excludes the `kube-system` namespace and a circuit-breaker test in the webhook deployment process. Director note: every webhook in my org goes through a blast radius review before production deployment. The question "what happens if this webhook goes down?" must have an answer in the design doc.

**Q5. "What is your philosophy on the internal developer platform?"**

Answer: The IDP is SRE's product. Product engineers are the customers. I evaluate an IDP the same way a product team evaluates a product: what is the time-to-first-deploy for a new service, what is the self-service rate (percentage of developer needs met without opening a ticket), and what is NPS from engineering. The failure mode of most IDPs is that they become a maintenance burden with adoption rates below 50% because SRE built what they thought engineers needed rather than what engineers actually asked for. I run quarterly developer experience surveys and treat the results as product roadmap input. The IDP roadmap goes through the same prioritization process as the product roadmap.

---

## Domain 5: DevSecOps and Compliance

**Q1. "How do you embed security into CI/CD without creating friction?"**

Answer: Shift left and automate. The principle: every security check that can run in under 30 seconds belongs in the developer's pre-commit hook. Every check that takes 2–5 minutes belongs in the CI pipeline. Every check that requires human review belongs in the CD gate. The developer experience looks like: commit triggers a 20-second local scan (gitleaks, dependency check), then a 3-minute pipeline scan (SAST with Semgrep, container image scan with Trivy), then a human security review only for infrastructure changes or new external integrations. The friction-to-value ratio: most developers never see the automated checks because they pass. The ones that fail are catching real issues. When a check fails, the error message links directly to the remediation runbook — not a generic error, a specific fix.

**Q2. "What is your approach to secrets management across a Kubernetes platform?"**

Answer: External Secrets Operator pulling from AWS Secrets Manager is my current default. The model: secrets live in Secrets Manager, versioned and audited. A Kubernetes ExternalSecret resource references the secret path. The External Secrets Operator syncs the value into a Kubernetes Secret on a 1-minute poll or event-triggered. The Kubernetes Secret is never stored in Git — only the ExternalSecret reference is. This model means: rotation happens in Secrets Manager and propagates to all pods within minutes. Access control is IAM policies on the Secrets Manager paths, audited via CloudTrail. The alternative — Vault with a Vault Agent sidecar — is more powerful for dynamic secrets but adds operational complexity. I choose Secrets Manager for AWS-native deployments and Vault when I need dynamic database credentials or multi-cloud secrets.

**Q3. "How do you manage compliance evidence collection for SOC2 in an automated platform?"**

Answer: Compliance-as-code. Every control that can be automated, should be. I use a combination of AWS Config rules (continuous compliance monitoring against a control set), OPA policies in Kubernetes (for container and RBAC compliance), and a compliance pipeline that generates evidence artifacts — screenshots, logs, exports — on a scheduled basis and archives them to S3 with immutable retention. The evidence package for the SOC2 auditor is generated automatically 30 days before the audit window. The manual controls — access reviews, employee training records — are tracked in a compliance tracker with automated reminders. This model reduces audit prep from 2 weeks of engineering time to 2 days of review and exception handling.

**Q4. "What is your SBOM strategy?"**

Answer: Software Bill of Materials is the inventory of every component in your software supply chain. My strategy: generate an SBOM at container build time using Syft or Trivy, store it in the artifact registry alongside the image, and scan it against the NVD vulnerability database on every deploy and on a daily scheduled scan. Any critical or high CVE in a production image triggers a P2 alert to the owning team with a 72-hour SLA to patch or accept-risk. The SBOM is also a compliance artifact — SOC2 and increasingly NIST frameworks require it. I store SBOMs in an immutable S3 bucket for 3 years. The Director conversation: an SBOM strategy is also a vendor management conversation. When you can show a supplier that their component has a critical CVE and you tracked it to your production image, you have leverage in SLA negotiations.

**Q5. "How do you think about supply chain security for container images?"**

Answer: Four layers. One, base image provenance: all base images come from a curated internal registry that pins to verified digests, not tags. Tags are mutable — digests are not. Two, build-time signing: every image built in CI is signed with Cosign using a Sigstore workflow. The admission webhook verifies the signature before allowing the image to run in production. An unsigned image cannot run. Three, runtime scanning: a Falco or similar runtime agent watches for anomalous behavior in running containers — unexpected network connections, privilege escalation attempts, unexpected file writes. Four, dependency pinning: all package managers use lock files (requirements.txt pinned, package-lock.json, go.sum). The pipeline fails if a lock file is missing or unpinned. Together these four layers mean: the image that runs in production is the image that was built, signed, and scanned in CI.

---

## Domain 6: Observability and Monitoring

**Q1. "What is the difference between monitoring and observability, and why does it matter for a Director?"**

Answer: Monitoring tells you when something is wrong. Observability tells you why. Monitoring is a predefined set of checks against known failure modes. Observability is the property of a system that lets you ask questions you did not know you needed to ask before the incident. For a Director, the distinction matters because: monitoring is a cost center — you buy tools and maintain dashboards. Observability is a capability investment — you instrument systems so that the next unknown failure can be diagnosed in minutes instead of hours. I fund both, but I measure observability by MTTD for novel failure modes, not by dashboard count.

**Q2. "How do you scale observability infrastructure without runaway cost?"**

Answer: Three cost controls. One, tiered retention: high-resolution metrics (1-minute intervals) retained for 7 days, then downsampled to 5-minute intervals for 30 days, then to hourly for 1 year. Log retention: full-resolution for 3 days (covers most incident investigations), then sampled at 10% for 30 days, then cold storage. Two, tail-based sampling for traces: capture 100% of error traces, 10% of slow traces, 1% of normal traces. You keep all the signal that matters and reduce storage cost by 80%. Three, cost attribution: every team sees their observability spend in the platform cost dashboard. Engineers who create 10,000-metric-cardinality Prometheus labels get a Slack message from the cost alert. Attribution drives behavior change faster than policy.

**Q3. "How do you instrument a legacy Java application that cannot be modified?"**

Answer: Three approaches depending on access level. One, JVM agent instrumentation: attach the OpenTelemetry Java agent at startup via the JAVA_OPTS — `javaagent:/path/to/opentelemetry-javaagent.jar`. Zero code changes. Gets you metrics, traces, and log correlation for supported frameworks automatically. Two, sidecar log parsing: deploy Fluentbit as a sidecar container that reads the application log file, parses it with a structured regex or JSON rule, and forwards to your log aggregator. Three, external probes: if the application exposes any HTTP endpoint, you can get availability and latency data from external synthetic probes without touching the code. For a legacy monolith I cannot modify, this is the fastest path to basic observability in 2 hours.

**Q4. "How do you prevent dashboard sprawl from making observability useless?"**

Answer: Dashboard governance. Every dashboard in the observability platform has an owner and a purpose tag. I run a quarterly dashboard audit: any dashboard not viewed in the last 30 days is archived. Any dashboard without a defined purpose is tagged for review. The golden set: I maintain a canonical set of 12 dashboards — executive SLO view, service health per domain, infrastructure capacity, on-call triage board — and these are the defaults. Teams can create additional dashboards but the canonical set is sacrosanct. I have seen organizations with 2,000 Grafana dashboards where engineers could not find the right one during an incident. That is not an observability problem — it is a governance problem.

**Q5. "What is your OpenTelemetry adoption strategy?"**

Answer: OTel is the right long-term bet because it is vendor-neutral and the ecosystem is maturing rapidly. My adoption strategy: greenfield services adopt OTel SDK from day one — it is in the service template. Existing services instrument in priority order: services on the critical path first (revenue-impacting, high-toil). I target 80% of critical services instrumented within 6 months of starting the OTel program. I do not require 100% before starting — I start collecting signal and let the value demonstrate itself. The migration path from proprietary agents (DataDog, New Relic agents) to OTel is parallel-run: instrument with both for 30 days, validate that OTel data matches the proprietary agent, then cut over. Do not do a big bang cutover from a vendor agent to OTel — you will lose a monitoring gap and have an incident.

---

## Domain 7: Hiring and Talent Development

**Q1. "What is your interviewing process for a senior SRE?"**

Answer: Four rounds. One, a 30-minute recruiter/values screen — I want to know if the candidate can communicate ambiguity clearly and if they have genuine curiosity about failure modes. Two, a technical screen with an on-call simulation: I give the candidate a fake alert and a set of fake logs and ask them to walk me through their diagnosis. I am evaluating: do they form hypotheses or do they randomly check things? Do they ask clarifying questions? Three, a system design round: design a monitoring system for a distributed application. I am evaluating whether they think about failure modes, data retention, and cost — not just the happy path architecture. Four, a leadership/collaboration round with two team members — I want to know if they work well with people who are not SREs, because SRE is a service function. A senior SRE who cannot explain their work to a product engineer is a liability.

**Q2. "How do you identify and develop your next SRE manager from your IC team?"**

Answer: I look for three signals: comfort with ambiguity (managers deal with human problems that have no right answer), communication under pressure (visible in incident command), and genuine interest in other people's growth (not just their own). When I identify a potential manager, I give them a low-stakes leadership opportunity: owning the on-call rotation scheduling, leading the new hire orientation, facilitating the weekly postmortem. I give them a managing-as-IC project — a cross-team initiative they lead without formal authority. If they can drive that to completion with no direct reports, they are ready for a team. I do not promote to manager as a reward for IC excellence. The skills are different. I have seen excellent ICs fail as managers because no one told them that.

**Q3. "How do you handle a high-performer who is burning out?"**

Answer: I catch it before it becomes a resignation conversation. The signals I watch for: increased abruptness in Slack, late responses on low-urgency items, reduced quality of postmortem contributions. When I see the pattern, I have a direct conversation: "I notice you seem stretched. Tell me what is taking the most energy." Usually it is one of three things: on-call load (fix: adjust the rotation), a project that has no end date (fix: timebox it and define done), or a relationship friction with a peer or product team (fix: have the harder conversation with the other party). The worst response to burnout signals is more appreciation and less structural change. People do not burn out because they feel unappreciated. They burn out because the system is consuming more than it returns.

**Q4. "What is your philosophy on remote vs. in-office for SRE teams?"**

Answer: SRE teams function well remote because the work is fundamentally asynchronous between incidents — runbook writing, dashboard building, architecture review. Incidents are synchronous but modern tooling (Slack huddles, Zoom, shared terminals) handles that well. My requirement: on-call engineers must be able to respond within 5 minutes and have a reliable connection. Beyond that, I am outcome-oriented, not location-oriented. The benefit of remote is talent access — I can hire the best SRE in Seattle or Austin rather than the best available SRE who will commute. The risk of remote is culture degradation — postmortem culture, mentorship, informal knowledge transfer all require intentional effort when remote. I invest in quarterly in-person gatherings for the whole team: two days of working sessions, one day of social. That rhythm maintains the human layer that remote erodes.

**Q5. "How do you build psychological safety in a team that is accountable for reliability?"**

Answer: The seeming contradiction is: we hold the team accountable for reliability AND we say every mistake is blameless. How do you hold both? The answer is: accountability is for commitments, not for outcomes. An SRE who commits to running a chaos exercise and does not do it is accountable. An SRE who runs the chaos exercise and finds an unexpected failure mode is celebrated. The failure mode was always there — they just found it. I model this from the top by sharing my own mistakes openly in team meetings. I wrote a public postmortem for a monitoring gap I personally introduced three years ago. I put it on the team wiki. New engineers read it during onboarding. It signals: we investigate, we learn, we share, we do not hide. Psychological safety is not about being nice — it is about making truth-telling safe.

---

## Domain 8: Strategy and Business Translation

**Q1. "How do you build a reliability roadmap that aligns with business strategy?"**

Answer: Start with the business OKRs for the year and ask: what reliability risks threaten each OKR? If the company OKR is "expand to three new markets," the reliability risk is: does the platform scale to 3x the current load? Does compliance posture cover the new regulatory environments? The reliability roadmap is a risk register with investment priorities, not a technology wishlist. I present it to the VP of Engineering and the CTO in terms of: here are the four risks to the business's annual goals, here are the investments that mitigate them, here is the cost of not investing in each one. That framing gets budget approval faster than "we need to upgrade our observability stack."

**Q2. "How do you communicate the value of SRE to a CEO who does not understand it?"**

Answer: One slide. Top half: cost of last 3 incidents in engineering hours and revenue impact. Bottom half: what we invested to prevent the next one and the expected incident rate reduction. The CEO cares about two things: is the business at risk and is the investment rational. A CEO who sees that last quarter's incidents cost $400K in engineering time and customer churn, and that a $150K investment in chaos engineering and runbook automation could reduce incident frequency by 40%, understands SRE. You do not need to explain Kubernetes. You need to explain insurance math.

**Q3. "What is your approach to vendor management for reliability tooling?"**

Answer: I treat reliability tool vendors as strategic partners, not commodity suppliers. My criteria: can the vendor's roadmap grow with our scale, do they have a strong open standards commitment (OTel, OpenMetrics), and what is our lock-in exposure if we need to switch? I review contracts annually with a focus on data portability — can I export my data if I switch? I benchmark the three major tools in each category every two years: not to switch, but to validate that we are on the best product and to maintain negotiating leverage. The procurement decision I am most careful about is the one that becomes invisible — the tool that works so well no one ever questions it for five years. Those are the tools with the highest switching cost and the most leverage.

**Q4. "How do you make the SRE function visible to the business during a period of stability?"**

Answer: The stability paradox: SRE is most valuable when nothing happens, but that is when it is least visible. My solution is proactive communication. I publish a monthly reliability brief to the VP of Engineering and the product leadership: SLO health, error budget balance, incident trend, and — critically — what the team prevented. "This month we identified a memory leak in the payments service during chaos testing, patched before production, estimated impact: $200K in prevented downtime." Incidents that did not happen are invisible unless you tell the story. I make the prevented-incident stories as prominent as the incident postmortems.

**Q5. "How do you approach the build-vs-buy decision for platform tooling?"**

Answer: My framework has four questions. One, is this in our value chain? If the tool is directly related to our core technical differentiation, consider building. If it is commodity infrastructure, buy. Two, what is the total cost of ownership? Build cost includes not just development but ongoing maintenance, documentation, and the opportunity cost of not shipping product work. Three, what is the vendor market maturity? If there are three strong vendors with a proven track record, buying is almost always right. If the vendor market is immature or dominated by a single player with high lock-in risk, building becomes more attractive. Four, what is the adoption risk? A great internal tool with 40% adoption is worse than a mediocre commercial tool with 90% adoption. I have a graveyard of excellent internal tools that died because no one had time to maintain them.

---

# PART 3: TIMED DRILL SYSTEM

Ten drills, 3 minutes each. Set a timer. Speak aloud. Record yourself if possible.

**Scoring Rubric — PASS requires all four:**
- P: stated the Problem clearly (what was wrong, what was the risk)
- A: described your Approach (what you decided and why)
- T: gave a T-Mobile anchor (real example or direct parallel)
- TR: articulated a Tradeoff (what you gave up or what could have gone differently)

A missing element is a FAIL. Review the rubric after each drill before the next one.

---

**Drill 1: "Tell me about a time you reduced operational toil."**

Timer: 3 minutes. Hit all four elements. T-Mobile anchor: notification platform runbook automation. Common fail: spending 2 minutes on the technical solution and never stating the business impact.

Model skeleton: "Problem: our on-call team was spending 35% of their capacity on a diagnostic task that repeated in the same form three times a week. Approach: I had one senior SRE build a Python script that automated the first six steps of the runbook — it ran in 90 seconds and cut that task from 20 minutes to 2 minutes. Anchor: T-Mobile notification platform, RabbitMQ queue depth incidents, 2023. Tradeoff: automated runbooks can mask underlying problems — the script runs, it looks clean, but it does not ask whether the recurring incident is a sign of something we should fix permanently. We added a recurrence counter to the script — five or more executions in 30 days triggered a separate engineering review."

---

**Drill 2: "How would you structure SRE for a company that is growing from 50 engineers to 200 in 18 months?"**

Timer: 3 minutes. Common fail: describing the end state without describing the transition plan or the risks during the transition.

Model skeleton: "Problem: at 50 engineers, informal SRE works because everyone knows each other. At 200, you have unknown failure domains and no shared standards. Approach: I would build the platform function first — 3 engineers, shared tooling and on-call standards — before expanding headcount. Then add domain-aligned SREs as each product domain grows past 20 engineers. Anchor: T-Mobile — we went from 8 to 15 SREs over 24 months; the platform function was the forcing factor that made the growth manageable. Tradeoff: front-loading platform investment means slower incident response coverage in the first 6 months. You accept that risk in exchange for a stable foundation."

---

**Drill 3: "How do you set the hiring bar for SRE when competing with FAANG salaries?"**

Timer: 3 minutes. State the problem clearly before offering a solution.

Model skeleton: "Problem: FAANG can outbid on cash and equity, particularly for senior SREs. My approach is not to compete on compensation alone but on mission and scope. I hire people who want to build something from scratch more than they want to maximize salary. I look for people early in their management journey or people burned out by Big Tech scale who want high leverage. Anchor: T-Mobile offers a mission — zero Sev1 incidents on a platform processing 25M messages per day. That is tangible scope. Tradeoff: I may lose to offers with 20% higher compensation. The candidates I do get are often more execution-focused and less burnout-prone than hyperscale refugees."

---

**Drill 4: "Explain error budget burn rate to a VP of Product who has never heard the term."**

Timer: 3 minutes. Common fail: using SRE jargon. Must be entirely jargon-free.

Model skeleton: "Problem: how do we decide when to slow down feature development to fix reliability? Approach: we give each service a quarterly 'failure allowance' — the amount of downtime or errors the product can experience before users are significantly impacted. We track how fast we are consuming that allowance. If we are burning through it three times faster than the quarterly budget in the first week, that is the signal to pause and stabilize. Anchor: T-Mobile notification platform — we track this weekly and have used it twice to push back on a release that would have consumed our entire monthly budget in one deploy. Tradeoff: some teams see it as a ceiling that limits feature work; the reframe is that it is a budget — you can spend it on risk if you choose to, but you own the tradeoff consciously."

---

**Drill 5: "A major incident happened on your watch. The CEO is asking for a 5-minute briefing. What do you say?"**

Timer: 3 minutes. Common fail: technical depth. The CEO briefing has zero technical jargon.

Model skeleton: "Current status: the issue that caused the incident has been identified and resolved as of [time]. Customer impact: [X] users experienced [Y] for [Z] duration. Revenue impact: we estimate [N] based on [transaction volume]. What we are doing now: we have a team of four reviewing the root cause and we will have a written summary by [time]. What we are doing to prevent recurrence: we have identified two process gaps that we are closing this week. I will send you a written summary within 4 hours and schedule a 30-minute review with you and the VP of Product tomorrow."

---

**Drill 6: "How do you manage an SRE team across three time zones?"**

Timer: 3 minutes. Focus: on-call coverage, communication norms, team cohesion.

Model skeleton: "Problem: a distributed team risks fragmentation, async communication challenges, and on-call load imbalance across zones. Approach: I establish clear on-call handoff protocols — Americas region picks up from EMEA at 6am local, EMEA hands to APAC at their morning standup. All critical decisions wait for a synchronous huddle — I schedule weekly all-hands at a rotating time that is 3pm somewhere. Anchor: T-Mobile has SREs in multiple US time zones; we run the standup at 10am Pacific, which is 12pm Central. Everyone owns the inconvenience equally by rotating the meeting time quarterly. Tradeoff: no single time is painless; async documentation becomes mandatory rather than nice-to-have because not everyone can attend every call."

---

**Drill 7: "What is the most important Kubernetes concept a Director should understand even if they are not operating the cluster themselves?"**

Timer: 3 minutes. Common fail: going IC-level deep. Stay at the blast radius and governance level.

Model skeleton: "Problem: Directors make decisions that affect how Kubernetes is governed — who has access, how services are isolated, how upgrades happen. If I do not understand the risk surface, I cannot govern it. Approach: the concept I consider most important is namespace-level blast radius — in Kubernetes, a namespace is the primary isolation boundary. Understanding what can cross namespace boundaries (network by default, secrets with the right RBAC) and what cannot is the minimum viable knowledge for a Director making access control decisions. Anchor: at T-Mobile, a misconfigured network policy allowed a staging pod to communicate with a production RabbitMQ cluster. The namespace was the correct boundary — the network policy had a gap. I have since required network policy reviews as part of namespace provisioning. Tradeoff: tight network policies slow down development because engineers need to explicitly allow traffic. We accept that cost for production namespaces and allow open-by-default in development namespaces."

---

**Drill 8: "How do you handle a situation where your SRE team disagrees with a decision made by the VP of Engineering?"**

Timer: 3 minutes. Focus: disagreement process, escalation without burning relationships.

Model skeleton: "Problem: organizational disagreement can become adversarial if not managed well. Approach: I ensure the SRE team has a clear voice before the decision is made, not after. If SRE has a strong objection to a planned deployment or architecture decision, I schedule a 30-minute review with the VP of Engineering and the relevant product lead before the decision is final. I come with data, not opinions. Anchor: T-Mobile — we objected to a scheduled deployment of new RabbitMQ topology the week before a major holiday. Our data showed it would have consumed our entire error budget if something went wrong. We proposed a two-week delay. The VP of Engineering deferred the deployment. Tradeoff: I do not always win these reviews. When the VP decides to proceed against our recommendation, I ensure the team understands the business rationale and we prepare accordingly with extra on-call coverage."

---

**Drill 9: "What is your approach to chaos engineering at a company that has never done it?"**

Timer: 3 minutes. Common fail: starting with tooling instead of culture and process.

Model skeleton: "Problem: you cannot build resilience without testing your failure assumptions. But chaos engineering at a company that has never done it will create incidents if you start with production. Approach: I start with Game Days, not automated chaos. A Game Day is a scheduled, controlled failure injection with full team awareness, in a non-production environment, with a documented hypothesis: 'we believe the service will recover within 3 minutes if we kill one instance.' We run the experiment, observe what actually happens, and write a postmortem-style finding. We run Game Days monthly for 90 days before introducing any automation. Anchor: T-Mobile — we ran six Game Days on the notification platform before we were confident enough in our runbooks to consider automated chaos. We found three runbook gaps that would have been P1 incidents in production. Tradeoff: Game Days require 2–4 hours of engineering time and need a production-like environment that is expensive to maintain. The alternative — no testing — is more expensive when the real failure occurs."

---

**Drill 10: "What do you do in the first 30 days as a VP SRE at a new company?"**

Timer: 3 minutes. Common fail: jumping to solutions before completing listening and assessment.

Model skeleton: "Problem: the highest-risk thing I can do in the first 30 days is change things I do not yet understand. Approach: I have a structured 30-day listening plan. Week one: 1:1s with every direct report and every peer leader — VPs of Engineering, Product, Security. I ask the same four questions: what is working, what is not working, what do you wish SRE owned that it does not, and what does SRE do that adds friction? Week two: I shadow on-call for 3 shifts — not to run the incident, but to observe the response process and tool chain. Week three: I review the last 12 postmortems and last quarter's reliability metrics — MTTD, MTTR, error budget balance. Week four: I draft a 90-day plan and share it with my team for input before presenting it to the VP of Engineering. Anchor: this is exactly what I did when I took over the notification platform team at T-Mobile — the listening tour before action is how I built trust fast. Tradeoff: 30 days of listening looks like inaction to some stakeholders. I communicate this explicitly: 'I am gathering data this month. You will see my first proposals in week 5.' Setting the expectation prevents the pressure to act before you have enough information."

---

# PART 4: LEADERSHIP PHILOSOPHY STATEMENT

**Prompt:** "What is your philosophy on SRE?"

**Draft — 2 minutes — in Vishweshwar's voice:**

"My philosophy comes from 21 years of watching systems fail in ways no one predicted — and watching people respond.

What I have learned is this: reliability is not a technical problem. It is a trust problem. The product team trusts that their service will run. The customer trusts that the platform will deliver. The business trusts that the engineering org is managing risk. SRE exists to honor those trust commitments — and to be honest when the trust is at risk.

In practice, that means three things for me. First, make failure visible before it reaches the customer. That is the whole point of observability, SLOs, and chaos testing — to find the failure mode on your terms, not on the customer's terms. Second, make reliability the path of least resistance for product engineers. If my team is the reliability police — the people who say no, slow down, wait — we have failed. My team should be the people who make it easy to build reliably. The golden path, the guardrails, the platform. Third, own the truth in the room. When a service is at risk of burning its error budget, I say it to the VP of Engineering before it becomes an incident. When an architecture decision creates a reliability debt, I put a number on it and put it in the room where the decision is being made.

The metric I care about most is not uptime — it is MTTD. How fast do we know something is wrong? If we know fast, we recover fast. If we know fast and repeatedly, our customers never find out. That is the reliability standard I hold myself to and the one I build teams to achieve."

---

**Alternative version — 30 seconds:**

"My philosophy is: reliability is a trust contract with the people who depend on your systems. My job is to maintain that contract under all conditions — including conditions I have not thought of yet. I do that by building teams that find failure before customers do, and cultures where the truth about risk is always spoken, even when it is uncomfortable."

---

# PART 5: THE 30-SECOND PITCH — THREE VARIANTS

---

## Variant 1: Startup — Builder, Zero-to-One, AI-Native

"I am an SRE Director with 21 years of operational experience and a track record of building reliability from scratch. At T-Mobile, I took a notification platform from reactive firefighting to zero Sev1 in 36 months — 25 million messages a day, 15 people, no major incidents. What draws me to your stage is the opportunity to set the defaults that the company scales on. I bring infrastructure, tooling, AI-augmented operations, and — most importantly — the judgment to know what to build and what to buy. I am looking to be the first director-level SRE hire and make reliability a competitive advantage from day one."

---

## Variant 2: Enterprise — Scale, Governance, Zero Sev1

"I am an SRE Director at T-Mobile leading a 15-person team on a platform that processes 25 million messages per day on Kubernetes on AWS. Over 36 months, my team has maintained zero Sev1 incidents while delivering continuous feature releases — including a full observability stack migration and a GitOps rollout. My strength is translating reliability risk into business language and building the governance models that hold as organizations scale from 100 to 1,000 engineers. At the VP level, I bring both the technical credibility to earn my team's respect and the executive communication skills to earn the business's trust."

---

## Variant 3: Internal Promotion — Continuity, Institutional Knowledge, Step-Up

"Over five years at T-Mobile, I have built the notification platform's reliability function from the ground up — SLO framework, blameless postmortem culture, AI-assisted anomaly detection, zero Sev1 in 36 months. I have managed 15 people, coached three engineers into senior roles, and influenced reliability standards across two adjacent platform teams. I am ready to step into a Director role that lets me apply this operating model at the division level. The case for internal promotion: I know the systems, the people, and the culture. The ramp from VP-with-context is faster than VP-from-outside, and the reliability risk during transition is lower."

---

## Comprehension Check

Before running a mock interview practice session, answer these three questions. Pass 2/3 to proceed.

**Q1.** You are in a 45-minute startup interview and the Engineering VP asks: "We have 3 embedded SREs and they are all doing different things. How would you fix this?" What is the structural answer and what is the thing you would NOT do in the first 90 days?

**Q2.** A CTO asks you: "Do you think AI will replace SREs in five years?" You have 90 seconds. What are the two categories of SRE work that AI will replace and what is the category it will not?

**Q3.** You have been asked to defend the SRE team's budget in a quarterly business review. The platform had zero major incidents last quarter. How do you make the case that the investment was worth it when nothing visibly went wrong?

---

## ANSWER KEY — Comprehension Check

**A1.** Structural answer: federated model — small central platform team for shared tooling and standards, domain-aligned SREs for product context. The thing NOT to do: reorganize in the first 90 days. The correct first move is a structured listening tour to understand why the embedded model exists and where the real pain is. Big-bang reorganization during a period of high organizational change is a reliability risk.

**A2.** AI replaces: (1) pattern-matching reactive work — log triage, alert correlation, runbook execution for known failure modes; (2) toil automation — routine operational tasks with bounded state spaces. AI does not replace: organizational judgment — the call that balances technical risk against business timelines, the influence conversation with a VP of Product, the culture that makes blameless postmortems work. That judgment requires contextual authority and trust built over time.

**A3.** The prevented-incident story. Calculate: what did last quarter's reliability investment (headcount, tooling, game days) cost? Then identify 2–3 failure modes that were caught before production — via chaos testing, synthetic probes, runbook automation. Estimate what those failures would have cost in incident time and customer impact. Present the delta as the ROI. Zero incidents is not evidence that nothing was at risk — it is evidence that the risk management worked. The Director job is to make that visible.

---

## Interview Questions — 5 Staff/Principal Level

1. "How do you build an SRE function that is operationally excellent AND viewed as an accelerant by product engineering, not a gatekeeper?"

2. "Describe your framework for deciding how much reliability investment is enough for a given service. How do you avoid over-engineering and under-engineering?"

3. "You have inherited an SRE team with strong technical skills but poor product partner relationships. What is your 90-day plan?"

4. "How do you govern AI adoption within an SRE team — what tasks do you automate, what do you keep human, and what is the risk management model?"

5. "What is the reliability conversation you have not been able to win yet — and what would it take to win it?"

---

## STAR Anchor — T-Mobile Framing Per Question

| Interview Question | T-Mobile Story Anchor |
|---|---|
| Reducing toil | RabbitMQ runbook automation — 35% to 8% reactive time |
| Setting SLOs from scratch | Notification platform — first SLO framework, conservative start, calibrated in 60 days |
| Conflict with product team | Velocity vs. reliability — joint error budget scorecard introduced |
| Building blameless culture | Postmortem for monitoring gap I personally introduced — published publicly |
| Incident communication | P1 bridge call structure — MTTD reduction from 8 min to 90 sec |
| Scaling team | 8 to 15 SREs in 24 months — platform-first sequencing |
| Letting someone go | Performance improvement plan, 90 days, team credibility outcome |
| AI strategy | Anomaly detection Python + Splunk MLTK — AI in the loop, human final decision |

---

## Tradeoffs and Failure Modes — Top 3

**Tradeoff 1: Technical credibility vs. strategic altitude**

As you move toward Director/VP, the risk is that staying technically deep consumes time that should go to strategy, talent, and business alignment. The tradeoff is deliberate: I stay sharp enough to earn technical respect (quarterly on-call rotation, one hands-on project per quarter) but I do not solve technical problems that my team should own. The failure mode is a Director who is the best IC on the team — that person is blocking their team's growth.

**Tradeoff 2: Speed of change vs. stability during transition**

Every organizational change — new team structure, new tool, new process — introduces a transient reliability risk. The tradeoff is: how much change can the team absorb while maintaining reliability commitments? My heuristic: never run two major organizational changes simultaneously. If you are reorganizing the team, do not also migrate the observability stack. Sequence, do not parallelize, change.

**Tradeoff 3: Centralization vs. autonomy in platform design**

A central SRE platform team can enforce standards so strictly that product teams route around it — shadow IT for reliability tooling. Too much autonomy and you have 20 different monitoring stacks with no shared signal. The correct calibration: mandate the interface (OTel SDK, structured logs, Prometheus metrics endpoint) and let teams choose their tooling within those interfaces. Standardize the contract, not the implementation.
