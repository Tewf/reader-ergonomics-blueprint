# Frame: the loop's problem and its names

Step 1 of the review on autoformalization, read on 2026-10-29: a grey pass by two reviewers, one per side of the loop, then a formal pass in three strands, merged.
It states the problem, defines each term once, maps the scope's five questions to each side's and strand's sub-questions, and links what is held elsewhere.

## The problem in one sentence

How a model turns a claim a person wrote as a topic into a Lean statement meaning what they meant, has Lean check it, and returns guidance that helps them think, not only get checked.

## Names

One row per term; every file of this folder uses these names. A source is where a side or a strand first met the term; "human side" or "strand A" means it defined the term without a source.

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
| **faithfulness** | the formal literature's name for statement fidelity; some papers say semantic consistency, semantic alignment or semantic equivalence | strand A |
| **unfaithful step** | a formal statement that experts judge not equivalent to the person's step | Guo 2026b |
| **BEq** | a check against a reference: two formal statements are each proved from the other, with a model prover | Liu 2025b |
| **BEq+** | the same check by fixed tactics, run on a CPU | Poiroux 2025 |
| **type-check rate**, compile rate | the share of a translator's outputs that Lean accepts as well formed, true or not | strand A |
| **pass@k** | the share of problems solved when k attempts are allowed | strand B |
| **misformalization** | a formal statement that does not say what the intended claim says, often proved without trouble; also a label in Formal Conjectures | Google DeepMind 2026; Alexeev 2025; a taxonomy in Firsching 2026 |
| **autoformalization** | translation of informal mathematics into a proof assistant's language by a model: of statements, of proofs, or of whole papers; research now also applies the word to any verifiable logic | Hales 2026; Wu 2022; Mensfelt 2025 |
| **quasi-autoformalization** | autoformalization in which humans step in when the model is stuck | Hales 2026 |
| **natural-language scaffolding** | the human-written informal plan a formalizing agent follows | Math Inc 2025 |
| **controlled natural language (CNL)** | a fixed fragment of a natural language, with a grammar a program parses | Naproche 2026; Massot 2026b; Kuhn 2014 |
| **declarative proof** | a proof that states each intermediate claim before justifying it, as in Isar | Isabelle 2026; Harrison 1998; Wiedijk 2012b |
| **procedural proof** | a script of commands whose proof states appear only when it runs | Harrison 1998; Wiedijk 2012b |
| **hammer** | a tool that sends a goal to automatic provers and rebuilds the proof inside the proof assistant | Blanchette 2016 |
| **suggestion** | text Lean offers after a search tactic (`exact?`, `simp?`), checked before it is shown | Lean FRO 2026d |
| **named error** | an error with a stable code and an explanation page | Lean FRO 2025 |
| **iterative refinement**, **self-correction** | a model reads Lean's errors and rewrites its proof | CMU L3 2025; Goedel-LM 2025 |
| **proof repair** | fixing a proof broken by a change, or a failed attempt, given the checker's output | Ringer 2019 |
| **programming error message**, enhanced | the diagnostic a compiler or interpreter shows; an enhanced one is rewritten for novices | Becker 2019 |
| **model audit**, AI audit; **model judge** | a model checks formal statements against their cited sources (audit), or an informal account against a challenge file (judge); in research, a model judge is asked whether a formal statement means what its informal source means | Adamczewski 2026; Palomar 2026; strand A |
| **paper matching** | the Lean statement copies the paper's statement and its citation | PNT-plus 2026 |
| **AI disclosure**, AI label | stating in a pull request that a model wrote part of it; a CI job may add a label | PNT-plus 2026; Tao 2026e |
| **vibe coding**, **vibe proving**, **vibe formalisation** | a model writes the Lean while the person does not read it | Tao 2025b; Tao 2025c; Tanswell 2026 |
| **slop** | large, unreviewed model output | LZ 2025b; Tanswell 2026 |
| **junk values** | Lean's total functions, such as x / 0 = 0, that let a statement be true for a trivial reason | Alexeev 2025; Paulson 2026 |
| **humanization** of a machine proof | rewriting a prover's output as lemmas a person can follow | LZ 2025c |
| **digestion** | turning a checked proof into an account a person understands and can explain | Tao 2026i; Tao 2026j |
| **impedance mismatch** | generation, verification and digestion out of step: proofs are now easier to produce than to check and understand | Tao 2026i |
| **de Bruijn factor** | the ratio of the length of a formal proof to its informal original; measured on both texts compressed | Scholze 2021; Wiedijk 2000 |
| **transfer** | a skill practised in a proof assistant shows in proofs written on paper | Massot 2024 |
| **quasi-experiment** | a comparison of groups not assigned at random | Otte 2026 |
| **over-reliance**, automation bias | accepting a tool's output without checking it; automation bias is the tendency to over-rely on automation | Zhai 2024; Goddard 2012 |
| **Pollack-consistency** | a prover parses back every formula it prints, so the user knows what was proved | Wiedijk 2012 |
| **proof auditing** | an independent check of a formalization against what it claims | Adams 2016 |
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

