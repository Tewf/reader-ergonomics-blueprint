# AI-augmented topic

The topic as the one format a person, a language model and a checking program all work on. The person writes the
reasoning; programs check the writing and, where the reasoning is formal, the logic; the model helps between them.

> **Status:** moved out of reader-ergonomics-topic on 2026-10-29, with its history, into a repository of its own; its
> name and scope are being settled. The review of autoformalization is done, grey and formal, and names baseline B1;
> nothing of the loop is built yet.

## The loop

![The person writes topics; checks in CI return findings to the model; the model translates a formal topic into Lean, which returns errors and goals left open; the model returns guidance to the person: what to split, what is unclear, what the proof assistant rejected, and why.](readme-loop.svg)

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

The figure reads from the person downward; what comes back, errors and goals to the model and guidance to the person, runs upward. Each part has one role:

| Part | Role | Decides |
|---|---|---|
| **person** | owns the reasoning; writes each step as a topic | what is claimed |
| **checks** | programs: the [topic check](https://github.com/Tewf/reader-ergonomics-topic/blob/3ce8ec139fc08c2852f77e893b8bc38f073f668e/checks/local/topic.py) and the reader-ergonomics checks | whether the form is clear |
| **model** | a language model: explains, proposes, translates | nothing: its output is always checked |
| **proof assistant** | Lean, for what is formalized | whether the reasoning is valid |

The topic is the shared unit: what the person writes, what the checks read, what the model translates, and what one
Lean declaration mirrors.

## Scope

| | What | Why |
|---|---|---|
| in | the topic as the interface between a person, a model and a checker | the one problem of this extension |
| in | proofs written as topics and checked in Lean, as the first instance | a checker whose verdict is exact exists |
| in | what the model may do (explain, propose, translate) and what it may not (decide) | a model's output is checked, never trusted |
| in | the evidence, grey literature first: how practice joins informal writing, models and proof assistants | the tools move faster than papers |
| out | building a prover or training a model | others do it; this uses them |
| out | other formal targets, such as TLA+ or tests for code, for now | one instance first; named, not reviewed |
| out | AI writing assistants with no checker behind them | without an exact verdict, nothing closes the loop |

## Questions the review must answer

- **Prior art.** Who already joins structured informal writing to a proof assistant, and what does each way ask of
  the writer?
- **Translation.** How faithful is a model's translation of an informal statement into Lean, and how is a wrong
  translation caught, a correct proof of the wrong statement?
- **Feedback.** How is a proof assistant's output turned into guidance a person can act on?
- **Form.** Does a format that obliges the writer to split reasoning into small claims help the person think, or only
  the machine check?
- **Limits.** Where does the loop fail: a wrong translation, reliance on the model, claims no checker can decide?

## The baseline, named by the grey review

The grey pass of the review, [autoformalization](../evidence/autoformalization/), named one baseline:

- **B1, the audited blueprint**: a blueprint of small lemmas, each copied from its source. A model may write proofs
  and decides nothing. Lean checks every submission in CI, and comparator checks that the proof proves the stated
  claim. A person audits each statement against its source.
- It confirms the first candidate named before the review, a blueprint project built in CI. Neither side found
  practice naming the other two, a controlled natural language or plain Lean with a model, as a baseline.
- The formal pass and an audit of every number come next; the [baseline](../evidence/autoformalization/baseline.md)
  says how a comparison with the loop would be measured.

## Where it sits

- It builds on the [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/3ce8ec139fc08c2852f77e893b8bc38f073f668e/shapes/topic.md) and its check. A node template drafted earlier, unpublished, already
  gave each claim a Lean file; it is the starting point, not the baseline.
- Structured proofs are reviewed in reader-ergonomics-academic, `evidence/mathematical-writing`; this extension links
  that review and does not repeat it.

## See also

The [repository's front page](https://github.com/Tewf/reader-ergonomics-topic/blob/3ce8ec139fc08c2852f77e893b8bc38f073f668e/README.md), the parent of this folder.
