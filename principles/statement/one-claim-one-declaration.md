# One claim, one declaration

**Claim:** a claim names exactly one Lean declaration, that declaration exists, and no declaration serves two claims.

- **Grade:** convention, adopted: leanblueprint's `checkdecls` and the projects built on it do the same; no study measured an effect.
- **Evidence:** [Massot 2026](../../evidence/bibliography.md), `checkdecls`; [PNT-plus 2026](../../evidence/bibliography.md), every named declaration is checked to exist; [review, Q1](../../evidence/autoformalization/review.md).
- **Check:** `lean-link` (exact): one `**Lean:**` line, a declaration of that name in the sources, no name shared by two claims.
- **Reader styles:** none.

## What it asks

- Give each claim topic one `**Lean:**` line with the full name of one declaration.
- Name no declaration twice, so a claim has one place.

## Why

- B1 ties one statement to one Lean name, so a reader and a program find the same declaration ([baseline](../../evidence/autoformalization/baseline.md)).
- A renamed or deleted declaration then fails at once, not at the audit.

## Limits

- The check compares names and never calls Lean; that Lean accepts the declaration is the build's job.
- That the declaration proves the claim in the topic is the person's audit.
