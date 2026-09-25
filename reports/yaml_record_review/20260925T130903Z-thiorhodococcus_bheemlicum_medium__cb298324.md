# YAML Record Review: thiorhodococcus_bheemlicum_medium__cb298324

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiorhodococcus_bheemlicum_medium__cb298324.yaml`
- Started UTC: 2026-09-25T13:09:03Z
- Finished UTC: 2026-09-25T13:09:03Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002910`
- Name: `thiorhodococcus_bheemlicum_medium`
- Source grounding: direct JCM/MediaDive Medium J561 merged with JCM J562 and J570 references

## Validation

- Schema validation: passed with no issues.
- Strict validation: passed with zero errors; `/private/tmp/thiorhodococcus_bheemlicum_medium__cb298324.strict.tsv` was header-only.
- Reference validation: passed with zero checks.
- Term validation: passed after the known EUtils warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The canonical record is grounded to `mediadive.medium:J561`, JCM Medium 561.
- The merge also includes JCM J562, `LAMPROBACTER ROSEUS MEDIUM`, and JCM J570, `ALLOCHROMATIUM RENUKAII MEDIUM`.
- The exact source search found only J561, J562, and J570 in this generated merge group; the search included ignored and hidden files.

## Evidence

- JCM 561 is a 1021 ml parent recipe with 0.5 g KH2PO4, 0.15 g CaCl2 x 2 H2O, 2.0 g MgSO4 x 7 H2O, 0.34 g NH4Cl, 20 g NaCl, 0.4 g yeast extract, 3 g sodium pyruvate, 1 ml Micronutrient solution SL7, 5 ml ferric citrate at 0.1% w/v, 15 ml NaHCO3 at 10% w/v, final 1 mM Na2S x 9 H2O, final 6 mM Na2S2O3 x 5 H2O, and 1 L water.
- Micronutrient solution SL7 is a 1001 ml stock containing 1 ml HCl at 25% v/v, 70 mg ZnCl2, 100 mg MnCl2 x 4 H2O, 60 mg H3BO3, 200 mg CoCl2 x 6 H2O, 20 mg CuCl2 x 2 H2O, 20 mg NiCl2 x 6 H2O, 40 mg Na2MoO4 x 2 H2O, and 1 L water.
- JCM 562 is defined as Medium 561 supplemented with 1 ml/L vitamin B12 solution at 2 mg/100 ml.
- JCM 570 is defined as Medium 561 supplemented with 1 ml/L vitamin B12 solution at 2 mg/ml.

## Completeness

- The generated record includes the J561 main rows, final sulfide and thiosulfate conversions, and SL7 ingredients.
- The generated merged record has no vitamin B12 row or variant to distinguish J562 and J570.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- The 1 ml Micronutrient solution SL7 stock is flattened at stock strength into final ingredient rows.
- HCl is represented as `1` `G_PER_L`, even though the source SL7 row is 1 ml of 25% v/v HCl inside the stock solution.
- Ferric citrate is represented as `5` `G_PER_L`; the source is 5 ml of a 0.1% w/v stock in a 1021 ml parent.
- NaHCO3 is represented as `15` `G_PER_L`; the source is 15 ml of a 10% w/v stock.
- J562 and J570 were merged as exact duplicates of J561 after copying the J561 composition, but both source media add vitamin B12 to J561.

## Recommended Edits

- Restore Micronutrient solution SL7 as a stock dosed at 1 ml in the J561 parent.
- Preserve ferric citrate and NaHCO3 as ml stock additions or convert them from the stated stock concentrations.
- Split J562 and J570 out of exact-duplicate status and model their vitamin B12 additions explicitly.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after stock and variant repair.
- Compare J562 and J570 carefully because their JCM vitamin B12 stock concentrations differ.

## Additional Notes

- Empty optional fields were not treated as defects.
