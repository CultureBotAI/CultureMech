# YAML Record Review: HS Medium (Methanol-Acetate)
- Repository: CultureMech
- Record: data/merge_yaml/merged/hs_medium_methanol_acetate.yaml
- Started UTC: 2026-09-23T12:43:48Z
- Finished UTC: 2026-09-23T12:44:41Z
- Verdict: needs curation

## Target

Reviewed the generated MediaDB branch for MediaDB Medium 472, `HS Medium (Methanol-Acetate)`, at `data/merge_yaml/merged/hs_medium_methanol_acetate.yaml`. The maintained source is `data/normalized_yaml/bacterial/hs_medium_methanol_acetate.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hs_medium_methanol_acetate.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record ID, `MEDIADB:472` source accession, and compound signature identify MediaDB Medium 472, `Hs medium (methanol-acetate)`. The generated artifact is stale: both `original_name` and `media_term.term.label` are truncated to a leading quote and `HS Medium (Methanol-Acetate` instead of the repaired maintained label `HS Medium (Methanol-Acetate)`.

## Evidence

MediaDB Medium 472 lists exactly 12 compounds and amounts in mM: acetate 40, methanol 125, magnesium chloride 54, calcium chloride anhydrous 2, resazurin 0.004, sodium bicarbonate 45, sodium chloride 400, potassium chloride 13, cysteine-HCl 2.8, potassium dihydrogen phosphate 5, ammonium chloride 19, and sodium sulfide 0.4. The generated ingredient table matches those amounts.

The MediaDB source page for this medium links the formulation and its growth records to Metcalf WW et al. 1996, PubMed 8824630. The generated `curation_history` still says the MediaDB import reference was Mazumdar et al. 2014, which is the MediaDB database paper rather than the formulation-specific source.

MediaDB 472 and its tab-delimited endpoint do not specify pH or the three generic preparation steps carried in the generated record: dissolve all ingredients in distilled water, adjust pH if specified, and filter-sterilize through a 0.22 um filter.

## Completeness

The concentration table is complete relative to MediaDB's 12 listed compounds. The generated record does not carry MediaDB's two organism/growth records for Methanosarcina acetivorans C2A and Methanosarcina barkeri Fusaro, so growth support is omitted rather than over-scoped. Empty pH is appropriate because MediaDB 472 does not list a pH value.

## Findings

- **major**: The generated artifact is stale and still has the MediaDB SQL-parser truncation in `original_name` and `media_term.term.label`; `data/normalized_yaml/bacterial/hs_medium_methanol_acetate.yaml` has already repaired the label.
- **major**: The three generated `preparation_steps` are unsupported generic importer text, not MediaDB 472 instructions.
- **major**: The import provenance cites Mazumdar et al. 2014 instead of the formulation-specific Metcalf WW et al. 1996 source linked from MediaDB.
- **minor**: MediaDB growth records 859 and 860 are absent from `target_organisms` or `growth_metrics`.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/hs_medium_methanol_acetate.yaml` so the merged artifact inherits the repaired MediaDB 472 label from `data/normalized_yaml/bacterial/hs_medium_methanol_acetate.yaml`.
- Remove the unsupported generic dissolve, pH-adjustment, and filter-sterilization steps from the normalized MediaDB source unless an inspected Metcalf 1996 protocol supports them.
- Replace the generic Mazumdar 2014 import reference with the MediaDB 472 source, Metcalf WW et al. 1996 / PMID 8824630.
- Consider curating MediaDB growth records 859 and 860 into scoped target-organism or growth-metric entries after inspecting those records and the underlying paper.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open MediaDB Medium 472, its tab-delimited endpoint, and MediaDB Source 144 to confirm the regenerated record preserves the 12 supported millimolar ingredients and does not retain unsupported preparation prose.
- Run the repository's merge freshness audit to prove the generated MediaDB 472 branch no longer lags its normalized source.

## Additional Notes

None.