The scope's five questions, with the sub-questions each side of the grey pass answered; the last column gives the formal pass's sub-questions, whose strands are named in [protocol](protocol.md), section 4.

| Id | Scope question | Formal side | Human side | Formal pass |
|---|---|---|---|---|
| Q1 | **Prior art.** Who joins structured informal writing to a proof assistant, and what does each way ask of the writer? | F1: which projects join informal writing to Lean, by what workflow, and how many use them? F2: what do controlled natural languages and readable proof languages ask of the writer? | H1: what do practitioners who work with a person, a model and a proof assistant together report: what worked, what did not, what they changed in how they write? | strand B: controlled natural languages, declarative proof languages, blueprints and structured workflows, as research |
| Q2 | **Translation.** How faithful is a model's translation into Lean, and how is a correct proof of the wrong statement caught? | F3: what do autoformalization tools claim, what has been measured, by whom, and how is a wrong statement caught by machine? | H2: how are wrong translations caught in practice, and by whom? | strand A: A1 how faithfulness is measured; A2 how often a translation is wrong; A3 how a misformalization is detected; A4 which methods and benchmarks carry translation |
| Q3 | **Feedback.** How is a proof assistant's output turned into guidance a person can act on? | F4: how is it turned into guidance, without a model and with one? | H3: which checks of writing clarity run in CI, and how is model feedback on structured writing used? | strand B: error messages for people, with and without a model; the checker's output explained to people; the checker's output as guidance for a model |
| Q4 | **Form.** Does obliging the writer to split reasoning into small claims help the person think, or only the machine check? | handed to the human side | H4: the same question | strand C: C1 transfer to paper; C2 how people use the checker's verdict; C3 effects on research mathematicians |
| Q5 | **Limits.** Where does the loop fail: a wrong translation, reliance on the model, claims no checker can decide? | F5: where does the machine half fail? | H1, what did not work | strand C: C4 trust in the checker; C5 the gap between the informal and the formal claim; C6 over-reliance; C7 cost |

## Words the formal pass started from

- Academic names: statement autoformalization; proof autoformalization; semantic equivalence of formal statements; neural theorem proving; proof repair; premise selection; natural proof checking; declarative proof language.
- Acronyms: CNL, ATP, ITP, NTP.
- Benchmarks named in practice: MiniF2F, PutnamBench, ProverBench, FormalMATH, CombiBench, FLTEval.
- Faithfulness metrics named in practice: BEq, BEq+.

## Held elsewhere, linked, not repeated

- Structured proofs (Lamport), blueprints as explicit structure, the PFR case (Tao 2023) and mathlib's documentation style (Mathlib 2026): reader-ergonomics-academic, [mathematical-writing review](https://github.com/Tewf/reader-ergonomics-academic/blob/master/evidence/mathematical-writing/review.md), section 6.
- Prose linting and documentation as code: reader-ergonomics-topic, [document-model review](https://github.com/Tewf/reader-ergonomics-topic/blob/master/evidence/document-model/review.md), section 5.
- Structured proofs read by students (Fuller 2014), surveys of proof in education (Stylianides 2024; Lessing 2025), and of proof assistants in teaching (Tran Minh 2025): mathematical-writing review, sections 0 and 5.
- Cognitive load and expertise reversal (Kalyuga 2003): reader-ergonomics, [learning-science review](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/evidence/learning-science/review.md), section 3.
- Model help and learning (Bastani 2025): reader-ergonomics-learning, [exercise-sets review](https://github.com/Tewf/reader-ergonomics-learning/blob/master/evidence/exercise-sets/review.md), section 5.
- Self-correction of language models (Kamoi 2024): reader-ergonomics, [llm-readers review](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/evidence/llm-readers/review.md).
