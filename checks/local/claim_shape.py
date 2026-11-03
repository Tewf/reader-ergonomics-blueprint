"""Claim shape: every claim topic of a proof has the parts shapes/claim.md asks for, in its order.

The claims are the markdown files that `[claim_shape] files` names in checks/config.toml, less `exempt` (the
theorem's own README). A claim reads, top to bottom:

- title: the first block is one `# ` heading (exact);
- the claim: the paragraph after the title is one sentence, ending in a period, of at most `max_words` words (exact);
- five labelled lines, each once, in this order: Shape, Lean, In words, Prose audited, Audited (exact);
- the Shape line links the shape file, `shape` in the config (exact);
- the In words line holds at least three words (exact);
- the Prose audited line is `not yet`, or a date followed by who read: "by a model" with "not a person", or
  "by the maintainer", or "by a person" (exact). A model's reading never passes for a person's audit;
- the parts `## Statement`, `## Proof` and `## See also`, in that order, with a statement that is not empty (exact).

The Lean name is the link check's, and the form of the Audited line is the comparator's; neither is repeated here.

What a run with no error guarantees, for the files the config names: each claim has the parts above, so a reader
and a program find the same line in every claim, and a model's reading is labelled as a model's.

What it does not guarantee: that the claim is one claim, that the statement is right, that the proof is, or that
the person who is named did read (meaning, and the audit).
Time O(text).
"""
from __future__ import annotations

import re
from pathlib import Path

from framework.check_api import Finding, files_in_scope, matches_any, prose_only

NAME = "claim-shape"
EXACT = True

LABELS = ["Shape", "Lean", "In words", "Prose audited", "Audited"]
LABEL_LINE = re.compile(r"^\*\*(Shape|Lean|In words|Prose audited|Audited):\*\*[ \t]*(.*?)\s*$")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}\b")
SENTENCE_BREAK = re.compile(r"\.\s+[A-Z]")


def parts(text: str) -> dict:
    """The title, the first paragraph, the labelled lines and the `##` headings of one claim, with line numbers."""
    lines = text.splitlines()
    found = {"title": None, "claim": None, "labels": [], "headings": [], "statement": ""}
    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index < len(lines):
        match = HEADING.match(lines[index])
        if match and len(match.group(1)) == 1:
            found["title"] = index + 1
            index += 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    start = index
    while index < len(lines) and lines[index].strip():
        index += 1
    if start < len(lines) and not LABEL_LINE.match(lines[start]) and not HEADING.match(lines[start]):
        found["claim"] = (start + 1, " ".join(line.strip() for line in lines[start:index]))
    current = None
    for number, line in enumerate(lines, 1):
        label, heading = LABEL_LINE.match(line), HEADING.match(line)
        if label:
            found["labels"].append((number, label.group(1), label.group(2)))
        if heading and len(heading.group(1)) == 2:
            current = heading.group(2).lower()
            found["headings"].append((number, current))
        elif current == "statement" and line.strip() and not heading:
            found["statement"] += line
    return found


def who_audited(value: str) -> str | None:
    """None when the line is acceptable, else what is wrong with it."""
    if value.lower().startswith("not yet"):
        return None
    if not DATE.match(value):
        return "a date (YYYY-MM-DD) or 'not yet'"
    if "by a model" in value:
        return None if "not a person" in value else "a model's audit says it is not a person's"
    if "by the maintainer" in value or "by a person" in value:
        return None
    return "who read: 'by a model, not a person', 'by the maintainer' or 'by a person'"


def check_claim(path: str, text: str, shape: str, max_words: int) -> list[Finding]:
    found = parts(prose_only(text))
    findings = []
    if found["title"] is None:
        findings.append(Finding(NAME, path, 1, "a claim opens with its title, one '# ' heading"))
    if found["claim"] is None:
        findings.append(Finding(NAME, path, 1, "no claim sentence right after the title"))
    else:
        line, sentence = found["claim"]
        if not sentence.endswith(".") or SENTENCE_BREAK.search(sentence):
            findings.append(Finding(NAME, path, line, "the claim is one sentence, ending in a period"))
        elif len(sentence.split()) > max_words:
            findings.append(Finding(NAME, path, line, f"a claim of {len(sentence.split())} words, past {max_words}"))
    seen = [label for _, label, _ in found["labels"]]
    for label in LABELS:
        if seen.count(label) != 1:
            findings.append(Finding(NAME, path, 1, f"{seen.count(label)} **{label}:** lines: a claim has exactly one"))
    order = [label for label in seen if label in LABELS]
    if all(seen.count(label) == 1 for label in LABELS) and order != LABELS:
        findings.append(Finding(NAME, path, 1, "the labelled lines are not in the shape's order: " + ", ".join(LABELS)))
    for number, label, value in found["labels"]:
        if label == "Shape" and not any(target.endswith(shape) for target in LINK.findall(value)):
            findings.append(Finding(NAME, path, number, f"the Shape line does not link {shape}"))
        if label == "In words" and len(value.split()) < 3:
            findings.append(Finding(NAME, path, number, "the In words line gives no reading of the Lean statement"))
        if label == "Prose audited" and who_audited(value):
            findings.append(Finding(NAME, path, number, f"the Prose audited line needs {who_audited(value)}"))
    names = [name for _, name in found["headings"]]
    wanted = ["statement", "proof", "see also"]
    for part in wanted:
        if part not in names:
            findings.append(Finding(NAME, path, 1, f"no '## {part.title() if part != 'see also' else 'See also'}' part"))
    kept = [name for name in names if name in wanted]
    if all(part in names for part in wanted) and kept != wanted:
        findings.append(Finding(NAME, path, 1, "the parts are not in the order Statement, Proof, See also"))
    if "statement" in names and not found["statement"].strip():
        findings.append(Finding(NAME, path, 1, "the Statement part is empty"))
    return findings


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("claim_shape", {})
    patterns = settings.get("files", [])
    if not patterns:
        return []
    exempt, shape = settings.get("exempt", []), settings.get("shape", "shapes/claim.md")
    findings = []
    for path in sorted(files_in_scope(root, config, {".md"})):
        if matches_any(path, patterns) and not matches_any(path, exempt):
            text = (root / path).read_text(encoding="utf-8", errors="replace")
            findings += check_claim(path, text, shape, settings.get("max_words", 35))
    return findings
