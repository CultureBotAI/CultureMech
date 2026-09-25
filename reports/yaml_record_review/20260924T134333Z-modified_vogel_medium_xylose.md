# YAML Record Review: modified_vogel_medium_xylose

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_vogel_medium_xylose.yaml
- Started UTC: 2026-09-24T13:42:30Z
- Finished UTC: 2026-09-24T13:43:33Z
- Verdict: needs curation

## Target

Reviewed merged generated record `CultureMech:007210`, `modified_vogel_medium_xylose`, imported from MediaDB medium 311 and emitted as a defined liquid bacterial recipe with 14 millimolar ingredients.

## Validation

The generated record passed the focused open schema validator, which reported `No issues found`.

Strict validation passed with 0 errors. The TSV output contained only its header row.

Reference validation passed. The checker executed 0 reference checks for this record.

Term validation passed. The validator emitted the known `eutils` / `pkg_resources` warning before reporting success.

Embedded `curation_history` entries were not checked: `just validate-history` validates standalone `history/` content, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The generated record is stale relative to the normalized source owner. `data/merge_yaml/merged/modified_vogel_medium_xylose.yaml` still carries the malformed `original_name: '''Modified Vogel Medium (xylose` and `media_term.term.label: '''Modified Vogel Medium (xylose` values that were repaired in `data/normalized_yaml/bacterial/modified_vogel_medium_xylose.yaml` on 2026-08-31.

The `MediaDB Medium 311` grounding is the right external identity for the generated recipe. MediaDB medium 311 is named `Modified vogel medium (xylose)` on the live medium page and exposes a tab-delimited export for the same medium.

The recipe category is not supported by the linked biological evidence. The only organism visible on the live MediaDB page is `Aspergillus niger AB1.13`, which is a fungus, while the record is typed as `category: bacterial`.

`Ferrous ammonium sulfate` has a concentration but no structured `term` or `mediaingredientmech_chebi_term` grounding.

## Evidence

The live MediaDB medium 311 page identifies the medium as `Modified vogel medium (xylose)`, flags it as not minimal, links the `/defined_media/media_text/311/` tabular export, and lists 14 compounds. Those 14 compounds match the generated ingredient set, including `Xylose` at `133.2` mM and the same trace salts.

The same MediaDB page links one organism, `Aspergillus niger AB1.13`, one growth data page, `Aspergillus niger AB1.13 on Modified vogel medium (xylose)` at growth data record 636, and source 119.

MediaDB source 119 identifies first author Lu X, journal `Microbial Cell Factories`, year 2010, PubMed 20406453, and title `The intra- and extracellular proteome of Aspergillus niger growing on defined medium with xylose or maltose as carbon substrate.` This is the source-level provenance for MediaDB medium 311.

The record curation history instead says only `Reference: Mazumdar et al. (2014) PLOS One`, and the free-text notes only point to the MediaDB root URL. That provenance is enough to explain the importer but not enough to resolve this medium back to MediaDB 311 and source 119.

## Completeness

The structured ingredient list is complete against the 14 compounds visible on the live MediaDB medium 311 page.

The generated preparation section is generic. MediaDB exports formula rows and source links for this entry, but no evidence inspected for medium 311 supports a pH adjustment or 0.22 um filtration step.

The source linkage is incomplete. The generated recipe should preserve MediaDB medium 311, growth data 636, source 119, and PubMed 20406453 in machine-resolvable provenance instead of retaining only a root MediaDB URL and the 2014 MediaDB database citation.

## Findings

1. The generated record is stale relative to the 2026-08-31 MediaDB name repair. `original_name` and `media_term.term.label` still contain the truncated quoted string instead of `Modified Vogel Medium (xylose)`.

2. `category: bacterial` conflicts with the only organism on the MediaDB medium 311 page, `Aspergillus niger AB1.13`; this record should be curated as fungal or otherwise marked with a non-bacterial CultureMech category if the schema supports one.

3. Provenance is too coarse. The recipe points to the MediaDB root and Mazumdar et al. 2014, but the inspected source chain for this exact medium is MediaDB medium 311, MediaDB source 119, Lu X et al. 2010, PubMed 20406453, and growth data 636.

4. The generated `ADJUST_PH` and `FILTER_STERILIZE` preparation steps are unsupported by the inspected MediaDB medium 311 evidence and read as importer filler.

5. `Ferrous ammonium sulfate` lacks structured ontology grounding while the other trace salts are grounded.

## Recommended Edits

Refresh or regenerate the merged artifact from the repaired normalized owner so `original_name` and `media_term.term.label` match the restored `Modified Vogel Medium (xylose)` label.

Reclassify the record away from `bacterial` or quarantine it from bacterial exports until fungal records have first-class category support.

Preserve the exact MediaDB provenance chain in the normalized owner: medium 311, source 119, growth data 636, Lu X et al. 2010, and PubMed 20406453.

Remove or mark the generic pH and filtration instructions as unsupported unless Lu X et al. 2010 or a linked supplement confirms those steps.

Ground `Ferrous ammonium sulfate` to the most specific appropriate CHEBI term if one exists.

## Follow-up Checks

After editing `data/normalized_yaml/bacterial/modified_vogel_medium_xylose.yaml` or the merge importer, regenerate the merged YAML and rerun open schema, strict, reference, and term validation.

Compare the regenerated formula against the MediaDB `/defined_media/media_text/311/` export and verify that all 14 compounds and the 133.2 mM xylose concentration remain unchanged.

Check the maltose sibling, `modified_vogel_medium_maltose`, for the same category, provenance, preparation-step, and `Ferrous ammonium sulfate` grounding fixes.

## Additional Notes

The adjacent normalized source file already contains a `REPAIRED_MEDIADB_TRUNCATED_NAME` entry explaining that the MediaDB SQL parser truncated values containing an opening parenthesis and that the name was recovered from `media_database.07Oct2015.sql`.
