# YAML Record Review: MRS MEDIUM WITH SOYBEAN PEPTONE

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml
- Started UTC: 2026-09-24T15:13:36Z
- Finished UTC: 2026-09-24T15:15:07Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:003272` / `mrs_medium_with_soybean_peptone` at `data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml`.

- Generated source: `data/normalized_yaml/bacterial/mrs_medium_with_soybean_peptone.yaml`
- Merge source: `mrs_medium_with_soybean_peptone`
- Merge fingerprint: `6fcb2d792bb0d157eb4c73051cad2f9e5b9823dccd0cefa714bc4eb460f88917`
- Category: `bacterial`
- Medium term: `mediadive.medium:J925`, label `MRS MEDIUM WITH SOYBEAN PEPTONE`
- Source: JCM GRMD 925

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml --out /private/tmp/mrs_medium_with_soybean_peptone__6fcb2d79.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The generated record identifies MediaDive/JCM J925, MRS MEDIUM WITH SOYBEAN PEPTONE. JCM GRMD 925 is live and lists 55 g Lactobacilli MRS broth (BD-Difco), 5 g Phytone peptone (BD-BBL), 15 g Bacto agar (BD-Difco), and 1 L distilled water. TOGO M971 mirrors the same JCM source.

The generated record predates the 2026-09-11 normalized repair. The maintained `data/normalized_yaml/bacterial/mrs_medium_with_soybean_peptone.yaml` now has all four source rows, preserves the BD-Difco / BD-BBL qualifiers, grounds Phytone peptone to `FOODON:03315720`, adds the JCM autoclave step, removes stale `kg_microbe_match: mediadive.medium:12`, and links the TOGO M971 source duplicate.

The exact `CultureMech:003272` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found the maintained J925 owner, this generated merge, generated indexes, and the reciprocal duplicate reference in `data/normalized_yaml/bacterial/TOGO_M971_MRS_Medium_With_Soybean_Peptone.yaml`.

## Evidence

JCM GRMD 925 and TOGO M971 support the same four-row soybean-peptone MRS formulation and the default JCM autoclave instruction. An exact ignored-file-inclusive search for `GRMD=925` found both `data/normalized_yaml/bacterial/mrs_medium_with_soybean_peptone.yaml` and `data/normalized_yaml/bacterial/TOGO_M971_MRS_Medium_With_Soybean_Peptone.yaml`, plus their stale generated outputs.

The generated J925 merge still reflects the old three-row MediaDive import: it has no water row, no source qualifiers on the product names, no Phytone peptone FOODON grounding, no JCM autoclave step, no references, no quality flags, no source-duplicate relationship, and a stale `kg_microbe_match: mediadive.medium:12`.

## Completeness

The generated record is stale and incomplete relative to the maintained source. Empty pH, target-organism, and growth-metric fields are acceptable because JCM GRMD 925 does not specify pH or growth evidence.

## Findings

### Major

1. The generated J925 record is stale relative to its repaired normalized owner.
   - Evidence: `data/normalized_yaml/bacterial/mrs_medium_with_soybean_peptone.yaml` has a 2026-09-11 repair event that restored water, product qualifiers, Phytone peptone grounding, autoclave evidence, references, quality flags, and the TOGO M971 source-duplicate link; the generated record still ends at the 2026-08-06 merge event.
   - Impact: generated consumers see an incomplete old J925 import even though the maintained source is already corrected.
   - Owner: regenerate `data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml`.

2. JCM GRMD 925 remains split across TOGO and MediaDive generated outputs.
   - Evidence: the maintained J925 and TOGO M971 records both cite GRMD 925 and now contain reciprocal `SOURCE_DUPLICATE` links, but `data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml` and `data/merge_yaml/merged/MRS_MEDIUM_WITH_SOYBEAN_PEPTONE.yaml` are still separate stale generated outputs.
   - Impact: the same JCM soybean-peptone recipe can publish twice until the merge is regenerated and verified.
   - Owner: regenerate `data/merge_yaml/merged/` and verify the source-duplicate merge rule.

3. The generated record carries a stale KG-Microbe match.
   - Evidence: the generated file still has `kg_microbe_match: mediadive.medium:12`; the 2026-09-11 maintained repair removed that stale MediaDive 12 match from the J925 owner.
   - Impact: generated consumers can link J925 to an unrelated medium until the generated output is refreshed.
   - Owner: regenerate `data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml`.

### Minor

None found.

### Blocker

None found.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from the already repaired `data/normalized_yaml/bacterial/mrs_medium_with_soybean_peptone.yaml` and `data/normalized_yaml/bacterial/TOGO_M971_MRS_Medium_With_Soybean_Peptone.yaml`.
2. Confirm the generated J925/M971 output has the 1 L water row, BD-Difco / BD-BBL qualifiers, Phytone peptone FOODON grounding, JCM autoclave step, source references, data-quality flags, and no `mediadive.medium:12` KG-Microbe match.
3. Confirm the generated corpus no longer publishes both the MediaDive J925 and TOGO M971 source copies as distinct recipes.

## Follow-up Checks

After regeneration, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_soybean_peptone__6fcb2d79.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun merge freshness and an exact ignored-file-inclusive `GRMD=925` search to verify J925 and TOGO M971 no longer emit stale duplicate generated recipes.

## Additional Notes

None found.
