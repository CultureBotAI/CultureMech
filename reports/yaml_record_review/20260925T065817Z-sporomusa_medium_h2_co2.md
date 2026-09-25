# YAML Record Review: sporomusa_medium_h2_co2

- Repository: CultureMech
- Record: data/merge_yaml/merged/sporomusa_medium_h2_co2.yaml
- Started UTC: 2026-09-25T06:56:39Z
- Finished UTC: 2026-09-25T06:58:17Z
- Verdict: needs curation

## Target

Reviewed the generated record for DSMZ Medium 311a, `SPOROMUSA MEDIUM (H2/CO2)`, assigned `CultureMech:001411`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record is a DSMZ/MediaDive import for `mediadive.medium:311a`. MediaDive identifies medium 311a as `SPOROMUSA MEDIUM (H2/CO2)`, source `DSMZ`, pH 7.0, and links it to the DSMZ Medium 311a PDF.

The generated record preserves the DSMZ medium identity, pH, direct base-medium rows, DTT reducing-agent row, and H2-CO2/N2 anaerobic preparation instructions. The ingredient rows are mostly grounded, but nested trace/vitamin stocks are grounded at stock concentrations rather than final-medium concentrations.

## Evidence

DSMZ and MediaDive list three nested stocks that should enter Medium 311a as 1 ml aliquots: `Trace element solution SL-10`, `Selenite-tungstate solution`, and `Wolin's vitamin solution (10x)`. In the generated target, every solute from those 1 L stock recipes was flattened at its full stock concentration instead of being diluted by the 1 ml over 1005 ml aliquot factor.

The direct main-medium rows are scaled to MediaDive's 1005 ml final volume. For example, 0.50 g `NH4Cl` becomes 0.497512 g/l, 1.00 g `Na2CO3` becomes 0.995025 g/l, 0.15 g `DL-Dithiothreitol` becomes 0.149254 g/l, and 0.50 ml of 0.1 percent sodium resazurin becomes 0.000497512 g/l.

## Completeness

The generated record includes all named DSMZ base and stock ingredients, preparation text for the base medium and trace element stock, and pH 7.0. Distilled-water rows are omitted, which is consistent with the generated representation elsewhere.

The formula is not quantitatively complete because nested MediaDive stock recipes are represented at their stock concentrations instead of their diluted final concentrations.

## Findings

- High: The MediaDive stock solutions were flattened without aliquot dilution. Rows derived from the 1 ml `Trace element solution SL-10`, 1 ml `Selenite-tungstate solution`, and 1 ml `Wolin's vitamin solution (10x)` stocks are roughly 1005x too concentrated in the final-medium record.
- Medium: Full-strength stock acids and bases are consequently represented as main-medium solutes. For example, `HCl` from the 1 L SL-10 stock is recorded as 2.5 g/l in the final medium, and `NaOH` from the 1 L selenite-tungstate stock is recorded as 0.5 g/l, even though DSMZ Medium 311a only uses 1 ml of each stock.

## Recommended Edits

- Fix the MediaDive import or normalization logic so nested solution components are multiplied by their aliquot volume over the final main-solution volume before they become final-medium `G_PER_L` concentrations.
- Regenerate `data/normalized_yaml/bacterial/sporomusa_medium_h2_co2.yaml` and `data/merge_yaml/merged/sporomusa_medium_h2_co2.yaml` from corrected MediaDive 311a scaling.
- Add regression coverage using DSMZ 311a or another medium with trace-element, selenite-tungstate, and 10x vitamin stock aliquots so full 1 L stock concentrations cannot reappear as final-medium concentrations.

## Follow-up Checks

- Keep the DSMZ strain-specific 2.50 g/l Na-pyruvate supplement for DSM 11379, DSM 11380, DSM 11381, and DSM 11382 out of the base medium formula unless separate variants are curated.

## Additional Notes

None found
