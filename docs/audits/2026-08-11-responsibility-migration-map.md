# Pass B responsibility migration map — 2026-08-11

## Scope and verdict

**FRAGILE — audit-only.** This map reviews only the 25 non-lore scanner-source
paths named by the canonical prose-refactor manifest after Pass A batch A-05-01
closed at `3b878bb719a4dc4174b68749d53b66a8ab5935da`. It is not an edit batch and
does not change a `KEEP` scanner disposition into edit authorization.

The architecture contract requires one mechanic owner for each player-facing
interaction and a separate shared-system owner only where a value or lifecycle
is actually universal. The registry and entity records below already preserve
that boundary in most cases. Three owner gaps are explicitly recorded by the
active corpus; no target is invented for them.

Excluded: `02_World_Lore`, all generated route pages, `00_Index.md`, and every
scanner source outside the manifest inventory.

## Evidence classes

- **AUTHOR CONSTRAINT:** `01_Core_Vision/01_Vision.md` requires observable
  condition, cost, and failure trace for magic; `01_Core_Vision/02_Core_Loop.md`
  assigns each loop step to its detailed owner rather than the loop overview.
- **GDD FACT:** `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`
  states that an interface record links a faction to one interaction and that
  its `mechanic_owner_ref` resolves eligibility, cost, state, reward, and
  failure. `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`
  assigns policy to one domain owner and labels absent owners `MISSING_OWNER`.
- **GDD FACT:** `07_Gear_Inventory/Thermos_System.md` separates definitions,
  assembly instances, and the Assembly Resolver; its current models and modules
  remain blocked until topology, contracts, ownership links, and calibration
  exist.
- **STRUCTURAL INFERENCE:** a repeated atomic registry field is not duplicated
  normative prose when its record contract makes the field independently
  queryable and declares the resolver elsewhere.
- **EMPIRICAL UNKNOWN / CONTENT GAP:** numeric status values, encounter tuning,
  Thermos topology, coverage, and calibration remain intentionally unresolved;
  none creates a second rule owner.

## Migration index

| Migration | Source | Current role | Decision | Status |
|---|---|---|---|---|
| M-01 | Faction active records | INTERFACE REGISTRY | Retain registry boundary | KEEP |
| M-02 | Faction planned records | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-03 | District grammar | LORE / ENTITY | Retain social grammar | KEEP |
| M-04 | Keepers late reveal | LORE / ENTITY | Retain entity narrative | KEEP |
| M-05 | Quest archive grammar | MECHANIC | Retain quest owner | KEEP |
| M-06 | Reputation consequence | MECHANIC | Retain reputation owner | KEEP |
| M-07 | Race × Spec record | CONTENT INSTANCE | Retain atomic combo record | KEEP |
| M-08 | Active parameter contracts | INTERFACE REGISTRY | Retain contract registry | KEEP |
| M-09 | Status policy contract | SYSTEM | Await canonical resolver | MISSING_OWNER |
| M-10 | Foundling history | LORE / ENTITY | No lore owner proven | MISSING_OWNER |
| M-11 | Status effect records | CONTENT INSTANCE | Retain atomic effect records | KEEP |
| M-12 | Status universal policy | SYSTEM | Await canonical resolver | MISSING_OWNER |
| M-13 | Three Debts trace | MECHANIC | Retain combat owner | KEEP |
| M-14 | Traversal geography | MECHANIC | Retain traversal owner | KEEP |
| M-15 | Weapon-frame guidance | PRESENTATION | Retain design guide | KEEP |
| M-16 | Condenser frame records | CONTENT INSTANCE | Retain frame records | KEEP |
| M-17 | Needle frame records | CONTENT INSTANCE | Retain frame records | KEEP |
| M-18 | Pulse frame records | CONTENT INSTANCE | Retain frame records | KEEP |
| M-19 | Scatter frame records | CONTENT INSTANCE | Retain frame records | KEEP |
| M-20 | Rez nature and wallet | MECHANIC | Retain currency owner | KEEP |
| M-21 | Thermos module records | CONTENT INSTANCE | Block pending domain owners | MISSING_OWNER |
| M-22 | Thermos model records | CONTENT INSTANCE | Retain blocked topology | KEEP |
| M-23 | Mutation-line records | CONTENT INSTANCE | Retain line records | KEEP |
| M-24 | Biome-tier records | CONTENT INSTANCE | Retain biome records | KEEP |
| M-25 | Environment-state records | CONTENT INSTANCE | Retain scene records | KEEP |
| M-26 | Mob and variant records | CONTENT INSTANCE | Retain physiology records | KEEP |
| M-27 | Hub weather presentation | PRESENTATION | Retain downstream link | KEEP |

