# AVA — Atlas Virtual Assistant

AVA is the central Finance AI entry point for D365 support at WiseTech Global. It is built in Microsoft Copilot Studio as a parent agent that answers from approved Procedure Guides (PGs) and QRCs and routes specialist questions to child agents (FIN, MAP, TAM, WIA).

This repo is the **single source of truth** for AVA's configuration, decisions, and history. It replaces the copies scattered across SharePoint, OneDrive, and people's machines.

## Source-of-truth order

1. **Copilot Studio (live agent).** What users get. If it disagrees with this repo, Studio wins, and the repo gets updated.
2. **[`config/`](config/).** A mirror of Studio, captured on the date in each file.
3. **[`docs/`](docs/).** Architecture, history, and open items, written from 1 and 2.
4. **[`archive/`](archive/).** Original documents. Reference only and largely outdated.

## Layout

```text
config/
  ava/              overview, instructions, knowledge, tools, topics   ← live AVA config
  child-agents/     fin, map, tam, wia (+ simmy, disabled) + shared standards
evaluations/        Copilot Studio test sets (CSV import format)
docs/
  architecture.md   parent–child model, routing logic, constraints
  history.md        timeline, pilot results, people
  open-items.md     known gaps between live config and intent   ← start here
  analytics.md      dated usage, quality, and knowledge-use snapshots
screenshots/        dated Copilot Studio captures
archive/            original files + searchable text copies (_text/)
CHANGELOG.md        every change made in Studio, newest first
```

## Current snapshot (2026-10-16)

| | |
|---|---|
| Model | Claude Opus 4.6 |
| Last published | 8/6/2026 |
| Child agents | FIN, MAP, TAM, WIA (SIMMY: disabled test) |
| Knowledge | 3 Microsoft websites + 16 SharePoint sources, each scoped to one agent |
| Channels | Teams, Microsoft 365, SharePoint (org-wide) |
| Status | 3 warnings: no eval run, premium licence needed to publish, shared org-wide · see [`docs/open-items.md`](docs/open-items.md) |

## Making a change

1. Make the change in Copilot Studio (draft).
2. Update the matching file in `config/` with the exact text.
3. Run the relevant test set from `evaluations/` in the Test or Evaluation pane.
4. Publish in Studio.
5. Add a `CHANGELOG.md` entry: what changed, why, and the eval result.
