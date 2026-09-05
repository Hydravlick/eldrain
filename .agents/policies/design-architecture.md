# Design vocabulary

This is harness guidance, not Eldrain game canon. Read it when decomposing a design or choosing a page's responsibility. Physical placement of the future Feature layer is intentionally undecided.

| Concept | Responsibility |
|---|---|
| Feature | A complete player-facing capability or experience, assembled from systems, UX, authored content and validation surfaces. Owns its promise, use cases and integration completeness; links to the rules below it. |
| System | A coherent stateful model of rules, states, transitions and interfaces. Owns authoritative resolution across its instances. |
| Mechanic | A local or atomic rule, action or interaction primitive. May be owned inside a system page; a separate file is useful only when independently readable. |
| Content | A specific authored configuration using an existing rule grammar: encounter, sector, quest, variant or event. |
| Entity | A concrete object with identity, context and stable properties: person, faction, species, place or weapon frame. Its identity does not grant ownership of every system it participates in. |
| Registry | Stable IDs, structured records, fields/schema, bounded interface records or an authored configuration family. A family overview may instead read entity-owned data; declare the role and do not maintain both copies. |
| View | A derived representation of canonical data/rules for reading, analysis, diagnostics or navigation, with explicit upstream sources. Computation and displayed relationships confer no rule authority. |
| Lore | World truth, history, culture, resident interpretation and fictional causality. Gameplay predicates belong to the relevant mechanic/system, even when fiction explains them. |
| Design Research | Investigation of observed behavior, mechanisms, genre forces, comparable implementations, transfer conditions and consequences, with explicit evidence and uncertainty. |

Vision -> Core Experience -> Features -> Systems -> Mechanics -> Content -> Data is a decomposition view, not a mandatory folder tree or a one-parent hierarchy. Systems can support several features. An entity can participate through several interfaces. Data is owned configuration, not necessarily a new page type.

Overview, rationale, presentation and player-experience synthesis are valid reading surfaces. Keep their unique explanations, examples and voice. One primary responsibility does not mean one file for every conceptual layer.

Current `type` values include historical labels such as `mechanic` on large systems. Classify from meaning and ownership before proposing a metadata change. Do not bulk relabel the corpus to match this vocabulary.

## Authority, not representation

Matrix, Table, Map, Graph and Dashboard describe representation shape, not authority class. Such a document may be a View, Registry/data model, System owner or Feature projection according to what it asserts. Do not create a `matrix` authority type. A document that defines a canonical formula, topology, rule or resolver is not a View, however it is named or rendered.

A Registry must not hide universal runtime behavior, lifecycle, predicates, state transitions, resolver order, general gameplay formulas, capability law or shared gameplay prohibitions inside its records. During an authorized refactor, preserve structured records, identify the correct System/Mechanic owner, move the normative rule there and link to it from the Registry. This is a classification contract, not permission to migrate current registries now.

A View can use Dataview, DataviewJS, an Obsidian Base, JSON Canvas, generated Markdown or another projection. Show its upstream canonical sources to the reader; a calculated comparison is not the owner of the formula it applies. For newly classified Markdown views use `type: view` and `upstream_sources`, a list of quoted source wikilinks; active views require a nonempty list. Optional `view_kind` and explicit semantic parameters describe the projection. View notes never declare `owns` or `canonical_id`. Source validity and authority still require reading, not merely a successful query or validator. Existing documents are not reclassified by filename or renderer. See [obsidian-workflow.md](obsidian-workflow.md) for reusable interactive views.

For architecture work, trace the player promise to use cases, owning states, transitions, interfaces and content/configuration. Find absent responsibility, copied rules, circular state authority and features with no playable completion or failure path. A dependency cycle is not automatically a design error; competing writers to the same state are.

Read [feature-contract.md](feature-contract.md) for a feature, [canon-ownership.md](canon-ownership.md) for authority, and [design-research.md](design-research.md) when the proposed architecture depends on an untested causal explanation.
