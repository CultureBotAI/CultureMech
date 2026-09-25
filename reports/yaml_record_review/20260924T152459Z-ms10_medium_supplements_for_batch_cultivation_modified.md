# YAML Record Review: ms10_medium_supplements_for_batch_cultivation_modified

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ms10_medium_supplements_for_batch_cultivation_modified.yaml
- Started UTC: 2026-09-24T15:23:19Z
- Finished UTC: 2026-09-24T15:24:59Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:007316 |
| Name | ms10_medium_supplements_for_batch_cultivation_modified |
| Original name | `'MS10 Medium + Supplements for Batch Cultivation (Modified` in the generated record; repaired to `MS10 Medium + Supplements for Batch Cultivation (Modified)` upstream |
| Category | bacterial |
| Source identity | MEDIADB:415 |
| Reviewed artifact | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation_modified.yaml |
| Merge status | One source recipe; `merged_from: ms10_medium_supplements_for_batch_cultivation_modified` |

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate` | Passed; `No issues found` |
| Strict validation with `scripts/validate_strict.py` | Passed with 0 errors |
| Reference validation with `linkml-reference-validator` | Passed; 0 reference checks |
| Term validation with `linkml-term-validator` | Passed |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML |

## Identity and Grounding

The source accession is correct but the generated labels are stale. MediaDB Medium 415 is titled `Ms10 medium + supplements for batch cultivation (modified)`, links source 127 `Nordkvist m et al, 2003`, and links Growth Data 799 for Lactococcus lactis MG1363 on the same medium. The maintained owner already repaired the import's truncated parenthetical name, but the generated output still has the leading quote and missing close parenthesis in `original_name` and `media_term.term.label`.

An exact gitignore-independent search for `CultureMech:007316`, `MEDIADB:415`, `MediaDB Medium 415`, and the MediaDB 415 page forms under `data/normalized_yaml` and `data/merge_yaml` found only this generated record, its maintained owner, and generated indexes. No sibling MediaDB 415 recipe was found in those record corpora.

The generated record preserves all 30 MediaDB millimolar amounts and its mapped Cysteine, Proline, Glucose, Glycine, Nicotinate, Biotin, Pyridoxamine, Thiamine, Sodium acetate, DL-methionine, Calcium pantothenate, Ammonium sulfate, Manganese chloride, Arginine, Histidine, Tryptophan, Asparagine, and Potassium dihydrogen phosphate groundings are source-backed or exact.

Three source-generic amino acids are over-narrowed:

- MediaDB exports `Valine` with `CHEBI:27266` for `valine`, but the YAML asserts `CHEBI:16414` for `L-valine`.
- MediaDB exports `Phenylalanine` with `CHEBI:28044` for `phenylalanine`, but the YAML asserts `CHEBI:17295` for `L-phenylalanine`.
- MediaDB exports `Alanine` with `CHEBI:16449` for `alanine`, but the YAML asserts `CHEBI:16977` for `L-alanine`.

## Evidence

Supported source claims:

- MediaDB Medium 415 and the MediaDB tab-delimited export support the `MEDIADB:415` identity, repaired source title, `DEFINED` composition, liquid defined-medium status, and 30 compound amounts in millimolar units.
- MediaDB Source 127 supports PubMed 12788751: Nordkvist M, Jensen NB, and Villadsen J, 2003, `Glucose metabolism in Lactococcus lactis MG1363 under different aeration conditions: requirement of acetate to sustain growth under microaerobic conditions.`
- MediaDB Growth Data 799 supports the associated organism, Lactococcus lactis MG1363, and its growth on Medium 415 at pH 6.6, 30 C, and microaerobic conditions.

Unsupported or stale claims:

- The imported history says `Reference: Mazumdar et al. (2014) PLOS One`, but MediaDB Medium 415 links only source 127, Nordkvist M et al. 2003, and PubMed 12788751.
- The Valine, Phenylalanine, and Alanine ChEBI mappings above do not preserve MediaDB's own ChEBI identifiers.
- The generated record predates both the 2026-08-20 threonine grounding repair and the 2026-08-31 MediaDB truncated-name repair in the maintained owner.

## Completeness

The formulation itself is largely complete: all MediaDB 415 compound rows and amounts are present.

Consequential gaps remain:

- The generated name and media term are stale relative to the maintained owner and the live MediaDB title.
- Source provenance points to the wrong paper in curation history and does not preserve the linked MediaDB source page or PMID.
- MediaDB Growth Data 799 is not represented as a `target_organisms` entry, growth metric, pH value, temperature value, or incubation-atmosphere note. This is a bounded import gap from the linked MediaDB growth-data object rather than a mismatch in the formulation table.

Empty term slots on `DL-Serine`, `Glutamine`, and `Lysine-HCl` are acceptable until exact stereochemistry or salt groundings are resolved.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated identity labels are stale and still carry the MediaDB parenthesis-truncation artifact. | MediaDB Medium 415 and the repaired maintained owner say `MS10 Medium + Supplements for Batch Cultivation (Modified)`; the generated `original_name` and `media_term.term.label` still say `'MS10 Medium + Supplements for Batch Cultivation (Modified`. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation_modified.yaml |
| Major | The source-paper provenance names an unrelated citation. | MediaDB Medium 415 links Source 127, Nordkvist M et al. 2003, PMID 12788751; the record's MediaDB import event says `Reference: Mazumdar et al. (2014) PLOS One`. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation_modified.yaml |
| Major | Three amino acids are narrowed from the generic source ChEBI IDs to `L-` enantiomers. | MediaDB exports Valine/CHEBI:27266, Phenylalanine/CHEBI:28044, and Alanine/CHEBI:16449, but the YAML asserts L-valine/CHEBI:16414, L-phenylalanine/CHEBI:17295, and L-alanine/CHEBI:16977. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation_modified.yaml |
| Major | The generated record is stale for the threonine repair. | The maintained owner contains an `apply_mim_groundings.py` 2026-08-20 event and adds threonine/CHEBI:26986; the generated merge predates that event and leaves `Threonine` ungrounded. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation_modified.yaml |
| Minor | `Thiamine` still carries a deprecated `mediaingredientmech_term` link. | The record still has `MediaIngredientMech:000898` even though the 2026-06-05 migration history says old MediaIngredientMech IDs were replaced with CHEBI-keyed links because that ID scheme was deprecated. | data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation_modified.yaml |

