# YAML Record Review: deshpande_medium_fang_et_al

- Repository: CultureMech
- Record: `data/merge_yaml/merged/deshpande_medium_fang_et_al.yaml`
- Started UTC: 2026-09-22T17:19:35Z
- Finished UTC: 2026-09-22T17:19:35Z
- Verdict: needs curation

## Target

Generated bacterial `deshpande_medium_fang_et_al` record for MediaDB Medium 205.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to MediaDB 205, `Deshpande medium; fang et al`. The live MediaDB page and tab-delimited export list the same 11 compounds at the same millimolar concentrations as the CultureMech record.

The defined/defined classification is supported because every MediaDB 205 component is a named chemical compound.

## Evidence

The generated file is stale relative to `data/normalized_yaml/bacterial/deshpande_medium_fang_et_al.yaml`: `repair_mediadb_names.py` fixed the normalized source on 2026-08-31 by restoring `Iron(III) chloride`, but the generated record still has the parser-truncated `'''Iron(III'` preferred term.

MediaDB's tab-delimited export carries PubChem and CHEBI columns for most rows. The generated record omits source CHEBI grounding for `Iron(III) chloride`, despite MediaDB listing CHEBI `30808`, and for `Sodium borate`, despite MediaDB listing CHEBI `38909`.

MediaDB 205 lists only the compound table, organism, source citation, and growth-data row. The generic `preparation_steps` in the generated record are not source-specific; MediaDB does not state a pH to adjust, and the filter-sterilization instruction is an importer assumption rather than an explicit MediaDB 205 condition.

## Completeness

All 11 MediaDB compounds are present with matching millimolar values.

The source supports Bacillus subtilis 168 growth on this medium via MediaDB's growth-data record, but the generated CultureMech record retains only broad applications and does not preserve the organism-specific evidence.

## Findings

- Needs curation: `'''Iron(III'` is a stale generated artifact from the MediaDB SQL parser's parenthesis truncation.
- Needs curation: source CHEBI IDs for `Iron(III) chloride` and `Sodium borate` are absent.
- Needs curation: `preparation_steps` assert generic pH adjustment and 0.22 um filtration steps that are not backed by the MediaDB 205 page.
- Minor issue: the MediaDB Bacillus subtilis 168 growth-evidence row is not represented in target-organism evidence.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/deshpande_medium_fang_et_al.yaml` from the repaired normalized source so `Iron(III) chloride` is restored.
- Add or verify CHEBI terms for `Iron(III) chloride`, `Sodium borate`, and `Molybdic acid ammonium salt tetrahydrate` from MediaDB's compound metadata.
- Remove generic preparation steps or mark them explicitly as assumptions if the schema needs non-null preparation guidance.
- Add `Bacillus subtilis 168` as target organism evidence for MediaDB's growth-data record if target-organism curation is in scope.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Recheck the 11 MediaDB 205 rows against `/defined_media/media_text/205/`.
- Confirm no generated ingredient name remains truncated at a parenthesis.

## Additional Notes

MediaDB Medium 205 and its tab-delimited export were reachable during review.
