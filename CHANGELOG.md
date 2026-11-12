# Changelog

Every release of this repository, and the releases of reader-ergonomics and reader-ergonomics-topic it pins, newest
first, in the form of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). A pin move is recorded here, not in
decisions/.

## [Unreleased]

### Changed

- Pinned reader-ergonomics v1.24.2 (`65e4247`), from v1.22.1 (`0206e69`): fixes that remove false findings in the sentence, term and figure checks, and `[defined_terms] cues`.

## [0.1.2] - 2026-11-07

### Changed

- Pinned reader-ergonomics v1.22.1 (`0206e69`), from v1.21.0 (`2e5b6f0`): front matter skipped by the sentence checks and LaTeX maths blanked, escaped-pipe wikilinks resolved, and `standard-pin` moves a pin.

## [0.1.1] - 2026-11-04

### Changed

- Pinned reader-ergonomics v1.21.0 (`2e5b6f0`), from v1.20.0 (`4f99372`): duplication skips the lines a declared shape prescribes
- Pinned reader-ergonomics v1.20.0 (`4f99372`), from v1.19.2 (`b9732b9`): the runner's verdicts file (`--out`), and hand-written llms.txt lines kept through a rebuild
- Tag v0.1.1 and a GitHub release of the same name.

## [0.1.0] - 2026-11-03

### Added

- The first release, at 0.x because the loop is not built: a review of autoformalization (273 sources, grey and formal)
  that names its baseline, B1, the audited blueprint.
- The card: five principles in two groups, the statement a person audits and the claim a person writes, each with its
  grade, and one shape, the claim.
- Euclid's theorem as the first proof: a theorem topic and three claim topics, each naming one Lean declaration, with
  a challenge file that holds the statements apart from the proofs.
- Checks beside the standard's: the claim check, the Lean link check and the comparator in `checks/local/`, with 63
  unit tests run in CI before the standard's checks, and Lean built in CI.
- Take it, on the front page: the shape to copy, the pin and the one command to run.

### Changed

- Pinned reader-ergonomics v1.19.2 (`b9732b9`), from v1.13.0 (`7a76cc6`): the release-version check, the changelog
  form and its check, grades per clause and the take-your-own-version section. reader-ergonomics-topic stays at
  v0.6.0 (`092ae2f`).

## 2026-10-29

### Changed

- Pinned reader-ergonomics v1.13.0 (`7a76cc6`) and reader-ergonomics-topic v0.6.0 (`092ae2f`), at the repository's
  start: the standard's figure, link and pin checks, and the topic with its splitting rule.
