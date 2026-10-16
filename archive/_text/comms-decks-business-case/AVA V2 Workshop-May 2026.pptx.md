> Text extracted from `comms-decks-business-case/AVA V2 Workshop-May 2026.pptx` for search/diff only.

```text
--- slide 1
EXECUTIVE WORKSHOP
AVA V2
Centralized D365 Finance support
Today's discussion
01
Proposed design
02
Operating model
03
Benefits
04
Next steps
Proposed future-state model
--- slide 2
EXECUTIVE SUMMARY
Speed vs. capability — and why it matters now
SHAREPOINT COPILOT
Quick, lightweight Q&A
Fast to deploy and great for basic page- or site-level question-answering. Limited to information delivery — no logic, tools, or actions.
COPILOT STUDIO
Scalable, governed, extensible
Purpose-built for enterprise. Adds tools, flows, analytics, and multi-agent orchestration that SharePoint cannot deliver alone.
Bottom line: SharePoint agents inform. Studio agents act, govern, and scale.
--- slide 3
CAPABILITY COMPARISON
Side by side
Dimension | SharePoint Copilot | Copilot Studio
Creation & setup | Fast, low-config UI | Deliberate, instruction + flow build
Knowledge & grounding | SharePoint pages only | SharePoint, OneDrive, APIs, connectors
Tools & automation | No Power Automate, no actions | Flows, business actions, structured input
Conversation control | Minimal system prompt; no logic | Full prompt control + multi-step logic
Analytics & governance | Basic usage stats | Custom metrics + exec reporting
Scale & architecture | Single-agent only | Parent / child agent ecosystem
--- slide 4
THE INFLECTION POINT
Information vs. action
If the agent needs to do something — submit, generate, route, log, escalate — SharePoint hits a wall immediately.
SHAREPOINT — what's missing
✕
No Power Automate flows
✕
No business actions (ADO, D365, Forms)
✕
No structured input or validations
STUDIO — what's possible
✓
Triggers Power Automate flows natively
✓
Acts on D365, ADO, Forms, Excel, CSVs
✓
Loops, dropdowns, validated user input
--- slide 5
Why we are proposing this model
The case for a centralized, governed Finance AI model
↗
Growing demand
Increasing interest across Finance in stream-specific AI agents
⚠
Fragmentation risk
Disconnected, one-off bots being built in isolation
◆
Need to scale
A scalable, governed, and reusable model is required
◉
Single front door + back-end
Use AVA as the unified entry point for D365 Finance support and creates standardization across all critical components
One model that scales properly across Finance — instead of fragmented bots in isolation.
[NOTES] Growing demand + need to scale

However, with this push there is an evergrowing risk of fragmentation. Which isn’t a concern now, but is guaranteed to be in the future

Following the AI newsletter there are great tools being created. EXCEPT all of these are in isolation. There is no brand. No vision but a holistic experience. And these tools are using different AI models, custom APIs, customer workflows, and all require different levels of security approvals, licenses, and access

This model ensure we never will face any of those roadblocks via AVA
--- slide 6
Why AVA is the right starting point
Existing credibility, governance, and adoption
Today's foundation
Governed documentation assistant already in production
Approved PG and QRC retrieval for D365 users
Strong existing foundation for Finance-wide expansion
Existing traction
86
unique users
1,000+
unique conversations on track in next 1–2 months
The front-door concept is stronger because AVA is already trusted and adopted.
28 // 233 // 1.7%
--- slide 7
AVA V2 — target model
High-level architecture
Microsoft Teams  •  user interface
AVA
PARENT AGENT
Centralised D365 Finance entry point
Documentation retrieval
Triage and routing
O2C
child agent
P2P
child agent
R2R
child agent
TAX
child agent
P2A
child agent
REP
child agent
KNOWLEDGE SOURCES
Shared Drive
Microsoft Resources
SME Inputs
AVA remains the front door — child agents hold deeper expertise by stream.
--- slide 8
How AVA V2 would work
Operating model — single entry, intelligent routing
User
Enters through AVA in Teams / SharePoint / 365
AVA assesses
Understands intent and decides path based on child specialization
Answer directly
From approved documentation
Route to child agent
Stream-specific deep expertise
Redirect safely
If query is unsupported
Child agent
Handles deeper stream expertise
Routing principle
AVA answers broad/general documentation questions directly. 
It routes early when deeper domain expertise is required — keeping the user experience seamless across one front door.
--- slide 9
Why this model is better
Benefits of the parent–child approach
◉
Single entry point
One front door for all D365 Finance support
✦
Better discoverability
Users don't need to choose the right bot first
◆
Specialist depth
Child agents go deep within their stream
↗
Scalability
Add new agents without redesigning the model
◈
Governance
Clear ownership, source control, and consistency
◐
Change management
One ecosystem for rollout, training, and comms
A better long-term model than separate agents across different tools and teams.
--- slide 10
Why Copilot / Microsoft
Platform rationale — operating model and governance, not just technology
Core apps already in Microsoft
D365
Teams
SharePoint
M365
Outlook
AVA V2 lives where Finance already works.
1
Natural integration path
Builds on existing connections across Microsoft apps
2
Avoids parallel tooling
No unnecessary custom setup or duplicate platforms
3
Enterprise-grade by default
Security, DPA, access controls, authentication, logging
4
Easier user adoption
Delivered through Teams — already part of daily routine
This is as much an operating model and governance decision as it is a technology decision.
ADO
--- slide 11
Workshop decisions and next steps
What we need to align on today
01
Endorsement on AVA + parent-child approach
DECISION
02
Agree the first-priority child agent / use case
DECISION
03
Align on source and content expectations by stream
ALIGNMENT
04
Confirm ownership and governance model
DECISION
05
Agree next steps for testing, design, and rollout
NEXT STEPS
Goal: leave with aligned direction and an agreed next step — not solve everything today.
--- slide 12
The child agent deployment process
Initial process estimate
9 phases
27 steps
BUT, we can introduce a structured Microsoft forms for BPOs / SMEs to fill out
4 phases
14 steps
THEN, track and manage via ADO
Forms = tickets
Review weekly via ticket dashboard
--- slide 13
The child agent deployment process
Initial process estimate
9 phases
27 steps
BUT, we can introduce a structured Microsoft forms for BPOs / SMEs to fill out
4 phases
14 steps
THEN, track and manage via ADO
Forms = tickets
Review weekly via ticket dashboard
--- slide 14
--- slide 15
Agent flow components (things you won’t need to know if we leverage the AVA setup)
Triggers
Flow
Manual
Scheduled 
Event-based
Connector Actions
Microsoft connectors
Custom connectors
Inputs / Outputs
AI Actions
Invoke
JSON / schema-based
extraction, classification, etc.
Actions
Strings
Objects
Arrays
Booleans
Variables
String
Integer
Float
Boolean
Array
Object (JSON)
Variable actions
Initialize variable
Set variable
Increment / decrement
Append to array
Compose
Control logic (Flow branching & structure)
Conditional logic
Iteration
Error / scope handling
Expressions & data operations
concat, substring, replace
utcNow, addDays
JSON Access 
Parse JSON
Human-in-the-loop (Agent flows only)
Connections & run context
Outputs back to the agent 
(Tool contract)
Output patterns (simple / structured)
Packaging & lifecycle
--- slide 16
Child agent development roadmap
Indicative phases — to be confirmed once first-priority use case is agreed
1
PHASE 1
Workshop & decision
Agree front-door model, first-priority child agent, and governance.
● TODAY
2
PHASE 2
Use case scoping
Define scope, sources, and SMEs for the first-priority child agent/s.
○ TBC
3
PHASE 3
Design & build
Design parent–child routing logic and build the first child agent.
○ TBC
4
PHASE 4
Pilot & test
Limited rollout with target users; refine routing and content.
○ TBC
5
PHASE 5
Rollout & adoption
Wider release with training, comms, and feedback loops.
○ TBC
6
PHASE 6
Scale to next streams
Add subsequent child agents using the proven model.
○ TBC
WE ARE HERE
Phases 2–6 to be confirmed once the first-priority child agent and ownership are agreed.
--- slide 17
19-MAY
Note: this was actually me testing the Microsoft learn capability
```
