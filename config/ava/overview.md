# AVA — Overview (live)

Captured 2026-10-16 from Copilot Studio. Screenshot: [`screenshots/2026-10-16/overview.png`](../../screenshots/2026-10-16/overview.png).

## Identity

| Field | Value |
|---|---|
| Name | AVA (Atlas Virtual Assistant) |
| Description (217/1024) | AVA is the central Finance AI entry point for D365-related support. It helps users quickly retrieve approved guidance, navigate to the right documentation, and route more specialized queries to the appropriate expert. |
| Environment | WiseTech Global Pty Ltd (default) — `Default-8b493985-e1b4-4b95-ade6-98acafdbdb01` |
| Bot ID | `dd76dbb0-6543-f111-88b3-7c1e526243e2` |
| Studio link | https://copilotstudio.microsoft.com/environments/Default-8b493985-e1b4-4b95-ade6-98acafdbdb01/bots/dd76dbb0-6543-f111-88b3-7c1e526243e2/overview |
| Owner | Daniel Moreira |
| Last published | 8/6/2026, 1:31 PM, by Daniel Moreira |
| Agent status | **3 Warnings**, listed below |

## Agent status warnings

Captured 2026-10-16 ([screenshot](../../screenshots/2026-10-16/agent-status.png)). All three are on the Draft.

| Severity | Message | Category | Action in Studio |
|---|---|---|---|
| Warning | No evaluation has been run on this agent. Run one to verify quality before publishing. | Quality | Evaluate agent |
| Warning | This agent uses premium features. You'll need an upgraded license to publish it. | Licensing | Go premium |
| Warning | This agent is shared with everyone in your organization, giving all users access to its content. | Access | Share settings |

## Model

| Setting | Value |
|---|---|
| Primary model | Claude Opus 4.6 |

## Capabilities

| Setting | Value |
|---|---|
| Web Search | Disabled |
| Triggers | None |
| Instructions | [`instructions.md`](instructions.md) |
| Knowledge | [`knowledge.md`](knowledge.md) |
| Tools | [`tools.md`](tools.md) |
| Child agents | FIN, MAP, TAM, WIA (SIMMY disabled) · [`../child-agents/`](../child-agents/README.md) |
| Topics | [`topics.md`](topics.md) |

## Suggested prompts (Teams / Microsoft 365)

| Title | Prompt |
|---|---|
| What is AVA? | How do I use AVA? |
| Get Started | I need help with a D365 Task. |
| Find a guide | Provide me with a link to where the Procedure guides are located. |

## Channels

Confirmed by Daniel Moreira, 2026-10-17.

| Channel | Status |
|---|---|
| Microsoft 365 | Live |
| Microsoft Teams | Live |
| SharePoint | Live |

Microsoft authentication limits AVA to these three channels. AVA is shared with the whole organisation.

## Monitor snapshot (last 7 days)

| Captured | Sessions | Reactions | Engagement |
|---|---|---|---|
| 2026-10-16 | 14 (↓33%) | 0 (—0%) | 29% (↑21%) |
| 2026-08-16 (design doc) | 26 (↓48%) | 0 | 81% (↓10%) |
