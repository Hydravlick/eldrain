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
| M-01a | First Reception admission | INTERFACE REGISTRY | Retain record boundary | KEEP |
| M-01b | First Reception return | INTERFACE REGISTRY | Retain record boundary | KEEP |
| M-01c | First Reception assessment | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01d | Storehouse reserve release | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01e | Contour attestation | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01f | Weighing provenance | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01g | Artel load order | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01h | Cathedral rite | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01i | Proving repeatability | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
| M-01j | Circle temporary pause | INTERFACE REGISTRY | No target may be inferred | MISSING_OWNER |
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
| M-25 | Environment-state records | CONTENT INSTANCE | Await exact dungeon resolver | MISSING_OWNER |
| M-26 | Mob and variant records | CONTENT INSTANCE | Retain physiology records | KEEP |
| M-27 | Hub weather presentation | PRESENTATION | Retain downstream link | KEEP |

## Entry evidence and boundaries

### M-01a — `first_reception.continuity_admission_presentation`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### first_reception.continuity_admission_presentation`, lines 80–93.
- Target owner: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` owns this normalized participation record.
- Entity role: First Reception is `PROVIDER`.
- Mechanic owner: `04_Player_Entities/Spawn_Logic.md`.
- Universal system owner: `04_Player_Entities/Lifecycle_Roster.md` owns shared roster lifecycle; it is a dependency, not this interaction's resolver.
- Does not own: PawnID creation, continuity epoch, readiness resolution, welfare eligibility, tag assignment, or lifecycle settlement.
- Direct consumers and linked pages: `04_Player_Entities/Spawn_Logic.md`, `04_Player_Entities/Lifecycle_Roster.md`, and `03_Factions_Societies/Lore/The_First_Reception.md`.
- Preserved meaning: a named living candidate and the roster admission predicate cross one bounded interface.
- Required skill or handoff: architecture lead, curator boundary check, and lorekeeper faction-interface check; no further handoff changes the evidence.
- Approval and validation: no migration. Validate one non-missing mechanic owner and this record's non-empty `does_not_own` boundary.

### M-01b — `first_reception.first_return_presentation`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### first_reception.first_return_presentation`, lines 95–108; scanner line 106.
- Target owner: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` owns this normalized participation record.
- Entity role: First Reception is `PRESENTER`.
- Mechanic owner: `04_Player_Entities/Tags_System.md`.
- Universal system owner: none; `04_Player_Entities/Trait_Development.md` is a dependency, not a universal resolver for the presentation.
- Does not own: First Return predicate, TagID assignment, Dawn settlement, tag-slot accounting, or combat resolution.
- Direct consumers and linked pages: `04_Player_Entities/Tags_System.md`, `04_Player_Entities/Trait_Development.md`, and `03_Factions_Societies/Lore/The_First_Reception.md`.
- Preserved meaning: an immutable revealed TagID and a readable result cross one bounded interface.
- Required skill or handoff: architecture lead, curator boundary check, and lorekeeper faction-interface check; no further handoff changes the evidence.
- Approval and validation: no migration. Validate one non-missing mechanic owner and this record's non-empty `does_not_own` boundary.

### M-01c — `first_reception.quarantine_assessment`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### first_reception.quarantine_assessment`, lines 114–127; scanner lines 124–125.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: First Reception is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `04_Player_Entities/Lifecycle_Roster.md` is a dependency and cannot be inferred as resolver.
- Does not own: personhood, custody, property, permanent access, city-wide quarantine, or treatment resolution.
- Direct consumers and linked pages: `04_Player_Entities/Lifecycle_Roster.md` and `03_Factions_Societies/Lore/The_First_Reception.md`.
- Preserved meaning: identity, observed signs, assessed risk, uncertainty, and expiry remain the minimum boundary.
- Required skill or handoff: lorekeeper confirms witness authority is not runtime authority; architecture lead confirms dependency is not ownership.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the assessment state machine and source of truth.

