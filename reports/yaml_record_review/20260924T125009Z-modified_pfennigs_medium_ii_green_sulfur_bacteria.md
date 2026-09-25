# YAML Record Review: modified_pfennigs_medium_ii_green_sulfur_bacteria

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_pfennigs_medium_ii_green_sulfur_bacteria.yaml
- Started UTC: 2026-09-24T12:50:09Z
- Finished UTC: 2026-09-24T12:50:54Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:008358`, `modified_pfennigs_medium_ii_green_sulfur_bacteria`, generated from `data/normalized_yaml/bacterial/modified_pfennigs_medium_ii_green_sulfur_bacteria.yaml`.
- The record represents TOGO `M1790`, sourced from NBRC `NBRC_M1013`, named `Modified Pfennig's Medium II (green sulfur bacteria)`.
- The generated TOGO record was compared with TOGO `M1790` and the primary NBRC `NO=1013` page.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` exited 0 with no diagnostics.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M1790` points to NBRC `NBRC_M1013`, and NBRC `NO=1013` identifies Modified Pfennig's Medium II for green sulfur bacteria.
- A gitignore-independent exact search for the TOGO and NBRC identifiers found only one maintained YAML record, `data/normalized_yaml/bacterial/modified_pfennigs_medium_ii_green_sulfur_bacteria.yaml`, plus this generated record and index metadata.
- CoCl2 x 6 H2O and NiCl2 x 6 H2O are grounded to non-hydrate chloride labels rather than hexahydrate-specific terms.
- No inspected source payload identified a target organism for this medium.

## Evidence

- NBRC lists a basal medium with CaCl2 x 2 H2O, KH2PO4, NH4Cl, KCl, MgSO4 x 7 H2O, 1 ml Vitamin B12 0.002 percent solution, 1 ml Trace element solution SL-10B, 1.5 g NaHCO3, 0.6 g Na2S x 9 H2O, 0.5 mg Resazurin, 998 ml distilled water, and pH 6.8.
- NBRC instructs dissolving everything except Vitamin B12 and sulfide, dispensing into culture vessels, and autoclaving under an 80:20 N2/CO2 atmosphere.
- NBRC's SL-10B stock has 7.7 ml 25 percent HCl, 1.5 g FeSO4 x 7 H2O, milligram-scale ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O, and 1 L distilled water.
- NBRC's neutralized sulfide stock has 1.5 g Na2S x 9 H2O and 100 ml distilled water, is autoclaved under N2, and is pH-adjusted to about 7.3 with sterile 2 N H2SO4.

## Completeness

- Basal salts are present.
- The 1 ml Vitamin B12 and 1 ml SL-10B additions were migrated to empty `solutions` stubs with `G_PER_L` units.
- The SL-10B and neutralized sulfide stock components were flattened into the top-level ingredient list.
- NBRC's basal, SL-10B, and neutralized-sulfide water rows were merged into one `1099.0` `G_PER_L` Distilled water row.
- The final pH target, 80:20 N2/CO2 gas ratio, pH-adjustment role of Na2CO3, and stock-specific pH handling are not structurally represented.

## Findings

- Blocker: SL-10B stock ingredients are flattened at stock strength and often with milligram amounts copied as grams per liter. For example, 300 mg H3BO3 in the 1 L stock becomes `300` `G_PER_L`, 100 mg MnCl2 x 4 H2O becomes `100` `G_PER_L`, and 36 mg Na2MoO4 x 2 H2O becomes `36` `G_PER_L`.
- Blocker: basal Na2S x 9 H2O and neutralized-sulfide Na2S x 9 H2O are merged into a single `2.1` `G_PER_L` top-level row even though the 1.5 g row belongs to a 100 ml stock solution.
- Blocker: the 998 ml basal water, 1 L SL-10B water, and 100 ml sulfide-stock water rows are merged into one `1099.0` `G_PER_L` row, losing three scopes and all volume units.
- Major: Vitamin B12 0.002 percent solution and Trace element solution SL-10B are represented as empty `G_PER_L` solution stubs instead of source 1 ml additions.
- Major: the generated record creates variable `HCl`, `H2SO4`, `N2`, and gas rows from pH-adjustment and gas-handling prose while omitting the source Na2CO3 pH-adjuster.
- Minor: hydrated cobalt and nickel chlorides need hexahydrate-specific grounding.

## Recommended Edits

- Preserve Vitamin B12 solution and Trace element solution SL-10B as 1 ml additions, not empty gram-per-liter solution stubs.
- Preserve SL-10B and neutralized sulfide as scoped stock recipes and keep their waters, HCl, H2SO4, and N2 handling under the stock-specific instructions.
- Keep basal Na2S x 9 H2O separate from neutralized-sulfide Na2S x 9 H2O.
- Preserve the 998 ml basal water, 1 L SL-10B water, and 100 ml sulfide-stock water rows with their original volume contexts.
- Represent the final pH 6.8, final 80:20 N2/CO2 atmosphere, stock pH adjustment to about 7.3, and HCl/Na2CO3 pH-adjuster options in structured or parseable preparation fields.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting TOGO solution migration.
- Recompare the regenerated record against NBRC `NBRC_M1013`, including the three water scopes, both sulfide rows, SL-10B milligram units, Vitamin B12 solution, and neutralized sulfide preparation note.
- Confirm with a gitignore-independent exact identifier search that TOGO `M1790` remains represented by only one generated record.

## Additional Notes

None found.
