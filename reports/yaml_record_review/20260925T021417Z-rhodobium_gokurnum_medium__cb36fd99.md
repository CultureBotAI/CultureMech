# YAML Record Review: rhodobium_gokurnum_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodobium_gokurnum_medium__cb36fd99.yaml`
- Started UTC: 2026-09-25T02:14:16Z
- Finished UTC: 2026-09-25T02:14:31Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002867` for JCM Medium J516 / `mediadive.medium:J516`, merged from `rhodobium_gokurnum_medium`, `marichromatium_imhoffii_medium`, and `modified_rhodobacter_spaeroides_medium`.

## Validation

- Open schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The target ID, label, and `mediadive.medium:J516` grounding agree with JCM and MediaDive for Rhodobium gokurnum medium. An ignored-inclusive search for the exact `mediadive.medium:J516`, `mediadive.medium:J517`, and `mediadive.medium:J588` IDs found the expected maintained owner records, generated target source IDs, and merge manifest rows.

`J517` is not an exact source duplicate of `J516`: JCM Medium 517 and MediaDive J517 define Marichromatium imhoffii medium as Rhodobium gokurnum medium with 0.5 to 1.0 mM Na2S. `J588` is a real concentration variant of the same basic recipe; JCM Medium 588 changes MgCl2 x 6H2O, NaCl, NH4Cl, CaCl2 x 2H2O, yeast extract, and pH relative to J516.

## Evidence

JCM Medium 516 and MediaDive J516 list 0.5 g KH2PO4, 1.0 g MgCl2 x 6H2O, 20.0 g NaCl, 0.6 g NH4Cl, 0.15 g CaCl2 x 2H2O, 3.0 g sorbitol, 3.0 g sodium pyruvate, 0.4 g yeast extract, 5.0 ml 0.1% ferric citrate solution, 1.0 L distilled water, and pH 6.8. The post-autoclave row is 1.0 ml Trace element solution SL7, and SL7 itself contains 1.0 ml 25% HCl, 70.0 mg ZnCl2, 100.0 mg MnCl2 x 4H2O, 60.0 mg H3BO3, 200.0 mg CoCl2 x 6H2O, 20.0 mg CuCl2 x 2H2O, 20.0 mg NiCl2 x 6H2O, 40.0 mg Na2MoO4 x 2H2O, and 1.0 L distilled water per stock.

The generated target instead emits ferric citrate as a 5 g/L final ingredient, omits final distilled water, omits the 1 ml/L SL7 stock row, and emits HCl plus all SL7 salts as final-medium ingredients at their stock concentrations.

## Completeness

J516 is missing its 1 L final distilled water row, its 1 ml Trace element solution SL7 row, and the nested SL7 stock water. The J517 and J588 relationships also need regeneration after their maintained owners stop sharing the flattened J516 ingredient signature.

Empty optional literature and organism fields are not defects for this imported JCM medium.

## Findings

- Major: the generated final recipe flattens stocks from `data/normalized_yaml/bacterial/rhodobium_gokurnum_medium.yaml`. JCM J516 lists 5 ml 0.1% ferric citrate solution and 1 ml SL7 stock; the generated record reports `Ferric citrate` as `5 G_PER_L` and reports every SL7 component as a top-level final-medium ingredient.
- Major: water and stock topology are incomplete in `data/normalized_yaml/bacterial/rhodobium_gokurnum_medium.yaml`. The imported owner and generated target have no final distilled-water row, no 1 ml/L `Micronutrient solution SL7` row, and no nested SL7 stock with its own 1 L water basis.
- Major: `data/normalized_yaml/bacterial/marichromatium_imhoffii_medium.yaml` is misclassified as a `SOURCE_DUPLICATE` of J516. Its own JCM source says to use Medium 516 with 0.5 to 1.0 mM Na2S, so the source duplicate merge drops a chemically consequential sulfide addition.
- Major: `data/normalized_yaml/bacterial/modified_rhodobacter_spaeroides_medium.yaml` is a concentration variant, not a synonym of J516. The maintained owner already records `CONCENTRATION_VARIANT`, but the generated target still lists `mediadive.medium:J588` as a synonym and includes J588 in `merged_from`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/rhodobium_gokurnum_medium.yaml` so the J516 main solution includes final distilled water, 5 ml/L 0.1% ferric citrate solution, and 1 ml/L Micronutrient solution SL7 instead of flattening those stocks.
- Add the nested SL7 stock recipe, including 1 ml 25% HCl, the seven trace salts, and 1 L distilled water.
- Change `data/normalized_yaml/bacterial/marichromatium_imhoffii_medium.yaml` from `SOURCE_DUPLICATE` to a variant of J516 that explicitly preserves the 0.5 to 1.0 mM Na2S addition.
- Regenerate `data/merge_yaml/merged` so J517 and J588 are represented as variants of J516, not duplicate source synonyms merged into the J516 target.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for regenerated J516, J517, and J588 records.
- Compare the regenerated J516 final-medium rows against JCM Medium 516 and confirm SL7 components are only nested under the SL7 stock.
- Confirm the regenerated J517 record retains the Na2S addition.
- Confirm the regenerated J516 record keeps J588 only as a concentration variant child, not as a duplicate synonym.

## Additional Notes

The generated target's J588 concentration-variant relationship is directionally correct. The defect is that the merge product still treats that child variant as one of the J516 duplicate source records.
