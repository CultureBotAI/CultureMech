# YAML Record Review: Pfennig's Medium II With Salt

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium_ii_with_salt__0165a5bc.yaml
- Started UTC: 2026-09-24T20:58:57Z
- Finished UTC: 2026-09-24T20:58:57Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pfennigs_medium_ii_with_salt__0165a5bc.yaml`, the TOGO M2258-derived record for DSMZ Medium 40 / Pfennig's Medium II With Salt.

The merged record has one source recipe, `TOGO_M2258_Pfennig_s_Medium_II_With_Salt`, grounded to TOGO `M2258` and the DSMZ Medium 40 PDF.

## Validation

- LinkML open validation: passed; no issues found.
- Strict schema validation: passed; `/private/tmp/pfennigs_medium_ii_with_salt__0165a5bc.strict.tsv` has one header row and zero error rows.
- Reference validation: passed; 1 file validated, 0 checks configured.
- Term validation: passed.
- Embedded curation history validation: Not checked; the available `just validate-history` target validates standalone `history/` records rather than `MediaRecipe.curation_history` blocks inside merged YAML.

## Identity and Grounding

The record is grounded to the correct TOGO import of DSMZ Medium 40. TOGO M2258 and the DSMZ PDF both define Medium 40 as Medium 29 plus 1% NaCl.

The same DSMZ Medium 40 formula is split across at least three merged records: this TOGO M2258 record, the TOGO M2477 sibling `pfennigs_medium_ii_with_salt__b93e3483.yaml`, and the direct/KOMODO DSMZ 40 source-duplicate record `pfennigs_medium_ii_with_salt.yaml`.

The source hierarchy is not preserved. `Medium 29` is a parent recipe reference in the source, but the target stores it as a `100.1 G_PER_L` ingredient and also expands Medium 29 into the same top-level ingredient list.

## Evidence

- Fetched the DSMZ Medium 40 PDF and confirmed its complete formula is "To medium 29 add 1% NaCl."
- Fetched TOGO M2258 and confirmed its first component block contains `NaCl` at 1% and `Medium 29` at 100.1 ml, followed by nested Medium 29 solution blocks.
- Reused the rendered DSMZ Medium 29 source to verify the Solution A-F, Trace element solution SL-10 B, and Neutralized sulfide solution rows that TOGO expands under the Medium 29 heading.
- Compared the TOGO source hierarchy with the merged target and confirmed final formula references, solution aliquots, source water rows, gases, and trace stock rows were all flattened into one top-level ingredient array.
- Searched with ignored files included for exact DSMZ Medium 40 source identifiers and found sibling TOGO M2477 and direct/KOMODO DSMZ 40 merged records.

## Completeness

The target keeps the 1% NaCl row but otherwise loses the derived-medium structure. DSMZ Medium 40 should be Medium 29 with salt; Medium 29 should remain a nested source recipe rather than a final chemical row.

The solution stubs are incomplete because their milliliter aliquots are stored as `G_PER_L`, their names are all `Unknown solution`, and their compositions are empty. The source pH range inherited from Medium 29, 6.8-7.1, is also absent.

## Findings

- The parent `Medium 29` reference is misrepresented as a `100.1 G_PER_L` ingredient.
- Medium 29 solution aliquots, including 46 ml Solution A, 50 ml Solution D+C+E, 4 ml Solution B, 0.1 ml Solution F, and 1 ml Trace element solution SL-10 B, were migrated as `G_PER_L` solution concentrations.
- Source water rows from seven scopes were summed into `2270.0 G_PER_L` Distilled water, with a separate `50 G_PER_L` H2O row left behind.
- Nitrogen and carbon dioxide sparging steps were converted into multiple `VARIABLE` gas ingredients.
- SL-10 B milligram rows were imported as gram values: 36 mg Na2MoO4 x 2 H2O became `36 G_PER_L`, 300 mg H3BO3 became `300 G_PER_L`, and 70 mg ZnCl2 became `70 G_PER_L`.
- Independent Solution B and Neutralized sulfide Na2S x 9 H2O rows were merged into a single `5.0 G_PER_L` row.
- The inherited pH range 6.8-7.1 is missing.
- `Pyruvic acid sodium salt` still carries a legacy `mediaingredientmech_term` block instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits

- Normalize TOGO M2258 as DSMZ Medium 29 plus 1% NaCl.
- Represent Medium 29 as a parent recipe reference or nested recipe, not as a mass concentration.
- Preserve Medium 29's Solution A-F, Trace element solution SL-10 B, and Neutralized sulfide solution scopes with volume-aware aliquots.
- Convert SL-10 B milligram rows correctly and keep them scoped to the trace stock.
- Carry the inherited 6.8-7.1 pH range.
- Remove gas sparging labels from final ingredients and represent them as preparation steps.
- Replace the legacy `mediaingredientmech_term` on `Pyruvic acid sodium salt` with a CHEBI-keyed `mediaingredientmech_chebi_term` for `CHEBI:50144`.
- Re-run merge after TOGO M2258, TOGO M2477, KOMODO 40, and direct DSMZ 40 all normalize to equivalent DSMZ Medium 40 structure.

## Follow-up Checks

- Re-run LinkML open validation, strict validation, reference validation, and term validation on regenerated DSMZ 40 records.
- Confirm the regenerated M2258 record has 1% NaCl plus a Medium 29 reference and no `Medium 29` mass ingredient.
- Confirm no milliliter source volume remains as `G_PER_L`.
- Search with ignored files included for `TOGO:M2258`, `TOGO:M2477`, `DSMZ_Medium40`, `komodo.medium:40`, and `mediadive.medium:40` and verify exact DSMZ Medium 40 sources reconcile.

## Additional Notes

Empty optional fields were not treated as defects. The high-metal flag appears to be a consequence of milligram-to-gram and stock-scope flattening errors, not direct source biology.
