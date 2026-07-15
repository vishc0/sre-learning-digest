# Master Plan Additions — Updates to Training_Plan_Master.md
## Generated: June 2026 | Extends program to 10 weeks + adds Director/VP leadership track

---

## How to Apply These Updates
This file contains surgical additions to the existing 8-week plan plus two new weeks (AI Engineering).
Do not rewrite Training_Plan_Master.md — add these sections to it. Priority: add Week 9 and 10 first, then fold in the per-week additions during Sunday rituals as you approach each week.

---

## Section 1: Surgical Additions to Existing Weeks 1–8

### Week 1 — Terraform Foundation
**Add:** FinOps basics alongside IaC — cost tagging strategy, AWS Cost Explorer, Terraform cost estimation with Infracost
**Where:** Day 4 or weekend session
**Why:** "How do you ensure IaC doesn't create runaway cloud spend?" is a common Director-level Terraform question
**Lab:** Add `infracost breakdown --path .` to the Terraform lab; add cost allocation tags to every resource
**Vocabulary added:** Infracost, cost allocation tags, showback, chargeback, unit economics

**Add:** Atlantis or Spacelift for team-scale Terraform governance
**Where:** Weekend reading (concept only, no lab)
**Why:** Directors are asked "how do you govern Terraform across 20 teams?" not just "how do you run apply"
**Vocabulary added:** Atlantis, Spacelift, GitOps for IaC, plan-in-PR workflow

---

### Week 2 — Supply Chain Security
**Add:** SLSA framework levels 1–3 — what each level requires, how to get a pipeline to SLSA Level 2
**Where:** Day 2 alongside Cosign/Sigstore
**Why:** SLSA is now the standard interviewers reference when asking about supply chain; "SLSA Level 2" appears in ~40% of DevSecOps Director JDs
**Lab:** Generate SLSA provenance with `slsa-github-generator` in a GitHub Actions pipeline
**Vocabulary added:** SLSA, provenance attestation, build integrity, hermetic build

**Add:** Compliance-as-code concepts — OpenSCAP, InSpec, AWS Config rules as code
**Where:** Day 5
**Why:** Director/VP candidates are expected to understand how compliance is automated, not just audited
**Vocabulary added:** InSpec, OpenSCAP, compliance-as-code, control mapping, audit evidence automation

---

### Week 3 — Kubernetes Internals
**Add:** Karpenter vs Cluster Autoscaler — when to use each, cost implications
**Where:** Day 3
**Why:** "How do you right-size your EKS cluster?" is asked in nearly every K8s Director interview; Karpenter is the 2025 answer
**Lab:** Deploy Karpenter on EKS sandbox, configure a NodePool, observe scale-up
**Vocabulary added:** Karpenter, NodePool, NodeClaim, EC2 Spot with Karpenter, bin packing

**Add:** Multi-tenancy patterns — namespace isolation vs. virtual clusters (vCluster) vs. separate clusters
**Where:** Weekend concept session
**Why:** Directors design multi-tenant platforms; this question separates IC from Director-level thinking
**Vocabulary added:** vCluster, hard multi-tenancy, soft multi-tenancy, namespace isolation limits

---

### Week 4 — AWS Depth + GitOps
**Add:** AWS Organizations + Service Control Policies (SCPs) for multi-account governance
**Where:** Day 2
**Why:** Director-level AWS question: "How do you govern 15 AWS accounts across teams?" SCPs are the answer
**Lab:** Create an SCP that denies `ec2:RunInstances` outside us-east-1 in a test OU
**Vocabulary added:** AWS Organizations, OU, SCP, Control Tower, Account Vending Machine

**Add:** ArgoCD ApplicationSet + app-of-apps pattern for fleet management
**Where:** Day 4 (extends existing ArgoCD coverage)
**Why:** "How do you manage GitOps across 50 teams?" — ApplicationSet is the answer
**Vocabulary added:** ApplicationSet, cluster generator, git generator, app-of-apps, fleet management

---

### Week 5 — Observability Translation
**Add:** FinOps for observability — cardinality cost management, Prometheus storage sizing, sampling strategies to control cost
**Where:** Day 3
**Why:** "Your observability bill tripled — what do you do?" is a real Director interview question
**Lab:** Add recording rules to reduce cardinality on a sample Prometheus setup; calculate storage cost
**Vocabulary added:** cardinality explosion, high-cardinality label, recording rules for cost, exemplars vs raw traces

