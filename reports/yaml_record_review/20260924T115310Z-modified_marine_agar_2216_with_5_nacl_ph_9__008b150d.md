# YAML Record Review: MODIFIED MARINE AGAR 2216 WITH 5% NaCl (pH 9)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9__008b150d.yaml
- Started UTC: 2026-09-24T11:53:10Z
- Finished UTC: 2026-09-24T11:53:10Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9__008b150d.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:015392` |
| Name | `modified_marine_agar_2216_with_5_nacl_ph_9` |
| Source identity | `mediadive.medium:J1189` |
| Category | `specialized` |
| Maintained owner | `data/normalized_yaml/specialized/modified_marine_agar_2216_with_5_nacl_ph_9.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one MediaDive-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9__008b150d.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9__008b150d.yaml --out /private/tmp/modified_marine_agar_2216_with_5_nacl_ph_9__008b150d.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9__008b150d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_marine_agar_2216_with_5_nacl_ph_9__008b150d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes MediaDive's JCM 1189 copy of "MODIFIED MARINE AGAR 2216 WITH 5% NaCl (pH 9)". Its source identity and pH are correct, but its ingredient list conflates main-medium ingredients with the trace-vitamin stock composition.

An exact gitignore-independent search under `data/normalized_yaml/` found a second JCM 1189 import, `TOGO:M1274`, with the same medium name and CultureMech ID `CultureMech:007807`. That TOGO record has already been repaired to keep Trace vitamins as a 10 ml/L stock addition and to model 10% Na2CO3 as a pH-adjustment stock.

## Evidence

JCM 1189, TOGO M1274, and MediaDive J1189 support the same main-medium additions: 55.1 g Marine agar 2216, 1.0 g Casitone, 1.0 g Soytone or Phytone peptone, 1.0 g Malt extract, 50.0 g NaCl, 10.0 ml Trace vitamins, and 990.0 ml distilled water, adjusted to pH 9.0 with sterilized 10% Na2CO3 solution.

MediaDive J1189 also exposes a Trace vitamins stock with ten vitamin rows. Those rows are the stock recipe, not ten independent final-medium additions at the displayed stock concentrations. The generated MediaDive record flattens the ten vitamin rows into top-level ingredients and omits both the `Trace vitamins` stock boundary and the 990 ml water row.

## Completeness

The generated record is incomplete because it lacks the 10 ml/L Trace vitamins addition, the 990 ml/L water row, the 10% Na2CO3 stock identity, and the Soytone-or-Phytone alternative text present in the source.

No target organism claims were expected from the inspected JCM, TOGO, or MediaDive medium records.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The MediaDive J1189 import flattens the Trace vitamins stock into unsupported final-medium ingredient rows. | JCM 1189 adds 10 ml Trace vitamins; MediaDive exposes a separate Trace vitamins stock; the generated YAML promotes Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium pantothenate, Vitamin B12, p-Aminobenzoic acid, and Lipoic acid to top-level ingredients at stock concentrations. | Repair `data/normalized_yaml/specialized/modified_marine_agar_2216_with_5_nacl_ph_9.yaml` or reconcile it with the repaired TOGO M1274 record, then regenerate. |
| major | The MediaDive J1189 import omits the source water row. | JCM 1189, TOGO M1274, and MediaDive J1189 list 990 ml distilled water; the generated MediaDive record has no water ingredient. | Preserve the MediaDive 990 ml water row in the maintained source. |
| major | The same JCM 1189 medium is maintained twice with different CultureMech IDs. | `mediadive.medium:J1189` and `TOGO:M1274` both derive from JCM 1189 and generate same-slug records under different category folders. | Reconcile the specialized MediaDive J1189 source with the repaired bacterial TOGO M1274 source. |
| major | The source Soytone-or-Phytone alternative is narrowed to Soytone. | JCM and TOGO allow Soytone (BD-Difco) or Phytone peptone (BD-BBL); the generated MediaDive YAML stores only `Soytone`. | Preserve the alternative source text or explicitly model the alternate peptone choices. |
| major | Marine agar 2216 is incorrectly grounded to pure agar. | The source ingredient is the undefined commercial product Marine agar 2216 (BD-Difco), while the generated record assigns `CHEBI:2509` agar. | De-ground the MediaDive J1189 Marine agar 2216 row and preserve the BD-Difco product label. |

## Recommended Edits

1. Replace the flattened vitamin ingredients in `data/normalized_yaml/specialized/modified_marine_agar_2216_with_5_nacl_ph_9.yaml` with a 10 ml/L Trace vitamins stock addition and structured stock composition.
2. Add the missing 990 ml distilled water row.
3. Reconcile the MediaDive J1189 and TOGO M1274 normalized records so the same JCM 1189 recipe has one CultureMech identity.
4. Preserve the Soytone-or-Phytone alternative wording and de-ground the Marine agar 2216 commercial product from `CHEBI:2509`.
5. Preserve the 10% Na2CO3 pH-adjustment stock if using the TOGO M1274 repair as the canonical source.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated JCM 1189 YAML.
- Re-open JCM 1189, TOGO M1274, TOGO M190, and MediaDive J1189 and confirm the generated YAML contains one 10 ml/L Trace vitamins addition, not ten top-level vitamin rows.
- Confirm no generated `modified_marine_agar_2216_with_5_nacl_ph_9` row omits distilled water or grounds Marine agar 2216 to `CHEBI:2509`.
- Run an exact gitignore-independent search for `TOGO:M1274`, `JCM_M1189`, and `mediadive.medium:J1189` under `data/normalized_yaml/` to confirm duplicate source identities have been reconciled.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
- The strict TSV was counted after rerunning the count because the first count ran before the strict validator had written its output file.
