from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import subprocess
import sys

from tools.build_routes import MetadataError, build, check, render_root, render_domain


class BuildRoutesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.write(
            "01_Core_Vision/01_Vision.md",
            """---
status: active
index_route: owner
index_group: vision
index_order: 10
index_summary: \"Фиксирует обещание игры.\"
read_when: \"Когда решение меняет фантазию игрока.\"
---
""",
        )
        self.write(
            "01_Core_Vision/02_Core_Loop.md",
            """---
status: active
index_route: owner
index_group: core_loop
index_order: 20
index_summary: \"Определяет сессионный цикл.\"
read_when: \"Когда меняется рейдовый ритм.\"
---
""",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, text: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_renders_sorted_domain_routes_from_owner_metadata(self) -> None:
        rendered = render_domain(self.root, "01_Core_Vision")
        self.assertIn("## vision", rendered)
        self.assertLess(rendered.index("01_Vision"), rendered.index("02_Core_Loop"))
        self.assertIn("Когда решение меняет фантазию игрока.", rendered)

    def test_rejects_owner_without_required_route_metadata(self) -> None:
        self.write("01_Core_Vision/Missing.md", "---\nstatus: active\nindex_route: owner\n---\n")
        with self.assertRaises(MetadataError):
            render_domain(self.root, "01_Core_Vision")

    def test_build_writes_root_and_local_route_pages(self) -> None:
        build(self.root)
        self.assertTrue((self.root / "00_Index.md").is_file())
        self.assertTrue((self.root / "01_Core_Vision/00_Routes.md").is_file())
        self.assertIn("01_Core_Vision/00_Routes", (self.root / "00_Index.md").read_text(encoding="utf-8"))
        self.assertEqual(check(self.root), [])

    def test_check_reports_stale_generated_route_page(self) -> None:
        build(self.root)
        routes = self.root / "01_Core_Vision/00_Routes.md"
        routes.write_text("stale", encoding="utf-8")
        self.assertIn(routes, check(self.root))

    def test_check_reports_missing_domain_projection(self) -> None:
        build(self.root)
        routes = self.root / "01_Core_Vision/00_Routes.md"
        routes.unlink()
        self.assertIn(routes, check(self.root))

    def test_nonactive_owners_do_not_enter_routes(self) -> None:
        from tools.document_model import ACTIVE, MODEL
        for status in MODEL["statuses"]:
            if status != ACTIVE:
                self.write(f"01_Core_Vision/{status}.md", f"---\nstatus: {status}\nindex_route: owner\n---\n")
        rendered = render_domain(self.root, "01_Core_Vision")
        for status in MODEL["statuses"]:
            if status != ACTIVE:
                self.assertNotIn(f"[[01_Core_Vision/{status}]]", rendered)

    def test_build_is_idempotent_and_does_not_rewrite_unchanged_files(self) -> None:
        build(self.root)
        routes = self.root / "01_Core_Vision/00_Routes.md"
        before = routes.read_bytes(), routes.stat().st_mtime_ns
        build(self.root)
        self.assertEqual((routes.read_bytes(), routes.stat().st_mtime_ns), before)

    def test_bad_metadata_does_not_leave_partial_generated_output(self) -> None:
        self.write("08_World_Generation/Bad.md", "---\nstatus: active\nindex_route: owner\n---\n")
        with self.assertRaises(MetadataError):
            build(self.root)
        self.assertFalse((self.root / "01_Core_Vision/00_Routes.md").exists())

    def test_zero_order_and_unquoted_valid_yaml_are_supported(self) -> None:
        self.write("01_Core_Vision/Zero.md", "---\nstatus: active\nindex_route: owner\nindex_group: test\nindex_order: 0\nindex_summary: A rule.\nread_when: Editing it.\n---\n")
        rendered = render_domain(self.root, "01_Core_Vision")
        self.assertLess(rendered.index("/Zero]]"), rendered.index("/01_Vision]]"))

    def test_cli_writes_and_checks_routes(self) -> None:
        script = Path(__file__).with_name("build_routes.py")
        written = subprocess.run(
            [sys.executable, str(script), "--write", "--root", str(self.root)],
            capture_output=True,
            text=True,
        )
        checked = subprocess.run(
            [sys.executable, str(script), "--check", "--root", str(self.root)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(written.returncode, 0, written.stderr)
        self.assertEqual(checked.returncode, 0, checked.stderr)


if __name__ == "__main__":
    unittest.main()
