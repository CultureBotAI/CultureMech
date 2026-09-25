# YAML Record Review: mcn_medium_whitman

- Repository: CultureMech
- Record: data/merge_yaml/merged/mcn_medium_whitman.yaml
- Started UTC: 2026-09-24T00:54:10Z
- Finished UTC: 2026-09-24T00:57:49Z
- Verdict: needs curation

## Target

Reviewed generated merged record `data/merge_yaml/merged/mcn_medium_whitman.yaml` for MediaDB medium 473. The exact normalized owner is `data/normalized_yaml/bacterial/mcn_medium_whitman.yaml`; `find` located no same-named owner under another normalized category with ignored files included.

The generated record is stale relative to its normalized owner. It still has `original_name: '''McN Medium (Whitman` and `media_term.term.label: '''McN Medium (Whitman`, while the owner has the 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` curation event and the repaired `McN Medium (Whitman)` label. Exact `MEDIADB:473` scans over the generated record, the owner, and the existing normalized source indexes included ignored files and found the source only on this record family and the matching index entries.

## Validation

- Open LinkML validation against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`: passed with `No issues found`.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows; the strict TSV had a header only.
- LinkML reference validation: passed; 0 reference checks were emitted for this file.
- LinkML term validation with labels and `conf/oak_config.yaml`: passed.
- Embedded `curation_history`: Not checked. The repository `just validate-history` target validates standalone `history/` files rather than embedded generated-record history blocks.

## Identity and Grounding

`media_term.term.id` is `MEDIADB:473`, matching the MediaDB page `/defined_media/media/473/` for `Mcn medium (whitman)`. The source page for `/defined_media/sources/148/` identifies Whitman et al. 1986, `Isolation and Characterization of 22 Mesophilic Methanococci`, and links this medium to growth-data record 861. Growth record 861 links Methanococcus maripaludis JJ, MediaDB medium 473, and source 148 at pH 6.5 and 30.0 C.

No duplicate CultureMech ID or alternate normalized owner was found during exact scans with ignored files included. The record is the only expected merged product for normalized owner `mcn_medium_whitman`.

## Evidence

The MediaDB text export for medium 473 lists 26 tab-delimited source compounds. The generated CultureMech record has 27 `preferred_term` rows.

The target preserves most MediaDB numeric rows, including low-value `2-Mercaptoethanesulfonate` at `7.032e-06` mM, but it is not a faithful transcription of the MediaDB source rows:

- Missing source row: `3-Methylbutanoic acid` at `0.04896` mM.
- Missing source row: `2-methylbutanoic acid` at `0.04896` mM.
- Extra row: `Tryptone` at `10.0` g/L, introduced from a third-party LB Miller product expansion rather than from MediaDB 473.
- Extra row: `Yeast extract` at `5.0` g/L, introduced from the same LB Miller expansion.
- Extra row: an additional `Sodium chloride` at `10.0` g/L, also from the LB Miller expansion; MediaDB 473 already supplies the source `Sodium chloride` row at `376.0` mM.

Exact searches for the two missing acid names over the generated record and normalized owner included ignored files and returned no matches. Exact searches of the MediaDB 473 rendered page and text export found no `Tryptone`, `Yeast extract`, `LB`, `Luria`, or `Miller` evidence for the imported commercial-product expansion.

## Completeness

The MediaDB formula coverage is incomplete because two source compounds are absent and three unrelated LB Miller constituents are present. The importer placeholder `DISSOLVE`, `ADJUST_PH`, and `FILTER_STERILIZE` preparation steps are generic and not supported by the inspected MediaDB medium, source, text, or growth pages.

Several surviving rows also need enrichment cleanup after the source formula is corrected. `Sodium sulfide` and `Cysteine-HCl` still carry only legacy `mediaingredientmech_term` blocks, and `Sodium tungstate`, `Nickel chloride`, and `Cupric sulfate` have `term` mappings without migrated `mediaingredientmech_chebi_term` blocks.

## Findings

1. `needs curation` - The ingredient list mixes MediaDB 473 with an unsupported LB Miller commercial-product expansion. The target adds Tryptone 10.0 g/L, Yeast extract 5.0 g/L, and a second Sodium chloride 10.0 g/L row that are absent from MediaDB medium 473, the MediaDB text export, source 148, and growth record 861.
2. `needs curation` - The ingredient list omits two compounds that are explicitly listed by MediaDB 473: `3-Methylbutanoic acid` 0.04896 mM and `2-methylbutanoic acid` 0.04896 mM.
3. `needs curation` - `data/merge_yaml/merged/mcn_medium_whitman.yaml` is stale relative to `data/normalized_yaml/bacterial/mcn_medium_whitman.yaml`, so the generated record still exposes the SQL-parser truncation in `original_name` and `media_term.term.label`.
4. `minor` - The recipe still has generic importer preparation steps and several incomplete MediaIngredientMech-to-ChEBI migrated links.

## Recommended Edits

Regenerate merged MediaDB 473 from the repaired normalized owner after correcting the normalized recipe to remove the unsupported LB Miller constituent rows and restore both missing branched-chain acid rows from the MediaDB source. Keep the source-backed 376.0 mM `Sodium chloride` row.

Remove the generic preparation steps unless a curator can find Whitman et al. preparation evidence, and rerun enrichment/migration for rows that still lack `mediaingredientmech_chebi_term` entries where CHEBI grounding is already available.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validators on the regenerated merged record.
- Re-count the source formula after regeneration and confirm 26 MediaDB compounds are represented exactly once.
- Search the regenerated YAML for `Tryptone`, `Yeast extract`, `LB Medium`, `Luria`, and `Miller`; the search should return no matches for this MediaDB-only record unless primary-source support is added.
- Re-check `MEDIADB:473` in the normalized source indexes with ignored files included.

## Additional Notes

The rendered MediaDB page, text export, source page, and growth page were inspected directly. The source 148 page links to `/defined_media/growthdata/861/`; `/defined_media/growthdata/473/` is a 404 and should not be used as the growth-data evidence URL for this medium.
