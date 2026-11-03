import Mathlib

/-!
# There are infinitely many primes

Euclid's argument in three claims, one declaration each. The topics under
`proofs/infinitely-many-primes/` state the claims in prose and name these declarations.
-/

namespace Blueprint.InfinitelyManyPrimes

open Nat   -- for the notation `n !`

/-- Claim 1: every natural number at least 2 has a prime factor. -/
theorem exists_prime_factor (n : ℕ) (h : 2 ≤ n) : ∃ p, p.Prime ∧ p ∣ n :=
  Nat.exists_prime_and_dvd (by omega)

/-- Claim 2: `n ! + 1` is at least 2, so it has a prime factor. -/
theorem factorial_succ_has_prime_factor (n : ℕ) : ∃ p, p.Prime ∧ p ∣ n ! + 1 :=
  exists_prime_factor (n ! + 1) (by have := Nat.factorial_pos n; omega)

/-- Claim 3: a prime factor `p` of `n ! + 1` exceeds `n`. -/
theorem prime_factor_gt (n p : ℕ) (hp : p.Prime) (hd : p ∣ n ! + 1) : n < p := by
  by_contra h
  have h1 : p ∣ n ! := Nat.dvd_factorial hp.pos (not_lt.mp h)
  have h2 : p ∣ 1 := (Nat.dvd_add_right h1).mp hd
  exact hp.one_lt.ne' (Nat.dvd_one.mp h2)

/-- Euclid's theorem: for every `n` there is a prime greater than `n`. -/
theorem exists_prime_gt (n : ℕ) : ∃ p, p.Prime ∧ n < p :=
  let ⟨p, hp, hd⟩ := factorial_succ_has_prime_factor n
  ⟨p, hp, prime_factor_gt n p hp hd⟩

end Blueprint.InfinitelyManyPrimes
