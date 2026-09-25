# YAML Record Review: glucose_salt_medium_k

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glucose_salt_medium_k.yaml
- Started UTC: 2026-09-23T06:45:16Z
- Finished UTC: 2026-09-23T06:46:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Stale generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:007123` |
| Name | `glucose_salt_medium_k` |
| Original name | `'''Glucose salt (Medium K` |
| Category | `bacterial` |
| Media term | `MEDIADB:228` |
| Maintained parent | `data/normalized_yaml/bacterial/glucose_salt_medium_k.yaml` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glucose_salt_medium_k.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glucose_salt_medium_k.yaml --out /private/tmp/glucose_salt_medium_k.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glucose_salt_medium_k.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glucose_salt_medium_k.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This record denotes MediaDB medium 228, `Glucose salt (medium k); schaechter et al`. A gitignore-independent exact search for `MEDIADB:228`, `Medium ID: 228`, and `glucose_salt_medium_k` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only the maintained parent, this generated merge, and normalized indexes.

The generated merge is stale for the MediaDB SQL parenthesis repair. The maintained parent has `original_name: Glucose salt (Medium K); Schaechter et al` and the same value under `media_term.term.label`; the generated record still has the truncated `'''Glucose salt (Medium K` in both places.

Ingredient identity is broadly aligned with the MediaDB source labels. Sodium ammonium phosphate is ungrounded because the MediaDB tab-delimited ChEBI column is empty for that compound.

## Evidence

The live MediaDB HTML page and tab-delimited view support all six stored millimolar concentrations:

| Ingredient | Generated mM |
|---|---:|
| D-Glucose | 11.1012 |
| Citrate | 5.20497 |
| Dibasic sodium phosphate | 28.0899 |
| Potassium chloride | 9.92605 |
| Magnesium sulfate | 0.405729 |
| Sodium ammonium phosphate | 8.32187 |

The source page lists Schaechter et al. 1958 as the only source and Salmonella enterica Typhimurium LT2 as the only linked growth organism. The generated import history instead says `Reference: Mazumdar et al. (2014) PLOS One`, and no MediaDB growth organism is represented under `target_organisms`.

The MediaDB source does not state a pH value, filtration pore size, or heat-sensitivity warning. The three generated preparation steps are generic importer text rather than source-backed steps.

## Completeness

The generated record is complete for MediaDB 228's six concentration rows, but stale for the medium label and incomplete for source-specific literature and growth metadata.

Empty optional fields such as `references` and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record is stale and still has a parenthesis-truncated medium label already fixed in the maintained parent. | The maintained parent restored `Glucose salt (Medium K); Schaechter et al` on August 31, 2026; the generated merge still has `'''Glucose salt (Medium K` and an August 6, 2026 merge timestamp. | Regenerate `data/merge_yaml/merged/glucose_salt_medium_k.yaml` from `data/normalized_yaml/bacterial/glucose_salt_medium_k.yaml`. |
| Major | The generated preparation steps are not source-backed and include a placeholder pH instruction. | MediaDB 228 exposes the concentration table, one organism link, and one source link, but no inspected MediaDB page states 0.22 um filtration or a pH adjustment for this recipe. | MediaDB importer or `data/normalized_yaml/bacterial/glucose_salt_medium_k.yaml`. |
| Minor | The import history cites the wrong paper for MediaDB 228. | MediaDB 228 lists Schaechter et al. 1958 as its source; the import history says Mazumdar et al. (2014) PLOS One. | MediaDB importer history construction or the maintained parent. |
| Minor | MediaDB growth-organism links are absent. | MediaDB 228 lists Salmonella enterica Typhimurium LT2 and growth-data record 452; the generated recipe has no `target_organisms`. | MediaDB importer if growth data are in scope for MediaDB records. |

## Recommended Edits

1. Regenerate this merged record from the maintained parent so the August 2026 MediaDB name repair propagates.
2. Remove the generic MediaDB preparation steps from the maintained parent, or replace them with source-backed protocol text if Schaechter et al. supplies a protocol.
3. Correct the import history to cite Schaechter et al. 1958 for MediaDB 228.
4. Decide whether MediaDB growth-data records should populate `target_organisms`; if yes, import the Salmonella enterica Typhimurium LT2 link from MediaDB 228.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated merged record.
- Re-fetch the MediaDB 228 HTML and tab-delimited pages and verify all six millimolar concentrations and the full medium label.
- Re-run the exact gitignore-independent search for `MEDIADB:228`, `Medium ID: 228`, and `glucose_salt_medium_k` across `data/normalized_yaml/` and `data/merge_yaml/merged/`.

## Additional Notes

MediaDB marks this recipe as not minimal, but the six-component formulation is chemically defined; `medium_type: DEFINED` and `composition_type: DEFINED` are therefore reasonable.
