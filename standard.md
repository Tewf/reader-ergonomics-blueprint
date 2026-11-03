# The blueprint standard

What writing a person's reasoning as a tree of checked claims adds to the standard: the statement the person audits, and the claim the person writes. It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/standard.md): read that one first. Its principles come from the [review of autoformalization](evidence/autoformalization/README.md), and none is measured as a whole loop: they are the conditions under which a topic can be the interface of a person, a model and Lean.

## How to use it

1. **Write each claim** to the [claim shape](shapes/claim.md), and name it with a `**Shape:**` line that links it.
2. **Write to the principles** below, and to those of reader-ergonomics and of the [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/shapes/topic.md), which still hold.
3. **Check:** run the standard's checks on the repository. `claim-shape` checks each claim, `lean-link` its declaration, `comparator` its statement against the challenge file, and `topic` the tree. Lean checks the proofs in CI.

Grades mean what they mean in [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/4f99372093729dacf982e9174e94f6b8793c513d/standard.md#grades): measured, supported with caveat, convention, not supported. Each principle states its grade and never claims more.

## Principles

<!-- principles:start -->

### Statement: what the person audits

| Principle | Claim | Grade |
|---|---|---|
| [One claim, one declaration](principles/statement/one-claim-one-declaration.md) | a claim names exactly one Lean declaration, that declaration exists, and no declaration serves two claims. | convention, adopted: leanblueprint's `checkdecls` and the projects built on it do the same; no study measured an effect |
| [A short statement, apart from its proof](principles/statement/short-statement-apart-from-proof.md) | the Lean statement a person audits sits in a short file of its own, apart from every proof, and each proof is held to it. | supported with caveat for people repairing the statement they read and for a precise match to a vetted reference; convention, untested for the loop as a whole |
| [The model decides nothing](principles/statement/the-model-decides-nothing.md) | the person audits the statement that was checked, never a repaired one, and a model's reading of a statement is labelled as a model's, apart from the person's audit. | supported with caveat: model judges overrate translations, and students missed unfaithful steps shown as verified; the two audit columns are a convention, untested |

### Claim: what the person writes

| Principle | Claim | Grade |
|---|---|---|
| [Guidance at the claim's grain](principles/claim/guidance-at-the-claims-grain.md) | a verdict, an error or a hint names the person's claim, not the checker's internal step. | supported with caveat: messages at the checker's grain stopped students; convention, untested for the grain itself |
| [The person splits the reasoning](principles/claim/the-person-splits-the-reasoning.md) | each claim is one topic the person wrote, with one sentence, a statement and a proof; the splitting into claims is not left to a model. | convention, untested for the loop; supported with caveat for checking, which small claims help every time practice reports, while help for thinking is reported only where the person did the splitting |

<!-- principles:end -->

## Where the evidence is

Every principle links its review in [evidence/](evidence/README.md), and every work cited is listed once in the [bibliography](evidence/bibliography.md).
