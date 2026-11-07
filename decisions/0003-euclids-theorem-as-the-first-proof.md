# 0003: Euclid's theorem as the first proof

**Decision:** the first proof is Euclid's theorem, that for every n there is a prime greater than n, as a theorem topic
holding three claim topics.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/0206e6950b4feca4194af419384c217863b7c42e/shapes/decision-record.md).

## Context

- The first build tests the pipeline, not a theorem ([design](../design/first-build.md)).
- Every step of the argument is a separate claim a program can check.

## Decision

- Three claims: every natural number at least 2 has a prime factor; n! + 1 has a prime factor p; p exceeds n.
- Layout: `proofs/infinitely-many-primes/README.md` for the theorem, one file per claim beside it.
- Each topic names its Lean declaration on one line.

## Consequences

- The proof is short and classical, so a reader can audit each statement against its source in minutes.
- **Bad:** it says little about a proof with real dependencies; a second proof with a diamond in its graph is next.

## See also

[Decisions](README.md); [0004](0004-lean-on-mathlib.md), the Lean side.
