# Training Session Start Template

**INSTRUCTIONS**: Copy this file content and paste it at the start of every Claude Code session.
Update the fields in [brackets] before pasting. This gives Claude instant context without re-reading 1,939 lines.

---

## Session Start — [DATE e.g. June 18, 2026]

**Who I am**: Vishweshwar Chippa, SRE Manager targeting Director/VP SRE at T-Mobile (15-person team, 25M msg/day notification platform). Targeting Director/VP SRE and Senior DevSecOps roles, $200k–$350k+ TC. H1B active, I-140 approved, open to relocate.

Full profile: read `CLAUDE.md`
Roadmap: read `ROADMAP.md`
Full program: read `00-program/training-plan-master.md`
Progress log: read `00-program/progress-log.md`

**Current program state**:
- Program week: [X of 10]  
- Sprint: [e.g., "Week 1 — Terraform Foundation"]
- Topics completed since last session: [e.g., "Terraform state, S3 backend, DynamoDB locking"]
- Topics in progress (confidence below 4): [e.g., "Terraform modules — read concept, not yet done lab"]
- Open question from last session: [e.g., "Why does `terraform refresh-only` differ from `terraform plan`?"]
- Confidence ratings (1=read it, 5=can teach it): [e.g., "Terraform state: 3/5, SBOM: 2/5"]

**Today's goal** (one specific deliverable):
[e.g., "Complete the Terraform modules lab — get the EKS module to run `terraform plan` successfully"]

**Job search strategy**:
- Phase 1 (Weeks 1–5): Build depth in startup/mid-size SRE toolchains — focus on hands-on lab portfolio
- Phase 2 (Weeks 6–10): Scale narrative to FAANG-grade architecture, AI/ML ops, and executive communication
- Portfolio projects target: GitHub public repos + LinkedIn case studies anchored to T-Mobile experience

**Program context (10 weeks total)**:
- Weeks 1–5: Cloud-native IaC, Kubernetes internals, supply chain security, observability translation
- Weeks 6–8: Integration capstones, portfolio projects, interview readiness
- Weeks 9–10: AI Engineering for SRE — LLM ops, AI-assisted incident command, prompt caching for runbooks, embedding-based observability

**Environment** (confirmed, do not ask):
- WSL2 installed and working — use bash/Ubuntu commands directly
- AWS training account being set up — all labs run on real AWS (not LocalStack)
- AWS CLI configured in WSL2 with `training-admin` IAM user
- Region: us-east-1 for all labs unless specified otherwise
- Always include `terraform destroy` / `eksctl delete cluster` cleanup steps at end of every AWS lab
- Billing alert set at $25/month — flag if any lab step looks like it will exceed $5 unexpectedly

**Constraints**:
- Available time today: [X hours]
- Do not start new topics today unless I confirm today's goal is complete.
- Learning model: READ → comprehension check → LAB (with expected outputs and cleanup) → proceed. Do not deliver all four artifacts at once.

**Reference files**:
- `CLAUDE.md` — my profile, learning style, working style for Claude
- `ROADMAP.md` — master navigation: all phases, topics, and links
- `00-program/training-plan-master.md` — full 10-week program (Sections 1–6)
- `00-program/resource-library.md` — canonical books, courses, YouTube per domain
- `00-program/progress-log.md` — weekly confidence scores and completed topics
- `00-program/session-start-prompt.md` — this file

**What I need today**:
[Choose one]:
- [ ] Concept guide for [topic] — with middleware analogy + vocabulary translation table
- [ ] Lab for [topic] — WSL2-compatible, with EXPECTED_OUTPUT at every step
- [ ] Comprehension check (3 questions) for [topic] — to unlock the lab
- [ ] Interview prep quiz (5 questions, escalating) for [topic]
- [ ] LinkedIn post draft for [topic] — practitioner voice, T-Mobile anchored
- [ ] Full review of my progress-log.md — what do I need to repeat or revisit?
