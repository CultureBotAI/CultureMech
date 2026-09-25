# YAML Record Review: modified_vy_2_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_vy_2_agar.yaml
- Started UTC: 2026-09-24T13:44:24Z
- Finished UTC: 2026-09-24T13:45:29Z
- Verdict: needs curation

## Target

Reviewed merged generated record `CultureMech:008725`, `modified_vy_2_agar`, a solid undefined bacterial recipe imported from TOGO `M2131` / NBRC `M1463`.

## Validation

The generated record passed the focused open schema validator, which reported `No issues found`.

Strict validation passed with 0 errors. The TSV output contained only its header row.

Reference validation passed. The checker executed 0 reference checks for this record.

Term validation passed. The validator emitted the known `eutils` / `pkg_resources` warning before reporting success.

Embedded `curation_history` entries were not checked: `just validate-history` validates standalone `history/` content, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The external medium identity is coherent: generated `TOGO:M2131` resolves to TOGO medium `M2131`, which in turn reports the original media id `NBRC_M1463`, the NBRC medium URL for `NO=1463`, the name `modified-VY/2-Agar`, and pH 7.2.

The generated solution identity is not coherent. The source contains a recipe-local `*Trace element solution`, but the generated record links that solution to reusable `mediadive.solution:6187`. The MediaDive solution 6187 record contains Na2-EDTA, FeCl3 x 6 H2O, MnCl2 x 4 H2O, ZnCl2 x 6 H2O, CoCl2 x 6 H2O, and Na2MoO4 x 2 H2O at concentrations unrelated to the NBRC M1463 trace stock, so it is not an identity match for this local stock.

The generated record also has ungrounded undefined or brand components `Dry yeast` and `Bacto Agar`, and ungrounded `beta-glycerophosphate-2Na`. The undefined components can remain ungrounded if no suitable structured term exists, but `beta-glycerophosphate-2Na` should be investigated for a CHEBI grounding.

## Evidence

The live NBRC medium 1463 page names the medium `modified-VY/2-Agar` and lists these final-medium additions before `Distilled water 1 L`: 5 g dry yeast, 0.2 g CaCl2 x 2 H2O, 2 g NaCl, 1.6 g MgSO4 x 7 H2O, 0.1 g yeast extract, 30 mg NaHCO3, 4 mg H3BO3, 16 mg KBr, 6 mg SrCl2, 20 mg beta-glycerophosphate-2Na, 0.2 ml trace element solution, 0.5 mg cyanocobalamin, and 15 g Bacto Agar. It also specifies pH 7.2.

The TOGO API for `M2131` returns the same final-medium composition, pH 7.2, original media id `NBRC_M1463`, and the NBRC medium 1463 source URL.

NBRC and TOGO both define the nested `*Trace element solution` as MnCl2 x 4 H2O 100 mg, CoCl2 20 mg, CuSO4 10 mg, Na2MoO4 x 2 H2O 10 mg, ZnCl2 20 mg, LiCl 5 mg, SnCl2 x 2 H2O 5 mg, KI 20 mg, Fe(III)-EDTA 8 g, and distilled water 1 L. The source states to sterilize that stock by filtration.

NBRC and TOGO also preserve a final comment to add 1 ml from a filter-sterilized stock solution containing 50 mg per 100 ml after autoclaving. This appears to define the cyanocobalamin addition, because a 1 ml aliquot of that stock contributes 0.5 mg.

## Completeness

The generated final ingredient list is not complete as a normalized final-medium recipe. It flattens the local trace stock into final ingredients, converts multiple source `mg` values into `G_PER_L` without scaling, and represents the source `0.2 ml` trace-stock addition as a `0.2 G_PER_L` solution row.

Preparation and condition metadata are incomplete. The source pH 7.2, trace-stock filtration instruction, and post-autoclave filter-sterilized stock addition are not preserved in structured fields.

The normalized owner already has a 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` curation entry that collapsed the duplicate water rows back to a single 1 L final-medium solvent. The generated merged record is stale and still sums main water plus trace-stock water into `Distilled water` at `2.0 G_PER_L`.

## Findings

1. `Distilled water` is stale in the generated merge output. The normalized owner repaired this source-local duplicate from `2.0` back to `1.0`, but `data/merge_yaml/merged/modified_vy_2_agar.yaml` still has the erroneous summed value.

2. Several source milligram final-medium additions were promoted to gram-per-liter quantities without the 1000-fold conversion: `H3BO3`, `NaHCO3`, `cyanocobalamin`, `KBr`, `SrCl2`, and `beta-glycerophosphate-2Na`.

3. The `*Trace element solution` stock was flattened into final-medium ingredients at stock recipe amounts. The stock components belong under a nested local solution and then the final medium should add only `0.2 ml` of that stock per 1 L.

4. The generated solution row links the local NBRC trace stock to `mediadive.solution:6187`, whose composition is a different trace solution and is not a valid identity for this record.

5. The source pH 7.2 and sterilization instructions are absent from the generated record, including the instruction to filter sterilize the trace element solution and the post-autoclave filter-sterilized stock addition.

6. `beta-glycerophosphate-2Na` lacks structured ontology grounding.

## Recommended Edits

Regenerate the merged artifact from the normalized owner after the 2026-09-02 duplicate-water repair, or apply the same repair in the merge generator so stock solvent rows are never summed into final-medium water.

Convert every final-medium `mg` source amount to `G_PER_L` before serialization: `NaHCO3` 0.03, `H3BO3` 0.004, `KBr` 0.016, `SrCl2` 0.006, `beta-glycerophosphate-2Na` 0.02, and `cyanocobalamin` 0.0005.

Keep the NBRC `*Trace element solution` as a recipe-local stock with its own composition, mark it as filter sterilized, and reference it from the final recipe with the source amount `0.2 ml` per liter.

Remove the `mediadive.solution:6187` link from this local stock unless a source-independent reconciliation can prove equivalence, which the inspected compositions do not support.

Record pH 7.2 and the cyanocobalamin stock addition from the NBRC comment.

Investigate a CHEBI grounding for `beta-glycerophosphate-2Na`.

## Follow-up Checks

After editing `data/normalized_yaml/bacterial/modified_vy_2_agar.yaml` or the TOGO merge/import logic, regenerate the merged YAML and rerun open schema, strict, reference, and term validation.

Recompare the regenerated final recipe against both TOGO `M2131` and NBRC `M1463`: the main recipe should have 1 L water, pH 7.2, 0.2 ml local trace stock, and no stock-only trace constituents as final ingredients.

Check sibling records that contain `mediadive.solution:6187` for name-only trace-solution matches to unrelated local stocks.

## Additional Notes

An exact, ignored-file-inclusive search for `TOGO:M2131`, `M2131`, `NBRC_M1463`, and the NBRC `NO=1463` URL under `data/normalized_yaml` and `data/merge_yaml/merged` found this normalized owner and this generated merge record, but no duplicate generated sibling for the same TOGO source.
