# YAML Record Review: pennassay_g_thy_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/pennassay_g_thy_medium.yaml`
- Started UTC: 2026-09-24T20:18:01Z
- Finished UTC: 2026-09-24T20:18:01Z
- Verdict: pass with minor issues

## Target

Reviewed `data/merge_yaml/merged/pennassay_g_thy_medium.yaml`, a generated `MediaRecipe` merge record.

- ID: `CultureMech:005971`
- Label: `pennassay_g_thy_medium`
- Category: `bacterial`
- Source terms: `komodo.medium:542`; duplicate DSMZ parent `mediadive.medium:542`
- Physical state: `LIQUID`
- Maintained owners: `data/normalized_yaml/bacterial/KOMODO_542_PENNASSAY_G-THY_medium.yaml`; `data/normalized_yaml/bacterial/pennassay_g_thy_medium.yaml`
- Generated from: `KOMODO_542_PENNASSAY_G-THY_medium`, `pennassay_g_thy_medium`

## Validation

- Passed: open LinkML validation of `data/merge_yaml/merged/pennassay_g_thy_medium.yaml` against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`; no issues found.
- Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pennassay_g_thy_medium.yaml --out /private/tmp/pennassay_g_thy_medium.strict.tsv --workers 1 --quiet`; the TSV contained only its header, so strict validation found 0 errors.
- Passed: focused `linkml-reference-validator validate data data/merge_yaml/merged/pennassay_g_thy_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 0 references were checked.
- Passed: focused `linkml-term-validator validate-data data/merge_yaml/merged/pennassay_g_thy_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
- Not checked: embedded `curation_history`; the documented `just validate-history` target validates standalone `history/` YAML rather than `MediaRecipe.curation_history` embedded in generated records.

## Identity and Grounding

`komodo.medium:542` names PENNASSAY G-THY medium and records DSMZ Medium 542 provenance; `mediadive.medium:542` resolves to DSMZ Medium 542, PENNASSAY G-THY MEDIUM. The generated record correctly merges the KOMODO and DSMZ maintained inputs as a `SOURCE_DUPLICATE` because the non-water ingredient signature is identical: 17.5 g/L Pennassay Broth, 20 g/L Glucose, and 0.05 g/L Thymine.

Glucose and Thymine are correctly grounded to CHEBI. Pennassay Broth is a complex commercial medium and is correctly left ungrounded rather than forced to an adjacent simple chemical.

## Evidence

- DSMZ Medium 542 lists 17.50 g Pennassay Broth, 20.00 g Glucose, 0.05 g Thymine, and 1000.00 ml Distilled water.
- MediaDive 542 reports the same Main solution rows and concentrations.
- The generated record carries the three non-water ingredient rows and preserves the reciprocal KOMODO-to-DSMZ `SOURCE_DUPLICATE` relationship in `parent_media`, `variant_relationship`, and `merged_from`.

## Completeness

The generated record omits the 1000 ml Distilled water row present in DSMZ Medium 542 and MediaDive 542. That solvent row is the only source-backed component missing from the inspected final formulation.

Empty optional fields are not defects.

An ignored-inclusive exact search of `data`, `src`, and `scripts` for `komodo.medium:542`, `mediadive.medium:542`, `CultureMech:005971`, `CultureMech:001675`, `DSMZ_Medium542`, `PENNASSAY_G-THY`, and `pennassay_g_thy_medium` found the two maintained owners, this generated merge record, index rows, and the local ungrounded-ingredient report for Pennassay Broth. It found no additional same-source YAML records.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Minor | The final 1000 ml Distilled water row is missing. | DSMZ 542 and MediaDive 542 both list 1000 ml Distilled water in the 1 L final recipe; both maintained duplicate inputs and the generated merge output omit it. | `data/normalized_yaml/bacterial/pennassay_g_thy_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_542_PENNASSAY_G-THY_medium.yaml` |

## Recommended Edits

1. Add 1000 ml/L Distilled water to both maintained source duplicates so they retain the same source signature and continue to merge as duplicates.
2. Regenerate `data/merge_yaml/merged/pennassay_g_thy_medium.yaml`.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on both maintained duplicate inputs, then regenerate `data/merge_yaml/merged/pennassay_g_thy_medium.yaml` and rerun the same focused validators on the generated record.
- Manually confirm the regenerated record still has exactly one KOMODO child and one DSMZ parent connected by `SOURCE_DUPLICATE`.

## Additional Notes

None found.
