# Protocol: how the merged grey pool was built

Every search, count and rule of both sides of the grey pass, run on 2026-10-29, one reviewer per side, then merged.
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

The scope's five questions, Q1 to Q5 of [frame](frame.md): prior art, translation, feedback, form, limits. The frame maps each side's sub-questions (F1 to F5, H1 to H4) onto them.

## 3. Existing reviews

- Neither side found a grey review of the whole loop.
- Formal side: two grey overviews of practice were found and used, Hales 2026 and Avigad 2026. One practitioner answer catalogues the checks for a wrong statement, PASE 2026. One formal survey was met and listed, on proof assistants for teaching.
- Human side: two formal surveys were met by citation and listed in [formal leads](formal-leads.md), not read.
- Held by the family, linked and not repeated: structured proofs and blueprints (reader-ergonomics-academic, mathematical-writing); prose linting and docs as code (reader-ergonomics-topic, document-model).

## 4. Formal search

Not run in this pass. Papers met by both sides are listed in [formal leads](formal-leads.md), not reviewed.

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

## 8. Selection

- Formal side, include: a source on joining informal mathematical writing to a proof assistant, on translating it, on checking the translation, or on turning a checker's output into guidance. Include also a company's account of its own prover, labelled as its owner's claim.
- Formal side, exclude: papers (listed as leads); news coverage of a primary page that was itself readable; opinion threads with no practice or data; duplicates.
- Human side, include any of: a report of practice where a person works with a model or a proof assistant on reasoning a person wrote; a wrong formal statement caught, and how. Also a check of writing in CI with a model in it, or a report on whether splitting reasoning helped thinking.
- Human side: English, dated or datable, readable without login on the search date.
- Human side, exclude: news rewrites, mirrors and aggregators (about 25 links: secondary); product pages on prover capability (to the formal side); formal papers (to the leads); Vale-in-CI pages already held by document-model (3).
- Both: a page that could not be read is reported in section 11 and never used.

## 9. Quality of grey sources

- The 20 criteria and the threshold: [evidence README](../README.md#method).
- A count read from a public listing (stars, downloads, registry totals) is the reviewer's measurement, not a source, and is not scored.
- Formal side, outlet tier: project documentation, company pages, model cards, forum and Q/A pages, tier 2 (0.5); blogs and gists, tier 3 (0); no tier 1 source was found.
- Formal side: a company page scores low on objectivity, as it reports its own success. Q/A authority is 0.5 for the site, plus 1 for an answerer at or above 20,000 reputation, 0.5 at or above 5,000.
- Human side, outlet tier: project documentation, Q/A, company and organiser pages, talk abstracts, tier 2 (0.5); blogs, microblog posts and chat threads, tier 3 (0).
- Human side: A1 is 0 for a personal blog, 0.5 for a moderated forum or site, 1 for an institution; a company page about its own tool scores 0 on O3 (vested interest).
- Human side, impact 1 or 0.5: blogs, 30 comments or 10; Mathstodon, 50 favourites or 10; repositories, 500 stars or 100. Chat threads, 50 messages or 15; Q/A, the shared rule, 30 votes or 10.

## 10. Extraction, synthesis and merge

- Extracted per source by both sides: producer, date, the practice, the claim, any number with where it sits in the source, and whether the number is the source's own.
- Each side wrote its synthesis by its own sub-questions; the merge reorders every finding by Q1 to Q5 in [review](review.md), each with its key and where.
- Keys: one key per work across both sides. Where the sides used different keys for one work, or one key for two works, the formal side's key is kept. That side had already checked its keys against the five bibliographies of the family.
- Keys were then checked by script against the bibliographies of reader-ergonomics-topic (branch and master), reader-ergonomics, reader-ergonomics-academic, reader-ergonomics-presentations and reader-ergonomics-software-design. A key used there for another work took the next free letter; a work already there kept its key. The renamed keys are listed in [sources](sources.md).
- Scores: a source scored by both sides keeps the score of the side that read more of it. That is judged first by the pages read, then by the parts of the source each side cites; the other side's score is given in its row.

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
