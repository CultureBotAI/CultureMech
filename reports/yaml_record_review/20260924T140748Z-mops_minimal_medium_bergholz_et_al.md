# YAML Record Review: MOPS minimal medium (Bergholz et al)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mops_minimal_medium_bergholz_et_al.yaml
- Started UTC: 2026-09-24T14:07:12Z
- Finished UTC: 2026-09-24T14:07:48Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:006989 |
| Name | mops_minimal_medium_bergholz_et_al |
| Original name | 'MOPS minimal medium (Bergholz et al |
| Source owner | data/normalized_yaml/bacterial/mops_minimal_medium_bergholz_et_al.yaml |
| Generated record | Yes; produced under data/merge_yaml/merged with merge_fingerprint 62b443a926b29f26572d1e8efcac265d2ee820549973a9323d7b5f562a8f39f8 |

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mops_minimal_medium_bergholz_et_al.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/mops_minimal_medium_bergholz_et_al.yaml --out /private/tmp/mops_minimal_medium_bergholz_et_al.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows, and the TSV contained only the header. |
| `linkml-reference-validator validate data data/merge_yaml/merged/mops_minimal_medium_bergholz_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| `linkml-term-validator validate-data data/merge_yaml/merged/mops_minimal_medium_bergholz_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded `curation_history` | Not checked: the documented history validator targets the standalone `history/` corpus, not inline `MediaRecipe.curation_history`. |

## Identity and Grounding

The record denotes MediaDB medium 102, `Mops minimal medium (bergholz et al)`, with 16 millimolar compounds. The MediaDB page and tab-delimited export support all 16 amounts in the YAML.

The generated record is stale relative to its owner. `data/normalized_yaml/bacterial/mops_minimal_medium_bergholz_et_al.yaml` has an 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` history entry and restores `MOPS minimal medium (Bergholz et al)`, but this generated YAML still has the truncated leading-quote label `'MOPS minimal medium (Bergholz et al`.

An ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml` for `MEDIADB:102`, `MediaDB Medium 102`, `mops_minimal_medium_bergholz_et_al`, `MOPS minimal medium (Bergholz et al)`, and `Medium ID: 102` found only the expected normalized owner, generated output, and index entries.

`Magnesium chloride` is grounded to CHEBI:86345 `magnesium dichloride hexahydrate`; MediaDB exports the ingredient as magnesium chloride and supplies CHEBI 6636 instead.

## Evidence

MediaDB medium 102 lists D-glucose, magnesium chloride, calcium chloride anhydrous, boric acid, potassium sulfate, potassium dibasic phosphate, sodium chloride, ammonium chloride, ferrous sulfate, cobalt chloride, zinc sulfate, manganese chloride, cupric sulfate, molybdic acid ammonium salt tetrahydrate, MOPS, and tricine. The generated record preserves the listed millimolar concentrations exactly.

The provenance is too coarse. MediaDB medium 102 links to source 25, `Bergholz et al, 2007`, and that source page records the BMC Microbiology article `Global transcriptional response of escherichia coli o157:h7 to growth transitions in glucose minimal medium` plus PMID 17967175. Medium 102 and growth-data record 152 identify the organism as `Escherichia coli O157:H7 RIMD0509952`; the growth-data record also stores growth rate 1.08465 1/h, pH 7.4, and temperature 37.0.

The generated preparation steps are unsupported. The inspected MediaDB medium, tab-delimited export, source, and growth-data pages do not state to dissolve all ingredients in water, adjust pH if specified, or sterilize by 0.22 um filtration.

## Completeness

No empty optional fields are present.

The record is incomplete for MediaDB context: it drops the source page, PMID, organism, and growth-data record, and it carries generic applications rather than the specific growth context attached to MediaDB medium 102.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record is stale relative to the maintained name repair. | The normalized owner repaired the original name and media label on 2026-08-31, but this generated file still has the truncated leading-quote name. | Regenerate `data/merge_yaml/merged/mops_minimal_medium_bergholz_et_al.yaml` from `data/normalized_yaml/bacterial/mops_minimal_medium_bergholz_et_al.yaml`. |
| Major | The magnesium chloride row has a hydrate-specific CHEBI term unsupported by MediaDB. | MediaDB exports `Magnesium chloride` with CHEBI 6636; the YAML uses CHEBI:86345 `magnesium dichloride hexahydrate`. | `data/normalized_yaml/bacterial/mops_minimal_medium_bergholz_et_al.yaml` and CHEBI enrichment. |
| Major | The preparation steps are generic and unsupported. | None of the inspected MediaDB medium 102, media text 102, source 25, or growth-data 152 pages mention the generated pH-adjustment or 0.22 um filtration instructions. | The MediaDB import that produced the normalized owner. |
| Major | MediaDB source specificity is lost. | The medium page points to source 25, growth-data 152, and *Escherichia coli* O157:H7 RIMD0509952, while the YAML only cites the MediaDB root URL and a coarse Mazumdar et al. import note. | The MediaDB importer should carry medium/source/growth-data IDs into `data/normalized_yaml/bacterial/mops_minimal_medium_bergholz_et_al.yaml`. |

## Recommended Edits

1. Regenerate merged media after the 2026-08-31 MediaDB name repair so the output carries `MOPS minimal medium (Bergholz et al)`.
2. Reground `Magnesium chloride` to CHEBI:6636 or another non-hydrate magnesium chloride term supported by the MediaDB export.
3. Remove or qualify the generic dissolve, pH, and filter-sterilization steps unless Bergholz et al. 2007 is inspected and supports them.
4. Replace the root MediaDB provenance with exact structured references for medium 102, source 25, PMID 17967175, and growth-data record 152.
5. Add *Escherichia coli* O157:H7 RIMD0509952 and the MediaDB pH 7.4 / 37.0 C / 1.08465 1/h growth data if the schema has an appropriate target-organism or growth-condition slot.

## Follow-up Checks

- Rerun merge generation, then run `linkml-validate`, `scripts/validate_strict.py`, `linkml-reference-validator`, and `linkml-term-validator` on the regenerated MOPS Bergholz record.
- Recompare all 16 mM compound amounts against MediaDB `media_text/102`.
- Manually inspect MediaDB medium 102, source 25, and growth-data 152 to confirm the exact provenance and growth context are present.
- Run an ignored-inclusive search for `MEDIADB:102` and `mops_minimal_medium_bergholz_et_al` across `data/normalized_yaml` and `data/merge_yaml` to confirm no duplicate owner was introduced.

## Additional Notes

The formula matches MediaDB; the defects are stale generated naming, grounding, provenance, and unsupported generated process text.
