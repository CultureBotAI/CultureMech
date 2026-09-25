# YAML Record Review: R2A MEDIUM WITH 25% SALT

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r2a_medium_with_25_salt__a6f5c04b.yaml
- Started UTC: 2026-09-25T00:35:25Z
- Finished UTC: 2026-09-25T00:35:43Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Generated record | data/merge_yaml/merged/r2a_medium_with_25_salt__a6f5c04b.yaml |
| Maintained owner | data/normalized_yaml/bacterial/r2a_medium_with_25_salt.yaml |
| Stable ID | CultureMech:002413 |
| Name | r2a_medium_with_25_salt |
| Original name | R2A MEDIUM WITH 25% SALT |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | 7.5 |
| Source grounding | mediadive.medium:J1247, JCM Medium 1247 |
| Merge fingerprint | a6f5c04bf9419c6884561b986f7d2627a37ba8eb6d4094ab5c9b69b877846981 |
| Merged from | r2a_medium_with_25_salt |

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r2a_medium_with_25_salt__a6f5c04b.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/r2a_medium_with_25_salt__a6f5c04b.yaml --out /private/tmp/r2a_medium_with_25_salt__a6f5c04b.strict.tsv --workers 1 --quiet` | Passed. `/private/tmp/r2a_medium_with_25_salt__a6f5c04b.strict.tsv` had one line, the header only, so 0 strict errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/r2a_medium_with_25_salt__a6f5c04b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused check reported 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/r2a_medium_with_25_salt__a6f5c04b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes the correct direct JCM source, JCM Medium 1247, R2A MEDIUM WITH 25% SALT. Its source ID, pH 7.5, R2A base ingredients, and high-metal flag all identify the intended high-salt R2A variant.

The formulation is not grounded at the right structural level. JCM lists 833 ml of a nested `30% Seawater solution` plus 167 ml distilled water in the main recipe, then defines the seawater stock separately. The reviewed record flattens all stock salts into top-level ingredients and leaves only a top-level `Sea water` pseudo-ingredient with the nonsensical concentration `833 G_PER_L`.

## Evidence

- Supported: JCM 1247 supports the R2A dry base at 0.5 g each yeast extract, proteose peptone No. 3, casamino acids, glucose, and soluble starch; 0.3 g each sodium pyruvate and K2HPO4; and 0.05 g MgSO4 x 7 H2O.
- Supported: JCM 1247 supports pH 7.5.
- Unsupported by omission: JCM 1247 includes 167 ml distilled water in the main recipe; the reviewed record omits that top-level water row.
- Unsupported by unit and type: JCM 1247 includes 833 ml `30% Seawater solution (see below)`; the reviewed record stores that stock as `Sea water` at `833 G_PER_L`.
- Unsupported by flattening: the seawater stock's NaCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, KCl, CaCl2 x 2 H2O, NaBr, NaHCO3, and 1 L make-up volume belong inside the stock, not as top-level medium ingredients.

## Completeness

The reviewed direct JCM record preserves pH 7.5, unlike the TOGO duplicate, but it still loses the layered formula: it has no nested `30% Seawater solution`, no explicit 167 ml distilled-water top-level row, and no way to tell that the 61 g MgSO4 x 7 H2O row belongs to the seawater stock rather than the R2A base.

The ignored-inclusive exact search for `TOGO:M1341`, `togomedium.org/medium/M1341`, `JCM_M1247`, and `GRMD=1247` covered `data/normalized_yaml`, `data/merge_yaml`, `scripts`, and `src`. It found this direct JCM J1247 owner/generated record and the separate TOGO M1341 owner/generated record at `data/normalized_yaml/bacterial/TOGO_M1341_R2A_Medium_With_25_Salt.yaml` and `data/merge_yaml/merged/r2a_medium_with_25_salt.yaml`. They are duplicate imports of the same JCM source.

Empty optional fields are not otherwise defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The 30% seawater stock is flattened into top-level ingredients. | JCM 1247 lists the stock as 833 ml in the main recipe and gives its salt formula in a separate table; the reviewed record keeps NaCl, MgCl2 x 6 H2O, 61 g/L MgSO4 x 7 H2O, KCl, CaCl2 x 2 H2O, NaBr, and NaHCO3 as top-level ingredients. | data/normalized_yaml/bacterial/r2a_medium_with_25_salt.yaml |
| Major | The 833 ml stock and 167 ml water top-level volumes are not represented correctly. | The reviewed record stores the stock as `Sea water` at `833 G_PER_L` and omits the JCM 167 ml distilled-water row. | data/normalized_yaml/bacterial/r2a_medium_with_25_salt.yaml |
| Major | Top-level MgSO4 x 7 H2O is summed with stock MgSO4 x 7 H2O. | JCM 1247 has 0.05 g MgSO4 x 7 H2O in the R2A base and 61 g in the seawater stock; the reviewed record has one `61.05 G_PER_L` top-level row. | data/normalized_yaml/bacterial/r2a_medium_with_25_salt.yaml |
| Major | The direct JCM J1247 and TOGO M1341 records are unreconciled duplicates of the same source medium. | The exact ignored-inclusive search found both source owners and both generated records pointing at JCM GRMD 1247. | JCM J1247 and TOGO M1341 duplicate merge handling |

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/r2a_medium_with_25_salt.yaml` to represent 833 ml of the nested 30% seawater stock and 167 ml distilled water at the top level.
2. Move NaCl, MgCl2 x 6 H2O, 61 g MgSO4 x 7 H2O, KCl, CaCl2 x 2 H2O, NaBr, NaHCO3, and the 1 L stock make-up volume into a nested 30% seawater solution.
3. Keep the R2A base MgSO4 x 7 H2O row separate at 0.05 g/L.
4. Merge, retire, or repair `data/normalized_yaml/bacterial/TOGO_M1341_R2A_Medium_With_25_Salt.yaml` so TOGO M1341 and direct JCM J1247 no longer generate independent flattened records for the same source.
5. Regenerate merged YAML and indexes so the direct JCM generated record carries the stock repair.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated direct JCM 1247 record.
- Run an ignored-inclusive exact search for `TOGO:M1341`, `JCM_M1247`, and `GRMD=1247` under `data/normalized_yaml` and `data/merge_yaml` to confirm the duplicate source records were intentionally reconciled.
- Manually inspect the regenerated YAML and verify that the 30% seawater stock is nested, pH 7.5 is retained, and no stock salt appears as a top-level medium ingredient.

## Additional Notes

None found.
