# Feature contract

A Feature is an experiential design synthesis of a player-facing capability. Its first job is to let a reader imagine and understand this part of Eldrain without knowing the vault's internal architecture. It explains lived play first and maps its supporting integration second.

Read alongside [design-architecture.md](design-architecture.md) when a feature is proposed or revised. Feature descriptions live in `01_Core_Vision/Features`; their map and coverage views remain derived from those descriptions.

## Explain the playable experience

Move from a concrete situation to what the player sees, does and changes, then to the next choice that follows. Explain design intent and supporting systems after the reader can follow the play. Use the amount and order of prose this capability needs to answer:

- Where is the player, and what are they trying to do?
- What information and signals can they see? What remains unknown?
- Which concrete options can they choose between?
- Which consequences can they foresee, and which do they discover later? Where does the earlier choice show up again?
- What changes on success, cancellation, failure or return, and what can the player do next?
- Which supported details make this capability characteristic of Eldrain?
- Which recurring gameplay decisions arise from it?

These are coverage questions for completeness, not required headings or a page template. Features need not share the same structure. Ground situations and examples in existing owners/lore; a vivid example cannot silently introduce a design decision. Read [editorial-quality.md](editorial-quality.md) for language and page-specific voice.

## Connect the experience to its support

After explaining play, connect it to Systems, UX, Content and Data. The Feature retains integration intent and acceptance coverage as maintenance responsibilities. Check responsible owners at relevant flow boundaries, state/interface dependencies and gaps, configuration/data sources, authored content, UX signals and unavailable states, observable acceptance scenarios and remaining playtest questions. Identify production disciplines such as gameplay, UX, audio, animation, narrative, level design and QA where they contribute. This coverage does not dictate the voice or order of the main prose.

A Feature is not a mini System specification. Its opening must not be organized around state ownership, resolver boundaries, ItemID edge cases, schema, internal predicates, QA corner cases or lists of production disciplines. Technical details that do not help the reader understand player experience must not occupy its upper half. Keep technical connections in queryable properties, owner links, a short late section such as “Под капотом”, or derived Feature × Owner views. Do not mechanically repeat those connections in the body.

Universal rules, formulas, eligibility predicates and state resolution remain with system/mechanic owners. A Feature links to those contracts; its high-level flow must not become a competing resolver. Keep this harness rule here; individual Features only need the connections that explain their own capability.

## Properties

A property belongs in YAML when it serves a real query, view, validation or identity need. The body does not have to repeat it literally. Existing `player_promise` or `expected_dynamics` properties may remain when used by Feature Map/Base consumers; write the main prose naturally. This editorial guidance does not change the metadata/schema contract or authorize cleanup. Any later metadata cleanup must check every affected Base and Dataview consumer.

`type: feature` is supported now. A feature uses ordinary `status` and `system`, a unique `feature_id`, and a nonempty `system_owners` list of quoted wikilinks to active routable system/mechanic owners. Optional `data_sources` and `ux_surfaces` lists also use existing note links. `production_disciplines` is a list of text labels. `validation` may link to acceptance or playtest notes; a test does not certify the completeness of their prose.

A Feature cannot declare `owns` or `canonical_id` for underlying rules. `feature_id` identifies the capability. `index_route: owner` can make it discoverable as the owner of the feature description; this routing flag does not grant gameplay authority. Route metadata follows the normal route contract.

The validator checks these fields wherever a feature is placed in an approved gameplay domain. Draft/deferred features may be incomplete, but declared links must resolve and declared system owners must be valid; only active features require the complete machine-checkable contract.
