# YAML Record Review: blood_agar_base_bab_broth_or_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/blood_agar_base_bab_broth_or_agar__59b823d6.yaml
- Started UTC: 2026-09-21T22:27:10Z
- Finished UTC: 2026-09-21T22:28:04Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/blood_agar_base_bab_broth_or_agar__59b823d6.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:008806` |
| Name | `blood_agar_base_bab_broth_or_agar` |
| Original name | `Blood Agar Base (BAB) broth or agar` |
| Source identity | `TOGO:M2216`, TOGO Medium M2216 |
| Category | `bacterial` |
| Physical state | `SOLID_AGAR` |
| Merge fingerprint | `59b823d6bea0887a3dd4ff9d6d4bbc868a9382af2a3484e3737dbc418328a4c5` |
| Merged from | `blood_agar_base_bab_broth_or_agar` |
| Maintained owner | `data/normalized_yaml/bacterial/blood_agar_base_bab_broth_or_agar.yaml` |
| Generated status | Derived merge product; future fixes belong in `data/normalized_yaml/bacterial/blood_agar_base_bab_broth_or_agar.yaml` or merge regeneration, not in this generated YAML. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/blood_agar_base_bab_broth_or_agar__59b823d6.yaml` | Passed, `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/blood_agar_base_bab_broth_or_agar__59b823d6.yaml --out /private/tmp/blood_agar_base_bab_broth_or_agar__59b823d6.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/blood_agar_base_bab_broth_or_agar__59b823d6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. The generated record has no structured `references` to check. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/blood_agar_base_bab_broth_or_agar__59b823d6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a non-fatal `eutils` `pkg_resources` warning. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone files under `history/`. |

`just validate-schema`, `just validate-strict`, and `just validate-terms` were not used directly because the project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation starts. The no-project Python 3.11 commands above are the same focused checks run without installing the project dependency set.

## Identity and Grounding

- `CultureMech:008806`, `name: blood_agar_base_bab_broth_or_agar`, `media_term.term.id: TOGO:M2216`, and `physical_state: SOLID_AGAR` agree with the TOGO M2216 agar source identity.
- The live TOGO M2216 API identifies the recipe as `Blood Agar Base (BAB) broth or agar`, has no upstream `src_url`, states `pH 7.3 +/- 0.2`, and includes the same base formulation as TOGO M2217 plus 15 g agar.
- The generated and maintained TOGO M2216 records retain the imported `1 G_PER_L` water artifact and omit the source pH.
- The active TOGO M2217 broth sibling exists as `CultureMech:008807`; the records are not linked even though the formulae differ only by the M2216 agar addition.

## Evidence

| Claim | Review |
|---|---|
| TOGO source identity | Supported by the live TOGO M2216 API. |
| Agar composition | Partially supported. TOGO lists sodium chloride, agar, meat extract, and peptone at 5 g, 15 g, 10 g, and 10 g respectively; the record captures these amounts as g/L. |
| Distilled water amount | Incorrect. TOGO lists 1 L distilled water, but the YAML stores `Distilled water` as `1 G_PER_L`. |
| pH | Missing. TOGO states `7.3 +/- 0.2`, but the record has neither `ph_value` nor `ph_range`. |
| Source provenance | Incomplete. The live TOGO API has an empty `src_url`, and the YAML has no structured reference or discussion explaining that no original paper or provider page was resolved. |
| Broth sibling | Incomplete. The active M2217 broth sibling exists separately with the same slug and no agar row but is not linked as the broth parent or liquid variant. |

## Completeness

- Consequentially missing fields: pH, structured `references`, a discussion or quality flag for missing upstream provenance, and a relationship to the M2217 broth sibling.
- The source does not state target organisms, incubation temperature, incubation duration, storage conditions, or preparation steps beyond the plain formulation. Those empty optional fields are not defects.
- Exact ignored-file-inclusive searches for `CultureMech:008806`, `TOGO:M2216`, `togomedium.org/medium/M2216`, and `Blood_Agar_Base_BAB_broth_or_agar` over `data/normalized_yaml`, `data/merge_yaml/merged`, the registry/catalog TSVs, `scripts`, `tests`, `reports/yaml_record_review`, and `history` found the active M2216 owner, the active M2217 sibling, their registry/catalog/by-source index rows, this generated merge, and the M2217 generated merge.
- No existing `*-blood_agar_base_bab_broth_or_agar__59b823d6.md` report was found under ignored `reports/yaml_record_review/` before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner for a fix |
|---|---|---|---|
| Major | The water row has the wrong dimension. | TOGO M2216 lists 1 L distilled water; the generated and normalized rows store `1 G_PER_L`, which is a mass concentration. | Correct `data/normalized_yaml/bacterial/blood_agar_base_bab_broth_or_agar.yaml`, then regenerate. |
| Major | Source pH is missing. | The live TOGO API reports `pH 7.3 +/- 0.2`; the record has no pH field. | Add pH 7.3 +/- 0.2 to the normalized owner. |
| Major | Upstream provenance is unresolved and unflagged. | TOGO M2216 has an empty `src_url`, and the record stores no structured `references` or discussion of the missing primary/provider source. | Add a TOGO reference and a concrete discussion or quality flag for unresolved original provenance. |
| Major | The agar and broth sibling records are unlinked. | The exact ignored-file-inclusive search found active M2216 agar and M2217 broth owners with the same Blood Agar Base formula, except the M2216 owner adds 15 g agar. Neither owner links the other as a variant. | Add a parent/child variant relationship between `blood_agar_base_bab_broth_or_agar.yaml` and `TOGO_M2217_Blood_Agar_Base_BAB_broth_or_agar.yaml`. |

## Recommended Edits

1. Change distilled water from `1 G_PER_L` to an explicit 1 L quantity in `data/normalized_yaml/bacterial/blood_agar_base_bab_broth_or_agar.yaml`.
2. Add the TOGO pH 7.3 +/- 0.2 value.
3. Add structured TOGO M2216 `references` and flag the missing upstream `src_url` as an unresolved provenance gap.
4. Link TOGO M2216 and the M2217 broth sibling as a broth/agar variant pair.
5. Regenerate `data/merge_yaml/merged/` after the normalized owner is corrected.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validation on the normalized owner and regenerated merge.
- Rerun `just validate-media-variant-links` after adding the broth/agar sibling relationship.
- Rerun `just verify-merges` and inspect both Blood Agar Base generated siblings to confirm the water unit and sibling links are fresh.

## Additional Notes

- This was a read-only review. I did not edit normalized YAML, generated merge YAML, generated pages, GitHub issues, or PR state.
- The M2217 broth sibling was reviewed separately in `reports/yaml_record_review/20260921T222529Z-blood_agar_base_bab_broth_or_agar.md`.