**Add:** DORA + SPACE framework metrics — how to measure engineering effectiveness at the Director level
**Where:** Day 5
**Why:** Directors are expected to report on engineering health to VPs and C-suite; SPACE is the 2025 update to DORA
**Vocabulary added:** SPACE framework, developer satisfaction, performance, activity, communication, efficiency

---

### Week 6 — Portfolio
**Add:** All 3 capstone projects must have a Director/VP narrative layer:
- Architecture decision record (ADR) — why you made each key design choice
- Business impact statement — what failure would have cost in dollars or customer impact
- Team/org story — how you led the work, who you influenced, what tradeoffs you negotiated

**Add:** AI/ML portfolio artifact — one of the 3 capstones should include an AI component (anomaly detection, LLM-assisted runbook, or AI observability dashboard) to signal AI-native leadership

---

### Week 7 — Interview Readiness
**Add:** Director/VP interview loop preparation — these companies add rounds that Staff/Principal loops don't have:
- Executive presentation round: 15-min prepared presentation on "how you would build SRE at this company"
- Org design question: "You are joining a 200-person company with no SRE practice. What do you build first, second, third?"
- Business case question: "Justify the budget for an SRE team of 5 to a CFO who thinks ops is a cost center"

**Add:** Leadership philosophy statement — 2-minute answer to "What is your philosophy on SRE?" that is uniquely yours, not a Google SRE book recitation. Draft this in Week 7, practice it until it sounds natural.

---

### Week 8 — Polish + Active Search
**Add:** Phase 1 startup search activation — LinkedIn search strings, Wellfound/AngelList setup, Crunchbase filters for Series B-D companies with SRE Director openings
**Add:** H1B verification workflow — run h1bdata.info check on every company before first recruiter call
**Add:** Mentor outreach — identify 2-3 Directors/VPs from your network for informational conversations about Director interview patterns at their companies

---

## Section 2: New — Week 9: AI Engineering Foundations

### Overview
Builds the AI infrastructure and LLM fundamentals track. Connects to your existing observability and SRE expertise. Every concept is framed through the lens of "how do I run AI reliably in production" — not "how do I build AI models."

---

