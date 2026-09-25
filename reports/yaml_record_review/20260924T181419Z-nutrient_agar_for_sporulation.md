# YAML Record Review: nutrient_agar_for_sporulation

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/nutrient_agar_for_sporulation.yaml
- Started UTC: 2026-09-24T18:13:13Z
- Finished UTC: 2026-09-24T18:14:19Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:008929 |
| Name | nutrient_agar_for_sporulation |
| Original name | Nutrient Agar (For sporulation) |
| Category | bacterial |
| Media term | TOGO:M2341 / Nutrient Agar (For sporulation) |
| Generated path | data/merge_yaml/merged/nutrient_agar_for_sporulation.yaml |
| Maintained source | data/normalized_yaml/bacterial/nutrient_agar_for_sporulation.yaml |
| Merge fingerprint | baa1417c96685062c9118f146caeb40e161035bad99cabd5a4b5039b476b2fe0 |
| Merged from | nutrient_agar_for_sporulation |

This is a generated singleton for TOGO M2341, a DSMZ Medium 1 Nutrient Agar sporulation variant supplemented with MnSO4 x H2O. The maintained source has been repaired since this generated YAML was emitted.

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/nutrient_agar_for_sporulation.yaml` | Passed with "No issues found". |
| Strict validation with `scripts/validate_strict.py data/merge_yaml/merged/nutrient_agar_for_sporulation.yaml --out /private/tmp/nutrient_agar_for_sporulation.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header line. |
| Reference validation with `linkml-reference-validator validate data data/merge_yaml/merged/nutrient_agar_for_sporulation.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 total checks and no failures. |
| Term validation with `linkml-term-validator validate-data data/merge_yaml/merged/nutrient_agar_for_sporulation.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator validates standalone `history/` entries, not embedded generated `MediaRecipe.curation_history`. |

## Identity and Grounding

The intended identity is TOGO M2341, the Nutrient Agar for sporulation formulation that uses DSMZ Medium 1 plus 10 mg/L MnSO4 x H2O. The generated record has the right TOGO identifier and label, but it predates the maintained-source repairs to the manganese unit, water unit, pH, references, and source-duplicate relationship.

An ignored-file-inclusive PCRE2 search for exact `TOGO:M2341`, `TOGO:M2340`, `nutrient_agar_for_sporulation`, and `TOGO_M2340_Nutrient_Agar` across `data/normalized_yaml` and `data/merge_yaml/merged` found this maintained M2341 source, the maintained M2340 source duplicate, the canonical `nutrient_agar` parent, generated M2340 `nutrient_agar__d9de7eec.yaml`, generated M2341 `nutrient_agar_for_sporulation.yaml`, and the unrelated Alkaline Nutrient Agar for sporulation sibling.

## Evidence

DSMZ Medium 1 lists Peptone 5.0 g/L, Meat extract 3.0 g/L, Agar if necessary 15.0 g/L, Distilled water 1000 ml, pH adjustment to 7.0, and a recommendation to add 10.0 mg MnSO4 x H2O for Bacillus strain sporulation. The maintained M2341 normalized source now represents that source as 1.0 L water, 10.0 MG_PER_L manganese sulfate monohydrate, and pH 7.0, and links TOGO M2340 as the same formulation.

The generated record is stale. It stores Distilled water as `1000 G_PER_L`, stores MnSO4 x H2O as `10 G_PER_L`, omits pH 7.0, lacks source references, and does not link to TOGO M2340.

## Completeness

The base DSMZ ingredients and the manganese sulfate supplement are present, but the generated units and relationships are incomplete relative to the maintained source. The missing pieces are pH 7.0, 1.0 L water, 10 mg/L manganese sulfate, the DSMZ/TOGO references, and the M2340 source-duplicate link.

Empty target-organism and citation slots are acceptable for this provider formula. Bacillus is a usage scope in the DSMZ note, not a strain-specific target-organism assertion.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | The generated M2341 Nutrient Agar for sporulation record is stale relative to its repaired maintained source. | `data/normalized_yaml/bacterial/nutrient_agar_for_sporulation.yaml` now stores 1.0 L water, 10.0 MG_PER_L MnSO4 x H2O, pH 7.0, references, curated ingredient terms, and a `SOURCE_DUPLICATE` parent pointing to M2340. The generated file still has 1000 g/L water, 10 g/L manganese sulfate, no pH, and no source-duplicate metadata. | Regenerate `data/merge_yaml/merged` from the repaired M2341 and M2340 normalized inputs. |
| Major | The true M2340 source duplicate remains in a separate generated singleton. | The maintained M2341 source declares M2340 as a `SOURCE_DUPLICATE`, but generated M2341 and M2340 are still split between `nutrient_agar_for_sporulation.yaml` and `nutrient_agar__d9de7eec.yaml`. | Merge regeneration from repaired source-duplicate relationships. |

## Recommended Edits

1. Regenerate merged YAML so TOGO M2341 and TOGO M2340 collapse into one Nutrient Agar for sporulation variant.
2. Confirm the regenerated record preserves 1.0 L water, 10.0 MG_PER_L MnSO4 x H2O, pH 7.0, and the source-duplicate relationship between M2341 and M2340.

## Follow-up Checks

1. Run the focused open schema, strict, reference, and term validators on the regenerated M2341/M2340 record.
2. Search with ignored files included for exact `TOGO:M2341`, `TOGO:M2340`, and `nutrient_agar_for_sporulation` to confirm the two source IDs merge into one generated recipe.

## Additional Notes

None found.