### M-01d — `common_storehouses.emergency_reserve_release`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### common_storehouses.emergency_reserve_release`, lines 129–142; scanner line 138.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Common Storehouses is `PROVIDER`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `06_Economy_Loot/Economy_Core.md` is a dependency and cannot be inferred as resolver.
- Does not own: item prices, Welfare predicate, vendor-stock generation, stash capacity, or debt settlement.
- Direct consumers and linked pages: `06_Economy_Loot/Economy_Core.md` and `03_Factions_Societies/Lore/The_Common_Storehouses.md`.
- Preserved meaning: branch, reserve, protected minimum, amount, reason, witnesses, and review time remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define release, refusal, review, and failure handling.

### M-01e — `contour_chamber.evidence_attestation`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### contour_chamber.evidence_attestation`, lines 144–157; scanner line 153.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Contour Chamber is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `08_World_Generation/Hub/01_Hub_Map_Table.md` is a dependency and cannot be inferred as resolver.
- Does not own: guilt, ownership, biological status, global truth, route eligibility, or fog-of-war resolution.
- Direct consumers and linked pages: `08_World_Generation/Hub/01_Hub_Map_Table.md` and `03_Factions_Societies/Lore/The_Contour_Chamber.md`.
- Preserved meaning: observation, place, time, method, witnesses, uncertainty, and version remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define attestation scope, versioning, and refusal.

### M-01f — `weighing_houses.provenance_adjudication`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### weighing_houses.provenance_adjudication`, lines 159–172; scanner line 168.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Weighing Houses is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `06_Economy_Loot/Loot_Sync_Cycle.md` is a dependency and cannot be inferred as resolver.
- Does not own: human guilt, universal property law, item value, barter result, debt collection, or physical transfer.
- Direct consumers and linked pages: `06_Economy_Loot/Loot_Sync_Cycle.md` and `03_Factions_Societies/Lore/The_Weighing_Houses.md`.
- Preserved meaning: object identity, transfer signatures, custody, conflicts, scope, and expiry remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the evidence and adjudication lifecycle.

### M-01g — `support_artels.infrastructure_load_order`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### support_artels.infrastructure_load_order`, lines 174–187; scanner line 183.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Support Artels is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `08_World_Generation/Hub/01_Hub_Map_Table.md` is a dependency and cannot be inferred as resolver.
- Does not own: district evacuation, player access, item durability, armor repair, route generation, or permanent ownership.
- Direct consumers and linked pages: `08_World_Generation/Hub/01_Hub_Map_Table.md` and `03_Factions_Societies/Lore/The_Support_Artels.md`.
- Preserved meaning: structure, observed load, local testimony, calculation holder, and review time remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define recommendation lifetime and release conditions.

### M-01h — `cathedral.ritual_stress_service`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### cathedral.ritual_stress_service`, lines 189–202; scanner line 198.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Cathedral of All Faiths is `PROVIDER`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `05_Combat_Survival/Status_Effects.md` is a dependency and cannot be inferred as resolver.
- Does not own: proof of gods, generic combat buff, status resolution, relic effects, contract reward, or raid alliance.
- Direct consumers and linked pages: `05_Combat_Survival/Status_Effects.md` and `03_Factions_Societies/Lore/The_Cathedral.md`.
- Preserved meaning: participant consent, rite, state, duration, failure, and exit remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the stress-state transition, refusal, and failure.

### M-01i — `proving_houses.repeatability_attestation`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### proving_houses.repeatability_attestation`, lines 204–217; scanner line 213.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Proving Houses is `WITNESS`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `07_Gear_Inventory/_Registries/Registry_CraftingRecipes.md` is a dependency and cannot be inferred as resolver.
- Does not own: all research, education, item identification, recipe unlock, crafting result, or universal sales ban.
- Direct consumers and linked pages: `07_Gear_Inventory/_Registries/Registry_CraftingRecipes.md` and `03_Factions_Societies/Lore/The_Proving_Houses.md`.
- Preserved meaning: sample owner, conditions, independent repetitions, failure mode, and harm owner remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the attestation state and review outcome.

### M-01j — `circle_of_interposition.temporary_pause`