## Entry evidence and boundaries

### M-01 — faction active records

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `## Active interfaces`, lines 80–108; scanner lines 106.
- Target owner: this registry remains the normalized participation-record owner.
- Entity role: First Reception is `PROVIDER` or `PRESENTER`; its presentation page supplies diegetic context only.
- Mechanic owner: `04_Player_Entities/Spawn_Logic.md` and `04_Player_Entities/Tags_System.md` for the two active records.
- Universal system owner: none; the registry explicitly forbids it from becoming a resolver.
- Does not own: institution history, eligibility, cost, state, reward, or failure handling.
- Direct consumers: `04_Player_Entities/Lifecycle_Roster.md`, `04_Player_Entities/Trait_Development.md`, and `03_Factions_Societies/Lore/The_First_Reception.md`.
- Preserved meaning: one interaction, one role, one mechanic owner, non-empty negative boundary.
- Required skill or handoff: architecture lead, curator boundary check, and lorekeeper faction-interface check; no further handoff changes the evidence.
- Approval and validation: no migration. Validate active records keep one non-missing mechanic owner and a non-empty `does_not_own` field.

### M-02 — faction planned records

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `## Planned interfaces with unresolved owners`, lines 110–232; scanner lines 124, 125, 138, 153, 168, 183, 198, 213, and 228.
- Target owner: `MISSING_OWNER`; the sources name no canonical resolver for quarantine assessment, reserve release, evidence attestation, provenance adjudication, load order, ritual stress service, repeatability attestation, or temporary pause.
- Entity role: respectively `WITNESS` or `PROVIDER`, as each interface record declares.
- Mechanic owner: `MISSING_OWNER` in every planned record.
- Universal system owner: none proven; a common owner must not be assumed from the listed consumers.
- Does not own: the explicit exclusions in each record, including custody, price, global truth, route eligibility, status resolution, crafting result, guilt, and city-wide law.
- Direct consumers: Lifecycle Roster, Economy Core, Hub Map Table, Loot Sync Cycle, Status Effects, Registry Crafting Recipes, and Pledge Contracts.
- Preserved meaning: each institution may present, witness, or provide a bounded interaction without acquiring runtime authority.
- Required skill or handoff: lorekeeper confirms social authority is not runtime authority; architecture lead confirms a dependency is not an owner.
- Approval and validation: **APPROVAL_REQUIRED** before creating any resolver. A future bounded batch must name a state machine, source of truth, and one exact owner for each interface.

### M-03 — district grammar

- Source evidence: `03_Factions_Societies/Lore/City_District_Social_Grammar.md`, `## Район как зависимость`, line 31.
- Target owner: this lore framework.
- Entity role: district identity, social dependency, temporary authority, and civic memory.
- Mechanic owner: none claimed; location geometry and routes are expressly deferred to world-generation owners.
- Universal system owner: `08_World_Generation/City_State/Civic_Event_Lifecycle.md` only for shared CivicEvent outcomes.
- Does not own: geometry, POI, street generation, routes, or physical state.
- Direct consumers: its declared civic, district, anomaly, and event-lifecycle dependencies.
- Preserved meaning: the candidate supplies a concrete social test, not a location-generation rule.
- Required skill or handoff: lorekeeper evidence applied; no handoff because no runtime rule is asserted.
- Approval and validation: no migration; preserve the stated physical-location boundary.

