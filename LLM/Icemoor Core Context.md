# Icemoor Core Context

**This is the reduced version.** Session notes appear only as their one-paragraph recap. Details that exist only in session text are missing. Use the Full Context file whenever the model's context window allows.

Read **Part 1** first: it explains how the notes are written and how far each kind of statement can be trusted.

## Part 1: How to read this vault

### AI Reading Guide

How to read this vault when answering questions about the Icemoor campaign. If you are a language model, read this note first. It explains how the notes are written, how much each kind of statement can be trusted, and where the known gaps and contradictions are.

#### What the vault is

A record of a Dungeons & Dragons 5e campaign set in the Icemoor mountains. The players wrote the session notes after each game night. Every other note was written later, from those session notes, to organise the same information.

**Trust order, highest first:**
1. **Session notes** (`Sessions/`). The primary record. When anything else disagrees with a session note, the session note wins. A session file named with an underscore, like `Session_39.md`, is raw text that hasn't been set up yet: no header, recap or links. It is still a session note; read it the same way.
2. **[[Campaign Setup]]** (`Resources/`). The players' own setup notes from before Session 1: the party, Deanira's backstory, the quest list.
3. **Every other note.** Summaries written from the sessions. Useful for orientation, but a summary can be wrong. Check claims that matter against the session it cites.

#### Who's who in the writing

- The notes are written by the players, mostly in the first person plural ("we"), from the party's point of view. They only know what the characters learned.
- The players are Anita (plays [[Riffle]]), Lyra ([[Deanira]]), Taylor ([[WISC]]) and Dhruv ([[Furgus]]); see [[Session 09]] and [[Session 10]]. Player names occasionally appear in the narrative, e.g. "Dhruv talks to the half elf" in [[Session 07]] means Furgus did. The narrator or DM appears once as "Mike" ([[Session 10]]).
- Out-of-character remarks are mixed in: dice rolls ("rolls a Nat 20", "we roll initiative"), game mechanics, and jokes ("I metagame", [[Session 09]]). Treat dice and mechanics as describing how things went, not as in-world events.
- [[Session 26]] is titled "Missed Session" and is written in the third person ("the party"), unlike the others.
- [[Riffle]] is usually "they/them" in the notes, sometimes "he/him". It's the same character.

#### Dates and time

- The date on a session (e.g. "Session 37 — 12 September 2026") is **the real-world date of the game night, not an in-world date**. In-world time is only given in passing ("it's around June right now", [[Session 13]]; "the next full moon is in a month", [[Session 35]]).
- Sessions are in chronological order of play, and the story mostly runs in the same order. The session number is the best guide to "before" and "after".
- Sessions 1 and 2 are undated in the source.

#### Note layout

Every person, place, faction, quest, item, lore and mystery note has the same parts:

- **Header card** under the title: type, status, other names ("Also called"), and the first session that mentions it.
- **Summary**: who or what it is.
- **Facts by session**: one line per development, each starting with the session it comes from, e.g. `[[Session 38]]: ...`.
- **Connections**: relationships drawn on the campaign's boards and diagrams, written as `[[A]] —relationship→ [[B]]`.
- **Session history** (collapsed in Obsidian): every sentence in the session notes that mentions this note, quoted word for word.

Session notes have a header card (session number, the real-world date, previous and next session), a **TL;DR** recap written later, then the players' original text, unchanged apart from added links. A session's metadata lists the people, places, factions, quests and items it links to.

#### Evidence labels

Bullet points in the non-session notes carry a label when they aren't plain fact:

| Label | Meaning |
|---|---|
| *(none)* | Something the session notes record as having happened or been observed. |
| **[reported]** | Something a character said, told or claimed. It may be untrue or mistaken. |
| **[suspicion]** | Contains a guess, theory, rumour or suspected link. The rest of the line may still be fact; read the wording. |
| **[inference]** | A conclusion drawn when the vault was organised, not something said in a session. |
| **[fact]** | Marked by hand as established, overriding an automatic label. |
| *a line ending in "?"* | An open question. |

In **Connections**, a `[suspicion]` line or a relationship ending in "?" is a suspected link, not an established one.

#### Names

