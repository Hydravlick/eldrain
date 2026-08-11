---
name: eldraine-gdd-author
description: Use when turning Eldraine notes, references, dictated ideas, decisions, or revisions into canonical GDD, especially when a mechanically correct page has become dry, generic, tonally flat, or detached from its intended atmosphere.
---

# Eldraine GDD Author

## Principle

Integrate decisions into the living vault instead of producing isolated design prose. Find the canonical home before creating a file.


## Active Canon Language

Describe the accepted target state affirmatively: name the active entities, rules, scope, and consequences.

Historical context belongs outside active rule statements. When it helps explain provenance or a reference, label it as contextual material and return the adopted model in the canonical result.

## Responsibility Boundary

Own canonical placement, document responsibility, integration, and prose after the design decision is known. Do not resolve disputed cross-system ownership, certainty allocation, genre compatibility, or scaling philosophy through polished writing. Use `eldraine-system-architect` first when those questions remain open, then encode the approved contract without duplicating its audit method in GDD.

## Locate the Home

Read `09_Project_Management/Architecture_MVP.md`, `00_Index.md`, and the relevant system files.

Choose among:

1. Extend an existing canonical document.
2. Add an entry to an existing registry or matrix.
3. Create a new focused document inside one of the nine active blocks.
4. Keep the material as a proposal when core decisions remain unresolved.

Prefer extension over duplication. Place active design in an active owner, registry, or new focused document; contextual material retains provenance while the adopted rule lives in its active owner.

## Resolve Before Writing

Extract:

- accepted decisions;
- explicit author constraints;
- missing values;
- contradictions;
- assumptions required to make the text coherent.

Do not silently choose among materially different designs. Ask one blocking question when necessary; otherwise label a reversible assumption clearly.

## Document Contract

Match nearby canonical files. Include only relevant sections:

- YAML frontmatter with `type`, `status`, `system`, and `tags`;
- concise concept and player-facing purpose;
- rules and state transitions;
- gameplay loop or interaction sequence;
- links to dependent systems;
- structured fields, formulas, registry keys, or tables where needed;
- diegetic and UI feedback;
- failure cases and edge conditions;
- risks, open measurements, or author decisions.

Use current root-relative Obsidian links, for example:

`[[08_World_Generation/Generation/08_Gate_Check|Gate Check]]`

Validate target paths and headings before adding links.

For every Markdown table, apply `eldraine-vault-curator`'s **Render-Safe Tables** contract: one short Obsidian link is permitted only with an escaped `\|` alias separator; place multiple links outside the table.

## Executable Mechanic Contract

Use this section set only when the page owns a mechanic that must be implemented or tested:

- **Player promise:** the concrete experience or competence the mechanic exists to create.
- **Player loop:** player action -> system response -> feedback -> next decision.
- **Rule state machine:** precondition, trigger, ordered resolution, and postcondition.
- **Interfaces:** inputs, outputs, canonical owners, and direct consumers.
- **Formulas and tuning:** link the owning numeric source; do not duplicate values.
- **Edge cases:** exact condition and exact outcome.
- **Acceptance criteria:** observable `GIVEN / WHEN / THEN` results for core rules.

### Behavior versus implementation

The GDD owns observable behavior, player decisions, state transitions, interfaces, feedback, and failure resolution. Code architecture, engine nodes, storage layout, signal buses, and other technical choices belong in implementation documentation or an ADR. Do not remove a design interface merely because its implementation is not yet chosen.

## Four-Pass Drafting

1. **Function pass:** state what decision, rule, or canon claim the section must carry.
2. **Rule pass:** replace atmosphere that hides actors, conditions, order, values, or outcomes with explicit terms.
3. **Voice pass:** restore only the approved atmosphere or character voice that carries experience, inference, mystery, or identity.
4. **Brevity pass:** cut repeated conclusions, decorative contrasts, and examples that add no new case.

Do not run the Voice pass before the rule is stable. Do not make a lore page sound like a system spec or a system page sound like promotional lore.

## Навигация и контекст

Для обычной GDD-задачи читать `00_Index.md`, `09_Project_Management/Architecture_MVP.md`, целевую каноническую страницу и её прямые зависимости. Следовать границе active corpus из `AGENTS.md`.

Контекстный материал можно открывать для референса, исходного намерения или вопроса автору. Помечать его роль в результате; принятое правило и его доказательство брать из active owner.

