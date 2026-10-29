# State of the art, per question

Step 3 of the review: who holds the best evidence on each of the scope's five questions, by what method, measured how. What has been achieved is kept apart from what is shown impossible or not yet shown, with the practice most adopted beside it. Terms are defined in [frame](frame.md); sources are in [review](review.md).

## Answer first

- The best evidence of faithfulness is still a person reading the statement: every automatic measure read was validated against people on 3,752 items or fewer, and none decides faithfulness.
- On guidance, the controlled evidence is on programming languages; on proofs, one classroom study coded a loop like this one (Guo 2026b).
- On form, every positive effect of a proof assistant on paper proofs comes from self-selected groups.

## Best evidence per question

| Question | Holder | Method | Measured how | Grade |
|---|---|---|---|---|
| Q1, controlled languages | Carl 2022 | one lecture of 228 students | system verdicts on 184 number-theory attempts and a questionnaire (127 answers); no control group | measured, descriptive |
| Q1, declarative proof languages | Xu 2025, for models | the same models fine-tuned on Isar or on a 10-operation language | pass@1 on PISA; no study with people found | measured, for models (secondary) |
| Q1, blueprints and structured workflows | Jiang 2023c and Kung 2026, for machines; Yanahama 2026 and Guo 2026b, for people's work | an ablation with and without the informal proof, and a comparison with a correct one added, which disagree; decomposition into checked lemmas in one framework; the share of nodes left for human review; coded sessions with students | miniF2F test in Isabelle, success within 100 attempts per problem; Lean-IMO-Bench, one-shot pass@128, and Putnam (2025), 12 problems; six projects; 23 sessions | measured; measured, descriptive |
| Q2, A1 faithfulness measured | Poiroux 2025 | BEq+: each statement proved from the other by fixed tactics | 3,752 human-labelled pairs: precision 98.0%, recall 48.3% (Table 1); Pearson 0.974 with human accuracy across models (Table 2) | measured, on ProofNetVerif |
| Q2, A1 | Chen 2025 | model judges on a binary faithfulness task | 859 expert-annotated items: best accuracy 85.8% (section 4.5) | measured, on ConsistencyCheck |
| Q2, A1 | Zhang 2026 | compile plus two judges of different families | agrees with the human majority on 54 of 59 audited cases, 91.5% (section 1) | measured, small audit |
| Q2, A1 | Han 2026 | SA-Pass: implication to and from expert shadow theorems | ranks six systems as two experts do, rho 1.00 (appendix F) | measured, 178 problems, six systems |
| Q2, A2 how often wrong | Ospanov 2025 | people re-judge outputs that a model judge accepted | miniF2F v1 test, 128 samples: 97.5% by the judge against 62.7% by people for one translator, 98.4% against 90.6% for another (Table 2) | measured, two translators (three at one sample) |
| Q2, A2 | Chen 2025; Poiroux 2025 | expert re-annotation of benchmark ground truth | 16.4% of miniF2F and 38.5% of ProofNet statements wrong (Chen 2025, section 4.5); 31.8% of Lean 4 ProofNet entries wrong (Poiroux 2025, section 1) | measured, descriptive |
| Q2, A3 detection | Ammanamanchi 2026 | static checkers over five benchmarks, a model filter on warnings | 4,833 findings, 398 certified mechanically (abstract and Table 4) | measured, descriptive |
| Q2, A3 | Firsching 2026 | human review, test lemmas, prover runs over all statements | 291 misformalizations fixed, typed by a three-level taxonomy (section 3.3) | measured, descriptive |
| Q2, A4 methods | Hubert 2025 | a fine-tuned formalizer; equivalence to reference statements proved by the prover during training | pass@1 60% on 50 IMO and 64% on 50 Putnam problems, judged by experts (Methods) | measured, 100 problems |
| Q3, messages for people, no model | Denny 2020; Becker 2016; Hentschel 2016 for a proof tool | randomised (n > 700) and controlled studies; a controlled comparison of two verifier interfaces | debugging time and error counts; correct answers on proof understanding tasks | measured (Denny 2020 and Becker 2016 secondary) |
| Q3, model explanations for people | Wang 2024b | randomised trial, 8,762 students assigned, 5,707 analysed | repeats of an error and attempts to resolve it | measured |
| Q3, the checker's output explained to people | Guo 2026b | expert coding of 97 step messages and 87 revision iterations | 23 sessions in one course | measured, descriptive |
| Q3, model feedback on research papers | Liang 2024c | GPT-4's comments matched against the published human reviews, with the overlap between two reviewers as baseline; a user study | 3,096 Nature-family and 1,709 ICLR papers: overlap 30.85% and 39.23%, against 28.58% and 35.25% (Fig. 2a, 2b); 308 self-selected researchers; no draft revised from the feedback | measured; the user study measured, descriptive |
| Q3, the checker's output as guidance for a model | First 2023; Lin 2025b; Deng 2026 | an equal-cost comparison and an ablation without the error message; an ablation of error messages; a per-failure-type analysis | PISA; MiniF2F, pass@32; a LeanDojo subset of 1,990 theorems | measured |
| Q4, C1 transfer | Thoma 2022 | 157 students, Lean users self-selected, covariate adjusted | final exam, analysis of variance adjusted for the first test: partial η² = 0.06, p = 0.002 | supported with caveat |
| Q4, C1 | Otte 2026 | quasi-experiment with a full control group, 80 consenting students | first quiz grade, linear mixed model, p = 0.101; proof steps coded: more explicit steps | supported with caveat |
| Q4, C2 use | Guo 2026b | 23 students, classroom deployment, prose formalized by a model | 87 revision iterations coded by outcome: 58% progress, 29% stuck or not useful | measured, descriptive |
| Q4, C3 research use | Collins 2026 | 7 participants, 5 with postgraduate mathematics, 6 problems each, with and without AI, random week order | binary accuracy of statement and proof, one grader per problem: +0.30 (95% CI 0.10 to 0.50); time p = 0.797 | measured, one small study |
| Q5, C4 trust | Carneiro 2024 | an independent typechecker run over mathlib | run time against the reference kernel: 20% to 50% slower; one soundness bug found | measured, the owner's run (secondary) |
| Q5, C5 the gap | Guo 2026b | experts judged each formalized step against the student's | 1,155 steps: 2% of correct and 18% of incorrect steps unfaithful | measured, descriptive |
| Q5, C6 over-reliance | Buçinca 2021; Fan 2025 | controlled experiments, N = 199 and N = 117 | over-reliance on wrong AI advice; knowledge gain and transfer | measured (secondary) |
| Q5, C7 cost | Wiedijk 2000; Gonthier 2013; Hales 2017 | counts on finished formalizations | a de Bruijn factor of about four; 4 to 5 formal lines per informal line; 5,000 processor hours for one subclaim | measured, descriptive |

