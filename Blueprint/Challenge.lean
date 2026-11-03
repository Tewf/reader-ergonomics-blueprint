import Mathlib

/-!
# The challenge file

The statements of `Blueprint/InfinitelyManyPrimes.lean`, written once more, apart from the proofs.
This file is the one the maintainer audits against the source. The proof file must prove exactly
these statements, and every body here is `sorry`, so no proof can hide in it.

Three programs hold the proof file to this one:
- `checks/local/comparator.py` matches each statement as text, after whitespace and comments;
- `Blueprint/Agreement.lean` has Lean compare the types and list the axioms of each proof;
- `lake build BlueprintCompare` in CI runs the second.

Names: the challenge for `Blueprint.X` is `Challenge.X`.
-/

namespace Challenge.InfinitelyManyPrimes

open Nat   -- for the notation `n !`

theorem exists_prime_factor (n : ℕ) (h : 2 ≤ n) : ∃ p, p.Prime ∧ p ∣ n := by
  sorry

theorem factorial_succ_has_prime_factor (n : ℕ) : ∃ p, p.Prime ∧ p ∣ n ! + 1 := by
  sorry

theorem prime_factor_gt (n p : ℕ) (hp : p.Prime) (hd : p ∣ n ! + 1) : n < p := by
  sorry

theorem exists_prime_gt (n : ℕ) : ∃ p, p.Prime ∧ n < p := by
  sorry

end Challenge.InfinitelyManyPrimes
