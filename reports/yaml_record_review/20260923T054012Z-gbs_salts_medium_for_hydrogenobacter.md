# YAML Record Review: gbs_salts_medium_for_hydrogenobacter

- Repository: CultureMech
- Record: data/merge_yaml/merged/gbs_salts_medium_for_hydrogenobacter.yaml
- Started UTC: 2026-09-23T05:39:32Z
- Finished UTC: 2026-09-23T05:40:12Z
- Verdict: needs curation

## Target

Generated CultureMech:015844 is the direct JCM import for GRMD 1366, "GBS SALTS MEDIUM FOR HYDROGENOBACTER".

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The medium identity and `jcm.grmd:1366` grounding are correct.

The main salt rows are grounded to appropriate hydrated or anhydrous CHEBI terms.

Mineral solution A, 8% NaHCO3 solution, 1.0 M Na2S2O3 solution, and 0.5 M Na2HPO4 solution are ungrounded stock/additive rows. Mineral solution A is explicitly cross-referenced to JCM Medium 1353 but has no structured link to that recipe.

## Evidence

JCM 1366 lists 3.0 g NaCl, 0.15 g KCl, 0.3 g Na2SO4, 0.123 g MgSO4 x 7H2O, 14.5 mg CaCl2 x 2H2O, 0.107 g NH4Cl, 5.0 ml Mineral solution A from Medium No. 1353, and 1.0 L distilled water.

After mixing, the medium is distributed under N2, sealed, autoclaved, cooled, and amended per liter with 12.5 ml 8% NaHCO3 solution, 2.5 ml 1.0 M Na2S2O3 solution, and 20.0 ml 0.5 M Na2HPO4 solution at pH 8.0.

After inoculation, JCM instructs addition of air to 30-40% of the gas phase followed by pressurization to 100 KPa with H2-CO2 at 4:1 v/v.

The generated record preserves those basal and post-autoclave ingredient rows and both preparation steps.

## Completeness

The cross-reference from Mineral solution A to Medium No. 1353 is only retained as prose inside `preferred_term`. The generated record has no structured pointer to the stock source or its composition.

The three post-autoclave stocks are represented as solution rows, which is source-faithful, but they have no ontology grounding or parsed final concentration equivalents.

No final pH is declared in JCM 1366; the only explicit pH is for the 0.5 M Na2HPO4 stock, and the generated record correctly does not promote that stock pH to the whole medium.

## Findings

- Major: The 1.0 L distilled-water final volume was encoded as `1.0 ML_PER_L`.
- Major: Mineral solution A is a resolvable JCM 1353 stock cross-reference but is left as an ungrounded free-text ingredient with no structured stock source.
- Minor: The NaHCO3, Na2S2O3, and Na2HPO4 solution rows are ungrounded stock solutions; their concentration labels are preserved only in `preferred_term`.

## Recommended Edits

- Convert the 1.0 L distilled-water row to final-volume context instead of `1.0 ML_PER_L`.
- Represent Mineral solution A as a 5.0 ml/L stock addition linked to its JCM 1353 definition.
- Add ontology grounding or structured stock-solution metadata for the 8% NaHCO3, 1.0 M Na2S2O3, and 0.5 M Na2HPO4 additions.
- Preserve the gas-phase instructions exactly as post-inoculation preparation metadata.

## Follow-up Checks

- Confirm that resolving Mineral solution A does not inline its 1 L stock recipe at stock strength as direct final-medium ingredients.
- Confirm that the final record does not assign pH 8.0 to the whole medium.
- Re-run strict, reference, term, and LinkML validation after regenerating the record.

## Additional Notes

None found
