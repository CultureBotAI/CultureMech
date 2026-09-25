# YAML Record Review: MB MEDIUM FOR METHANOBACTERIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/mb_medium_for_methanobacterium__e472b6b3.yaml`
- Started UTC: 2026-09-24T00:33:23Z
- Finished UTC: 2026-09-24T00:34:24Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/mb_medium_for_methanobacterium__e472b6b3.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:003293`
- Name: `mb_medium_for_methanobacterium`
- Original name: `MB MEDIUM FOR METHANOBACTERIUM`
- Source accession: `mediadive.medium:J945`, labeled `MB MEDIUM FOR METHANOBACTERIUM`
- Maintained owner for future fixes: `data/normalized_yaml/archaea/mb_medium_for_methanobacterium.yaml`
- Generated status: generated canonical merge of one normalized record. The generated curation history records fingerprint `e472b6b395a78f813a6e73771b7099730f4a9937b187d086cb4a43e54ce0b9e6` from `mb_medium_for_methanobacterium.yaml`.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed. `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mb_medium_for_methanobacterium__e472b6b3.yaml` exited 0 with `No issues found`. |
| Strict schema | Passed. `scripts/validate_strict.py data/merge_yaml/merged/mb_medium_for_methanobacterium__e472b6b3.yaml --out /private/tmp/mb_medium_for_methanobacterium__e472b6b3.strict.tsv --workers 1 --quiet` scanned 1 file with 0 error rows; the TSV was header-only. |
| References | Passed. `linkml-reference-validator validate data data/merge_yaml/merged/mb_medium_for_methanobacterium__e472b6b3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` exited 0 with 0 checks and no failures. |
| Terms | Passed. `linkml-term-validator validate-data data/merge_yaml/merged/mb_medium_for_methanobacterium__e472b6b3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. It emitted the expected `eutils` `pkg_resources` warning before reporting `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The generated record denotes JCM Medium 945, `MB MEDIUM FOR METHANOBACTERIUM`. Its `media_term` is `mediadive.medium:J945`, its source link is the JCM `GRMD=945` recipe page, and the live JCM page returned the same medium number and title.

The similarly named `data/normalized_yaml/archaea/TOGO_M992_MB_Medium_For_Methanobacterium.yaml` record was inspected as a source sibling. It points at `TOGO:M992` with original source `JCM_M945`, but it did not merge into this canonical file and it is not the maintained owner for this generated JCM record.

The mineral, bicarbonate, reducing-agent, gas, and vitamin names all match JCM or the MediaDive solution export closely enough to preserve the direct source identity. `MnSO4 x n H2O` is intentionally broader than a fixed hydrate, and its primary `CHEBI:86360` grounding is therefore weaker than the hydrated salts with exact CHEBI links but not enough to change the record's identity.

## Evidence

### Supported

- The basal JCM 945 table supports `KH2PO4`, `K2HPO4`, `NaCl`, `(NH4)2SO4`, `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, 10 ml trace-minerals solution, 1 mg resazurin, and 932 ml distilled water before autoclaving.
- The JCM 945 preparation text supports autoclaving the basal mixture under an `N2-CO2 (80:20, v/v)` gas atmosphere, aseptically adding 48 ml 8 percent `NaHCO3` and 10 ml trace vitamins after cooling, dispensing under `H2-CO2 (80:20, v/v)`, adding 6 ml each of anaerobic 5 percent `L-Cysteine HCl x H2O` and 5 percent `Na2S x 9 H2O`, and pressurizing inoculated vessels to 200 kPa `H2-CO2`.
- The JCM 945 page supports the Trace minerals solution as a separate 1 L stock recipe containing nitrilotriacetic acid, `MgSO4 x 7 H2O`, `MnSO4 x n H2O`, `FeSO4 x 7 H2O`, `CoSO4 x 7 H2O`, `ZnSO4 x 7 H2O`, `CuSO4 x 5 H2O`, `H3BO3`, and `Na2MoO4 x 2 H2O`.
- JCM 945 points to JCM Medium 197 for the trace-vitamin stock. The JCM 197 page and MediaDive solution 3861 both support a 1 L Trace vitamins stock containing biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, Vitamin B12, p-aminobenzoic acid, and lipoic acid at the amounts carried by MediaDive.

### Unsupported or over-scoped

- The root record lacks `solutions:` and flattens Trace minerals solution, Trace vitamins, 8 percent `NaHCO3`, 5 percent `L-Cysteine HCl x H2O`, and 5 percent `Na2S x 9 H2O` into direct root ingredients.
- The trace-minerals ingredients are stock ingredients, not root final-medium ingredients at the stock `G_PER_L` concentrations. This also caused `MgSO4 x 7 H2O` from the basal medium and from the trace-minerals stock to be merged into one 3.118577 `G_PER_L` root ingredient.
- The 48 ml, 6 ml, and 6 ml solution additions are recorded as 48, 6, and 6 `G_PER_L` for `NaHCO3`, `L-Cysteine HCl x H2O`, and `Na2S x 9 H2O`. JCM specifies solution volumes and percent strengths, not those root gram-per-litre amounts.
- The trace-vitamin ingredients are stock ingredients from Medium 197; the final J945 recipe only adds 10 ml of that stock.
- The record-level `ph_value: 6.5` is unsupported as a final medium pH. The inspected JCM 945 page places the pH 6.5 adjustment inside the Trace minerals solution recipe, followed by a final trace-minerals pH of 7.0.

