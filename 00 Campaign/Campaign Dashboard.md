---
title: "Campaign Dashboard"
tags:
  - campaign
  - dashboard
  - index
---
# Icemoor Campaign Dashboard

## Party
- [[WISC]]
- [[Furgus]]
- [[Deanira]]
- [[Riffle]]
- [[Philip]]
- [[Theo'din Corvis]]

## Boards
Canvas maps of the big threads. Yellow arrows are suspicions, not established facts.
- [[Party Overview.canvas|Party Overview]]: each character and their personal threads
- [[Skeletal Hand Web.canvas|Skeletal Hand Web]]: necromancy in the north and recruiting in Amberhold
- [[Riffle Framed.canvas|Riffle Framed]]: the Daggins murder and Talir's stolen documents
- [[Axeholm Trail.canvas|Axeholm Trail]]: every clue toward the lost city

## Where we left off
*Live tables; need the Dataview plugin. Full set in [[Dataview Queries]].*

```dataview
TABLE WITHOUT ID file.link AS "Session", date AS "Date", locations AS "Where"
FROM "Sessions"
SORT session DESC
LIMIT 3
```

```dataview
TABLE WITHOUT ID
  file.link AS "Open thread",
  status AS "Status",
  reverse(sort(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))))[0] AS "Last touched"
FROM "Quests" OR "Clues & Mysteries"
WHERE status != "completed" AND status != "resolved"
SORT reverse(sort(filter(file.inlinks, (l) => startswith(meta(l).path, "Sessions/"))))[0] DESC
```

## Major campaign threads

| Thread | Status | Primary links |
|---|---|---|
| Mystery Stone / Lord of Fire | unresolved | [[Mystery Stone]], [[Mystery Stone Investigation]], [[Lords of the Elements]], [[Library of Deneir]], [[Mistra's Academy]] |
| Axeholm | unresolved | [[Axeholm]], [[Zyuir]], [[Daggins's Journal]], [[Axeholm Map]] |
| Skeletal Hand / Master of Death | unresolved | [[Skeletal Hand]], [[Master of Death]], [[Christolf Nightfall]], [[Blond Skeletal Hand Recruiter]] |
| Daggins murder | unresolved | [[Daddy Dildo Daggins]], [[Daggins Murder]], [[Union of Many]] |
| Riffle framed again | unresolved | [[Talir's Stolen Documents]], [[Siobhan]], [[Talir Rengavi]] |
| Necromancy in the North | unresolved | [[Skeletal Hand]], [[Christolf Nightfall]], [[Axeholm]] |
| Golden-eyed bugbear | unresolved | [[WISC]], [[Golden-Eyed Bugbear Mystery]], [[Jane Pedimore]] |
| Were-bear curse | resolved | [[Werebear Curse]], [[Bianca Onyxcrest]], [[Samuel Patel]] |
| Cornhusk dolls / Fae | unresolved | [[Cornhusk Dolls]], [[Mystery of the Cornhusk Dolls]], [[Wetel]], [[Agatha]] |
| Anthracite / Mithril supply | unresolved | [[Black Hand Dwarves]], [[Kohlemine]], [[Anthracite Trade Mystery]] |
| Floating island / Val | unresolved | [[Deanira]], [[Val]], [[Floating Island Mystery]] |
| Owens family deaths | unresolved | [[Owens Family Deaths]], [[Peter Owens]], [[Owens Family Mausoleum]] |
| Heaven's Touch enchantment | unresolved | [[Heaven's Touch Enchantment]], [[Heaven's Touch]], [[Zelda]] |
| Gala & Gauntlet | upcoming | [[Academy Gala]], [[Gauntlet]], [[Mistra's Academy]] |
| Missing sanitation workers | active | [[Missing Sanitation Workers]] |

## Key organizations
- [[Library of Deneir]]
- [[Mistra's Academy]]
- [[Elementalist Syndicate]]
- [[Skeletal Hand]]
- [[Cult of the Destroyer]]
- [[Dragon League]]
- [[Confederation]]

## Key places
- [[Truemetal Halls]]
- [[Amberhold]]
- [[Axeholm]]
- [[Wren Nalore]]
- [[Venburg]]
- [[Emerald Glade]]
