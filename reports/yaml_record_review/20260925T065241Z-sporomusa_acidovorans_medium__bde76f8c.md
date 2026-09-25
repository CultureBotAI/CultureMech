# YAML Record Review: sporomusa_acidovorans_medium__bde76f8c

- Repository: CultureMech
- Record: data/merge_yaml/merged/sporomusa_acidovorans_medium__bde76f8c.yaml
- Started UTC: 2026-09-25T06:50:54Z
- Finished UTC: 2026-09-25T06:52:41Z
- Verdict: needs curation

## Target

Reviewed the generated record for DSMZ Medium 311c, `SPOROMUSA ACIDOVORANS MEDIUM`, assigned `CultureMech:001412`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a DSMZ/MediaDive import for `mediadive.medium:311c`. MediaDive identifies medium 311c as `SPOROMUSA ACIDOVORANS MEDIUM`, source `DSMZ`, pH 6.5 to 7.0, final volume 1005 ml, and links it to the DSMZ Medium 311c PDF.

The generated record preserves the DSMZ pH range, the primary MediaDive identity, most direct main-medium solutes, and the DSMZ preparation text for anoxic 80% N2 plus 20% CO2 sparging, post-autoclave stock additions, carbonate stock handling, fructose/vitamin filtration, and final pH adjustment.

## Evidence

DSMZ and MediaDive list three nested stocks that should enter Medium 311c as 1 ml aliquots: `Trace element solution SL-10`, `Selenite-tungstate solution`, and `Wolin's vitamin solution (10x)`. In the generated target, every solute from those nested 1 L stock recipes was flattened at its full stock concentration instead of being diluted by the 1 ml over 1005 ml aliquot factor.

The direct main-medium rows are scaled to MediaDive's 1005 ml final volume. For example, 0.50 g `NH4Cl` becomes 0.497512 g/l, 5.00 g `D-Fructose` becomes 4.97512 g/l, 0.30 g `Na2S x 9 H2O` becomes 0.298507 g/l, and 0.50 ml of 0.1 percent sodium resazurin becomes 0.000497512 g/l.

## Completeness

The generated record includes all named DSMZ base and stock ingredients, preparation text for the base medium and trace element stock, and the pH range. Distilled-water rows are omitted, which is consistent with the generated representation elsewhere.

The formula is not quantitatively complete because nested MediaDive stock recipes are represented at their stock concentrations instead of their diluted final concentrations.

## Findings

- High: The MediaDive stock solutions were flattened without aliquot dilution. Rows derived from the 1 ml `Trace element solution SL-10`, 1 ml `Selenite-tungstate solution`, and 1 ml `Wolin's vitamin solution (10x)` stocks are roughly 1005x too concentrated in the final-medium record.
- Medium: Full-strength stock acids and bases are consequently represented as main-medium solutes. For example, `HCl` from the 1 L SL-10 stock is recorded as 2.5 g/l in the final medium, and `NaOH` from the 1 L selenite-tungstate stock is recorded as 0.5 g/l, even though DSMZ Medium 311c only uses 1 ml of each stock.

## Recommended Edits

- Fix the MediaDive import or normalization logic so nested solution components are multiplied by their aliquot volume over the final main-solution volume before they become final-medium `G_PER_L` concentrations.
- Regenerate `data/normalized_yaml/bacterial/sporomusa_acidovorans_medium.yaml` and `data/merge_yaml/merged/sporomusa_acidovorans_medium__bde76f8c.yaml` from corrected MediaDive 311c scaling.
- Add regression coverage using a medium with 1 ml trace-element and vitamin stock aliquots so full 1 L stock concentrations cannot reappear as final-medium concentrations.

## Follow-up Checks

- Keep the DSMZ strain-specific replacement notes out of the base medium formula unless separate variants are curated for DSM 4440, DSM 6539, DSM 6540, DSM 11501, DSM 14980, DSM 16652, DSM 17108, DSM 17189, DSM 17285, DSM 26537, DSM 26827, DSM 116159, or DSM 116160.

## Additional Notes

None found
