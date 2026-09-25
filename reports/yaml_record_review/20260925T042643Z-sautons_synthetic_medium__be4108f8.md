# YAML Record Review: sautons_synthetic_medium__be4108f8

- Repository: CultureMech
- Record: data/merge_yaml/merged/sautons_synthetic_medium__be4108f8.yaml
- Started UTC: 2026-09-25T04:26:43Z
- Finished UTC: 2026-09-25T04:26:43Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002986`, `sautons_synthetic_medium`, from `data/merge_yaml/merged/sautons_synthetic_medium__be4108f8.yaml`.

The record is the direct MediaDive/JCM J63 import for `SAUTON'S SYNTHETIC MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM Medium J63.

It is the same original JCM medium as TOGO M55 but remains split from the TOGO path because the two generated records carry different quantitative errors.

The live JCM GRMD page for JCM 63 currently returns `Nothing found`, but TOGO M55 still records the imported JCM M63 formula.

## Evidence

TOGO M55 lists 1 L Distilled water, 0.5 g MgSO4 x 7H2O, 0.5 g K2HPO4, 60 ml Glycerol, 50 mg Ferric ammonium citrate, 4 g L-Asparagine, 15 g Agar, 2 g Citric acid, and an NH4OH pH adjustment.

The TOGO M55 preparation comment says to adjust pH to 7.2 with NH4OH.

## Completeness

The direct generated record has the solid ingredients, Glycerol, pH 7.2, and the NH4OH adjustment step.

The 1 L Distilled water row is absent.

The 60 ml Glycerol addition is represented as 60 g/L.

Most solid ingredients are scaled down by an apparent 1.06 L final volume; for example, L-Asparagine is 3.77358 g/L instead of 4 g/L, Citric acid is 1.88679 g/L instead of 2 g/L, and Agar is 14.1509 g/L instead of 15 g/L.

## Findings

The generated MediaDive record divided solid source amounts by a final volume that includes the 60 ml Glycerol aliquot, while also storing Glycerol itself as a 60 g/L mass concentration.

Ferric ammonium citrate is near the correct 0.05 g/L source value, but it was also scaled down to 0.0471698 g/L by the same volume-normalization step.

The record is a duplicate split from TOGO M55 / JCM M63. The TOGO copy preserved the source-scale solid quantities but inflated Ferric ammonium citrate, while the direct MediaDive copy preserved the ferric mass scale but diluted most other rows.

## Recommended Edits

Repair the direct MediaDive J63 normalized source so the one-liter source formula retains 4 g L-Asparagine, 2 g Citric acid, 0.5 g K2HPO4, 0.5 g MgSO4 x 7H2O, 50 mg Ferric ammonium citrate, 60 ml Glycerol, and 15 g Agar.

Add the 1 L Distilled water row or omit it consistently only if repository policy intentionally drops water rows.

Regenerate the merge layer after both the MediaDive/JCM J63 and TOGO M55 normalized sources are repaired so they collapse into one generated Sauton's Synthetic Medium record.

## Follow-up Checks

Confirm the regenerated direct path has no 3.77358 g/L L-Asparagine, 1.88679 g/L Citric acid, 0.471698 g/L K2HPO4, or 14.1509 g/L Agar rows.

Confirm the regenerated recipe has pH 7.2 and retains the NH4OH pH-adjustment step.

Confirm only one generated `sautons_synthetic_medium` record remains after the TOGO and MediaDive paths converge.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
