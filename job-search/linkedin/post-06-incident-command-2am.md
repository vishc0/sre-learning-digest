# Post 6: Incident Command at 2am

---

The Google SRE book will teach you about incident command structure. It will not teach you what to do when the incident commander is wrong and everyone on the bridge knows it.

I have run hundreds of incidents. The ones that went badly were almost never caused by the technical failure. They were caused by the room dynamics around the technical failure.

Here is what the book does not say:

The incident commander's most important job is not coordination. It is information triage. At 2am, with five engineers talking over each other on a bridge, the commander's job is to slow the conversation down, not speed it up. "Stop. What do we know for certain? What are we assuming?" Those two questions save more time than any runbook.

The second thing: separate the hypothesis from the fix. Engineers under pressure want to fix things. They will apply a change before they have confirmed a hypothesis, and now you have a new variable in a system that was already failing. "What would prove that theory before we touch anything?" is a sentence that should be said out loud in every incident.

The third thing — and this is the one nobody writes about: someone on that bridge is carrying the weight of a previous incident. They are pattern-matching to the last time something broke. Sometimes that instinct is right. Sometimes it sends the team down the wrong path for 45 minutes. The IC has to recognize that dynamic and name it.

Incident command is not a technical discipline. It is a communication discipline under pressure.

What is the hardest call you have had to make on an incident bridge?

#SRE #IncidentManagement #SiteReliability #EngineeringLeadership #Reliability #DevOps #OnCall
