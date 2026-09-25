# YAML Record Review: lb_glucose_10_g_l_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_glucose_10_g_l_medium.yaml
- Started UTC: 2026-09-23T18:50:06Z
- Finished UTC: 2026-09-23T18:51:09Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009504` for `lb_glucose_10_g_l_medium` in `data/merge_yaml/merged/lb_glucose_10_g_l_medium.yaml`.

- Source identity: TogoMedium `TOGO:M2983`, labeled `LB + glucose (10 g/L) medium`.
- Generated lineage: `merge_fingerprint: 5e981a6bdcb4f1f294a35d2bcb0b7ac101b320f7b90db8f3434c68f7d8fb6abf`, `merged_from: lb_glucose_10_g_l_medium`.
- Maintained owner for fixes: `data/normalized_yaml/bacterial/lb_glucose_10_g_l_medium.yaml`.
- Source limitation: TogoMedium M2983 has no `src_url` in its API payload.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with "No issues found". |
| `scripts/validate_strict.py data/merge_yaml/merged/lb_glucose_10_g_l_medium.yaml --workers 1 --quiet` | Passed with 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lb_glucose_10_g_l_medium.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lb_glucose_10_g_l_medium.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

The TOGO medium identity is correct: TogoMedium M2983 is `LB + glucose (10 g/L) medium`. Its actual component list is narrow, with 10 g/L glucose plus 1 L `LB medium`; it does not resolve the LB base into Miller LB constituents.

The generated `kg_microbe_match: mediadive.medium:681` is not correct. MediaDive medium 681 is DSMZ `TGA-MEDIUM`, a tryptone, 2 g/L glucose, and 5 g/L NaCl recipe adjusted to pH 7.0. That is not the TogoMedium M2983 record, which adds 10 g/L glucose to an unresolved LB medium and records pH 5.0.

## Evidence

TogoMedium M2983 lists `glucose` at 10 g/L and `LB medium` at 1 L. Its metadata has pH 5.0, and its comment says `B. coagulans strain 36D1` was cultured in the LB plus 10 g/L glucose medium at pH 5.0, 50 C, and 200 RPM, citing an internal reference `[10]` that is not exposed as a URL in the API.

The generated YAML preserves the 10 g/L glucose value, but it loses or invents the surrounding context:

- It drops the source `LB medium` component and substitutes tryptone, yeast extract, and 10 g/L sodium chloride from an unrelated Miller LB supplier annotation.
- It omits pH 5.0.
- It omits the TogoMedium growth-condition comment for `B. coagulans strain 36D1`.
- It maps the record to DSMZ TGA medium, which has a different glucose concentration and pH.

## Completeness

The record is not complete enough because the base medium is unsupported, the source pH is missing, and the only source-provided growth context is absent. The TogoMedium payload has no primary URL, so the Bacillus coagulans claim should be treated as unverified until the exact source behind `[10]` is identified.

No source was found in TogoMedium M2983 for sterilization, stock-solution nesting, atmosphere, or storage.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:009504`, `TOGO:M2983`, `mediadive.medium:681`, the source slug, and the merge fingerprint found the maintained normalized owner, this generated merge, index rows, and the real DSMZ/KOMODO TGA medium records for MediaDive 681. It did not find an alternate maintained overlay or a prior archived curation report for this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The LB base has been expanded without source support. | TogoMedium M2983 lists an unresolved 1 L `LB medium` component; the YAML substitutes a Miller LB tryptone, yeast extract, and 10 g/L NaCl formula from `laboratorynotes.com`. | `data/normalized_yaml/bacterial/lb_glucose_10_g_l_medium.yaml` |
| Major | The source pH is missing. | TogoMedium M2983 records pH 5.0; the YAML has no pH field. | `data/normalized_yaml/bacterial/lb_glucose_10_g_l_medium.yaml` |
| Major | `kg_microbe_match: mediadive.medium:681` points to the wrong medium. | MediaDive 681 is DSMZ `TGA-MEDIUM`, with 2 g/L glucose and pH 7.0, not TogoMedium `LB + glucose (10 g/L) medium`. | `data/normalized_yaml/bacterial/lb_glucose_10_g_l_medium.yaml` |
| Major | Growth context is present only in the TOGO comment and lacks the primary source needed for verification. | TogoMedium M2983 mentions `B. coagulans strain 36D1`, pH 5.0, 50 C, and 200 RPM, but has no `src_url`; the YAML has no target-organism evidence or discussion of the missing primary reference. | `data/normalized_yaml/bacterial/lb_glucose_10_g_l_medium.yaml` |
| Minor | Material source URLs are present only in free text. | The generated record names TogoMedium M2983 in `notes`, but it has no `references`, so the reference validator had 0 URL checks. | `data/normalized_yaml/bacterial/lb_glucose_10_g_l_medium.yaml` |

No blocker findings were found.

## Recommended Edits

1. Restore the unresolved 1 L `LB medium` component or replace it only with a primary-source-supported base LB formulation.
2. Remove the unsupported Miller LB constituent expansion and `laboratorynotes.com` supplier metadata.
3. Add pH 5.0 from TogoMedium M2983.
4. Remove or recompute `kg_microbe_match: mediadive.medium:681`.
5. Add a TogoMedium M2983 `references` entry and add a discussion or quality flag stating that the Bacillus coagulans growth comment lacks an exposed primary source URL.
6. Regenerate `data/merge_yaml/merged/lb_glucose_10_g_l_medium.yaml` after the normalized YAML is curated.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on `data/normalized_yaml/bacterial/lb_glucose_10_g_l_medium.yaml`.
- Re-run the merge pipeline and verify that the generated `CultureMech:009504` record carries 10 g/L glucose, the source-supported LB base, pH 5.0, no DSMZ medium 681 match, and a TogoMedium M2983 reference.
- Re-run strict, schema, term, and reference validation on the regenerated `data/merge_yaml/merged/lb_glucose_10_g_l_medium.yaml`.
- Search for the exact TogoMedium M2983 growth sentence to identify the primary Bacillus coagulans study before adding target-organism growth evidence.

## Additional Notes

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
