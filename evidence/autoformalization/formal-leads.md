# Formal leads met in the grey pass

Papers, benchmarks and authors met by both sides on 2026-10-29 while reading grey sources, one line per work, for the formal pass, grouped by the questions of [frame](frame.md).

- None was opened or reviewed; identifiers are as the search engine or the citing page showed them, and must be checked before use.
- Each lead says where it was met: the grey key or search string, prefixed by its side when it matters.

## Q1. Prior art: blueprints, collaboration, readable proof languages

- The Equational Theories Project: advancing collaborative mathematical research at scale. arXiv 2512.07087; met by both sides (human: W6, Tao 2025d).
- LeanArchitect: automating blueprint generation for humans and AI. arXiv 2601.22554.
- KnowTeX: visualizing mathematical dependencies. arXiv 2601.15294.
- Lean Atlas: an integrated proof environment for human-AI collaborative formalization. arXiv 2604.16347.
- Astrolabe: a content-addressable hypergraph for semantic knowledge management. arXiv 2604.10435.
- Prove2Me: an open collaborative platform for scaling math formalization (Chen, Marwaha, Lu, Yuen, Peng). arXiv 2608.28433, cited by Anthropic 2026c.
- From lecture notes to Lean: formalizing a textbook on probability theory. arXiv 2607.27298.
- A paper in ITP (2026), LIPIcs volume 382, paper 25, on blueprints (title not seen). doi 10.4230/LIPIcs.ITP.2026.25.
- Urban (2026), 130k lines of formal topology in two weeks, arXiv id not read; named in Hales 2026, met by both sides.
- ATLAS, a Meta project autoformalizing parts of 26 textbooks, 2026, not read; named in Hales 2026, met by both sides.
- Bloom and Mehta (2022), the formalization of Bloom's unit fractions result (Erdős 47); met in Alexeev 2025.
- Yang et al. (2023), LeanDojo; met in Tao 2023m.
- Lean Copilot: large language models as copilots for theorem proving in Lean (Song et al.). arXiv 2404.12534; met by both sides (human: W1).
- Kinyon (2019), a method of proof simplification for automated provers. arXiv 1808.04251; met in LZ 2025c.
- A Vampire to Dedukti proof export. arXiv 2503.15541; met in LZ 2025c.
- Kondylidou, Heule and Blanchette (2026), a minimizer of equational proofs, paper not identified; met in LZ 2025c.
- Proof assistants for teaching: a survey. arXiv 2505.13472. The one existing survey the formal side met.
- Teaching mathematics using Lean and controlled natural language (Massot). ITP (2024), doi 10.4230/LIPIcs.ITP.2024.27; met by both sides (human: Massot 2026b).
- Waterproof: educational software for learning how to write mathematical proofs. arXiv 2211.13513.
- Waterproof Editor: an educational environment for proof assistants and programming languages. arXiv 2606.01875.
- The educational proof assistant Waterproof in an introductory proof course. arXiv 2606.26809.
- Natural language proof checking in introduction to proof classes: first experiences with Diproche (Carl, Lorenzen, Schmitz). arXiv 2202.08131.
- Number theory and axiomatic geometry in the Diproche system. arXiv 2006.01794.
- Automatized evaluation of formalization exercises in mathematics. arXiv 2006.01800.
- Using automated theorem provers for mistake diagnosis in the didactics of mathematics (Carl). arXiv 2002.05083.
- Naproche: Koepke's preprints The Naproche system and Premise selection in the Naproche system; Cramer's (2013) Bonn dissertation; a CADE-28 chapter, doi 10.1007/978-3-030-79876-5_36.
- Lurch: a word processor that can grade students' proofs; From formal to expository (Carter, Monks).
- Structured proofs in Isar/HOL (Nipkow, TYPES (2002)); Isabelle/Isar, a generic framework (Wenzel).
- ProofAug: neural theorem proving via fine-grained proof structure analysis. arXiv 2501.18310.

## Q2. Translation: autoformalization, provers, faithfulness, misformalization

