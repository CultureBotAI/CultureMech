# YAML Record Review: mcna_medium_lupa

- Repository: CultureMech
- Record: data/merge_yaml/merged/mcna_medium_lupa.yaml
- Started UTC: 2026-09-24T00:58:27Z
- Finished UTC: 2026-09-24T00:59:16Z
- Verdict: needs curation

## Target

Reviewed generated merged record `data/merge_yaml/merged/mcna_medium_lupa.yaml` for MediaDB medium 474. The exact normalized owner is `data/normalized_yaml/bacterial/mcna_medium_lupa.yaml`; `find` located no same-named or same-prefix alternate owner with ignored files included.

The generated record is stale relative to its normalized owner. It still has `original_name: '''McNA Medium (Lupa` and `media_term.term.label: '''McNA Medium (Lupa`, while the owner has the 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` event and the repaired `McNA Medium (Lupa)` label. Exact `MEDIADB:474` scans over the generated record, the owner, and existing normalized source indexes included ignored files and found the source only on this record family and the matching index entries.

## Validation

- Open LinkML validation against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`: passed with `No issues found`.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows; the strict TSV had a header only.
- LinkML reference validation: passed; 0 reference checks were emitted for this file.
- LinkML term validation with labels and `conf/oak_config.yaml`: passed.
- Embedded `curation_history`: Not checked. The repository `just validate-history` target validates standalone `history/` files rather than embedded generated-record history blocks.

## Identity and Grounding

`media_term.term.id` is `MEDIADB:474`, matching the MediaDB page `/defined_media/media/474/` for `Mcna medium (lupa)`. The MediaDB medium page links source 147, `Lupa b et al, 2008`; source 147 identifies the 2008 Applied and Environmental Microbiology article `Formate-dependent H2 production by the mesophilic methanogen Methanococcus maripaludis.` and links nine associated Methanococcus maripaludis growth-data records, 862 through 870.

Growth record 862 ties Methanococcus maripaludis S2 to MediaDB medium 474 and source 147 at pH 6.5 and 37.0 C. The record is the only expected merged product for normalized owner `mcna_medium_lupa`.

## Evidence

The MediaDB text export for medium 474 lists 27 tab-delimited source compounds. The generated CultureMech record has 28 `preferred_term` rows.

The target preserves most MediaDB numeric rows, including `Acetate` at `10.0` mM, but it is not a faithful transcription of the MediaDB source rows:

- Missing source row: `3-Methylbutanoic acid` at `0.04896` mM.
- Missing source row: `2-methylbutanoic acid` at `0.04896` mM.
- Extra row: `Tryptone` at `10.0` g/L, introduced from a third-party LB Miller product expansion rather than from MediaDB 474.
- Extra row: `Yeast extract` at `5.0` g/L, introduced from the same LB Miller expansion.
- Extra row: an additional `Sodium chloride` at `10.0` g/L, also from the LB Miller expansion; MediaDB 474 already supplies the source `Sodium chloride` row at `376.0` mM.

Exact searches for the two missing acid names over the generated record and normalized owner included ignored files and returned no matches. Exact searches of the MediaDB 474 rendered page and text export found no `Tryptone`, `Yeast extract`, `LB`, `Luria`, or `Miller` evidence for the imported commercial-product expansion.

## Completeness

The MediaDB formula coverage is incomplete because two source compounds are absent and three unrelated LB Miller constituents are present. The importer placeholder `DISSOLVE`, `ADJUST_PH`, and `FILTER_STERILIZE` preparation steps are generic and not supported by the inspected MediaDB medium, text, source, or growth pages.

Several surviving rows also need enrichment cleanup after the source formula is corrected. `Sodium sulfide` and `Cysteine-HCl` still carry only legacy `mediaingredientmech_term` blocks, and `Sodium tungstate`, `Nickel chloride`, `Cupric sulfate`, and `Acetate` have `term` mappings without migrated `mediaingredientmech_chebi_term` blocks.

## Findings

1. `needs curation` - The ingredient list mixes MediaDB 474 with an unsupported LB Miller commercial-product expansion. The target adds Tryptone 10.0 g/L, Yeast extract 5.0 g/L, and a second Sodium chloride 10.0 g/L row that are absent from MediaDB medium 474, the MediaDB text export, source 147, and growth record 862.
2. `needs curation` - The ingredient list omits two compounds that are explicitly listed by MediaDB 474: `3-Methylbutanoic acid` 0.04896 mM and `2-methylbutanoic acid` 0.04896 mM.
3. `needs curation` - `data/merge_yaml/merged/mcna_medium_lupa.yaml` is stale relative to `data/normalized_yaml/bacterial/mcna_medium_lupa.yaml`, so the generated record still exposes the SQL-parser truncation in `original_name` and `media_term.term.label`.
4. `minor` - The recipe still has generic importer preparation steps and several incomplete MediaIngredientMech-to-ChEBI migrated links.

## Recommended Edits

Correct the normalized MediaDB 474 recipe to remove the unsupported LB Miller constituent rows and restore both missing branched-chain acid rows from the MediaDB source. Preserve source-backed `Acetate` 10.0 mM and `Sodium chloride` 376.0 mM, then regenerate the merged record from the repaired owner.

Remove the generic preparation steps unless a curator can find Lupa et al. preparation evidence, and rerun enrichment/migration for rows that still lack `mediaingredientmech_chebi_term` entries where CHEBI grounding is already available.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validators on the regenerated merged record.
- Re-count the source formula after regeneration and confirm 27 MediaDB compounds are represented exactly once.
- Search the regenerated YAML for `Tryptone`, `Yeast extract`, `LB Medium`, `Luria`, and `Miller`; the search should return no matches for this MediaDB-only record unless primary-source support is added.
- Re-check `MEDIADB:474` in the normalized source indexes with ignored files included.

## Additional Notes

The rendered MediaDB page, text export, source page, and one representative growth page were inspected directly. MediaDB 474 links multiple growth-data records for Methanococcus maripaludis mutants; the ingredient defects above are already visible on the medium-level page and text export.
