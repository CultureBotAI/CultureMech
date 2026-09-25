# YAML Record Review: modified_pfennig_medium_with_acetate_and_fumarate

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_pfennig_medium_with_acetate_and_fumarate.yaml
- Started UTC: 2026-09-24T12:48:48Z
- Finished UTC: 2026-09-24T12:49:30Z
- Verdict: pass with minor issues

## Target

- Reviewed merged record `CultureMech:015833`, `modified_pfennig_medium_with_acetate_and_fumarate`, generated from `data/normalized_yaml/bacterial/JCM_J1341_MODIFIED_PFENNIG_MEDIUM_WITH_ACETATE_AND_FUMARATE.yaml`.
- The record represents JCM `GRMD=1341`, named `MODIFIED PFENNIG MEDIUM WITH ACETATE AND FUMARATE`.
- The generated record was compared with the primary JCM `GRMD=1341` recipe.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- JCM `GRMD=1341` identifies Modified Pfennig Medium with Acetate and Fumarate and the generated record points to that source.
- A gitignore-independent exact search for the JCM medium identifier found one maintained YAML record, `data/normalized_yaml/bacterial/JCM_J1341_MODIFIED_PFENNIG_MEDIUM_WITH_ACETATE_AND_FUMARATE.yaml`, plus this generated record and index metadata.
- The six solution additions are literal JCM rows and have no separate ontology grounding.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists a 920 ml basal formulation with 2.0 g NaCl, 0.2 g KH2PO4, 0.25 g NH4Cl, 0.5 g MgCl2 x 6 H2O, 0.4 g KCl, 0.4 g CaCl2 x 2 H2O, and 0.5 mg Resazurin.
- JCM instructs autoclaving under an N2-CO2 gas mixture at 80:20 by volume.
- JCM then adds 50 ml 8 percent NaHCO3 solution, 10 ml 1.0 M Sodium fumarate solution, 10 ml 1.0 M Sodium acetate solution, 10 ml Trace vitamins from JCM Medium 197, 1 ml Trace element solution from JCM Medium 899, and 6 ml 5 percent Na2S x 9 H2O solution.
- JCM instructs checking the pH at 7.0-7.2.

## Completeness

- All basal ingredient rows are present with source numeric values and units.
- All six post-autoclave solution additions are present with source milliliter units.
- The N2-CO2 80:20 gas mixture and the final pH range are preserved in preparation text.
- The Trace vitamins and Trace element solution references are present in names but not cross-linked to structured JCM 197 or JCM 899 stock recipes.

## Findings

- Minor: the N2-CO2 80:20 gas mixture is present only in prose and is not represented as a structured anaerobic gas phase.
- Minor: the final pH range, 7.0-7.2, is present only in prose and not represented in a structured pH field.
- Minor: `Trace vitamins* (see Medium No. 197 )` and `Trace element solution* (see Medium No. 899 )` preserve JCM cross-references only as display text, not as links to structured stock recipes.

## Recommended Edits

- Represent the 80:20 N2-CO2 gas mixture in a structured gas-phase field if the schema gains one.
- Add structured support for a pH range, or preserve the 7.0-7.2 range in a more parseable preparation annotation.
- Cross-link the Trace vitamins and Trace element solution rows to curated JCM 197 and JCM 899 stock recipes when stock references are supported.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after any structured gas, pH, or stock-reference edits.
- Recompare the regenerated record against JCM `GRMD=1341`, especially the six post-autoclave solution volumes and the 80:20 gas mixture.
- Confirm with a gitignore-independent exact identifier search that JCM `GRMD=1341` remains represented by only one generated record.

## Additional Notes

None found.