### Day 1: LLM Fundamentals — Operational Mental Model
**Vocabulary:** transformer, token, context window, temperature, top-p, top-k, inference, prompt, completion, system prompt, few-shot, zero-shot, hallucination, model weights, quantization, GGUF, vLLM, Ollama
**Lab:** Run Llama 3 locally via Ollama in WSL2; experiment with temperature and context window settings; observe latency vs quality tradeoff
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3
ollama run llama3
```
**Interview questions:**
- "What is a context window and what operational problem does it create at scale?"
- "Why does temperature matter for a production AI system — when do you set it to 0?"
- "Your LLM inference latency spiked from 800ms to 4s. Walk me through your diagnostic approach."
- "What is quantization and why would an SRE care about it?"
**What good looks like:** Treats LLMs like any other stateful service — SLA, latency percentiles, error budget, cost per call. Does not treat them as magic.
**T-Mobile STAR anchor:** "I already built ML-based anomaly detection and a GenAI leadership agent on our notification platform. What I'm adding is the infrastructure knowledge to deploy and operate these at enterprise scale, not just prototype them."
**Analogy:** An LLM is like a RabbitMQ consumer that never crashes but sometimes returns a message you didn't expect — you still need dead-letter handling, retry logic, and SLOs on response quality.

---

### Day 2: AI Platform Landscape — API, Pricing, Positioning
**Vocabulary:** Claude/Anthropic, GPT-4o/OpenAI, Gemini/Google, Grok/xAI, Llama/Meta, API key, rate limit, RPM, TPM, context caching, prompt caching, model routing, model gateway, LiteLLM
**Lab:** Call Claude API and OpenAI API from WSL2 Python; implement prompt caching on Claude; compare latency and cost for the same prompt across providers
```python
pip install anthropic openai litellm
# Compare: claude-sonnet-4-6 vs gpt-4o for same SRE runbook task
# Implement: Anthropic prompt caching to reduce cost on repeated system prompts
```
**Interview questions:**
- "Your company uses OpenAI today. The CTO wants to evaluate Claude and Gemini. How do you run that evaluation systematically?"
- "How does prompt caching work and why does it matter for production AI cost?"
- "What is model routing and when would you use LiteLLM in a production system?"
- "Gemini 2.0 has a 1M token context window. What operational problems does that create?"
**What good looks like:** Has a vendor evaluation framework. Knows pricing models. Understands that model choice is an architecture decision with cost, latency, and reliability tradeoffs — not just "which one is smartest."
**T-Mobile STAR anchor:** "When I evaluated Splunk MLTK vs custom Python for anomaly detection, I ran a structured evaluation with latency, cost, and accuracy metrics. I'd apply the same framework to LLM vendor selection."

---

### Day 3: AWS AI Infrastructure — Bedrock, SageMaker, GPU EKS
**Vocabulary:** AWS Bedrock, Bedrock Knowledge Base, Bedrock Guardrails, SageMaker endpoint, SageMaker JumpStart, EC2 g4dn/p3/p4 instances, NVIDIA CUDA, GPU node pool, EKS GPU operator, NVIDIA device plugin, inference endpoint, model serving, batch inference
**Lab:** Deploy a Claude model via AWS Bedrock API; create a Bedrock Knowledge Base with an S3 data source; query it via Python
```bash
aws bedrock list-foundation-models --region us-east-1
aws bedrock-runtime invoke-model --model-id anthropic.claude-sonnet-4-6 ...
```
**Interview questions:**
- "When would you use AWS Bedrock vs. running your own model on EC2 GPU vs. SageMaker endpoints?"
- "How do you add GPU nodes to an EKS cluster and ensure GPU workloads are scheduled correctly?"
- "Your Bedrock inference cost doubled in a week. How do you investigate and fix it?"
- "What is SageMaker JumpStart and when is it the right tool vs. a custom model?"
**What good looks like:** Can make the build-vs-buy decision for AI inference infrastructure. Knows Bedrock = managed API, SageMaker = managed ML platform, EC2 GPU = full control. Treats GPU capacity like any other scarce resource.

---

### Day 4: Azure AI Infrastructure — Azure OpenAI, AKS GPU, Azure ML
**Vocabulary:** Azure OpenAI Service, deployment (Azure OAI), Azure AI Foundry, Azure ML workspace, AKS GPU node pool, NC-series VMs, Azure AI Search, Cognitive Services, Managed Identity for AI, Azure AI Content Safety
**Lab:** Deploy a GPT-4o model via Azure OpenAI Service; call it via Python with Managed Identity (no API key stored); configure content filtering
```python
from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI
# Keyless auth via Managed Identity — demonstrate to interviewer
```
**Interview questions:**
- "What is the difference between Azure OpenAI Service and the OpenAI API? When does a company choose Azure?"
- "How do you authenticate to Azure OpenAI without storing API keys anywhere?"
- "A financial services client needs GPT-4 but cannot send data outside their Azure tenant. How do you architect this?"
- "What is Azure AI Content Safety and when is it a compliance requirement?"
**What good looks like:** Knows Azure OpenAI = enterprise GPT with data residency, VNET integration, Managed Identity, compliance controls. Understands why regulated industries choose Azure OpenAI over direct OpenAI API.

---

### Day 5: RAG — Retrieval Augmented Generation Design
**Vocabulary:** RAG, retrieval augmented generation, embedding, embedding model, vector database, Pinecone, pgvector, Chroma, Weaviate, Qdrant, semantic search, chunk, chunking strategy, overlap, metadata filtering, reranking, hybrid search, BM25, FAISS, cosine similarity, hallucination reduction
**Lab:** Build a RAG pipeline using AWS Bedrock Knowledge Base + S3; ingest your SRE runbooks; query them with natural language
```python
# Ingest: upload SRE runbooks to S3
# Index: Bedrock Knowledge Base with Titan Embeddings
# Query: "What are the steps to recover from a RabbitMQ queue backup?"
# Evaluate: does the answer match the actual runbook?
```
**Interview questions:**
- "What is RAG and why is it better than fine-tuning for an internal knowledge base use case?"
- "Walk me through your chunking strategy for a 500-page operations runbook."
- "What is hybrid search and when does it outperform pure vector search?"
- "Your RAG system is returning irrelevant documents. What do you investigate first?"
**What good looks like:** Treats RAG as an information retrieval problem with SRE properties — latency, recall, precision, cost per query, freshness of index. Not just "plug LangChain in and it works."
**T-Mobile STAR anchor:** "My MART framework in Splunk is essentially RAG before RAG had a name — we retrieve relevant operational context (metrics, logs, past incidents) and surface it to the responder. Bedrock RAG is the same pattern, modernized."

---

### Weekend Lab: Deploy End-to-End RAG on AWS Bedrock
**Goal:** Build a working RAG system that queries your own SRE documentation
**Resources used:** S3 bucket (free tier), Bedrock Knowledge Base (~$0.10), Bedrock Claude API (~$0.05 for testing)
**Modules:**
1. Upload 5-10 markdown files from `learning/concepts/` to S3
2. Create Bedrock Knowledge Base, sync S3 source
3. Write Python script to query Knowledge Base
4. Ask 5 operational questions; evaluate answer quality
5. Teardown: delete Knowledge Base data source (S3 bucket stays, no ongoing cost)

---

## Section 3: New — Week 10: AI Platform Engineering & Agentic Systems

### Overview
Moves from consuming AI APIs to orchestrating AI systems. Covers the engineering infrastructure for multi-agent workflows, AI observability, and safety — the Director/VP layer of AI, not the data scientist layer.

---

### Day 1: LLM Orchestration — LangChain, LlamaIndex, LangGraph
**Vocabulary:** LangChain, LlamaIndex, LangGraph, chain, runnable, LCEL (LangChain Expression Language), DocumentLoader, TextSplitter, retriever, LLMChain, SequentialChain, graph, node, edge, state, conditional edge, checkpointer
**Lab:** Build a simple chain in LangChain that: loads a runbook, splits it, embeds it, retrieves relevant sections, and answers an operational question
**Interview questions:**
- "What is LangChain and when would you NOT use it in a production system?"
- "What is LangGraph and how does it differ from a simple LangChain chain?"
- "You have a complex multi-step AI workflow. How do you decide between LangGraph vs. a simple Python state machine?"
- "LangChain has been criticized for being too complex. What would you use instead for a simple RAG use case?"
**What good looks like:** Treats orchestration frameworks with SRE skepticism — adds complexity, adds failure modes, adds dependencies. Uses them when the workflow is genuinely complex; uses plain Python otherwise.
**Analogy:** LangGraph is like a workflow orchestrator (think Apache Airflow for AI) — you use it when you have conditional logic, retries, and state you need to manage. Simple chains are like a bash pipeline — use that first.

---

### Day 2: Agentic AI — Agents, Tool Use, Multi-Agent Systems
**Vocabulary:** AI agent, ReAct pattern, tool use, function calling, tool schema, tool result, multi-agent system, orchestrator agent, subagent, CrewAI, AutoGen, Swarm, agent loop, observation, thought, action, human-in-the-loop, agent memory, short-term memory, long-term memory, semantic memory
**Lab:** Build a simple tool-using agent with Claude API that can: check a URL status, summarize a log file, and output a structured incident report
```python
# Define tools: check_url(), parse_log_file(), format_incident_report()
# Wire to Claude claude-sonnet-4-6 with tool_use
# Watch the ReAct loop: observe → think → act → observe again
```
**Interview questions:**
- "What is the ReAct pattern and how does it differ from a simple LLM call?"
- "You want to build an AI agent that can triage Kubernetes alerts. What tools does it need and what are the failure modes?"
- "What is the difference between CrewAI and AutoGen for multi-agent systems?"
- "A multi-agent system is producing inconsistent results. How do you debug it?"
**What good looks like:** Sees agents as distributed systems — race conditions, inconsistent state, retry storms, cost runaway are all real problems. Applies SRE thinking: SLOs on agent task completion, circuit breakers on tool calls, observability on every step.
**T-Mobile STAR anchor:** "I already built a leadership chat agent on our notification platform. What I'm adding is the multi-agent orchestration layer — having multiple agents collaborate on incident triage, escalation, and runbook execution."

---

### Day 3: MCP — Model Context Protocol
**Vocabulary:** MCP, Model Context Protocol, MCP server, MCP client, tool registration, resource, prompt template, stdio transport, HTTP+SSE transport, Claude Desktop, MCP host, tool schema (JSON Schema), capability negotiation
**Lab:** Build a simple MCP server in Python that exposes two tools: `get_k8s_pod_status(namespace, pod_name)` and `get_recent_alerts(service_name, hours)`. Connect it to Claude Desktop and test it.
```python
# pip install mcp
# Implement: FastMCP server with two tools
# Test: Claude Desktop calls your tools during a conversation
```
**Interview questions:**
- "What is MCP and why did Anthropic create it instead of just using function calling?"
- "How is MCP different from LangChain tools?"
- "You want Claude to be able to query your internal monitoring system. Walk through how you'd build an MCP server for that."
- "What are the security considerations of giving an AI agent access to your production Kubernetes cluster via MCP?"
**What good looks like:** Understands MCP as a standardization layer — like how REST standardized APIs, MCP standardizes how AI models access tools. Thinks about security first: what can the agent do, what can it NOT do, how do you audit it.

---

### Day 4: AI Observability — Tracing, Evaluation, Cost Monitoring
**Vocabulary:** LangSmith, Langfuse, Arize Phoenix, OpenTelemetry for LLMs, trace, span, LLM span attributes, token usage per trace, latency percentiles, hallucination detection, RAGAS, faithfulness, answer relevancy, context precision, context recall, LLM-as-judge, cost per query, prompt version tracking, A/B testing prompts
**Lab:** Add Langfuse tracing to the RAG pipeline from Week 9 weekend lab; instrument: latency, token count, cost, retrieval quality score
```python
from langfuse import Langfuse
# Trace every LLM call + retrieval step
# Dashboard: p50/p95 latency, cost per query, quality scores
```
**Interview questions:**
- "How do you put an SLO on an AI system when the outputs are non-deterministic?"
- "What is RAGAS and how does it help you evaluate a RAG system in production?"
- "Your AI system's hallucination rate increased after a model upgrade. How do you detect and respond to this?"
- "How do you do A/B testing on prompts in production without disrupting users?"
**What good looks like:** Treats AI observability as an extension of MELT — the "T" (traces) now includes LLM call traces with token counts, latency, cost, and quality scores. Has an answer for "how do you know the AI is working correctly" that isn't "we read the outputs manually."
**Analogy:** AI observability is like APM for your application — except instead of just measuring latency and errors, you're also measuring answer quality. Langfuse is your AppDynamics for the AI layer.

---

### Day 5: AI Safety, Guardrails, Responsible AI
**Vocabulary:** prompt injection, jailbreak, indirect prompt injection, output filtering, Guardrails AI, NeMo Guardrails, AWS Bedrock Guardrails, Azure AI Content Safety, PII detection, PII redaction, presidio, data privacy for LLMs, model card, responsible AI, fairness, bias detection, AI governance, acceptable use policy
**Lab:** Add AWS Bedrock Guardrails to the RAG pipeline; configure PII redaction + topic denial; test with adversarial prompts
```bash
aws bedrock create-guardrail --name "sre-rag-guardrail" \
  --sensitive-information-policy-config '{"piiEntitiesConfig": [{"type": "EMAIL", "action": "ANONYMIZE"}]}'
