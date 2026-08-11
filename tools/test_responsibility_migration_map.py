from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "docs" / "audits" / "2026-08-11-responsibility-migration-map.md"
MANIFEST = ROOT / "docs" / "audits" / "2026-08-11-canonical-prose-refactor-manifest.md"
PROMPT = ROOT / "docs" / "prompts" / "2026-08-11-terra-responsibility-refactor-microprompt.md"
PASS_A_ROOTS = (
    "01_Core_Vision",
    "02_World_Lore",
    "03_Factions_Societies",
    "04_Player_Entities",
    "05_Combat_Survival",
    "06_Economy_Loot",
    "07_Gear_Inventory",
    "08_World_Generation",
)
PASS_B_ROOTS = (
    "03_Factions_Societies",
    "04_Player_Entities",
    "05_Combat_Survival",
    "06_Economy_Loot",
    "07_Gear_Inventory",
    "08_World_Generation",
)


def route_owners() -> set[str]:
    owners: set[str] = set()
    for root_name in PASS_B_ROOTS:
        for path in (ROOT / root_name).rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            frontmatter = text.split("---", 2)[1] if text.startswith("---") else ""
            if re.search(r"(?m)^index_route:\s*owner\s*$", frontmatter):
                owners.add(path.relative_to(ROOT).as_posix())
    return owners


def pass_a_route_owners() -> set[str]:
    owners: set[str] = set()
    for root_name in PASS_A_ROOTS:
        for path in (ROOT / root_name).rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            frontmatter = text.split("---", 2)[1] if text.startswith("---") else ""
            if re.search(r"(?m)^index_route:\s*owner\s*$", frontmatter):
                owners.add(path.relative_to(ROOT).as_posix())
    return owners


def section(text: str, entry_id: str) -> str:
    match = re.search(
        rf"(?ms)^### {re.escape(entry_id)}\b.*?(?=^### M-|^## Approval gate)",
        text,
    )
    if match is None:
        raise AssertionError(f"Missing detail section {entry_id}")
    return match.group(0)


def detail_sections(text: str) -> dict[str, str]:
    headings = list(re.finditer(r"(?m)^### (M-\d+(?:[a-z])?)\s+—", text))
    ids = [match.group(1) for match in headings]
    if len(ids) != len(set(ids)):
        duplicates = sorted(entry_id for entry_id in set(ids) if ids.count(entry_id) > 1)
        raise AssertionError(f"Duplicate detail sections: {duplicates}")
    sections: dict[str, str] = {}
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else text.index("## Approval gate", match.end())
        sections[match.group(1)] = text[match.start():end]
    return sections


def expand_detail_ref(detail_ref: str) -> list[str]:
    resolved: list[str] = []
    for item in (part.strip() for part in detail_ref.split(",")):
        if not item:
            raise AssertionError(f"Empty item in detail_ref {detail_ref!r}")
        if ".." not in item:
            resolved.append(item)
            continue
        start, end = item.split("..", 1)
        first = re.fullmatch(r"(M-\d+)([a-z])", start)
        last = re.fullmatch(r"(M-\d+)([a-z])", end)
        if first is None or last is None or first.group(1) != last.group(1):
            raise AssertionError(f"Unsupported detail_ref range {item!r}")
        if ord(first.group(2)) > ord(last.group(2)):
            raise AssertionError(f"Descending detail_ref range {item!r}")
        resolved.extend(
            f"{first.group(1)}{chr(letter)}"
            for letter in range(ord(first.group(2)), ord(last.group(2)) + 1)
        )
    return resolved


class ResponsibilityMigrationMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = MAP.read_text(encoding="utf-8")
        cls.manifest = MANIFEST.read_text(encoding="utf-8")

    def coverage_records(self) -> list[tuple[str, str, str, str]]:
        return re.findall(
            r"(?m)^- \[owner_path:: ([^\]]+\.md)\] "
            r"\[primary_responsibility:: ([A-Z_]+)\] "
            r"\[coverage_status:: (AUDIT_REQUIRED|DETAILED)\] "
            r"\[detail_ref:: ([^\]]+)\]$",
            self.text,
        )

    def test_complete_route_owner_coverage(self) -> None:
        expected = route_owners()
        records = self.coverage_records()
        covered = {record[0] for record in records}
        self.assertEqual(len(expected), 116)
        self.assertEqual(len(records), 116)
        self.assertEqual(covered, expected)
        self.assertFalse(any(path.startswith("02_World_Lore/") for path in covered))
        self.assertTrue(all(record[2] == "DETAILED" for record in records))

    def test_every_detail_ref_resolves_once_and_names_its_owner(self) -> None:
        sections = detail_sections(self.text)
        index_ids = re.findall(r"(?m)^\| (M-\d+(?:[a-z])?) \|", self.text)
        self.assertEqual(len(index_ids), 132)
        self.assertEqual(set(index_ids), set(sections))
        self.assertEqual(len(sections), 132)
        for owner, role, _status, detail_ref in self.coverage_records():
            for entry_id in expand_detail_ref(detail_ref):
                self.assertIn(entry_id, sections, f"{owner} references missing {entry_id}")
                self.assertIn(owner, sections[entry_id], f"{entry_id} does not name {owner}")
                if role == "LORE_ENTITY":
                    self.assertNotIn(
                        f"Mechanic owner:** `{owner}`",
                        sections[entry_id],
                        f"{entry_id} makes lore owner {owner} its own runtime mechanic owner",
                    )

    def test_preserved_meaning_is_not_template_boilerplate(self) -> None:
        generic = (
            "the player action, stated consequence, and direct-dependency boundaries "
            "remain in this mechanic."
        )
        self.assertNotIn(generic, self.text)
        meanings = re.findall(r"(?m)^- \*\*Preserved meaning:\*\* (.+)$", self.text)
        self.assertEqual(len(meanings), 132)
        self.assertEqual(len(meanings), len(set(meanings)))

    def test_status_policy_is_one_source_conflict_stream(self) -> None:
        status_entry = section(self.text, "M-09")
        self.assertIn("SOURCE_CONFLICT", status_entry)
        self.assertIn("05_Combat_Survival/Status_Effects.md", status_entry)
        self.assertIsNone(re.search(r"(?m)^### M-12(?:\s|—)", self.text))

    def test_foundling_history_stays_with_foundling_owner(self) -> None:
        foundling_entry = section(self.text, "M-10")
        self.assertIn(
            "Target owner: `04_Player_Entities/Shell_Foundlings.md`",
            foundling_entry,
        )
        self.assertIn("Approval and validation: no migration", foundling_entry)
        index_row = next(
            line for line in self.text.splitlines() if line.startswith("| M-10 ")
        )
        self.assertTrue(index_row.rstrip().endswith("| KEEP |"), index_row)

    def test_summary_counts_match_detailed_index(self) -> None:
        rows = [line for line in self.text.splitlines() if line.startswith("| M-")]
        statuses = [line.split("|")[5].strip() for line in rows]
        self.assertEqual(len(rows), 132)
        self.assertEqual(statuses.count("KEEP"), 115)
        self.assertEqual(statuses.count("MISSING_OWNER"), 16)
        self.assertEqual(statuses.count("SOURCE_CONFLICT"), 1)
        self.assertIn("Route-owner coverage: **116/116**", self.text)
        self.assertIn(
            "Detailed decisions: **132** — 115 `KEEP`, 16 `MISSING_OWNER`, 1 `SOURCE_CONFLICT`",
            self.text,
        )

    def test_pass_a_inventory_covers_each_owner_with_specific_evidence(self) -> None:
        rows = re.findall(
            r"(?m)^- \[owner_path:: ([^\]]+\.md)\] "
            r"\[register:: ([A-Z_]+)\] "
            r"\[pass_a_verdict:: (KEEP|REWRITE_COMPLETE)\] "
            r"\[evidence:: inspected `# .+?` -> `## .+?`; .+\]$",
            self.manifest,
        )
        expected = pass_a_route_owners()
        inventory_paths = [row[0] for row in rows]
        self.assertEqual(len(expected), 126)
        self.assertEqual(len(rows), 126)
        self.assertEqual(set(inventory_paths), expected)
        self.assertEqual(len(inventory_paths), len(set(inventory_paths)))
        rewritten = {path for path, _register, verdict in rows if verdict == "REWRITE_COMPLETE"}
        self.assertEqual(
            rewritten,
            {
                "01_Core_Vision/Art_Direction_Material_Grammar.md",
                "02_World_Lore/Lizard_Culture.md",
                "02_World_Lore/Squirrel_Culture.md",
                "02_World_Lore/Toad_Culture.md",
                "03_Factions_Societies/Reputation_Rules.md",
                "05_Combat_Survival/Combat_Three_Debts.md",
                "05_Combat_Survival/Traversal_Core.md",
                "08_World_Generation/Hub/04_Time_Atmosphere.md",
            },
        )

    def test_core_vision_metadata_is_semantic_not_generated_scaffolding(self) -> None:
        expected = {
            "01_Core_Vision/01_Vision.md": (
                "Фиксирует тон Элдрейна: уютная безысходность, ответственность за последствия и надежда без обещания безопасного исхода.",
                "Читайте, когда новая система, сцена или награда может изменить тон игры, её обещание компетентности или цену надежды.",
            ),
            "01_Core_Vision/02_Core_Loop.md": (
                "Описывает полный игровой цикл: подготовка, вход в рейд, рискованная работа, экстракция и последствия, возвращающиеся в следующий выбор.",
                "Читайте при изменении этапов цикла, переходов между Хабом и рейдом, условий провала, возвращения или последствий вылазки.",
            ),
            "01_Core_Vision/Art_Direction_Material_Grammar.md": (
                "Задаёт визуальный язык материалов, износа, ремонта и energy tells, чтобы состояние мира и предметов читалось до объяснения интерфейса.",
                "Читайте при изменении визуального языка объектов, повреждений, ремонта, следов энергии или читаемости материального состояния.",
            ),
        }
        for relative_path, (summary, when) in expected.items():
            frontmatter = (ROOT / relative_path).read_text(encoding="utf-8").split("---", 2)[1]
            self.assertIn(f'index_summary: "{summary}"', frontmatter)
            self.assertIn(f'read_when: "{when}"', frontmatter)
            self.assertNotIn('index_summary: "1."', frontmatter)
            self.assertNotIn("остальным контрактом", frontmatter)
            self.assertNotIn(Path(relative_path).stem, frontmatter)

    def test_micro_prompt_names_execution_contract(self) -> None:
        prompt = PROMPT.read_text(encoding="utf-8")
        for required in (
            "gpt-5.6-terra",
            "reasoning effort `high`",
            "eldraine-system-architect",
            "eldraine-gdd-author",
            "eldraine-vault-curator",
            "eldraine-lorekeeper",
            "03_Factions_Societies",
            "08_World_Generation",
            "02_World_Lore",
            "python tools/test_responsibility_migration_map.py",
            "python tools/vault_guard.py",
            "Не делай вторую аудиторскую проходку",
        ):
            self.assertIn(required, prompt)


if __name__ == "__main__":
    unittest.main()
