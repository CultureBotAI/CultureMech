# YAML Record Review: GYM STREPTOMYCES medium 10% NACL

- Repository: CultureMech
- Record: `data/merge_yaml/merged/gym_streptomyces_medium_10_nacl.yaml`
- Started UTC: 2026-09-23T08:13:36Z
- Finished UTC: 2026-09-23T08:15:07Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:003868`, `gym_streptomyces_medium_10_nacl`, merged from KOMODO medium 1159, DSMZ / MediaDive medium 1159, and an incorrect direct JCM 15% NaCl child.

## Validation

- LinkML validation: passed.
- Strict validation: passed with 0 ERROR rows in `/private/tmp/gym_streptomyces_medium_10_nacl.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked: the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

KOMODO 1159 and DSMZ / MediaDive 1159 are true duplicates for `GYM STREPTOMYCES MEDIUM 10% NACL`: both contain 100 g/L NaCl and the same GYM agar ingredient signature. Exact ignored-file-inclusive search also found the direct JCM/MediaDive `gym_agar_with_15_nacl` parent and Togo `M1055` parent for the 15% NaCl child; those are salinity variants, not exact duplicates of this 10% NaCl formula.

Glucose, CaCO3, NaCl, and Agar are grounded. Yeast extract and Malt extract are ungrounded complex components.

## Evidence

The DSMZ Medium 1159 PDF lists 4.0 g Glucose, 4.0 g Yeast extract, 10.0 g Malt extract, 2.0 g CaCO3, 100.0 g NaCl, 15.0 g Agar, and 1000.0 ml distilled water, followed by `Adjust pH to 7.2. Delete CaCO3 if liquid medium is used.` The generated record preserves the 100 g/L NaCl 10% ingredient signature and pH 7.2.

The normalized DSMZ 10% parent correctly treats `data/normalized_yaml/bacterial/gym_agar_with_15_nacl.yaml` as a `SALINITY_VARIANT` child. The generated record instead lists `gym_agar_with_15_nacl` in `merged_from` and as a synonym with `source_id: mediadive.medium:J999`, even though that child raises NaCl from 100 g/L to 150 g/L.

## Completeness

The ingredient concentrations and pH value are complete for the 10% NaCl DSMZ 1159 formula. The generated record is incomplete because it over-merges a 15% NaCl child as an exact duplicate and drops the DSMZ preparation instruction for pH adjustment and CaCO3 removal in liquid medium. It also carries the KOMODO `2026-01-27T01:15:01.fZ` timestamp into embedded history.

## Findings

- The 15% NaCl JCM child is incorrectly merged into the 10% NaCl generated record. `gym_agar_with_15_nacl` / `mediadive.medium:J999` should remain a salinity variant child; it should not be listed in `merged_from`, `curation_history`, or `synonyms` as an exact source of DSMZ 1159.
- The DSMZ preparation step is missing from the generated record, losing `Adjust pH to 7.2. Delete CaCO3 if liquid medium is used.`
- The generated `media_term` keeps only `komodo.medium:1159`; DSMZ / MediaDive 1159 is represented indirectly via `parent_media`, so generated source identity is less explicit than the true duplicate merge warrants.
- The embedded KOMODO import history timestamp `2026-01-27T01:15:01.fZ` is malformed.
- Yeast extract and Malt extract remain ungrounded. These are complex ingredients, but they should be checked against available mappings.

## Recommended Edits

- Remove the direct JCM 15% NaCl record from the 10% NaCl exact-duplicate merge and preserve it only through `variant_children` / `SALINITY_VARIANT`.
- Preserve the DSMZ 1159 preparation step in the generated 10% NaCl record.
- Make the DSMZ / MediaDive 1159 source identity explicit in regenerated provenance, not only through `parent_media`.
- Fix the malformed KOMODO history timestamp in the normalized KOMODO parent.
- Attempt complex-component groundings for Yeast extract and Malt extract.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validators after recuration.
- Verify that regenerated `merged_from` contains only KOMODO 1159 and DSMZ/MediaDive 1159 exact duplicates.
- Recompare the 10% and 15% GYM records and confirm that the only intended concentration difference is 100 g/L versus 150 g/L NaCl.

## Additional Notes

The MediaDive 1159 REST payload reports a contradictory Agar `amount: 20` and `g_l: 15`; DSMZ's own PDF confirms the correct agar value is 15 g/L, matching the generated record.
