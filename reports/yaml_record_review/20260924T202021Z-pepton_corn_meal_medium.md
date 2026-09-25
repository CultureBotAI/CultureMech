# YAML Record Review: pepton_corn_meal_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/pepton_corn_meal_medium.yaml`
- Started UTC: 2026-09-24T20:20:21Z
- Finished UTC: 2026-09-24T20:20:22Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pepton_corn_meal_medium.yaml`, a generated `MediaRecipe` merge record.

- ID: `CultureMech:006624`
- Label: `pepton_corn_meal_medium`
- Category: `bacterial`
- Source terms: `komodo.medium:831`; duplicate DSMZ parent `mediadive.medium:831`
- Physical state: `SOLID_AGAR`
- Maintained owners: `data/normalized_yaml/bacterial/KOMODO_831_PEPTON-CORN_MEAL_medium.yaml`; `data/normalized_yaml/bacterial/pepton_corn_meal_medium.yaml`
- Generated from: `KOMODO_831_PEPTON-CORN_MEAL_medium`, `pepton_corn_meal_medium`

## Validation

- Passed: open LinkML validation of `data/merge_yaml/merged/pepton_corn_meal_medium.yaml` against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`; no issues found.
- Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pepton_corn_meal_medium.yaml --out /private/tmp/pepton_corn_meal_medium.strict.tsv --workers 1 --quiet`; the TSV contained only its header, so strict validation found 0 errors.
- Passed: focused `linkml-reference-validator validate data data/merge_yaml/merged/pepton_corn_meal_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 0 references were checked.
- Passed: focused `linkml-term-validator validate-data data/merge_yaml/merged/pepton_corn_meal_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
- Not checked: embedded `curation_history`; the documented `just validate-history` target validates standalone `history/` YAML rather than `MediaRecipe.curation_history` embedded in generated records.

## Identity and Grounding

`komodo.medium:831` names PEPTON-CORN MEAL medium and records DSMZ Medium 831 provenance; `mediadive.medium:831` resolves to DSMZ Medium 831, PEPTON-CORN MEAL MEDIUM. The generated record correctly merges the KOMODO and DSMZ maintained inputs as `SOURCE_DUPLICATE` records because the source ingredient signatures match.

The Starch, NaCl, and CaCl2 groundings are supported by DSMZ 831 and MediaDive 831. The Peptone and Corn meal agar rows are complex/undefined products; Peptone is correctly ungrounded, but Corn meal agar is incorrectly grounded as pure agar.

## Evidence

- DSMZ 831 lists 10 g Starch, 5 g NaCl, 0.5 g CaCl2, 5 g Pepton, 17 g Corn meal Agar with Oxoid CM103 in parentheses, 1000 ml Distilled water, and pH 7.2.
- MediaDive 831 reports the same amounts and stores the 17 g row as `Corn meal agar` with attribute `Oxoid CM103`.
- The generated record carries the non-water concentrations, pH, solid-agar physical state, and the KOMODO-to-DSMZ `SOURCE_DUPLICATE` relationship.

## Completeness

The generated record omits the 1000 ml Distilled water row present in DSMZ 831 and MediaDive 831. It also overstates Corn meal agar grounding by assigning `CHEBI:2509` agar to a complex commercial corn-meal agar product.

Empty optional fields are not defects.

An ignored-inclusive exact search of `data`, `src`, and `scripts` for `komodo.medium:831`, `mediadive.medium:831`, `CultureMech:006624`, `CultureMech:001989`, `DSMZ_Medium831`, `PEPTON-CORN`, and `pepton_corn_meal_medium` found the two maintained owners, this generated merge record, and index rows. It found no additional same-source YAML records.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | `Corn meal agar` is incorrectly grounded to pure agar. | DSMZ 831 and MediaDive 831 identify the row as the Oxoid CM103 Corn meal agar product. That is an undefined complex product, not `CHEBI:2509` agar. | `data/normalized_yaml/bacterial/pepton_corn_meal_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_831_PEPTON-CORN_MEAL_medium.yaml` |
| Minor | The final 1000 ml Distilled water row is missing. | DSMZ 831 and MediaDive 831 both list 1000 ml Distilled water in the final recipe; both maintained duplicate inputs and the generated merge output omit it. | `data/normalized_yaml/bacterial/pepton_corn_meal_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_831_PEPTON-CORN_MEAL_medium.yaml` |

## Recommended Edits

1. Remove the `CHEBI:2509` term and `mediaingredientmech_chebi_term` from `Corn meal agar` in both maintained source duplicates, unless a curated product-level term for Oxoid CM103 Corn meal agar is added.
2. Add 1000 ml/L Distilled water to both maintained source duplicates.
3. Regenerate `data/merge_yaml/merged/pepton_corn_meal_medium.yaml` and confirm the KOMODO and DSMZ inputs still collapse into the same generated duplicate.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on both maintained duplicate inputs, then regenerate `data/merge_yaml/merged/pepton_corn_meal_medium.yaml` and rerun the same focused validators on the generated record.
- Manually compare the regenerated record against DSMZ 831 and MediaDive 831, confirming that Corn meal agar is no longer asserted to be pure agar.

## Additional Notes

None found.
