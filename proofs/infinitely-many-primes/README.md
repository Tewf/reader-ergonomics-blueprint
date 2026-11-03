# There are infinitely many primes

For every natural number n there is a prime greater than n. Euclid's argument proves it in three claims.

**Shape:** [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/092ae2fc2e07226b695e219e3eb14b40286faa25/shapes/topic.md)
**Lean:** `Blueprint.InfinitelyManyPrimes.exists_prime_gt`

**Prose audited:** 2026-11-03, the three claims against Euclid IX.20 (Joyce 1996) and its factorial variant (Wikipedia 2026 Euclid). By a model on the maintainer's order; not a person's audit.

**Audited:** not yet

The two lines are the two columns of [0007](../../decisions/0007-the-audit-has-two-columns.md): the prose against its source, which the maintainer reads, and the Lean statement against the prose, which waits for a reader of Lean. Each claim's "In words" line is a model's reading of its Lean line, not an audit.

## Statement

For every natural number n, there is a prime p with n < p.

## Contents

| Claim | Summary |
|---|---|
| [A prime factor exists](prime-factor-exists.md) | every natural number at least 2 has a prime factor |
| [The successor of a factorial has a prime factor](factorial-successor-has-prime-factor.md) | n! + 1 is at least 2, so some prime p divides it |
| [The prime factor is large](prime-factor-is-large.md) | p exceeds n, since p at most n would divide n! and so divide 1 |

## Proof

1. By [claim 2](factorial-successor-has-prime-factor.md), n! + 1 has a prime factor p.
2. By [claim 3](prime-factor-is-large.md), p exceeds n.
3. So p is a prime greater than n.

## See also

[Design of the first build](../../design/first-build.md); [the front page](../../README.md).
