# Notification Platform Reliability — Portfolio Project | Week 6 Capstone 1

---

## Why This Matters

**Interview relevance**: A Director/VP SRE candidate who cannot show a portfolio artifact is a candidate who is describing skills they may or may not have. This capstone converts everything from Weeks 1–5 into a public GitHub repository that hiring managers at AWS, Google, Databricks, and Snowflake can read before your first call. It is the difference between "I know SLOs" and "here is the SLO YAML I wrote for a production platform."

**Business impact**: The notification platform in this portfolio processes 25M messages/day. Every reliability engineering decision here — the SLO definition, the error budget policy, the runbooks — directly affects whether T-Mobile customers receive fraud alerts, 2FA codes, and network outage notifications. Hiring managers at mature SRE organizations recognize this level of production engineering when they see it.

**What this unlocks**: After this capstone is on GitHub, you have a concrete artifact to reference in every interview. "Let me show you the error budget policy I wrote" is a more powerful answer than describing a policy you wrote. The portfolio also demonstrates GitHub fluency — itself a signal.

---

## Analogy: The Reliability Practice as a Flight Operations Manual

Think of this portfolio project the way an airline's operations division thinks about its Flight Operations Manual (FOM). The FOM does not make the planes fly — the engineers and pilots do. But the FOM is what turns individual expertise into institutional reliability. It answers: what are the standards (SLOs), what happens when those standards are being violated (error budget policy and runbooks), what decisions were made about the equipment and why (ADRs), and what does the operation's performance look like against industry benchmarks (DORA).

Your portfolio is the FOM for the notification platform. A hiring manager reading it is not just evaluating whether you know the technology — they are evaluating whether you know how to build a reliability practice that survives you. A practice that would still function if you left tomorrow. That is what Director/VP SRE means.

---

## Vocabulary Translation Table

| Their Term | Your Existing Mental Model |
|---|---|
| SLO (Service Level Objective) | TIBCO SLA threshold — the number below which the business escalates |
| Error budget | Compliance margin in a regulated process — how much defect rate you can absorb before stopping the line |
| Burn rate | Consumption rate of a limited resource — like a data center UPS battery draining faster than it charges |
| Sloth (SLO tool) | TIBCO BusinessWorks deployment descriptor — declarative config that generates operational artifacts |
| DLQ (Dead Letter Queue) | The "undeliverable" holding queue in TIBCO EMS — messages that failed all retries |
| ADR (Architecture Decision Record) | A CAB (Change Advisory Board) decision document — the permanent record of a significant technical choice and its tradeoffs |
| DORA metrics | ITSM KPIs — MTTR and change failure rate are directly equivalent; deployment frequency maps to release cadence |
| Canary deployment | A controlled partial rollout in PCF — like pushing to 10% of a CF space before the full push |
| OTel Collector sidecar | A Splunk Universal Forwarder running per-pod — collects and forwards telemetry without touching the application |

---

## 30-Second Version

This capstone produces a GitHub-ready portfolio project showing the SLO definitions, error budget policy, runbooks, ADRs, and DORA metrics for the notification platform you operate at T-Mobile. It demonstrates production SRE engineering practice at Director/VP level. It is the concrete artifact that replaces "I know how to do this" with "here is the work."

---

## 2-Minute Version

The notification platform capstone has seven artifacts:

1. **PORTFOLIO_README.md** — the hiring manager entry point. Architecture diagram, outcome summary, file map.
2. **slo-definitions.yaml** — three SLOs in Sloth format: SMS delivery success rate (99.5%), push latency P95 (99.0%), API availability (99.9%). Deployable to a Prometheus/Kubernetes stack.
3. **error-budget-policy.md** — what happens at 50%, 75%, and 100% budget consumption. Who decides what. How feature freeze is invoked and lifted.
4. **Grafana dashboard JSON** — four panels: error budget gauge, burn rate time series, queue depth, consumer throughput vs. depth. Importable into any Grafana 10.x instance.
5. **Two runbooks** — high burn rate response (NOTIF-RB-001) and RabbitMQ DLQ backup (NOTIF-RB-002). Step-by-step with exact commands and EXPECTED_OUTPUT.
6. **Three ADRs** — EKS over PCF, dual-export telemetry, RabbitMQ over Kafka. Each has context, decision, consequences, and alternatives considered.
7. **DORA metrics baseline** — 18-month data showing the team moved from Medium to Elite/High band. Explains the engineering practices that drove each improvement.

---

## 5-Minute Version (Tradeoffs, Failure Modes, Design Decisions)

