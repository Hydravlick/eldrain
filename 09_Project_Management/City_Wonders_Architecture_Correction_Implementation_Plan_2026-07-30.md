# City Wonders Architecture Correction Implementation Plan

> **For agentic workers:** Execute inline in the current workspace. The user has explicitly prohibited creating a Git commit for this migration.

**Goal:** Move Civic Dispatch to contextual reference and make shared CityState, account progression, civic events, magic, practices, Constants, and Requiems obey the approved architecture.

**Architecture:** A regional-shard `CityState` publishes a shared world revision, merchant catalogue, and civic-event ledger. Raid sessions consume the published world revision but keep live raid state local; accounts own contracts, discovery, personal stock, rewards, and social consequences. City event lifecycle, Quest Engine, social grammar, and the Hub Map have non-overlapping responsibilities.

**Tech Stack:** Obsidian Markdown, YAML frontmatter, root-relative wikilinks, `tools/build_routes.py`, `tools/vault_guard.py`.

## Global Constraints

- Active rule owners live only in `01_` through `08_`; `10_Reference` is contextual and cannot define MVP runtime rules.
- Do not add an active Civic Dispatch system, real-time wait, hidden success chance, or off-scene lethal Pawn outcome.
- A shared POI is part of `world_revision`; only discovery, contract binding, rewards, and social consequences are account-scoped.
- The Map Table is a projection and cannot own CityState, event transitions, contracts, merchant stock, or rewards.
- Requiem remains a localized POI inside an Anomaly with a readable source, extent, entry tell, exit, and refusal path.
- This migration does not reopen Constantine chronology: it preserves current historical references provisionally and records chronology as a separate unresolved lore decision.
- Do not select the single-race hero-kit prototype in this migration.
- Do not stage or commit files.

---

### Task 1: Separate active city calls from deferred Civic Dispatch

**Files:**

- Create: `10_Reference/Civic_Dispatch_Gorodskoi_Otklik_Reference.md`
- Modify: `03_Factions_Societies/Quest_Engine.md`
- Modify: `09_Project_Management/City_Wonders_Canon_Integration_Design_2026-07-30.md`

**Interfaces:**

- Produces: a reference-only `Civic Dispatch` proposal with `READY → CIVIC_COMMITTED → NEEDS_INTERVENTION | RESOLVED → READY`.
- Preserves: active Quest Engine may turn a civic call into an ordinary extraction contract, but does not name a Pawn, set readiness, delegate work, or resolve a Dispatch outcome.

- [x] Create the reference note with contextual frontmatter, scope, future state machine, visible risk requirements, player intervention rule, and explicit `not_active_canon` boundary.
- [x] Remove the active roster-presentation and anti-Dispatch implementation text from Quest Engine; replace it with a civic-call interface that consumes `affected_parties[]` and `public_pressures[]` from CityState.
- [x] Update the earlier integration note so it no longer describes an active `Городское обязательство` as the adopted roster link.
- [x] Verify with `rg -n "CIVIC_COMMITTED|Пешку-представителя|Dispatch-система" 01_Core_Vision 02_World_Lore 03_Factions_Societies 04_Player_Entities 08_World_Generation` that only the reference note contains deferred Dispatch state.

### Task 2: Establish CityState and the civic-event lifecycle

**Files:**

- Create: `08_World_Generation/City_State/Civic_Event_Lifecycle.md`
- Modify: `08_World_Generation/Generation/07_Server_Lifecycle.md`

**Interfaces:**

- Produces: `CityState(city_state_id, city_revision, world_revision, merchant_catalog_revision, civic_events[])` and `CivicEvent` state transitions.
- Consumes: ordered CityRevision barriers and validated `ContributionReceipt` records from completed account contracts.
- Guarantees: a SessionID consumes a published `world_revision` and cannot alter CityState; local live raid changes never cross sessions.

- [x] Define `CIVIC_EVENT_LIFECYCLE` as the sole owner of CityState, event transitions, public contribution aggregation, `resolution_policy_ref`, and typed residue.
- [x] Define the event record with `affected_parties[]`, `public_pressures[]`, contribution channels, typed residue, persistence, and the no-FOMO invariant.
- [x] Define `ContributionReceipt` as a consequence of validated account contract evidence, with a personal receipt and an anonymized public ledger contribution.
- [x] Update Server Lifecycle so a new SessionID reads the already-published WorldRevision; retain SessionID ownership of local clock, phase barriers, and live map settlement.
- [x] Verify one-owner language with `rg -n "CityState|world_revision|ContributionReceipt|CIVIC_EVENT_LIFECYCLE" 08_World_Generation`.

### Task 3: Wire the event entity to social, quest, map, merchant, and POI consumers

**Files:**

- Modify: `03_Factions_Societies/Lore/City_District_Social_Grammar.md`
- Modify: `03_Factions_Societies/Quest_Engine.md`
- Modify: `08_World_Generation/Hub/01_Hub_Map_Table.md`
- Modify: `08_World_Generation/Hub/03_Hub_Map_Interaction.md`
- Modify: `08_World_Generation/Generation/04_Global_Map_Rotation.md`
- Modify: `06_Economy_Loot/Barter_System.md`
- Modify: `08_World_Generation/_Registries/Registry_POIs.md`

