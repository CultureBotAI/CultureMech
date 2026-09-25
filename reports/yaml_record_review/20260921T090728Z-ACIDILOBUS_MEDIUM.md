# YAML Record Review: acidilobus_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDILOBUS_MEDIUM.yaml`
- Started UTC: 2026-09-21T09:06:07Z
- Finished UTC: 2026-09-21T09:07:28Z
- Verdict: needs curation

## Target

Generated merge record `ACIDILOBUS_MEDIUM.yaml` is a singleton merge from `data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml`. It represents TOGO M303, whose original source is JCM Medium 308 / ACIDILOBUS MEDIUM.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history` files.

## Identity and Grounding

TOGO M303 and the direct JCM J308 source point at the same JCM recipe: TOGO reports `original_media_id: JCM_M308`, and both records use `GRMD=308`. They are not currently merged. Exact `TOGO:M303` occurs in `ACIDILOBUS_MEDIUM.yaml`, while exact `mediadive.medium:J308` occurs only as a synonym inside `ACIDOLOBUS_ACETICUS_MEDIUM.yaml`.

That destination is suspect: ACIDILOBUS MEDIUM / JCM 308 is not the same named medium as ACIDOLOBUS ACETICUS MEDIUM, and the `acidilobus_medium` source should not disappear into an Acidolobus Aceticus generated record merely because both old imports flattened the same JCM 187 and JCM 197 stocks.

## Evidence

- Primary JCM source `GRMD=308`: source page fetched from JCM during review. It lists 1 ml FeCl2 solution from JCM Medium 187, 1 ml trace element solution from JCM Medium 187, 10 ml trace vitamins from JCM Medium 197, 1 mg resazurin, 1 L water, sulfur powder, Na2S.9H2O, and core salts; it then gives anaerobic handling under N2-CO2 80:20, separate yeast/sulfide/sulfur/vitamin sterilization, final pH 3.5-3.8 adjustment with sterile 1 N H2SO4, and 100 kPa N2-CO2 80:20 pressurization.
- TOGO M303 API fetched during review: preserves `JCM_M308`, pH 3.5-3.8, the three stock cross-reference rows, the gas additions, 1 N H2SO4, and the full JCM comment before CultureMech normalization drops the comment and turns the stock additions into empty `solutions`.
- Direct JCM normalized record `data/normalized_yaml/archaea/acidilobus_medium.yaml`: has `mediadive.medium:J308` and keeps the long anaerobic preparation step, but it flattened JCM 187 / JCM 197 stock contents into the parent recipe and now merges into `ACIDOLOBUS_ACETICUS_MEDIUM.yaml`.

## Completeness

The target preserves simple source ingredient labels and amounts but is missing the operational part of the medium. There is no pH 3.5-3.8 field, no preparation step, no N2-CO2 gas ratio, no sulfur steaming instruction, and no record that yeast extract, Na2S.9H2O, or trace vitamins must be sterilized separately.

It also leaves the three JCM stock additions empty and malformed: FeCl2 solution, trace element solution, and trace vitamins are `1`, `1`, and `10` `G_PER_L` entries rather than 1 ml, 1 ml, and 10 ml additions.

## Findings

- CRITICAL: The three JCM stock additions are represented as empty `solutions` with gram-per-liter units. JCM 308 calls for 1 ml FeCl2 solution, 1 ml trace element solution, and 10 ml trace vitamins; the target stores those volumes as 1, 1, and 10 `G_PER_L` and does not link them structurally to JCM Medium 187 or 197.
- MAJOR: TOGO M303 and the direct JCM J308 source are not reconciled. The direct JCM source was merged as a synonym into `ACIDOLOBUS_ACETICUS_MEDIUM.yaml`, while the source-equivalent TOGO record remains a singleton.
- MAJOR: The generated target drops pH 3.5-3.8 and the entire anaerobic preparation protocol, including separate autoclaving of 10% yeast extract and 5% Na2S.9H2O under N2, sulfur steaming for three successive days, N2-gassed trace-vitamin filtration, and 100 kPa N2-CO2 80:20 pressurization.
- MAJOR: `Resazurin 1 mg` was imported as `1 G_PER_L` rather than `0.001 G_PER_L`.
- MINOR: `Distilled water 1 L` was stored as `1 G_PER_L`; if retained, water should use a volume model rather than a mass concentration.

## Recommended Edits

- Re-curate `data/normalized_yaml/archaea/TOGO_M303_Acidilobus_Medium.yaml` with FeCl2 solution, trace element solution, and trace vitamins as 1 ml, 1 ml, and 10 ml stock additions linked to the corresponding JCM 187 and JCM 197 media.
- Restore pH 3.5-3.8 and the full JCM/TOGO anaerobic `preparation_steps` text, including the N2-CO2 ratio and separate treatment of yeast extract, Na2S.9H2O, sulfur, and vitamins.
- Convert resazurin from 1 mg/L to `0.001 G_PER_L` or an explicit milligram unit if the schema supports it.
- Pull `data/normalized_yaml/archaea/acidilobus_medium.yaml` out of the `ACIDOLOBUS_ACETICUS_MEDIUM` source-duplicate merge, repair its same stock-preserving structure, and regenerate so exact `TOGO:M303` and exact `mediadive.medium:J308` form an ACIDILOBUS MEDIUM merge.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the corrected TOGO M303 and JCM J308 normalized records and regenerated target.
- Re-run an ignored-inclusive exact search for `TOGO:M303`, `mediadive.medium:J308`, and `GRMD=308` to confirm JCM 308 is represented in one Acidilobus generated record and no longer in `ACIDOLOBUS_ACETICUS_MEDIUM`.
- Verify regenerated ACIDILOBUS MEDIUM has no empty stock `solutions` and no milliliter or milligram source rows represented as `G_PER_L`.

## Additional Notes

The direct JCM J308 import should not be used as-is for repair; although it preserved preparation text, it flattened the JCM 187 FeCl2 / trace-element and JCM 197 vitamin stocks into top-level ingredients.
