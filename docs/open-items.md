# Open items

These are gaps between the live Copilot Studio config (2026-10-16) and what the agent is meant to do. Close an item by fixing it in Studio, updating the matching `config/` file, and logging the change in [`CHANGELOG.md`](../CHANGELOG.md).

| # | Priority | Item | Evidence | Suggested action |
|---|---|---|---|---|
| 1 | High | **SIMMY changes are not live.** SIMMY and the `D365 Simulations` source were modified ~9 days ago, but the agent was last published 8/6/2026. Users get the published version. | Agents and Knowledge tabs vs "Published 8/6/2026" | Test SIMMY in the Test pane, then **Publish**. |
| 2 | High | **AVA's own knowledge has no PG or QRC library.** The live list has no `D365 Procedure Guides` or `D365 Quick Reference Cards` source; the Aug 2026 design doc did. PGs 30–34 are scoped to FIN only. AVA's CASE 1 (direct PG answer) therefore relies on the FD Decision Support Tool and Microsoft websites. | `config/ava/knowledge.md` vs design doc §3.2 | Check the full Knowledge list in Studio. If the libraries are gone, re-add them as Available to AVA. Then run `evaluations/AVA_eval.csv` (PR / PO receipt questions). |
| 3 | High | **SIMMY is missing from AVA's routing table and triggers.** AVA can only reach it through its description. | `config/ava/instructions.md` | Add a SIMMY row and trigger. AVA's instructions have 137 characters left, so trim first (for example, merge the ROUTING TRIGGERS list into the routing table, which repeats it). |
| 4 | Medium | **3 Warnings** on agent status (was 1 in Aug: "shared with all users"). | Overview tab | Open *Review*, record the warnings in `config/ava/overview.md`, then fix or accept them. |
| 5 | Medium | **MAP's named source is not connected.** The instructions point to `D365 procurement subcategories-MainAccountMappings_11.03.2026.xlsx` and its sheets; only the PDF QRC is connected. | `config/child-agents/map.md` | Connect the workbook to MAP, or rewrite the source section to match the QRC. |
| 6 | Medium | **Tool list incomplete.** Overview shows Get work item attachment / comments / details. The Aug design doc listed comments / details / List work item fields / Search for work items. WIA's instructions also mention Get query results. | `config/ava/tools.md` | Capture the full Tools tab. |
| 7 | Low | Duplicate `D365 Financial Dimension Decision Support Tool.pdf` (one for FIN, one for AVA). | Knowledge tab | Keep it only if AVA needs it directly; otherwise remove AVA's copy. |
| 8 | Low | Locale mismatch: the instructions cite `learn.microsoft.com/en-au/dynamics365/`, but the knowledge source is `en-us`. | Instructions vs Knowledge | Use one locale. |
| 9 | Low | Child-agent instructions here are the Jun 2026 baseline, not a live capture. | `config/child-agents/*.md` | Paste each child's instructions from Studio. |
| 10 | Low | No evaluation set for SIMMY. | `evaluations/` | Write `SIMMY_eval.csv` once its scope is captured. |
| 11 | Info | Engagement dropped from 81% (Aug) to 29%, and sessions from 26 to 14 per 7 days. | Monitor snapshots | Check the Monitor tab for causes (usage limits, licensing: only 22 of 295 D365 users had M365 Copilot as of Jun 2026). |
