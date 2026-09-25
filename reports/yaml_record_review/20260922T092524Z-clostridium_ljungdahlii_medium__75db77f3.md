# YAML Record Review: Clostridium Ljungdahlii Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_ljungdahlii_medium__75db77f3.yaml`
- Started UTC: `2026-09-22T09:25:24Z`
- Finished UTC: `2026-09-22T09:25:48Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:009604` for TOGO Medium `M3134`, generated from `data/normalized_yaml/bacterial/TOGO_M3134_Clostridium_Ljungdahlii_Medium.yaml` on merge fingerprint `75db77f3d31ddfc38cc6a866c1430b1e1b225b5cd4287f1035f4d7b893df86c0`.

The stated source is DSMZ Medium 879, `CLOSTRIDIUM LJUNGDAHLII MEDIUM`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_ljungdahlii_medium__75db77f3.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The record is recognizable as TOGO `M3134` for DSMZ Medium 879, but it is not merged with the direct DSMZ/KOMODO generated branch `data/merge_yaml/merged/CLOSTRIDIUM_LJUNGDAHLII_MEDIUM.yaml`, which points to the same DSMZ PDF.

Several stock ingredients have been merged with parent-medium ingredients under a single CHEBI term. `MgSO4 x 7 H2O` is stored as `3.2 G_PER_L` from the sum of the final-medium 0.2 g and Modified Wolin mineral-stock 3.0 g rows; `NaCl` is stored as `1.8 G_PER_L` from the sum of the final-medium 0.8 g and mineral-stock 1.0 g rows. `CaCl2 x 2 H2O` from the final medium and the mineral stock also need separate contexts.

`NiCl2 x 6 H2O` is still grounded to generic nickel dichloride. `D-Fructose` retains a legacy `mediaingredientmech_term`, and `Calcium D-(+)-pantothenate` has no CHEBI-keyed MediaIngredientMech link.

## Evidence

The TOGO API reports `M3134` as `Clostridium Ljungdahlii Medium`, cites the DSMZ Medium 879 PDF, and carries pH `5.9`.

The DSMZ Medium 879 PDF states final pH 5.9 and final volume 1011 ml. Its base formula uses 1000 ml water, 10 ml Modified Wolin's mineral solution, 0.5 ml 0.1% sodium resazurin, 1 ml Wolin's vitamin solution (10x), base salts, fructose, yeast extract, bicarbonate, cysteine, and sulfide. Modified Wolin's mineral solution and Wolin's vitamin solution are separate one-liter stocks.

DSMZ also documents two variants: for DSM 13641, replace fructose with 5 g/l sucrose, increase NaHCO3 to 2.50 g/l, and adjust the complete medium to pH 6.9; for DSM 115981, omit yeast extract.

## Completeness

The record is missing source facts that are visible in TOGO and DSMZ:

- No `ph_value: 5.9` is present.
- The anoxic 80% N2 / 20% CO2 preparation, 121 C for 15 min autoclaving, 100% N2 stock handling, and final pH adjustment instructions are absent.
- DSM 13641 and DSM 115981 variants are absent.
- Modified Wolin's mineral solution and Wolin's vitamin solution are empty `solutions` shells instead of structured stock compositions.
- KOH is represented as an empty variable-concentration solution rather than as a pH adjustment reagent inside the mineral stock preparation.

## Findings

- Three distinct water rows were collapsed into `Distilled water` at `3000.0 G_PER_L`: 1000 ml final-medium water, 1000 ml Modified Wolin mineral-stock water, and 1000 ml Wolin vitamin-stock water.
- `MgSO4 x 7 H2O` and `NaCl` combine final-medium masses with mineral-stock masses, yielding impossible `3.2 G_PER_L` and `1.8 G_PER_L` concentrations in the parent formula.
- Source milliliter aliquots were moved into `solutions` with gram-per-liter units: Modified Wolin's mineral solution is `10 G_PER_L` instead of 10 ml/l, Wolin's vitamin solution is `1 G_PER_L` instead of 1 ml/l, and 0.5 ml resazurin remains a parent `0.5 G_PER_L` ingredient.
- Modified Wolin mineral-stock internals are flattened into final `ingredients`; `Nitrilotriacetic acid` `1.5 G_PER_L`, `MnSO4 x H2O` `0.5 G_PER_L`, `FeSO4 x 7 H2O` `0.1 G_PER_L`, `CoSO4 x 7 H2O` `0.18 G_PER_L`, `ZnSO4 x 7 H2O` `0.18 G_PER_L`, `Na2SeO3 x 5 H2O` `0.3 G_PER_L`, and `Na2WO4 x 2 H2O` `0.4 G_PER_L` are stock-composition rows, not final-medium rows.
- Wolin vitamin-stock internals are likewise inflated from source mg/l values to gram-per-liter final ingredients, including `Biotin` `20 G_PER_L`, `Pyridoxine hydrochloride` `100 G_PER_L`, `Vitamin B12` `1 G_PER_L`, and `p-Aminobenzoic acid` `50 G_PER_L`.
- `N2` and `Carbon dioxide gas` are stored as variable ingredients even though they describe preparation atmospheres, not final-medium chemical concentrations.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/TOGO_M3134_Clostridium_Ljungdahlii_Medium.yaml` or the TOGO import logic, then regenerate; `data/merge_yaml/merged/clostridium_ljungdahlii_medium__75db77f3.yaml` is derived.
- Keep the parent DSMZ Medium 879 formula separate from Modified Wolin's mineral solution and Wolin's vitamin solution.
- Represent the 10 ml mineral, 1 ml vitamin, and 0.5 ml resazurin aliquots as volume additions rather than gram-per-liter concentrations.
- Add pH 5.9 and the DSMZ anaerobic preparation steps.
- Model DSM 13641 and DSM 115981 as explicit variants.
- Reconcile this TOGO branch with the direct DSMZ/KOMODO branch once both represent stock solutions consistently.
- Re-ground nickel chloride hexahydrate and replace or add stale MediaIngredientMech links where CHEBI-keyed links are missing.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm no stock water is merged into final-medium water.
- Confirm MgSO4, NaCl, and CaCl2 from the base and Modified Wolin stock are not summed across solution boundaries.
- Confirm Wolin vitamin stock rows keep milligram units in the stock composition and do not appear as gram-per-liter final ingredients.
- Confirm DSM 13641 and DSM 115981 source differences survive regeneration as variant metadata.

## Additional Notes

Empty optional fields are not defects. The critical curation boundary is the nested solution structure: DSMZ 879 is a parent formula that consumes stock aliquots, not a single flat ingredient table.
