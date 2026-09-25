# YAML Record Review: py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml
- Started UTC: 2026-09-24T22:08:10Z
- Finished UTC: 2026-09-24T22:08:53Z
- Verdict: needs curation

## Target

- Reviewed generated `MediaRecipe`: `data/merge_yaml/merged/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml`
- Stable ID: `CultureMech:009274`
- Label: `py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium`
- Original label: `PY-glucose (ATCC medium 1524) with 10 g glucose per liter of medium`
- Category: `bacterial`
- Source grounding: TOGO Medium M2724, `TOGO:M2724`, imported from ATCC medium 1527
- Merge provenance: generated from one normalized record, `data/normalized_yaml/bacterial/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml`
- Maintained owner path for future fixes: `data/normalized_yaml/bacterial/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml`, or the TOGO importer if regenerated normalized records would overwrite direct edits

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml` | Passed; exited 0 with `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml --out /private/tmp/py_glucose_atcc_1524.strict.tsv --workers 1 --quiet` | Passed; the TSV at `/private/tmp/py_glucose_atcc_1524.strict.tsv` had 1 header row and 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the usual `eutils` `pkg_resources` warning. |
| Embedded history | Not run | Not checked: the repository exposes `just validate-history` for standalone `history/` files, not for `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

- TOGO M2724 and the ATCC PDF identify the target as PY-glucose based on ATCC Medium 1524 with 10 g glucose per liter of medium.
- The ATCC source PDF title is `ATCC medium: 1527 PY-glucose (ATCC medium 1524) with 10 g glucose per liter of medium`; the local record preserves the recipe label but not the ATCC 1527 source number in a structured field.
- An ignored-file-inclusive search over `data/**/*.yaml` for `TOGO:M2724`, `gm_id=M2724`, `medium/M2724`, `3F8B6BDFCC2D44F88C84F6E1FE4DE6A2`, and the full local slug found only this generated record and its single normalized owner.

## Evidence

- The ATCC PDF and TOGO M2724 both support these main-medium additions: 5.0 g Bacto peptone, 5.0 g Trypticase peptone, 10.0 g yeast extract, 10.0 g glucose, 4.0 ml 0.025% aqueous resazurin, 40.0 ml Salt Solution, 10.0 ml Hemin Solution, 0.2 ml Vitamin K1 Solution, 0.5 g L-Cysteine . HCl, and 950.0 ml distilled water.
- The ATCC source supports pH 7.0, boiling all ingredients except cysteine under 80% N2, 10% H2, and 10% CO2, adding cysteine and readjusting pH if necessary, tubing anaerobically with the same gas phase, and autoclaving at 121 C for 15 minutes.
- The ATCC source supports a Salt Solution stock with 2.0 g NaCl, 1.0 g KH2PO4, 1.0 g K2HPO4, 10.0 g NaHCO3, 0.2 g CaCl2, and 0.2 g MgSO4 per 1 L water, added at 40 ml per liter of main medium.
- The ATCC source supports a Hemin Solution stock with 50.0 mg hemin and 1.0 ml N NaOH brought to 100.0 ml with distilled water, added at 10 ml per liter of main medium.
- The ATCC source supports a Vitamin K1 Solution stock with 0.15 ml vitamin K1 in 30.0 ml 95% ethanol, added at 0.2 ml per liter of main medium.

## Completeness

