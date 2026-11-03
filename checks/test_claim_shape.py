"""Tests of checks/local/claim_shape.py: each rule fails where it should and stays silent where it should not.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable, as for the other local checks' tests.
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
SPEC = importlib.util.spec_from_file_location("claim_shape", REPOSITORY / "checks" / "local" / "claim_shape.py")
claim_shape = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(claim_shape)

CONFIG = {"claim_shape": {"files": ["proofs/*/*.md"], "exempt": ["proofs/*/README.md"]}}
GOOD = """# A claim

Every n at least 2 has a prime factor.

**Shape:** [claim](../../shapes/claim.md)
**Lean:** `A.b`

**In words:** for n with 2 le n, there is a prime that divides n.

**Prose audited:** 2026-11-03, by a model, not a person

**Audited:** not yet

## Statement

If 2 le m, some prime divides m.

## Proof

Take the least divisor above 1.

## See also

[The theorem](README.md).
"""


class Rules(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.root)

    def messages(self, text: str, path: str = "proofs/p/c.md") -> list[str]:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return [finding.message for finding in claim_shape.check(self.root, CONFIG)]

    def test_good_claim_passes(self) -> None:
        self.assertEqual(self.messages(GOOD), [])

    def test_theorem_readme_is_exempt(self) -> None:
        self.assertEqual(self.messages("# T\n\nno parts\n", "proofs/p/README.md"), [])

    def test_files_outside_the_claims_are_ignored(self) -> None:
        self.assertEqual(self.messages("# T\n", "notes/x.md"), [])

    def test_no_config_no_findings(self) -> None:
        self.messages(GOOD)
        self.assertEqual(claim_shape.check(self.root, {}), [])

    def test_two_sentences(self) -> None:
        text = GOOD.replace("prime factor.", "prime factor. It is small.")
        self.assertIn("one sentence", self.messages(text)[0])

    def test_claim_without_final_period(self) -> None:
        self.assertIn("one sentence", self.messages(GOOD.replace("prime factor.", "prime factor"))[0])

    def test_claim_too_long(self) -> None:
        text = GOOD.replace("Every n at least 2", "Every " + "very " * 40 + "n at least 2")
        self.assertIn("past 35", self.messages(text)[0])

    def test_missing_label(self) -> None:
        text = GOOD.replace("**Audited:** not yet\n\n", "")
        self.assertIn("0 **Audited:** lines", self.messages(text)[0])

    def test_repeated_label(self) -> None:
        text = GOOD.replace("**Audited:** not yet", "**Audited:** not yet\n\n**Audited:** not yet")
        self.assertIn("2 **Audited:** lines", self.messages(text)[0])

    def test_labels_out_of_order(self) -> None:
        text = GOOD.replace("**Shape:** [claim](../../shapes/claim.md)\n**Lean:** `A.b`",
                            "**Lean:** `A.b`\n**Shape:** [claim](../../shapes/claim.md)")
        self.assertIn("order", self.messages(text)[0])

    def test_shape_line_links_another_shape(self) -> None:
        text = GOOD.replace("shapes/claim.md", "shapes/topic.md")
        self.assertIn("does not link shapes/claim.md", self.messages(text)[0])

    def test_in_words_empty(self) -> None:
        text = GOOD.replace("for n with 2 le n, there is a prime that divides n.", "")
        self.assertIn("In words", self.messages(text)[0])

    def test_audit_without_date(self) -> None:
        self.assertIn("a date", self.messages(GOOD.replace("2026-11-03, by a model, not a person", "done"))[0])

    def test_model_audit_not_labelled_as_such(self) -> None:
        self.assertIn("not a person's", self.messages(GOOD.replace(", not a person", ""))[0])

    def test_audit_without_a_reader(self) -> None:
        self.assertIn("who read", self.messages(GOOD.replace("by a model, not a person", "checked"))[0])

    def test_audit_by_the_maintainer(self) -> None:
        self.assertEqual(self.messages(GOOD.replace("by a model, not a person", "by the maintainer")), [])

    def test_not_yet_audit(self) -> None:
        self.assertEqual(self.messages(GOOD.replace("2026-11-03, by a model, not a person", "not yet")), [])

    def test_missing_part(self) -> None:
        self.assertIn("no '## Proof' part", self.messages(GOOD.replace("## Proof", "## Argument"))[0])

    def test_parts_out_of_order(self) -> None:
        text = GOOD.replace("## Statement", "## Tmp").replace("## Proof", "## Statement").replace("## Tmp", "## Proof")
        self.assertIn("order Statement", self.messages(text)[0])

    def test_empty_statement(self) -> None:
        self.assertIn("empty", self.messages(GOOD.replace("If 2 le m, some prime divides m.", ""))[0])

    def test_no_title(self) -> None:
        self.assertIn("title", self.messages(GOOD.replace("# A claim", "A claim"))[0])


if __name__ == "__main__":
    unittest.main()
