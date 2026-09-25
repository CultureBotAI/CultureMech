# YAML Record Review: ms10_medium_supplements_acetate_for_batch_cultivation

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ms10_medium_supplements_acetate_for_batch_cultivation.yaml
- Started UTC: 2026-09-24T15:19:23Z
- Finished UTC: 2026-09-24T15:23:18Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| CultureMech ID | CultureMech:007315 |
| Name | ms10_medium_supplements_acetate_for_batch_cultivation |
| Original name | MS10 Medium + Supplements + Acetate for Batch Cultivation |
| Category | bacterial |
| Source identity | MEDIADB:414 |
| Reviewed artifact | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/ms10_medium_supplements_acetate_for_batch_cultivation.yaml |
| Merge status | One source recipe; `merged_from: ms10_medium_supplements_acetate_for_batch_cultivation` |

## Validation

| Check | Result |
| --- | --- |
| Open schema validation with `linkml-validate` | Passed; `No issues found` |
| Strict validation with `scripts/validate_strict.py` | Passed with 0 errors |
| Reference validation with `linkml-reference-validator` | Passed; 0 reference checks |
| Term validation with `linkml-term-validator` | Passed |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML |

## Identity and Grounding

The medium identity is correct. MediaDB Medium 414 is titled `Ms10 medium + supplements + acetate for batch cultivation`, exposes a tab-delimited export for the same 31 compounds, links organism 171 `Lactococcus lactis MG1363`, links source 127 `Nordkvist m et al, 2003`, and links Growth Data 798 for Lactococcus lactis MG1363 on the same medium.

An exact gitignore-independent search for `CultureMech:007315`, `MEDIADB:414`, `MediaDB Medium 414`, and the MediaDB 414 page forms under `data/normalized_yaml` and `data/merge_yaml` found only this generated record, its maintained owner, and generated indexes. No sibling MediaDB 414 recipe was found in those record corpora.

Several ingredient quantities and groundings are exact: the generated record preserves all 31 MediaDB millimolar amounts, and the ChEBI terms for cysteine, proline, sodium acetate, glucose, glycine, nicotinate, biotin, pyridoxamine, thiamine, DL-methionine, calcium pantothenate, ammonium sulfate, manganese chloride, arginine, histidine, tryptophan, and asparagine are source-backed or exact.

Other ontology mappings are too narrow or too broad relative to the MediaDB export:

- MediaDB exports `Valine` with `CHEBI:27266` for `valine`, but the YAML asserts `CHEBI:16414` for `L-valine`.
- MediaDB exports `Phenylalanine` with `CHEBI:28044` for `phenylalanine`, but the YAML asserts `CHEBI:17295` for `L-phenylalanine`.
- MediaDB exports `Alanine` with `CHEBI:16449` for `alanine`, but the YAML asserts `CHEBI:16977` for `L-alanine`.
- MediaDB exports `Lipoate` with `CHEBI:30314` for `(R)-lipoic acid`, but the YAML asserts only `CHEBI:16494` for `lipoic acid`.

## Evidence

Supported source claims:

- MediaDB Medium 414 and the MediaDB tab-delimited export support the `MEDIADB:414` identity, title, `DEFINED` composition, liquid defined-medium status, and 31 compound amounts in millimolar units.
- MediaDB Source 127 supports PubMed 12788751: Nordkvist M, Jensen NB, and Villadsen J, 2003, `Glucose metabolism in Lactococcus lactis MG1363 under different aeration conditions: requirement of acetate to sustain growth under microaerobic conditions.`
- MediaDB Growth Data 798 supports the associated organism, Lactococcus lactis MG1363, and its growth on Medium 414 at pH 6.6, 30 C, and microaerobic conditions.

Unsupported or stale claims:

- The imported history says `Reference: Mazumdar et al. (2014) PLOS One`, but MediaDB Medium 414 links only source 127, Nordkvist M et al. 2003, and PubMed 12788751.
- The Valine, Phenylalanine, Alanine, and Lipoate ChEBI mappings above do not preserve MediaDB's own ChEBI identifiers.
- The maintained owner has a 2026-08-20 `apply_mim_groundings.py` history event that adds the previously absent threonine grounding; the generated record is still the older 2026-08-06 merge and leaves `Threonine` ungrounded.

