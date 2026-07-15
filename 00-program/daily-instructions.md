# Daily Instructions — SRE/DevSecOps Interview Prep Program

> **Start every session at [`ROADMAP.md`](../ROADMAP.md) — it has the complete phase map and links to every topic.**
> **Open your current week file in [`1-phase-foundations/1.11-weekly-tracker/`](../1-phase-foundations/1.11-weekly-tracker/) — that is your weekly checklist.**

---

## The Non-Negotiable Rules (read every session)

- **Open `00-program/session-start-prompt.md` first — paste it to Claude before asking anything else.**
- **Do not advance to the next week until you pass 2/3 comprehension check AND lab EXPECTED_OUTPUT match.**
- **Every lab step must produce the expected output before you type the next command.**
- **Run `terraform destroy` or `eksctl delete cluster` at the end of every AWS session — no exceptions.**
- **If stuck more than 20 minutes, follow the Stuck Protocol — do not thrash or skip ahead.**
- **Log confidence score in `00-program/progress-log.md` at the end of every session, even if it did not change.**
- **Job search actions run in parallel from Week 1 — one low-effort action per week minimum until Week 6 mandatory applications begin.**

---

## Daily Routine Card

| Step | Action | Time | Done? |
|------|--------|------|-------|
| 1 | Open `session-start-prompt.md`, fill in today's week/topic/goal | 2 min | [ ] |
| 2 | Paste the filled prompt to Claude — wait for orientation response | 1 min | [ ] |
| 3 | Run the session playbook for today (weekday or weekend) | Per playbook | [ ] |
| 4 | At close: log confidence score + one sentence of what you learned in `00-program/progress-log.md` | 3 min | [ ] |
| 5 | Run teardown if any AWS resources were provisioned | 2 min | [ ] |

**Total overhead: 8 minutes. Everything else is learning.**

---

## Weekday Session Playbook (2–3 hours)

1. **Setup (5 min)**
   - Open WSL2 terminal. Confirm AWS CLI works: `aws sts get-caller-identity`
   - Open `session-start-prompt.md`. Fill in: current week, last completed topic, today's goal, confidence score for the domain.
   - Paste to Claude.

2. **READ Phase (30 min)**
   - Ask Claude for the concept guide on today's topic.
   - Read the analogy first, then the vocabulary translation table, then the 2-minute version.
   - Do not copy-paste commands yet. Read the full explanation before opening a terminal.

3. **Dialogue Phase (20 min)**
   - Ask Claude: "Give me a real-world example of this from a notification platform or middleware context."
   - Ask one follow-up: "What breaks in production if I get this wrong?"
   - Note the answer in your own words before continuing.

4. **Vocabulary Lock (10 min)**
   - Without looking, write down the 3–5 key terms from the topic and their one-sentence definitions.
   - Check against Claude. Fix any gaps before the gate.

5. **Comprehension Gate — 3 Questions (15 min)**
   - Ask Claude: "Give me the 3-question comprehension check for [topic]."
   - Answer all 3 in writing (typed or handwritten).
   - Pass = 2/3 correct. Fail = re-read the concept guide once more, then retake. Do NOT proceed to lab on a fail.

6. **LAB Phase in WSL2 (60–80 min)**
   - Ask Claude: "Give me the lab for [topic] with EXPECTED_OUTPUT at every major step."
   - Run each command. Match output before proceeding.
   - If output does not match: follow Stuck Protocol before next step.
   - Screenshot or copy terminal output for the final validation step.

7. **Tradeoffs Check (10 min)**
   - Ask Claude: "What are the top 3 tradeoffs or failure modes for [topic]?"
   - Record them. These are direct interview ammunition.

8. **LOG Phase (5 min)**
   - Open `00-program/progress-log.md`.
   - Update: date, topic, confidence score (1–5), lab completed (yes/no), one sentence on what you can now explain.
   - If confidence did not increase after the session, note why — that is a red flag (see Red Flags table).

**Total: 2 hrs 35 min maximum. Trim READ or Dialogue if time is short — never trim the gate or the log.**

---

## Weekend Session Playbook (5 hours)

1. **Setup (10 min)**
   - Open WSL2. Confirm AWS CLI, kubectl, terraform all respond.
   - Open `session-start-prompt.md`. Fill in weekend context: which lab you are running, which week, goal for the day.
   - Paste to Claude.

2. **Concept Refresh (20 min)**
   - Ask for the 5-minute version of the week's primary concept.
   - Pay attention to the Staff/Principal lens: how does a team lead govern this vs. an IC who implements it?
   - Note one thing you want to be able to explain in a 3-minute mock answer.

