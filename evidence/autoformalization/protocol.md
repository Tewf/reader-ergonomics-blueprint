# Protocol: how the pool of both passes was built

Every search, count and rule of the review, run on 2026-10-29: the grey pass, one reviewer per side, then the formal pass, one reviewer per strand, all merged.
Terms are defined in [frame](frame.md); the pool is in [sources](sources.md). Shared rules of the family: [evidence README](https://github.com/Tewf/reader-ergonomics-topic/blob/master/evidence/README.md#method).

## 1. Why grey literature

Garousi 2019, Table 4, answered by each side: seven of seven questions get a yes on both.

| # | Question | Formal side | Human side |
|---|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: blueprints, comparator, registries and editor tools come from practice | yes: the workflows changed month by month in 2025 and 2026; papers lag |
| 2 | Lack of volume or quality of evidence? | yes: tools change monthly; no grey source measured guidance for a person | yes: this pass met no controlled study of the loop |
| 3 | Context important? | yes: competition problems against research papers; teaching against research | yes: research, teaching and benchmarks; experts and novices |
| 4 | Corroborate research with practice? | yes: benchmark scores against what practitioners check | yes |
| 5 | Challenge practice with research, or the reverse? | yes: compile rates against statement fidelity | yes: reports disagree on whether formalizing helps understanding (review Q4) |
| 6 | Would a synthesis serve both communities? | yes | yes |
| 7 | Large practitioner volume? | yes: the public forum archive lists 9,893 topics in its general channel alone | yes: 5,053 pull requests in Formal Conjectures at this side's count (5,054 at the audit later that day) and 1,399 in PNT+ (GitHub 2026f, 2026g); 482 topics in one forum stream (P4) |

## 2. Questions

The scope's five questions, Q1 to Q5 of [frame](frame.md): prior art, translation, feedback, form, limits. The frame maps each side's sub-questions (F1 to F5, H1 to H4) and each formal strand's (A1 to A4, C1 to C7, and strand B's parts of Q1 and Q3) onto them.

## 3. Existing reviews

- Neither side found a grey review of the whole loop.
- Formal side: two grey overviews of practice were found and used, Hales 2026 and Avigad 2026. One practitioner answer catalogues the checks for a wrong statement, PASE 2026. One formal survey was met and listed, on proof assistants for teaching.
- Human side: two formal surveys were met by citation and listed among the formal leads, not read; the formal pass screened them (section 4).
- Held by the family, linked and not repeated: structured proofs and blueprints (reader-ergonomics-academic, mathematical-writing); prose linting and docs as code (reader-ergonomics-topic, document-model).
- Formal pass: each strand searched for existing reviews before its other strings (section 4); the reviews found are in [review](review.md), section 0.

## 4. Formal search

The formal pass ran on 2026-10-29 in three strands, one reviewer each: A, translation (Q2); B, prior art and feedback (Q1, Q3); C, form and limits (Q4, Q5). Their sub-questions are in [frame](frame.md).

- The grey pass's formal leads went to the strands. Each lead a strand screened is named in its section below, kept or set aside with its reason.
- The lead screen: on 2026-10-29, after the merge, one reviewer screened the sixteen leads that no strand had screened, by the rule of section 8. Each lead was identified on arXiv, Crossref or OpenAlex without a key or account. Its abstract was read, and its full text where open and needed. Every kept number was then checked against its source; Liang 2024c, met in a kept work, was read in full.
- Its decisions on the leads first listed here as unread: LEAP kept, as Kung 2026; Meta's ATLAS kept, as Rammal 2026, with its namesake Liu 2025d. Urban (2026) on formal topology, Bloom and Mehta (2022) and the LeanDojo paper (Yang and others, 2023) set aside, each with its reason in [sources](sources.md).
- These leads have no record of screening, in a strand or at the lead screen, and stay leads, unread.
- They are the Waterproof Editor (arXiv 2606.01875); Nipkow's Isar/HOL tutorial, given at TYPES in 2002 and Wenzel's Isabelle/Isar framework; ProofAug (arXiv 2501.18310).
- Also: OEIS Open (arXiv 2608.11941); Alexeev and Mixon (2025, arXiv 2510.19804); the Erdős 728 write-up (arXiv 2601.07421); arXiv 2601.22401, 2603.28636 and 2604.18869; Aristotle (arXiv 2510.01346) and its API report (arXiv 2605.20120).
- Also: BFS-Prover and BFS-Prover-V2 (arXiv 2502.03438, 2509.06493); the DeepSeek-Prover-V2 report; DeepSeekMath-V2; ProofBridge (arXiv 2510.15681); FormL4 (arXiv 2406.01940); MathAdv, LeanFlow, Numina-Lean-Agent and MathCoPilot.
- Also: Avigad's essay of 2026 on AI and formalization; a survey of AI for mathematics met in Kirov 2026b; Thurston (1994) and Jaffe and Quinn (1993); the benchmarks VERINA, MathOlympiadBench and FLTEval.
- Also: Jayaram, Tyler, Woodruff and others (2026), Google's Paper Assistant Tool (arXiv 2606.28277), a grey lead (W7) that strand B did not pursue.
- Also: Biswas, Schoepp, Vasan and others (2026), the AAAI-26 AI review pilot (arXiv 2604.13940), met at the lead screen in Wu 2026, section 2.5.
- Also, met at the lead screen in the search for Urban (2026): Bryant, Huerta y Munive, Kaliszyk and Urban (2026), Munkres' general topology autoformalized in Isabelle/HOL (arXiv 2604.07455).
- Also, met in the same search: Brown, Kaliszyk and Urban (2026), Agent Hunt (arXiv 2603.06737).
- Also most of the authors the grey pass listed to search by name.
- Each strand searched for existing reviews first, then ran its strings, then snowballed; each was then audited line by line against its sources (section 10).
- Databases: the Semantic Scholar bulk search, without a key (title and abstract; `+` is AND, `|` is OR; stemmed words, so noisy upper bounds); the arXiv search API, without a key (`abs:` field).
- OpenAlex (title and abstract, phrase search) was counted by script, with a key the script reads itself and never writes.
- A cell reads "not run" where the database was not queried with that string. Counts are those of the day; a rerun will give others.

### Strand A: translation and its faithfulness

- Existing reviews, searched first with R1 to R4 and the arXiv form of R1: two surveys (Weng 2025, Li 2024b), one integrated survey (Raiyan 2026).
- Also two position papers (Yang 2024, Min 2026) and one framework paper (Mensfelt 2025). Two benchmark audits act as reviews of one object: Ospanov 2025 and Ammanamanchi 2026.
- Not found: a systematic review, mapping study or meta-analysis of faithfulness measures. R1 to R4 returned none, and none of the six reviews pools results across studies.
- arXiv refused calls with `max_results=0` on the day, so counts were read with one result requested. OpenAlex counted at 14:57 to 14:58 UTC.

