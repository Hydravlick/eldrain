# Eldrain

This project folder contains the current Eldrain GDD canon.

## Reading

1. Start with `00_Index.md` and select the relevant system route page.
2. Resolve the requested subject to its `index_route: owner` page.
3. Open that owner and only its direct dependencies.
4. Exclusion clauses narrow source selection and do not add sources.
5. Use project-wide search only after owner selection, for dependency and consistency checks.
6. Treat an exclusion clause as a source filter, never as an additional search target.

The route pages and `00_Index.md` are generated projections. Do not edit them manually; update owner metadata and run `python tools/build_routes.py --write`.

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

## Scope

- Only files currently present in this project folder may supply current canon.
- Do not inspect `.git`, sibling folders, deleted files, backups, caches, or external archives.
- If a requested historical source is absent, return `HISTORICAL_SOURCE_NOT_IN_PROJECT` and ask the user to provide it.

## Verification

Run `python3 tools/vault_guard.py` before completing project work.
