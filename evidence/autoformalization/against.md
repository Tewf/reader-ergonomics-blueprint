# Against: null results, failed replications, critiques and the limits of the measures

This file gathers the evidence against the claims of [review](review.md) and [state of the art](state-of-the-art.md), for all five questions. It holds accuracies that shrink when people re-judge them, null results on people, weak designs, and benchmarks that are themselves wrong. Terms are defined in [frame](frame.md).

## Answer first

- Reported translation accuracies shrink when people re-judge them, and the benchmarks that measure them are wrong in a sixth to nearly two fifths of their statements.
- One argument holds that faithfulness cannot be decided at all.
- Better error messages help people in some controlled studies and not in others, and preference is not performance.
- Every positive effect of a proof assistant on paper proofs comes from groups that chose to use it.

## Failed replications: accuracy re-judged by people

| Claim | Re-judged | Source, with where |
|---|---|---|
| a translator reports 96.7% on miniF2F-test, checked by compile and a model back-translation | people found 62.7% for the same translator on miniF2F v1 test at 128 samples, where its judge gave 97.5% | Gao 2025, section 1; Ospanov 2025, Table 2 |
| translation and proving each near their reported best, about 97% and 69% | chained and judged against the informal problem, about 36% | Ospanov 2025, abstract (secondary) |
| compile rates of 87.2% for the best agent | 57.7% accepted, and people confirmed 23.8 of the 29.5 point gap as real errors | Zhang 2026, section 1 |
| challenge entrants compile 61.6% on average | SA-Pass soft gives 11.1% on average, a gap of about 5.5 times | Han 2026, appendix G |


## Null results

| Source | What was not found, with where |
|---|---|
| Dai 2026 | Lean feedback did not reduce semantic errors: semantic-only failures fell by 5 to 6 of 16, not significant by bootstrap (section 5.1) |
| Zhang 2026 | nearly half of the compile gain an agent got from Lean feedback failed the semantic criterion (section 1, ablation in section 5) |
| Kim 2026b | no systematic gaming: with compile rates of 87% to 99% on 303 logic problems, models preferred reporting failure to forcing a proof; the authors add that unfaithfulness may still evade their signals (abstract, secondary) |
| Denny 2014 | enhanced error messages showed no significant effect in a controlled study (abstract, secondary) |
| Pettit 2017 | over several semesters, enhanced messages showed no measurable benefit, though surveys and instructors called the tool helpful (abstract, secondary) |
| Prather 2017 | a think-aloud study of 31 students found no substantial gain in learning outcomes over the control (abstract, secondary) |
| Santos 2024 | model-written messages beat stock compiler messages on time-to-fix in only 1 of 6 tasks, with 106 students (abstract, secondary) |
| Moraru 2026 | model rewrites were rated clearer but did not improve fix rate, attempts or time, with 103 participants (abstract, secondary) |
| Otte 2026 | the number of exercises done in Waterproof had no significant effect on the quiz grade, p = 0.101 (Table 3); the effect on the learning process was inconclusive (section 4.2) |
| Bottoni 2025 | Lean volunteers did not score significantly better in the interviews, p = 0.54 (Table 21) |
| Collins 2026 | model access did not change the time to formalize significantly, p = 0.797 (section on accuracy) |
| Fan 2025 | the model group improved its essays, with no difference in knowledge gain or transfer (abstract, secondary) |
| Fuller 2014 | structured proofs, against linear ones, were mostly no better for comprehension; held by the mathematical-writing review, section 5 |

## Why the results on people disagree

- Prather 2017 lists five reasons: students do not read messages, studies measure the wrong thing, effects are hard to measure, messages are badly designed, or cognitive load hides good ones (abstract).
- The positive trial counted repeats and attempts in an online course (Wang 2024b); the null ones timed fixes, in two lab sections (Santos 2024) and online (Moraru 2026). These are different outcomes, and both stand.
- Preference is not performance: students preferred model explanations while not fixing faster (Santos 2024, section 1); subjective gains did not reach objective ones (Moraru 2026).
- Mihaylova 2026 reports an association in course data, not a randomised effect (abstract).
- The deployment with 2,565 students has no control group, and its explanations often gave the solution against instructions (Taylor 2024b, abstract).