- Source evidence: `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md`, `### circle_of_interposition.temporary_pause`, lines 219–232; scanner line 228.
- Target owner: `MISSING_OWNER`; `03_Factions_Societies/_Registries/Registry_Faction_Interfaces.md` only stores the planned record.
- Entity role: Circle of Interposition is `PROVIDER`.
- Mechanic owner: `MISSING_OWNER`.
- Universal system owner: none proven; `03_Factions_Societies/Pledge_Contracts.md` is a dependency and cannot be inferred as resolver.
- Does not own: guilt, investigation, custody, property, biological status, permanent imprisonment, or city-wide law.
- Direct consumers and linked pages: `03_Factions_Societies/Pledge_Contracts.md` and `03_Factions_Societies/Lore/The_Circle_of_Interposition.md`.
- Preserved meaning: subject, harm, pause holder, witness, scope, expiry, and release condition remain the minimum boundary.
- Required skill or handoff: lorekeeper and architecture evidence; no handoff can supply the absent resolver.
- Approval and validation: **APPROVAL_REQUIRED**. A future owner must define the timed-pause state, extension, and release.

### M-03 — district grammar

- Source evidence: `03_Factions_Societies/Lore/City_District_Social_Grammar.md`, `## Район как зависимость`, line 31.
- Target owner: `03_Factions_Societies/Lore/City_District_Social_Grammar.md`.
- Entity role: district identity, social dependency, temporary authority, and civic memory.
- Mechanic owner: none claimed; location geometry and routes are expressly deferred to world-generation owners.
- Universal system owner: `08_World_Generation/City_State/Civic_Event_Lifecycle.md` only for shared CivicEvent outcomes.
- Does not own: geometry, POI, street generation, routes, or physical state.
- Direct consumers and linked pages: `03_Factions_Societies/Lore/City_Genesis.md`, `03_Factions_Societies/Lore/Civic_Order.md`, `03_Factions_Societies/Lore/Civic_Ethos_Under_Lamps.md`, `03_Factions_Societies/Lore/Hearth_Anatomy.md`, `03_Factions_Societies/Lore/The_Cathedral.md`, `08_World_Generation/Anomaly/Anomaly_System.md`, `08_World_Generation/City_State/Civic_Event_Lifecycle.md`, and `08_World_Generation/Districts/City_Center.md`.
- Preserved meaning: the candidate supplies a concrete social test, not a location-generation rule.
- Required skill or handoff: lorekeeper evidence applied; no handoff because no runtime rule is asserted.
- Approval and validation: no migration; preserve the stated physical-location boundary.

### M-04 — Keepers late reveal

- Source evidence: `03_Factions_Societies/Lore/The_Keepers.md`, `## Позднее Прямое Общение`, line 177.
- Target owner: `03_Factions_Societies/Lore/The_Keepers.md`.
- Entity role: the Keepers observe and eventually present a narrative recognition of the Shard.
- Mechanic owner: none is asserted by the candidate paragraph.
- Universal system owner: none.
- Does not own: roster metaphysics, late-meta progression predicate, Tag assignment, contract lifecycle, reward, or access resolution.
- Direct consumers and linked pages: `03_Factions_Societies/Quest_Engine.md`, `03_Factions_Societies/_Registries/Registry_Factions.md`, `03_Factions_Societies/Pledge_Contracts.md`, `03_Factions_Societies/Lore/Faction_Address_System.md`, and `03_Factions_Societies/Lore/The_Circle_of_Interposition.md`; these links do not transfer runtime ownership.
- Preserved meaning: the late reveal is causal lore with intentionally incomplete Keeper knowledge.
- Required skill or handoff: lorekeeper verdict `CANON` for entity/narrative placement; no additional handoff.
- Approval and validation: no migration; any implementation of the late condition requires a separately scoped mechanic-owner audit.

### M-05 — quest archive grammar

