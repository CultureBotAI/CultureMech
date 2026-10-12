# Adversarial Review

## Applied Corrections

1. Flattened resazurin rate could be mistaken for stock strength. Source row
   explicitly specifies 0.1% w/v and 0.50 ml; the repair separates them and
   uses L for batch dose, not ML_PER_L without a measured final-volume basis.
2. Cysteine/sulfide were direct ingredients despite the post-sterilization stock
   instruction. The repair moves them to separate descriptors, preserves
   0.15 g batch requirements, and withdraws unsupported stock-rate assertions.
3. The standalone water percentage was a unit error. The repair restores 1 L
   input, and adds the missing source water to the two medium copies.
4. KOMODO's aerobic import annotation could contradict the procedure. Historical
   text is preserved and explicitly scoped; the verified anoxic procedure is
   added without asserting organism growth or an incubation condition.
5. Old snippets must not endorse newly moved stock concentrations. Explicit
   successor resolutions preserve the old text while withdrawing that reading.

## Remaining Limits

- Reducer stock strength, solvent and volume are not specified by the inspected
  exact recipe. They remain unknown, not estimated from neighboring media.
- The resazurin ontology mapping is retained and explicitly unvalidated as the
  sodium salt. This batch does not claim chemical-identity review completion.
- Eight retained concentrations are provider-nominal rates, not independent
  final-volume measurements. No final-medium concentration is derived.
- Existing legacy solution placeholders and quality flags remain untouched.
- The first Python 3.11 run loaded an outdated historical-withholding test before
  its successor list was extended. The original failure remains recorded;
  the identical final selection passes all 315 tests, and the cached Python
  3.13 selection passes 238. The preserved historical finding is checked against
  `before_text`, not silently replaced by the new applied result.
- The fast tier cannot collect in the cached environment because `dotenv`,
  `rapidfuzz`, `pandas` and `bs4` are missing. Product/reference validators also
  lack dependencies. None is counted as successful validation.
- Passing schema/tests does not prove downstream provenance retention. The
  actual-group audit fails for both media: 28/29 scoped snippets survive but
  complete ingredient/stock/procedure/provenance fields do not. The standalone
  solution remains outside medium merging. Global gates are recorded separately.

This is a local agent review with regression tests, not a hosted PR or human
review. The all-record objective remains unfinished.
