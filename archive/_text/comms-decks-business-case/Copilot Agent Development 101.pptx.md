> Text extracted from `comms-decks-business-case/Copilot Agent Development 101.pptx` for search/diff only.

```text
--- slide 1
KNOWLEDGE TRANSFER SESSION
Copilot Agent
Development 101
Building agents with Copilot Studio
Daniel Moreira
Wednesday 22 July 2026   ·   Procurement Operations team
--- slide 2
What we'll cover today
A practical intro to building your own Copilot agents.
1
What an agent is
AVA as a live example
2
Cost & governance
How Copilot Credits work
3
How to build one
A Copilot Studio walkthrough
4
Your first use case
A Procurement child agent
5
Q&A & next steps
Where we go from here
OUR WORKED EXAMPLE
AVA
Atlas Virtual Assistant
The Finance team's own Copilot agent
--- slide 3
01
WHAT IS AN AGENT?
What is a Copilot agent?
A purpose-built AI assistant you create in Copilot Studio — working in natural language, grounded in the sources and rules you define. Beyond answering questions, agents can take on real work:
Answer questions
Self-service answers from your approved knowledge
Guide a process
Step-by-step help through tasks and fields
Take actions
Track, consolidate, organize, update records and lists etc. via connectors
Automate routine work
Cut repetitive manual tasks, extensive admind, and hand-offs
Route to a specialist
Send people to the right agent or team
Work inside Teams
Available where people already work
--- slide 4
01
WHAT IS AN AGENT? (A REAL EXAMPLE)
The Copilot agent example: AVA
AVA — the Atlas Virtual Assistant — is the Finance’s teams own Copilot agent: one “front door” in Microsoft Teams for D365 Finance support, which has the capability to connect to other specialist child agent.
AVA AT A GLANCE
Built in Copilot Studio
Lives in Microsoft Teams
Scoped to D365 Finance support
The central Finance AI “front door”
AVA ROUTES TO SPECIALIST CHILD AGENTS
ADO  ·  ADO ticket admin
MAP  ·  COA / GL / VAT mapping
Fin. Dimensions  ·  BU, cost centre
P2P  ·  Procure-to-pay
O2C  ·  Billing & integrations
R2R  ·  Record-to-report
TAX  ·  Tax & compliance
Reporting  ·  Analytics
Guardrails throughout: approved sources only · answers cite internal docs.
FIN  ·  Financial Dimensions, CC, BU, etc.
--- slide 5
02
COST & GOVERNANCE
How Copilot Credits work
Currently – all Copilot Credits sit in a shared tenant pool for WTG. Everything that uses billed credits draws from the same pool.
One shared pool
Its size depends on the licences the business holds across Copilot, Power Platform and 365.
Everything draws on it
Cowork and Power Platform agents both consume from the same tenant pool.
If the pool runs dry
Agents stop working — unless a billing plan adds pay-as-you-go overage (runs, but outside budget).
Reserve to protect
Allocate credits to an environment (e.g. Production) so the agent won't stop.
From the “Ava governance & costs” session — Trent Walsh, 13 Jul
--- slide 6
02
COST & GOVERNANCE
Build the agent, licence the users — and usage stops draining the pool
With a proper Copilot licence, agent usage (like AVA) doesn't draw from the tenant pool — effectively non-billed against the shared credits.
Cowork is different — it always will draw from the pool, even for licensed users.
So purpose-built agents + correct licensing protect the shared pool for everyone and minimizes cost.
Real Finance numbers — the drop came purely from correct licensing.
BILLED-CREDIT USAGE
~40,000
prior 60 days
~1,000
last 30 days
--- slide 7
03
HOW TO BUILD ONE
Building an agent in Copilot Studio
Copilot Studio is just the portal — underneath, your agent is a set of Dataverse objects. Four building blocks:
Instructions
Define the agent's persona, scope and rules.
Knowledge
Connect approved sources: Procedure Guides, Procurement Policy, Finance docs, etc.
Guardrails
e.g. Approved sources only, decline out-of-scope, cite the source.
Connectors
Add actions — e.g. SharePoint, Outlook, Teams, ADO (eventually D365) etc.
Same knowledge grounding AVA uses today — approved WTG guidance, and Microsoft resources.
--- slide 8
03
HOW TO BUILD ONE
Build it right: keep it out of the default environment
In best practice the default environment should be used. However, with the current setup at WTG use the default environment for early builds + testing only — fine to experiment, but not where a shared agent should live.
Dev
build & change
›
SIT
locked once moved
›
UAT
business test
›
Production
users see this
Package it in a solution
The objects move as one governed, versioned unit.
Allocate credits to Production
So the agent keeps working when the pool is tight.
Per Trent's governance session — AVA is being moved out of default and into this lifecycle now.
--- slide 9
04
YOUR FIRST USE CASE
Your turn: a Procurement child agent
The recipe — five things to define, then connect into AVA:
1
Use case  — the specific question or task
2
Approved sources  — the guidance it will rely on
3
Ownership  — who maintains it, where are items stored
4
Guardrails  — what it always follow & never do
5
Testing path  — Early Dev → Publish
So — what's your first use case?
PROCUREMENT AGENT
Nic has a use case he'd like to work through — let’s work through it together.
[NOTES] Forms feed SP > Requesterscentralise so agent can readi inbox, scan invoice and populate eharepoint page (record of request)
- Determine PO requirement
--- slide 10
Next steps & questions
NEXT STEPS
Pick a first Procurement use case (Nic's)
Define its sources, owner and guardrails
Build it in a solution — not the default environment
Test through Dev → UAT before go-live
Get everyone on the correct Copilot licence
WHO TO TALK TO
Daniel — agent design & build
Trent — environments, credits & governance
```
