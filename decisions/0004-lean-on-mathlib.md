# 0004: Lean on Mathlib

**Decision:** the Lean sources are a Lake project at the root, built on Mathlib at the tag whose toolchain it takes.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/0206e6950b4feca4194af419384c217863b7c42e/shapes/decision-record.md).

## Context

- The claims are one-line Mathlib lemmas or close to them.
- Lean alone would make the miniature a small library of number theory.

## Decision

- `lakefile.toml`, `lean-toolchain` and `Blueprint/InfinitelyManyPrimes.lean` at the root.
- Mathlib is required at the tag v4.35.0, and the toolchain is the one that tag names.
- Considered: core Lean only, which needs no cache and was dropped for the reason above.

## Consequences

- A reader who knows Mathlib can check each statement against a library it trusts.
- **Bad:** a cold build is slow and the cache is large, so CI fetches the cache before it builds.

## See also

[Decisions](README.md); [0003](0003-euclids-theorem-as-the-first-proof.md), what is proved.
