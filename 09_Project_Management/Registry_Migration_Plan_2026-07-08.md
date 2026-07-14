---
type: implementation_plan
status: superseded
system: project_management
tags: [registry, migration, dataview, player_entities]
related_files:
  - "[[09_Project_Management/Architecture_MVP|Architecture MVP]]"
  - "[[04_Player_Entities/_Registries/Registry_Races|Registry Races]]"
  - "[[04_Player_Entities/_Registries/Registry_Specs|Registry Specs]]"
  - "[[04_Player_Entities/_Registries/Registry_Combos|Registry Combos]]"
  - "[[04_Player_Entities/_Matrices/00_Synergy_Map|Synergy Map]]"
---
# Entity Registry Migration Implementation Plan

> **Исторический план.** Миграция была выполнена для прежней наследуемой модели, но её вычисляемые `base_vector`, `weak_to` и T.O.U.C.H.-поля сняты новым контрактом authored hero-kit. Этот файл не является источником активной схемы; текущий канон: [[04_Player_Entities/Combat_Profile_Pipeline|Combat Profile Pipeline]] и [[04_Player_Entities/_Registries/Registry_Combos|Registry Combos]].

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Перенести расы и практики в отдельные YAML-сущности, оставить комбинации единым дельта-реестром и сократить четыре пересекающиеся матрицы до обзора комбинаций и карты синергий.

**Architecture:** Страница расы или практики является единственным page-level YAML-источником собственных полей. `Registry_Races` и `Registry_Specs` становятся семейными обзорами на native Dataview, а `Registry_Combos` сохраняет блочные записи и вычисляет наследуемый профиль через DataviewJS. `00_Synergy_Map` читает те же YAML-источники; старые матрицы выводятся из активной структуры только после прохождения тестов.

**Tech Stack:** Obsidian Markdown, YAML Properties, Dataview, DataviewJS, Node.js `node:test`.

## Global Constraints

- Работать только с файлами внутри текущего vault; Git не использовать.
- Не изменять `00_Faction_Reputation` и структуру `Registry_Factions`.
- Не хранить `TOUCH`, `base_vector`, `weak_to`, биологическую основу или методологию практики в `Registry_Combos`.
- Не использовать embeds как наследование данных.
- Не вводить Obsidian Bases: текущий pipeline уже опирается на Dataview, а второй слой представления не нужен.
- Во всех представлениях показывать отсутствующий источник, дублирующий ID и пустой результат.
- Сохранить текущую семантику `00_Synergy_Map`: 9 MVP-профилей, 30 строгих контр-связей, 6 сильных поддержек и 6 пар общей слабости.

---

## File Map

**Create**

- `_Archive/_MERGED_SOURCES.md`
- `04_Player_Entities/Races/Hedgehog.md`
- `04_Player_Entities/Races/Rat.md`
- `04_Player_Entities/Races/Squirrel.md`
- `04_Player_Entities/Races/Toad.md`
- `04_Player_Entities/Races/Lizard.md`
- `04_Player_Entities/Specs/Guardian.md`
- `04_Player_Entities/Specs/Vanguard.md`
- `04_Player_Entities/Specs/Technocrat.md`
- `04_Player_Entities/Specs/Drifter.md`
- `04_Player_Entities/Specs/Dogmat.md`
- `tests/entity-registry.test.mjs`

**Modify**

- `04_Player_Entities/_Registries/Registry_Races.md`
- `04_Player_Entities/_Registries/Registry_Specs.md`
- `04_Player_Entities/_Registries/Registry_Combos.md`
- `04_Player_Entities/_Matrices/00_Synergy_Map.md`
- `tests/synergy-map.test.mjs`
- `04_Player_Entities/Two_Paradox_Vector_Matrix.md`
- `04_Player_Entities/Two_Paradox_Birth.md`
- `04_Player_Entities/Tags_System.md`
- `09_Project_Management/Risk_Register.md`
- `09_Project_Management/Architecture_MVP.md`
- deep links in race culture pages, `02_World_Lore/Energy_Concept.md`, `03_Factions_Societies/Lore/The_Cathedral.md` and `05_Combat_Survival/Magic_Batteries.md`

**Move out of active structure after verification**

- `04_Player_Entities/_Matrices/00_Archetype_Matrix.md` -> `_Archive/Merged/Legacy_00_Archetype_Matrix.md`
- `04_Player_Entities/_Matrices/00_Character_Matrix.md` -> `_Archive/Merged/Legacy_00_Character_Matrix.md`
- `04_Player_Entities/_Matrices/00_Balance.md` -> `_Archive/Merged/Legacy_00_Balance.md`

---

### Task 1: Lock the entity and inheritance contract with tests

