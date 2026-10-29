# Frame: the loop's problem and its names

Step 1 of the grey review on autoformalization, read on 2026-10-29 by two reviewers, one per side of the loop, and merged.
It states the problem, defines each term once, maps the scope's five questions to the sides' sub-questions, and links what is held elsewhere.

## The problem in one sentence

How a model turns a claim a person wrote as a topic into a Lean statement meaning what they meant, has Lean check it, and returns guidance that helps them think, not only get checked.

## Names

One row per term; every file of this folder uses these names. A source is where a side first met the term; "human side" means that side defined it without a source.

| Term | What practice means by it | Sources |
|---|---|---|
| **Lean** | a proof assistant: a program that accepts a proof only if each step follows from the rules | human side |
| **mathlib** | Lean's library of formal mathematics; definitions in it are shared and reviewed | human side; counts in Mathlib 2026b |
| **kernel** | the small part of Lean that checks every final proof term | Hales 2026 |
| **sorry** | the Lean placeholder for a missing proof; a file with one compiles but proves nothing there | Numina 2025 |
| **axiom check** | listing the axioms a proof depends on, to catch added assumptions | Lean FRO 2026a; LZ 2025a |
| **blueprint** | a LaTeX outline of a proof in which each statement lists the labels it uses and the Lean declaration it maps to | Massot 2026 |
| **dependency graph** | the graph drawn from those `\uses` labels, coloured by formal status | Massot 2026 |
| **blueprint node** | one statement of the blueprint, tied one to one to a Lean declaration | Vergo 2026; Zhu 2026 |
| **challenge file** | a short Lean file holding only the statements claimed, meant to be read by a person: the trusted statement, kept apart from a proof supplied by anyone | Tao 2026f; Lean FRO 2026a; LZ 2025a |
| **solution module** | the Lean file holding the proofs of those statements, of any length | Tao 2026f |
| **comparator** | a program that checks the solution module proves exactly the challenge file's statements, with permitted axioms only | Lean FRO 2026a |
| **formalization.yaml** | a self-report file: sources, automation used, divergences, review status, and a table from source statements to Lean names | Mathlib Initiative 2026 |
| **statement fidelity**, human audit | whether the formal statement means what its informal source means; a human audit is a person checking it | Hales 2026 |
| **misformalization** | a formal statement that does not say what the intended claim says, often proved without trouble; also a label in Formal Conjectures | Google DeepMind 2026; Alexeev 2025 |
| **autoformalization** | translation of informal mathematics into a proof assistant's language by a model: of statements, of proofs, or of whole papers | Hales 2026 |
| **quasi-autoformalization** | autoformalization in which humans step in when the model is stuck | Hales 2026 |
| **natural-language scaffolding** | the human-written informal plan a formalizing agent follows | Math Inc 2025 |
| **controlled natural language (CNL)** | a fixed fragment of a natural language, with a grammar a program parses | Naproche 2026; Massot 2026b |
| **declarative proof** | a proof that states each intermediate claim before justifying it, as in Isar | Isabelle 2026 |
| **suggestion** | text Lean offers after a search tactic (`exact?`, `simp?`), checked before it is shown | Lean FRO 2026d |
| **named error** | an error with a stable code and an explanation page | Lean FRO 2025 |
| **iterative refinement**, **self-correction** | a model reads Lean's errors and rewrites its proof | CMU L3 2025; Goedel-LM 2025 |
| **model audit**, AI audit; **model judge** | a model checks formal statements against their cited sources (audit), or an informal account against a challenge file (judge) | Adamczewski 2026; Palomar 2026 |
| **paper matching** | the Lean statement copies the paper's statement and its citation | PNT-plus 2026 |
| **AI disclosure**, AI label | stating in a pull request that a model wrote part of it; a CI job may add a label | PNT-plus 2026; Tao 2026e |
| **vibe coding**, **vibe proving**, **vibe formalisation** | a model writes the Lean while the person does not read it | Tao 2025b; Tao 2025c; Tanswell 2026 |
| **slop** | large, unreviewed model output | LZ 2025b; Tanswell 2026 |
| **junk values** | Lean's total functions, such as x / 0 = 0, that let a statement be true for a trivial reason | Alexeev 2025; Paulson 2026 |
| **humanization** of a machine proof | rewriting a prover's output as lemmas a person can follow | LZ 2025c |
| **digestion** | turning a checked proof into an account a person understands and can explain | Tao 2026i; Tao 2026j |
| **impedance mismatch** | generation, verification and digestion out of step: proofs are now easier to produce than to check and understand | Tao 2026i |
| **de Bruijn factor** | the ratio of the length of a formal proof to its informal original | Scholze 2021 |
| **prose linting**, docs as code | programs that check writing style in CI | held by document-model; PostHog 2026 |
| **Paper Assistant Tool** | a model that reviews a paper before submission, here theory papers for STOC 2026 | Google 2025 |
| **Formal Conjectures** | Google DeepMind's repository of formal statements of open problems | Google DeepMind 2026 |
| **Palomar** | a registry of Lean verified mathematics; its minimum, as the formal side read it, is a challenge file checked by comparator and a formalization.yaml | Tao 2026f; Palomar 2026 |
| **PNT+**, **IEANTN** | the PrimeNumberTheoremAnd project, and the integrated explicit analytic number theory network that runs in it | PNT-plus 2026; Tao 2026e |
| **ETP** | the Equational Theories Project | Tao 2024; Tao 2025d |
| **Erdős problems database** | the database and wiki of Erdős problems, with their formal and AI status | Erdős DB 2026; Erdős-wiki 2026 |

