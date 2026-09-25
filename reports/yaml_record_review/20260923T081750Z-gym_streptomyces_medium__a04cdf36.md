# YAML Record Review: GYM Streptomyces Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/gym_streptomyces_medium__a04cdf36.yaml`
- Started UTC: 2026-09-23T08:16:20Z
- Finished UTC: 2026-09-23T08:17:50Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008918`, `gym_streptomyces_medium`, merged from Togo `M2331` and the Togo `M3229` full-media agar variant.

## Validation

- LinkML validation: passed.
- Strict validation: passed with 0 ERROR rows in `/private/tmp/gym_streptomyces_medium_a04cdf36.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked: the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record is the 12 g/L agar Togo `M2331` formula. Exact ignored-file-inclusive search across `data/normalized_yaml/bacterial` and `data/merge_yaml/merged` found the expected `TOGO:M2331` parent plus `TOGO:M3229`, a full-media child that increases agar to 20 g/L. The 20 g/L child is already annotated as a `CONCENTRATION_VARIANT`, so it should not be grouped as an exact duplicate in this generated 12 g/L record.

Glucose, CaCO3, water, and Agar are grounded. Yeast extract and Malt extract are ungrounded complex components.

## Evidence

Togo `M2331` lists 1000 ml Distilled water, 4 g Yeast extract, 2 g CaCO3, 4 g Glucose, 12 g Agar, and 10 g Malt extract, with a comment to adjust pH to 7.2 before adding agar and delete CaCO3 if liquid medium is used. Togo `M3229` lists the same non-agar ingredients but 20 g Agar, has `ph: "7.2"`, describes itself as the full DSMZ Medium 65 formulation, and repeats the same pH/CaCO3 preparation comment.

The generated record preserves the `M2331` 12 g/L Agar row, but `merged_from`, `curation_history`, and `synonyms` also include the 20 g/L `full_media_gym_streptomyces_medium` child as if it were an exact duplicate.

## Completeness

The `M2331` ingredient mass concentrations are present, but the record is incomplete because it over-merges a 20 g/L agar concentration variant, drops pH 7.2 and the pH/CaCO3 preparation instruction, and turns the 1000 ml distilled-water solvent into a 1000 g/L top-level mass concentration.

## Findings

- Togo `M3229` is incorrectly merged into the `M2331` generated record. It differs at Agar 20 g/L versus 12 g/L and should remain a `CONCENTRATION_VARIANT`, not a duplicate in `merged_from`, `curation_history`, or `synonyms`.
- The generated record is missing the pH 7.2 target and the preparation instruction to adjust pH before adding agar and delete CaCO3 for liquid medium.
- Distilled water is misrepresented as `1000 G_PER_L`; the Togo source records a 1000 ml solvent volume.
- Yeast extract and Malt extract remain ungrounded. These are complex ingredients, but they should be checked against available mappings.

## Recommended Edits

- Remove `full_media_gym_streptomyces_medium` / `TOGO:M3229` from the exact merge for `TOGO:M2331` and keep it only as the 20 g/L agar concentration-variant child.
- Preserve pH 7.2 and the pH/CaCO3 preparation instruction from the Togo comments.
- Correct Togo milliliter water handling so 1000 ml Distilled water is not emitted as `1000 G_PER_L`.
- Attempt complex-component groundings for Yeast extract and Malt extract.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validators after recuration.
- Verify that the regenerated 12 g/L and 20 g/L GYM Streptomyces records stay separate and differ only by agar concentration.
- Verify that pH 7.2 and the liquid-medium CaCO3 instruction are visible on both records.

## Additional Notes

The official DSMZ Medium 65 record in `data/normalized_yaml/bacterial/gym_streptomyces_medium.yaml` is the 20 g/L agar formula and is part of a larger DSMZ 65 family; it should be compared to the `M3229` full-media child rather than to the `M2331` 12 g/L variant.
