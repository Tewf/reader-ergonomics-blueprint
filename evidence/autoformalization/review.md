# Review: autoformalization in practice, by the scope's five questions

Findings of both sides of the grey pass, read on 2026-10-29 and merged, by the questions Q1 to Q5 of [frame](frame.md).

Markings: owner, a claim a source makes about itself; **count**, the reviewer's count on a public record; independent, a check by someone other than the owner; example only, a source below 10 of 20 ([sources](sources.md)).
Grade for all of it: practice, convention, untested, unless a line says measured. What is held elsewhere is linked in [frame](frame.md).

## Answer first

| Id | Question | Answer from practice |
|---|---|---|
| Q1 | Prior art | Blueprint projects join informal statements to Lean declarations, checked in CI; the closest to the loop keeps its statements in a short challenge file checked by comparator, with a formalization.yaml mapping each source statement to its Lean name (Tao 2026f; Lean FRO 2026a; Mathlib Initiative 2026); the person's work moves from writing proofs to scoping tasks, checking statements and digesting output. |
| Q2 | Translation | Lean decides the proof, and no program decides whether the statement means what the person meant; wrong statements are common, pass Lean, and are caught by a person rereading the source, by a counterexample, or by a model audit whose claim Lean then checks. |
| Q3 | Feedback | Guidance reaches models in full (errors, goals) and people through mechanisms written ahead of time; model feedback on informal writing is measured only by satisfaction surveys. |
| Q4 | Form | Splitting into small claims is reported to help checking and sharing every time, and to help thinking only where a person did or followed the splitting. |
| Q5 | Limits | A misformalized statement passes Lean, a model judge is not repeatable, kernels have bugs, and model output is long enough that review becomes the bottleneck. |

The figure maps each part of the scope's loop to the practice read; the sections below give the sources.

```text
 person
   │  topic: claim, summary, parts
   ▼
 blueprint node: \uses, \lean, or @[blueprint]
   │
   ▼
 challenge file ◀── translates ── model
   │  statements only, short,       ▲
   │  read by a person              │
   │                                │
   ├─▶ fidelity: same meaning as    │
   │   the topic? human audit;      │
   │   model judge as filter;       │
   │   match to a vetted statement; │
   │   tests                        │
   │                                │ errors, goals
   ▼  proofs                        │ (LSP, refinement)
 solution module ───────────────────┘
   │
   ▼
 comparator / lake check
   │  same statement, permitted axioms,
   │  kernel accepts
   ▼
 person ◀── guidance: named errors, Try this,
            help tactic, hints, checked suggestions
```

## Q1. Prior art: who joins informal writing to Lean, and what each way asks

### Projects and workflows

