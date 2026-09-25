# YAML Record Review: HI Plus Medium w/ YE #3
- Repository: CultureMech
- Record: data/merge_yaml/merged/hi_plus_medium_w_ye_3__d40eed2b.yaml
- Started UTC: 2026-09-23T11:59:25Z
- Finished UTC: 2026-09-23T12:00:00Z
- Verdict: needs curation

## Target

Reviewed the generated Togo M2177 / ATCC Medium 243 record for `HI Plus Medium w/ YE #3` at `data/merge_yaml/merged/hi_plus_medium_w_ye_3__d40eed2b.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hi_plus_medium_w_ye_3__d40eed2b.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M2177`, which cites ATCC Medium 243. It is a duplicate ATCC 243 import alongside `TOGO:M2467`, and both sources describe the same HI Plus Medium w/ YE #3 recipe.

## Evidence

ATCC Medium 243 lists a base medium with 25.0 g Heart Infusion Broth, 15.0 g Agar Noble if required, and 700.0 ml DI water. After autoclaving at 121 C and cooling to 55 C, the source aseptically adds 200.0 ml heat-inactivated horse serum and 100.0 ml Yeast Extract #3. Yeast Extract #3 is made separately from 150.0 g store-bought yeast and 1000.0 ml DI water, then mixed, autoclaved, settled overnight, centrifuged, transferred as supernatant, autoclaved again, and stored sterile at 2-8 C.

The generated M2177 branch instead combines base water with Yeast Extract #3 water into `1700.0 G_PER_L`, puts Yeast Extract #3's yeast in the final medium at `150 G_PER_L`, imports 200 ml horse serum and 100 ml Yeast Extract #3 as grams per liter, and lacks the pH 7.4 and preparation workflow.

## Completeness

The normalized M2177 source already has a September 2026 repair with corrected ATCC amounts, a nested Yeast Extract #3 solution, milliliter units for water, horse serum, and the Yeast Extract #3 addition, plus basic base-autoclaving and aseptic-addition preparation steps. The generated artifact is stale relative to that source.

## Findings

- The 700 ml base-water row and 1000 ml Yeast Extract #3 water row were incorrectly summed into one final-medium water ingredient.
- Horse serum and Yeast Extract #3 are aseptic volume additions, not mass concentrations.
- The Yeast Extract #3 stock's 150 g yeast is a nested stock ingredient, not a top-level final-medium ingredient.
- ATCC's 25.0 g Heart Infusion Broth and 15.0 g optional Agar Noble were downscaled to 17.5 g and 10 g in the stale generated artifact.
- Optional Agar Noble is modeled as an unconditional solidifying ingredient.
- The ATCC 121 C base autoclave, 55 C cooling, horse-serum heat inactivation, Yeast Extract #3 preparation, and final pH 7.4 are absent.

## Recommended Edits

- Regenerate this artifact from the repaired `data/normalized_yaml/bacterial/hi_plus_medium_w_ye_3.yaml` source.
- Preserve Yeast Extract #3 as a nested 100 ml/L solution with its own 150 g/L yeast and 1000 ml/L DI-water recipe.
- Preserve horse serum as a 200 ml/L aseptic supplement.
- Keep Agar Noble optional or split the source into liquid and solid variants.
- Merge or alias the M2177 and M2467 ATCC Medium 243 branches after regeneration.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated artifact.
- Confirm the regenerated record no longer has top-level `1700.0 G_PER_L` water, `100 G_PER_L` Yeast Extract #3, or `150 G_PER_L` Yeast.

## Additional Notes

None.
