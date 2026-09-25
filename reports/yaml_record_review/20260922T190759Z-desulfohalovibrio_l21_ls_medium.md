# YAML Record Review: desulfohalovibrio_l21_ls_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfohalovibrio_l21_ls_medium.yaml
- Started UTC: 2026-09-22T19:07:48Z
- Finished UTC: 2026-09-22T19:07:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfohalovibrio_l21_ls_medium.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owner | `data/normalized_yaml/bacterial/desulfohalovibrio_l21_ls_medium.yaml` and the MediaDive importer that produced it |
| Class | `MediaRecipe` |
| ID | `CultureMech:001000` |
| Label | `desulfohalovibrio_l21_ls_medium` |
| Original label | `DESULFOHALOVIBRIO (L21 LS) MEDIUM` |
| Source identity | DSMZ / MediaDive medium 1526c |
| Merge lineage | `merge_recipes.py` merged one source record, `desulfohalovibrio_l21_ls_medium.yaml`, into fingerprint `02852fe382decda368d9919a03c37931b28d4eb43f1fce025900ed051520ffcd` |

I read the full generated record and confirmed with a gitignore-independent `find` search that the only maintained normalized owner with this filename is `data/normalized_yaml/bacterial/desulfohalovibrio_l21_ls_medium.yaml`.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfohalovibrio_l21_ls_medium.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfohalovibrio_l21_ls_medium.yaml --out /private/tmp/desulfohalovibrio_l21_ls_medium.strict.tsv --workers 1 --quiet` | Passed; TSV contained only the header row |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfohalovibrio_l21_ls_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfohalovibrio_l21_ls_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The record identity is correct. `CultureMech:001000`, `desulfohalovibrio_l21_ls_medium`, `mediadive.medium:1526c`, and the original DSMZ label all resolve to DSMZ / MediaDive medium 1526c, and the inspected MediaDive REST payload and DSMZ PDF both identify 1526c as the L21 LS medium for Desulfohalovibrio.

The top-level medium is correctly classified as a bacterial, complex, undefined, liquid medium with a final pH range of 7.3-7.5. The category and physical-state fields do not conflict with the inspected DSMZ formulation.

The record is not correctly grounded at the formulation level. DSMZ 1526c contains a main solution that calls for two stock additions, 10 ml of Modified Wolin's mineral solution and 1 ml of Wolin's vitamin solution (10x). The generated record has no `solutions:` block and instead serializes the stock recipes as top-level final-medium ingredients.

## Evidence

The source provenance is recoverable. The generated `notes` field points to the DSMZ medium PDF, and the `media_term` preserves `mediadive.medium:1526c`.

The inspected DSMZ PDF and MediaDive REST payload support the main direct rows for NaCl, MgSO4 x 7 H2O, KCl, Na2S2O3 x 5 H2O, NH4Cl, CaCl2 x 2 H2O, K2HPO4, BD Bacto yeast extract, 0.1% sodium resazurin, Na2CO3, Na-pyruvate, Na2S x 9 H2O, and distilled water.

The same sources support the preparation text about sparging the base medium with an 80:20 N2/CO2 mixture, dispensing under that atmosphere, autoclaving, adding pyruvate, vitamins, sulfide, and carbonate from sterile anoxic stocks, and adjusting the complete medium to pH 7.3-7.5 before use.

The source does not support the current flattened evidence model for the two stocks:

- `Nitrilotriacetic acid` through `Na2WO4 x 2 H2O` are the per-liter recipe for Modified Wolin's mineral solution. DSMZ 1526c adds 10 ml of that stock to the main recipe; it does not add those g/L and mg/L rows directly to the final medium.
- `Biotin` through `(DL)-alpha-Lipoic acid` are the per-liter recipe for Wolin's vitamin solution (10x). DSMZ 1526c adds 1 ml of that stock to the main recipe; it does not add the vitamin stock concentrations directly to the final medium.
- The generated NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O rows sum the direct main-solution amount and the corresponding stock-solution amount, producing `61.0`, `9.0`, and `0.5` g/L rows that DSMZ 1526c does not state as direct additions.

## Completeness

The generated record is consequentially incomplete because the two solution additions are absent. A gitignore-independent search of the target file for top-level `solutions:`, `references:`, and `target_organisms:` found no matches.

The empty `target_organisms` and `references` slots are not defects for this generated DSMZ source record: the DSMZ recipe gives a formulation and recovery link, not strain-level growth evidence. The missing `solutions:` block is a defect because those stock additions are needed to make the formulation chemically and procedurally reproducible.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The two DSMZ stock solutions were flattened into the final medium instead of represented as 10 ml and 1 ml solution additions. | DSMZ / MediaDive 1526c lists the main solution with 10 ml Modified Wolin's mineral solution and 1 ml Wolin's vitamin solution (10x); their stock recipes are printed separately. The generated record has no `solutions:` block and emits every stock component as a top-level ingredient. | `data/normalized_yaml/bacterial/desulfohalovibrio_l21_ls_medium.yaml`; reusable repair belongs in the MediaDive import path that maps REST `solutions[].recipe` and nested `solution_id` rows into `SolutionRecipe` references. |
| Major | Duplicate-salt cleanup summed rows from different preparation scopes. | The generated NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O entries are annotated as sums of `60.0;1.0`, `6.0;3.0`, and `0.4;0.1`. Those smaller rows come from the separate Modified Wolin's mineral solution recipe, not the final main solution. | `data/normalized_yaml/bacterial/desulfohalovibrio_l21_ls_medium.yaml`; the merge or import cleanup must avoid collapsing ingredients across a parent medium and stock solution boundary. |
| Major | The mineral-stock preparation step is attached to the final medium. | The final generated step that dissolves nitrilotriacetic acid first and adjusts the mineral stock to pH 6.5 then 7.0 is the preparation procedure for Modified Wolin's mineral solution, not a third top-level step after the L21 LS inoculum note. | `data/normalized_yaml/bacterial/desulfohalovibrio_l21_ls_medium.yaml`; the MediaDive step import should keep solution-scoped steps on the corresponding stock solution. |

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/desulfohalovibrio_l21_ls_medium.yaml` by restoring the main medium as a recipe with 10 ml Modified Wolin's mineral solution and 1 ml Wolin's vitamin solution (10x) references instead of flattened stock components.
2. Preserve the two stocks as nested `SolutionRecipe` objects or references with their own 1000 ml recipes, including the Modified Wolin mineral stock preparation text.
3. Undo the cross-scope duplicate sums so the main direct rows remain at DSMZ amounts and any repeated NaCl, MgSO4 x 7 H2O, or CaCl2 x 2 H2O entries inside the mineral stock remain scoped to that stock.
4. Add enough source evidence or provenance on the normalized record to distinguish DSMZ main-solution rows from MediaDive solution rows after regeneration.
5. Regenerate `data/merge_yaml/merged/desulfohalovibrio_l21_ls_medium.yaml` from the normalized source instead of editing the generated merge by hand.

## Follow-up Checks

1. Rerun the open schema, strict schema, term, and reference validators on the maintained normalized record and the regenerated merged record.
2. Rerun `merge_recipes.py` or the repository merge target and verify that the merged output contains solution references rather than flattened Wolin stock rows.
3. Manually compare the regenerated record against DSMZ / MediaDive 1526c and confirm the main rows, two stock addition volumes, two stock recipes, and solution-scoped preparation step all remain in their DSMZ scopes.
4. Recheck `data/import_tracking/reports/merged_duplicates.tsv` and confirm this record no longer reports `DIFFERING_PARTS` for NaCl, MgSO4 x 7 H2O, or CaCl2 x 2 H2O.

## Additional Notes

- MediaDive's REST endpoint for `1526c` was available and matched the DSMZ PDF for the main recipe, solution IDs 241 and 5980, and the pH range.
- `find` and `rg --no-ignore --hidden` were used for absence-sensitive checks, so ignored files under `reports/` and generated data were included where relevant.
