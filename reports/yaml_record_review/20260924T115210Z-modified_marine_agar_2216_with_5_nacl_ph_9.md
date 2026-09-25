# YAML Record Review: Modified Marine Agar 2216 With 5% NaCl (pH 9)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9.yaml
- Started UTC: 2026-09-24T11:52:10Z
- Finished UTC: 2026-09-24T11:52:10Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:007807` |
| Name | `modified_marine_agar_2216_with_5_nacl_ph_9` |
| Source identity | `TOGO:M1274`, originally JCM `JCM_M1189` |
| Category | `bacterial` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_marine_agar_2216_with_5_nacl_ph_9.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one TOGO-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9.yaml --out /private/tmp/modified_marine_agar_2216_with_5_nacl_ph_9.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes TOGO M1274 / JCM 1189, "Modified Marine Agar 2216 With 5% NaCl (pH 9)". Its generated identity is correct, but the generated artifact predates the maintained record's 2026-09-11 source repair.

The current maintained YAML now has pH 9.0, 990.0 ml/L water, 10.0 ml/L Trace vitamins with the TOGO M190/JCM 197 composition, and a 10% Na2CO3 stock used for pH adjustment. The generated artifact still has no `ph_value`, has water at `990 G_PER_L`, and keeps Trace vitamins plus Na2CO3 solution as empty `Unknown solution` rows.

## Evidence

JCM 1189, TOGO M1274, and MediaDive J1189 all support the same main formulation:

| Main-medium item | Amount |
|---|---|
| Marine agar 2216 (BD-Difco) | 55.1 g |
| Casitone (BD-Difco) | 1.0 g |
| Soytone (BD-Difco) or Phytone peptone (BD-BBL) | 1.0 g |
| Malt extract (BD-Difco) | 1.0 g |
| NaCl | 50.0 g |
| Trace vitamins | 10.0 ml |
| Distilled water | 990.0 ml |

JCM instructs adjustment to pH 9.0 with sterilized 10% Na2CO3 solution. TOGO M1274 represents that sodium carbonate stock as a 10% solution and links Trace vitamins to M190; MediaDive J1189 exposes a `Trace vitamins` solution with the same ten vitamin rows plus 1000 ml water.

## Completeness

The generated YAML is incomplete because it has lost the pH, structured trace-vitamin stock, 10% sodium carbonate stock, repaired water unit, FOODON grounding on malt extract, and curated source references that are already present in the maintained TOGO M1274 YAML.

No target organism claims were expected from the inspected JCM, TOGO, or MediaDive medium records.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record is stale relative to the repaired TOGO M1274 normalized record. | The maintained source was repaired on 2026-09-11 after the 2026-08-06 merge run; the generated file lacks the source pH, corrected water unit, stock compositions, references, roles, and 10% Na2CO3 representation now present upstream. | Regenerate `data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9.yaml` from `data/normalized_yaml/bacterial/modified_marine_agar_2216_with_5_nacl_ph_9.yaml`. |
| major | Trace vitamins and sodium carbonate solution are empty unknown stocks in the generated YAML. | JCM 1189 adds 10 ml Trace vitamins and adjusts pH with sterilized 10% Na2CO3 solution; the generated `solutions` entries have `composition: []` and `name: Unknown solution`. | Preserve the repaired `solutions` block from the maintained TOGO source when regenerating. |
| major | The same JCM 1189 medium is maintained twice with different CultureMech IDs. | The TOGO M1274 bacterial record and MediaDive J1189 specialized record both denote JCM 1189, but use `CultureMech:007807` and `CultureMech:015392`, respectively. | Reconcile the TOGO and MediaDive J1189 normalized records after preserving nested stock structure. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` so the September 2026 repair to `data/normalized_yaml/bacterial/modified_marine_agar_2216_with_5_nacl_ph_9.yaml` reaches the generated artifact.
2. Confirm the regenerated file keeps `ph_value: 9.0`, `Distilled water` at 990.0 ml/L, the full Trace vitamins composition from TOGO M190, and the 10% Na2CO3 stock solution.
3. Reconcile `TOGO:M1274` with `mediadive.medium:J1189` so JCM 1189 has one generated identity while retaining both source accessions.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated TOGO M1274 YAML.
- Re-open JCM 1189, TOGO M1274, TOGO M190, and MediaDive J1189 and confirm the regenerated record preserves the 10 ml/L trace-vitamin addition plus the 10% Na2CO3 pH-adjustment stock.
- Confirm no generated `modified_marine_agar_2216_with_5_nacl_ph_9` row contains `Unknown solution`, an empty Trace vitamins `composition`, or `Distilled water` with `unit: G_PER_L`.
- Run an exact gitignore-independent search for `TOGO:M1274`, `JCM_M1189`, and `mediadive.medium:J1189` under `data/normalized_yaml/` to confirm source identities have been reconciled.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
- The Trace vitamins stock was checked against TOGO M190 because TOGO M1274 references that medium directly.
