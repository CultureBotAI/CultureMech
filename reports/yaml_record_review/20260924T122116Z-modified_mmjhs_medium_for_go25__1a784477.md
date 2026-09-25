# YAML Record Review: modified_mmjhs_medium_for_go25

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_mmjhs_medium_for_go25__1a784477.yaml
- Started UTC: 2026-09-24T12:21:16Z
- Finished UTC: 2026-09-24T12:21:16Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:002827`, `modified_mmjhs_medium_for_go25`, generated from `data/normalized_yaml/bacterial/modified_mmjhs_medium_for_go25.yaml`.
- The record represents JCM Medium J478 / MediaDive `mediadive.medium:J478`, named `MODIFIED MMJHS MEDIUM FOR GO25`.
- The generated record was compared with the maintained MediaDive normalized record, JCM `GRMD=478`, MediaDive `J478`, and the parallel TOGO `M479` import of the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- MediaDive `J478`, JCM `GRMD=478`, and TOGO `M479` all identify the same JCM recipe for Modified MMJHS Medium for GO25.
- A gitignore-independent duplicate check for the exact normalized name and JCM/MediaDive identifiers found a second maintained record, `data/normalized_yaml/bacterial/TOGO_M479_Modified_MMJHS_Medium_For_GO25.yaml`, and a second generated record, `data/merge_yaml/merged/MODIFIED_MMJHS_MEDIUM_FOR_GO25.yaml`.
- No inspected source payload gave an organism taxon for the GO25 label, so no target organism assertion was checked.

## Evidence

- JCM lists the 1 L base recipe with NaCl, phosphate salts, CaCl2 x 2 H2O, NH4Cl, NaNO3, MgSO4 x 7 H2O, MgCl2 x 6 H2O, KCl, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Fe2(SO4)3 x n H2O, H2WO4, Na2S2O3 x 5 H2O, 10 ml Trace mineral solution, 1 ml Trace vitamins, 2 g NaHCO3, 10 g sulfur powder, 1 mg resazurin, and 1 L distilled water.
- MediaDive `J478` represents the same main recipe as `Main sol. J478` with the 10 ml Trace mineral solution addition and 1 ml Trace vitamins addition preserved as solution references.
- MediaDive solution `4090` is a 1000 ml Trace mineral solution with nitrilotriacetic acid, MnSO4 x n H2O, CoSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, Na2MoO4 x 2 H2O, SrCl2 x 6 H2O, NaBr, KI, and 1000 ml distilled water.
- MediaDive solution `3861` is the 1000 ml Trace vitamins stock used at only 1 ml in the J478 main solution.
- The generated record flattens both nested stocks into the top-level ingredient list at the 1 L stock concentrations.

## Completeness

- Main inorganic salts, NaHCO3, sulfur, sodium thiosulfate pentahydrate, and resazurin are present.
- The 10 ml Trace mineral solution and 1 ml Trace vitamins additions are not preserved as first-class additions; their stock components are flattened into the top-level ingredient list.
- The generated record omits the 1 L base-water row and the two 1000 ml stock-water rows.
- The generated sulfur row keeps the source mass but grounds `Sulfur (powder)` to `CHEBI:26833`, `sulfur atom`, rather than elemental sulfur.

## Findings

- Blocker: the MediaDive import flattened the Trace mineral solution and Trace vitamins recipes into top-level ingredients at stock concentration. This changes all vitamin rows, all metals unique to the trace stock, and stock-only salts such as NaBr and KI from nested stock components into apparent direct additions to JCM 478.
- Major: the 10 ml Trace mineral solution and 1 ml Trace vitamins main-recipe additions are absent as structured ingredients, so the generated YAML cannot reconstruct the JCM formula or the MediaDive main recipe from structured fields.
- Major: source water rows are omitted for the main recipe and both embedded 1 L stocks, obscuring the recipe scopes that distinguish main-medium components from nested solutions.
- Major: `Sulfur (powder)` is grounded to `CHEBI:26833` with the label `sulfur atom`; the JCM ingredient is elemental sulfur powder, not atomic sulfur.
- Major: the same JCM 478 medium is maintained under two CultureMech IDs, `CultureMech:002827` for MediaDive and `CultureMech:009865` for TOGO, and it generates two separate merged YAML records.

## Recommended Edits

- Preserve the 10 ml Trace mineral solution and 1 ml Trace vitamins rows as solution additions or nested recipes before the merged YAML is generated.
- Keep solution-specific 1 L stock compositions under their solution contexts; do not place the Trace mineral solution or Trace vitamins components in the main ingredient list at stock strength.
- Preserve distilled-water rows for the base and stock contexts if water is in scope for structured recipes.
- Re-ground the sulfur powder row to elemental sulfur, for example `CHEBI:33403`, after confirming the preferred local grounding for source `Sulfur (powder)`.
- Merge or explicitly cross-link the MediaDive `J478` and TOGO `M479` maintained records before regeneration so JCM `GRMD=478` has a single CultureMech identity.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting nested-solution handling and sulfur grounding.
- Recompare the generated ingredient scopes with JCM `GRMD=478`, including the 10 ml Trace mineral solution and 1 ml Trace vitamins rows.
- Confirm that generated YAML no longer contains both `modified_mmjhs_medium_for_go25__1a784477.yaml` and `MODIFIED_MMJHS_MEDIUM_FOR_GO25.yaml` as separate records for the same JCM recipe.

## Additional Notes

None found.
