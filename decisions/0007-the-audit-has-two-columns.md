# 0007: The audit has two columns

**Decision:** A claim carries two audit lines, the prose against its source and the Lean statement against the
prose. The maintainer reads the prose and not the Lean, so the second line waits for a reader of Lean.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/shapes/decision-record.md).

## Context

- B1 asks a person to audit each statement against its source. The first build gave each topic one Audited line.
- The maintainer does not read Lean. The review found that no program decides whether a formal statement means what
  its source means. It also found that a model's judgment overrates the translation. So a model's reading of the Lean
  line can be shown, labelled, but cannot count as the audit.

## Decision

- Each topic carries an "In words" line, a model's reading of its Lean statement, labelled as such on the folder's page.
- Two lines: "Prose audited", the prose against its source, which the maintainer gives; "Audited", the Lean statement
  against the prose, which waits for a reader of Lean and which the comparator reads. The comparator and Lean still check that the proof proves the stated
  Lean line, so what is unaudited is only the meaning of that line.

## Consequences

- The maintainer can close the first column today by reading three sentences against Euclid's argument.
- **Bad:** until a reader of Lean fills the second column, B1 is complete in form and open in meaning, and the front
  page says so.

## See also

[Decisions](README.md); the three claims under [proofs/infinitely-many-primes/](../proofs/infinitely-many-primes/README.md).
