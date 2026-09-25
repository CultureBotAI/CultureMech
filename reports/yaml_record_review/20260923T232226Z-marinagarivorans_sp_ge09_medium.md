# YAML Record Review: marinagarivorans_sp_ge09_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marinagarivorans_sp_ge09_medium.yaml
- Started UTC: 2026-09-23T23:22:26Z
- Finished UTC: 2026-09-23T23:22:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:015838 |
| name | marinagarivorans_sp_ge09_medium |
| original_name | Marinagarivorans sp. GE09 medium |
| category | bacterial |
| medium_type | DEFINED |
| composition_type | DEFINED |
| physical_state | LIQUID |
| source term | jcm.grmd:1357, Marinagarivorans sp. GE09 medium |
| generated path | data/merge_yaml/merged/marinagarivorans_sp_ge09_medium.yaml |
| maintained owner | data/normalized_yaml/bacterial/JCM_J1357_Marinagarivorans_sp_GE09_medium.yaml |

The reviewed YAML is a derived merge artifact. Its `merged_from` value names the exact normalized owner `JCM_J1357_Marinagarivorans_sp_GE09_medium`. The normalized owner also carries an August 2026 deduplication event that removed one duplicate `Distilled water` row after import.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:015838`, `jcm.grmd:1357`, `GRMD=1357`, `JCM_J1357_Marinagarivorans_sp_GE09_medium`, and `Marinagarivorans sp. GE09 medium` found this normalized owner, this generated copy, and derived JSON indexes; no second YAML in those searched trees claimed the same exact CultureMech or JCM identifier.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinagarivorans_sp_ge09_medium.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/marinagarivorans_sp_ge09_medium.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The record denotes JCM Medium 1357, `Marinagarivorans sp. GE09 medium`, and its liquid state, defined composition class, and direct main-medium additions agree with JCM.

JCM GRMD 1357 has three nested formulation boundaries:

| Boundary | Source representation |
|---|---|
| Final medium | 0.132 g ammonium sulfate, 1.0 g cellobiose, 0.06 g urea, 50 ml trace mineral solution, and 1.0 L artificial seawater |
| Trace mineral solution | 0.4 g Na2CO3, 20 ml Trace Metal Mix A5, 20 mg EDTA x Na2, 0.12 g ferric ammonium citrate, 0.4 g K2HPO4, and 1.0 L distilled water |
| Trace Metal Mix A5 | 2.86 g KNO3, 1.81 g MnCl2 x 4H2O, 0.222 g ZnSO4 x 7H2O, 0.39 g Na2MnO4 x 2H2O, 0.079 g CuSO4 x 5H2O, 49.4 mg Co(NO3)2 x 6H2O, and 1.0 L distilled water |

The generated record preserves the final-medium stock rows for trace mineral solution and artificial seawater but then appends every trace-mineral and A5 component as if each stock recipe were also a final-medium ingredient. That loses the stock hierarchy and makes the final recipe chemically wrong.

## Evidence

Supported:

- The final-medium ammonium sulfate, cellobiose, urea, and 50 ML_PER_L trace-mineral rows match JCM.
- The filter-sterilization step with a 0.22 um PES filter matches JCM.
- The CHEBI grounding on ammonium sulfate, cellobiose, urea, sodium carbonate, ferric ammonium citrate, K2HPO4, KNO3, ZnSO4 x 7H2O, CuSO4 x 5H2O, and Co(NO3)2 x 6H2O matches the corresponding source strings.

Unsupported or over-scoped:

- `Artificial seawater` is 1.0 L in JCM but `1.0 ML_PER_L` in the record.
- JCM has two 1.0 L distilled-water rows, one for each nested stock recipe. The record retained a single `1.0 ML_PER_L` row and then a deduplication event removed the other identical bad row.
- Na2CO3, Trace Metal Mix A5, EDTA x Na2, ferric ammonium citrate, and K2HPO4 are trace-mineral-solution components, not final-medium components.
- KNO3, MnCl2 x 4H2O, ZnSO4 x 7H2O, Na2MnO4 x 2H2O, CuSO4 x 5H2O, and Co(NO3)2 x 6H2O are Trace Metal Mix A5 components, not final-medium components.

## Completeness

Missing or incomplete:

- The nested trace mineral solution and Trace Metal Mix A5 recipes are not represented.
- The 1 L artificial-seawater row was misparsed as 1 ML_PER_L.
- Both nested 1 L distilled-water rows were misparsed as 1 ML_PER_L; one was later deleted as a duplicate.

Complete enough:

- No pH is listed by JCM for GRMD 1357.
- No agar or physical-state correction is needed.
- No target-organism evidence is required for this JCM recipe import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | Two stock recipes were flattened into the final medium. | JCM scopes Na2CO3 through K2HPO4 to trace mineral solution and KNO3 through Co(NO3)2 x 6H2O to Trace Metal Mix A5. The record also keeps the `Trace mineral solution` and `Trace Metal Mix A5` rows, so it represents both a stock addition and that stock's internal ingredients as final ingredients. | data/normalized_yaml/bacterial/JCM_J1357_Marinagarivorans_sp_GE09_medium.yaml, or the JCM importer if it owns nested stock parsing |
| major | One-liter liquid additions were imported as 1 ML_PER_L. | JCM lists 1.0 L artificial seawater in the final medium and 1.0 L distilled water inside each nested stock recipe; the record stores artificial seawater and distilled water as `1.0 ML_PER_L`. | data/normalized_yaml/bacterial/JCM_J1357_Marinagarivorans_sp_GE09_medium.yaml, or the JCM importer |
| major | The duplicate-water cleanup removed a symptom of the unit bug. | The normalized owner recorded `REMOVED_DUPLICATE_INGREDIENT_ROWS` for `Distilled water`; the two rows were distinct stock-solution waters in JCM but looked identical only after both 1 L amounts had been flattened and converted to `1.0 ML_PER_L`. | data/normalized_yaml/bacterial/JCM_J1357_Marinagarivorans_sp_GE09_medium.yaml and the deduplication rule |

## Recommended Edits

1. Restore the JCM boundaries in `data/normalized_yaml/bacterial/JCM_J1357_Marinagarivorans_sp_GE09_medium.yaml`: final medium, trace mineral solution, and Trace Metal Mix A5.
2. Represent artificial seawater as the 1 L final-medium base, not as `1 ML_PER_L`.
3. Keep one 1 L distilled-water row inside trace mineral solution and one 1 L distilled-water row inside Trace Metal Mix A5; do not deduplicate them against each other.
4. Patch the JCM importer and any duplicate-ingredient cleanup rule that collapses same-label rows across different solution scopes.

## Follow-up Checks

- Rerun open schema, strict, term, and reference validation on the normalized owner and regenerated merged record.
- Re-fetch JCM GRMD 1357 and verify that the regenerated record has exactly three formulation scopes matching the final medium, trace mineral solution, and Trace Metal Mix A5 tables.
- Add a regression test that a JCM medium with nested `see below` stock tables preserves separate 1 L water rows per stock.

## Additional Notes

None found.
