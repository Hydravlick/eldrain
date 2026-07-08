---
type: implementation_plan
status: complete
system: project_management
tags: [factions, registry, migration, dataview]
related_files:
  - "[[09_Project_Management/Architecture_MVP|Architecture MVP]]"
  - "[[03_Factions_Societies/_Registries/Registry_Factions|Registry Factions]]"
  - "[[03_Factions_Societies/_Matrices/00_Faction_Reputation|Faction Reputation]]"
---
# Faction Registry Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Превратить 20 записей `Registry_Factions` в самостоятельные фракционные страницы без потери 58 направленных отношений и переключить реестр и карту на новые источники.

**Architecture:** Page-level YAML хранит устойчивые свойства фракции. Повторяемые `rel_*` остаются inline Dataview-полями в теле страницы вместе с причиной. `Registry_Factions` становится native Dataview-обзором, а `00_Faction_Reputation` загружает страницы и парсит отношения без собственного набора данных.

**Tech Stack:** Obsidian Markdown, YAML Properties, Dataview, DataviewJS, D3, Node.js `node:test`.

## Global Constraints

- Git не использовать.
- Не изменять `04_Player_Entities/Races`, `04_Player_Entities/Specs`, `deferred_rule` или `capability`.
- Не менять типы отношений, цели и причины из текущего `Registry_Factions`.
- Не использовать YAML-словари или списки объектов.
- `The_Cartographers.md` остаётся вспомогательным лором без `faction_id`.
- Существующий лор подробных страниц сохраняется целиком.
- Допустимые relation-типы: `conflict`, `hunt`, `monitor`, `spy`, `trade`, `union`.
- Итог: 20 уникальных `faction_id`, 58 relations, включая `monitor -> all` и `hunt -> all`.

---

## File Map

**Extend existing pages**

- `03_Factions_Societies/Lore/The_First_Reception.md` -> `first_reception`
- `03_Factions_Societies/Lore/The_Common_Storehouses.md` -> `common_storehouses`
- `03_Factions_Societies/Lore/The_Circle_of_Interposition.md` -> `circle_of_interposition`
- `03_Factions_Societies/Lore/The_Contour_Chamber.md` -> `contour_chamber`
- `03_Factions_Societies/Lore/The_Weighing_Houses.md` -> `weighing_houses`
- `03_Factions_Societies/Lore/The_Support_Artels.md` -> `support_artels`
- `03_Factions_Societies/Lore/The_Cathedral.md` -> `cathedral_all_faiths`
- `03_Factions_Societies/Lore/The_Proving_Houses.md` -> `proving_houses`
- `03_Factions_Societies/Lore/The_Minstrels.md` -> `minstrels`
- `03_Factions_Societies/Lore/The_Keepers.md` -> `keepers`

**Create missing pages**

- `03_Factions_Societies/Lore/The_Night_Guarantors.md`
- `03_Factions_Societies/Lore/The_Warm_Kitchens.md`
- `03_Factions_Societies/Lore/The_Garden_Chains.md`
- `03_Factions_Societies/Lore/The_Lamp_Shifts.md`
- `03_Factions_Societies/Lore/The_Lift_Families.md`
- `03_Factions_Societies/Lore/The_Chalk_Hands.md`
- `03_Factions_Societies/Lore/The_Funeral_Circles.md`
- `03_Factions_Societies/Lore/The_Free_Benches.md`
- `03_Factions_Societies/Lore/The_Ash_Commission.md`
- `03_Factions_Societies/Lore/The_Hidden_Entity.md`

**Modify views and references**

- `03_Factions_Societies/_Registries/Registry_Factions.md`
- `03_Factions_Societies/_Matrices/00_Faction_Reputation.md`
- `09_Project_Management/Architecture_MVP.md`
- `02_World_Lore/The_Anchor.md`
- `tests/faction-registry.test.mjs`

---

### Task 1: Lock source preservation with a failing test

**Files:**
- Create: `tests/faction-registry.test.mjs`

**Interfaces:**
- Consumes: YAML `type`, `faction_id`, `display_name`, `faction_role`, `promise`; body `[rel_TYPE:: TARGET] (REASON)`.
- Produces: exact entity and relation invariants for later tasks.

- [x] Add a test reader that scans `03_Factions_Societies/Lore/*.md`, selects `type: faction`, parses frontmatter scalars and inline relations.
- [x] Assert the exact 20-ID set: `ash_commission`, `cathedral_all_faiths`, `chalk_hands`, `circle_of_interposition`, `common_storehouses`, `contour_chamber`, `first_reception`, `free_benches`, `funeral_circles`, `garden_chains`, `hidden_entity`, `keepers`, `lamp_shifts`, `lift_families`, `minstrels`, `night_guarantors`, `proving_houses`, `support_artels`, `warm_kitchens`, `weighing_houses`.
- [x] Assert 58 relations with type counts `conflict=18`, `hunt=1`, `monitor=5`, `spy=5`, `trade=9`, `union=20`.
- [x] Assert each target is another ID or `all`, every reason is non-empty, and `The_Cartographers` has no `faction_id`.
- [x] Assert `Registry_Factions` contains the Lore Dataview query and no `[faction::` or `[rel_` fields.
- [x] Assert `00_Faction_Reputation` reads `03_Factions_Societies/Lore` and does not parse `Registry_Factions.md`.
- [x] Run the red test before migration and confirm that the block-based registry fails the new contract.