| Id | String as run (Semantic Scholar syntax) | Semantic Scholar | arXiv | OpenAlex |
|---|---|---|---|---|
| R1 | ("autoformalization" \| "autoformalisation") +(survey \| review) | 21 | 8 (A-R1) | 32 |
| R2 | ("neural theorem proving" \| "automated theorem proving" \| "theorem proving") +("deep learning" \| "language model" \| "language models") +(survey \| review) | 29 | not run | 77 |
| R3 | ("formal mathematical reasoning" \| "formal mathematics" \| "formal reasoning") +(survey \| review \| "position paper") +("language model" \| "language models") | 27 | not run | 75 |
| R4 | "mathematical reasoning" +("large language models" \| LLM) +survey +(formal \| Lean \| "theorem proving") | 4 (first call refused, second ran) | not run | 36 |
| F1 | "autoformalization" \| "autoformalisation" \| "auto-formalization" | 259 | 201 (abs:autoformalization) and 15 (abs:autoformalisation); the OR form was refused three times | 321 |
| F2 | "statement autoformalization" \| "autoformalization of statements" \| "theorem statement" +autoformalization | 24 | 11 (abs:"statement autoformalization") | 12 |
| F3 | "proof autoformalization" \| "autoformalization of proofs" \| "autoformalizing proofs" | 10 | 6 (abs:"proof autoformalization") | 9 |
| F4 | (autoformalization \| autoformalisation) +(faithful \| faithfulness \| fidelity \| "semantic correctness" \| "semantic accuracy") | 49 | 34 | 52 |
| F5 | (autoformalization \| autoformalisation) +("semantic equivalence" \| "logical equivalence" \| "equivalence checking" \| "definitional equality") | 7 | 15 (abs:equivalence) | 8 |
| F6 | (autoformalization \| autoformalisation) +("back-translation" \| backtranslation \| informalization \| "round-trip") | 57 | 65 (AND abs:informalization); 1 (AND abs:"back-translation") | 68 |
| F7 | (autoformalization \| autoformalisation) +(judge \| "LLM-as-a-judge" \| critic \| verifier \| evaluator) | 154 (first call refused, second ran) | 129 (judge, critic, evaluator) | 25 |
| F8 | misformalization \| misformalisation \| misformalized \| "formalization errors" \| "mistranslation" +Lean | 11 (4 on topic) | 1, 1 and 1 for three single words, none on topic | 35 |
| F9 | miniF2F \| "mini-F2F" | 136 | 118 | 136 |
| F10 | ProofNet +(autoformalization \| Lean \| "theorem proving") | 43 | 42 (abs:ProofNet) | 35 |
| F11 | PutnamBench | 45 | 42 | 43 |
| F12 | FormalMATH \| CombiBench \| ProverBench \| "Lean Workbook" \| "FATE-M" \| "LeanCat" | 38 | not run | 32 (without the last two) |
| F13 | "neural theorem proving" \| "neural theorem prover" \| "neural theorem provers" | 68 | 15 (first phrase) | 73 |
| F14 | (Lean \| "Lean 4") +("large language model" \| "large language models" \| LLM) +("theorem proving" \| prover) | 195 (first call refused, second ran) | not run | 310 |
| F15 | (autoformalization \| autoformalisation) +("human evaluation" \| "human judgment" \| "expert evaluation" \| "manual evaluation" \| annotators) | 14 | 17 | 13 |
| F16 | (benchmark \| benchmarks) +(Lean \| "formal statements") +(errors \| defects \| mislabeled \| "incorrect formalizations") | 152 (noise: lean manufacturing; unusable) | not run | not run |
| F17 | (miniF2F \| ProofNet \| PutnamBench \| "Lean Workbook") +(errors \| mistakes \| "incorrect statements" \| misformalized \| "wrong formalizations" \| flawed) | 29 | 24 | 28 |
| F18 | ("neural machine translation" \| translation) +(informal \| "natural language") +(Mizar \| Isabelle \| Lean \| Coq \| HOL) +(formal \| formalization) | 123 | not run | 153 |
| F19 | "BEq" \| "bidirectional extended definitional equivalence" \| "definitional equivalence" +autoformalization | 8 | not run | 810 (noise: the token BEq) |
| F20 | ("Formal Conjectures" \| "Erdős problems" \| "Erdos problems") +(Lean \| formal \| formalization) | 27 | not run | 121 |
| U1 | arXiv only: au:Szegedy AND (abs:formal OR abs:autoformalization) | not run | 11 | not run |
| U2 | arXiv only: au:Kaliszyk AND au:Urban AND (abs:informal OR abs:translation OR abs:autoformalization) | not run | 16 | not run |
| U3 | arXiv only: au:Jamnik AND (abs:autoformalization OR abs:formalization) | not run | 9 | not run |
| U4 | arXiv only: au:Bosselut AND abs:autoformalization | not run | 2 | not run |
| U5 | arXiv only: au:Avigad AND (abs:Lean OR abs:autoformalization) | not run | 18 | not run |

- Three ways per term: academic name (F1 to F7), acronym or benchmark name (F9 to F13, F19), author (U1 to U5).
- The arXiv strings use the same terms as the Semantic Scholar strings, written with `abs:`; where they differ the cell says how.
- F8 returned almost nothing on arXiv: the word misformalization is rare in abstracts. It was rephrased as F17 (errors in named benchmarks) and F16 (defects in Lean benchmarks), and F17 found the defect papers.
- Screening: on Semantic Scholar, the 15 most cited results of each string, by title, all where fewer (R1: 20; F7, F14, F17, F18, F20: 12 shown). On arXiv, every title returned by the strings asked for titles (A-R1, F4, F5, F7, F8, F15, F17, U1 to U5), up to 34 per string. OpenAlex gave counts only.
- A title passed when it named autoformalization, a translation benchmark, or the faithfulness of formal statements; then the abstract decided.
- Backward snowballing: Poiroux 2025, appendix A.5, gave Liu 2025b (BEq) and its numbers; Chen 2025 gave Peng 2025; Zhang 2026, section 1, listed the evaluation families checked against the review.
- Forward snowballing, through the Semantic Scholar citations endpoint: four seeds, 743 citing records, the 25 most cited per seed read by title.
- 141 of them passed a keyword screen on titles: faithful, equivalence, judge, misformal, semantic, align, evaluat, consistency, human, error, defect, robust.

| Seed | Citing records | Passing the title screen | Added |
|---|---|---|---|
| Wu 2022 | 384 | 65 | none new; confirmed Poiroux 2025, Lu 2025, Zhang 2026, Ammanamanchi 2026 |
| Azerbayev 2023 | 227 | 47 | Han 2026 |
| Poiroux 2025 | 49 | 18 | Venturim 2026, Shen 2026, Mei 2026 (also F3) |
| Wang 2018 | 83 | 11 | none new |

- These leads of the grey pass for Q2 were all re-found by the strings and checked against arXiv: Firsching 2026, Ammanamanchi 2026, Zhang 2026, Gui 2026, Poiroux 2025.
- Also Tsoukalas 2024, Wu 2025b, Wang 2025, Lin 2025, Gao 2025.
- Unsupported, as the audit found: the 314 Semantic Scholar titles screened hold only if F16, called unusable, counted 15; the 172 arXiv titles recorded fall short of the 191 the rule allows. Titles shown per string were not logged.

### Strand B: prior art and feedback

- Scope: Q1 as research (blueprints, controlled natural languages, declarative proof languages) and Q3 (error messages and their usability, proof repair, models that explain errors or propose fixes), measured on users where possible.
- Programming error messages are included because no controlled study of a proof assistant's messages read by people was found; they are the nearest measured evidence, and every row says which language it concerns.
- Existing reviews, searched first by R1 to R6, then by the forward citations of First 2023: Ringer 2019, Kuhn 2014, Blanchette 2016, Becker 2019, Li 2024b.
- Kamoi 2024 and Tran Minh 2025 are held by sibling reviews.
- Not found: a systematic review or mapping study of proof assistant error messages, of CNLs for mathematics, or of blueprints.
- The arXiv and OpenAlex forms were derived mechanically from the Semantic Scholar form: `+` became AND, `\|` became OR, and each arXiv term got `abs:`; arXiv returned up to 10 results per call.
- Semantic Scholar and arXiv ran from 14:38 to 15:13 UTC. OpenAlex counted the 33 main strings at 14:38 to 14:39 UTC and the acronym strings at 15:31 UTC.

