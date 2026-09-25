# YAML Record Review: fervidicoccus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fervidicoccus_medium__f5f6a020.yaml
- Started UTC: 2026-09-23T03:16:30Z
- Finished UTC: 2026-09-23T03:18:22Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:009236` / `fervidicoccus_medium`, the TOGO M2681 import for Fervidicoccus Medium.
- Confirmed that this generated record comes from `data/normalized_yaml/archaea/TOGO_M2681_Fervidicoccus_Medium.yaml`.
- Cross-checked TOGO M2681 against its cited DSMZ 395b PDF and the equivalent MediaDive REST payload for DSMZ medium 395b.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/fervidicoccus_medium_f5f6a020.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The medium identity is coherent: `media_term` is `TOGO:M2681`, the source note cites the TOGO M2681 page, and TOGO M2681 cites DSMZ medium 395b as its original URL.
- The record is not the same source as same-slug `data/normalized_yaml/archaea/fervidicoccus_medium.yaml`, which is a separate DSMZ 395b MediaDive import with CultureMech ID `CultureMech:001504`.
- Direct salt CHEBI groundings are mostly appropriate, but `HCl (25%; 7.7 M)`, Trypticase peptone, Yeast extract, Carbon dioxide gas, Nitrogen gas, N2 gas, and the three solution entries lack complete `mediaingredientmech_chebi_term` coverage.
- `D-Ca-pantothenate` is grounded as `CHEBI:31345` but lacks a mirrored `mediaingredientmech_chebi_term` entry.

## Evidence

- TOGO M2681 carries a `ph` value of 6.0-6.1 and includes comments for the anoxic sparge, Hungate-tube or serum-vial dispensing, autoclaving, post-autoclave stock additions, filter sterilization of vitamins, and pH adjustment of the complete medium.
- The DSMZ 395b PDF and MediaDive 395b payload expose the same preparation text and pH range.
- The main DSMZ 395b recipe adds Trace element solution SL-10 at 1 ml/L and Wolin's vitamin solution (10x) at 1 ml/L; TOGO M2681 exposes Trace element solution SL-10 at 1 ml/L and Vitamin solution at 10 ml/L.
- The imported record keeps `solutions` rows for Na-resazurin solution, Trace element solution SL-10, and Vitamin solution, but records their addition volumes as `G_PER_L` instead of `ML_PER_L`.
- The imported record also flattens the 990 ml stock water from SL-10 and 1000 ml stock water from the vitamin solution into the top-level water row, producing 2990.0 `G_PER_L`.

## Completeness

- The generated record omits the source pH range entirely.
- The generated record has no `preparation_steps`, so the anoxic handling, autoclave, stock-addition, filter-sterilization, and pH-readjustment instructions from TOGO, DSMZ, and MediaDive are lost.
- No organisms were asserted in this generated recipe; target organism coverage was not evaluated for this stock-boundary review.

## Findings

- Needs curation: `ph_range` 6.0-6.1 is source-asserted in TOGO and DSMZ but absent from the generated record.
- Needs curation: source preparation instructions are absent, including the 80% N2 / 20% CO2 sparge, anoxic dispensing, autoclaving, sterile post-autoclave stock additions, vitamin filtration, and complete-medium pH adjustment.
- Needs curation: the three solution additions imported from TOGO use `G_PER_L` despite source `ml` units: Na-resazurin solution should be 0.5 ml/L, Trace element solution SL-10 should be 1 ml/L, and Vitamin solution should be 10 ml/L.
- Needs curation: nested Trace element solution SL-10 and Vitamin solution components were flattened into top-level ingredients at stock strength. Trace-element milligram rows became huge gram-per-liter values, vitamin milligram rows likewise became gram-per-liter values, and two stock water rows were merged into direct medium water.
- Needs curation: N2 gas from the vitamin stock preparation context is represented as a top-level variable-concentration ingredient, even though the stock was only prepared under a 100% N2 atmosphere.

## Recommended Edits

- Reparse or hand-curate `data/normalized_yaml/archaea/TOGO_M2681_Fervidicoccus_Medium.yaml` so top-level `ingredients` contain only final-medium components and top-level `solutions` preserve source ml/L addition volumes.
- Restore `ph_range` with `min: 6.0` and `max: 6.1`.
- Add preparation steps capturing the TOGO/DSMZ anoxic sparge, autoclave, post-autoclave stock additions, vitamin filtration, bicarbonate/sulfide handling, and final pH adjustment.
- Either preserve nested SL-10 and vitamin stock recipes as proper stock compositions or leave them out of top-level `ingredients`; do not promote their water and mg-scale subingredients as direct final-medium grams per liter.
- Re-evaluate whether variable gas rows should be retained as ingredients or moved into preparation context.

## Follow-up Checks

- After curation, rerun open-schema, strict, reference, and term validation on the generated M2681 YAML.
- Confirm Na-resazurin solution, Trace element solution SL-10, and Vitamin solution all use `ML_PER_L`.
- Confirm the regenerated file no longer has 2990.0 `G_PER_L` water or stock-strength vitamin and trace-element rows as top-level direct ingredients.
- Compare the repaired Togo import with `data/normalized_yaml/archaea/fervidicoccus_medium.yaml`, the DSMZ 395b MediaDive import, to decide whether they should remain separate records or be reconciled as source duplicates.

## Additional Notes

- This defect is present in the normalized TOGO M2681 source as well as the generated merge; fix the normalized source or the TOGO import logic before regenerating derived YAML.
