# YAML Record Review: MOPS medium; VanBogelen

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mops_medium_vanbogelen.yaml
- Started UTC: 2026-09-24T14:05:48Z
- Finished UTC: 2026-09-24T14:06:30Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007057 |
| Name | mops_medium_vanbogelen |
| Original name | MOPS medium; VanBogelen |
| Source owner | data/normalized_yaml/bacterial/mops_medium_vanbogelen.yaml |
| Generated record | Yes; produced under data/merge_yaml/merged with merge_fingerprint 15c6e97714cfbbebc1b33070e036b9c60523f4c2827fc8c0cd2ac2b1b0a40bba |

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mops_medium_vanbogelen.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/mops_medium_vanbogelen.yaml --out /private/tmp/mops_medium_vanbogelen.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows, and the TSV contained only the header. |
| `linkml-reference-validator validate data data/merge_yaml/merged/mops_medium_vanbogelen.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| `linkml-term-validator validate-data data/merge_yaml/merged/mops_medium_vanbogelen.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded `curation_history` | Not checked: the documented history validator targets the standalone `history/` corpus, not inline `MediaRecipe.curation_history`. |

## Identity and Grounding

The record denotes MediaDB medium 166, `Mops medium; vanbogelen`, with 11 millimolar compounds. The MediaDB page and tab-delimited export support all 11 compound amounts in the YAML: D-glucose 22.0, thiamine 0.01, magnesium chloride 0.523, calcium chloride anhydrous 0.0005, potassium sulfate 0.276, potassium dibasic phosphate 1.0, sodium chloride 50.0, ammonium chloride 9.52, ferrous sulfate 0.01, MOPS 40.0, and tricine 4.0 mM.

An ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml` for `MEDIADB:166`, `MediaDB Medium 166`, `mops_medium_vanbogelen`, `MOPS medium; VanBogelen`, and `Medium ID: 166` found only the expected normalized owner, generated output, and index entries.

Two grounding issues remain. `Magnesium chloride` is grounded to magnesium chloride hexahydrate even though MediaDB exports magnesium chloride and CHEBI 6636, not a hydrated salt. `Thiamine` still has a legacy `mediaingredientmech_term` instead of a `mediaingredientmech_chebi_term`.

## Evidence

The local formula is quantitatively faithful to MediaDB medium 166. The MediaDB medium page lists the same 11 compounds and the tab-delimited export agrees with the generated values.

The provenance is too coarse. MediaDB medium 166 links to source 60, `Vanbogelen et al, 1987`, and that source page records the Journal of Bacteriology article `Differential induction of heat shock, sos, and oxidation stress regulations and accumulation of nucleotides in escherichia coli` plus PMID 3539918. The medium page and growth-data record 335 identify the organism as `Escherichia coli W3110`; the growth-data record also stores growth rate 0.24 1/h, pH 7.4, and temperature 37.0.

The preparation steps are unsupported. MediaDB gives concentrations, organism, source, and growth data, but the inspected medium page, tab-delimited export, source page, and growth-data page do not state to dissolve all ingredients in water, adjust pH if specified, or sterilize by 0.22 um filtration.

## Completeness

No empty optional fields are present.

The recipe is incomplete for source-local context: it does not preserve MediaDB's organism, source-page, PMID, or growth-data links, and it replaces all of them with the MediaDB root URL and generic systems-biology applications. The record also lacks a pH/growth-condition representation for MediaDB growth-data record 335.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The magnesium chloride row has a hydrate-specific CHEBI term unsupported by MediaDB. | MediaDB exports `Magnesium chloride` with CHEBI 6636; the YAML uses CHEBI:86345 `magnesium dichloride hexahydrate`. | `data/normalized_yaml/bacterial/mops_medium_vanbogelen.yaml` and CHEBI enrichment. |
| Major | The preparation steps are generic and unsupported. | None of the inspected MediaDB medium 166, media text 166, source 60, or growth-data 335 pages mention the generated pH-adjustment or 0.22 um filtration instructions. | The MediaDB import that produced `data/normalized_yaml/bacterial/mops_medium_vanbogelen.yaml`. |
| Major | MediaDB source specificity is lost. | The medium page points to source 60, growth-data 335, and *Escherichia coli* W3110, while the YAML only cites the MediaDB root URL and a coarse Mazumdar et al. import note. | `data/normalized_yaml/bacterial/mops_medium_vanbogelen.yaml`; the MediaDB importer should carry medium/source/growth-data IDs. |
| Minor | Thiamine still uses a legacy MediaIngredientMech field. | The ingredient has `mediaingredientmech_term: MediaIngredientMech:000898` instead of a CHEBI-keyed `mediaingredientmech_chebi_term`. | MediaIngredientMech migration over the normalized MediaDB owner. |

## Recommended Edits

1. Reground `Magnesium chloride` to CHEBI:6636 or another non-hydrate magnesium chloride term supported by the MediaDB export.
2. Remove or qualify the generic dissolve, pH, and filter-sterilization steps unless a source-specific method from Vanbogelen et al. 1987 is inspected and added.
3. Replace the root MediaDB provenance with exact links or structured references for medium 166, source 60, PMID 3539918, and growth-data record 335.
4. Add *Escherichia coli* W3110 and the MediaDB pH 7.4 / 37.0 / 0.24 1/h growth data if the schema has an appropriate target-organism or growth-condition slot.
5. Refresh MediaIngredientMech migration so thiamine uses a CHEBI-keyed mirror instead of a legacy MediaIngredientMech identifier.

## Follow-up Checks

- Rerun `linkml-validate`, `scripts/validate_strict.py`, `linkml-reference-validator`, and `linkml-term-validator` on the regenerated MOPS VanBogelen record.
- Recompare all 11 mM compound amounts against MediaDB `media_text/166`.
- Manually inspect MediaDB medium 166, source 60, and growth-data 335 to confirm the exact provenance and growth context are present.
- Run an ignored-inclusive search for `MEDIADB:166` and `mops_medium_vanbogelen` across `data/normalized_yaml` and `data/merge_yaml` to confirm no duplicate owner was introduced.

## Additional Notes

The formula itself matches the inspected MediaDB page; the defects are grounding, provenance, and unsupported generated process text.