## Completeness

- A gitignore-independent exact field scan of `data/merge_yaml/merged/mb_medium_for_methanobacterium__e472b6b3.yaml`, `data/normalized_yaml/archaea/mb_medium_for_methanobacterium.yaml`, and `data/normalized_yaml/archaea/TOGO_M992_MB_Medium_For_Methanobacterium.yaml` found no top-level `solutions:`, `references:`, or `target_organisms:` slots in the generated file or its direct JCM normalized owner.
- Missing `solutions:` is consequential because every post-autoclave addition in JCM 945 is a solution addition, and two solution recipes are included or referenced by the source.
- Missing `references:` is acceptable for this JCM-derived import; the authoritative recipe page is recorded in `notes`, and there are no paper citations on the inspected JCM 945 page to transcribe.
- Missing `target_organisms:` is acceptable. The JCM medium name mentions Methanobacterium generically but the inspected page does not report a taxon-specific growth result.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock solutions and post-autoclave additions were flattened into root ingredients. | JCM and MediaDive encode trace minerals, trace vitamins, 8 percent bicarbonate, 5 percent cysteine, and 5 percent sulfide as solution additions; the generated record has no `solutions:` block and stores those stock components under root `ingredients`. | `data/normalized_yaml/archaea/mb_medium_for_methanobacterium.yaml` |
| major | Root quantities for several post-autoclave solution additions use millilitre amounts as `G_PER_L` amounts. | JCM gives 48 ml 8 percent `NaHCO3`, 6 ml 5 percent `L-Cysteine HCl x H2O`, and 6 ml 5 percent `Na2S x 9 H2O`; the record stores 48, 6, and 6 `G_PER_L`. | `data/normalized_yaml/archaea/mb_medium_for_methanobacterium.yaml` |
| major | The record-level pH comes from the Trace minerals solution, not from the final MB medium. | The only pH 6.5 instruction on the JCM 945 page is within the Trace minerals solution block and is followed by a final stock pH 7.0; the normalized record promotes 6.5 to root `ph_value`. | `data/normalized_yaml/archaea/mb_medium_for_methanobacterium.yaml` |
| minor | `MnSO4 x n H2O` has a primary CHEBI term but no `mediaingredientmech_chebi_term` mirror. | The normalized and generated records include `term: CHEBI:86360` for this ingredient but no CHEBI-keyed MediaIngredientMech link, unlike the neighboring mineral salts. | `data/normalized_yaml/archaea/mb_medium_for_methanobacterium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/archaea/mb_medium_for_methanobacterium.yaml`, re-encode JCM 945 with root ingredients for the basal table only and `solutions:` entries for Trace minerals solution, 8 percent `NaHCO3`, Trace vitamins, 5 percent `L-Cysteine HCl x H2O`, and 5 percent `Na2S x 9 H2O`.
2. Keep Trace minerals solution as its own 1 L stock recipe with the pH 6.5 and pH 7.0 preparation instructions scoped to that stock, not to root MB medium.
3. Keep Trace vitamins as the JCM 197/MediaDive 3861 1 L stock and add it to JCM 945 at 10 ml/L instead of lifting the vitamin stock strengths to root `ingredients`.
4. Move the 8 percent bicarbonate, 5 percent cysteine, and 5 percent sulfide solutions out of root `ingredients` and encode them as solution additions with their source percentages and addition volumes.
5. Add the CHEBI-keyed `mediaingredientmech_chebi_term` mirror for `MnSO4 x n H2O` only if the packaged MIM label index resolves that exact variable-hydrate label to the same checked identity.

## Follow-up Checks

- Run open schema, strict schema, reference, and term validation on the corrected normalized owner.
- Regenerate merged YAML and verify the regenerated `mb_medium_for_methanobacterium__e472b6b3.yaml` no longer has stock-only trace minerals or vitamins under root `ingredients`.
- Manually compare the regenerated root ingredients, solution additions, gas atmospheres, and trace-stock pH steps against the live JCM 945 page and JCM 197 trace-vitamin table.
- Recheck the similarly named `TOGO_M992_MB_Medium_For_Methanobacterium.yaml` after fixing the JCM owner; it is a separate import of JCM 945 with partial empty `solutions:` entries that likely needs the same stock-boundary treatment.

## Additional Notes

- The live JCM 945 page, live MediaDive REST JSON for `J945`, live JCM 197 page, live MediaDive solution `3861`, and the live TOGO M992 API response were all inspected.
- This review did not patch generated YAML, normalized YAML, or GitHub state.
