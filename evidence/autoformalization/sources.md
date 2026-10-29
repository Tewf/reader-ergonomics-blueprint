# Sources: the merged pool, its flow and its scores

The pool of both sides of the grey pass, read on 2026-10-29: the flow from results to sources, then each source with its score, the counts, and the keys renamed at the merge.
Searches are in [protocol](protocol.md); terms in [frame](frame.md). Below 10 of 20, a source is an example of practice only, never support for a claim.

## Flow

| Stage | Formal side | Human side | Total |
|---|---|---|---|
| Web strings run | 24 | 9 | 33 |
| Web results seen and screened by title | 323 | 180 | 503 |
| Q/A strings run | 22 | 10 | 32 |
| Q/A threads returned and screened | 134 | 72 | 206 |
| All strings | 46 | 19 | 65 |
| All string results seen and screened | 457 | 252 | 709 |
| Producers visited | 11 | 6 (P1 to P6) | 17 visits; Tao's blog, the Xena blog, the forum archive and GitHub were visited by both |
| Producer listings scanned | forum archive: 24,928 titles filtered, 126 matched | blogs: 60 and 83 titles; microblog: 1,000 statuses, 32 matched; forum: 117 titles matched; 11 repositories; 2 indexes | not summed: different units |
| Opened and read | about 40 producer pages; 4 forum threads; 5 Q/A threads | 62, and 2 failed | not summed: the formal count is approximate |
| Included and scored | 43: web 19, visits 20, Q/A 4 | 43: web 4, visits 38, Q/A 1 | 86 rows; 80 sources, 6 of them scored by both |
| Below 10, examples only | 3 | 6 | 9 |
| Counts read, not scored | 4 | 3 | 7 |
| Read, not scored | 1 forum thread, passed to the human side | none | 1 (LZ 2026b) |

- Formal side, excluded after reading: 2 forum threads (opinion, no practice) and 1 forum thread passed to the human side (LZ 2026b). Also 1 Q/A thread with no answer, and 1 blog post with no loop content (a Lean companion to a textbook).
- Formal side, excluded by title: papers (to [formal leads](formal-leads.md)), news coverage of readable primary pages, duplicates; not reachable: the Isar reference manual and the Isabelle programming tutorial (server timeout).
- Human side, excluded after reading: off the loop, 8 pages (such as essays on the value of mathematics with no workflow in them), and one foundations thread. Failed: the audit site and one forum topic.
- Human side, excluded by title: news rewrites, mirrors and aggregators (about 25); Vale-in-CI pages held by document-model (3). It passed 34 formal leads on, merged in [formal leads](formal-leads.md).

## Grey sources, scored

Subtotals A to T are the eight groups of criteria, in the order of [protocol](protocol.md), section 9, which also holds each side's scoring rules. Route codes are each side's own, in its section of the protocol.
A source scored by both sides keeps the score of the side that read more of it, and gives the other side's in its row.

