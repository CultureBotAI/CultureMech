# YAML Record Review: desulfocarbo_indianensis_medium__1088b609

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfocarbo_indianensis_medium__1088b609.yaml`
- Started UTC: 2026-09-22T18:30:02Z
- Finished UTC: 2026-09-22T18:30:02Z
- Verdict: needs curation

## Target

Generated bacterial `desulfocarbo_indianensis_medium` record for MediaDive/JCM Medium J1020.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is correctly grounded to MediaDive medium J1020 / JCM Medium J1020, `DESULFOCARBO INDIANENSIS MEDIUM`.

An exact ignored-file search found one separate TOGO M1081 same-name import. This generated record has a single `merged_from` source and is the MediaDive/JCM import.

The defined, bacterial, liquid classification is supported by the live source recipe.

## Evidence

The generated direct main-medium rows match MediaDive's J1020 normalization against a 1085 ml final volume: Na2SO4, NaCl, MgCl2 x 6 H2O, KCl, NH4Cl, KH2PO4, CaCl2 x 2 H2O, Fe(NH4)2(SO4)2 x 6 H2O, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, sodium benzoate, and resazurin are scaled from the JCM table.

The source also contains 9.3 mg NiCl2 x 6 H2O directly, 10 ml Trace element solution from JCM 187, and 10 ml Trace vitamins from JCM 197.

The trace-element and vitamin stocks were flattened into top-level final-medium rows at their stock concentrations. ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and all JCM 197 vitamin rows are in `ingredients` instead of nested stock scopes.

Flattening also merged the 0.00857143 g/L direct NiCl2 x 6 H2O row with the 0.024 g/L stock Trace element row into one 0.03257143 G_PER_L top-level ingredient.

The post-cooling additions are mis-modeled: 60 ml of 8% NaHCO3 is represented as `60` G_PER_L, and 5 ml of 5% Na2S x 9 H2O is represented as `5` G_PER_L.

The 1 L source water row is absent.

## Completeness

The N2-CO2 dispensing, Balch-type-tube autoclaving, and aseptic anaerobic post-cooling addition instruction survived.

The post-cooling table rows and the JCM 187 / JCM 197 stock links did not survive as structured milliliter additions.

Filter-sterilization for the 8% bicarbonate addition and autoclaving for the 5% sulfide addition are absent.

## Findings

- Major issue: JCM 187 Trace element solution and JCM 197 Trace vitamins are flattened into the final recipe at stock concentration.
- Major issue: direct NiCl2 and trace-stock NiCl2 were merged into a single top-level ingredient even though they come from different scopes.
- Major issue: 60 ml 8% NaHCO3 and 5 ml 5% Na2S x 9 H2O use raw addition volumes as G_PER_L final concentrations.
- Major issue: the 1 L source water component is missing.
- Minor issue: stock-addition sterilization notes for bicarbonate and sulfide are dropped.

## Recommended Edits

- Rebuild the normalized source record from JCM 1020, MediaDive J1020, or TOGO M1081 with explicit milliliter additions for Trace element solution, Trace vitamins, 8% NaHCO3, and 5% Na2S x 9H2O.
- Move JCM 187 trace elements and JCM 197 vitamins under nested stock records.
- Preserve the direct 9.3 mg NiCl2 x 6 H2O row separately from the JCM 187 Trace element solution NiCl2 row.
- Compute bicarbonate and sulfide final concentrations from stock strengths and addition volumes.
- Restore the 1 L distilled-water row or an equivalent main-solution total-volume representation.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after restructuring the record.
- Confirm NiCl2 x 6 H2O appears in both direct and trace-stock scopes without duplicate merging.
- Confirm the corrected top-level ingredient list contains no JCM 187 or JCM 197 stock ingredients.
- Compare the direct MediaDive/JCM record against TOGO M1081 before any same-name deduplication.

## Additional Notes

JCM GRMD 1020, MediaDive REST medium J1020, and TOGO M1081 were reachable during review.
