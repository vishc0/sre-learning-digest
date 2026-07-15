# STAR Story 05: Error Budget Policy — Holding the Line Against Product
## Domain: SLO Governance / Stakeholder Management

---

## Situation

Six months after I established a formal SLO framework and error budget policy for the notification platform, we hit the real test. The error budget policy I had written — signed off at the VP level — stated that when monthly error budget was more than 50% consumed, new feature deployments required SRE sign-off. When 100% was consumed, all non-critical deployments were blocked until the next calendar month's budget reset. We had spent four months without triggering either condition. Then in month five, a cascading issue during a Cassandra compaction window consumed 78% of our monthly error budget in 72 hours. Three days later, the product team wanted to ship a major notification template redesign that had been in development for 8 weeks.

## Task

My task was to enforce the error budget policy as written, communicate the decision clearly to product and business stakeholders, and do it in a way that preserved the relationship and the credibility of the policy — because a policy that gets waived the first time it's inconvenient is not a policy. Simultaneously, I had to explain to my team why we were enforcing it, because one engineer argued internally that the Cassandra event was "infrastructure's fault" and shouldn't count against the product team's deployment window.

## Action (IC Technical Depth)

The first conversation was internal — with my own team. The engineer who argued the Cassandra event "shouldn't count" was making a politically understandable but technically incorrect argument. Error budget tracks customer-experienced unavailability, not the organizational source of it. A customer who couldn't receive a fraud alert during that 72-hour window didn't care whether the root cause was a Cassandra compaction bug or a bad deployment. The budget measures customer trust, not blame assignment. I ran a 30-minute team discussion on this, let everyone argue, and then made the call: the event counts, the policy applies.

The second conversation was with the product director. I requested a meeting rather than sending a rejection email — the face-to-face framing matters. I came with three things: the policy document (their VP had signed it), the SLI data from the Cassandra event (error rates, customer-impacting duration, quantified impact), and an alternate deployment timeline — I wasn't saying "no forever," I was saying "not this week, and here's when."

I proposed the following: the notification template redesign would deploy on day 3 of the next calendar month, after error budget reset. I also offered a partial release — read-only preview of new templates in a non-production environment accessible to their QA team during the wait, so the 8-week development effort didn't feel frozen. And I committed to a post-incident review with product present to walk through what happened with Cassandra and what we were doing to prevent recurrence — making them a partner in reliability rather than a recipient of restrictions.

The product director's initial reaction was frustration. She said: "We've been building this for 8 weeks and now you're blocking us because of an infrastructure problem we didn't cause." I acknowledged that directly: "I understand the frustration, and you're right that your team didn't cause this. But the policy is designed around customer experience, not internal accountability. If we waive it the first time it's inconvenient, it's not a policy anymore — it's a suggestion. Your VP signed this policy specifically so we'd have a shared framework for this exact conversation."

She agreed. The deployment held.

Then, one month later, the same product director proactively asked me whether the error budget was healthy before scheduling their next major release. The policy had become part of her planning process.

## Result

Policy enforced without exception — the notification template redesign deployed on schedule in the following month's error budget window. Zero Sev1 incidents in that deployment. The product director became an advocate for SLO governance: she presented the error budget framework at a product leadership quarterly as a model for release decision-making. I was asked to extend the SLO framework to two additional platform teams. The policy was subsequently cited in a T-Mobile engineering blog post (internal) as a case study in SRE/product collaboration.

On the internal team side: the conversation about why the Cassandra event counted became a foundational moment for the team's understanding of SLO philosophy. Several engineers later cited it as the point where they stopped thinking about error budgets as "an SRE metric" and started thinking about it as "a customer trust metric."

---

## Director/VP Version (Leadership Framing)

"SLO governance only works if the policy has teeth the first time it matters. When we hit our first real error budget enforcement — blocking an 8-week product effort — I enforced it exactly as written, but I did it in a way that built a partnership rather than a conflict. I gave the product director a clear rationale anchored in customer experience, not blame. I offered an alternate timeline and a partial release option so the block wasn't punitive. Six months later, she was presenting the error budget framework to product leadership as a model. That's the outcome I was aiming for: not just compliance, but ownership. When product teams internalize the SLO philosophy, SRE doesn't have to be the policy enforcer anymore."

## IC Version (Technical Depth)

"The internal debate about whether the Cassandra event should 'count' was a teaching moment I didn't want to miss. Error budget measures customer-experienced unavailability — the unit is customer minutes affected, not root cause category. If you start discounting budget consumption based on organizational blame, you corrupt the measurement. I held a 30-minute team discussion, let the argument play out, then made the call clearly. That conversation shaped how the team reasons about SLOs more than any document I've written. On the product side, the key move was coming with an alternate timeline, not just a rejection. 'No' with no path forward creates adversaries. 'No this week, here's when and here's why' is a partnership conversation."

---

## 30-Second Version

"We consumed 78% of monthly error budget during a Cassandra incident. Three days later, product wanted to ship. I enforced the policy as written — no exceptions — but I came to that conversation with an alternate timeline and a partial release option. The product director was frustrated initially but agreed. Six months later she was presenting the error budget framework to product leadership as a model. The policy worked because I enforced it the first time it was inconvenient."

---

## 2-Minute Version

"We'd had the error budget policy in place for five months without triggering it. Then a Cassandra compaction issue consumed 78% of our monthly budget in 72 hours. Three days later, product wanted to ship a major release they'd been building for 8 weeks.

The first challenge was internal. One of my engineers argued the Cassandra event 'shouldn't count' because it wasn't the product team's fault. I stopped that argument clearly: error budget measures customer-experienced unavailability, not organizational blame. The customer who didn't get a fraud alert doesn't care about our internal root cause categories. If we discount budget consumption based on blame, we corrupt the measurement. Policy applies. The event counts.

The product conversation was harder emotionally but simpler structurally. I didn't send an email — I requested a meeting. I came with three things: the signed policy document, the SLI data quantifying customer impact, and an alternate deployment timeline. I wasn't saying no forever. I was saying 'not this week, and here's when.'

The director's first response was 'we've been building this for 8 weeks and you're blocking us for an infrastructure problem we didn't cause.' I acknowledged that directly, then reframed: the policy exists specifically for this moment. If we waive it because it's inconvenient, it becomes a suggestion, not a policy. Her VP signed it for this exact reason.

She agreed. The deployment held. One month later she called me before scheduling their next release to ask if the error budget was healthy. The policy had become part of her planning workflow. A year later she presented the error budget framework at a product leadership quarterly as a model for release governance. The enforcement created a partner, not an adversary — because I came prepared to explain, not just to say no."

---

## Key Metrics to Remember
- Error budget consumed: 78% in 72 hours from Cassandra compaction event
- Policy trigger: 50% consumed = SRE sign-off required; 100% = deployments blocked
- Time held: blocked 8-week development effort from shipping for ~1 month
- Outcome: zero exceptions granted, zero Sev1 in subsequent deployment
- Long-term: product director became SLO advocate, presented framework at QPR
- Policy extended to 2 additional platform teams following this incident
- Internal: team conversation on error budget = customer trust metric (not blame metric)