**SLO calibration tradeoff**: The three SLOs are set at 99.5%, 99.0%, and 99.9%. These are deliberately not all at 99.9%. Setting SMS delivery at 99.9% would give you 43.8 minutes/month of budget — any single carrier incident (which is outside your control) would consume it entirely. Setting it at 99.5% gives 216 minutes, which is survivable. SLO targets that are too tight punish the team for external failures; SLO targets that are too loose give no signal. Calibration requires knowing your actual failure modes and their frequency.

**Error budget policy tradeoff**: The policy invokes feature freeze at 75% consumption. Some organizations freeze at 50%; some never formally freeze. The 75% threshold was chosen because the team has 15 engineers across two feature streams — a freeze at 50% would happen 2–3 times per year under normal operations and would create "cry wolf" dynamics. The threshold must match the team's actual operating reality, not a theoretical ideal.

**Dual-export telemetry tradeoff**: Running OTel collectors as sidecars (one per pod, not one per node) adds ~50MB memory per pod. At 25 pods, that is 1.25GB of additional cluster memory that could run application workloads. The cost is real. The benefit — blast radius isolation and observability independence from a single vendor — was judged worth it. A DaemonSet agent would cost less but means a single failing collector can cause a multi-pod blind spot. At 25M messages/day, a 30-second blind spot during an incident is unacceptable.

**RabbitMQ vs. Kafka failure mode**: The biggest operational risk with RabbitMQ at scale is the memory alarm — when broker memory exceeds the high watermark (default 40% of system RAM), RabbitMQ blocks all publishers. At 25M messages/day, a memory alarm that lasts 5 minutes is a 87,000-message backup. The mitigation is: monitor broker memory continuously, size nodes with 2x headroom, and have a pre-tested scale-up procedure. This failure mode does not exist in Kafka (Kafka applies backpressure differently, via consumer lag). This is the honest cost of the RabbitMQ decision.

**Director lens**: The real value of this portfolio is not the technical content — it is that it exists at all. A Director who can produce this artifact demonstrates that they build practices that are documented, transferable, and not dependent on heroism. That is exactly what a VP of Engineering wants to hire at the Director level: someone who builds systems, not someone who is the system.

---

## Director/VP Lens

**How a Director governs this vs. how an IC implements it**:

IC implementation:
- Writes the Sloth YAML, deploys the PrometheusRule CRDs, tunes the alert thresholds.
- Responds to the burn rate alert, executes the runbook, resolves the incident.
- Maintains the Grafana dashboard as the monitoring tool changes.

Director governance:
- Sets the SLO target levels (99.5% vs. 99.9%) based on business context and upstream contract obligations — not just technical feasibility.
- Owns the error budget policy as a joint agreement with the Engineering Manager and Product Manager. When feature freeze is invoked, the Director is accountable to the VP for the business decision to slow delivery in order to protect reliability.
- Reviews DORA metrics quarterly as an organizational health signal, not just as a team metric. A CFR increase from 4% to 8% is a conversation about engineering practice, not a conversation about individual engineers.
- Uses the portfolio itself as a hiring and team development artifact — "this is the standard we operate to" — rather than just a personal credentials document.

**How AI changes this domain**:
- AI-assisted runbook generation from incident data (LLM trained on past incidents can draft the next runbook update). The human role shifts to validation and judgment, not drafting.
- AI-driven burn rate anomaly detection (not just threshold alerts, but pattern recognition: "this burn rate trajectory matches the carrier outage pattern from 8 months ago"). This is the OpsGenie/BigPanda evolution direction.
- The Director role: governance of AI-generated reliability artifacts. Ensuring that AI-written runbooks are validated by humans before they reach production on-call use. Responsible for the AI-augmented SRE practice, not just the SRE practice.

---

## Comprehension Check

Answer 2 of 3 to proceed to the lab.

**Q1**: The SMS delivery SLO is set at 99.5%, not 99.9%. The error budget policy says feature freeze happens at 75% budget consumption. If an unexpected carrier outage causes 30% of SMS messages to fail for 2 hours, approximately how much of the monthly error budget is consumed, and what policy threshold does that cross?

**Q2**: The OTel Collector runs as a sidecar per pod, not as a DaemonSet agent. What specific reliability benefit does the sidecar model provide, and what is the concrete operational cost that was accepted in exchange?

**Q3**: ADR-003 chose RabbitMQ over Kafka. The ADR says this decision should be re-evaluated if throughput exceeds 5,000 msg/s. Currently the platform runs at ~290 msg/s peak. What business or technical change would most likely drive the platform to a throughput level that forces that re-evaluation, and what would the migration path look like?

