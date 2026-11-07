# 0008: Which findings became principles

**Decision:** five findings of the review became principles, each graded as the review graded it, and the others stayed findings.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/0206e6950b4feca4194af419384c217863b7c42e/shapes/decision-record.md).

## Context

- The standard asks an extension for a card of principles, each with a grade and a check.
- The review graded few of its findings above convention. Its [position](../evidence/autoformalization/position.md) names four conditions under which a topic can be the loop's interface, and the repository already enforces three rules by program: `topic`, `lean-link` and `comparator`.

## Decision

- **Principles:** the four conditions, and the rule `lean-link` enforces, which makes five:
  - [a short statement, apart from its proof](../principles/statement/short-statement-apart-from-proof.md) (condition 1);
  - [one claim, one declaration](../principles/statement/one-claim-one-declaration.md) (`lean-link`);
  - [the model decides nothing](../principles/statement/the-model-decides-nothing.md) (condition 2);
  - [guidance at the claim's grain](../principles/claim/guidance-at-the-claims-grain.md) (condition 3);
  - [the person splits the reasoning](../principles/claim/the-person-splits-the-reasoning.md) (condition 4).
- **One shape and one check:** the [claim](../shapes/claim.md) and `claim-shape`, because the three claims already shared a form no program read.
- **Stayed findings:** every other finding, because none earned supported with caveat for a rule about writing:
  - the benchmark accuracies and error rates describe models, not a rule for a writer;
  - the effects on thinking and on learning have no randomised study;
  - the error messages for people have mixed results;
  - the costs of the audit were not measured.
- **Each principle names an existing check**, since `principle-coverage` fails a principle with none. Where a program decides only the form, the principle says that the meaning is judgment.

## Consequences

- **Good:** each rule has a grade, a source and a program that runs in CI.
- **Bad:** guidance at the claim's grain and the person's splitting are checked by form only; whether they help the person is untested.
- **Bad:** a finding that stays a finding is easy to forget; the review lists them.
- **To keep it true:** a principle's grade moves only with a cited source, and a new finding that earns one becomes a principle by a new record.

## See also

[Decisions](README.md); [the card](../standard.md); [0007](0007-the-audit-has-two-columns.md), whose two audit columns the second principle holds.