---

### Task 2: Promote ten existing lore pages

**Files:** ten existing pages listed in File Map.

**Interfaces:**
- Consumes: the matching block in `Registry_Factions`.
- Produces: one canonical page with YAML identity and inline relations.

- [x] Change frontmatter `type: lore` to `type: faction` and `system: factions_lore` to `system: factions` while preserving all existing tags, `related_files`, and `related_mechanics`.
- [x] Add scalar fields in this order: `faction_id`, `display_name`, `sort_order`, `faction_role`, optional `player_label`, `promise`, optional `access_model`, optional `hearth_origin`.
- [x] Preserve each existing page body as its detailed profile without copying that lore into the family hub.
- [x] Insert `## Отношения` after the H1 and copy each relation exactly as `[rel_TYPE:: TARGET] (REASON)`.
- [x] Run the intermediate test and confirm the ten promoted entities preserve their relation subsets.

---

### Task 3: Create ten missing faction pages

**Files:** ten new pages listed in File Map.

**Interfaces:**
- Consumes: the ten blocks without `detail` pages in `Registry_Factions`.
- Produces: minimal but complete independent faction pages.

- [x] Use the same scalar YAML contract as Task 2 and `tags: [faction, <faction_role>]`.
- [x] Body structure: H1, one-line promise, `## Роль в городе`, registry description, `## Отношения`, exact relation lines.
- [x] Use sort order `100` through `180` in registry order. `The_Hidden_Entity` uses `sort_order: 200` and remains `faction_role: hidden`.
- [x] Run the intermediate test and confirm entity and relation counts before converting the views.

---

### Task 4: Convert Registry_Factions into the family hub

**Files:**
- Modify: `03_Factions_Societies/_Registries/Registry_Factions.md`
- Modify: `09_Project_Management/Architecture_MVP.md`
- Modify: `02_World_Lore/The_Anchor.md`
- Modify: entity-page deep links to headings inside the old faction registry found during the initial audit.

**Interfaces:**
- Consumes: 20 page-level faction entities.
- Produces: stable family entrypoint with no duplicate entity data.

- [x] Preserve the current explanations of the ecosystem and action types at the top of `Registry_Factions`.
- [x] Remove all faction blocks and the block template.
- [x] Add native Dataview:

```dataview
TABLE WITHOUT ID
  file.link AS "Фракция",
  faction_role AS "Роль",
  player_label AS "Игроковый контур",
  promise AS "Обещание"
FROM "03_Factions_Societies/Lore"
WHERE type = "faction"
SORT sort_order ASC
```

- [x] Replace deep links to registry headings with direct page links.
- [x] Update `Architecture_MVP` from transition wording to current page-level source wording and increment version once.
- [x] Run `node --test tests/faction-registry.test.mjs`; hub assertions pass.

---

### Task 5: Switch 00_Faction_Reputation to faction pages

**Files:**
- Modify: `03_Factions_Societies/_Matrices/00_Faction_Reputation.md`
- Test: `tests/faction-registry.test.mjs`

**Interfaces:**
- Consumes: `dv.pages('"03_Factions_Societies/Lore"')` filtered by `type === "faction"` plus inline `rel_*` fields loaded with `dv.io.load(page.file.path)`.
- Produces: the existing radial graph with unchanged filters, directions, reasons and `all` expansion.

- [x] Replace `sourceFilePath` and registry block splitting with page enumeration.
- [x] Normalize each node to `id`, `name`, `path`, `isCenter`, `desc`, `rawRelations`.
- [x] Detect duplicate IDs, unknown targets, unknown relation types and empty relation reasons before rendering; show them in the Dataview error block.
- [x] Expand `target: all` to all other non-player faction nodes exactly as the current graph does.
- [x] Open the node's `path` on click instead of a registry heading.
- [x] Run the faction suite successfully and execute the full suite; two current race/synergy assertions remain outside this migration because `Hedgehog.md` now exposes one parsed `weak_to` value instead of three.

---

### Task 6: Close and verify migration

**Files:**
- Modify: `09_Project_Management/Faction_Registry_Migration_Plan_2026-07-08.md`

- [x] Validate YAML for all `type: faction` pages with PyYAML.
- [x] Parse the DataviewJS block by compiling it as an async function.
- [x] Verify active vault pages contain no links to faction headings inside `Registry_Factions`.
- [x] Verify `rg -n "^\[(faction|rel_[a-z_]+)::" 03_Factions_Societies/_Registries/Registry_Factions.md` has no results.
- [x] Set this plan to `status: complete` after the faction-specific verification commands pass.
