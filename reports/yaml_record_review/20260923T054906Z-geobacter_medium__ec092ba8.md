# YAML Record Review: geobacter_medium__ec092ba8

- Repository: CultureMech
- Record: data/merge_yaml/merged/geobacter_medium__ec092ba8.yaml
- Started UTC: 2026-09-23T05:48:18Z
- Finished UTC: 2026-09-23T05:49:06Z
- Verdict: needs curation

## Target

Generated CultureMech:006023 merges KOMODO Medium 579 with the direct DSMZ Medium 579 import for "GEOBACTER MEDIUM".

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The KOMODO/DSMZ `SOURCE_DUPLICATE` merge is appropriate: KOMODO_579_GEOBACTER_MEDIUM states DSMZ Medium 579 provenance and matches the direct DSMZ 579 normalized record.

The main-medium ingredients have plausible small-molecule groundings. NiCl2 x 6H2O is grounded to anhydrous CHEBI:34887 `nickel dichloride`, so the nickel chloride hydration state is too weak.

## Evidence

DSMZ 579 defines a 1011 ml final medium with 13.70 g ferric citrate, 1.50 g NH4Cl, 0.60 g NaH2PO4, 0.10 g KCl, 2.50 g Na-acetate, 10.00 ml Modified Wolin's mineral solution, 2.50 g NaHCO3, 1.00 ml Wolin's vitamin solution (10x), and 1000.00 ml distilled water.

DSMZ then defines Modified Wolin's mineral solution as a separate 1 L stock and Wolin's vitamin solution (10x) as a separate 1 L stock. MediaDive preserves those same boundaries as separate solution IDs 241 and 5980.

The generated record includes the DSMZ main-medium preparation text, inoculum note, and Modified Wolin's mineral preparation text, but it has no `preparation_steps` for the 10x vitamin stock.

## Completeness

The generated record flattens the two stock recipes into direct ingredients and drops the direct 10 ml/L Modified Wolin and 1 ml/L Wolin vitamin stock-addition rows.

All three 1000 ml distilled-water rows are absent: main medium, Modified Wolin's mineral solution, and Wolin's vitamin solution (10x).

The DSMZ/MediaDive 1011 ml final volume is only implicit in the normalized main-medium g/L values.

## Findings

- Major: Modified Wolin's mineral solution was expanded at stock strength even though DSMZ adds only 10 ml/L to the final Geobacter medium.
- Major: Wolin's vitamin solution (10x) was expanded at stock strength even though DSMZ adds only 1 ml/L to the final Geobacter medium, inflating vitamin rows by approximately 1000-fold relative to final-medium concentration.
- Major: Source stock additions and all final-volume water rows were dropped, so the generated record has no way to distinguish main-medium ingredients from stock definitions.
- Minor: NiCl2 x 6H2O is linked to an anhydrous nickel dichloride CHEBI term.

## Recommended Edits

- Preserve the 10 ml/L Modified Wolin's mineral solution and 1 ml/L Wolin's vitamin solution (10x) additions as stock rows, or pre-dilute their internal components by the documented addition volumes.
- Preserve final-volume rows for the 1011 ml main medium and both 1 L stocks as context, not direct solutes.
- Carry Wolin's vitamin solution stock metadata instead of leaving vitamin stock preparation empty.
- Re-ground hydrated nickel chloride if a specific hexahydrate term is available.

## Follow-up Checks

- Confirm that regenerated vitamin concentrations reflect a 1 ml/L 10x stock addition rather than undiluted 10x stock concentrations.
- Confirm that regenerated Modified Wolin mineral rows are diluted 100-fold if expanded.
- Re-run strict, reference, term, and LinkML validation after regenerating the merged DSMZ/KOMODO 579 record.

## Additional Notes

None found