Acronyms: **ATP** automated theorem prover; **ITP** interactive theorem prover; **NTP** neural theorem proving; **CI** continuous integration. Also **LSP** language server protocol; **MCP** model context protocol, a way to give a model tools; **FRO** focused research organization (the Lean FRO maintains Lean).

Products named by practitioners and not reviewed: AlphaProof (Google DeepMind), ChatGPT and Codex (OpenAI), Anthropic's coding agent, GitHub Copilot, canonical, SafeVerify and lean4checker (checkers). The provers and translators reviewed are in [review](review.md), Q2.

## Questions

The scope's five questions, with the sub-questions each side answered.

| Id | Scope question | Formal side | Human side |
|---|---|---|---|
| Q1 | **Prior art.** Who joins structured informal writing to a proof assistant, and what does each way ask of the writer? | F1: which projects join informal writing to Lean, by what workflow, and how many use them? F2: what do controlled natural languages and readable proof languages ask of the writer? | H1: what do practitioners who work with a person, a model and a proof assistant together report: what worked, what did not, what they changed in how they write? |
| Q2 | **Translation.** How faithful is a model's translation into Lean, and how is a correct proof of the wrong statement caught? | F3: what do autoformalization tools claim, what has been measured, by whom, and how is a wrong statement caught by machine? | H2: how are wrong translations caught in practice, and by whom? |
| Q3 | **Feedback.** How is a proof assistant's output turned into guidance a person can act on? | F4: how is it turned into guidance, without a model and with one? | H3: which checks of writing clarity run in CI, and how is model feedback on structured writing used? |
| Q4 | **Form.** Does obliging the writer to split reasoning into small claims help the person think, or only the machine check? | handed to the human side | H4: the same question |
| Q5 | **Limits.** Where does the loop fail: a wrong translation, reliance on the model, claims no checker can decide? | F5: where does the machine half fail? | H1, what did not work |

## Words for the formal pass

- Academic names: statement autoformalization; proof autoformalization; semantic equivalence of formal statements; neural theorem proving; proof repair; premise selection; natural proof checking; declarative proof language.
- Acronyms: CNL, ATP, ITP, NTP.
- Benchmarks named in practice: MiniF2F, PutnamBench, ProverBench, FormalMATH, CombiBench, FLTEval.
- Faithfulness metrics named in practice: BEq, BEq+.

## Held elsewhere, linked, not repeated

- Structured proofs (Lamport), blueprints as explicit structure, the PFR case (Tao 2023) and mathlib's documentation style (Mathlib 2026): reader-ergonomics-academic, [mathematical-writing review](https://github.com/Tewf/reader-ergonomics-academic/blob/master/evidence/mathematical-writing/review.md), section 6.
- Prose linting and documentation as code: reader-ergonomics-topic, [document-model review](https://github.com/Tewf/reader-ergonomics-topic/blob/master/evidence/document-model/review.md), section 5.