| Id | String as run | Semantic Scholar | arXiv | OpenAlex |
|---|---|---|---|---|
| R1 | ("proof assistant" \| "interactive theorem prover" \| "interactive theorem proving") +(survey \| "systematic review" \| "literature review" \| "mapping study") | 83 | 22 | 111 |
| R2 | "controlled natural language" +(survey \| classification \| review) | 73 | 8 | 87 |
| R3 | ("error message" \| "error messages") +(compiler \| programming) +(survey \| review \| landscape) | 128 | 4 | 134 |
| R4 | ("proof assistant" \| "interactive theorem prover" \| "theorem prover") +(usability \| "user study" \| "user interface" \| "human factors") +(survey \| review) | 514 | 8 | 726 |
| R5 | ("proof engineering" \| "formally verified software") +(survey \| review) | 19 | 3 | 28 |
| R6 | ("large language model" \| "large language models" \| "deep learning") +("theorem proving" \| "formal mathematics" \| autoformalization) +(survey \| review) | 40 | 24 | 98 |
| F1 | blueprint +(Lean \| formalization \| formalisation \| "proof assistant") | 606 | 123 | 1,580 |
| F2 | ForTheL | 16 | 0 | 9 |
| F3 | Naproche \| "Naproche-SAD" | 28 | 3 | 22 |
| F4 | "controlled natural language" +(mathematics \| mathematical \| proof \| proofs) | 62 | 6 | 64 |
| F5 | "declarative proof" \| "declarative proofs" \| "declarative proof language" | 44 | 6 | 40 |
| F6 | Isar +(Isabelle \| "proof language" \| readable) | 139 | 15 | 124 |
| F7 | Mizar +(proof \| proofs \| "proof checker" \| language) | 444 | 32 | 336 |
| F8 | ("proof sketch" \| "proof sketches") +(formal \| "proof assistant" \| Isabelle \| Lean) | 80 | 23 | 178 |
| F9 | ("informal proof" \| "informal proofs") +("proof assistant" \| Isabelle \| Lean \| formal) +(sketch \| sketches \| decomposition \| blueprint) | 17 | 4 | 12 |
| F10 | "natural language proof checking" \| "natural proof checking" \| Diproche | 13 | 4 | 8 |
| F11 | ("mathematical vernacular" \| "language of mathematics") +(formal \| formalization \| "proof assistant") | 472 | 14 | 173 |
| F12 | ("collaborative formalization" \| "collaborative formalisation" \| "large-scale formalization" \| "formalization project") +(Lean \| Coq \| Isabelle \| mathlib) | 28 | 21 | 37 |
| F13 | "Liquid Tensor Experiment" \| "Polynomial Freiman-Ruzsa" \| "spec-driven development" \| "Equational Theories Project" | 79 | 48 | 162 |
| F14 | declarative +procedural +("proof style" \| "proof styles" \| "proof assistant" \| "theorem prover") | 40 | 7 | 25 |
| F20 | "proof repair" | 37 | 17 | 52 |
| F21 | ("proof repair" \| "repair proofs" \| "proof fixing") +("large language model" \| "large language models" \| LLM) | 13 | 9 | 15 |
| F22 | ("error message" \| "error messages") +("proof assistant" \| "theorem prover" \| Lean \| Coq \| Isabelle \| Agda) | 34 | 8 | 31 |
| F23 | "compiler error messages" \| "programming error messages" \| "enhanced error messages" | 143 | 19 | 154 |
| F24 | ("error message" \| "error messages") +("large language model" \| "large language models" \| LLM \| GPT) +(explanation \| explanations \| novice \| novices) | 35 | 14 | 42 |
| F25 | ("type error" \| "type errors") +("error message" \| "error messages" \| diagnosis \| explanation \| localization) | 240 | 51 | 280 |
| F26 | ("interactive theorem prover" \| "proof assistant" \| "interactive verification") +("user study" \| usability \| "focus group" \| "focus groups" \| "empirical evaluation" \| "user interaction") | 4,190 | 29 | 4,540 |
| F27 | ("compiler feedback" \| "error feedback" \| "proof assistant feedback" \| "verifier feedback" \| "self-correction") +("theorem proving" \| Lean \| "formal proof" \| "proof generation") | 63 | 39 | 96 |
| F28 | (informalization \| verbalization \| "natural language explanation" \| "natural language explanations") +("formal proof" \| "formal proofs" \| "proof assistant") | 502 | 207 | 488 |
| F29 | "proof presentation" +("natural language" \| readable \| human) | 32 | 6 | 28 |
| F30 | (tutor \| tutoring \| feedback) +("proof assistant" \| Lean \| "theorem prover" \| Isabelle \| Coq) +(student \| students \| learners) | 582 | 23 | 800 |
| F31 | (Sledgehammer \| hammer) +("proof assistant" \| Isabelle \| "premise selection" \| "automated theorem prover") | 102 | 27 | 142 |
| F32 | ("human-style" \| "human-like" \| "human-oriented") +(proof \| proofs) +(output \| "write-up" \| presentation \| "theorem prover") | 64 | 14 | 77 |
| K1 | CNL +(mathematics \| mathematical \| proof \| proofs) | 92 | 4 | 90 |
| K2 | (PEM \| PEMs) +("error message" \| "error messages" \| novice \| novices) | failed (429, 15:32 UTC) | 1 | 23 |
| K3 | ITP +(usability \| "user study" \| "user interface" \| interaction) | 9,209 | 48 | 10,482 |

- Retries: F10 and F31 failed on Semantic Scholar at 14:49 and 15:09 UTC and returned at 15:22 and 15:23 UTC; F27 failed on arXiv at 14:59 UTC and returned at 15:23 UTC.
- K2 failed on Semantic Scholar at 15:32 UTC and was not retried; its cell stays failed.
- K1 and K3 are the acronym forms of F4 and F26; they return mostly other fields' acronyms (CNL in physics, ITP in haematology) and added no source.
- F1, F11, F26, F28 and F30 are noisy on Semantic Scholar, whose most cited hits for them are off topic; their arXiv lists carried the relevant titles.

Strings run on arXiv only:

| Id | String as run | arXiv | Screened |
|---|---|---|---|
| X1 | abs:Mizar AND (abs:declarative OR abs:readable OR abs:readability) | 3 | 3 |
| X2 | abs:Naproche OR abs:ForTheL OR ti:Naproche | 3 | 3 |
| X3 | abs:"error messages" AND (abs:randomized OR abs:RCT OR abs:"controlled experiment" OR abs:"controlled study") | 4 | 4 |
| X4 | (abs:"error message" OR abs:"error messages") AND (abs:LLM OR abs:GPT OR abs:"large language model" OR abs:"large language models") | 69 | 25 |
| X5 | (abs:"error message" OR abs:"error messages" OR abs:"error reporting") AND (abs:"proof assistant" OR abs:"theorem prover" OR abs:Lean OR abs:Coq OR abs:Isabelle OR abs:Agda OR abs:Idris OR abs:"dependently typed" OR abs:"dependent types") | 8 | 8 |
| X6 | (abs:tutor OR abs:tutoring OR abs:feedback OR abs:hint OR abs:hints) AND (abs:"proof assistant" OR abs:Lean OR abs:"theorem prover") AND (abs:student OR abs:students OR abs:learners) | 24 | 24 |

Author strings, on arXiv. The first form, with initials (for example `au:Ringer_T AND abs:proof`), returned 0 for seven authors; the query was wrong, and the surname form below was run instead.