## Critiques of the measures of faithfulness

| Critique | Source, with where |
|---|---|
| compile rate certifies form only: its correlation with human accuracy across models is 0.655, against 0.974 for BEq+ | Poiroux 2025, Table 2 |
| yet at system level a ranking by compile rate matched experts at rho 0.99, while a model judge reached 0.72; the authors call system-level ranking coarse, so agreement on rankings says little about single statements | Han 2026, appendix F |
| BEq+ is precise but misses half of the faithful outputs, recall 48.3%; BEq-style checks need a correct reference, which practice rarely has | Poiroux 2025, Table 1 |
| model judges err on 14.2% or more of a binary task that is easier than translation | Chen 2025, section 4.5 |
| a model judge scored lowest among the measures compared, below a trained scorer and below people | Lu 2025, section 4.4 |
| people are an imperfect reference: experts agreed at kappa 0.81, and matched reference labels on 79.58% of items | Mohammad 2026, section 11.3; Lu 2025, section 4.4 |
| many validations are small or circular: 59 audited cases, 150 statements judged by the authors, judges validated by the teams that built them | Zhang 2026; Wu 2022; Yu 2025c; Peng 2025 |
| the four drift classes of one certifier were found in a pilot on 400 outputs of a single translator; its numbers come from one preprint and its own benchmark | Mohammad 2026, section 3, the pilot reported in section 10 |
| a model judge in practice is not repeatable: one commit scored 5, then 4, and no agreement rate against people is published | Palomar 2026, About, last section on scores |

## Limits of the measures of people

| Limit | Source, with where |
|---|---|
| correctness is binary, one grader per problem, and its authors call it subjective | Collins 2026, Analysis methodology |
| accuracy is judged against a course rubric: a valid step finer than the rubric counts as wrong | Guo 2026b, section 7.2.1 |
| exam and quiz grades may miss the effect: more explicit proofs, no grade difference, read as a difference the rubric does not score | Otte 2026, section 4.1 |
| proofs scored from 0 to 4 on a scheme adapted from earlier work | Thoma 2022, analysis, Step 2 |
| six problems of one competition | Petrov 2025, abstract (secondary) |
| no benchmark measures the person in the loop: the prover and translation benchmarks measure machines | strand C, review Q4 and Q5 |

## Limits of the benchmarks themselves

