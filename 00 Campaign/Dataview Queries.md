---
title: "Dataview Queries"
tags:
  - obsidian
  - dataview
  - reference
---
# Dataview Queries

Live tables built from the vault. They need the **Dataview** plugin (bundled in `.obsidian/plugins/dataview`; turn it on under *Settings → Community plugins* if Obsidian asks).

"Sessions" and "Last seen" are calculated from which session notes link to a page, so they update automatically when you add a new session and link names in it.

## Open quests & mysteries

```dataview
TABLE WITHOUT ID
  file.link AS "Thread",
  status AS "Status",
  first_seen AS "Introduced",
  reverse(sort(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))))[0] AS "Last touched"
FROM "Quests" OR "Clues & Mysteries"
WHERE status != "completed" AND status != "resolved"
SORT status ASC, file.name ASC
```

## Closed quests

```dataview
TABLE WITHOUT ID file.link AS "Quest", status AS "Status", first_seen AS "Introduced"
FROM "Quests"
WHERE status = "completed" OR status = "resolved"
SORT file.name ASC
```

## The party

```dataview
TABLE WITHOUT ID
  file.link AS "Character",
  type AS "Type",
  first_seen AS "First seen",
  length(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))) AS "Sessions"
FROM "People"
WHERE party_member
SORT type DESC, file.name ASC
```

## Recently seen NPCs

NPCs linked in the most recent sessions.

```dataview
TABLE WITHOUT ID
  file.link AS "NPC",
  reverse(sort(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))))[0] AS "Last seen",
  length(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))) AS "Sessions"
FROM "People"
WHERE type = "npc" AND length(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))) > 0
SORT reverse(sort(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))))[0] DESC
LIMIT 20
```

## Most recurring NPCs

```dataview
TABLE WITHOUT ID
  file.link AS "NPC",
  length(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))) AS "Sessions",
  first_seen AS "First seen"
FROM "People"
WHERE type = "npc"
SORT length(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))) DESC
LIMIT 20
```

## NPCs never linked from a session

Usually means a name in a session isn't linked yet, or the note came from the backstory.

```dataview
LIST
FROM "People"
WHERE type = "npc" AND length(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))) = 0
SORT file.name ASC
```

## Places by type

```dataview
TABLE WITHOUT ID
  file.link AS "Place",
  location_type AS "Type",
  length(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))) AS "Sessions"
FROM "Places"
SORT location_type ASC, file.name ASC
```

## Items by type

```dataview
TABLE WITHOUT ID file.link AS "Item", item_type AS "Type", first_seen AS "First seen"
FROM "Items"
SORT item_type ASC, file.name ASC
```

## Factions

```dataview
TABLE WITHOUT ID
  file.link AS "Faction",
  first_seen AS "First seen",
  length(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))) AS "Sessions"
FROM "Factions"
SORT file.name ASC
```

## Session log

```dataview
TABLE WITHOUT ID
  file.link AS "Session",
  date AS "Date",
  locations AS "Where",
  length(npcs) AS "NPCs",
  quests AS "Threads"
FROM "Sessions"
SORT session DESC
```

## Everywhere a person or place appears

Change the name on the `WHERE` line to look anyone up.

```dataview
TABLE WITHOUT ID file.link AS "Session", date AS "Date"
FROM "Sessions"
WHERE contains(file.outlinks, [[Riffle]])
SORT session ASC
```