## Completeness

The formulation itself is largely complete: all MediaDB 414 compound rows and amounts are present.

Consequential gaps remain:

- Source provenance points to the wrong paper in curation history and does not preserve the linked MediaDB source page or PMID.
- The generated output is stale relative to the maintained owner for the threonine grounding.
- MediaDB Growth Data 798 is not represented as a `target_organisms` entry, growth metric, pH value, temperature value, or incubation-atmosphere note. This is a bounded import gap from the linked MediaDB growth-data object rather than a mismatch in the formulation table.

Empty term slots on `DL-Serine`, `Glutamine`, and `Lysine-HCl` are acceptable until exact stereochemistry or salt groundings are resolved.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The source-paper provenance names an unrelated citation. | MediaDB Medium 414 links Source 127, Nordkvist M et al. 2003, PMID 12788751; the record's MediaDB import event says `Reference: Mazumdar et al. (2014) PLOS One`. | data/normalized_yaml/bacterial/ms10_medium_supplements_acetate_for_batch_cultivation.yaml |
| Major | Three amino acids are narrowed from the generic source ChEBI IDs to `L-` enantiomers. | MediaDB exports Valine/CHEBI:27266, Phenylalanine/CHEBI:28044, and Alanine/CHEBI:16449, but the YAML asserts L-valine/CHEBI:16414, L-phenylalanine/CHEBI:17295, and L-alanine/CHEBI:16977. | data/normalized_yaml/bacterial/ms10_medium_supplements_acetate_for_batch_cultivation.yaml |
| Major | Lipoate is broadened away from the source-provided stereospecific ChEBI ID. | MediaDB exports Lipoate/CHEBI:30314, which the local ChEBI cache labels `(R)-lipoic acid`; the YAML asserts generic lipoic acid/CHEBI:16494. | data/normalized_yaml/bacterial/ms10_medium_supplements_acetate_for_batch_cultivation.yaml |
| Major | The generated record is stale for the threonine repair. | The maintained owner contains an `apply_mim_groundings.py` 2026-08-20 event and adds threonine/CHEBI:26986; the generated merge predates that event and leaves `Threonine` ungrounded. | data/normalized_yaml/bacterial/ms10_medium_supplements_acetate_for_batch_cultivation.yaml |
| Minor | `Thiamine` still carries a deprecated `mediaingredientmech_term` link. | The record still has `MediaIngredientMech:000898` even though the 2026-06-05 migration history says old MediaIngredientMech IDs were replaced with CHEBI-keyed links because that ID scheme was deprecated. | data/normalized_yaml/bacterial/ms10_medium_supplements_acetate_for_batch_cultivation.yaml |

## Recommended Edits

1. Replace the incorrect Mazumdar import provenance with MediaDB's Source 127 citation and PubMed 12788751 in `data/normalized_yaml/bacterial/ms10_medium_supplements_acetate_for_batch_cultivation.yaml`.
2. Reconcile Valine, Phenylalanine, Alanine, and Lipoate against the MediaDB tab-delimited export, preserving exact source ChEBI IDs unless the source paper supports a narrower stereochemical assertion.
3. Convert the remaining `Thiamine` `mediaingredientmech_term` to the current CHEBI-keyed MediaIngredientMech slot or leave it empty if no exact CHEBI-keyed link exists.
4. Consider importing MediaDB Growth Data 798 as target-organism and condition evidence for Lactococcus lactis MG1363 at pH 6.6, 30 C, and microaerobic conditions.
5. Rerun the merge generator so the generated record picks up the maintained 2026-08-20 threonine grounding and the provenance fixes above.

## Follow-up Checks

1. Re-run open schema, strict, reference, and term validation on the regenerated merged record.
2. Re-diff all 31 regenerated compounds against `https://mediadb.systemsbiology.net/defined_media/media_text/414/`.
3. Re-check MediaDB Source 127 and PubMed 12788751 to confirm the record no longer cites the unrelated Mazumdar paper.
4. Run the exact gitignore-independent `MEDIADB:414` duplicate search again after regeneration to make sure no sibling source record was introduced.

## Additional Notes

- Growth data ID 414 is a different Bacillus subtilis record; the relevant linked growth data for MediaDB Medium 414 is Growth Data 798.
- The exact duplicate search above included ignored files.
