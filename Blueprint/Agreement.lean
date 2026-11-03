import Blueprint.InfinitelyManyPrimes
import Blueprint.Challenge
import Blueprint.SameStatement

/-!
# Agreement of the proofs with the challenge

One line per topic: Lean compares the type of the proof with the type of its challenge, and lists
the axioms the proof rests on. A line is missing only when the comparator script finds it so.
-/

#same_statement Blueprint.InfinitelyManyPrimes.exists_prime_factor Challenge.InfinitelyManyPrimes.exists_prime_factor
#same_statement Blueprint.InfinitelyManyPrimes.factorial_succ_has_prime_factor Challenge.InfinitelyManyPrimes.factorial_succ_has_prime_factor
#same_statement Blueprint.InfinitelyManyPrimes.prime_factor_gt Challenge.InfinitelyManyPrimes.prime_factor_gt
#same_statement Blueprint.InfinitelyManyPrimes.exists_prime_gt Challenge.InfinitelyManyPrimes.exists_prime_gt
