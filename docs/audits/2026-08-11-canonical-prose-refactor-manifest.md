# Canonical prose-refactor audit manifest — 2026-08-11

## Scope and decision boundary

This is writable execution state for the complete Pass A and Pass B run. It
records every approved owner-scoped prose batch, every `KEEP` disposition, and
the source inventory for the responsibility review. It does not authorize
generated navigation, registry rewrites, management-note changes, or edits to a
row marked `KEEP`.

Audit baseline: `dc346d98e6246585266a5d49bbb7c6cbed737ca6`.

The deterministic owner enumeration found 126 active routed owners: 3 in
`01_Core_Vision`, 7 in `02_World_Lore`, 7 in `03_Factions_Societies`, 14 in
`04_Player_Entities`, 20 in `05_Combat_Survival`, 13 in `06_Economy_Loot`, 22
in `07_Gear_Inventory`, and 40 in `08_World_Generation`.

The detect-only scan covered every non-route Markdown file in those domains. It
returned 250 candidates: 1, 18, 14, 10, 21, 1, 138, and 47 respectively. This
differs from the historical brief total of 258; this manifest records the actual
baseline result rather than manufacturing eight candidates.

## Approved Pass A batch index

| Batch | Pass | Register | Owner | Decision | Status |
|---|---|---|---|---|---|
| A-05-01 | Pass A + Pass B | MECHANIC | Traversal Core | Direct opening rule | REWRITE COMPLETE |
| A-01-01 | Pass A | SYSTEM | Material Grammar | Damage feedback sentence | REWRITE COMPLETE |
| A-03-01 | Pass A | MECHANIC | Reputation Rules | Political-consequence sentence | REWRITE COMPLETE |
| A-05-02 | Pass A | MECHANIC | Combat Three Debts | Debt-trace opening | REWRITE COMPLETE |
| A-08-01 | Pass A | PRESENTATION | Hub Time & Atmosphere | Weather consequence sentence | REWRITE COMPLETE |
| A-02-01 | Pass A | LORE | Lizard Culture | Remove duplicated race/temperament scaffold | REWRITE COMPLETE |
| A-02-02 | Pass A | LORE | Squirrel Culture | Remove duplicated race/temperament scaffold | REWRITE COMPLETE |
| A-02-03 | Pass A | LORE | Toad Culture | Remove duplicated race/temperament scaffold | REWRITE COMPLETE |
| A-02-04 | Pass A | LORE | Lizard Culture | Remove redundant cross-culture opening scaffold | REWRITE COMPLETE |
| A-02-05 | Pass A | LORE | Squirrel Culture | Remove redundant cross-culture opening scaffold | REWRITE COMPLETE |
| A-02-06 | Pass A | LORE | Toad Culture | Remove redundant cross-culture opening scaffold | REWRITE COMPLETE |
| B-03-01 | Pass B | INTERFACE → MECHANIC | First Reception continuity admission | Move duplicated lifecycle out of lore | MIGRATED |

### A-05-01 — Traversal Core opening

- **Editable surface:** the opening paragraph under `## 1. Тактическая География`, anchored at line 18; the supported defect is confined to its contrast clause.
- **Canonical owner:** `05_Combat_Survival/Traversal_Core.md` (`index_route: owner`).
- **Direct dependencies:** `05_Combat_Survival/Movement_Physics.md` and `08_World_Generation/Generation/10_World_Topology.md` are named by `related_files`; they are read-only context for this batch.
- **Incoming links:** `05_Combat_Survival/00_Routes.md` is the only current incoming corpus link. It is generated and is not editable in this batch.
- **Evidence:** under `## 1. Тактическая География`, line 18 opens with “Успех выживания зависит не только от меткости, но и от грамотного использования геометрии уровня.” The scanner classifies this as `FORMULAIC_PROSE`; the surrounding three-tier list already supplies the concrete rule.
- **Curator finding:** `FORMULAIC_PROSE`. The contrast construction delays the player-facing premise without adding a condition, state, value, or boundary.
- **Smallest safe repair:** replace only the contrast clause with a direct premise that survival depends on marksmanship and use of level geometry; retain the Verticality term and the following three-echelon list unchanged.
- **Preserved meaning:** the three-echelon topology, each tier’s examples and trade-offs, the 2.5 metre climb limit, no-sticky-cover boundary, all hazards, YAML, headings, links, numeric literals, and table structure.
- **Approval:** approved by this prose-refactor plan for one MECHANIC owner; no lore, balance, or location-design decision is introduced.
- **Validation:** `validate_rewrite.py` returned `valid: true`; the post-edit scanner returned zero findings, `test_canonical_guidance.py` passed, `git diff --check` passed, and the final `vault_guard.py` run exited 0 with no output.

### A-01-01 — Material Grammar feedback

- **Editable surface:** the complete feedback paragraph under its existing material-grammar heading, anchored at line 115.
- **Evidence and finding:** `FORMULAIC_PROSE`; “не только … но и” repeats the preceding concrete damage grammar while delaying the readable player consequence.
- **Smallest repair:** state directly that the player sees both the break and the location of the broken continuity.
- **Preserved meaning:** all material signals, the damage examples, the Thermos cross-link, headings, table, and gameplay-feedback rule.
- **Approval and validation:** curator-approved SYSTEM batch; snapshot `C:\Temp\eldrain-prose-refactor-pass-a-02\Art_Direction_Material_Grammar.md`, protected-structure validation, exact diff, and prose scan.

