"""Topic: every topic of the tree opens with a title and a summary, is listed by its parent with that summary,
and no topic includes itself.

The topics are the markdown files that `[topic] files` names in checks/config.toml. A topic's parent is the
README.md of the nearest folder above it that is a topic (for a README.md, of the folder above its own); `root`
has none. Following parents from any topic reaches the root, so the rules hold at any depth:

- title: the first block is the one `# ` heading of the file (exact);
- summary: within the first `summary_within` blocks after the title, a block labelled with one of
  `summary_labels` (a `## Abstract` heading and the paragraph under it, or a paragraph opening `**Abstract.**`),
  so a byline or a status line may stand before it; with no label, the next block after any badges, which must be
  a paragraph or a quote (exact); at most `summary_words` words (heuristic: the bound is a tunable);
- listed: the parent links the topic, so a reader can reach it from the root (exact);
- with its summary: the parent's listing carries at least `listing_words` words beside the link, unless the
  child is of a type named in `typed`, whose role is stated once where the type is defined (heuristic);
- no inclusion cycle among `{{< include >}}` shortcodes, in any markdown file (exact);
- announced: a file that `[topic] shapes` declares of a shape links that shape's file, `shapes/<name>.md`, here or in
  another repository, such as the standard's (exact).

Heading depth, links that resolve and the headings a shape requires are reader-ergonomics' own checks.
Time O(text) for the blocks and the links, O(files + inclusions) for the cycles.

What a run with no error guarantees, for the files `[topic] files` declares:
- each opens with one `# ` title, followed by a summary block, or by one an allowed label marks;
- each but the root is linked from its containing topic, so a chain of links leads from the root to it;
- no markdown file in scope includes itself through `{{< include >}}`, directly or at any depth;
- each file declared of a shape links that shape, so a reader knows which blocks to expect.

What it does not guarantee:
- that a summary stands for its topic, or that a listing repeats the child's own summary (meaning);
- anything about nesting inside one file: sections are not topics here;
- links given as absolute addresses, and inclusions by any mechanism other than the Quarto shortcode.

A file it cannot decode is read with replacement characters, never skipped; an inclusion of a missing file is
ignored by the cycle search, since reader-ergonomics' link check reports what is missing.
"""
from __future__ import annotations

import posixpath
import re
from pathlib import Path

from framework.check_api import MARKDOWN_SUFFIXES, Finding, files_in_scope, matches_any, prose_only
from framework.prose import blocks

NAME = "topic"
EXACT = True

LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
BADGE = re.compile(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)|!\[[^\]]*\]\([^)]*\)")
INCLUDE = re.compile(r"\{\{<\s*include\s+([^\s>]+)\s*>\}\}")
WORD = re.compile(r"[^\W_]+(?:'[^\W_]+)?")


def words(text: str) -> int:
    """Words a reader sees: link addresses and markup removed."""
    return len(WORD.findall(re.sub(r"\]\([^)]*\)", "]", text)))


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("topic", {})
    patterns = settings.get("files", [])
    if not patterns:
        return []
    exempt = settings.get("exempt", [])
    root_topic = settings.get("root", "README.md")
    summary_words = settings.get("summary_words", 60)
    listing_words = settings.get("listing_words", 3)
    labels = [label.lower() for label in settings.get("summary_labels", ["summary", "abstract"])]
    within = settings.get("summary_within", 4)
    typed = set(settings.get("typed", []))
    shapes = settings.get("shapes", {})
    markdown = files_in_scope(root, config, MARKDOWN_SUFFIXES)
    topics = {path for path in markdown
              if path.endswith(".md") and matches_any(path, patterns) and not matches_any(path, exempt)}
    findings = []
    for path in sorted(topics):
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        findings += opening(path, text, summary_words, labels, within)
        findings += announced(root, path, text, shapes)
        if path == root_topic:
            continue
        parent = containing(path, topics)
        if parent is None:
            findings.append(Finding(NAME, path, 1, f"no containing topic: no path leads from {root_topic} to it"))
            continue
        findings += listing(root, parent, path, listing_words, typed)
    findings += cycles(root, markdown)
    return findings


def labelled(units: list, labels: list[str], within: int):
    """The summary a label announces among the first blocks after the title, or None."""
    for index, unit in enumerate(units[:within]):
        name = re.sub(r"^[\d.\s]+", "", unit.text).strip().rstrip(".:").lower()
        if unit.kind == "heading" and name in labels:
            return units[index + 1] if index + 1 < len(units) else None
        bold = re.match(r"^\*\*([^*]+?)[.:]?\*\*[.:]?\s*", unit.text)
        if unit.kind == "paragraph" and bold and bold.group(1).strip().lower() in labels:
            return type(unit)(unit.kind, unit.line, unit.text[bold.end():], unit.info)
    return False


