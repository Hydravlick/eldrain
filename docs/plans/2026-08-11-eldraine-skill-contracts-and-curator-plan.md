# Eldraine Skill Contracts and Vault Curator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:test-driven-development and superpowers:writing-skills. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add precise mechanic and prose-safety contracts to the current Eldraine skill system without changing active canon.

**Architecture:** Existing specialist skills retain ownership and receive small, domain-specific contract sections. A new explicit-only `eldraine-vault-curator` orchestrates owner-first audits and calls two standard-library Python tools: a detect-only prose auditor and a structural rewrite validator.

**Tech Stack:** Markdown skills, YAML UI metadata, Python 3 standard library, `unittest`.

## Global Constraints

- No external repository installation or network dependency.
- No active-canon edits.
- No automatic rewrite.
- Preserve current dirty-worktree changes outside the files listed below.
- Do not commit while unrelated staged changes remain in the index.

---

### Task 1: Contract tests

**Files:**
- Create: `tools/test_eldraine_skill_contracts.py`
- Create: `tools/test_vault_curator.py`

- [ ] Write tests for the new curator metadata, workflow, protected invariants, detector output, and rewrite validation.
- [ ] Write tests for the required additions to architect, GDD author, balance, crash-test, player-experience, lorekeeper, narrative-impact, and location-designer.
- [ ] Run both test modules and confirm failure because the new contracts and tools are absent.

### Task 2: Vault curator

**Files:**
- Create: `.agents/skills/eldraine-vault-curator/SKILL.md`
- Create: `.agents/skills/eldraine-vault-curator/agents/openai.yaml`
- Create: `.agents/skills/eldraine-vault-curator/scripts/audit_prose.py`
- Create: `.agents/skills/eldraine-vault-curator/scripts/validate_rewrite.py`

- [ ] Initialize the skill with the bundled skill-creator scaffolder.
- [ ] Implement the minimal owner-first detect/repair/approval workflow.
- [ ] Implement protected-region-aware Russian prose candidate detection.
- [ ] Implement structural rewrite validation.
- [ ] Run curator tests until green.

### Task 3: Existing specialist contracts

**Files:**
- Modify: `.agents/skills/eldraine-system-architect/SKILL.md`
- Modify: `.agents/skills/eldraine-gdd-author/SKILL.md`
- Modify: `.agents/skills/eldraine-balance-modeler/SKILL.md`
- Modify: `.agents/skills/eldraine-crash-test/SKILL.md`
- Modify: `.agents/skills/eldraine-player-experience/SKILL.md`
- Modify: `.agents/skills/eldraine-lorekeeper/SKILL.md`
- Modify: `.agents/skills/eldraine-narrative-impact/SKILL.md`
- Modify: `.agents/skills/eldraine-location-designer/SKILL.md`
- Modify: `AGENTS.md`

- [ ] Add only the contract owned by each specialist.
- [ ] Add the curator to explicit root orchestration with a non-overlapping trigger.
- [ ] Run contract tests until green.

### Task 4: Verification

- [ ] Run the new test modules.
- [ ] Run all existing `tools/test_*.py` tests.
- [ ] Run skill-creator validation for the new skill.
- [ ] Run `python tools/vault_guard.py`.
- [ ] Review `git diff` and confirm no unrelated file was edited.