3. **Module 1 — Setup Lab (60 min)**
   - Ask Claude: "Give me Module 1 of the [topic] weekend lab — environment setup and baseline resources."
   - Follow step by step. Every step must produce EXPECTED_OUTPUT before continuing.
   - At end of Module 1: state out loud or in writing what you just built and why it matters.

4. **Module 2 — Core Lab (60 min)**
   - Ask Claude: "Give me Module 2 — the core hands-on work for [topic]."
   - This is the highest-density section. Slow down if needed. Do not rush past error messages.
   - If a command fails: follow Stuck Protocol before trying a variation.

5. **Module 3 — Validation + Break/Fix (60 min)**
   - Ask Claude: "Give me Module 3 — validation steps and one intentional break/fix scenario."
   - Run validation. Match EXPECTED_OUTPUT.
   - Complete the break/fix scenario: introduce the failure, observe it, recover it.
   - This is the section that maps directly to "debug this in prod" interview questions.

6. **Timed Drill (15 min)**
   - Set a 3-minute timer.
   - Ask Claude: "Give me one senior SRE interview question on [topic]."
   - Answer out loud without notes. Time yourself.
   - Then ask Claude to evaluate your answer and identify one gap.

7. **Interview Question Practice (15 min)**
   - Ask Claude: "Frame my experience with [today's topic] using the STAR method anchored to T-Mobile."
   - Review the draft. Edit one sentence to make it more specific to your team or platform.

8. **Resource Teardown (10 min)**
   - Run `terraform destroy` or `eksctl delete cluster` as appropriate.
   - Confirm in AWS Console that no unexpected resources remain.
   - Check estimated cost in AWS Cost Explorer if you ran anything beyond free tier.

9. **LOG Phase (10 min)**
   - Update `00-program/progress-log.md`: date, lab name, modules completed (1/2/3), EXPECTED_OUTPUT matched (yes/no per module), confidence score before and after, timed drill pass/fail.
   - One sentence: what can you now explain that you could not explain before this session?

**Total: 5 hours. Do not skip teardown or log. They are part of the session.**

---

## Sunday Ritual (30 minutes)

Run this every Sunday evening before the new week begins.

- [ ] **Step 1 — Confidence Calibration (10 min)**
  - Open `00-program/progress-log.md`. Review confidence scores for each topic covered this week.
  - For every score that did not increase: identify the specific gap (concept? lab? vocabulary?). Write one sentence.
  - Scores required to advance: CRITICAL gaps at 4+, MODERATE gaps at 3+ (see Progress Gates table).

- [ ] **Step 2 — Timed Drill (10 min)**
  - Pick one topic from the current week.
  - Ask Claude: "Give me a senior SRE interview question on [topic] — I have 3 minutes."
  - Set timer. Answer out loud. Record pass/fail in `00-program/progress-log.md`.
  - If you fail the drill for a topic you rated yourself 3+: lower the confidence score by 1. This is a decay check.

- [ ] **Step 3 — Job Search Tracker Update (5 min)**
  - Open `00-program/progress-log.md` H1B tracker section.
  - Log any applications submitted, responses received, or follow-ups needed.
  - Weeks 1–5: minimum 1 low-effort action (LinkedIn connect, company research, JD saved).
  - Weeks 6–10: minimum 1 application submitted or 1 interview scheduled per week.
  - H1B disclosure rule: after tech screen, before offer — mark this in your tracker for each active pipeline.

- [ ] **Step 4 — Week-Ahead Preview (5 min)**
  - Open the Week-by-Week Focus Table (Section below).
  - Read the next week's domain, primary lab, and prerequisite.
  - Confirm you meet the prerequisite. If not: schedule a catch-up session on Monday, not a skip.
  - Identify one thing to ask Claude about at the start of next week's first session.

---

## The Stuck Protocol

Use this decision tree any time you are blocked. Do not improvise. Do not skip.

