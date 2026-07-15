# Research Archive

All research conducted for the SRE/DevSecOps training program. Each file is a clean human-readable synthesis of an adversarially verified research run.

## Files

| File | What it answers | Agents | Verified |
|---|---|---|---|
| [research-01-job-market-intelligence.md](research-01-job-market-intelligence.md) | What do $180k+ SRE/DevSecOps jobs require? Vocabulary, depth, salary, toolchains, interview patterns. | 110 | 2/25 hard facts (salary unverifiable; vocabulary confirmed) |
| [research-02-learning-resources.md](research-02-learning-resources.md) | Best books, Coursera programs, YouTube channels, thought leaders, free resources by domain. | 107 | 18/25 hard facts |
| [research-03-program-review-and-gap-analysis.md](research-03-program-review-and-gap-analysis.md) | Full gap analysis, blind spots, risk register, capstone project specs, freshness protocol. | Agent review | Grounded in Training_Plan_Master.md |
| [research-04-interview-intelligence.md](research-04-interview-intelligence.md) | Verbatim interview questions + depth levels + vocabulary + "what good looks like" + T-Mobile STAR anchors — all 8 domains. | Synthesized | From Training_Plan_Master.md Section 1 |
| [research-05-enterprise-security-trends.md](research-05-enterprise-security-trends.md) | Latest 2025-2026 enterprise security trends: zero-trust (Gartner/Forrester verified), AI/LLM OWASP Top 10 (verified), eBPF at hyperscalers (verified), supply chain platformization (verified), secrets sprawl stats, policy-as-code engines (OPA/Kyverno/Cedar), SPIFFE/SPIRE, regulatory frameworks (NIST CSF 2.0, DORA, EU CRA). | 115 | 13/25 hard facts |

## How to Use During Training

**When writing a LinkedIn post or resume bullet**:
→ `research-01` Section 2 (verified vocabulary lists — security + observability)
→ `research-05` "Interview Vocabulary Master List" (enterprise security trends vocabulary)

**When starting a new domain**:
→ `research-02` — find the domain, enroll in the primary course before first study session

**When preparing salary negotiation**:
→ `research-01` Section 4 — use levels.fyi directly; do not cite refuted figures

**When asked about zero-trust**:
→ `research-05` Trend 1 — Forrester definition (3-0 verified), Gartner stats, five functional domains

**When asked about AI/LLM security**:
→ `research-05` Trend 2 — OWASP LLM Top 10, LLM03 supply chain, LLM06 excessive agency (both 3-0)

**When asked about supply chain security**:
→ `research-01` Section 1 Finding 1 (OWASP A03:2025)
→ `research-05` Trend 4 (GitHub/npm/PyPI native provenance, 71% unpinned actions stat)
→ `research-02` Section 1 (OWASP Supply Chain Cheat Sheet)

**When asked about observability / MELT**:
→ `research-01` Section 1 Finding 2 (MELT verified)
→ `research-04` Domain D (verbatim interview questions + burn rate math)

**When asked about eBPF**:
→ `research-05` Trend 3 (Meta Katran + GKE Autopilot — 3-0 verified)
→ `research-04` Domain A (K8s interview questions referencing eBPF CNI)

**When asked about secrets management**:
→ `research-05` Trend 5 (70% still valid stat, ESO VaultDynamicSecret pattern — 3-0 verified)

**For mock interview prep (any domain)**:
→ `research-04` — verbatim questions, vocabulary, T-Mobile STAR anchors, burn rate math

**When asked about compliance frameworks**:
→ `research-05` Trend 9 — NIST CSF 2.0, DORA, EU CRA, FedRAMP, SOC2 table

## Confidence System
- ✅ Hard-verified: cite confidently in interviews and on resume
- ⚠️ Directional: use for learning; do not cite as primary-sourced fact
- ❌ Refuted: do not use; go to primary source directly

## Refresh Schedule
- **Monthly**: Check OWASP Top 10 page for updates; verify Kubernetes version references
- **Bi-weekly**: Pull 5 new job postings from target companies; compare vocabulary against research-01
- **Before enrolling in any course**: Verify Coursera program structure at the URL listed — program structures change
- **Before any cert exam**: Verify exam code and objectives at the official certification body
