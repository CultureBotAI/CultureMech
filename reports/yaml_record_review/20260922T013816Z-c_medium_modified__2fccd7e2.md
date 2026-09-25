# YAML Record Review: C Medium, Modified

- Repository: CultureMech
- Record: data/merge_yaml/merged/c_medium_modified__2fccd7e2.yaml
- Started UTC: 2026-09-22T01:38:16Z
- Finished UTC: 2026-09-22T01:38:16Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000328`, `c_medium_modified`, `C Medium, Modified`.
- Merge lineage: one source recipe on fingerprint `2fccd7e2ba1d43477516f56559c3b6ba5eaee3519ec70750f0774eff8989a4c3`.
- Authoritative owner: `data/normalized_yaml/bacterial/c_medium_modified.yaml`.
- Claimed source identity: MediaDive CCAP Medium `C20`, PDF `MR_C_Modified.pdf`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The record denotes the same CCAP C Medium, Modified source as the algae-side CCAP `C_Modified` owners.
- The record is miscategorized as `bacterial`; C Medium, Modified is a CCAP freshwater green algae recipe.
- `KNO3`, calcium nitrate tetrahydrate, magnesium sulfate heptahydrate, Tris, agar, disodium EDTA, ferric chloride hexahydrate, manganese chloride tetrahydrate, cobalt chloride hexahydrate, sodium molybdate dihydrate, thiamine hydrochloride, cyanocobalamin, and biotin are source-compatible ingredients.
- Sodium glycerophosphate and `ZnCl2 x 6 H2O` remain ungrounded.

## Evidence

- `MR_C_Modified.pdf` specifies 0.1 g `KNO3`, 0.15 g `Ca(NO3).4H2O`, 0.05 g disodium glycerophosphate, 0.04 g `MgSO4.7H2O`, 0.5 g Tris, 3 ml trace element solution, 1 ml vitamin B1, 1 ml vitamin B12, and 10 ml biotin per final liter.
- The PDF makes agar conditional: add 15 g/L Bacterial Agar for agar.
- The trace-element section is a separate 1 L stock with 0.75 g `Na2EDTA`, 97 mg `FeCl3.6H2O`, 41 mg `MnCl2.4H2O`, 5 mg `ZnCl2.6H2O`, 2 mg `CoCl2.6H2O`, and 4 mg `Na2MoO4.2H2O`.
- The vitamin sections are separate filter-sterile stocks: 0.12 g thiamine hydrochloride in 100 ml, 0.1 g cyanocobalamin in 100 ml followed by a 1:100 dilution, and 0.005 g biotin in 100 ml.

## Completeness

- The generated record includes the final mineral/base ingredients and the subordinate trace/vitamin stock components.
- Distilled water rows are missing from the final medium, trace-element stock, and vitamin stocks.
- The record has no structured CCAP or PDF references.
- The record does not preserve stock boundaries or the final-liter addition volumes for trace elements and vitamins.

## Findings

- `Na2-EDTA`, the five trace-metal rows, thiamine hydrochloride, cyanocobalamin, and biotin are stock concentrations flattened into the final medium.
- The 3 ml trace element solution, 1 ml vitamin B1, 1 ml vitamin B12, and 10 ml biotin additions are absent as final-medium ingredients.
- Agar is modeled as an unconditional 15 g/L ingredient and the whole record is `SOLID_AGAR`, but the source treats agar as optional for an agar formulation.
- The record omits the 900 ml starting water, the final 1 L water makeup, the trace-stock water, and all vitamin-stock water.
- The three filter-sterilization steps are orphaned from their vitamin stock recipes, and the vitamin B12 dilution step is not linked to a stock name.
- Sodium glycerophosphate and `ZnCl2 x 6 H2O` are ungrounded, and `Cyanocobalamine` is misspelled.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/c_medium_modified.yaml` or, preferably, consolidate it with the maintained algae-side CCAP owner under the correct category.
- Model the trace-element, vitamin B1, vitamin B12, and biotin stocks as subordinate recipes and reference them by final-medium volumes.
- Move stock component concentrations and preparation steps out of the top-level final-medium ingredient list.
- Represent agar as a conditional solid formulation rather than making the base record unconditional `SOLID_AGAR`.
- Add the missing distilled-water rows and structured CCAP/PDF provenance.
- Ground sodium glycerophosphate and resolve the source's `ZnCl2 x 6 H2O` identity or leave it explicitly ungrounded with a quality flag if no exact term is available.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Regenerate merged YAML and verify that this MediaDive C20 source no longer generates separately from CCAP `C_Modified`.
- Compare the regenerated recipe against `MR_C_Modified.pdf`, including stock volumes, optional agar, pH 7.5, 15 psi autoclaving, and all filter-sterile vitamin stock details.

## Additional Notes

- A gitignore-independent exact search for `CultureMech:000328`, `mediadive.medium:C20`, `Source: CCAP, ID: C20`, and the merge fingerprint found the active owner, generated merge, registry/index/report rows, archived references to the old `CCAP_C20_C_Medium_Modified.yaml` path, and current plausibility reports for the flattened thiamine/cyanocobalamin stock concentrations and ungrounded `ZnCl2 x 6 H2O`.
