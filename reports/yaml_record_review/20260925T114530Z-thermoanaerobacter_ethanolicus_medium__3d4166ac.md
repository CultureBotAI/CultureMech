# YAML Record Review: THERMOANAEROBACTER ETHANOLICUS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobacter_ethanolicus_medium__3d4166ac.yaml
- Started UTC: 2026-09-25T11:42:04Z
- Finished UTC: 2026-09-25T11:45:30Z
- Verdict: needs curation

## Target

- Generated YAML for JCM Medium J221, THERMOANAEROBACTER ETHANOLICUS MEDIUM.
- The record was generated directly from `thermoanaerobacter_ethanolicus_medium`.
- The checked sources were JCM Medium 221 and MediaDive J221.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to JCM/MediaDive Medium J221.
- JCM 221 and MediaDive J221 both identify the formula as THERMOANAEROBACTER ETHANOLICUS MEDIUM.
- The generated record is a direct single-source import with no merged source duplicates.

## Evidence

- JCM 221 lists a main recipe with 0.5 ml Vitamin solution, 5 ml Wolfe's modified mineral elixir, 40 ml Reducing solution, and 960 ml distilled water.
- Vitamin solution is a 500 ml stock added at 0.5 ml/L.
- Wolfe's modified mineral elixir is a 1 L stock added at 5 ml/L.
- Reducing solution contains 200 ml 0.2 N NaOH, 2.5 g Na2S x 9 H2O, and 2.5 g L-Cysteine HCl x H2O; the main recipe uses 40 ml/L.
- JCM 221 gives pH 6.5 and directs the curator to boil the main ingredients under N2-H2 95:5, add Reducing solution during gassing, and autoclave the stoppered anaerobic tubes.

## Completeness

- pH 6.5 is present.
- JCM preparation steps for the main recipe, mineral elixir, and reducing solution are present.
- The 960 ml main distilled-water row is missing.
- Vitamin solution, Wolfe's modified mineral elixir, and Reducing solution are flattened at undiluted stock strength.

## Findings

- Vitamin solution was expanded at full 500 ml stock strength instead of as a 0.5 ml/L addition.
- Wolfe's modified mineral elixir was expanded at full 1 L stock strength instead of as a 5 ml/L addition.
- Reducing solution was expanded at full 200 ml stock strength instead of as a 40 ml/L addition.
- The 0.2 N NaOH solution volume inside Reducing solution was converted to a nonsensical 200 G_PER_L sodium hydroxide ingredient row.
- The 960 ml main distilled-water row is missing.

## Recommended Edits

- Regenerate JCM 221 with Vitamin solution, Wolfe's modified mineral elixir, and Reducing solution retained as stock additions, or expand them only after applying the 0.5 ml/L, 5 ml/L, and 40 ml/L dilution factors.
- Preserve 0.2 N NaOH as a solution volume inside Reducing solution rather than converting its 200 ml amount to 200 G_PER_L.
- Preserve the main 960 ml distilled-water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that JCM 221 no longer carries 200 G_PER_L sodium hydroxide or undiluted vitamin, Wolfe mineral, and reducing-solution rows in the main ingredient list.

## Additional Notes

- None found.
