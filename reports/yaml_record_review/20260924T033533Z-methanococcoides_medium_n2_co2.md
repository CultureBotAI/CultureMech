# YAML Record Review: methanococcoides_medium_n2_co2
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanococcoides_medium_n2_co2.yaml
- Started UTC: 2026-09-24T03:33:54Z
- Finished UTC: 2026-09-24T03:35:34Z
- Verdict: needs curation

## Target
- ID: CultureMech:009201
- Name: methanococcoides_medium_n2_co2
- Label: Methanococcoides Medium (N2/CO2)
- Category: archaea
- Source: TOGO:M2644, sourced from DSMZ Medium 280
- Merge fingerprint: 1812cb72db4ffe24eaf6401e25f03bc717328482096aeefb2092b6fdc69c8eb1
- Merged from: TOGO_M2644_Methanococcoides_Medium_N2_CO2

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity matches TOGO M2644 and DSMZ Medium 280.
- The record still points to `mediadive.solution:6187` and `mediadive.solution:6241`, but DSMZ/MediaDive 280 uses solution 241, Modified Wolin's mineral solution, and solution 5980, Wolin's vitamin solution (10x). The 6187 and 6241 records are unrelated standalone stock recipes.
- Trimethylamine-HCl is ungrounded despite a source label of trimethylamine hydrochloride.
- `preferred_term: MgSO4 x 7 H2O` has a hydrate-specific primary CHEBI term but a stale `mediaingredientmech_chebi_term` for generic magnesium sulfate.
- `NiCl2 x 6 H2O` is grounded to generic nickel dichloride rather than a hydrate-specific term.

## Evidence
- DSMZ Medium 280 lists 10 ml of Modified Wolin's mineral solution, 2 ml of 0.1% Fe(NH4)2(SO4)2 x 6 H2O, 0.5 ml of 0.1% Sodium resazurin, 1 ml of Wolin's vitamin solution (10x), 0.5 g L-Cysteine HCl x H2O, 0.5 g Na2S x 9 H2O, 3 g Trimethylamine-HCl, and 1 L distilled water in the main formula.
- The DSMZ Modified Wolin stock is a 1 L stock containing NTA, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and water.
- The DSMZ Wolin vitamin 10x stock is a 1 L stock containing Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium D-(+)-pantothenate, Vitamin B12, p-Aminobenzoic acid, (DL)-alpha-Lipoic acid, and water.
- DSMZ instructs users to sparge the medium with 80% N2 and 20% CO2 for 30 to 45 minutes, add bicarbonate, adjust pH to 7.0, distribute under the same gas atmosphere before autoclaving, add trimethylamine, cysteine, and sulfide from sterile anoxic stocks autoclaved under 100% N2, prepare vitamins under N2 and filter-sterilize them, and adjust the complete medium to pH 7.0 to 7.2.
- The YAML has all stock children as top-level ingredients, five empty `Unknown solution` stubs, no preparation steps, and no pH value.

## Completeness
- The main formula salts, organics, and gases are present.
- The Modified Wolin mineral and Wolin vitamin stock recipes were flattened into final-medium scope rather than retained as stock solutions.
- The source preparation steps, pH instructions, gas ratios, and filter-sterilization instructions are absent.
- Empty optional fields are acceptable, but empty solution compositions for required stock additions make the recipe incomplete.

## Findings
- The stock hierarchy is lost. Modified Wolin mineral rows and Wolin vitamin rows were promoted to top-level ingredients, and the original stock additions remain as empty `Unknown solution` rows.
- The stock addition units are wrong. Sodium resazurin 0.5 ml, Fe(NH4)2(SO4)2 x 6 H2O solution 2 ml, trace-element stock 10 ml, and vitamin stock 10 ml are represented as `G_PER_L` quantities.
- Duplicate cleanup summed across stock boundaries. MgSO4 x 7 H2O is `6.45 G_PER_L` from 3.45 g final plus 3 g stock; NaCl is `19.0 G_PER_L` from 18 g final plus 1 g stock; and CaCl2 x 2 H2O is `0.24000000000000002 G_PER_L` from 0.14 g final plus 0.1 g stock. The normalized owner has repaired only the identical water sum.
- Two milligram trace-stock values were imported as grams per liter: 0.3 mg Na2SeO3 x 5 H2O became `0.3 G_PER_L`, and 0.4 mg Na2WO4 x 2 H2O became `0.4 G_PER_L`.
- The two solution references are wrong. DSMZ/MediaDive 280 uses Modified Wolin's mineral solution and Wolin's vitamin solution (10x), not `mediadive.solution:6187` or `mediadive.solution:6241`.
- KOH is a pH-adjustment reagent for the mineral stock, but the YAML represents `KOH solution` as a final `Unknown solution` with variable concentration.
- The source pH range, 80/20 N2/CO2 sparging, N2 handling of post-autoclave stocks, filter-sterile vitamin addition, and Hungate/serum-vial preparation text are absent.
- Trimethylamine-HCl, generic MgSO4, and generic NiCl2 grounding need cleanup.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/TOGO_M2644_Methanococcoides_Medium_N2_CO2.yaml` from DSMZ Medium 280 or MediaDive medium 280.
- Keep final-medium rows, Modified Wolin mineral stock rows, Wolin vitamin stock rows, 0.1% resazurin, and 0.1% Fe(NH4)2(SO4)2 x 6 H2O in their source scopes.
- Use volume additions for the source solution additions and remove `G_PER_L` from the 0.5 ml, 2 ml, and 10 ml solution rows.
- Replace the incorrect `mediadive.solution:6187` and `mediadive.solution:6241` references with local DSMZ 280 stock recipes or the correct MediaDive solution identities.
- Treat KOH as the Modified Wolin mineral stock pH adjuster, not as a final-medium stock addition.
- Restore source preparation text for anoxic sparging, autoclaving, N2 stock preparation, filter sterilization, Hungate/serum-vial dispensing, and pH 7.0 to 7.2.
- Ground trimethylamine-HCl and refresh stale MgSO4/NiCl2 CHEBI links.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanococcoides_medium_n2_co2.yaml`.
- Confirm that the regenerated final medium keeps 3.45 g/L MgSO4 x 7 H2O, 18 g/L NaCl, and 0.14 g/L CaCl2 x 2 H2O at final scope.
- Confirm that Modified Wolin rows, Wolin vitamin rows, and KOH no longer appear as top-level final ingredients.
- Confirm that no ml solution addition is represented as `G_PER_L` and no source mg quantity is inflated to whole-number grams per liter.
- Confirm that `mediadive.solution:6187`, `mediadive.solution:6241`, and `Unknown solution` are gone from this DSMZ 280 owner.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- MediaDive medium 280 reports a normalized main-solution volume of 1013 ml because the stock volumes are included in the final mixture. Either represent the DSMZ tabular amounts directly or document any normalization to final volume so downstream concentration values remain interpretable.
