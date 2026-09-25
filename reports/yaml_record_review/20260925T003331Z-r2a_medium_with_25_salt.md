# YAML Record Review: R2A Medium With 25% Salt

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r2a_medium_with_25_salt.yaml
- Started UTC: 2026-09-25T00:33:31Z
- Finished UTC: 2026-09-25T00:34:37Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Generated record | data/merge_yaml/merged/r2a_medium_with_25_salt.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1341_R2A_Medium_With_25_Salt.yaml |
| Stable ID | CultureMech:007877 |
| Name | r2a_medium_with_25_salt |
| Original name | R2A Medium With 25% Salt |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source grounding | TOGO:M1341, original JCM_M1247 |
| Merge fingerprint | 9b9d630d39771104109663227705f13bdb813d8a73d4592fdbe63a4aab985182 |
| Merged from | TOGO_M1341_R2A_Medium_With_25_Salt |

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r2a_medium_with_25_salt.yaml` | Passed; exited 0 with no diagnostics. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/r2a_medium_with_25_salt.yaml --out /private/tmp/r2a_medium_with_25_salt.strict.tsv --workers 1 --quiet` | Passed. `/private/tmp/r2a_medium_with_25_salt.strict.tsv` had one line, the header only, so 0 strict errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/r2a_medium_with_25_salt.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused check reported 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/r2a_medium_with_25_salt.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes TOGO M1341, which mirrors JCM Medium 1247, R2A MEDIUM WITH 25% SALT. Its label, `LIQUID` state, R2A base ingredients, and high-metal flag all point at the intended high-salt R2A variant.

The generated formula does not preserve the stock boundary in JCM 1247. JCM puts 833 ml of a `30% Seawater solution` into the main recipe and defines that solution separately by adding NaCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, KCl, CaCl2 x 2 H2O, NaBr, and NaHCO3 to distilled water and bringing the stock to 1.0 L. The generated record has an empty `solutions` entry and also flattens every stock salt into the top-level medium.

## Evidence

- Supported: JCM 1247 and TOGO M1341 support the R2A base amounts: 0.5 g each yeast extract, proteose peptone No. 3, casamino acids, glucose, and soluble starch; 0.3 g each sodium pyruvate and K2HPO4; and 0.05 g MgSO4 x 7 H2O.
- Supported: JCM 1247 and TOGO M1341 support 833 ml 30% seawater solution plus 167 ml distilled water in the top-level medium.
- Supported: JCM 1247 supports pH 7.5.
- Unsupported by flattening: the 30% seawater stock salts and stock make-up water are solution components, not top-level medium ingredients.
- Unsupported by unit: the 833 ml seawater stock and 167 ml distilled water top-level rows are stored as `833 G_PER_L` and `168.0 G_PER_L`; the water quantity was also summed with the stock make-up water.
- Unsupported by omission: TOGO M1341 exposes pH 7.5, but the generated CultureMech record has no `ph_value`.

## Completeness

The current generated record is not complete enough for the JCM formulation because the nested 30% seawater solution is empty and the salt chemistry is flattened into the wrong layer. The `30% Seawater solution` object must carry the NaCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, KCl, CaCl2 x 2 H2O, NaBr, NaHCO3, and 1 L stock make-up volume, while the top-level medium must reference only 833 ml of that stock.

The ignored-inclusive exact search for `TOGO:M1341`, `togomedium.org/medium/M1341`, `JCM_M1247`, and `GRMD=1247` covered `data/normalized_yaml`, `data/merge_yaml`, `scripts`, and `src`. It found this TOGO M1341 owner/generated record and a separate direct JCM J1247 owner/generated record at `data/normalized_yaml/bacterial/r2a_medium_with_25_salt.yaml` and `data/merge_yaml/merged/r2a_medium_with_25_salt__a6f5c04b.yaml`. That direct import has the same source and also flattens the stock.

Empty optional fields are not otherwise defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The 30% seawater stock is empty and flattened into top-level ingredients. | JCM 1247 lists `30% Seawater solution (see below)` as 833 ml, then defines the stock separately; the generated `solutions` entry has `composition: []`, and NaCl, MgCl2 x 6 H2O, 61 g/L MgSO4 x 7 H2O, KCl, CaCl2 x 2 H2O, NaBr, and NaHCO3 appear as top-level medium ingredients. | data/normalized_yaml/bacterial/TOGO_M1341_R2A_Medium_With_25_Salt.yaml |
| Major | Top-level water and MgSO4 x 7 H2O concentrations were summed across the main recipe and stock recipe. | The source has 167 ml top-level distilled water plus 1 L stock make-up water, and 0.05 g top-level MgSO4 x 7 H2O plus 61 g in the stock; the generated record has `168.0 G_PER_L` distilled water and `61.05 G_PER_L` MgSO4 x 7 H2O. | data/normalized_yaml/bacterial/TOGO_M1341_R2A_Medium_With_25_Salt.yaml |
| Major | pH 7.5 was lost from the TOGO-derived record. | JCM 1247 states `Adjust pH to 7.5`; the direct JCM owner has `ph_value: 7.5`, but the TOGO M1341 owner and generated record do not. | data/normalized_yaml/bacterial/TOGO_M1341_R2A_Medium_With_25_Salt.yaml |
| Major | The direct JCM J1247 and TOGO M1341 records are unreconciled duplicates of the same source medium. | The exact ignored-inclusive search found both source owners and both generated records pointing at JCM GRMD 1247. | JCM J1247 and TOGO M1341 duplicate merge handling |

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/TOGO_M1341_R2A_Medium_With_25_Salt.yaml` to keep the main JCM 1247 recipe and the 30% seawater stock as separate layers.
2. Represent the top-level medium with 833 ml of the 30% seawater stock, 167 ml distilled water, the R2A base dry ingredients, and pH 7.5.
3. Move NaCl, MgCl2 x 6 H2O, 61 g MgSO4 x 7 H2O, KCl, CaCl2 x 2 H2O, NaBr, NaHCO3, and the 1 L stock make-up volume into the nested 30% seawater solution.
4. Merge, retire, or repair `data/normalized_yaml/bacterial/r2a_medium_with_25_salt.yaml` so the direct JCM and TOGO records for GRMD 1247 are no longer independent flattened copies of the same stock recipe.
5. Regenerate merged YAML and indexes so the reviewed TOGO M1341 generated record carries the repair or disappears into a reconciled JCM 1247 output.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated high-salt R2A record.
- Run an ignored-inclusive exact search for `TOGO:M1341`, `JCM_M1247`, and `GRMD=1247` under `data/normalized_yaml` and `data/merge_yaml` to confirm the TOGO and direct JCM source records were intentionally reconciled.
- Manually inspect the regenerated YAML and verify that top-level MgSO4 x 7 H2O remains 0.05 g/L, 61 g MgSO4 x 7 H2O remains inside the 30% seawater stock, and pH 7.5 is explicit.

## Additional Notes

None found.
