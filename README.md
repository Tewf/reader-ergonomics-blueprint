# Blueprint

[![Checks against reader-ergonomics](https://github.com/Tewf/reader-ergonomics-blueprint/actions/workflows/checks.yml/badge.svg)](https://github.com/Tewf/reader-ergonomics-blueprint/actions/workflows/checks.yml)
[![Site](https://github.com/Tewf/reader-ergonomics-blueprint/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/reader-ergonomics-blueprint/)

A person's reasoning written as a tree of topics, each part with a checker, Lean for logic first. A language model
interprets the verdicts and guides, so the person does not get lost and the reasoning can be communicated. Formal
mathematics calls such a graph of checked claims a **blueprint**.

This page in French: [README.fr.md](README.fr.md).

> **Audit (2026-11-03):** the three claims' prose was verified against Euclid IX.20 (Joyce 1996) and its factorial variant
> (Wikipedia 2026 Euclid) by a model on the maintainer's order, not by a person; the Lean statements wait for a reader of Lean.
>
> **Status (2026-11-03), release 0.1.0:** the review of autoformalization is done, grey and formal, 273 sources, and names its
> baseline, B1. B1 is built in miniature, except the audit: Euclid's theorem as a theorem topic and three claim
> topics, each naming one Lean declaration ([design](design/first-build.md)), with a challenge file that holds the
> four statements apart from the proofs ([0006](decisions/0006-a-challenge-file-holds-the-audited-statements.md)).
> Five checks run in CI: the topic check, a claim check, a link check, a comparator, and Lean. The [card](standard.md)
> holds five principles and one [shape](shapes/claim.md), the claim. The maintainer has not yet compared
> the statements with their source. The model is not in the loop yet. The work began in reader-ergonomics-topic and
> moved here with its history ([0001](decisions/0001-a-repository-of-its-own.md)).
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. Corrections are welcome as issues.

## Take it

The blueprint is meant to be copied and kept as your own. Copy it from a tagged release
([tags](https://github.com/Tewf/reader-ergonomics-blueprint/tags)), so a later change here never changes your copy.

1. Copy [shapes/claim.md](shapes/claim.md), the shape, and the checks in [checks/local/](checks/local/):
   `claim_shape.py`, `lean_link.py`, `comparator.py` and `topic.py`, into the same paths of your repository.
2. Write each step of your reasoning as a claim topic, and name one Lean declaration on its **Lean:** line. Keep the
   statements to audit in a challenge file, apart from the proofs, as [Blueprint/Challenge.lean](Blueprint/Challenge.lean) does.
3. Add `checks/config.toml` with `extends = "reader-ergonomics"` and the tables of this repository's own for
   `[topic]`, `[claim_shape]`, `[lean_link]` and `[comparator]`; set their paths to yours.
4. Pin the standard by commit and run the checks, one command:

   ```sh
   git clone https://github.com/Tewf/reader-ergonomics ../reader-ergonomics
   git -C ../reader-ergonomics checkout b9732b9814c71768f722691f3c5049ec2b8ed378   # v1.19.2
   python3 ../reader-ergonomics/checks/run.py .
   ```

   Lean is built apart, in CI, with `lake build`; the checks read the declarations' names and never run Lean.

A disagreement has three places to go:

- your reader style, as an override with its reason, when it is about your reader;
- an extension, when it is about a genre;
- an issue on [this repository](https://github.com/Tewf/reader-ergonomics-blueprint/issues), when its evidence or its shape is wrong.


The standard's section, [Take your own version](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/README.md#take-your-own-version), gives the rest.

## Where it sits

- **It builds on the [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/shapes/topic.md)** (reader-ergonomics-topic v0.6.0): every node of a blueprint is a
  topic, with its title, its summary, its parts as contents and what it uses as links.
- **It obeys [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/standard.md)** (v1.19.2) and runs its checks in CI.
- **It links down only.** Both are pinned by commit; neither links up to this repository.

## The loop

![The person writes topics; checks in CI return findings to the model; the model translates a formal topic into Lean, which returns errors and goals left open; the model returns guidance to the person: what to split, what is unclear, what the proof assistant rejected, and why.](loop.svg)

<details>
<summary>Graphviz source</summary>

```dot
// The loop of the AI-augmented topic: the figure of ai-augmented/README.md.
// Colours: one per kind of part, the same in every figure of this extension; each kind is also named in its box.
// person orange, program blue, model green, proof assistant blue (a program); a back edge returns to its sender.
digraph loop {
  graph [rankdir=TB, nodesep=0.5, ranksep=0.55, bgcolor="white", pad=0.2, fontname="Inter"];
  node  [shape=box, style="rounded,filled", fontname="Inter", fontsize=13, margin="0.2,0.1", penwidth=1.5, fontcolor="#1F2328"];
  edge  [fontname="Inter", fontsize=11, color="#3D434B", fontcolor="#55575F", penwidth=1.3, arrowsize=0.8];
  P [label=<<b>person</b><br/><font point-size="11" color="#55575F">writes the idea as topics: one claim</font><br/><font point-size="11" color="#55575F">each, its summary, its parts</font>>, fillcolor="#FBEDE4", color="#B4541A", penwidth=2.6];
  C [label=<<b>checks, in CI</b><br/><font point-size="11" color="#55575F">the form: title, summary, one claim</font><br/><font point-size="11" color="#55575F">per topic, every part listed</font>>, fillcolor="#E8EEF8", color="#2F5DA8"];
  M [label=<<b>model</b><br/><font point-size="11" color="#55575F">explains findings, proposes clearer</font><br/><font point-size="11" color="#55575F">wording; translates a formal topic</font><br/><font point-size="11" color="#55575F">into Lean</font>>, fillcolor="#E6F2EA", color="#2E7D4F"];
  L [label=<<b>proof assistant</b><br/><font point-size="11" color="#55575F">Lean checks the reasoning</font>>, fillcolor="#E8EEF8", color="#2F5DA8"];
  P -> C [label=" topics"];
  C -> M [label=" findings"];
  M -> L [label=" Lean"];
  L -> M [label=" errors, goals\l left open\l"];
  M -> P [label=" guidance: what to split, what is\l unclear, what the proof assistant\l rejected, and why\l"];
}
```

</details>

The figure reads from the person downward; what comes back, errors and goals to the model and guidance to the person,
runs upward. Each part has one role:

| Part | Role | Decides |
|---|---|---|
| **person** | owns the reasoning; writes each step as a topic | what is claimed |
| **checks** | programs: the [topic check](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/checks/local/topic.py) and the reader-ergonomics checks | whether the form is clear |
| **model** | a language model: explains, proposes, translates | nothing: its output is always checked |
| **proof assistant** | Lean, for what is formalized | whether the reasoning is valid |

## Scope

| | What | Why |
|---|---|---|
| in | any reasoning or creation, written as a tree or graph of topics | a topic can hold any information |
| in | the topic's properties on every node: title and summary, parts as contents, uses as links, no cycle, three levels in view | the person does not get lost, and the reasoning can be communicated |
| in | a checker for each part | each claim is checked where it stands, not the whole at the end |
| in | Lean as the oracle for logic and proofs, the first and for now only checker of meaning | its verdict is exact |
| in | the model as interpreter of the verdicts and as guide; it decides nothing and never splits for the person | conditions 2 and 4 of the review's [position](evidence/autoformalization/position.md) |
| later | other checkers (sources, tests, specifications), after a review of assurance cases | a claim split into sub-claims each backed by evidence is what systems engineering calls an assurance case |
| out | building a prover or training a model | others do it; this uses them |
| out | the topic template itself | reader-ergonomics-topic holds it; this repository pins a release |

## What the review found

The [review](evidence/autoformalization/) reads 80 grey and 182 formal sources, with 11 linked from sibling reviews.

- No program decides whether a formal statement means what its source means; research measures it against people or
  a vetted reference.
- Model judges overrate translations: one translator scored 97.5% by its judge and 62.7% by people. Benchmarks' own
  human-written statements are wrong in 16.4% and 38.5% of two benchmarks.
- For a model, the checker's error message is what makes repair work; for people, no study of a proof assistant's
  messages was found.
- Splitting reasoning into small claims helps checking every time, and thinking only where the person did the
  splitting; no randomised trial was found.

## The baseline

**B1, the audited blueprint** ([baseline](evidence/autoformalization/baseline.md)):

- a blueprint of small lemmas, each statement copied from its source;
- a model may write proofs, and decides nothing;
- Lean checks every submission in CI, and comparator checks that each proof proves the stated claim;
- a person audits each statement against its source.

## Next

1. **The audit of B1:** the maintainer compares each of the four statements in
   [the challenge file](Blueprint/Challenge.lean) with its source and writes the date on the topic's **Audited:** line.
   The comparator and the challenge file are in; the audit is the one part of B1 that is not.
2. **Then the loop:** the model's place in it, as interpreter and guide, measured against B1.
3. **Before any checker other than Lean:** a review of assurance cases, the field's name for the general case.

## Contents

| Part | Summary |
|---|---|
| [standard](standard.md) | the card: five principles, two of them on the statement a person audits and two on the claim a person writes, each with its grade |
| [principles](principles/) | one file per principle, with its claim, grade, evidence and check |
| [shapes](shapes/) | the claim: the skeleton of one claim of a proof, with the three claims of Euclid's theorem as its examples |
| [design](design/) | the designs proposed before a build: the first build is Euclid's theorem as topics checked by Lean |
| [proofs](proofs/infinitely-many-primes/) | Euclid's theorem as a theorem topic and three claim topics, each naming its Lean declaration |
| [evidence](evidence/) | the review behind the repository: autoformalization, grey and formal, and its bibliography |
| [decisions](decisions/) | one record per choice that shapes this repository, each opening with the decision in one sentence |

## Check it

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py path/to/this/repository
```

CI runs the same checks on every push, at the commits [checks.yml](.github/workflows/checks.yml) pins.

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish, with
credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