| Key | Tier, kind | Side and route | Score (A / M / O / D / P / N / I / T) | Used in |
|---|---|---|---|---|
| Adamczewski 2026 | 2, project documentation and run data | human: P5; W4 | 15 (2.5 / 5.5 / 3 / 1 / 0.5 / 2 / 0 / 0.5) | frame; protocol; review Q2; review Q3; baseline |
| Alexeev 2025 | 3, guest blog post | human: P1; W2 | 15 (2.5 / 5.5 / 3 / 1 / 1 / 2 / 0 / 0) | frame; protocol; review Q1; review Q2 |
| Anthropic 2026c | 2, company research page | formal: G9 | 13.5 (3 / 3.5 / 1.5 / 1 / 1 / 2 / 1 / 0.5) | protocol; review Q1; review Q2 |
| Avigad 2026 | 3, guest blog post | formal: P | 15.5 (4 / 3.5 / 3 / 1 / 1 / 2 / 1 / 0) | protocol; review Q1; review Q2; review Q3; review Q5 |
| Axiom 2026 | 2, company research page | formal: G21 | 11.5 (2.5 / 3 / 1.5 / 1 / 0.5 / 1.5 / 1 / 0.5) | protocol; review Q2; review Q4 |
| Buzzard 2024 | 3, blog | human: P1 | 15.5 (3 / 5 / 3.5 / 1 / 1 / 1.5 / 0.5 / 0) | review Q2; review Q4 |
| Buzzard 2025 | 3, blog | human: P1 | 12.5 (3 / 4 / 2 / 1 / 1 / 1.5 / 0 / 0) | review Q2; baseline |
| Buzzard 2026a | 3, blog | both; formal: P; human: P1 | 16.5 (3 / 5.5 / 3.5 / 1 / 0.5 / 2 / 1 / 0), human side, kept: both read the post; the human side cites two of its sections (The code base, What this work is), the formal side one; formal side 16 (4 / 3.5 / 3.5 / 1 / 1 / 2 / 1 / 0) | protocol; review Q2; review Q5 |
| Buzzard 2026b | 3, blog | formal: P | 15 (4 / 4 / 3 / 1 / 0.5 / 2 / 0.5 / 0) | protocol; review Q1; review Q2; review Q5 |
| Buzzard 2026c | 3, blog | human: P1 | 13.5 (3 / 3.5 / 3 / 1 / 1 / 1 / 1 / 0) | review Q4 |
| Buzzard 2026d | 3, blog | human: P1 | 15 (3 / 4.5 / 2.5 / 1 / 1 / 2 / 1 / 0) | review Q2 |
| CMU L3 2025 | 2, repository README | formal: P | 12.5 (3.5 / 2.5 / 2.5 / 1 / 0.5 / 1.5 / 0.5 / 0.5) | frame; protocol; review Q3 |
| DeepSeek 2025 | 2, model card | formal: P | 12 (3 / 3.5 / 1.5 / 0.5 / 1 / 1 / 1 / 0.5) | protocol; review Q2 |
| Dressler 2026 | 2, repository README | formal: G18 | 10.5 (1.5 / 2.5 / 2.5 / 0.5 / 0.5 / 1.5 / 1 / 0.5) | protocol; review Q3 |
| Erdős DB 2026 | 2, project documentation | human: P5; W5 | 16 (3 / 4.5 / 3.5 / 1 / 1 / 1.5 / 1 / 0.5) | frame; protocol; review Q1; review Q4 |
| Erdős-wiki 2026 | 2, project wiki | human: P5 | 16 (2.5 / 5 / 3.5 / 1 / 1 / 1.5 / 1 / 0.5) | frame; review Q2 |
| Gadgil 2026 | 2, repository README | formal: P | 11.5 (3 / 2.5 / 2.5 / 0.5 / 0.5 / 1.5 / 0.5 / 0.5) | protocol; review Q2 |
| GasStationManager 2026 | 2, repository README | formal: P | 11 (1.5 / 3 / 2.5 / 0.5 / 1 / 1.5 / 0.5 / 0.5) | protocol; review Q3 |
| Goedel-LM 2025 | 2, model card | formal: P | 12 (3 / 3.5 / 2 / 0.5 / 1 / 1 / 0.5 / 0.5) | frame; protocol; review Q2; review Q3 |
| Google 2025 | 2, company blog about its own tool | human: W7 | 12.5 (3.5 / 3.5 / 1.5 / 1 / 0.5 / 1.5 / 0.5 / 0.5) | frame; protocol; review Q3 |
| Google DeepMind 2026 | 2, project documentation | both; formal: G19; human: P5; W2 | 14.5 (3.5 / 3.5 / 3 / 0.5 / 1 / 1.5 / 1 / 0.5), formal side, kept: the formal side read the README and the contributing guide, the human side the README; human side 14 (3.5 / 4 / 2.5 / 0 / 1 / 1.5 / 1 / 0.5) | frame; protocol; review Q1; review Q2 |
| Hales 2026 | 3, guest blog post | both; formal: P, tag pages; human: P2 | 15 (4 / 3.5 / 3 / 1 / 1 / 1.5 / 1 / 0), formal side, kept: the formal side cites three of its sections, the human side one; human side 16 (3 / 5 / 3.5 / 1 / 1 / 1.5 / 1 / 0) | frame; protocol; review Q2; review Q5; baseline |
| Harmonic 2024 | 2, company news page | formal: G10 | 12 (2.5 / 3 / 1.5 / 1 / 1 / 1.5 / 1 / 0.5) | protocol; review Q2 |
| Isabelle 2026 | 2, project site | formal: P | 11.5 (4 / 2 / 2.5 / 0 / 0.5 / 1 / 1 / 0.5) | frame; protocol; review Q1 |
| Kirov 2026a | 3, blog | human: P6, from Tao's Mathstodon | 13 (1 / 5.5 / 3 / 1 / 1 / 1.5 / 0 / 0) | review Q1; review Q4 |
| Kirov 2026b | 3, blog | human: P6 | 13.5 (1 / 5.5 / 3 / 1 / 1 / 2 / 0 / 0) | review Q1 |
| Lean-community 2026 | 2, tool documentation | formal: P | 12 (3 / 3 / 3 / 0 / 0.5 / 1 / 1 / 0.5) | protocol; review Q3 |
| Lean FRO 2025 | 2, release notes | formal: G4 | 14.5 (4 / 3 / 3.5 / 1 / 0.5 / 1.5 / 0.5 / 0.5) | frame; protocol; review Q3; baseline |
| Lean FRO 2026a | 2, tool documentation | both; formal: P, link in Tao 2026f; human: P5; LZ 2025a | 14 (3.5 / 4.5 / 3 / 0 / 0.5 / 1.5 / 0.5 / 0.5), human side, kept: both read the README; the human side cites two of its sections (Deprecation, Definition Holes), the formal side one; formal side 17 (4 / 5 / 3.5 / 0.5 / 0.5 / 2 / 1 / 0.5) | frame; protocol; review answer; review Q1; review Q2; baseline |
| Lean FRO 2026b | 2, release notes | formal: P | 15 (4 / 3.5 / 3.5 / 1 / 0.5 / 1.5 / 0.5 / 0.5) | protocol; review Q1 |
| Lean FRO 2026c | 2, language reference | formal: G4 | 15 (4 / 4 / 3.5 / 0.5 / 0.5 / 1.5 / 0.5 / 0.5) | protocol; review Q3 |
| Lean FRO 2026d | 2, language reference | formal: G15 | 14 (4 / 3 / 3.5 / 0.5 / 0.5 / 1 / 1 / 0.5) | frame; protocol; review Q3; baseline |
| LeanDojo 2026 | 2, repository README | formal: G7 | 12.5 (3.5 / 2.5 / 2.5 / 0.5 / 1 / 1 / 1 / 0.5) | protocol; review Q3 |
| Lurch 2026 | 2, project site | formal: G17 | 6.5 (2 / 1 / 2 / 0 / 0 / 1 / 0 / 0.5) | protocol; review Q1 (example only) |
| LZ 2025a | 3, forum thread | human: P4 | 15 (3 / 4.5 / 3.5 / 1 / 1 / 1.5 / 0.5 / 0) | frame; review Q2 |
| LZ 2025b | 3, forum thread | human: P4; also met by the formal side, not scored | 9.5 (2.5 / 2 / 2 / 1 / 0.5 / 0.5 / 1 / 0) | frame; review Q5 (example only) |
| LZ 2025c | 3, forum thread | human: P4 | 14.5 (3 / 4 / 3.5 / 1 / 1 / 1.5 / 0.5 / 0) | frame; review Q4 |
| LZ 2025d | 3, forum thread | human: P4 | 9.5 (1.5 / 3 / 2 / 1 / 0.5 / 1 / 0.5 / 0) | protocol; review Q1 (example only) |
| LZ 2025e | 3, forum thread | human: P4 | 13.5 (2.5 / 4 / 3.5 / 1 / 1 / 1.5 / 0 / 0) | review Q2 |
| LZ 2025f | 3, forum thread | human: P4 | 13.5 (3 / 3.5 / 3 / 1 / 1 / 1 / 1 / 0) | review Q1; review Q3; review Q4 |
| LZ 2025g | 3, forum thread | human: P4 | 6.5 (1 / 2 / 1.5 / 1 / 0 / 0.5 / 0.5 / 0) | protocol; review Q2 (example only) |
| LZ 2025h | 3, forum thread | human: P4 | 7 (1.5 / 1 / 2 / 1 / 1 / 0.5 / 0 / 0) | protocol; review Q3 (example only) |
| LZ 2026a | 3, forum thread | human: P4 | 14 (3 / 4 / 3 / 1 / 1 / 1.5 / 0.5 / 0) | review Q1; review Q2 |
| Massot 2026 | 2, carried, repository | both; formal: P, re-read; human: linked | 13.5 there (3.5 / 3.5 / 3 / 0.5 / 0.5 / 1 / 1 / 0.5), carried by the formal side; the human side links it, not rescored | frame; protocol; review Q1; baseline |
| Massot 2026b | 2, tool documentation | both; formal: G5; human: P5 | 15.5 (4 / 3.5 / 3 / 0.5 / 1 / 2 / 1 / 0.5), formal side, kept: the formal side read the README, examples and configuration guide, the human side the README; human side 10 (3 / 2.5 / 2 / 0 / 0.5 / 1 / 0.5 / 0.5) | frame; protocol; review Q1; review Q3 |
| Math Inc 2025 | 2, company page | formal: G14 | 10.5 (2.5 / 2.5 / 1 / 0.5 / 0.5 / 2 / 1 / 0.5) | frame; protocol; review Q1; review Q2 |
| Mathlib Initiative 2026 | 2, README and template of a standard | formal: P, link in Tao 2026f | 15 (3.5 / 4 / 3.5 / 0 / 1 / 2 / 0.5 / 0.5) | frame; protocol; review answer; review Q1; baseline |
| MathOverflow 2026 | 2, Q/A thread | formal: Q/A `q=Lean formalization AI` | 13 (1.5 / 3.5 / 3 / 1 / 1 / 1.5 / 1 / 0.5) | protocol; review Q1; review Q5; baseline |
| Mistral 2026 | 2, company news page | formal: G20 | 11 (2.5 / 3 / 1 / 1 / 0.5 / 1.5 / 1 / 0.5) | protocol; review Q2; review Q3 |
| Naproche 2026 | 2, project site and tutorial | formal: P | 13.5 (3.5 / 3.5 / 3 / 0.5 / 0.5 / 1.5 / 0.5 / 0.5) | frame; protocol; review Q1; review Q3 |
| Numina 2025 | 2, model card | formal: G2 | 7.5 (2.5 / 1 / 2 / 0 / 0 / 1 / 0.5 / 0.5) | frame; protocol; review Q2 (example only) |
| Palomar 2026 | 2, registry pages | formal: P | 16 (3.5 / 5 / 3 / 0.5 / 1 / 2 / 0.5 / 0.5) | frame; protocol; review Q1; review Q2; review Q5; baseline |
| PASE 2022 | 2, Q/A thread | formal: Q/A `q=Isar readable` | 11 (0.5 / 3.5 / 3 / 1 / 0.5 / 1.5 / 0.5 / 0.5) | protocol; review Q1 |
| PASE 2022b | 2, Q/A thread | human: P7 `title=formalization` | 11.5 (0.5 / 4 / 3 / 1 / 1 / 1 / 0.5 / 0.5) | review Q4 |
| PASE 2024 | 2, Q/A thread | formal: Q/A `q=blueprint` | 11 (0.5 / 3.5 / 3 / 1 / 1 / 1 / 0.5 / 0.5) | protocol; review Q1 |
| PASE 2026 | 2, Q/A thread | formal: Q/A `q=autoformalization` | 12.5 (1 / 4.5 / 2.5 / 1 / 1 / 2 / 0 / 0.5) | protocol; review Q2 |
| Paulson 2026 | 3, blog | human: P6, from Kirov's blog | 13.5 (3 / 4 / 3.5 / 1 / 1 / 1 / 0 / 0) | frame; review Q1; review Q2; baseline |
| PNT-plus 2026 | 2, project documentation | human: P5 | 16 (3 / 5 / 3.5 / 0.5 / 1 / 2 / 0.5 / 0.5) | frame; review Q1; review Q3; review Q5; baseline |
| PostHog 2026 | 2, company handbook | human: W8 | 9 (2 / 3 / 2 / 0 / 0.5 / 1 / 0 / 0.5) | frame; protocol; review Q3 (example only) |
| Rivin 2026 | 3, gist | formal: G10 | 9 (1.5 / 3 / 1.5 / 1 / 0.5 / 1.5 / 0 / 0) | protocol; review Q2 (example only) |
| Scholze 2021 | 3, guest blog post | human: P1 | 16.5 (3 / 5 / 4 / 1 / 1 / 2 / 0.5 / 0) | frame; review Q4 |
| StepFun 2025 | 2, model card | formal: G2 | 10.5 (2.5 / 2.5 / 2 / 0.5 / 1 / 1 / 0.5 / 0.5) | protocol; review Q2 |
| STOC 2026 | 2, organisers' page | human: W7; LZ 2025h | 11 (3 / 3 / 2.5 / 0.5 / 0 / 1 / 0.5 / 0.5) | frame; protocol; review Q3 |
| Tanswell 2026 | 2, talk abstract | human: W9 | 9 (2.5 / 1.5 / 2 / 1 / 0.5 / 1 / 0 / 0.5) | frame; protocol; review Q2 (example only) |
| Tao 2023m | 3, microblog thread | human: P3 | 15.5 (3 / 4.5 / 3.5 / 1 / 1 / 1.5 / 1 / 0) | review Q3; review Q4 |
| Tao 2024 | 3, blog | formal: G8b | 15.5 (4 / 4 / 3 / 1 / 1 / 1.5 / 1 / 0) | frame; protocol; review Q1 |
| Tao 2025a | 3, microblog post | human: P3 | 14 (3 / 3.5 / 3.5 / 1 / 1 / 1 / 1 / 0) | review Q4 |
| Tao 2025b | 3, microblog thread | human: P3 | 15 (3 / 4 / 3.5 / 1 / 1 / 1.5 / 1 / 0) | frame; review Q1; review Q2 |
| Tao 2025c | 3, microblog thread | human: P3 | 14 (3 / 4.5 / 3.5 / 1 / 0.5 / 1 / 0.5 / 0) | frame; review Q1; review Q5 |
| Tao 2025d | 3, blog | human: P2 | 15 (3 / 5 / 3.5 / 1 / 1 / 1 / 0.5 / 0) | frame; review Q1; review Q5 |
| Tao 2026e | 3, blog | both; formal: P, tag pages; human: P2 | 16 (4 / 4.5 / 3.5 / 1 / 1 / 1.5 / 0.5 / 0), formal side, kept: the formal side names the paragraph on AI use and the task sizes; the human side names no part; human side 14 (3 / 4.5 / 3.5 / 1 / 1 / 1 / 0 / 0) | frame; protocol; review Q1; review Q2; review Q3; review Q5; baseline |
| Tao 2026f | 3, blog | formal: P, tag pages | 15.5 (4 / 4 / 3 / 1 / 1 / 2 / 0.5 / 0) | frame; protocol; review answer |
| Tao 2026g | 3, microblog post | human: P3 | 11.5 (3 / 3 / 3 / 1 / 0 / 1 / 0.5 / 0) | review Q3 |
| Tao 2026h | 3, microblog post | human: P3 | 11 (3 / 2.5 / 3 / 1 / 0.5 / 0.5 / 0.5 / 0) | review Q1 |
| Tao 2026i | 3, microblog thread | human: P3 | 14.5 (3 / 4 / 3.5 / 1 / 1 / 1.5 / 0.5 / 0) | frame; review Q1; review Q5 |
| Tao 2026j | 3, blog | human: P2 | 14 (3 / 3.5 / 3.5 / 1 / 1 / 1 / 1 / 0) | frame; review Q4 |
| Tao 2026k | 3, microblog thread | human: P3 | 14.5 (3 / 4 / 3.5 / 1 / 1 / 1.5 / 0.5 / 0) | review Q2; review Q3 |
| TUe 2026 | 2, university project page | formal: G13 | 12 (3 / 3.5 / 3.5 / 0 / 0.5 / 1 / 0 / 0.5) | protocol; review Q1; review Q3 |
| Vergo 2026 | 2, forum thread | formal: P, forum archive | 11 (1.5 / 2.5 / 3 / 1 / 1 / 1.5 / 0 / 0.5) | frame; protocol; review Q1 |
| Zhu 2026 | 2, repository README | formal: G12 | 13 (3 / 3 / 3 / 0.5 / 1 / 1.5 / 0.5 / 0.5) | frame; protocol; review Q1; baseline |

