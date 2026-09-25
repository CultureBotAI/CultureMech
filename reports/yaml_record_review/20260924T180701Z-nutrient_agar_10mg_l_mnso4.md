# YAML Record Review: nutrient_agar_10mg_l_mnso4

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/nutrient_agar_10mg_l_mnso4.yaml
- Started UTC: 2026-09-24T18:05:41Z
- Finished UTC: 2026-09-24T18:07:01Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:008850 |
| Name | nutrient_agar_10mg_l_mnso4 |
| Original name | Nutrient Agar + 10mg/L MnSO4 |
| Category | bacterial |
| Media term | TOGO:M2263 / Nutrient Agar + 10mg/L MnSO4 |
| Generated path | data/merge_yaml/merged/nutrient_agar_10mg_l_mnso4.yaml |
| Maintained source | data/normalized_yaml/bacterial/nutrient_agar_10mg_l_mnso4.yaml |
| Merge fingerprint | b076939743374683a087471cf8959c082bc06790b371da3d908a4af24fa225ed |
| Merged from | nutrient_agar_10mg_l_mnso4 |

This is a generated singleton TOGO record for a DSMZ Medium 1 Nutrient Agar variant with added MnSO4. Corrections belong in the maintained TOGO normalized source, followed by merged-record regeneration.

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/nutrient_agar_10mg_l_mnso4.yaml` | Passed with "No issues found". |
| Strict validation with `scripts/validate_strict.py data/merge_yaml/merged/nutrient_agar_10mg_l_mnso4.yaml --out /private/tmp/nutrient_agar_10mg_l_mnso4.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header line. |
| Reference validation with `linkml-reference-validator validate data data/merge_yaml/merged/nutrient_agar_10mg_l_mnso4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 total checks and no failures. |
| Term validation with `linkml-term-validator validate-data data/merge_yaml/merged/nutrient_agar_10mg_l_mnso4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator validates standalone `history/` entries, not embedded generated `MediaRecipe.curation_history`. |

## Identity and Grounding

The TOGO `M2263` identity matches a Nutrient Agar variant that uses the DSMZ Medium 1 PDF and adds MnSO4 x H2O. The bacterial category, undefined composition, solid-agar state, water, agar, Meat extract, Peptone, and manganese sulfate monohydrate grounding agree with the TOGO and DSMZ sources.

An ignored-file-inclusive search for `TOGO:M2263`, `M2263`, `Nutrient Agar + 10mg/L MnSO4`, and `nutrient_agar_10mg_l_mnso4` across `data/normalized_yaml` and `data/merge_yaml/merged` found only this maintained source, index entries, and this generated record. A broader `DSMZ_Medium1.pdf` search also found expected sibling Nutrient Agar variants that reuse the DSMZ Medium 1 PDF, but no additional M2263 copy.

## Evidence

DSMZ Medium 1 lists Peptone at 5.0 g/L, Meat extract at 3.0 g/L, agar if necessary at 15.0 g/L, distilled water at 1000 ml, pH adjustment to 7.0, and a note that adding 10.0 mg MnSO4 x H2O is recommended for Bacillus strain sporulation. TOGO M2263 carries the same ingredients and explicitly stores MnSO4 x H2O with unit `mg`.

The generated record incorrectly stores MnSO4 x H2O as `10 G_PER_L`, 1000-fold higher than the source 10.0 mg/L value. It also drops the pH 7.0 instruction and the Bacillus-sporulation context for the manganese addition.

## Completeness

Peptone, Meat extract, agar, distilled water, and the MnSO4 ingredient identity are present. The consequential missing or distorted details are the MnSO4 unit conversion, the pH 7.0 adjustment, and the fact that manganese sulfate is specifically a Bacillus sporulation supplement to base Nutrient Agar.

Empty target-organism and citation slots are acceptable for this TOGO provider variant. The provider source names Bacillus strains as a use context but does not identify a precise target organism.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | The TOGO importer converted a 10 mg/L MnSO4 x H2O supplement into `10 G_PER_L`. | TOGO M2263 stores MnSO4 x H2O as `volume: 10` and `unit: mg`, and DSMZ Medium 1 says 10.0 mg MnSO4 x H2O is recommended for sporulation. The generated record records the same numeric value with a gram-per-liter unit. | TOGO import normalization for `data/normalized_yaml/bacterial/nutrient_agar_10mg_l_mnso4.yaml`, then merged-record regeneration. |
| Major | The pH 7.0 source value was dropped. | TOGO M2263 has `ph: 7.0`, and DSMZ Medium 1 instructs pH adjustment to 7.0. The generated record has no `ph_value`, `ph_range`, or pH preparation step. | TOGO import normalization for `data/normalized_yaml/bacterial/nutrient_agar_10mg_l_mnso4.yaml`. |
| Minor | The generated record loses the Bacillus sporulation scope of the MnSO4 supplement. | DSMZ Medium 1 specifically frames 10.0 mg MnSO4 x H2O as recommended for Bacillus strain sporulation; the generated record keeps only generic `Microbial cultivation`. | TOGO comments-to-notes mapping for the maintained normalized source. |

## Recommended Edits

1. Convert TOGO `mg` component amounts to grams per liter so M2263 stores MnSO4 x H2O as `0.01 G_PER_L`.
2. Preserve the TOGO/DSMZ pH 7.0 value on the normalized record.
3. Preserve the DSMZ Bacillus sporulation note as a bounded preparation or ingredient note, without converting it into a target-organism assertion.

## Follow-up Checks

1. Regenerate normalized and merged YAML, then confirm MnSO4 x H2O is `0.01 G_PER_L` and pH 7.0 is present.
2. Run the focused open schema, strict, reference, and term validators on `data/merge_yaml/merged/nutrient_agar_10mg_l_mnso4.yaml`.
3. Search with ignored files included for `TOGO:M2263` and `Nutrient Agar + 10mg/L MnSO4` to confirm the repaired record remains a singleton M2263 merge.

## Additional Notes

None found.