```
Are you stuck on a LAB STEP (command fails, output does not match)?
  |
  +-- Stuck < 5 min?
  |     --> Read the error message top to bottom. Google the exact error string. Try once.
  |
  +-- Stuck 5–20 min?
  |     --> Ask Claude: "I ran [exact command]. I expected [EXPECTED_OUTPUT]. I got [actual output]. What is wrong?"
  |     --> Apply the fix. If it works: continue. Log the error and fix in progress-log.md.
  |
  +-- Stuck > 20 min, same error?
  |     --> STOP. Do not try random variations.
  |     --> Ask Claude: "I have been stuck > 20 min on [step]. Walk me through diagnosing this from scratch."
  |     --> If still unresolved after one full Claude diagnostic pass: defer the step, mark it in progress-log.md, continue the rest of the lab.
  |
  +-- Output is wrong but no error message?
        --> Ask Claude: "My command ran without error but produced [actual output] instead of [expected output]. What does this mean?"

Are you stuck on a CONCEPT (does not make sense after 2 reads)?
  |
  +-- Ask Claude: "Explain [concept] using a RabbitMQ/TIBCO/middleware analogy. Then give me the 30-second version."
  |
  +-- Still unclear?
  |     --> Ask Claude: "What is the one thing I must understand about [concept] to answer an interview question about it?"
  |
  +-- Still unclear after that?
        --> Mark the concept as "needs revisit" in progress-log.md. Move on. Return to it in the Sunday ritual.

Is the entire WEEK'S DOMAIN unfamiliar and the lab is overwhelming?
  |
  +-- Do not skip the week. Ask Claude: "Give me the absolute minimum I need to understand about [domain] to do the lab safely."
  +-- Run only Module 1 of the lab this session. Schedule Module 2 for next session.
  +-- Use one of the two buffer weeks if you have used > 3 extra sessions in this domain.
```

---

## Claude Usage Rules

**What to paste at session start:**
Open `session-start-prompt.md` and fill in all fields before pasting. The template must include:
- Current week number and domain
- Last completed topic and confidence score
- Today's goal (one sentence)
- Session type: weekday concept / weekday lab / weekend lab / Sunday ritual

**Example of a good session-opening prompt:**
```
Week 3, Kubernetes Internals. Last session: completed RBAC concept guide, confidence 3/5.
Today's goal: Run the weekend lab for RBAC + IRSA, complete all 3 modules, match EXPECTED_OUTPUT.
Session type: Weekend lab.
Platform: WSL2 Ubuntu, kubectl + eksctl installed, AWS CLI configured as training-admin.
```

**What NOT to do:**
- Do not open a session without pasting the session-start-prompt. Claude has no memory of your last session without it.
- Do not ask Claude "what should I study today?" — you have a plan. Use it.
- Do not ask for a full week's content in one prompt. Ask for one concept guide, one lab, one question at a time.
- Do not skip the comprehension check because you feel confident. Run it anyway — confidence and correctness diverge.
- Do not ask Claude to simplify a lab step just because it looks long. Read it first.

**How to ask for different session types:**
- Concept guide: "Give me the concept guide for [topic] — include analogy, vocabulary table, 2-minute and 5-minute versions."
- Lab: "Give me the [topic] lab with EXPECTED_OUTPUT at every major step. I am running this in WSL2 Ubuntu."
- Comprehension check: "Give me the 3-question comprehension check for [topic]."
- Interview prep: "Frame my [topic] experience in STAR format anchored to my T-Mobile notification platform work."
- Tradeoffs: "What are the top 3 tradeoffs and failure modes for [topic] at Staff/Principal level?"

---

## Progress Gates — When You May Move to Next Week

| Week | Must Be Able To Do | Minimum Confidence Score |
|------|-------------------|--------------------------|
| 1 | Write a Terraform module from scratch, explain state locking, run apply + destroy on real AWS resources | 3 on Terraform core concepts |
| 2 | Define SBOM, run a SAST scan, write one OPA policy, explain supply chain attack vector in 2 min | 3 on DevSecOps supply chain |
| 3 | Explain control plane components, configure RBAC, describe admission webhook flow, set up IRSA | 3 on Kubernetes internals |
| 4 | Deploy ArgoCD, explain pull vs push GitOps, configure IRSA for a workload, explain drift detection | 3 on GitOps + AWS depth |
| 5 | Define MELT, instrument one service with OTel, write an error budget burn rate alert, explain SLO math | 3 on Observability |
| 6 | Present 3 capstone projects with architecture decisions and tradeoff explanations; have one GitHub repo live | 4 on at least 2 capstone domains |
| 7 | Pass a timed mock interview (30 min) with STAR answers on at least 3 domains; explain one tradeoff at Staff level | 4 on CRITICAL gaps; 3 on MODERATE gaps |
| 8 | Active applications submitted; LinkedIn updated; cert registration confirmed; resume variants complete | 4 on all CRITICAL domains |
| 9 | Explain LLM API integration, implement prompt caching, describe AI observability patterns | 3 on AI Engineering basics |
| 10 | Full mock interview passed; top-tier applications submitted; H1B disclosure strategy rehearsed | 4 on all domains targeted in applications |