- Source evidence: `03_Factions_Societies/Quest_Engine_Grammar.md`, `## 7. Сохранение и журнал` and `### Гроссбух`, line 230.
- Target owner: `03_Factions_Societies/Quest_Engine_Grammar.md`; `03_Factions_Societies/Quest_Engine.md` is its direct mechanic dependency.
- Entity role: an issuer or address may supply a contract seed but owns no archive result.
- Mechanic owner: Quest Engine.
- Universal system owner: none.
- Does not own: faction identity, roster state, hub POI state, or server lifecycle.
- Direct consumers and linked pages: `03_Factions_Societies/Quest_Engine.md`, `03_Factions_Societies/Reputation_Rules.md`, `03_Factions_Societies/Lore/Faction_Address_System.md`, `04_Player_Entities/Trait_Development.md`, `04_Player_Entities/Shell_Foundlings.md`, `04_Player_Entities/Lifecycle_Roster.md`, `08_World_Generation/Hub/01_Hub_Map_Table.md`, and `08_World_Generation/Generation/07_Server_Lifecycle.md`.
- Preserved meaning: archive fields describe the player-visible contract outcome and remain queryable.
- Required skill or handoff: architecture and curator evidence; no specialist question remained.
- Approval and validation: no migration; retain the listed direct-owner links.

### M-06 — reputation consequence

- Source evidence: `03_Factions_Societies/Reputation_Rules.md`, `### Спорный контракт`, line 55.
- Target owner: `03_Factions_Societies/Reputation_Rules.md`.
- Entity role: a Hearth or faction supplies an address and in-world consequence.
- Mechanic owner: Reputation Rules.
- Universal system owner: none proven.
- Does not own: faction membership, generic vendor stock, contract lifecycle, or a city-wide hidden score.
- Direct consumers and linked pages: `03_Factions_Societies/_Registries/Registry_Factions.md`, `03_Factions_Societies/Lore/Faction_Address_System.md`, `03_Factions_Societies/Lore/The_Circle_of_Interposition.md`, `06_Economy_Loot/Vendor_Logic.md`, and `03_Factions_Societies/Pledge_Contracts.md`.
- Preserved meaning: a contested contract carries a political consequence visible to the player.
- Required skill or handoff: lorekeeper confirms the faction framing does not grant resolver authority.
- Approval and validation: no migration; keep explicit feedback and negative membership boundary.

### M-07 — Race × Spec record

- Source evidence: `04_Player_Entities/_Registries/Registry_Combos.md`, `## Крыса × Ладчик`, line 259.
- Target owner: `04_Player_Entities/_Registries/Registry_Combos.md`.
- Entity role: a combo is an authored player-content coordinate, not a faction or runtime entity.
- Mechanic owner: Combat Profile Pipeline consumes the selected record.
- Universal system owner: none; the registry delegates P/Q/E contracts and module effects.
- Does not own: personal MasteryContribution, inherited unknown abilities, P/Q/E resolution, or module-effect policy.
- Direct consumers and linked pages: `04_Player_Entities/MVP_3x3_Design_Contract.md`, `04_Player_Entities/_Registries/Registry_Races.md`, `04_Player_Entities/_Registries/Registry_Specs.md`, `04_Player_Entities/Combat_Profile_Pipeline.md`, `04_Player_Entities/Proficiency_Arsenal.md`, and `07_Gear_Inventory/Thermos_System.md`.
- Preserved meaning: repeated profile fields are atomic content-instance records; pending cells remain pending.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration; do not normalize repeated fields into prose.

### M-08 — active parameter contracts