## Ответственность, навигация и Dataview

Before writing, assign one responsibility to each affected file:

- semantic index — статические wikilinks с кратким назначением и условием чтения;
- universal system — shared rules and state transitions;
- entity page — identity, in-world context, relations, and the entity's own lived or institutional reality;
- content instance — one sector, anomaly, encounter, or other concrete realization of an existing grammar;
- interface registry — one normalized relation between an entity and a mechanic;
- registry or matrix — stable atomic IDs, records, and structured source data;
- Dataview view — optional filtered presentation of already canonical data.

Use **entity page + interface registry + system owner** for a faction, Hearth, place, culture, NPC, or other entity that participates in several mechanics:

1. The entity page answers what the entity is. It does not own rewards, state transitions, formulas, validators, runtime IDs, or service resolution merely because the mechanic is presented through that entity.
2. Each distinct playable interaction gets one interface record. The record names the entity, player-facing verb/result, the entity's role, one canonical mechanic owner, and an explicit boundary; it links to rules instead of copying them.
3. The system page remains the only normative owner of rules and failure handling.
4. The entity page may render a short linked list of interfaces. This is a projection, not a second contract.
5. Create a separate player-experience page only when the entity has a unique multi-step lived loop. Do not create one file per semantic layer by default.

An entity may be an `ADDRESS`, `ISSUER`, `PROVIDER`, `WITNESS`, `PRESENTER`, or `CONSUMER` of a mechanic. These roles describe participation, not authority. A missing mechanic owner is `MISSING_OWNER`; do not hide it in prose or assign it to the entity as a writing convenience.

`00_Index.md` и другие обзорные страницы используют только статические wikilinks: каждая ссылка объясняет, что открывает страница и когда её читать. Индекс не является полным каталогом и не использует Dataview для навигации.

When a note needs a filtered list already represented in a registry, keep the registry as the **единый источник**; native Dataview may render that list without copying definitions. Give structured records stable frontmatter or inline fields before adding a view.

- Design rules live in prose and registries; Dataview не является источником канона.
- DataviewJS допустим только в явно обозначенной инструментальной заметке или матрице, когда native query недостаточен.
- DataviewJS не превращает заголовки и свободную прозу в данные через ручной разбор; сначала вынести стабильные поля в реестр или frontmatter.
- Make a missing source or empty result visible in the rendered note and verify query syntax, source paths, expected rows, and empty-state behavior after editing.

## Narrative Density Pass

After the rules are correct, preserve the **emotional promise** of a content instance, lore page, encounter, or creature. Universal mechanics and pure Dataview views may remain dry.

Before finalizing narrative content, identify:

- what the player is meant to feel before understanding the rule;
- what the body notices before the explanation arrives;
- which trusted support becomes conditional;
- how a local victory changes the next situation;
- what ordinary life, relationship, or future makes loss matter.

Place atmosphere according to file responsibility:

- universal system — at most one sentence naming the experiential promise;
- content instance — one short spine: almost normal → bodily wrongness → lost support → impossible combination → aftermath or return;
- registry entry — one diegetic line, one sensory tell, and one aftermath or incomplete resident belief;
- Dataview view — presentation only; do not make it a second source of prose.

Use a strict **prose budget**: keep an atmospheric sentence only when it performs at least **two functions** from `reveal a rule / foreshadow a consequence / convey resident interpretation / preserve mystery / connect victory to the next state`. Cut decorative repetition.

When adapting a reference, transfer the produced effect and design question. Rewrite its cause, imagery, terminology, scene structure, and gameplay realization for Eldraine; never carry distinctive phrases or signature creatures into canon.

**REQUIRED SUB-SKILL:** Use `eldraine-player-experience` when the mechanic is complete but the lived sequence is absent.

## Answer Contract

Before editing, report:

- proposed canonical location;
- extend versus create decision;
- unresolved assumptions;
- files affected.

When the user requests only formatting or a draft, return the page without writing. When the user requests implementation, edit only the approved scope and preserve unrelated content.

After editing, summarize:

- what became canon;
- what remains an assumption;
- cross-links added;
- follow-up validation needed.

Use `eldraine-lorekeeper` before writing when canon compatibility is disputed. Use `eldraine-balance-modeler` when numerical fields are unproven. Do not hide design uncertainty behind polished prose.
