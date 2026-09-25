# YAML Record Review: mogensen_minimal_medium_glucose

- Repository: CultureMech
- Record: data/merge_yaml/merged/mogensen_minimal_medium_glucose.yaml
- Started UTC: 2026-09-24T13:52:48Z
- Finished UTC: 2026-09-24T13:53:12Z
- Verdict: needs curation

## Target

Reviewed merged generated record `CultureMech:007207`, `mogensen_minimal_medium_glucose`, imported from MediaDB medium 309 and emitted as a defined liquid bacterial recipe with 15 millimolar ingredients.

## Validation

The generated record passed the focused open schema validator; it exited 0 with no diagnostics.

Strict validation passed with 0 errors. The TSV output contained only its header row.

Reference validation passed. The checker executed 0 reference checks for this record.

Term validation passed. The validator emitted the known `eutils` / `pkg_resources` warning before reporting success.

Embedded `curation_history` entries were not checked: `just validate-history` validates standalone `history/` content, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The generated record is stale relative to the normalized source owner. `data/merge_yaml/merged/mogensen_minimal_medium_glucose.yaml` still carries the malformed `original_name: '''Mogensen Minimal Medium (Glucose` and `media_term.term.label: '''Mogensen Minimal Medium (Glucose` values that were repaired in `data/normalized_yaml/bacterial/mogensen_minimal_medium_glucose.yaml` on 2026-08-31.

The `MediaDB Medium 309` grounding is the right external identity for the glucose variant. MediaDB medium 309 is named `Mogensen minimal medium (glucose)` on the live page.

The recipe category is not supported by the linked biological evidence. The MediaDB page lists two organisms, `Aspergillus nidulans A187` and `Aspergillus nidulans creA`, while the CultureMech record is typed as `category: bacterial`.

`Sodium EDTA` has a concentration but no structured `term` or `mediaingredientmech_chebi_term` grounding.

## Evidence

The live MediaDB medium 309 page identifies the medium as `Mogensen minimal medium (glucose)`, flags it as minimal, links the `/defined_media/media_text/309/` tabular export, and lists 15 compounds. Those 15 compounds match the generated ingredient set, including `Glucose` at `55.51` mM.

The same MediaDB page links organisms `Aspergillus nidulans A187` and `Aspergillus nidulans creA`, source 116, and growth data records 633 and 634 for the glucose variant.

MediaDB source 116 identifies first author Mogensen J, journal `Fungal Genetics And Biology : Fg & B`, year 2006, PubMed 16698295, and title `Transcription analysis using high-density micro-arrays of Aspergillus nidulans wild-type and creA mutant during growth on glucose or ethanol.` The source page also links the ethanol growth data records for the same paper.

The generated record instead cites only `Reference: Mazumdar et al. (2014) PLOS One` in import history and the MediaDB root URL in free-text notes. That provenance explains the database import but not the exact medium, source, paper, and growth data used for MediaDB 309.

## Completeness

The structured ingredient list is complete against the 15 compounds visible on the live MediaDB medium 309 page.

The generated preparation section is generic. MediaDB exposes formula rows and source links for this entry, but no inspected MediaDB evidence supports a pH adjustment or 0.22 um filtration step.

The source linkage is incomplete. The generated recipe should preserve MediaDB medium 309, source 116, growth data 633 and 634, and PubMed 16698295 in machine-resolvable provenance rather than retaining only a root MediaDB URL and the 2014 MediaDB database citation.

## Findings

1. The generated record is stale relative to the 2026-08-31 MediaDB name repair. `original_name` and `media_term.term.label` still contain the truncated quoted string instead of `Mogensen Minimal Medium (Glucose)`.

2. `category: bacterial` conflicts with the only organisms on the MediaDB medium 309 page, both of which are `Aspergillus nidulans` strains.

3. Provenance is too coarse. The recipe points to the MediaDB root and Mazumdar et al. 2014, but the inspected source chain for this exact medium is MediaDB medium 309, MediaDB source 116, Mogensen J et al. 2006, PubMed 16698295, and growth data 633/634.

4. The generated `ADJUST_PH` and `FILTER_STERILIZE` preparation steps are unsupported by the inspected MediaDB medium 309 evidence and read as importer filler.

5. `Sodium EDTA` lacks structured ontology grounding.

## Recommended Edits

Refresh or regenerate the merged artifact from the repaired normalized owner so `original_name` and `media_term.term.label` match the restored `Mogensen Minimal Medium (Glucose)` label.

Reclassify the record away from `bacterial` or quarantine it from bacterial exports until fungal records have first-class category support.

Preserve the exact MediaDB provenance chain in the normalized owner: medium 309, source 116, growth data 633 and 634, Mogensen J et al. 2006, and PubMed 16698295.

Remove or mark the generic pH and filtration instructions as unsupported unless Mogensen et al. 2006 or a linked supplement confirms those steps.

Ground `Sodium EDTA` to the most specific appropriate CHEBI term if one exists.

## Follow-up Checks

After editing `data/normalized_yaml/bacterial/mogensen_minimal_medium_glucose.yaml` or the MediaDB merge/import logic, regenerate the merged YAML and rerun open schema, strict, reference, and term validation.

Compare the regenerated formula against the MediaDB `/defined_media/media_text/309/` export and verify that all 15 compounds and the 55.51 mM glucose concentration remain unchanged.

Check the Mogensen ethanol sibling for the same name repair, category, provenance, preparation-step, and `Sodium EDTA` grounding fixes.

## Additional Notes

An exact, ignored-file-inclusive search for `MEDIADB:309`, `MediaDB Medium 309`, and `mogensen_minimal_medium_glucose` under `data/normalized_yaml` and `data/merge_yaml/merged` found this normalized owner and this generated merge record, but no duplicate generated sibling for the same MediaDB source.
