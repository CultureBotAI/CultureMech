# YAML Record Review: Pfennig's Medium II

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium_ii.yaml
- Started UTC: 2026-09-24T20:55:15Z
- Finished UTC: 2026-09-24T20:55:15Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pfennigs_medium_ii.yaml`, the TOGO-derived record for DSMZ Medium 29 / Pfennig's Medium II.

The merged record has one source recipe, `TOGO_M2595_Pfennig_s_Medium_II`, grounded to TOGO `M2595` and the DSMZ Medium 29 PDF.

## Validation

- LinkML open validation: passed; no issues found.
- Strict schema validation: passed; `/private/tmp/pfennigs_medium_ii.strict.tsv` has one header row and zero error rows.
- Reference validation: passed; 1 file validated, 0 checks configured.
- Term validation: passed.
- Embedded curation history validation: Not checked; the available `just validate-history` target validates standalone `history/` records rather than `MediaRecipe.curation_history` blocks inside merged YAML.

## Identity and Grounding

The record identity is correct for Pfennig's Medium II from DSMZ Medium 29 as imported through TOGO M2595.

The same DSMZ Medium 29 source also exists as a direct DSMZ-derived sibling, `data/merge_yaml/merged/pfennigs_medium_ii__98923e03.yaml`, and failed to merge with this TOGO version. The two records should reconcile after the DSMZ 29 named solutions are modeled with their stock scopes and aliquot volumes.

Most simple salts are grounded to the expected CHEBI concepts, but they are grounded at the wrong level. Components from Solution A, Solution B, Solution C, Solution D, Solution E, Solution F, Trace element solution SL-10 B, and Neutralized sulfide solution were retained as top-level final ingredients, while their corresponding solution aliquots were also migrated into `solutions`.

## Evidence

- Fetched TOGO M2595 and confirmed it points to DSMZ Medium 29 with pH 6.8-7.1.
- Fetched and rendered the DSMZ Medium 29 PDF, which lists Solution A-F, Trace element solution SL-10 B, a Neutralized sulfide solution, and final assembly instructions using 46 ml Solution A, 50 ml Solution D+C+E, 4 ml Solution B, and 0.1 ml Solution F per bottle.
- Compared the TOGO component hierarchy with the merged YAML and confirmed the final solution aliquots were converted to `G_PER_L` solution entries while their stock rows were also kept as final ingredients.
- Located the direct DSMZ Medium 29 sibling that carries the same DSMZ source URL but did not merge with this TOGO-derived record.

## Completeness

The source hierarchy is not complete in the target. The target has placeholder `solutions` entries for the source aliquots, but all migrated solution concentrations use `G_PER_L` for milliliter volumes, carry the generic name `Unknown solution`, and lack nested compositions.

The target also omits the source pH range of 6.8-7.1, flattens source gases and pH-adjustment reagents into top-level ingredients, and sums stock water volumes into impossible final ingredient rows.

## Findings

- Solution aliquots are misunitized: 46 ml Solution A, 50 ml Solution D+C+E, 4 ml Solution B, 0.1 ml Solution F, 450.5 ml Solution D, 50 ml Solution C, 26 ml Solution E, and 1 ml Trace element solution SL-10 B are all stored under `solutions` as `G_PER_L`.
- Stock and assembly scopes are duplicated. Rows from the same named solutions remain in top-level `ingredients` even though corresponding solution stubs also exist under `solutions`.
- Water rows from seven different solution scopes were summed to one `2270.0 G_PER_L` Distilled water ingredient, with an additional `50 G_PER_L` H2O row left separate.
- Independent Solution B and Neutralized sulfide solution Na2S x 9 H2O rows were merged into one `5.0 G_PER_L` top-level row.
- Trace element solution SL-10 B milligram rows were imported as grams per liter without conversion: for example, 36 mg Na2MoO4 x 2 H2O is stored as `36 G_PER_L`, 300 mg H3BO3 is stored as `300 G_PER_L`, and 70 mg ZnCl2 is stored as `70 G_PER_L`.
- Nitrogen and carbon dioxide sparging instructions appear repeatedly as `VARIABLE` top-level gas ingredients.
- The pH range 6.8-7.1 from DSMZ/TOGO is missing.
- `Pyruvic acid sodium salt` still carries a legacy `mediaingredientmech_term` block instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits

- Re-normalize TOGO M2595 as a nested DSMZ Medium 29 recipe with Solution A, Solution B, Solution C, Solution D, Solution E, Solution F, Trace element solution SL-10 B, and Neutralized sulfide solution as scoped stocks or assembly intermediates.
- Preserve milliliter aliquot volumes with `ML_PER_L` or another volume-aware representation; do not encode them as `G_PER_L`.
- Move all water, gas, trace-metal, vitamin B12, bicarbonate, heterotrophic-salt, and sulfide rows into their correct source solution scopes.
- Convert SL-10 B milligram stock rows to grams only after dividing by 1000, and keep them in the stock solution rather than the final medium.
- Carry the DSMZ/TOGO pH range of 6.8-7.1.
- Remove gas sparging labels from final ingredients and represent them as preparation steps.
- Replace the legacy `mediaingredientmech_term` on `Pyruvic acid sodium salt` with a CHEBI-keyed `mediaingredientmech_chebi_term` for `CHEBI:50144`.
- Re-run merge after the TOGO and direct DSMZ Medium 29 normalizations are aligned.

## Follow-up Checks

- Re-run LinkML open validation, strict validation, reference validation, and term validation on the regenerated merged record.
- Search with ignored files included for `TOGO:M2595`, `DSMZ_Medium29`, and `mediadive.medium:29` to confirm the TOGO and direct DSMZ sources reconcile instead of splitting exact DSMZ Medium 29.
- Confirm no milliliter source volume remains as `G_PER_L`.
- Confirm the very large trace rows no longer set `high_metal: true`.

## Additional Notes

Empty optional fields were not treated as defects. The high-metal flag appears to be a consequence of milligram-to-gram and stock-scope flattening errors, not direct source biology.
