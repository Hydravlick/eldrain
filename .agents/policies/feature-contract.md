# Feature contract

A Feature describes a complete capability or experience the player can use. It owns integration intent and acceptance coverage. Universal rules, formulas, eligibility predicates and state resolution remain with system/mechanic owners. A Feature links to those contracts; its high-level flow must not become a competing resolver.

Read alongside [design-architecture.md](design-architecture.md) when a feature is proposed or revised. This contract prepares Prompt 2 without selecting a folder, moving existing pages or declaring the Feature corpus complete.

Use the amount of prose the capability needs to explain:

- player promise and purpose;
- scope and use cases, including success, cancellation, failure and return;
- high-level flow with the system owner responsible at each boundary;
- state/interface dependencies and integration gaps;
- configuration/data sources and authored content;
- UX surfaces, signals and relevant empty/unavailable states;
- observable acceptance scenarios and remaining playtest questions;
- production disciplines involved, such as gameplay, UX, audio, animation, narrative, level design and QA.

These are coverage questions, not required headings. Read [editorial-quality.md](editorial-quality.md) when writing the page.

## Properties ready for future pages

`type: feature` is supported now. A feature uses ordinary `status` and `system`, a unique `feature_id`, and a nonempty `system_owners` list of quoted wikilinks to active routable system/mechanic owners. Optional `data_sources` and `ux_surfaces` lists also use existing note links. `production_disciplines` is a list of text labels. `validation` may link to acceptance or playtest notes; a test does not certify the completeness of their prose.

A Feature cannot declare `owns` or `canonical_id` for underlying rules. `feature_id` identifies the capability. `index_route: owner` can make it discoverable as the owner of the feature description; this routing flag does not grant gameplay authority. Route metadata follows the normal route contract.

The validator checks these fields wherever a future feature is placed in an approved gameplay domain. Extending the domain map is a separate, explicit placement change in Prompt 2. Draft/deferred features may be incomplete, but declared links must resolve and declared system owners must be valid; only active features require the complete machine-checkable contract.
