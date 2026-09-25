# YAML Record Review: Bordet-Gengou agar (supplemented with 15% sheep's blood)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml
- Started UTC: 2026-09-21T23:16:56Z
- Finished UTC: 2026-09-21T23:17:38Z
- Verdict: needs curation

## Target

- Reviewed generated merged record `data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml`.
- Target class: `MediaRecipe`
- Stable ID: `CultureMech:009393`
- Name and source label: `bordet_gengou_agar_supplemented_with_15_sheep_s_blood` / Bordet-Gengou agar supplemented with 15% sheep blood
- Source grounding: `TOGO:M2850`
- Immediate maintained owner: `data/normalized_yaml/bacterial/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml`
- Merge status: single-source merge from `bordet_gengou_agar_supplemented_with_15_sheep_s_blood` with fingerprint `2374f922267ec1d3aeb98012c9f9efc7753b94ed891e79b876c3375d6931df1e`

This is a derived Layer 4 record. The current normalized TOGO owner already has the supported source repair; this generated merge needs to be regenerated from it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml --out /private/tmp/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator found 0 record-level reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the only output was the known `pkg_resources` warning from `eutils`. |
| Embedded `curation_history` | Not checked: this repository documents `just validate-history` for standalone history files, and no focused embedded `MediaRecipe.curation_history` validator is exposed for one merged record. |

The direct `just validate-schema`, `just validate-strict`, and `just validate-terms` wrappers were not rerun for this one-record report because the project environment currently fails while trying to build `llvmlite==0.46.0` under Python 3.13. The table above uses the same focused validators through an offline Python 3.11 no-project environment.

## Identity and Grounding

- The generated record's `TOGO:M2850` grounding matches the live TOGO payload for Bordet-Gengou agar supplemented with 15% sheep blood.
- The live TOGO payload lists 15% sheep blood and 1 L Bordet-Gengou agar, and its source comment states that strains were grown for 3 days at 35 C.
- A gitignore-independent exact search for `TOGO:M2850`, `M2850`, `CultureMech:009393`, fingerprint `2374f922267ec1d3aeb98012c9f9efc7753b94ed891e79b876c3375d6931df1e`, `bordet_gengou_agar_supplemented_with_15_sheep_s_blood`, and `15% sheep` covered `data`, `src`, and `scripts`. It found the active normalized owner, the generated merge and indexes, and import diagnostics; it did not find a second active owner for `TOGO:M2850`.
- The prepared Bordet-Gengou agar base is correctly left as an opaque product in the repaired normalized owner because M2850 does not spell out the underlying base formula.

## Evidence

The source text supports the normalized owner, not the stale generated merge:

- The normalized owner records `Sheep blood` at 15 `PERCENT_V_V`; the generated merge still has the stale 15 `PERCENT_W_V`.
- The normalized owner records `Bordet-Gengou agar` at 1000 `ML_PER_L`; the generated merge still has the stale 1 `G_PER_L`.
- The normalized owner now records `temperature_value: 35.0`, a TOGO M2850 reference, ingredient `source` annotations, and notes that keep the base opaque.

The inspected source does not support:

- treating the prepared Bordet-Gengou agar base as a mass concentration;
- treating sheep blood as weight/volume instead of volume/volume;
- expanding the Bordet-Gengou agar base into a more detailed commercial or ATCC Medium 35 recipe.

## Completeness

- Required schema shape is complete enough to validate, but the generated record is stale relative to the normalized owner and is missing the structured 1 L base, 15% v/v blood supplement, temperature, reference, and source annotations.
- Empty optional pH and sterilization fields are acceptable for M2850; the inspected TOGO payload does not provide them.
- Empty optional organism growth evidence is acceptable here. The source comment says "strains" grew on this medium but the TOGO payload does not preserve recoverable strain names.
- No duplicate active owner for `TOGO:M2850` was found by the exact, gitignore-independent search over `data`, `src`, and `scripts` described above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and still has the wrong base and blood units. | The generated record has 1 `G_PER_L` Bordet-Gengou agar and 15 `PERCENT_W_V` sheep blood. The repaired normalized owner has 1000 `ML_PER_L` prepared agar and 15 `PERCENT_V_V` sheep blood. | Regenerate `data/merge_yaml/merged/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml` from `data/normalized_yaml/bacterial/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml`. |

## Recommended Edits

1. Regenerate the merged corpus so this generated record receives the September 7 TOGO M2850 repair.

## Follow-up Checks

- Confirm the regenerated merge keeps `Bordet-Gengou agar` at 1000 `ML_PER_L` and sheep blood at 15 `PERCENT_V_V`.
- Rerun focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/bordet_gengou_agar_supplemented_with_15_sheep_s_blood.yaml` if the normalized owner changes.
- Run `just verify-merges` and `just audit-merge-freshness` after merge regeneration.
- Re-run the exact ignored-file-inclusive search for `TOGO:M2850`, `M2850`, `CultureMech:009393`, fingerprint `2374f922267ec1d3aeb98012c9f9efc7753b94ed891e79b876c3375d6931df1e`, and `bordet_gengou_agar_supplemented_with_15_sheep_s_blood` under `data`, `src`, and `scripts` after regeneration to confirm no duplicate owner was introduced.

## Additional Notes

- The exact gitignore-independent search included ignored files and found no other active `TOGO:M2850` owner.
- This record should not be auto-expanded from the ATCC Medium 35 Bordet-Gengou Agar formulation. M2850 says only `Bordet-Gengou agar` and does not cite the detailed ATCC recipe.
