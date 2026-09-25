# YAML Record Review: mannitol_agar_without_calcium_carbonate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mannitol_agar_without_calcium_carbonate.yaml
- Started UTC: 2026-09-23T23:13:09Z
- Finished UTC: 2026-09-23T23:13:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003089 |
| name | mannitol_agar_without_calcium_carbonate |
| original_name | MANNITOL AGAR WITHOUT CALCIUM CARBONATE |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| source term | mediadive.medium:J746, MANNITOL AGAR WITHOUT CALCIUM CARBONATE |
| generated path | data/merge_yaml/merged/mannitol_agar_without_calcium_carbonate.yaml |
| maintained owner | data/normalized_yaml/bacterial/mannitol_agar_without_calcium_carbonate.yaml |

The reviewed YAML is a derived merge artifact. Its terminal curation events report that `mannitol_agar` and `mannitol_agar_without_calcium_carbonate` were merged as duplicate recipes on fingerprint `8a2646aa8d124238fe51c54eaaeb75508aba51aaeeaff4fd49d0f321993631f8`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:003089`, `mediadive.medium:J746`, `CultureMech:002946`, `mediadive.medium:J598`, `GRMD=746`, and `GRMD=598` found the J746 owner, the J598 parent, this generated copy, the derived JSON indexes, and TOGO records that cite the same JCM pages by URL. No second YAML in those searched trees claimed the exact `CultureMech:003089` ID or `mediadive.medium:J746` source ID.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mannitol_agar_without_calcium_carbonate.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/mannitol_agar_without_calcium_carbonate.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The reviewed record is supposed to denote JCM 746, `MANNITOL AGAR WITHOUT CALCIUM CARBONATE`. JCM 746 is an override recipe that says to use JCM 598, `MANNITOL AGAR`, without `CaCO3`.

JCM 598 supports this parent formula:

| Component | Amount |
|---|---:|
| Yeast extract | 5.0 g |
| Peptone | 3.0 g |
| Mannitol | 25.0 g |
| CaCO3 | 10.0 g |
| Agar | 20.0 g |
| Distilled water | 1.0 L |

Therefore JCM 746 should inherit yeast extract, peptone, mannitol, agar, distilled water, the pH 6.8 adjustment, and a solid agar physical state from JCM 598, but it should not include calcium carbonate. The generated record instead includes `CaCO3` and then merges JCM 746 with JCM 598 as if the two source recipes were identical.

## Evidence

The JCM 746 page itself contains no ingredient table; its only composition instruction is to use Medium No. 598 without CaCO3. The maintained J746 owner records a `copy_referenced_compositions` event with `source: CultureMech:002946` and copied 5 ingredients from `mannitol_agar`; that copied the excluded CaCO3 ingredient along with the ingredients that should have been inherited.

The generated merge compounds that error:

- `CaCO3` remains present at 10 G_PER_L.
- `mannitol_agar` and `mannitol_agar_without_calcium_carbonate` are both in `merged_from`.
- The generated J746 record has `kg_microbe_match: mediadive.medium:J598`.
- The generated J746 record has a `synonyms` row for `mannitol_agar` with source ID `mediadive.medium:J598`.

The record also omits the 1.0 L distilled-water row from JCM 598, omits JCM 598's pH 6.8 adjustment, and declares `physical_state: LIQUID` despite inheriting 20 G_PER_L agar from JCM 598.

## Completeness

Missing or incomplete:

- Calcium carbonate must be removed from the J746 normalized owner before this medium can denote "without calcium carbonate".
- JCM 746 needs the inherited JCM 598 distilled-water basis.
- JCM 746 needs the inherited pH 6.8 adjustment.
- `physical_state` should be compatible with the inherited agar, not `LIQUID`.
- The duplicate merge with JCM 598 should be broken after the CaCO3 row is removed.

Complete enough:

- No stock-solution references are needed for JCM 746 or JCM 598.
- Yeast extract and peptone are undefined ingredients and do not require CHEBI grounding.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The generated record conflates two JCM media with opposite calcium-carbonate semantics. | JCM 746 explicitly says to use Medium No. 598 without CaCO3, but the generated J746 record includes 10 G_PER_L CaCO3 and was merged with `mannitol_agar`, the JCM 598 parent that contains CaCO3. | data/normalized_yaml/bacterial/mannitol_agar_without_calcium_carbonate.yaml and the referenced-composition copy logic |
| major | The resolved JCM 746 composition copied the parent without applying the source exclusion. | The April `copy_referenced_compositions` event says it copied 5 ingredients from `CultureMech:002946`; the J746 source requires all of JCM 598 except CaCO3, so only 4 non-water solutes should have been copied. | data/normalized_yaml/bacterial/mannitol_agar_without_calcium_carbonate.yaml and the referenced-composition copy logic |
| major | Inherited parent fields were not copied from JCM 598. | JCM 598 contains 1.0 L distilled water and pH 6.8; both are required by JCM 746's "Use Medium No. 598" instruction, but they are absent from the J746 generated record. | data/normalized_yaml/bacterial/mannitol_agar_without_calcium_carbonate.yaml and, for the water row, data/normalized_yaml/bacterial/mannitol_agar.yaml |
| major | The physical state is inconsistent with the inherited agar. | JCM 746 inherits 20 G_PER_L agar from JCM 598, but the record declares `physical_state: LIQUID`. | data/normalized_yaml/bacterial/mannitol_agar_without_calcium_carbonate.yaml |

## Recommended Edits

1. Remove the `CaCO3` ingredient from `data/normalized_yaml/bacterial/mannitol_agar_without_calcium_carbonate.yaml`; update the referenced-composition resolver so `without <component>` instructions subtract the named component before writing inherited formulas.
2. Carry the JCM 598 pH 6.8 adjustment and 1.0 L distilled-water basis into the JCM 746 normalized owner, and patch JCM 598 itself if the parent remains missing its water row.
3. Change JCM 746 `physical_state` from `LIQUID` to `SOLID_AGAR`.
4. Regenerate merged records and verify that JCM 746 no longer shares a merge fingerprint with JCM 598, no longer lists `mannitol_agar` as a synonym, and no longer carries `kg_microbe_match: mediadive.medium:J598`.

## Follow-up Checks

- Rerun open schema, strict, term, and reference validation on the J746 owner, the J598 parent if edited, and the regenerated J746 merge.
- Rerun merge generation and a focused merge-freshness check proving JCM 746 and JCM 598 are no longer deduplicated.
- Re-fetch JCM GRMD 746 and 598 and confirm that the regenerated J746 record contains every J598 ingredient except CaCO3 plus the inherited pH 6.8 adjustment.
- Add or run a focused regression test for the referenced-composition resolver against an instruction of the form `Use Medium No. <id> without <component>`.

## Additional Notes

None found.