## Counts, not scored

Read by the reviewers on 2026-10-29 through public interfaces; descriptive, and each one's caveat is in [review](review.md).

| Key | What was counted | Side | Used in |
|---|---|---|---|
| GitHub 2026e | public repository metadata (stars, last push) of the repositories named in review.md, through the unauthenticated API: 23 repositories and one repository search, and LeanDojo's stars | formal; LeanDojo by the human side | review Q1, Q3 |
| GitHub 2026f | Formal Conjectures items by the labels misformalization and ai-audit, and their states | human; checked again at the audit, when the pull requests had moved from 5,053 to 5,054 | protocol; review Q2; baseline |
| GitHub 2026g | PNT+ pull requests with the ai label against the rest, by state | human | protocol; review Q1 |
| Erdős-wiki 2026, counted | rows of the AI contributions wiki of the Erdős problems database by section, outcome, Lean and variant, frozen at 2026-06-30 | human | review Q2 |
| PyPI 2026 | recent downloads of `leanblueprint` and `lean-lsp-mcp` from the public statistics API | formal | review Q1, Q3 |
| Palomar 2026b | registry-wide totals from the registry's public data API: 845 results from 660 projects at the formal side's read, 847 from 661 at the audit later that day | formal | protocol; review Q1 |
| Mathlib 2026b | the mathlib statistics page: definitions, theorems, contributors | formal | frame; review Q1 |

