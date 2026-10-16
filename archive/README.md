# Archive

**Reference only. Nothing here is the current configuration.** Copilot Studio is the source of truth, mirrored in [`config/`](../config/).

These files were consolidated from SharePoint and OneDrive on 2026-10-16. Each Word, PowerPoint, Excel, and PDF file has a text copy under [`_text/`](_text/), so the archive can be searched and diffed on GitHub.

## Status of each file

| File | Date | Status |
|---|---|---|
| **design-documentation/** | | |
| `AVA_Detailed_Design_Document.docx` | 2026-08-16 | Most complete snapshot before this repo. Superseded by `config/` where they differ. 5 identical copies existed; one kept. |
| **instruction-rewrites-claude-project/** | | |
| `AVA INSTRUCTIONS (revised).docx` | 2026-06-17 | **Matches live AVA instructions** (2026-10-16). |
| `FIN / MAP / TAM / WIA INSTRUCTIONS (revised).docx` | 2026-06-17 | Baseline for `config/child-agents/` (match the Aug design doc). Pending live check. |
| **child-agent-instructions/** | | |
| `FIN / MAP / TAM / WIA … INSTRUCTIONS.001.docx` | 2026-06-17 | Outdated: earlier versions without the Shared Standards block. |
| `TAM INSTRUCTIONS-001.docx` | 2026-06-04 | Outdated: first TAM draft. Has the direct D365 Templates folder link. |
| `TIM Instructions-001.docx` | 2026-04-30 | Retired: TIM created ADO work items directly. (`-002` was identical and was dropped.) |
| `TIM Instructions-003-redirect.docx` | 2026-04-30 | Retired: TIM redirects to the Issue Form. |
| `TIM Instructions-004-redirect-simple.docx` | 2026-05-13 | Retired: final TIM. Builds a copy-paste table for the Issue Form. Fallback email `d365fosupport@wisetechglobal.com`. AVA's CASE 4 now covers this. |
| **comms-decks-business-case/** | | |
| `AVA – Business Case and Pilot Findings- Apri2026l.docx` | Apr 2026 | Pilot metrics + AI Awards answers. Summarised in `docs/history.md`. |
| `AVA – Atlas Virtual Assistant - AI Awards.pptx / .pdf` | 2026-04 | AI Awards submission deck. |
| `Comprehensive Summary of the AVA Introduction Deck-April-2026.docx` | Apr 2026 | V1 positioning. |
| `Ask Ava - Intro Demo Script .docx` | 2026-01/02 | V1 demo script. |
| `AVA Agent Set - child, systems, automations.pptx` | 2026-05-01 | Child-agent naming ideas (PAT/PAL, ACE) and Studio tool patterns. |
| `AVA V2 Workshop-May 2026.pptx` | 2026-05 | Parent–child target model and rollout phases. Summarised in `docs/architecture.md`. |
| `AVA V2 COMMS - .docx`, `… full launch - Copy.docx`, `… full launch - May-2026.docx` | 2026-05 | V2 launch email drafts; `May-2026` is the final. |
| `AVA-1-pager.png`, `AVA-1-pager-v2.png` | 2026-04 | One-pagers. |
| `AVA-PPT-PROMPT.docx` | 2026-04 | Prompt used to generate the deck. |
| `Copilot Agent Development 101.pptx` | 2026-07 | Enablement session deck. |
| **images-branding/** | | |
| `Designer (2–6).png`, `poc/Ask Ava.png` | 2026-01/03 | AVA avatar and branding. |
| **inventory/** | | |
| `AVA_Document_Inventory.xlsx` | 2026-10-17 | Index of all 144 files, 97 emails, and 20 Teams chats about AVA across M365, with SharePoint locations. Most of those files are not in this repo. |

## Not yet in the repo

The inventory lists items that weren't in the upload. Add any that are still useful:

- Instruction history V1.00 → "final V1" (`7. AVA › 0. AVA Archived Instructions`)
- Scenario tests and parent–child tests (`01. AVA Scenario Testing`, `99. AVA Config Testing`)
- Change and rollout pack (Con Dolmas): change plan, RAID register, rollout plan, QRCs
- PG-authoring prompt framework (`69. PROMPTS`: `Atlas_PG_Master_Guide.md` and others)
- ACE / O2C files (`20. APRIL`)
