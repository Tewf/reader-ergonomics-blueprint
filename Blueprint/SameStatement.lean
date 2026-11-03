import Lean

/-!
# Same statement

`#same_statement proof challenge` fails unless the two constants have definitionally equal types
and the proof depends only on the three axioms Mathlib allows. It is the part of comparator's job
that Lean alone can do; the text match in `checks/local/comparator.py` is the part a program can do
without Lean. Neither decides whether the statement means what its source says: a person does.
-/

open Lean Elab Command Meta

namespace Blueprint

/-- The axioms a proof may rest on. -/
def permittedAxioms : List Name := [`propext, `Classical.choice, `Quot.sound]

elab "#same_statement " proof:ident challenge:ident : command => do
  let proofName ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo proof
  let challengeName ← liftCoreM <| realizeGlobalConstNoOverloadWithInfo challenge
  let env ← getEnv
  let some proofInfo := env.find? proofName | throwErrorAt proof "{proofName} is not declared"
  let some challengeInfo := env.find? challengeName | throwErrorAt challenge "{challengeName} is not declared"
  let same ← liftTermElabM <| isDefEq proofInfo.type challengeInfo.type
  unless same do
    throwErrorAt proof "{proofName} does not state what {challengeName} states"
  let axioms ← liftCoreM <| collectAxioms proofName
  for used in axioms do
    unless permittedAxioms.contains used do
      throwErrorAt proof "{proofName} depends on the axiom {used}"

end Blueprint
