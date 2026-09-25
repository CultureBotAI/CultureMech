# YAML Record Review: peptoclostridium_medium_betaine

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/peptoclostridium_medium_betaine.yaml`
- Started UTC: 2026-09-24T20:19:21Z
- Finished UTC: 2026-09-24T20:19:21Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/peptoclostridium_medium_betaine.yaml`, a generated `MediaRecipe` merge record.

- ID: `CultureMech:001615`
- Label: `peptoclostridium_medium_betaine`
- Category: `bacterial`
- Source term: `mediadive.medium:487`
- Source name: DSMZ Medium 487, PEPTOCLOSTRIDIUM MEDIUM (BETAINE)
- Physical state: `LIQUID`
- Maintained owners: `data/normalized_yaml/bacterial/peptoclostridium_medium_betaine.yaml`; `data/normalized_yaml/bacterial/clostridium_m1_medium.yaml`; `data/normalized_yaml/bacterial/for_dsm_5388.yaml`
- Generated from: `peptoclostridium_medium_betaine`, `clostridium_m1_medium`, `for_dsm_5388`

## Validation

- Passed: open LinkML validation of `data/merge_yaml/merged/peptoclostridium_medium_betaine.yaml` against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`; no issues found.
- Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/peptoclostridium_medium_betaine.yaml --out /private/tmp/peptoclostridium_medium_betaine.strict.tsv --workers 1 --quiet`; the TSV contained only its header, so strict validation found 0 errors.
- Passed: focused `linkml-reference-validator validate data data/merge_yaml/merged/peptoclostridium_medium_betaine.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 0 references were checked.
- Passed: focused `linkml-term-validator validate-data data/merge_yaml/merged/peptoclostridium_medium_betaine.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
- Not checked: embedded `curation_history`; the documented `just validate-history` target validates standalone `history/` YAML rather than `MediaRecipe.curation_history` embedded in generated records.

## Identity and Grounding

`mediadive.medium:487` resolves to DSMZ Medium 487, PEPTOCLOSTRIDIUM MEDIUM (BETAINE), with pH range 7.3 to 7.5 and a 1003 ml final volume. `komodo.medium:487` mirrors the same DSMZ Medium 487 recipe, while `komodo.medium:487.1` applies the same base medium to DSM 5388.

The generated record's DSMZ identity, bacterial category, liquid physical state, pH range, and main final-medium chemical groundings are coherent. Its scope is wrong for three stock solutions: Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution (10x). The generated merge topology is also stale relative to the 2026-09-13 repair that moved `for_dsm_5388` under the DSMZ parent as a `STRAIN_SPECIFIC_VARIANT`.

## Evidence

- DSMZ 487 and MediaDive 487 add 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 1 ml Wolin's vitamin solution (10x), 0.5 ml Sodium resazurin stock, and 1000 ml Distilled water to the final medium.
- DSMZ 487 and MediaDive 487 scope HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml Distilled water to the SL-10 stock.
- DSMZ 487 and MediaDive 487 scope NaOH, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and 1000 ml Distilled water to the Selenite-tungstate stock.
- DSMZ 487 and MediaDive 487 scope all vitamin rows and 1000 ml Distilled water to the Wolin's vitamin solution (10x) stock.
- The generated record lists every stock child as a top-level final-medium `ingredient`, has no `solutions` block, omits the four stock-addition rows, and omits all water rows.

## Completeness

The generated record is materially incomplete because the final recipe cannot be reconstructed without its three nested stock solutions and solvent rows. The maintained owner still has the same flattened structure.

The generated merge record is stale. After the 2026-09-13 topology repair, `data/normalized_yaml/bacterial/peptoclostridium_medium_betaine.yaml` owns two children: `clostridium_m1_medium` as a `SOURCE_DUPLICATE` and `for_dsm_5388` as a `STRAIN_SPECIFIC_VARIANT`. The generated record still merges all three sources into one record and marks `for_dsm_5388` as a `SOURCE_DUPLICATE`.