- Formal Conjectures: an open and evolving benchmark for verified discovery in mathematics (Firsching and others, 2026). arXiv 2605.13171; met by both sides (human: W2, W4, Google DeepMind (2026)).
- Faults in our formal benchmarking: dataset defects and evaluation failures in Lean theorem proving. arXiv 2606.29493; met in W4.
- OEIS Open: how many conjectures can language models turn into theorems? arXiv 2608.11941; met by both sides. The human side (W4) names Adamczewski as its author; it is a work apart from the audit repository Adamczewski 2026.
- LeanMarathon: toward reliable AI co-mathematicians through long-horizon Lean autoformalization. arXiv 2606.05400; met by both sides (human: W2).
- Alexeev and Mixon 2025, Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof. arXiv 2510.19804 (Erdős 707); met in W2, Alexeev 2025.
- Resolution of Erdős problem 728: a writeup of Aristotle's Lean proof. arXiv 2601.07421, authors not read; met in W2, Tao 2026k.
- arXiv 2601.22401, a report of an AI agent on Erdős problems, title not read; met in W2.
- AlphaProof paper, Google DeepMind, venue not read; met in Alexeev 2025.
- Aristotle: IMO-level automated theorem proving. arXiv 2510.01346.
- Using the Aristotle API for AI-assisted theorem proving in Lean 4: the Grasshopper problem. arXiv 2605.20120.
- Global product intersection sets in semigroups, met in a search on Aristotle. arXiv 2604.18869.
- Optimal bounds for an Erdős problem on matching integers to distinct multiples. arXiv 2603.28636.
- Beyond compilation: evaluating faithful natural-language-to-Lean statement formalization. arXiv 2606.31002.
- Evaluating the robustness of proof autoformalization in Lean 4. arXiv 2606.14867.
- Reliable evaluation and benchmarks for statement autoformalization (BEq+), named in PASE 2026; BEq, code at Purewhite2019/rethinking_autoformalization.
- PutnamBench (Tsoukalas and others), a benchmark whose solutions are checked with SafeVerify; met in LZ 2025a.
- StepFun-Formalizer. arXiv 2508.04440.
- Kimina-Prover. arXiv 2504.11354.
- Goedel-Prover-V2. arXiv 2508.03613.
- BFS-Prover-V2, arXiv 2509.06493; BFS-Prover, arXiv 2502.03438.
- DeepSeek-Prover-V2, technical report linked from its model card; its output once exploited a way to skip adding a theorem (human: LZ 2025a). The first DeepSeek-Prover paper is named in PASE 2026 for negation and inconsistency filters.
- DeepSeekMath-V2, named in PASE 2026 for training a model judge.
- Herald: a natural language annotated Lean 4 dataset. arXiv 2410.10878.
- ProofBridge: autoformalization of natural language proofs via joint embeddings. arXiv 2510.15681.
- Process-driven autoformalization in Lean 4 (FormL4). arXiv 2406.01940.
- MathAdv: what theorem provers know, reason, formalize and generalize. arXiv 2608.25449.
- LEAP: agentic frameworks for formal mathematics. arXiv 2606.03303.
- LeanFlow: workflow-driven Lean autoformalization. arXiv 2607.20503.
- Numina-Lean-Agent. arXiv 2601.14027.
- MathCoPilot: human-AI symbiotic mathematical research. arXiv 2607.14582.
- Long-horizon autoformalization of a core theorem underlying MIP* = RE. arXiv 2609.19814.
- Multi-agent autoformalization of tensor network theory. arXiv 2607.07857.
- Formalization of Landau damping in the Vlasov-Poisson equations in Lean. arXiv 2609.16801.

## Q3. Feedback: error messages, guidance, model feedback on writing

- Debugging without error messages. arXiv 2501.05706.
- Two papers on model explanations of compiler errors for novices, titles not seen: arXiv 2308.11873 and arXiv 2409.18661 (the engine's summary gave 2,565 students for one and 106 participants for the other, unchecked).
- Natural language translation of formal proofs through informalization of proof steps and recursive summarization (Hattori, Matsuzaki, Fujiwara), INLG (2025). arXiv 2509.09726.
- Towards automating scientific review with Google's Paper Assistant Tool. arXiv 2606.28277; met in W7.
- Can AI review improve paper drafting? An empirical study on 20 computer architecture submissions. arXiv 2606.01013; met in W7.

## Q4. Form: teaching, thinking and understanding

- Thoma and Iannone (2022), Learning about proof with the theorem prover LEAN: the abundant numbers task; met in LZ 2025f.
- Teaching mathematics with Lean: interactive theorem provers in the classroom, authors not read; met in LZ 2025f.
- Klowden and Tao (2026), Mathematical methods and human thought in the age of AI, arXiv id not read; met in P2 (human).
- An essay on AI and formalization by Avigad, 2026, title not read; met in P2 (human). Whether it is the Xena guest post Avigad 2026 was not checked.
- Commelin, Jamnik, Ochigame, Taelman and Venkatesh (2026), a paper on AI in mathematics, title not read; met in P2 (human).
- Alper (2026), Embracing AI and formalization, an essay, not read; met in W9.
- AI for mathematics: a survey, authors not read; met in Kirov 2026b.
- Thurston (1994) and Jaffe and Quinn (1993), on proof and understanding; met in Buzzard 2026c (Thurston (1994) is held by mathematical-writing).

## Q5. Limits: foundations and trust

- Carneiro (2019), the type theory of Lean, MS thesis; named in Hales 2026.
- arXiv 2607.13662 and arXiv 2403.14064, on Lean's metatheory; named in Hales 2026.
- Werner (1997), Sets in types, types in sets; met in Hales 2026.
- Wiedijk (editor), The seventeen provers of the world; met in Hales 2026.
- Hartnett (2026), The proof in the code, a book on the history of Lean, not read; met in Hales 2026.

## Benchmarks named in practice

MiniF2F, PutnamBench, ProverBench, FormalMATH-Lite, CombiBench, FLTEval, VERINA, MathOlympiadBench, the Annals set on lean-eval.

## Authors to search by name

- Patrick Massot, Dan Velleman, Siddhartha Gadgil, Heather Macbeth: proof writing taught with Lean (human side, LZ 2025f).
- Jason Rute, Joseph Myers, Mario Carneiro: protocols for checking a proof against a trusted statement (human side, LZ 2025a, LZ 2025e).
- Boris Alexeev, Thomas Bloom: misformalization in the Erdős problems (human side, Alexeev 2025).
- Tom Adamczewski: model audits of formal statements (human side, Adamczewski 2026).
- Named by the formal side, with no reason given. The authors are Patrick Massot; Kevin Buzzard; Terence Tao; Jeremy Avigad; Thomas Hales; Jason Rute; Josef Urban; Peter Koepke; Marcos Cramer; Merlin Carl; Makarius Wenzel; Tobias Nipkow; Jim Portegies; Siddhartha Gadgil; Tianyi Peng; Mario Carneiro.