## Read, not scored

| Key | What | Used in |
|---|---|---|
| LZ 2026b | a forum thread read by the formal side and passed to the human side's questions; cited as an example of practice, never as support | review Q2, Q5 |

## Linked, not rescored

| Key | Held by | Score there | Side |
|---|---|---|---|
| Tao 2023 | reader-ergonomics-academic, mathematical-writing (the PFR blueprint tour) | 15 | both |
| Mathlib 2026 | reader-ergonomics-academic, mathematical-writing (documentation style) | 12 | human |
| Wenzel 1999 | reader-ergonomics-academic, mathematical-writing (Isar) | a research source there, not scored as grey | formal |

## Keys

One key per work, across both sides and the family's five bibliographies; a work already in the family keeps its key.

## Kinds of claim

| Kind | Sources |
|---|---|
| an owner about its own tool or result | Harmonic 2024; Math Inc 2025; Anthropic 2026c; Mistral 2026; Axiom 2026; DeepSeek 2025; Goedel-LM 2025; StepFun 2025; Numina 2025; Google 2025 (a survey of its users); Adamczewski 2026 (counts of its own audit); Google DeepMind 2026; Lean FRO 2026a; Palomar 2026 (its own judge); Massot 2026b (its aim); TUe 2026 (its feedback) |
| a practitioner's estimate | Tao 2025c (six hours by hand); Kirov 2026a (ten times); Tao 2026i (hours against weeks) |
| checked by someone other than the owner | Buzzard 2026a (compiled the FLT proof and ran comparator) |
| counted by a program on a public record | GitHub 2026e to 2026h; PyPI 2026; Palomar 2026b; Mathlib 2026b; the Erdős DB 2026 statistics; the 56 trivial proofs compiled in Adamczewski 2026 |
| measured in a controlled study | none, on either side |

