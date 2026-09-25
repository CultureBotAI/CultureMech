# YAML Record Review: saltwater_medium_for_oceanic_aoa__5af9c5ef

- Repository: CultureMech
- Record: data/merge_yaml/merged/saltwater_medium_for_oceanic_aoa__5af9c5ef.yaml
- Started UTC: 2026-09-25T04:15:12Z
- Finished UTC: 2026-09-25T04:15:12Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002365`, `saltwater_medium_for_oceanic_aoa`, from `data/merge_yaml/merged/saltwater_medium_for_oceanic_aoa__5af9c5ef.yaml`.

The record is a single-source direct MediaDive/JCM J1198 import for `SALTWATER MEDIUM FOR OCEANIC AOA`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM Medium J1198.

No duplicate merge or synonym issue was found in the generated YAML.

## Evidence

JCM 1198 lists a parent saltwater base with 26 g NaCl, 5 g MgSO4 x 7H2O, 5 g MgCl2 x 6H2O, 1.5 g CaCl2 x 2H2O, 0.1 g KBr, and 980 ml distilled water.

After autoclaving and cooling, JCM 1198 adds six stock aliquots in order: 10 ml HEPES solution from JCM 1004, 5 ml 3 mM KH2PO4 solution, 2 ml 1 M NaHCO3 solution, 1 ml Modified trace element mixture from JCM 1004, 1 ml 7.5 mM FeNaEDTA solution at pH 7.0, and 1 ml 1 M NH4Cl solution.

JCM 1198 then checks pH 7.2, adds freshly prepared filter-sterilized catalase to a final 5-10 units/ml, and cultivates in glass or polystyrene containers in the dark without shaking.

JCM 1004 defines HEPES solution as a separate 500 ml stock made from 12 g NaOH and 119.2 g HEPES free acid, and defines Modified trace element mixture as a separate trace-metal stock with 12.5 ml 25% HCl, 30 mg H3BO3, 100 mg MnCl2 x 4H2O, 190 mg CoCl2 x 6H2O, 24 mg NiCl2 x 6H2O, 2 mg CuCl2 x 2H2O, 144 mg ZnSO4 x 7H2O, 36 mg Na2MoO4 x 2H2O, and 987 ml distilled water.

## Completeness

The saltwater base salts are present.

The 980 ml distilled-water base row is absent.

The HEPES, KH2PO4, NaHCO3, Modified trace element mixture, FeNaEDTA, and NH4Cl stocks are flattened into parent ingredient rows instead of modeled as six aseptic solution additions.

Catalase is preserved only as preparation prose, not as a structured ingredient or stock addition.

## Findings

The generated direct MediaDive record misreads post-autoclave aliquot volumes as final grams per liter. `KH2PO4` is 5 g/L instead of 5 ml/L of a 3 mM stock, `NaHCO3` is 2 g/L instead of 2 ml/L of a 1 M stock, `FeNa-EDTA` is 1 g/L instead of 1 ml/L of a 7.5 mM stock, and `NH4Cl` is 1 g/L instead of 1 ml/L of a 1 M stock.

The JCM 1004 HEPES stock was flattened into the parent medium, which turns 12 g NaOH and 119.2 g HEPES per 500 ml stock into final `G_PER_L` parent rows.

The JCM 1004 Modified trace element mixture was also flattened into the parent medium. The generated record therefore treats 25% HCl volume and trace-metal stock-strength milligram rows as final gram-per-liter concentrations.

The parent saltwater base lost its 980 ml distilled-water row.

The generated HEPES preparation step belongs to the HEPES stock, not directly to the finished JCM 1198 medium.

## Recommended Edits

Repair the direct MediaDive J1198 normalized source so it has a saltwater base plus six solution aliquots: HEPES solution, 3 mM KH2PO4 solution, 1 M NaHCO3 solution, Modified trace element mixture, 7.5 mM FeNaEDTA solution, and 1 M NH4Cl solution.

Move the JCM 1004 HEPES and Modified trace element mixture formulas into nested solution scopes and preserve the JCM 1198 aliquots as milliliters per liter.

Add the 980 ml distilled-water base component from JCM 1198.

Preserve catalase as a freshly prepared, filter-sterilized final addition with its 5-10 units/ml activity note.

Regenerate the merge layer after the normalized MediaDive J1198 source is repaired.

## Follow-up Checks

Confirm no regenerated direct parent ingredient has `KH2PO4` 5 g/L, `NaHCO3` 2 g/L, `FeNa-EDTA` 1 g/L, `NH4Cl` 1 g/L, `NaOH` 12 g/L, `HEPES` 119.2 g/L, or `HCl` 12.5 g/L.

Confirm the HEPES stock preparation note remains tied to the HEPES solution and not to the final saltwater medium.

Confirm the final generated medium still records pH 7.2, fresh filter-sterilized catalase, glass or polystyrene containers, dark cultivation, and no shaking.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
