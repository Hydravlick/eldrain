---
name: eldraine-gdd-author
description: Use when an approved Eldraine decision must be placed or revised in one active canonical GDD owner.
---

# Eldraine GDD Author

## Principle

Put an approved decision in its one active owner; preserve links and avoid duplicate rules.

## Current Sources

Read `00_Index.md`, the proposed active owner, and only its direct active dependencies. Read `09_Project_Management/Architecture_MVP.md` only when the requested placement still needs its current ownership route.

## Workflow

1. Confirm the decision is approved and identify the owner.
2. Choose extension, registry entry, or a focused active page; prefer extension when it retains one owner.
3. Record any unresolved assumption instead of deciding it in prose.
4. When asked to edit, match the owner’s current structure, add direct links, and update direct consumers.

## Output

Before editing, state location, extend-or-create choice, assumptions, and affected files. After editing, state the canon placed, remaining assumptions, links added, and required validation.

## Stop

If the decision is unapproved, return `APPROVAL_REQUIRED`. If ownership is missing or conflicted, return `MISSING_OWNER` or `SOURCE_CONFLICT` with exact paths. For a shared ownership decision, return `BLOCKED: ARCHITECTURE_DECISION_REQUIRED`; do not invoke another skill automatically.
