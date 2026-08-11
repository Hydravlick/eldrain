# Canonical prose-refactor audit manifest — 2026-08-11

## Scope and decision boundary

This is an audit-only manifest. It records the sole approved Pass A edit batch and
the scanner-source inventory for the later Pass B responsibility review. It does
not authorize changes to generated navigation, registries, management notes, or
any row marked `KEEP`.

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
| A-05-01 | Pass A + Pass B | MECHANIC | Traversal Core | Direct opening rule | REWRITE |

### A-05-01 — Traversal Core opening

- **Editable source:** `05_Combat_Survival/Traversal_Core.md`, line 18 only.
- **Canonical owner:** `05_Combat_Survival/Traversal_Core.md` (`index_route: owner`).
- **Direct dependencies:** `05_Combat_Survival/Movement_Physics.md` and `08_World_Generation/Generation/10_World_Topology.md` are named by `related_files`; they are read-only context for this batch.
- **Incoming links:** `05_Combat_Survival/00_Routes.md` is the only current incoming corpus link. It is generated and is not editable in this batch.
- **Evidence:** under `## 1. Тактическая География`, line 18 opens with “Успех выживания зависит не только от меткости, но и от грамотного использования геометрии уровня.” The scanner classifies this as `FORMULAIC_PROSE`; the surrounding three-tier list already supplies the concrete rule.
- **Curator finding:** `FORMULAIC_PROSE`. The contrast construction delays the player-facing premise without adding a condition, state, value, or boundary.
- **Smallest safe repair:** replace only the contrast clause with a direct premise that survival depends on marksmanship and use of level geometry; retain the Verticality term and the following three-echelon list unchanged.
- **Preserved meaning:** the three-echelon topology, each tier’s examples and trade-offs, the 2.5 metre climb limit, no-sticky-cover boundary, all hazards, YAML, headings, links, numeric literals, and table structure.
- **Approval:** approved by this prose-refactor plan for one MECHANIC owner; no lore, balance, or location-design decision is introduced.
- **Validation:** run `python .agents/skills/eldraine-vault-curator/scripts/validate_rewrite.py --json <before-copy> 05_Combat_Survival/Traversal_Core.md`; inspect the opening and the cover table for protected-structure parity; then run `python3 tools/vault_guard.py`.

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

- `01_Core_Vision/Art_Direction_Material_Grammar.md:115` — 1 `FORMULAIC_PROSE`; the contrast identifies the player-visible damage signal and remains concrete material grammar.
- `02_World_Lore/Lizard_Culture.md:65,185,269,273,329,337` — 6 `FORMULAIC_PROSE`; all are concrete cultural practices, spatial signals, or intentional lore framing. This 4,567-word culture page exceeds 3,000 words, so it is explicitly not combined with another culture page; no supported rewrite is admitted.
- `02_World_Lore/Magipunk_Physics.md:67` — 1 `FORMULAIC_PROSE`; compact statement of the practice-versus-understanding premise.
- `02_World_Lore/Protocol_Resonance.md:86` — 1 `FORMULAIC_PROSE`; defines stored context beyond speech.
- `02_World_Lore/Rat_Culture.md:137,177` — 2 `FORMULAIC_PROSE`; carries lineage and production-provenance constraints.
- `02_World_Lore/Squirrel_Culture.md:41,43,65,177` — 4 `FORMULAIC_PROSE`; carries storage-state, succession, and food-timing rules.
- `02_World_Lore/The_Ark.md:127` — 1 `FORMULAIC_PROSE`; defines the time as well as spatial failure condition.
- `02_World_Lore/The_Entity.md:116` — 1 `FORMULAIC_PROSE`; carries a late metaprogression reveal in approved lore voice.
- `02_World_Lore/Toad_Culture.md:34,531` — 2 `FORMULAIC_PROSE`; preserves anti-essentialist characterization and faction ideology.
- `03_Factions_Societies/Lore/City_District_Social_Grammar.md:31` — 1 `FORMULAIC_PROSE`; its following list makes the district test concrete.
- `03_Factions_Societies/Lore/The_Keepers.md:177` — 1 `FORMULAIC_PROSE`; intentional reveal voice and causal claim.
- `03_Factions_Societies/Quest_Engine_Grammar.md:230` — 1 `FORMULAIC_PROSE`; specifies archive outcome fields.
- `03_Factions_Societies/Reputation_Rules.md:55` — 1 `FORMULAIC_PROSE`; expresses the player-facing political consequence.
- `04_Player_Entities/Shell_Foundlings.md:42` — 1 `FORMULAIC_PROSE`; specifies both origin place and catastrophe-relative epoch.
- `05_Combat_Survival/Combat_Three_Debts.md:55` — 1 `FORMULAIC_PROSE`; states counterplay traces and the no-idle-punishment boundary.
- `05_Combat_Survival/Weapon_Manifesto.md:102` — 1 `FORMULAIC_PROSE`; specifies information, AI, anomaly, and player response to loud fire.
- `06_Economy_Loot/Currency_Rez.md:24` — 1 `FORMULAIC_PROSE`; intentional lore-to-economy identity statement.
- `08_World_Generation/Hub/04_Time_Atmosphere.md:31` — 1 `FORMULAIC_PROSE`; direct gameplay-weather rule with an authoritative downstream contract link.

Every `02_World_Lore` source above is `Pass A only`; no World Lore source enters
Pass B through this manifest.

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

Task 7 reviews responsibility only after each closed Pass A batch. Its in-scope
source inventory is the 25 non-lore scanner-source paths under `03_` through `08_`
represented by the following groups: the single A-05-01 owner; the non-lore
`KEEP — intentional voice` entries above; and all `KEEP — structured repetition`
registry and atomic-profile entries above. The exact paths and scanner line
evidence are the lists in this manifest. It must not reopen any `02_World_Lore`
source, generated `00_Routes.md` page, `00_Index.md`, or a registry merely because
the scanner matched its deliberately repeated schema.

Pass B may report an authority concern only with owner-scoped evidence. It does
not convert a `KEEP` disposition into an edit authorization; a newly supported
finding requires a new bounded batch and approval.

## Batch limits check

- A-05-01 contains one normal owner, no editable dependency, and one MECHANIC register.
- Its editable surface is one non-table line, below the 1,500-line limit.
- No batch crosses a domain boundary, and no culture page is admitted to a mixed batch.
- No table cell contains a link, raw path list, line break, or literal pipe.
