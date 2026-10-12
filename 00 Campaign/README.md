---
title: "Icemoor Campaign Vault"
tags:
  - campaign
  - dnd
  - 5e
---
# Icemoor Campaign Vault

A structured Obsidian vault generated from the campaign notes in **Icemoor Mountains copy.docx**.

## How this vault is organized

- [[Campaign Dashboard]] — central navigation and active mysteries
- [[Timeline]] — session chronology and major events
- `Sessions/` — one note per recorded session
- `People/` — PCs and NPCs
- `Places/` — settlements, regions, dungeons, shops, and landmarks
- `Factions/` — organizations, clans, cults, and political groups
- `Quests/` — active, completed, and unresolved hooks
- `Items/` — important objects and magic items
- `Lore/` — gods, history, mysteries, monsters, and setting facts
- `Clues & Mysteries/` — investigation threads and unresolved questions
- `Resources/` — extracted reference material and campaign indexes

### Conventions

- `[[Wiki Links]]` are intentionally dense to improve graph visualization.
- YAML frontmatter supports Obsidian search and Dataview-style workflows.
- `status: unresolved` is used for plot threads that remain open in the notes.
- Information is preserved as **campaign notes**, not treated as externally verified canon.
- Contradictory spellings from the source notes are retained in aliases where useful.
- Every note name is unique, so a `[[link]]` always points at one note. Quests that are also investigations live in `Quests/`, with their clues under **Clues & findings**.

### Metadata fields

These power the tables in [[Dataview Queries]] and the live sections of the [[Campaign Dashboard]].

| Field | Used on | Values |
|---|---|---|
| `type` | every note | `pc`, `npc`, `location`, `faction`, `quest`, `mystery`, `item`, `lore`, `session` |
| `party_member` | party characters | `true` |
| `status` | quests & mysteries | `active`, `unresolved`, `upcoming`, `partially resolved`, `resolved`, `completed` |
| `first_seen` | anything linked from a session | the first session that links it |
| `location_type` / `item_type` | places / items | e.g. `inn`, `temple`, `weapon` |
| `session`, `date` | sessions | number, `YYYY-MM-DD` |
| `previous_session`, `next_session` | sessions | links |
| `party`, `npcs`, `locations`, `factions`, `quests`, `items` | sessions | links to everything the session mentions |

Appearance counts and "last seen" aren't stored. Dataview works them out from which sessions link to a note, so **linking names in a new session note is all it takes** to keep those tables current.

### Adding a new session
1. Name it `Session NN.md` (two digits).
2. Add the frontmatter fields above and a `> [!summary] TL;DR` callout under the heading.
3. Link people, places, factions, quests and items with `[[ ]]`.
