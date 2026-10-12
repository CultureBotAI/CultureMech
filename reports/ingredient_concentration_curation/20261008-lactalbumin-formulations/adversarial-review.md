# Adversarial Self-Review

This is local self-review, not independent PR approval.

## Addressed

- Guard false-LB nodes by original position and supplier metadata. The genuine
  yeast extract and sodium chloride survive even though labels overlap.
- Do not treat casein hydrolysate, lactalbumin hydrolysate and bovine serum
  albumin as interchangeable. The original DSMZ PDF supplies an explicit
  hydrolysate alternative that its API omits; KOMODO selects casein and TOGO
  M2287 selects lactalbumin.
- Do not import DSMZ stock rates as KOMODO finished-medium concentrations.
  Inspect both actual KOMODO detail pages, their per-liter heading and exact
  displayed amounts. Preserve rounded source precision.
- Keep A/B batch doses inside the pre-serum basal preparation. Neither stock
  water inputs nor a serum parts ratio supplies a measured final medium volume.
- Do not accept generic serum Gram/Mol columns as density or molarity evidence.
  Keep serum supplementation explicit without an unsupported numeric assertion.
- Null gas amounts are unknown, not zero. The variant's explicit gas rows and
  missing pH prevent an unsupported exact-duplicate or inherited-pH claim.
- Retain source sequence: separate A/B sterilization, cooling, combination,
  then sterile serum. Do not autoclave serum or infer a filtration pore size.
- Do not silently choose w/v for TOGO's 5% serum. Keep basal rates distinct from
  any inferred post-supplement dilution.
- Every original quantity and source ingredient row is independently accounted
  for. Regression tests reject corrupted quantities, units, chemical forms,
  evidence, history, source identity, variant links, lineage and bibliography.
  Fixture tests cover guarded preview, all-target checks, concurrent edits,
  forged plans, symlinks and idempotent application.

## Remaining Limits

Historical generic KOMODO checks failed at table boundaries. The later
[parser repair](../20261008-komodo-reference-validation/README.md) passes all
86 cohort checks and four reference CLI commands without changing any evidence.
Its requests refresh still received HTTP 403; explicit separate public captures
succeeded with identical bytes. Both outcomes remain recorded.

The source does not supply TOGO serum percentage basis, fixed serum doses,
variant gas quantities, or a complete quantified liquid alternative. Existing
groundings, including hydrate-sensitive links, are not all recertified by an
amount review. No newly verified DOI or organism-growth association is claimed.
Global merge/freshness and publication require separate successful checks.