- Bastani 2025, held by the exercise-sets review, is the largest controlled study of model access in mathematics learning met here.

## Upper bounds: what has been achieved

| Question | Achievement | Benchmark, metric or design | Source, with where |
|---|---|---|---|
| Q1 | a CNL checked by provers in an editor | system | De Lon 2021 |
| Q1 | 57% of submitted number-theory attempts judged correct by the system in one class | one lecture, no control | Carl 2022, section 5.1 |
| Q1 | pass@1 69.1% on PISA with a minimal declarative language, up to 20 points over Isar with Sledgehammer, 29 without | PISA, fine-tuned models | Xu 2025 (secondary) |
| Q1 | miniF2F test 99.2% by recursive decomposition | agentic pass rate on 244 problems under a budget of thousands of calls, no pass@k | Varambally 2025, Table 1 |
| Q1 | miniF2F test 99.2% at pass@1, 100% with a seeding informal proof; PutnamBench 597 of 672 (88.8%) with it | pass@1 | Chung 2026 (secondary) |
| Q1 | Putnam (2025), 12 of 12, by decomposition into checked lemmas, where the same model alone solved none at one-shot pass@128 | two rollouts of one framework, run on its authors' own model family | Kung 2026, Table 2 |
| Q1 | review set cut by 94-99% in proof-heavy projects | average node reduction, six projects | Yanahama 2026 (secondary) |
| Q2 | highest human-judged statement accuracy read: 90.6% | miniF2F v1 test, Kimina autoformalizer at 128 samples | Ospanov 2025, Table 2; the translator, Wang 2025, appendix C.2.3 |
| Q2 | highest expert-judged pass@1 on IMO- and Putnam-level problems: 64% on 50 Putnam problems, 60% on 50 IMO problems | pass@1, experts in A/B studies | Hubert 2025, Methods |
| Q2 | highest accuracy on undergraduate statements judged by people: 69.4% for ReForm-8B; 45.1% for GPT-4o | ProofNet test; ProofNet# with 50 samples and a selection heuristic | Chen 2025, section 4.5; Poiroux 2025, section 1 |
| Q2 | best reference-free acceptance on textbook statements: 57.7% accepted of 87.2% compiled | 227 statements, two-judge criterion | Zhang 2026, section 1 |
| Q2 | largest translated corpus: about 80 million formal problems from about 1 million informal ones, never fully checked for faithfulness | training data | Hubert 2025, Methods |
| Q2 | lowest accepted-error rate of an automatic gate: 1.9% to 9.2% | three labelled sets | Mei 2026, section 5.2 |
| Q2 | closest automatic agreement with experts: kappa 0.77 against 0.81 between experts | 384 expert-labelled pairs; a single preprint | Mohammad 2026, section 11.3 |
| Q3 | shorter debugging with short, readable messages with hints; fewer errors and repeats | randomised, n > 700; controlled, CS1 Java | Denny 2020; Becker 2016 (secondary) |
| Q3 | 23.1% fewer repeated errors (GPT Default) and 34.8% fewer additional attempts (either GPT message) against standard messages | randomised trial | Wang 2024b, Figure 3, p. 1398 |
| Q3 | experts judged that 85% of next-step hints and 63% of step messages reflected the mistake; 58% of iterations made progress | 23 sessions, expert coding | Guo 2026b, sections 7.2.2, 8 |
| Q3 | MiniF2F pass@32 90.4% with self-correction; up to 32% relative gain from step repair | pass@32; 1,990 LeanDojo theorems | Lin 2025b; Deng 2026 (secondary) |
| Q4 | students who chose a proof assistant did better on a paper exam, and wrote more explicit proofs | self-selected groups | Thoma 2022; Bottoni 2025; Otte 2026 |
| Q4 | with model access, participants, most with postgraduate mathematics, formalized correctly more often | randomised week order, 7 people | Collins 2026 |
| Q4 | a model formalizes a student's prose step by step well enough that most revisions progress | 87 iterations | Guo 2026b |
| Q5 | a second kernel rechecks a whole library at modest cost, and found a bug | the owner's run | Carneiro 2024 (secondary) |
| Q5 | designs that force the person to think reduce over-reliance, or avoid the learning harm | controlled experiments | Buçinca 2021 (secondary); Bastani 2025 |

