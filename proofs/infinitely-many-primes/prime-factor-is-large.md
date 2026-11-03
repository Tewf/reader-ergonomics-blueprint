# The prime factor is large

A prime p that divides n! + 1 is greater than n.

**Lean:** `Blueprint.InfinitelyManyPrimes.prime_factor_gt`

**Audited:** not yet

## Statement

If p is prime and p divides n! + 1, then n < p.

## Proof

1. Suppose p ≤ n. Then p is one of the factors of n!, so p divides n!.
2. Then p divides the difference (n! + 1) − n!, which is 1.
3. A prime does not divide 1. So p > n.

## See also

[The theorem](README.md); uses [the successor of a factorial](factorial-successor-has-prime-factor.md), whose prime factor it bounds.
