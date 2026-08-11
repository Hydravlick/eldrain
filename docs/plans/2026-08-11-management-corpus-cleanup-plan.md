# Management Corpus Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove completed management clutter while retaining only active risks and unfinished actions in the project-management surface.

**Architecture:** Enforce the cleanup policy with a small standard-library regression test. Remove only evidence-backed completed rows and checkboxes; retain whole documents that are still active, have pending work, or are referenced by active pages. Git history, rather than a new archive, remains recovery provenance.

**Tech Stack:** Markdown corpus, Python standard library `unittest`, `rg`, `tools/build_routes.py`, `tools/vault_guard.py`.

## Global Constraints

- Delete rather than archive completed material.
- A risk register contains only `in_progress` or `deferred` rows; retain Risk IDs without renumbering.
- An active project plan contains no checked-off task; its remaining tasks remain unchanged.
- Do not delete a whole document unless all retained rules have canonical owners and it has no incoming live links.
- Do not modify `00_Index.md` or generated routes directly.
- Do not commit automatically: the worktree has unrelated user changes.

### Task 1: Add the hygiene regression test

**Files:**

- Create: `tools/test_management_hygiene.py`
- Read: `09_Project_Management/Risk_Register.md`, `09_Project_Management/TODO.md`, `09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23.md`

**Interfaces:**

- Consumes: Markdown table rows beginning with `| R` and YAML frontmatter in active project-plan files.
- Produces: `python tools/test_management_hygiene.py`, which exits non-zero for a closed risk in the active register or a checked-off task in an active plan.

- [ ] **Step 1: Write the failing test**

```python
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANAGEMENT = ROOT / "09_Project_Management"


class ManagementHygieneTests(unittest.TestCase):
    def test_risk_register_has_only_active_statuses(self) -> None:
        rows = [
            line for line in (MANAGEMENT / "Risk_Register.md").read_text(encoding="utf-8").splitlines()
            if line.startswith("| R")
        ]
        statuses = {line.split("|")[4].strip() for line in rows}
        self.assertTrue(statuses <= {"in_progress", "deferred"}, statuses)

    def test_active_plans_have_no_completed_checkbox(self) -> None:
        for path in MANAGEMENT.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            frontmatter = text.split("---", 2)[1] if text.startswith("---") else ""
            is_active_plan = (
                "status: active" in frontmatter
                and ("type: project_plan" in frontmatter or "type: implementation_plan" in frontmatter)
            )
            if is_active_plan:
                self.assertNotRegex(text, r"(?m)^- \[[xX]\]", path.name)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and observe the expected failure**

Run: `python tools/test_management_hygiene.py`

Expected: failure listing `fixed` as a Risk Register status and `Worldbuilding_Refactor_Roadmap_2026-07-23.md` as an active plan containing checked-off steps.

### Task 2: Remove closed risks from the active register

**Files:**

- Modify: `09_Project_Management/Risk_Register.md`
- Test: `tools/test_management_hygiene.py::ManagementHygieneTests.test_risk_register_has_only_active_statuses`

**Interfaces:**

- Consumes: the existing table schema `ID | failure | resolution | status | owners`.
- Produces: a register of the 18 currently active or deferred risks, with their existing IDs, wording, owners, and statuses preserved.

- [ ] **Step 1: Delete every row whose status cell is exactly `fixed`**

Remove the 40 table rows currently marked `fixed`. Do not edit the 12 `in_progress` rows or the 6 deferred rows.

- [ ] **Step 2: Preserve the section boundaries and deferred list**

Leave `## Решения MVP`, `## Оставить На Потом`, all `in_progress` rows, and R14/R17/R18/R19/R20/R22/R49 unchanged. Do not renumber the remaining IDs.

- [ ] **Step 3: Run the targeted test**

Run: `python tools/test_management_hygiene.py ManagementHygieneTests.test_risk_register_has_only_active_statuses`

Expected: PASS.

### Task 3: Remove completed checkboxes from active roadmaps

**Files:**

- Modify: `09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23.md`
- Test: `tools/test_management_hygiene.py::ManagementHygieneTests.test_active_plans_have_no_completed_checkbox`

**Interfaces:**

- Consumes: completed steps under the roadmap's first source-ingestion task.
- Produces: an active plan containing only unfinished work and its still-current acceptance criteria.

- [ ] **Step 1: Delete exactly these completed lines**

```markdown
- [x] Перенести приложенный текст без исправлений.
- [x] Отметить, что последняя фраза оборвана в самом источнике.
```

- [ ] **Step 2: Keep the remaining source constraint**

Retain the unchecked instruction about future clarifications; it still constrains future work.

- [ ] **Step 3: Run the targeted test**

Run: `python tools/test_management_hygiene.py ManagementHygieneTests.test_active_plans_have_no_completed_checkbox`

Expected: PASS.

### Task 4: Prove that no whole document qualifies for deletion yet

**Files:**

- Read: `09_Project_Management/Canonical_Refactor_Migration_Map_2026-07-23.md`, `09_Project_Management/Lore_Gameplay_Boundary_Refactor_Plan_2026-07-23.md`, `09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23.md`, `09_Project_Management/Refactor_Unresolved_Registry_2026-07-23.md`

**Interfaces:**

- Consumes: document statuses, unchecked steps, and inbound link results.
- Produces: an explicit `KEEP` decision for each document that still owns a current plan or unresolved decision.

- [ ] **Step 1: Re-run the candidate evidence search**

Run: `rg -n -i "status: active|\[ \]|pending|APPROVED / PENDING_MIGRATION" 09_Project_Management/Canonical_Refactor_Migration_Map_2026-07-23.md 09_Project_Management/Lore_Gameplay_Boundary_Refactor_Plan_2026-07-23.md 09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23.md 09_Project_Management/Refactor_Unresolved_Registry_2026-07-23.md`

Expected: evidence that all four documents retain live work, pending migration, or unresolved decisions.

- [ ] **Step 2: Record no document deletion for this pass**

Do not delete any of those four documents. Their removal would violate the approved migration-and-link criterion.

### Task 5: Validate and hand off to the gameplay refactor plan

**Files:**

- Verify: `tools/test_management_hygiene.py`, `09_Project_Management/Risk_Register.md`, `09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23.md`
- Modify next: `docs/plans/2026-08-11-core-loop-and-pawn-errands-refactor-plan.md`

- [ ] **Step 1: Run the complete hygiene test**

Run: `python tools/test_management_hygiene.py`

Expected: PASS.

- [ ] **Step 2: Check removal scope**

Run: `git diff --check` and `git diff -- 09_Project_Management/Risk_Register.md 09_Project_Management/Worldbuilding_Refactor_Roadmap_2026-07-23.md tools/test_management_hygiene.py`

Expected: only the 40 closed risks, the two completed roadmap steps, and the new hygiene test.

- [ ] **Step 3: Run corpus validation**

Run: `python tools/vault_guard.py`

Expected: no violation attributable to the removals; report the known pre-existing baseline separately.

- [ ] **Step 4: Refresh the gameplay refactor plan**

Update `docs/plans/2026-08-11-core-loop-and-pawn-errands-refactor-plan.md` with a concise precondition stating that management cleanup is complete and R65 remains the relevant active guardrail for Pawn errands.
