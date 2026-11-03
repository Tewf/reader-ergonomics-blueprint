# The successor of a factorial has a prime factor

For every n, the number n! + 1 has a prime factor p.

**Lean:** `Blueprint.InfinitelyManyPrimes.factorial_succ_has_prime_factor`

**In words:** for every natural number n, there is a p such that p is prime and p divides n! + 1.

**Prose audited:** not yet

**Audited:** not yet

## Statement

For every natural number n, there is a prime p that divides n! + 1.

## Proof

1. The factorial n! is at least 1, so n! + 1 is at least 2.
2. By [the first claim](prime-factor-exists.md), a number at least 2 has a prime factor.

## See also

[The theorem](README.md); uses [a prime factor exists](prime-factor-exists.md).
