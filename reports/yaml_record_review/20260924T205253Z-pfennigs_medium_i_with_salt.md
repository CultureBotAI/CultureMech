# YAML Record Review: PFENNIG'S MEDIUM I WITH SALT

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium_i_with_salt.yaml
- Started UTC: 2026-09-24T20:52:53Z
- Finished UTC: 2026-09-24T20:52:53Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pfennigs_medium_i_with_salt.yaml`, the merged DSMZ/MediaDive record for DSMZ medium 46 / PFENNIG'S MEDIUM I WITH SALT.

The merged record is grounded to `mediadive.medium:46` and the DSMZ Medium 46 PDF, but its `merged_from` list contains both `DSMZ_46_PFENNIG_S_MEDIUM_I_WITH_SALT` and `pfennigs_medium_i_with_salt`.

## Validation

- LinkML open validation: passed; no issues found.
- Strict schema validation: passed; `/private/tmp/pfennigs_medium_i_with_salt.strict.tsv` has one header row and zero error rows.
- Reference validation: passed; 1 file validated, 0 checks configured.
- Term validation: passed.
- Embedded curation history validation: Not checked; the available `just validate-history` target validates standalone `history/` records rather than `MediaRecipe.curation_history` blocks inside merged YAML.

## Identity and Grounding

The canonical medium identity is correct for DSMZ 46: DSMZ medium 46 is PFENNIG'S MEDIUM I WITH SALT and the PDF says to add 1% NaCl to DSMZ medium 28.

The merged provenance is not correct. The second merged source, `data/normalized_yaml/bacterial/pfennigs_medium_i_with_salt.yaml`, is DSMZ medium 43 with `mediadive.medium:43`, whose PDF says to add 3% NaCl to DSMZ medium 28. DSMZ 43 should remain a 30 g/L NaCl salinity variant of the 10 g/L DSMZ 46 recipe, not a merged duplicate source for the DSMZ 46 record.

The ingredient groundings also inherit the DSMZ 28 stock-solution flattening problem. Bicarbonate, sulfide, vitamin B12, resazurin, and heterotrophic salts stock concentrations are represented as top-level final-medium concentrations rather than as named solutions used to assemble the final medium.

## Evidence

- Fetched the DSMZ Medium 46 PDF and confirmed its whole formula is "To medium 28 add 1% NaCl."
- Fetched the MediaDive REST record for medium 46 and confirmed it represents the formula as `Main sol. 28` plus 1% NaCl, equivalent to 10 g/L.
- Fetched the DSMZ Medium 43 PDF and MediaDive REST record and confirmed DSMZ 43 is the 3% NaCl variant of medium 28, equivalent to 30 g/L.
- Compared both normalized source records with the merged YAML and confirmed the merge absorbed DSMZ 43 even though the target kept DSMZ 46's 10 g/L NaCl value.
- Compared inherited medium 28 solution structure against the top-level ingredient list and found the same flattened stock concentrations present in DSMZ 28-derived records.

## Completeness

The target preserves DSMZ 46's pH range and 10 g/L NaCl addition. It also preserves several inherited DSMZ 28 preparation sentences.

The target does not preserve the DSMZ 28 solution hierarchy that DSMZ 46 references. The source calls for Main sol. 28 plus NaCl; Main sol. 28 is assembled from multiple named solutions. Those stock additions and their water rows are mostly flattened away, and Trace element solution SL-12 B is not represented as a stock addition under the heterotrophic salts solution.

The merged provenance is internally inconsistent: the output advertises `pfennigs_medium_i_with_salt.yaml` as a variant child while also listing that same 30 g/L DSMZ 43 source under `merged_from`.

## Findings

- DSMZ 43 and DSMZ 46 are distinct salinity variants but have been merged. DSMZ 46 adds 1% NaCl, while DSMZ 43 adds 3% NaCl.
- Rows from Solution A, bicarbonate solution, resazurin solution, Pfennig's heterotrophic salts solution, and vitamin B12 solution appear as final top-level ingredients with stock concentrations.
- The Trace element solution SL-12 B aliquot inherited from DSMZ 28 is absent rather than being modeled as a 1 ml stock addition inside Pfennig's heterotrophic salts solution.
- The sulfide rows from the 1.5% sulfide stock and the 3% neutralized sulfide feed were summed into one `44.8148 G_PER_L` Na2S x 9 H2O row, even though the source treats them as separate preparations.
- The DSMZ 43 variant source appears both as a merged source and as a `SALINITY_VARIANT` child, so the variant relationship contradicts the merge provenance.
- `Pyruvic acid sodium salt` still carries a legacy `mediaingredientmech_term` block instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits

- Keep DSMZ medium 46 and DSMZ medium 43 as separate records linked by `SALINITY_VARIANT`: DSMZ 46 at 10 g/L NaCl, DSMZ 43 at 30 g/L NaCl.
- Remove `pfennigs_medium_i_with_salt` / DSMZ 43 from this record's `merged_from` provenance.
- Re-normalize DSMZ medium 46 as `Main sol. 28` plus 1% NaCl, with the medium 28 nested solution structure preserved instead of flattened.
- Restore the Trace element solution SL-12 B aliquot as part of Pfennig's heterotrophic salts solution.
- Stop merging the two independent Na2S stock/feed rows.
- Replace the legacy `mediaingredientmech_term` on `Pyruvic acid sodium salt` with a CHEBI-keyed `mediaingredientmech_chebi_term` for `CHEBI:50144`.

## Follow-up Checks

- Re-run LinkML open validation, strict validation, reference validation, and term validation on regenerated DSMZ 46 and DSMZ 43 merged records.
- Verify DSMZ 46 has 10 g/L NaCl and DSMZ 43 has 30 g/L NaCl.
- Search with ignored files included for `DSMZ_Medium43`, `DSMZ_Medium46`, `mediadive.medium:43`, and `mediadive.medium:46` and confirm the two source IDs no longer collapse into one merged record.
- Confirm no stock-only concentration from medium 28 is exposed as a final top-level concentration.

## Additional Notes

Empty optional fields were not treated as defects. The review used DSMZ Medium 28 only because DSMZ media 43 and 46 are defined as salt additions to medium 28.
