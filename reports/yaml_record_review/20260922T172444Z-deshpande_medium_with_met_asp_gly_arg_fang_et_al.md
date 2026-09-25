# YAML Record Review: deshpande_medium_with_met_asp_gly_arg_fang_et_al

- Repository: CultureMech
- Record: `data/merge_yaml/merged/deshpande_medium_with_met_asp_gly_arg_fang_et_al.yaml`
- Started UTC: 2026-09-22T17:24:44Z
- Finished UTC: 2026-09-22T17:24:44Z
- Verdict: needs curation

## Target

Generated bacterial `deshpande_medium_with_met_asp_gly_arg_fang_et_al` record for MediaDB Medium 207.

## Validation

- LinkML validation against `MediaRecipe`: passed.
- Strict validation via `scripts/validate_strict.py`: passed.
- Reference validation via `linkml-reference-validator`: passed.
- Term validation via `linkml-term-validator`: passed.
- Embedded `curation_history`: not checked; the standalone `history/` validator is not scoped to embedded generated-record history.

## Identity and Grounding

The record is grounded to MediaDB 207, `Deshpande medium with Met, Asp, Gly, Arg; Fang et al`. The live MediaDB page and tab-delimited export list the same 15 compounds at the same millimolar concentrations as the generated record.

The defined/defined classification is supported because every MediaDB 207 component is a named chemical compound.

## Evidence

The generated file is stale relative to `data/normalized_yaml/bacterial/deshpande_medium_with_met_asp_gly_arg_fang_et_al.yaml`. The normalized source gained an L-Aspartate CHEBI grounding on 2026-08-20, and `repair_mediadb_names.py` restored `Iron(III) chloride` on 2026-08-31; the generated record still leaves `L-Aspartate` without a term and still emits the parser-truncated `'''Iron(III'` row.

MediaDB's tab-delimited export carries CHEBI IDs for Glycine, L-Aspartate, L-Methionine, Arginine, calcium chloride anhydrous, potassium dihydrogen phosphate, cobalt chloride, zinc sulfate, manganese chloride, cupric sulfate, sodium citrate, Iron(III) chloride, and sodium borate. The generated record omits the available source CHEBI groundings for L-Aspartate, Iron(III) chloride, and Sodium borate.

MediaDB 207 lists a compound table, two organisms, the Fang et al. source citation, and two growth-data rows. It does not state pH adjustment or 0.22 um filtration instructions, so the generated `preparation_steps` are importer-generic assumptions rather than source-specific evidence.

## Completeness

All 15 MediaDB compounds are present with matching millimolar values, including the Met, Asp, Gly, and Arg additions above base Deshpande medium.

The source supports Bacillus subtilis 168 and Bacillus subtilis 1S53 growth on this medium via two MediaDB growth-data records, but the generated CultureMech record retains only broad applications and does not preserve organism-specific evidence.

## Findings

- Needs curation: `'''Iron(III'` is a stale generated artifact from the MediaDB SQL parser's parenthesis truncation.
- Needs curation: available CHEBI groundings for L-Aspartate, Iron(III) chloride, and Sodium borate are absent.
- Needs curation: `preparation_steps` assert generic pH adjustment and 0.22 um filtration steps that are not backed by MediaDB 207.
- Minor issue: the two MediaDB Bacillus subtilis growth-evidence rows are not represented in target-organism evidence.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/deshpande_medium_with_met_asp_gly_arg_fang_et_al.yaml` from the repaired normalized source so `Iron(III) chloride` and the L-Aspartate grounding are restored.
- Add or verify CHEBI terms for `Iron(III) chloride`, `Sodium borate`, and `Molybdic acid ammonium salt tetrahydrate` from MediaDB's compound metadata.
- Remove generic preparation steps or mark them explicitly as assumptions if the schema needs non-null preparation guidance.
- Add Bacillus subtilis 168 and Bacillus subtilis 1S53 as target organism evidence for MediaDB's growth-data records if target-organism curation is in scope.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validators after regeneration.
- Recheck the 15 MediaDB 207 rows against `/defined_media/media_text/207/`.
- Confirm no generated ingredient name remains truncated at a parenthesis.
- Confirm L-Aspartate retains the grounding present in normalized YAML.

## Additional Notes

MediaDB Medium 207 and its tab-delimited export were reachable during review.