| Id | String as run | arXiv | Note |
|---|---|---|---|
| A1 | au:Ringer AND abs:proof | 14 | proof repair and proof engineering |
| A2 | au:Becker AND (abs:"error message" OR abs:"error messages") | 4 | programming error messages |
| A3 | au:Denny AND (abs:"error message" OR abs:"error messages") | 3 | programming error messages |
| A4 | au:Wenzel AND abs:Isabelle | 13 | the Isabelle prover IDE |
| A5 | au:Koepke AND (abs:proof OR abs:natural) | 19 | noise: other authors of the name; Naproche papers are not on arXiv |
| A6 | au:Wiedijk | 9 | declarative styles, proof re-animation |
| A7 | au:Carl AND (abs:Diproche OR abs:"proof checking" OR abs:didactics) | 5 | Diproche |
| A8 | au:Ganesalingam | 1 | human-style output |
| A9 | au:Massot | 64 | noise: other authors of the name |
| A10 | au:Grebing | 20 | noise, except the focus-group paper and a proof-script debugger |

- Author strings were not counted in OpenAlex: the counting script searches titles and abstracts, not authors.
- Screening: the 15 most cited Semantic Scholar results and the first 10 arXiv results per string, all of them where fewer; then by abstract for every candidate.
- Full text was read where a number or a design was needed and the text was open.
- Forward snowballing, through the Semantic Scholar citations endpoint, titles filtered by words of the strand, then screened:

| Seed | Citing works returned | Matching the title filter | Screened | Added |
|---|---|---|---|---|
| Becker 2019 | 223 | 117 | 30 | Denny 2020, Denny 2021, Wang 2024b; confirmed Leinonen 2023, Santos 2023, Taylor 2024b, Santos 2024 |
| Jiang 2023c | 390 | 39 | 25 | Hu 2025, Varambally 2025; confirmed Chung 2026 |
| First 2023 | 227 | 17 | 17 | Kamoi 2024 (held); confirmed Lin 2025b, Zheng 2023 |

- Forward citations of Wenzel 1999 failed (429). Those planned for Cramer 2010, Aitken 1998, Ganesalingam 2017, Leinonen 2023 and Beckert 2014 were not run, to leave the rate limit to the counts.
- OpenAlex forward citations were refused without a key (401), and the key was kept for the counting script.
- Backward: Ringer 2019, section 7.1.3, gave Aitken 1998, Aitken 2000 and Beckert 2014 (and a questionnaire study cited there, not searched).
- Kuhn 2014's appendix gave ForTheL, Naproche CNL and CLM; Santos 2024, section 2.1, pointed to the null results already found.
- Leads of the grey pass, checked and included: the ETP paper (Bolan 2025), and LeanArchitect, which is the ITP (2026) paper 25 the grey pass could not name (Zhu 2026b).
- Also Lean Atlas, Prove2Me, Lean Copilot, Verbose Lean's ITP paper, two Diproche papers, the Isabelle/Naproche paper.
- Also the error-message papers 2501.05706, 2308.11873 and 2409.18661 (Salmon 2025; Taylor 2024b; Santos 2024). The grey pass's unchecked numbers for the last two are confirmed: 2,565 students and 106 participants.
- Leads the strand did not pursue, out of time or out of strand, then screened at the lead screen (section 4, above). Astrolabe set aside; of the proof-minimization works met in the equational project, Kondylidou 2026 kept, Kinyon's method and the Vampire to Dedukti export set aside.
- Of Lurch's papers, Carter 2013 kept, two set aside and one not found. Of two further Diproche papers, Carl 2020b kept and the other set aside; Koepke's preprints set aside; Cramer's dissertation kept, as Cramer 2013.
- Also not pursued by the strand: two papers on model review of research papers, which concern prose, not a checker. At the lead screen Wu 2026 was kept; the other, Google's Paper Assistant Tool, stays a lead, unread (section 4, above).
- Recalled by the reviewer and verified before use: Commelin 2024, Marceau 2011, Prather 2017, Eremondi 2019, Hentschel 2016, Ringer 2020, Coscoy 1995, Lu 2024, Thakur 2024, and Ganesalingam 2017 (also found by A8).
- Unsupported, as the audit found: 82 titles were recorded as screened for the author strings, where the stated rule gives 72, so 1,023 screened in all where the rule gives 1,013. Per-string counts for A1 to A10 were not recorded.

### Strand C: form and limits

- Existing reviews, searched first by R1 to R4 and from the one survey the grey pass met (Tran Minh 2025). On the person's side, 6: Ouvrier-Buffet 2026, Tran Minh 2025, Zhai 2024, Goddard 2012, Parasuraman 2010, Gleirscher 2023. Held and linked: Stylianides 2024 and Lessing 2025.
- Found on the machine side and handed to strand A: Li 2024b, Weng 2025, Raiyan 2026, and the position paper Yang 2024.
- Not found: a review of the person's side of a loop of person, model and proof assistant.
- Held elsewhere and not repeated: structured proofs and Lamport (mathematical-writing review, sections 4 and 5); cognitive load and worked examples (learning-science review, section 3); model help and learning (exercise-sets review, section 5).

Terms searched three ways:

| Concept | Academic name | Acronym | Authors searched |
|---|---|---|---|
| proof assistants in teaching | proof assistant, interactive theorem prover, teaching, transition to proof | ITP | Iannone, Thoma, Hanna, Massot, Portegies, Narboux, Carl |
| explicit structure | structured proof | none | Lamport, Leron, Fuller (held) |
| over-reliance | overreliance, automation bias, metacognitive laziness | AB | Parasuraman, Goddard, Buçinca |
| trust in the checker | trusted kernel, de Bruijn criterion, Pollack-consistency, proof auditing | TCB | Pollack, Wiedijk, Harrison, Adams, Carneiro |
| the gap | formal and informal proof, surveyability | none | Tymoczko, Rav, Tanswell, Avigad |
| cost | de Bruijn factor, proof engineering effort | none | Wiedijk, Matichuk |
| person, model and prover | user study, interview, mathematicians, language model | LLM | Collins, Frieder, Ranade |

- Semantic Scholar ran between 15:02 and 15:54 UTC, sorted by citations; arXiv between 14:59 and 15:13 UTC; OpenAlex counted at 14:37 UTC.
- The Semantic Scholar counts of L1 to L10 arrived after the strand's protocol was written, between 15:56 and 16:18 UTC, marked "late" below.
- L5 was refused 12 times, and L7 to L10 were not reached before the run's cap.