## Lower bounds: what is shown impossible, or not yet shown

| Question | Limit | Kind | Source, with where |
|---|---|---|---|
| Q1 | any effect of writing in a CNL on reasoning or on a reader | not shown | the formal pass, review Q1 |
| Q1 | a human benefit of declarative over procedural proofs; the survey of the field asks for such studies | not shown | Ringer 2019, 7.1.5 |
| Q1 | research-level blueprint lemmas: best model 10.3% pass@128 on proof autoformalization and 8.8% on theorem proving, normal mode; the same 7B prover scores over 75% on MiniF2F | measured | Poiroux 2025b, section 4, Figure 1 |
| Q1 | definition-heavy projects: only 27.3% of review saved | measured, descriptive | Yanahama 2026 (secondary) |
| Q2 | no general method decides whether two formal statements that are not definitionally equal say the same thing | stated as the reason for human evaluation | Azerbayev 2023, section 4.1.1 |
| Q2 | logical equivalence of two theorems is generally intractable | stated | Murphy 2024, section 1 |
| Q2 | resolving the ambiguity of mathematical text needed for a faithful translation sits above the halting problem | argument from computability, preprint | Bastounis 2026, abstract and appendix A.2.1 |
| Q2 | equivalence to a reference needs the reference to be right, and references are wrong in 16.4% to 38.5% of two benchmarks | measured | Chen 2025, section 4.5 |
| Q2 | research-level test sets stay small: 619 pairs in RLM25, 178 problems in ShadowBench (13 of them research level), 50 statements in AnnalsChallenge | measured, descriptive | Poiroux 2025, section 1; Han 2026, section 4; Browning 2026, abstract |
| Q2 | no study compares the detection checks of A3 on one shared set of misformalizations | not yet shown | review Q2 |
| Q2 | Lean feedback has not been shown to reduce semantic errors | not significant in one study | Dai 2026, section 5.1 |
| Q3 | no measurable benefit of enhanced messages in two studies | measured, null | Denny 2014; Pettit 2017 (secondary) |
| Q3 | only 19% of respondents reported being able to identify errors from a CNL checker's messages | measured, descriptive, self-report | Carl 2022, section 5 |
| Q3 | no controlled study of a Lean, Isabelle or Coq error message read by a person | not yet shown | review Q3 |
| Q3 | that model feedback on a paper improves the draft or its writer: the studies compare it with reviews of submitted papers | not yet shown | Liang 2024c; Wu 2026; review Q3 |
| Q3 | model messages faster than stock ones in 1 of 6 tasks; no objective gain from clearer rewrites; explanations correct for 48% of inputs | measured | Santos 2024 (secondary); Moraru 2026 (secondary); Leinonen 2023, section 4, Table 1 |
| Q3 | 23% of continuation errors judged to reflect the mistake; 18% of incorrect steps formalized unfaithfully | measured, descriptive | Guo 2026b, sections 7.1, 7.2.2 |
| Q3 | gains from step repair limited to shallow failures; repair from the error message adds 1.5 points at 16 samples (8b model) on PISA; agents do not repair design | measured; one expert review | Deng 2026 (secondary); First 2023, Table 4; Ilin 2026 |
| Q4 | no randomised trial of a proof assistant on the skill of writing proofs on paper; every positive comparison is between self-selected groups | not yet shown | review Q4, C1 |
| Q4 | transfer to paper is highly complex and often partial, in a systematic review of nine works | review | Ouvrier-Buffet 2026, section 3.2 |
| Q4 | where a control group existed, the effect on grades was not significant | measured, null | Otte 2026, Table 3 |
| Q5 | models did not shorten formalization, and checked explicit proofs are several times longer | measured | Collins 2026; Gonthier 2013 |
| Q5 | automation bias appears in experts and is not prevented by training or instructions | review | Parasuraman 2010 (secondary) |
| Q5 | models given a false statement often prove it anyway: 29.0% of the time for the best model on one benchmark, so a model's informal proof is no check | measured on that benchmark, judged by a model | Petrov 2025b |
| Q5 | people do not reliably see a gap between what they meant and what was checked | measured, descriptive | Collins 2024; Guo 2026b |
| Q5 | informal proofs are argued not to be reducible to formal derivations, so a check of the formal claim may certify less than the informal proof holds | argued | Rav 1999; Tanswell 2015 |

