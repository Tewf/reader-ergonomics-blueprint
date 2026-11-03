"""Tests of checks/local/lean_link.py: each rule fails where it should and stays silent where it should not.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or check
reader-ergonomics out beside this repository (as CI does, under the name standard).
"""
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
REPOSITORY = HERE.parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""), REPOSITORY / "checks" / "out" / "standard" / "checks",
              REPOSITORY.parent / "standard" / "checks", REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))
SPEC = importlib.util.spec_from_file_location("lean_link", REPOSITORY / "checks" / "local" / "lean_link.py")
lean_link = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lean_link)

CONFIG = {"lean_link": {"topics": ["proofs/"], "sources": ["Lib/"]}}
LEAN = "namespace A\n\ntheorem one : True := trivial\n\nnamespace B\ntheorem two : True := trivial\nend B\n\nend A\n"


class Declarations(unittest.TestCase):
    def test_namespaces_prefix_names(self) -> None:
        self.assertEqual(lean_link.declarations(LEAN), {"A.one", "A.B.two"})

    def test_namespace_closes(self) -> None:
        self.assertIn("three", lean_link.declarations(LEAN + "theorem three : True := trivial\n"))

    def test_section_does_not_prefix_but_its_end_is_not_a_namespace_end(self) -> None:
        text = "namespace A\nsection\ntheorem x : True := trivial\nend\ntheorem y : True := trivial\nend A\n"
        self.assertEqual(lean_link.declarations(text), {"A.x", "A.y"})

    def test_dotted_and_root_names(self) -> None:
        text = "namespace A\ntheorem foo.bar : True := trivial\ntheorem _root_.baz : True := trivial\nend A\n"
        self.assertEqual(lean_link.declarations(text), {"A.foo.bar", "baz"})

    def test_modifiers_and_attributes(self) -> None:
        text = "namespace A\n@[simp] protected theorem p : True := trivial\nprivate def q := 1\nend A\n"
        self.assertEqual(lean_link.declarations(text), {"A.p", "A.q"})

    def test_comments_hide_declarations(self) -> None:
        text = "-- theorem a : True\n/- theorem b : True\n/- nested -/ theorem c : True -/\n/-- doc -/\ntheorem d : True := trivial\n"
        self.assertEqual(lean_link.declarations(text), {"d"})


class Check(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        self.write("Lib/A.lean", LEAN)

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def write(self, path: str, text: str) -> None:
        (self.root / path).parent.mkdir(parents=True, exist_ok=True)
        (self.root / path).write_text(text, encoding="utf-8")

    def messages(self) -> list[str]:
        return [finding.message for finding in lean_link.check(self.root, CONFIG)]

    def test_a_topic_naming_an_existing_declaration_passes(self) -> None:
        self.write("proofs/t.md", "# T\n\nSummary.\n\n**Lean:** `A.one`\n")
        self.assertEqual(self.messages(), [])

    def test_nested_namespace_declaration_passes(self) -> None:
        self.write("proofs/t.md", "# T\n\nSummary.\n\n**Lean:** `A.B.two`\n")
        self.assertEqual(self.messages(), [])

    def test_missing_line(self) -> None:
        self.write("proofs/t.md", "# T\n\nSummary.\n")
        self.assertEqual(len(self.messages()), 1)
        self.assertIn("names no Lean declaration", self.messages()[0])

    def test_missing_declaration(self) -> None:
        self.write("proofs/t.md", "# T\n\nSummary.\n\n**Lean:** `A.nope`\n")
        self.assertIn("A.nope is not declared", self.messages()[0])

    def test_unqualified_name_is_missing(self) -> None:
        self.write("proofs/t.md", "# T\n\nSummary.\n\n**Lean:** `one`\n")
        self.assertIn("not declared", self.messages()[0])

    def test_two_lines(self) -> None:
        self.write("proofs/t.md", "# T\n\n**Lean:** `A.one`\n\n**Lean:** `A.B.two`\n")
        self.assertIn("2 **Lean:** lines", self.messages()[0])

    def test_name_not_in_backticks(self) -> None:
        self.write("proofs/t.md", "# T\n\n**Lean:** A.one\n")
        self.assertIn("anything but one name", self.messages()[0])

    def test_two_names_on_one_line(self) -> None:
        self.write("proofs/t.md", "# T\n\n**Lean:** `A.one` and `A.B.two`\n")
        self.assertIn("anything but one name", self.messages()[0])

    def test_two_topics_one_declaration(self) -> None:
        self.write("proofs/a.md", "# A\n\n**Lean:** `A.one`\n")
        self.write("proofs/b.md", "# B\n\n**Lean:** `A.one`\n")
        self.assertIn("one topic per declaration", self.messages()[0])

    def test_files_outside_the_topics_are_ignored(self) -> None:
        self.write("notes.md", "# N\n\nNo link.\n")
        self.assertEqual(self.messages(), [])

    def test_declaration_in_a_comment_does_not_count(self) -> None:
        self.write("Lib/B.lean", "-- theorem ghost : True\n")
        self.write("proofs/t.md", "# T\n\n**Lean:** `ghost`\n")
        self.assertIn("not declared", self.messages()[0])

    def test_no_config_no_findings(self) -> None:
        self.assertEqual(lean_link.check(self.root, {}), [])


if __name__ == "__main__":
    unittest.main()
