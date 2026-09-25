# YAML Record Review: sporomusa_medium_marine

- Repository: CultureMech
- Record: data/merge_yaml/merged/sporomusa_medium_marine.yaml
- Started UTC: 2026-09-25T06:58:17Z
- Finished UTC: 2026-09-25T06:59:53Z
- Verdict: needs curation

## Target

Reviewed the generated record for DSMZ Medium 311b, `SPOROMUSA MEDIUM (MARINE)`, assigned `CultureMech:015352`.

## Validation

- LinkML validation: Passed; no issues found.
- Strict validation: Passed; the TSV contained only the header, with 0 error rows.
- LinkML reference validation: Passed; 0 reference checks were run and all passed.
- LinkML term validation: Passed.
- Embedded history validation: Not checked; the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The canonical source record is a specialized DSMZ/MediaDive import for `mediadive.medium:311b`. MediaDive identifies medium 311b as `SPOROMUSA MEDIUM (MARINE)`, source `DSMZ`, pH 7.5 to 7.7, and links it to the DSMZ Medium 311b PDF.

The generated record is not single-source: it merged `sporomusa_medium_marine` with nine bacterial DSMZ/KOMODO records, including KOMODO records named `For DSM 3132`, `For DSM 4440`, `For DSM 16652`, `For DSM 11379, DSM 11380, DSM 11381 and DSM 11382`, `MEDIUM 311 MODIFIED FOR DSM 2767`, and `MEDIUM 311 MODIFIED FOR DSM 5090`. Several of those normalized children had `variant_relationship: STRAIN_SPECIFIC_VARIANT`, but the generated merge keeps only `synonyms`, `categories`, and `merged_from` entries.

## Evidence

DSMZ and MediaDive list three nested stocks that should enter Medium 311b as 1 ml aliquots: `Trace element solution SL-10`, `Selenite-tungstate solution`, and `Wolin's vitamin solution (10x)`. In the generated target, every solute from those 1 L stock recipes was flattened at its full stock concentration instead of being diluted by the 1 ml over 1005 ml aliquot factor.

The direct marine rows are scaled to MediaDive's 1005 ml final volume. For example, 25.00 g `NaCl` becomes 24.8756 g/l, 6.70 g `Betaine x H2O` becomes 6.66667 g/l, 1.50 g `Na2CO3` becomes 1.49254 g/l, and 0.50 ml of 0.1 percent sodium resazurin becomes 0.000497512 g/l.

## Completeness

The generated record includes all named DSMZ 311b base and stock ingredients, preparation text for the base medium and trace element stock, and the pH range. Distilled-water rows are omitted, which is consistent with the generated representation elsewhere.

The formula is not quantitatively complete because nested MediaDive stock recipes are represented at their stock concentrations instead of their diluted final concentrations. The generated record also does not preserve the parent/variant relationships from the merged KOMODO strain-specific records, so a consumer cannot distinguish true source duplicates from modified 311-series variants after merge.

## Findings

- High: The MediaDive stock solutions were flattened without aliquot dilution. Rows derived from the 1 ml `Trace element solution SL-10`, 1 ml `Selenite-tungstate solution`, and 1 ml `Wolin's vitamin solution (10x)` stocks are roughly 1005x too concentrated in the final-medium record.
- Medium: Full-strength stock acids and bases are consequently represented as main-medium solutes. For example, `HCl` from the 1 L SL-10 stock is recorded as 2.5 g/l in the final medium, and `NaOH` from the 1 L selenite-tungstate stock is recorded as 0.5 g/l, even though DSMZ Medium 311b only uses 1 ml of each stock.
- Medium: The generated merge collapses DSMZ 311b with nine DSMZ/KOMODO 311-series records, including strain-specific variants, into a single `SPOROMUSA MEDIUM (MARINE)` record. Those sources should be audited as explicit duplicates or retained as variant children so the strain-specific curation is not reduced to synonym strings.

## Recommended Edits

- Fix the MediaDive import or normalization logic so nested solution components are multiplied by their aliquot volume over the final main-solution volume before they become final-medium `G_PER_L` concentrations.
- Regenerate `data/normalized_yaml/specialized/sporomusa_medium_marine.yaml` and `data/merge_yaml/merged/sporomusa_medium_marine.yaml` from corrected MediaDive 311b scaling.
- Audit the nine non-311b records currently merged into this target; keep true duplicates as `SOURCE_DUPLICATE` children and keep strain-specific modifications as separate variants with `STRAIN_SPECIFIC_VARIANT` relationships rather than flattening them into synonyms.

## Follow-up Checks

- After the variant audit, confirm that bacterial and specialized categories are not being mixed only because DSMZ 311b became the canonical record for a fingerprint shared by unrelated KOMODO variant names.

## Additional Notes

None found