### M-04 — Keepers late reveal

- Source evidence: `03_Factions_Societies/Lore/The_Keepers.md`, `## Позднее Прямое Общение`, line 177.
- Target owner: this faction entity page.
- Entity role: the Keepers observe and eventually present a narrative recognition of the Shard.
- Mechanic owner: none is asserted by the candidate paragraph.
- Universal system owner: none.
- Does not own: roster metaphysics, late-meta progression predicate, Tag assignment, contract lifecycle, reward, or access resolution.
- Direct consumers: the page’s declared Quest Engine and Pledge Contracts references are contextual consumers, not evidence of a transfer.
- Preserved meaning: the late reveal is causal lore with intentionally incomplete Keeper knowledge.
- Required skill or handoff: lorekeeper verdict `CANON` for entity/narrative placement; no additional handoff.
- Approval and validation: no migration; any implementation of the late condition requires a separately scoped mechanic-owner audit.

### M-05 — quest archive grammar

- Source evidence: `03_Factions_Societies/Quest_Engine_Grammar.md`, `## 7. Сохранение и журнал` and `### Гроссбух`, line 230.
- Target owner: this quest-mechanic page, with `03_Factions_Societies/Quest_Engine.md` as its direct mechanic dependency.
- Entity role: an issuer or address may supply a contract seed but owns no archive result.
- Mechanic owner: Quest Engine.
- Universal system owner: none.
- Does not own: faction identity, roster state, hub POI state, or server lifecycle.
- Direct consumers: Reputation Rules, Shell Foundlings, Trait Development, Lifecycle Roster, Hub Map Table, and Server Lifecycle.
- Preserved meaning: archive fields describe the player-visible contract outcome and remain queryable.
- Required skill or handoff: architecture and curator evidence; no specialist question remained.
- Approval and validation: no migration; retain the listed direct-owner links.

### M-06 — reputation consequence

- Source evidence: `03_Factions_Societies/Reputation_Rules.md`, `### Спорный контракт`, line 55.
- Target owner: this reputation mechanic.
- Entity role: a Hearth or faction supplies an address and in-world consequence.
- Mechanic owner: Reputation Rules.
- Universal system owner: none proven.
- Does not own: faction membership, generic vendor stock, contract lifecycle, or a city-wide hidden score.
- Direct consumers: Registry Factions, Faction Address System, Circle of Interposition, Vendor Logic, and Pledge Contracts.
- Preserved meaning: a contested contract carries a political consequence visible to the player.
- Required skill or handoff: lorekeeper confirms the faction framing does not grant resolver authority.
- Approval and validation: no migration; keep explicit feedback and negative membership boundary.

### M-07 — Race × Spec record

- Source evidence: `04_Player_Entities/_Registries/Registry_Combos.md`, `## Крыса × Ладчик`, line 259.
- Target owner: this combo registry.
- Entity role: a combo is an authored player-content coordinate, not a faction or runtime entity.
- Mechanic owner: Combat Profile Pipeline consumes the selected record.
- Universal system owner: none; the registry delegates P/Q/E contracts and module effects.
- Does not own: personal MasteryContribution, inherited unknown abilities, P/Q/E resolution, or module-effect policy.
- Direct consumers: MVP 3×3 Design Contract, Registry Races, Registry Specs, Combat Profile Pipeline, Proficiency Arsenal, and Thermos System.
- Preserved meaning: repeated profile fields are atomic content-instance records; pending cells remain pending.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration; do not normalize repeated fields into prose.

### M-08 — active parameter contracts

