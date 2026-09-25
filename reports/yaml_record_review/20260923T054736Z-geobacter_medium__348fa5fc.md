# YAML Record Review: geobacter_medium__348fa5fc

- Repository: CultureMech
- Record: data/merge_yaml/merged/geobacter_medium__348fa5fc.yaml
- Started UTC: 2026-09-23T05:46:40Z
- Finished UTC: 2026-09-23T05:47:36Z
- Verdict: needs curation

## Target

Generated CultureMech:010375 is the TOGO M951 import for JCM_M907, "Geobacter Medium".

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The TOGO:M951 identity is correct for the current JCM GRMD 907 recipe.

The separate MediaDive/JCM J907 normalized record has the same medium number but represents a 920 ml / Fe-NTA import that lacks the current 1.0 M sodium fumarate addition; it should be reconciled manually rather than blindly merged into M951.

The DSMZ/KOMODO `geobacter_medium` records are same-title records for other Geobacter media and are not duplicates of JCM 907.

All base salts are grounded plausibly. N2 and CO2 are grounded as gas ingredients, but the 80:20 v/v gas-mixture ratio is not structured.

## Evidence

JCM 907 and TOGO M951 list 910 ml distilled water, 0.147 g CaCl2 x 2H2O, 0.136 g KH2PO4, 0.535 g NH4Cl, 0.204 g MgCl2 x 6H2O, 0.82 g sodium acetate, 0.142 g Na2SO4, 10 ml Trace element solution, 10 ml Trace vitamins, 1 ml Se/W solution, an N2-CO2 80:20 v/v autoclave atmosphere, 30 ml 8% NaHCO3, 10 ml 1.0 M sodium fumarate, and 50 ml Iron(III) citrate solution.

JCM says to mix and autoclave under N2-CO2, add the post-cooling solutions aseptically and anaerobically, adjust pH to 7.0-7.2 if necessary, and optionally replace Iron(III) citrate solution with filter-sterilized Fe NTA solution from Medium 1355.

## Completeness

The base salts and water row are present at their source amounts.

All six stock additions are present only as empty `solutions` entries and the source ml amounts were changed to `G_PER_L`.

The pH range, anaerobic/autoclave/addition instructions, gas-mixture ratio, and Iron(III) citrate / Fe NTA replacement note are absent.

## Findings

- Major: Trace element solution, Trace vitamins, Se/W solution, 8% NaHCO3 solution, 1.0 M sodium fumarate solution, and Iron(III) citrate solution have source amounts in ml/L but are encoded as 10, 10, 1, 30, 10, and 50 g/L.
- Major: The cross-referenced M235, M190, M278, and M1072 stock compositions are unresolved empty arrays.
- Major: pH 7.0-7.2, N2-CO2 80:20 v/v, anaerobic post-cooling addition, and the Iron(III) citrate replacement note were dropped.
- Minor: The direct MediaDive/JCM J907 normalized record is split from this TOGO/JCM record even though both point at GRMD 907; the two source versions differ enough to need manual reconciliation.

## Recommended Edits

- Preserve the six post-cooling solution additions with ml/L units and structured cross-references to M235, M190, M278, M1072, and M1355 where applicable.
- Add preparation steps for N2-CO2 autoclaving, anaerobic additions, pH 7.0-7.2 adjustment, and optional Fe NTA replacement.
- Preserve the 80:20 v/v gas-mixture ratio rather than independent variable N2 and CO2 rows.
- Review the MediaDive/JCM J907 variant against the current JCM 907 page before deciding whether it should merge, supersede, or remain separate.

## Follow-up Checks

- Confirm that regenerated `solutions` entries no longer use `G_PER_L` for ml source additions.
- Confirm that the direct JCM/MediaDive record's 920 ml / Fe-NTA formulation does not overwrite the TOGO M951 910 ml / fumarate / Iron(III) citrate formulation.
- Re-run strict, reference, term, and LinkML validation after regenerating the record.

## Additional Notes

None found
