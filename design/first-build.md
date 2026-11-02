# The first build: Euclid's theorem as topics checked by Lean

**Decision asked.** Whether the first build is one classical theorem written as a tree of topics. Each claim is tied
to one Lean declaration, and three checks run in CI. The maintainer decides before the build is pushed.

**Status.** accepted, 2026-11-03. **Shape:** [design document](https://github.com/Tewf/reader-ergonomics-software-design/blob/48b497ba591e9d6ffc962b1d08448930fa8158de/shapes/design-document.md)

**Summary.** The smallest blueprint that exercises every part of the loop but the model: Euclid's theorem, three
claims, one topic each, one Lean declaration each. A program checks the form of the topics, a second program checks
that every topic names a declaration that exists, and Lean checks the proofs.

## Motivation

The review names the baseline, B1, and nothing of it is built. A first build shows that the pieces meet before
the model joins them.

- Use case: a person writes a short proof as topics. Today nothing says whether a topic's Lean declaration exists,
  or whether Lean accepts it.
- Use case: a reader of the proof wants to see each claim alone, and the one it depends on, without the others.

## Goals and non-goals

- Goal: every claim is its own topic, and the topic check passes on each.
- Goal: every topic under `proofs/` names exactly one Lean declaration, and that declaration is in the Lean sources.
- Goal: `lake build` in CI proves the declarations and fails on any `sorry`.
- Non-goal: a model in the loop. It comes next, measured against B1.
- Non-goal: comparator and a challenge file. They finish B1 and come after this build.
- Non-goal: a checker other than Lean. It waits for a review of assurance cases.

## Design

![The theorem topic lists three claim topics; the second uses the first, the third uses the second; each names one Lean declaration.](first-build.svg)

<details>
<summary>Graphviz source</summary>

```dot
digraph first_build {
  graph [rankdir=TB, nodesep=0.5, ranksep=0.5, bgcolor="white", pad=0.2, fontname="Inter"];
  node  [shape=box, style="rounded,filled", fontname="Inter", fontsize=13, margin="0.2,0.1", penwidth=1.5, fontcolor="#1F2328"];
  edge  [fontname="Inter", fontsize=11, color="#3D434B", fontcolor="#55575F", penwidth=1.3, arrowsize=0.8];
  T  [label=<<b>theorem</b><br/><font point-size="11" color="#55575F">for every n, a prime greater than n</font>>, fillcolor="#FBEDE4", color="#B4541A", penwidth=2.6];
  C1 [label=<<b>claim 1</b><br/><font point-size="11" color="#55575F">a number at least 2 has a prime factor</font>>, fillcolor="#FBEDE4", color="#B4541A"];
  C2 [label=<<b>claim 2</b><br/><font point-size="11" color="#55575F">n! + 1 has a prime factor p</font>>, fillcolor="#FBEDE4", color="#B4541A"];
  C3 [label=<<b>claim 3</b><br/><font point-size="11" color="#55575F">p exceeds n</font>>, fillcolor="#FBEDE4", color="#B4541A"];
  L  [label=<<b>Lean</b><br/><font point-size="11" color="#55575F">one declaration per topic</font>>, fillcolor="#E8EEF8", color="#2F5DA8"];
  T -> C1 [label=" contains"];
  T -> C2 [label=" contains"];
  T -> C3 [label=" contains"];
  C2 -> C1 [label=" uses", style=dashed];
  C3 -> C2 [label=" uses", style=dashed];
  C1 -> L [label=" names", style=dotted];
  C2 -> L [style=dotted];
  C3 -> L [style=dotted];
  T -> L [style=dotted];
}
```

</details>

- **Theorem and claims:** the theorem, in `proofs/infinitely-many-primes/`, holds three claims as its
  contents, one file each beside it. Each opens with a title and a summary, as every topic does.
- **Link to Lean:** each topic carries one line, `**Lean:** \`Blueprint.InfinitelyManyPrimes.<name>\``.
- **Lean project:** a Lake project at the root, on Mathlib, its toolchain taken from Mathlib's tag.
- **Three checks, three CI steps:** the topic check; `checks/local/lean_link.py`, which reads the Lean sources
  and the topics and compares the names; `lake build`, with Mathlib's cache.

The records [0003](../decisions/0003-euclids-theorem-as-the-first-proof.md) to
[0005](../decisions/0005-three-checks-each-its-own-ci-step.md) keep each choice.

## Alternatives

| Option | Consequences | Why it lost |
|---|---|---|
| A longer theorem (irrationality of the square root of 2, a lemma of a course) | more claims, nearer to use | the build would test the theorem, not the pipeline |
| Core Lean without Mathlib | no cache to fetch, a fast build | the claims would be proved from scratch, and the miniature becomes a library |
| One checker for link and build, in `lake` | one step | a missing name and a failing proof are different findings; a program can say which |
| Match topic to declaration by file name | no `**Lean:**` line | a rename of either breaks the link silently, and the line is what a reader sees |

## Consequences

- Drawbacks: Mathlib is large, so a cold CI run is slow without the cache, and the Lake manifest pins one Mathlib
  version that a later bump must move.
- Risks: the link check reads names, not meaning. Nothing here shows that a Lean statement says what its topic says.
  That is the audit of B1, done by a person, and comparator does not replace it.
- Compatibility: the topic check and the standard's checks run unchanged on the new folder.
- Security: CI runs `lake exe cache get` from Mathlib's public cache, and no secret.

## Feasibility and plan

- Shown to work by: each claim is a one-line Mathlib lemma or close to it, and the proof was built locally.
- Tested by: the topic check, unit tests for the link check, and `lake build` without `sorry`.
- Rolled out by: this design, the records, the proof as topics, the Lake project, the link check, the CI steps, in
  that order, one commit each.

## Open questions

- Whether the link check should also read the declaration's statement, to show it beside the topic. Not decided.
