# Child agents

Live list from Copilot Studio › Agents, 2026-10-16 ([screenshot](../../screenshots/2026-10-16/agents.png)). Every child has Relationship = Child, Trigger = By agent, Enabled = On.

| Agent | Domain | Config file | Config status |
|---|---|---|---|
| FIN — Financial Dimensions Selector | Legal Entity, Business Unit, Cost Centre, Activity, PR coding | [`fin.md`](fin.md) | Baseline (Jun 2026 rewrite) |
| MAP — Mapping Assistant | Procurement category/subcategory, main account/GL, Item VAT Group | [`map.md`](map.md) | Baseline (Jun 2026 rewrite) |
| SIMMY — D365 Simulation provider | D365 simulations | [`simmy.md`](simmy.md) | **Not captured** |
| TAM — Template Access Manager | Approved D365 templates | [`tam.md`](tam.md) | Baseline (Jun 2026 rewrite) |
| WIA — Work Item Assistant (for ADO) | Existing Azure DevOps work items (read-only) | [`wia.md`](wia.md) | Baseline (Jun 2026 rewrite) |

## Shared standards

FIN, MAP, TAM, and WIA all carry this same block. Change it in every child at once, or not at all.

```text
SHARED STANDARDS
These baseline rules apply to this agent and are identical across all AVA child agents:
- Use formal business tone and American English.
- Use only approved WiseTech Global source material; never invent codes, names, or steps.
- Ask users to confirm by name or description — never "reply with a number only."
- Do not display full tables or lists unless explicitly requested; narrow by keyword.
- Never modify, submit, or approve anything in D365 or any system of record.
- Distinguish confirmed values from values that still require confirmation.
- For anything outside this agent's lane, hand control back to AVA (see Boundary).
```

## Not connected (historical / proposed)

| Agent | Status | Where it lives now |
|---|---|---|
| TIM — Ticket & Issues Manager | Retired. AVA's CASE 4 + the D365 Finance (Atlas) Issue Form now cover its job | [`archive/child-agent-instructions/`](../../archive/child-agent-instructions/) (v001, v003, v004) |
| ACE — Atlas Customer Expert (O2C) | Proposed and built by April Pei (May 2026); not connected to AVA | SharePoint only: `7. AVA › 20. APRIL` |
| PAT / PAL (P2P) | Naming options only (Agent Set deck). "PAT" exists today as a FIN knowledge source | [`archive/comms-decks-business-case/`](../../archive/comms-decks-business-case/) |
| R2R, TAX, P2A, REP | Target-state streams from the V2 workshop (May 2026) | [`docs/architecture.md`](../../docs/architecture.md) |
