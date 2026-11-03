"""Tests of checks/local/comparator.py: each rule fails where it should and stays silent where it should not.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable, as for test_lean_link.py.
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
SPEC = importlib.util.spec_from_file_location("comparator", REPOSITORY / "checks" / "local" / "comparator.py")
comparator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(comparator)

CONFIG = {"comparator": {"topics": ["proofs/"], "proofs": ["Lib/"], "challenge": "Lib/Challenge.lean",
                         "agreement": "Lib/Agreement.lean", "proof_prefix": "P.", "challenge_prefix": "C."}}
PROOF = "namespace P\nopen Nat\n\n/-- Doc. -/\ntheorem one (n : ℕ) : n + 0 = n := by\n  simp\n\nend P\n"
CHALLENGE = "namespace C\nopen Nat\n\ntheorem one (n : ℕ) : n + 0 = n := by\n  sorry\n\nend C\n"
AGREEMENT = "import P\n-- #same_statement P.nope C.nope\n#same_statement P.one C.one\n"
TOPIC = "# T\n\nSummary.\n\n**Lean:** `P.one`\n\n**Audited:** not yet\n"


class Reading(unittest.TestCase):
    def test_statement_leaves_out_the_name_and_the_comments(self) -> None:
        text = "namespace P\n-- a comment\ntheorem one (n : ℕ)   -- inline\n    : n = n := rfl\nend P\n"
        self.assertEqual(comparator.read_declarations(text)["P.one"].statement, "theorem (n : ℕ) : n = n")

    def test_the_first_definition_outside_brackets_ends_the_statement(self) -> None:
        text = "theorem t (x : Nat := 3) : x = x := rfl\n"
        self.assertEqual(comparator.read_declarations(text)["t"].statement, "theorem (x : Nat := 3) : x = x")

    def test_body_stops_at_the_next_declaration(self) -> None:
        text = "theorem a : True := by\n  sorry\n\ntheorem b : True := trivial\n"
        found = comparator.read_declarations(text)
        self.assertEqual((found["a"].body, found["b"].body), ("by sorry", "trivial"))

    def test_opens_follow_scopes(self) -> None:
        text = "namespace A\nopen Nat\ntheorem a : True := trivial\nend A\ntheorem b : True := trivial\n"
        found = comparator.read_declarations(text)
        self.assertEqual((found["A.a"].opens, found["b"].opens), (frozenset({"Nat"}), frozenset()))

    def test_no_definition_gives_no_statement(self) -> None:
        self.assertIsNone(comparator.read_declarations("theorem a : True\n")["a"].statement)


class Check(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        self.write("Lib/P.lean", PROOF)
        self.write("Lib/Challenge.lean", CHALLENGE)
        self.write("Lib/Agreement.lean", AGREEMENT)
        self.write("proofs/t.md", TOPIC)

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def write(self, path: str, text: str) -> None:
        (self.root / path).parent.mkdir(parents=True, exist_ok=True)
        (self.root / path).write_text(text, encoding="utf-8")

    def messages(self) -> list[str]:
        return [finding.message for finding in comparator.check(self.root, CONFIG)]

    def test_matching_statements_pass(self) -> None:
        self.assertEqual(self.messages(), [])

    def test_whitespace_and_comments_do_not_matter(self) -> None:
        self.write("Lib/Challenge.lean", "namespace C\nopen Nat\n/-- Other doc. -/\ntheorem one\n  (n : ℕ) :   n + 0 = n   -- c\n  := sorry\nend C\n")
        self.assertEqual(self.messages(), [])

    def test_a_changed_statement_fails(self) -> None:
        self.write("Lib/Challenge.lean", CHALLENGE.replace("n + 0 = n", "0 + n = n"))
        self.assertIn("states", self.messages()[0])

    def test_a_changed_binder_fails(self) -> None:
        self.write("Lib/Challenge.lean", CHALLENGE.replace("(n : ℕ)", "{n : ℕ}"))
        self.assertIn("states", self.messages()[0])

    def test_a_changed_keyword_fails(self) -> None:
        self.write("Lib/Challenge.lean", CHALLENGE.replace("theorem", "lemma"))
        self.assertIn("states", self.messages()[0])

    def test_different_opens_fail(self) -> None:
        self.write("Lib/Challenge.lean", CHALLENGE.replace("open Nat\n", ""))
        self.assertIn("different opens", self.messages()[0])

    def test_a_missing_challenge_fails(self) -> None:
        self.write("Lib/Challenge.lean", "namespace C\nend C\n")
        self.assertIn("has no challenge", self.messages()[0])

    def test_a_proof_in_the_challenge_fails(self) -> None:
        self.write("Lib/Challenge.lean", CHALLENGE.replace("sorry", "simp"))
        self.assertIn("other than sorry", self.messages()[0])

    def test_a_challenge_no_topic_names_fails(self) -> None:
        self.write("Lib/Challenge.lean", CHALLENGE + "theorem extra : True := by\n  sorry\n")
        self.assertTrue(any("challenge of no topic" in message for message in self.messages()))

    def test_an_axiom_in_the_challenge_is_an_orphan(self) -> None:
        self.write("Lib/Challenge.lean", CHALLENGE.replace("end C", "axiom bad : False\nend C"))
        self.assertTrue(any("C.bad" in message for message in self.messages()))

    def test_a_missing_agreement_line_fails(self) -> None:
        self.write("Lib/Agreement.lean", "import P\n-- #same_statement P.one C.one\n")
        self.assertIn("has no line", self.messages()[0])

    def test_a_name_outside_the_prefix_fails(self) -> None:
        self.write("Lib/Q.lean", "theorem other : True := trivial\n")
        self.write("proofs/t.md", "# T\n\n**Lean:** `other`\n\n**Audited:** not yet\n")
        self.assertIn("proof_prefix", self.messages()[0])

    def test_a_declaration_lean_link_reports_is_left_to_it(self) -> None:
        self.write("proofs/t.md", "# T\n\n**Lean:** `P.nope`\n\n**Audited:** not yet\n")
        self.assertEqual(self.messages(), ["C.one is the challenge of no topic"])

    def test_files_outside_the_topics_are_ignored(self) -> None:
        self.write("notes.md", "# N\n\n**Lean:** `P.nope`\n")
        self.assertEqual(self.messages(), [])

    def test_a_date_is_an_audit(self) -> None:
        self.write("proofs/t.md", TOPIC.replace("not yet", "2026-11-04"))
        self.assertEqual(self.messages(), [])

    def test_a_missing_audit_line_fails(self) -> None:
        self.write("proofs/t.md", TOPIC.replace("\n**Audited:** not yet\n", ""))
        self.assertIn("0 **Audited:** lines", self.messages()[0])

    def test_two_audit_lines_fail(self) -> None:
        self.write("proofs/t.md", TOPIC + "\n**Audited:** not yet\n")
        self.assertIn("2 **Audited:** lines", self.messages()[0])

    def test_a_malformed_audit_fails(self) -> None:
        self.write("proofs/t.md", TOPIC.replace("not yet", "done"))
        self.assertIn("holds `done`", self.messages()[0])

    def test_no_config_no_findings(self) -> None:
        self.assertEqual(comparator.check(self.root, {}), [])


if __name__ == "__main__":
    unittest.main()
