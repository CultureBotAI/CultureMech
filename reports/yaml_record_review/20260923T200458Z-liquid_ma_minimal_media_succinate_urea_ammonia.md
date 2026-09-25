# YAML Record Review: Liquid MA minimal media + Succinate + Urea - Ammonia

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/liquid_ma_minimal_media_succinate_urea_ammonia.yaml
- Started UTC: 2026-09-23T20:03:37Z
- Finished UTC: 2026-09-23T20:04:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007158 |
| Name | liquid_ma_minimal_media_succinate_urea_ammonia |
| Original name | Liquid MA minimal media + Succinate + Urea - Ammonia |
| Category | bacterial |
| Medium/composition type | DEFINED / DEFINED |
| Physical state | LIQUID |
| Structured pH | None |
| Media grounding | MEDIADB:25 |
| Source provenance | MediaDB Medium 25 |
| Generated file | data/merge_yaml/merged/liquid_ma_minimal_media_succinate_urea_ammonia.yaml |
| Maintained owner | data/normalized_yaml/bacterial/liquid_ma_minimal_media_succinate_urea_ammonia.yaml |
| Merge fingerprint | 925927056f82f30d3f4594aa134562aacbe50cdbec0e5277f2d04529ee9bbea1 |

The reviewed target is a generated one-source MediaDB merge. Future fixes belong in `data/normalized_yaml/bacterial/liquid_ma_minimal_media_succinate_urea_ammonia.yaml` or the MediaDB importer, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/liquid_ma_minimal_media_succinate_urea_ammonia.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/liquid_ma_minimal_media_succinate_urea_ammonia.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The MediaDB HTML and tab-delimited pages confirm that MediaDB 25 is `Liquid ma minimal media + succinate + urea - ammonia`, a minimal defined medium whose variant-specific rows are 25 mM Succinate and 20 mM Urea and whose basal formula omits ammonium chloride.

The generated record keeps the correct stable ID, source accession, bacterial category, Succinate and Urea variant rows, and 17 source amount values, but it predates the maintained owner's 2026-08-31 repair of two labels truncated at an internal close parenthesis.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007158`, anchored `MEDIADB:25`, the maintained filename, and the merge fingerprint found only this generated record and its maintained owner.

## Evidence

Supported in the inspected MediaDB sources:

- MediaDB Medium 25 lists 17 components and their millimolar amounts. The generated YAML preserves those amount values, including 25 mM Succinate and 20 mM Urea.
- The corrected MediaDB labels for the two truncated rows are `Iron(III) chloride` at 0.003 mM and `Chromium(III) Chloride` at 0.0003 mM.
- MediaDB links this medium to `Acinetobacter baylyi ADP1`, Durot et al. 2008, and Growth Data 53.
- The reused MediaDB source page identifies Durot et al., 2008, in BMC Systems Biology, with PubMed ID 18840283.

Unsupported or incomplete in the generated record:

- The generated ingredient names `'Iron(III` and `'Chromium(III` are truncated and no longer identify the chloride salts in MediaDB.
- The maintained owner has an unmerged 2026-08-31 `repair_mediadb_names.py` event that restored those two labels, but the generated target does not include it yet.
- MediaDB reports CHEBI:30808 for Iron(III) chloride and CHEBI:53351 for Chromium(III) Chloride in the tab-delimited source; the maintained owner restored the labels but still leaves both rows ungrounded.
- The record has generic dissolve, pH-adjustment, and 0.22 um filter-sterilization steps that are not present on the inspected MediaDB medium, growth-data, organism, or source pages.
- The MediaDB organism, growth-data, and publication links are absent from structured organism/growth evidence and structured references.

## Completeness

The record is complete for the MediaDB 25 identity, all 17 component amounts, the Succinate + Urea - Ammonia variant, and high-level defined/minimal classification.

It is incomplete for the two post-import repaired labels, MediaDB-provided CHEBI groundings for iron and chromium chloride, MediaDB's Acinetobacter baylyi ADP1 growth-data association, structured Durot et al. and MediaDB references, and source-supported preparation information. Empty optional pH, incubation, and storage fields are acceptable for this review because the inspected MediaDB medium and growth-data pages expose those values as absent.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Two ingredient identities are truncated in the generated target. | MediaDB names `Iron(III) chloride` and `Chromium(III) Chloride`; the generated record stores only `'Iron(III` and `'Chromium(III`. The maintained owner has repaired those labels, but the repair has not been regenerated. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_succinate_urea_ammonia.yaml` |
| Major | Generic preparation steps are unsupported. | The generated YAML asserts dissolve, pH-adjustment, and 0.22 um filter-sterilization steps; the inspected MediaDB medium, tab-delimited, growth-data, organism, and source pages do not describe preparation. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_succinate_urea_ammonia.yaml` or the MediaDB importer |
| Major | The MediaDB growth-data association is missing. | MediaDB links medium 25 to Growth Data 53 for `Acinetobacter baylyi ADP1` from Durot et al. 2008; the YAML has no structured target organism or growth-evidence entry. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_succinate_urea_ammonia.yaml` |
| Minor | Source-provided CHEBI IDs remain missing for the repaired iron and chromium rows. | The MediaDB tab-delimited view reports CHEBI:30808 for Iron(III) chloride and CHEBI:53351 for Chromium(III) Chloride; both rows are ungrounded in the maintained owner and truncated in the generated target. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_succinate_urea_ammonia.yaml` |
| Minor | Structured references are missing. | The generated target carries only a generic MediaDB URL in `notes`, and the reference validator performed zero checks. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_succinate_urea_ammonia.yaml` |

## Recommended Edits

1. Regenerate this merge after the 2026-08-31 maintained-owner label repair so `Iron(III) chloride` and `Chromium(III) Chloride` replace the truncated generated labels.
2. Remove or replace the generic preparation steps unless a citable source is inspected for this medium's filtration, pH, and dissolution procedure.
3. Add structured MediaDB and Durot et al. 2008 references, including PubMed ID 18840283 if the schema can represent it.
4. Add a bounded target-organism or growth-evidence entry for MediaDB Growth Data 53 that is scoped to `Acinetobacter baylyi ADP1` and does not invent growth rate, pH, or temperature values that MediaDB reports as absent.
5. Ground Iron(III) chloride and Chromium(III) Chloride to the CHEBI IDs exported by MediaDB if those IDs are accepted by the current term validator.
6. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated record against MediaDB medium 25 and `/media_text/25/` for all 17 ingredient names, millimolar values, and exported CHEBI IDs.
- Re-run an ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007158`, anchored `MEDIADB:25`, and `liquid_ma_minimal_media_succinate_urea_ammonia` after regeneration to confirm the maintained owner and generated target agree.

## Additional Notes

Ammonium chloride is intentionally absent from MediaDB 25, unlike the single-carbon variants in this MA minimal medium series.
