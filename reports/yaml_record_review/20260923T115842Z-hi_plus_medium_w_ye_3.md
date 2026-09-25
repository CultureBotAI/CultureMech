# YAML Record Review: HI Plus Medium w/ YE #3
- Repository: CultureMech
- Record: data/merge_yaml/merged/hi_plus_medium_w_ye_3.yaml
- Started UTC: 2026-09-23T11:57:47Z
- Finished UTC: 2026-09-23T11:58:42Z
- Verdict: needs curation

## Target

Reviewed the generated Togo M2467 / ATCC Medium 243 record for `HI Plus Medium w/ YE #3` at `data/merge_yaml/merged/hi_plus_medium_w_ye_3.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hi_plus_medium_w_ye_3.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M2467`, which cites ATCC Medium 243. The Togo and ATCC titles match the generated medium name.

## Evidence

ATCC Medium 243 lists a base medium with 25.0 g Heart Infusion Broth, 15.0 g Agar Noble if required, and 700.0 ml DI water. After autoclaving at 121 C and cooling to 55 C, the source aseptically adds 200.0 ml heat-inactivated horse serum and 100.0 ml Yeast Extract #3. Yeast Extract #3 is a separate subrecipe made from 150.0 g store-bought yeast in 1000.0 ml DI water, mixed, autoclaved, left overnight, centrifuged at 9,000 rpm for 50 minutes, bottled as supernatant, autoclaved again, and stored sterile at 2-8 C. The final pH should be 7.4.

The generated record merges the 700 ml base-water row with the 1000 ml Yeast Extract #3 water row into `1700.0 G_PER_L`, promotes the Yeast Extract #3 stock's 150 g yeast into a top-level ingredient, represents 200 ml horse serum and 100 ml Yeast Extract #3 as grams per liter, and lacks pH and preparation steps.

## Completeness

The normalized source, `data/normalized_yaml/bacterial/TOGO_M2467_HI_Plus_Medium_w_YE_3.yaml`, already has a September 2026 ATCC repair with corrected 25 g/L Heart Infusion Broth, 15 g/L optional Agar Noble, 700 ml/L DI water, 200 ml/L horse serum, a nested 100 ml/L Yeast Extract #3 solution, pH 7.4, and the base-medium preparation sequence. The generated artifact is stale relative to that source.

## Findings

- Base-medium water and Yeast Extract #3 water were deduplicated into one top-level `1700.0 G_PER_L` water row.
- `Yeast (Store bought Fleischmann's yeast)` belongs inside the Yeast Extract #3 subrecipe, not as a final-medium ingredient at 150 g/L.
- Horse serum and Yeast Extract #3 are 200 ml and 100 ml aseptic supplements, not gram-per-liter ingredients.
- The generated record uses the old Togo-downscaled 17.5 g Heart Infusion Broth and 10 g Agar Noble values instead of ATCC's 25 g and 15 g values for the final liter.
- Agar Noble is optional in the ATCC base, but the generated physical state and ingredient row make it an unconditional solid-agar recipe.
- The source pH 7.4, 121 C autoclaving, 55 C cooling, heat-inactivation of horse serum, and Yeast Extract #3 centrifugation/autoclaving workflow are missing.

## Recommended Edits

- Regenerate this artifact from the repaired normalized source.
- Preserve Yeast Extract #3 as a nested solution and keep its 1000 ml water distinct from the base-medium 700 ml water.
- Preserve horse serum and Yeast Extract #3 as milliliter supplements added aseptically after the base cools to 55 C.
- Model Agar Noble as optional or split liquid and solid variants instead of making agar unconditional.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Confirm the regenerated artifact no longer has `1700.0 G_PER_L` water or any top-level Fleischmann's yeast ingredient.

## Additional Notes

None.
