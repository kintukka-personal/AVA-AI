# Open items

These are gaps between the live Copilot Studio config and what the agent is meant to do. Close an item by fixing it in Studio, updating the matching `config/` file, and logging the change in [`CHANGELOG.md`](../CHANGELOG.md).

Last reviewed: 2026-10-16 (after the live capture of all child agents, tools, and warnings).

## Open

| # | Priority | Item | Evidence | Suggested action |
|---|---|---|---|---|
| 1 | High | **Publishing may be blocked by licensing.** Studio warns: "This agent uses premium features. You'll need an upgraded license to publish it." The agent was last published 8/6/2026, so any fix below stays in Draft until this is cleared. | Agent status warning ([screenshot](../screenshots/2026-10-16/agent-status.png)) | Open *Go premium* to see which feature triggers it, then raise it with the Copilot licensing owner (Trent Walsh covered credits and governance in Jul 2026). |
| 2 | High | **Where do the PG and QRC libraries live?** The Knowledge tab captured on 2026-10-16 doesn't list `D365 Procedure Guides` or `D365 Quick Reference Cards`. Yet analytics show them as AVA's most-used sources: 420 and 65 questions over 180 days, and 167 and 20 over the last 90. The full 20-source usage list is exactly the 18 Knowledge-tab sources plus these two, so they are still active. They sit somewhere the Knowledge tab doesn't list, most likely a generative-answers node inside a topic such as Conversational boosting. | `config/ava/knowledge.md` vs [`docs/analytics.md`](analytics.md) | Open the Conversational boosting topic (and any other topic with a generative-answers node), check its data sources, and record where both libraries are configured in `config/ava/knowledge.md`. |
| 3 | High | **WIA can't use the attachment tool it is told to use.** `Get work item attachment` is scoped to AVA, not WIA, so WIA's CASE D (attachment review) has no tool. `Get query results` (named in WIA's instructions, used by CASE G) isn't configured at all. | `config/ava/tools.md`; WIA's call success rate is 36% over the last 90 days (22 calls), the lowest of the children ([`docs/analytics.md`](analytics.md)) | Change `Get work item attachment` to Available to WIA. Then either add `Get query results` to WIA or remove it from WIA's ADO CONTEXT line. |
| 4 | Medium | **No evaluation has ever been run** (Studio warning). | Agent status warning | Import the CSVs in `evaluations/` (one test set per agent) and run them. Log the scores here and in the changelog. |
| 5 | Medium | **MAP's named source isn't connected.** The instructions point to `D365 procurement subcategories-MainAccountMappings_11.03.2026.xlsx` and six of its sheets; only the PDF QRC is connected. | `config/child-agents/map.md` | Connect the workbook to MAP, or rewrite the APPROVED SOURCE MATERIALS section to match the QRC. |
| 6 | Medium | **TAM has no folder URL.** Its instructions say `Direct folder link: [D365 Templates]` (twice), with no URL behind it. The original draft had the full link. | `config/child-agents/tam.md` | Put the URL into both placeholders. TAM's instructions are well under 8,000 characters. |
| 7 | Low | **SIMMY leftovers.** SIMMY is switched off, but the agent and its `D365 Simulations` knowledge source still exist. | Agents and Knowledge tabs | Delete both if the test is finished. |
| 8 | Low | **Shared with everyone** (Studio warning). | Agent status warning | This is intended for an org-wide front door. Record the decision and accept the warning. |
| 9 | Low | Duplicate `D365 Financial Dimension Decision Support Tool.pdf` (one for FIN, one for AVA). | Knowledge tab | Keep AVA's copy only if AVA needs it directly. |
| 10 | Low | Locale mismatch: the instructions cite `learn.microsoft.com/en-au/dynamics365/`, but the knowledge source is `en-us`. | Instructions vs Knowledge | Use one locale. |
| 11 | Low | Topics tab not captured in full (Overview shows 3 topics, then "See all"). | `config/ava/topics.md` | Paste the Topics tab. |
| 12 | Info | Engagement dropped from 81% (Aug) to 29%, and sessions from 26 to 14 per 7 days. Over 180 days: 3,113 sessions, 18% engagement, 11 average daily users. | Monitor snapshots; [`docs/analytics.md`](analytics.md) | Check the Monitor tab for causes (usage limits, licensing: only 22 of 295 D365 users had M365 Copilot as of Jun 2026). |
| 13 | Info | Custom metric definitions not captured. The "Blocker Status" (41.6% blocked) and "Issue Resolution Outcome" metrics can't be interpreted without them. | [`docs/analytics.md`](analytics.md) | Paste each metric's definition from Activity › Custom metrics. |
| 14 | Info | MAP was called 19 times in the last 90 days, but its only knowledge source answered 1 question (0% good quality), and 2 over 180 days. FIN was called 17 times, yet 9 of its 11 sources answered nothing in 90 days. | [`docs/analytics.md`](analytics.md) | Relates to item 5 (MAP's named workbook isn't connected). Check whether child-agent knowledge use is attributed in this table before acting. |
| 15 | High | **Credits per session rose about 70-fold:** ≈ 1.8 (Apr–Jul) to ≈ 128 (Jul–Oct). The last 90 days used 45,087 of the 180-day 50,158 credits, from 353 of 3,113 sessions. | [`docs/analytics.md`](analytics.md) comparison section | Open Activity › Billing ("See billing") to see which feature drives consumption, such as the model (Claude Opus 4.6), child-agent calls, or tool calls. Cost governance was already a topic (Trent Walsh, Jul 2026). |

## Closed

| Date | Item | Resolution |
|---|---|---|
| 2026-10-16 | SIMMY changes not published / SIMMY missing from routing table / no SIMMY eval set | SIMMY was only a test and has been switched off. It is not part of AVA's design. |
| 2026-10-16 | 3 warnings not captured | Captured in `config/ava/overview.md`; now items 1, 4, 8. |
| 2026-10-16 | Tool list incomplete | Captured all 5 tools (`config/ava/tools.md`); the gap is now item 3. |
| 2026-10-16 | Child-agent instructions not a live capture | FIN, MAP, TAM, and WIA captured live; they match the Jun 2026 rewrite word for word. |
