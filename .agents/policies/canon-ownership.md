# Canon and ownership

Current game canon is established by active owners in `01_` through `08_`. `00_Index.md` and `00_Routes.md` are generated navigation. `09_Project_Management` holds work, risks and placement decisions, not gameplay resolution. `10_Reference`, fiction drafts, `docs`, proposals and harness files provide context, never current-rule authority merely because their status is active.

Start at the index and relevant route; open the selected owner and dependencies needed for the question. Expand through incoming links, referenced entities or targeted search when evidence demands it. Harness/tooling tasks can inspect their own files directly. Exclusions narrow the requested sources.

Use the latest explicit user decision as authority to change canon. Until integrated, distinguish that decision from what the current owner says. A risk marked resolved is not evidence that its gameplay owner implements the decision. Cite current claims to exact active owners; report incompatible owners as `SOURCE_CONFLICT` and an absent rule home as `MISSING_OWNER`, with paths and the practical consequence.

One rule or stable data field has one source. `index_route: owner` is navigational metadata, not proof that a whole page owns every rule it mentions. Optional `canonical_id` identifies a rule owner and `owns` declares its rule keys; duplicate active IDs/keys are errors. Legacy route owners without these optional declarations remain usable and still require semantic review.

Entity-owned properties stay on the entity. A registry can own atomic or relational records, or display entity records. Derived Dataview, Bases and Canvas surfaces read those sources. They do not store parallel authoritative records. Lore may explain a mechanic's cause, but a resident institution does not thereby resolve its reward, eligibility or lifecycle.

Keep names consistent with `01_Core_Vision/Glossary.md`. Separate player-facing names from stable machine keys. Do not introduce an alias that quietly changes the concept.

Document lifecycle and field requirements are defined in [validation.md](validation.md) and its machine-readable model. A non-active note can be referenced as history or proposal, but must not enter active routes or be declared as an active system dependency.
