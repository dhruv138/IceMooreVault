# Decisions: reorganising the vault for a local reasoning model

Branch: `testing`. Goal: a local Ollama model with reasoning should be able to answer questions and make labelled assumptions about the campaign, using **everything** in the vault.

Each decision below says what was done, why, and what it costs. The step-by-step instructions for using all this are in `scripts/README.md`, Part 3.

---

## 1. The model reads the whole vault at once, not a search result

**Your requirement:** "If it's in the vault I want it to be accessible and usable. I don't want things to be missed because a file wasn't loaded into a context."

**Decision:** every question is answered with the entire vault in the model's context. The vault is compiled into one file (`LLM/Icemoor Full Context.md`), and `scripts/ask_vault.py` sends it with every question.

**Why not search (retrieval)?** Retrieval tools, including Obsidian chat plugins, pick the handful of passages that best match the question and only show the model those. That's exactly how things get missed. Questions like "who might have stolen Talir's documents?" depend on clues spread over sessions 24, 25, 37, 38 and 39, and no search reliably returns all of them. The vault's current Obsidian setup can't load everything either. Ollama Notes Chat is set to retrieval mode with a 16,000 truncation limit, using qwen3:1.7b, which holds about 40,000 tokens; the vault is twice that.

**Trade-off:** the model needs a large context window and the memory to go with it, and the first answer takes longer while it reads everything (see 2 and 3).

## 2. How big the vault is, and what that requires

