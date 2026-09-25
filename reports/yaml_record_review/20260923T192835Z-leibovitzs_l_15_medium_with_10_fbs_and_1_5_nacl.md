# YAML Record Review: Leibovitz's L-15 Medium With 10% FBS And 1.5% NaCl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml
- Started UTC: 2026-09-23T19:26:49Z
- Finished UTC: 2026-09-23T19:28:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:010402 |
| Name | leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl |
| Original name | Leibovitz's L-15 Medium With 10% FBS And 1.5% NaCl |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | TOGO:M976 |
| Source provenance | Togo M976 imported from JCM_M930 |
| Generated file | data/merge_yaml/merged/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M976_Leibovitz_s_L-15_Medium_With_10_FBS_And_1.5_NaCl.yaml |
| Merge fingerprint | 2abf9b7da959e0c7c0d43cf8e00fd54a8334bb285f2bcaedfc8f4c5c0cc52258 |

The reviewed target is a generated one-source merge from Togo M976. The maintained owner already contains September 2026 curation for this recipe, so the primary fix is to regenerate `data/merge_yaml/merged/` and downstream products from the maintained normalized YAML.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M976, JCM `GRMD=930`, and MediaDive J930 all identify the same Leibovitz L-15 medium with 10% FBS and 1.5% NaCl recipe. The separate MediaDive normalized record, `data/normalized_yaml/bacterial/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml`, has already been marked as the `SOURCE_DUPLICATE` parent of this Togo owner, and both maintained owners were repaired by `repair_togo_m976_leibovitz_score15.py`.

The generated record is stale relative to that maintained owner: it lacks the corrected volume units, filter-sterilization step, source-duplicate relationship, structured references, MediaDive product groundings, and removal of the obsolete `kg_microbe_match: mediadive.medium:74` Thermus thermophilus link. An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the Togo owner, the MediaDive J930 owner, the matching generated MediaDive sibling, source indexes, validation archives, and multiple exact legacy `kg_microbe_match: mediadive.medium:74` rows.

## Evidence

Supported in the inspected JCM, Togo, and MediaDive sources:

- The JCM 930, Togo M976, and MediaDive J930 identities are supported.
- The recipe contains 1 L Leibovitz's L-15 medium, 100 ml fetal bovine serum, and 15 g NaCl.
- The medium should be filter-sterilized with a 0.22 um PES filter.
- The maintained Togo owner already stores the corrected `L`, `ML_PER_L`, and `G_PER_L` units, the filter step, structured JCM/Togo references, a `SOURCE_DUPLICATE` parent link to the MediaDive J930 owner, and no MediaDive 74 KG match.

Unsupported or incomplete in the generated record:

- Leibovitz's L-15 medium is represented as `1 G_PER_L` instead of a liquid volume.
- Fetal bovine serum is represented as `100 G_PER_L` instead of 100 ml/L.
- The source filter-sterilization instruction is absent.
- `kg_microbe_match` incorrectly points at MediaDive 74, which is DSMZ Thermus thermophilus medium and not JCM 930.
- The source-duplicate relationship to the MediaDive J930 parent is absent.
- Structured Togo and JCM references are absent from the generated record.

## Completeness

The generated record preserves the Togo identity and all three source ingredients, but the August 2026 merge output is missing the September 2026 repair that corrected units, sterilization, source-duplicate links, and references in the maintained normalized owner.

Empty optional organism, pH, incubation, and storage fields are acceptable for this review because the inspected JCM, Togo, and MediaDive J930 records do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated YAML is stale relative to the maintained owner. | The maintained Togo owner contains the September 2026 `RESOLVED_TOGO_M976_LEIBOVITZ_FBS` repair, but the generated file still contains the August 2026 pre-repair quantities and metadata. | merge regeneration |
| Major | Two liquid components are represented with mass units. | JCM 930, Togo M976, and MediaDive J930 list 1 L Leibovitz's L-15 medium and 100 ml fetal bovine serum; the generated YAML stores `1 G_PER_L` and `100 G_PER_L`. | already fixed in `data/normalized_yaml/bacterial/TOGO_M976_Leibovitz_s_L-15_Medium_With_10_FBS_And_1.5_NaCl.yaml`; needs regeneration |
| Major | The source filter-sterilization step is absent. | JCM 930 and Togo M976 say to filter-sterilize with a 0.22 um PES filter; the maintained owner has that step, but the generated YAML has no `preparation_steps`. | already fixed in the maintained owner; needs regeneration |
| Major | `kg_microbe_match` points at the wrong MediaDive record. | MediaDive 74 is Thermus thermophilus medium; this record is JCM 930 / MediaDive J930, and the maintained owner already removed the stale MediaDive 74 link. | already fixed in the maintained owner; needs regeneration |
| Minor | Source-duplicate and reference metadata have not propagated. | The maintained Togo owner has a `SOURCE_DUPLICATE` parent pointing to CultureMech:003278 and structured Togo/JCM references; the generated YAML does not. | merge regeneration |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from the repaired normalized owners.
2. Confirm that the regenerated M976 file carries `1.0 L` Leibovitz's L-15 medium, `100.0 ML_PER_L` fetal bovine serum, and `15.0 G_PER_L` NaCl.
3. Confirm that the regenerated M976 file carries the 0.22 um PES filter step and `sterilization.method: FILTER`.
4. Confirm that the obsolete `kg_microbe_match: mediadive.medium:74` is absent from both generated Leibovitz/FBS records.
5. Confirm that the Togo M976 and MediaDive J930 records remain linked as source duplicates instead of independent unrelated recipes.
6. Regenerate downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Diff the regenerated `data/merge_yaml/merged/leibovitzs_l_15_medium_with_10_fbs_and_1_5_nacl.yaml` against `data/normalized_yaml/bacterial/TOGO_M976_Leibovitz_s_L-15_Medium_With_10_FBS_And_1.5_NaCl.yaml` to confirm that the September 2026 curation propagated.
- Re-run an ignored-inclusive exact search for `TOGO:M976`, `GRMD=930`, and `mediadive.medium:J930` to confirm the Togo and MediaDive JCM 930 identities are linked and no longer emit stale generated records.

## Additional Notes

The inspected MediaDive 74 REST record is DSMZ Thermus thermophilus medium; it is unrelated to this Leibovitz/FBS recipe and confirms that the generated `kg_microbe_match` value is stale noise rather than a valid alias.
