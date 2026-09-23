---
title: "Dataview Queries"
tags:
  - obsidian
  - dataview
  - reference
---
# Dataview Queries

These snippets require the Obsidian Dataview plugin.

## Active quests

```dataview
TABLE status, file.link AS "Quest"
FROM "Quests"
WHERE status != "completed"
SORT status ASC, file.name ASC
```

## People

```dataview
TABLE type, file.link AS "Person"
FROM "People"
SORT file.name ASC
```

## Places

```dataview
TABLE type, file.link AS "Place"
FROM "Places"
SORT type ASC, file.name ASC
```

## Campaign mysteries

```dataview
TABLE status, file.link AS "Mystery"
FROM "Clues & Mysteries"
SORT status ASC, file.name ASC
```

## Sessions

```dataview
TABLE file.link AS "Session"
FROM "Sessions"
SORT file.name ASC
```