Measured on this branch (token counts are estimates at about 3.7 characters per token; the exact count depends on each model's tokenizer):

| | Tokens | Notes |
|---|---|---|
| **Full context** | about 80,000 | everything; 222 notes plus 39 sessions |
| of which session text | about 50,000 | 32,600 words, the primary record |
| **Core context** | about 36,000 | every note, but sessions reduced to their recap |

**Decision:** the model needs a context window of at least **100,000 tokens** for the full vault (80,000 plus about 20,000 of room to reason and answer; raised from 12,000 because high reasoning effort thinks at length). In practice, choose a model with a **128K or larger** context length.

**Models checked on Ollama's library** (October 2026; confirm with `ollama show <model>`):

| Model | Download | Context length | Fits the full vault? |
|---|---|---|---|
| `gpt-oss:20b` | 14 GB | 128K | **Yes.** A reasoning model. Recommended starting point. |
| `qwen3:30b` | 19 GB | 256K | **Yes.** Needs more memory. |
| `qwen3:4b` | 2.5 GB | 256K | **Yes, on paper.** Smallest download, but holding a long context needs a lot of extra memory for its size. |
| `qwen3:8b`, `qwen3:1.7b` | 5.2 GB, 1.4 GB | 40K | **No.** They can't hold even the core context. |

**Memory:** holding about 96,000 tokens needs extra memory on top of the model file. These are my estimates from each model's published design: roughly 2–3 GB for gpt-oss:20b, which uses a space-saving attention design; roughly 9 GB for qwen3:30b; roughly 14 GB for qwen3:4b. Setting the environment variables `OLLAMA_FLASH_ATTENTION=1` and `OLLAMA_KV_CACHE_TYPE=q8_0` before starting Ollama roughly halves that extra memory.

## 3. A script sets the context size, and refuses to truncate silently

**Decision:** `scripts/ask_vault.py` is the supported way to ask questions. It:
- loads the compiled vault and sends it as the system message with every question, keeping the conversation for follow-ups;
- asks Ollama for a context window sized to fit (`num_ctx`), because Ollama's default window is only a few thousand tokens and would silently drop most of the vault;
- reads the model's real context limit from Ollama and **stops before sending** if the vault won't fit, explaining what to do;
- hides the model's reasoning unless `--show-thinking` is given;
- uses only Python's standard library.

**Not changed:** the Obsidian chat plugins' settings. As configured they can't see the whole vault. Making a plugin send the full context file would mean raising its truncation and context limits; I haven't tested that, so I left their settings alone.

## 4. The compiled files are generated from the notes, never edited

You chose to restructure the notes themselves rather than maintain a separate model-only copy, so all editing happens in the notes. The context files in `LLM/` are just the notes concatenated and cleaned. `build_llm_context.py` rebuilds them on every update, so they can't drift from the notes.

`LLM/` is excluded from Obsidian's search and graph (Settings → Files and links → Excluded files), so the vault doesn't show every note twice.

## 5. What's left out of the compiled context, and why

| Left out | Why |
|---|---|
| Metadata blocks | Each note's header card shows the same information in readable form. |
| Generated "Session history" boxes | Word-for-word quotes of session text that the context already contains in full. Including them would add about 19,000 tokens of repetition. |
| Dataview code, index pages (Timeline, People/Places/Quest Index, Dashboard) | Lists of links or code with no information of their own. |
| Canvas files, Mermaid code | Their relationships are converted into plain "A —relationship→ B" lines on each note instead (decision 9). |
| Templates, scripts, Obsidian settings, the README files, this `decisions.md` | About the vault's tooling, not the campaign. |
| **`AI Chats/`** | Earlier conversations with a small chatbot that **invented** facts: "Icemoor Elves", files that don't exist, and Philip as "a rogue from the southern kingdoms". Feeding those to a model as if they were notes would mislead it. |
| `LLM/Test Questions.md` | Contains the answers. |

Everything else in the vault is included.

## 6. The original source document is now readable, and filled real gaps

`Resources/Icemoor Mountains copy.docx` is a Word file, which a language model can't read. I converted it to text and compared it with the vault.

- **Sessions 1 and 2 were missing from the vault** and are now `Sessions/Session 01.md` and `Session 02.md`. Session 1 is where the party's ram throws up the black stone. Session 2 is the arrival at Truemetal Halls and the first meeting with The Bastard's Band.
- **The campaign setup notes were missing**: the party, Deanira's backstory, the original quest list with details such as Balgus and the Glabrezu, and the apothecary's pay rates. They are now `Resources/Campaign Setup.md`, word for word.
- **Sessions 3–36 were compared word by word** with the source. Six places where the original import had changed the meaning were restored. They are listed in `00 Campaign/Contradictions and Uncertainties.md`; the important ones are Klaus being "the elected Burgermeister of Venburg" and the female half-elf "Onyxcrest" being Bianca, not Hambrick.
- The Word file has no images, so nothing was lost in conversion. It stays in `Resources/` as the original.

**Note:** these import errors also exist on `claude_web` and the other branches. They were only fixed here.

## 7. Every note now has the same layout

**Decision:** all 222 people, place, faction, quest, mystery, item and lore notes follow one layout:

1. **Header card**: type, status, other names, first session.
2. **Summary**.
3. Any topic-specific sections the note already had (Objective, Clues & findings, Backstory and so on).
4. **Facts by session**: one line per development, starting with its session.
5. **Connections**: the note's relationships as "A —relationship→ B" lines.
6. **Session history**: kept for reading in Obsidian; left out of the model's context.

**Why:** a fixed layout lets the model find the same kind of information in the same place for every subject, and lines that start with their session make "when did this happen?" answerable.

Session notes get only a header card (session number, the real-world date it was played, previous and next session). The players' text is never rewritten.

The layout is applied by `scripts/structure_notes.py`, which runs as part of the normal update, so new notes get it automatically.

## 8. Evidence labels separate fact from hearsay and guesswork

A reasoning model needs to know how far to trust each statement, or it will repeat a suspicion as fact.

| Label | Meaning |
|---|---|
| *(none)* | The session notes record it as having happened. |
| **[reported]** | Someone said, told or claimed it. |
| **[suspicion]** | Contains a guess, theory, rumour or suspected link. |
| **[inference]** | A conclusion drawn while organising the vault. |
| **[fact]** | Marked by hand as established. |

The script sets [reported] and [suspicion] from keywords. I then reviewed every one of the 43 labelled lines by hand, corrected the misfires, and narrowed the keywords. Lines ending in a question mark are treated as open questions and left unlabelled.

**Limitation:** only bullet points are labelled. Paragraphs already state uncertainty in words ("not established", "possibly"). The keywords will occasionally mislabel a line you write later; start it with [fact] to override.

## 9. Relationships are written out as text

The canvas boards and Mermaid diagrams hold 93 labelled relationships, but a model can't read a drawing. **Decision:** each relationship is written onto both notes it connects, in the Connections section.

While doing this I found that dotted lines on the Relationships diagrams had been used loosely. Some marked established facts, such as the Skeletal Hand being banned or Gavin Gosling's death. Those 8 are now solid, so a dotted line always means "suspected", matching the diagram's own legend.

## 10. Errors in the notes corrected along the way

- **Theo'din and the twin.** His note said his *twin* was taken by the Raven Queen; Session 32 says Theo'din *was* the twin taken.
- **Two Gunther Rockhammers.** Session 24 says the tanner is "another Gunther Rockhammer, not the one who runs The Warhammer", but both were linked to one note. The tanner now has his own note: `Gunther Rockhammer (Tanner)`.
- **Hambrick and Bianca.** "Onyxcrest, a female half-elf" in Session 23 had been linked to Hambrick, who is male. It's Bianca.
- **"Theo'din Corvis’din".** A garbled name in Session 32 was restored to "Theo’din".
- **Hall of the Four Clans.** Now described from Session 2.
- **Morgran Ironoak.** A new note for the apothecary from the setup notes. That he's the sessions' unnamed "Alchemist" is marked as an inference.
- **Session 1 recap.** Corrected to match the text: Deanira came out of the tree line; she wasn't herding.

## 11. Two guides for the model, and an alias list

- **`00 Campaign/AI Reading Guide.md`** covers how to read the vault:
  - The trust order: sessions over summaries.
  - Who the players are, and that out-of-character remarks and dice rolls appear in the notes.
  - That session dates are **real-world game nights, not in-world dates**.
  - What the evidence labels mean, and how to answer: cite sessions, keep fact, hearsay, suspicion and inference apart, say "the vault doesn't say", and label speculation.
- **`00 Campaign/Contradictions and Uncertainties.md`** lists every known conflict (for example the robe-retirement dates), unsettled identity (Peter Owens and the recruiter, two Gunthers), open question (Philip's lycanthropy) and spelling variant.
- **`00 Campaign/Aliases.md`** is generated from the notes: 44 subjects with other names or spellings.

All three go at the start of the compiled context, and `ask_vault.py` tells the model to follow them.

## 12. Session 39 on this branch is made up

`Sessions/Session_39.md` is the theoretical session written for testing ingestion on `generic_feature_development`. **None of it happened in the game.** On this branch it stays raw (not set up): the scripts skip it, and the compiled context includes it as "raw notes, not yet set up". Several test questions (9, 15, 16, 17, 19) use it to check that the model reads unprocessed notes.

- **To test on real events only:** delete `Sessions/Session_39.md` and run the update before asking questions.
- **Running the full update** (`update_all.py` or the double-click shortcut) will set Session 39 up the way any new session is set up. That's the normal behaviour; I avoided running it here to keep the raw file intact.

## 13. Test questions

`LLM/Test Questions.md` has 20 questions with the answers the vault supports. They cover lookups, aliases, identity traps, contradictions, things the vault doesn't say, chronology, and questions that ask the model to reason or assume. There's also one false premise ("Icemoor elves"). The file is excluded from the context.

## 14. Script fixes made along the way

- **Status corruption.** The metadata step read a quest's status from any "**Status:**" text, and with header cards that meant copying the whole header line into the status field on every run. Now only a status at the start of a line, or the existing metadata, counts.
- **Stale next session.** When a session stopped being the latest, its `next_session` link could survive. Previous/next links are now rebuilt from scratch.
- **Raw session protection.** The metadata step no longer adds a header to a raw session file; that happens only in the dedicated setup step.

These fixes are on this branch only.

## 15. What I couldn't check

- **No real model was run.** There's no Ollama here, so `ask_vault.py` was tested against a stand-in server, covering: the model too small, a large-enough model, a missing model, Ollama not running, and the core context. Real answer quality is what the test questions are for.
- **Token counts are estimates.** Actual counts depend on each model's tokenizer; `ask_vault.py` builds in a margin.
- **The restructured notes haven't been viewed in Obsidian.** The layout uses only standard Markdown and Obsidian comment markers, which are hidden in reading view.