| Limit | Source, with where |
|---|---|
| ground truth wrong: 16.4% of miniF2F and 38.5% of ProofNet formal statements hold semantic errors | Chen 2025, section 4.5 |
| ports wrong: 31.8% of the entries in Lean 4 ports of ProofNet | Poiroux 2025, section 1 |
| unprovable as formalized: 16 miniF2F statements | Ospanov 2025, section 2.2 |
| 4,833 static findings, 398 certified mechanically, over miniF2F, ProofNet, FormalMATH, CombiBench and ProverBench | Ammanamanchi 2026, abstract and Table 4 |
| harness exploits: a bug in Lean before 4.20.0 let `apply?` pass without a checked declaration, used in at least three published prover solutions | Ammanamanchi 2026, section 3.2 |
| source errors no encoding can fix: a ProverBench problem states a wrong Pell solution | Ammanamanchi 2026, section 3.3 |
| misformalizations found in PutnamBench while training a prover, corrected upstream | Hubert 2025, Methods |
| expert-written research statements still wrong: 11 of 50 formalizations had mistakes after manual review | Browning 2026, section 2.5 |
| leakage: solutions to public benchmark problems appear online, so a score may measure memory | Firsching 2026, section 1 |
| domain: competition and olympiad statements depend on few facts, unlike research mathematics | Azerbayev 2023, section 1 |
| competition statements at IMO (2024) were formalized by experts, not by the system | Hubert 2025, Methods |
| miniF2F is saturated: 99.2% on its test split by Chung 2026 at pass@1 and by Varambally 2025 as an agentic pass rate under thousands of calls, 100% with a seeding proof; the same 7B prover that scores over 75% on MiniF2F reaches 10.3% pass@128 on research-level blueprint lemmas | Chung 2026 (secondary); Varambally 2025, Table 1; Poiroux 2025b, section 4 |
| the gain from repair is small on PISA: 1.5 points at 16 samples (8b model) | First 2023, Table 4 |
| Lean Copilot's assistance numbers come from replaying textbook proofs, not from users | Song 2024, section 5 |
| the Draft, Sketch, and Prove ablation holds on miniF2F in Isabelle only, and the human informal proofs beat the best model's by 0.4 points on the test set | Jiang 2023c, Table 1 |
| in Lean, a correct informal proof did not help: one model's one-shot pass@128 on Lean-IMO-Bench stayed at 20.0% and 3.3%, basic and advanced sets | Kung 2026, Table 1 |
| Xu 2025's gain is for fine-tuned models on PISA, not for human readers | Xu 2025, abstract |
| LeanTutor is evaluated on its authors' own benchmark of 371 proofs | Patel 2025, abstract (secondary) |

## A checker's own messages, read by students

- In the Diproche class, 67% of the 57 answers on what students disliked named the difficulty of finding a mistake from the error messages (Carl 2022, section 5).
- Only 19% reported being able to identify errors from those messages, and 33% being able to use the feedback to improve a proof (Carl 2022, section 5).
- Success messages encouraged 88%, and error messages discouraged 41% (Carl 2022, section 5).

## Model explanations are often wrong

- Expert raters judged model explanations correct for 48% of inputs, and proposed fixes correct for 33% (Leinonen 2023, section 4, Table 1).
- On proofs, 4% of correct steps (40 of 1,020) were judged wrong by the system, and step errors were often below the student's granularity (Guo 2026b, sections 7.2.1 and 7.2.2).
- The compiler-guided loop silently corrected a student's small error in 12 cases, so the statement checked was not the one the student wrote (Guo 2026b, section 7.1).

## What feedback does not fix, for a model

- Self-correction succeeds with reliable external feedback; with feedback from a prompted model alone, no prior work shows it working outside tasks suited to it (Kamoi 2024, abstract, secondary).
- Step repair gains come from shallow tactic failures, not from structural errors such as type mismatches (Deng 2026, abstract, secondary).
- Models get a Coq proof's high-level structure right and its low-level details wrong (Lu 2024, abstract, secondary). The low level is where a checker's message points; that this holds for Lean is this review's inference.
- An agent's sorry-free formalization still failed expert review on definitions, generality and API; agents fixed local, checkable points only (Ilin 2026, abstract).
- Messages tuned for humans may be wrong for agents: more detail helped an agent repair type errors, against the brevity human-factors work recommends (Krishnamurthi 2026, abstract).

## Selection, confounds and size in the studies of people

- Every positive effect of a proof assistant on paper proofs comes from groups that chose to use it (Thoma 2022; Bottoni 2025; Otte 2026).
- Thoma 2022 compares 18 Lean users with 139 others at a university with the highest entrance requirements; its authors draw no general conclusion (Discussion).
- Bottoni 2025 rests on five volunteers.
- Otte 2026 cannot separate the tool from two teachers shaped by proof assistants (section 4.3).
- Collins 2026 had 7 participants, mostly postgraduates rather than expert mathematicians (Limitations).
- Guo 2026b recruited from one course, mostly computer science students, who may trust verification more than others; it covers linear algebra and optimisation only (section 10).
- Massot 2024 and Wemmenhove 2024 are their owners' reports; Massot calls his anecdotal (section 7).
- Kosmyna 2025 is a preprint, and only 18 of its 54 participants did the session that swapped conditions (abstract, secondary).
- Zhai 2024 synthesises 14 articles (section on selection).
- The Diproche class gives descriptive data only, with no comparison group: the average exercise was solved correctly by about 27% of all students for number theory, 16% for set theory (Carl 2022, section 5.1).

