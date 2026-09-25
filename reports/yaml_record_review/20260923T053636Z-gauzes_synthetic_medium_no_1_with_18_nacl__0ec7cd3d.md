# YAML Record Review: gauzes_synthetic_medium_no_1_with_18_nacl__0ec7cd3d

- Repository: CultureMech
- Record: data/merge_yaml/merged/gauzes_synthetic_medium_no_1_with_18_nacl__0ec7cd3d.yaml
- Started UTC: 2026-09-23T05:36:03Z
- Finished UTC: 2026-09-23T05:36:36Z
- Verdict: needs curation

## Target

Generated CultureMech:003226 is the direct MediaDive/JCM import for JCM 879, "GAUZE'S SYNTHETIC MEDIUM NO. 1 WITH 18% NaCl".

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The record is correctly grounded to `mediadive.medium:J879`, but it remains a singleton generated duplicate rather than being merged with the TOGO imports for the same JCM page.

TOGO M919 is the liquid high-salt form of JCM 879 and carries the same six base ingredients as this direct MediaDive/JCM record. TOGO M920 is the solid sibling that adds 18 g/L agar. The generated direct JCM record was not merged with either source, so CultureMech currently has three generated records for Gauze's Synthetic Medium No. 1 with 18% NaCl.

All primary ingredient ontology groundings are acceptable.

## Evidence

JCM medium 879 lists 20.0 g soluble starch, 180.0 g NaCl, 1.0 g KNO3, 0.5 g K2HPO4, 0.5 g MgSO4 x 7H2O, and 0.01 g FeSO4 x 7H2O, then instructs the curator to bring the volume to 1.0 L, adjust pH to 7.0-7.2, and add 18.0 g/L agar when preparing the solid medium.

MediaDive J879 has the same amounts, pH 7.1, and preparation steps, and marks the starch recipe item with the `soluble` attribute.

The generated YAML preserves the six base concentrations, `ph_value: 7.1`, and the three MediaDive preparation steps.

## Completeness

The generated record does not preserve MediaDive's `soluble` qualifier on starch; it reduces the row to preferred term `Starch` and CHEBI:28017 `starch`.

The JCM page-level autoclaving default, 121 C for 15 min unless otherwise stated, is absent.

The equivalent high-salt TOGO M919/M920 evidence is absent from `merged_from`.

## Findings

- Major: This direct JCM/MediaDive record is split from the equivalent TOGO M919 liquid import and the same-form/sibling TOGO M920 solid import, leaving duplicate generated records for the same source JCM medium.
- Minor: The starch row lost the upstream `soluble` qualifier.
- Minor: The KNO3 row still has the stale `mediaingredientmech_term` mapping instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.
- Minor: JCM's page-level default autoclave instruction was not captured.

## Recommended Edits

- Merge the direct MediaDive/JCM J879 record with the TOGO M919 liquid import for JCM_M879.
- Preserve the TOGO M920 JCM_M879-2 solid form as the 18 g/L agar variant of J879 rather than leaving it as an unrelated same-name record.
- Preserve the `soluble` starch qualifier in generated notes or preferred display text.
- Refresh the KNO3 MediaIngredientMech link to the CHEBI-keyed form.
- Carry JCM default autoclaving metadata into the normalized record or document why page-level defaults are intentionally omitted.

## Follow-up Checks

- Confirm that the regenerated high-salt liquid record merges MediaDive J879 and TOGO M919.
- Confirm that the high-salt solid record uses 18 g/L agar and is related to the liquid form without being merged with low-salt TOGO M72.
- Re-run strict, reference, term, and LinkML validation after regenerating the high-salt records.

## Additional Notes

None found
