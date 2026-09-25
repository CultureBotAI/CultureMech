# YAML Record Review: tepidibacillus_decaturensis_medium__8959e5e1

- Repository: CultureMech
- Record: data/merge_yaml/merged/tepidibacillus_decaturensis_medium__8959e5e1.yaml
- Started UTC: 2026-09-25T09:19:11Z
- Finished UTC: 2026-09-25T09:20:12Z
- Verdict: needs curation

## Target

Generated merged MediaRecipe `CultureMech:002315`, `tepidibacillus_decaturensis_medium`, grounded to `mediadive.medium:J1142` / JCM Medium 1142.

## Validation

- LinkML schema validation passed.
- Strict validation passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- Reference validation passed: 1 file validated, 0 reference checks, all validations passed.
- Term validation passed.
- Embedded `curation_history` was not checked because the standalone history validator targets files under `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

- JCM `GRMD=1142` is live and serves `TEPIDIBACILLUS DECATURENSIS MEDIUM`.
- MediaDive `J1142` currently resolves to status 200, count 1, source `JCM`, name `TEPIDIBACILLUS DECATURENSIS MEDIUM`, and the JCM `GRMD=1142` source URL.
- TOGO `M1224` identifies the same JCM recipe as `original_media_id: JCM_M1142` with the JCM `GRMD=1142` source URL.
- An exact `J1142` / `GRMD=1142` / `tepidibacillus_decaturensis_medium` search scoped to `data/merge_yaml/merged` and `data/normalized_yaml/bacterial` with ignored files included found this generated record, its normalized MediaDive source, a MediaDive split-out `Main sol. J1142` solution, the TOGO `M1224` normalized duplicate, and the TOGO-generated duplicate.

## Evidence

- JCM `GRMD=1142` and MediaDive `J1142` agree on a main 1040 ml recipe containing 0.08 g `CaCl2 x 2 H2O`, 0.2 g `MgCl2 x 6 H2O`, 10 g NaCl, 1 g KCl, 1 g NH4Cl, 1 g PIPES, 0.5 g yeast extract, 1 mg resazurin, and 1 L distilled water.
- The same main recipe adds 1 ml FeCl2 solution, 1 ml trace element solution, 1 ml trace vitamins, 1 ml selenite-tungstate solution, and 5 ml phosphate buffer.
- JCM then instructs cooling under an `N2-CO2` 80:20 gas mixture, adding 2 g NaHCO3 and 0.031 g `L-Cysteine HCl x H2O`, autoclaving in culture vessels, and then adding 10 ml 1.0 M glucose, 20 ml 0.25 M ferric citrate at pH 7.0, and 0.5 ml 5% `Na2S x 9 H2O` per liter.
- MediaDive keeps FeCl2 solution, trace element solution, trace vitamins, selenite-tungstate solution, and phosphate buffer as distinct nested solutions rather than final-medium solutes.
- TOGO `M1224` preserves the same recipe as a JCM import and maps the referenced FeCl2, trace-element, vitamin, and selenite-tungstate stocks to TOGO media `M180`, `M190`, and `M431`.

## Completeness

- The direct base compounds and the JCM preparation sequence are present.
- The target has no `ph_value`, matching the absence of an explicit final pH on the live JCM page and in the MediaDive `J1142` medium object.
- The nested FeCl2, trace-element, trace-vitamin, selenite-tungstate, and phosphate-buffer recipes are flattened into final top-level ingredients.
- The source-equivalent TOGO import remains split out in `data/merge_yaml/merged/TEPIDIBACILLUS_DECATURENSIS_MEDIUM.yaml`.

## Findings

- The MediaDive/JCM branch collapses every nested solution into final top-level `G_PER_L` rows at stock strength. The 1 ml trace-vitamin addition should not become 0.002 G_PER_L biotin, 0.002 G_PER_L folic acid, 0.01 G_PER_L pyridoxine hydrochloride, and the rest of the stock vitamin recipe in the final medium.
- The 5 ml phosphate-buffer addition is expanded as 12.5 G_PER_L KH2PO4 and 20 G_PER_L K2HPO4. Those are the stock phosphate-buffer recipe values, not the final-medium concentrations after 5 ml are added.
- The late 10 ml 1.0 M glucose, 20 ml 0.25 M ferric citrate, and 0.5 ml 5% sodium sulfide additions are represented as 10, 20, and 0.5 `G_PER_L` values, respectively. The source quantities are liquid stock volumes with concentration attributes, not gram masses.
- The TOGO `M1224` duplicate was not merged into the JCM/MediaDive target even though it points to the same JCM `GRMD=1142` source.
- The TOGO-generated duplicate contains seven empty `Unknown solution` entries with `G_PER_L` units and non-ASCII GMO gas labels inherited from TOGO.

## Recommended Edits

- Fix the MediaDive/JCM import or merge expansion so the referenced FeCl2, trace-element, trace-vitamin, selenite-tungstate, phosphate-buffer, glucose, ferric-citrate, and sodium-sulfide stocks stay modeled as stock additions instead of flattened final solutes.
- Do not hand-edit `data/merge_yaml/merged/tepidibacillus_decaturensis_medium__8959e5e1.yaml`; repair `data/normalized_yaml/bacterial/tepidibacillus_decaturensis_medium.yaml` or the generation path, then regenerate this file.
- Merge the source-equivalent TOGO `M1224` record into the same `CultureMech` record by recognizing the shared `JCM_M1142` / `GRMD=1142` grounding.
- Correct the TOGO import's empty cross-reference solutions and unit handling if the TOGO branch is retained as corroborating source evidence.

## Follow-up Checks

- After importer or merge fixes, rerun schema, strict, reference, and term validation on the regenerated merged record.
- Re-run an exact duplicate search for `J1142`, `JCM_M1142`, `TOGO:M1224`, and `GRMD=1142` with ignored files included.
- Verify the regenerated record keeps stock preparations nested and does not expose stock recipe concentrations as final-medium `G_PER_L` rows.
- Verify the TOGO duplicate is gone or merged into the same `CultureMech` record.

## Additional Notes

None found