People and places often appear under several names or spellings ("Theo" for [[Theo'din Corvis]], "Tallir" for [[Talir Rengavi]], "Venberg" for [[Venburg]]). The header card's "Also called" lists them, and [[Aliases]] lists them all in one place. A link written `[[Theo'din Corvis|Theo]]` means the text said "Theo" and it refers to Theo'din Corvis.

#### Known gaps and contradictions

[[Contradictions and Uncertainties]] lists every known conflict between notes, spelling variant, and unconfirmed identity. Check it before stating one of those as settled.

#### How to answer

- Answer from the vault. If the vault doesn't say, say so; don't fill the gap from general D&D knowledge without saying that's what you're doing.
- Cite the session(s) your answer rests on, e.g. "(Session 36)".
- Keep four things apart in your answer: what happened, what someone said, what the party suspects, and your own reasoning.
- When asked to speculate or make assumptions, do it, but label it as your inference and give the evidence for and against.
- If notes conflict, say so and say which source you trust more and why (sessions over summaries; later sessions can correct earlier ones).

### Contradictions and Uncertainties

Everything known to be in conflict, ambiguous or unconfirmed in the vault. Check here before treating any of these as settled. See [[AI Reading Guide]] for how sources rank.

#### Conflicting statements

| Topic | What the notes say | Notes |
|---|---|---|
| When the red Library robes were retired | [[Hana Goldfirm]]: all red robes were "discontinued/destroyed 20 years ago" ([[Session 26]]). [[Ester]]: the robes changed from red to purple **50–60 years ago**, and some people may have kept theirs ([[Session 37]]). | Both are hearsay. Ester is the Chief Archivist and her account is more specific. Session 39's raw notes add that 12 old red robes were listed in Storeroom B and only 11 are there. |
| Timing of the Harvest festival and the Gauntlet | "In 3 months" ([[Session 24]]); "In three weeks" ([[Session 35]]); "will begin in a week and a half" ([[Session 36]]). | Consistent with time passing between sessions. In-world dates are never given precisely. |
| Who Riffle saw with golden eyes | Riffle saw a bugbear with WISC's rare eye colour among the raiders from [[Darham Hold]] ([[Session 19]]). [[Jane Pedimore]] describes a golden-eyed bugbear extorting families near [[Copperhead Hollow]] ([[Session 32]]). | Whether these are the same bugbear is not established. See [[Golden-Eyed Bugbear Mystery]]. |

#### Identities that aren't settled

- **The recruiter "Peter" and [[Peter Owens]].** A dead cultist said he was recruited by "a blond-haired youth by the name of Peter" ([[Session 30]]). Peter Owens is a strange Academy student ([[Session 38]]), but his hair is never described and nothing ties him to the Skeletal Hand. Whether they're the same person is unknown. See [[Blond Skeletal Hand Recruiter]].
- **"Andrew"** ([[Session 38]]): a young blond man seen at the Velvet Glove. Possibly the recruiter; not established.
- **Philip and Peter.** In [[Session 36]], Riffle half-remembers the Owens son's name as "Philip?Peter? (Something with a P)". That is a memory slip. The Owens son is [[Peter Owens]], and [[Philip]] is the hunter from Venburg who travels with the party.
- **Two Gunther Rockhammers.** [[Gunther Rockhammer]] runs [[The Warhammer]]. [[Gunther Rockhammer (Tanner)]] is a different man with the same name ([[Session 24]]).
- **The real and fake Hector.** The [[Hector]] who poisoned the party ([[Session 24]]) looked exactly like the real Hector, who had an alibi ([[Session 25]]). Someone disguised themselves as him.
- **"Onyxcrest, a female half-elf"** ([[Session 23]]) is taken to be [[Bianca Onyxcrest]], because Session 24 introduces Bianca by name in the same scene as an Academy colleague. [[Hambrick Onyxcrest]] is the male wizard.
- **"The Alchemist"** who offers the ingredient job ([[Session 09]], [[Session 24]]) is probably [[Morgran Ironoak]], the apothecary named in [[Campaign Setup]], but the sessions never name him.
- **[[Savehaven]] and "Safehaven".** Possibly the same port; not confirmed.
- **[[Theo'din Corvis]] and his twin.** His mother gave up one of her twins to the Raven Queen, and the twin taken was Theo'din himself ([[Session 32]]). Older summaries wrongly said "his twin was taken".
- **The Man in the Grey Mask and the [[Master of Death]]** (Session 39 raw notes): the party wonders if they're the same; nothing connects them yet.

#### Open status questions

- **[[Philip]]'s were-bear bite.** Philip and Hanz were attacked by the Stone Giant were-bears ([[Session 33]]), and [[Session 34]] says both are doomed to transform. The cure in [[Session 37]] covered "the others" with lycanthropy, but the notes never say whether Philip was among them.
- **The [[Mystery Stone]].** It is in the [[Library of Deneir]]'s keeping and will be shown at the [[Academy Gala]]; the Academy has access to it ([[Session 36]]).
- **The golden-eyed bugbear and WISC's father.** WISC's father left before WISC was a baby. That the bugbear might be a younger half-brother is a guess ([[Session 19]]).

#### Spelling variants

These are the same person or place. The vault uses the first form; the others appear in the session text.

| Vault name | Also written |
|---|---|
| [[Talir Rengavi]] | Tallir |
| [[Hana Goldfirm]] | Hannah |
| [[Christolf Nightfall]] | Kristoff, Kristof |
| [[Klaus]] | Claus (he is the elected Burgermeister of Venburg) |
| [[Venburg]] | Venberg, Venragh (on the map, [[Session 25]]) |
| [[Darham Hold]] | Durham Hold, Durham Hall |
| [[Wren Nalore]] | Renn Nalore |
| [[Zyuir]] | Zyvuir ([[Session 14]]) |
| [[Kriptin Forest]] | Krypton Forest |
| [[Tryborne Pass]] | Triborn Pass |
| [[Peter Owens]] | Peter Owen |
| [[Morgran Ironoak]] | Morgren Ironoak |
| [[Nastil]] | Nastril |
| [[Corthos]] | Corthis |
| [[Elzock Emberstone]] | Elzoc |
| [[Mittens]] | Mitt |
| [[Deneir]] | Denier, Danir |
| [[Abbathor]] | Abathor |
| [[Mithril]] | Mithral, Mithras |
| [[Philip]] | Phillip |
| [[WISC]] | Wisc, Wisk, WIS |
| [[Furgus]] | Fergus |

#### Corrections made when the vault was reorganised

The original import had changed a few words of the session text. These were restored from the source document (`Resources/Icemoor Mountains copy.docx`):

- [[Session 31]]: Klaus is "the elected **Burgermeister** of Venburg" (the import had replaced the title with his name); Furgus's brother is "Bad (Bunny)".
- [[Session 24]]: "Olga **the Bartender**".
- [[Session 23]]: the female half-elf "Onyxcrest" had been linked to Hambrick; it is Bianca.
- [[Session 18]]: the Tabaxi introduces themself as "Mitt (Mittens)".
- [[Session 07]]: "Amex Oswald" (as written in the source).
- [[Session 32]]: "Theo’din" had been garbled into "Theo'din Corvis’din".
- Sessions 1 and 2 and the [[Campaign Setup]] notes were missing from the vault and have been added from the source.

### Aliases

Every note that goes by more than one name. Generated by `scripts/build_llm_context.py` from each note's aliases; edit the aliases on the note itself, not here.

| Name in the vault | Kind | Also called |
|---|---|---|
| [[Bianca Onyxcrest]] | People | Bianca |
| [[Christolf Nightfall]] | People | Christolf, Kristoff Nightfall, Kristof |
| [[Corthos]] | People | Corthis |
| [[Countess Opal Darham]] | People | Opal Darham |
| [[Daddy Dildo Daggins]] | People | Daggins |
| [[Dagin Tillmore]] | People | Daggen, Dagin |
| [[Elzock Emberstone]] | People | Elzock, Elzoc |
| [[Ester]] | People | Esther |
| [[Gunther Rockhammer]] | People | Gunther |
| [[Hambrick Onyxcrest]] | People | Onyxcrest |
| [[Hana Goldfirm]] | People | Hannah, Hana |
| [[Jane Pedimore]] | People | Jane |
| [[Klaus]] | People | Claus |
| [[Lord Ivan Deepshaft]] | People | Lord Deepshaft, Ivar Deepshaft |
| [[Mittens]] | People | Mitt |
| [[Morgran Ironoak]] | People | Morgren Ironoak |
| [[Oma]] | People | WISC's Grandmother, WISC's grandmother |
| [[Oswald]] | People | Amex Oswald |
| [[Peter Owens]] | People | Peter, Peter Owen |
| [[Queen]] | People | Queen the mouser |
| [[Quithos the Breaker]] | People | Quithos, Tomb of Quithos the Breaker |
| [[Rupert Bubblegum]] | People | Mr. Bubblegum |
| [[Samuel Patel]] | People | Head Cleric of Mistra |
| [[Siobhan]] | People | Archivist Siobhan |
| [[Talir Rengavi]] | People | Talir, Tallir |
| [[The Bastard]] | People | Bastard |
| [[The Poet]] | People | Poet |
| [[Theo'din Corvis]] | People | Theo’din Corvis, Theo'din, Theo |
| [[Ambercrown Kingdom]] | Places | Ambercrown |
| [[Derragh]] | Places | Titan Fall |
| [[Kriptin Forest]] | Places | Krypton Forest |
| [[Owens Family Mausoleum]] | Places | Owens Mausoleum, Owen Family Mausoleum |
| [[Savehaven]] | Places | Safehaven |
| [[Tryborne Pass]] | Places | Triborn Pass |
| [[Venburg]] | Places | Venberg |
| [[Raven Queen's servants]] | Factions | Order of the Black Feathers |
| [[Sect of Torm]] | Factions | Followers of Torm, Torm sect |
| [[Union of Many]] | Factions | The Union of Many, Daggins' order |
| [[Academy Gala]] | Quests | Gala, The Gala |
| [[Gauntlet]] | Quests | The Gauntlet |
| [[Missing Sanitation Workers]] | Quests | Sewer missing persons |
| [[Blond Skeletal Hand Recruiter]] | Clues & Mysteries | Skeletal Hand recruiter, Skeletal Hand scholarship |
| [[Owens Family Deaths]] | Clues & Mysteries | Owen Family Deaths, Lord Richard Owens |
| [[Mithril]] | Lore | Mithral |

## Part 2: Campaign setup

### Campaign Setup

Everything in the source document (`Icemoor Mountains copy.docx`) before Session 1, transcribed word for word. Links were added; the wording is unchanged.

The largest political body up here is the [[Confederation]] (mostly Dwarven)

The Capitol is [[Truemetal Halls]] where there is a large deposit of Mithras and adamantine. Each major settlement is based on a vein of a specific ore, like iron, adamantine, etc.

#### Party

[[WISC]] the Bugbear

[[Furgus]] the Herrengon

[[Deanira]] the Satyr

#### Backstory

Deanira was born in a coastal village where the tides were strange and the stars never matched the charts. She didn’t have parents in particular, the culture of the tribe was that the children were raised by the whole community, not just by one or two. She was very close to a kind man named [[Val]], who was a handsome and gruff satyr in his late 40s/early 50s. She would sit with him and look over his shoulder as a small child and watch him draw exquisite maps. He taught her some cartography skills over the years. He would vanish over the horizon now and then, to chart what was beyond the line, especially looking for this floating island whose position eternally changed and no map could hold. If you charted it on a map, the marking on the map would vanish as well. Some of the villagers thought he was mad, but Deanira thought he could see what no one else could. He was convinced that there were ruins on the island that would explain the origin of the world and why the stars change. One day he never came back. It’s taken everything in Deanira to hold herself back from sailing off to find him and his island. Everyone insisted that she drop the subject or the island would drive her mad, like it had to someone each generation. Now she’s honing her map making skills by travelling the Icemoor mountains and charting ruins, so that one day she may become skilled enough to find that island, and maybe find him too.

#### Quests

• [[Oswald's Letter to Mary|Oswald’s letter to Mary]]. Avenge the death of Oswald and his partner’s son Albert. He asks us to also send word to his parter Mary Salter via a courier.

• [[Shredding Dude]]. Young half elf who died snowboarding. Wants us to return his body to Amberhold so he can be buried in the family masoleum. He died north of Truemetal Halls at a place called the MurderDrum (Matterhorn)

• [[Warrior of Kord]], The Brawler and Storm Lord. Half orc dressed in plate armour with the god’s crest on it, a shield with 4 lightning bolts radiating out from the center in the four diagonals. He is [[Balgus]], paladin of Kord. He died on a holy quest to reclaim a mountaintop Kord temple that was desecrated by a fiend. He died in solo battle with it. He offers us any of the equipment on him, but warns us to not loot the temple itself, or incur the wrath of Kord. His body and items can be found in the temple. He recalls the enemy to be a mighty fiend named [[Glabrezu]] with multiple arms and several pincers.

• The Apothecary shop (run by [[Morgran Ironoak]]) wants to hire us to secure a shipment and bring it to shop in Truemetal Halls and potentially gather additional ingredients along the way. Each 100 gp upon completion. Advance payment is either 4 regular healing potions or 2 greater healing potions. He will pay us 50gp for an egg and 10gp for a vial of blood. The town we are headed to receive the shipment from is Renn Nalore. It will be a week’s journey each way.

• [[Flesh Golems and Poison Mine|Flesh Golems and poison mine]]

• [[Mystery of the Cornhusk Dolls|Cornhusk dolls]]

• [[Darham Hold Unrest|Darham Hold]]. Their guards killed the goblin village

• Basilisk eggs

• [[Seasonal Festival]] with WISC and Furgus’s families

• [[Southern Auction|Auction in the south]]

• [[Mystery of Axeholm]]

• [[Mystery Stone Investigation|Mystery stone]]

#### Misc Information

Boarding the horse in Truemetal Halls: 2 sp per day

### Source Notes

**Original source:** `Icemoor Mountains copy.docx`

This vault is a structured transformation of the campaign notes. The source contains 80 pages and records at least 36 numbered sessions, plus campaign setup, backstory, quests, and miscellaneous notes.

#### Data-model choices

- Characters/NPCs → `People/`
- Settlements/regions/locations → `Places/`
- Organizations → `Factions/`
- Important objects → `Items/`
- Plot hooks → `Quests/`
- Unresolved investigations → `Clues & Mysteries/`
- Worldbuilding/reference facts → `Lore/`
- Play-by-play records → `Sessions/`

#### Canon / uncertainty

The original notes contain inconsistent spellings and occasional uncertain names. Those are preserved through aliases or separate reference notes where practical.

Examples:
- [[Talir Rengavi]] / Tallir / Talir
- [[Christolf Nightfall]] / Kristoff / Kristof
- [[Venburg]] / Venberg
- [[Kriptin Forest]] / Krypton Forest
- [[Tryborne Pass]] / Triborn Pass
- [[Savehaven]] / Safehaven (possibly the same port; unconfirmed)
- [[Peter Owens]] / Peter Owen
- [[Klaus]] / Claus
- [[Wren Nalore]]
- [[Zyuir]]

When the notes explicitly express uncertainty, this vault does not silently convert it into certainty.

## Part 3: Notes on people, places, factions, quests, mysteries, items and lore

## People

### Agatha

**Type:** Non-player character · **First seen:** [[Session 21]]
#### Summary

Long-armed hag-like figure encountered near the basilisk grounds. Trades information for personal objects and knowledge. Identified the [[Cornhusk Dolls]] as a fae creation associated with a pixie.

#### Connections

- [[Agatha]] —told the party→ [[Zyuir]]

### Alex

**Type:** Non-player character · **First seen:** [[Session 36]]
#### Summary

Sailor at the [[Cock and Pig]] who explained that his ship, back from [[Savehaven]], can't be unloaded because its owner Lord Richard Owens died ([[Session 36]]). See [[Owens Family Deaths]].

### Alkan

**Type:** Non-player character · **First seen:** [[Session 11]]
#### Summary

Goliath druid with [[Ilkan]]'s raiders, often sent out as a hawk or owl to scout; that's how the raiders found the party ([[Session 11]]). Ran off after the camp fell ([[Session 13]]).

### Ambria

**Type:** Non-player character · **First seen:** [[Session 28]]
#### Summary

Dragonborn from [[Venburg]] rescued from captivity in [[Quithos the Breaker]]'s tomb.

### Andrew

**Type:** Non-player character · **First seen:** [[Session 38]]
#### Summary

Name given by a young blond man who visited a worker named Angela at the [[Velvet Glove Brothel]], according to [[Sabrina]] ([[Session 38]]).

The party wonders whether he is the blond [[Skeletal Hand]] recruiter. That is a suspicion, not established. The recruiter gave the name Peter in [[Session 30]]. See [[Blond Skeletal Hand Recruiter]].

#### Connections

- [suspicion] [[Andrew]] —same person?→ [[Blond Skeletal Hand Recruiter]]

### Annika

**Type:** Non-player character · **First seen:** [[Session 31]]
#### Summary

Furgus's sister-in-law in [[Venburg]]. Helped prepare medical supplies for the community.

#### Connections

- [[Bad]] —married→ [[Annika]]

### Anton

**Type:** Non-player character · **First seen:** [[Session 07]]
#### Summary

Ghostly bartender at [[Unfinished Business]], a tavern for souls not ready to pass on.

### Atheela

**Type:** Non-player character · **First seen:** [[Session 38]]
#### Summary

Half-elf member of the [[Union of Many]]. Carries a staff topped with a distinctively shaped wooden knot.

- [[Session 38]]: [reported] Met [[Deanira]] in the basement of [[The Two Tits]]. Knew [[Daddy Dildo Daggins]] as "Brother Daggins" and was devastated to hear of his death. Explained the order's beliefs and that they meet at the inn about once a week.

### Bad

**Type:** Non-player character · **First seen:** [[Session 31]]
#### Summary

[[Furgus]]'s brother, who lives in [[Venburg]] with his wife [[Annika]] and their babies [[James]] and [[Julia]] ([[Session 31]]).

#### Connections

- [[Furgus]] —brother→ [[Bad]]
- [[Bad]] —married→ [[Annika]]

### Balgus

**Type:** Non-player character
#### Summary

Deceased paladin of Kord whose body and equipment lie in a desecrated mountaintop temple guarded by a [[Glabrezu]]. See [[Warrior of Kord]].

### Bianca Onyxcrest

**Type:** Non-player character · **Also called:** Bianca · **First seen:** [[Session 23]]
#### Summary

Mage associated with [[Mistra's Academy]]. Later became Headmistress after [[Gavin Gosling]]'s death. Helped arrange magical treatment for the [[Werebear Curse]].

#### Facts by session
- [[Session 37]]: Her arrangement with [[Samuel Patel]] cured the [[Werebear Curse]].
- [[Session 38]]: Her assistant [[Karyn]] is overwhelmed with [[Academy Gala]] and [[Gauntlet]] preparations.

#### Connections

- [[Bianca Onyxcrest]] —Headmistress→ [[Mistra's Academy]]
- [[Karyn]] —Bianca's assistant→ [[Bianca Onyxcrest]]

### Cam Jergins

**Type:** Non-player character · **First seen:** [[Session 36]]
#### Summary

Goliath sailor encountered at the [[Cock and Pig]]. Has both a dragon-skull tattoo and a [[Skeletal Hand]] tattoo.

#### Facts by session
- [[Session 37]]: [suspicion] The party suspects the blond young man at the tavern is who Cam copied the tattoo from. See [[Blond Skeletal Hand Recruiter]].

#### Connections

- [[Cam Jergins]] —copied tattoo from a blond kid→ [[Blond Skeletal Hand Recruiter]]

### Christolf Nightfall

**Type:** Non-player character · **Also called:** Christolf, Kristoff Nightfall, Kristof · **First seen:** [[Session 16]]
#### Summary

Undertaker in [[Truemetal Halls]] secretly involved with necromancy and the [[Skeletal Hand]]. Ultimately encountered in [[Quithos the Breaker]]'s tomb.

#### Facts by session
- [[Session 37]]: The party recalled that the cultist questioned with Speak with Dead in the cave where Christolf was killed had been recruited by a young blond man in [[Amberhold]]. See [[Blond Skeletal Hand Recruiter]].

#### Connections

- [[Master of Death]] —expected him at the rendezvous→ [[Christolf Nightfall]]
- [[Christolf Nightfall]] —his Greater Zombie assistant→ [[Nastil]]
- [[Christolf Nightfall]] —stole the body→ [[Dagin Tillmore]]
- [[Christolf Nightfall]] —reanimated→ [[Corthos]]

### Corthos

**Type:** Non-player character · **Also called:** Corthis · **First seen:** [[Session 29]]
#### Summary

Ancient Goliath hero entombed in honey at [[Quithos the Breaker]]'s tomb. His body was targeted by the [[Skeletal Hand]] for reanimation.

#### Connections

- [[Christolf Nightfall]] —reanimated→ [[Corthos]]
- [[Corthos]] —entombed in his tomb→ [[Quithos the Breaker]]

### Countess Opal Darham

**Type:** Non-player character · **Also called:** Opal Darham
#### Summary

Ruler of [[Darham Hold]]. Her guards say the Eisenberg lords forfeited the land by failing to protect it ([[Session 17]]). See [[Darham Hold Unrest]].

#### Connections

- [[Countess Opal Darham]] —rules→ [[Darham Hold]]

### Daddy Dildo Daggins

**Type:** Non-player character · **Also called:** Daggins · **First seen:** [[Session 09]]
#### Summary

Collector and researcher in [[Truemetal Halls]]. Investigated [[Axeholm]] and the journal cipher. Murdered in his home; his Axeholm research disappeared.

#### Facts by session
- [[Session 38]]: [fact] Revealed to have been a member ("Brother Daggins") of the [[Union of Many]], a fertility and love order. This explains his collection of fertility statues. He entrusted a silver dildo to [[Deanira]].

#### Connections

- [[Daddy Dildo Daggins]] —deciphered→ [[Daggins's Journal]]
- [[Daddy Dildo Daggins]] —victim→ [[Daggins Murder]]
- [[Daddy Dildo Daggins]] —"Brother Daggins"→ [[Union of Many]]

### Dagin Tillmore

**Type:** Non-player character · **Also called:** Daggen, Dagin
#### Summary

Dwarf who fell from a ladder hanging market banners in [[Truemetal Halls]] and died ([[Session 09]]); the foreman called him "Daggen". His city-funded cremation was handled by [[Christolf Nightfall]] ([[Session 16]]), but his distinctively scarred arm turned up on the poisonous flesh golem ([[Session 14]]). See [[Flesh Golems and Poison Mine]].

#### Connections

- [[Christolf Nightfall]] —stole the body→ [[Dagin Tillmore]]
- [[Dagin Tillmore]] —arm used in a golem→ [[Flesh Golems and Poison Mine]]

### Deanira

**Type:** Player character · **Party member** · **First seen:** [[Session 01]]
#### Summary

**Role:** Player character  
**Species:** Satyr

#### Backstory
Deanira was raised communally in a coastal village where tides were strange and the stars did not match the charts. She was close to [[Val]], an older satyr cartographer who searched for a mysterious floating island whose position constantly changed. Val believed ruins there could explain the origin of the world and the changing stars. Val eventually disappeared.

Deanira now travels the Icemoor region, improving her cartography skills and searching for clues to the island and Val.

#### Important relationships
- [[WISC]], [[Furgus]], [[Riffle]], [[Philip]]
- [[Val]] — missing mentor/father figure.
- [[Agatha]] — exchanged information with her.
- [[Oma]] — met during the Venburg festival.

#### Notable events
- Experienced a vision involving a ship, changing stars, a storm, and a mysterious webbed hand.
- Has repeatedly encountered [[Cornhusk Dolls]].
- Was bitten by the were-bears but did not develop the same persistent symptoms as WISC/Furgus.

#### Facts by session
- [[Session 37]]: [[Samuel Patel]] found a minor curse on her. At the Student Health Clinic the [[Mask of the Green Dragon]] was removed, and she suddenly felt much better about [[WISC]].
- [[Session 37]]: Bought maps of four other continents from a cartography shop. The shop had charted nothing in the Feywild and knew nothing of an unchartable island, so she questioned sailors (see [[Floating Island Mystery]]).
- [[Session 37]]: Wants to continue Daggins's work collecting fertility statues from around the world.
- [[Session 38]]: Met the [[Union of Many]] in the basement of [[The Two Tits]] and confirmed [[Daddy Dildo Daggins]] was a member. Showed [[Atheela]] the silver dildo Daggins entrusted to her.
- [[Session 38]]: Bought a gold and blue feathered ballgown and a collar of fine jewels for the [[Academy Gala]].

#### Connections

- [[Deanira]] —searching→ [[Floating Island Mystery]]
- [[Deanira]] —missing mentor→ [[Val]]
- [[Deanira]] —carrying on Daggins's work→ [[Union of Many]]
- [[Deanira]] —mentor, missing→ [[Val]]

### Ea

**Type:** Non-player character · **First seen:** [[Session 15]]
#### Summary

Young Tiefling rescued after encountering the flesh golem near [[Darham Hold]].

### Earl Emberstone

**Type:** Non-player character · **First seen:** [[Session 08]]
#### Summary

Parent of [[Elzock Emberstone]]. His family rewarded the party after Elzock's rescue.

#### Connections

- [[Earl Emberstone]] —father of→ [[Elzock Emberstone]]
- [[Earl Emberstone]] —connected to→ [[Ring of Gold]]

### Elzock Emberstone

**Type:** Non-player character · **Also called:** Elzock, Elzoc · **First seen:** [[Session 05]]
#### Summary

Dwarf rescued from the underground tunnels. Son of [[Earl Emberstone]]. Later rewarded the party and returned to his family in the [[Ring of Gold]].

#### Connections

- [[Earl Emberstone]] —father of→ [[Elzock Emberstone]]

### Ester

**Type:** Non-player character · **Also called:** Esther · **First seen:** [[Session 36]]
#### Summary

Chief Archivist at the [[Library of Deneir]] in [[Amberhold]].

#### Facts by session
- [[Session 37]]: [suspicion] Told [[Riffle]] the robes were changed from red to purple 50–60 years ago, because the Headmaster at the time preferred a different colour. Some people may have kept their old red robes. (Relevant to the [[Daggins Murder]].)

#### Connections

- [[Ester]] —Chief Archivist→ [[Library of Deneir]]

### Evelyn Keep

**Type:** Non-player character · **First seen:** [[Session 36]]
#### Summary

Innkeeper of the [[Cock and Pig]] in the Merchant District of [[Amberhold]].

### Fizz

**Type:** Non-player character · **First seen:** [[Session 15]]
#### Summary

Goblin proprietor of [[Fizz and Ugly's Travelling Store]].

### Furgus

**Type:** Player character · **Party member** · **First seen:** [[Session 03]]
#### Summary

**Role:** Player character  
**Species:** Herrengon

#### Known history
- Family is based in [[Venburg]].
- Furgus has an archaeology background.
- Furgus's parents, brother [[Bad]], sister-in-law [[Annika]], and nieces/nephews [[James]] and [[Julia]] live in Venburg.

#### Important relationships
- [[WISC]], [[Deanira]], [[Riffle]], [[Philip]]
- [suspicion] [[Uthal]] — complicated relationship with possible romantic undertones.
- [[Oma]] — part of WISC's family circle.

#### Notable events
- Received a chromatic-dragon-skin magical quiver from the Emberstone family.
- Became involved in the [[Werebear Curse]] investigation.
- Helped recover prisoners from [[Quithos the Breaker]]'s tomb.

#### Facts by session
- [[Session 37]]: Cured of lycanthropy at the [[Temple of Mistra]] ([[Werebear Curse]]).
- [[Session 37]]: Spotted the hint of a [[Skeletal Hand]] tattoo on the blond young man at the tavern (see [[Blond Skeletal Hand Recruiter]]).

#### Connections

- [[Furgus]] —complicated…→ [[Uthal]]
- [[Furgus]] —brother→ [[Bad]]
- [[Furgus]] —cured S37→ [[Werebear Curse]]
- [[Furgus]] —complicated→ [[Uthal]]

### Gavin Gosling

**Type:** Non-player character
#### Summary

Former head of [[Mistra's Academy]]. His death was reported in [[Session 26]], and [[Bianca Onyxcrest]] succeeded him as Headmistress ([[Session 36]]).

#### Connections

- [[Gavin Gosling]] —former head, died→ [[Mistra's Academy]]

### Glasses

**Type:** Non-player character · **First seen:** [[Session 02]]
#### Summary

Gnome wizard and member of [[The Bastard's Band]].

### Gunther Rockhammer (Tanner)

**Type:** Non-player character · **First seen:** [[Session 24]]
#### Summary

Owner of a tannery in [[Truemetal Halls]], on the same level of the city as [[Christolf Nightfall]]'s undertaker shop. **A different person from [[Gunther Rockhammer]], who runs [[The Warhammer]]**, despite having the same name ([[Session 24]]).

- [[Session 24]]: [reported] The young Dwarf calling himself [[Hector]] said he worked here.
- [[Session 25]]: The party visited. This Gunther called out for Hector, and the boy looked exactly like the one who had poisoned them, but he had spent that night playing a game ("Humans and Households"). The party concluded someone had been pretending to be Hector.

### Gunther Rockhammer

**Type:** Non-player character · **Also called:** Gunther · **First seen:** [[Session 02]]
#### Summary

Owner of [[The Warhammer]] in [[Truemetal Halls]]. Provides jobs and serves as a contact with the city and [[Court]].

#### Connections

- [[Gunther Rockhammer]] —runs→ [[The Warhammer]]

### Hambrick Onyxcrest

**Type:** Non-player character · **Also called:** Onyxcrest · **First seen:** [[Session 02]]
#### Summary

Wizard and proprietor of a magic shop in [[Truemetal Halls]]. Identified the [[Mystery Stone]] as an 'onion' layered with spells.

### Hana Goldfirm

**Type:** Non-player character · **Also called:** Hannah, Hana · **First seen:** [[Session 23]]
#### Summary

Researcher and close friend of [[Riffle]]. Works within the [[Department of Acquisitions]]. Her office in [[Amberhold]] was broken into and some items were stolen.

#### Connections

- [[Riffle]] —best friend, smitten→ [[Hana Goldfirm]]
- [[Hana Goldfirm]] —holds the last copy→ [[Daggins's Journal]]
- [suspicion] [[Hana Goldfirm]] —her office was also burgled?→ [[Talir's Stolen Documents]]
- [[Hana Goldfirm]] —researcher→ [[Department of Acquisitions]]
- [[Riffle]] —best friend→ [[Hana Goldfirm]]

### Hector

**Type:** Non-player character · **First seen:** [[Session 24]]
#### Summary

Young Dwarf from [[Truemetal Halls]] who appeared friendly but was later impersonated in connection with the poisoning mystery.

#### Connections

- [[Hector]] —impostor poisoned the party that night→ [[Daggins Murder]]

### Hilda

**Type:** Non-player character · **First seen:** [[Session 06]]
#### Summary

Halfling proprietor of the [[Black Dragon Inn]], missing both legs. Has unusual dragon-wing trophies and magical expertise.

### Ilkan

**Type:** Non-player character · **First seen:** [[Session 11]]
#### Summary

Leader of the Goliath raiders in the mountains. Replaced Uthal's father and turned the group toward raiding. Worked with a scouting druid named [[Alkan]].

### James

**Type:** Non-player character
#### Summary

Baby nephew or niece of [[Furgus]], child of [[Bad]] and [[Annika]], in [[Venburg]] ([[Session 31]]).

### Jane Pedimore

**Type:** Non-player character · **Also called:** Jane · **First seen:** [[Session 32]]
#### Summary

Young Halfling from [[Copperhead Hollow]] whose family was murdered after refusing protection demands from a golden-eyed bugbear.

### Julia

**Type:** Non-player character
#### Summary

Baby niece or nephew of [[Furgus]], child of [[Bad]] and [[Annika]], in [[Venburg]]. WISC played with Julia during the visit ([[Session 31]]).

### Karyn

**Type:** Non-player character · **First seen:** [[Session 38]]
#### Summary

Staff member at [[Mistra's Academy]] and assistant to [[Bianca Onyxcrest]].

- [[Session 38]]: Stressed and overworked preparing the [[Academy Gala]] and the [[Gauntlet]]. [[Riffle]] brought her a sandwich and coffee and helped tidy her office, and glimpsed details of the Gauntlet while doing so.

#### Connections

- [[Karyn]] —Bianca's assistant→ [[Bianca Onyxcrest]]

### Klaus

**Type:** Non-player character · **Also called:** Claus · **First seen:** [[Session 31]]
#### Summary

Hill Dwarf who has been the elected leader of [[Venburg]] for 27 years, and does a good job keeping the town running. The notes write the name both **Klaus** and **Claus**.

- [[Session 31]]: More stressed than ever, with refugees from around [[Eisenberg]] swelling the town. He was so delighted by news of [[Lord Ivan Deepshaft]]'s supply carts that he yodelled at length.
- [[Session 32]]: Pointed the party to [[Theo'din Corvis]], who had come looking for them.
- [[Session 33]]: Asked the party to deal with the bear near [[Hawk's Nest]], worried for the town's free-ranging hogs.
- [[Session 35]]: Lit the festival effigy of Melora.

#### Connections

- [[Klaus]] —elected leader→ [[Venburg]]

### Lord Ivan Deepshaft

**Type:** Non-player character · **Also called:** Lord Deepshaft, Ivar Deepshaft · **First seen:** [[Session 08]]
#### Summary

Member of the [[Court]]. Investigated the party's discovery of the Duergar mining operation and later commissioned the delivery of supplies to [[Venburg]].

#### Connections

- [[Lord Ivan Deepshaft]] —member→ [[Court]]
- [[Lord Ivan Deepshaft]] —sent supply carts→ [[Venburg]]

### Mary Salter

**Type:** Non-player character · **First seen:** [[Session 07]]
#### Summary

Oswald's partner/wife and the person the party was asked to contact after his death.

### Mika

**Type:** Non-player character
#### Summary

Runs the blacksmith [[Baptism by Fire]] in [[Truemetal Halls]] with partner [[Siri]]. They repaired WISC's half plate ([[Session 14]]).

### Mittens

**Type:** Non-player character · **Also called:** Mitt · **First seen:** [[Session 18]]
#### Summary

Tabaxi encountered at [[Bog's Rest]]. Provided news about [[Amberhold]] and the upcoming [[Gauntlet]].

### Morgran Ironoak

**Type:** Non-player character · **Also called:** Morgren Ironoak
#### Summary

Runs the apothecary shop in [[Truemetal Halls]]. He hired the party to collect a shipment of ingredients from [[Wren Nalore]] (spelled "Renn Nalore" in [[Campaign Setup]]), paying 100 gp each on completion, an advance of healing potions, and 50 gp per basilisk egg and 10 gp per vial of basilisk blood. See [[Apothecary Shipment]].

[inference] He is probably the "Alchemist" who offers and pays for this job in [[Session 09]] and [[Session 24]], but the sessions never name that person. The spelling is "Morgran" in [[Campaign Setup]] and "Morgren" in [[Session 18]].

### Nastil

**Type:** Non-player character · **First seen:** [[Session 16]]
#### Summary

"Assistant undertaker" to [[Christolf Nightfall]] in [[Truemetal Halls]]. Pale, breathless and incurious; he was undead. The party fought him in [[Session 16]], and [[Lord Ivan Deepshaft]] later said he was a Greater Zombie, which requires someone of note to make ([[Session 25]]).

#### Connections

- [[Christolf Nightfall]] —his Greater Zombie assistant→ [[Nastil]]

### Olga

**Type:** Non-player character · **First seen:** [[Session 24]]
#### Summary

Barmaid at [[The Warhammer]] who checked on [[Daddy Dildo Daggins]] for the party and brought him food. She last saw him excited to tell them something, and arrived just after the party found his body ([[Session 24]], [[Session 25]]).

### Oma

**Type:** Non-player character · **Also called:** WISC's Grandmother, WISC's grandmother · **First seen:** [[Session 31]]
#### Summary

[[WISC]]'s grandmother, who raised him in a cabin in the woods near [[Venburg]] with a barn, pigs and a pumpkin patch. Her late partner was Clarence. She dotes on WISC ("WISCchenzo"), nags him and [[Furgus]] about settling down, and turns sour when asked how WISC's parents met. [[Uthal]] now works for her.

- [[Session 31]]: WISC dreamt she cast Finger of Death on Riffle, then brought the party home for real.
- [[Session 35]]: WISC left her a letter and 100 gold with [[Uthal]], to be delivered only if he doesn't return.

#### Connections

- [[WISC]] —grandmother→ [[Oma]]
- [[WISC]] —grandson→ [[Oma]]
- [[Uthal]] —works for→ [[Oma]]

### Oswald

**Type:** Non-player character · **Also called:** Amex Oswald · **First seen:** [[Session 07]]
#### Summary

Ghost encountered at [[Unfinished Business]]. Asked the party to tell [[Mary Salter]] about his death and avenge his family's killers.

### Peter Owens

**Type:** Non-player character · **Also called:** Peter, Peter Owen · **First seen:** [[Session 36]]
#### Summary

Graduate student at [[Mistra's Academy]] (School of Conjuration, per [[Session 36]]). Son of the late Lord Richard Owens, the merchant whose death has left a ship stuck in port because its cargo can't be unloaded into his warehouse.

The notes spell the family name both **Owens** ([[Session 36]]) and **Owen** ([[Session 38]]).

- [[Session 36]]: [[Riffle]] remembered the son's name only as "something with a P".
- [[Session 38]]: [reported] Both his parents recently died, and he has taken a leave of absence. Students say he has been visiting the [[Owens Family Mausoleum]] more often, which they find strange because he wasn't close to his parents. They describe him as strange, with "icky weird vibes". He lives in an apartment off campus. See [[Owens Family Deaths]].

**Possible link (unconfirmed):** the [[Skeletal Hand]] recruiter in [[Session 30]] was described as a blond youth named Peter. See [[Blond Skeletal Hand Recruiter]].

#### Connections

- [suspicion] [[Peter Owens]] —the "Peter"?→ [[Blond Skeletal Hand Recruiter]]
- [[Peter Owens]] —parents just died→ [[Owens Family Deaths]]
- [[Peter Owens]] —visiting often→ [[Owens Family Mausoleum]]
- [[Peter Owens]] —grad student, on leave→ [[Mistra's Academy]]
- [suspicion] [[Peter Owens]] —the recruiter 'Peter'?→ [[Skeletal Hand]]

### Philip

**Type:** Player character · **Party member** · **First seen:** [[Session 33]]
#### Summary

**Role:** Player character / party member

Hunter from [[Venburg]], helped to bring food for the village, first to be attacked by the wearbear stonegiants.

Philip appears in later campaign notes as part of the adventuring party, including the journey to [[Amberhold]] and the [[Gauntlet]] preparations. Earlier notes do not establish a detailed biography.

#### Connections

- [[Philip]] —hunter from→ [[Venburg]]

### Queen

**Type:** Non-player character · **Also called:** Queen the mouser · **First seen:** [[Session 31]]
#### Summary

Large Maine Coon-type cat and chief mouser in [[Venburg]].

### Quithos the Breaker

**Type:** Non-player character · **Also called:** Quithos, Tomb of Quithos the Breaker
#### Summary

Legendary Goliath hero who drove the Minotaurs out of the north centuries ago. He was entombed in honey with Minotaur captives as guardians, near [[Venburg]] ([[Session 25]]). In [[Session 29]], the party found the entombed Goliath was [[Corthos]], reanimated by [[Christolf Nightfall]] for the [[Skeletal Hand]].

#### Connections

- [[Corthos]] —entombed in his tomb→ [[Quithos the Breaker]]
- [[Skeletal Hand]] —held captives here→ [[Quithos the Breaker]]

### Ree Tealeaf

**Type:** Non-player character · **First seen:** [[Session 02]]
#### Summary

Associated with [[Junk in the Trunk]], the curiosity shop in [[Truemetal Halls]] that supplied [[Daddy Dildo Daggins]].

### Riffle

**Type:** Player character · **Party member** · **First seen:** [[Session 09]]
#### Summary

**Role:** Player character  
**Species:** Kenku  
**Class:** Cleric of [[Deneir]]

#### Affiliations
- [[Library of Deneir]]
- [[Department of Acquisitions]]
- Connected to [[Mistra's Academy]]
- [[Talir Rengavi]] is a father-figure.
- [[Hana Goldfirm]] is Riffle's close friend/researcher.

#### Backstory
Riffle serves as a clandestine collector of knowledge, artifacts, and secrets for the Library. During a past journey with Talir, a fire injured Riffle while they rescued Talir. Riffle describes the burn as the price paid to become a cleric.

#### Major threads
- [[Axeholm]]
- [[Skeletal Hand]]
- [[Master of Death]]
- [[Daddy Dildo Daggins]]
- [[Mystery Stone]]
- [suspicion] Suspicion that the conspiracy may involve [[Amberhold]], [[Mistra's Academy]], or the [[Library of Deneir]] itself.

#### Notes
Riffle is highly inquisitive, prone to theft and mischief, and has accumulated a substantial number of secrets.

#### Facts by session
- [[Session 37]]: Asked [[Talir Rengavi]] to read the scholarship flyer. Talir thought Riffle was admitting they couldn't read and apologised for being a "bad" father; the misunderstanding was cleared up.
- [[Session 37]]: Learned of the [[Sect of Torm]] attacks on alcohol shops.
- [[Session 37]]: [suspicion] Learned from [[Ester]] that the old red robes were changed to purple 50–60 years ago and some people may have kept theirs. The person seen at Daggins's murder wore red robes (see [[Daggins Murder]]).
- [[Session 38]]: [reported] Met [[Sabrina]] outside the [[Velvet Glove Brothel]], who described a blond young man named [[Andrew]].
- [[Session 38]]: Upset with Theo for getting the party thrown out of [[Heaven's Touch]].
- [[Session 38]]: Helped [[Karyn]] and glimpsed details of the [[Gauntlet]].
- [[Session 38]]: Accused by Talir, via Sending, of stealing documents from his safe. See [[Talir's Stolen Documents]].

#### Connections

- [[Riffle]] —father figure→ [[Talir Rengavi]]
- [[Riffle]] —best friend, smitten→ [[Hana Goldfirm]]
- [[Riffle]] —accused→ [[Talir's Stolen Documents]]
- [[Riffle]] —competing for the Library→ [[Gauntlet]]
- [[Daggins Murder]] —framed: blood letters RI…F, black feathers→ [[Riffle]]
- [[Talir's Stolen Documents]] —accused: Siobhan's sighting→ [[Riffle]]
- [[Riffle]] —field agent→ [[Department of Acquisitions]]
- [[Riffle]] —best friend→ [[Hana Goldfirm]]

### Rupert Bubblegum

**Type:** Non-player character · **Also called:** Mr. Bubblegum
#### Summary

Gnome with fuzzy pink hair and the deepest voice the party has ever heard. He runs [[The Shooting Star]] magic shop in [[Truemetal Halls]] and couldn't identify the stone ([[Session 08]]).

### Sabrina

**Type:** Non-player character · **First seen:** [[Session 35]]
#### Summary

Tiefling bartender at the [[Velvet Glove Brothel]] in [[Amberhold]] and acquaintance of [[Riffle]].

#### Facts by session
- [[Session 38]]: Met [[Riffle]] outside the brothel to discuss the rivalry with [[Heaven's Touch]]. Mentioned a young blond man named [[Andrew]] who saw a worker named Angela.

### Samuel Patel

**Type:** Non-player character · **Also called:** Head Cleric of Mistra · **First seen:** [[Session 37]]
#### Summary

Head Cleric at the [[Temple of Mistra]] in [[Amberhold]]. [[Bianca Onyxcrest]] asked him to prepare the spells that cured [[WISC]] and [[Furgus]] of the [[Werebear Curse]].

- [[Session 37]]: [reported] Told [[Deanira]] she had a minor curse on her and sent her, with a letter, to the Student Health Clinic, where the [[Mask of the Green Dragon]] was removed.

#### Connections

- [[Samuel Patel]] —Head Cleric→ [[Temple of Mistra]]

### Sana Valxia

**Type:** Non-player character · **First seen:** [[Session 18]]
#### Summary

Religious leader at the [[Temple of the Wild Mother and Lawbringer]] in [[Wren Nalore]]. Accepted the goblin child into the temple.

### Sherlock Gnomes

**Type:** Non-player character · **First seen:** [[Session 25]]
#### Summary

Investigator who interviewed the party after [[Daddy Dildo Daggins]]'s murder and suspected someone was impersonating [[Riffle]].

#### Connections

- [[Sherlock Gnomes]] —concluded Riffle is being framed→ [[Daggins Murder]]

### Siobhan

**Type:** Non-player character · **Also called:** Archivist Siobhan · **First seen:** [[Session 38]]
#### Summary

Archivist at the [[Library of Deneir]].

- [[Session 38]]: [reported] According to [[Talir Rengavi]], Siobhan saw [[Riffle]] enter Talir's office the afternoon documents were stolen from his safe. See [[Talir's Stolen Documents]].

#### Connections

- [[Siobhan]] —witness→ [[Talir's Stolen Documents]]
- [[Siobhan]] —Archivist→ [[Library of Deneir]]

### Siri

**Type:** Non-player character
#### Summary

Runs the blacksmith [[Baptism by Fire]] in [[Truemetal Halls]] with partner [[Mika]] ([[Session 14]]).

### Talir Rengavi

**Type:** Non-player character · **Also called:** Talir, Tallir · **First seen:** [[Session 23]]
#### Summary

Director of the [[Library of Deneir]] and a father figure to [[Riffle]]. He can arrange magical transportation and has access to major institutional resources.

#### Facts by session
- [[Session 37]]: Misread Riffle asking him to read a flyer as an admission Riffle can't read, and apologised for failing as a father.
- [[Session 38]]: Very stressed and overworked preparing the [[Academy Gala]] and [[Gauntlet]].
- [[Session 38]]: Sent Riffle an angry Sending demanding the return of documents stolen from his safe, citing Archivist [[Siobhan]] as a witness. See [[Talir's Stolen Documents]].

#### Connections

- [[Riffle]] —father figure→ [[Talir Rengavi]]
- [[Talir Rengavi]] —victim→ [[Talir's Stolen Documents]]
- [[Talir Rengavi]] —Director→ [[Library of Deneir]]

### The Bastard

**Type:** Non-player character · **Also called:** Bastard · **First seen:** [[Session 02]]
#### Summary

Leader of [[The Bastard's Band]]. His party later lost [[The Poet]] to the Duergar's paralytic mushroom operation and sought help in [[Emerald Glade]].

### The Poet

**Type:** Non-player character · **Also called:** Poet · **First seen:** [[Session 02]]
#### Summary

Member of [[The Bastard's Band]]. Died after being attacked during the party's encounter with the Duergar mushroom operation.

### Theo'din Corvis

**Type:** Non-player character · **Party member** · **Also called:** Theo’din Corvis, Theo'din, Theo · **First seen:** [[Session 32]]
#### Summary

Shadar-kai associated with the [[Raven Queen]]. Joined the party later and investigated northern necromancy. His mother made a deal with the Raven Queen to survive a near-death experience while pregnant with twins. The price was one twin, collected on their first birthday, and that twin was Theo'din himself ([[Session 32]]).

#### Facts by session
- [[Session 37]]: Visited the [[Temple of the Raven Queen]] to confirm he is on the right path. Communed with the [[Raven Queen]], who appeared in a white mask, black dress and cloak of raven feathers, and recalled the tenets of the Order of the Black Feathers (see [[Raven Queen's servants]]). He feels the party, though "pretty whack", shares his goals. Left a [[Cornhusk Dolls|cornhusk doll]] in the temple.
- [[Session 38]]: Sensed an enchantment over the people in [[Heaven's Touch]]. Tried to Dispel Magic on [[Zelda]] and was escorted out (see [[Heaven's Touch Enchantment]]).

#### Connections

- [[Theo'din Corvis]] —patron→ [[Raven Queen]]
- [[Theo'din Corvis]] —Order of the Black Feathers→ [[Raven Queen's servants]]

### Tiny

**Type:** Non-player character · **First seen:** [[Session 02]]
#### Summary

Goliath cleric and member of [[The Bastard's Band]].

### Ugly

**Type:** Non-player character · **First seen:** [[Session 15]]
#### Summary

Large half-giant/ogre-like companion of [[Fizz]] and proprietor of the travelling interdimensional shop.

### Uthal

**Type:** Non-player character · **First seen:** [[Session 11]]
#### Summary

Goliath former raider who defected from [[Ilkan]]'s group and helped the party infiltrate their camp. Riffle killed him during the infiltration, but Uthal survived by rolling a natural 20 on death saves. Later sought work with [[Oma]].

#### Connections

- [[Furgus]] —complicated…→ [[Uthal]]
- [[Uthal]] —works for→ [[Oma]]
- [[Furgus]] —complicated→ [[Uthal]]

### Val

**Type:** Non-player character · **First seen:** [[Session 07]]
#### Summary

Deanira's cartographer mentor who disappeared while searching for a shifting floating island.

#### Facts by session
- [[Session 37]]: [[Deanira]] gathered sailors' sightings of a vanishing island. See [[Floating Island Mystery]].

#### Connections

- [[Deanira]] —missing mentor→ [[Val]]
- [[Deanira]] —mentor, missing→ [[Val]]

### Vistra

**Type:** Non-player character · **First seen:** [[Session 16]]
#### Summary

Dwarven priest in [[Truemetal Halls]] who provided information about [[Christolf Nightfall]].

### WISC

**Type:** Player character · **Party member** · **First seen:** [[Session 03]]
#### Summary

**Role:** Player character  
**Species:** Bugbear

#### Known history
- WISC's father left before WISC was a baby.
- WISC grew up around [[Venburg]] and [[Oma]].
- A rare eye colour links WISC to another golden-eyed bugbear.
- [reported] A woman from [[Copperhead Hollow]] reported a golden-eyed bugbear extorting protection taxes and murdering her family. She initially believed WISC was that bugbear.

#### Important relationships
- [[Furgus]] — long-time adventuring companion.
- [[Deanira]] — party member.
- [[Riffle]] — party member; often suspicious of WISC.
- [[Oma]] — grandmother.
- [[Uthal]] — former enemy/ally whose history became entangled with WISC's family.

#### Items / notable events
- Uses the [[Grey Bag of Tricks]].
- Received [[Reaper]] from the Emberstone family.
- Was affected by the [[Werebear Curse]].
- Has repeatedly interacted with [[Cornhusk Dolls]].

#### Open threads
- Identity and origin of the golden-eyed bugbear.
- WISC's missing father.
- Whether the golden-eyed bugbear is related to WISC.

#### Facts by session
- [[Session 37]]: Cured of lycanthropy at the [[Temple of Mistra]] ([[Werebear Curse]]).

#### Connections

- [[WISC]] —shares the rare eyes→ [[Golden-Eyed Bugbear Mystery]]
- [[WISC]] —grandmother→ [[Oma]]
- [[WISC]] —cured S37→ [[Werebear Curse]]
- [[WISC]] —grandson→ [[Oma]]
- [[WISC]] —same rare eyes→ [[Golden-Eyed Bugbear Mystery]]

### Wetel

**Type:** Non-player character · **First seen:** [[Session 17]]
#### Summary

Pixie who gave [[Deanira]] a bag for generating more [[Cornhusk Dolls]] as a prank.

### Wolf

**Type:** Non-player character · **First seen:** [[Session 08]]
#### Summary

Bugbear hunter from [[Venburg]] rescued from captivity in [[Quithos the Breaker]]'s tomb.

### Zeke

**Type:** Non-player character · **First seen:** [[Session 28]]
#### Summary

Goblin mercenary from [[Venburg]] who was captured and transported to [[Quithos the Breaker]]'s tomb.

### Zelda

**Type:** Non-player character · **First seen:** [[Session 38]]
#### Summary

Brothel worker who moved from the [[Velvet Glove Brothel]] to [[Heaven's Touch]] a few weeks before [[Session 38]].

- [[Session 38]]: [reported] [[Riffle]] recognised her at Heaven's Touch. She said she needed a change of scenery and that it "just felt so nice here". She appeared to be enchanted; [[Theo'din Corvis]] tried to cast Dispel Magic on her. See [[Heaven's Touch Enchantment]].

## Places

### Admiral's Point

**Type:** Place (port)
#### Summary

Place with an island to its south, home to a holy pool tended by a religious order of [[Sune]] ([[Session 34]]). One of three blessed-water sites for a [[Wolfsbane Potion]].

### Ambercrown Kingdom

**Type:** Place · **Also called:** Ambercrown
#### Summary

Kingdom ruled by King Xavier, who took the throne shortly before its war with the [[Dragon League]] about 15–20 years ago. The war lasted only a few months and the Dragon League lost ([[Session 36]]). This year the King's birthday coincides with the Harvest Moon festival, making for a bigger celebration in [[Amberhold]] ([[Session 24]]).

### Amberhold

**Type:** Place (major city) · **First seen:** [[Session 13]]
#### Summary

Major southern city and home of [[Riffle]]'s [[Library of Deneir]], [[Mistra's Academy]], the Mage's District, and the upcoming [[Gauntlet]].

#### Facts by session
- [[Session 37]]: A [[Sect of Torm]] has been attacking alcohol shops. The city job board offers the [[Missing Sanitation Workers]] job and a suspicious scholarship flyer (see [[Blond Skeletal Hand Recruiter]]).
- [[Session 37]]–38: New locations include the [[Temple of Mistra]], the [[Temple of the Raven Queen]], and the [[Owens Family Mausoleum]] in the graveyard to the west.

### Axeholm

**Type:** Place (lost city) · **First seen:** [[Session 05]]
#### Summary

Ancient Dwarven city lost beneath the glacier. Once wealthy from gold and jewels. A supernatural greed event preceded the city's sealing and disappearance. The party has several maps, journal fragments, and clues but has not yet reached it.

#### Connections

- [[Mystery of Axeholm]] —goal→ [[Axeholm]]
- [[Zyuir]] —Drow outpost: the key→ [[Axeholm]]
- [[Crystalline Glacier]] —rumoured landmark→ [[Axeholm]]
- [[Coal Caster River]] —city lay along it→ [[Axeholm]]
- [[Axeholm Map]] —inside the mountain→ [[Axeholm]]

### Baptism by Fire

**Type:** Place (blacksmith) · **First seen:** [[Session 14]]
#### Summary

Blacksmith shop near the mine entrance in [[Truemetal Halls]], run by [[Siri]] and [[Mika]].

### Black Dragon Inn

**Type:** Place (inn) · **First seen:** [[Session 06]]
#### Summary

Tudor-style inn with hot springs, unusual magical hospitality, and proprietor [[Hilda]].

### Bog's Rest

**Type:** Place (inn)
#### Summary

Tavern and lodging in [[Wren Nalore]] with a diverse clientele. The party stayed here while waiting on the [[Living Bloom]] ([[Session 18]]).

- [[Session 18]]: Riffle met the Tabaxi [[Mittens]], who brought news of [[Gauntlet|The Gauntlet]] in [[Amberhold]].
- [[Session 19]]: [[Cornhusk Dolls]] resembling each party member appeared outside their doors.

### Coal Caster River

**Type:** Place (river)
#### Summary

River associated with the lost Dwarven city of [[Axeholm]].

#### Connections

- [[Coal Caster River]] —city lay along it→ [[Axeholm]]

### Cock and Pig

**Type:** Place (inn) · **First seen:** [[Session 36]]
#### Summary

Busy sailor inn in the Merchant District of [[Amberhold]].

### Coda's Landing

**Type:** Place (coastal village)
#### Summary

[[Deanira]]'s hometown: a coastal village where the tides were strange, the stars never matched the charts, and children were raised by the whole community. Her mentor [[Val]] sailed from here in search of the [[Floating Island Mystery|floating island]] ([[Session 07]]).

[[Agatha]]'s porridge tasted to Deanira like her favourite fish dish from Coda's Landing ([[Session 21]]).

### Copperhead Hollow

**Type:** Place (settlement)
#### Summary

Settlement south of [[Eisenberg]], where a golden-eyed bugbear murdered [[Jane Pedimore]]'s family after they refused to pay him protection ([[Session 32]]). See [[Golden-Eyed Bugbear Mystery]].

### Crystalline Glacier

**Type:** Place (landmark) · **First seen:** [[Session 14]]
#### Summary

Landmark believed to conceal or mark the buried remains of [[Axeholm]].

#### Connections

- [[Crystalline Glacier]] —rumoured landmark→ [[Axeholm]]

### Darham Hold

**Type:** Place (town) · **First seen:** [[Session 15]]
#### Summary

Fortified settlement under [[Countess Opal Darham]] after the Eisenberg lords allegedly failed to protect the region. Uses an ice-axe banner.

See also: [[Darham Hold Unrest]]

#### Connections

- [[Darham Hold]] —broke from the Eisenberg lords→ [[Eisenberg]]
- [[Countess Opal Darham]] —rules→ [[Darham Hold]]

### Decanter 3 Table

**Type:** Place (wine shop) · **First seen:** [[Session 36]]
#### Summary

Backup wine shop in [[Amberhold]] used by Riffle before dinner with [[Bianca Onyxcrest]].

#### Facts by session
- [[Session 37]]: Many alcohol shops now post visible security because of attacks by the [[Sect of Torm]].

### Derragh

**Type:** Place (city) · **Also called:** Titan Fall
#### Summary

Dwarven city in the far north (Dwarvish for "Titan Fall"), built inside the hollowed-out body of the Lord of Earth ([[Session 24]]). See [[Lords of the Elements]].

### Dunnings Auction House

**Type:** Place (auction house) · **First seen:** [[Session 13]]
#### Summary

Auction house in [[Western Point]]. A future auction was expected to include a [[Quill of Deneir]].

### Eisenberg

**Type:** Place (city) · **First seen:** [[Session 15]]
#### Summary

Major Iron Dwarf city/region. Notes mention an uprising or civil war causing refugees to travel toward [[Venburg]].

#### Connections

- [[Iron Dwarves]] —connected to→ [[Eisenberg]]
- [[Darham Hold]] —broke from the Eisenberg lords→ [[Eisenberg]]
- [[Eisenberg]] —unrest sends refugees to→ [[Venburg]]

### Emerald Glade

**Type:** Place (region) · **First seen:** [[Session 23]]
#### Summary

Region containing the [[Kriptin Forest|Krypton Forest]] / [[Kriptin Forest]] and a rumored holy pool. [[The Bastard's Band]] headed here seeking help for [[The Poet]] and later may be relevant to the [[Werebear Curse]].

### Evermeet

**Type:** Place (island) · **First seen:** [[Session 36]]
#### Summary

Port/island destination represented by an anchor tattoo among sailors in [[Amberhold]].

### First Star

**Type:** Place (tavern) · **First seen:** [[Session 07]]
#### Summary

Alternate/derelict appearance of [[Unfinished Business]].

### Fizz and Ugly's Travelling Store

**Type:** Place (shop)
#### Summary

Interdimensional general store run by [[Fizz]] and [[Ugly]]. A cloth from Ugly's bowler hat becomes a hole in the ground with a ladder down into the shop. The party bought nearly all its unique goods, including [[Dream Weed]] and the [[Unbreakable Vial]] ([[Session 15]]).

### Golden Sea

**Type:** Place (sea) · **First seen:** [[Session 18]]
#### Summary

Sea route near [[Wren Nalore]] used by caravans and travelers.

### Great Chamber

**Type:** Place (district) · **First seen:** [[Session 02]]
#### Summary

Grand chamber inside [[Truemetal Halls]], including the [[Hall of the Four Clans]].

### Hall of the Four Clans

**Type:** Place (landmark) · **First seen:** [[Session 02]]
#### Summary

Hall in [[Truemetal Halls]] where the four major Dwarven clans are represented (see [[Iron Dwarves]] and [[Great Chamber]]). [[Session 04]] mentions clan statues in the city that leave out the [[Duergar]], who aren't considered true Dwarves.

Described in [[Session 02]]: a grand chamber entered through a portcullis past the city's main doors. The floor is a mosaic of the Great Cosmic Wheel. In each corner stands a statue of a dwarf for one of the four major clans of the Icemoor mountains: the [[Iron Dwarves]], [[Ice Dwarves]], [[Fire Dwarves]] and [[Truemetal Dwarves]]. A mithril statue of Moradin, god of the Dwarves, hangs from the ceiling.

### Hawk's Nest

**Type:** Place (landmark) · **First seen:** [[Session 33]]
#### Summary

Rocky area south of the party's location during the were-bear investigation. The party fought three Stone Giant were-bears here.

### Heaven's Touch

**Type:** Place (brothel) · **First seen:** [[Session 35]]
#### Summary

New brothel in [[Amberhold]] competing with the [[Velvet Glove Brothel]]. Known for magically/uncannily matching clients with preferences.

A warehouse by the waterfront, recently converted, and beautiful inside, comparable to the Velvet Glove. Casting magic is forbidden on the premises.

#### Facts by session
- [[Session 38]]: The party visited and were offered a free drink. [[Theo'din Corvis]] sensed an enchantment over the people inside, and former Velvet Glove worker [[Zelda]] seemed enchanted. The party was asked to leave after Theo tried to cast Dispel Magic. See [[Heaven's Touch Enchantment]].

### Junk in the Trunk

**Type:** Place (shop) · **First seen:** [[Session 02]]
#### Summary

Shop in [[Truemetal Halls]] associated with [[Ree Tealeaf]] and historical/odd items. Connected to [[Daddy Dildo Daggins]].

### Kicking Ass

**Type:** Place (pub) · **First seen:** [[Session 16]]
#### Summary

Pub in the miners' area of [[Truemetal Halls]]. [[Elzock Emberstone]] mentioned he'd been frequenting it ([[Session 16]]).

### Kohlemine

**Type:** Place (mine town) · **First seen:** [[Session 17]]
#### Summary

Eastern mining settlement associated with the [[Black Hand Dwarves]] and production of [[Anthracite]].

#### Connections

- [[Black Hand Dwarves]] —mine anthracite at→ [[Kohlemine]]

### Kriptin Forest

**Type:** Place (forest) · **Also called:** Krypton Forest · **First seen:** [[Session 34]]
#### Summary

Forest in the [[Emerald Glade]] containing one of the holy pools identified by [[Hana Goldfirm]].

### Lakeshire

**Type:** Place (town) · **First seen:** [[Session 06]]
#### Summary

Hometown of [[Oswald]] and destination for the message to [[Mary Salter]].

### Living Bloom

**Type:** Place (apothecary supplier) · **First seen:** [[Session 18]]
#### Summary

Apothecary supplier in [[Wren Nalore]]. Provided the ingredients for the party's return trip to [[Truemetal Halls]].

### Mage's District

**Type:** Place (district)
#### Summary

District of [[Amberhold]] surrounding the [[Library of Deneir]] and [[Mistra's Academy]].

### Merchant District

**Type:** Place (district) · **First seen:** [[Session 36]]
#### Summary

Dockside district of [[Amberhold]], including the [[Cock and Pig]].

### Mine District

**Type:** Place (district) · **First seen:** [[Session 36]]
#### Summary

Dense district of [[Amberhold]], where [[The Three Candles]] is located.

### Moaning Gorge

**Type:** Place (region) · **First seen:** [[Session 34]]
#### Summary

Far-northern volcanic valley, home region of the Stone Giant were-bears encountered near [[Hawk's Nest]].

### Moroden's Forge

**Type:** Place (crematory)
#### Summary

Specific crematory/funerary location referenced in the investigation of [[Dagin Tillmore]].

### MurderDrum

**Type:** Place (mountain)
#### Summary

Mountain location described as the Matterhorn where a young half-elf died snowboarding.

### Murderhorn

**Type:** Place (mountain region) · **First seen:** [[Session 08]]
#### Summary

Mountain region north of [[Truemetal Halls]]; maps are unreliable because weather closes passes.

### Owens Family Mausoleum

**Type:** Place (crypt) · **Also called:** Owens Mausoleum, Owen Family Mausoleum · **First seen:** [[Session 38]]
#### Summary

Family mausoleum of the Owens family, in a graveyard to the west outside [[Amberhold]].

- [[Session 38]]: [[Peter Owens]] has been seen visiting more often since his parents died. As the party approached in the rain, a cloaked, hooded figure entered the structure and vanished. See [[Owens Family Deaths]].

#### Connections

- [[Peter Owens]] —visiting often→ [[Owens Family Mausoleum]]

### Ring of Gold

**Type:** Place (district) · **First seen:** [[Session 07]]
#### Summary

Affluent residential district of [[Truemetal Halls]], associated with [[Elzock Emberstone]]'s family.

#### Connections

- [[Earl Emberstone]] —connected to→ [[Ring of Gold]]
- [[Ring of Gold]] —connected to→ [[Truemetal Halls]]

### Savehaven

**Type:** Place (port) · **Also called:** Safehaven · **First seen:** [[Session 36]]
#### Summary

Port mentioned by sailors in [[Amberhold]].

Also written **Safehaven** in [[Session 36]], where sailors say an anchor tattoo means they've been to Safehaven or [[Evermeet]]. The notes treat this as possibly the same port; it isn't confirmed.

### Temple of Mistra

**Type:** Place (temple) · **First seen:** [[Session 37]]
#### Summary

Temple on the campus of [[Mistra's Academy]] in [[Amberhold]]. Head Cleric: [[Samuel Patel]].

- [[Session 37]]: The [[Werebear Curse]] was cured here. Samuel detected a minor curse on [[Deanira]] and referred her to the campus Student Health Clinic, where the [[Mask of the Green Dragon]] was removed.

#### Connections

- [[Mistra's Academy]] —connected to→ [[Temple of Mistra]]
- [[Samuel Patel]] —Head Cleric→ [[Temple of Mistra]]

### Temple of the Raven Queen

**Type:** Place (temple) · **First seen:** [[Session 37]]
#### Summary

Temple of the [[Raven Queen]] in [[Amberhold]]. Has a magical darkness and silence room used to commune with the Matron.

- [[Session 37]]: Recognising [[Theo'din Corvis]]'s raven, the priests discreetly directed him to a side door. He spoke with the Head Priest, then communed with the Raven Queen in the deprivation room. He left one of the [[Cornhusk Dolls]] in the temple.

### Temple of the Wild Mother and Lawbringer

**Type:** Place (temple) · **First seen:** [[Session 18]]
#### Summary

Temple in [[Wren Nalore]] dedicated to the contrast and union of chaos and order in nature. [[Sana Valxia]] accepted the goblin child here.

### The Forge

**Type:** Place (religious district) · **First seen:** [[Session 15]]
#### Summary

Religious/funerary area of [[Truemetal Halls]] where Dwarven bodies are traditionally cremated.

### The Shooting Star

**Type:** Place (magic shop) · **First seen:** [[Session 07]]
#### Summary

Magic item shop in [[Truemetal Halls]] operated by [[Rupert Bubblegum]] / Mr. Bubblegum.

### The Three Candles

**Type:** Place (inn) · **First seen:** [[Session 36]]
#### Summary

Inn in the [[Mine District]] of [[Amberhold]], lit only by three candles, hence the name. The district's buildings lean in so far that the streets feel like a tunnel. [[WISC]] and [[Theo'din Corvis]] lodge here during the festival ([[Session 36]]).

### The Two Tits

**Type:** Place (inn) · **First seen:** [[Session 36]]
#### Summary

Inn on the western side of the market square in [[Amberhold]].

#### Facts by session
- [[Session 37]]: Busy at dinner, with people quietly slipping away in pairs to the basement.
- [[Session 38]]: The basement is where the [[Union of Many]] worship about once a week.

### The Vine's Bounty

**Type:** Place (wine shop)
#### Summary

Riffle's favorite wine shop in [[Amberhold]]. Found boarded up with signs of broken glass shortly before the party's meeting with [[Bianca Onyxcrest]].

#### Facts by session
- [[Session 37]]: [suspicion] The [[Sect of Torm]] has been attacking shops that sell alcohol, which likely explains the damage.

### The Warhammer

**Type:** Place (inn) · **First seen:** [[Session 02]]
#### Summary

Inn and adventurer job hub in [[Truemetal Halls]]. Owned by [[Gunther Rockhammer]].

#### Connections

- [[Gunther Rockhammer]] —runs→ [[The Warhammer]]
- [[The Warhammer]] —connected to→ [[Truemetal Halls]]

### Truemetal Halls

**Type:** Place (major city) · **First seen:** [[Session 02]]
#### Summary

Capital of the northern [[Confederation]]. Built within the mountains around major deposits of mithril and adamantine. Home of [[The Warhammer]], [[Baptism by Fire]], [[The Shooting Star]], [[Junk in the Trunk]], and the [[Ring of Gold]].

#### Relationships
![[Relationships#Dwarven powers and Venburg]]

#### Connections

- [[Confederation]] —capital→ [[Truemetal Halls]]
- [[Truemetal Halls]] —connected to→ [[Court]]
- [[The Warhammer]] —connected to→ [[Truemetal Halls]]
- [[Ring of Gold]] —connected to→ [[Truemetal Halls]]
- [[Truemetal Dwarves]] —connected to→ [[Truemetal Halls]]
- [suspicion] [[Black Hand Dwarves]] —doubled the price; another buyer?→ [[Truemetal Halls]]

### Tryborne Pass

**Type:** Place (mountain pass) · **Also called:** Triborn Pass · **First seen:** [[Session 07]]
#### Summary

Mountain pass where the party discovered the dead [[Oswald]] caravan.

### Unfinished Business

**Type:** Place (planar tavern) · **First seen:** [[Session 07]]
#### Summary

A shifting tavern for souls who have died but are not ready to pass on. The party met [[Anton]] and [[Oswald]] here.

### Valley of Fire

**Type:** Place (region) · **First seen:** [[Session 31]]
#### Summary

Valley containing [[Venburg]]. The surrounding meadow is famous for orange foliage and blueberries.

### Velvet Glove Brothel

**Type:** Place (brothel) · **First seen:** [[Session 35]]
#### Summary

Brothel in [[Amberhold]] where the party accidentally arrived after magical transportation went slightly off target.

#### Facts by session
- [[Session 38]]: [reported] Losing workers such as [[Zelda]] to [[Heaven's Touch]]. [[Sabrina]] reported a young blond man named [[Andrew]] seeing a worker named Angela.

### Venburg

**Type:** Place (town) · **Also called:** Venberg · **First seen:** [[Session 25]]
#### Summary

Winter-oriented fortified community associated with [[WISC]] and [[Furgus]]. Community longhouses, palisades, and strong seasonal traditions. Receives refugees from the [[Eisenberg]] region.

#### Relationships
![[Relationships#Dwarven powers and Venburg]]

#### Connections

- [[Philip]] —hunter from→ [[Venburg]]
- [[Eisenberg]] —unrest sends refugees to→ [[Venburg]]
- [[Klaus]] —elected leader→ [[Venburg]]
- [[Lord Ivan Deepshaft]] —sent supply carts→ [[Venburg]]

### Western Point

**Type:** Place (city) · **First seen:** [[Session 13]]
#### Summary

Southern city containing [[Dunnings Auction House]]. The party may eventually travel there for a Deneir quill and other auction items.

### Wren Nalore

**Type:** Place (city) · **First seen:** [[Session 14]]
#### Summary

City built on a series of small islands connected by bridges. Surrounded by swamps and basilisk habitat. The party was eventually exiled after trouble involving [[Agatha]] and the town authorities.

### Zyuir

**Type:** Place (drow outpost) · **First seen:** [[Session 21]]
#### Summary

Drow outpost. [[Agatha]] identified it as the key to finding the route to [[Axeholm]]. The name appeared in [[Daddy Dildo Daggins]]'s deciphered notes.

#### Connections

- [[Zyuir]] —Drow outpost: the key→ [[Axeholm]]
- [[Agatha]] —told the party→ [[Zyuir]]
- [[Daggins's Journal]] —"Coal Caster = Zyvuir"→ [[Zyuir]]

## Factions

### Black Hand Dwarves

**Type:** Faction · **First seen:** [[Session 10]]
#### Summary

Dwarven group operating [[Kohlemine]] and producing [[Anthracite]]. Their sudden price increase may indicate a hidden buyer.

#### Connections

- [[Black Hand Dwarves]] —mine anthracite at→ [[Kohlemine]]
- [suspicion] [[Black Hand Dwarves]] —doubled the price; another buyer?→ [[Truemetal Halls]]

### Confederation

**Type:** Faction
#### Summary

Largest political body in the northern region, predominantly Dwarven. [[Truemetal Halls]] is its capital.

#### Connections

- [[Confederation]] —capital→ [[Truemetal Halls]]

### Court

**Type:** Faction · **First seen:** [[Session 08]]
#### Summary

Political authority within [[Truemetal Halls]]. [[Lord Ivan Deepshaft]] represents this power structure.

#### Connections

- [[Truemetal Halls]] —connected to→ [[Court]]
- [[Lord Ivan Deepshaft]] —member→ [[Court]]

### Cult of the Destroyer

**Type:** Faction · **First seen:** [[Session 17]]
#### Summary

Historical cult that rose under [[Cidis]], accumulated wealth through taxation and mining, and used slaves. Their operations around the [[Miner's Death Lode]] were abandoned because the poison killed too many workers.

### Department of Acquisitions

**Type:** Faction
#### Summary

Library department composed of multiple research/field teams. [[Hana Goldfirm]] works here with [[Riffle]].

#### Connections

- [[Library of Deneir]] —connected to→ [[Department of Acquisitions]]
- [[Hana Goldfirm]] —researcher→ [[Department of Acquisitions]]
- [[Riffle]] —field agent→ [[Department of Acquisitions]]

### Dragon League

**Type:** Faction · **First seen:** [[Session 21]]
#### Summary

Historical dragon-worshiping organization devoted to [[Tiamat]]. They could control dragons and used them in warfare.

The Dragon League fought the [[Ambercrown Kingdom]] around 15–20 years before the campaign. The notes also describe older Dragon League-related ruins containing:
- a dragon shrine
- a baptismal font
- dragon imagery
- a vault containing magical equipment
- documents and blackmail materials

The party recovered evidence that may connect ancient Dragon League activity to [[Axeholm]].

#### Connections

- [[Dragon League]] —found in their vault→ [[Axeholm Map]]

### Duergar

**Type:** Faction
#### Summary

Underground-dwelling Dwarves, not counted among the true Dwarven clans, in conflict with them for millennia. In the mine below [[Truemetal Halls]] they ran a slave-worked smelting compound, carried lead dagger pendants of [[Abbathor]], and used Knockers to mine [[Mithril]] for an army ([[Session 04]], [[Session 08]]). [[The Bastard's Band]] later disrupted them ([[Session 23]]).

#### Connections

- [[Duergar]] —millennia of conflict→ [[Truemetal Dwarves]]

### Elementalist Syndicate

**Type:** Faction · **First seen:** [[Session 24]]
#### Summary

Mage group formed roughly 3,000 years ago to control powerful elementals. Their experiments produced the [[Lords of the Elements]].

### Fire Dwarves

**Type:** Faction · **First seen:** [[Session 02]]
#### Summary

Dwarves associated with the western volcanic region and the defeat of the [[Lord of Fire]].

### Horizon

**Type:** Faction
#### Summary

Company selling [[Sending Stones]] in [[Amberhold]], including a 150 gp "Party Plan" for unlimited sending within the city ([[Session 35]]).

### Ice Dwarves

**Type:** Faction · **First seen:** [[Session 02]]
#### Summary

One of the four major Dwarven clans of the Icemoor region.

### Iron Dwarves

**Type:** Faction · **First seen:** [[Session 02]]
#### Summary

One of the four major Dwarven clans represented in the [[Hall of the Four Clans]]. Associated with [[Eisenberg]].

#### Connections

- [[Iron Dwarves]] —connected to→ [[Eisenberg]]

### Library of Deneir

**Type:** Faction · **First seen:** [[Session 13]]
#### Summary

Organization dedicated to collecting books, knowledge, artifacts, and secrets. [[Riffle]] is a clandestine field agent. Directed by [[Talir Rengavi]].

#### Facts by session
- [[Session 38]]: [reported] Documents were stolen from [[Talir Rengavi]]'s safe. Archivist [[Siobhan]] claims she saw [[Riffle]] enter his office. See [[Talir's Stolen Documents]].

#### Relationships
![[Relationships#Amberhold institutions]]

#### Connections

- [[Skeletal Hand]] —once part of, banned→ [[Library of Deneir]]
- [[Mistra's Academy]] —the Library is an offshoot→ [[Library of Deneir]]
- [[Library of Deneir]] —connected to→ [[Department of Acquisitions]]
- [[Skeletal Hand]] —banned from→ [[Library of Deneir]]
- [[Talir Rengavi]] —Director→ [[Library of Deneir]]
- [[Ester]] —Chief Archivist→ [[Library of Deneir]]
- [[Siobhan]] —Archivist→ [[Library of Deneir]]

### Mistra's Academy

**Type:** Faction · **First seen:** [[Session 37]]
#### Summary

Major magical academy in [[Amberhold]]. Connected to [[Bianca Onyxcrest]], [[Hambrick Onyxcrest]], and the historical [[Skeletal Hand]].

#### Facts by session
- [[Session 37]]: Campus includes the [[Temple of Mistra]] and a Student Health Clinic. Students range widely in age and background.
- [[Session 38]]: Preparing the [[Academy Gala]] and the [[Gauntlet]]. Graduate student [[Peter Owens]] is on leave after his parents' deaths.

#### Relationships
![[Relationships#Amberhold institutions]]

#### Connections

- [[Skeletal Hand]] —once part of, banned→ [[Mistra's Academy]]
- [[Peter Owens]] —grad student, on leave→ [[Mistra's Academy]]
- [[Mistra's Academy]] —the Library is an offshoot→ [[Library of Deneir]]
- [[Skeletal Hand]] —banned from→ [[Mistra's Academy]]
- [[Mistra's Academy]] —connected to→ [[Temple of Mistra]]
- [[Bianca Onyxcrest]] —Headmistress→ [[Mistra's Academy]]
- [[Gavin Gosling]] —former head, died→ [[Mistra's Academy]]

### Raven Queen's servants

**Type:** Faction · **Also called:** Order of the Black Feathers · **First seen:** [[Session 37]]
#### Summary

Religious network opposing necromancy. [[Theo'din Corvis]] serves the Raven Queen and investigates northern necromantic activity.

#### Facts by session
- [[Session 37]]: [fact] The **Order of the Black Feathers** holds that the dead should stay dead. Calling people back from the Queen's realm through divine intervention may be acceptable, but death should be respected as a process. Followers should intervene against dark magic that steals souls from the beyond or desecrates the bodies left behind. [[Theo'din Corvis]] recalled these tenets while communing at the [[Temple of the Raven Queen]].

#### Connections

- [[Theo'din Corvis]] —Order of the Black Feathers→ [[Raven Queen's servants]]

### Sect of Torm

**Type:** Faction · **Also called:** Followers of Torm, Torm sect · **First seen:** [[Session 37]]
#### Summary

Religious sect worshipping Torm, Lawful Good god of self-discipline. Has been breaking into and destroying establishments in [[Amberhold]] that sell alcohol.

- [[Session 37]]: [reported] [[Riffle]] noticed obvious security outside many wine and alcohol shops; a proprietor explained the sect's attacks.

This likely explains why [[The Vine's Bounty]] was boarded up with broken glass, and why [[Decanter 3 Table]] had a guard at the door ([[Session 36]]). That link is an inference.

### Skeletal Hand

**Type:** Faction · **First seen:** [[Session 28]]
#### Summary

Secret society of necromancers once associated with the [[Library of Deneir]] and [[Mistra's Academy]]. Banned for pushing the boundaries of necromancy. Several members were encountered at [[Quithos the Breaker]]'s tomb.

#### Facts by session
- [[Session 37]]: [suspicion] Appears to recruit in [[Amberhold]] through a coded scholarship flyer and a blond young recruiter. See [[Blond Skeletal Hand Recruiter]].

#### Connections

- [[Master of Death]] —appears to direct→ [[Skeletal Hand]]
- [[Skeletal Hand]] —held captives here→ [[Quithos the Breaker]]
- [[Skeletal Hand]] —once part of, banned→ [[Mistra's Academy]]
- [[Skeletal Hand]] —once part of, banned→ [[Library of Deneir]]
- [[Blond Skeletal Hand Recruiter]] —recruits for→ [[Skeletal Hand]]
- [[Skeletal Hand]] —banned from→ [[Mistra's Academy]]
- [[Skeletal Hand]] —banned from→ [[Library of Deneir]]
- [suspicion] [[Peter Owens]] —the recruiter 'Peter'?→ [[Skeletal Hand]]

### The Bastard's Band

**Type:** Faction · **First seen:** [[Session 02]]
#### Summary

Adventuring party consisting of [[The Bastard]], [[The Poet]], [[Glasses]], and [[Tiny]]. They became involved with the Duergar mine and later headed toward the [[Emerald Glade]].

### Truemetal Dwarves

**Type:** Faction · **First seen:** [[Session 02]]
#### Summary

Major Dwarven clan associated with [[Truemetal Halls]] and its mithril/adamantine economy.

#### Connections

- [[Truemetal Dwarves]] —connected to→ [[Truemetal Halls]]
- [[Duergar]] —millennia of conflict→ [[Truemetal Dwarves]]

### Union of Many

**Type:** Faction · **Also called:** The Union of Many, Daggins' order · **First seen:** [[Session 38]]
#### Summary

Religious order whose members follow many deities of fertility and love, including Shialliah, Lethander and Melorah. They emphasise open love, strong relationships within their community and across deity lines, and living life to the fullest. Their gatherings begin with a Zone of Truth and are restricted to those over 18.

#### Members
- [[Atheela]]
- [[Daddy Dildo Daggins]] ("Brother Daggins"). His collection of fertility statues from many cultures makes sense in this light.

#### Places
- Meets in the basement of [[The Two Tits]] about once a week.

#### History
- [[Session 37]]: [suspicion] [[Deanira]] noticed people with a staff and phallic pins pairing off into the inn's basement and suspected a link to Daggins.
- [[Session 38]]: Deanira met them, confirmed Daggins was a member, and showed Atheela the silver dildo Daggins entrusted to her.

#### Connections

- [[Deanira]] —carrying on Daggins's work→ [[Union of Many]]
- [[Daddy Dildo Daggins]] —"Brother Daggins"→ [[Union of Many]]

## Quests

### Academy Gala

**Type:** Quest · **Status:** upcoming · **Also called:** Gala, The Gala · **First seen:** [[Session 37]]
#### Summary

Gala at [[Mistra's Academy]] to show off the stone from the belly of the ram (the [[Mystery Stone]]) and to kick off the [[Gauntlet]]. It is drawing many alumni donations and much scholarly interest. The party has been asked to represent both the Academy and the [[Library of Deneir]].

- [[Session 36]]: Announced by [[Bianca Onyxcrest]].
- [[Session 37]]: "Shop for the Gala" added to the party's to-do list.
- [[Session 38]]: The party went shopping. [[Deanira]] bought a gold and blue feathered ballgown and a collar of fine jewels. [[Talir Rengavi]] and [[Karyn]] are both overworked preparing it.

### Anthracite Trade Mystery

**Type:** Quest · **Status:** active · **First seen:** [[Session 10]]
#### Objective

Determine why [[Black Hand Dwarves]] doubled the price of [[Anthracite]] and whether another buyer is secretly purchasing it.

#### Clues & findings

[[Anthracite]] is essential for forging [[Mithril]] and adamantine. The [[Black Hand Dwarves]] unexpectedly doubled its price despite historically stable pricing.

This suggests they may have another buyer or are diverting supply.

**Potential links:** [[Kohlemine]], [[Black Hand Dwarves]], [[Truemetal Halls]], [[Mithril]], [[Axeholm]].

### Apothecary Shipment

**Type:** Quest · **Status:** completed
#### Summary

Deliver ingredients from [[Wren Nalore]] / [[Living Bloom]] to the apothecary in [[Truemetal Halls]]. The party also harvested basilisk eggs and blood.

### Daggins Murder

**Type:** Quest · **Status:** active
#### Objective

Determine who murdered [[Daddy Dildo Daggins]], stole his Axeholm research, and attempted to frame [[Riffle]].

#### Clues & findings

[[Daddy Dildo Daggins]] was found dead in his study with a knife in his back. His blood appeared to spell `RI` followed by part of an `F`.

Black feathers surrounded the body, and a witness claimed someone resembling [[Riffle]] entered the house wearing red vestments.

The party determined:
- The feathers were ordinary bird feathers, not Kenku feathers.
- Red Library robes had been discontinued/destroyed about 20 years ago.
- Someone had purchased unusually small black raven feathers from a fletcher.
- Daggins's Axeholm research disappeared.
- [suspicion] [[Sherlock Gnomes]] believes someone was trying to impersonate and frame Riffle.

#### Facts by session
- [[Session 37]]: [suspicion] [[Ester]] dates the change from red to purple robes to **50–60 years ago**, not about 20 years as recorded above. The source notes conflict, so both are kept. She also says some people may have kept their old robes, so the red-robed figure need not be Library staff.
- [[Session 38]]: Daggins was "Brother Daggins" of the [[Union of Many]].
- [[Session 38]]: Riffle is again accused of a theft on the word of a witness. See [[Talir's Stolen Documents]].

#### Connections

- [[Daggins Murder]] —framed: blood letters RI…F, black feathers→ [[Riffle]]
- [[Daddy Dildo Daggins]] —victim→ [[Daggins Murder]]
- [[Daggins Murder]] —Axeholm research taken→ [[Daggins's Journal]]
- [[Sherlock Gnomes]] —concluded Riffle is being framed→ [[Daggins Murder]]
- [[Hector]] —impostor poisoned the party that night→ [[Daggins Murder]]

### Darham Hold Unrest

**Type:** Quest · **Status:** unresolved
#### Summary

Understand why [[Darham Hold]] militarized, why the Eisenberg authorities lost legitimacy, and whether this connects to the wider necromantic disturbances.

### Flesh Golems and Poison Mine

**Type:** Quest · **Status:** active
#### Summary

Investigate the source of necromantic flesh golems made from stolen bodies and the naturally occurring poison associated with a sealed mithril mine.

#### Connections

- [[Dagin Tillmore]] —arm used in a golem→ [[Flesh Golems and Poison Mine]]

### Floating Island Mystery

**Type:** Quest · **Status:** active · **First seen:** [[Session 37]]
#### Objective

Find [[Val]] and the mysterious floating island whose location changes and whose map markings disappear.

#### Clues & findings

[[Val]] searched for a floating island whose position constantly changes. Attempts to map it cause the mark to disappear.

Val believed ruins on the island could explain:
- the origin of the world
- why the stars change

Val disappeared while searching for it.

[[Deanira]] continues to pursue this mystery.

#### Facts by session
- [[Session 37]]: An [[Amberhold]] cartography shop has charted nothing in the Feywild and knows of no unchartable island.
- [[Session 37]]: Sailors near the Barren Toll saw lights that looked like they were coming into port, though they were days from any port. By sunrise nothing was there.
- [[Session 37]]: Two days out from Wellview Helm, sailors saw an island in the distance that was gone the next day.
- [[Session 37]]: [reported] The reported locations are wildly scattered across the map.

#### Connections

- [[Deanira]] —searching→ [[Floating Island Mystery]]

### Gauntlet

**Type:** Quest · **Status:** upcoming · **Also called:** The Gauntlet · **First seen:** [[Session 18]]
#### Summary

Competition at [[Mistra's Academy]] in [[Amberhold]]. The party will compete on behalf of the [[Library of Deneir]], and has also been asked to represent the Academy. Kicked off by the [[Academy Gala]].

#### Rules (from [[Bianca Onyxcrest]], [[Session 36]])
- 5 bouts against creatures. Teams compete independently, not against each other.
- A prize is awarded at the end of each bout.
- About 10–15 minutes between bouts while the arenas reset.
- One short rest allowed across the 5 bouts (via the Cat Nap spell).
- Clerics on hand revive anyone who falls, but a member revived by them is out for the remaining bouts. A member revived by their own party can keep fighting.

#### Known details ([[Session 38]])
[[Riffle]] glimpsed these in [[Karyn]]'s office:
- Four teams in total.
- Five themed rounds: Beasts, Celestials, Fiends, Elementals, and Fey.

#### Connections

- [[Riffle]] —competing for the Library→ [[Gauntlet]]

### Golden-Eyed Bugbear Mystery

**Type:** Quest · **Status:** active
#### Objective

Identify the golden-eyed bugbear who terrorized [[Copperhead Hollow]] and determine whether they are related to [[WISC]].

#### Clues & findings

[[WISC]] shares a rare eye colour with another bugbear encountered indirectly.

[[Jane Pedimore]] reported that a golden-eyed bugbear had extorted protection payments from her family near [[Copperhead Hollow]]. When they refused, her brother, father, and grandfather were killed.

The party suspects this bugbear may be related to WISC.

#### Connections

- [[WISC]] —shares the rare eyes→ [[Golden-Eyed Bugbear Mystery]]
- [[WISC]] —same rare eyes→ [[Golden-Eyed Bugbear Mystery]]

### Master of Death

**Type:** Quest · **Status:** active · **First seen:** [[Session 30]]
#### Objective

Identify the hooded necromancer who summoned [[Christolf Nightfall]] to an extraction point and who appears to direct the [[Skeletal Hand]].

#### Clues & findings

An unidentified male humanoid / human-Elf figure connected to the [[Skeletal Hand]].

##### Observed description
- Late 40s to early 50s.
- Slight greying at temples.
- Clean shaven with slight sideburns.
- Green eyes.
- Appeared extremely annoyed when the party interfered with [[Christolf Nightfall]]'s plans.
- Uses advanced magic including Sending and portals/rifts through reality.

##### Known statement
He appeared at an extraction rendezvous expecting Christolf and complained that the party had interfered. He then opened a rift and disappeared.

#### Facts by session
- [[Session 37]]: [suspicion] Possible lead on Skeletal Hand recruitment in Amberhold: [[Blond Skeletal Hand Recruiter]].

#### Connections

- [[Master of Death]] —expected him at the rendezvous→ [[Christolf Nightfall]]
- [[Master of Death]] —appears to direct→ [[Skeletal Hand]]

### Missing Sanitation Workers

**Type:** Quest · **Status:** active · **Also called:** Sewer missing persons · **First seen:** [[Session 37]]
#### Summary

Find three sanitation workers who vanished in the sewers of [[Amberhold]]. Four people sent to look for them have also disappeared. Posted on the city job board for 200 gp ([[Session 36]]).

- [[Session 37]]: A city representative gave the party the job and they accepted.

### Mystery Stone Investigation

**Type:** Quest · **Status:** active
#### Summary

Determine the nature and significance of the [[Mystery Stone]], now identified as a fragment of the [[Lord of Fire]].

### Mystery of Axeholm

**Type:** Quest · **Status:** active
#### Summary

Find the lost Dwarven city of [[Axeholm]]. Current clues point toward [[Zyuir]] and the [[Crystalline Glacier]].

#### Connections

- [[Mystery of Axeholm]] —goal→ [[Axeholm]]

### Mystery of the Cornhusk Dolls

**Type:** Quest · **Status:** unresolved
#### Summary

Determine who or what keeps leaving [[Cornhusk Dolls]] resembling party members. [[Agatha]] identified them as a fae creation connected to a pixie.

#### Facts by session
- [[Session 37]]: [[Theo'din Corvis]] left a doll in the [[Temple of the Raven Queen]].

### Oswald's Letter to Mary

**Type:** Quest · **Status:** active
#### Summary

Deliver news of [[Oswald]] and Albert's deaths to [[Mary Salter]] in [[Lakeshire]] and eventually avenge their killers.

### Seasonal Festival

**Type:** Quest · **Status:** completed
#### Summary

Attend the family and harvest festival in [[Venburg]].

### Shredding Dude

**Type:** Quest · **Status:** unresolved
#### Summary

Return the body of a young half-elf who died snowboarding at [[MurderDrum]] to [[Amberhold]] for burial in the family mausoleum.

### Southern Auction

**Type:** Quest · **Status:** upcoming · **First seen:** [[Session 13]]
#### Summary

Travel to [[Western Point]] for the [[Dunnings Auction House]] auction, especially the [[Quill of Deneir]].

### Warrior of Kord

**Type:** Quest · **Status:** unresolved
#### Summary

[[Balgus]], a deceased paladin of Kord, wants his body and equipment recovered from a desecrated mountaintop temple guarded by a [[Glabrezu]].

### Werebear Curse

**Type:** Quest · **Status:** resolved · **First seen:** [[Session 34]]
#### Objective

Cure [[WISC]] and [[Furgus]] after their wounds failed to heal following the Stone Giant were-bear encounter. [[Bianca Onyxcrest]] arranged magical treatment.

#### Clues & findings

The party fought Stone Giant were-bears near [[Hawk's Nest]]. [[WISC]] and [[Furgus]] later discovered that their bite wounds were not healing.

Notes establish:
- Lycanthropy can be acquired through a bite.
- A first full moon creates a critical deadline for conventional cures.
- [suspicion] A [[Wolfsbane Potion]] may be possible.
- [suspicion] Possible ingredients include wolfsbane, a stabilizing agent, powdered moonstone/moon seed, lycanthrope blood, and purified/blessed water.
- [[Bianca Onyxcrest]] eventually agreed to arrange magical treatment.

#### Facts by session
- [[Session 37]]: [[WISC]] and [[Furgus]] were cured of lycanthropy at the [[Temple of Mistra]] by [[Samuel Patel]].

#### Connections

- [[WISC]] —cured S37→ [[Werebear Curse]]
- [[Furgus]] —cured S37→ [[Werebear Curse]]

## Clues & Mysteries

### Blond Skeletal Hand Recruiter

**Type:** Mystery · **Status:** unresolved · **Also called:** Skeletal Hand recruiter, Skeletal Hand scholarship
#### Summary

A blond young man who appears to recruit for the [[Skeletal Hand]] in [[Amberhold]].

#### Evidence
- [[Session 30]]: [reported] A cultist questioned with Speak with Dead after [[Christolf Nightfall]] was killed said he couldn't afford the Academy, and was offered "a different path" by a blond-haired youth **named Peter**, at an inn in Amberhold.
- [[Cam Jergins]] copied his Skeletal Hand tattoo from a small, blond young "kid" ([[Session 36]]).
- [[Session 37]]: [fact] A job-board flyer appears as a request for help moving boxes to Academy-associated people, but as a private scholarship offer to everyone else. It says to go to a particular tavern, order a beer, an ale and a wine at once, and wait. A blond young man approached the party, said those not admitted to the Academy would be hired for quests, and left. [[Furgus]] saw a Skeletal Hand tattoo under his sleeve. The party believes he used Disguise Self on leaving, and a black-haired woman they didn't recognise followed him out.
- [[Session 38]]: [suspicion] [[Sabrina]] described a young blond man calling himself [[Andrew]] who saw a Velvet Glove worker named Angela. The party wonders if he's the same person.

#### Open questions
- The recruiter gave the name **Peter** ([[Session 30]]). [[Peter Owens]] is a strange Academy graduate student. The notes don't connect the two, so whether they're the same person is unestablished.
- Is "Andrew" ([[Session 38]]) an alias of the same person?
- [[Session 25]]: The black feathers left at the [[Daggins Murder]] were bought by an androgynous human with long blonde hair. Unclear if related.

#### Party plans
- [[Riffle]] is considering ordering the drinks again after several days to see whether they are approached.

#### Connections

- [[Blond Skeletal Hand Recruiter]] —recruits for→ [[Skeletal Hand]]
- [[Cam Jergins]] —copied tattoo from a blond kid→ [[Blond Skeletal Hand Recruiter]]
- [suspicion] [[Andrew]] —same person?→ [[Blond Skeletal Hand Recruiter]]
- [suspicion] [[Peter Owens]] —the "Peter"?→ [[Blond Skeletal Hand Recruiter]]

### Heaven's Touch Enchantment

**Type:** Mystery · **Status:** unresolved
#### Summary

In [[Session 38]], [[Theo'din Corvis]] noticed an aura or enchantment settled on people inside [[Heaven's Touch]]. [[Zelda]], who left the [[Velvet Glove Brothel]] for Heaven's Touch a few weeks earlier, also appeared enchanted.

The brothel is a no-magic-casting area. Theo was escorted out for trying to Dispel Magic on Zelda, and the party had to leave with him.

#### Related
- Heaven's Touch is known for uncannily matching clients to their preferences ([[Session 35]]).
- It is drawing business away from the Velvet Glove.

### Lords of the Elements

**Type:** Mystery · **First seen:** [[Session 24]]
#### Summary

About 3,000 years ago, elemental forces were wreaking havoc across [[Ligos]]. The [[Elementalist Syndicate]] tried to control them by binding multiple elementals into larger entities.

The resulting beings became too powerful and escaped.

#### Known Lords

- **Lord of Earth** — body became the foundation of [[Derragh]], a Dwarven settlement in the far north.
- [suspicion] **Lord of Air** — believed alive and possibly residing in the upper atmosphere.
- [suspicion] **Lord of Water** — took to the sea; supposedly killed by an ancient dragon turtle, but unconfirmed.
- **Lord of Fire** — defeated in the western volcanic region. Mages froze it into obsidian and shattered it. The [[Mystery Stone]] is one fragment.

### Miner's Death Lode

**Type:** Mystery · **First seen:** [[Session 16]]
#### Summary

A legendary / highly dangerous mithril mine containing naturally occurring poisonous gas. Even Dwarves' natural poison resistance is insufficient.

Historical records indicate the [[Cult of the Destroyer]] attempted to mine it but abandoned the project because too many enslaved workers died.

The party later encountered necromantic activity and stolen bodies connected to a mine with similar poison characteristics.

### Owens Family Deaths

**Type:** Mystery · **Status:** unresolved · **Also called:** Owen Family Deaths, Lord Richard Owens
#### Summary

Lord Richard Owens, a wealthy [[Amberhold]] merchant, and his wife recently died. Sailors at the [[Cock and Pig]] are stuck in port because his ship can't be unloaded into his warehouse ([[Session 36]]).

#### What the party has heard ([[Session 38]])
- [suspicion] Rumours say the cook poisoned them.
- Their son [[Peter Owens]] has taken leave from [[Mistra's Academy]] and is visiting the [[Owens Family Mausoleum]] unusually often.
- Students find Peter strange and unsettling.
- A cloaked, hooded figure entered the mausoleum and vanished as the party arrived.

#### Connections

- [[Peter Owens]] —parents just died→ [[Owens Family Deaths]]

### Talir's Stolen Documents

**Type:** Mystery · **Status:** unresolved
#### Summary

At the end of [[Session 38]], [[Talir Rengavi]] sent [[Riffle]] a furious Sending message. He demanded that Riffle return documents stolen from his safe that afternoon, saying Archivist [[Siobhan]] saw Riffle enter his office.

Riffle did visit Talir that day, before helping [[Karyn]] tidy her office. The notes don't say whether Riffle was ever in Talir's office alone or went near the safe. This is the second time a witness has placed someone resembling Riffle at a theft. Compare the framing in the [[Daggins Murder]].

#### Open questions
- What documents were taken?
- Who did Siobhan see, and can she be trusted?
- Is this the same person or group who framed Riffle for Daggins's murder?

#### Connections

- [[Riffle]] —accused→ [[Talir's Stolen Documents]]
- [[Talir's Stolen Documents]] —accused: Siobhan's sighting→ [[Riffle]]
- [[Siobhan]] —witness→ [[Talir's Stolen Documents]]
- [[Talir Rengavi]] —victim→ [[Talir's Stolen Documents]]
- [suspicion] [[Hana Goldfirm]] —her office was also burgled?→ [[Talir's Stolen Documents]]

## Items

### Arcane Grimoire +1

**Type:** Item (magic item)
#### Summary

Magic grimoire recovered from [[Christolf Nightfall]].

### Armour of Cold Resistance

**Type:** Item (magic armor) · **First seen:** [[Session 21]]
#### Summary

Studded leather armor with abjuration magic, found in the Dragon League vault.

### Axeholm Map

**Type:** Item (map)
#### Summary

Map recovered from a Dragon League-associated ruin. Another map was also found in the vault. It indicates [[Axeholm]] is somewhere inside the mountain.

#### Connections

- [[Axeholm Map]] —inside the mountain→ [[Axeholm]]
- [[Dragon League]] —found in their vault→ [[Axeholm Map]]

### Blade of the Ancestors

**Type:** Item (weapon) · **First seen:** [[Session 29]]
#### Summary

Halberd associated with [[Corthos]] / the ancient Goliath hero in [[Quithos the Breaker]]'s tomb.

### Cornhusk Dolls

**Type:** Item (fae object) · **First seen:** [[Session 15]]
#### Summary

Recurring dolls resembling party members. Their origin appears to be fae; [[Agatha]] identified them as a [[Wetel|pixie]] creation.

#### Facts by session
- [[Session 37]]: [[Theo'din Corvis]] left one in the [[Temple of the Raven Queen]].

See also: [[Mystery of the Cornhusk Dolls]]

### Dagger of Venom

**Type:** Item (weapon) · **First seen:** [[Session 21]]
#### Summary

Evocation magic dagger found in the Dragon League vault.

### Daggins's Journal

**Type:** Item (document)
#### Summary

Journal containing clues to [[Axeholm]]. Original was stolen after [[Daddy Dildo Daggins]]'s murder; backup transcription survives with [[Hana Goldfirm]].

#### Connections

- [[Daggins's Journal]] —"Coal Caster = Zyvuir"→ [[Zyuir]]
- [[Daddy Dildo Daggins]] —deciphered→ [[Daggins's Journal]]
- [[Hana Goldfirm]] —holds the last copy→ [[Daggins's Journal]]
- [[Daggins Murder]] —Axeholm research taken→ [[Daggins's Journal]]

### Dread Helm

**Type:** Item (magic item) · **First seen:** [[Session 29]]
#### Summary

Helm worn by the reanimated Goliath [[Corthos]] in the tomb of [[Quithos the Breaker]], taken after the fight along with the [[Blade of the Ancestors]] and two jewelled snake arm rings ([[Session 29]]).

### Dream Weed

**Type:** Item (consumable) · **First seen:** [[Session 15]]
#### Summary

Magical substance sold by [[Fizz and Ugly's Travelling Store]]. Smoking it allows people to share memories via dreams.

### Duck Tape

**Type:** Item (wondrous item) · **First seen:** [[Session 21]]
#### Summary

Silvery magical tape found in the Dragon League vault.

### Grey Bag of Tricks

**Type:** Item (wondrous item) · **First seen:** [[Session 10]]
#### Summary

Produces animals including giant badgers, giant rats, boars, and repeatedly a giant elk. The elk repeatedly became a source of chaotic accidents.

### Helm of the Summer Moon

**Type:** Item (magic item) · **First seen:** [[Session 12]]
#### Summary

Identified in the notes as a headband of intellect. Recovered after the Goliath raider encounter.

### Immovable Rod

**Type:** Item (magic item) · **First seen:** [[Session 12]]
#### Summary

Magic item used creatively by the party, including helping restrain a basilisk in a hunting-trap setup.

### Javelin of Lightning

**Type:** Item (weapon) · **First seen:** [[Session 33]]
#### Summary

Magical javelin found among the Stone Giant were-bears' possessions.

### Mask of the Green Dragon

**Type:** Item (magic item) · **First seen:** [[Session 21]]
#### Summary

Ancient green dragon-shaped wooden mask found in the flooded Dragon League fortress. Transmutation magic.

#### Facts by session
- [[Session 37]]: Found to have placed a minor curse on [[Deanira]]. It was removed at the Student Health Clinic of [[Mistra's Academy]], after which she felt much better about [[WISC]].

### Music Box

**Type:** Item (wondrous item) · **First seen:** [[Session 13]]
#### Summary

Found in the druid's tent at the Goliath raider camp by [[Deanira]]. It plays Meredith's Lullaby, known in taverns by a ruder name ([[Session 13]]).

### Mystery Stone

**Type:** Item (artifact) · **First seen:** [[Session 01]]
#### Summary

A smooth black river stone initially small enough to carry. [[Hambrick Onyxcrest]] discovered that it was heavily layered with spells and called it an 'onion'. Its true form is a massive black stone. [[Bianca Onyxcrest]] and the [[Library of Deneir]] believe it is a fragment of the [[Lord of Fire]], an ancient elemental. The party eventually transferred it to [[Talir Rengavi]] / the Library for research.

#### Facts by session
- [[Session 36]]–38: The stone will be showcased at the [[Academy Gala]].

See also: [[Mystery Stone Investigation]]

### Pipes of the Sewers

**Type:** Item (wondrous item) · **First seen:** [[Session 33]]
#### Summary

Magical pipes that attracted rats when played.

### Quill of Deneir

**Type:** Item (artifact)
#### Summary

Holy quill of [[Deneir]] to be sold at the [[Dunnings Auction House]] in [[Western Point]] on the first Monday after the Beaver Moon. Riffle badly wants it ([[Session 13]]). See [[Southern Auction]].

### Reaper

**Type:** Item (weapon) · **First seen:** [[Session 08]]
#### Summary

Bill hook with a Raindrop Damascus pattern, forged by the Iron Dwarves and gifted to [[WISC]] by the Emberstone family.

### Ring of Gaseous Forms

**Type:** Item (ring) · **First seen:** [[Session 21]]
#### Summary

Ring engraved with animals and imbued with transmutation magic; found in the Dragon League vault.

### Rod of Fishing

**Type:** Item (wondrous item) · **First seen:** [[Session 21]]
#### Summary

Odd magical rod with a button; found in the Dragon League vault.

### Scroll of Revivify

**Type:** Item (spell scroll) · **First seen:** [[Session 21]]
#### Summary

Spell scroll found inside the map case in the Dragon League vault.

### Sending Stones

**Type:** Item (magic item) · **First seen:** [[Session 35]]
#### Summary

Communication stones purchased in [[Amberhold]]. [[Horizon]] offered an unlimited local sending plan.

### Silver Pie Cutter

**Type:** Item (treasure) · **First seen:** [[Session 17]]
#### Summary

Belonged to [[Daddy Dildo Daggins]]. [[Riffle]] secretly slipped it, with some gold, into [[Furgus]]'s bag as a prank, and Furgus refused to sell it ([[Session 17]]).

### Staff of Ham

**Type:** Item (wondrous item) · **First seen:** [[Session 12]]
#### Summary

Comedic magical staff capable of conjuring a country ham. Used to feed the goblin child and repeatedly assist the party with food and mischief.

### Tapestry of Feats

**Type:** Item (wondrous item) · **First seen:** [[Session 29]]
#### Summary

Magical tapestry that weaves itself to depict the holder's greatest feat. [[WISC]] saw the party's encounter with [[Agatha]] depicted on it.

### Unbreakable Vial

**Type:** Item (wondrous item) · **First seen:** [[Session 15]]
#### Summary

Small glass vial demonstrated to be extremely resistant to damage. Used to contain the ashes of a [[Flame Skull]].

## Lore

### Abbathor

**Type:** Lore · **First seen:** [[Session 04]]
#### Summary

Dwarven god of greed. In the notes, Abbathor is viewed by many Dwarves more as a curse than a blessing and is associated with madness.

The party encountered an underground temple with an Abbathor symbol while investigating the [[Duergar]] mining operation.

### Anthracite

**Type:** Lore
#### Summary

Extremely hard coal that burns hot enough, for long enough, to forge [[Mithril]] and adamantine. It is mined only by the [[Black Hand Dwarves]] at [[Kohlemine]]. Its price suddenly doubled ([[Session 10]], [[Session 17]]). See [[Anthracite Trade Mystery]].

### Cidis

**Type:** Lore
#### Summary

Dragon in whose name the [[Cult of the Destroyer]] ruled, taxed and mined. Cidis vanished about 800 years ago, after which the cult was overthrown and its dam broken, turning the forest into bog ([[Session 17]]).

### Deneir

**Type:** Lore
#### Summary

God associated in the notes with scribes, knowing, writing, books, and knowledge.

[[Riffle]] is a cleric of Deneir and works for the [[Library of Deneir]].

### Flame Skull

**Type:** Lore
#### Summary

Undead the party destroyed in the sunken Dragon Cult fortress ([[Session 20]]). Its ashes would reanimate, so they sealed them in the [[Unbreakable Vial]], later traded to [[Agatha]] ([[Session 21]]). Riffle's journal copies burned in this fight ([[Session 36]]).

### Glabrezu

**Type:** Lore
#### Summary

Demon guarding the desecrated mountaintop temple where [[Balgus]] lies. See [[Warrior of Kord]].

### Ligos

**Type:** Lore
#### Summary

Name of the world (or continent) where elementals ran rampant about 3,000 years ago, before the [[Elementalist Syndicate]] bound them ([[Session 24]]).

### Lord of Fire

**Type:** Lore
#### Summary

One of the [[Lords of the Elements]]. It was defeated in the western volcanic region now home to the [[Fire Dwarves]], frozen into obsidian and shattered. The [[Mystery Stone]] is one of its fragments ([[Session 24]]).

### Mithril

**Type:** Lore · **Also called:** Mithral
#### Summary

Precious metal mined and forged in the north. The Knockers and [[Duergar]] were mining it to arm a force ([[Session 03]], [[Session 08]]). Working it requires [[Anthracite]]. The poisonous [[Miner's Death Lode]] was a mithril mine.

### Raven Queen

**Type:** Lore · **First seen:** [[Session 32]]
#### Summary

[[Theo'din Corvis]] serves the Raven Queen and describes her as strongly opposed to necromancy.

Theo's personal history involves a bargain his mother made with the Raven Queen to save her life, at the cost of one of her twins.

#### Facts by session
- [[Session 37]]: Theo communed with her ("the Matron") at the [[Temple of the Raven Queen]]. She appeared as a woman in a white mask, a black dress, and a cloak of raven feathers.

#### Connections

- [[Theo'din Corvis]] —patron→ [[Raven Queen]]

### Sune

**Type:** Lore
#### Summary

Deity whose religious order tends a holy pool on an island south of [[Admiral's Point]] ([[Session 34]]).

### Tiamat

**Type:** Lore
#### Summary

Dragon goddess worshipped by the [[Dragon League]], whose blessing let them control dragons. About 100 years ago she was put down in a battle among the gods, and the League lost that power ([[Session 36]]).

### Wolfsbane Potion

**Type:** Lore
#### Summary

Campaign recipe notes:

- Wolfsbane
- Stabilizing agent (holy water, belladonna, etc.)
- Powdered moonstone or moon seed
- Blood of a lycanthrope
- Purified water or water from a blessed body of water

Potential blessed-water locations:
- [[Kriptin Forest]]
- [[Amberhold]] — cared for by the sisters of Lethander
- An island south of [[Admiral's Point]] under the care of a religious order of [[Sune]]

## Part 4: Session notes, in order of play

### Session 1

**Session:** 1 · Not dated in the source notes · **Next:** [[Session 02]]
> [!summary] TL;DR
> [[Deanira]] comes out of the tree line as a big ram goes berserk and kills a sheep-herding partner. When the party tries to stop it, it throws up blood and a smooth black stone: the [[Mystery Stone]]. ([[Session 02]] calls the sheep "our" sheep.)

### Session 2

**Session:** 2 · Not dated in the source notes · **Previous:** [[Session 01]] · **Next:** [[Session 03]]
> [!summary] TL;DR
> The party arrives at [[Truemetal Halls]] to sell their sheep, meets [[The Bastard's Band]], finds [[Hambrick Onyxcrest]] away in the Feywild, and takes [[Gunther Rockhammer]]'s job clearing and mapping a mine beneath the city.

### Session 3 — 29 February 2025

**Session:** 3 · Source notes say 29 February 2025, which isn't a valid date · **Previous:** [[Session 02]] · **Next:** [[Session 04]]
> [!summary] TL;DR
> Exploring the sealed mine, the party fights shadow Dwarves, gricks and a gelatinous cube, and recovers goggles of night from two dead Halfling miners. Beyond the cave-in they find Knockers mining mithril for "The Great One" and jump down the chute to meet his priests.

### Session 4 — 9 March 2025

**Session:** 4 · Played 9 March 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 03]] · **Next:** [[Session 05]]
> [!summary] TL;DR
> At the bottom they ambush Duergar hauling ore and spot a large Duergar smelting compound worked by slaves. Across an underground lake, a blood-opened door leads to a temple of [[Abbathor]], where they kill an evil priestess.

### Session 5 — 18 April 2025

**Session:** 5 · Played 18 April 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 04]] · **Next:** [[Session 06]]
> [!summary] TL;DR
> They escape by water breathing past a water weird and free six captives, including [[Elzock Emberstone]]. A dead Halfling adventurer's coded journal yields the word **Axeholm**, and they emerge into daylight.

### Session 6 — 2 May 2025

**Session:** 6 · Played 2 May 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 05]] · **Next:** [[Session 07]]
> [!summary] TL;DR
> WISC and Furgus reveal dreams in which Abbathor offered protection (Furgus signed in blood). Freed bugbear Crez guides them to the [[Black Dragon Inn]], where [[Hilda]] can't identify the stone.

### Session 7 — 1 June 2025

**Session:** 7 · Played 1 June 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 06]] · **Next:** [[Session 08]]
> [!summary] TL;DR
> In [[Tryborne Pass]] they find a slaughtered caravan and fight ravens and dire wolves. The ghost of [[Oswald]] leads them to [[Unfinished Business]], a tavern for lingering souls, and asks them to tell [[Mary Salter]] of his death. Elzock is returned to the [[Ring of Gold]].

### Session 8 — 18 June 2025

**Session:** 8 · Played 18 June 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 07]] · **Next:** [[Session 09]]
> [!summary] TL;DR
> The Emberstones reward the party with [[Reaper]], a chromatic quiver and thunderous handwraps. [[Lord Ivan Deepshaft]] of the [[Court]] debriefs them on the mine in secret and asks them to keep quiet; the city pays 900 gold for the information.

### Session 9 — 17 July 2025 Anita: Riﬄe

**Session:** 9 · Played 17 July 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 08]] · **Next:** [[Session 10]]
> [!summary] TL;DR
> [[Riffle]] joins after pickpocketing and copying the journal. The party meets [[Daddy Dildo Daggins]], who tells them the legend of Axeholm and agrees to crack the cipher. Deanira keeps his silver dildo as collateral.

### Session 10 — 22 July 2025 Lyra: Deanira

**Session:** 10 · Played 22 July 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 09]] · **Next:** [[Session 11]]
> [!summary] TL;DR
> [[Hambrick Onyxcrest]] dispels the stone, revealing a giant "onion" of layered spells. The party hears of the [[Anthracite Trade Mystery|anthracite price hike]], takes a job clearing the grain route, and gains the horse Dante and the [[Grey Bag of Tricks]].

### Session 11 — 6 August 2025

**Session:** 11 · Played 6 August 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 10]] · **Next:** [[Session 12]]
> [!summary] TL;DR
> Goliath raiders ambush them, and one, [[Uthal]], defects with intel on [[Ilkan]]'s camp. The party scouts the camp and plans a pre-dawn attack.

### Session 12 — 12 August 2025

**Session:** 12 · Played 12 August 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 11]] · **Next:** [[Session 13]]
> [!summary] TL;DR
> The night raid goes chaotically: a hopeless Uthal ends up stabbed by Riffle, but survives on a lucky death save without knowing who did it. Loot includes the [[Staff of Ham]], [[Immovable Rod]], [[Helm of the Summer Moon]] and Oswald's wife's pocketwatch.

### Session 13 — 20 August 2025

**Session:** 13 · Played 20 August 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 12]] · **Next:** [[Session 14]]
> [!summary] TL;DR
> Clearing the camp nets a music box, and Uthal slips away. At the Black Dragon Inn, Riffle reveals they work for the [[Library of Deneir]] and wants the Quill of Deneir at the [[Southern Auction]]. Furgus and WISC are invited to the family festival.

### Session 14 — 9 September 2025

**Session:** 14 · Played 9 September 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 13]] · **Next:** [[Session 15]]
> [!summary] TL;DR
> Daggins decodes "Coal Caster = Zyvuir" and links Axeholm to the [[Crystalline Glacier]]. On the road to [[Wren Nalore]], the party kills a poisonous flesh golem built partly from the arm of the Dwarf who died at the market.

### Session 15 — 20 September 2025

**Session:** 15 · Played 20 September 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 14]] · **Next:** [[Session 16]]
> [!summary] TL;DR
> They escort [[Ea]] to [[Darham Hold]] and suspect stolen corpses are being repurposed. They shop at [[Fizz]] and [[Ugly]]'s travelling store, then find the first [[Cornhusk Dolls]] by their fire.

### Session 16 — 9 October 2025

**Session:** 16 · Played 9 October 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 15]] · **Next:** [[Session 17]]
> [!summary] TL;DR
> At [[The Forge]], Riffle traces the stolen bodies to undertaker [[Christolf Nightfall]]. His undead assistant fights them, Christolf escapes, and a half-burned letter mentions the poisonous [[Miner's Death Lode]].

### Session 17 — 16 October 2025

**Session:** 17 · Played 16 October 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 16]] · **Next:** [[Session 18]]
> [!summary] TL;DR
> The party confirms the anthracite price spike and receives a journal transcription about a survivor of undead-haunted Axeholm. The pixie [[Wetel]] recruits Deanira into his doll pranks. Darham Hold is under new rule, and they rescue a goblin baby from a burned village.

### Session 18 — 25 October 2025

**Session:** 18 · Played 25 October 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 17]] · **Next:** [[Session 19]]
> [!summary] TL;DR
> In Wren Nalore they leave the goblin child with [[Sana Valxia]] and research flesh golems. Deanira has a vision of a satyr drowning at sea before a webbed hand grabs her, and they hear of [[Gauntlet|The Gauntlet]].

### Session 19 — 6 November 2025

**Session:** 19 · Played 6 November 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 18]] · **Next:** [[Session 20]]
> [!summary] TL;DR
> Cornhusk dolls appear again. Deanira shares her vision through [[Dream Weed]], and Riffle notes a raider bugbear with WISC's rare eye colour. Hunting basilisks, they fall into a sunken fortress with a green dragon statue.

### Session 20 — 22 November 2025

**Session:** 20 · Played 22 November 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 19]] · **Next:** [[Session 21]]
> [!summary] TL;DR
> Inside the sunken fortress they fight a flame skull and bottle its ashes. They find Dragon Cult blackmail documents and a map of Axeholm. WISC's fish stick stand plans are revealed.

### Session 21 — 8 December 2025

**Session:** 21 · Played 8 December 2025 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 20]] · **Next:** [[Session 22]]
> [!summary] TL;DR
> They clear the dragon shrine and vault, finding the [[Mask of the Green Dragon]] and other magic items. The hag [[Agatha]] identifies the dolls as a pixie's work and says the Drow outpost of [[Zyuir]] is the key to Axeholm.

### Session 22 — 28 Jan 2026

**Session:** 22 · Played 28 January 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 21]] · **Next:** [[Session 23]]
> [!summary] TL;DR
> Using ham bait and the Immovable Rod, they harvest basilisk eggs and blood. They then learn they've been exiled from Wren Nalore, largely thanks to Riffle.

### Session 23 — 5 February 2026

**Session:** 23 · Played 5 February 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 22]] · **Next:** [[Session 24]]
> [!summary] TL;DR
> WISC bribes their goods back while Riffle pranks the guard tower. They camp with a grieving [[The Bastard's Band]], then [[Hambrick Onyxcrest]] portals them home to meet [[Talir Rengavi]] and [[Hana Goldfirm]].

### Session 24 — 9 February 2026

**Session:** 24 · Played 9 February 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 23]] · **Next:** [[Session 25]]
> [!summary] TL;DR
> The stone is revealed as a fragment of the Lord of Fire ([[Lords of the Elements]]) and sold to the Library. Talir offers to sponsor the party in the Gauntlet. A teen posing as "Hector" poisons them, and they find Daggins murdered with "RI…F" in blood and black feathers.

### Session 25 — 16 February 2026

**Session:** 25 · Played 16 February 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 24]] · **Next:** [[Session 26]]
> [!summary] TL;DR
> Riffle hides the feathers and blood letters, and Daggins's Axeholm research is gone. [[Sherlock Gnomes]] concludes someone is framing Riffle. Deepshaft hires the party to check the tomb of Quithos the Breaker near [[Venburg]].

### Session 26 — Missed Session

**Session:** 26 · Missed session · **Previous:** [[Session 25]] · **Next:** [[Session 27]]
> [!summary] TL;DR
> *Missed session.* On the road they meet hunters, kill two honeymooning hill giants and an owlbear. Hana reports the Academy's head has died and that red Library robes were destroyed 20 years ago.

### Session 27 — 9 March 2026

**Session:** 27 · Played 9 March 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 26]] · **Next:** [[Session 28]]
> [!summary] TL;DR
> The party skirts a spore field, kills a troll with a giant snake, and frees WISC from an enchanted fiddle. They reach the cliffs where the tomb is carved.

### Session 28 — 8 April 2026

**Session:** 28 · Played 8 April 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 27]] · **Next:** [[Session 29]]
> [!summary] TL;DR
> Past an illusory door and rune-bound minotaur skeletons, they kill four [[Skeletal Hand]] members. They find captives from Venburg, including [[Zeke]], [[Ambria]] and [[Wolf]].

### Session 29 — 15 April 2026

**Session:** 29 · Played 15 April 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 28]] · **Next:** [[Session 30]]
> [!summary] TL;DR
> Freed prisoners describe an "extraction point" and "work below". In the honey-entombed chamber, the party kills [[Christolf Nightfall]] and the reanimated Goliath hero [[Corthos]], gaining the [[Dread Helm]] and [[Blade of the Ancestors]].

### Session 30 — 3 June 2026

**Session:** 30 · Played 3 June 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 29]] · **Next:** [[Session 31]]
> [!summary] TL;DR
> Speak with Dead reveals the cultists were recruited in Amberhold by a blond youth named **Peter**. Following the trail, they find boneless corpses and a trapped rendezvous. They glimpse the [[Master of Death]] before he vanishes through a rift.

### Session 31 — 16 June 2026

**Session:** 31 · Played 16 June 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 30]] · **Next:** [[Session 32]]
> [!summary] TL;DR
> After a nightmare about [[Oma]], WISC brings the party home, where Uthal now works. They arrive in [[Venburg]] to find it swollen with refugees from unrest around [[Eisenberg]], and meet Furgus's family.

### Session 32 — 9 July 2026

**Session:** 32 · Played 9 July 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 31]] · **Next:** [[Session 33]]
> [!summary] TL;DR
> [[Theo'din Corvis]], a Shadar-kai servant of the [[Raven Queen]] hunting northern necromancy, joins the party. [[Jane Pedimore]] tells Riffle a golden-eyed bugbear murdered her family.

### Session 33 — 20 July 2026

**Session:** 33 · Played 20 July 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 32]] · **Next:** [[Session 34]]
> [!summary] TL;DR
> Hunters return from a bear attack near [[Hawk's Nest]]. The party kills three Stone Giant were-bears and loots the [[Javelin of Lightning]] and the [[Pipes of the Sewers]].

### Session 34 — 27 July 2026

**Session:** 34 · Played 27 July 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 33]] · **Next:** [[Session 35]]
> [!summary] TL;DR
> Speak with Dead explains lycanthropy and its full-moon deadline. WISC and Furgus's bites won't heal, so the [[Werebear Curse]] clock starts. Theo gets his first cornhusk doll, and the party plans a cure via [[Amberhold]].

### Session 35 — 17 August 2026

**Session:** 35 · Played 17 August 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 34]] · **Next:** [[Session 36]]
> [!summary] TL;DR
> At the Venburg festival Riffle reveals how their burn made them a cleric. A portal drops the party, with [[Philip]], into the [[Velvet Glove Brothel]] in Amberhold, where [[Sabrina]] warns of the rival [[Heaven's Touch]].

### Session 36 — 31 August 2026

**Session:** 36 · Played 31 August 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 35]] · **Next:** [[Session 37]]
> [!summary] TL;DR
> The party arrives at the Library and lodges around Amberhold. They meet [[Cam Jergins]], whose [[Skeletal Hand]] tattoo was copied from a blond youth. [[Bianca Onyxcrest]] arranges the were-bear cure and explains the [[Gauntlet]], and a messenger delivers the last copy of the journal pages.

### Session 37 — 12 September 2026

**Session:** 37 · Played 12 September 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 36]] · **Next:** [[Session 38]]
> [!summary] TL;DR
> The were-bear curse is cured and the [[Mask of the Green Dragon]]'s curse is lifted from Deanira. A coded scholarship flyer leads to a blond [[Skeletal Hand]] recruiter, and sailors report vanishing islands. Theo communes with the [[Raven Queen]].

### Session 38 — 24 September 2026

**Session:** 38 · Played 24 September 2026 (real-world date of the game night, not an in-world date) · **Previous:** [[Session 37]]
> [!summary] TL;DR
> Deanira meets [[Daddy Dildo Daggins]]'s fertility order, the [[Union of Many]], and Theo gets the party ejected from enchanted [[Heaven's Touch]]. Rumours surround [[Peter Owens]] and his family's deaths. At his family mausoleum, [[Talir Rengavi]] accuses Riffle of stealing from his safe.

### Session 39 (raw notes, not yet set up: no recap, header or links)

Session 39
8 October 2026
Standing in the rain outside the mausoleum, Riffle sends a message back to Talir: "Was not me. Was not in office. Will explain. Please do not burn bell tower." Talir doesn't answer. Riffle is visibly rattled but insists we finish what we came here to do first.
The mausoleum belongs to the Owens family. Carved above the door: "OWENS — WHAT THE SEA GIVES, THE SEA KEEPS". Inside are two new stone coffins, Lord Richard Owens and Lady Margaret Owens, with fresh white lilies on both. Theo feels a cold prickle along his arms, the kind the Raven Queen's servants are taught to recognise. Someone has been doing necromancy in here recently, but not on the bodies; Riffle checks and both corpses are still very much dead (and smell like it).
Furgus notices scuff marks on the floor in front of an older coffin belonging to a great-grandfather, Bartholomew Owens. WISC pushes it and it slides aside on hidden rollers. Underneath is a spiral stair going down. We hear dripping water and smell the sewers. Deanira realises this must connect to the sewers where the sanitation workers went missing.
At the bottom is an old brick tunnel, much older than the sewers above it. Deanira maps as we go. We find a sanitation worker's lantern and an orange city work vest with the name "PIM" stitched on it. Further on, the tunnel opens into a round chamber with old drains on every side. Six people are chained to the walls. Four of them are alive. Two are not, and they get up when we walk in.
We roll initiative. The two dead workers have been turned into ghouls, and a robed figure on a ledge above starts chanting. Furgus shoots him in the shoulder and his hood falls back: it's a young man with dark hair and a Skeletal Hand tattoo on his wrist, NOT the blond guy. Deanira plays the Pipes of the Sewers and about forty rats pour out of the drains and swarm the ghouls, which buys WISC time to cut the chains. Theo calls on the Raven Queen and both ghouls crumble to ash. The acolyte tries to run but WISC throws the Javelin of Lightning at him and he goes down.
The four survivors are Gertrude "Gert" Mossbottom (the sanitation foreman, a very angry halfling), Pim Lark (the young human whose vest we found), and two of the city searchers, Odo and Fenwick. That makes six of the seven missing people. Gert says the seventh, a searcher named Hollis, was taken to "the man in the grey mask" two days ago and never came back. She says the masked man talked about needing "fresh ones, not old ones" for "the night of the stone".
The acolyte is alive but unconscious. On him we find: a black iron key, a vial of grave dust, 14 gold, and a folded page of Library letterhead. Riffle recognises it immediately as a page from the Library's storeroom ledger. It lists "Ceremonial robes (red, old pattern), 12, Storeroom B, sub-basement". Someone had circled the line and written "11" next to it.
We bring the survivors and the prisoner up through the mausoleum. On the way out Philip spots someone watching us from the graveyard wall, a tall cloaked figure in a grey mask. When Theo steps toward him, he turns and walks into the rain and is gone. Nobody gets a good look.
The city watch takes the acolyte. The captain, Captain Imelda Thorne, thanks us and says the city will pay the 200gp reward once the foreman confirms everything, plus extra for the searchers. Gert hugs WISC around the knees and won't let go for a while.
The next morning Riffle goes to see Talir in person, with Hana. Talir is cold at first. Riffle explains that they were in Karyn's office tidying up when the documents were taken, and Karyn backs this up when Hana fetches her. Siobhan is called in. She is certain she saw a kenku in RED robes go into Talir's office and leave by the east stair, but when Riffle stands next to her she admits it was "maybe a bit taller". Talir apologises, awkwardly. He finally tells us what was stolen: the plans for the warding glyphs on the display vault where the stone will be shown at the Gala. Whoever has them knows exactly how the stone is protected.
Riffle shows Talir the ledger page. Talir goes pale. He goes down to Storeroom B with us and there are only eleven red robes in the crate.
Meanwhile, Deanira goes back to the Two Tits to see Atheela. Atheela says the Union of Many has heard that a fertility statue from the old Dragon League continent is going to be sold at the Dunnings auction in Western Point. Deanira is now VERY interested in the southern auction.
WISC and Furgus go to the Academy practice yard to watch the other Gauntlet teams train. One team is from the Academy itself, Team Ember, led by a very serious tiefling evoker named Corvina Ashgrove. Another is a team of halfling adventurers called the Copper Kettles, led by Marigold Thistlewick, who challenges Furgus to an archery contest. Furgus wins by one point. Marigold says they're friends now.
Philip spends the day at the Cock and Pig with Evelyn Keep and the sailors. One of them, a sailor named Bertram, says his crew saw an island with a broken white tower on it two nights out from the city, and the next morning there was nothing but sea. Philip writes it down for Deanira.
On the way back to The Three Candles, WISC and Theo pass a wine shop where four men in white tabards are smashing bottles. They are the followers of Torm. Their leader, Brother Aldric Venn, tells us drink "dulls the discipline the gods require" and that the city will be "clean before the Gala". Theo asks why the Gala matters to them and Aldric just smiles and walks off.
That night Theo finds a new cornhusk doll on his pillow. It looks like Philip.
Late that night Riffle gets a Sending from Sabrina: "Angela didn't come to work. Her room at the Velvet Glove is empty. She left everything."
Loot:
- Black iron key (unknown lock)
- Vial of grave dust
- 14 gold
- Library ledger page (the robes)
- 200gp city reward (pending)
Todo list:
- Find out what the black iron key opens
- Question the acolyte once the watch is done with him
- Who is the man in the grey mask? Is he the Master of Death?
- Find out who took the missing red robe
- Tell Bianca about the stolen warding plans before the Gala
- Find Angela
- Deanira: plan for the Dunnings auction
- Ask Wetel why Philip has a doll now