- Source evidence: `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`, `## Активные домены`, lines 44–128; scanner lines 61–63, 74, 102, and 114.
- Target owner: this parameter-contract registry.
- Entity role: sources submit modifier requests; none receives entity-level authority from the registry.
- Mechanic owner: the declared domain owners, including Weapon Ranged, Skill Build Philosophy, Dissonance System, Ballistics Armor, Physical Weight, and Magic Batteries.
- Universal system owner: each named `domain_owner` only inside its own parameter domain.
- Does not own: source values, unrelated domains, or a global rating.
- Direct consumers: Combat Profile Pipeline, Skill Build Philosophy, Magic Batteries, Dissonance System, Thermos Assembly, and Thermos Interfaces.
- Preserved meaning: the record maps authority to modify a result without duplicating the result’s values.
- Required skill or handoff: architecture lead and curator boundary check; no handoff.
- Approval and validation: no migration; retain one declared domain owner per active contract.

### M-09 — status application policy

- Source evidence: `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`, `### status_application_policy` and its warning, lines 80–93; scanner lines 86–87.
- Target owner: `MISSING_OWNER`.
- Entity role: none.
- Mechanic owner: `MISSING_OWNER`; the Status Effects registry stores effects but is explicitly not declared the universal runtime resolver.
- Universal system owner: `MISSING_OWNER` for application, repeat, and conflict policy.
- Does not own: status values for all effects, action results, or environmental instances.
- Direct consumers: Registry StatusEffects and any future declared delivery source.
- Preserved meaning: no local source may invent priority, floor, or cap while this resolver is absent.
- Required skill or handoff: architecture lead identifies an ownerless cross-system policy; curator confirms the registry must not silently become the owner.
- Approval and validation: **APPROVAL_REQUIRED**. A new bounded SYSTEM owner must establish application, repeat, conflict, cap, and failure policy before the pending contract can become active.

### M-10 — Foundling history

- Source evidence: `04_Player_Entities/Shell_Foundlings.md`, `## 2. Исторический срез`, line 42.
- Target owner: `MISSING_OWNER`; this Pass B scope excludes `02_World_Lore`, and the direct dependencies do not establish a separate lore owner for the catastrophe-relative history.
- Entity role: Foundling origin and historical context.
- Mechanic owner: Shell Foundlings resolves rescue, custody, extraction, reveal, and roster consequences, not the historical claim’s independent canon.
- Universal system owner: none.
- Does not own: a new lore chronology or a replacement lore authority.
- Direct consumers: Physical Weight, Trait Development, Lifecycle Roster, Extraction Stabilization Loop, Quest Engine, Quest Engine Grammar, and The First Reception.
- Preserved meaning: origin place and catastrophe-relative epoch stay factual; no rewrite or removal is authorized.
- Required skill or handoff: lorekeeper finds a boundary concern but no eligible owner in scope.
- Approval and validation: **APPROVAL_REQUIRED** for a future lore-owner selection; no migration in Pass B.

### M-11 — status effect records

- Source evidence: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`, effect-record headings from `### Кровотечение` through `### Насыщение восстановления`, scanner lines 92, 112, 139, 163, 187, 215, 234, 237, 239, 283, 285, 289, and 310.
- Target owner: this content registry.
- Entity role: none.
- Mechanic owner: `05_Combat_Survival/Status_Effects.md` supplies effect mechanics; the registry supplies atomic instances.
- Universal system owner: none claimed by an individual record.
- Does not own: local environment-state ownership, automatic reactions, or a universal application resolver.
- Direct consumers: Status Effects, Combat Three Debts, and Registry Environment States.
- Preserved meaning: repeat, telegraph, counter-action, and persistence fields are independently comparable content data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration; retain the global-versus-local boundary.

### M-12 — status universal policy