- Source evidence: `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`, `## Активные домены`, lines 44–128; scanner lines 61–63, 74, 102, and 114.
- Target owner: `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`.
- Entity role: sources submit modifier requests; none receives entity-level authority from the registry.
- Mechanic owner: the declared domain owners, including Weapon Ranged, Skill Build Philosophy, Dissonance System, Ballistics Armor, Physical Weight, and Magic Batteries.
- Universal system owner: each named `domain_owner` only inside its own parameter domain.
- Does not own: source values, unrelated domains, or a global rating.
- Direct consumers and linked pages: `04_Player_Entities/Combat_Profile_Pipeline.md`, `04_Player_Entities/Skill_Build_Philosophy.md`, `05_Combat_Survival/Magic_Batteries.md`, `05_Combat_Survival/Dissonance_System.md`, `07_Gear_Inventory/Thermos_Assembly.md`, and `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md`.
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
- Direct consumers and linked pages: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`; every future delivery source remains `MISSING_OWNER` until an exact owner path is declared.
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
- Direct consumers and linked pages: `07_Gear_Inventory/Physical_Weight.md`, `04_Player_Entities/Trait_Development.md`, `04_Player_Entities/Lifecycle_Roster.md`, `06_Economy_Loot/Extraction_Stabilization_Loop.md`, `03_Factions_Societies/Quest_Engine.md`, `03_Factions_Societies/Quest_Engine_Grammar.md`, and `03_Factions_Societies/Lore/The_First_Reception.md`.
- Preserved meaning: origin place and catastrophe-relative epoch stay factual; no rewrite or removal is authorized.
- Required skill or handoff: lorekeeper finds a boundary concern but no eligible owner in scope.
- Approval and validation: **APPROVAL_REQUIRED** for a future lore-owner selection; no migration in Pass B.

### M-11 — status effect records

- Source evidence: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`, effect-record headings from `### Кровотечение` through `### Насыщение восстановления`, scanner lines 92, 112, 139, 163, 187, 215, 234, 237, 239, 283, 285, 289, and 310.
- Target owner: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`.
- Entity role: none.
- Mechanic owner: `05_Combat_Survival/Status_Effects.md` supplies effect mechanics; the registry supplies atomic instances.
- Universal system owner: none claimed by an individual record.
- Does not own: local environment-state ownership, automatic reactions, or a universal application resolver.
- Direct consumers and linked pages: `05_Combat_Survival/Status_Effects.md`, `05_Combat_Survival/Combat_Three_Debts.md`, and `08_World_Generation/_Registries/Registry_Environment_States.md`.
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
- Direct consumers and linked pages: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`, `08_World_Generation/_Registries/Registry_Environment_States.md`, and `05_Combat_Survival/Dissonance_System.md`; future delivery sources remain `MISSING_OWNER` until exact paths are declared.
- Preserved meaning: the current budget and global/local boundary remain canon; values remain prototype-level empirical unknowns.
- Required skill or handoff: architecture lead identifies the bottleneck; curator distinguishes supported owner gap from scanner repetition.
- Approval and validation: **APPROVAL_REQUIRED** before moving or duplicating policy. The future owner must preserve the stated combat budget and environment boundary.

### M-13 — Three Debts trace

- Source evidence: `05_Combat_Survival/Combat_Three_Debts.md`, `## 2. Общий цикл действия`, line 55.
- Target owner: `05_Combat_Survival/Combat_Three_Debts.md`.
- Entity role: none.
- Mechanic owner: Combat Three Debts.
- Universal system owner: none; subordinate systems retain their own debt implementation.
- Does not own: weapon values, movement physics, status resolution, Dissonance calculation, or ability synergy.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Core.md`, `05_Combat_Survival/Hunt_Frontier_Loop.md`, `05_Combat_Survival/Magic_Batteries.md`, `05_Combat_Survival/Movement_Physics.md`, `05_Combat_Survival/Acoustic_Stealth.md`, `05_Combat_Survival/Status_Effects.md`, `05_Combat_Survival/Dissonance_System.md`, and `04_Player_Entities/Ability_Synergy.md`.
- Preserved meaning: counterplay traces and the no-idle-punishment boundary remain the combat contract.
- Required skill or handoff: architecture evidence; no specialist evidence changes the ownership finding.
- Approval and validation: no migration.

### M-14 — Traversal geography

- Source evidence: `05_Combat_Survival/Traversal_Core.md`, `## 1. Тактическая География`, line 18.
- Target owner: `05_Combat_Survival/Traversal_Core.md`.
- Entity role: none.
- Mechanic owner: Traversal Core.
- Universal system owner: none.
- Does not own: movement physics implementation or generated world topology.
- Direct consumers and linked pages: `05_Combat_Survival/Movement_Physics.md` and `08_World_Generation/Generation/10_World_Topology.md`.
- Preserved meaning: the closed Pass A direct opening and all three-echelon tactical trade-offs.
- Required skill or handoff: curator confirms A-05-01 is closed; no Pass B edit follows.
- Approval and validation: no migration; Pass A commit remains the only authorized change.

### M-15 — weapon-frame guidance

