# YAML Record Review: caldimicrobium_thiodismutans_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDIMICROBIUM_THIODISMUTANS_MEDIUM.yaml
- Started UTC: 2026-09-22T02:16:14Z
- Finished UTC: 2026-09-22T02:17:59Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:000740`, `caldimicrobium_thiodismutans_medium`, `CALDIMICROBIUM THIODISMUTANS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caldimicrobium_thiodismutans_medium` on fingerprint `aabfecf9b02a3b89bad457ce2c447401c035c573b5ff857d9ce6fec673ff2166`.
- Authoritative owner: `data/normalized_yaml/bacterial/caldimicrobium_thiodismutans_medium.yaml`.
- Claimed source identity: DSMZ / MediaDive Medium 1277b, `CALDIMICROBIUM THIODISMUTANS MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 1277b is `CALDIMICROBIUM THIODISMUTANS MEDIUM`; the live DSMZ PDF agrees with the record's pH range 7.5 to 8.0 and its anaerobic preparation text.
- The direct final-medium MgCl2, CaCl2, ammonium sulfate, KH2PO4, KCl, sodium carbonate, and sodium disulfite rows are source-compatible identities.
- SL-10 trace salts, selenite-tungstate rows, amorphous ferrihydrite preparation reagents, and Seven vitamins rows are grounded to source-compatible chemical identities but are modeled at the wrong formulation level.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.

## Evidence

- DSMZ Medium 1277b lists magnesium chloride hexahydrate, calcium chloride dihydrate, ammonium sulfate, KH2PO4, KCl, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 45 ml Amorphous Fe(OH)3, sodium carbonate, sodium disulfite, 1 ml Seven vitamins solution, and 960 ml distilled water in the final medium.
- DSMZ lists SL-10, Selenite-tungstate solution, Amorphous Fe(OH)3, and Seven vitamins solution as separate subordinate recipes, not as direct final-medium ingredient rows.
- The record has no `Amorphous Fe(OH)3` final addition; it instead contains 320 g/L ferric chloride hexahydrate from the precipitated-stock instructions.
- The generated 20.5 g/L NaOH row sums 0.5 g/L from Selenite-tungstate solution with an unsupported 20.0 g/L from the ferrihydrite preparation context.
- DSMZ instructs curators to withhold carbonate, pyrosulfite, and vitamins from the autoclaved base; sparge with 80% N2 / 20% CO2; add pyrosulfite, vitamins, and carbonate from sterile filtered or anoxic stocks; adjust the final pH to 7.5 to 8.0; and incubate without shaking.

## Completeness

- The pH range and DSMZ preparation prose are present.
- The 960 ml distilled-water row for the final medium is absent.
- The water rows for SL-10, Selenite-tungstate solution, and Seven vitamins solution are absent because those stocks were flattened.
- The source's DSM 110365-specific replacement of pyrosulfite with filtered thiosulfate is not modeled as a strain-specific variant.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a broad growth claim.

## Findings

- Major: Trace element solution SL-10 is flattened into final-medium ingredient rows at stock strength; DSMZ Medium 1277b calls for only 1 ml of this stock per final recipe.
- Major: Selenite-tungstate solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of this stock per final recipe.
- Major: Seven vitamins solution is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of this stock per final recipe.
- Major: Amorphous Fe(OH)3 is missing as a 45 ml final-medium addition and is replaced by unsupported top-level ferrihydrite stock reagents, including 320 g/L FeCl3 hexahydrate.
- Major: duplicate cleanup merged unrelated NaOH rows from Selenite-tungstate solution and Amorphous Fe(OH)3 preparation into a single 20.5 g/L top-level ingredient.
- Major: the generated record omits the 960 ml final distilled-water row and the stock water rows.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: the DSM 110365-specific thiosulfate replacement is not represented as a bounded variant of this base medium.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldimicrobium_thiodismutans_medium.yaml`, not the generated merge.
- Model SL-10, Selenite-tungstate solution, Amorphous Fe(OH)3, and Seven vitamins solution as subordinate additions at their DSMZ 1277b volumes, and move their internal ingredients into stock recipes.
- Restore the 45 ml Amorphous Fe(OH)3 final addition and remove the ferric chloride and NaOH stock-preparation reagents from the final ingredient list.
- Split the summed NaOH row back into its stock-specific contexts.
- Add the 960 ml water row for the final medium and the water rows for the stock recipes.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Consider representing the DSM 110365 pyrosulfite-to-thiosulfate substitution as a strain-specific medium variant.
- Regenerate merged YAML and verify that the one-source generated record preserves stock additions instead of flattening their recipes.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 1277b, with special attention to subordinate stock boundaries, the 45 ml Amorphous Fe(OH)3 addition, exact water amounts, separated NaOH contexts, the optional DSM 110365 variant, and the hydrate-specific nickel chloride grounding.

## Additional Notes

- `find . -iname '*caldimicrobium*'` included ignored and hidden files and found only the two Caldimicrobium generated merges, their two active normalized owners, and the prior Caldimicrobium Medium review report.
- A gitignore-independent search for Caldimicrobium thiodismutans Medium labels, slugs, DSMZ 1277b identifiers, and the DSMZ PDF filename found the active DSMZ owner, the generated merge, registry/catalog rows, current content review manifest rows, an organism-candidate stub keyed by the retired DSMZ filename, import-tracking rows that had already flagged NaOH and stock-scale outliers, and archived DSMZ 1277b validation rows.
