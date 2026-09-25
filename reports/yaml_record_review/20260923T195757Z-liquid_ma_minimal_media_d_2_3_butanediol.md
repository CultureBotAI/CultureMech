# YAML Record Review: Liquid ma minimal media + d-2,3-butanediol

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/liquid_ma_minimal_media_d_2_3_butanediol.yaml
- Started UTC: 2026-09-23T19:56:33Z
- Finished UTC: 2026-09-23T19:57:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007103 |
| Name | liquid_ma_minimal_media_d_2_3_butanediol |
| Original name | Liquid ma minimal media + d-2,3-butanediol |
| Category | bacterial |
| Medium/composition type | DEFINED / DEFINED |
| Physical state | LIQUID |
| Structured pH | None |
| Media grounding | MEDIADB:20 |
| Source provenance | MediaDB Medium 20 |
| Generated file | data/merge_yaml/merged/liquid_ma_minimal_media_d_2_3_butanediol.yaml |
| Maintained owner | data/normalized_yaml/bacterial/liquid_ma_minimal_media_d_2_3_butanediol.yaml |
| Merge fingerprint | 4e7ee0d57fbd398873cf8b204b482e015786430e408a42ba0a1cea4dd3be56ae |

The reviewed target is a generated one-source MediaDB merge. Future fixes belong in `data/normalized_yaml/bacterial/liquid_ma_minimal_media_d_2_3_butanediol.yaml` or the MediaDB importer, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/liquid_ma_minimal_media_d_2_3_butanediol.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/liquid_ma_minimal_media_d_2_3_butanediol.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The MediaDB HTML and tab-delimited pages confirm that MediaDB 20 is `Liquid ma minimal media + d-2,3-butanediol`, a minimal defined medium whose 25 mM carbon-source row is `(R,R)-Butane-2,3-diol`.

The generated record keeps the correct stable ID, source accession, bacterial category, and 17 source amount values, but it predates the maintained owner's 2026-08-31 repair of three labels truncated at internal close parentheses.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007103`, anchored `MEDIADB:20`, the maintained filename, and the merge fingerprint found only this generated record and its maintained owner.

## Evidence

Supported in the inspected MediaDB sources:

- MediaDB Medium 20 lists 17 components and their millimolar amounts. The generated YAML preserves those amount values, including 25 mM `(R,R)-Butane-2,3-diol`.
- The corrected MediaDB labels for the three truncated rows are `(R,R)-Butane-2,3-diol` at 25 mM, `Iron(III) chloride` at 0.003 mM, and `Chromium(III) Chloride` at 0.0003 mM.
- MediaDB links this medium to `Acinetobacter baylyi ADP1`, Durot et al. 2008, and Growth Data 48.
- The reused MediaDB source page identifies Durot et al., 2008, in BMC Systems Biology, with PubMed ID 18840283.

Unsupported or incomplete in the generated record:

- The generated ingredient names `'(R,R`, `'Iron(III`, and `'Chromium(III` are truncated and no longer identify the carbon source or chloride salts in MediaDB.
- The maintained owner has an unmerged 2026-08-31 `repair_mediadb_names.py` event that restored those three labels, but the generated target does not include it yet.
- MediaDB reports CHEBI:16982 for `(R,R)-Butane-2,3-diol`, CHEBI:30808 for Iron(III) chloride, and CHEBI:53351 for Chromium(III) Chloride in the tab-delimited source; the maintained owner restored the labels but still leaves all three rows ungrounded.
- The record has generic dissolve, pH-adjustment, and 0.22 um filter-sterilization steps that are not present on the inspected MediaDB medium, growth-data, organism, or source pages.
- The MediaDB organism, growth-data, and publication links are absent from structured organism/growth evidence and structured references.

## Completeness

The record is complete for the MediaDB 20 identity, all 17 component amounts, and high-level defined/minimal classification.

It is incomplete for the three post-import repaired labels, MediaDB-provided CHEBI groundings for the butanediol, iron, and chromium rows, MediaDB's Acinetobacter baylyi ADP1 growth-data association, structured Durot et al. and MediaDB references, and source-supported preparation information. Empty optional pH, incubation, and storage fields are acceptable for this review because the inspected MediaDB medium and growth-data pages expose those values as absent.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Three ingredient identities are truncated in the generated target. | MediaDB names `(R,R)-Butane-2,3-diol`, `Iron(III) chloride`, and `Chromium(III) Chloride`; the generated record stores only `'(R,R`, `'Iron(III`, and `'Chromium(III`. The maintained owner has repaired those labels, but the repair has not been regenerated. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_d_2_3_butanediol.yaml` |
| Major | Generic preparation steps are unsupported. | The generated YAML asserts dissolve, pH-adjustment, and 0.22 um filter-sterilization steps; the inspected MediaDB medium, tab-delimited, growth-data, organism, and source pages do not describe preparation. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_d_2_3_butanediol.yaml` or the MediaDB importer |
| Major | The MediaDB growth-data association is missing. | MediaDB links medium 20 to Growth Data 48 for `Acinetobacter baylyi ADP1` from Durot et al. 2008; the YAML has no structured target organism or growth-evidence entry. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_d_2_3_butanediol.yaml` |
| Minor | Source-provided CHEBI IDs remain missing for the repaired rows. | The MediaDB tab-delimited view reports CHEBI:16982 for `(R,R)-Butane-2,3-diol`, CHEBI:30808 for Iron(III) chloride, and CHEBI:53351 for Chromium(III) Chloride; all three rows are ungrounded in the maintained owner and truncated in the generated target. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_d_2_3_butanediol.yaml` |
| Minor | Structured references are missing. | The generated target carries only a generic MediaDB URL in `notes`, and the reference validator performed zero checks. | `data/normalized_yaml/bacterial/liquid_ma_minimal_media_d_2_3_butanediol.yaml` |

## Recommended Edits

1. Regenerate this merge after the 2026-08-31 maintained-owner label repair so `(R,R)-Butane-2,3-diol`, `Iron(III) chloride`, and `Chromium(III) Chloride` replace the truncated generated labels.
2. Remove or replace the generic preparation steps unless a citable source is inspected for this medium's filtration, pH, and dissolution procedure.
3. Add structured MediaDB and Durot et al. 2008 references, including PubMed ID 18840283 if the schema can represent it.
4. Add a bounded target-organism or growth-evidence entry for MediaDB Growth Data 48 that is scoped to `Acinetobacter baylyi ADP1` and does not invent growth rate, pH, or temperature values that MediaDB reports as absent.
5. Ground `(R,R)-Butane-2,3-diol`, Iron(III) chloride, and Chromium(III) Chloride to the CHEBI IDs exported by MediaDB if those IDs are accepted by the current term validator.
6. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated record against MediaDB medium 20 and `/media_text/20/` for all 17 ingredient names, millimolar values, and exported CHEBI IDs.
- Re-run an ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007103`, anchored `MEDIADB:20`, and `liquid_ma_minimal_media_d_2_3_butanediol` after regeneration to confirm the maintained owner and generated target agree.

## Additional Notes

None found.