## Most adopted in practice, beside the best evidence

The grey pass holds the practice records; the formal record differs on almost every line.

| Question | Most adopted (grey pass) | Best evidence (formal pass) | Where they differ |
|---|---|---|---|
| Q1, controlled languages | Verbose Lean, 162 stars, and Naproche, 53 stars (Massot 2026b; Naproche 2026; GitHub 2026e) | Carl 2022, descriptive classroom data | practice runs a CNL for teaching; research has descriptive data only |
| Q1, declarative languages | Isar, a structured proof text its owner calls understandable by people and machines (Isabelle 2026) | Xu 2025, for models | no adoption count was read in either pass; the only controlled number concerns models |
| Q1, blueprints | leanblueprint, 37 projects listed; PNT+ builds its blueprint with LeanArchitect, requires checkdecls and runs no comparator (Massot 2026; GitHub 2026i) | Poiroux 2025b; Yanahama 2026 | research measures blueprints as machine benchmarks or review load, not as a writer's tool |
| Q2, A1 measuring faithfulness | a person audits the challenge file; a model judge only filters (Palomar 2026; Lean FRO 2026a) | BEq+ against a reference; validated model judges | practice has no reference statement to compare against, so BEq-style checks do not apply; it falls back on the person research uses as ground truth |
| Q2, A2 how often wrong | 787 Formal Conjectures items carry the misformalization label (GitHub 2026f) | rates on benchmarks, 13.4% to 90.6% judged by people | the formal count is of merged fixes (291, then 511 by 2026-10-02), the grey count of labels on issues and pull requests; neither is a rate |
| Q2, A3 detection | comparator checks the proof matches the challenge file; prover runs over Formal Conjectures (Lean FRO 2026a; Google DeepMind 2026) | hypothesis rejection, disproofs, static checkers, test lemmas | comparator certifies the statement proved is the one claimed, not that the claim is faithful; research checks catch vacuous or false statements, not true but wrong ones |
| Q2, A4 methods | translation agents on real projects, scored by their owners (review Q2) | trained translators scored on benchmarks | benchmark scores come from competition and textbook statements; practice formalizes research papers |
| Q3, messages without a model | Lean's named errors, since 4.22.0, with 14 explanation pages (Lean FRO 2025; Lean FRO 2026c) | Denny 2020; Becker 2016; Hentschel 2016 | no study measured Lean's messages; the error-message literature is on C, Java and Python |
| Q3, model explanations | none specific to proofs in the grey pass | Wang 2024b on programming; Guo 2026b on proofs | research has a large trial on programming and a classroom study on proofs |
| Q3, guidance for a model | errors and goals sent to agents through the language server: lean-lsp-mcp, 730,424 downloads in a month (Dressler 2026; PyPI 2026) | First 2023; Lin 2025b | the research record agrees that the message is the active part for a model |
| Q4, C1 transfer | Verbose Lean and Waterproof used in courses, reported by their owners (review Q1) | Otte 2026: no significant grade effect | adoption runs ahead of a measured effect |
| Q4, C2 use | named errors, hints and a help tactic, written ahead of time (review Q3) | Guo 2026b; Carl 2022: messages at the checker's granularity block students | practice measures no person's use of the guidance |
| Q4, C3 research use | the audited blueprint, B1: a model writes proofs, a person audits statements | Collins 2026: accuracy up, time not significantly changed, 7 people | the time saved in practice is the practitioners' estimate |
| Q5, C4 trust | comparator, axiom checks, several kernels (review Q2, Q5) | Wiedijk 2012: a printed statement may not be the one proved | practice checks the proof, not what the person reads |
| Q5, C5 the gap | a person audits statement fidelity (review Q2) | Collins 2024; Guo 2026b: people repair or miss differences | the audit B1 relies on is itself fallible |
| Q5, C6 over-reliance | disclosure labels and a cap on model pull requests (review Q1, Q5) | Buçinca 2021; Bastani 2025: designs that force engagement | practice limits volume, not the person's checking |
| Q5, C7 cost | practitioners' estimates of time saved (review Q1) | Collins 2026: no significant time effect | estimates against one small measurement |

## Adoption counts, descriptive, taken 2026-10-29

| Count | Value | Source |
|---|---|---|
| projects listed by leanblueprint | 37 | Massot 2026 |
| stars, leanblueprint; downloads last month | 394; 31,309, not a count of users | GitHub 2026e; PyPI 2026 |
| registered results in Palomar | 845 from 660 projects at the formal side's read; 847 from 661 at the audit later that day | Palomar 2026b |
| pull requests in Formal Conjectures labelled misformalization; issues | 533; 254, of 5,053 pull requests at the human side's count | GitHub 2026f |
| downloads last month, lean-lsp-mcp | 730,424 | PyPI 2026 |
| stars, Lean Copilot; Verbose Lean; Naproche | 1,339; 162; 53 | GitHub 2026e |
