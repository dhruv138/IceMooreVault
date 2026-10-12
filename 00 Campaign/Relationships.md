---
title: "Relationships"
tags:
  - campaign
  - diagram
  - index
---
# Relationships

Diagrams of who belongs to what and how the campaign's arcs connect. They render natively in Obsidian; click a box to open its note. Dotted lines are suspicions or unconfirmed links, not established facts.

For thread-by-thread boards, see the canvases linked from the [[Campaign Dashboard]].

## Amberhold institutions

```mermaid
flowchart TB
  MA["Mistra's Academy"]
  LD["Library of Deneir"]
  DA["Department of Acquisitions"]
  SH["Skeletal Hand"]
  TM["Temple of Mistra"]

  MA -->|"the Library is an offshoot"| LD
  LD --> DA
  SH -.->|"banned from"| MA
  SH -.->|"banned from"| LD
  MA --- TM

  BO["Bianca Onyxcrest"] -->|"Headmistress"| MA
  GG["Gavin Gosling"] -.->|"former head, died"| MA
  KA["Karyn"] -->|"Bianca's assistant"| BO
  PO["Peter Owens"] -->|"grad student, on leave"| MA
  SP["Samuel Patel"] -->|"Head Cleric"| TM

  TR["Talir Rengavi"] -->|"Director"| LD
  ES["Ester"] -->|"Chief Archivist"| LD
  SI["Siobhan"] -->|"Archivist"| LD
  HG["Hana Goldfirm"] -->|"researcher"| DA
  RI["Riffle"] -->|"field agent"| DA
  RI -->|"father figure"| TR

  PO -.->|"the recruiter 'Peter'?"| SH

  class MA,LD,DA,SH,TM,BO,GG,KA,PO,SP,TR,ES,SI,HG,RI internal-link
```

## Dwarven powers and Venburg

```mermaid
flowchart LR
  CF["Confederation"] -->|"capital"| TH["Truemetal Halls"]
  TH --- CO["Court"]
  ID["Lord Ivan Deepshaft"] -->|"member"| CO
  GR["Gunther Rockhammer"] -->|"runs"| WH["The Warhammer"]
  WH --- TH
  EE["Earl Emberstone"] -->|"father of"| EZ["Elzock Emberstone"]
  EE --- RG["Ring of Gold"]
  RG --- TH

  TD["Truemetal Dwarves"] --- TH
  IR["Iron Dwarves"] --- EB["Eisenberg"]
  BH["Black Hand Dwarves"] -->|"mine anthracite at"| KM["Kohlemine"]
  BH -.->|"doubled the price; another buyer?"| TH
  DU["Duergar"] -.->|"millennia of conflict"| TD

  DH["Darham Hold"] -.->|"broke from the Eisenberg lords"| EB
  OD["Countess Opal Darham"] -->|"rules"| DH
  EB -.->|"unrest sends refugees to"| VB["Venburg"]
  KL["Klaus"] -->|"elected leader"| VB
  ID -->|"sent supply carts"| VB

  class CF,TH,CO,ID,GR,WH,EE,EZ,RG,TD,IR,EB,BH,KM,DU,DH,OD,VB,KL internal-link
```

## The party's people

```mermaid
flowchart TB
  W["WISC"] -->|"grandson"| OM["Oma"]
  UT["Uthal"] -->|"works for"| OM
  F["Furgus"] -->|"brother"| BA["Bad"]
  BA -->|"married"| AN["Annika"]
  F -.->|"complicated"| UT
  D["Deanira"] -->|"mentor, missing"| VA["Val"]
  R["Riffle"] -->|"father figure"| TR["Talir Rengavi"]
  R -->|"best friend"| HG["Hana Goldfirm"]
  T["Theo'din Corvis"] -->|"patron"| RQ["Raven Queen"]
  P["Philip"] -->|"hunter from"| VB["Venburg"]
  W -.->|"same rare eyes"| GB["Golden-Eyed Bugbear Mystery"]

  class W,OM,UT,F,BA,AN,D,VA,R,TR,HG,T,RQ,P,VB,GB internal-link
```

## Campaign arcs

```mermaid
timeline
  title Icemoor campaign by arc
  Sessions 3–8 : The sealed mine under Truemetal Halls : Knockers, Duergar and Abbathor : Emberstone reward and the Court
  Sessions 9–17 : Riffle joins, Daggins and the Axeholm cipher : The stone is an "onion" : Christolf Nightfall's stolen corpses
  Sessions 18–23 : Wren Nalore and the sunken Dragon Cult fortress : Agatha names Zyuir : Exile, then portal home
  Sessions 24–25 : The stone is a fragment of the Lord of Fire : Daggins murdered, Riffle framed
  Sessions 26–30 : Tomb of Quithos the Breaker : Skeletal Hand and the Master of Death
  Sessions 31–35 : Venburg, Oma and the festival : Theo'din joins : Were-bear curse
  Sessions 36–38 : Amberhold : Cure, recruiter flyer, Union of Many : Riffle accused again
```
