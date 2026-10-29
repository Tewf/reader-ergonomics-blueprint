# Autoformalization: how practice joins a person's reasoning, a model and Lean, and catches the wrong statement

The grey pass of the AI-augmented topic, its two sides merged. It asks how practice joins informal reasoning to Lean through a model, catches a correct proof of the wrong statement, and returns the verdict to a person.
It holds 80 grey sources: 44 tier 2, 36 tier 3, 9 below the threshold; no tier 1, no controlled study.

## Files

| File | Role |
|---|---|
| [frame](frame.md) | step 1: the loop's problem, every term once, and the five questions mapped to both sides |
| [protocol](protocol.md) | how each side searched, selected and scored, and how the two were merged |
| [sources](sources.md) | the flow per side and in total, then each source with its score |
| [review](review.md) | step 2: the findings, by prior art, translation, feedback, form and limits |
| [baseline](baseline.md) | step 5: the two sides' proposals read as one baseline, and how it would be compared |
| [bibliography](../bibliography.md) | every work cited, one row each, with a stable link |
| [formal leads](formal-leads.md) | papers, benchmarks and authors met, for the formal pass, not reviewed |

## Claims

| Claim | Grade | Where |
|---|---|---|
| Blueprint projects join informal statements to Lean declarations, checked in CI: leanblueprint lists 37 projects; Palomar held 845 results from 660 projects at the formal side's read of 2026-10-29 | convention, untested; the counts measured, descriptive | review.md Q1 |
| The person's work moves from writing proofs to scoping tasks, checking statements and digesting output | practice reports; the time saved is the practitioners' own estimate | review.md Q1, Q4 |
| Readable formal languages ask for fixed phrasing, or for intermediate statements where a prover fails; their effect on writers is reported only by owners | convention, untested | review.md Q1 |
| Prover and translator scores are their owners' claims; one result was checked by someone else: Buzzard compiled the FLT proof and comparator passed | owners' claims, one independent check | review.md Q2 |
| Misformalization is common and passes Lean: 787 Formal Conjectures items carry the label; a model audit flagged 139 of 1,268 files, and Lean settled 56 of those trivially | measured, descriptive (counts on public records) | review.md Q2 |
| No program decides statement fidelity: comparator checks a solution against a challenge file, and a person audits the challenge | convention | review.md Q2 |
| A model judge of fidelity is not repeatable: one repository at one commit scored 5, then 4 | measured, the owner's own report | review.md Q2 |
| Guidance reaches people through mechanisms written ahead of time, and models through errors and goals; no grey source measured guidance for a person | convention, untested | review.md Q3 |
| Model feedback on informal writing is measured only by its owner's satisfaction survey: 97% of consenting respondents found it helpful | owner's claim, a survey | review.md Q3 |
| Splitting into small claims helps checking and sharing; it is reported to help thinking only where the person did or followed the splitting | practice reports, untested | review.md Q4 |
| The loop fails where no checker decides: a misformalized statement, an unrepeatable judge, kernel bugs, long model output that makes review the bottleneck | practice reports | review.md Q5 |
| The two sides' proposed baselines are one | the reviewers' synthesis of both sides | baseline.md |

## Named baseline

- **B1, the audited blueprint**: the PNT+ workflow, with the Palomar minimum.
- The workflow: a blueprint of small lemmas copied from the paper, model proofs disclosed, Lean in CI, a person auditing each statement.
- The minimum: a challenge file checked by comparator, and a formalization.yaml mapping each source statement to its Lean name.
- The formal side proposed the second, the human side the first; they share one core and are one baseline ([baseline](baseline.md)).

## Status

This is the grey pass. The state of the art, the position and the case against wait for the formal pass, whose leads are in [formal leads](formal-leads.md).
