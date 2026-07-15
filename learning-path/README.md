# Dev Lead to Director of Operations: The Complete Learning Path

## What This Learning Path Is

This is a self-paced, structured program that takes a software development lead with 5–10 years of experience through three operational leadership levels:

```
Dev Lead  →  Senior SRE  →  Principal SRE  →  Director of Operations
```

It is built entirely from the existing Training content library — no external courses required. The path sequences that content deliberately: concepts before frameworks, vocabulary before measurement, measurement before execution. Each phase has defined entry prerequisites and exit competency gates so you know exactly when you are ready to advance.

Estimated total commitment: **32–36 weeks of structured study**, plus the application of concepts in your actual day-to-day role. Real mastery is built at work, not in a reading queue.

---

## Who This Is For

- Software development leads (tech leads, staff engineers, engineering leads) who want to move into operational leadership
- Senior engineers with 5+ years of development experience who have realized reliability is the next frontier
- Senior SREs who have the technical depth but lack the operational management framework
- Anyone preparing for Principal SRE or Director of Engineering/Operations interviews

---

## What This Is NOT

- This is not a certification course. There are no tests, no badges, no vendor credentials.
- This is not a theory textbook. Every concept connects to something you will do at work this week.
- This is not a once-through reading list. The frameworks in Phase 2–4 are reference material you will return to during incidents, CAB meetings, and 1:1s.
- This is not a substitute for doing the work. Reading about incident command does not make you an incident commander. The path is the scaffold; your job is the construction site.

---

## The Four Phases

| Phase | Title | Duration | Entry Point |
|-------|-------|----------|-------------|
| Phase 1 | SRE Foundations | 8 weeks | Dev Lead, no SRE background |
| Phase 2 | SRE Practitioner | 12 weeks | Junior/Mid SRE with on-call experience |
| Phase 3 | Principal SRE | 12 weeks | Senior SRE, 4+ years, P1 IC experience |
| Phase 4 | Director of Operations | 16+ weeks (ongoing) | Principal SRE or Senior Manager |

**Total**: 32–36 weeks of structured study. The rest of the learning comes from applying these frameworks in your actual role.

---

## Weekly Time Commitment

- **5–8 hours per week** of structured study (reading, exercises, labs)
- The remaining learning comes from applying concepts in your role
- Phase 1 includes hands-on lab weeks — budget additional time for lab setup and teardown
- Phase 4 reading pairs directly with your management practice — much of it is done by doing your job with intention

---

## How to Use This Path

### Starting out
Read your phase file (`phase-1-*.md` through `phase-4-*.md`). Each file gives you a week-by-week reading plan, the specific files to read, and what competency you should be able to demonstrate before moving to the next phase.

### Navigating the content
Use `content-map.md` in this directory to find any piece of content by topic, phase, or audience. Every major file in the Training library is mapped there.

### When you hit a real incident
Do not pause your learning path to handle it — use it. The frameworks in Phase 2 are designed to be picked up mid-incident. If you are on-call and have not started Phase 2 yet, jump directly to:

```
2-phase-sre-practitioner/2.1-incident-management/playbook/
```

Read the playbook. Come back to the chapters after the incident.

### When you are preparing for interviews
Phase 4 runs concurrently with `job-search/`. Start the job search content as soon as you begin Phase 3 — interview preparation and framework mastery reinforce each other.

---

## Navigation Guide: "I Want to Learn X → Go to Y"

| I want to learn... | Go to... | Phase |
|--------------------|----------|-------|
| How to run an incident | 2-phase-sre-practitioner/2.1-incident-management/ | Phase 2 |
| How to write an SLO | 2-phase-sre-practitioner/2.3-service-level-management/ + 1-phase-foundations/1.0-vocabulary/1.0.2-sli-slo-error-budgets.md | Phase 2 |
| How to do a postmortem | 2-phase-sre-practitioner/2.2-problem-management/ | Phase 2 |
| How to talk to executives about risk | 1-phase-foundations/1.0-vocabulary/1.0.10-principal-leadership-communication.md + 4-phase-director/4.1-director-management-course/4.1.2-executive-communication.md | Phase 3–4 |
| How to review a change safely | 2-phase-sre-practitioner/2.5-change-release-management/ | Phase 2–3 |
| How to build a reliability program from scratch | phase-3-principal-sre.md | Phase 3 |
| How to measure reliability with numbers | 2-phase-sre-practitioner/2.0-metrics-foundation/ | Phase 2–3 |
| How to run a team | 4-phase-director/4.3-operations-team-roles/ | Phase 4 |
| How to manage a budget | 4-phase-director/4.1-director-management-course/4.1.3-budgeting-and-financial-management.md | Phase 4 |
| How to handle a vendor relationship | 4-phase-director/4.1-director-management-course/4.1.6-vendor-management.md | Phase 4 |
| How Kubernetes reliability works | 1-phase-foundations/1.3-kubernetes/ + 1-phase-foundations/1.0-vocabulary/1.0.6-kubernetes-platform-reliability.md | Phase 1 |
| How chaos engineering works | 1-phase-foundations/1.7-interview-readiness/ | Phase 1–2 |
| What BRI/EBV/RIS mean | 2-phase-sre-practitioner/2.0-metrics-foundation/ | Phase 2–3 |
| How to prep for Director interviews | job-search/ + phase-4-director-operations.md | Phase 4 |
| What to do right now in a P1 | 2-phase-sre-practitioner/2.1-incident-management/playbook/ | Any phase |

