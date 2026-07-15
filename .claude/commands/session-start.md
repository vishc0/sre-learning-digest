Read the following files and give me a crisp training session brief:
1. `progress-log.md` — current week, confidence scores, completed topics
2. `CLAUDE.md` — program structure, learning model, lab rules
3. `session-start-prompt.md` — paste contents if user has filled it in

Then output:

**Current week**: Week [N] — [sprint name]
**Completed this week**: [list topics with confidence scores]
**Today's domain**: [which learning area]
**Lab environment status**: [AWS account / WSL2 / tools ready or needs setup]
**Open blockers**: [anything from last session that was unresolved]

Then ask: "What are we working on today — concept, lab, or interview prep?"

Remind me of the learning model: READ → THINK → TEST → PROJECT → PROCEED. Do not skip gates.
Remind me: Always run `terraform destroy` or `eksctl delete cluster` at end of any session that provisioned AWS resources.
