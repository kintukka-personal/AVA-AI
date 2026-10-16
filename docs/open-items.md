# Open items

These are gaps between the live Copilot Studio config and what the agent is meant to do. Close an item by fixing it in Studio, updating the matching `config/` file, and logging the change in [`CHANGELOG.md`](../CHANGELOG.md).

Last reviewed: 2026-10-16 (after the live capture of all child agents, tools, and warnings).

## Open

| # | Priority | Item | Evidence | Suggested action |
|---|---|---|---|---|
| 1 | High | **Publishing may be blocked by licensing.** Studio warns: "This agent uses premium features. You'll need an upgraded license to publish it." The agent was last published 8/6/2026, so any fix below stays in Draft until this is cleared. | Agent status warning ([screenshot](../screenshots/2026-10-16/agent-status.png)) | Open *Go premium* to see which feature triggers it, then raise it with the Copilot licensing owner (Trent Walsh covered credits and governance in Jul 2026). |
| 2 | High | **AVA's own knowledge has no PG or QRC library.** The live list has no `D365 Procedure Guides` or `D365 Quick Reference Cards` source; the Aug 2026 design doc did. PGs 30–34 are scoped to FIN only. AVA's CASE 1 (direct PG answer) therefore relies on the FD Decision Support Tool and Microsoft websites. | `config/ava/knowledge.md` vs design doc §3.2 | Re-add the PG and QRC libraries as Available to AVA. Then run `evaluations/AVA_eval.csv` (the PR and PO-receipt questions). |
| 3 | High | **WIA can't use the attachment tool it is told to use.** `Get work item attachment` is scoped to AVA, not WIA, so WIA's CASE D (attachment review) has no tool. `Get query results` (named in WIA's instructions, used by CASE G) isn't configured at all. | `config/ava/tools.md` | Change `Get work item attachment` to Available to WIA. Then either add `Get query results` to WIA or remove it from WIA's ADO CONTEXT line. |
| 4 | Medium | **No evaluation has ever been run** (Studio warning). | Agent status warning | Import the CSVs in `evaluations/` (one test set per agent) and run them. Log the scores here and in the changelog. |
| 5 | Medium | **MAP's named source isn't connected.** The instructions point to `D365 procurement subcategories-MainAccountMappings_11.03.2026.xlsx` and six of its sheets; only the PDF QRC is connected. | `config/child-agents/map.md` | Connect the workbook to MAP, or rewrite the APPROVED SOURCE MATERIALS section to match the QRC. |
| 6 | Medium | **TAM has no folder URL.** Its instructions say `Direct folder link: [D365 Templates]` (twice), with no URL behind it. The original draft had the full link. | `config/child-agents/tam.md` | Put the URL into both placeholders. TAM's instructions are well under 8,000 characters. |
| 7 | Low | **SIMMY leftovers.** SIMMY is switched off, but the agent and its `D365 Simulations` knowledge source still exist. | Agents and Knowledge tabs | Delete both if the test is finished. |
| 8 | Low | **Shared with everyone** (Studio warning). | Agent status warning | This is intended for an org-wide front door. Record the decision and accept the warning. |
| 9 | Low | Duplicate `D365 Financial Dimension Decision Support Tool.pdf` (one for FIN, one for AVA). | Knowledge tab | Keep AVA's copy only if AVA needs it directly. |
| 10 | Low | Locale mismatch: the instructions cite `learn.microsoft.com/en-au/dynamics365/`, but the knowledge source is `en-us`. | Instructions vs Knowledge | Use one locale. |
| 11 | Low | Topics tab not captured in full (Overview shows 3 topics, then "See all"). | `config/ava/topics.md` | Paste the Topics tab. |
| 12 | Info | Engagement dropped from 81% (Aug) to 29%, and sessions from 26 to 14 per 7 days. | Monitor snapshots | Check the Monitor tab for causes (usage limits, licensing: only 22 of 295 D365 users had M365 Copilot as of Jun 2026). |

## Closed

| Date | Item | Resolution |
|---|---|---|
| 2026-10-16 | SIMMY changes not published / SIMMY missing from routing table / no SIMMY eval set | SIMMY was only a test and has been switched off. It is not part of AVA's design. |
| 2026-10-16 | 3 warnings not captured | Captured in `config/ava/overview.md`; now items 1, 4, 8. |
| 2026-10-16 | Tool list incomplete | Captured all 5 tools (`config/ava/tools.md`); the gap is now item 3. |
| 2026-10-16 | Child-agent instructions not a live capture | FIN, MAP, TAM, and WIA captured live; they match the Jun 2026 rewrite word for word. |