**Files:**
- Create: `tests/entity-registry.test.mjs`
- Modify: `tests/synergy-map.test.mjs`

**Interfaces:**
- Consumes: page YAML fields `type`, `id`, `content_scope`, `base_vector`, `weak_to`, `touch`.
- Produces: regression checks used by every later task.

- [x] **Step 1: Add a frontmatter reader using only Node built-ins**

```js
function scalar(frontmatter, key) {
    return frontmatter.match(new RegExp(`^${key}:\\s*([^\\n]+)$`, "m"))?.[1]?.trim().replace(/^['"]|['"]$/g, "");
}

function inlineList(frontmatter, key) {
    const raw = scalar(frontmatter, key) || "[]";
    return raw.replace(/^\[|\]$/g, "").split(",").map(value => value.trim()).filter(Boolean);
}
```

- [x] **Step 2: Add failing assertions for the target source layout**

```js
assert.deepEqual(raceIds.sort(), ["hedgehog", "lizard", "rat", "squirrel", "toad"]);
assert.deepEqual(specIds.sort(), ["assault", "guard", "scout", "specialist", "support"]);
assert.equal(new Set(raceIds).size, raceIds.length);
assert.equal(new Set(specIds).size, specIds.length);
assert.doesNotMatch(comboRegistry, /\[base_weakness::/);
assert.doesNotMatch(raceHub, /\[id::/);
assert.doesNotMatch(specHub, /\[id::/);
```

- [x] **Step 3: Verify the test fails before migration**

Run: `node --test tests/entity-registry.test.mjs`

Expected: FAIL because `04_Player_Entities/Races` and `04_Player_Entities/Specs` do not exist and the hubs still contain inline IDs.

- [x] **Step 4: Change `tests/synergy-map.test.mjs` fixtures to read page YAML folders**

Replace block parsing for races/specs with `parseEntityFolder("04_Player_Entities/Races", "race")` and `parseEntityFolder("04_Player_Entities/Specs", "spec")`. Keep block parsing only for `Registry_Combos.md`.

- [x] **Step 5: Run the full test set and record the expected temporary failure**

Run: `node --test tests/entity-registry.test.mjs tests/synergy-map.test.mjs`

Expected: the existing pure synergy helper tests pass; source-layout tests fail until Tasks 2-5 are complete.

---

### Task 2: Create five race YAML entities

**Files:**
- Create: `04_Player_Entities/Races/Hedgehog.md`
- Create: `04_Player_Entities/Races/Rat.md`
- Create: `04_Player_Entities/Races/Squirrel.md`
- Create: `04_Player_Entities/Races/Toad.md`
- Create: `04_Player_Entities/Races/Lizard.md`

**Interfaces:**
- Consumes: all fields and prose currently owned by race blocks in `Registry_Races.md`.
- Produces: one page-level YAML source per race.

- [x] **Step 1: Create each page with the same property schema**

```yaml
---
type: race
status: active
system: player_entities
id: hedgehog
display_name: Ёж
latin_name: Erinaceus
sort_order: 10
content_scope: mvp
base_vector: kinetics
weak_to: [hazard, shadow, aether]
touch: {TRQ: 4, GRP: -2, LYR: 3, GLW: -1, SNS: 0}
substats: {brace: 15, recoil_damp: 8, trauma_resist: 10}
cap_mod: {max_carry_kg: 5}
vulnerability_note: slow_reposition
culture: "[[02_World_Lore/Hedgehog_Culture|Ежи: Культура Удерживаемого Пространства]]"
tags: [race, player_entity]
---
```

Use `content_scope: post_mvp` for Toad and Lizard. Preserve every current value exactly; normalize only YAML shape and numeric zeroes.

- [x] **Step 2: Move the biological basis and description into the page body**

Each page has exactly:

```markdown
# Ёж (Erinaceus)

> Несокрушимый оплот стабильности.

## Биологическая основа: Масса и иглы

<current biological basis without data duplication>

## Описание

<current description>
```

- [x] **Step 3: Verify all race pages expose required fields**

Run: `node --test tests/entity-registry.test.mjs`

Expected: race count and unique race IDs pass; hub assertions still fail.

---

### Task 3: Create five specialization YAML entities

**Files:**
- Create: `04_Player_Entities/Specs/Guardian.md`
- Create: `04_Player_Entities/Specs/Vanguard.md`
- Create: `04_Player_Entities/Specs/Technocrat.md`
- Create: `04_Player_Entities/Specs/Drifter.md`
- Create: `04_Player_Entities/Specs/Dogmat.md`

**Interfaces:**
- Consumes: all fields and prose currently owned by spec blocks in `Registry_Specs.md`.
- Produces: one page-level YAML source per specialization.