### A-03-01 — Reputation consequence

- **Editable surface:** the complete political-consequence paragraph, anchored at line 55.
- **Evidence and finding:** `FORMULAIC_PROSE`; the contrast construction restates the documented faction-conflict consequence without adding a new condition or outcome.
- **Smallest repair:** name the political effect directly: a contribution changes the city balance rather than merely helping one party.
- **Preserved meaning:** the disputed-contract trigger, reputation gain/loss, faction terminology, city-balance consequence, access rules, and all links. Lorekeeper review preserves the institution-facing meaning; no responsibility moves.
- **Approval and validation:** curator/lorekeeper-approved MECHANIC batch; snapshot `C:\Temp\eldrain-prose-refactor-pass-a-02\Reputation_Rules.md`, protected-structure validation, exact diff, and prose scan.

### A-05-02 — Three Debts trace

- **Editable surface:** the complete debt-trace opening paragraph, anchored at line 55.
- **Evidence and finding:** `FORMULAIC_PROSE`; “не только HP или статус” is an announcement before the concrete trace, route, cargo, and POI consequences.
- **Smallest repair:** open with the complete consequence of a strong action and keep the no-idle-punishment boundary unchanged.
- **Preserved meaning:** six-step interaction sequence, trace/counterplay, route, cargo, POI, chosen-action cost, and all state terms.
- **Approval and validation:** curator-approved MECHANIC batch; snapshot `C:\Temp\eldrain-prose-refactor-pass-a-02\Combat_Three_Debts.md`, protected-structure validation, exact diff, and prose scan.

### A-08-01 — Hub weather presentation

- **Editable surface:** the complete weather-presentation paragraph, anchored at line 31.
- **Evidence and finding:** `FORMULAIC_PROSE`; “не только атмосферу” repeats the blockquote’s cosmetic boundary before the concrete projected effects.
- **Smallest repair:** list atmosphere and the projected physics/route/gear/enemy/trap/exit bundle directly, retaining the Dynamic Weather owner link.
- **Preserved meaning:** presentation-only role, atmospheric examples, gameplay relevance, the downstream owner, and the explicit non-ownership boundary.
- **Approval and validation:** curator-approved PRESENTATION batch; snapshot `C:\Temp\eldrain-prose-refactor-pass-a-02\04_Time_Atmosphere.md`, protected-structure validation, exact diff, and prose scan.

### A-02-01 — Lizard Culture opening

- **Editable surface:** the complete culture-opening paragraph, anchored at line 31.
- **Canonical owner and dependency:** `02_World_Lore/Lizard_Culture.md` is a LORE owner; `02_World_Lore/Culture_Language.md#Биологическая Норма Города` owns the cluster-wide rule that ancestry does not determine an individual’s character, beliefs, or profession.
- **Evidence and finding:** line 31 repeats that owner rule, then uses the same four-adjective temperament scaffold as the Squirrel and Toad culture openings. The unique claim is the false-sea consequence of mistaking appearance for reality.
- **Smallest repair:** retain only that Lizard-specific bodily inheritance and causal consequence.
- **Preserved meaning:** the Great Lens world, unreliable appearance, caravan risk, all headings, links, and lore voice; no rule moves from World Lore.
- **Approval and validation:** curator/lorekeeper-approved LORE batch; snapshot `C:\Temp\eldrain-prose-refactor-culture-cluster-20260811\Lizard_Culture.md`, protected-structure validation, exact diff, and prose scan.

### A-02-02 — Squirrel Culture opening

- **Editable surface:** the complete culture-opening paragraph, anchored at line 29.
- **Canonical owner and dependency:** `02_World_Lore/Squirrel_Culture.md` is a LORE owner; `02_World_Lore/Culture_Language.md#Биологическая Норма Города` already owns the non-deterministic ancestry rule.
- **Evidence and finding:** line 29 repeats that rule and the same four-adjective scaffold. Its non-duplicated cultural claim is attention to routes, changing stores, and the cost of delay.
- **Smallest repair:** state that Squirrel inheritance directly, without restating an individual-temperament norm.
- **Preserved meaning:** distributed readiness, storage timing, routes, all headings, links, and lore voice; no World Lore responsibility changes.
- **Approval and validation:** curator/lorekeeper-approved LORE batch; snapshot `C:\Temp\eldrain-prose-refactor-culture-cluster-20260811\Squirrel_Culture.md`, protected-structure validation, exact diff, and prose scan.

### A-02-03 — Toad Culture opening

- **Editable surface:** the complete culture-opening paragraph, anchored at line 34.
- **Canonical owner and dependency:** `02_World_Lore/Toad_Culture.md` is a LORE owner; `02_World_Lore/Culture_Language.md#Биологическая Норма Города` owns the repeated anti-essentialist rule.
- **Evidence and finding:** line 34 repeats that rule and the cluster’s four-adjective temperament scaffold. Its unique claim is the Toad practice of reading an object through the conditions that formed it; the previous `KEEP` disposition was unsupported.
- **Smallest repair:** preserve the condition-of-becoming observation as the complete culture-specific sentence.
- **Preserved meaning:** transformation, care, material conditions, all headings, links, and lore voice; no World Lore responsibility changes.
- **Approval and validation:** curator/lorekeeper-approved LORE batch; snapshot `C:\Temp\eldrain-prose-refactor-culture-cluster-20260811\Toad_Culture.md`, protected-structure validation, exact diff, and prose scan.