---

## ANSWER KEY — Comprehension Check

**A1**: 
- At 25M messages/day = ~290 msg/s average = ~17,400 msg/minute.
- 30% failure for 2 hours = 0.30 × 17,400 × 120 minutes = ~626,400 failed messages.
- Monthly error budget at 99.5% = 0.5% × 25M/day × 30 days = 3,750,000 messages.
- Budget consumed = 626,400 / 3,750,000 = ~16.7%.
- This does NOT cross the 50% policy threshold. It is a material consumption event but does not trigger feature freeze.
- However: the ADR also states that carrier-attributed failures (carrier_fault=true) are excluded from the error budget. If the carrier outage is correctly attributed, the impact on the budget is 0% — this is exactly why the carrier_fault label exclusion exists.
- Full credit for either answer if the reasoning is correct.

**A2**:
- Reliability benefit: sidecar isolation means a failure, misconfiguration, or memory saturation in one pod's collector does not affect any other pod's telemetry. With a DaemonSet agent, a single failing agent on a node causes a blind spot for all pods on that node simultaneously.
- Concrete cost accepted: approximately 50MB memory + 20m CPU per pod. At 25 pods = 1.25GB additional cluster memory that could otherwise run application workloads. This is a real, measurable cost — not a theoretical trade-off.

**A3**:
- Most likely driver: T-Mobile launches a new real-time notification channel that requires high-volume, low-latency streaming (e.g., real-time network event notifications for IoT devices, or a push-to-device mesh for T-Mobile Home Internet). This could push sustained throughput to 5,000–10,000 msg/s.
- Migration path: RabbitMQ Streams (added in RabbitMQ 3.9) provides a Kafka-compatible interface on existing RabbitMQ infrastructure. A migration path would be: evaluate RabbitMQ Streams for the new high-volume channel first (retains operational familiarity); if RabbitMQ Streams cannot meet throughput targets, migrate the high-volume channel to MSK (managed Kafka) while retaining RabbitMQ for the existing notification channels (dual-broker for 12-18 months); then evaluate full consolidation based on operational experience.

---

## Lab: Build the Portfolio Directory Structure

### Prerequisites

- WSL2 Ubuntu terminal open
- `git` installed in WSL2: `git --version` should return 2.x+
- GitHub account with SSH key configured: `ssh -T git@github.com` should return your username
- Confirm working directory is in your WSL2 home or a projects folder: `pwd`

**Note**: The files in this lab already exist in `C:\Work\Training\portfolio\notification-platform-reliability\` (Windows path) = `/mnt/c/Work/Training/portfolio/notification-platform-reliability/` (WSL2 path). The lab walks through verification, git initialization, and GitHub push preparation.

---

### Step 1: Verify File Structure

```bash
# In WSL2 terminal
cd /mnt/c/Work/Training/portfolio/notification-platform-reliability/

# Verify all expected files exist
find . -type f | sort
```

**EXPECTED_OUTPUT**:
```
./PORTFOLIO_README.md
./WEEK6-CAPSTONE1-TUTORIAL.md
./adr/001-eks-over-pcf.md
./adr/002-dual-export.md
./adr/003-rabbitmq-vs-kafka.md
./dashboards/grafana-slo-dashboard.json
./director-vp-narrative.md
./dora-metrics-baseline.md
./error-budget-policy.md
./runbooks/high-burn-rate.md
./runbooks/queue-backup.md
./slo-definitions.yaml
```

**WHY**: Confirming the file tree matches the expected structure before committing prevents publishing an incomplete portfolio. A hiring manager cloning a half-finished repository is worse than no repository.

---

### Step 2: Initialize Git Repository

```bash
cd /mnt/c/Work/Training/portfolio/notification-platform-reliability/

git init
git add .
git status
```

**EXPECTED_OUTPUT**:
```
Initialized empty Git repository in /mnt/c/Work/Training/portfolio/notification-platform-reliability/.git/

On branch main
No commits yet

Changes to be staged:
  (use "git rm --cached <file>..." to unstage)
        new file:   PORTFOLIO_README.md
        new file:   WEEK6-CAPSTONE1-TUTORIAL.md
        new file:   adr/001-eks-over-pcf.md
        new file:   adr/002-dual-export.md
        new file:   adr/003-rabbitmq-vs-kafka.md
        new file:   dashboards/grafana-slo-dashboard.json
        new file:   director-vp-narrative.md
        new file:   dora-metrics-baseline.md
        new file:   error-budget-policy.md
        new file:   runbooks/high-burn-rate.md
        new file:   runbooks/queue-backup.md
        new file:   slo-definitions.yaml
