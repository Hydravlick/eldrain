# Eldrain

This project folder contains the current Eldrain GDD canon.

## Reading

1. Start with `00_Index.md`.
2. Resolve the requested subject to its active canonical owner.
3. Open that owner and only its direct dependencies.
4. Exclusion clauses narrow source selection and do not add sources.
5. Use project-wide search only after owner selection, for dependency and consistency checks.
6. Treat an exclusion clause as a source filter, never as an additional search target.

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

## Scope

- Only files currently present in this project folder may supply current canon.
- Do not inspect `.git`, sibling folders, deleted files, backups, caches, or external archives.
- If a requested historical source is absent, return `HISTORICAL_SOURCE_NOT_IN_PROJECT` and ask the user to provide it.

## Verification

Run `python3 tools/vault_guard.py` before completing project work.
