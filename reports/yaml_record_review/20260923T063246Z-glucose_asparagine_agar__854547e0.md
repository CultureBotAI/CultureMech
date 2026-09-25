# YAML Record Review: glucose_asparagine_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glucose_asparagine_agar__854547e0.yaml
- Started UTC: 2026-09-23T06:30:52Z
- Finished UTC: 2026-09-23T06:32:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:009707` |
| Name | `glucose_asparagine_agar` |
| Original name | `Glucose-Asparagine Agar` |
| Category | `bacterial` |
| Media term | `TOGO:M32` |
| Source | Togo Medium M32, originally JCM `JCM_M40` / JCM `GRMD=40` |
| Maintained parent | `data/normalized_yaml/bacterial/TOGO_M32_Glucose-Asparagine_Agar.yaml` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glucose_asparagine_agar__854547e0.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glucose_asparagine_agar__854547e0.yaml --out /private/tmp/glucose_asparagine_agar__854547e0.strict.tsv --workers 1 --quiet` | Passed; TSV had only the header row and 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glucose_asparagine_agar__854547e0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glucose_asparagine_agar__854547e0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This record denotes Togo M32, a Togo import of JCM medium 40, `GLUCOSE-ASPARAGINE AGAR`. The identity itself is correct, but it is not de-duplicated with the separate direct JCM normalized record for the same JCM `GRMD=40`.

A gitignore-independent exact search for `TOGO:M32`, `JCM_M40`, `GRMD=40`, and `TOGO_M32_Glucose-Asparagine_Agar` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found this Togo parent and generated record, plus `data/normalized_yaml/bacterial/JCM_J40_GLUCOSE-ASPARAGINE_AGAR.yaml` and its generated counterpart `data/merge_yaml/merged/Glucose_Asparagine_Agar.yaml`.

The ingredient groundings match the intended source ingredients: water, dipotassium hydrogen phosphate, glucose, L-asparagine, and agar. The display string `L--Asparagine` is a Togo import artifact; the CHEBI grounding correctly points to L-asparagine.

## Evidence

JCM `GRMD=40` lists glucose 10.0 g, L-asparagine 0.5 g, K2HPO4 0.5 g, agar 15.0 g, and distilled water 1.0 L, followed by an instruction to adjust pH to 6.8-7.0. Togo M32 mirrors the same five components and exposes `meta.ph` as `6.8-7.0`.

The generated Togo record preserves the four non-water masses, but it has three source-level divergences:

- Distilled water is represented as `value: '1'` plus `unit: G_PER_L`; the source unit is 1 L, not 1 g/l.
- The source pH range and JCM pH-adjustment instruction are absent.
- The record is classified as `medium_type: COMPLEX` and `composition_type: UNDEFINED` even though the direct JCM import of the same source is `DEFINED` / `DEFINED` and the formula contains only defined salts, glucose, L-asparagine, agar, and water.

The separate direct-JCM generated record captures pH 6.9 and the preparation step, but omits the 1 L water row. It therefore did not merge with the Togo branch.

## Completeness

This generated record is complete for the four dry ingredient quantities, source accession, and Togo GMO role/property annotations stored in ingredient notes.

It is incomplete for final volume and pH, and it is a duplicate of the direct JCM `GRMD=40` record that should not remain as a separate generated medium after the Togo water conversion is fixed.

Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects here.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Togo import converted `Distilled water 1 L` into `1 G_PER_L`, creating a physically wrong ingredient concentration and a fingerprint that cannot merge with the direct JCM record. | Togo M32 and the JCM `GRMD=40` table both give distilled water as 1 L; the generated Togo record has `Distilled water` at `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M32_Glucose-Asparagine_Agar.yaml` or the Togo importer. |
| Major | The Togo and direct-JCM records for the same JCM `GRMD=40` source are split into two generated media. | The no-ignore exact search found the Togo branch at `glucose_asparagine_agar__854547e0.yaml` and the direct JCM branch at `Glucose_Asparagine_Agar.yaml`. Both point to `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=40`. | Togo import normalization and `scripts/merge_recipes.py` duplicate matching after the water row is repaired. |
| Major | The Togo record lost the source pH range and pH-adjustment preparation step. | Togo M32 reports `ph: 6.8-7.0` and comment `Adjust pH to 6.8--7.0.`; JCM states the same preparation instruction. The generated Togo record has no `ph_value` or `preparation_steps`. | The Togo importer or normalized Togo parent. |
| Minor | The Togo branch classifies the medium as complex and undefined even though this glucose/asparagine/K2HPO4/agar formula is defined. | The direct JCM parent for the same source has `medium_type: DEFINED` and `composition_type: DEFINED`. | `data/normalized_yaml/bacterial/TOGO_M32_Glucose-Asparagine_Agar.yaml`. |
| Minor | `preferred_term: L--Asparagine` carries an import spelling artifact. | The Togo payload spells the display name with a double hyphen, while the direct JCM page and the CHEBI label use `L-asparagine`. | The Togo importer or normalized Togo parent. |

## Recommended Edits

1. Convert the Togo 1 L distilled-water row to the representation used for JCM final-volume water, or drop it consistently if water rows are intentionally excluded from direct JCM recipes.
2. Add the Togo/JCM pH range and the pH-adjustment preparation step to `TOGO_M32_Glucose-Asparagine_Agar.yaml`.
3. Reclassify the Togo parent as `DEFINED` / `DEFINED`.
4. Normalize the L-asparagine display label while keeping `CHEBI:17196`.
5. Regenerate merged records and verify the Togo M32 branch merges with `JCM_J40_GLUCOSE-ASPARAGINE_AGAR.yaml` instead of producing `glucose_asparagine_agar__854547e0.yaml`.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated direct-JCM/Togo merged record.
- Repeat the gitignore-independent exact search for `TOGO:M32`, `JCM_M40`, `GRMD=40`, and `TOGO_M32_Glucose-Asparagine_Agar` across `data/normalized_yaml/` and `data/merge_yaml/merged/` and confirm there is one generated YAML record for JCM `GRMD=40`.
- Compare the regenerated record against the live JCM `GRMD=40` page and Togo M32 API payload, checking glucose, L-asparagine, K2HPO4, agar, distilled water, and pH.

## Additional Notes

The initial in-sandbox Togo and JCM `curl` attempts failed with DNS resolution errors; both source requests succeeded after rerunning `curl -L` with network escalation.
