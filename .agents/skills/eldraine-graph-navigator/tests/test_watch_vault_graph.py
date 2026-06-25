import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "watch_vault_graph.py"


def load_module():
    spec = importlib.util.spec_from_file_location("watch_vault_graph", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_note(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class WatchVaultGraphTest(unittest.TestCase):
    def test_once_builds_outputs_and_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_note(root, "A.md", "# A\n[[B]]\n")
            write_note(root, "B.md", "# B\n")
            out_dir = root / ".graph"
            cache_path = out_dir / "vault-graph-cache.json"

            rc = load_module().main([
                str(root),
                "--out",
                str(out_dir),
                "--cache",
                str(cache_path),
                "--once",
            ])
            data = json.loads((out_dir / "vault-graph.json").read_text(encoding="utf-8"))
            cache_exists = cache_path.exists()

        self.assertEqual(rc, 0)
        self.assertEqual(data["summary"]["nodes"], 2)
        self.assertTrue(cache_exists)


if __name__ == "__main__":
    unittest.main()
