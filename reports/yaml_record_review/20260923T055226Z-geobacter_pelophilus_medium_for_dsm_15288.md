# YAML Record Review: geobacter_pelophilus_medium_for_dsm_15288

- Repository: CultureMech
- Record: data/merge_yaml/merged/geobacter_pelophilus_medium_for_dsm_15288.yaml
- Started UTC: 2026-09-23T05:51:28Z
- Finished UTC: 2026-09-23T05:52:26Z
- Verdict: needs curation

## Target

Generated CultureMech:009275 is the TOGO M2725 import for the DSM 15288 / DSM 16228 variant of DSMZ Medium 838.

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The TOGO:M2725 identity is appropriate for DSMZ 838 as modified for DSM 15288: the record omits the parent Na-acetate and Na-ascorbate rows and adds yeast extract, Na-DL-lactate, and Wolin's vitamin solution.

Most source labels are grounded plausibly, but MgSO4 x 7H2O still has a stale generic `mediaingredientmech_chebi_term`, NiCl2 x 6H2O is linked to anhydrous nickel dichloride, and Fe(III)-citrate (19% Fe) is ungrounded.

## Evidence

DSMZ 838 defines a 1002 ml basal Geoanaerobacter medium with ferric citrate, salts, 1 ml Trace element solution SL-11, 1 ml Selenite-tungstate solution, Na2CO3, Na-acetate, Na-ascorbate, and 1000 ml distilled water.

For DSM 15288 and DSM 16228, DSMZ says to omit Na-acetate and Na-ascorbate and to supplement the autoclaved medium with 10 ml/L Wolin's vitamin solution, 1 g/L Na-DL-lactate, and 1 g/L yeast extract from sterile anoxic stocks prepared under 100% N2.

DSMZ defines Trace element solution SL-11, Selenite-tungstate solution, and Wolin's vitamin solution as separate stock recipes with milligram-scale trace rows and separate 1000 ml distilled-water rows.

## Completeness

The generated record is stale relative to `data/normalized_yaml/bacterial/geobacter_pelophilus_medium_for_dsm_15288.yaml`: normalized YAML has already collapsed the four identical 1000 ml water rows back to one 1000 g/L row, while generated output still has the pre-repair 4000 g/L sum.

The generated `solutions` entries preserve only the 1, 1, and 10 source amounts, and each is incorrectly typed as `G_PER_L`.

The anoxic ferric-citrate dissolution, N2-CO2 sparging, post-autoclave stock additions, and trace-stock preparation instructions are absent.

## Findings

- Major: Four separate 1000 ml water rows from the basal medium and three stock recipes were merged into one 4000 g/L direct water row.
- Major: Trace element solution SL-11, Selenite-tungstate solution, and Wolin's vitamin solution were both left as 1/1/10 g/L `solutions` entries and flattened as direct final-medium ingredients.
- Major: Milligram stock ingredients were converted to grams per liter; for example CoCl2 x 6H2O is 190 mg in SL-11 but appears as 190 g/L, and Na2WO4 x 2H2O is 4 mg in Selenite-tungstate solution but appears as 4 g/L.
- Major: The Wolin vitamin stock was flattened at stock strength even though DSMZ adds only 10 ml/L.
- Major: Preparation instructions for anoxic handling and stock preparation were dropped.
- Minor: MgSO4 x 7H2O, NiCl2 x 6H2O, and Fe(III)-citrate groundings need cleanup.

## Recommended Edits

- Regenerate this derived record from the September-repaired normalized source so the 4000 g/L water sum is removed.
- Model SL-11, Selenite-tungstate solution, and Wolin's vitamin solution as stock additions with their own 1000 ml water rows, or pre-dilute their internal components by the documented 1, 1, and 10 ml/L addition volumes.
- Preserve DSMZ's DSM 15288 variant note and anoxic stock-preparation instructions as preparation metadata.
- Refresh MgSO4 x 7H2O and NiCl2 x 6H2O CHEBI-keyed links and ground Fe(III)-citrate if an appropriate term exists.

## Follow-up Checks

- Confirm that regenerated output no longer has 4000 g/L water.
- Confirm that no SL-11, Selenite-tungstate, or Wolin vitamin component appears at stock strength as a final-medium row.
- Re-run strict, reference, term, and LinkML validation after regenerating the record.

## Additional Notes

None found
