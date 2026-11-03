# A prime factor exists

Every natural number m with m at least 2 has a prime factor.

**Lean:** `Blueprint.InfinitelyManyPrimes.exists_prime_factor`

## Statement

If 2 ≤ m, there is a prime p that divides m.

## Proof

Take the least divisor of m that exceeds 1.
A divisor of it strictly between 1 and itself would divide m and be smaller, so there is none, and it is prime.

## See also

[The theorem](README.md).
