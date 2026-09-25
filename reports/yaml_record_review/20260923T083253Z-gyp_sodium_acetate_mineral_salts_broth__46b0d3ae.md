# YAML Record Review: GYP-SODIUM ACETATE-MINERAL SALTS BROTH

- Repository: CultureMech
- Record: `data/merge_yaml/merged/gyp_sodium_acetate_mineral_salts_broth__46b0d3ae.yaml`
- Started UTC: 2026-09-23T08:32:15Z
- Finished UTC: 2026-09-23T08:32:53Z
- Verdict: pass with minor issues

## Target

Reviewed generated record `CultureMech:003035`, `gyp_sodium_acetate_mineral_salts_broth`, imported from JCM / MediaDive medium `J68`.

## Validation

- LinkML validation: passed.
- Strict validation: passed with 0 ERROR rows in `/private/tmp/gyp_sodium_acetate_mineral_salts_broth_46b0d3ae.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked: the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The record identity is coherent: the record carries `mediadive.medium:J68`, the JCM `GRMD=68` URL, and the correct JCM Medium 68 label. Exact ignored-file-inclusive search found this direct JCM parent, two split Togo imports for the same formula, and two salinity-variant children of JCM Medium 68.

The simple ingredients are grounded. Yeast extract and Bacto peptone are ungrounded complex components. The MnSO4 x n H2O row has a ChEBI grounding but no `mediaingredientmech_chebi_term`.

## Evidence

The live JCM 68 page lists 10 g Glucose, 10 g Yeast extract (BD-Difco), 10 g Bacto peptone (BD-Difco), 10 g Sodium acetate, 0.2 g MgSO4 x 7 H2O, 10 mg MnSO4 x n H2O, 10 mg FeSO4 x 7 H2O, 10 mg NaCl, and 1 L Distilled water, followed by `Adjust pH to 6.8.`

The generated direct JCM/MediaDive record correctly stores 10 g/L for the four main g-scale rows, 0.2 g/L for MgSO4 x 7 H2O, 0.01 g/L for MnSO4 x n H2O, FeSO4 x 7 H2O, and NaCl, and pH 6.8.

## Completeness

The recipe is materially complete. Relationship completeness is slightly stale: `data/normalized_yaml/bacterial/gyp_sodium_acetate_mineral_salts_broth.yaml` gained salinity-variant children for JCM Medium 69 and Togo `M61` on 2026-09-13, after the generated artifact was last merged.

## Findings

- The generated record is stale relative to its normalized parent's salinity-variant backlinks to `jcm_medium_no_69` and `togo_medium_m61`.
- The equivalent Togo `M60` import of JCM `GRMD=68` is not grouped with this direct JCM/MediaDive `J68` record.
- Yeast extract and Bacto peptone remain ungrounded. These are complex ingredients, but they should be checked against available mappings.
- MnSO4 x n H2O lacks a `mediaingredientmech_chebi_term` even though it has a ChEBI `term`.

## Recommended Edits

- Regenerate this record from the current normalized JCM parent so the salinity-variant children are visible.
- Reconcile Togo `M60` with this direct JCM record after repairing the Togo milligram unit conversion.
- Attempt complex-component groundings for Yeast extract and Bacto peptone, and backfill a MediaIngredientMech/ChEBI link for MnSO4 x n H2O if appropriate.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validators after regeneration.
- Recompare regenerated ingredient rows against JCM `GRMD=68`, especially the three 10 mg mineral rows.

## Additional Notes

None found.
