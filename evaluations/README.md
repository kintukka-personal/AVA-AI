# Evaluations

Test sets in the Copilot Studio **Evaluation** import format: a CSV with `question` and `expectedResponse`, up to 100 questions, each 500 characters or fewer. Import one in Copilot Studio › Evaluation › New test set › Import.

| File | Agent | Cases | Covers |
|---|---|---|---|
| [`AVA_eval.csv`](AVA_eval.csv) | AVA | 25 | Routing to each child, ambiguity handling, PG step extraction, troubleshooting / escalation, refusals, prompt-leak resistance |
| [`FIN_eval.csv`](FIN_eval.csv) | FIN | 23 | BU / cost-centre / activity code lookups, sequence rules |
| [`MAP_eval.csv`](MAP_eval.csv) | MAP | 23 | Main account mappings, VAT groups, lease treatment |
| [`TAM_eval.csv`](TAM_eval.csv) | TAM | 20 | Template identification and purpose |
| [`WIA_eval.csv`](WIA_eval.csv) | WIA | 21 | Read-only refusals, summaries |

Written 2026-06-17 alongside the instruction rewrite. Expected answers that contain specific codes (FIN, MAP) or file names (TAM) reflect the source files as of that date. Re-check them when a source file changes.

## Run them

- Before every **Publish** that changes instructions, knowledge, or child agents.
- Log the score in [`CHANGELOG.md`](../CHANGELOG.md) with the change.
