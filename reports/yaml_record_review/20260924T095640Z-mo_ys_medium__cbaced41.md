# YAML Record Review: MO-YS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mo_ys_medium__cbaced41.yaml
- Started UTC: 2026-09-24T09:56:40Z
- Finished UTC: 2026-09-24T09:56:40Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/mo_ys_medium__cbaced41.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002252` |
| Name | `mo_ys_medium` |
| Original name | `MO-YS MEDIUM` |
| Category | `bacterial` |
| Medium source | MediaDive `J1071`, imported from JCM |
| Maintained owner | `data/normalized_yaml/bacterial/mo_ys_medium.yaml` |
| Related normalized solutions | `data/normalized_yaml/bacterial/mediadive_5136_Main_sol_J1071.yaml`, `data/normalized_yaml/bacterial/mediadive_4580_Trace_vitamins_solution.yaml`, `data/normalized_yaml/bacterial/mediadive_4581_Trace_element_solution.yaml` |
| Generated status | Generated merge output from one normalized MediaDive record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mo_ys_medium__cbaced41.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/mo_ys_medium__cbaced41.yaml --out /private/tmp/mo_ys_medium__cbaced41.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/mo_ys_medium__cbaced41.strict.tsv` contained only the header line, so no strict errors were reported. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/mo_ys_medium__cbaced41.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/mo_ys_medium__cbaced41.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record denotes the MediaDive import of JCM medium `J1071` / `MO-YS MEDIUM`. Its ID, name, category, pH 7.5, MediaDive CURIE, and JCM source URL agree with the live MediaDive `J1071` payload.

Most simple ingredient groundings fit their displayed labels. The shared trace-element stock still has one exact-form grounding problem copied into this generated medium: `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / nickel dichloride rather than to a nickel chloride hexahydrate term.

## Evidence

The live MediaDive `J1071` REST payload supports a multi-solution formula:

| Source claim | Record representation | Review |
| --- | --- | --- |
| Medium `J1071` is `MO-YS MEDIUM`, complex, from JCM, pH 7.5. | The record has `mediadive.medium:J1071`, `MO-YS MEDIUM`, `COMPLEX`, and `ph_value: 7.5`. | Supported. |
| `Main sol. J1071` is MediaDive solution `5136` with 1112 ml total volume. It includes the base components, 1 ml Trace vitamins solution `4580`, 1 ml Trace element solution `4581`, 1000 ml water, 0.86 g crotonic acid, 100 ml water, 5 ml 3% L-Cysteine HCl x H2O, and 5 ml 3% Na2S x 9 H2O. | The generated record has one flat `ingredients` list with no `solutions` links or stock-addition rows. | Unsupported representation: MediaDive solution additions were flattened away. |
| The base and carbon-source `g_l` values are final MediaDive concentrations calculated over 1112 ml. | Rows such as `Yeast extract` `0.044964 G_PER_L`, `NaCl` `18.3903 G_PER_L`, and `Crotonic acid` `0.773381 G_PER_L` match MediaDive `g_l` fields. | Supported for the direct main-solution compound rows. |
| Trace vitamins solution `4580` and Trace element solution `4581` are 1000 ml stocks added to the 1112 ml main solution at 1 ml each. | All vitamin and trace-element stock rows are copied into the medium at their stock `G_PER_L` concentrations. | Unsupported final-medium amount: the stock rows are not diluted by their 1 ml addition. |
| The two reducing additives are 5 ml aliquots of 3% stock solutions. | `L-Cysteine HCl x H2O` and `Na2S x 9 H2O` are both stored as `5 G_PER_L`. | Unsupported unit conversion: 5 ml stock additions are not 5 g/L pure-compound rows. |
| The MediaDive steps describe Solution A, Solution B, N2-CO2 cooling, N2 sterilization, and anaerobic assembly. | Preparation prose is present, but the corresponding structured Solution A/B compartments are absent. | Partially supported; the procedure references compartments that are not represented in the formulation. |

## Completeness

The record is incomplete as a structured MO-YS formulation. It omits explicit links to MediaDive solution `5136`, Trace vitamins solution `4580`, and Trace element solution `4581`, and it lacks structured rows for the 1 ml and 5 ml volume additions that control stock dilution.

The optional absence of `target_organisms` was not treated as a defect. MediaDive `J1071` identifies a source medium formula, not organism-specific growth evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The MediaDive J1071 medium is flattened even though its source payload and local normalized corpus both expose its solution graph. | MediaDive has `Main sol. J1071` `5136`, Trace vitamins solution `4580`, and Trace element solution `4581`; exact ignored-inclusive search of `data/normalized_yaml` found `mediadive_5136_Main_sol_J1071.yaml`, while the generated `MediaRecipe` has only a top-level `ingredients` list. | `data/normalized_yaml/bacterial/mo_ys_medium.yaml`; MediaDive medium import or solution-linking logic. |
| major | Trace vitamin and trace element stock concentrations are copied into the final medium at stock strength. | MediaDive J1071 adds each stock solution at 1 ml into the 1112 ml main solution; the generated medium stores vitamin and trace rows such as `Biotin` `0.0049 G_PER_L` and `FeCl3 x 6 H2O` `1.27 G_PER_L`. | `data/normalized_yaml/bacterial/mo_ys_medium.yaml`; MediaDive stock expansion logic. |
| major | Two 5 ml 3% reducing-solution additions are represented as 5 g/L ingredient concentrations. | MediaDive records 5 ml additions with attribute `3%`; the generated rows for `L-Cysteine HCl x H2O` and `Na2S x 9 H2O` are both `5 G_PER_L`. | `data/normalized_yaml/bacterial/mo_ys_medium.yaml`; MediaDive volume-unit normalization. |
| major | `NiCl2 x 6 H2O` has the wrong exact CHEBI grounding. | MediaDive and the row label name nickel chloride hexahydrate, but the generated row and shared `mediadive.solution:4581` stock ground it to `CHEBI:34887` / nickel dichloride. | `data/normalized_yaml/bacterial/mediadive_4581_Trace_element_solution.yaml` and regenerated records that copy its trace-element rows. |
| minor | Preparation steps reference missing compartments. | Steps named `Solution A:` and `Solution B:` remain, but the formulation has no structured Solution A/B rows to bind those steps to. | `data/normalized_yaml/bacterial/mo_ys_medium.yaml`; MediaDive preparation import. |

## Recommended Edits

1. Update `data/normalized_yaml/bacterial/mo_ys_medium.yaml` so J1071 links to or nests `mediadive.solution:5136`, `4580`, and `4581` instead of flattening all MediaDive solution contents into final top-level ingredients.
2. Preserve stock-addition units for the 1 ml trace stocks and the two 5 ml 3% reducing stocks; only compute optional final concentrations when the source stock, addition volume, and final volume remain explicit.
3. Correct the `NiCl2 x 6 H2O` CHEBI grounding in `data/normalized_yaml/bacterial/mediadive_4581_Trace_element_solution.yaml`.
4. Regenerate `data/merge_yaml/merged/mo_ys_medium__cbaced41.yaml` after the MediaDive import path and shared trace stock are repaired.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on the edited MediaDive J1071 medium, `mediadive_4581_Trace_element_solution.yaml` if changed, and the regenerated merge record.
2. Manually compare the regenerated record against the live MediaDive J1071 payload to confirm that `Main sol. J1071` remains a 1112 ml solution, trace stocks remain 1 ml additions, and reducing additions remain 5 ml 3% stocks.
3. Confirm that the preparation steps still line up with structured Solution A and Solution B compartments after regeneration.

## Additional Notes

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
