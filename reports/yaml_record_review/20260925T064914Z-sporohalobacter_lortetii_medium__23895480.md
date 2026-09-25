# YAML Record Review: sporohalobacter_lortetii_medium__23895480

- Repository: CultureMech
- Record: data/merge_yaml/merged/sporohalobacter_lortetii_medium__23895480.yaml
- Started UTC: 2026-09-25T06:47:37Z
- Finished UTC: 2026-09-25T06:49:14Z
- Verdict: needs curation

## Target

Reviewed the generated record for DSMZ Medium 319, `SPOROHALOBACTER LORTETII MEDIUM`, assigned `CultureMech:001420`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a DSMZ/MediaDive import for `mediadive.medium:319`. MediaDive identifies medium 319 as `SPOROHALOBACTER LORTETII MEDIUM`, source `DSMZ`, pH 6.5, complex medium, and links it to the DSMZ Medium 319 PDF.

The merge also records `data/normalized_yaml/bacterial/KOMODO_319_SPOROHALOBACTER_LORTETII_medium.yaml` as a `SOURCE_DUPLICATE` child with `CultureMech:005007`. The KOMODO child points back to DSMZ Medium 319 and carries the same flattened ingredient signature, plus a variable `NaOH` pH-adjuster and `Sporohalobacter lortetii` target organism metadata that the DSMZ parent does not carry.

## Evidence

The DSMZ PDF and MediaDive REST payload agree on the Medium 319 hierarchy: main solution 319 uses 1000 ml water, 10 ml `Modified Wolin's mineral solution`, 2 ml FeSO4 stock, 0.5 ml sodium resazurin stock, and 1 ml `Wolin's vitamin solution (10x)`. The generated target preserves the main-solution rows and preparation text, including the anoxic 100% N2 handling, the pH 6.5 adjustment before dispensing, the post-sterilization magnesium/calcium/vitamin additions, and the separate mineral-solution pH-adjustment note.

The generated target does not preserve the stock-solution dilution. It imports the full 1 L concentrations from `Modified Wolin's mineral solution` as final-medium `G_PER_L` values even though only 10 ml of that stock are added to the main solution. It also imports the full 1 L concentrations from `Wolin's vitamin solution (10x)` as final-medium `G_PER_L` values even though only 1 ml of that stock is added.

## Completeness

All named DSMZ stock ingredients are represented, and the source duplicate relationship to the KOMODO extraction is explicit. Distilled-water rows are omitted, which is consistent with the generated representation elsewhere.

The formula is not quantitatively complete because nested MediaDive stock recipes are represented at their stock concentrations instead of their diluted final concentrations.

## Findings

- High: The MediaDive stock solutions were flattened without aliquot dilution. Rows derived from the 10 ml `Modified Wolin's mineral solution` stock are roughly 100x too concentrated in the final-medium record, and rows derived from the 1 ml `Wolin's vitamin solution (10x)` stock are roughly 1000x too concentrated.
- Medium: The duplicate merge sums main-solution contributions with undiluted stock concentrations for `NaCl`, `FeSO4 x 7 H2O`, and `CaCl2 x 2 H2O`. For example, the target records `NaCl` as 104.653 g/l from MediaDive's 103.653 g/l main contribution plus the mineral stock's full 1.0 g/l concentration, rather than adding only the small contribution from a 10 ml stock aliquot.

## Recommended Edits

- Fix the MediaDive import or normalization logic so nested solution components are multiplied by the aliquot volume over final main-solution volume before they become final-medium `G_PER_L` concentrations.
- Regenerate `data/normalized_yaml/bacterial/sporohalobacter_lortetii_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_319_SPOROHALOBACTER_LORTETII_medium.yaml`, and the generated merge records for DSMZ/KOMODO Medium 319 after stock-solution scaling is corrected.
- Recompute duplicate ingredient merges for `NaCl`, `FeSO4 x 7 H2O`, and `CaCl2 x 2 H2O` from scaled child amounts, preserving the main-solution and stock-solution provenance in notes if duplicate rows are collapsed.

## Follow-up Checks

- After regeneration, confirm that the liquid medium still excludes the optional agar, CaCO3, and soluble starch from DSMZ's agar-medium note.
- Confirm that the KOMODO child continues to merge as a `SOURCE_DUPLICATE` and that its variable `NaOH` pH-adjuster does not overwrite the DSMZ parent recipe.

## Additional Notes

None found
