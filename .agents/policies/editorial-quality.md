# Human GDD prose

Stabilize meaning before polishing language. Write the accepted state directly, with actors, conditions, actions and consequences. In design-facing prose, move from concrete play to abstraction:

concrete situation -> what the player sees -> what they do -> what changes -> the next choice -> design explanation and supporting systems.

If a design statement cannot quickly be connected to an observable gameplay situation, make it more concrete. This is an order of explanation, not a required set of headings. Match the page's job and Eldrain's existing voice.

## Voice by page type

| Page | Voice and order |
|---|---|
| Vision / Core Concept | Simple, clear language, concrete images and gameplay facts, with little internal terminology. Explain direction and atmosphere without turning the page into an advertising pitch. |
| Feature | A game designer explaining playable experience: situation, actions, concrete options, consequences and characteristic moments first; supporting owners, UX, data and validation afterward. The reader should be able to imagine play. See [feature-contract.md](feature-contract.md). |
| System | Technical precision is expected. Use state, predicate, resolver, contract, interface and schema where they add necessary precision. When the System directly affects players, begin with a short plain-language explanation of its observable role before the detailed model. |
| Mechanic | A short, exact account of one action or rule, including the conditions and consequences needed to use it. Keep its scope proportional; a simple mechanic does not need a Feature/System essay. |
| Registry | Data and schema with minimal explanatory prose. Do not add atmosphere to enliven records. |
| Lore | Preserve the world's voice, material detail, culture and fictional causality. Keep design jargon and System specification out of the account. |
| Project Management | State the action or open question, supporting evidence and done condition. Link the canonical gameplay owner when needed; do not retell its rule. |

## Plain design language

**Direct statement.** State the point directly. Avoid routinely building sentences around “не X, а Y” when an ordinary assertion conveys the same meaning. A real contrast can clarify a distinction; this is judgment about a recurring rhetorical habit, not a regex ban.

**Concrete before abstract.** Terms such as “осмысленный”, “динамика”, “давление”, “ритм”, “пространство решений”, “цена выбора”, “напряжение”, “вовлечённость”, “агентность”, “контригра” and “meaningful choice” are useful only when nearby actions, conditions or consequences make their meaning clear. The term itself is not an explanation.

**Causes before feelings.** Before writing “игрок должен чувствовать X”, describe what the player knows and does not know, what they can lose, how much time they have, which signals they see and which options remain. Name an emotional target afterward if it adds useful design information.

**No synthetic importance.** Remove metaphors, antitheses, solemn phrasing, advertising cadence and philosophical generalizations that add emphasis without design information. Do not add atmosphere for its own sake. Preserve material detail and intentional voice when they explain something specific.

**Actions over nominalizations.** Prefer actor + action + condition + consequence to abstract nouns. “Система поддерживает устойчивое пространство решений” leaves the play unexplained. “После потери маршрута игрок всё ещё может отступить через известный проход или рискнуть новым путём” identifies actions and a condition. This illustrates a level of concreteness, not a rule to copy into canon.

**No repeated architecture prose.** Harness rules belong in the harness. Do not repeat generic statements on each Feature about formulas remaining with owners, what `specified` or `untested` means, or how TODO/validation architecture works. Keep only explanations and links needed to understand the particular page. The same applies to metadata: body prose need not mechanically repeat frontmatter. Preserve fields needed by queries/views/validation/identity; metadata cleanup requires checking affected Base and Dataview consumers.

## Setting specificity

Feature and Core prose should explain Eldrain through specifics supported by current owners/lore: a particular Пешка and its current condition, physical cargo, a Термос, masks/filters, batteries, the Стол, the Порог, city addresses, an item's provenance, a sector's condition, or known and unknown parts of a route. Select details relevant to the situation; this is neither a quota nor a checklist of objects to mention.

Verify the relationship and consequence as well as the named thing. A canonical filter does not by itself establish a new filter effect or route interaction. Do not invent canon for a vivid example. If an example needs a new design decision, keep that decision explicitly unresolved until accepted; use a supported situation for the current prose.

## Editorial Pass

After the Design Correctness Pass, perform an Editorial Pass:

1. Meaning: identify what each paragraph adds, including explanation, rationale, sensory evidence or uncertainty.
2. Human Reading: for design-facing pages, follow concrete play before design abstraction: situation, information, action, consequence and next choice. Make the experience understandable without the vault's internal architecture.
3. Concrete Language: resolve unexplained abstract nouns into actions, conditions or observable consequences. Check gameplay causes before any “player should feel” claim.
4. Voice: apply the page-specific voice above. Keep deliberate Eldrain phrasing and material detail; remove generated cadence, announcement sentences, forced contrasts, slogan-like prose and promotional filler.
5. Compression: remove repeated architecture boilerplate and sentences that add no meaning. Keep examples, rationale and synthesis that teach something distinct; do not force identical headings across pages.
6. Technical Precision: place technical detail at the appropriate layer, then reread conditions, negations, quantities, order, interfaces and failure behavior after improving the prose.

Avoid stock openings such as "Система обеспечивает...", "Данный механизм позволяет..." and "Игрок получает возможность..." when a direct verb says it better. This is editorial judgment, not a banned-word detector. Do not impose a quota of atmosphere or a repeated document template.

On design-facing pages, a reader should understand play before implementation-facing detail. Systems and Registries retain the technical precision their roles require. Keep stable fields at their existing owner and link other owners. Technical implementation choices belong in tooling/implementation material unless they change observable behavior.

Human prose is the standard for every writing skill. Lorekeeper specializes in fictional truth and speaking voices; it is not a mandatory gate for readable system text. Mechanical checks cannot prove that a rewrite preserves meaning or reads well. Do not add stylistic regex tests, banned-word checks, heading requirements, example counts or phrase-lock assertions. Change tests only for a real metadata/schema contract change; editorial quality requires reading.