- Source evidence: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`, `## Контракт Записи` through `## Граница глобального статуса`, lines 19–65.
- Target owner: `MISSING_OWNER`.
- Entity role: none.
- Mechanic owner: the source points to `05_Combat_Survival/Status_Effects.md`, but the active Parameter Contracts page expressly says that page is not declared the universal runtime resolver for status application policy.
- Universal system owner: `MISSING_OWNER` for cross-effect application, repeat, conflict, and priority resolution.
- Does not own: environment-instance source, local scene consequence, or a second combat owner.
- Direct consumers: Registry StatusEffects, Registry Environment States, Dissonance System, and future delivery sources.
- Preserved meaning: the current budget and global/local boundary remain canon; values remain prototype-level empirical unknowns.
- Required skill or handoff: architecture lead identifies the bottleneck; curator distinguishes supported owner gap from scanner repetition.
- Approval and validation: **APPROVAL_REQUIRED** before moving or duplicating policy. The future owner must preserve the stated combat budget and environment boundary.

### M-13 — Three Debts trace

- Source evidence: `05_Combat_Survival/Combat_Three_Debts.md`, `## 2. Общий цикл действия`, line 55.
- Target owner: this combat mechanic.
- Entity role: none.
- Mechanic owner: Combat Three Debts.
- Universal system owner: none; subordinate systems retain their own debt implementation.
- Does not own: weapon values, movement physics, status resolution, Dissonance calculation, or ability synergy.
- Direct consumers: Weapon Core, Hunt Frontier Loop, Magic Batteries, Movement Physics, Acoustic Stealth, Status Effects, Dissonance System, and Ability Synergy.
- Preserved meaning: counterplay traces and the no-idle-punishment boundary remain the combat contract.
- Required skill or handoff: architecture evidence; no specialist evidence changes the ownership finding.
- Approval and validation: no migration.

### M-14 — Traversal geography

- Source evidence: `05_Combat_Survival/Traversal_Core.md`, `## 1. Тактическая География`, line 18.
- Target owner: this traversal mechanic.
- Entity role: none.
- Mechanic owner: Traversal Core.
- Universal system owner: none.
- Does not own: movement physics implementation or generated world topology.
- Direct consumers: Movement Physics and `08_World_Generation/Generation/10_World_Topology.md`.
- Preserved meaning: the closed Pass A direct opening and all three-echelon tactical trade-offs.
- Required skill or handoff: curator confirms A-05-01 is closed; no Pass B edit follows.
- Approval and validation: no migration; Pass A commit remains the only authorized change.

### M-15 — weapon-frame guidance

- Source evidence: `05_Combat_Survival/Weapon_Manifesto.md`, `## 5. Фазы столкновения`, line 102.
- Target owner: this design-manifest presentation layer.
- Entity role: a frame is a designed tool, not a player class.
- Mechanic owner: Weapon Core, Weapon Melee, and Weapon Ranged resolve runtime weapon rules.
- Universal system owner: Combat Three Debts supplies the shared cost grammar.
- Does not own: a frame record, weapon registry values, ballistic result, AI response resolver, or Anomaly behavior resolver.
- Direct consumers: Combat Three Debts, Weapon Core, Weapon Melee, Weapon Ranged, Combat Profile Pipeline, and the Port Manifest.
- Preserved meaning: loud fire has information consequences for anomaly, AI, and players without making the manifesto a runtime owner.
- Required skill or handoff: architecture and curator evidence; no further handoff.
- Approval and validation: no migration.

### M-16 — Condenser frame records

- Source evidence: `05_Combat_Survival/Weapons/Condenser_Rig_2H.md`, `## Экземпляры`, scanner line 66.
- Target owner: this weapon-frame content page.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts for common commitment debt.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers: the page’s declared Weapon Core, Weapon Ranged, registry, and profile dependencies.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-17 — Needle frame records

- Source evidence: `05_Combat_Survival/Weapons/Needle_Thrower_2H.md`, `## Экземпляры`, scanner line 64.
- Target owner: this weapon-frame content page.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers: the page’s declared Weapon Core, Weapon Ranged, registry, and profile dependencies.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-18 — Pulse frame records

- Source evidence: `05_Combat_Survival/Weapons/Pulse_Tool_1H.md`, `## Экземпляры`, scanner line 67.
- Target owner: this weapon-frame content page.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers: the page’s declared Weapon Core, Weapon Ranged, registry, and profile dependencies.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-19 — Scatter frame records