def opening(path: str, text: str, summary_words: int, labels: list[str], within: int) -> list[Finding]:
    """The title first, then the summary that stands for the topic when it is folded."""
    units = blocks(text)
    titles = [unit for unit in units if unit.kind == "heading" and unit.info == "1"]
    if not units or units[0].kind != "heading" or units[0].info != "1":
        return [Finding(NAME, path, units[0].line if units else 1, "a topic opens with its title, one '# ' heading")]
    found = [Finding(NAME, path, title.line, "a second '# ' title: a topic has one title") for title in titles[1:]]
    following = [unit for unit in units[1:] if not (unit.kind == "paragraph" and not BADGE.sub("", unit.text).strip())]
    found_label = labelled(following, labels, within)
    summary = found_label if found_label is not False else (following[0] if following else None)
    if summary is None or summary.kind not in ("paragraph", "quote"):
        found.append(Finding(NAME, path, summary.line if summary else units[0].line,
                             "no summary after the title: one to three sentences that stand for the topic"))
    elif words(summary.text) > summary_words:
        found.append(Finding(NAME, path, summary.line,
                             f"a summary of {words(summary.text)} words, past {summary_words}: "
                             "it no longer stands for the topic when folded", "warning"))
    return found


def announced(root: Path, path: str, text: str, shapes: dict) -> list[Finding]:
    """A file declared of a shape links that shape's file."""
    found = []
    for name, patterns in shapes.items():
        if not matches_any(path, patterns):
            continue
        addresses = [match.group(2) for match in LINK.finditer(prose_only(text))]
        local = {target_of(path, address, root) for address in addresses}
        remote = {address.split("#")[0] for address in addresses if re.match(r"^https?://", address)}
        if f"shapes/{name}.md" not in local and not any(url.endswith(f"/shapes/{name}.md") for url in remote):
            found.append(Finding(NAME, path, 1, f"declared a {name} but does not link shapes/{name}.md: "
                                                "announce the shape, so a reader knows which blocks to expect"))
    return found


def containing(path: str, topics: set[str]) -> str | None:
    """The README.md of the nearest folder above that is a topic; for a README.md, above its own folder."""
    folder = posixpath.dirname(path)
    if posixpath.basename(path) == "README.md":
        if not folder:
            return None
        folder = posixpath.dirname(folder)
    while True:
        candidate = posixpath.join(folder, "README.md") if folder else "README.md"
        if candidate in topics and candidate != path:
            return candidate
        if not folder:
            return None
        folder = posixpath.dirname(folder)


def target_of(source: str, address: str, root: Path) -> str | None:
    """The repository path a relative link points to; a folder stands for its README.md."""
    if re.match(r"^[a-z][a-z0-9+.-]*:", address) or address.startswith("#"):
        return None
    address = address.split("#")[0]
    path = posixpath.normpath(posixpath.join(posixpath.dirname(source), address))
    if address.endswith("/") or (root / path).is_dir():
        path = posixpath.join(path, "README.md")
    return path


def listing(root: Path, parent: str, child: str, listing_words: int, typed: set[str]) -> list[Finding]:
    """The parent links the child, and the line that does so says more than the bare link, or the child is typed."""
    text = prose_only((root / parent).read_text(encoding="utf-8", errors="replace"))
    for number, line in enumerate(text.splitlines(), 1):
        for match in LINK.finditer(line):
            if target_of(parent, match.group(2), root) != child:
                continue
            if line.lstrip().startswith("|"):
                cells = line.strip().strip("|").split("|")
                beside = " ".join(cell for cell in cells if match.group(0) not in cell)
            else:
                after = line[match.end():]
                beside = after[:next_link.start()] if (next_link := LINK.search(after)) else after
            if words(beside) < listing_words and posixpath.basename(child) not in typed:
                return [Finding(NAME, child, 1, f"listed by {parent} (line {number}) as a bare link: "
                                                "list it with its summary", "warning")]
            return []
    return [Finding(NAME, child, 1, f"not listed by its containing topic {parent}: a reader cannot reach it from the root")]


def cycles(root: Path, markdown: list[str]) -> list[Finding]:
    """Each inclusion cycle once, from the first file met on it."""
    graph = {}
    for path in markdown:
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        graph[path] = [posixpath.normpath(posixpath.join(posixpath.dirname(path), target))
                       for target in INCLUDE.findall(text)]
    findings, state, reported = [], {}, set()

    def visit(node: str, trail: list[str]) -> None:
        state[node] = "open"
        for nxt in graph.get(node, []):
            if state.get(nxt) == "open":
                loop = trail[trail.index(nxt):] + [nxt] if nxt in trail else [node, nxt]
                key = frozenset(loop)
                if key not in reported:
                    reported.add(key)
                    findings.append(Finding(NAME, loop[0], 1, "inclusion cycle: " + " -> ".join(loop)))
            elif nxt in graph and state.get(nxt) is None:
                visit(nxt, trail + [nxt])
        state[node] = "done"

    for node in sorted(graph):
        if state.get(node) is None:
            visit(node, [node])
    return findings
