# YAML Record Review: seleniivibrio_medium_arsenate

- Repository: CultureMech
- Record: data/merge_yaml/merged/seleniivibrio_medium_arsenate.yaml
- Started UTC: 2026-09-25T05:09:02Z
- Finished UTC: 2026-09-25T05:09:02Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:001634`, `seleniivibrio_medium_arsenate`, from `data/merge_yaml/merged/seleniivibrio_medium_arsenate.yaml`.

The target record is a direct MediaDive/DSMZ Medium 503d import for `SELENIIVIBRIO MEDIUM (ARSENATE)`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to MediaDive/DSMZ Medium 503d.

No same-source generated duplicate was found for the direct MediaDive DSMZ 503d import.

The KOMODO 503d family is represented under a separate TMAO3/TMPN3 recipe with strain-specific wrappers, not as another generated copy of DSMZ Medium 503d.

## Evidence

DSMZ Medium 503d defines a top-level medium made from 942 ml Solution A, 30 ml Solution B, 10 ml Solution C, 1 ml Solution D, 10 ml Solution E, and 10 ml Solution F.

Solution A contains 0.20 g KH2PO4, 0.25 g NH4Cl, 1.00 g NaCl, 0.40 g MgCl2 x 6H2O, 0.50 g KCl, 0.15 g CaCl2 x 2H2O, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 0.50 ml Sodium resazurin 0.1% w/v, and 940 ml Distilled water.

Solutions B, C, E, and F are separate anoxic stocks containing Na2CO3, Na-acetate, Na2HAsO4 x 7H2O, and Na2S x 9H2O, respectively.

Trace element solution SL-10, Seven vitamins solution, and Selenite-tungstate solution are nested stocks with their own 1000 ml preparations.

DSMZ Medium 503d uses 80% N2 / 20% CO2 for Solution A and Solution B and 100% N2 for Solutions C through F; Solutions D and E are filter-sterilized, and the finished medium is adjusted to pH 7.2 to 7.4 if necessary.

## Completeness

The generated record flattens the Solution A-F formulation and represents concentrated Solution B, C, E, and F stock ingredients as if they were direct final-medium g/L rows.

Trace element solution SL-10, Seven vitamins solution, and Selenite-tungstate solution are also flattened into parent ingredients.

All Distilled water rows from Solution A, Solution B, Solution C, Solution E, Solution F, Trace element solution SL-10, Seven vitamins solution, and Selenite-tungstate solution are absent.

The generated merge layer predates the partial August cocktail-nesting repair in `data/normalized_yaml/bacterial/seleniivibrio_medium_arsenate.yaml`.

The pH range 7.2 to 7.4 is preserved.

## Findings

Concentrated stock recipes were imported as direct final-medium ingredients.

The multi-solution DSMZ recipe was collapsed into a single flat ingredient list, losing Solution A-F addition volumes and the sequential completion procedure.

Trace, vitamin, and selenite-tungstate stock boundaries are missing from the generated record.

The normalized source still needs a complete repair: it nests Trace element solution SL-10 and four Seven vitamins rows, but Solution B, Solution C, Solution E, Solution F, Selenite-tungstate solution, and several vitamin and trace rows remain flattened.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/seleniivibrio_medium_arsenate.yaml` so the top-level medium contains Solution A-F with the DSMZ 942 ml, 30 ml, 10 ml, 1 ml, 10 ml, and 10 ml addition volumes.

Move Na2CO3, Na-acetate, Na2HAsO4 x 7H2O, and Na2S x 9H2O under Solutions B, C, E, and F instead of leaving their concentrated stock values as parent ingredients.

Nest the complete Trace element solution SL-10, Seven vitamins solution, and Selenite-tungstate solution compositions, including their source water rows and preparation notes.

Represent the 80% N2 / 20% CO2 and 100% N2 handling requirements in structured gas rows if the importer supports them; otherwise keep them in preparation prose.

Regenerate the merged YAML after the normalized source is fully repaired.

## Follow-up Checks

Confirm the regenerated parent no longer has 50 g/L Na2CO3, 80 g/L Na-acetate, 310 g/L Na2HAsO4 x 7H2O, or 30 g/L Na2S x 9H2O as direct final-medium ingredients.

Confirm Solution A retains 940 ml water and its 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, and 0.50 ml Sodium resazurin source additions.

Confirm all seven vitamin rows are under Seven vitamins solution, and NaOH, Na2SeO3 x 5H2O, and Na2WO4 x 2H2O are under Selenite-tungstate solution.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