**Hard gate rule**: If you cannot meet the minimum confidence score AND demonstrate the capability, do not advance. Use a buffer week. Using buffer weeks is expected — it is not failure.

---

## The Two Parallel Tracks

This program runs TWO tracks simultaneously every week. Neither is optional.

**Track 1 — Technical** (weekday sessions): Labs, concept guides, comprehension gates, EXPECTED_OUTPUT matching.
**Track 2 — Leadership** (mid-week evening + Sunday ritual): Frameworks, scripts, drills, Director vocabulary.

Together they build the complete Director/VP profile. Technical alone makes you a strong IC. Leadership alone makes you a capable manager. You need both to compete for Director roles.

---

## Week-by-Week Focus Table

| Week | Technical Track | Leadership Track Module | Job Search Milestone | AWS Cost |
|------|----------------|------------------------|----------------------|----------|
| 1 | Terraform — state, modules, remote backend, drift | **Module 01: Decision-Making** — DACI, reversibility, 1-pager, pre-mortem | Save 5 Director/VP JDs; H1B check on 3 Phase 1 companies | ~$0 |
| 2 | DevSecOps — SBOM, SAST, OPA, Cosign, SLSA | **Module 02: People Leadership** — rigid/timid/rogue/disengaged scripts, PIP, promotion | LinkedIn headline updated to Director framing; 1 recruiter connection | ~$0 |
| 3 | Kubernetes — control plane, RBAC, webhooks, IRSA | **Module 03: Vendor Management** — RFP, negotiation, build-vs-buy, QBR, sunset | Submit 1 Phase 1 application after vetting checklist | ~$1–3 |
| 4 | AWS — VPC, Organizations/SCPs, ArgoCD, FinOps | **Module 04: Budget and P&L** — headcount budget, CFO justification, cloud cost governance | Submit 2 more Phase 1 applications | ~$2–4 |
| 5 | Observability — OTel, MELT, SLO math, Prometheus | **Module 05: Strategy and Roadmap** — 30-60-90 plan, OKRs, saying no, quarterly planning | 3 total applications; aim for 1 recruiter screen | ~$1–3 |
| 6 | Portfolio — 3 capstone projects built and published | **Module 06: Executive Communication** — BLUF, 1-pager, incident comms, bad news delivery | First mandatory Phase 2 calibration application; capstone on LinkedIn | ~$5 |
| 7 | Interview Readiness — mock scripts, STAR drills | **Module 07: Cross-functional Influence** — product vs SRE, CISO vs SRE, peer Director scripts | 3+ applications; 1 recruiter screen completed; adjust based on feedback | ~$0 |
| 8 | Polish — certs, resume variants, LinkedIn posts | **Module 08: Building Teams** — first 3 hires, org design, onboarding, culture from scratch | 5+ applications; cert exam registered | ~$0 |
| 9 | AI Engineering — LLM, RAG, Bedrock, Azure OpenAI | **Module 09: Motivation and Culture** — 1:1 library, SBI feedback, psychological safety | AI story added to pitch and LinkedIn; continue active pipelines | ~$5–10 |
| 10 | AI Platform — agents, MCP, observability, safety | **Module 10: Stability and Risk** — risk register, change governance, Director P1 checklist | Offers expected; negotiation prep; premium processing ask rehearsed | ~$0 |

**Leadership Track files**: `1-phase-foundations/1.7-interview-readiness/leadership-competencies/` — 11 files, one per module plus master index.

---

## Leadership Track Session Structure

### Mid-Week Leadership Session (30–45 min, Tuesday or Wednesday evening)
1. Open the week's module file from `1-phase-foundations/1.7-interview-readiness/leadership-competencies/`
2. Read the Mental Model and Framework sections (15 min)
3. Run ONE drill with Claude — paste the drill prompt from the module (15 min)
4. Write 3 sentences in your own words: what you learned, how it connects to T-Mobile, how you'd say it in an interview (5 min)

### Sunday Ritual — Leadership Component (15 min of the 30-min Sunday ritual)
1. Read the "How to Talk About This in Interviews" section from the week's module
2. Say the answer out loud — time yourself at 2 minutes
3. Ask Claude: "Evaluate my answer to [this Director interview question] — what's missing?"
4. Log: can you answer it without notes? Y/N

### Before Any Director Interview
1. Identify which modules map to the role (startup → Module 8 Build Teams; enterprise → Module 6 Exec Communication)
2. Read the relevant module's "Interview Questions" section the night before
3. Run the mock drill with Claude: "Ask me 5 Director-level questions on [topic] and evaluate my answers"

