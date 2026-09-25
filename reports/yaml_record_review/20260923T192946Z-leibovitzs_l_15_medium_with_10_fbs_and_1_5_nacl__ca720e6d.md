# YAML Record Review: LEIBOVITZ'S L-15 MEDIUM WITH 10% FBS AND 1.5% NaCl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl__ca720e6d.yaml
- Started UTC: 2026-09-23T19:28:36Z
- Finished UTC: 2026-09-23T19:29:46Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003278 |
| Name | leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl |
| Original name | LEIBOVITZ'S L-15 MEDIUM WITH 10% FBS AND 1.5% NaCl |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | mediadive.medium:J930 |
| Source provenance | MediaDive JCM Medium J930 |
| Generated file | data/merge_yaml/merged/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl__ca720e6d.yaml |
| Maintained owner | data/normalized_yaml/bacterial/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml |
| Merge fingerprint | ca720e6d5ff15b27d943e500041fbdd9081a0eac27fdbbc36e49465fd1a97468 |

The reviewed target is a generated one-source merge from MediaDive J930. Its maintained owner already contains September 2026 curation, so the needed repair is to regenerate `data/merge_yaml/merged/` and downstream pages from the maintained normalized record.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl__ca720e6d.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl__ca720e6d.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

MediaDive J930 is the JCM `GRMD=930` Leibovitz L-15 with 10% FBS and 1.5% NaCl recipe. The maintained MediaDive owner links Togo M976 / CultureMech:010402 as a `SOURCE_DUPLICATE` child, and the Togo owner links back to this record as its parent.

The generated record is stale relative to `data/normalized_yaml/bacterial/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml`: it lacks the September 2026 unit fixes, MediaDive compound links for L-15 medium and FBS, corrected NaCl concentration, structured JCM/MediaDive references, and source-duplicate child link. An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found this generated record, its maintained owner, the Togo M976 normalized and generated siblings, source indexes, the J930 solution record, and validation archives.

## Evidence

Supported in the inspected MediaDive and JCM sources:

- The MediaDive J930 and JCM 930 identities are supported.
- The recipe contains 1 L Leibovitz's L-15 medium, 100 ml fetal bovine serum, and 15 g NaCl.
- The recipe should be filter-sterilized with a 0.22 um PES filter.
- The maintained MediaDive owner already stores the corrected `L`, `ML_PER_L`, and `G_PER_L` units, the filter step, structured MediaDive/JCM references, a `SOURCE_DUPLICATE` child link to Togo M976, and no MediaDive 74 KG match.

Unsupported or incomplete in the generated record:

- Leibovitz's L-15 medium is represented as `1000 G_PER_L` instead of a liquid volume.
- Fetal bovine serum is represented as `100 G_PER_L` instead of 100 ml/L.
- NaCl remains at the old MediaDive normalized 13.6364 g/L value, while the curated owner stores the JCM amount as 15.0 g/L.
- The filter-sterilization step contains mojibake in the micrometer unit.
- `kg_microbe_match` incorrectly points at MediaDive 74, which is DSMZ Thermus thermophilus medium and not JCM 930.
- The source-duplicate relationship to the Togo M976 child is absent.
- Structured MediaDive and JCM references are absent from the generated record.

## Completeness

The generated record preserves the MediaDive identity, all three ingredient rows, and the presence of a filter-sterilization step, but the August 2026 merge output predates the normalized owner's September 2026 repairs.

Empty optional organism, pH, incubation, and storage fields are acceptable for this review because the inspected JCM and MediaDive records do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated YAML is stale relative to the maintained owner. | The maintained MediaDive owner contains the September 2026 `RESOLVED_MEDIADIVE_J930_LEIBOVITZ_FBS` repair, but the generated file still contains the August 2026 pre-repair units and metadata. | merge regeneration |
| Major | Two liquid components are represented with mass units. | JCM 930 and MediaDive J930 list 1 L Leibovitz's L-15 medium and 100 ml fetal bovine serum; the generated YAML stores `1000 G_PER_L` and `100 G_PER_L`. | already fixed in `data/normalized_yaml/bacterial/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml`; needs regeneration |
| Major | `kg_microbe_match` points at the wrong MediaDive record. | MediaDive 74 is Thermus thermophilus medium; this record is JCM 930 / MediaDive J930, and the maintained owner already removed the stale MediaDive 74 link. | already fixed in the maintained owner; needs regeneration |
| Minor | The filter step contains a corrupted unit string. | JCM says to filter-sterilize with a 0.22 um PES filter, while the generated MediaDive import has mojibake where the micrometer symbol should be. | already fixed in the maintained owner; needs regeneration |
| Minor | Source-duplicate and reference metadata have not propagated. | The maintained MediaDive owner has a `SOURCE_DUPLICATE` child pointing to CultureMech:010402 and structured MediaDive/JCM references; the generated YAML does not. | merge regeneration |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from the repaired normalized owners.
2. Confirm that the regenerated MediaDive J930 file carries `1.0 L` Leibovitz's L-15 medium, `100.0 ML_PER_L` fetal bovine serum, and `15.0 G_PER_L` NaCl.
3. Confirm that the regenerated filter step says `0.22 um PES filter` without mojibake.
4. Confirm that the obsolete `kg_microbe_match: mediadive.medium:74` is absent.
5. Confirm that the MediaDive J930 generated record links Togo M976 as its source-duplicate child.
6. Regenerate downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Diff the regenerated `data/merge_yaml/merged/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl__ca720e6d.yaml` against `data/normalized_yaml/bacterial/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml` to confirm that the September 2026 curation propagated.
- Re-run an ignored-inclusive exact search for `mediadive.medium:J930`, `CultureMech:010402`, and `GRMD=930` to confirm the MediaDive and Togo JCM 930 identities are linked.

## Additional Notes

The generated Togo M976 sibling has the same stale MediaDive 74 KG match and should be regenerated in the same batch.
