import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_vault_graph.py"


def load_module():
    spec = importlib.util.spec_from_file_location("build_vault_graph", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_note(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class BuildVaultGraphTest(unittest.TestCase):
    def test_build_graph_resolves_wikilinks_frontmatter_and_backlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(
                root,
                "00_Index.md",
                """---
type: index
status: active
system: navigation
tags: [master_index, gdd]
---
# Index
See [[01_Core_Vision/01_Vision|Vision]] and [[Missing Note]].
""",
            )
            write_note(
                root,
                "01_Core_Vision/01_Vision.md",
                """---
type: vision
status: active
tags:
  - core
---
# Vision
Back to [[00_Index]].
""",
            )

            graph = load_module().build_graph(root)

        index = graph["nodes"]["00_Index.md"]
        vision = graph["nodes"]["01_Core_Vision/01_Vision.md"]

        self.assertEqual(index["frontmatter"]["type"], "index")
        self.assertEqual(index["frontmatter"]["tags"], ["master_index", "gdd"])
        self.assertEqual(vision["frontmatter"]["tags"], ["core"])
        self.assertIn("01_Core_Vision/01_Vision.md", index["outgoing"])
        self.assertIn("00_Index.md", vision["outgoing"])
        self.assertIn("00_Index.md", vision["backlinks"])
        self.assertEqual(
            graph["broken_links"],
            [
                {
                    "source": "00_Index.md",
                    "target": "Missing Note",
                    "kind": "wikilink",
                }
            ],
        )

    def test_main_writes_json_dot_and_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "A.md", "# A\n[[B]]\n")
            write_note(root, "B.md", "# B\n")
            out_dir = root / ".graph"

            rc = load_module().main([str(root), "--out", str(out_dir)])

            data = json.loads((out_dir / "vault-graph.json").read_text(encoding="utf-8"))
            dot = (out_dir / "vault-graph.dot").read_text(encoding="utf-8")
            report = (out_dir / "vault-graph-report.md").read_text(encoding="utf-8")

        self.assertEqual(rc, 0)
        self.assertEqual(data["summary"]["nodes"], 2)
        self.assertEqual(data["summary"]["edges"], 1)
        self.assertIn('"A.md" -> "B.md"', dot)
        self.assertIn("## Summary", report)

    def test_cache_tracks_new_and_changed_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "A.md", "# A\n[[B]]\n")
            write_note(root, "B.md", "# B\n")
            out_dir = root / ".graph"
            cache_path = out_dir / "vault-graph-cache.json"

            rc = load_module().main([str(root), "--out", str(out_dir), "--cache", str(cache_path)])
            self.assertEqual(rc, 0)
            self.assertTrue(cache_path.exists())

            write_note(root, "C.md", "# C\n[[A]]\n")
            rc = load_module().main([str(root), "--out", str(out_dir), "--cache", str(cache_path)])
            data = json.loads((out_dir / "vault-graph.json").read_text(encoding="utf-8"))

        self.assertEqual(rc, 0)
        self.assertEqual(data["summary"]["nodes"], 3)
        self.assertEqual(data["summary"]["edges"], 2)
        self.assertIn("C.md", data["nodes"]["A.md"]["backlinks"])

if __name__ == "__main__":
    unittest.main()
