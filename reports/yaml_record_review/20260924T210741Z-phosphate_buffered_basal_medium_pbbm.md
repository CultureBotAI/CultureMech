# YAML Record Review: phosphate_buffered_basal_medium_pbbm

- Repository: CultureMech
- Record: data/merge_yaml/merged/phosphate_buffered_basal_medium_pbbm.yaml
- Started UTC: 2026-09-24T21:07:41Z
- Finished UTC: 2026-09-24T21:07:41Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:009311
- Name: phosphate_buffered_basal_medium_pbbm
- Source import: phosphate_buffered_basal_medium_pbbm
- Primary external ID: TOGO:M2760
- Source URL: `https://togomedium.org/medium/M2760`

This generated record represents TOGO Medium M2760, Phosphate-buffered basal medium (Pbbm).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/phosphate_buffered_basal_medium_pbbm.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the right TOGO identity, and an exact ignored-file search across `data` found only this normalized source and this merged record for `TOGO:M2760` / `togomedium.org/medium/M2760`.

The major problem is recipe structure, not identity. TOGO M2760 defines the final basal medium, a Trace mineral stock, a Vitamin solution stock, and a Phosphate buffer stock. The generated YAML exposes the Trace mineral and Vitamin solution stock components as top-level final-medium rows and keeps the same stocks as solution stubs with `G_PER_L` concentrations.

Several groundings also need cleanup once the stock boundaries are restored:

- `MgSO4 . 2H2O`, `Thiamine . HCl`, and `Pyridoxine . HCl` are ungrounded.
- `CoCl2 . 6H2O` is grounded to generic cobalt dichloride rather than the hexahydrate.
- `NiSO4 . 6H2O` is grounded to generic nickel sulfate rather than the hexahydrate.

## Evidence

- TOGO M2760 lists the final medium with 944 ml water, 1 ml 0.02% resazurin solution, 25 ml 2.5% Na2S x 9H2O solution, 2 g yeast extract, 0.9 g NaCl, 0.2 g CaCl2 x 2H2O, 1 g NH4Cl, 20 mM glucose, 0.2 g MgSO4 . 2H2O, 10 ml Trace mineral, 10 ml Vitamin solution, and 10 ml Phosphate buffer.
- The same TOGO payload defines Trace mineral as a separate 1 L stock containing NaCl, CaCl2, boric acid, FeSO4, MnCl2, CoCl2, CuCl2, ZnCl2, NTA, Na2SeO3, NiSO4, and Na2MoO3.
- TOGO defines Vitamin solution as a separate 1 L stock containing milligram amounts of biotin, p-aminobenzoic acid, thiamine HCl, pyridoxine HCl, folic acid, cyanocobalamine, riboflavin, nicotinic acid, pantothenic acid, and lipoic acid.
- TOGO defines Phosphate buffer (1 M, pH 7.2) as 10 ml of 1 M KH2PO4 plus 10 ml of 1 M Na2HPO4.

## Completeness

The generated record is incomplete as a curated medium because it flattens source stocks into the final recipe:

- `Trace mineral` is stored as 10 G_PER_L and its one-liter ingredients are also present as top-level ingredients.
- `Vitamin solution` is stored as 10 G_PER_L in `solutions`, and the milligram-scale vitamin stock rows are also top-level ingredients with `G_PER_L` units.
- `Phosphate buffer (1 M, pH 7.2)` is stored as 10 G_PER_L, and the two 1 M buffer solution rows are also top-level 10 G_PER_L ingredients.
- Base NaCl and CaCl2 are summed with Trace mineral stock NaCl and CaCl2, producing 1.9 G_PER_L NaCl and 0.30000000000000004 G_PER_L CaCl2 x 2H2O.
- Source water was summed across the final medium, Trace mineral stock, and Vitamin solution stock.
- TOGO metadata pH 7.2 is absent from `ph_value`.
- The alternate H2-CO2 carbon source with KHCO3 is present only in TOGO comments and not represented in the generated recipe.

## Findings

1. Stock-solution internals were copied into the base recipe and assigned final-medium units.
2. Duplicate cleanup crossed source boundaries by summing base NaCl/CaCl2/water with Trace mineral and Vitamin stock rows.
3. Vitamin rows were imported as grams per liter even though the source amounts are milligrams in a 1 L stock that contributes only 10 ml to the final medium.
4. The phosphate buffer is structurally wrong: the generated record has both `Phosphate buffer (1 M, pH 7.2)` as 10 G_PER_L and its two 1 M stock components as 10 G_PER_L final rows.
5. The source pH 7.2 did not populate the structured `ph_value`.
6. Several hydrate-specific salts and vitamin salts are ungrounded or grounded only to generic ChEBI terms.

## Recommended Edits

- Rebuild TOGO M2760 with Trace mineral, Vitamin solution, and Phosphate buffer as nested 10 ml stock additions.
- Keep NaCl, CaCl2 x 2H2O, and water rows inside Trace mineral separate from base-medium NaCl, CaCl2 x 2H2O, and water.
- Convert vitamin milligram stock amounts through the 10 ml stock addition before deriving final concentrations.
- Represent the 1 ml resazurin stock and 25 ml sulfide stock as solution additions, not as `G_PER_L` masses.
- Add structured pH 7.2 from TOGO metadata.
- Add or repair groundings for magnesium sulfate dihydrate, thiamine hydrochloride, pyridoxine hydrochloride, cobalt chloride hexahydrate, and nickel sulfate hexahydrate.
- Preserve the H2-CO2 plus KHCO3 optional carbon-source variant in a schema-appropriate way if CultureMech supports variants.

## Follow-up Checks

- Regenerate merged YAML and verify that only `TOGO:M2760` remains for PBBM.
- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M2760` and `togomedium.org/medium/M2760` with ignored files included to confirm no duplicate normalized source was added.
- Spot-check the rendered page to ensure Trace mineral, Vitamin solution, and Phosphate buffer are displayed as stocks rather than flattened final rows.

## Additional Notes

None found.
