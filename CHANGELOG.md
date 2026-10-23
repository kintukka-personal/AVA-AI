# Changelog

Changes to the live Copilot Studio agent, newest first. Format: date · agent · what changed · why · eval result.

## 2026-10-23 · Analytics snapshot (no config change)

- Recorded 180-day Activity analytics in `docs/analytics.md`: 3,113 sessions, 50,158 credits, 94.6% good answers.
- Re-opened open item 2. Analytics show the PG and QRC libraries in heavy use, but they're missing from the Knowledge tab capture.

## 2026-10-16 · SIMMY switched off; live capture completed

- **SIMMY:** Enabled → Off. It was a test, not part of AVA's design. Not yet published (the Draft also carries the licensing warning).
- Captured live instructions for FIN, MAP, TAM, and WIA. They match the 2026-06-17 rewrite word for word, so nothing changed there.
- Captured all 5 tools and the 3 agent-status warnings.
- Open items re-triaged: 4 closed, new items for the licence-to-publish warning, WIA's missing attachment tool, and TAM's missing folder URL.
- Eval: none run yet (open item 4).

## 2026-10-16 · Repo created

- Captured live AVA config from Copilot Studio: overview, instructions (7,863 chars), knowledge (19 sources), child agents (5).
- Seeded child-agent configs from the 2026-06-17 rewrite (pending live capture).
- Archived consolidated SharePoint/OneDrive files with searchable text copies.
- Logged 11 open items in `docs/open-items.md`.

## History before this repo

The instruction history V1.00 (2026-01-27) → V2 launch (2026-05-14) → Claude-project rewrite (2026-06-17) is reconstructed in [`docs/history.md`](docs/history.md). Changes made in Studio between 2026-06-17 and 2026-10-16 that are known only from their effects:

- ≈2026-10-07 · SIMMY — child agent and `D365 Simulations` knowledge added (unpublished as of 2026-10-16).
- Between 2026-08-16 and 2026-10-16 · AVA — `Get work item attachment` tool visible; `D365 Procedure Guides` / `D365 Quick Reference Cards` no longer in the knowledge list.