### A-02-04 — Lizard Culture comparative scaffold

- **Editable surface:** the complete culture-opening paragraph, anchored at line 27.
- **Canonical owner and evidence:** `02_World_Lore/Culture_Language.md#Культура за пределами функции` already owns the comparative matrix: a people’s historical contribution does not reduce its full life to a function. The Lizard opening redundantly named Rat and Squirrel before stating its own criterion.
- **Smallest repair:** retain the full Lizard question of evidence, time, and changed reality as a single owner-local premise.
- **Preserved meaning:** the verifiable-state thesis, independent testimony, and all later cartographic causality; no comparison is needed for the premise to be intelligible.
- **Approval and validation:** curator/lorekeeper-approved separate LORE batch; snapshot `C:\Temp\eldrain-prose-refactor-culture-cross-comparison-20260811\Lizard_Culture.md`, protected-structure validation, exact diff, and prose scan.

### A-02-05 — Squirrel Culture comparative scaffold

- **Editable surface:** the complete culture-opening paragraph, anchored at line 25.
- **Canonical owner and evidence:** `02_World_Lore/Culture_Language.md#Культура за пределами функции` owns the cluster comparison. The Squirrel opening used Rat only as a contrast before stating its actual route-and-delivery premise.
- **Smallest repair:** make location, recipient, route, and route loss the direct definition of distributed readiness.
- **Preserved meaning:** caches, stores, signal networks, emergency rations, timing, and the civic minimum; no other people’s role is required to carry it.
- **Approval and validation:** curator/lorekeeper-approved separate LORE batch; snapshot `C:\Temp\eldrain-prose-refactor-culture-cross-comparison-20260811\Squirrel_Culture.md`, protected-structure validation, exact diff, and prose scan.

### A-02-06 — Toad Culture comparative scaffold

- **Editable source:** `02_World_Lore/Toad_Culture.md`; complete culture-opening paragraph, anchored at line 30.
- **Canonical owner and evidence:** `02_World_Lore/Culture_Language.md#Культура за пределами функции` already says that a people are not reducible to a function. The Toad opening’s Rat comparison contributed no distinct condition beyond the Toad question of transformation.
- **Smallest repair:** make the possible transformation and the environment required for it the direct cultural premise.
- **Preserved meaning:** medicine, wet alchemy, Cup architecture, body rites, the Cathedral link, and the conflict between care and imposed outcome.
- **Approval and validation:** curator/lorekeeper-approved separate LORE batch; snapshot `C:\Temp\eldrain-prose-refactor-culture-cross-comparison-20260811\Toad_Culture.md`, protected-structure validation, exact diff, and prose scan.

### B-03-01 — First Reception continuity admission

- **Editable sources:** `03_Factions_Societies/Lore/The_First_Reception.md`, `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`; existing mechanic owner `04_Player_Entities/Spawn_Logic.md` is read as the target and remains the lifecycle resolver.
- **Evidence:** the lore page’s complete `## Протокол нулевого ростера` repeated `ContinuityAdmissionAllowed`, atomic Ward creation, `WelfareEligible`, tag boundaries, and raid entry already specified under `Spawn_Logic#2. Первый Приём при ContinuityAdmissionAllowed`; the active interface `first_reception.continuity_admission_presentation` already names that mechanic owner.
- **Responsibility repair:** lore now carries only the First Reception’s civic presentation of a living candidate. The interface record states the resolved Ready-Ward result. Spawn Logic remains the single owner of lifecycle resolution, while Lifecycle Roster remains its predicate owner.
- **Preserved meaning:** one named living candidate, announced hero-kit, one Ready Ward, no duplicate Ward or Welfare overlay, no reroll/trait preview, no altered raid path, and the First Reception’s `PROVIDER` role. No rule, number, lifecycle transition, or direct consumer was added.
- **Direct consumers:** `Spawn_Logic`, `Lifecycle_Roster`, and the First Reception interface record were rechecked; `Pledge_Contracts`, `Reputation_Rules`, and `Quest_Engine` remain linked mechanics rather than new owners.
- **Approval and validation:** approved conflict-free migration; snapshots in `C:\Temp\eldrain-first-reception-continuity-migration-20260811`, exact diff, interface-boundary review, `validate_rewrite.py` with intentional migration exceptions recorded, and project validators.

## Candidate triage and Pass B source inventory

All scanner candidates are accounted for below. A scanner marker is not a finding
on its own. `DUPLICATE_SENTENCE` candidates remain `KEEP — structured repetition`
where they are repeated record fields, registry rows, or atomic equipment entries.
`FORMULAIC_PROSE` candidates remain `KEEP — intentional voice` where the contrast
is the shortest carrier of a concrete rule, player consequence, factual boundary,
or approved lore voice.

### REWRITE — supported finding

- `05_Combat_Survival/Traversal_Core.md:18` — 1 `FORMULAIC_PROSE` candidate; batch A-05-01 above.

### KEEP — intentional voice or concrete claim (28 candidates)

