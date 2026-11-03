# A short statement, apart from its proof

**Claim:** the Lean statement a person audits sits in a short file of its own, apart from every proof, and each proof is held to it.

- **Grade:** supported with caveat for people repairing the statement they read and for a precise match to a vetted reference; convention, untested for the loop as a whole.
- **Evidence:** [Collins 2024](../../evidence/bibliography.md), experts repaired misstated problems in their heads; [Poiroux 2025](../../evidence/bibliography.md), Table 1, equivalence to a reference is precise; [Lean FRO 2026a](../../evidence/bibliography.md) and [Palomar 2026](../../evidence/bibliography.md), practice keeps a challenge file; [position, condition 1](../../evidence/autoformalization/position.md).
- **Check:** `comparator` (exact): the challenge file holds the same statement as the proof, with body `sorry`, and no orphan; whether the statement means what its source means is judgment.
- **Reader styles:** none.

## What it asks

- Write each claim's Lean statement once more in a challenge file, with the body `sorry`.
- Keep that file short enough to read in one sitting; the person audits it, not the proofs.
- Let a program, then Lean, hold each proof to the challenge.

## Why

- No program decides whether a formal statement means what its source means (Azerbayev 2023, section 4.1.1).
- People read the statement they expect, so a short statement apart from its proof is the one they can repair.
- The challenge file is B1's practice ([baseline](../../evidence/autoformalization/baseline.md)).

## Limits

- Two different texts may state the same claim, and the check then fails; a person says which side to change.
- Equal texts mean the same only if the names in them do; the audit covers that.
- No study compared a challenge file with a statement read inside the proof file.