- Source evidence: `05_Combat_Survival/Weapon_Manifesto.md`, `## 5. Фазы столкновения`, line 102.
- Target owner: `05_Combat_Survival/Weapon_Manifesto.md`.
- Entity role: a frame is a designed tool, not a player class.
- Mechanic owner: Weapon Core, Weapon Melee, and Weapon Ranged resolve runtime weapon rules.
- Universal system owner: Combat Three Debts supplies the shared cost grammar.
- Does not own: a frame record, weapon registry values, ballistic result, AI response resolver, or Anomaly behavior resolver.
- Direct consumers and linked pages: `05_Combat_Survival/Combat_Three_Debts.md`, `05_Combat_Survival/Weapon_Core.md`, `05_Combat_Survival/Weapon_Melee.md`, `05_Combat_Survival/Weapon_Ranged.md`, `04_Player_Entities/Combat_Profile_Pipeline.md`, and `08_World_Generation/Content/World_Atlas/Sectors/Port/00_Port_Manifest.md`.
- Preserved meaning: loud fire has information consequences for anomaly, AI, and players without making the manifesto a runtime owner.
- Required skill or handoff: architecture and curator evidence; no further handoff.
- Approval and validation: no migration.

### M-16 — Condenser frame records

- Source evidence: `05_Combat_Survival/Weapons/Condenser_Rig_2H.md`, `## Экземпляры`, scanner line 66.
- Target owner: `05_Combat_Survival/Weapons/Condenser_Rig_2H.md`.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts for common commitment debt.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Ranged.md`, `05_Combat_Survival/Magic_Batteries.md`, and `05_Combat_Survival/_Registries/Registry_Weapons.md`.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-17 — Needle frame records

- Source evidence: `05_Combat_Survival/Weapons/Needle_Thrower_2H.md`, `## Экземпляры`, scanner line 64.
- Target owner: `05_Combat_Survival/Weapons/Needle_Thrower_2H.md`.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Ranged.md` and `05_Combat_Survival/_Registries/Registry_Weapons.md`.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-18 — Pulse frame records

- Source evidence: `05_Combat_Survival/Weapons/Pulse_Tool_1H.md`, `## Экземпляры`, scanner line 67.
- Target owner: `05_Combat_Survival/Weapons/Pulse_Tool_1H.md`.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Ranged.md`, `05_Combat_Survival/Magic_Batteries.md`, and `05_Combat_Survival/_Registries/Registry_Weapons.md`.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-19 — Scatter frame records

- Source evidence: `05_Combat_Survival/Weapons/Scatter_Valve_2H.md`, `## Экземпляры`, scanner lines 66–67.
- Target owner: `05_Combat_Survival/Weapons/Scatter_Valve_2H.md`.
- Entity role: authored weapon-frame instance.
- Mechanic owner: Weapon Ranged and Weapon Core.
- Universal system owner: Combat Three Debts.
- Does not own: generic status rules, item registry ownership, or all ranged-gun behavior.
- Direct consumers and linked pages: `05_Combat_Survival/Weapon_Ranged.md`, `05_Combat_Survival/Magic_Batteries.md`, and `05_Combat_Survival/_Registries/Registry_Weapons.md`.
- Preserved meaning: parallel fields remain atomic frame data.
- Required skill or handoff: curator structured-record evidence; no handoff.
- Approval and validation: no migration.

### M-20 — Rez nature and wallet

- Source evidence: `06_Economy_Loot/Currency_Rez.md`, `## 1. Природа Валюты`, line 24.
- Target owner: `06_Economy_Loot/Currency_Rez.md`.
- Entity role: Rez is a physical economic item, not an independent lore institution.
- Mechanic owner: Currency Rez.
- Universal system owner: Economy Core for economy-wide lifecycle only.
- Does not own: inventory slot capacity, Economy Core rules, battery behavior, or combat-damage resolution.
- Direct consumers and linked pages: `07_Gear_Inventory/Containers_Slots.md`, `06_Economy_Loot/Economy_Core.md`, and `05_Combat_Survival/Magic_Batteries.md`.
- Preserved meaning: physical currency, aggregated UI, spending order, and the non-Rez combat-cost boundary.
- Required skill or handoff: architecture evidence; no specialist handoff.
- Approval and validation: no migration.

### M-21 — Thermos module records

