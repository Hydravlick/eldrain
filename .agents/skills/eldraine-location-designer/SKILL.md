---
name: eldraine-location-designer
description: Use when designing or reviewing an Eldraine sector, district, raid map, street network, traversal layer, procedural layout, POI topology, T1/T2/T3 spatial evolution, or when location flow may be unreadable, disconnected, repetitive, or infeasible to build.
---

# Eldraine Location Designer

## Principle

Design a location as a sequence of readable spatial decisions. Make every phase change preserve causality, navigation and a credible production method.


## Responsibility Boundary

Own the location's spatial decisions, route grammar, connectivity, phase readability, and production method. Report which spatial facts remain learnable across procedural variants and which uncertainty the map contributes. Do not allocate the total uncertainty budget across map, Pawn, build, encounter, and rules; use `eldraine-system-architect` when those layers interact.

## Establish Context

Read `09_Project_Management/Architecture_MVP.md`, `00_Index.md`, `08_World_Generation/Content/World_Atlas/Sectors/_Sector_Manifest_Template.md`, the relevant live lore, and the generation systems touched by the location.

Use sub-skills only when their condition is present:

- **REQUIRED SUB-SKILL:** Use `eldraine-lorekeeper` when architecture or phase effects derive from a civilization, catastrophe or metaphysical rule.
- **REQUIRED SUB-SKILL:** Use `eldraine-player-experience` when judging lived navigation, warning, commitment, retreat or failure comprehension.
- **REQUIRED SUB-SKILL:** Use `eldraine-balance-modeler` when density, distance, timing, probability or thresholds are claimed.
- **REQUIRED SUB-SKILL:** Use `eldraine-crash-test` when route topology may create camping, safe farming, dominant shortcuts or unreachable rewards.
- **REQUIRED SUB-SKILL:** Use `eldraine-gdd-author` before editing the vault.
- **REQUIRED LEAD SKILL:** Use `eldraine-system-architect` first when the question is the combined effect of spatial uncertainty with build, roster, identity, or progression uncertainty.

## Build the Spatial Contract

Produce these units in order:

1. **Spatial promise:** State what the player learns and which decision becomes harder.
2. **Manual frame:** Name handcrafted safe zones, landmarks, master sockets and immutable boundaries.
3. **Procedural kernel:** Name roots, allowed modules, forbidden changes and required connections.
4. **Route grammar:** Define primary paths, secondary paths, convergence spaces, landmarks, vertical layers and transitions between them.
5. **Connectivity invariants:** Preserve a path from every active insertion to at least one extraction. Telegraph closures before commitment. Provide a readable alternate layer when an essential route is lost.
6. **Tier deltas:** Give each Tier one leading spatial verb. T1 teaches it safely, T2 demands rerouting, T3 combines known rules under a timed or positional commitment.
7. **Stable representation:** Separate the physical Stable-sector from its Generation Snapshot and Peaceful Projection. The player uses Stable POIs through the lobby table, not free traversal.

## Map Effects to Production

Classify every proposed effect:

| Class | Method | Default verdict |
|:---|:---|:---|
| State | material, light, door state, hazard volume, NavLink | `REALIZABLE` |
| Variant | prepared module swap or bounded prefab set | `REALIZABLE` |
| Set-piece | authored sequence with a narrow trigger | `PROTOTYPE_REQUIRED` |
| Simulation | runtime deformation, fluid simulation, arbitrary destruction or topology rewrite | `OVERBUILT` unless separately proven |

Use the smallest method that preserves the intended decision. Example: implement a T2 bridge loss with a prepared broken variant, disabled NavLink, visible warning and an already taught roof bypass; do not simulate structural collapse across the whole district.

## Phase Delta Contract

For each Tier, provide:

| Field | Required answer |
|:---|:---|
| Perception | What the player sees or hears before danger |
| Interpretation | What rule the signal teaches |
| Route delta | Which path or layer changes |
| Decision | Continue, reroute, wait or retreat |
| Commitment | Exposure, time, resource or lost return path |
| Feedback | What proves the state changed |
| Failure | Why loss remains understandable |
| Implementation | Exact production class and method |

Historical layers are source material, not automatic runtime-Tier assignments. Verify the mapping against live canon.

## Guardrails

- Do not replace location design with lists of mobs, loot or art assets; link registries.
- Do not use “more enemies” or stronger debuffs as the only Tier progression.
- Do not close every route or create an insertion without a valid extraction path.
- Do not make UI the sole warning for a spatial change.
- Do not require a traversal verb before teaching it in a lower-pressure context.
- Do not present an unproven runtime technology as ordinary content work.
- Do not treat the Stable-sector projection as a freely walkable hub location.

## Answer Contract

Lead with one verdict:

- `REALIZABLE` — the flow uses proven, bounded methods and satisfies connectivity.
- `PROTOTYPE_REQUIRED` — the concept is coherent, but one or more interactions need a focused test.
- `OVERBUILT` — the intended result depends on excessive runtime complexity or cannot preserve readable flow.

Then provide:

1. intended emotional and navigational arc;
2. canon support and tensions;
3. manual frame, kernel, roots and boundaries;
4. route layers and connectivity invariants;
5. T1/T2/T3 delta table;
6. success, retreat and failure paths;
7. production mapping and expensive assumptions;
8. prototype observations;
9. canonical files to extend or create.

Do not edit files unless the user asks. When editing, keep sector-specific detail in its manifest and shared rules in the universal template or generation systems.
