# YAML Record Review: lactate_salt_schaechter_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactate_salt_schaechter_et_al.yaml
- Started UTC: 2026-09-23T18:08:01Z
- Finished UTC: 2026-09-23T18:09:10Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/lactate_salt_schaechter_et_al.yaml`, generated `MediaRecipe` record `CultureMech:007126` for MediaDB medium 230.

- Maintained owner: `data/normalized_yaml/bacterial/lactate_salt_schaechter_et_al.yaml`.
- Merge provenance: `merged_from: lactate_salt_schaechter_et_al`; generated merge fingerprint `ab9a5e01e4a6b99e7d2cda5e4358a75f53ad009d5bac06d4698a90c25e62eac2`.
- Source claim: MediaDB medium 230 / `MEDIADB:230`.
- Current generated identity: `medium_type: DEFINED`, `composition_type: DEFINED`, `physical_state: LIQUID`.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactate_salt_schaechter_et_al.yaml`. |
| Strict schema | Passed with `python scripts/validate_strict.py data/merge_yaml/merged/lactate_salt_schaechter_et_al.yaml --out /private/tmp/lactate_salt_schaechter_et_al.strict.tsv --workers 1 --quiet`. |
| Reference integrity | Passed with `linkml-reference-validator validate data data/merge_yaml/merged/lactate_salt_schaechter_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; there were 0 checks. |
| Term integrity | Passed with `linkml-term-validator validate-data data/merge_yaml/merged/lactate_salt_schaechter_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

MediaDB medium 230 resolves to `Lactate salt; schaechter et al` and lists six millimolar ingredients. An exact ignored-file-inclusive search of `data/normalized_yaml` and `data/merge_yaml` for `CultureMech:007126`, `MEDIADB:230`, and `mediadive.medium:J526` found one maintained MediaDB 230 owner, the generated merge, sibling Schaechter MediaDB salt records that carry the same suspect `kg_microbe_match`, and a real JCM J526 owner for `norris_ferroplasma_medium`.

The generated record is stale relative to its owner. `data/normalized_yaml/bacterial/lactate_salt_schaechter_et_al.yaml` repaired the second ingredient to `(R)-Lactate` on 2026-08-31, but the reviewed merge still has the truncated `'''(R` value. The generated record also carries `kg_microbe_match: mediadive.medium:J526`; MediaDive J526 is JCM `NORRIS FERROPLASMA MEDIUM`, not a Schaechter lactate salt medium.

## Evidence

The MediaDB text view for medium 230 supports all six compound rows and millimolar amounts in the current maintained owner: citrate 5.20497, `(R)-Lactate` 22.4543, dibasic sodium phosphate 28.0899, potassium chloride 9.92605, magnesium sulfate 0.405729, and sodium ammonium phosphate 8.32187.

MediaDB source 84 identifies the primary source as Schaechter et al. 1958 and links PMID 13611202. NCBI E-utilities verified PMID 13611202 as the 1958 `J Gen Microbiol` paper by Schaechter, Maaloe, and Kjeldgaard on Salmonella typhimurium medium and temperature dependence.

MediaDB growth data 454 links this medium to `Salmonella enterica Typhimurium LT2`, pH 7.0, and a 0.624 1/h growth rate. The record has no target organism or growth metric for that source assertion.

No inspected source page supports the generated preparation steps. MediaDB medium 230 gives a six-row amount table, source 84, organism 67, and growth data 454; it does not say to adjust pH or filter-sterilize through a 0.22 um filter.

## Completeness

The ingredient list is complete for MediaDB medium 230 in the maintained owner after the `(R)-Lactate` name repair. Consequential gaps remain:

- The generated artifact has not been regenerated since that repair.
- The MediaDB growth-data row is absent.
- Structured source metadata for MediaDB source 84 and PMID 13611202 is absent.
- `(R)-Lactate` has MediaDB ChEBI ID 42111, but the maintained YAML has no `term` for that row.
- `kg_microbe_match` points at an unrelated JCM/MediaDive medium.

No additional maintained YAML duplicate for `MEDIADB:230` was found by the exact ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record is stale and still contains the MediaDB parser truncation artifact for `(R)-Lactate`. | The reviewed merge has `'''(R`; the maintained owner repaired that row to `(R)-Lactate` after the merge timestamp. | Regenerate from `data/normalized_yaml/bacterial/lactate_salt_schaechter_et_al.yaml` |
| Major | `kg_microbe_match` is a false cross-reference. | `mediadive.medium:J526` resolves to JCM Norris Ferroplasma Medium at pH 1.2, not MediaDB lactate salt from Schaechter et al. | `data/normalized_yaml/bacterial/lactate_salt_schaechter_et_al.yaml` |
| Major | Preparation steps are unsupported generic placeholders. | The inspected MediaDB pages do not support pH adjustment or 0.22 um filtration instructions. | `data/normalized_yaml/bacterial/lactate_salt_schaechter_et_al.yaml` |
| Major | MediaDB growth evidence is not represented. | MediaDB growth data 454 associates medium 230 with `Salmonella enterica Typhimurium LT2`, pH 7.0, and growth rate 0.624 1/h. | `data/normalized_yaml/bacterial/lactate_salt_schaechter_et_al.yaml` |
| Minor | Primary source metadata is incomplete. | MediaDB source 84 and PMID 13611202 are absent from the YAML, and `(R)-Lactate` is missing the ChEBI identifier that MediaDB supplies. | `data/normalized_yaml/bacterial/lactate_salt_schaechter_et_al.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/lactate_salt_schaechter_et_al.yaml` so the maintained `(R)-Lactate` repair reaches the generated artifact.
2. Remove `kg_microbe_match: mediadive.medium:J526` from this record and the sibling Schaechter salt records unless a source-supported JCM match exists.
3. Remove the generic preparation steps or replace them with source-supported preparation evidence.
4. Add a source-scoped Salmonella LT2 growth assertion for MediaDB growth data 454.
5. Add structured references for MediaDB source 84 and PMID 13611202, and map `(R)-Lactate` to the supplied ChEBI term if it is valid in the repository's ChEBI source.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators against the regenerated merged record.
- Recheck MediaDB `/defined_media/media_text/230/` row by row and confirm the generated record now has `(R)-Lactate`.
- Query MediaDive J526 and confirm no `kg_microbe_match` remains between that Norris Ferroplasma source and Schaechter salt records.
- Inspect MediaDB growth data 454 and source 84 after curation to ensure the growth rate, pH, and PMID stay scoped to Salmonella LT2 on this lactate salt medium.

## Additional Notes

The same unsupported `kg_microbe_match: mediadive.medium:J526` appears in several Schaechter salt records found by exact ignored-inclusive search. They should be audited as a family rather than by patching only this generated lactate record.