---

## The Three Knowledge Layers

This library organizes knowledge in three layers that build on each other. Do not skip layers.

### Layer 1: Understand — Cookbook (1-phase-foundations/1.0-vocabulary/)
Vocabulary, concepts, and interview-level explanations of every major SRE domain. Read these first. They give you the mental model before you encounter the operational complexity of the full frameworks.

- 19 topic files covering everything from reliability foundations to AI for SRE
- Written at the level of "explain this in an interview" — crisp, practical, memorable
- Maps to Phase 1 and Phase 2 primarily; some files extend into Phase 3–4

### Layer 2: Measure — Textbook (2-phase-sre-practitioner/2.0-metrics-foundation/)
A proprietary reliability measurement framework built around quantified metrics: BRI (Blast Radius Index), EBV (Error Budget Velocity), SCS (SLO Coherence Score), RIS (Reliability Index Score), and related terms. Gives you the numbers layer that turns operational intuition into executive communication.

- 9 chapters
- Read during Phase 2 and Phase 3 in parallel with the domain frameworks
- Chapter 9 is a live daily-practice reference — keep it open during incidents and CAB

### Layer 3: Operate — Domain Frameworks (concepts/[domain]/)
The full operational playbooks. These are the systems you run: incident management, change/release, SLM, availability, performance engineering, architecture governance, and director operations. Full chapters, playbooks, and templates for each domain.

- 13 domain frameworks
- Start reading these in Phase 2
- The director-level frameworks (director-management-course, director-operations-manual, operations-team-roles) are Phase 4 material

---

## Quick-Start Paths by Starting Point

### "I'm a dev lead new to SRE — where do I start?"
Start at Phase 1, Week 1. Do not skip the Linux and Kubernetes weeks even if you are comfortable with them — the lab exercises build operational habits, not just technical recall.

→ **Go to**: `phase-1-sre-foundations.md`

### "I'm already a Senior SRE — do I have to start at Phase 1?"
No. Validate your Phase 1 competency gates. If you can hit all six, skip to Phase 2. If you are missing one or two, read the specific week's content, not the whole phase.

→ **Go to**: `phase-2-sre-practitioner.md` — check the prerequisites and competency gates first

### "I'm a Senior SRE with 5+ years and P1 IC experience"
You likely belong in Phase 3. Check the Phase 3 prerequisites and competency gates. If your gap is the measurement framework (textbook), start there in parallel with your Phase 3 reading.

→ **Go to**: `phase-3-principal-sre.md`

### "I'm preparing for Director-level interviews in the next 3–6 months"
Start Phase 4 immediately and run `job-search/` in parallel. Do not wait until you have finished Phases 1–3 — Director interview prep is its own track, and the frameworks in Phase 4 give you the vocabulary to talk about operational leadership credibly.

→ **Go to**: `phase-4-director-operations.md` + `job-search/`

### "I need to respond to a P1 right now"
Stop reading this document.

→ **Go to**: `2-phase-sre-practitioner/2.1-incident-management/playbook/`

Come back when the incident is closed. Then read `2-phase-sre-practitioner/2.1-incident-management/` to understand why the playbook is structured the way it is.

### "I have a job interview next week for a Senior SRE role"

- Day 1: `1-phase-foundations/1.0-vocabulary/1.0.17-principal-sre-mastery-roadmap.md` — read the full roadmap
- Days 2–3: Vocabulary topics 1.0.1 through 1.0.5 (reliability foundations through distributed systems)
- Days 4–5: Vocabulary topics 1.0.6 through 1.0.10 (Kubernetes through principal leadership)
- Day 6: `2-phase-sre-practitioner/2.0-metrics-foundation/2.0.3-blast-radius-bri-cc-fli-dsa.md` (BRI) + `2.0.4-health-signals-ebv-apr-mtbi-ocr.md` (EBV) — high-frequency interview topics
- Day 7: `3-phase-principal-sre/3.5-capstone/scenarios/` for storytelling material

### "I have a job interview next week for a Director of Operations role"

- Day 1: `4-phase-director/4.1-director-management-course/4.1.1-directors-role.md`
- Day 2: `4-phase-director/4.1-director-management-course/4.1.2-executive-communication.md`
- Day 3: `4-phase-director/4.1-director-management-course/4.1.3-budgeting-and-financial-management.md` + `4.1.4-managing-senior-managers.md`
- Day 4: `4-phase-director/4.1-director-management-course/4.1.6-vendor-management.md` + `4.1.7-partnership-management.md`
- Day 5: `4-phase-director/4.3-operations-team-roles/4.3.2-role-definitions.md`
- Days 6–7: `job-search/` interview prep + practice STAR stories anchored to T-Mobile DND platform

### "I want to know what's missing from this curriculum"

→ **Go to**: `gap-analysis.md` — all 33 gaps across infrastructure, technical SRE, and leadership domains

### "I need the complete content map"

→ **Go to**: `content-map.md` — every file mapped to a phase and audience

---

## A Note on Pacing

This path is designed for working professionals, not students. You are learning while running an operational role. That is an advantage: every framework you read, you can apply at work the same week. The competency gates at the end of each phase are designed to be demonstrated through real work, not simulated exercises.

If a phase takes longer than the suggested duration, that is normal. The clock is a guide, not a deadline. What matters is whether you can demonstrate the competency gates — not whether you finished in 12 weeks.

Move at the pace of your role, not the pace of the calendar.
