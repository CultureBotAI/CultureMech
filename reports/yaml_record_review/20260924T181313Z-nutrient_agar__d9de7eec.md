# YAML Record Review: nutrient_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/nutrient_agar__d9de7eec.yaml
- Started UTC: 2026-09-24T18:12:03Z
- Finished UTC: 2026-09-24T18:13:13Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:008928 |
| Name | nutrient_agar |
| Original name | Nutrient Agar |
| Category | bacterial |
| Media term | TOGO:M2340 / Nutrient Agar |
| Generated path | data/merge_yaml/merged/nutrient_agar__d9de7eec.yaml |
| Maintained source | data/normalized_yaml/bacterial/TOGO_M2340_Nutrient_Agar.yaml |
| Merge fingerprint | d9de7eeccd358692f7563b25714b565985e26279e0b0b0e75735e44b668554af |
| Merged from | TOGO_M2340_Nutrient_Agar |

This is a generated singleton for the TOGO M2340 / DSMZ Medium 1 Nutrient Agar variant with the source-recommended MnSO4 x H2O supplement for Bacillus sporulation. The maintained source has been repaired since this generated YAML was emitted.

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/nutrient_agar__d9de7eec.yaml` | Passed with "No issues found". |
| Strict validation with `scripts/validate_strict.py data/merge_yaml/merged/nutrient_agar__d9de7eec.yaml --out /private/tmp/nutrient_agar__d9de7eec.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header line. |
| Reference validation with `linkml-reference-validator validate data data/merge_yaml/merged/nutrient_agar__d9de7eec.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 total checks and no failures. |
| Term validation with `linkml-term-validator validate-data data/merge_yaml/merged/nutrient_agar__d9de7eec.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator validates standalone `history/` entries, not embedded generated `MediaRecipe.curation_history`. |

## Identity and Grounding

The intended identity is TOGO M2340, which represents DSMZ Medium 1 Nutrient Agar supplemented with MnSO4 x H2O for Bacillus-strain sporulation. The generated file has the right TOGO identifier and variant, but it still has the old unit and pH omissions that were repaired in the maintained source.

An ignored-file-inclusive PCRE2 search for exact `TOGO:M2340`, `TOGO:M2341`, and `nutrient_agar_for_sporulation` across `data/normalized_yaml` and `data/merge_yaml/merged` found the maintained M2340 source, the maintained M2341 source duplicate, the canonical `nutrient_agar` parent link, the generated `nutrient_agar_for_sporulation.yaml` M2341 singleton, and this generated M2340 singleton. The current maintained relationship says M2340 and M2341 should merge as source duplicates of the same Bacillus-sporulation variant.

## Evidence

DSMZ Medium 1 lists Peptone 5.0 g/L, Meat extract 3.0 g/L, Agar if necessary 15.0 g/L, Distilled water 1000 ml, pH adjustment to 7.0, and a recommendation to add 10.0 mg MnSO4 x H2O for Bacillus strain sporulation. The repaired M2340 normalized source represents that as 10.0 MG_PER_L manganese sulfate monohydrate and a supplemented-variant relationship to canonical DSMZ Nutrient Agar.

The generated record is stale. It stores Distilled water as `1000 G_PER_L`, stores `MnSO4` as `10 G_PER_L` grounded to anhydrous CHEBI:86360, omits pH 7.0, omits the Bacillus sporulation context, and has no link to the M2341 source duplicate.

## Completeness

The DSMZ base ingredients are present in the generated file, and the extra manganese sulfate row makes this the correct sporulation variant rather than plain Nutrient Agar. The consequential gaps are all repaired upstream already: the water unit, the 10 mg/L manganese concentration and hydrate identity, pH 7.0, the `SUPPLEMENTED_VARIANT` parent, the M2341 source-duplicate child, references, and data-quality flags.

Empty target-organism and citation slots are acceptable for this provider formula. Bacillus is a usage scope in the DSMZ note, not a strain-specific target-organism assertion.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | The generated M2340 Nutrient Agar variant is stale relative to its repaired maintained source. | `data/normalized_yaml/bacterial/TOGO_M2340_Nutrient_Agar.yaml` now stores MnSO4 x H2O as `10.0 MG_PER_L`, pH 7.0, 1.0 L water, the Bacillus sporulation note, and the `SUPPLEMENTED_VARIANT` parent. The generated file still stores MnSO4 as `10 G_PER_L`, stores water as `1000 G_PER_L`, and has no pH or relationship metadata. | Regenerate `data/merge_yaml/merged` from the repaired M2340 and M2341 normalized inputs. |
| Major | The true M2341 source duplicate remains in a separate generated singleton. | The maintained M2340 source links `data/normalized_yaml/bacterial/nutrient_agar_for_sporulation.yaml` as a `SOURCE_DUPLICATE`, but the generated corpus still has separate M2340 `nutrient_agar__d9de7eec.yaml` and M2341 `nutrient_agar_for_sporulation.yaml` files. | Merge regeneration from repaired source-duplicate relationships. |

## Recommended Edits

1. Regenerate merged YAML so TOGO M2340 and TOGO M2341 collapse into one Nutrient Agar for sporulation variant of canonical DSMZ Medium 1.
2. Confirm the regenerated variant keeps the 10.0 MG_PER_L MnSO4 x H2O amount, pH 7.0, 1.0 L water, and `SUPPLEMENTED_VARIANT` relationship to plain Nutrient Agar.

## Follow-up Checks

1. Run the focused open schema, strict, reference, and term validators on the regenerated M2340/M2341 record.
2. Search with ignored files included for exact `TOGO:M2340`, `TOGO:M2341`, and `nutrient_agar_for_sporulation` to confirm the two source IDs now merge into the intended generated recipe.

## Additional Notes

None found.
