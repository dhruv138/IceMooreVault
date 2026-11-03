# Notes for Claude: Icemoor vault

This file brings Claude on a desktop up to speed on work started in a Claude web session (handed over 3 November 2026). Claude Code reads it automatically when opened in this folder. In any other Claude, attach it or paste it in first.

## What this is

This is an Obsidian vault for a D&D campaign set in **Icemoor**. The repo is `dhruv138/IceMooreVault`. The **session notes** in `Sessions/` are the source of truth. Every other note is derived from them, in these folders: `People/`, `Places/`, `Factions/`, `Quests/`, `Items/`, `Lore/` and `Clues & Mysteries/`. The party is Riffle, Deanira, WISC, Furgus and Theo'din Corvis (often called "Theo").

## How the owner likes to work

- **One branch per change**, so the owner can see what each change did. Branch from whichever branch the work builds on, and say which one.
- **Don't merge into `main`** until the owner asks. They will collapse branches themselves later.
- **Keep the owner's wording.** Link names as `[[Peter Owens|Peter]]` rather than rewriting the text.
- **Never invent facts.** If the session is unclear, ask or add an open question. A local model once invented "Icemoor elves"; avoiding that is why the review step exists.
- **Explain things plainly.** The owner reads the README as a non-technical user.

## Vault conventions

- **Note frontmatter:** each note has `title`, `type`, `status`, `first_seen`, `tags` and `aliases`. Party members also have `party_member`; places have `location_type` and items have `item_type`.
- **Session frontmatter:** the scripts write this from `[[links]]` in the body. Fields are `session`, `date`, `previous_session`, `next_session`, `party`, `npcs`, `locations`, `factions`, `quests` and `items`.
- **Session titles:** `# Session 39 — 14 October 2026`, with an optional `> [!summary] TL;DR` box under the title. The dashboard uses that box as the session's recap.
- **Generated blocks:** `%% session-history:start %% … %% session-history:end %%` is rewritten by the scripts. Don't edit inside it.
- **Updates on a note:** new facts go under `## Recent developments` as `- [[Session N]]: …`. Unresolved points go under `## Open questions`. Both sit above the session-history block.
- **Quests and mysteries:** these have a `**Status:**` line.

## Scripts (`scripts/`)

These use Python 3.8+ and the standard library only. `scripts/README.md` has step-by-step instructions for a non-technical user; keep it updated whenever the scripts change.

| Script | What it does |
|---|---|
| `update_all.py` | Runs `update_metadata`, then `update_session_history`, then `build_dashboard`. Safe to rerun. |
| `update_metadata.py` | Sets up raw sessions: renames, adds the header and links names. It also refreshes frontmatter, sets `first_seen`, adds Timeline entries and prints a "Things to check" list. |
| `update_session_history.py` | Rewrites the session-history boxes. |
| `build_dashboard.py` | Builds `dashboard/Icemoor Dashboard.html` from `dashboard_template.html`. |
| `vault_names.py` | Shared name matcher. `AMBIGUOUS` lists names that are never auto-linked; `EXACT_CASE` lists names that must match capitals exactly. |
| `link_session.py "Session 39" [--apply]` | Links names while keeping the wording. Without `--apply` it only previews. |
| `ingest_session.py --model qwen3:8b "Session 39"` | Asks a local Ollama model for suggestions and writes them to `Ingestion/Session 39 proposals.md` and `.json`. |
| `apply_ingestion.py "Session 39"` | Writes the ticked proposals into the vault, links names and runs `update_all`. Rerunning skips items already applied. |

How `ingest_session.py` works:
- **Structured output:** it sends Ollama `/api/chat` with `format` set to a JSON schema. If the server rejects the schema, it falls back to `"json"`.
- **Context size:** it checks `/api/show` for the model's context length and refuses to run if the prompt won't fit.
- **Checks:** every item is validated before it reaches the review page.
  - Evidence quotes must appear in the session, matched word by word with at least 85% overlap.
  - A new note's name must appear in the session and mustn't already exist.
  - Facts must target a note that exists.
  - Only quests and mysteries can get a status.
  - Items that fail go to a **Rejected** section and can't be applied.

## Branches

| Branch | Built from | What's on it |
|---|---|---|
| `main` | — | The original vault. Leave it alone for now. |
| `claude_web` | main | Human-readability work: vault cleanup, tidy-up, stub notes, Mermaid diagrams, canvases, dashboard and the scripts README. Each step was done on its own branch, then merged in. |
| `online_session39_ingestion` | claude_web | The real Session 39, ingested by Claude with the owner's corrections. This is the quality target. |
| `local_session39_ingestion` | claude_web | The real Session 39 after the owner ran the scripts locally. |
| **`local_ingestion_pipeline`** | local_session39_ingestion (raw S39) | **Current work.** Offline ingestion, steps 1 and 2. |
| `generic_feature_development` | claude_web | A made-up Session 39 for testing, not ingested. |
| `web_ingestion` / `local_ingestion` / `testing` | generic_feature_development | The made-up Session 39 ingested online. `local_ingestion` is unused so far. `testing` is restructured for a local reasoning model and holds `decisions.md` and `ask_vault.py`. |
| `character_sheets` | generic_feature_development | Furgus's character sheet. |
| `ask-vault-reasoning-effort`, `ChatGPTWeb`, `ollama_session37`, `claude_ollama_session37` | — | The owner's own branches. |

### Session 39 corrections

These are the owner's corrections to the real Session 39; they are already in both Session 39 branches:
- Deanira and Riffle were the ones trapped; WISC rescued them.
- Furgus didn't teleport, because the glyph couldn't find another sarcophagus for him. The glyph is still intact.
- Furgus charmed Peter with an Arrow of the Harpy.

## Where the work stands

The goal is to bring `local_session39_ingestion` as close to `online_session39_ingestion` as possible using only offline tools.

1. **Done, commit 1ce6e86.** Deterministic fixes:
   - header cleanup
   - an auto-linker that keeps the wording
   - cleaner history snippets
   - `first_seen` counting unlinked mentions
   - an automatic Timeline entry
2. **Done, commit 8ac211d.** Local-model proposals with a review page and validation, plus the apply script.
   - Tested only against a mock Ollama server. Ollama couldn't be installed in the web session.
   - The mock run caught all six planted bad items, applied 11 ticked items correctly, and was safe to rerun.
3. **Not started; wait for the owner.** A comparison or scoring script that measures the local result against the online result: links, new notes, facts, recap and `first_seen`.
4. **Not started; wait for the owner.** Tuning prompts and models based on step 3.

### Suggested next step on the desktop

Try step 2 with a real model:

```
ollama pull qwen3:8b            # or gpt-oss:20b with 24 GB+ of memory
python3 scripts/ingest_session.py --model qwen3:8b "Session 39"
# tick items in Ingestion/Session 39 proposals.md, then:
python3 scripts/apply_ingestion.py "Session 39"
git diff --stat
```

Then compare the result with `online_session39_ingestion`, for example with `git diff local_ingestion_pipeline online_session39_ingestion -- People Places Sessions`. Look for:
- **Good facts rejected by the checks:** consider loosening the checks.
- **Things the model missed:** improve the prompt in `ingest_session.py`.
- **Wrong links:** add the name to `AMBIGUOUS` or `EXACT_CASE` in `vault_names.py`.

The owner's model and amount of memory haven't been confirmed yet; ask before assuming.

Test-run output in `Ingestion/` shouldn't be committed unless the owner wants it kept as an example.
