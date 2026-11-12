# Shape: claim

One claim of a proof, written so that a person audits its statement, Lean checks its proof, and a program finds each part by its label.

It follows the [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/shapes/topic.md): a title, a summary, and a parent that lists it. It adds the lines that tie the claim to Lean and to the person's audit.

## When to use it

- For each step of a proof that has one Lean declaration: a lemma, or the theorem's last step.
- Not for the theorem that lists the claims: that is a topic, whose table is its contents.
- Not for a design or a decision: those have their own shapes.

## The skeleton

```markdown
# <the claim, as a short phrase>

<The claim in one sentence, ending in a period.>

**Shape:** [claim](<path to this shape>)
**Lean:** `<Full.Name.Of.The.Declaration>`

**In words:** <a reading of the Lean statement, as plain words, by a model; not an audit.>

**Prose audited:** <not yet | YYYY-MM-DD, by a model, not a person | YYYY-MM-DD, by the maintainer: against which source>

**Audited:** <not yet | YYYY-MM-DD, when a reader of Lean compared the Lean statement with the prose>

## Statement
<The claim stated in full, as the Lean statement says it.>

## Proof
<Numbered steps, each a sentence a reader can check.>

## See also
<The theorem, and the claims this one uses.>
```

## Where each part comes from

| Part | What it does | Evidence | Grade |
|---|---|---|---|
| Claim sentence | the summary that stands for the claim when folded | [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/shapes/topic.md); [overview first](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/principles/document/overview-first.md) | measured, for overview first |
| Lean line | ties the claim to one declaration, which `lean-link` finds | [one claim, one declaration](../principles/statement/one-claim-one-declaration.md) | convention, adopted |
| In words | a model's reading of the Lean statement, for a reader who does not read Lean | [the model decides nothing](../principles/statement/the-model-decides-nothing.md) | supported with caveat |
| Prose audited, Audited | the audit in two columns: the prose against its source, the Lean against the prose | [decision 0007](../decisions/0007-the-audit-has-two-columns.md) | convention, untested |
| Statement, Proof | the claim stated apart from its proof, in steps | [a short statement, apart from its proof](../principles/statement/short-statement-apart-from-proof.md) | supported with caveat |

## The rules

1. The sentence under the title is one sentence, of at most 35 words.
2. The five labelled lines come once each, in the order of the skeleton.
3. A model's audit says it is not a person's; a date is written only by the one who read.
4. The Lean name is a full name, in backticks, that no other claim names.
5. The parts are Statement, Proof and See also, in that order, and Statement is not empty.
6. The Shape line links this shape.

## Checked by

- `claim-shape`, in this repository's `checks/local/`: rules 1, 2, 3, 5 and 6.
- `lean-link`: rule 4. `comparator`: the form of the Audited line, and that the proof states the challenge.
- `topic` and `shape-conformance`: the title and summary, the parent's listing, and the three parts.

## Worked example

The three claims of Euclid's theorem follow this shape, each carrying its Shape line:

- [A prime factor exists](../proofs/infinitely-many-primes/prime-factor-exists.md);
- [The successor of a factorial has a prime factor](../proofs/infinitely-many-primes/factorial-successor-has-prime-factor.md);
- [The prime factor is large](../proofs/infinitely-many-primes/prime-factor-is-large.md).

Their theorem is [There are infinitely many primes](../proofs/infinitely-many-primes/README.md).
