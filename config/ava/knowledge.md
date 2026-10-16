# AVA — Knowledge (live)

Captured 2026-10-16 from Copilot Studio › Knowledge. Screenshot: [`screenshots/2026-10-16/knowledge.png`](../../screenshots/2026-10-16/knowledge.png).

All sources show **Status: Ready** and **Usage: General**, and Daniel Moreira last modified all of them. "Available to" sets which agent can use a source.

| # | Name | Type | Available to | Last modified |
|---|---|---|---|---|
| 1 | https://support.microsoft.com/en-us | Public website | AVA | ~3 months ago |
| 2 | https://learn.microsoft.com/en-us/dynamics365/ | Public website | AVA | ~5 months ago |
| 3 | https://learn.microsoft.com/en-us/ | Public website | AVA | ~5 months ago |
| 4 | D365 Simulations | SharePoint | SIMMY (disabled test) | ~9 days ago |
| 5 | D365 Templates | SharePoint | TAM | ~4 months ago |
| 6 | 33-Procurement (Purchase Requisitions) PG.pdf | SharePoint | FIN | ~5 months ago |
| 7 | 32-Vendor Payments PG.pdf | SharePoint | FIN | ~5 months ago |
| 8 | 34-Procurement (Purchase Agreements) PG.pdf | SharePoint | FIN | ~5 months ago |
| 9 | 30-Vendor Onboarding and Maintenance PG.pdf | SharePoint | FIN | ~5 months ago |
| 10 | 31-Vendor Invoices PG.pdf | SharePoint | FIN | ~5 months ago |
| 11 | D365 QRC - Procurement Subcategories – Main Account Mappings.pdf | SharePoint | MAP | ~5 months ago |
| 12 | WTG - AU Legal Entities.xlsx | SharePoint | FIN | ~5 months ago |
| 13 | D365_FinDims_PR_CodingGuide.xlsx | SharePoint | FIN | ~5 months ago |
| 14 | D365 QRC - What are Financial Dimensions.pdf | SharePoint | FIN | ~5 months ago |
| 15 | Financial Dimensions Codes.xlsx | SharePoint | FIN | ~5 months ago |
| 16 | PAT | SharePoint | FIN | ~5 months ago |
| 17 | D365 Financial Dimension Decision Support Tool.pdf | SharePoint | FIN | ~5 months ago |
| 18 | D365 Financial Dimension Decision Support Tool.pdf | SharePoint | AVA | ~5 months ago |

## What each agent can draw on

| Agent | Sources |
|---|---|
| AVA | 3 Microsoft public websites; FD Decision Support Tool (2nd copy) |
| FIN | PGs 30–34, AU Legal Entities, FinDims PR Coding Guide, What are FDs QRC, FD Codes, PAT, FD Decision Support Tool |
| MAP | Procurement Subcategories – Main Account Mappings QRC |
| TAM | D365 Templates library |
| SIMMY (disabled) | D365 Simulations library (leftover from the test) |
| WIA | None (uses ADO tools — see [`tools.md`](tools.md)) |

## Changes since the Aug 2026 design document

- **Added:** `D365 Simulations` (for the SIMMY test; remove with SIMMY).
- **Not in the live list:** `D365 Procedure Guides` and `D365 Quick Reference Cards`, which the design document listed as AVA's own SharePoint sources. AVA's instructions say approved PGs/QRCs come first, yet the only SharePoint source AVA has is the FD Decision Support Tool. See [`docs/open-items.md`](../../docs/open-items.md) item 2.
