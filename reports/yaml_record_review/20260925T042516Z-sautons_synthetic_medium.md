# YAML Record Review: sautons_synthetic_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/sautons_synthetic_medium.yaml
- Started UTC: 2026-09-25T04:25:16Z
- Finished UTC: 2026-09-25T04:25:16Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009954`, `sautons_synthetic_medium`, from `data/merge_yaml/merged/sautons_synthetic_medium.yaml`.

The record is a single-source TOGO M55 / JCM M63 import for `Sauton's Synthetic Medium`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO Medium M55.

No duplicate merge or synonym issue was found in the generated YAML.

The live JCM GRMD page for JCM 63 currently returns `Nothing found`, but the TOGO M55 API still exposes the imported JCM M63 component list.

## Evidence

TOGO M55 lists 1 L Distilled water, 0.5 g MgSO4 x 7H2O, 0.5 g K2HPO4, 60 ml Glycerol, 50 mg Ferric ammonium citrate, 4 g L-Asparagine, 15 g Agar, 2 g Citric acid, and an NH4OH pH adjustment.

The TOGO M55 preparation comment says to adjust pH to 7.2 with NH4OH.

## Completeness

The generated record contains all named source components.

The generated record records Distilled water as 1 g/L, not 1 L.

The generated record records 60 ml Glycerol as 60 g/L.

The generated record records 50 mg Ferric ammonium citrate as 50 g/L instead of 0.05 g/L.

The generated record has `ph_value: 7.0`, no pH 7.2, and no preparation step for NH4OH adjustment.

## Findings

The TOGO importer or downstream normalization converted source volumes and milligrams to grams per liter without preserving units. The ferric-ammonium-citrate concentration is inflated 1000-fold.

The source pH is 7.2 adjusted with NH4OH, but the generated YAML says pH 7.0 and carries NH4OH only as a variable-concentration ingredient.

## Recommended Edits

Repair the TOGO M55 normalized source so Ferric ammonium citrate is 0.05 g/L and Glycerol is represented from the source 60 ml/L liquid addition.

Represent Distilled water as a 1 L solvent row or omit it consistently only if repository policy intentionally drops water rows.

Restore pH 7.2 and capture `Adjust pH to 7.2 with NH4OH` as a preparation step.

Regenerate the merge layer after repairing the normalized TOGO M55 source.

## Follow-up Checks

Confirm the regenerated record has no 50 g/L Ferric ammonium citrate row and no 60 g/L Glycerol row.

Confirm the regenerated record carries pH 7.2 and no stray pH 7.0.

Confirm the regenerated record remains a single TOGO M55 source with no new Sauton duplicate merge.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
