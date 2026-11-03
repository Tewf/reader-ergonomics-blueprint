# The model decides nothing

**Claim:** the person audits the statement that was checked, never a repaired one, and a model's reading of a statement is labelled as a model's, apart from the person's audit.

- **Grade:** supported with caveat: model judges overrate translations, and students missed unfaithful steps shown as verified; the two audit columns are a convention, untested.
- **Evidence:** [Ospanov 2025](../../evidence/bibliography.md), Table 2, 97.5% by a judge against 62.7% by people; [Guo 2026b](../../evidence/bibliography.md), sections 7.1 and 8.1.2; [Leinonen 2023](../../evidence/bibliography.md), model explanations correct for 48% of inputs; [position, condition 2](../../evidence/autoformalization/position.md); [decision 0007](../../decisions/0007-the-audit-has-two-columns.md).
- **Check:** `comparator` (exact): one `Audited` line, `not yet` or a date, and a proof that states its challenge. `claim-shape` (exact): a dated prose audit says who made it.
- **Reader styles:** none.

## What it asks

- Show the Lean statement beside a line "In words", labelled as a model's reading.
- Keep two audit lines: the prose against its source, and the Lean statement against the prose.
- Write a date on either line only when that reader has read.

## Why

- A compile loop silently corrected students' mistakes in 12 cases (Guo 2026b, section 7.1).
- A model cannot count as the audit: its fidelity judgments disagree with people's.

## Limits

- The "In words" line helps a reader who does not read Lean, and is itself unaudited.
- No study measured the cost of the person's audit.
