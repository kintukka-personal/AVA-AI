# SIMMY — D365 Simulation provider (disabled test)

| Field | Value |
|---|---|
| Status | **Disabled. A test only, not in use** (confirmed by Daniel Moreira, 2026-10-16) |
| Relationship | Child of AVA |
| Trigger | By agent |
| Enabled | **Off** (switched off 2026-10-16) |
| Studio link | https://copilotstudio.microsoft.com/environments/Default-8b493985-e1b4-4b95-ade6-98acafdbdb01/bots/dd76dbb0-6543-f111-88b3-7c1e526243e2/agents/ee20f1b7-de40-4df9-a090-54f0c0d4dce2/details |

SIMMY was added around 2026-10-07, after the last publish (8/6/2026), so users never had it. It is not part of AVA's design, and AVA's routing table correctly leaves it out.

## Leftovers to clean up

- `D365 Simulations` knowledge source (SharePoint, Available to: SIMMY) is still listed on AVA's Knowledge tab.
- The SIMMY agent itself. Delete it if the test has no further use, so it can't be switched back on by mistake.
