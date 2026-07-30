from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.vault_guard import (
    check_frontmatter,
    check_index,
    check_links,
    check_owners,
    check_surface,
    parse_frontmatter,
    project_files,
    resolve_wikilink,
)


class VaultGuardTests(unittest.TestCase):
    def make_root(self) -> Path:
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        (root / "01_Core_Vision").mkdir()
        (root / "09_Project_Management").mkdir()
        return root

    def tearDown(self) -> None:
        if hasattr(self, "temp"):
            self.temp.cleanup()

    @staticmethod
    def write(path: Path, text: str = "") -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_resolves_root_relative_wikilink(self) -> None:
        root = self.make_root()
        source = root / "01_Core_Vision" / "Source.md"
        target = root / "01_Core_Vision" / "Target.md"
        self.write(source)
        self.write(target)
        self.assertEqual(resolve_wikilink(source, "01_Core_Vision/Target", set(project_files(root))), target)

    def test_resolves_root_relative_wikilink_from_relative_corpus(self) -> None:
        source = Path("01_Core_Vision/Source.md")
        target = Path("01_Core_Vision/Target.md")
        self.assertEqual(resolve_wikilink(source, "01_Core_Vision/Target", {source, target}), target)

    def test_resolves_alias_and_heading(self) -> None:
        root = self.make_root()
        source = root / "01_Core_Vision" / "Source.md"
        target = root / "01_Core_Vision" / "Target.md"
        self.write(source)
        self.write(target)
        self.assertEqual(resolve_wikilink(source, "01_Core_Vision/Target#Rule|Shown", set(project_files(root))), target)

    def test_resolves_escaped_alias_and_heading(self) -> None:
        root = self.make_root()
        source = root / "01_Core_Vision" / "Source.md"
        target = root / "01_Core_Vision" / "Target.md"
        self.write(source)
        self.write(target)
        self.assertEqual(resolve_wikilink(source, "01_Core_Vision/Target\\|Shown", set(project_files(root))), target)

    def test_ignores_dataview_template_target(self) -> None:
        root = self.make_root()
        self.write(root / "01_Core_Vision" / "Page.md", "```dataview\n${row.link}\n```\n")
        self.assertEqual(check_links(root), [])

    def test_reports_missing_target(self) -> None:
        root = self.make_root()
        self.write(root / "01_Core_Vision" / "Page.md", "[[Missing]]")
        self.assertIn("MISSING_LINK_TARGET", {v.code for v in check_links(root)})

    def test_reports_index_link_to_nonactive_page(self) -> None:
        root = self.make_root()
        self.write(root / "00_Index.md", "[[01_Core_Vision/Old]]")
        self.write(root / "01_Core_Vision" / "Old.md", "---\nstatus: deprecated\n---\n")
        self.assertIn("INDEX_TARGET_NOT_ACTIVE", {v.code for v in check_index(root)})

    def test_reports_duplicate_owns_value(self) -> None:
        root = self.make_root()
        for name in ("A", "B"):
            self.write(root / "01_Core_Vision" / f"{name}.md", "---\nstatus: active\nowns: shared.rule\n---\n")
        self.assertIn("DUPLICATE_OWNS", {v.code for v in check_owners(root)})

    def test_reports_unquoted_route_text_metadata(self) -> None:
        root = self.make_root()
        self.write(
            root / "01_Core_Vision" / "Broken.md",
            "---\nstatus: active\nindex_summary: Правило: с двоеточием.\nread_when: Читайте: при изменении.\n---\n",
        )
        self.assertIn("ROUTE_TEXT_NOT_QUOTED", {v.code for v in check_frontmatter(root)})

    def test_parses_escaped_double_quoted_metadata(self) -> None:
        root = self.make_root()
        path = root / "01_Core_Vision" / "Quoted.md"
        self.write(path, '---\nindex_summary: "Топология: \\"Цветок\\"."\n---\n')
        self.assertEqual(parse_frontmatter(path)["index_summary"], 'Топология: "Цветок".')

    def test_reports_forbidden_local_state_file(self) -> None:
        root = self.make_root()
        self.write(root / ".obsidian" / "workspace.json", "{}")
        self.assertIn("FORBIDDEN_LOCAL_STATE", {v.code for v in check_surface(root, strict=False)})

    def test_git_directory_is_excluded_from_sources(self) -> None:
        root = self.make_root()
        self.write(root / ".git" / "hidden.md", "[[Missing]]")
        self.assertNotIn(root / ".git" / "hidden.md", project_files(root))

    def test_strict_surface_rejects_unapproved_top_level_path(self) -> None:
        root = self.make_root()
        self.write(root / "unexpected.txt", "x")
        self.assertIn("FORBIDDEN_TOP_LEVEL_PATH", {v.code for v in check_surface(root, strict=True)})

    def test_strict_surface_limits_project_management_files(self) -> None:
        root = self.make_root()
        self.write(root / "09_Project_Management" / "Old.md", "x")
        self.assertIn("FORBIDDEN_PROJECT_MANAGEMENT_FILE", {v.code for v in check_surface(root, strict=True)})


if __name__ == "__main__":
    unittest.main()