| Practice | What the person gives | What a program checks | Numbers, with where | Source |
|---|---|---|---|---|
| leanblueprint | LaTeX statements with `\uses`, `\lean`, `\leanok`; the tool is little tied to Lean, a practitioner estimating two days to port its core (PASE 2024, top answer) | dependency graph built in CI; `checkdecls` checks every named Lean declaration exists | 37 distinct projects listed (README, list after the origin paragraph); **count**: 394 stars; 31,309 downloads last month, not a count of users | Massot 2026; PASE 2024; GitHub 2026e; PyPI 2026 |
| LeanArchitect | a `@[blueprint]` tag on Lean declarations, with `uses`, exported to LaTeX; enforced in PNT+ (PNT-plus 2026, sections 6 and 12) | `lake build :blueprint` | **count**: 94 stars | Zhu 2026; PNT-plus 2026; GitHub 2026e |
| side-by-side blueprint | the informal text inside the Lean attribute; one node per declaration | rendered beside the code in the editor | a prototype, 2026-02 | Vergo 2026 |
| PNT+ and IEANTN | a blueprint of bite-sized lemmas, each claimed as a task sized XS to XL; AI use disclosed; the person writes, scopes and reviews the blueprint | every submission must typecheck in CI; `checkdecls` checks that each named declaration exists; no comparator step | the label counts below | Tao 2026e; PNT-plus 2026; GitHub 2026i |
| ETP | a crowd of contributors; models play no major role | Lean, and automated provers | 4694 laws (Tao 2024, first paragraph) | Tao 2024; Tao 2025d |
| Erdős problems | statements from Formal Conjectures; one model explains the proof, another formalizes it; the person picks the problem, checks and posts | Lean, CI on GitHub | about 240 statements and 17 solutions formalized on 2025-12-05 (Alexeev 2025, section Background); 975 statements and 318 solutions of 1,221 problems by 2026-10-29 (Erdős DB 2026, STATISTICS page, the database's own count); the pipeline ran about ten times, with occasional manual repair (Alexeev 2025, section Human formalization with AI) | Alexeev 2025; Erdős DB 2026 |
| statement graph with prose | each statement keeps a natural-language description; statements and proofs in separate files | Lean; comparator against mathlib's statement | owner: an 86-page human blueprint for the initial phase | Anthropic 2026c |
| challenge file, comparator, formalization.yaml | statements, proofs, and an alignment table from source statements to Lean names; the bare minimum advised to a mathematician, with the challenge file as simple and readable as possible (MathOverflow 2026, top answer) | comparator, a program; a model judge, as a filter; comparator entered Lean 4.35.0 (2026-10-12) as `lake comparator` and `lake check` (Lean FRO 2026b, Highlights; Lean FRO 2026a, Deprecation) | **count**: 845 registered results from 660 projects at the formal side's read on 2026-10-29; 847 from 661 at the audit later that day | Palomar 2026; Palomar 2026b; Mathlib Initiative 2026; MathOverflow 2026 |
| statements only | formal statements of open problems or of journal theorems; unit-test statements for new definitions | human review; prover runs over the statements | 50 Annals theorems stated, about 20% of Annals papers since 2020 (Buzzard 2026b, section A challenge for humans) | Google DeepMind 2026; Buzzard 2026b |
| AI-written, AI-reviewed libraries | human roadmaps; AI writes; other AIs review against rubrics | Lean | Tau Ceti about 3 million lines; Formal Frontier 41 libraries, about 200k lines (Avigad 2026, section Lessons so far) | Avigad 2026 |
| textbook exercises | a numbered sketch of each proof, for Anthropic's coding agent run as two agents | Lean | three textbook sections in a weekend, about two hours at the computer; he estimates ten times more without AI (Kirov 2026a, section Results) | Kirov 2026a; Kirov 2026b |

- **count**: mathlib holds 291,665 theorems, 139,769 definitions and 772 contributors (Mathlib 2026b); Avigad 2026 gives 950 contributors and 65 reviewers; the counts differ by method.
- Grade: convention, untested; the counts are measured, descriptive.

### What the person's work becomes

| Change | Source, with where |
|---|---|
| The plan comes first: natural-language scaffolding and expert guidance from the person, the agent formalizing (owner); a sketch numbered by placeholder, the model asked to align its proof with it; tasks scoped smaller and in advance, expecting an AI proof to arrive | Math Inc 2025, fifth paragraph; Kirov 2026b, case 8.2.5; Tao 2026i, post 3 |
| Statements copy the paper verbatim and keep the citation, as the audit trail; each AI-assisted pull request names its tool, and a CI job reads the line and adds a label | PNT-plus 2026, section 3; section 13, rule 1 |
| The agent is configured: style preferences learned from model drafts go in a skills file; skills files, an MCP server for the Lean language server, a second model asked for review | Tao 2026h; LZ 2025d (example only); LZ 2026a; Kirov 2026a |
| Checking is fast: the community checked the Erdős 707 proof within thirty minutes, which Tao calls instant refereeing; once a claim is formalized, disputes about it stop and discussion moves to method | Tao 2025b, post 3 of 3; Tao 2024, paragraph on the project's progress |
| Time drops, by the practitioners' own estimates, with no control: IEANTN lemmas that took volunteers weeks were done by AI within hours by 2026-06; a vibe-coded formalization took two or three hours of attention against an estimated six by hand | Tao 2026i, posts 1 and 2 of 3; Tao 2025c, post 4 of 4 |
| **count**, descriptive: in PNT+, 362 of 1,399 pull requests carry the ai label, 291 merged and 58 closed unmerged; without it, 896 merged and 130 closed unmerged; labels began on 2026-01-05, so the two groups cover different periods | GitHub 2026g |

### Readable formal languages: what they ask of the writer

| Language | Asked of the writer | What the machine does | Stars (**count**, GitHub 2026e) | Source |
|---|---|---|---|---|
| Naproche (ForTheL) | a controlled language inside LaTeX; where the prover fails, a list of intermediate statements | turns each step into an obligation for ATPs; a failed goal is underlined in red after a timeout | 53, read by both sides | Naproche 2026 |
| Verbose Lean | fixed English or French phrasings, which are Lean tactics; the teacher configures them | Lean checks; a help tactic and a suggestion widget | 162 | Massot 2026b |
| Waterproof (Rocq) | a declarative style that reads like mathematical text | Rocq checks; its team calls the feedback hard to interpret | 44 | PASE 2022; TUe 2026 |
| Isar (Isabelle) | a structured proof text, which the owner calls understandable by people and machines; explicit premises and locales, a guard against false context | continuous checking; Sledgehammer calls external provers | not counted | Isabelle 2026; Paulson 2026 |
| Lurch | the meaningful parts of the text marked | checks the marked claims | not counted | Lurch 2026 (example only) |

- Naproche's own tutorial warns that complete, unambiguous text in a readable language is subtle and needs ample exercise (Naproche 2026, introduction).
- Verbose Lean's stated aim is Lean code easier to transfer to a paper proof, not easier to write (owner; Massot 2026b, README, first paragraph, read again at the merge). The human side gave the contrast as not teaching Lean, citing LZ 2025f as well.
- A controlled language without editor support was dropped: Coq's declarative mode was removed, and the accepted answer calls its exact phrasing almost impossible to remember (PASE 2022).
- Two families appear (the formal side's synthesis): prover-backed languages let the writer skip obvious steps and ask for more only where the prover fails; tactic-backed ones ask for every step in fixed words.
- Grade: convention, untested; effects on writers are reported by owners or in papers left for the formal pass ([formal leads](formal-leads.md)).

## Q2. Translation: how faithful, and how a wrong statement is caught

### What the products claim, and who checked

| Product | Claim | Who checked |
|---|---|---|
| Aristotle | 90% on MiniF2F; many benchmark statements fixed, some having become trivial or impossible in Lean; a user describes a sorry-filling mode, then an informal mode that formalizes LaTeX, used in the Erdős pipeline | owner (Harmonic 2024, section 90% on MiniF2F); the modes, Alexeev 2025 |
| Gauss | the strong prime number theorem in three weeks; about 25,000 lines; over 1,000 theorems and definitions | owner (Math Inc 2025, third and fourth paragraphs) |
| an Anthropic model, on Prove2Me | Fermat's Last Theorem in 11 days; 13 million lines; 29,500 theorems used; comparator matched mathlib's statement | owner (Anthropic 2026c); independent: Buzzard compiled it and ran comparator, which passed; over 13.4 million lines, formalized in an 11 day period; nearly 20 times mathlib's compile time on 96 cores (Buzzard 2026a, sections The code base and What this work is). Checked again against the post: the proof follows the 1995 Darmon, Diamond and Taylor account of the Wiles and Taylor-Wiles argument, not the modern proof; it covers primes p at least 17, the smaller ones handled before; and Buzzard writes that it tells us essentially nothing new mathematically (Buzzard 2026a) |
| Leanstral | on FLTEval, built from pull requests to the FLT project: 26.3 at pass@2, 31.9 at pass@16 | owner (Mistral 2026, benchmark paragraph) |
| AxiomProver | 12 of 12 Putnam (2025) problems, 8 within exam time; Lean files released | owner (Axiom 2026, second paragraph) |
| DeepSeek-Prover-V2 | 88.9% on MiniF2F-test; 49 of 658 PutnamBench problems | owner (DeepSeek 2025, model card summary) |
| Goedel-Prover-V2 | 84.6% (8B) and 88.0% (32B) on MiniF2F at pass@32 | owner (Goedel-LM 2025, introduction) |
| StepFun-Formalizer, Kimina-Autoformalizer | statement translators; StepFun scored with BEq; Kimina ends each statement with `by sorry` | owner, each (StepFun 2025; Numina 2025, example only) |
| LeanAide | in the editor, `#theorem "..." >> translate_theorem`, and `#doc` for the reverse | none (Gadgil 2026) |
| a prover on 823 problems | 97.6% sorry-free, 67.3% judged faithful by a single model arbiter, no human check | example only (Rivin 2026, headline list) |

- Prover scores are measured on formal statements someone supplied; Harmonic says it rewrote those statements before scoring (Harmonic 2024).
- Company claims met by the human side and not read at the source (Hales 2026; Buzzard 2026d; Buzzard 2026a). They are Math Inc's Gauss on sphere packing, Logical Intelligence on the unit distance disproof, Logos Research's autoformalization tool, and OpenAI's models.

### Wrong statements caught in practice

The figure follows a claim from its source to the kernel; each step names a failure and what caught it in practice.

```text
 informal source (paper, problem)
 │  fails: vague or wrong source
 │  caught by: formalizing, or a counterexample
 │  Buzzard 2024, 2026d
 ▼
 formal statement (person or model)
 │  fails: misformalization (typo, missing
 │  hypothesis, wrong definition)
 │  caught by: a person rereading the source, a
 │  model audit, a trivial-proof test
 │  Alexeev 2025, Adamczewski 2026
 ▼
 proof (model)
 │  fails: added axiom, changed meaning (a local
 │  instance, a hidden placeholder)
 │  caught by: comparator, the axiom check, a
 │  sandbox
 │  Lean FRO 2026a, LZ 2025a
 ▼
 kernel accepts
    fails: soundness bug
    caught by: other kernels and a verified checker
    Hales 2026
```

| Case | What was wrong | Caught by | Source |
|---|---|---|---|
| Erdős 480 and 56 | in 480, m ≠ 0 written for n ≠ 0; in 56, a hypothesis implicit in the source was missing | a model counterexample: in 480 using the typo and a junk value; in 56 a trivial one with tiny parameters, such as 2 | Alexeev 2025, section Misformalization |
| Erdős 124 | the solved version was likely not the one Erdős meant | the person who ran the model, and public discussion, after the proof | Alexeev 2025, section Formalization entirely by AI |
| Erdős 707 | a nonzero condition on a modulus was omitted | the authors, while formalizing the proof | Tao 2025b, post 2 |
| Erdős 728 | a constant read as small was meant to be large | a closer human reading of the source paper, days later | Tao 2026k, posts 2 and 3 |
| Annals theorems | typos that made theorems trivially false, four of them in papers by Fields Medallists | writing the formal statement, which surfaced the missing hypotheses | Buzzard 2026b, section A challenge for humans and the one after it |
| an AI definition of a reductive group | an empty class and a field of type True | an expert reading the pull request | LZ 2026a |
| a generated proof | `Nat.primeCounting'` used where the asker meant the prime counting function, off by one | a reader; the reply says to learn enough Lean to read statements, and that generated comments are unverified | LZ 2026b (read, not scored) |
| a refereed paper | an assumption, false, that every z is nonzero, in every theorem | a referee wary of proofs that looked too simple | Paulson 2026 |

- Alexeev found misformalization in three styles, low-level bugs, missing hypotheses and a mistake of the person stating the problem (section Misformalization), and more often than he expected (section Takeaways).
- In one lab's release, informal and formal pairs diverge in subtle or significant ways (Avigad 2026, section The concerns).
- **count**, descriptive: in Formal Conjectures, 787 items carry the misformalization label, 533 pull requests and 254 issues (GitHub 2026f). They are out of 5,053 pull requests and 2,589 issues at the human side's count. One more pull request had opened by the audit later the same day (5,054); the labelled counts were unchanged.
- **count**, descriptive: the Erdős wiki labels some outcomes Solution to variant problem (Erdős-wiki 2026, its rows counted on 2026-10-29). That is 8 of 61 rows for AI alone and 10 of 132 for AI with people, in data frozen at 2026-06-30.

### Checks against a wrong statement

| Check | Decided by | Source, with where |
|---|---|---|
| the statement compiles, which is necessary, not sufficient, for a faithful statement; then prove the negation, derive False from the hypotheses, test definitional equality, or score with BEq+ | program | PASE 2026, accepted answer |
| the solution module proves exactly the challenge file's statements, with permitted axioms; it cannot check that the challenge means what the person meant, and definition holes can be gamed | program | Lean FRO 2026a, README and section Definition Holes |
| SafeVerify, lean4checker, the axiom check and a sandbox, against an added axiom or a changed meaning | program | LZ 2025a |
| reuse a statement already vetted (mathlib's FLT; Formal Conjectures) | program, after human vetting | Anthropic 2026c; Avigad 2026; Google DeepMind 2026 |
| run provers over all statements (human review, and periodic AlphaProof runs); unit-test statements for definitions; a fixed misformalization bumps the benchmark version | program, then person | Google DeepMind 2026, README and contributing guide |
| tests for a definition: lemmas it must satisfy before anyone trusts it | program | LZ 2026a |
| a model audit of every file against its cited source: 1,268 files, 139 flagged, 209 misformalizations claimed; Lean compiled a short proof or refutation for 56 of the 139, a program-checked sign that the statement as written is trivially settled; the output is called findings for review, not verdicts, and a person reviews each draft issue before it is filed | model, then program, then person | Adamczewski 2026, run 2026-09-11 metadata and README |
| the audit's issues: of 175, 155 closed as completed, 5 as not planned, 15 open; closing is the maintainers' act, not a check of each finding | person | **count**, GitHub 2026f |
| the informal account matches the challenge file; one repository at one commit scored 5, then 4, on one axis over two runs, so Palomar now publishes only whether a blocking problem was found | model, not repeatable | Palomar 2026, About, last section on scores |
| back-translation compared by embeddings | model | PASE 2026 |
| a template that puts the statement and its definitions in one place, so a referee reads only those | person | LZ 2025e |
| statement fidelity audited, definitions too, since Lean cannot check that a definition matches the concept it names | person | Hales 2026; Tao 2026e; Buzzard 2025; Paulson 2026 |
| Buzzard's own check, under 5 minutes: the statement uses only mathlib concepts, says what is claimed, and compiles | person | Buzzard 2026d, section Group schemes |

- Hales asks that no Lean proof be accepted until "a human audit is performed to ensure statement fidelity" (Hales 2026, section Is Lean reliable?, part Lean's design). The formal side placed it in the section, the human side in the part; the page, read again at the merge, has the part inside the section.
- Example only: messy model code can hide assumptions that make a statement trivial (Tanswell 2026); an informal model proof skipped all cases but one (LZ 2025g).
- Grade: owners' claims, with one independent check; no grey faithfulness number reaches the threshold; the audit and label counts are measured, descriptive.

## Q3. Feedback: from the checker's output to guidance

| Mechanism | For | Model | What it gives | Count | Source |
|---|---|---|---|---|---|
| named errors | person | no | since 4.22.0 (2025-08-14); 14 explanation pages, each with causes and Original and Fixed examples; an unknown name also gets a code action proposing near names | | Lean FRO 2025; Lean FRO 2026c |
| `exact?`, `apply?`, `simp?` | person | no | a `Try this` suggestion | | Lean FRO 2026d |
| help tactic | student | no | rule-based help providers chosen by the teacher; writing one needs programming | | Massot 2026b |
| strong automation beside the student, proposed | student | no | a teacher, who calls Lean's error messages cryptic, proposes automation that says a fact is true but more steps must be written | | LZ 2025f |
| game hints | player | no | text written by the author, shown when the player's goal matches | lean4game 575 stars | Lean-community 2026 |
| failed obligation | writer | no | the step underlined; the writer adds intermediate statements | | Naproche 2026 |
| Waterproof's feedback | student | no | its own team says it may be hard to interpret, and plans a redesign (owner) | | TUe 2026 |
| suggested tactics and proofs | person | yes | clickable next tactics or whole proofs; LLMLean checks them in Lean and can refine from the errors; Tao described in 2023 their loop of sending Lean errors back to the model | Lean Copilot 1,339 stars, read by both sides; LeanDojo 850, read by the human side; LLMLean 216 | CMU L3 2025; LeanDojo 2026; Tao 2023m |
| errors and goals to an agent | model | yes | diagnostics, goals and hover text through LSP; Leanstral was trained for this tool | lean-lsp-mcp 541 stars, 730,424 downloads last month | Dressler 2026; Mistral 2026; GasStationManager 2026 |
| self-correction | model | yes | two rounds of rewriting from compiler feedback | | Goedel-LM 2025 |
| adversarial review | model | yes | other models review AI contributions against rubrics | | Avigad 2026 |

Stars and downloads: **count** (GitHub 2026e; PyPI 2026).

- Without a model, guidance is written ahead of time and covers what its author foresaw (the formal side's synthesis).
- With a model, the verdict goes to the model; in the tools read, the person receives a checked suggestion or a proof, not an explanation (the formal side's synthesis).

### Checks of form in CI, and model feedback on writing

| Practice | A checker behind it | Source, with where |
|---|---|---|
| CI rejects any proof that does not typecheck, and labels AI-assisted pull requests | Lean | Tao 2026e; PNT-plus 2026, section 13 |
| blueprint fields carry LaTeX rules; the LaTeX run downstream catches their errors, not the Lean build step | LaTeX | PNT-plus 2026, section 6 |
| a model reviewed theory papers before submission to STOC 2026; owner, a survey: over 80% of submitted papers opted in, and of consenting respondents 97% found it helpful and 81% said clarity improved; the organisers warn that a flagged error need not be an error, and no false-positive rate is given | none | STOC 2026; Google 2025; the forum thread that led to it, LZ 2025h (example only) |
| the model audit of Q2, whose claims Lean tests by compiling | Lean | Adamczewski 2026 |
| a model triaged a referee report: unambiguous fixes for 11 of 12 points, two options for the twelfth, chosen by the person; under fifteen minutes in all | none | Tao 2026g |
| a model rewrote a Lean-checked proof into readable prose; a later version filled gaps in the original informal proof | Lean, for the proof | Tao 2026k, post 3 |
| detect with a linter, fix with a model, since models are slow and unreliable as linters | the linter | PostHog 2026 (example only) |

- No grey source measured whether a person fixes a Lean error better with any of these mechanisms, or whether a CI check of clarity changes what a person writes. Studies on C and Python are leads.
- Grade: convention, untested; the survey is its owner's.

## Q4. Form: do small claims help thinking, or only checking?

| Helps | Report | Source, with where |
|---|---|---|
| thinking | Lean showed Scholze one goal at a time, and the proof assistant helped him understand his own proof; he learned what made it work, a reduction from a non-convex problem over the reals to a convex one over the integers; the blueprint came after formalization, about 2.5 times longer than the notes, and he puts the de Bruijn factor around 20 | Scholze 2021 |
| thinking | Lean pushed Tao to plan ahead and abstract many small lemmas, more than he would by hand | Tao 2023m, post of 2023-11-05 |
| thinking | writing a prover's output as named lemmas made it readable and led to fixing steps in the Lean proof | LZ 2025c, the human write-up of 650 => 448 |
| thinking | formalization changed the mathematics: it exposed a false lemma in a standard source on divided powers, and isolated a simpler construction that replaced a hard one in the Liquid Tensor Experiment | Buzzard 2024; PASE 2022b, top answer |
| checking, sharing | the split lets a person prove without the whole: contributors prove one lemma without the global picture; Tao formalized a one-page proof in 33 minutes with no high-level idea of it | Tao 2023m, post of 2023-11-19; Tao 2025a |
| checking | when someone else decides the lemmas, Kirov gets no practice at decomposing a theorem, the hardest part | Kirov 2026a, section Is there a problem |
| checking | the checked proof still needs digestion: a Lean-checked AI proof needed several days of it to become a paper; the Erdős database keeps a Lean-checked solution at its informal status until a person has digested it | Tao 2026j; Erdős DB 2026, STATISTICS |
| checking | a formal proof shows little of its ideas: it gives confidence but little sign of where the ideas are; readers of a machine geometry proof needed to draw the figure by hand, and reading Lean line by line is tedious | Buzzard 2026c, section Thurston's view; Axiom 2026, sections on problems B1 and A2 |
| teaching | Verbose Lean aims at the transfer to a paper proof (Q1); whether writing in Lean helps students write better proofs without it was asked, and answered only by pointers to papers; Verbose Lean's ITP (2024) paper, the Waterproof course studies and the Diproche classroom trial are leads | LZ 2025f; [formal leads](formal-leads.md) |

- Grade: practice reports, untested; no controlled study in either side.

## Q5. Limits: where the loop fails

| Failure | Source, with where |
|---|---|
| a misformalized statement cannot be detected by the proof assistant | Tao 2026e, paragraph on AI use |
| missing definitions block even stating a theorem | Buzzard 2026b |
| several kernel soundness bugs were found in July and 2026-08, with AI; about 25 independent Lean kernels exist, and cross-checking missed one bug; the human side also notes a checker with a consistency proof | Hales 2026, sections Summer of Soundness Bugs and Bug extermination |
| the model judge is not repeatable (Q2) | Palomar 2026 |
| model proofs are long: 1,125 lines, many proving trivial things; hundreds of lines longer than a person's; AI proofs carry bloat that humans must edit, and AI use must be disclosed | Tao 2025c, post 4; Tao 2026i, post 2; Tao 2026e |
| models struggle to discover a refactor, though they carry one out once a person explains it; assistants close a placeholder by inventing machinery instead of following the paper's proof | Tao 2026i, post 2; PNT-plus 2026, section 13, rule 4 |
| review becomes the bottleneck: one project caps a contributor at 3 open AI-assisted pull requests; one team found cleaning AI code more trouble than rewriting it, and threw it away | PNT-plus 2026, section 13, rule 7; Avigad 2026, section The concerns |
| size defeats reading: the FLT repository makes the editor sluggish | Buzzard 2026a |
| models do not always pay: in the ETP, automated provers were cheaper and covered most of what models could do | Tao 2025d, last paragraph |
| reliance on the model: students passively accepting an autoformalizer's results; generated comments unverified; sloppy AI code discouraging learning Lean | LZ 2025b (example only, met by both sides); LZ 2026b; MathOverflow 2026, top answer |

- Claims no checker decides: statement fidelity (Q2), and whether an error a model flags in prose is an error (Q3).

## Where practice runs ahead of the evidence

- A model already judges statement fidelity in a public registry, with no published agreement rate against people.
- The formal pass should look for that rate, for any measure of guidance given to a person, and for whether the loop's checks find misformalizations that the [baseline](baseline.md) lets through.