| Id | String as run (Semantic Scholar syntax) | Semantic Scholar | arXiv | OpenAlex |
|---|---|---|---|---|
| R1 | ("proof assistant" \| "proof assistants" \| "interactive theorem prover" \| "interactive theorem provers") +(teaching \| education) +(survey \| review) | 8 | 3 | 16 |
| R2 | ("theorem prover" \| "theorem provers" \| "proof assistant") +("mathematics education" \| "proof education") +("systematic review" \| "literature review" \| "mapping study") | 0 | 3 | 2 |
| R3 | (overreliance \| "over-reliance" \| "automation bias") +("artificial intelligence" \| "large language model" \| ChatGPT \| "generative AI") +("systematic review" \| "literature review") | 602 | 4 | 1,078 |
| R4 | ("formal mathematics" \| autoformalization \| "formal mathematical reasoning" \| "AI for mathematics") +(survey \| "position paper") | 186 | 4 | 92 |
| C1 | ("proof assistant" \| "proof assistants") +(students \| undergraduate) +(proof \| proving) | 131 | 32 | 119 |
| C2 | Lean +("theorem prover" \| "proof assistant") +(students \| undergraduate \| classroom) | 41 | 3 | 54 |
| C3 | ("interactive theorem prover" \| "interactive theorem proving" \| "interactive theorem provers") +(learning \| students) +(study \| experiment \| evaluation) | 44 | 0 | 77 |
| C4 | (Coq \| Isabelle \| Lean \| Rocq) +("introduction to proof" \| "transition to proof" \| "proof writing") | 7 | 1 | 11 |
| C5 | Waterproof +("proof assistant" \| proof) | 1,712 | 3 | 885 |
| C6 | Diproche \| (Lurch +proof +students) | 11 | 4 | 15 |
| C7 | ("structured proof" \| "structured proofs") +(comprehension \| students \| teaching) | 24 | 1 | 37 |
| C8 | (formalization \| formalisation) +mathematicians +("proof assistant" \| Lean) +(understanding \| interview \| survey \| experience) | 14 | 32 | 14 |
| C9 | "de Bruijn factor" | 4 | 0 | 3 |
| C10 | ("proof assistant" \| "theorem prover") +(logic) +(course \| teaching) +(evaluation \| students) | 124 | 12 | 91 |
| L1 | ("trusted kernel" \| "de Bruijn criterion" \| "trusted computing base") +("proof assistant" \| "proof checker" \| "theorem prover") | 64 (late, 15:56) | 3 | 68 |
| L2 | ("soundness bug" \| "soundness bugs" \| "bugs") +("proof assistant" \| "proof assistants") +(empirical \| study) | 21 (late, 15:59) | 0 | 25 |
| L3 | ("formal proof" \| "formal proofs") +("informal proof" \| "informal proofs") +(mathematical practice \| gap \| philosophy) | 21 (late, 16:03) | 11 | 15 |
| L4 | surveyability +(proof \| "computer-assisted proof") | 17,142 (late, 16:06; unusable) | 10 | 20,120 |
| L5 | (overreliance \| "over-reliance" \| "metacognitive laziness") +("large language model" \| ChatGPT \| "generative AI") +(learning \| students) | not obtained (HTTP 429 after 12 tries) | 17 | 2,891 |
| L6 | ("large language model" \| "large language models" \| LLM) +("theorem proving" \| "proof assistant" \| Lean) +("user study" \| interview \| "human study" \| mathematicians) | 43 (late, 16:18) | 0 | 68 |
| L7 | ("proof engineering" \| "formal verification") +(cost \| effort \| productivity) +(empirical \| estimation \| measured) | not obtained (run cap) | 9 | 168 |
| L8 | mathematicians +("language models" \| ChatGPT) +proofs +(evaluation \| interactive \| correctness) | not obtained (run cap) | 12 | 41 |
| L9 | ("proof auditing" \| "statement auditing" \| "audit") +("formal proof" \| "formalised mathematics" \| "formalized mathematics") | not obtained (run cap) | 10 | 401 |
| L10 | ("machine-checked proof" \| "computer-verified proof" \| "formal verification") +(trust \| reliability) +(mathematics \| mathematical) | not obtained (run cap) | 7 | 400 |

The arXiv forms of these strings, in abstract fields:

| Id | arXiv form, abstract fields |
|---|---|
| R1 | `abs:"proof assistants" AND abs:teaching AND abs:survey` |
| R2 | `abs:"theorem provers" AND abs:"mathematics education"` |
| R3 | `abs:overreliance AND abs:"systematic review"` |
| R4 | `abs:"formal mathematical reasoning" AND (abs:survey OR abs:position)` |
| C1 | `abs:"proof assistant" AND abs:students AND abs:proof` |
| C2 | `abs:Lean AND abs:"theorem prover" AND abs:students` |
| C3 | `abs:"interactive theorem proving" AND abs:students AND abs:study` |
| C4 | `abs:"proof writing" AND (abs:Lean OR abs:Coq OR abs:Isabelle)` |
| C5 | `abs:Waterproof AND abs:proof` |
| C6 | `abs:Diproche OR (abs:Lurch AND abs:proof)` |
| C7 | `abs:"structured proofs" AND abs:students` |
| C8 | `abs:formalization AND abs:mathematicians AND abs:Lean` |
| C9 | `abs:"de Bruijn factor"` |
| C10 | `abs:"proof assistant" AND abs:logic AND abs:course` |
| L1 | `abs:"de Bruijn criterion" OR (abs:"trusted kernel" AND abs:proof)` |
| L2 | `abs:bugs AND abs:"proof assistants" AND abs:empirical` |
| L3 | `abs:"formal proofs" AND abs:"informal proofs"` |
| L4 | `abs:surveyability` |
| L5 | `abs:overreliance AND (abs:ChatGPT OR abs:"large language models") AND abs:students` |
| L6 | `abs:"user study" AND abs:"theorem proving" AND abs:"language models"` |
| L7 | `abs:"proof engineering" AND (abs:cost OR abs:effort)` |
| L8 | `abs:mathematicians AND abs:"language models" AND abs:proofs AND abs:evaluation` |
| L9 | `abs:audit AND abs:"formal proof"` |
| L10 | `abs:"machine-checked" AND abs:trust AND abs:mathematics` |

- Zero means the query was wrong, not that nothing exists. R2 returned 0 on Semantic Scholar and was covered by R1 and C10; C3, C9, L2 and L6 returned 0 on arXiv and were rephrased as A3 to A5 below.
- Unusable counts: L4 on Semantic Scholar (17,142) and OpenAlex (20,120) matches survey for surveyability; C5 on Semantic Scholar and OpenAlex is mostly waterproof materials. Both were screened by title only for the relevant few.

Five strings ran on arXiv only, through its API, sorted by relevance:

| Id | String as run | Results |
|---|---|---|
| A1 | `ti:"survey" AND (ti:"AI for mathematics" OR ti:"AI4Math" OR ti:"mathematical reasoning" OR ti:"theorem proving" OR ti:"autoformalization")` | 8 |
| A2 | `ti:"Lean" AND (abs:students OR abs:classroom OR abs:undergraduate) AND (abs:proof OR abs:teaching)` | 2 |
| A3 | `(abs:Lean OR abs:"proof assistant" OR abs:"theorem prover") AND (abs:tutor OR abs:tutoring OR abs:students OR abs:education) AND (abs:"language model" OR abs:"language models" OR abs:LLM)`, from 2023 | 17 |
| A4 | `abs:mathematicians AND (abs:interview OR abs:interviews OR abs:survey OR abs:"user study") AND (abs:Lean OR abs:"proof assistant" OR abs:"proof assistants" OR abs:formalization)` | 2 |
| A5 | `(abs:bugs OR abs:"soundness") AND (abs:"proof assistants" OR abs:"proof assistant") AND (abs:empirical OR abs:study)` | 15, none relevant |

