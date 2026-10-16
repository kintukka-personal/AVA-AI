# Architecture

## Model

AVA is a **parent orchestration agent** in Microsoft Copilot Studio. It is the single front door for D365 Finance support. It answers general documentation questions itself and routes specialist questions to child agents.

```text
                Microsoft Teams · Microsoft 365 · SharePoint
                                   │
                         ┌─────────▼─────────┐
                         │        AVA        │  Claude Opus 4.6
                         │  parent / router  │  Web Search: off
                         └─────────┬─────────┘
     ┌─────────────┬───────────────┼───────────────┬──────────────┐
     ▼             ▼               ▼               ▼              ▼
   FIN           MAP             TAM             WIA           SIMMY
 Fin. Dims    Proc./GL/VAT    Templates     ADO work items   Simulations
 PGs 30–34,   Subcategory –   D365          ADO connector    D365
 FD codes,    Main Account    Templates     (read-only,      Simulations
 coding guide QRC             library       wtg-finance)     library

  Not an agent: new issues → D365 Finance (Atlas) Issue Form · Atlas D365 User Support Hub
  Out of scope → People Leader
```

## How AVA decides

AVA classifies every query internally on two axes:

1. **Documentation confidence:** Direct match · Partial · Ambiguous · No match
2. **Domain ownership:** AVA / general D365 docs · child-agent domain · support / out-of-scope

| Case | When | Action |
|---|---|---|
| 1 — Direct answer | General PG question, no specialist needed | Extract documented steps: PG name, topic, pages, Action/Description table |
| 2 — Clarify | Could belong to more than one topic or domain | Ask one targeted question (never "reply with a number") |
| 3 — Route | Clearly a child's domain | Hand off without answering first |
| 4 — Refuse / redirect | Unsupported, undocumented, or an issue to log | First-line troubleshooting → Issue Form → People Leader |

## Design principles

- **Governed retrieval:** approved WiseTech PGs and QRCs only, with exact citations and no invented steps.
- **Domain ownership:** each child owns its lane and hands back to AVA for anything outside it.
- **Read-only everywhere:** no agent submits, approves, or changes D365, ADO, or SharePoint.
- **Scoped knowledge:** each knowledge source is "Available to" exactly one agent.
- **Shared standards:** every child carries the same baseline rules block ([`config/child-agents/README.md`](../config/child-agents/README.md)).

## Target state (V2 workshop, May 2026)

AVA stays the front door, with one child agent per Finance stream: **O2C, P2P, R2R, TAX, P2A, REP**. The proposed onboarding path for a new child: the BPO or SME fills in a structured Microsoft Form (4 phases, 14 steps), which becomes an ADO ticket and gets a weekly review. Today's children are function-based (FIN, MAP, TAM, WIA, SIMMY), not stream-based.

## Platform constraints

- Microsoft authentication limits channels to Teams, M365, and SharePoint.
- Usage limits caused an outage on 2026-06-05 (IT requests CS02363172 / CS02363197).
- Licensing: 22 of 295 D365 users (7.5%) had M365 Copilot as of 2026-06-23. Copilot credit cost governance was reviewed with Trent Walsh on 2026-07-07.
- The WIA ADO search tool is unreliable for broad queries (98+ results).
