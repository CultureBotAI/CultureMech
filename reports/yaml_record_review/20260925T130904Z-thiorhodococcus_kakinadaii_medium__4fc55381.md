# YAML Record Review: thiorhodococcus_kakinadaii_medium__4fc55381

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiorhodococcus_kakinadaii_medium__4fc55381.yaml`
- Started UTC: 2026-09-25T13:09:04Z
- Finished UTC: 2026-09-25T13:09:04Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002909`
- Name: `thiorhodococcus_kakinadaii_medium`
- Source grounding: direct JCM/MediaDive import of JCM Medium J560, `THIORHODOCOCCUS KAKINADAII MEDIUM`

## Validation

- Schema validation: passed with no issues.
- Strict validation: passed with zero errors; `/private/tmp/thiorhodococcus_kakinadaii_medium__4fc55381.strict.tsv` was header-only.
- Reference validation: passed with zero checks.
- Term validation: passed after the known EUtils warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The record is grounded to `mediadive.medium:J560`.
- The live JCM GRMD 560 page resolved and agrees with the MediaDive J560 parent recipe.
- No second JCM J560 generated record was found by the exact source search; the search included ignored and hidden files.

## Evidence

- JCM 560 is a 1021 ml parent recipe with 0.5 g KH2PO4, 0.05 g CaCl2 x 2 H2O, 1.0 g MgSO4 x 7 H2O, 0.34 g NH4Cl, 20 g NaCl, 0.6 g yeast extract, 3 g sodium pyruvate, 1 ml Micronutrient solution SL7, 5 ml ferric citrate at 0.1% w/v, 15 ml NaHCO3 at 10% w/v, final 3 mM Na2S x 9 H2O, and 1 L water.
- Micronutrient solution SL7 is referenced from JCM Medium 533 and contains 1 ml HCl at 25% v/v plus mg quantities of ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 1 L water.
- The parent recipe is adjusted to pH 7.0 and is autoclaved before the filter-sterilized NaHCO3 and Na2S x 9 H2O solutions are added.

## Completeness

- The generated record includes the parent ingredients, final sulfide conversion, SL7 stock ingredients, and post-autoclave addition instruction.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- The 1 ml Micronutrient solution SL7 dose is flattened at stock strength into final ingredient rows.
- HCl is represented as `1` `G_PER_L`, but it is a 1 ml 25% v/v component of the SL7 stock.
- Ferric citrate is represented as `5` `G_PER_L`; JCM 560 specifies 5 ml of a 0.1% w/v stock.
- NaHCO3 is represented as `15` `G_PER_L`; JCM 560 specifies 15 ml of a 10% w/v stock.

## Recommended Edits

- Restore Micronutrient solution SL7 as a stock dosed at 1 ml in the parent recipe.
- Preserve ferric citrate and NaHCO3 as filter-sterilized stock additions or convert them from their stated stock concentrations.
- Keep the parent pH 7.0 step separate from SL7 stock composition.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after stock repair.
- Compare the repaired J560 recipe against J561 so shared SL7 stock handling stays consistent.

## Additional Notes

- Empty optional fields were not treated as defects.