- Titles were resolved to DOIs on Crossref by bibliographic query, and abstracts read on OpenAlex by DOI, with no mailto and no key.
- Screening: the OpenAlex top 15 of 23 strings (L4 unusable), the Semantic Scholar top 15 where the call succeeded, all 44 arXiv-only results, and the citing works below; abstracts were read for every candidate.
- Backward snowballing: the reference list of Tran Minh 2025 gave Hanna 2021, Böhne 2018, Hales 2017, Bartzia 2026, and a work by Keenan and Omar (2024) for strand B.
- Those of Ouvrier-Buffet 2026 gave Kerjean 2022, and of Thoma 2022 gave Avigad 2019.
- Forward, through the OpenAlex citation filter, no key: Thoma 2022, 24 citing works, all screened; Pollack 1997, 48, the 20 most cited screened; Wiedijk 2012, 13, all; Adams 2016, 4, all. They gave Iannone 2023, Hanna 2024, Wemmenhove 2024, Iannone 2025b, Harrison 2006 and Gleirscher 2023.
- Forward, through the Semantic Scholar citations endpoint: refused (HTTP 429) for Thoma 2022 at 15:27 UTC; the OpenAlex filter stands in for it.
- Leads of the grey pass checked where they bear on Q4 and Q5: Thoma 2022, Iannone 2025a, Massot 2024, the Waterproof and Diproche papers. Also checked: Klowden 2026, Commelin 2026, Carneiro 2024, and arXiv 2607.13662 (read, not used).
- Not opened: Carneiro's thesis (2019), Werner (1997), Wiedijk's seventeen provers, Hartnett (2026), Alper (2026).
- 17 works were named from the reviewer's memory and verified on Crossref or arXiv before use.
- Unsupported, as the audit found: the strand recorded its exclusions by title rounded to tens, which with the 57 included account for about 350 titles, where its stated rule gives 584 screened. Titles screened per string were not logged.

- String ids are each strand's own: strand B's A1 to A10 are author strings and strand C's A1 to A5 arXiv-only strings, not strand A's sub-questions; in [sources](sources.md) a strand letter precedes them.

## 5. Grey search, formal side

- Types: tool repositories and documentation, because the tools are the practice; the Lean reference and release notes, the checker's account of its own feedback; company pages, as their owners' claims.
- Producers: the practitioners who run the largest projects (Tao, Buzzard and their guests), who report workflows; the Lean community forum's public archive and Q/A sites, for practitioners' own questions.
- Engine: a general web search engine, first result page per string, no login. Results personalise and change.

### Web strings

| Id | String as run | Shown | Included |
|---|---|---|---|
| G1 | Lean blueprint projects list leanblueprint dependency graph formalization | 10 | 0 (papers only, to leads) |
| G2 | autoformalization Lean tool natural language statement to Lean 4 | 9 | 2 (StepFun 2025, Numina 2025) |
| G3 | controlled natural language proof checker Naproche ForTheL | 9 | 0 (papers; site visited, P) |
| G4 | Lean 4 error messages explanations improve readability error explanation | 10 | 2 (Lean FRO 2025, 2026c) |
| G5 | Lean Verbose Massot controlled natural language Lean tactics teaching | 10 | 1 (Massot 2026b) |
| G6 | Isabelle Isar readable structured proof language what it asks of the writer | 9 | 0 (manuals timed out; P) |
| G7 | Lean Copilot LeanDojo suggest_tactics LLM proof automation README | 10 | 1 (LeanDojo 2026) |
| G8 | Terence Tao blog Lean formalization AI tools experience | 9 | 0 (secondary only) |
| G8b | terrytao.wordpress.com Lean AI formalization equational theories project (restricted to that site) | 9 | 1 (Tao 2024) |
| G9 | Kevin Buzzard Xena blog AI Lean formalisation Fermat's Last Theorem blueprint | 9 | 1 (Anthropic 2026c) |
| G10 | Harmonic Aristotle Lean autoformalization formal verification claims | 19 | 2 (Harmonic 2024, Rivin 2026) |
| G11 | LLM explain Lean error message beginner feedback tool | 9 | 0 (none on Lean; C and Python papers to leads) |
| G12 | leanblueprint checkdecls GitHub Actions CI blueprint docgen-action | 9 | 1 (Zhu 2026) |
| G13 | Waterproof Coq Rocq students natural language proofs feedback Eindhoven | 20 | 1 (TUe 2026) |
| G14 | Math Inc Gauss autoformalization agent strong prime number theorem Lean | 10 | 1 (Math Inc 2025) |
| G15 | Lean 4 hint tactic exact? apply? suggestions try this guidance | 29 | 1 (Lean FRO 2026d) |
| G16 | Diproche automated proof checking students natural language feedback Carl | 10 | 0 (papers to leads) |
| G17 | Lurch word processor checks mathematical reasoning natural language proofs | 10 | 1 (Lurch 2026) |
| G18 | lean-lsp-mcp Lean language server MCP agents diagnostics goals | 9 | 1 (Dressler 2026) |
| G19 | Formal Conjectures Google DeepMind repository misformalization review open problems Lean | 28 | 1 (Google DeepMind 2026) |
| G20 | Leanstral Mistral Lean prover agent release | 19 | 1 (Mistral 2026) |
| G21 | AxiomProver Putnam (2025) Lean formal proofs Axiom Math claims | 19 | 1 (Axiom 2026) |
| G22 | tool translate Lean proof into natural language explanation informalization | 10 | 0 (papers to leads) |
| G23 | blueprint LLM agents formalization workflow informal blueprint written by mathematicians AI fills Lean | 28 | 0 (papers to leads) |
| Total | 24 strings | 323 | 19 |

- G8 returned only secondary coverage, so it was rephrased (G8b) and followed by the blog's tag pages (P).
- G11 returned nothing on Lean in three phrasings (G11, G15, G22); Lean-specific guidance was found by producer visits.
- The engine's answer text was used only to find pages; every number was read on the page itself.

### Producer visits (P)

| Producer | Pages read | Included |
|---|---|---|
| leanblueprint repository | README, public metadata | Massot 2026 (carried key, re-read) |
| Tao's blog | three tag pages (11 posts listed), 5 posts read | Tao 2026e, Tao 2026f, Hales 2026 |
| Xena blog | front page (10 posts listed), 3 posts read | Buzzard 2026a, Buzzard 2026b, Avigad 2026 |
| Palomar registry | About, Statement, How to submit, public data API | Palomar 2026; a count |
| Lean FRO | comparator README; release notes 4.35.0 | Lean FRO 2026a, 2026b |
| Mathlib Initiative | formalization.yaml README and template | Mathlib Initiative 2026 |
| Naproche, Isabelle | project site and tutorial; overview page | Naproche 2026, Isabelle 2026 |
| Lean community | lean4game documentation; mathlib statistics page | Lean-community 2026; a count |
| Model cards | DeepSeek-Prover-V2, Goedel-Prover-V2 | DeepSeek 2025, Goedel-LM 2025 |
| Tool repositories | LeanAide, LLMLean, LeanTool | Gadgil 2026, CMU L3 2025, GasStationManager 2026 |
| Forum archive | 8 channel indexes, 24,928 topic titles filtered by keyword, 126 matched, 4 threads read | Vergo 2026; one thread to the other side (LZ 2026b here) |

### Q/A sites

Stack Exchange API 2.3, `search/advanced`, sorted by votes, 30 per page, no key, no login.

| Site | Strings as run | Returned = screened | Included |
|---|---|---|---|
| Proof Assistants | `q=autoformalization` 2; `q=blueprint` 3; `q=controlled natural language` 0; `title=natural language` 2; `title=readable` 0; `title=error message` 0; `q=Naproche` 0; `q=Isar readable` 1; `q=Verbose Lean` 4; `title=declarative` 0; `title=error` 28; `q=human-readable proof` 5; `q=natural language proof` 19; `q=Mizar` 15; `q=LLM` 3; `title=AI` 0; `q=structured proof` 30; `q=hammer suggest` 0 | 112 | 3 (PASE 2022, 2024, 2026) |
| MathOverflow | `q=autoformalization` 2; `q=blueprint Lean` 0; `q=Lean formalization AI` 11; `q=controlled natural language` 9 | 22 | 1 (MathOverflow 2026) |

- Zero-result strings were rephrased in title and body forms before concluding.
- Display names are recorded only for answerers whose answer is used, as the platform shows them.

## 6. Grey search, human side

All on 2026-10-29. No login, no key, no identity sent; public interfaces only.

