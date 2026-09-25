# YAML Record Review: desulfosporosinus_acidiphilus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.yaml
- Started UTC: 2026-09-22T19:51:35Z
- Finished UTC: 2026-09-22T19:51:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owner | `data/normalized_yaml/bacterial/desulfosporosinus_acidiphilus_medium.yaml` |
| Related same-upstream owner | `data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml` |
| Related main-solution owner | `data/normalized_yaml/bacterial/mediadive_4652_Main_sol_J728.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:003072` |
| Label | `desulfosporosinus_acidiphilus_medium` |
| Original label | `DESULFOSPOROSINUS ACIDIPHILUS MEDIUM` |
| Source identity | MediaDive J728 / JCM Medium 728 |
| Merge lineage | `merge_recipes.py` merged `desulfosporosinus_acidiphilus_medium.yaml` into fingerprint `0c10268ad3bc791cef36eb67935fc7710c949c62aa615fc10b9423e670164050` |

I read the full generated record, its maintained normalized owner, the same-upstream TOGO M751 owner, the same-label TOGO generated record, and the MediaDive main-solution owner. A gitignore-independent exact search for the label, J728, M751, and the merge fingerprint found the MediaDive owner, TOGO owner, target generated record, same-label TOGO generated record, and the local `mediadive_4652_Main_sol_J728.yaml` stock record.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.yaml --out /private/tmp/desulfosporosinus_acidiphilus_medium__0c10268a.strict.tsv --workers 1 --quiet` | Passed; 0 errors |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The record denotes JCM Medium 728 as imported through MediaDive J728. MediaDive reports the same `DESULFOSPOROSINUS ACIDIPHILUS MEDIUM` name, pH 5.5, and `complex_medium: yes`, which supports the generated semi-defined/complex classification because yeast extract is present.

TOGO M751 also names `JCM_M728`, so `data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml` is a same-upstream duplicate that did not merge with this MediaDive record. JCM's direct `GRMD=728` endpoint returned a `Nothing found` page during this review.

Most top-level CHEBI groundings match the stock ingredients they came from, but the row scopes are wrong: HBS solution, Trace minerals, Ni-Se-W solution, 1 M ZnSO4, 10 mM FeSO4, and 1 M glycerol are source stock additions, not simple final-medium ingredients.

## Evidence

MediaDive J728 supports a 1000 ml final recipe with 20 ml HBS solution, 10 ml Trace minerals, 10 ml Ni-Se-W solution, 0.87 g K2SO4, 0.1 g yeast extract, 939 ml water, 4 ml 1 M glycerol, 10 ml 10 mM FeSO4 at pH 2.0, and 7 ml 1 M ZnSO4. Its single preparation step adjusts the base to pH 5.5 with H2SO4, autoclaves under N2, and aseptically adds the filter-sterilized stock solutions after cooling.

MediaDive also exposes the three referenced stock recipes. HBS is MgSO4 x 7H2O, K2HPO4, KCl, ammonium sulfate, sodium sulfate, calcium nitrate tetrahydrate, and water. Trace minerals is nitrilotriacetic acid, MgSO4 x 7H2O, manganese sulfate hydrate, NaCl, FeSO4 x 7H2O, CoSO4 x 7H2O, CaCl2 x 2H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, potassium aluminium sulfate, boric acid, Na2MoO4 x 2H2O, and water, with a pH 6.5 to 7.0 preparation note. Ni-Se-W is NiCl2 x 6H2O, ammonium nickel sulfate hexahydrate, Na2SeO3, Na2SeO4, Na2WO4 x 2H2O, and water.

The generated record flattens every HBS, Trace minerals, and Ni-Se-W constituent into the main `ingredients` list, then coalesces both MgSO4 x 7H2O stock rows into one `28.0 G_PER_L` row. That `28.0` value is neither a source stock concentration nor a final medium concentration; it is the sum of 25 g/L HBS MgSO4 and 3 g/L Trace minerals MgSO4.

## Completeness

The record is missing all modeled solution boundaries. It has no `solutions:` block for HBS, Trace minerals, Ni-Se-W, 1 M glycerol, 10 mM FeSO4, or 1 M ZnSO4, and it omits the stock water rows that would keep those recipes reproducible.

The empty `target_organisms` and `references` slots are not defects for this imported source recipe because MediaDive and TOGO provide formulation provenance, not primary growth-study evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | HBS, Trace minerals, and Ni-Se-W stocks are flattened into the main ingredient list. | MediaDive J728 adds 20 ml HBS, 10 ml Trace minerals, and 10 ml Ni-Se-W to the final medium; the generated target has every stock constituent at top level and no `solutions:` block. | `data/normalized_yaml/bacterial/desulfosporosinus_acidiphilus_medium.yaml` and MediaDive solution import logic. |
| Major | Distinct MgSO4 x 7H2O stock rows were summed into a false concentration. | HBS contains 25 g/L MgSO4 x 7H2O and Trace minerals contains 3 g/L MgSO4 x 7H2O. The generated target has one `28.0 G_PER_L` MgSO4 row with duplicate-merge notes, even though the source adds only 20 ml/L and 10 ml/L of those stocks. | Same normalized owner and duplicate-ingredient cleanup after flattening. |
| Major | Three post-autoclave milliliter stocks are encoded as gram-per-liter ingredients. | MediaDive J728 adds 4 ml 1 M glycerol, 10 ml 10 mM FeSO4, and 7 ml 1 M ZnSO4 after cooling. The generated target has `Glycerol`, `FeSO4`, and `ZnSO4` rows at `4`, `10`, and `7 G_PER_L`. | `data/normalized_yaml/bacterial/desulfosporosinus_acidiphilus_medium.yaml` and `data/normalized_yaml/bacterial/mediadive_4652_Main_sol_J728.yaml`. |
| Major | The same JCM 728 recipe is split across MediaDive and TOGO generated records. | MediaDive J728 and TOGO M751 both cite `GRMD=728` / `JCM_M728`, but the generated corpus contains separate `desulfosporosinus_acidiphilus_medium__0c10268a.yaml` and `DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml` records. | MediaDive and TOGO normalized owners plus merge-deduplication rules. |
| Minor | The Trace minerals preparation note is attached to the main medium instead of to that stock solution. | MediaDive scopes the nitrilotriacetic acid dissolution and pH 6.5-to-7.0 adjustment to solution 3804, `Trace minerals`; the generated step appears on the main J728 MediaRecipe. | MediaDive solution import and preparation-step placement. |

## Recommended Edits

1. Restore HBS, Trace minerals, and Ni-Se-W as structured solution additions on `data/normalized_yaml/bacterial/desulfosporosinus_acidiphilus_medium.yaml` with 20, 10, and 10 ml/L addition volumes.
2. Represent the 1 M glycerol, 10 mM FeSO4 at pH 2.0, and 1 M ZnSO4 stocks as post-autoclave solution additions instead of `G_PER_L` ingredients.
3. Prevent duplicate cleanup from summing stock-scope ingredients such as the two MgSO4 x 7H2O rows; any duplicate detection must respect solution scope.
4. Attach the Trace minerals pH-preparation note to the Trace minerals solution.
5. Merge or explicitly link TOGO M751 and MediaDive J728 before regenerating `data/merge_yaml/merged/`, so the same JCM 728 recipe does not remain split into two generated records.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on the edited MediaDive and TOGO normalized records and on regenerated merged output.
2. Compare the regenerated J728 record against the MediaDive J728 REST payload, checking the 20/10/10 ml HBS/Trace minerals/Ni-Se-W additions, the 4/10/7 ml direct stock additions, and pH 5.5.
3. Confirm there is no top-level `28.0 G_PER_L` MgSO4 row and no top-level stock-only FeSO4, ZnSO4, Ni-Se-W, HBS, or Trace minerals constituents.
4. Confirm merge regeneration leaves one JCM 728 generated record rather than separate MediaDive and TOGO fingerprints.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfosporosinus_acidiphilus_medium__0c10268a` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