## Result of the scoring

- 80 grey sources: tier 1, 0; tier 2, 44; tier 3, 36. No book, standard or thesis on the loop was found.
- Per side, before the merge: formal, 43 (tier 2, 35; tier 3, 8); human, 43 (27 tier 3 blogs, posts and threads above 10; 10 tier 2 documents above 10; 6 below 10).
- 9 fall below 10 and are examples only: Lurch 2026, Numina 2025 and Rivin 2026 (formal side); LZ 2025b, LZ 2025d, LZ 2025g, LZ 2025h, PostHog 2026 and Tanswell 2026 (human side).
- The highest: 16.5 for first-hand case reports with their numbers, Scholze 2021 and Buzzard 2026a. Then 16 for Palomar 2026, Tao 2026e, and project rules that are enforced, PNT-plus 2026, Erdős DB 2026 and Erdős-wiki 2026.
- The comparator's documentation scored 17 on the formal side, its highest, and 14 on the human side; 14 is kept, by the rule above.
- On the formal side, company pages score 10.5 to 13.5, held down by objectivity, as each reports its own result. On the human side, Google 2025 is its owner's claim and scores lowest on objectivity.
- The six sources both sides scored differ by 0.5 to 5.5 points, a mean absolute difference of 2.1 of 20, the formal side 1.6 points higher on average.
- They differ most on methodology (0.92) and authority (0.75), least on outlet tier (0). The sides' authority rules differ (protocol section 9), and the two reviewers read apart, so this is no blind second rating.
- Reputation, votes and views of Q/A threads, and all counts, are those of 2026-10-29.
