# Autoformalization: how practice joins a person's reasoning, a model and Lean, and catches the wrong statement

The review of the AI-augmented topic, its grey and formal passes merged. It asks how practice and research join informal reasoning to Lean through a model, and catch a correct proof of the wrong statement. It asks how the verdict returns to a person as guidance, and what that does to the person's thinking.

- It holds 264 sources: 80 grey, 173 formal, and 11 works linked from sibling reviews.
- Grey: 44 tier 2 and 36 tier 3, of which 9 score below the threshold and serve as examples only; no tier 1, and no
  controlled study of the loop.
- Formal: 64 measured, 31 measured descriptively or qualitatively, 15 supported with caveat, 52 convention, argument or review, 11 not graded or located only.

## Files

| File | Role |
|---|---|
| [frame](frame.md) | step 1: the loop's problem, every term once, and the five questions mapped to each side and strand |
| [protocol](protocol.md) | how each side of the grey pass and each strand of the formal pass searched, selected and graded, and how they were merged and audited |
| [sources](sources.md) | the flow for both passes, then each work with its grade or score |
| [review](review.md) | step 2: the findings, by prior art, translation, feedback, form and limits, grey and formal together |
| [state of the art](state-of-the-art.md) | step 3: the best evidence per question, upper bounds apart from lower bounds, and the practice most adopted beside it |
| [position](position.md) | step 4: what the evidence allows the topic to claim, under four conditions, and what is not known |
| [against](against.md) | accuracies that shrink when people re-judge them, null results on people, and benchmarks that are wrong |
| [baseline](baseline.md) | step 5: the audited blueprint, B1, and how fidelity and guidance would be measured against it |
| [bibliography](../bibliography.md) | every work cited, one row each, with a stable link |
| `flow.json` | the formal pass's flow as data, drawn in the figure of [sources](sources.md) |

## Claims

| Claim | Grade | Where |
|---|---|---|
| Blueprint projects join informal statements to Lean declarations, checked in CI: leanblueprint lists 37 projects; Palomar held 845 results from 660 projects at the formal side's read of 2026-10-29, 847 from 661 later that day | convention, untested, for the writer; the counts measured, descriptive | review.md Q1 |
| The person's work moves from writing proofs to scoping tasks, checking statements and digesting output | practice reports | review.md Q1, Q4 |
| Model help saves time: practitioners estimate large savings; the one measurement found no significant effect on time (7 people) while correct formalizations rose by 0.30 | practice estimates against one small study, measured | review.md, where the two passes disagree; Q4, C3 |
| Controlled and declarative proof languages are well described; no study found measured their effect on a writer or reader, and the only controlled comparison of proof form concerns models | convention, untested, for people; measured, for models | review.md Q1 |
| Structure helps machines: removing the informal proof costs 5.3 points on miniF2F test in Isabelle, within 100 attempts | measured, one ablation | review.md Q1 |
| Translations are often wrong: judged by people, the best system per benchmark is right on 13.4% to 90.6% of statements; a model judge gave 97.5% where people gave 62.7% | measured, on each benchmark | review.md Q2 |
| Benchmarks are wrong too: 16.4% of miniF2F's and 38.5% of ProofNet's human-written statements; and Formal Conjectures carries 787 misformalization labels | measured; the label count measured, descriptive | review.md Q2 |
| No program decides statement fidelity: research measures it against people or a vetted reference; BEq+ against a reference has precision 98.0% and recall 48.3% | supported with caveat: stated by the field and argued from computability, not proved | review.md Q2; state-of-the-art.md |
| Model judges of fidelity err: the best on a binary task is wrong on 14.2%; a registry's judge scored one commit 5, then 4 | measured, on a benchmark; the registry's case its owner's report | review.md Q2 |
| For people, better error messages help in some controlled studies and not in others, on programming languages; one randomised trial found model explanations helped; no study of a proof assistant's messages read by people was found | measured, mixed, on programming languages; on proofs, descriptive only | review.md Q3 |
| For a model, the checker's error message is what makes repair work, mostly on shallow errors; Lean feedback repairs form more than meaning | measured, on benchmarks; the last in two preprints | review.md Q2, Q3 |
| Model feedback on informal writing is measured only by its owner's survey (97% found it helpful); research finds preference and performance apart | owner's claim; measured, two studies | review.md Q3; where the two passes disagree |
| Splitting into small claims helps checking and sharing; it is reported to help thinking where the person did the splitting; students who chose a proof assistant wrote more explicit proofs, and where a control existed grades did not differ | practice reports; supported with caveat (self-selected groups); no randomised trial | review.md Q4 |
| People read the statement they expect: experts repaired misstated problems in their heads, and students missed unfaithful steps shown as verified | measured, descriptive | review.md Q5, C5 |
| The loop fails where no checker decides: a misformalized statement, an unrepeatable judge, kernel bugs, over-reliance robust in experts, review as the bottleneck | practice reports; over-reliance measured, outside proofs | review.md Q5 |
| Formal text is several times longer than the informal one: a de Bruijn factor of about four | measured, descriptive | review.md Q5, C7 |
| The two sides' proposed baselines are one, B1, and the formal pass names none stronger | the reviewers' synthesis | baseline.md |
| The topic can be the loop's interface under four conditions: a short statement checked against a vetted one, the checked statement shown, guidance at the person's grain, the splitting left to the person | supported with caveat, as a design; untested | position.md |

## Named baseline

- **B1, the audited blueprint**: the PNT+ workflow, with the Palomar minimum. It holds after the formal pass, which names no workflow measured against it.
- The workflow: a blueprint of small lemmas copied from the paper, model proofs disclosed, Lean in CI, a person auditing each statement.
- The minimum: a challenge file checked by comparator, and a formalization.yaml mapping each source statement to its Lean name.
- Fidelity would be measured by people against the source, by BEq+ against the challenge file, and by model judges reported with their accuracy; guidance, by what the person does next ([baseline](baseline.md)).

## Status

Both passes are in: the grey pass and the formal pass, in three strands, each number audited against its source. Three papers are still in the university queue: Knobelsdorf 2017, Tymoczko 1979 and Avigad 2019. Four others, Wang 2024b, Hentschel 2016, Aitken 2000 and Becker 2019, were read there and applied in strand B.