---

## Progress Gates — When You May Move to Next Week

| Week | Technical Gate | Leadership Gate |
|------|---------------|-----------------|
| 1 | Write Terraform module from scratch, explain state locking | Can explain a hard decision using DACI — 2 min, no notes |
| 2 | Run SAST scan, write OPA policy, explain supply chain attack | Can describe how you'd handle a rigid team member — specific script |
| 3 | Configure RBAC, set up IRSA, explain admission webhook flow | Can run a vendor evaluation — scorecard exists, 3 criteria named |
| 4 | Deploy ArgoCD, explain GitOps pull model, run SCP | Can build a headcount budget line and justify it to a CFO |
| 5 | Write SLO YAML, calculate burn rate, instrument OTel | Can present a 30-60-90 day plan for a new Director role |
| 6 | 3 capstone projects on GitHub with Director narrative | Can deliver a 5-minute exec summary of any topic without notes |
| 7 | Pass 30-min timed mock interview, STAR answers on 3 domains | Can handle the "product vs reliability" negotiation — full script |
| 8 | Active applications; cert registered; LinkedIn updated | Can describe how you'd build an SRE team from scratch — first 3 hires |
| 9 | LLM API integrated, RAG pipeline working | Can run a 1:1 that uncovers real issues — 5 questions ready |
| 10 | Multi-agent working; AI capstone on GitHub | Can present platform risk to a CTO in 5 minutes using business language |

**Both gates must be met before advancing. Technical gate alone is not enough.**

---

## Red Flags & Corrective Actions

| Signal | Meaning | Fix |
|--------|---------|-----|
| Confidence score unchanged after 2 consecutive sessions on same topic | You are re-reading without building | Switch from READ to LAB immediately; do not add more reading |
| Failed comprehension check twice on same topic | Concept explanation is not landing | Ask Claude for the middleware/RabbitMQ analogy version; then retake |
| Lab EXPECTED_OUTPUT does not match on > 2 steps in one session | Environment drift or command error accumulation | Stop lab; ask Claude for a diagnostic pass from the last clean step |
| Timed drill answer scores lower than your logged confidence | Confidence inflation — you understand passively, not actively | Lower confidence score by 1; add one more STAR drill before advancing |
| AWS bill exceeds $10 in a single week | Resources not being destroyed after sessions | Run `aws ec2 describe-instances` and `terraform show` immediately; destroy all; set a $15 billing alert |
| Skipping the Sunday ritual 2 weeks in a row | Decay is accumulating invisibly | Block 30 min on Sunday calendar as a non-negotiable; treat it as a stand-up with yourself |
| Week gate not met but advancing anyway | Compounding gaps — downstream labs will fail | Use a buffer week; do not advance; gaps compound fastest in Weeks 3–4 (K8s internals) |
| Session starts without pasting session-start-prompt | Claude has no context; advice will be generic | Always paste before asking anything; restart the session if you forgot |
| Job search tracker empty at Week 6 | Parallel track has been neglected | Spend 30 min on Sunday ritual exclusively on job search; submit one application same day |
| Burnout signal: skipping sessions 3+ days in a row | Pace is unsustainable or motivation gap | Shorten sessions to 1 hr; run one timed drill only; do not add catch-up sessions back-to-back |

---

## Appendix

### Session Folder Template

Each week, create a folder under the relevant domain directory:

```
Training/
  terraform/
    week-01/
      concept-notes.md       # Your own words, not Claude's
      lab-output.txt         # Terminal output from lab steps
      comprehension-check.md # Your answers to the 3-question gate
      confidence-log.md      # Start score, end score, gap identified
```

Repeat this structure for every domain folder: `kubernetes/`, `devsecops/`, `observability/`, `aws/`, `platform-engineering/`.

### Critical Reminders

- **H1B rule**: Disclose H1B status after technical screen, before offer. Never as first disclosure. Negotiate premium processing (~$2,805) as part of offer terms. Track per-company status in `00-program/progress-log.md`.
- **Buffer weeks**: 2 buffer weeks exist in the 10-week plan. Using them is expected. If you reach Week 6 without using any buffer, you are ahead of plan.
- **Cert timing**: Register for exams at Week 8 — not earlier. Studying for certs and interview prepping simultaneously dilutes both.
- **Top-tier sponsors** (verified H1B history): AWS, Google, Microsoft, Meta, Databricks, Snowflake, Verizon. Variable: Netflix, Stripe, HashiCorp/IBM, Coinbase — verify per role before applying.
- **This file is the system.** Read it at the start of every week, not just once.
