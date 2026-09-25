# YAML Record Review: lactate_bicarbonate_buffered_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactate_bicarbonate_buffered_medium__61c2aabd.yaml
- Started UTC: 2026-09-23T18:06:21Z
- Finished UTC: 2026-09-23T18:07:19Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/lactate_bicarbonate_buffered_medium__61c2aabd.yaml`, generated `MediaRecipe` record `CultureMech:003203` for MediaDive/JCM medium J857.

- Maintained owners: `data/normalized_yaml/bacterial/lactate_bicarbonate_buffered_medium.yaml`, `data/normalized_yaml/bacterial/glucose_bicarbonate_buffered_medium.yaml`, and `data/normalized_yaml/bacterial/betaine_bicarbonate_buffered_medium.yaml`.
- Merge provenance: `merged_from` lists the MediaDive J770 betaine parent plus the J857 lactate and J1281 glucose children; generated merge fingerprint `61c2aabdd45e610b335e0f6ef37b5677371ae3b4fc3d5f68c209d59125f9af09`.
- Source claim: JCM Medium J857, `mediadive.medium:J857`, original JCM medium 857.
- Current generated identity: `medium_type: COMPLEX`, `composition_type: SEMI_DEFINED`, `physical_state: LIQUID`.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lactate_bicarbonate_buffered_medium__61c2aabd.yaml`. |
| Strict schema | Passed with `python scripts/validate_strict.py data/merge_yaml/merged/lactate_bicarbonate_buffered_medium__61c2aabd.yaml --out /private/tmp/lactate_bicarbonate_buffered_medium__61c2aabd.strict.tsv --workers 1 --quiet`. |
| Reference integrity | Passed with `linkml-reference-validator validate data data/merge_yaml/merged/lactate_bicarbonate_buffered_medium__61c2aabd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; there were 0 checks. |
| Term integrity | Passed with `linkml-term-validator validate-data data/merge_yaml/merged/lactate_bicarbonate_buffered_medium__61c2aabd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` files, not embedded `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

An exact ignored-file-inclusive search of `data/normalized_yaml` and `data/merge_yaml` for `CultureMech:003203`, `mediadive.medium:J857`, `mediadive.medium:J770`, and `mediadive.medium:J1281` found only the J857 lactate owner, J770 betaine parent, J1281 glucose owner, and this generated merge.

JCM 857 and MediaDive J857 identify the target as `LACTATE+BICARBONATE BUFFERED MEDIUM`; JCM 857 is a recipe note that instructs curators to use JCM 770 while replacing the betaine solution in Solution B with 1.0 M sodium lactate to make 10.0 mM final lactate. JCM 1281 gives the parallel glucose replacement. JCM 770 is the betaine parent, not a source duplicate of either child.

The merged record incorrectly treats all three as source duplicates. Worse, both maintained children still contain the parent `Betaine` row copied from JCM 770, so the J857 lactate record currently describes a mixture with betaine plus a one-line lactate replacement instruction instead of a betaine-free lactate variant.

## Evidence

The inspected JCM pages and MediaDive REST payloads agree on the recipe roles:

- J770 is the complete betaine-bicarbonate buffered medium with Solution A, Solution B, Solution C, phosphate, trace-metal, mineral-salt, and vitamin stock recipes.
- J857 is a J770-derived lactate variant that replaces betaine solution in Solution B with 1.0 M sodium lactate.
- J1281 is a J770-derived glucose variant that replaces betaine solution in Solution B with 1.0 M glucose.

MediaDive J857 and J1281 expose only the replacement step, so copying the referenced J770 composition was a reasonable transform. The transform is incomplete, though: it copied every J770 ingredient into the children without deleting the betaine row or adding explicit sodium lactate and glucose rows. The copied ingredients also flatten J770 stock-solution concentrations into one top-level list, so vitamin and trace-metal stock recipes appear at stock strength rather than as 1 ml additions to 50 ml Solution B.

## Completeness

The generated record is missing critical variant and preparation structure:

- Lactate, glucose, and betaine are separate JCM media, not source synonyms of one medium.
- J857 needs a sodium lactate replacement for the J770 betaine row.
- J1281 needs a glucose replacement for the J770 betaine row.
- J770 stock boundaries and final assembly under an 80:20 N2-CO2 gas mixture are not represented.
- The only `preparation_steps` row is the J857 replacement instruction; all J770 stock preparation, filtration, autoclaving, anaerobic assembly, and final pH checks are absent.

Empty target organism rows are acceptable: the inspected JCM/MediaDive pages describe formulas only and do not assert strain-specific growth.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The merge falsely collapses J770, J857, and J1281 carbon-source variants into one generated record. | J857 replaces betaine with sodium lactate and J1281 replaces betaine with glucose; those are variant modifications, not source duplicates of J770. | Merge fingerprint logic plus all three MediaDive/JCM maintained owners |
| Blocker | The copied J857 and J1281 child formulas still contain betaine. | `copy_referenced_compositions` copied J770 ingredients into the J857 and J1281 owners, but the JCM child instructions say to replace the betaine solution. | `data/normalized_yaml/bacterial/lactate_bicarbonate_buffered_medium.yaml` and `data/normalized_yaml/bacterial/glucose_bicarbonate_buffered_medium.yaml` |
| Major | J770 nested stock solutions are flattened into a top-level ingredient list. | MediaDive J770 and JCM 770 keep phosphate, trace-metal, mineral-salt, and vitamin solution recipes separate; the merged YAML lists stock-strength trace and vitamin ingredients as if they were final medium ingredients. | J770 import and `copy_referenced_compositions` |
| Major | J770 preparation is largely absent after copy and merge. | JCM 770 specifies Solution A autoclaving, Solution B and C filter sterilization under N2-CO2, final anaerobic assembly, and a pH 6.9 to 7.2 check; the merged J857 record keeps only the one-line lactate replacement instruction. | `data/normalized_yaml/bacterial/lactate_bicarbonate_buffered_medium.yaml` and transform logic |

## Recommended Edits

1. Change reference-copying for J857 and J1281 so the betaine solution from J770 is replaced by sodium lactate or glucose rather than copied into the child.
2. Preserve J770, J857, and J1281 as separate variant records; do not merge them as source duplicates.
3. Preserve J770 solution boundaries and represent 1 ml or 12.5 ml stock additions instead of flattening all stock ingredients at stock strength.
4. Copy or reference the J770 preparation instructions when expanding J857 and J1281, then append the specific lactate or glucose replacement step.
5. Regenerate `data/merge_yaml/merged` after fixing the maintained records and copy/merge transforms.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators against the regenerated J770, J857, and J1281 merged records.
- Inspect regenerated J857 and J1281 to confirm betaine is absent and sodium lactate or glucose is present.
- Inspect regenerated `merged_from` blocks to confirm betaine, lactate, and glucose records are not merged under one fingerprint.
- Recompare the regenerated solution hierarchy against MediaDive J770 and JCM 770.

## Additional Notes

This is distinct from `lactate_bicarbonate_buffered_medium.yaml`, the TOGO-derived merge that also conflates lactate and glucose variants. Both generated records trace back to JCM 857, but one is owned by the MediaDive/JCM import path and the other is owned by the TOGO import path.
