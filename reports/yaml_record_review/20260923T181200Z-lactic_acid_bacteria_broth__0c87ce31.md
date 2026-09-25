# YAML Record Review: lactic_acid_bacteria_broth

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactic_acid_bacteria_broth__0c87ce31.yaml
- Started UTC: 2026-09-23T18:11:21Z
- Finished UTC: 2026-09-23T18:12:00Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/lactic_acid_bacteria_broth__0c87ce31.yaml`, generated `MediaRecipe` record `CultureMech:002551` for MediaDive/JCM medium J18.

- Maintained owner: `data/normalized_yaml/bacterial/lactic_acid_bacteria_broth.yaml`.
- Merge provenance: `merged_from: lactic_acid_bacteria_broth`; generated merge fingerprint `0c87ce316fc67efb1274377fe2d0b17b04438d225799a9fda113a263c11faf13`.
- Source claim: JCM Medium J18 / `mediadive.medium:J18`, original JCM GRMD 18.
- Current generated identity: `medium_type: COMPLEX`, `composition_type: UNDEFINED`, `physical_state: LIQUID`, pH 5.2.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactic_acid_bacteria_broth__0c87ce31.yaml`; the command exited 0 with no output. |
| Strict schema | Passed with `python scripts/validate_strict.py data/merge_yaml/merged/lactic_acid_bacteria_broth__0c87ce31.yaml --out /private/tmp/lactic_acid_bacteria_broth__0c87ce31.strict.tsv --workers 1 --quiet`. |
| Reference integrity | Passed with `linkml-reference-validator validate data data/merge_yaml/merged/lactic_acid_bacteria_broth__0c87ce31.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; there were 0 checks. |
| Term integrity | Passed with `linkml-term-validator validate-data data/merge_yaml/merged/lactic_acid_bacteria_broth__0c87ce31.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

JCM GRMD 18 and MediaDive J18 both identify the target as `LACTIC ACID BACTERIA BROTH` at pH 5.1 to 5.3, so the top-level source identity and pH are grounded. An exact ignored-file-inclusive search over the relevant normalized and generated YAML files for `CultureMech:002551`, `mediadive.medium:J18`, `JCM Medium J18`, and the JCM GRMD 18 URL found this MediaDive/JCM owner and generated merge plus a separate TOGO M11 owner and generated `LACTIC_ACID_BACTERIA_BROTH.yaml` that point to the same JCM recipe.

JCM 18 defines two distinct stock solutions. Solution A contains K2HPO4 and KH2PO4 in 100 ml distilled water, while Solution B contains MgSO4 x 7 H2O, NaCl, FeSO4 x 7 H2O, MnSO4 x n H2O, and 100 ml distilled water. The current normalized record loses that boundary and flattens both stock recipes into top-level ingredients at stock strength.

## Evidence

The JCM main recipe lists 10 g Trypticase peptone, 5 g yeast autolysate, 12 g sodium acetate, 10 g glucose, 5 ml Solution A, 5 ml Solution B, and 1 L distilled water. It then instructs pH adjustment to 5.1 to 5.3. MediaDive normalizes the main recipe to a 1010 ml final volume, which supports the first four generated `G_PER_L` values.

The JCM stock rows do not support the stock ingredients as final-medium `G_PER_L` rows. K2HPO4 and KH2PO4 are present at 10 g per 100 ml in Solution A and only 5 ml of Solution A is added to the final medium. MgSO4 x 7 H2O, NaCl, FeSO4 x 7 H2O, and MnSO4 x n H2O are in separate Solution B, and only 5 ml of that stock is added. The MediaDive JSON already shows the parsing bug: both the Solution A and Solution B main-solution additions point at `solution_id: 3641`, after which the Solution A object contains all rows from both JCM stocks.

## Completeness

The record is incomplete in several consequential places:

- Solution A and Solution B are not represented as separate additions.
- Stock ingredients are not diluted to final-medium concentrations.
- The `MIX` preparation step contains only literal HTML for a Solution B heading and no instruction.
- The separate TOGO M11 import of the same JCM 18 source remains unmerged.
- JCM and MediaDive source metadata are not represented in structured `sources` or `source_data`.

Empty `target_organisms` is acceptable: the inspected JCM and MediaDive pages describe the formulation and do not assert growth of a particular organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | JCM Solution A and Solution B were conflated. | JCM 18 has separate 5 ml additions of Solution A and Solution B; MediaDive maps both to `solution_id: 3641`, and the YAML has no separate Solution B. | MediaDive import for `data/normalized_yaml/bacterial/lactic_acid_bacteria_broth.yaml` |
| Major | Stock solution ingredients are flattened at stock strength. | The generated K2HPO4, KH2PO4, MgSO4, NaCl, FeSO4, and MnSO4 values are the stock concentrations, not their final concentrations after adding 5 ml of each stock to the 1010 ml main recipe. | `data/normalized_yaml/bacterial/lactic_acid_bacteria_broth.yaml` or importer logic |
| Major | A stock-table heading is stored as a preparation step. | The second `preparation_steps` row contains only `<I>Solution B: </I>`, which is an HTML heading from the JCM table, not a preparation instruction. | `data/normalized_yaml/bacterial/lactic_acid_bacteria_broth.yaml` |
| Major | JCM 18 is duplicated across import paths. | The exact ignored-inclusive YAML search found this MediaDive/JCM owner and a separate TOGO M11 owner for the same JCM GRMD 18 source. | Merge or cross-import duplicate resolution |
| Minor | JCM provenance is only free text. | The JCM 18 URL is stored in `notes`; no structured `sources` slot captures JCM GRMD 18 or the MediaDive REST source. | `data/normalized_yaml/bacterial/lactic_acid_bacteria_broth.yaml` |

## Recommended Edits

1. Correct the JCM 18 import so Solution A and Solution B remain separate stock solutions and the main recipe adds 5 ml of each.
2. Recalculate stock components to final concentrations only if the schema requires flattening; otherwise, preserve Solution A and Solution B as referenced solutions.
3. Remove the HTML-only `preparation_steps` row.
4. Resolve the MediaDive J18 and TOGO M11 source duplicate once both imports have comparable solution structure.
5. Add structured JCM/MediaDive source metadata and regenerate the merged YAML.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators against the regenerated merged record.
- Recompare Solution A and Solution B row by row against JCM GRMD 18 and MediaDive J18.
- Confirm the regenerated record has no `<I>Solution B: </I>` preparation row.
- Search with `rg --no-ignore --hidden` for `GRMD=18` and `mediadive.medium:J18` in maintained and generated YAML to confirm the JCM and TOGO imports are intentionally linked or merged.

## Additional Notes

The broad term `J18` overmatches unrelated JCM accessions such as J180 through J189, so exact source searches for this record must either anchor `mediadive.medium:J18` at line end or search the literal GRMD 18 URL.
