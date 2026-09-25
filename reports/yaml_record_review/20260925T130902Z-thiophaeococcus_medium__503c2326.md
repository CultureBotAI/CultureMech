# YAML Record Review: thiophaeococcus_medium__503c2326

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiophaeococcus_medium__503c2326.yaml`
- Started UTC: 2026-09-25T13:09:02Z
- Finished UTC: 2026-09-25T13:09:02Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002996`
- Name: `thiophaeococcus_medium`
- Source grounding: direct JCM/MediaDive import of JCM Medium J650, `THIOPHAEOCOCCUS MEDIUM`

## Validation

- Schema validation: passed with no issues.
- Strict validation: passed with zero errors; `/private/tmp/thiophaeococcus_medium__503c2326.strict.tsv` was header-only.
- Reference validation: passed with zero checks.
- Term validation: passed after the known EUtils warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The record is grounded to `mediadive.medium:J650`.
- The live JCM GRMD 650 page resolved and agrees with the MediaDive J650 source.
- No second JCM J650 generated record was found by the exact source search; the search included ignored and hidden files.

## Evidence

- JCM 650 is a 1012 ml recipe with 0.5 g KH2PO4, 0.15 g CaCl2 x 2 H2O, 2.0 g magnesium sulfate hydrate, 0.64 g NH4Cl, 20 g NaCl, 0.4 g yeast extract, 3 g sodium pyruvate, 1 ml Trace element solution SL8, 10 ml NaHCO3 at 10% w/v, 1 ml vitamin B12 at 2 mg/ml, 1 mM Na2S x 9 H2O, 6 mM Na2S2O3 x 5 H2O, and 1 L water.
- The source uses final concentrations for sulfide and thiosulfate, so the generated 0.240182 g/L and 1.48912 g/L conversions are plausible.
- Trace element solution SL8 is a 1 L stock referenced from JCM Medium 190 and dosed at 1 ml.
- The JCM 190 SL8 stock contains 5.2 g EDTA-2Na, 1.5 g FeCl2 x 4 H2O, 70 mg ZnCl2, 100 mg MnCl2 x 4 H2O, 62 mg H3BO3, 190 mg CoCl2 x 6 H2O, 17 mg CuCl2 x 2 H2O, 24 mg NiCl2 x 6 H2O, 36 mg Na2MoO4 x 2 H2O, and 1 L water.

## Completeness

- The generated record includes the main ingredients, SL8 stock ingredients, final sulfide and thiosulfate, and the post-autoclave addition instruction.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- The 1 ml Trace element solution SL8 stock is flattened into final ingredients at stock concentrations.
- NaHCO3 is recorded as `10` `G_PER_L`; the source row is 10 ml of a 10% w/v stock.
- Vitamin B12 is recorded as `1` `G_PER_L`; the source row is 1 ml of a 2 mg/ml solution.
- The source magnesium sulfate hydrate should be checked manually because the JCM page is missing a separator in `MgSO4 7H2O` and the generated record currently uses generic magnesium sulfate.

## Recommended Edits

- Model Trace element solution SL8 as a 1 L stock dosed at 1 ml in the 1012 ml parent recipe.
- Preserve NaHCO3 and vitamin B12 as explicit stock additions or convert them from the stated ml stock doses.
- Review the magnesium sulfate hydrate label and CHEBI grounding against the JCM page before editing the record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after stock repair.
- Compare the repaired JCM 650 record with DSMZ 1162 to prevent accidental exact-duplicate merging of related but nonidentical recipes.

## Additional Notes

- Empty optional fields were not treated as defects.