Empty optional fields are not defects.

An ignored-inclusive exact search of `data`, `src`, and `scripts` for `mediadive.medium:487`, `komodo.medium:487`, `komodo.medium:487.1`, `CultureMech:001615`, `CultureMech:005610`, `DSMZ_Medium487`, `peptoclostridium_medium_betaine`, `clostridium_m1_medium`, and `for_dsm_5388` found the three maintained owners, this generated merge record, import diagnostics flagging stock-scale concentrations, and the September topology repair script.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Three stock solutions are flattened into direct final-medium ingredients and the stock additions are missing. | DSMZ 487 adds SL-10, Selenite-tungstate, and Wolin's vitamin solution as 1 ml final-medium additions. The generated record emits their internal HCl, trace metals, selenite/tungstate, and vitamin rows at top level and has no `solutions` block. | `data/normalized_yaml/bacterial/peptoclostridium_medium_betaine.yaml`; mirror the structural repair into `data/normalized_yaml/bacterial/clostridium_m1_medium.yaml` and `data/normalized_yaml/bacterial/for_dsm_5388.yaml` as needed. |
| Major | Required water rows are absent and stock preparation text is scoped to the final medium. | DSMZ 487 lists 1000 ml final Distilled water, 990 ml SL-10 water, 1000 ml Selenite-tungstate water, and 1000 ml Wolin vitamin stock water. The generated record omits all water rows and makes the SL-10 FeCl2/HCl preparation a top-level `DISSOLVE` step. | `data/normalized_yaml/bacterial/peptoclostridium_medium_betaine.yaml` |
| Major | The generated merge still treats the DSM 5388 child as a source duplicate. | The maintained parent now links `for_dsm_5388` as a `STRAIN_SPECIFIC_VARIANT`; the generated record still has `for_dsm_5388` in `merged_from`, `synonyms`, and a `SOURCE_DUPLICATE` `parent_media` link. | `data/normalized_yaml/bacterial/for_dsm_5388.yaml` is already linked as a strain-specific child; regenerate the merge output after the stock-scope fixes. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/peptoclostridium_medium_betaine.yaml`, keep the DSMZ 487 final rows as direct ingredients and add the missing final 1000 ml Distilled water row.
2. Add scoped `solutions` for 1 ml/L Trace element solution SL-10, 1 ml/L Selenite-tungstate solution, and 1 ml/L Wolin's vitamin solution (10x); move the stock child ingredients and stock water rows into those solutions.
3. Represent the 0.5 ml Sodium resazurin stock as a solution addition instead of only a calculated top-level g/L row if stock identity should be retained.
4. Apply the same structural source repair to `data/normalized_yaml/bacterial/clostridium_m1_medium.yaml` and `data/normalized_yaml/bacterial/for_dsm_5388.yaml` so duplicate and variant comparisons are not based on the old flattened signature.
5. Regenerate `data/merge_yaml/merged/peptoclostridium_medium_betaine.yaml` so only `clostridium_m1_medium` remains a `SOURCE_DUPLICATE` and `for_dsm_5388` remains a `STRAIN_SPECIFIC_VARIANT`.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on all three maintained inputs, then regenerate `data/merge_yaml/merged/peptoclostridium_medium_betaine.yaml` and rerun the same focused validators on the generated record.
- Manually compare the regenerated DSMZ parent against the DSMZ 487 PDF and MediaDive 487 REST output, with special attention to the 1003 ml final volume and the three 1 ml stock additions.
- Confirm the regenerated merge output no longer lists `for_dsm_5388` in `merged_from`.

## Additional Notes

`data/import_tracking/reports/concentration_plausibility.tsv` already flags `FeCl2 x 4 H2O` and `Pyridoxine hydrochloride` as stock-scale rows in all three maintained inputs.
