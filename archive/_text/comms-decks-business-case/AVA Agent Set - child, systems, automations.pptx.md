> Text extracted from `comms-decks-business-case/AVA Agent Set - child, systems, automations.pptx` for search/diff only.

```text
--- slide 1
--- slide 2
SK SOFT SPECIALIST BOT
CONFIG BOT
--- slide 3
--- slide 4
--- slide 5
--- slide 6
[NOTES] Each Finance stream can create a child agent by defining its use case, approved sources, ownership, guardrails, and testing path, then connecting it into AVA as the centralized front door for routing and access.
--- slide 7
P2P CHILD AGENT
Option 1: PAT
"PAT" has a very reliable, supportive ring to it.
Procurement Advisory Tool (Clean, corporate, and accurate to its function of suggesting codes.)
Purchasing Assistance Terminal (Sounds a bit more like a specific destination for help.)
Procurement Action Tracker (Good if the agent also helps users follow up on where their requisitions are.)
Option 2: PAL
"PAL" is inherently friendly and implies a partnership, which is perfect for an agent that acts as a guide.
Procurement Assistant Liaison (A liaison bridges the gap between the user and the complex P2P process.)
Procure-to-Pay Automated Librarian (A clever nod to the fact that it helps users find specific D365 documentation and files.)
Purchasing Advisory Locator (Highlights its ability to pinpoint the right codes and documents.)
Bonus "P" Names
If you want to look at just a few more options that match the AVA style:
PAM: Procurement Assistance Module
PEG: Purchasing Expert Guide (Directly references its status as a "procurement expert.")
PIP: Procurement Information Portal
--- slide 8
O2C CHILD AGENT
Option 1: ACE
ACE (Atlas Customer Expert) works well because it sounds:
confident 
capable 
customer-facing 
easy to remember 
like a real name/acronym, not just an abbreviation 
It also has a nice positioning difference from AVA:
AVA = guidance / retrieval / documentation 
ACE = customer / process / integration expertise 
That pairing feels intentional.
What’s especially good about ACE
“Ace” is already a word with positive meaning — expert, top performer, trusted 
It fits an agent with deep knowledge 
It sounds more capable than “assistant” without being too technical 
It works well for something that knows: 
processes 
custom integrations 
evolving knowledge
--- slide 9
ACE
Option 1: ACE
ACE (Atlas Customer Expert) works well because it sounds:
confident 
capable 
customer-facing 
easy to remember 
like a real name/acronym, not just an abbreviation 
It also has a nice positioning difference from AVA:
AVA = guidance / retrieval / documentation 
ACE = customer / process / integration expertise 
That pairing feels intentional.
What’s especially good about ACE
“Ace” is already a word with positive meaning — expert, top performer, trusted 
It fits an agent with deep knowledge 
It sounds more capable than “assistant” without being too technical 
It works well for something that knows: 
processes 
custom integrations 
evolving knowledge
--- slide 10
CoPilot Studio Tools
How to Combine These for PAT
Prompt: Handles all user Q&A, step extraction, and document guidance.
Agent Flow: Automates “Create PR”, “Submit invoice”, “Lookup code”, etc.
SharePoint/Excel Connectors: Pulls real-time data for codes, docs, and reference tables.
Teams Connector: Sends notifications or escalates when needed.
Human in the Loop: For exceptions or approvals.

1. Prompt
Purpose:Use this for all natural language understanding, document Q&A, and step-by-step guidance.Why:This is the core of PAT’s “knowledge worker” capability — answering questions, extracting steps from PGs/QRCs, and providing code/dimension guidance.

2. Agent Flow
Purpose:Automate predictable, repeatable procurement tasks (e.g., “Create PR”, “Submit invoice”, “Lookup code”).
Why:Lets PAT execute multi-step actions or trigger workflows (like sending a Teams notification, updating a SharePoint list, or logging a request).

3. SharePoint Connector
Purpose:Access and retrieve the latest WiseTech Global procurement documentation, code lists, and reference tables.
Why:Ensures PAT always pulls from the most current, official sources.

4. Excel Online (Business) Connector
Purpose:Lookup, validate, or suggest P2P codes and financial dimensions from a maintained Excel reference file.
Why:Many orgs keep code lists in Excel; this makes code lookup and validation easy and auditable.

5. Microsoft Teams Connector (optional, but powerful)
Purpose:Notify users, escalate queries, or send workflow updates directly in Teams.
Why:Keeps procurement comms in the flow of work.

6. Human in the Loop (optional)
Purpose:Route complex or ambiguous queries to a real procurement expert for review.
Why:Ensures compliance and user trust for edge cases.

--- slide 11
```