- Source evidence: `05_Combat_Survival/Weapons/Scatter_Valve_2H.md`, `## Экземпляры`, scanner lines 66–67.
- Target owner: this weapon-frame content page.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers: the page’s declared Weapon Core, Weapon Ranged, registry, and profile dependencies.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-20 — Rez nature and wallet

- Source evidence: `06_Economy_Loot/Currency_Rez.md`, `## 1. Природа Валюты`, line 24.
- Target owner: this currency mechanic.
- Entity role: Rez is a physical economic item, not an independent lore institution.
- Mechanic owner: Currency Rez.
- Universal system owner: Economy Core for economy-wide lifecycle only.
- Does not own: inventory slot capacity, Economy Core rules, battery behavior, or combat-damage resolution.
- Direct consumers: Containers Slots, Economy Core, and Magic Batteries.
- Preserved meaning: physical currency, aggregated UI, spending order, and the non-Rez combat-cost boundary.
- Required skill or handoff: architecture evidence; no specialist handoff.
- Approval and validation: no migration.

### M-21 — Thermos module records

- Source evidence: `07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md`, `## Candidate records`, scanner lines 76–444.
- Target owner: `MISSING_OWNER` for the listed effect domains; the registry remains the definition-record owner.
- Entity role: module definition is a content instance supplied to assembly.
- Mechanic owner: Thermos Assembly resolves an installed instance; declared ParameterContracts resolve runtime effects when they exist.
- Universal system owner: `MISSING_OWNER` for the module outputs listed as absent in Parameter Contracts.
- Does not own: selected pattern, occupied nodes, damage, stitched state, active body interface, or local effect-policy invention.
- Direct consumers: Thermos System, Thermos Assembly, Thermos Models, Thermos Interfaces, and Parameter Contracts.
- Preserved meaning: all records stay `blocked_calibration`; `concept_effects` remain nonauthoritative discovery fields and atomicity remains a review requirement.
- Required skill or handoff: architecture lead identifies the owner gap; curator confirms structured repetition is not itself duplication.
- Approval and validation: **APPROVAL_REQUIRED** for each parameter domain. Do not make a module installable until its exact owner, contract, topology, coverage, and calibration are present.

### M-22 — Thermos model records

- Source evidence: `07_Gear_Inventory/_Registries/Registry_Thermoses.md`, `### Городской серийный Термос` and `### Шаблон Термоса`, scanner lines 52, 53, and 55.
- Target owner: this Thermos-model registry.
- Entity role: model definition supplied to an assembly instance.
- Mechanic owner: Thermos Assembly resolves fitting and committed assembly state.
- Universal system owner: Thermos System owns shared definition-versus-instance boundary.
- Does not own: fit revision, selected pattern, occupied nodes, damage, stitched state, active effects, or derived slot count.
- Direct consumers: Thermos System, Thermos Assembly, Thermos Interfaces, and Equipment Paper Doll.
- Preserved meaning: `blocked_topology` is an explicit content gap, not missing authority or an invitation to infer topology.
- Required skill or handoff: architecture and curator evidence; no handoff.
- Approval and validation: no migration; preserve the block until topology, fit envelope, mass, and Paper Doll mapping exist.

### M-23 — mutation-line records

- Source evidence: `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`, active tier records, scanner lines 56, 68, 100, 114, 116, 118, 149, and 162.
- Target owner: this mutation-line registry.
- Entity role: anomaly-line and tier content instance.
- Mechanic owner: `08_World_Generation/Anomaly/Anomaly_System.md` resolves the overarching anomaly system.
- Universal system owner: none beyond the anomaly system’s shared lifecycle.
- Does not own: a global monster stat resolver, local scene state, or a second weather owner.
- Direct consumers: its declared anomaly-system and Port mutation-line dependencies.
- Preserved meaning: repeated tier fields express intentionally parallel authored content.
- Required skill or handoff: curator evidence; no handoff.
- Approval and validation: no migration.

