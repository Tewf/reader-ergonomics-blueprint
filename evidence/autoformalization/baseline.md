# Baseline: what the loop is compared against

Step 5 of the grey pass: the baseline the loop must beat, read from both sides' proposals. Terms are defined in [frame](frame.md); the findings behind each line are in [review](review.md).

## Two proposals, one baseline

The formal side names a blueprint project whose statements sit in a comparator challenge file with a formalization.yaml, checked in CI, with fidelity left to a human audit.
The human side names the PNT+ workflow.
Drawn as two sets, they share their core and differ only at the edges:

```text
   formal side's proposal                                           human side's proposal
 ┌──────────────────────────────┬──────────────────────────────────┬──────────────────────────────────┐
 │ challenge file, short and    │ a blueprint: one node per        │ statements copy the paper and    │
 │ read by a person             │ statement, tied to its Lean name │ keep its citation                │
 │ comparator in CI: the same   │ a model may write the proofs     │ bite-sized lemmas, each claimed  │
 │ statement, permitted axioms  │ Lean decides them, in CI         │ as a task                        │
 │ formalization.yaml table     │ a person audits each statement   │ AI use disclosed, labelled in CI │
 │ model judge as a filter only │ against its source               │ a cap on open AI pull requests   │
 └──────────────────────────────┴──────────────────────────────────┴──────────────────────────────────┘
        program checks of the          the shared core                 rules of a running project
        statement                                                      for the person's side
```

- They are one baseline, not two: both are a blueprint project in which a model may write proofs, Lean decides them in CI, and a person audits each statement against its source.
- The formal side's edge checks by program that the statement proved is the statement claimed; the human side's edge sets what the person does around it. Neither excludes the other.
- PNT+ already enforces LeanArchitect's `@[blueprint]` attribute (PNT-plus 2026, sections 6 and 12). Whether it runs comparator or keeps a formalization.yaml was not read by either side.

## The named baseline

**B1, the audited blueprint**: the PNT+ workflow (PNT-plus 2026; Tao 2026e) with the Palomar minimum, a challenge file checked by comparator and a formalization.yaml (Palomar 2026; Lean FRO 2026a; Mathlib Initiative 2026; MathOverflow 2026).

| Part of the loop | What B1 does | Source, with where |
|---|---|---|
| person writes | a blueprint of small lemmas, each statement copied from the paper with its citation, each lemma claimed as a task | PNT-plus 2026, section 3; Tao 2026e |
| model | writes proofs, with its use disclosed in the pull request; decides nothing | PNT-plus 2026, section 13, rule 1 |
| checks in CI | Lean typechecks every submission; the blueprint is built, by `checkdecls` with leanblueprint or by `lake build :blueprint` with LeanArchitect; comparator checks the solution module proves exactly the challenge file's statements, with permitted axioms; a job labels AI-assisted pull requests | Tao 2026e; Massot 2026; Zhu 2026; Lean FRO 2026a; PNT-plus 2026, section 13, rule 1 |
| statement fidelity | a person audits each statement against its source, definitions included; a model judge only filters | Hales 2026; Buzzard 2025; Paulson 2026; Palomar 2026 |
| guidance to the person | mechanisms written ahead of time: named errors, `Try this` suggestions | Lean FRO 2025; Lean FRO 2026d |
| review load | at most 3 open AI-assisted pull requests per contributor | PNT-plus 2026, section 13, rule 7 |

- It confirms the README's first candidate, a Lean blueprint project with a dependency graph built in CI. It adds the challenge file, comparator and the alignment table (formal side), and the project's rules for the person (human side).
- The README's two other candidates were named as baselines by neither side: a controlled natural language a machine checks, and plain Lean with a model in the editor. The grey pass holds no measure of either for a writer (review Q1, Q3).

## How a comparison would be measured

| Question | What the sides proposed | Records that exist in practice |
|---|---|---|
| Does the loop catch what B1 lets through? | whether the loop's topic check and model audit find misformalizations that this workflow lets through (human side) | the misformalization label and its counts (GitHub 2026f); the audit's flagged files and trivially settled statements (Adamczewski 2026) |
| Can a model judge stand in for the person? | an agreement rate of a model judge against people, which Palomar does not publish (formal side) | Palomar's two runs of one repository, scored 5 then 4 (Palomar 2026) |
| Does guidance help the person? | any measure of guidance given to a person (formal side) | none found on Lean; studies on C and Python, in [formal leads](formal-leads.md) |

- These are the sides' proposals for the formal pass, not results; no grey source ran any of these comparisons.
