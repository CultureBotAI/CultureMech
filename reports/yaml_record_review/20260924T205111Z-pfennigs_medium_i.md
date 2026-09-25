# YAML Record Review: PFENNIG'S MEDIUM I

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium_i.yaml
- Started UTC: 2026-09-24T20:51:11Z
- Finished UTC: 2026-09-24T20:51:11Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pfennigs_medium_i.yaml`, the direct DSMZ/MediaDive record for DSMZ medium 28 / PFENNIG'S MEDIUM I.

The merged record has a single source recipe, `pfennigs_medium_i`, grounded to `mediadive.medium:28` and the DSMZ Medium 28 PDF.

## Validation

- LinkML open validation: passed; no issues found.
- Strict schema validation: passed; `/private/tmp/pfennigs_medium_i.strict.tsv` has one header row and zero error rows.
- Reference validation: passed; 1 file validated, 0 checks configured.
- Term validation: passed.
- Embedded curation history validation: Not checked; the available `just validate-history` target validates standalone `history/` records rather than `MediaRecipe.curation_history` blocks inside merged YAML.

## Identity and Grounding

The medium identity is correct: DSMZ/MediaDive medium 28 is PFENNIG'S MEDIUM I with a pH range of 7.1-7.3, and the target uses `mediadive.medium:28`.

The ingredient groundings are attached to the wrong recipe scopes. DSMZ 28 is assembled from Solution A, sulfide solution 1.5%, bicarbonate solution, resazurin solution, Pfennig's heterotrophic salts solution, vitamin B12 solution, Trace element solution SL-12 B, and a neutralized sulfide feed. The target flattens most of those stock-solution formulas into the top-level `ingredients` list and stores stock concentrations as if they were final-medium concentrations.

## Evidence

- Fetched the MediaDive REST record for medium 28 and confirmed that the main solution is a recipe over named solutions, including 460 ml Solution A, 50 ml bicarbonate solution, 26 ml Pfennig's heterotrophic salts solution, 40 ml/L sulfide solution, and 1 ml/L vitamin B12 solution.
- Fetched and rendered the DSMZ Medium 28 PDF, which lists Solution A through Solution F, Trace element solution SL-12 B, and Neutralized sulfide solution as separate preparations.
- Compared those stock scopes with the merged YAML and confirmed that stock rows such as 30 g/L NaHCO3, 3 g/L Na2-EDTA, and 0.1 g/L vitamin B12 are not final-medium concentrations.
- Confirmed validation succeeds, so the defect is source fidelity and solution hierarchy rather than YAML structure.

## Completeness

The target preserves the medium identifier, pH range, and many source preparation sentences, but it does not preserve the source recipe hierarchy.

Water rows and stock volumes from the named solutions are omitted from the data model, the Trace element solution SL-12 B aliquot is flattened into top-level trace metal ingredients, the vitamin B12 stock is flattened into a top-level `0.1 G_PER_L` ingredient, and the two different sulfide preparations are collapsed into one summed Na2S row. These are stock recipes and feeds with separate addition volumes in the DSMZ source.

## Findings

- Solution boundaries are lost. Rows from Solution A, bicarbonate solution, Pfennig's heterotrophic salts solution, vitamin B12 solution, Trace element solution SL-12 B, and Neutralized sulfide solution all appear together as final top-level ingredients.
- The sulfide rows were merged arithmetically even though they come from different preparations: 2 g Na2S x 9 H2O in the 135 ml sulfide solution and 3 g Na2S x 9 H2O in the 100 ml neutralized sulfide feed. The target stores their stock strengths as one `44.8148 G_PER_L` final row with a "Merged 2 duplicates" note.
- Stock concentrations are misinterpreted as final concentrations. For example, DSMZ uses 1.5 g NaHCO3 in a 50 ml bicarbonate stock and 0.01 g vitamin B12 in a 100 ml stock; the target reports `30 G_PER_L` NaHCO3 and `0.1 G_PER_L` vitamin B12 as final medium ingredients.
- The Trace element solution SL-12 B formula is flattened into the final medium. Its 3 g/L Na2-EDTA, 1.1 g/L FeSO4 x 7 H2O, and mg/L trace salts are stock-solution concentrations used via a 1 ml aliquot inside the 26 ml heterotrophic salts solution.
- Source water and intermediate solution volumes are not represented, making the preparation steps impossible to reconcile with the ingredient concentrations.
- `Pyruvic acid sodium salt` still carries a legacy `mediaingredientmech_term` block even though the row has a CHEBI primary term and the rest of the record uses `mediaingredientmech_chebi_term`.

## Recommended Edits

- Re-normalize DSMZ/MediaDive medium 28 as a recipe with nested named solutions rather than a single flat final ingredient list.
- Preserve the source addition volumes for Solution A, resazurin solution, bicarbonate solution, Pfennig's heterotrophic salts solution, sulfide solution 1.5%, vitamin B12 solution, and the strain/stage-dependent neutralized sulfide feed.
- Keep Trace element solution SL-12 B as a stock under the heterotrophic salts solution instead of flattening its EDTA, iron, and trace metals into the final medium.
- Stop merging Na2S rows across the 1.5% sulfide solution and the neutralized 3% sulfide feed.
- Attach each preparation step to its appropriate stock solution or final assembly stage.
- Replace the legacy `mediaingredientmech_term` on `Pyruvic acid sodium salt` with a CHEBI-keyed `mediaingredientmech_chebi_term` for `CHEBI:50144`.

## Follow-up Checks

- Re-run LinkML open validation, strict validation, reference validation, and term validation on the regenerated merged record.
- Compare the regenerated YAML against DSMZ Medium 28 and verify that no stock-only concentration is exposed as a final-medium concentration.
- Confirm there is no top-level merged Na2S row summing independent sulfide preparations.
- Confirm the final pH range remains 7.1-7.3.

## Additional Notes

Empty optional fields were not treated as defects. KOMODO records that copy DSMZ medium 28 for strain-specific variants were not reviewed as part of this target.