- [x] **Step 1: Create each page with the same property schema**

```yaml
---
type: spec
status: active
system: player_entities
id: assault
display_name: Авангард
english_name: The Vanguard
sort_order: 20
content_scope: mvp
base_vector: ballistics
weak_to: [hazard, kinetics, tech]
touch: {TRQ: 2, GRP: 2, LYR: 1, GLW: 2, SNS: -2}
substats: {drift_control: 10, cell_swap_speed: 8, recoil_damp: 8}
condition_bonus: {after_stagger_weapon_swap_speed: 10}
tradeoff: {dissonance_load: 2}
tags: [spec, practice, player_entity]
---
```

Use `content_scope: post_mvp` for Guardian and Dogmat. Preserve every current value and example; do not invent missing tradeoffs.

- [x] **Step 2: Move methodology, transparent label and examples into the page body**

```markdown
# Авангард (The Vanguard)

> Линия импульса, магострельное давление и окно для добивания.

## Методология

<current description>

## Примеры профессий

<current examples>
```

- [x] **Step 3: Verify all spec pages expose required fields**

Run: `node --test tests/entity-registry.test.mjs`

Expected: entity counts and unique IDs pass; hub assertions still fail.

---

### Task 4: Convert race and spec registries into family hubs

**Files:**
- Modify: `04_Player_Entities/_Registries/Registry_Races.md`
- Modify: `04_Player_Entities/_Registries/Registry_Specs.md`
- Modify: deep links listed by `rg -n "Registry_(Races|Specs)#" . -g "*.md" -g "!_Archive/**"`

**Interfaces:**
- Consumes: entity YAML pages from Tasks 2-3.
- Produces: stable family entrypoints with no duplicated entity fields.

- [x] **Step 1: Replace race blocks with a native Dataview overview**

```dataview
TABLE WITHOUT ID
  file.link AS "Раса",
  content_scope AS "Контур",
  base_vector AS "Вектор",
  join(weak_to, ", ") AS "Слабости",
  culture AS "Культура"
FROM "04_Player_Entities/Races"
WHERE type = "race"
SORT sort_order ASC
```

- [x] **Step 2: Replace spec blocks with a native Dataview overview**

```dataview
TABLE WITHOUT ID
  file.link AS "Практика",
  content_scope AS "Контур",
  base_vector AS "Вектор",
  join(weak_to, ", ") AS "Слабости"
FROM "04_Player_Entities/Specs"
WHERE type = "spec"
SORT sort_order ASC
```

- [x] **Step 3: Preserve the family contracts above each query**

Keep the current MVP scope, race terminology and rule that `P/Q/E` belong to `Race × Spec`. Remove templates and all inline entity fields from both hubs.

- [x] **Step 4: Redirect heading links to entity pages**

Examples:

```markdown
[[04_Player_Entities/Races/Hedgehog|Ёж]]
[[04_Player_Entities/Races/Toad|Жаба]]
[[04_Player_Entities/Specs/Dogmat|Догмат]]
```

General links to `Registry_Races` and `Registry_Specs` remain valid because the hubs remain canonical family entrypoints.

- [x] **Step 5: Verify no duplicate source remains**

Run: `node --test tests/entity-registry.test.mjs`

Expected: all entity and hub tests pass.

---

### Task 5: Make Registry_Combos the only combination overview

**Files:**
- Modify: `04_Player_Entities/_Registries/Registry_Combos.md`
- Test: `tests/entity-registry.test.mjs`

**Interfaces:**
- Consumes: race/spec page YAML plus combo block fields.
- Produces: 3×3 navigation grid and compact inherited-profile table.

- [x] **Step 1: Remove inherited fields from combo blocks**

Delete every `[base_weakness:: ...]`. Do not add `base_vector`, `weak_to`, TOUCH fields or copied prose.

- [x] **Step 2: Add a DataviewJS loader with two source modes**

```js
const races = dv.pages('"04_Player_Entities/Races"').where(page => page.type === "race");
const specs = dv.pages('"04_Player_Entities/Specs"').where(page => page.type === "spec");
const comboSource = await dv.io.load(dv.current().file.path);
```

Parse combo blocks by `id`, `req_race`, `req_spec` and `design_status`. Resolve parents through maps keyed by YAML `id`.

- [x] **Step 3: Render the matrix as navigation and status, not a second source**

Each cell displays a link to the combo heading and one status: `approved`, `pending` or `missing`. Missing race/spec IDs render as a visible warning.

- [x] **Step 4: Render one compact audit table**

Columns: combination, race, practice, inherited vectors, computed shared weakness, design status. Do not render all TOUCH values, weapons, modules or abilities globally.