**Interfaces:**

- Consumes: CityState public revisions and civic event records.
- Produces: map projection, personal call candidates generated by Quest Engine, public merchant catalogue plus account-owned stock, and shared POI/account-relation boundary.

- [x] Keep City District Social Grammar responsible only for impossible rule, human dependency, and public dispute; link it to Civic Event Lifecycle instead of inventing event state.
- [x] Make Quest Engine generate an account contract from public pressures and affected parties, then emit a ContributionReceipt only after its normal evidence rule succeeds.
- [x] Make Map Table display visible events independently of the pinned contract, public merchant catalogue, and shared POI generation; preserve one pinned personal objective.
- [x] Make Barter System distinguish public merchant catalogue/availability from account-owned personal stock, purchase, custody, and inventory.
- [x] Make Registry POIs state that POI existence and base rule are WorldRevision-scoped, while discovery, contract relation, and reward are account-scoped.
- [x] Check no consumer declares lifecycle ownership: `rg -n "владеет.*CityState|владеет.*CivicEvent|CIVIC_EVENT_LIFECYCLE" 03_Factions_Societies 06_Economy_Loot 08_World_Generation`.

### Task 4: Correct magic and practice certainty boundaries

**Files:**

- Modify: `02_World_Lore/Magipunk_Physics.md`
- Modify: `04_Player_Entities/Specs/Vanguard.md`
- Modify: `04_Player_Entities/Specs/Technocrat.md`
- Modify: `04_Player_Entities/Specs/Drifter.md`
- Modify: `04_Player_Entities/_Registries/Registry_Specs.md`
- Modify: `09_Project_Management/TODO.md`

**Interfaces:**

- Produces: a common player-facing operational grammar and a non-exclusive author-facing ontology of causal modes.
- Preserves: active names, IDs, MVP matrix, and the fact that practices are not professions or mandatory party roles.

- [x] Replace the claim that ritual, alchemy, and industry control variables of one physical cycle with a distinction between operational readability and differing causal modes.
- [x] Describe each active practice only through its current readable method and limits; do not canonize the unproven three-verb symmetry as a universal assignment rule.
- [x] Add a direct link to the approved prototype requirement and update TODO to require a single-race three-practice test without choosing the race.
- [x] Verify stable IDs remain `assault`, `support`, and `scout`, and player labels remain Застрельщик, Ладчик, Странник.

### Task 5: Clarify ritual civic function, Constants, and Requiem locality

**Files:**

- Modify: `03_Factions_Societies/Lore/The_Cathedral.md`
- Modify: `02_World_Lore/The_Ark.md`
- Modify: `02_World_Lore/The_Entity.md`
- Modify: `08_World_Generation/Anomaly/Anomaly_System.md`
- Modify: `08_World_Generation/_Registries/Registry_POIs.md`

**Interfaces:**

- Produces: Аспекты as public ritual Masks; Constants with canonical relic-trace families; Requiems as bounded localized POI manifestations.
- Preserves: uncertainty about any external source that answers through an Aspect, provisional current historical references to Constants, and the causal link from a dense relic trace to Entity misinterpretation.

- [x] State that an Aspect is used to frame obligation, grief, mutual aid, and ritual compatibility; do not settle whether any external metaphysical agency answers through an Aspect.
- [x] Give every Constantine at least one `relic_trace_family` with a canonical precedent, multiple material/spatial/oral/procedural carriers, and disputed interpretations; make Requiem optional.
- [x] Define a Requiem record's `manifestation_anchor`, `manifestation_extent`, `entry_tell`, `exit_condition`, and `refusal_path`.
- [x] Permit creature, object, route, scene, or localized weather as a POI manifestation only when it respects those boundaries.
- [x] Verify no page says a Requiem is a global affix, whole sector, personal instance, or mandatory result of a Constantine.

### Task 6: Align project guidance and validate the corpus

**Files:**

- Modify: `09_Project_Management/City_Wonders_Architecture_Correction_Design_2026-07-30.md`
- Modify: `09_Project_Management/City_Wonders_Canon_Integration_Design_2026-07-30.md`
- Generated: `00_Routes.md` and system `00_Routes.md` pages, only through `tools/build_routes.py --write`

**Interfaces:**

- Produces: one approved architecture correction, no active Dispatch contradiction, and regenerated navigation.

- [x] Reconcile the earlier migration document with the approved correction, retaining provenance but marking superseded decisions as contextual history.
- [x] Ensure prototype criteria cover visibility, event/call distinction, public contribution causality, residue, refusal without FOMO, Requiem locality, and practice breadth.
- [x] Run `python tools/build_routes.py --write`.
- [x] Run `python tools/vault_guard.py`; record pre-existing failures separately from errors introduced by this migration.
- [x] Run focused `rg` checks for stale Dispatch states, old lifecycle path, duplicate CityState owners, and unresolved active links.
