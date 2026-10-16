# AVA — Tools (live)

Captured 2026-10-16 from Copilot Studio › Tools ([screenshot](../../screenshots/2026-10-16/tools.png)), plus the Tools list on WIA's Details page.

All 5 tools are Azure DevOps connector actions with Trigger = By agent and Enabled = On, last modified by Daniel Moreira.

| Tool | Available to | Last modified | Fixed inputs | AI-filled inputs |
|---|---|---|---|---|
| Get work item attachment | **AVA** | ~1 month ago | _to capture_ | _to capture_ |
| Get work item comments | WIA | ~2 months ago | Organization = `wtg-finance`; Project = `Atlas D365` | Work Item Id |
| Get work item details | WIA | ~2 months ago | Organization = `wtg-finance`; Project = `Atlas D365` | Work Item Type, Work Item Id |
| List work item fields | WIA | ~2 months ago | Organization = `wtg-finance` | — |
| Search for work items | WIA | ~2 months ago | Organization = `wtg-finance`; Project = `Atlas D365` | Search Text |

Inputs come from the Aug 2026 design doc. Open each tool to confirm them and to fill in the attachment tool.

## Gaps against WIA's instructions

| WIA's instructions allow | Live state |
|---|---|
| Get work item attachment (CASE D attachment review) | Exists, but **scoped to AVA, not WIA** |
| Get query results (CASE G reporting) | **Not configured** |

See [`docs/open-items.md`](../../docs/open-items.md) item 3.
