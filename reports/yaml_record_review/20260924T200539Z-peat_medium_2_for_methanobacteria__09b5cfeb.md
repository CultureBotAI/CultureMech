# YAML Record Review: peat_medium_2_for_methanobacteria

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/peat_medium_2_for_methanobacteria__09b5cfeb.yaml
- Started UTC: 2026-09-24T20:04:27Z
- Finished UTC: 2026-09-24T20:05:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003271 |
| Label | peat_medium_2_for_methanobacteria |
| Original label | PEAT MEDIUM 2 FOR METHANOBACTERIA |
| Category | archaea |
| Source identity | JCM Medium J924 |
| Maintained owner | data/normalized_yaml/archaea/peat_medium_2_for_methanobacteria.yaml |
| Generated review target | data/merge_yaml/merged/peat_medium_2_for_methanobacteria__09b5cfeb.yaml |

`data/merge_yaml/merged/peat_medium_2_for_methanobacteria__09b5cfeb.yaml` is a generated single-source merge from the direct JCM/MediaDive import `data/normalized_yaml/archaea/peat_medium_2_for_methanobacteria.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/peat_medium_2_for_methanobacteria__09b5cfeb.yaml` | Passed; no issues found. |
| Strict CultureMech validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/peat_medium_2_for_methanobacteria__09b5cfeb.yaml --out /private/tmp/peat_medium_2_for_methanobacteria__09b5cfeb.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/peat_medium_2_for_methanobacteria__09b5cfeb.strict.tsv` had only its header row. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/peat_medium_2_for_methanobacteria__09b5cfeb.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/peat_medium_2_for_methanobacteria__09b5cfeb.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run | Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

- `mediadive.medium:J924` resolves to JCM Medium 924, `PEAT MEDIUM 2 FOR METHANOBACTERIA`.
- The `archaea` category matches the methanobacteria/methanogen source context.
- The top-level pH is wrong: the generated direct JCM record stores `ph_value: 7.0`, but JCM 924 uses pH 7.0 only for Trace metal 2 solution and says the final completed medium should be about pH 5.7.
- The same JCM 924 recipe is imported separately through TOGO M970 in `data/normalized_yaml/archaea/TOGO_M970_Peat_Medium_2_For_Methanobacteria.yaml`; that maintained TOGO owner was repaired on 2026-09-10 with scoped stocks, 5 ml tube additions scaled to ml/L, and final pH 5.7.

## Evidence

JCM 924 supports a scoped protocol:

- Prepare the basal liter from 10 ml Major metals from JCM 923, 1 ml Trace metal 2 solution, and 1 L distilled water.
- Cool under N2-CO2, dispense 5 ml aliquots under the same gas, seal, and autoclave.
- Complete each 5 ml tube with 0.05 ml 83 mM TiNTA from JCM 923, 0.10 ml 1.0 M MES, 0.05 ml Vitamin solution from JCM 923, 0.01 ml 1% Yeast extract, 0.025 ml 50 mM Coenzyme M, 0.015 ml 10 mM Sodium acetate, and 0.05 ml 4 mM Na2S x 9H2O.
- Pressurize tubes to 70 kPa H2-CO2, stand at least 7 hr, and check final pH around 5.7.
- Prepare Trace metal 2 from 1 L Trace metal 1 solution from JCM 923 plus 37.23 g EDTA.2Na, adjusted to pH 7.0 with NaOH.

The generated direct JCM record flattens all of those scopes into one final `ingredients` list:

- It drops the final 10 ml/L Major metals, 1 ml/L Trace metal 2 solution, and 1000 ml/L distilled water rows.
- It stores Major metals, Trace metal 2, Trace metal 1, 83 mM TiNTA, and Vitamin stock interiors as final rows.
- It converts per-tube stock-addition volumes such as 0.10 ml 1.0 M MES and 0.015 ml 10 mM Sodium acetate into gram-per-liter final ingredients.
- It records the Trace metal 2 pH adjustment as the record-level `ph_value`.

## Completeness

- Consequentially incomplete: the reviewed generated record lacks structured stock scopes for Major metals, Trace metal 2, Trace metal 1, 83 mM TiNTA, Vitamin solution, 1.0 M MES, 1% Yeast extract, 50 mM Coenzyme M, 10 mM Sodium acetate, and 4 mM Na2S x 9H2O.
- Consequentially incomplete: the main distilled-water row is absent.
- Consequentially incomplete: gas handling is only free text, even though JCM 924 distinguishes N2-CO2 cooling/dispensing from 70 kPa H2-CO2 pressurization.
- Empty optional target-organism collections are not independently defective for this imported medium review.
- No required source or owner was found missing. The ignored-inclusive exact search covered `data/normalized_yaml`, `data/merge_yaml`, `data/import_tracking`, `data/culturemech_id_registry.tsv`, and `data/culturemech_recipe_catalog.tsv`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The record uses the wrong final pH. | JCM 924 adjusts Trace metal 2 solution to pH 7.0 but says the final completed medium is about pH 5.7; the generated record stores `ph_value: 7.0`. | data/normalized_yaml/archaea/peat_medium_2_for_methanobacteria.yaml |
| major | Stock and per-tube addition scopes are flattened into final ingredients. | JCM 924 gives 10 ml/L Major metals, 1 ml/L Trace metal 2, and several 0.015-0.10 ml additions to each 5 ml tube. The record stores stock interiors and those stock names as top-level `G_PER_L` rows. | data/normalized_yaml/archaea/peat_medium_2_for_methanobacteria.yaml; MediaDive/JCM importer |
| major | Several final concentrations are dimensionally unsupported. | Source values such as 0.10 ml of 1.0 M MES, 0.025 ml of 50 mM Coenzyme M, 7.2 ml of 1 M Tris base, and 37.23 g EDTA.2Na in Trace metal 2 belong to different stock scopes; the record stores their numeric values directly as final g/L concentrations. | data/normalized_yaml/archaea/peat_medium_2_for_methanobacteria.yaml |
| major | The direct JCM and curated TOGO imports are split even though they cite the same JCM recipe. | Ignored-inclusive exact search found repaired TOGO M970 with original source JCM_M924 and the same JCM GRMD 924 URL; it generates `data/merge_yaml/merged/PEAT_MEDIUM_2_FOR_METHANOBACTERIA.yaml` separately. | data/normalized_yaml/archaea/peat_medium_2_for_methanobacteria.yaml; data/normalized_yaml/archaea/TOGO_M970_Peat_Medium_2_For_Methanobacteria.yaml |
| minor | `TiCl3` remains ungrounded. | The generated record has no CHEBI term for `TiCl3`; the repaired TOGO M970 owner preserves the stock as `15% TiCl3 solution` with a variable concentration because the source gives only a volume. | data/normalized_yaml/archaea/peat_medium_2_for_methanobacteria.yaml |

## Recommended Edits

1. Retire or source-map `data/normalized_yaml/archaea/peat_medium_2_for_methanobacteria.yaml` into the already repaired `data/normalized_yaml/archaea/TOGO_M970_Peat_Medium_2_For_Methanobacteria.yaml`.
2. If the direct JCM owner survives, remodel it with the same scoped Major metals, Trace metal 2, TiNTA, MES, vitamin, yeast extract, Coenzyme M, acetate, and sulfide solution additions used in the repaired TOGO M970 owner.
3. Restore final `ph_value: 5.7` and keep the pH 7.0 NaOH adjustment scoped only to Trace metal 2 solution.
4. Regenerate `data/merge_yaml/merged/` so JCM 924 has one canonical generated record with final water, N2-CO2/H2-CO2 handling, and no top-level stock interiors.

## Follow-up Checks

1. Rerun open schema, strict, reference, and term validation against the regenerated JCM 924 merged record.
2. Manually compare the regenerated record against JCM GRMD 924 and confirm that every numeric value remains attached to the original liter stock, 5 ml tube, or final medium scope.
3. Confirm an ignored-inclusive exact search for `GRMD=924` no longer finds two active generated Peat Medium 2 records.
4. Confirm `data/import_tracking/reports/concentration_plausibility.tsv` no longer flags `CultureMech:003271` for stock-strength trace-metal or vitamin quantities.

## Additional Notes

- Exact ignored-inclusive searches were used while resolving the duplicate TOGO M970 import; ignored files were included.
- The repaired TOGO M970 record is a suitable structural model for future JCM 924 output because it was curated directly against TOGO M970, JCM 924, and the JCM 923 subrecipe source.