- `02_World_Lore/Lizard_Culture.md:65,185,269,273,329,337` — 6 `FORMULAIC_PROSE`; all are concrete cultural practices, spatial signals, or intentional lore framing. The separate A-02-01 opening repair does not alter these later supported KEEP dispositions.
- `02_World_Lore/Magipunk_Physics.md:67` — 1 `FORMULAIC_PROSE`; compact statement of the practice-versus-understanding premise.
- `02_World_Lore/Protocol_Resonance.md:86` — 1 `FORMULAIC_PROSE`; defines stored context beyond speech.
- `02_World_Lore/Rat_Culture.md:137,177` — 2 `FORMULAIC_PROSE`; carries lineage and production-provenance constraints.
- `02_World_Lore/Squirrel_Culture.md:41,43,65,177` — 4 `FORMULAIC_PROSE`; carries storage-state, succession, and food-timing rules.
- `02_World_Lore/The_Ark.md:127` — 1 `FORMULAIC_PROSE`; defines the time as well as spatial failure condition.
- `02_World_Lore/The_Entity.md:116` — 1 `FORMULAIC_PROSE`; carries a late metaprogression reveal in approved lore voice.
- `02_World_Lore/Toad_Culture.md:531` — 1 `FORMULAIC_PROSE`; preserves a concrete faction-ideology claim. Line 34 is the supported A-02-03 duplicate-rule repair.
- `03_Factions_Societies/Lore/City_District_Social_Grammar.md:31` — 1 `FORMULAIC_PROSE`; its following list makes the district test concrete.
- `03_Factions_Societies/Lore/The_Keepers.md:177` — 1 `FORMULAIC_PROSE`; intentional reveal voice and causal claim.
- `03_Factions_Societies/Quest_Engine_Grammar.md:230` — 1 `FORMULAIC_PROSE`; specifies archive outcome fields.
- `04_Player_Entities/Shell_Foundlings.md:42` — 1 `FORMULAIC_PROSE`; specifies both origin place and catastrophe-relative epoch.
- `05_Combat_Survival/Weapon_Manifesto.md:102` — 1 `FORMULAIC_PROSE`; specifies information, AI, anomaly, and player response to loud fire.
- `06_Economy_Loot/Currency_Rez.md:24` — 1 `FORMULAIC_PROSE`; intentional lore-to-economy identity statement.

Every `02_World_Lore` source above is `Pass A only`; no World Lore source enters
Pass B through this manifest.

### REWRITE COMPLETE — structural Pass A review

- `01_Core_Vision/Art_Direction_Material_Grammar.md:115` — A-01-01 removed a repeated feedback contrast while retaining the material signal and the Thermos link.
- `03_Factions_Societies/Reputation_Rules.md:55` — A-03-01 now states the city-balance consequence directly; faction meaning and runtime ownership remain unchanged.
- `05_Combat_Survival/Combat_Three_Debts.md:55` — A-05-02 now opens with the counterplay trace rather than the HP/status contrast.
- `05_Combat_Survival/Traversal_Core.md:18` — A-05-01 is the completed direct tactical premise repair.
- `08_World_Generation/Hub/04_Time_Atmosphere.md:31` — A-08-01 now names the projected weather bundle directly and retains `Dynamic Weather` as owner.
- `02_World_Lore/Lizard_Culture.md:31` — A-02-01 retains the false-sea causal inheritance while removing the duplicate cluster rule and adjective scaffold.
- `02_World_Lore/Squirrel_Culture.md:29` — A-02-02 retains route, store, and delay awareness without repeating the cluster rule.
- `02_World_Lore/Toad_Culture.md:34` — A-02-03 retains attention to formative conditions; the earlier intentional-voice verdict was corrected.

The full 126-owner Pass A review used the scanner as a seed and separately
checked opening claims, meta-announcements, repeated conclusions, fragmented
scaffolding, contrast formulas, and duplicated normative summaries against each
owner's register and direct dependencies. The remaining five formulaic scanner
hits are `KEEP`: `02_World_Lore/Protocol_Resonance.md:86`,
`02_World_Lore/Magipunk_Physics.md:67`,
`04_Player_Entities/Shell_Foundlings.md:42`,
`03_Factions_Societies/Lore/City_District_Social_Grammar.md:31`, and
`06_Economy_Loot/Currency_Rez.md:24`. In each case the syntax carries a
non-duplicated canon rule, chronology, lore voice, entity criterion, or
economic identity; no safe structural deletion was found. Registry repetition
remains schema evidence, not AI-shaped prose. `02_World_Lore` received this
register review only and was not redistributed.
+
### Pass A per-owner structural audit inventory

The following inventory is the evidence for the completed structural review. Each
row identifies the owner, its actual opening and first section, the register,
and an owner-specific verdict. The scanner was a seed; a `KEEP` does not grant
blanket approval.

