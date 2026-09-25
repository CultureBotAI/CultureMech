# YAML Record Review: spirochaeta_zuelzerae_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_zuelzerae_medium.yaml
- Started UTC: 2026-09-25T06:25:57Z
- Finished UTC: 2026-09-25T06:27:04Z
- Verdict: needs curation

## Target

Generated merged YAML for KOMODO 169 / DSMZ 169, TERETINEMA MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_zuelzerae_medium.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to KOMODO 169 and DSMZ 169.

The source medium is assembled from Solution A, Solution B, and Solution C, with agar optional for solid medium. The generated YAML flattens those solutions into one parent list and promotes optional agar to the base physical state.

## Evidence

DSMZ 169 lists 960.00 ml Solution A, 20.00 ml Solution B, and 20.00 ml Solution C as the final TERETINEMA MEDIUM assembly.

Solution A contains 0.04 g CaCl2 x 2 H2O, 0.50 g MgSO4 x 7 H2O, 4.00 g yeast extract (OXOID), 2.00 g D-glucose, 0.50 ml sodium resazurin (0.1% w/v), 0.50 g L-cysteine HCl x H2O, optional 10.00 g agar for solid medium, and 960.00 ml distilled water.

Solution B contains 1.00 g NaHCO3 and 20.00 ml distilled water. Solution C contains 16.04 ml 0.5 M K2HPO4 plus 3.96 ml 0.5 M KH2PO4 and is prepared to a pH around 7.4. The completed medium has a final pH of 7.5.

## Completeness

The generated record omits Solution A, Solution B, Solution C, both distilled-water rows, and the Solution C stock-mixture instruction. KOH from the pH adjustment is a variable ingredient rather than only a preparation detail.

## Findings

- Major: the 960 ml Solution A, 20 ml Solution B, and 20 ml Solution C additions are flattened into a single parent ingredient list.
- Major: optional solid-medium agar is promoted to `physical_state: SOLID_AGAR` in the base recipe.
- Major: NaHCO3 is represented as `50` `G_PER_L`, the stock strength of Solution B, instead of as a 20 ml Solution B addition.
- Major: Solution C phosphate-buffer volumes are flattened to final K2HPO4 and KH2PO4 ingredient rows and the 0.5 M stock-solution context is lost.
- Major: the 960 ml and 20 ml distilled-water rows are missing.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/spirochaeta_zuelzerae_medium.yaml` to model the source as Solution A, Solution B, and Solution C with 960 ml, 20 ml, and 20 ml final volumes.
- Preserve the 960 ml and 20 ml distilled-water rows under Solution A and Solution B.
- Move optional 10 g agar into a solid-medium variant or an optional Solution A row without making the base recipe solid agar.
- Keep Solution C as a phosphate-buffer stock mixture with 16.04 ml 0.5 M K2HPO4 and 3.96 ml 0.5 M KH2PO4.
- Regenerate `data/merge_yaml/merged/spirochaeta_zuelzerae_medium.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm the base recipe is not solid agar.
- Confirm Solution A, Solution B, and Solution C remain explicit.
- Confirm NaHCO3 is not represented as a direct `50` `G_PER_L` parent ingredient.

## Additional Notes

None found.
