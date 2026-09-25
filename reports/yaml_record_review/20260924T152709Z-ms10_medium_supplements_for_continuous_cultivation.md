# YAML Record Review: ms10_medium_supplements_for_continuous_cultivation

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ms10_medium_supplements_for_continuous_cultivation.yaml
- Started UTC: 2026-09-24T15:25:00Z
- Finished UTC: 2026-09-24T15:27:09Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:007313 |
| Name | ms10_medium_supplements_for_continuous_cultivation |
| Original name | MS10 Medium + Supplements for Continuous Cultivation |
| Category | bacterial |
| Source identity | MEDIADB:412, merged with MEDIADB:413 |
| Reviewed artifact | Generated merge output |
| Maintained owners | data/normalized_yaml/bacterial/ms10_medium_supplements_for_continuous_cultivation.yaml; data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation.yaml |
| Merge status | Generated from two source recipes: `ms10_medium_supplements_for_continuous_cultivation` and `ms10_medium_supplements_for_batch_cultivation` |

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate` | Passed; `No issues found` |
| Strict validation with `scripts/validate_strict.py` | Passed with 0 errors |
| Reference validation with `linkml-reference-validator` | Passed; 0 reference checks |
| Term validation with `linkml-term-validator` | Passed |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML |

## Identity and Grounding

The canonical source identity is MediaDB Medium 412, titled `Ms10 medium + supplements for continuous cultivation`, but the generated merge also collapses MediaDB Medium 413, titled `Ms10 medium + supplements for batch cultivation`, into a synonym. The two sources are not identical: MediaDB 412 contains 16.65 mM glucose and links Source 126, Jensen NB et al. 2001, while MediaDB 413 contains 55.51 mM glucose and links Source 127, Nordkvist M et al. 2003.

The generated record currently mixes those identities: `media_term` says `MEDIADB:412` continuous cultivation, while the ingredient list says glucose is 55.51 mM, which belongs to MEDIADB:413 batch cultivation.

An exact gitignore-independent search for `CultureMech:007313`, `MEDIADB:412`, `CultureMech:007314`, and `MEDIADB:413` under `data/normalized_yaml` and `data/merge_yaml` found the two maintained normalized records, their generated merged output, and generated indexes. No third MediaDB 412 or 413 recipe was found in those record corpora.

The generated record also has the same over-broad and over-narrow ChEBI issues as its MS10 siblings:

- MediaDB exports `Valine` with `CHEBI:27266` for `valine`, but the YAML asserts `CHEBI:16414` for `L-valine`.
- MediaDB exports `Phenylalanine` with `CHEBI:28044` for `phenylalanine`, but the YAML asserts `CHEBI:17295` for `L-phenylalanine`.
- MediaDB exports `Alanine` with `CHEBI:16449` for `alanine`, but the YAML asserts `CHEBI:16977` for `L-alanine`.
- MediaDB exports `Lipoate` with `CHEBI:30314` for `(R)-lipoic acid`, but the YAML asserts only `CHEBI:16494` for `lipoic acid`.

## Evidence

Supported source claims:

- MediaDB Medium 412 and its tab-delimited export support the `MEDIADB:412` identity, title, `DEFINED` composition, liquid defined-medium status, and 30 continuous-cultivation compound rows.
- MediaDB Source 126 and PubMed 11375180 support Jensen NB et al. 2001 as the literature source for the continuous-cultivation medium.
- MediaDB Growth Data 796 supports the associated organism, Lactococcus lactis MG1363, and its growth on Medium 412 at pH 6.6 and 30 C.
- MediaDB Medium 413 and its tab-delimited export support a separate batch-cultivation recipe with the same 30 compound names but 55.51 mM rather than 16.65 mM glucose.

Unsupported or stale claims:

- The generated record claims a single merged recipe for MediaDB 412 and 413 even though the two sources have different glucose amounts.
- The generated MediaDB 412 record uses the MediaDB 413 glucose amount.
- The imported history says `Reference: Mazumdar et al. (2014) PLOS One`, but MediaDB Medium 412 links Source 126, Jensen NB et al. 2001, and PubMed 11375180.
- The Valine, Phenylalanine, Alanine, and Lipoate ChEBI mappings above do not preserve MediaDB's own ChEBI identifiers.
- The maintained MediaDB 412 and 413 owners both have a 2026-08-20 `apply_mim_groundings.py` history event that adds the previously absent threonine grounding; the generated record is still the older 2026-08-06 merge and leaves `Threonine` ungrounded.

## Completeness

The generated record includes the expected 30 compound rows for one MS10 source, but it is not a complete representation of the two merged sources because it collapses a continuous-cultivation formulation and a batch-cultivation formulation with different glucose concentrations into one flat ingredient list.

Consequential gaps remain:

- The generated record cannot simultaneously represent MediaDB 412 at 16.65 mM glucose and MediaDB 413 at 55.51 mM glucose without splitting the records or modeling the difference as a variant.
- Source provenance points to the wrong paper in curation history and only retains the canonical MediaDB 412 import event, not the MEDIADB:413 source citation that appears in `merged_from`.
- MediaDB Growth Data 796 is not represented as a `target_organisms` entry, growth metric, pH value, or temperature value.

Empty term slots on `DL-Serine`, `Glutamine`, and `Lysine-HCl` are acceptable until exact stereochemistry or salt groundings are resolved.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Distinct MediaDB 412 and MediaDB 413 formulations are merged as duplicates. | MediaDB 412 continuous cultivation contains 16.65 mM glucose; MediaDB 413 batch cultivation contains 55.51 mM glucose. The generated record names MEDIADB:412 but emits the 55.51 mM batch glucose amount and lists MEDIADB:413 as a synonym. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_continuous_cultivation.yaml; data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation.yaml; merge logic |
| Major | The source-paper provenance names an unrelated citation. | MediaDB Medium 412 links Source 126, Jensen NB et al. 2001, PMID 11375180; the record's MediaDB import event says `Reference: Mazumdar et al. (2014) PLOS One`. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_continuous_cultivation.yaml |
| Major | Three amino acids are narrowed from the generic source ChEBI IDs to `L-` enantiomers. | MediaDB exports Valine/CHEBI:27266, Phenylalanine/CHEBI:28044, and Alanine/CHEBI:16449, but the YAML asserts L-valine/CHEBI:16414, L-phenylalanine/CHEBI:17295, and L-alanine/CHEBI:16977. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_continuous_cultivation.yaml; data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation.yaml |
| Major | Lipoate is broadened away from the source-provided stereospecific ChEBI ID. | MediaDB exports Lipoate/CHEBI:30314, which the local ChEBI cache labels `(R)-lipoic acid`; the YAML asserts generic lipoic acid/CHEBI:16494. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_continuous_cultivation.yaml; data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation.yaml |
| Major | The generated record is stale for the threonine repair. | The maintained owners contain 2026-08-20 `apply_mim_groundings.py` events and add threonine/CHEBI:26986; the generated merge predates those events and leaves `Threonine` ungrounded. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_continuous_cultivation.yaml; data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation.yaml |
| Minor | `Thiamine` still carries a deprecated `mediaingredientmech_term` link. | The records still have `MediaIngredientMech:000898` even though their 2026-06-05 migration history says old MediaIngredientMech IDs were replaced with CHEBI-keyed links because that ID scheme was deprecated. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_continuous_cultivation.yaml; data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation.yaml |

## Recommended Edits

1. Split MediaDB 412 and MediaDB 413 back into separate generated records, or model the 16.65 mM versus 55.51 mM glucose difference explicitly as source-scoped variants.
2. Replace the incorrect Mazumdar import provenance with MediaDB's Source 126 citation and PubMed 11375180 in `data/normalized_yaml/bacterial/ms10_medium_supplements_for_continuous_cultivation.yaml`; retain Source 127 / PubMed 12788751 for the separate MediaDB 413 batch record.
3. Reconcile Valine, Phenylalanine, Alanine, and Lipoate against the MediaDB tab-delimited exports, preserving exact source ChEBI IDs unless the source papers support narrower stereochemical assertions.
4. Convert the remaining `Thiamine` `mediaingredientmech_term` to the current CHEBI-keyed MediaIngredientMech slot or leave it empty if no exact CHEBI-keyed link exists.
5. Rerun the merge generator so `data/merge_yaml/merged/ms10_medium_supplements_for_continuous_cultivation.yaml` no longer mixes the MediaDB 412 identity with the MediaDB 413 glucose amount and picks up the 2026-08-20 threonine repair.

## Follow-up Checks

1. Re-run open schema, strict, reference, and term validation on the regenerated merged records.
2. Re-diff the continuous record against `https://mediadb.systemsbiology.net/defined_media/media_text/412/` and the batch record against `https://mediadb.systemsbiology.net/defined_media/media_text/413/`, with a specific assertion that their glucose amounts remain distinct.
3. Re-check MediaDB Source 126 and PubMed 11375180 to confirm the continuous record no longer cites the unrelated Mazumdar paper.
4. Run the exact gitignore-independent `MEDIADB:412` and `MEDIADB:413` duplicate searches again after regeneration to make sure the two source accessions are represented exactly once each.

## Additional Notes

- Growth Data 796 is linked to the continuous MediaDB 412 record. Growth Data 797, 800, and 802 are linked to the batch MediaDB 413 record.
- The exact duplicate search above included ignored files.
