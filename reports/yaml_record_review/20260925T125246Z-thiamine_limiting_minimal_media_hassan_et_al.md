# YAML Record Review: thiamine_limiting_minimal_media_hassan_et_al

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiamine_limiting_minimal_media_hassan_et_al.yaml
- Started UTC: 2026-09-25T12:52:46Z
- Finished UTC: 2026-09-25T12:53:10Z
- Verdict: needs curation

## Target

- Generated YAML for the MediaDB 117 thiamine-limiting minimal media Hassan et al record.
- The record was merged from `glucose_limiting_minimal_media_hassan_et_al`, `glucose_minimal_media_hassan_et_al`, `histidine_limiting_minimal_media_hassan_et_al`, and `thiamine_limiting_minimal_media_hassan_et_al`.
- The checked sources were the four local MediaDB imports for MediaDB 115, 116, 117, and 118, plus the MediaDB home page.

## Validation

- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; exited 0 after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to MEDIADB:117, a thiamine-limiting minimal-media record imported from MediaDB.
- MediaDB 115, 116, 117, and 118 were imported as separate glucose, glucose-limiting, thiamine-limiting, and histidine-limiting records, but the merge collapsed all four concentration variants into the MediaDB 117 YAML.
- The `original_name` and MediaDB label are truncated to `'thiamine limiting minimal media (Hassan et al`, including a leading quote with no closing source context.

## Evidence

- The record history says MEDIADB:117 came from the MediaDB import and cites Mazumdar et al. 2014.
- The merged synonyms preserve MEDIADB:115, MEDIADB:116, and MEDIADB:118 as the glucose, glucose-limiting, and histidine-limiting Hassan et al media.
- The MediaDB home page was reachable, but exact MediaDB formulation pages or an exact tabular export for these four medium IDs were not available from the downloaded page.

## Completeness

- The parent and variant fields correctly describe MediaDB 117 as a thiamine concentration variant of the glucose minimal medium record.
- The ingredient list still stores thiamine at 0.113053 mM while `variant_modifications` says the thiamine concentration should decrease to 0.000188423 mM.
- `Sodium ammonium phosphate` has no ChEBI or MediaIngredientMech grounding.
- The preparation steps are generic MediaDB import placeholders rather than source-specific Hassan et al protocol text.

## Findings

- The generated record combines four nonidentical MediaDB concentration variants into one canonical formulation.
- The MediaDB 117 identity conflicts with the ingredient table because thiamine still has the parent glucose-medium concentration.
- The malformed `original_name` and MediaDB label should be restored from exact MediaDB or publication evidence.
- `Sodium ammonium phosphate` remains ungrounded.
- The generic dissolve, pH-adjustment, and filtration steps need replacement or explicit marking as importer defaults.

## Recommended Edits

- Split MediaDB 115, 116, 117, and 118 back into separate exact formulations or model the limiting media as variants with their own ingredient deltas.
- Recompute MediaDB 117 so the ingredient row, variant description, and source ID all represent the same thiamine-limiting formula.
- Ground `Sodium ammonium phosphate` to a reviewed term or leave a curation note documenting why no exact term was accepted.
- Replace the truncated MediaDB label and placeholder preparation steps after consulting an exact MediaDB export or the Hassan et al source.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify all four MediaDB IDs with ignored-file searches before deciding whether to merge or retain variants.
- Check the Mazumdar et al. 2014 source for exact nutrient concentrations and preparation conditions.

## Additional Notes

- None found.