- Source evidence: `07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md`, `## Candidate records`, scanner lines 76–444.
- Target owner: `MISSING_OWNER` for the listed effect domains; `07_Gear_Inventory/_Registries/Registry_Thermos_Modules.md` remains the definition-record owner.
- Entity role: module definition is a content instance supplied to assembly.
- Mechanic owner: Thermos Assembly resolves an installed instance; declared ParameterContracts resolve runtime effects when they exist.
- Universal system owner: `MISSING_OWNER` for the module outputs listed as absent in Parameter Contracts.
- Does not own: selected pattern, occupied nodes, damage, stitched state, active body interface, or local effect-policy invention.
- Direct consumers and linked pages: `07_Gear_Inventory/Thermos_System.md`, `07_Gear_Inventory/Thermos_Assembly.md`, `07_Gear_Inventory/_Registries/Registry_Thermoses.md`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md`, and `04_Player_Entities/_Registries/Registry_Parameter_Contracts.md`.
- Preserved meaning: all records stay `blocked_calibration`; `concept_effects` remain nonauthoritative discovery fields and atomicity remains a review requirement.
- Required skill or handoff: architecture lead identifies the owner gap; curator confirms structured repetition is not itself duplication.
- Approval and validation: **APPROVAL_REQUIRED** for each parameter domain. Do not make a module installable until its exact owner, contract, topology, coverage, and calibration are present.

### M-22 — Thermos model records

- Source evidence: `07_Gear_Inventory/_Registries/Registry_Thermoses.md`, `### Городской серийный Термос` and `### Шаблон Термоса`, scanner lines 52, 53, and 55.
- Target owner: `07_Gear_Inventory/_Registries/Registry_Thermoses.md`.
- Entity role: model definition supplied to an assembly instance.
- Mechanic owner: Thermos Assembly resolves fitting and committed assembly state.
- Universal system owner: Thermos System owns shared definition-versus-instance boundary.
- Does not own: fit revision, selected pattern, occupied nodes, damage, stitched state, active effects, or derived slot count.
- Direct consumers and linked pages: `07_Gear_Inventory/Thermos_System.md`, `07_Gear_Inventory/Thermos_Assembly.md`, `07_Gear_Inventory/_Registries/Registry_Thermos_Interfaces.md`, and `07_Gear_Inventory/Equipment_PaperDoll.md`.
- Preserved meaning: `blocked_topology` is an explicit content gap, not missing authority or an invitation to infer topology.
- Required skill or handoff: architecture and curator evidence; no handoff.
- Approval and validation: no migration; preserve the block until topology, fit envelope, mass, and Paper Doll mapping exist.

### M-23 — mutation-line records

- Source evidence: `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`, active tier records, scanner lines 56, 68, 100, 114, 116, 118, 149, and 162.
- Target owner: `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`.
- Entity role: anomaly-line and tier content instance.
- Mechanic owner: `08_World_Generation/Anomaly/Anomaly_System.md` resolves the overarching anomaly system.
- Universal system owner: none beyond the anomaly system’s shared lifecycle.
- Does not own: a global monster stat resolver, local scene state, or a second weather owner.
- Direct consumers and linked pages: `08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md`, `08_World_Generation/_Registries/Registry_Mobs.md`, and `08_World_Generation/_Registries/Registry_Biomes.md`.
- Preserved meaning: repeated tier fields express intentionally parallel authored content.
- Required skill or handoff: curator evidence; no handoff.
- Approval and validation: no migration.

### M-24 — biome-tier records

- Source evidence: `08_World_Generation/_Registries/Registry_Biomes.md`, Port tier records, scanner lines 67, 81, 92, and 105.
- Target owner: `08_World_Generation/_Registries/Registry_Biomes.md`.
- Entity role: biome and threat-tier content instance.
- Mechanic owner: no separate mechanic resolver is claimed; `08_World_Generation/_Registries/Registry_Biomes.md` is the sole content owner for the biome-tier record.
- Universal system owner: none; numerical pressure is an empirical calibration issue.
- Does not own: loot table ownership, spawn resolver, a global mob rating, or a weather result resolver.
- Direct consumers and linked pages: `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`. The source names no canonical path for its generic map-generator reader, so no additional consumer is inferred.
- Preserved meaning: `env_pressure`, `gate_pulse`, and filter-rating values remain explicitly prototype-level.
- Required skill or handoff: architecture evidence distinguishes content gap from authority finding.
- Approval and validation: no migration.

