# YAML Record Review: 1/2 R2A Medium With 75% Artificial Seawater

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml
- Started UTC: 2026-09-21T05:26:20Z
- Finished UTC: 2026-09-21T05:27:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated canonical merge; do not edit directly |
| Generated path | data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml |
| ID | CultureMech:010168 |
| Name | 1_2_r2a_medium_with_75_artificial_seawater |
| Original name | 1/2 R2A Medium With 75% Artificial Seawater |
| Category | bacterial |
| Source grounding | TOGO:M761 / JCM_M736 |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml |

The reviewed file is the TOGO `M761` generated single-source merge. Its filename is suffixed because the direct JCM/MediaDive J736 record uses the unsuffixed generated filename.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml` | Passed: no issues found |
| Strict repository schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml --out /private/tmp/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| LinkML reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No documented focused validator exists for one generated `MediaRecipe.curation_history`; `just validate-history` targets standalone files under `history/` |

The repository-level `just` validators are currently blocked before target validation because project resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. I used the focused no-project Python 3.11 invocations above, matching the schema, strict, reference, and term validators without installing the full project environment.

## Identity and Grounding

The generated record's declared source identity is the TOGO wrapper for JCM 736:

- `id: CultureMech:010168`
- `name: 1_2_r2a_medium_with_75_artificial_seawater`
- `original_name: 1/2 R2A Medium With 75% Artificial Seawater`
- `media_term.term.id: TOGO:M761`
- `media_term.term.label: 1/2 R2A Medium With 75% Artificial Seawater`
- notes link TOGO `M761` to original source `JCM_M736` and the JCM GRMD 736 URL

The inspected TOGO `gmdb_medium_by_gmid` payload for `M761` confirms the TOGO/JCM identity, `ph: 7.2`, 250 ml distilled water in the main solution, `Artificial seawater (see below)` at 750 ml, and the same artificial-seawater stock recipe shown on the inspected JCM 736 page.

A hidden/ignored-inclusive exact search for `CultureMech:010168`, `TOGO:M761`, `M761`, and fingerprint `5b6dd332029aea048e5dd9a14edeebad240a08efb3e1ffd9076bfd34b9d75f1c` under `data/normalized_yaml`, `data/merge_yaml`, `data/raw`, `data/reference`, `data/import_tracking`, and `reports/yaml_record_review` found this maintained TOGO owner, this generated target, expected indexes and import reports, one unrelated JCM `M761` Mycoplasma source reference, the adjacent JCM sibling report's cross-reference, and no pre-existing report file for this target.

## Evidence

Supported by inspected sources:

- TOGO `M761` and JCM 736 both support the source identity and the same `1/2 R2A Medium With 75% Artificial Seawater` formulation.
- TOGO `M761` supports pH 7.2, but the record does not carry `ph_value`.
- The non-water, non-ASW ingredient amounts that are present match the JCM 736 page.
- The ASW salt amounts that are present match the 1 L ASW stock recipe before any 750 ml scaling.

Unsupported or internally incomplete:

- The top-level `Artificial seawater (see below)` ingredient is encoded as 750 `G_PER_L`, but the inspected source says 750 ml.
- The main 250 ml distilled-water volume and the ASW stock's 1 L water volume are collapsed to one top-level `Distilled water` at `251.0 G_PER_L`.
- The ASW stock is flattened into top-level ingredients at the stock's 1 L concentrations. If the record remains flat, the stock salts need to be scaled by 0.75; if the record preserves the source recipe boundary, the salts need to live under a nested local ASW solution.
- The source pH and preparation instructions are absent.
- Yeast extract, Proteose peptone No. 3, and Casamino acids lack exact ontology/MIM grounding even though exact mappings are present in the packaged label index.

## Completeness

Consequential gaps:

- `ph_value: 7.2` is missing.
- The source 250 ml main water, 750 ml ASW addition, and 1 L ASW stock water are not represented faithfully.
- The source instruction to adjust pH before autoclaving, separately autoclave ASW, cool, and combine is missing.
- The local ASW solution boundary is missing.
- Structured TOGO and JCM source provenance is absent.

Correctly empty optional slots:

- No target-organism or growth-evidence claims are present; neither the TOGO payload nor the JCM source page reports a taxon-scoped growth assay.
- No agar is present; JCM 736 describes a liquid medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The 250 ml main solution plus 750 ml ASW boundary is collapsed into invalid top-level concentration rows. | TOGO M761 and JCM 736 specify 250 ml distilled water and 750 ml artificial seawater. The record stores `Artificial seawater (see below)` as `750 G_PER_L`, merges water as `251.0 G_PER_L`, and flattens the ASW stock salts as full-strength top-level ingredients. | `data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml`; the TOGO importer/cleanup rules that flatten footnotes and merge duplicate water rows |
| major | The source pH and preparation sequence are missing. | TOGO M761 carries `ph: 7.2`; JCM 736 says to mix all components except artificial seawater, adjust pH to 7.2, autoclave, autoclave ASW separately, cool, and combine. The record has neither `ph_value` nor `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml` |
| minor | Three exact ingredient groundings are missing. | Hidden/ignored-inclusive label-index search found exact mappings for `yeast extract (BD-Difco)` to FOODON:03315426, `Proteose peptone No. 3 (BD-Difco)` to MICRO:0000180, and `Casamino acids` to FOODON:03315719, but the three ingredient rows have no `term` or `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml` |
| minor | Source provenance is free-text only. | TOGO M761 and JCM GRMD 736 are recoverable from `notes`, but the record has no structured `references` or `source_data`; the reference validator had 0 embedded checks. | `data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml`; the TOGO importer |

## Recommended Edits

1. Replace the top-level `Artificial seawater (see below) 750 G_PER_L` and flattened ASW stock salts with a recipe-local ASW solution added at 750 ml, or scale the ASW stock amounts by 0.75 and remove the aggregate row.
2. Split the merged `251.0 G_PER_L` water into the source 250 ml main-solution water and the ASW stock's own 1 L water.
3. Add `ph_value: 7.2`.
4. Add the pH-adjust/autoclave/separate-ASW/combine preparation sequence from JCM 736.
5. Add exact grounding for yeast extract, Proteose peptone No. 3, and Casamino acids from the packaged label index.
6. Add structured TOGO M761 and JCM 736 source provenance.

## Follow-up Checks

- Run strict, term, and reference validation on `data/normalized_yaml/bacterial/TOGO_M761_1_2_R2A_Medium_With_75_Artificial_Seawater.yaml`.
- If a local ASW solution is introduced, run `just validate-references-all`.
- Regenerate `data/merge_yaml/merged/` and run `just verify-merges` plus `just audit-merge-freshness`.
- Manually inspect regenerated `data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml` against both TOGO M761 and JCM 736, especially the 250 ml/750 ml solution volumes and pH/preparation fields.

## Additional Notes

- `data/import_tracking/reports/merged_duplicates.tsv` already flags the `251.0 G_PER_L` distilled-water row as a sum of distinct 250.0 and 1.0 source parts.
- The sibling direct JCM/MediaDive J736 record was reviewed separately at `reports/yaml_record_review/20260921T052616Z-1_2_r2a_medium_with_75_artificial_seawater.md`.
- A hidden/ignored-inclusive `find` for `*1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.md` under `reports/yaml_record_review` found no pre-existing report for this generated target before this file was written.
