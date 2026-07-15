# Apple — Per-Role Index

**Research dates:** 2026-05-07 (initial 6 roles, then 3 additional from your hints + req-ID verification)
**Total Apple roles tracked:** 9 live Manager-level + 1 JMET note (no Manager req exists)
**Status of req IDs:** All 9 verified live on jobs.apple.com (the two prior 404s on Analytics + InfoSec were transient JS-render glitches, both resolve correctly now)

## Priority ranking (apply in this order)

| Rank | File | Role | Req ID | Location | Match % | Salary low end |
|------|------|------|--------|----------|---------|----------------|
| 🎯 **1** | [07](07_Messaging_SRE_Mgr_ASE.md) | **Messaging SRE Mgr — ASE** | `200592669` | Cupertino, CA | **96%** | ~$230K (band est.) |
| 2 | [04](04_SRE_Mgr_Analytics.md) | SRE Mgr, Analytics — ASE | `200592602` | Cupertino, CA | 90% | ~$200K+ (band est.) |
| 3 | [06](06_Mgr_SRE_InfoSec.md) | Mgr, SRE — Information Security | `200624759-3278` | Not retrieved | 89% | ~$200K+ (band est.) |
| 4 | [08](08_Mgr_SRE_ETS.md) | Manager, SRE — ETS | `200582129-1052` | Austin, TX (likely) | 88% | ~$200K (band est.) |
| 5 | [09](09_SRE_Mgr_Apple_Maps.md) | SRE Mgr, Apple Maps | `200651886-0836` | Cupertino, CA (likely) | 84% | ~$235K (band est.) |
| 6 | [02](02_SRE_Mgr_Compute_Seattle.md) | SRE Mgr — ASE Compute | `200602617` | Seattle, WA | 83% | ~$216K (band est.) |
| 7 | [03](03_SRE_Mgr_Data_Platform.md) | SRE Mgr, Apple Data Platform | `200646432-0321` | Cupertino, CA | 82% | ~$200K+ (borderline) |
| 8 | [05](05_EM_Cloud_Network_Reliability.md) | Engineering Mgr, Cloud Network Reliability | `200642210-3956` | Sunnyvale, CA | 78% | ~$208K (band est.) |
| 9 | [01](01_SRE_Mgr_Storage_ASE.md) | SRE Mgr, Storage — ASE | `200620738-0836` | Cupertino, CA | 76% | **$216,600 (verified)** |
| — | [10](10_JMET_note.md) | JMET — no Manager req live | — | — | n/a | n/a (IC `200096662` only) |

> **Note on scoring.** Initial absolute scores (in files 01–06) were calculated per-role in isolation. The ranking in this table uses the second agent's relative scoring across all 9 roles, which is more useful for prioritization. Where a file's stated score differs from this table (e.g., file 01 says 88%, table says 76%), the table is the *relative* prioritization signal; the file's score reflects the *absolute* match per the role's own JD. Use the table for "which to apply to first."

## Top 3 to attack this week

1. **Role 07 — Messaging SRE Manager ASE (96%)** — your stack twin. APNs / iMessage / FaceTime server reliability is the same notification-pipeline pattern you run at T-Mobile across Adobe AJO, MoEngage, DND, MAT at 25M msgs/day. Open the live JD, confirm the posted band, apply with the tailored materials in file 07. **This is the application most likely to convert.**
2. **Role 04 — SRE Mgr Analytics ASE (90%)** — your MART framework + Splunk MLTK production work is the exact AI/observability discipline this team needs. Take the Spark Structured Streaming course (30 days) before the loop to close the Hadoop/Spark gap.
3. **Role 06 — Mgr SRE InfoSec (89%)** — Vault + CyberArk + AWS + IaC is your exact stack; 18 months of zero critical vulns in production is your headline number.

## Critical caveat — verify salary on live JD before applying

Apple's `jobs.apple.com` JD pages are JavaScript-rendered and the automated fetch could not retrieve the CA/WA-mandated salary range from most pages. Only **Role 01 (Storage)** has a verified posted floor ($216,600). For all other roles, salary estimates are inferred from comparable Apple Manager / EM bands. **Open each live JD in a browser and confirm the posted base range before tailoring an application.**

## How to use these files

Each `0N_*.md` file in this folder contains:
1. JD link, requisition ID, location, posted salary
2. Match score and rationale
3. What matched (JD requirement → resume evidence)
4. Gaps and 30–90 day mitigation
5. **Tailored resume** for that specific role
6. **Tailored 30-second pitch + cover-letter opener** for that role
7. Pre-application checklist

## Roles considered but excluded

- IC-level SRE roles at Senior / Staff (not Manager / Principal level)
- Traffic Engineering Manager reqs `200636812` / `200624416` — Software Engineering Manager titles, network mesh specialist, 0 production traffic-mesh on resume
- DevOps EM Employee Experience req `200587252` — 404 (no longer available)
- Senior Manager Data SRE Ad Platforms req `200493584` — salary low end $183,400, below threshold
- AI Developer Tools EM Seattle req `200658219-3337` — function is AI tooling, not SRE/DevOps

## Caveat on JMET understanding

You asked for "JMET eBusiness Services" — Apple's JMET appears to actually stand for **Joint Manufacturing & Enterprise Technology** (internal IT / security platform team). No Manager-level req is live for JMET as of 2026-05-07. The closest live Manager-level enterprise-IT SRE role is **Role 08 — Manager SRE ETS (`200582129-1052`)**. If you're specifically targeting a Japan/Asia retail platform, that would not be JMET — happy to research that as a separate query if you confirm the team name.
