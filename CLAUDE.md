# Working in this repo

This repo mirrors a Microsoft Copilot Studio agent (AVA) and its child agents. Nothing here runs: the files are configuration text, docs, eval sets, and archived documents.

## Rules

- **Copilot Studio is the source of truth.** When the user pastes Studio text or screenshots, update `config/` to match exactly and set the "Captured" date. Never "improve" captured text while mirroring it.
- **Keep proposed changes apart from captured config.** Draft new instructions in a PR or in `docs/`, and label them proposed. `config/` changes to the new text only after the user confirms it is live in Studio.
- **Respect Studio limits.** Agent instructions have an 8,000-character maximum; AVA is at 7,863. Report the character count for any proposed instruction change.
- **Archive is reference only.** Don't edit files in `archive/` except to add new originals and their `_text/` copies.
- **Every live change gets a `CHANGELOG.md` entry**, newest first.
- **Track gaps in `docs/open-items.md`.** Close items when they are fixed.
- When the routing table, the child agents, or the shared standards change, update `config/child-agents/README.md` and `docs/architecture.md` as well.
- Eval sets must stay in Copilot Studio import format: `question,expectedResponse`, up to 100 rows, each question 500 characters or fewer.

## Writing style

The agents' own style rules apply to any text that ends up in an agent: formal business tone, American English, no "reply with a number". Repo docs: short and factual.