| Type | Producers | Why |
|---|---|---|
| practitioner blogs | the Xena Project blog (Imperial College); Terence Tao's blog; two blogs reached by snowball | the people who run the largest projects write here first |
| microblog posts | Terence Tao's public Mathstodon account | his journal of each workflow, often with times and line counts |
| community forum | the Lean Zulip public archive | where practitioners report failures and propose checks |
| project documentation | Formal Conjectures, PNT+, the Erdős problems database and wiki, comparator, Verbose Lean, an audit repository | the rules projects actually enforce, and counts |
| Q/A site | Proof Assistants Stack Exchange | voted answers |
| company and organiser pages | Google Research, the STOC 2026 organisers, PostHog | model feedback on writing, as claimed by its owners |
| talks | one seminar abstract | a named failure mode |

### Web strings (a general web search engine)

| Id | String as run | Seen = screened | Included |
|---|---|---|---|
| W1 | Terence Tao Lean formalization GitHub Copilot experience blog | 18 | 0; led to P3 |
| W2 | misformalization Lean statement proved wrong version AI Erdős problem | 36 | 0 new; led to Alexeev 2025 and P5; 5 formal leads |
| W3 | Kevin Buzzard Xena blog AI formalization Lean | 9 | 0; led to P1 |
| W4 | tadamcz formal conjectures language model audit misformalizations review results | 9 | 0; led to Adamczewski 2026; 2 formal leads |
| W5 | erdosproblems.com forum guidelines AI-generated proofs Lean check main statement accuracy | 9 | 0; led to Erdős DB 2026 |
| W6 | Terence Tao YouTube "Formalizing" Lean AI tools video workflow autoformalize equational | 18 | 0; 1 formal lead |
| W7 | STOC 2026 Gemini automated feedback experiment results survey authors found helpful | 18 | Google 2025, STOC 2026; 2 formal leads |
| W8 | LLM documentation linter in CI pull request style guide Vale comparison practitioner write the docs | 27 | PostHog 2026 |
| W9 | "vibe proving" Lean experience report blog mathematician what worked what did not | 36 | Tanswell 2026; 1 formal lead |

### Producer visits

| Id | Producer and route | Listed | Opened | Included |
|---|---|---|---|---|
| P1 | Xena Project blog, public WordPress API, 60 latest titles | 60 | 7 | 7 |
| P2 | Tao's blog, public WordPress API, searches Lean, formalization, AI tools, Aristotle, equational theories | 83 (with repeats) | 8 | 4 |
| P3 | Tao's Mathstodon, public Mastodon API, 1,000 statuses back to 2022-12, keyword filter | 32 matched | 14 read in full | 8 |
| P4 | Lean Zulip archive: stream indexes filtered by title (Machine Learning for Theorem Proving 482 topics, Lean for teaching 171, general, mathlib4, PR reviews) | 117 matched | 9 read, 1 failed | 9 (4 below 10) |
| P5 | GitHub, public API without a token: Formal Conjectures, an audit repository, comparator, PNT+, the Erdős database, Verbose Lean | 11 repositories | 10 documents | 7, plus 3 counts |
| P6 | snowball from P3 to Kirov's blog, then to Paulson's blog | 2 indexes | 6 | 3 |
| P7 | Proof Assistants Stack Exchange, API 2.3, `search/advanced`, `order=desc&sort=votes&pagesize=30` | 72 | 2 | 1 |

- P7 strings: `q=autoformalization` 2, `q=LLM` 3, `title=formalization` 9, `q=blueprint` 3, `q=language model` 16, `q=statement faithful` 0, `q=structured proof` 30, `q=junk value` 0, `q=misformalization` 0, `q=wrong statement` 9.
- Four of them first failed on an encoding error and were rerun in the forms listed.
- Zero results were read as a weak query; the same idea was then run in another form.

### Read again at the merge

- The brief allowed the web again only to settle a conflict between the two sides. Two pages were read once more, on 2026-10-29, without saving them.
- Hales 2026: the sides placed its audit sentence in different sections; the page has the part Lean's design inside the section Is Lean reliable?, so both were right.
- Massot 2026b: the sides gave different contrasts for Verbose Lean's aim; the README's first paragraph says not easier to write.

## 7. Stopping rule

- Stated in the brief before searching, for both sides: top 10 per web string; stop after 5 consecutive results that add no concept; Q/A, top 30 by votes.
- Formal side: every lead of the brief was run, in three forms where the first found nothing; results beyond 10 came from the engine's follow-up pages and were screened by title. The run ended after G22 and G23 added only papers and no new practice concept.
- Human side: web strings returned lists of 9 links, and every title in a list was screened; each producer listing was read in full by title.
- Human side: opening stopped when each of H1 to H4 had at least three sources scoring 10 or more. The last five opened (LZ 2025d, LZ 2025g, LZ 2025h, two snowball posts) added no concept.
- Formal pass, stated before searching: effort bounded, with saturation at 5 consecutive titles adding no concept.
- Strand A: the 15 most cited Semantic Scholar results per string, and every arXiv title returned, up to 34 per string.
- Strand B: the 15 most cited Semantic Scholar results and the first 10 arXiv results per string; evidence exhaustion for F2, F3, F9, F10, F21 and X1 to X5, whose sets are small.
- Strand C: the 15 most cited results per string, with evidence exhaustion for strings under 20 results.

## 8. Selection

- Formal side, include: a source on joining informal mathematical writing to a proof assistant, on translating it, on checking the translation, or on turning a checker's output into guidance. Include also a company's account of its own prover, labelled as its owner's claim.
- Formal side, exclude: papers (listed as leads); news coverage of a primary page that was itself readable; opinion threads with no practice or data; duplicates.
- Human side, include any of: a report of practice where a person works with a model or a proof assistant on reasoning a person wrote; a wrong formal statement caught, and how. Also a check of writing in CI with a model in it, or a report on whether splitting reasoning helped thinking.
- Human side: English, dated or datable, readable without login on the search date.
- Human side, exclude: news rewrites, mirrors and aggregators (about 25 links: secondary); product pages on prover capability (to the formal side); formal papers (to the leads); Vale-in-CI pages already held by document-model (3).
- Both: a page that could not be read is reported in section 11 and never used.
- Formal, strand A, include: papers and preprints with a result or an argument on translating informal mathematics into a proof assistant. Its measurement, its error rate, and the detection of wrong statements count, as do existing reviews of these.
- Strand A, exclude: provers evaluated only on supplied formal statements (their scores are in review Q2); translation into first-order logic, law or software specifications, unless a method transfers (none was kept). Also long-horizon case studies with no measure of faithfulness (LeanMarathon, Landau damping, MIP* = RE, tensor networks).
- Strand B, include: a paper, thesis or preprint with results on a structured informal-to-formal workflow, a CNL or a declarative proof language for mathematics.
- Strand B, include also: results on error messages, proof repair, or explanations of a checker's output, preferably measured on people. Programming error-message studies with people are included as the nearest measured evidence, marked by language.
- Strand B, exclude: program verification with no user or feedback content; formalizations of single theorems; statement translation and faithfulness (strand A); learning outcomes and teaching studies (strand C). Works readable by title only stay out unless they name a system the strand must place, and then they are marked "title and venue only".
- Strand C, include: a study, review or argued paper on a person who writes or reads reasoning in a proof assistant, or with a model and a checker. Its subject is learning and transfer, use of the verdict, research practice, trust, the formal and informal gap, over-reliance, or cost. Reviews and controlled studies of over-reliance outside mathematics are included where no study inside it exists.
- Strand C, exclude: prover and translation performance (strand A); error messages, repair and tool usability (strand B); verification of software except measures of cost; off-topic matches.
- All strands: a work whose text and abstract could not be read is listed as located only, never as support.

