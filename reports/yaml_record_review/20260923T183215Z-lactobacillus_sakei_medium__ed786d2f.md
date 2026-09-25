# YAML Record Review: lactobacillus_sakei_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lactobacillus_sakei_medium__ed786d2f.yaml
- Started UTC: 2026-09-23T18:29:50Z
- Finished UTC: 2026-09-23T18:32:15Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002571` for `lactobacillus_sakei_medium` in `data/merge_yaml/merged/lactobacillus_sakei_medium__ed786d2f.yaml`.

- Source identity: MediaDive/JCM `mediadive.medium:J20`, labeled `LACTOBACILLUS SAKEI MEDIUM`, with JCM link `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=20`.
- Generated lineage: `merge_fingerprint: ed786d2fd2ca08475895fb56e222a365794185cba5eea0028c256c272f2848fc`, `merged_from: lactobacillus_sakei_medium`.
- Maintained owner for record-level fixes: `data/normalized_yaml/bacterial/lactobacillus_sakei_medium.yaml`.
- Current generated state: stale relative to the maintained normalized record, which already contains a September 2026 JCM J20 source repair.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with exit 0. |
| `scripts/validate_strict.py data/merge_yaml/merged/lactobacillus_sakei_medium__ed786d2f.yaml --workers 1 --quiet` | Passed; strict TSV contained only the header and 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lactobacillus_sakei_medium__ed786d2f.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lactobacillus_sakei_medium__ed786d2f.yaml` | Passed with exit 0. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

The record's main medium identity is sound: MediaDive REST record `J20` and the JCM `GRMD=20` page both identify JCM Medium 20 as `LACTOBACILLUS SAKEI MEDIUM`, and MediaDive links that record back to the same JCM page used in the generated `notes`.

The `media_term` CURIE is also aligned with that source recipe, but the copied `kg_microbe_match: mediadive.medium:12` is not. MediaDive medium 12 is DSMZ `SOIL EXTRACT MEDIUM`, a soil-water-agar recipe with pH 6.8 to 7.0 and no Lactobacillus sakei formulation overlap. That match is still present in the maintained normalized JCM J20 record, so a future fix belongs in `data/normalized_yaml/bacterial/lactobacillus_sakei_medium.yaml` before merge regeneration.

## Evidence

MediaDive REST `J20` records an 800 ml `Main sol. J20` recipe containing 700 ml sake, 5 g yeast extract, 13 g agar, 0.2 g liver extract concentrate, and 100 ml distilled water. The live JCM `GRMD=20` source records the same component list and amounts, with source attributes for `Yeast extract (BD-Difco)` and `Liver extract concentrate (NBCo)`. JCM also states the default JCM sterilization instruction to autoclave media at 121 C for 15 min unless otherwise stated.

The generated merge is stale against those inspected sources and against the maintained September 2026 repair:

- It omits the 100 ml distilled-water component from the source 800 ml recipe.
- It records `Sake` as `700 G_PER_L`; source J20 records sake volumetrically as 700 ml in an 800 ml recipe, equivalent to 875 ml/L after normalization.
- It lacks the maintained `MIX` and `AUTOCLAVE` preparation steps and the structured autoclave sterilization object.
- It still has no top-level `references`, so the JCM and MediaDive source URLs visible in the maintained normalized record do not propagate to this generated file.

No inspected source states a pH for JCM J20, so the absent pH in the maintained repair is appropriate.

## Completeness

The generated record is not complete enough for use because its formulation and procedure no longer reflect the authoritative normalized JCM J20 repair. A regenerated merge should contain distilled water, volumetric sake, structured JCM default autoclaving, JCM and MediaDive references, and the JCM/MediaDive support notes now present in `data/normalized_yaml/bacterial/lactobacillus_sakei_medium.yaml`.

No consequential pH, strain-growth, variant, or stock-solution gap was found in this review. The source is a base JCM recipe, not primary growth evidence for one tested target organism, and it has no stock solution nesting.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:002571`, `mediadive.medium:J20`, `GRMD=20`, the merge fingerprint, the source slug, and `LACTOBACILLUS SAKEI MEDIUM` found the maintained normalized owner, the reviewed stale merge, the Togo M13 sibling import of the same JCM recipe, index rows, and archived validation rows. The same bounded search found many other `kg_microbe_match: mediadive.medium:12` fallback-style rows, so the false medium 12 grounding may be systemic but should be fixed for this J20 record in its normalized YAML owner.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated JCM J20 merge is stale and still contains the pre-repair formulation. | MediaDive J20 and JCM `GRMD=20` list an 800 ml recipe with 700 ml sake, 5 g yeast extract, 13 g agar, 0.2 g liver extract concentrate, and 100 ml water. The generated file omits water, stores sake as `700 G_PER_L`, and lacks the JCM default autoclaving details already curated in the normalized record. | Regenerate `data/merge_yaml/merged/lactobacillus_sakei_medium__ed786d2f.yaml` from `data/normalized_yaml/bacterial/lactobacillus_sakei_medium.yaml`; do not patch the generated merge directly. |
| Major | `kg_microbe_match: mediadive.medium:12` grounds the JCM J20 recipe to the wrong medium. | MediaDive medium 12 is DSMZ `SOIL EXTRACT MEDIUM`, whose source, name, ingredients, and pH do not match JCM `LACTOBACILLUS SAKEI MEDIUM`. | Remove or recompute the stale match in `data/normalized_yaml/bacterial/lactobacillus_sakei_medium.yaml`, then regenerate the merge. |

No blocker findings were found: the stable CultureMech ID and primary `media_term` still point to JCM J20, so the record denotes the intended medium despite stale generated content.

No minor findings were found.

## Recommended Edits

1. Remove the false `kg_microbe_match: mediadive.medium:12` from `data/normalized_yaml/bacterial/lactobacillus_sakei_medium.yaml`, or replace it only if a reviewed matching KG-Microbe medium is available.
2. Regenerate `data/merge_yaml/merged/lactobacillus_sakei_medium__ed786d2f.yaml` from `data/normalized_yaml/bacterial/lactobacillus_sakei_medium.yaml` so the generated corpus receives the September 2026 JCM J20 repair.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on `data/normalized_yaml/bacterial/lactobacillus_sakei_medium.yaml` after deleting or recomputing `kg_microbe_match`.
- Re-run the merge pipeline and verify that the generated JCM J20 record contains 875 ml/L sake, 125 ml/L distilled water, 6.25 g/L yeast extract, 16.25 g/L agar, 0.25 g/L liver extract concentrate, the structured autoclave step, and both JCM and MediaDive references.
- Re-run strict, schema, term, and reference validation on the regenerated `data/merge_yaml/merged/lactobacillus_sakei_medium__ed786d2f.yaml`.
- Manually spot-check the regenerated file against MediaDive REST `J20` and JCM `GRMD=20` to confirm that the generated projection did not reintroduce the ml/g artifact.

## Additional Notes

The maintained Togo M13 import of the same JCM Medium 20 recipe already has the same September 2026 800 ml formulation repair, so the generated corpus may collapse or rename the final JCM Lactobacillus sakei merge differently after regeneration.

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
