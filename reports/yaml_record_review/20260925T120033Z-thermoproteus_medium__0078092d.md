# YAML Record Review: thermoproteus_medium__0078092d

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoproteus_medium__0078092d.yaml
- Started UTC: 2026-09-25T12:00:33Z
- Finished UTC: 2026-09-25T12:00:33Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:009232`, `thermoproteus_medium`, generated from TOGO Medium M2677 and ultimately sourced from ATCC Medium 1538.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoproteus_medium__0078092d.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The TOGO M2677 record points to an ATCC Medium 1538 PDF for "Thermoproteus medium". The fetched ATCC document defines a three-solution medium plus a separate Trace Elements stock, so its parts are not top-level final solutes.

## Evidence

- ATCC Medium 1538 combines 500 ml Solution A, 450 ml Solution B, and 50 ml Solution C, equilibrates them under 97% N2 and 3% H2, adjusts final pH to 4.8-5.6 with H2SO4, and stores completed medium under the same gas mixture.
- Solution A contains 490 ml distilled water, the sulfate/phosphate salts, yeast extract, glucose, resazurin 1.0 mg, and 10 ml Trace Elements; it is filter sterilized.
- Solution B contains 10.0 g sulfur in 450 ml water and is autoclaved at 100 C for 30 min on 3 consecutive days.
- Solution C contains 850.0 mg Na2S x 9H2O in 50 ml water and is autoclaved at 121 C for 15 min.
- Trace Elements is a 1 L stock with milligram-scale Mo, Mn, Zn, Cu, Co, borate, and vanadyl salts adjusted to pH 3.0.

## Completeness

The generated record lists the names of the ATCC Solution A, Solution B, Solution C, and Trace Elements ingredients, but it flattens all solution boundaries, merges water across stocks, omits all preparation instructions, omits pH 4.8-5.6, and records source volumes as G_PER_L values in the `solutions` array.

## Findings

- `Distilled water` 991 G_PER_L merges 490 ml, 450 ml, 50 ml, and 1 L water rows across Solution A, Solution B, Solution C, and Trace Elements.
- Solution B sulfur and Solution C Na2S x 9H2O are not top-level direct solutes; they belong to 450 ml and 50 ml stocks.
- `Resazurin` 1 G_PER_L copies 1.0 mg as grams per liter.
- Trace Elements milligram rows were copied as G_PER_L values and flattened even though Solution A receives 10 ml of that stock.
- The `solutions` entries store 500 ml, 450 ml, 50 ml, and 10 ml source additions as 500, 450, 50, and 10 G_PER_L.
- The 97% N2 / 3% H2 gas atmosphere and final pH 4.8-5.6 are absent from structured fields.

## Recommended Edits

- Rebuild the record with Solution A, Solution B, Solution C, and Trace Elements as stock-scoped structures.
- Move Solution B sulfur and Solution C Na2S x 9H2O out of the top-level final ingredient list.
- Fix all milligram-to-G_PER_L conversions for resazurin and Trace Elements.
- Add pH 4.8-5.6 and the ATCC filter-sterilization, tyndallisation, autoclaving, aseptic-combination, gas-equilibration, and storage steps.

## Follow-up Checks

- Confirm whether 500 + 450 + 50 ml should be treated as an exact 1 L final assembly before deriving final concentrations.
- Check whether ATCC Medium 1538 already exists under another source ID before adding repaired stock structure.

## Additional Notes

No target-organism evidence was reviewed. The exact source search included ignored and hidden files and found only the expected TOGO M2677 normalized source for this record.