### M-25 — environment-state records

- Source evidence: `08_World_Generation/_Registries/Registry_Environment_States.md`, `### Метка глубины`, scanner line 119.
- Target owner: `08_World_Generation/_Registries/Registry_Environment_States.md`.
- Entity role: a local scene-state instance with one local consequence.
- Mechanic owner: the record-local IDs `dungeon_commitment` and `dungeon_exit_rule` are not canonical paths; their resolver is `MISSING_OWNER` for this map entry.
- Universal system owner: none; a status aftermath is only a declared aftermath, never the scene’s owner.
- Does not own: a global status resolver, generic effect stack, or automatic reaction table.
- Direct consumers and linked pages: `05_Combat_Survival/_Registries/Registry_StatusEffects.md`, `08_World_Generation/Anomaly/Anomaly_System.md`, `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`, and `08_World_Generation/Content/World_Atlas/Sectors/Port/01_Foreign_Water_Mutation_Lines.md`.
- Preserved meaning: telegraph, choice, refusal, termination, and local consequence remain inseparable scene data.
- Required skill or handoff: architecture and curator evidence; no handoff.
- Approval and validation: **APPROVAL_REQUIRED** for the `mark_of_greed` resolver. A future bounded owner must map `dungeon_commitment` and `dungeon_exit_rule` to one canonical state machine while preserving one primary scene axis and consequence.

### M-26 — mob and variant records

- Source evidence: `08_World_Generation/_Registries/Registry_Mobs.md`, mutation-line and Hungry Form records, scanner lines 294–479.
- Target owner: `08_World_Generation/_Registries/Registry_Mobs.md`.
- Entity role: mob or mutation-variant content instance.
- Mechanic owner: each local `physiology_contract` and `action_contract` resolves its body and actions.
- Universal system owner: none; encounter numbers stay local to the MobID.
- Does not own: player-stat conversion, universal RPG debuffs, hidden rating variants, or a second status owner.
- Direct consumers and linked pages: `08_World_Generation/Anomaly/16_Anomaly_Mutation_Lines.md`, `08_World_Generation/Content/World_Atlas/Sectors/Port/01_Foreign_Water_Mutation_Lines.md`, and `08_World_Generation/_Registries/Registry_Anomaly_Mutations.md`.
- Preserved meaning: repeated tactical fields are the readable projection of local contracts.
- Required skill or handoff: curator evidence; no handoff.
- Approval and validation: no migration; preserve explicit compatible status interfaces and player-readable counterplay.

### M-27 — Hub weather presentation

- Source evidence: `08_World_Generation/Hub/04_Time_Atmosphere.md`, `## 2. Рейд: Аномальная Погода`, line 31.
- Target owner: `08_World_Generation/Hub/04_Time_Atmosphere.md`.
- Entity role: none.
- Mechanic owner: `08_World_Generation/Generation/03_Dynamic_Weather.md` owns the complete weather contract.
- Universal system owner: none.
- Does not own: physics, route, gear, enemy, trap, or exit resolution.
- Direct consumers and linked pages: `08_World_Generation/Generation/03_Dynamic_Weather.md`.
- Preserved meaning: weather is gameplay-relevant while this page only communicates the atmosphere and routing boundary.
- Required skill or handoff: architecture and curator evidence; no handoff.
- Approval and validation: no migration; retain the downstream contract link.

## Approval gate and follow-up

There are no `APPROVED_FOR_MIGRATION` rows. The map identifies four classes of
unapproved work: eight planned faction interfaces, status application policy,
Foundling historical ownership, Thermos effect domains, and the Mark of Greed
dungeon resolver. Each remains
unaltered under `MISSING_OWNER` or `APPROVAL_REQUIRED`; none licenses a canonical
move, rewrite, registry change, route regeneration, or management-page change.

`python3 tools/vault_guard.py` reports the workflow `.superpowers` directory.
This is an environment follow-up only; no source workaround is appropriate.
