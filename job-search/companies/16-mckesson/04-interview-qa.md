# McKesson — Interview Q&A

Q: How does your telecom experience translate to healthcare compliance?
"The compliance framework I've built at T-Mobile — legally-required message classes, immutable audit trails, suppression governance with zero false positives, Vault-managed secrets, and vulnerability management programs — maps directly to HIPAA operational requirements. The specific regulations differ but the operational discipline is identical: every action is logged, every exception is reviewed, every system has documented ownership. The main HIPAA-specific gap I'd fill: learning the PHI data classification requirements and ensuring our observability tools don't inadvertently log PHI."

Q: How do you handle legacy system integration in a compliance context?
"Legacy systems in regulated environments are particularly challenging because they weren't designed with modern audit requirements. My approach: add a compliance wrapper layer — an intermediary service that handles logging, audit trail creation, and error handling before passing data to/from the legacy system. This isolates the compliance concerns from the legacy system's internals and lets you modernize incrementally. I did this at T-Mobile with TIBCO systems that needed compliance enhancement before migration."

QUESTIONS TO ASK: 1. What's the primary notification infrastructure at McKesson — pharmacy alerts, clinical notifications, or supply chain? 2. Is this role part of the core McKesson platform or a specific business unit?
