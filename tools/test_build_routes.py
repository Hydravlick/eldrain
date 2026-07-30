from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import subprocess
import sys

from tools.build_routes import MetadataError, build, check, render_root, render_system


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

    def test_renders_sorted_system_routes_from_owner_metadata(self) -> None:
        rendered = render_system(self.root, "01_Core_Vision")
        self.assertIn("## vision", rendered)
        self.assertLess(rendered.index("01_Vision"), rendered.index("02_Core_Loop"))
        self.assertIn("Когда решение меняет фантазию игрока.", rendered)

    def test_rejects_owner_without_required_route_metadata(self) -> None:
        self.write("01_Core_Vision/Missing.md", "---\nstatus: active\nindex_route: owner\n---\n")
        with self.assertRaises(MetadataError):
            render_system(self.root, "01_Core_Vision")

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