```

**WHY**: `git init` creates the `.git/` directory that tracks all changes. `git add .` stages all files for the first commit. `git status` confirms what will be committed — always check before committing.

---

### Step 3: Create a .gitignore File

```bash
cat > .gitignore << 'EOF'
# Exclude anything with real credentials or internal URLs
*.env
*.secret
# Exclude OS files
.DS_Store
Thumbs.db
EOF
```

**WHY**: Before publishing to GitHub, ensure no file with internal URLs, credential strings, or PII is in the repository. The files created in this project use placeholder URLs (wiki.internal, grafana.internal) — these are safe to publish. A `.gitignore` prevents accidental inclusion of environment files if you add them later.

---

### Step 4: Make the First Commit

```bash
git add .gitignore
git commit -m "feat: notification platform reliability portfolio — Week 6 Capstone 1

- 3 production SLOs in Sloth YAML format (SMS delivery, push latency, API availability)
- Error budget policy with 50/75/100% threshold governance
- 2 runbooks: high burn rate (NOTIF-RB-001) and queue backup (NOTIF-RB-002)
- 3 ADRs: EKS over PCF, dual-export telemetry, RabbitMQ over Kafka
- Grafana 4-panel SLO dashboard JSON (importable)
- DORA metrics baseline (18-month, Medium to Elite/High band)
- Director/VP narrative for interview use"
```

**EXPECTED_OUTPUT**:
```
[main (root-commit) abc1234] feat: notification platform reliability portfolio — Week 6 Capstone 1
 12 files changed, NNNN insertions(+)
 create mode 100644 .gitignore
 create mode 100644 PORTFOLIO_README.md
 ...
```

**WHY**: A clean, descriptive first commit message signals engineering professionalism. Hiring managers sometimes read commit history — a thoughtful commit message in a portfolio repository is a small but real signal.

---

### Step 5: Create GitHub Repository and Push

```bash
# Create a new PUBLIC repository on GitHub
# Option A: via GitHub CLI (if installed)
gh repo create notification-platform-reliability \
  --public \
  --description "SRE portfolio: SLOs, error budget policy, runbooks, and ADRs for a 25M msg/day notification platform" \
  --source=. \
  --remote=origin \
  --push

# Option B: manual (if gh CLI not installed)
# 1. Go to github.com/new
# 2. Name: notification-platform-reliability
# 3. Description: SRE portfolio: SLOs, error budget policy, runbooks, and ADRs for a 25M msg/day notification platform
# 4. Set to PUBLIC
# 5. Do NOT initialize with README (you already have one)
# 6. Then run:
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/notification-platform-reliability.git
git branch -M main
git push -u origin main
```

**EXPECTED_OUTPUT** (Option A):
```
✓ Created repository YOUR_GITHUB_USERNAME/notification-platform-reliability on GitHub
  https://github.com/YOUR_GITHUB_USERNAME/notification-platform-reliability
Enumerating objects: 14, done.
...
To github.com:YOUR_GITHUB_USERNAME/notification-platform-reliability.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

**WHY**: A public repository is the portfolio artifact. The GitHub URL is what you include in your resume, LinkedIn, and cover letters. A private repository cannot be read by a hiring manager.

---

### Step 6: Verify the Published Repository

```bash
# Confirm remote is set and push succeeded
git remote -v
git log --oneline

# Open in browser (WSL2)
explorer.exe "https://github.com/YOUR_GITHUB_USERNAME/notification-platform-reliability"
```

**EXPECTED_OUTPUT**:
```
origin  git@github.com:YOUR_GITHUB_USERNAME/notification-platform-reliability.git (fetch)
origin  git@github.com:YOUR_GITHUB_USERNAME/notification-platform-reliability.git (push)

abc1234 feat: notification platform reliability portfolio — Week 6 Capstone 1
```

**Checklist before you call this done**:
- [ ] PORTFOLIO_README.md renders correctly on GitHub (check the main page)
- [ ] slo-definitions.yaml is readable and correctly formatted
- [ ] The adr/ directory shows three files
- [ ] The runbooks/ directory shows two files
- [ ] The dashboards/ directory shows the JSON file
- [ ] No internal URLs, credentials, or PII visible in any file
- [ ] Repository description is set (visible under the repo name on GitHub)
- [ ] Repository is PUBLIC (padlock icon should NOT appear)

---

## Lab ANSWER KEY — Diagnostics Per Step

