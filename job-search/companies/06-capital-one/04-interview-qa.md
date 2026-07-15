# Capital One — Interview Q&A Prep

## RECRUITER SCREEN
**Q: Tell me about yourself.**
"I'm Vishweshwar Chippa — 10 years at T-Mobile as SRE Principal. I operate AWS and Kubernetes in production, deploy Vault for secrets management, use GitLab for CI/CD, and build Python automation tools — which maps directly to Capital One's engineering standards. I run 4 platforms at 25M messages daily with 15 engineers, 99.99% uptime, zero critical vulnerabilities in 18 months. I have an approved I-140, so the transfer is clean."

## BEHAVIORAL QUESTIONS

**Q: Describe how you've applied security-first principles in your SRE work.**
"Security is in my pipeline, not added after. Every deployment in my GitLab CI/CD runs Aqua container scans, SonarQube static analysis, and AppScan before any environment promotion. Vault manages all secrets — no hardcoded credentials anywhere in 4 platforms. I run quarterly Cybersecurity Syndicate reviews with our security team. Results: zero critical security vulnerabilities reaching production in the last 18 months across all 4 platforms."

**Q: How do you approach Python automation as an SRE practice?**
"I treat toil as technical debt. Every manual process that happens more than twice a month gets a Python script. Every Python script that runs in production gets tested, monitored, and owned. In practice: I built monitoring tools, anomaly detection models, triage dashboards, and a natural language metrics agent — all in Python. My team's manual toil dropped ~25% over two years from this practice. The principle is: if a human does it repetitively, a script does it better."

**Q: How have you handled a compliance or audit situation?**
"We had an internal audit flagging our DND (suppression) domain for incomplete audit trail coverage — some message suppression decisions weren't logged with sufficient detail. I treated it like a Sev2: assigned an owner, defined the gap, and set a 2-week remediation timeline. Built immutable logging for every suppression decision with timestamp, suppression rule applied, and message ID. Passed the follow-up audit with zero findings. That implementation became the standard for all 4 platforms."

## TECHNICAL QUESTIONS

**Q: How do you use Vault in a Kubernetes-based platform?**
"We use the Vault Agent Injector pattern — Vault secrets are injected as files into pods via init containers rather than environment variables. This means secrets never touch application code directly. Vault policies are role-based, with separate roles per platform. Secret rotation is automated via Vault's dynamic secrets for database credentials. I also integrated Vault with our GitLab CI/CD to provide short-lived deploy tokens instead of long-lived API keys. Zero static credentials in our deployment process."

**Q: Walk me through your approach to FinOps/cost optimization for a Kubernetes platform.**
"Three levers: right-sizing, autoscaling, and waste elimination. 
- Right-sizing: We profiled actual CPU/memory usage at P95 load and adjusted requests/limits accordingly; found 30% over-provisioning in our initial K8s setup
- Autoscaling: HPA for CPU-driven pods, KEDA for queue-depth-driven scaling so we scale with actual message load
- Waste elimination: Monthly audit of idle pods, orphaned PVCs, and unused namespaces

This is an area I'd lean into more systematically — I want to add FinOps tagging and cost attribution per platform as a next step."

## QUESTIONS TO ASK
1. "How does Capital One's SRE organization handle the tension between AWS-native tooling and the engineering teams' desire to use diverse tools?"
2. "What's the expectation for Python automation scope at Principal SRE level?"
3. "How does the Plano campus SRE team collaborate with the McLean and Richmond offices?"