- [x] **Step 5: Verify all nine combo references resolve**

Run: `node --test tests/entity-registry.test.mjs`

Expected: 9 combo IDs, no missing parents, no duplicate IDs and no `base_weakness` fields.

---

### Task 6: Switch 00_Synergy_Map to page-level parents

**Files:**
- Modify: `04_Player_Entities/_Matrices/00_Synergy_Map.md`
- Modify: `tests/synergy-map.test.mjs`

**Interfaces:**
- Consumes: race/spec YAML pages and combo block records.
- Produces: unchanged counter/support/shared-weakness views.

- [x] **Step 1: Replace race/spec file paths with folder paths**

```js
const sources = {
    races: "04_Player_Entities/Races",
    specs: "04_Player_Entities/Specs",
    combos: "04_Player_Entities/_Registries/Registry_Combos.md"
};
```

- [x] **Step 2: Add page-level normalization**

```js
function entityRecord(page) {
    return {
        id: cleanId(page.id),
        name: page.display_name || page.file.name,
        path: page.file.path,
        baseVector: cleanId(page.base_vector),
        weakTo: Array.from(page.weak_to || []).map(cleanId).filter(Boolean)
    };
}
```

Keep the combo block parser. Links from graph nodes open the race/spec page or combo heading represented by the node.

- [x] **Step 3: Keep current missing-source and empty-state UI**

If either folder has no valid pages, render `Ошибка загрузки` with the exact missing source. Filter combos with unresolved parents and list their IDs instead of silently dropping them.

- [x] **Step 4: Run synergy tests**

Run: `node --test tests/synergy-map.test.mjs`

Expected: 8 tests pass, including counts `30 / 6 / 6`.

- [x] **Step 5: Run all tests**

Run: `node --test tests/entity-registry.test.mjs tests/synergy-map.test.mjs`

Expected: all tests pass.

---

### Task 7: Retire duplicate matrices and repair references

**Files:**
- Move: three legacy matrices listed in File Map
- Modify: `04_Player_Entities/Two_Paradox_Vector_Matrix.md`
- Modify: `04_Player_Entities/Two_Paradox_Birth.md`
- Modify: `04_Player_Entities/Tags_System.md`
- Modify: `09_Project_Management/Risk_Register.md`

**Interfaces:**
- Consumes: working `Registry_Combos` overview and `00_Synergy_Map`.
- Produces: one active navigation view and one active tactical view.

- [x] **Step 1: Move the three obsolete matrices into `_Archive/Merged`**

Before moving, resolve every source and destination to an absolute path and verify both remain under `C:\eldrain`.

- [x] **Step 2: Replace active references**

Use these responsibilities consistently:

- `Registry_Combos`: coverage, status and inherited profile.
- `00_Synergy_Map`: counters, strong support and shared weaknesses.
- `tests/entity-registry.test.mjs`: source integrity.
- `tests/synergy-map.test.mjs`: relation math.

- [x] **Step 3: Verify active notes no longer link to retired matrices**

Run: `rg -n "00_(Archetype_Matrix|Character_Matrix|Balance)" . -g "*.md" -g "!_Archive/**"`

Expected: only the historical migration explanation in `Architecture_MVP.md`, or no matches after wording cleanup.

- [x] **Step 4: Verify the active matrix folder is lean**

Run: `rg --files 04_Player_Entities/_Matrices`

Expected: only `04_Player_Entities/_Matrices/00_Synergy_Map.md`.

---

### Task 8: Close the migration contract

**Files:**
- Modify: `09_Project_Management/Architecture_MVP.md`
- Modify: `09_Project_Management/Registry_Migration_Plan_2026-07-08.md`

**Interfaces:**
- Consumes: verified final structure.
- Produces: architecture that describes current reality rather than a transition.

- [x] **Step 1: Remove the transitional-source warning from Architecture_MVP**

Replace it with a statement that `Registry_Races` and `Registry_Specs` are family views and their entity folders are canonical sources. Increment architecture version from `3.1` to `3.2`.

- [x] **Step 2: Mark this plan complete only after final verification**

Set frontmatter `status: complete` and check each task checkbox only when its command has passed.

- [x] **Step 3: Run final verification**

Run: `node --test tests/entity-registry.test.mjs tests/synergy-map.test.mjs`

Expected: all tests pass.

Run: `rg -n "Registry_(Races|Specs)#" . -g "*.md" -g "!_Archive/**"`

Expected: no deep links to removed hub headings.

Run: `rg -n "\[(id|base_vector|weak_to|TRQ|GRP|LYR|GLW|SNS)::" 04_Player_Entities/_Registries/Registry_Races.md 04_Player_Entities/_Registries/Registry_Specs.md`

Expected: no matches.
