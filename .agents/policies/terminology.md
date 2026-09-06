# World / Player / Schema language contract

This is harness guidance for terminology review, not game canon or authorization to migrate the corpus. It complements [canon-ownership.md](canon-ownership.md) without changing rule owners, page roles or schema. An internal identifier does not become a world term merely because it exists in the GDD.

## Vocabulary layers

| Layer | Purpose and grounding |
|---|---|
| WORLD VOCABULARY | Words that exist inside the fiction and can plausibly be spoken by a resident, craftsperson, doctor, Хранитель, institution, religious group or seeker. Ground them in an observable phenomenon, thing, work, place, institution or historical practice. They need not be scientifically accurate. |
| PLAYER / MECHANICAL VOCABULARY | Concepts players need to understand clearly: UI labels, gameplay states and readable mechanical categories. They need not exist in the fiction. |
| SCHEMA / DEVELOPER VOCABULARY | Precise internal GDD/runtime language: IDs, enum names, resolver terms, states, leases, runtime objects and formulas. It need not sound elegant, use world vocabulary or have a diegetic explanation. |

Classify usage in context; a word may serve more than one layer when each use is supported. Names such as `SessionRuntime`, `DissonanceLoad`, `RealityBuffer` and `SyncLease` do not establish fictional entities or explanations by themselves.

Ask: **“Кто использует это слово?” / “Who uses this word?”** If only the GDD author or schema uses it, do not automatically carry it into Lore or player-facing prose. For a proposed world term, identify a plausible speaker and a reason they would use it. This is a design/editorial question, not mandatory `spoken_by` metadata.

One phenomenon may have an internal key, a common city term, a Хранитель term, an institute's term, a religious name and local slang. Distinct names can express institutional disagreement. Create variants only when supported by history, function or institutional conflict; do not generate a full set or impose one universal spoken name.

## What canon knows

| Claim | Authority |
|---|---|
| OBSERVED RULE | What reliably happens, under the relevant conditions. State the observable operation and consequence precisely at its existing owner. |
| IN-WORLD THEORY | Why inhabitants think it happens. Attribute institutional models, resident beliefs, historical explanations and speculation to their sources; institutions may disagree. |
| AUTHORIAL METAPHYSICS | An accepted world truth about the ultimate nature of reality. Establish it only when gameplay/lore requires that knowledge and an explicit author decision or current owner supports it. |

Canon should state observable rules reliably without automatically endorsing a final theory of reality. For illustration only, “Якорь уничтожает сохранённую память, после чего город получает ещё время” describes an observable sequence that could be canon; this example establishes no Eldrain rule and supplies no final explanation.

Distinguish observed fact, institutional model, resident belief, historical explanation, speculation and accepted world truth. Ask who knows the claim, what they observe and what they infer. An attributed historical explanation is not automatically established history. “Дома Пробы называют это X” does not establish “the universe objectively works through X.” Scientific vocabulary is valid when its speaker, evidence and level of authority support it; neither a technical name nor confident narration makes a theory true.

## Backend and presentation

Not every technical process needs a lore equivalent. Matchmaking, ping, regional shard, reconnect, runtime, replication and session state can remain internal. Do not give a backend concept a magical world name solely for immersion. Use diegetic UI where it improves play; it is not a required justification for software architecture.

## Before changing a term

Identify the use's layer, speaker/audience, claim authority and current owner, then classify the proposed action using evidence from the current corpus and accepted author decisions:

| Action | When to use |
|---|---|
| KEEP | The current term performs its function. |
| LAYER | Retain the term internally/in design while removing or lowering its world/player-facing status. |
| RENAME | The current term is clearly obsolete and its replacement is already confirmed by the current corpus. |
| DEPRECATE | The old alias is useful only for search/history. |
| REVIEW | A poor name exposes a possible problem in the mechanic or lore itself; investigate before renaming. |
| AUTHOR_DECISION | Several substantively different options remain and cannot be chosen editorially. |

This is a working procedure for subsequent terminology passes, not mandatory frontmatter or permission for an unrequested architecture audit. Classification alone does not authorize corpus edits. Preserve Glossary discipline and existing ownership; resolve actual source conflicts under [canon-ownership.md](canon-ownership.md).

Internal IDs are stable by default. A player/world terminology refactor does not require renaming machine keys: `reality_burn` may remain internal even if nobody in the world says “Reality Burn.” Change an ID only for a concrete benefit within authorized scope, after checking its consumers and migration cost.

Terminology quality requires semantic review. Do not add banned-term/word tests, phrase-lock assertions, regex checks for scientific words, mandatory `spoken_by`, vocabulary-layer counts or other schema requirements to enforce this policy. Mechanical validators do not decide lore.