## 9. Quality of sources

- The 20 criteria and the threshold: [evidence README](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/evidence/README.md#method).
- A count read from a public listing (stars, downloads, registry totals) is the reviewer's measurement, not a source, and is not scored.
- Formal side, outlet tier: project documentation, company pages, model cards, forum and Q/A pages, tier 2 (0.5); blogs and gists, tier 3 (0); no tier 1 source was found.
- Formal side: a company page scores low on objectivity, as it reports its own success. Q/A authority is 0.5 for the site, plus 1 for an answerer at or above 20,000 reputation, 0.5 at or above 5,000.
- Human side, outlet tier: project documentation, Q/A, company and organiser pages, talk abstracts, tier 2 (0.5); blogs, microblog posts and chat threads, tier 3 (0).
- Human side: A1 is 0 for a personal blog, 0.5 for a moderated forum or site, 1 for an institution; a company page about its own tool scores 0 on O3 (vested interest).
- Human side, impact 1 or 0.5: blogs, 30 comments or 10; Mathstodon, 50 favourites or 10; repositories, 500 stars or 100. Chat threads, 50 messages or 15; Q/A, the shared rule, 30 votes or 10.
- Formal sources are graded, not scored. "measured" means a controlled study, a meta-analysis, or a benchmark with a stated protocol, said which.
- "measured, descriptive" or "measured, qualitative" means counts, logs, surveys or coded interviews, with no comparison group.
- "supported with caveat" means evidence with a stated limit, such as self-selected groups; "convention" means argued, proposed or reported by an owner, untested.
- "not graded" marks a work read by title and venue only; "located only" a work whose text and abstract could not be read.
- A benchmark number is measured on that benchmark only, with its split, its metric (pass@k, or the judge used for faithfulness) and its budget.

## 10. Extraction, synthesis and merge

- Extracted per source by both sides: producer, date, the practice, the claim, any number with where it sits in the source, and whether the number is the source's own.
- Each side wrote its synthesis by its own sub-questions; the merge reorders every finding by Q1 to Q5 in [review](review.md), each with its key and where.
- Keys: one key per work across both sides. Where the sides used different keys for one work, or one key for two works, the formal side's key is kept. That side had already checked its keys against the five bibliographies of the family.
- Keys were then checked by script against the bibliographies of reader-ergonomics-topic (branch and master), reader-ergonomics, reader-ergonomics-academic, reader-ergonomics-presentations and reader-ergonomics-software-design. A key used there for another work took the next free letter; a work already there kept its key. The renamed keys are listed in [sources](sources.md).
- Scores: a source scored by both sides keeps the score of the side that read more of it. That is judged first by the pages read, then by the parts of the source each side cites; the other side's score is given in its row.

### Formal pass

- Extracted per source by each strand: the design, the sample or benchmark, the metric, the judge of faithfulness (person, model or program), the number, and the section where it was read. Synthesis is narrative, by sub-question.
- Each strand was then audited by someone who had not written it: every line carrying a number, or graded measured, checked against its primary source, and the counts of its protocol checked by arithmetic.

| Strand | Rows | Correct | Imprecise | Wrong | Unverifiable | Checked before, or repeats |
|---|---|---|---|---|---|---|
| A | 81 | 63 | 10 | 1 | 0 | 7 |
| B | 95 | 66 | 15 | 1 | 0 | 13 |
| C | 94 | 68 | 11 | 1 | 0 | 14 |
| all | 270 | 197 | 36 | 3 | 0 | 34 |

- The three wrong rows: a comparison of two translators (three at one sample) given as five; a screened count of strand B (1,023) that its own rule makes 1,013.
- And strand C's recorded exclusions, which cannot follow from its rule (584 titles).
- Every wrong and imprecise row was corrected before the merge: budgets and metrics added to benchmark numbers, grades lowered where above their evidence, "(secondary)" added to abstract reads.
- Four works that strand B had read by abstract, behind a paywall, were read afterwards in full through the university library: Wang 2024b, Hentschel 2016, Aitken 2000 and Becker 2019. Their rows give the full texts' numbers.
- The merge: one key per work across the strands and the grey pass, checked against the family's six bibliographies.
- A key used there for another work took the next free letter, so Draft, Sketch and Prove is Jiang 2023c.
- A work met by two strands has one row in [sources](sources.md), its two routes joined, with the grade of the strand that read more of it.
- Its numbers were checked to agree across the merged files.
- Where an audit and a strand still disagreed at the merge, the audit's reading was kept.

## 11. Limits

- One reviewer per side; no second rater on this pass. The six sources both sides scored are the only overlap, compared in [sources](sources.md).
- Formal side: the Isabelle documentation server timed out on the Isar reference manual and the programming tutorial; Isar is covered by its overview page and by Wenzel 1999, held elsewhere.
- Both sides: the forum's public archive stops at 2026-02-28; later threads were not seen. One topic whose link holds `#` returned 404 (human side).
- Formal side: the unauthenticated GitHub search API hit its rate limit once, so the list of most-starred blueprint repositories was not read.
- Videos and talks were located but not watched. The video site served the human side a consent page, so claims about Tao's videos rest on his posts. Social media posts other than Tao's Mathstodon were not read.
- Human side: the audit site is rendered by script, so its repository data were read instead; Mastodon search needs a login, so the public timeline was paged and filtered instead.
- Human side: the web archive's lookup service answered HTTP 429 on the day, so its sources have no archived copies; the formal side linked archived copies where it found them.
- Pages carrying text addressed to automated readers were read as data only.
- Formal side: no PDF was read in this pass.
- Search engines personalise and change; counts on GitHub, PyPI, Palomar and Stack Exchange are those of 2026-10-29, and two moved the same day (Palomar 2026b, GitHub 2026f).

### Formal pass

- One reviewer per strand; no second rater on screening or extraction. The audits checked numbers and grades, not the screening.
- Strand A: full texts were read in the arXiv HTML version, by section, never whole; a number outside the sections read was not seen. Most included works are 2025 and 2026 preprints; venues are given where arXiv or Crossref states one.
- Strand A: Semantic Scholar refused three calls with rate limits; each was rerun once, and the rerun's count is given.
- Strand B: Semantic Scholar refused many calls (429), so one acronym cell failed and five forward lists were not run. Per-reason exclusion counts were not kept.
- Strand B: at the search, the ACM Digital Library and one university repository refused automated reads (403, 405). Aitken 2000, Hentschel 2016 and Wang 2024b were then read by abstract; the university library read came later (section 10).
- Strand C: the Semantic Scholar counts of L1 to L10 came late or not at all (section 4).
- arXiv refused strand C's calls for a few minutes (429), and the ten strings were rerun after a pause.
- Strand C, behind a paywall, listed and not used for numbers: Hanna 2021, Knobelsdorf 2017, Avigad 2019, Nipkow 2012, Harrison 2006, Pierce 2009, Tymoczko 1979, Rav 1999, Tanswell 2015.
- Matichuk 2015 is behind a paywall too; its abstract numbers are used, marked secondary.
- Strand C: Hanna 2024 was read in its author copy, found through OpenAlex. Iannone 2025a was not reached, since the publisher's page asked for a browser check; OpenAlex lists an open repository copy.
- Strand C: 17 works were found from memory and then verified, a bias toward known work, offset only partly by the strings.
- In the university queue, still to be read: Knobelsdorf 2017, Tymoczko 1979 and Avigad 2019.
- The strands saved no PDF or page; texts were read in memory. Text on pages addressed to automated readers was treated as data.
