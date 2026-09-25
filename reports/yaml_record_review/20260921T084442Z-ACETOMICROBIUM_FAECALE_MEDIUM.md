# YAML Record Review: Acetomicrobium Faecale Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml
- Started UTC: 2026-09-21T08:43:17Z
- Finished UTC: 2026-09-21T08:44:42Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml`.
- Stable identifier: `CultureMech:007645`.
- Source identity asserted by the record: TOGO Medium `M1124`, imported from JCM `JCM_M1057`.
- The generated record is merged from only `TOGO_M1124_Acetomicrobium_Faecale_Medium` on fingerprint `76657360d6359908211afe4e70d8365399674854cee6f144ec650844e65f16fd`.
- Current authoritative source owner: `data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- JCM Medium 1057 resolves and identifies the source as `1057 ACETOMICROBIUM FAECALE MEDIUM`.
- The TOGO and direct JCM records point to the same JCM source: TOGO `M1124` states `Original source: JCM - JCM_M1057`, and the direct JCM owner uses `mediadive.medium:J1057`.
- A bounded gitignore-independent exact search for `TOGO:M1124`, `JCM_M1057`, `GRMD=1057`, `mediadive.medium:J1057`, `ACETOMICROBIUM_FAECALE_MEDIUM`, and `acetomicrobium_faecale_medium` found the expected TOGO owner, the expected direct JCM owner, their two split generated records, and the expected source-index rows.
- Adjacent `ACETOMICROBIUM_FAECALIS` records exist but come from DSMZ/JCM 412 and are a separate source family.

## Evidence

- JCM Medium 1057 directly lists 2.0 g Trypticase peptone, 2.0 g yeast extract, 4.0 g glucose, 0.225 g KH2PO4, 0.255 g K2HPO4, 0.255 g ammonium sulfate, 0.5 g NaCl, 0.1 g MgSO4.7H2O, 0.07 g CaCl2.2H2O, 5.0 g sodium acetate.3H2O, 1.0 mg resazurin, 1.0 L distilled water, then 6.0 g NaHCO3 and 0.5 g L-cysteine.HCl.H2O after boiling and cooling under N2-CO2.
- The generated TOGO record preserves most main-medium gram quantities but parses `Distilled water 1.0 L` as `1 G_PER_L`.
- The generated TOGO record parses `Resazurin 1.0 mg` as `1 G_PER_L` instead of `0.001 G_PER_L`.
- JCM adds `10.0 ml` Trace vitamins from JCM Medium 197 and `10.0 ml` Trace minerals solution to the final medium; the generated TOGO record moves these to three empty `solutions` entries with concentrations `10 G_PER_L`, `10 G_PER_L`, and `1 G_PER_L`.
- The source's Trace minerals solution is a stock made from 1 L of JCM Medium 151 trace minerals, 0.03 g NiCl2.6H2O, and 0.3 mg Na2SeO3.5H2O. The generated TOGO record places NiCl2.6H2O directly in the final recipe at `0.03 G_PER_L` and misreads the Na2SeO3.5H2O stock row as final `0.3 G_PER_L`.
- The direct JCM owner generated as `data/merge_yaml/merged/acetomicrobium_faecale_medium__7f3cefe7.yaml` represents the same GRMD 1057 page more completely but also flattens JCM Medium 197 and JCM Medium 151 stock components at stock strength.

## Completeness

- The generated TOGO record is incomplete because the Trace vitamins, Trace minerals solution, and nested JCM Medium 151 trace-minerals stock are empty solution placeholders.
- JCM preparation steps are absent from the TOGO-generated record.
- The direct JCM duplicate is split into a separate generated record instead of being reconciled with TOGO M1124.
- The generated TOGO record lacks pH and the explicit N2-CO2 pressure condition from the direct JCM preparation.

## Findings

- BLOCKER: the generated TOGO record has unit-conversion errors for `Distilled water`, `Resazurin`, and the nested Na2SeO3.5H2O stock row.
- BLOCKER: the generated TOGO record leaves the 10 ml/L JCM Medium 197 vitamin stock, the 10 ml/L trace-minerals stock, and the nested JCM Medium 151 stock as empty solution references.
- MAJOR: the generated TOGO record places NiCl2.6H2O and Na2SeO3.5H2O from the Trace minerals solution directly in the final recipe instead of preserving the 10 ml/L stock addition.
- MAJOR: TOGO M1124 and direct `mediadive.medium:J1057` are source duplicates but generate two separate `data/merge_yaml/merged` records.
- MAJOR: the direct JCM owner is a useful reconciliation source but also flattens JCM Medium 197 vitamins and JCM Medium 151 trace-minerals stock components at stock strength.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M1124_Acetomicrobium_Faecale_Medium.yaml` to convert liters and milligrams with volume units, not `G_PER_L`.
- Encode the 10 ml/L Trace vitamins, 10 ml/L Trace minerals solution, and nested 1 L JCM Medium 151 reference as real stock recipes instead of empty solution placeholders.
- Apply the same stock hierarchy to `data/normalized_yaml/bacterial/acetomicrobium_faecale_medium.yaml` and preserve its JCM preparation steps.
- Reconcile TOGO M1124 with `mediadive.medium:J1057` as source duplicates after both normalized owners represent the same nested stock hierarchy.
- Regenerate `data/merge_yaml/merged/ACETOMICROBIUM_FAECALE_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch JCM `GRMD=1057` and verify the final recipe preserves the two 10 ml/L additions, the nested trace-minerals stock, resazurin as 1 mg/L, and water as a volume.
- Re-run ignored-file-inclusive exact searches for `TOGO:M1124`, `mediadive.medium:J1057`, and `GRMD=1057` to confirm the repaired TOGO/direct-JCM owners generate one source-duplicate merge.

## Additional Notes

- Optional empty fields were not treated as defects.