```
**Interview questions:**
- "What is prompt injection and how is it different from SQL injection? How do you defend against it?"
- "A user asks your internal AI assistant to ignore its instructions and reveal system prompts. What prevents this?"
- "Your company is deploying an LLM that processes customer PII. What guardrails do you put in place before go-live?"
- "How do you build an acceptable use policy for an internal AI tool used by 500 engineers?"
**What good looks like:** Treats AI safety as a systems security problem — threat modeling, defense in depth, audit trails. Does not treat it as an ethics exercise — treats it as an operational risk with real business consequences (data breach, compliance violation, reputational damage).

---

### Weekend Lab: Multi-Agent SRE Assistant on AWS EKS + Bedrock
**Goal:** Deploy a multi-agent system that can triage Kubernetes alerts, query a knowledge base, and produce structured incident reports
**Architecture:**
- Orchestrator agent (Claude via Bedrock) receives alert
- Tool 1: query Bedrock Knowledge Base for relevant runbook
- Tool 2: call kubectl (via MCP server) to get pod/node status
- Tool 3: format and output structured incident report
- Langfuse tracing on every agent step
**Resources:** EKS cluster (existing from Week 3), Bedrock ($0.10–0.50), Langfuse (free tier)
**Teardown:** Delete EKS cluster; Bedrock and Langfuse have no ongoing cost

---

## Section 4: Updated Certification Roadmap

| Cert | Issuer | When in Program | Cost | Why Added/Kept |
|---|---|---|---|---|
| Terraform Associate | HashiCorp | After Week 1 | $70 | Table stakes for IaC roles; fast to get |
| CKA (Kubernetes Administrator) | CNCF | After Week 3 | $395 | Required for most Director K8s conversations; killer.sh practice |
| AWS SAA-C03 | AWS | After Week 4 | $300 | Validates AWS depth claimed in resume |
| AWS Security Specialty | AWS | After Week 8 | $300 | Differentiator for DevSecOps Director roles |
| CKS (Kubernetes Security) | CNCF | After Week 8 | $395 | Pairs with CKA; signals deep K8s security |
| AWS AI Practitioner | AWS | After Week 9 | $100 | NEW — validates AI Engineering track; fast exam |
| Google Cloud Professional ML Engineer | Google | Optional, Phase 2 | $200 | Useful if targeting Google or GCP-heavy companies |
| CISSP (Certified Info Systems Security Prof) | ISC2 | Optional, Phase 2 | $699 | Opens CISO-adjacent conversations at VP level |

**Priority order:** Terraform Associate → CKA → AWS SAA → AWS AI Practitioner → AWS Security Specialty → CKS

---

## Section 5: Soft Skills / Leadership Module

One 30-minute session per Sunday ritual (rotating topics across the 10 weeks):

| Week | Sunday Leadership Topic | Format | Goal |
|---|---|---|---|
| 1 | Director vs. IC mindset shift — how your answer changes when you have a title | Self-reflection + Claude roleplay | Can articulate the mindset shift in 2 sentences |
| 2 | Executive communication — 30-second status update to a CTO during an incident | Timed drill with Claude | Can deliver a crisp exec update without technical jargon |
| 3 | Org design 101 — embedded vs. centralized SRE, when to use each | Read Team Topologies Chapter 5 + discuss with Claude | Can answer "how would you structure SRE at a 200-person company?" |
| 4 | Hiring for SRE — what do you look for that resumes don't show? | Draft your hiring philosophy | Have a 2-minute answer to "how do you hire?" |
| 5 | Budget and business case — justify SRE team cost to a CFO | Write a 1-page business case with Claude | Can translate reliability risk into dollars |
| 6 | Influence without authority — how you got alignment on a hard decision | STAR story draft | One polished influence story ready for interviews |
| 7 | Conflict and tradeoffs — when product wants to ship and error budget says no | Roleplay with Claude as VP of Product | Can hold the line with data, not emotion |
| 8 | Leadership philosophy statement — your 2-minute answer to "what's your philosophy on SRE?" | Draft + refine with Claude | Sounds like you, not like the Google SRE book |
| 9 | AI strategy for a non-AI company — how do you bring AI into an SRE org that has none? | Design a 90-day AI adoption plan | Can answer "how would you introduce AI tooling to my team?" |
| 10 | Negotiation — how to negotiate a Director offer including title, equity, premium processing | Roleplay offer negotiation with Claude | Have a script ready for the real negotiation |

---

## Section 6: Updated 10-Week Master Table

| Week | Sprint Name | Primary Domain | Secondary Domain | Lab Environment | Cert Prep | Job Search Action |
|---|---|---|---|---|---|---|
| 1 | Terraform Foundation | IaC — state, modules, apply | FinOps basics, cost tagging | AWS S3 + DynamoDB + Infracost | Terraform Associate | Save 5 Director/VP JDs; run h1bdata.info on 3 companies |
| 2 | Supply Chain Security | SBOM, OPA, SAST, SLSA | Compliance-as-code | GitHub Actions + Trivy + Cosign | — | Research Phase 1 companies on Crunchbase/Wellfound |
| 3 | Kubernetes Internals | Control plane, RBAC, webhooks, Karpenter | Multi-tenancy patterns | EKS (create + destroy each session) | CKA study begins | Submit 1 Phase 1 application; run vetting checklist |
| 4 | AWS Depth + GitOps | IRSA, Organizations, SCPs | ArgoCD ApplicationSet | EKS + IAM + ArgoCD | AWS SAA study begins | Submit 2 Phase 1 applications |
| 5 | Observability Translation | OTel, MELT, burn rate, SPACE | FinOps for observability | AWS CloudWatch + ADOT + Prometheus | — | 3 total applications submitted; 1 recruiter screen expected |
| 6 | Portfolio + Leadership | 3 capstone projects with Director narrative | Executive presentation prep | GitHub public repos | — | First calibration application to Phase 2 company |
| 7 | Interview Readiness | Mock interviews, STAR stories, leadership questions | Director loop prep | No lab — interview practice only | Terraform Associate exam | 5 total applications; adjust targeting based on feedback |
| 8 | Polish + Active Search | LinkedIn, certs, resume variants | Phase 1 search activation | — | AWS Security Specialty begins | 8 total applications; at least 1 in loop interview |
| 9 | AI Engineering Foundations | LLM infra, RAG, Bedrock, Azure OpenAI | AI platform landscape | AWS Bedrock + Ollama local | AWS AI Practitioner | Continue active pipelines; AI story added to pitch |
| 10 | AI Platform Engineering | Agents, MCP, AI observability, guardrails | Multi-agent on EKS | EKS + Bedrock + Langfuse | — | Offers expected in active pipelines; negotiate |