**Step 1 fails (file not found)**:
The portfolio files may be at a slightly different path. Run `find /mnt/c/Work/Training/portfolio -name "*.md" | head -20` to locate them. If files are missing, check that the Claude Code session that created them completed successfully.

**Step 2 — git init fails with "not a git repository" but files exist**:
Check that you are in the correct directory: `pwd` should show the notification-platform-reliability directory. If you are in a parent directory, `git add .` will include files you did not intend to commit.

**Step 4 — commit fails with "Please tell me who you are"**:
Git needs a user identity for commits. Configure it:
```bash
git config --global user.email "your.email@example.com"
git config --global user.name "Your Name"
```
Then re-run the commit command.

**Step 5 — push fails with "Permission denied (publickey)"**:
SSH key is not configured for GitHub. Either add your WSL2 SSH public key to GitHub (Settings > SSH and GPG keys), or use HTTPS instead:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/notification-platform-reliability.git
git push -u origin main
# Enter your GitHub username and personal access token (not password)
```

**Step 5 — gh repo create fails with "command not found"**:
Install GitHub CLI:
```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install gh -y
gh auth login
```

---

## Interview Questions (Staff/Principal Level)

**Q1**: Walk me through how you would define SLOs for a new notification channel — one that has never been in production. What data do you need, and how do you set the initial target?

**Q2**: Your error budget policy says feature freeze at 75% consumption. A product manager pushes back: "The feature I want to deploy is a reliability improvement, not a new feature. Why should it be frozen?" How do you respond, and what is the principle behind your answer?

**Q3**: You have three SLOs on the notification platform. They are all burning simultaneously. What is your diagnostic sequence? What does "all three burning at once" tell you that "one burning" does not?

**Q4**: The ADR chose RabbitMQ over Kafka in 2021. It is now 2026. The platform has scaled from 3M to 25M messages/day. What data would you review to decide whether to re-evaluate the decision, and what process would you use to evaluate it?

**Q5**: DORA metrics show your team is "High" on deployment frequency and "Elite" on MTTR. A new VP asks: "What would it take to get to Elite on deployment frequency?" How do you answer in a way that addresses both the technical path and the organizational trade-offs?

---

## STAR Anchor (T-Mobile Framing Per Question)

**Q1 (SLO definition for new channel)**:
- **S**: T-Mobile launched a new home internet product (T-Mobile Home Internet). The notification team was asked to onboard a new channel for device installation alerts.
- **T**: Define initial SLOs before any production traffic existed.
- **A**: Used 30-day shadow mode — ran the new channel in parallel with an existing one, collected error rate and latency data without alerting on it, set initial SLO targets at 2x the observed error rate (conservative). Reviewed at 90 days and tightened.
- **R**: SLOs were calibrated to real operating data before the first error budget policy enforcement. No false-positive freezes in the first quarter.

**Q3 (All three SLOs burning)**:
- **S**: During a major T-Mobile network event, we observed all three SLOs burning simultaneously.
- **T**: Diagnose whether this is one systemic cause or three independent causes.
- **A**: All three burning simultaneously is the "shared dependency" signal — it points to the broker layer (RabbitMQ) or the data layer (Cassandra), not to any individual channel's consumer. In that incident, it was a Cassandra write latency spike that caused consumer back-pressure, which backed up the queues, which increased API latency as producers waited for broker acknowledgement.
- **R**: Root cause identified in 8 minutes (vs. 47-minute MTTR baseline at the time), because the "all three burning" pattern was documented in the runbook as a shared dependency indicator.

---

## Tradeoffs and Failure Modes

**Top 3 tradeoffs to be ready to discuss**:

1. **SLO target tightness vs. error budget survivability**: A tighter SLO gives customers a better commitment but leaves less room for the team. The right calibration is "tight enough that failing to meet it is a real signal, loose enough that external failures do not consume it routinely." This requires quarterly calibration, not a one-time setting.

2. **Sidecar vs. DaemonSet OTel collector**: Sidecar costs more cluster memory but provides blast radius isolation. DaemonSet is cheaper but creates shared-fate observability failure. The right choice depends on the platform's tolerance for observability gaps during incidents. For a 25M msg/day production system, the memory cost is a better trade than the risk.

3. **RabbitMQ per-message TTL vs. Kafka simplicity**: RabbitMQ's TTL and DLQ features are powerful and exactly right for notification delivery. But they create operational complexity (DLQ management, poison message handling) that Kafka avoids through its log model. The notification platform accepted that complexity because the alternative — application-level TTL enforcement in every consumer — is worse. Know which complexity you are choosing.
