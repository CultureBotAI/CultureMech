# YAML Record Review: geobacter_nbaf_medium__db485dcd

- Repository: CultureMech
- Record: data/merge_yaml/merged/geobacter_nbaf_medium__db485dcd.yaml
- Started UTC: 2026-09-23T05:49:48Z
- Finished UTC: 2026-09-23T05:50:45Z
- Verdict: needs curation

## Target

Generated CultureMech:002490 is the direct MediaDive/JCM import for JCM 1327, "GEOBACTER NBAF MEDIUM".

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J1327` identity is correct, but the generated record remains split from TOGO M3002, another JCM_M1327 import.

Na2WO2 x 2H2O is an ungrounded typo in the direct MediaDive record; the JCM page and TOGO M3002 both have Na2WO4 x 2H2O. NiSO4 x 6H2O is linked to generic nickel sulfate rather than a hexahydrate-specific term.

The generated `ph_value: 8.2` appears to come from the NB Mineral elixir stock pH 8.0-8.5, not the final medium. The JCM final pH instruction says to check final pH around 7.0.

## Evidence

JCM 1327 lists basal KH2PO4, K2HPO4, NH4Cl, KCl, NaCl, CaCl2 x 2H2O, Fe2(SO4)3 x nH2O, MgSO4 x 7H2O, 1 ml 0.1% Na2SeO4, 10 ml NB Mineral elixir, and 900 ml distilled water.

After autoclaving under N2 and replacing the gas phase with N2-CO2 at 4:1 v/v, JCM adds 20 ml 8% NaHCO3, 10 ml 5% Na2CO3, 15 ml Trace vitamins, 15 ml 1 M sodium acetate, and 40 ml 1 M sodium fumarate from sterile anaerobic stocks.

The JCM NB Mineral elixir subsection contains a separate stock recipe and pH 8.0-8.5 adjustment step. The CoCl2 x 6H2O, ZnSO4 x 7H2O, CuCl2 x 2H2O, and AlK(SO4)2 rows carry malformed `vg` units in the JCM HTML, which TOGO leaves as variable but MediaDive imported as numeric stock-strength rows.

## Completeness

The generated preparation steps preserve the N2 autoclave, N2-CO2 replacement, sterile anaerobic additions, final pH check, and NB Mineral elixir pH-adjustment step.

All stock boundaries are lost: Na2SeO4, NB Mineral elixir, NaHCO3, Na2CO3, Trace vitamins, sodium acetate, and sodium fumarate are represented as direct ingredients instead of stock additions.

The 900 ml basal-water row and the NB Mineral elixir water/final-volume context are absent.

## Findings

- Major: The final medium is assigned pH 8.2 even though JCM 1327 instructs only the NB Mineral elixir stock to pH 8.0-8.5 and checks final medium pH around 7.0.
- Major: 1 ml 0.1% Na2SeO4, 20 ml 8% NaHCO3, 10 ml 5% Na2CO3, 15 ml 1 M sodium acetate, and 40 ml 1 M sodium fumarate were converted to 1, 20, 10, 15, and 40 g/L direct rows.
- Major: The 15 ml/L Trace vitamins stock was flattened at stock strength.
- Major: The 10 ml/L NB Mineral elixir stock was flattened at stock strength, and malformed `vg` source units were converted into g/L values for cobalt, zinc, copper, and aluminium salts.
- Major: The source Na2WO4 x 2H2O row is misspelled as Na2WO2 x 2H2O and left ungrounded.
- Major: The direct JCM/MediaDive record is split from the equivalent TOGO M3002 import.
- Minor: Na2SeO4 still has the stale `mediaingredientmech_term` link instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits

- Use final medium pH around 7.0 and keep pH 8.0-8.5 scoped to the NB Mineral elixir stock.
- Model Na2SeO4, NaHCO3, Na2CO3, Trace vitamins, sodium acetate, sodium fumarate, and NB Mineral elixir as stock additions with ml/L units.
- Resolve the JCM malformed `vg` trace-metal units before assigning any numeric mass units to CoCl2 x 6H2O, ZnSO4 x 7H2O, CuCl2 x 2H2O, or AlK(SO4)2.
- Correct Na2WO2 x 2H2O to Na2WO4 x 2H2O.
- Merge or cross-link the direct MediaDive/JCM J1327 and TOGO M3002 records after the source-unit conflict is resolved.
- Refresh the Na2SeO4 MediaIngredientMech link.

## Follow-up Checks

- Confirm that regenerated NBAF output has final pH 7.0 rather than 8.2.
- Confirm that none of the post-autoclave ml additions survive as g/L direct rows.
- Confirm that NB Mineral elixir trace metals are not expanded at stock strength into the final medium.
- Re-run strict, reference, term, and LinkML validation after curation.

## Additional Notes

None found