- Empty optional organism, growth, and literature slots are not defects for this imported ATCC/TOGO medium recipe.
- The record is not complete enough to reproduce the ATCC protocol because it flattens three stock solutions into the final medium, gives stock additions in `G_PER_L`, sums stock solvents into the main distilled-water amount, omits the final pH, and omits the ordered anaerobic preparation steps.
- The ignored-file-inclusive exact search described above found no duplicate TOGO M2724 owner elsewhere in `data`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Three milliliter stock additions are stored as gram-per-liter concentrations. | ATCC 1527 adds 40 ml Salt Solution, 10 ml Hemin Solution, and 0.2 ml Vitamin K1 Solution per liter. The generated `solutions` entries store `40`, `10`, and `0.2` as `G_PER_L`. | `data/normalized_yaml/bacterial/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml` or the TOGO importer |
| Major | Salt Solution is flattened at stock strength and loses its 40 ml/L dilution. | The source lists Salt Solution as a separate 1 L stock and adds only 40 ml of it to the final recipe. The generated final ingredients include stock-only NaCl, KH2PO4, K2HPO4, NaHCO3, CaCl2, and MgSO4 as if they were direct grams per liter. | `data/normalized_yaml/bacterial/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml` or the TOGO importer |
| Major | Hemin Solution is flattened at stock strength and loses its 10 ml/L dilution. | The source puts 50 mg hemin and 1 ml N NaOH in a 100 ml stock. The generated final ingredients list Hemin as `50 G_PER_L` and N NaOH as `1 G_PER_L`. | `data/normalized_yaml/bacterial/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml` or the TOGO importer |
| Major | Vitamin K1 Solution is flattened and its liquid volumes are treated as gram-per-liter masses. | The source stock contains 0.15 ml vitamin K1 and 30 ml 95% ethanol, and the final recipe adds only 0.2 ml of that stock. The generated final ingredients list `Vitamin K1` as `0.15 G_PER_L` and `95% Ethanol` as `30 G_PER_L`. | `data/normalized_yaml/bacterial/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml` or the TOGO importer |
| Major | Final and stock waters are merged into an unsupported `1051.0 G_PER_L` water ingredient. | The source has 950 ml distilled water in the final medium, 1 L in Salt Solution, and water up to 100 ml in Hemin Solution. The generated record merges `950.0`, `1.0`, and `100.0` as duplicate water ingredients. | `data/normalized_yaml/bacterial/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml` or the TOGO importer |
| Major | Final pH and anaerobic preparation conditions are not structured. | The source requires final pH 7.0, boiling under 80% N2, 10% H2, 10% CO2, adding cysteine, tubing with the same gas phase, and autoclaving at 121 C for 15 minutes. The generated record has variable gas ingredients but no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml` |

## Recommended Edits

1. Rework the maintained normalized record so `Salt Solution`, `Hemin Solution`, and `Vitamin K1 Solution` are represented as 40 ml/L, 10 ml/L, and 0.2 ml/L solution additions with stock-scoped compositions.
2. Move NaCl, KH2PO4, K2HPO4, NaHCO3, CaCl2, and MgSO4 into the Salt Solution stock at the source stock concentrations.
3. Move hemin, 1 ml N NaOH, and the 100 ml final stock volume into the Hemin Solution stock.
4. Move vitamin K1 and 95% ethanol into the Vitamin K1 Solution stock and preserve their milliliter source units without converting them to grams.
5. Restore 950 ml distilled water, pH 7.0, the 80% N2/10% H2/10% CO2 gas phase, and the source preparation order on the main medium.
6. Preserve the ATCC medium 1527 source number in notes or structured provenance while keeping TOGO M2724 as the imported accession.
7. Regenerate `data/merge_yaml/merged/py_glucose_atcc_medium_1524_with_10_g_glucose_per_liter_of_medium.yaml`.

## Follow-up Checks

- Re-run the schema, strict, reference, and term validators against the regenerated merged record.
- Manually compare the regenerated main-medium ingredients with the ATCC 1527 PDF and confirm that only peptone, Trypticase peptone, yeast extract, glucose, aqueous resazurin, L-Cysteine . HCl, distilled water, and the three stock references appear at top level.
- Manually compare each regenerated stock solution with the Salt Solution, Hemin Solution, and Vitamin K1 Solution sections in the ATCC source PDF.

## Additional Notes

- A broad exploratory `atcc` search was replaced with an ignored-file-inclusive exact search for TOGO M2724, the ATCC source hash, and the full local slug before ownership and absence were assessed.