## Critiques of the whole approach

| Critique | Source, with where |
|---|---|
| resolving ambiguity in mathematical text sits above the halting problem, so a Lean check of a translation may give no confidence in the original argument | Bastounis 2026, abstract |
| "Checking the logical equivalence between two theorems is generally intractable" | Murphy 2024, section 1 |
| a translation can close every placeholder and still fail expert review on definitions, generality and API; agents stayed weak at choosing definitions | Ilin 2026, abstract |
| manual evaluation is costly and automatic metrics inaccurate | Li 2024b, section 5; Yang 2024, section 4.2 |
| there is no systematic comparative study that favours one proof assistant over another for teaching | Tran Minh 2025, section 1.2 |
| Hanna 2021 regrets the lack of evidence that the tools improve learning and understanding | Tran Minh 2025, introduction |
| a syntax far from paper proofs makes transfer harder; exercises on bare tautologies made students lose faith in rigorous reasoning | Massot 2024, sections 2 and 7 |
| many students see programming as disconnected from proving, and not worth the time | Iannone 2023, abstract (secondary) |
| a student can finish every level by reacting to the checker without connecting the code to the mathematics | Iannone 2025b, Discussion |
| students working in an assistant can see only the local proof state, then confuse hypotheses and goals on paper | Kerjean 2022; Bartzia 2026; through Ouvrier-Buffet 2026 (secondary) |
| educational technology rarely lives up to its initial hype | Avigad 2024, section 13 |
| machine-checked mathematics depends on empirical knowledge of the physical world, which informal mathematics does not | Pollack 1997, abstract |
| informal proofs carry knowledge beyond their theorems; accounts that ground an informal proof in formal derivations cannot meet their own desiderata | Rav 1999, abstract; Tanswell 2015, abstract |
| an essay criticises recurring assumptions about automation in proof and its labour | Ochigame 2024, abstract |

## Limits of the prior art

- No study comparing declarative and procedural proofs for a human reader was found; the survey that maps the field asks for user studies (Ringer 2019, 7.1.5).
- A controlled language costs effort: Verbose Lean's natural syntax is slightly harder to write than tactics (Massot 2024, introduction).
- Coq's declarative mode (Corbineau 2008) was later removed, as the grey pass records; no formal account of why was read.
- Optimising a Mizar proof's order for readability is NP-complete (Pąk 2014, abstract).
- In definition-heavy projects, tooling saves only 27.3% of semantic review (Yanahama 2026, abstract, secondary), so the person's audit of definitions remains.
- Several large results are their owners' accounts: a textbook formalized by agents in a week (Gloeckle 2026) and a crowd platform (Chen 2026b).
- Also 26 textbooks formalized by agents and graded by the owners' model judges, checked by experts on one book only, with no agreement rate (Rammal 2026, section 5.1; Appendix G).

## Limits of the practice evidence

| Limit | Source |
|---|---|
| prover and translator scores in practice are their owners' claims; one result was checked by someone else | review Q2; Buzzard 2026a |
| the time saved is the practitioners' own estimate, with no control | Tao 2026i; Tao 2025c; Kirov 2026a |
| in practice, model feedback on writing is measured only by its owner's satisfaction survey, with no false-positive rate; research measures it against the reviews of submitted papers, not by whether a draft improved: by overlap with the reviewers, and in one owner's case study judged by a model | Google 2025; STOC 2026; Liang 2024c; Wu 2026 |
| counts of stars, downloads and labels measure interest or activity, not use or correctness | GitHub 2026e; PyPI 2026; GitHub 2026f |
| the grey pass met no controlled study of the loop on either side | review Q4 |