### M-24 — biome-tier records

- Source evidence: `08_World_Generation/_Registries/Registry_Biomes.md`, Port tier records, scanner lines 67, 81, 92, and 105.
- Target owner: this biome registry.
- Entity role: biome and threat-tier content instance.
- Mechanic owner: world-generation owners consume biome tags and weather contracts.
- Universal system owner: none; numerical pressure is an empirical calibration issue.
- Does not own: loot table ownership, spawn resolver, a global mob rating, or a weather result resolver.
- Direct consumers: Registry Anomaly Mutations and the applicable map-generation consumers.
- Preserved meaning: `env_pressure`, `gate_pulse`, and filter-rating values remain explicitly prototype-level.
- Required skill or handoff: architecture evidence distinguishes content gap from authority finding.
- Approval and validation: no migration.

### M-25 — environment-state records

- Source evidence: `08_World_Generation/_Registries/Registry_Environment_States.md`, `### Метка глубины`, scanner line 119.
- Target owner: this environment-state registry.
- Entity role: a local scene-state instance with one local consequence.
- Mechanic owner: the specific `world_owner` and `recognition_owner` declared by each record.
- Universal system owner: none; a status aftermath is only a declared aftermath, never the scene’s owner.
- Does not own: a global status resolver, generic effect stack, or automatic reaction table.
- Direct consumers: Registry StatusEffects and the anomaly/dungeon owners named by records.
- Preserved meaning: telegraph, choice, refusal, termination, and local consequence remain inseparable scene data.
- Required skill or handoff: architecture and curator evidence; no handoff.
- Approval and validation: no migration; preserve one primary scene axis and consequence per instance.

### M-26 — mob and variant records

- Source evidence: `08_World_Generation/_Registries/Registry_Mobs.md`, mutation-line and Hungry Form records, scanner lines 294–479.
- Target owner: this mob registry.
- Entity role: mob or mutation-variant content instance.
- Mechanic owner: each local `physiology_contract` and `action_contract` resolves its body and actions.
- Universal system owner: none; encounter numbers stay local to the MobID.
- Does not own: player-stat conversion, universal RPG debuffs, hidden rating variants, or a second status owner.
- Direct consumers: Anomaly Mutation Lines, Port mutation-line content, and Registry Anomaly Mutations.
- Preserved meaning: repeated tactical fields are the readable projection of local contracts.
- Required skill or handoff: curator evidence; no handoff.
- Approval and validation: no migration; preserve explicit compatible status interfaces and player-readable counterplay.

### M-27 — Hub weather presentation

- Source evidence: `08_World_Generation/Hub/04_Time_Atmosphere.md`, `## 2. Рейд: Аномальная Погода`, line 31.
- Target owner: this atmosphere presentation page.
- Entity role: none.
- Mechanic owner: `08_World_Generation/Generation/03_Dynamic_Weather.md` owns the complete weather contract.
- Universal system owner: none.
- Does not own: physics, route, gear, enemy, trap, or exit resolution.
- Direct consumers: Dynamic Weather is the explicit downstream owner.
- Preserved meaning: weather is gameplay-relevant while this page only communicates the atmosphere and routing boundary.
- Required skill or handoff: architecture and curator evidence; no handoff.
- Approval and validation: no migration; retain the downstream contract link.

## Approval gate and follow-up

There are no `APPROVED_FOR_MIGRATION` rows. The map identifies four classes of
unapproved work: eight planned faction interfaces, status application policy,
Foundling historical ownership, and Thermos effect domains. Each remains
unaltered under `MISSING_OWNER` or `APPROVAL_REQUIRED`; none licenses a canonical
move, rewrite, registry change, route regeneration, or management-page change.

`python3 tools/vault_guard.py` reports the workflow `.superpowers` directory.
This is an environment follow-up only; no source workaround is appropriate.
