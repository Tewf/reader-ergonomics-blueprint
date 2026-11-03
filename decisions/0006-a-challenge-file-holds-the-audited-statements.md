# 0006: A challenge file holds the audited statements

**Decision:** each claim's Lean statement is written once more in a challenge file, apart from the proofs, and the
person audits that file; a program and Lean then hold each proof to it.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/shapes/decision-record.md).

## Context

- B1 asks that comparator check that each proof proves the stated claim, and that a person audit each statement
  ([baseline](../evidence/autoformalization/baseline.md)).
- The proof file mixes statements and proofs, so a person auditing it reads proofs they need not read.
- Lean FRO's comparator needs its own sandbox and a build of the whole project; it is not run here.

## Decision

- `Blueprint/Challenge.lean` states each claim with the body `sorry`, under the names `Challenge.X` for `Blueprint.X`.
- `checks/local/comparator.py` reads both files as text and fails when a statement differs after comments and
  whitespace, when the `open` commands differ, when the challenge holds a proof, or when a challenge has no topic.
- `Blueprint/Agreement.lean` has Lean compare the two types and list the axioms of each proof, built in CI as
  `BlueprintCompare`, apart from the proofs because the challenge holds `sorry` on purpose.
- Each topic gains an `**Audited:**` line: `not yet`, or the date the maintainer compared the statement with its
  source. The maintainer writes the date; the comparator reads its form only.

## Consequences

- The person audits four short statements in one file, not the proofs.
- A proof that proves something else fails the build, in seconds by text and then by Lean.
- **Bad:** two texts that differ may state the same claim, and the text check fails them; the person or Lean then
  says which side to change.
- **Bad:** equal statements mean the same only if the names in them mean the same; the audit, not a program, covers it.
- **Bad:** this is the comparator's job done in a lighter way, not the tool itself; running the tool is later work.

## See also

[Decisions](README.md); [0005](0005-three-checks-each-its-own-ci-step.md), which left this out of the first build.
