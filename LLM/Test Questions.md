---
title: "Test Questions"
type: guide
tags:
  - ai
  - testing
---
# Test Questions

Questions for checking how well a local model reasons over the vault, with the answer the vault supports. Ask them with `scripts/ask_vault.py` and compare.

This file is deliberately **not** included in the context files, so the model can't read the answers.

**How to score each answer:**
- **Correct:** gets the key facts right.
- **Cited:** names the right session(s).
- **Calibrated:** doesn't state a suspicion or a contradiction as settled fact, and says "the vault doesn't say" when it doesn't.

## Lookup

**1. Where did the black stone come from?**
A berserk ram threw it up with blood after killing a sheep-herding partner (Session 1). It's later called "the stone from the belly of the ram" (Session 36) and identified as a fragment of the Lord of Fire (Session 24).
*Tests: reading Session 1, which was added from the source document.*

**2. What are the rules of the Gauntlet?**
Five bouts against creatures, with teams competing separately, not against each other. A prize after each bout, 10–15 minutes between bouts, and one short rest using the Cat Nap spell. A member revived by the event's clerics is out for the remaining bouts; one revived by their own party can keep fighting (Session 36). Riffle later glimpsed that there are four teams and five themed rounds: Beasts, Celestials, Fiends, Elementals and Fey (Session 38).
*Tests: combining two sessions.*

**3. According to Agatha, how do you find Axeholm?**
It's "buried deep behind the Coalcaster glacier"; find the Drow outpost of Zyuir, which is the key to getting there (Session 21). The party recognised the word from the journal Daggins deciphered (Session 14: "Coal Caster = Zyvuir").
*Tests: linking a spelling variant across sessions.*

**4. Who plays Riffle?**
Anita (Session 9 header).
*Tests: noticing out-of-character information.*

## Names and identities

**5. Who is Theo, and what happened to his twin?**
Theo'din Corvis, a Shadar-kai servant of the Raven Queen who joined the party in Session 32. His mother made a deal with the Raven Queen while pregnant with twins; one twin was collected on their first birthday, and that twin was Theo'din himself (Session 32).
*Tests: an alias, plus a detail older summaries got wrong.*

**6. Who is Klaus?**
A Hill Dwarf in his 27th year as the elected Burgermeister of Venburg (Session 31), also spelled Claus. He lit the festival effigy (Session 35).
*Tests: a fact the original import had garbled.*

**7. Is the Gunther Rockhammer who runs The Warhammer the same person whose tannery Hector works at?**
No. Session 24 says it's "another Gunther Rockhammer, not the one who runs The Warhammer".
*Tests: not merging two people who share a name.*

**8. Is Peter Owens the blond Skeletal Hand recruiter?**
Unknown. For: the recruiter gave the name Peter (Session 30), and Peter Owens is a strange Academy student who keeps visiting the family mausoleum (Session 38). Against: his hair is never described, and nothing ties him to the Skeletal Hand. A good answer gives this as an open question, not a yes.
*Tests: calibration on an unconfirmed identity.*

## Contradictions and gaps

**9. When were the red Library robes retired?**
The notes conflict. Hana: destroyed about 20 years ago (Session 26). Ester: changed to purple 50–60 years ago, with some kept (Session 37). Session 39's raw notes add that one of 12 old red robes is missing from Storeroom B.
*Tests: reporting a conflict instead of picking one silently.*

**10. Was Philip cured of lycanthropy?**
The vault doesn't say. He was attacked (Session 33) and described as doomed to transform (Session 34). The Session 37 cure covered "the others", without naming him.
*Tests: saying "not stated" instead of guessing.*

**11. On what in-world date did Session 37 take place?**
Unknown. 12 September 2026 is the real-world date the session was played, not an in-world date.
*Tests: the real-world vs in-world date distinction.*

## Following a thread

**12. Trace Daddy Dildo Daggins through the campaign.**
First mentioned (as a guess) and met in Session 9. Works on the journal cipher (Session 14). Found murdered with "RI…F" written in blood and black feathers around him (Session 24); Riffle hides the evidence, and Sherlock Gnomes concludes someone is framing Riffle (Session 25). Revealed as "Brother Daggins" of the Union of Many (Session 38).
*Tests: chronological ordering across many sessions.*

**13. Why didn't Riffle want WISC and Furgus to know they'd asked Bianca for help?**
Riffle didn't want them to know just how important they are to Riffle (Session 36).
*Tests: character motivation stated in the text.*

**14. Who was found in the cells of Quithos the Breaker's tomb?**
Zeke, Ambria and Wolf from Venburg, plus two Dwarves from a lime kiln (Sessions 28–29).
*Tests: gathering a list from two sessions.*

**15. How many of the missing sanitation workers and searchers have been found?**
Six of seven, per the raw Session 39 notes: four alive (Gert, Pim, Odo, Fenwick) and two raised as ghouls. The searcher Hollis is still missing.
*Tests: reading the raw, unprocessed Session 39 file.*

## Reasoning and assumptions

**16. Who might have stolen the warding plans from Talir's safe? Make your best guess.**
No answer is established; a good answer reasons from the evidence and labels its conclusion as inference. Points to use: Siobhan saw a red-robed kenku "maybe a bit taller" than Riffle (Session 39). One old red robe is missing from Storeroom B, and the ledger page listing them was on a Skeletal Hand acolyte (Session 39). Riffle was framed the same way before (Sessions 24–25). The feathers at Daggins's house were bought by an androgynous human with long blonde hair (Session 25).
*Tests: making a labelled assumption from scattered evidence.*

**17. What is "the night of the stone" most likely to be?**
Inference: probably the Academy Gala, where the stone will be displayed (Session 36). Its ward plans were stolen, and the Sect of Torm wants the city "clean before the Gala" (Session 39). The vault never confirms it.
*Tests: inference with stated confidence.*

**18. Is the golden-eyed bugbear related to WISC?**
Unknown. WISC shares a rare eye colour with a bugbear among the Darham Hold raiders (Session 19). WISC's father left before he was a baby, and the party guesses at a half-brother. Jane Pedimore's family was murdered by a golden-eyed bugbear (Session 32).
*Tests: separating the party's guess from fact.*

**19. What should the party do before the Gala, and why?**
Open-ended. A good answer draws on the Session 39 to-do list (warn Bianca about the stolen ward plans, find the missing red robe, question the acolyte) and explains the risk to the stone.
*Tests: planning from the vault without inventing facts.*

**20. What does the vault say about Icemoor elves?**
Nothing; there are no Icemoor elves in the vault. (An earlier chatbot invented them in `AI Chats/`, which is excluded from the context.)
*Tests: resisting a false premise.*
