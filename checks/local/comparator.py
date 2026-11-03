"""Comparator: each proof states exactly what its challenge states, as text, without Lean.

The challenge file (`[comparator] challenge` in checks/config.toml) holds each claim's Lean statement once more,
apart from the proofs, with the body `sorry`. The maintainer audits it against the source; the proof file must prove
exactly it. For each topic that `[comparator] topics` names, whose `**Lean:**` line names a declaration in a proof file
(`[comparator] proofs`), the rules are:

- a challenge exists: the name with `proof_prefix` swapped for `challenge_prefix` is declared in the challenge file (exact);
- same statement: the text from the keyword and modifiers to the first `:=` outside brackets, the name left out, is
  equal after comments are removed and whitespace is collapsed (exact);
- same context: the `open` commands in effect around the two declarations are the same set (exact);
- the challenge proves nothing: its body is `sorry` or `by sorry`, alone (exact);
- no orphan: every declaration of the challenge file is the challenge of some topic (exact);
- audit column: a topic has one `**Audited:**` line, `not yet` or the date (YYYY-MM-DD) the maintainer compared the
  statement with its source; the date is the maintainer's to write, and this check reads its form only (exact);
- Lean checks too: the agreement file (`[comparator] agreement`) holds one `#same_statement proof challenge` line for
  each topic, so the Lean build compares the types and lists the axioms (exact on the line, Lean on the rest).

What a run with no error guarantees: the proof file and the challenge file state each claim in the same words, in the
same context, and Lean is asked to compare them. This is the role of Lean FRO's comparator, in the part a program
can do without Lean.

What it does not decide:
- semantic equality: two different texts may state the same claim (the check then fails, and a person or Lean says
  which side to change), and two equal texts mean the same only if the definitions they name are the same, which the
  imports fix and this check does not read;
- that the statement means what the source says: only the maintainer's audit does, and each topic's **Audited:** line
  records it;
- that Lean accepts any of it: the build does;
- declarations produced by macros, or `open ... in` before a declaration: read as text, they are missed.

Time O(size of the files).
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

from framework.check_api import Finding, files_in_scope, matches_any

NAME = "comparator"
EXACT = True

_SPEC = importlib.util.spec_from_file_location("local_lean_link_for_comparator", Path(__file__).with_name("lean_link.py"))
lean_link = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(lean_link)

OPEN = re.compile(r"^\s*open\s+(.+?)\s*$")
OPENERS = "([{⦃⟨"
CLOSERS = ")]}⦄⟩"
SORRY_BODY = re.compile(r"^(?:by\s+)?sorry$")
AUDITED = re.compile(r"^\*\*Audited:\*\*\s*(.*?)\s*$", re.MULTILINE)
AUDIT_VALUE = re.compile(r"^(?:not yet|\d{4}-\d{2}-\d{2})$")
SAME_STATEMENT = re.compile(r"^\s*#same_statement\s+(\S+)\s+(\S+)\s*$", re.MULTILINE)


class Declaration:
    """One declaration read as text: its statement without its name, its body, the opens around it, its line."""

    def __init__(self, line: int, statement: str | None, body: str | None, opens: frozenset[str]) -> None:
        self.line, self.statement, self.body, self.opens = line, statement, body, opens


def squeeze(text: str) -> str:
    return " ".join(text.split())


def split_at_definition(rest: str) -> tuple[str, str] | None:
    """Split at the first `:=` outside brackets: (statement, body), or None when there is none."""
    depth = 0
    for index, char in enumerate(rest):
        if char in OPENERS:
            depth += 1
        elif char in CLOSERS:
            depth -= 1
        elif char == ":" and depth <= 0 and rest[index + 1:index + 2] == "=":
            return rest[:index], rest[index + 2:]
    return None


def read_declarations(text: str) -> dict[str, Declaration]:
    """Full name -> Declaration for one Lean file, with the namespace, section and `open` bookkeeping of lean_link."""
    plain = lean_link.without_comments(text)
    lines = plain.splitlines()
    scopes: list[tuple[list[str], list[str]]] = []   # (namespace parts, opens) per open scope
    found: dict[str, Declaration] = {}
    for number, line in enumerate(lines):
        space = lean_link.NAMESPACE.match(line)
        if space:
            scopes.append((space.group(1).split("."), []))
            continue
        if lean_link.SECTION.match(line):
            scopes.append(([], []))
            continue
        if lean_link.END.match(line):
            if scopes:
                scopes.pop()
            continue
        opened = OPEN.match(line)
        if opened and not opened.group(1).endswith(" in"):
            if scopes:
                scopes[-1][1].append(squeeze(opened.group(1)))
            else:
                scopes.append(([], [squeeze(opened.group(1))]))   # file level, closed by no `end`
            continue
        declared = lean_link.DECLARATION.match(line)
        if not declared:
            continue
        name = declared.group(1)
        prefix = [part for scope in scopes for part in scope[0]]
        full = name[len("_root_."):] if name.startswith("_root_.") else ".".join(prefix + [name])
        before, after = line[:declared.start(1)], "\n".join([line[declared.end(1):]] + lines[number + 1:])
        split = split_at_definition(after)
        opens = frozenset(item for scope in scopes for item in scope[1])
        if split is None:
            found[full] = Declaration(number + 1, None, None, opens)
            continue
        statement, rest = split
        # the body ends at the next declaration or end-of-scope line, so a trailing command is not part of it
        body_lines = []
        for next_line in rest.split("\n"):
            if body_lines and (lean_link.DECLARATION.match(next_line) or lean_link.END.match(next_line)
                               or lean_link.NAMESPACE.match(next_line) or OPEN.match(next_line)):
                break
            body_lines.append(next_line)
        found[full] = Declaration(number + 1, squeeze(before + " " + statement), squeeze(" ".join(body_lines)), opens)
    return found


def challenge_name(name: str, settings: dict) -> str | None:
    proof_prefix, challenge_prefix = settings.get("proof_prefix", ""), settings.get("challenge_prefix", "")
    if not name.startswith(proof_prefix):
        return None
    return challenge_prefix + name[len(proof_prefix):]


def read_all(root: Path, paths: list[str]) -> dict[str, Declaration]:
    found: dict[str, Declaration] = {}
    for path in paths:
        found.update(read_declarations((root / path).read_text(encoding="utf-8", errors="replace")))
    return found


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("comparator", {})
    topic_patterns = settings.get("topics", [])
    if not topic_patterns:
        return []
    challenge_path = settings["challenge"]
    agreement_path = settings.get("agreement", "")
    proofs = read_all(root, [p for p in files_in_scope(root, config, {".lean"}) if matches_any(p, settings.get("proofs", []))])
    challenges = read_all(root, [challenge_path]) if (root / challenge_path).is_file() else {}
    agreement = ((root / agreement_path).read_text(encoding="utf-8", errors="replace")
                 if agreement_path and (root / agreement_path).is_file() else "")
    lines_of_agreement = {(a, b) for a, b in SAME_STATEMENT.findall(lean_link.without_comments(agreement))}
    findings, claimed = [], set()
    for path in sorted(files_in_scope(root, config, {".md"})):
        if not matches_any(path, topic_patterns):
            continue
        topic_text = (root / path).read_text(encoding="utf-8", errors="replace")
        named = lean_link.named_by(topic_text)
        audits = AUDITED.findall(topic_text)
        if len(audits) != 1:
            findings.append(Finding(NAME, path, 1, f"{len(audits)} **Audited:** lines: a topic has one, `not yet` or a date"))
        elif not AUDIT_VALUE.match(audits[0]):
            findings.append(Finding(NAME, path, 1, f"**Audited:** holds `{audits[0]}`: write `not yet` or a date, YYYY-MM-DD"))
        if not named or named[0][1] is None or named[0][1] not in proofs:
            continue   # lean_link reports a missing line or a missing declaration
        number, name = named[0]
        target = challenge_name(name, settings)
        if target is None:
            findings.append(Finding(NAME, path, number, f"{name} does not start with proof_prefix: no challenge name"))
            continue
        claimed.add(target)
        if target not in challenges:
            findings.append(Finding(NAME, path, number, f"{name} has no challenge: {target} is not declared in {challenge_path}"))
            continue
        proof, challenge = proofs[name], challenges[target]
        if proof.statement is None or challenge.statement is None:
            findings.append(Finding(NAME, path, number, f"cannot read the statement of {name} or {target}: no `:=` found"))
        elif proof.statement != challenge.statement:
            findings.append(Finding(NAME, path, number,
                                    f"{name} states `{proof.statement}` but {target} states `{challenge.statement}`"))
        if proof.opens != challenge.opens:
            findings.append(Finding(NAME, path, number,
                                    f"{name} and {target} are read under different opens: {sorted(proof.opens)} and {sorted(challenge.opens)}"))
        if challenge.body is not None and not SORRY_BODY.match(challenge.body):
            findings.append(Finding(NAME, challenge_path, challenge.line, f"{target} has a body other than sorry"))
        if agreement_path and (name, target) not in lines_of_agreement:
            findings.append(Finding(NAME, path, number, f"{agreement_path} has no line `#same_statement {name} {target}`"))
    for target, challenge in sorted(challenges.items()):
        if target not in claimed:
            findings.append(Finding(NAME, challenge_path, challenge.line, f"{target} is the challenge of no topic"))
    return findings
