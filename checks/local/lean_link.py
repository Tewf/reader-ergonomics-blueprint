"""Lean link: every topic of a proof names one Lean declaration, and that declaration exists in the Lean sources.

The topics are the markdown files that `[lean_link] topics` names in checks/config.toml; the sources are the
`.lean` files that `[lean_link] sources` names. A topic names its declaration on a line of its own,

    **Lean:** `Blueprint.InfinitelyManyPrimes.exists_prime_gt`

and the rules are:

- one line: a topic has exactly one `**Lean:**` line, so a reader and a program find the same declaration (exact);
- exists: the name is the full name of a declaration in the sources, namespaces included (exact);
- one topic each: no two topics name the same declaration, so a claim has one place (exact).

The role is the one `checkdecls` plays for Lean blueprints: it compares names and never calls Lean. Whether the
declaration proves the claim in the topic is not decided here: a person reads the statement beside the topic.

What a run with no error guarantees, for the files the config names:
- each topic carries one `**Lean:**` line with one name;
- each name is declared in the sources by `theorem`, `lemma`, `def`, `abbrev`, `instance`, `structure`,
  `inductive`, `class`, `axiom` or `opaque`, under the `namespace` blocks around it;
- no two topics name the same declaration.

What it does not guarantee:
- that Lean accepts the declaration (the build step does), or that it has no `sorry` (the build fails on that);
- that the statement means what the topic says;
- declarations produced by a macro, by `deriving`, or inside a `namespace` opened by `open ... in` alone: the
  sources are read as text, comments removed, with no elaboration. Such a name is reported as missing.

Time O(size of the topics and the sources).
"""
from __future__ import annotations

import re
from pathlib import Path

from framework.check_api import Finding, files_in_scope, matches_any

NAME = "lean-link"
EXACT = True

LEAN_LINE = re.compile(r"^\*\*Lean:\*\*\s*(.*?)\s*$")
CODE_NAME = re.compile(r"^`([^`\s]+)`$")
NAMESPACE = re.compile(r"^\s*namespace\s+(\S+)")
SECTION = re.compile(r"^\s*section\b")
END = re.compile(r"^\s*end(?:\s+\S+)?\s*$")
DECLARATION = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|unsafe|partial|nonrec)\s+)*"
    r"(?:theorem|lemma|def|abbrev|instance|structure|inductive|class|axiom|opaque)\s+([^\s:({\[⦃]+)")


def without_comments(text: str) -> str:
    """The Lean text with line comments and nested block comments blanked, line numbers kept."""
    out, depth, index = [], 0, 0
    while index < len(text):
        pair = text[index:index + 2]
        if pair == "/-":
            depth += 1
            index += 2
        elif pair == "-/" and depth:
            depth -= 1
            index += 2
        elif depth:
            out.append("\n" if text[index] == "\n" else " ")
            index += 1
        elif pair == "--":
            while index < len(text) and text[index] != "\n":
                index += 1
        else:
            out.append(text[index])
            index += 1
    return "".join(out)


def declarations(text: str) -> set[str]:
    """Full names of the declarations in one Lean file, under the namespaces and sections around them."""
    scopes: list[list[str]] = []
    found = set()
    for line in without_comments(text).splitlines():
        space = NAMESPACE.match(line)
        if space:
            scopes.append(space.group(1).split("."))
        elif SECTION.match(line):
            scopes.append([])
        elif END.match(line):
            if scopes:
                scopes.pop()
        else:
            declared = DECLARATION.match(line)
            if declared:
                name = declared.group(1)
                if name.startswith("_root_."):
                    found.add(name[len("_root_."):])
                else:
                    found.add(".".join([part for scope in scopes for part in scope] + [name]))
    return found


def named_by(text: str) -> list[tuple[int, str | None]]:
    """The (line, name) of each `**Lean:**` line; name is None when the line does not hold exactly one code name."""
    lines = []
    for number, line in enumerate(text.splitlines(), 1):
        match = LEAN_LINE.match(line)
        if match:
            code = CODE_NAME.match(match.group(1))
            lines.append((number, code.group(1) if code else None))
    return lines


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("lean_link", {})
    topic_patterns = settings.get("topics", [])
    source_patterns = settings.get("sources", [])
    if not topic_patterns:
        return []
    known: set[str] = set()
    for path in files_in_scope(root, config, {".lean"}):
        if matches_any(path, source_patterns):
            known |= declarations((root / path).read_text(encoding="utf-8", errors="replace"))
    findings, owner = [], {}
    for path in sorted(files_in_scope(root, config, {".md"})):
        if not matches_any(path, topic_patterns):
            continue
        lines = named_by((root / path).read_text(encoding="utf-8", errors="replace"))
        if not lines:
            findings.append(Finding(NAME, path, 1, "names no Lean declaration: add one line, **Lean:** `Name`"))
            continue
        if len(lines) > 1:
            findings.append(Finding(NAME, path, lines[1][0], f"{len(lines)} **Lean:** lines: a topic names one declaration"))
        number, name = lines[0]
        if name is None:
            findings.append(Finding(NAME, path, number, "the **Lean:** line holds anything but one name in backticks"))
        elif name not in known:
            findings.append(Finding(NAME, path, number, f"{name} is not declared in the Lean sources"))
        elif name in owner:
            findings.append(Finding(NAME, path, number, f"{name} is also named by {owner[name]}: one topic per declaration"))
        else:
            owner[name] = path
    return findings