- [owner_path:: 01_Core_Vision/01_Vision.md] [register:: CORE_CONCEPT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Видение Проекта (Vision & Atmosphere)` -> `## 1. Атмосфера: "Уютная Безысходность"`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 01_Core_Vision/02_Core_Loop.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Игровой Цикл (The Core Loop)` -> `## Первый playable vertical slice`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 01_Core_Vision/Art_Direction_Material_Grammar.md] [register:: CORE_CONCEPT] [pass_a_verdict:: REWRITE_COMPLETE] [evidence:: inspected `# Материальная грамматика Элдрейна` -> `## Обещание арт-дирекшена`; A-01-01 direct feedback repair]
- [owner_path:: 02_World_Lore/Anomaly_Weather_Systems.md] [register:: LORE] [pass_a_verdict:: KEEP] [evidence:: inspected `# Небесная Твердь: Погода и Светила` -> `## 1. Записанные небеса`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 02_World_Lore/Culture_Language.md] [register:: LORE] [pass_a_verdict:: KEEP] [evidence:: inspected `# Культура Элдрейна: Мозаика Миров` -> `## 1. Портовая речь и резонансное обучение`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 02_World_Lore/Magipunk_Physics.md] [register:: LORE] [pass_a_verdict:: KEEP] [evidence:: inspected `# Технологии: Наследие Света` -> `## 1. Эстетика: Корневой магипанк`; scanner line 67 carries the practice-versus-understanding premise]
- [owner_path:: 02_World_Lore/Protocol_Resonance.md] [register:: LORE] [pass_a_verdict:: KEEP] [evidence:: inspected `# Протокол «Резонанс»: Интеграция Видов` -> `## Промежуток Безмолвия`; scanner line 86 carries the non-duplicated stored-context rule]
- [owner_path:: 02_World_Lore/The_Anchor.md] [register:: LORE] [pass_a_verdict:: KEEP] [evidence:: inspected `# Якорный Архив (The Anchor Archive)` -> `## 1. Концепция: Сердце повреждённого Ковчега`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 02_World_Lore/The_Collapse.md] [register:: LORE] [pass_a_verdict:: KEEP] [evidence:: inspected `# Гибель Реальности: Синтез Времени` -> `## 1. Преждевременный запуск Ковчега`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 02_World_Lore/The_Entropy.md] [register:: LORE] [pass_a_verdict:: KEEP] [evidence:: inspected `# Энтропия: Дыхание Пустоты` -> `## 1. Природа: Великое Забвение (The Fading)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр игровых интерфейсов фракций` -> `## Гранулярность`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 03_Factions_Societies/_Registries/Registry_Factions.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: городские Очаги и фракционные адреса` -> `## Игровая модель`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 03_Factions_Societies/Lore/City_District_Social_Grammar.md] [register:: LORE_FRAMEWORK] [pass_a_verdict:: KEEP] [evidence:: inspected `# Социальная грамматика районов Элдрейна` -> `## Район как зависимость`; scanner line 31 introduces the concrete district-test list]
- [owner_path:: 03_Factions_Societies/Lore/Civic_Order.md] [register:: LORE_FRAMEWORK] [pass_a_verdict:: KEEP] [evidence:: inspected `# Гражданский порядок Элдрейна` -> `## Основной закон`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 03_Factions_Societies/Lore/Hearth_Anatomy.md] [register:: LORE_FRAMEWORK] [pass_a_verdict:: KEEP] [evidence:: inspected `# Анатомия Очага` -> `## Что такое Очаг`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 03_Factions_Societies/Pledge_Contracts.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Поручения, адрес вклада и допуски` -> `## 1. Поручение`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 03_Factions_Societies/Reputation_Rules.md] [register:: MECHANIC] [pass_a_verdict:: REWRITE_COMPLETE] [evidence:: inspected `# Правила доверия и репутации` -> `## 1. Три типа действий`; A-03-01 direct consequence repair]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Combos.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: ячейки Race × Spec` -> `## Зафиксированная матрица`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Interaction_Families.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: семейства взаимодействий` -> `## 1. Закрытая грамматика`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Parameter_Contracts.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр параметрических контрактов` -> `## Контракт записи`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Races.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: Расы` -> `## Статическая навигация`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Skill_Types.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: грамматика и границы навыков` -> `## 1. Общий контракт и условные продолжения`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Specs.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: Практики / специализации` -> `## Статическая навигация`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/_Registries/Registry_Tags.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр личных тегов` -> `## Правила реестра`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/Body_Morphology_Contract.md] [register:: SYSTEM] [pass_a_verdict:: KEEP] [evidence:: inspected `# Контракт морфологии тела` -> `## 1. Владелец`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/Proficiency_Arsenal.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Адаптивный арсенал и профильные ёмкости` -> `## 1. Именованный арсенал hero-kit`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/Shell_Foundlings.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Найдёныши: спасение, custody и Origin` -> `## 1. Обещание`; scanner line 42 carries origin place and catastrophe-relative chronology]
- [owner_path:: 04_Player_Entities/Skill_Build_Philosophy.md] [register:: SYSTEM] [pass_a_verdict:: KEEP] [evidence:: inspected `# Философия навыков и билдостроения` -> `## 1. Один контракт для P, Q и E`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/Spawn_Logic.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Логика Спавна и Снаряжения Оболочек` -> `## 1. Выжившая Пешка (Survivor State)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/Tags_System.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Личные теги: свойства прожитой Пешки` -> `## 1. Что считается тегом`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 04_Player_Entities/Trait_Development.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Chronicle: память, а не дерево перков` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/_Registries/Registry_StatusEffects.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: Статусные Эффекты` -> `## Контракт Записи`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/_Registries/Registry_Weapons.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр оружейных фреймов` -> `## Контракт доступа`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Acoustic_Stealth.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Механика: Акустический Шум` -> `## 1. Назначение`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Ballistics_Armor.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Система: Баллистика и Броня` -> `## 1. PvE: Покров и Способ Вскрытия`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Ballistics_PvE.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Баллистика PvE: Покров и Рабочий Цикл` -> `## 1. Покров Не Является Gear Check`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Combat_Consumables.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Медицина, здоровье и необходимые расходники` -> `## 1. Граница расходников и навыков`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Combat_Three_Debts.md] [register:: MECHANIC] [pass_a_verdict:: REWRITE_COMPLETE] [evidence:: inspected `# Боевое ядро: Закон трёх долгов` -> `## 1. Обещание боя`; A-05-02 direct trace repair]
- [owner_path:: 05_Combat_Survival/Communication_Vox.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Акустический Протокол и VOIP` -> `## 1.  Канал Связи`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Dissonance_System.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Механика: Диссонанс (Dissonance)` -> `## 1. Концепция`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Field_Crafting.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Полевые Операции с Лутом` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Hunt_Frontier_Loop.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Охота на фронтире Аномалии` -> `## 1. Обещание фронтира`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Magic_Batteries.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Система: Магия и Батареи` -> `## 1. Канон батарей`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Masks_Filters.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Маски: Ключ от Мира` -> `## 1. Концепция (Mask Gating)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Movement_Physics.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Механика: Физика Движения` -> `## 0. Цель Ощущения`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Status_Effects.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Механика: Статусные Эффекты` -> `## 1. Назначение`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Threat_Thresholds.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Механика: Пороги Давления Аномалии (Dissonance Thresholds)` -> `## 1. Расчет Давления`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Traversal_Core.md] [register:: MECHANIC] [pass_a_verdict:: REWRITE_COMPLETE] [evidence:: inspected `# Система Перемещения: Вертикальность и Укрытия` -> `## 1. Тактическая География`; A-05-01 direct tactical premise repair]
- [owner_path:: 05_Combat_Survival/Weapon_Core.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Оружие: Магострельный Канон и Тиры` -> `## 1. Главный принцип`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Weapon_Melee.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Оружие: ближний бой` -> `## Цикл`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 05_Combat_Survival/Weapon_Ranged.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Оружие: дальний бой` -> `## Батарея не магазин`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Barter_System.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Адресный Бартер` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Blueprints.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Ограниченные Чертежи` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Craft_Modifiers.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Вариантный Ингредиент` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Currency_Rez.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Валюта: Рез (Rez)` -> `## 1. Природа Валюты`; scanner line 24 carries the lore-to-economy identity claim]
- [owner_path:: 06_Economy_Loot/Economy_Core.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Экономика: От Риска к Адресу` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Extraction_Stabilization_Loop.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Экстракция, стабилизация и наследие сектора` -> `## 1. Главная ставка`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Loot_Distribution.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Распределение Лута` -> `## 1. Пять осей размещения`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Loot_Sync_Cycle.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Происхождение Лута и Цикл Синхронизации` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/P2P_Interaction.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Физическая Передача Между Игроками` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Resource_Cycle.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Цикл Ресурсов: Состав и Адрес` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Return_Manifest_Contract.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Return Manifest Contract` -> `## Responsibility`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Sinks_Insurance.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Расходы и Вывод Валюты (Money Sinks)` -> `## 1. Стабилизация Добычи (Loot Stabilization)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 06_Economy_Loot/Vendor_Logic.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Адреса, Поставщики и Мастера` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Blueprints.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: LimitedBlueprint` -> `## 1. Ответственность и обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Consumables.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: необходимые расходники и экспедиционные предметы` -> `## 1. Контракт записи`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_CraftingRecipes.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: Адресные RecipeTransaction` -> `## 1. Ответственность и обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Headwear.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: Маски и Шлемы (Protective Gear)` -> `## (T1) Повязка Первопроходца (Pioneer Scarf)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Items.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: Предметы и Ресурсы (General Items)` -> `## 1. Ресурсы Крафта (Crafting Materials)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр интерфейсов Термоса` -> `## Invariants`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр модулей Термоса` -> `## Контракт`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/_Registries/Registry_Thermoses.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр моделей Термоса` -> `## Контракт модели`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Affix_Grammar.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Грамматика Аффиксов` -> `## 1. Принцип`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Containers_Slots.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Механика: Контейнеры и Слоты (Containers Hierarchy)` -> `## 1. Иерархия Хранилищ`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Dissonance_Value.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Механика: Диссонанс Предмета (Dissonance Value)` -> `## 1. Концепция`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Equipment_PaperDoll.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Кукла Персонажа (Equipment Slots)` -> `## 1. Философия: Tactical Goblincore`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Fashion_Gear.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Визуальный язык Термоса` -> `## 1. Четыре читаемых слоя`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Gear_Progression.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Прогрессия Снаряжения` -> `## 1. Обещание Прогрессии`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Inventory_Architecture.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Механика: Архитектура Инвентаря (Mass & Access)` -> `## 1. Базовый Принцип`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Inventory_QoL.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Система: Удобство и Сортировка (QoL)` -> `## 1. Контекстная Иерархия Сортировки`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Item_Attributes_UI.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Атрибуты Предмета и UI (Item Passport)` -> `## 1. Всплывающая Подсказка (Tooltip)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Looting_Process.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Процесс Обыска (Interaction Loop)` -> `## 1. Тайминги и Риск`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Physical_Weight.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Механика: Физический Вес (Physical Weight)` -> `## 1. Разделение понятий`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Stash_Architecture.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Архитектура Схрона и Менеджмент (Stash & Organization)` -> `## 1. Концепция: Общий Склад (Account-Wide)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Thermos_Assembly.md] [register:: SYSTEM] [pass_a_verdict:: KEEP] [evidence:: inspected `# Сборка Термоса` -> `## 1. Runtime entities`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 07_Gear_Inventory/Thermos_System.md] [register:: SYSTEM] [pass_a_verdict:: KEEP] [evidence:: inspected `# Термос: носимая система экипировки` -> `## 1. Четыре слоя сущностей`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/_Registries/Registry_Anomaly_Mutations.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: линии мутаций Аномалий` -> `## Чужая вода`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/_Registries/Registry_Biomes.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: Биомы и Уровни Угрозы (Biomes Registry)` -> `## Ржавый Порт (Rusty Port)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/_Registries/Registry_Environment_States.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: локальные средовые состояния` -> `## Как игрок читает среду`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/_Registries/Registry_Mobs.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: Глобальный бестиарий` -> `## Авторский контракт физиологии и действий`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/_Registries/Registry_POIs.md] [register:: REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Реестр: Объекты Карты (Map Table Objects)` -> `## Контракт адресного POI`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/_Registries/Registry_Raid_Interfaces.md] [register:: INTERFACE_REGISTRY] [pass_a_verdict:: KEEP] [evidence:: inspected `# Registry: Raid Interfaces` -> `## Owner-ID convention`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Anomaly/00_Anomaly_Core_Loop.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Ядро Аномалии: Правила Арены` -> `## 1. Мета-Правила Сессии`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Anomaly/05_Hazards_Traps.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Опасности Среды` -> `## 1. Аномальные Ловушки`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Anomaly/13_Insertion_Logic.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Insertion Logic` -> `## Responsibility`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Anomaly/14_Extraction_System.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Нестабильные Пороги: обычный выход` -> `## Responsibility`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Система линий мутаций Аномалии` -> `## Ответственность`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Anomaly/17_Apex_Last_Hour.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Apex Last Hour` -> `## Responsibility`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Anomaly/Anomaly_System.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Система: Аномалии (The Anomaly Engine)` -> `## 0. Что такое Аномалия`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/City_State/Civic_Event_Lifecycle.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# CityState и жизненный цикл городских явлений` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/02_Mechanic_Night_Benches.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Ночные Верстаки` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/03_Dynamic_Weather.md] [register:: SYSTEM] [pass_a_verdict:: KEEP] [evidence:: inspected `# Динамическая Погода` -> `## 1. Источник Погоды`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/04_Global_Map_Rotation.md] [register:: SYSTEM] [pass_a_verdict:: KEEP] [evidence:: inspected `# Ротация Активных и Stable-Секторов` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/05_Difficulty_Slots.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Слоты Сложности (Tier Spread)` -> `## 1. Правило "Трех Аномалий"`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/06_Async_Timers.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Асинхронные таймеры и regional service` -> `## 1. Ответственность`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/07_Server_Lifecycle.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Жизненный цикл сервера` -> `## 1. Единственный владелец времени и барьеров`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/08_Gate_Check.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Гейт-проверка` -> `## Responsibility`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/09_Loot_Respawn.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Логика Респавна Лута` -> `## 1. Глобальный Реролл (Global Shift)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/10_World_Topology.md] [register:: SYSTEM] [pass_a_verdict:: KEEP] [evidence:: inspected `# Топология Мира: Паттерн "Цветок"` -> `## 1. Иерархия Генерации`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/11_Socket_System.md] [register:: TECH_SPEC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Система Сокетов (Socket System)` -> `## 1. Структура Данных`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/12_Generation_Strategies.md] [register:: TECH_SPEC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Стратегии Генерации Города` -> `## 1. Гибридный Подход (Skeleton & Meat)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/13_Async_Double_Buffer.md] [register:: ARCHITECTURE] [pass_a_verdict:: KEEP] [evidence:: inspected `# Асинхронная Архитектура Мира` -> `## 1. Двойная Буферизация (World A / World B)`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/14_Sector_Content_Rules.md] [register:: DESIGN_RULE] [pass_a_verdict:: KEEP] [evidence:: inspected `# Правила Наполнения Сектора` -> `## 0. Обязательный манифест`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/15_Traversal_Shortcuts.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Слой Связности (Connectivity Layer)` -> `## 1. Цель Системы`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/16_UI_Map_Protocol.md] [register:: TECH_SPEC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Протокол Данных Мини-карты` -> `## 1. Проблема Динамики`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/19_Raid_Approach_and_Entry.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Raid Approach and Entry` -> `## Responsibility`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/20_Egress_Solvency.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Egress Solvency` -> `## Responsibility`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Generation/21_Location_Revision_Lifecycle.md] [register:: SYSTEM_CONTRACT] [pass_a_verdict:: KEEP] [evidence:: inspected `# Жизненный цикл ревизии локации` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Hub/00_Hub_Environment.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Хаб: Операционный Бункер` -> `## 1. Концепция Роли`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Hub/01_Hub_Map_Table.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Живая Миниатюра: Карта Рейдов и Адресов` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Hub/02_Hub_Services_Interaction.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Сервисы Хаба: Работа Через Диораму` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Hub/03_Hub_Map_Interaction.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Интерактивный Стол: Мирная Проекция` -> `## 1. Обещание`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Hub/04_Time_Atmosphere.md] [register:: MECHANIC] [pass_a_verdict:: REWRITE_COMPLETE] [evidence:: inspected `# Время и Атмосфера` -> `## 1. Хаб: "Уют вне Времени"`; A-08-01 direct presentation repair]
- [owner_path:: 08_World_Generation/Hub/05_Party_Syndicate.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Система Группы: Протокол "Стол"` -> `## 1. Концепция: Совместная Операция`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Persistence_Ledger.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Гроссбух: Архитектура Сохранений` -> `## 1. Модель "Check-in / Check-out"`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]
- [owner_path:: 08_World_Generation/Reality_Integrity.md] [register:: MECHANIC] [pass_a_verdict:: KEEP] [evidence:: inspected `# Целостность Реальности (Security & Validation)` -> `## 1. Серверный Авторитаризм`; no supported duplicate rule, meta-announcement, fragmented scaffold, or generic contrast after owner-scoped structural review]


### KEEP — structured repetition (221 candidates)

- `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md:106,124,125,138,153,168,183,198,213,228` — 10 `DUPLICATE_SENTENCE` candidates. Repeated interface fields are atomic records, not duplicated normative prose.
- `04_Player_Entities/_Registries/Registry_Combos.md:259` — 1 `DUPLICATE_SENTENCE` candidate; a structured combo record.
- `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md:61,62,63,74,86,87,102,114` — 8 `DUPLICATE_SENTENCE` candidates. Contract-field repetition is required for independent lookup.
- `05_Combat_Survival/_Registries/Registry_StatusEffects.md:92,112,139,163,187,215,234,237,239,283,285,289,310` — 13 `DUPLICATE_SENTENCE` candidates. Status-effect record fields are intentionally parallel.
- `05_Combat_Survival/Weapons/Condenser_Rig_2H.md:66`; `05_Combat_Survival/Weapons/Needle_Thrower_2H.md:64`; `05_Combat_Survival/Weapons/Pulse_Tool_1H.md:67`; `05_Combat_Survival/Weapons/Scatter_Valve_2H.md:66,67` — 5 `DUPLICATE_SENTENCE` candidates. These are atomic equipment profile fields and remain read-only.
- `07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md:76,79,83,86,89,90,92,98,101,105,108,111,112,113,114,120,123,127,130,133,134,135,136,142,145,149,152,156,157,158,164,167,171,174,177,178,179,180,186,189,193,196,199,200,201,202,208,211,215,221,222,223,224,230,233,237,240,243,244,245,246,252,255,259,262,265,266,267,268,274,277,281,284,287,288,289,290,296,299,303,306,309,310,311,312,318,321,325,327,328,331,332,333,334,340,343,347,350,353,354,355,356,362,365,369,372,375,376,377,378,384,387,391,392,394,397,398,399,400,406,409,413,416,419,420,421,422,428,431,435,438,441,442,443,444` — 135 `DUPLICATE_SENTENCE` candidates. The regular module record schema is intentional and must not be prose-normalized.
- `07_Gear_Inventory/_Registries/Registry_Thermoses.md:52,53,55` — 3 `DUPLICATE_SENTENCE` candidates; thermos record fields remain atomic.
- `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md:56,68,100,114,116,118,149,162` — 8 `DUPLICATE_SENTENCE` candidates. Mutation record fields remain parallel.
- `08_World_Generation/_Registries/Registry_Biomes.md:67,81,92,105` — 4 `DUPLICATE_SENTENCE` candidates. Biome records remain parallel.
- `08_World_Generation/_Registries/Registry_Environment_States.md:119` — 1 `DUPLICATE_SENTENCE` candidate; an environment-state record field.
- `08_World_Generation/_Registries/Registry_Mobs.md:294,298,304,311,315,332,345,349,355,362,366,372,383,396,400,406,413,417,423,435,437,446,449,450,451,460,463,464,465,474,477,478,479` — 33 `DUPLICATE_SENTENCE` candidates. Repeated mob profile fields are required for tactical comparison.

## Pass B handoff inventory

Task 7 reviews responsibility only after each closed Pass A batch. The 25
non-lore scanner-source paths under `03_` through `08_` are the seed set for
detailed triage, not the complete Pass B scope. The full execution queue is the
116-route-owner coverage inventory in
`docs/audits/2026-08-11-responsibility-migration-map.md`; every owner there must
reach an evidence-backed `DETAILED` decision in the same Pass B execution. The
scanner evidence remains represented by the single A-05-01 owner, the non-lore
`KEEP — intentional voice` entries above, and all `KEEP — structured repetition`
registry and atomic-profile entries above.

Task 7 must not reopen any `02_World_Lore` source, generated `00_Routes.md` page,
or `00_Index.md`. It also must not edit a registry merely because the scanner
matched its deliberately repeated schema; registry review is still required for
responsibility and boundary evidence.

Pass B may report an authority concern only with owner-scoped evidence. It does
not convert a `KEEP` disposition into an edit authorization; a newly supported
finding creates a new bounded Pass A batch only after curator evidence and
protected-invariant scope are recorded here. Pass B is closed in the
responsibility map with 116 `DETAILED` owner coverage records; it does not close
the corpus-wide Pass A structural review.

## Batch limits check

- Each recorded batch contains one normal owner, no editable dependency, and one declared register.
- Each editable surface is bounded to one owner and the complete evidence-defined paragraph or section; it is not constrained to one line or a minimal diff.
- No batch crosses a domain boundary, and no culture page is admitted to a mixed batch.
- No table cell contains a link, raw path list, line break, or literal pipe.