## Recommended Edits

1. Rerun the merge generator so the generated record picks up the maintained 2026-08-31 name repair and 2026-08-20 threonine grounding.
2. Replace the incorrect Mazumdar import provenance with MediaDB's Source 127 citation and PubMed 12788751 in `data/normalized_yaml/bacterial/ms10_medium_supplements_for_batch_cultivation_modified.yaml`.
3. Reconcile Valine, Phenylalanine, and Alanine against the MediaDB tab-delimited export, preserving exact source ChEBI IDs unless the source paper supports a narrower stereochemical assertion.
4. Convert the remaining `Thiamine` `mediaingredientmech_term` to the current CHEBI-keyed MediaIngredientMech slot or leave it empty if no exact CHEBI-keyed link exists.
5. Consider importing MediaDB Growth Data 799 as target-organism and condition evidence for Lactococcus lactis MG1363 at pH 6.6, 30 C, and microaerobic conditions.

## Follow-up Checks

1. Re-run open schema, strict, reference, and term validation on the regenerated merged record.
2. Re-diff all 30 regenerated compounds against `https://mediadb.systemsbiology.net/defined_media/media_text/415/`.
3. Re-check MediaDB Medium 415, MediaDB Source 127, and PubMed 12788751 to confirm the label and citation repairs.
4. Run the exact gitignore-independent `MEDIADB:415` duplicate search again after regeneration to make sure no sibling source record was introduced.

## Additional Notes

- The generated source accession, CultureMech ID, and merge source are correct despite the stale label.
- The exact duplicate search above included ignored files.
