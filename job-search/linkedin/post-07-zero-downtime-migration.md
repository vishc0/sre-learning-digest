# Post 7: Zero-Downtime Migrations

---

Six zero-downtime migrations. The one that almost was not.

The first five went smoothly enough that the team started calling us the "invisible migration" team. Database upgrades, message broker replacements, platform lifts — customers never knew. We had a pattern: dual-write, validate parity, shift traffic incrementally, decommission old path.

The sixth one was a Cassandra migration. Same pattern. We had done it before on smaller clusters.

What we had not done before was migrate 18 months of notification history under active write load while a marketing campaign was generating four times normal traffic — which we found out about 6 hours before the migration window.

The temptation was to go anyway. The pattern worked. The team was confident. The business stakeholder was in the room asking if we could proceed.

We delayed 48 hours.

Not because the technical plan was wrong. Because the blast radius of a failure during a peak traffic event, with customers actively receiving campaign notifications, was not acceptable. The migration plan was built for normal load. We were not at normal load.

That decision cost one engineering sprint cycle in downstream dependencies. It cost zero customers and zero revenue.

The Director-level framing: the most important variable in any migration is not the technical complexity — it is the business context around the window. Knowing when NOT to execute a plan you are confident in is a senior leadership skill, not a failure of nerve.

What context check does your team do before every major change window?

#SRE #Migrations #ZeroDowntime #EngineeringLeadership #Reliability #PlatformEngineering #ChangeManagement
