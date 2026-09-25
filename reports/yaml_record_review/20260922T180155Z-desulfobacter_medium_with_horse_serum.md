# YAML Record Review: desulfobacter_medium_with_horse_serum

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfobacter_medium_with_horse_serum.yaml`
- Started UTC: 2026-09-22T18:01:55Z
- Finished UTC: 2026-09-22T18:01:55Z
- Verdict: pass with minor issues

## Target

Generated bacterial `desulfobacter_medium_with_horse_serum` record for JCM Medium J1475.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to JCM Medium J1475 and the live JCM page confirms the `DESULFOBACTER MEDIUM WITH HORSE SERUM` identity.

The complex/undefined classification is supported by Tryptone and horse serum.

The generated source was the newer direct JCM GRMD import, not a TOGO or MediaDive flattening pass, and the source media number was preserved.

## Evidence

The generated base recipe matches live JCM 1475: 3.0 g Na2SO4, 0.2 g KH2PO4, 0.3 g NH4Cl, 21.0 g NaCl, 3.0 g MgCl2 x 6H2O, 0.5 g KCl, 0.15 g CaCl2 x 2H2O, 10.0 g Tryptone, 1.0 ml FeCl2 solution, 1.0 ml Trace element solution, 1.0 mg Resazurin, and 920.0 ml Distilled water.

The post-cooling additions also match the JCM page as volumes rather than bogus gram amounts: 10.0 ml Horse Serum, 10.0 ml Trace vitamins, 50.0 ml 8% NaHCO3, and 8.0 ml 5% Na2S x 9H2O.

JCM 1475 currently points FeCl2 solution and Trace element solution to JCM Medium 187 and Trace vitamins to JCM Medium 197. Those cross-references are preserved in the ingredient names.

The top-level `ph_value` is `7.1`, but the live source says to adjust pH to 7.1-7.4 if necessary.

## Completeness

The N2-CO2 autoclaving step and the aseptic, anaerobic post-cooling addition step both survived.

The imported stock additions are intentionally opaque `ML_PER_L` rows rather than nested stock records. That is acceptable for a direct first-pass JCM scrape, but the referenced JCM 187 and JCM 197 formulas should eventually be resolved into structured stock solutions.

The `*` marker on Horse Serum, Trace vitamins, and 8% NaHCO3 solution is preserved only in ingredient names, not as an explicit filter-sterilization flag.

## Findings

- Minor issue: source pH 7.1-7.4 is reduced to `ph_value: 7.1`.
- Minor issue: JCM 187 and JCM 197 stock formulas are not nested under `solutions`.
- Minor issue: filter-sterilized post-cooling stocks are denoted only by `*` in `preferred_term`.

## Recommended Edits

- Store pH as `ph_range` 7.1-7.4.
- Resolve JCM 187 FeCl2 and Trace element stocks and JCM 197 Trace vitamins into nested solution records.
- Move the filter-sterilized marker from stock names into structured preparation or sterilization metadata.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after any structural normalization.
- Confirm the four post-cooling additions remain `ML_PER_L` additions, not mass concentrations.
- Confirm JCM 187 and JCM 197 still match the live JCM 1475 cross-references before nesting those stock recipes.

## Additional Notes

JCM GRMD 1475 was reachable during review.
