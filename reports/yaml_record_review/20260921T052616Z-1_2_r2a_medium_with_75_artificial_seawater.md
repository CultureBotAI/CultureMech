# YAML Record Review: 1/2 R2A MEDIUM WITH 75% ARTIFICIAL SEAWATER

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml
- Started UTC: 2026-09-21T05:25:15Z
- Finished UTC: 2026-09-21T05:26:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated canonical merge; do not edit directly |
| Generated path | data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml |
| ID | CultureMech:003079 |
| Name | 1_2_r2a_medium_with_75_artificial_seawater |
| Original name | 1/2 R2A MEDIUM WITH 75% ARTIFICIAL SEAWATER |
| Category | bacterial |
| Source grounding | JCM Medium J736 via `mediadive.medium:J736` |
| Maintained owner | data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml |

The reviewed file is the generated single-source merge of the direct JCM/MediaDive J736 owner.

## Validation

| Check | Command | Result |
|---|---|---|
| Open-schema LinkML validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml` | Passed: no issues found |
| Strict repository schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml --out /private/tmp/1_2_r2a_medium_with_75_artificial_seawater.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| LinkML reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No documented focused validator exists for one generated `MediaRecipe.curation_history`; `just validate-history` targets standalone files under `history/` |

The repository-level `just` validators are currently blocked before target validation because project resolution attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools. I used the focused no-project Python 3.11 invocations above, matching the schema, strict, reference, and term validators without installing the full project environment.

## Identity and Grounding

The generated record's declared identity agrees with the inspected source:

- `id: CultureMech:003079`
- `name: 1_2_r2a_medium_with_75_artificial_seawater`
- `original_name: 1/2 R2A MEDIUM WITH 75% ARTIFICIAL SEAWATER`
- `media_term.term.id: mediadive.medium:J736`
- `media_term.term.label: 1/2 R2A MEDIUM WITH 75% ARTIFICIAL SEAWATER`
- notes link to `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=736`

The inspected JCM 736 page confirms the JCM number, medium label, pH 7.2, 250 ml distilled water in the main portion, and 750 ml artificial seawater prepared separately.

A hidden/ignored-inclusive exact search for `CultureMech:003079`, `mediadive.medium:J736`, `JCM, ID: J736`, `GRMD=736`, and fingerprint `ee844d0977658b03b16a211e356588b66850aeddad1812ddb364f5f4a94345a4` under `data/normalized_yaml`, `data/merge_yaml`, `data/raw`, `data/reference`, `data/import_tracking`, and `reports/yaml_record_review` found one maintained owner, this generated target, expected indexes and import reports, related records that cite JCM 736 as a reused artificial-seawater formulation, and no pre-existing review report for this target.

## Evidence

Supported by inspected sources:

- JCM 736 supports the eight non-ASW ingredients at the recorded gram amounts: yeast extract, Proteose peptone No. 3, Casamino acids, glucose, soluble starch, sodium pyruvate, K2HPO4, and MgSO4.7H2O.
- JCM 736 supports the 1 L artificial-seawater formula recorded in the target: NaCl 23.5 g, MgCl2.6H2O 4.9 g, Na2SO4 3.9 g, CaCl2.2H2O 1.1 g, KCl 0.66 g, NaHCO3 0.19 g, KBr 0.096 g, H3BO3 0.026 g, SrCl2.6H2O 0.024 g, NaF 0.003 g, and distilled water 1 L.
- JCM 736 supports `ph_value: 7.2`.

Unsupported or internally incomplete:

- JCM 736 specifies 250 ml distilled water in the main solution and 750 ml artificial seawater added after separate autoclaving. The record drops both volume terms and flattens the 1 L ASW composition into top-level ingredients at stock concentration.
- If the target is intended to publish final-medium amounts only, the ASW salts should be scaled by 0.75; if it is intended to preserve the source solution boundary, they should be nested under a local ASW solution.
- The preparation evidence is only partially represented: the record says `Adjust pH to 7.2` but omits the source's separate autoclaving and post-cooling combine sequence.
- Yeast extract, Proteose peptone No. 3, and Casamino acids lack exact ontology/MIM grounding even though exact mappings are present in the packaged label index.

## Completeness

Consequential gaps:

- The 250 ml main-solution water and 750 ml ASW addition are absent.
- The local ASW solution boundary is absent.
- Separate autoclaving and post-cooling combination steps are absent.
- Structured JCM source provenance is absent; JCM is only in free-text `notes`.

Correctly empty optional slots:

- No target-organism or growth-evidence claims are present; JCM 736 is a recipe page and does not report a taxon-scoped growth assay.
- No agar is present; JCM 736 describes a liquid medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The record flattened the 1 L artificial-seawater stock into top-level ingredient concentrations and lost the 750 ml dilution boundary. | JCM 736 says to mix 250 ml distilled water with 750 ml artificial seawater prepared from a separate 1 L recipe. The record has neither `Distilled water` nor `Artificial seawater`; its ASW salts are stored at the 1 L stock amounts. | `data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml`; the JCM/MediaDive importer if solution nesting is flattened there |
| major | Source preparation is materially incomplete. | JCM 736 instructs to mix all components except artificial seawater, adjust pH to 7.2, autoclave, separately autoclave ASW, cool, and combine the two solutions. The record only has one `ADJUST_PH` step. | `data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml` |
| minor | Three exact ingredient groundings are missing. | Hidden/ignored-inclusive label-index search found exact mappings for `yeast extract` to FOODON:03315426, `Proteose peptone No. 3 (BD-Difco)` to MICRO:0000180, and `Casamino acids` to FOODON:03315719, but the three ingredient rows have no `term` or `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml` |
| minor | Source provenance is free-text only. | The JCM 736 URL is recoverable from `notes`, but the record has no structured `references` or `source_data`; the reference validator had 0 embedded checks. | `data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml`; the JCM/MediaDive importer |

## Recommended Edits

1. Preserve the JCM 736 250 ml main solution plus 750 ml ASW boundary: either add a nested local ASW solution with the inspected 1 L recipe, or scale every ASW salt by 0.75 before storing final-medium amounts.
2. Add the source 250 ml distilled-water amount or an equivalent final-volume representation.
3. Expand `preparation_steps` so the record says to mix non-ASW components, adjust to pH 7.2, autoclave, autoclave ASW separately, cool, and then combine.
4. Add exact grounding for yeast extract, Proteose peptone No. 3, and Casamino acids from the packaged label index.
5. Add structured JCM 736 source provenance.

## Follow-up Checks

- Run strict, term, and reference validation on `data/normalized_yaml/bacterial/1_2_r2a_medium_with_75_artificial_seawater.yaml`.
- If a nested ASW solution is added, run `just validate-references-all` to verify the recipe-local solution reference.
- Regenerate `data/merge_yaml/merged/` and run `just verify-merges` plus `just audit-merge-freshness`.
- Manually inspect the regenerated `data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater.yaml` against JCM 736, with special attention to whether ASW salts are stored as stock or scaled final-medium amounts.

## Additional Notes

- The sibling TOGO M761 generated record at `data/merge_yaml/merged/1_2_r2a_medium_with_75_artificial_seawater__5b6dd332.yaml` should be reviewed independently because it has a distinct TOGO source owner.
- A hidden/ignored-inclusive `find` for `*1_2_r2a_medium_with_75_artificial_seawater.md` under `reports/yaml_record_review` found no pre-existing report for this generated target before this file was written.
