# A prime factor exists

Every natural number n with n at least 2 has a prime factor.

**Lean:** `Blueprint.InfinitelyManyPrimes.exists_prime_factor`

**In words:** for a natural number n with 2 ≤ n, there is a p such that p is prime and p divides n.

**Prose audited:** not yet

**Audited:** not yet

## Statement

If 2 ≤ m, there is a prime p that divides m.

## Proof

Take the least divisor of m that exceeds 1.
A divisor of it strictly between 1 and itself would divide m and be smaller, so there is none, and it is prime.

## See also

[The theorem](README.md).
