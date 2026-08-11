# Eldrain

This project folder contains the active Eldrain corpus and contextual material.

## Reading

1. Start with `00_Index.md` and select the relevant system route page.
2. Resolve the requested subject to its `index_route: owner` page.
3. Open that owner and only its direct dependencies.
4. Exclusion clauses narrow source selection and do not add sources.
5. Use corpus-wide search within `00_Index.md` and `01_` through `09_` only after owner selection, for dependency and consistency checks.

The route pages and `00_Index.md` are generated projections. Do not edit them manually. Outside corpus structural refactor mode, update owner metadata and run `python tools/build_routes.py --write`. During structural refactoring, record stale projections for later regeneration and do not run the route builder unless the user explicitly requests it.

## Canonical Corpus

The current canonical corpus is `00_Index.md` and the `01_` through `09_` directories.

- `00_Index.md` and the generated `00_Routes.md` pages provide navigation.
- Active owner pages under `01_` through `08_` establish current game rules.
- `09_Project_Management` establishes current work, risks, and approved placement; it does not redefine a game rule owned under `01_` through `08_`.

Current-canon claims cite active owners. Select owners and resolve rule conflicts inside this corpus before opening contextual material.

## Contextual Materials

`10_Reference`, `Истории`, `docs`, root-level proposals, media, configuration, runtime folders, and `.agents` serve reference, provenance, instructions, or tooling roles.

Contextual materials may be opened without a separate user request when useful for provenance, reference, or historical understanding. Label their role in the result, then state the adopted model from its active owner. They contribute context; active owners supply current-rule evidence.

## Authority

- Each rule has one canonical owner.
- Owner pages define rules.
- Registries provide structured records.
- Indexes provide routes.
- `09_Project_Management/TODO.md` contains current work.
- `09_Project_Management/Risk_Register.md` contains current risks.
- Conflicting active owners produce `SOURCE_CONFLICT` with exact paths.
- Missing ownership produces `MISSING_OWNER`.

## Changes

1. Place an approved decision in its canonical owner.
2. Update direct consumers and incoming links.
3. Run project-folder validation.
4. Remove the temporary source after successful migration.

## Skill Orchestration

The root agent is the Eldrain orchestrator. It explicitly selects skills from `.agents/skills/` when their condition matches; this is intentional orchestration, not passive description matching.

For GDD, lore, vault, prose, and other documentation work, operate in the
current checkout while preserving unrelated user changes. Use owner-scoped
review and after-edit structural validation; do not require a secondary
repository checkout or a code-oriented test-first cycle.

1. For a broad, cross-owner, ownership, lifecycle, uncertainty, or architecture question, start with `eldraine-system-architect`.
2. For a bounded question, select the matching specialist directly:
   - spatial flow, topology, sectors, routes, or production feasibility → `eldraine-location-designer`;
   - approved canonical placement or revision → `eldraine-gdd-author`;
   - lore, factions, terminology, metaphysics, or fiction-to-mechanics compatibility → `eldraine-lorekeeper`;
   - exploits, incentive abuse, dominance, or safe farming → `eldraine-crash-test`;
   - formulas, thresholds, probabilities, rewards, or numeric corridors → `eldraine-balance-modeler`;
   - equipment, loadouts, replacement, or progression dominance → `eldraine-gear-progression`;
   - lived sequence, feedback, readability, or failure comprehension → `eldraine-player-experience`;
   - motivation, adaptation, churn, or profile conflict → `eldraine-player-lens`;
   - story consequence, world-state change, reveal, or chronology → `eldraine-narrative-impact`.
   - note administration, duplicated authority, AI-shaped prose, owner-page readability, stale proposals, or structural vault cleanup → `eldraine-vault-curator`.
3. A selected skill may request one bounded specialist handoff when that evidence can change its verdict. The request must name the target skill, active owner paths, exact question, and expected return artifact.
4. The orchestrator invokes the requested specialist, returns its evidence to the caller, and does not fan out to unrelated skills. A handoff never transfers final ownership of the original verdict.
5. If the request has no subject, owner, or approved decision, ask for the missing input or return `MISSING_OWNER`, `SOURCE_CONFLICT`, or `APPROVAL_REQUIRED`; do not manufacture scope.

### Handoff Contract

```text
HANDOFF: <skill-name>
Affected owners: <exact active paths>
Question: <one bounded question>
Expected return: <evidence, table, constraint, or verdict>
```

Skills remain explicit-only in their metadata. The root agent performs the explicit selection described above; users may also invoke a skill directly with `$skill-name`.

### Corpus Structural Refactor

When the user requests repository cleanup, responsibility separation, AI-slop removal, lore/mechanic/system separation, or canonical corpus refactoring, select `eldraine-vault-curator` in structural refactor mode.

The Corpus Structural Refactor rule overrides the general broad/cross-owner routing rule above. Do not start `eldraine-system-architect` merely because the refactor spans many owners.

The request itself authorizes sequential edits throughout the named scope. Work owner by owner and finish each owner before advancing:

`read -> classify responsibility -> move/integrate -> rewrite -> remove duplication -> manually verify -> next owner`

Structural refactoring must conserve semantic coverage, not only canonical
rule authority.

Before removing or substantially compressing a semantic block, the curator
must prove one of:

- the unique meaning was moved;
- an exact active destination already preserves it;
- it is explicitly superseded;
- it is a true duplicate with no independent explanatory, experiential,
  presentation, rationale, lore, example, or uncertainty value.

Overview, design rationale, presentation, player-experience synthesis and
lore synthesis are valid responsibilities. Do not collapse them into link
hubs merely because their underlying systems have separate normative owners.

Destination edits happen before source deletion. The current owner is not
complete until the curator can account for the post-edit location of every
valuable semantic block.

A large deletion count or shorter file is not evidence of successful
refactoring.

Do not replace this workflow with a corpus-wide preliminary audit, scanner-generated candidate lists, migration manifests, a plan-only response, one-line cosmetic repairs, or per-file approval requests.

The curator directly relocates and integrates established material during structural refactoring.

Use `eldraine-gdd-author` only when the destination requires substantial new canonical writing rather than relocation or editing of established meaning, or when a genuinely new page must be authored beyond the curator's structural repair. Do not invoke `eldraine-gdd-author` for ordinary `MOVE`, `MERGE`, `LINK`, or `DELETE_DUPLICATE` operations. Make any necessary handoff during the current owner's repair; do not postpone it into a later project phase.

Use `eldraine-system-architect` only when the documentation exposes a real design contradiction or missing runtime owner. Poor placement by itself is an editorial problem.

The normal result of structural refactoring is changed canonical Markdown, not an audit document.

## Verification

For ordinary project work, run `python3 tools/vault_guard.py` before completion.

Exception: corpus structural refactor mode uses manual semantic verification owner by owner. Do not run Python validation or regenerate projections unless the user explicitly requests it. Report pending generated projections at the end.
