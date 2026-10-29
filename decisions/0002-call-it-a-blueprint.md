# 0002: Call it a blueprint

**Decision:** the repository is called reader-ergonomics-blueprint. A **blueprint** is the field's word for a graph of
claims each checked by a proof assistant; this repository writes one as topics.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/shapes/decision-record.md).

## Context

- The maintainer's rule is to name a thing as its field names it. In formal mathematics a blueprint is a dependency
  graph of informal statements, each linked to a Lean declaration that Lean checks; the review's baseline, B1, is one
  ([baseline](../evidence/autoformalization/baseline.md)).
- For the general case, a claim split into sub-claims each backed by evidence, systems engineering says **assurance
  case**. OpenAlex holds 3,099 such works on 2026-10-29: 441 with language models, 362 with proof assistants.

## Decision

- The name is blueprint, the term of the first and for now only checker; the general case keeps its own term, and
  gets a review before any checker other than Lean.
- Considered: assurance (the general term, tied to safety certification), reasoning and checked-reasoning (plain,
  not terms of art).

## Consequences

- A reader who knows Lean blueprints recognises the structure at once.
- **Bad:** the name says mathematics; a reader with another checker in mind may pass it by, until the general case is
  reviewed and named on the front page.

## See also

[Decisions](README.md); [0001](0001-a-repository-of-its-own.md), why it is a repository of its own.
