# YAML Record Review: lb_agar_with_mnso_sub_4_sub

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_agar_with_mnso_sub_4_sub.yaml
- Started UTC: 2026-09-23T18:41:50Z
- Finished UTC: 2026-09-23T18:42:57Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002225` for `lb_agar_with_mnso_sub_4_sub` in `data/merge_yaml/merged/lb_agar_with_mnso_sub_4_sub.yaml`.

- Source identity: MediaDive/JCM `mediadive.medium:J1040`, labeled `LB AGAR WITH MnSO<sub>4</sub>`.
- JCM source URL: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1040`.
- Generated lineage: `merge_fingerprint: b4daf4c5b70cc3bf760c76f8bf034e2ac46ac6ab01e1590f129be817996aa121`, `merged_from: lb_agar_with_mnso_sub_4_sub`.
- Maintained owner for fixes: `data/normalized_yaml/bacterial/lb_agar_with_mnso_sub_4_sub.yaml`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with "No issues found". |
| `scripts/validate_strict.py data/merge_yaml/merged/lb_agar_with_mnso_sub_4_sub.yaml --workers 1 --quiet` | Passed with 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lb_agar_with_mnso_sub_4_sub.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lb_agar_with_mnso_sub_4_sub.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

The main source identity is correct: MediaDive `J1040` and JCM `GRMD=1040` both identify JCM Medium 1040 as `LB AGAR WITH MnSO<sub>4</sub>`, and the ingredient masses in the YAML match the non-water component quantities in that source.

Two groundings are not sound:

- `MnSO4 x n H2O` denotes an unspecified manganese sulfate hydrate in JCM. The YAML grounds it to `CHEBI:86360` manganese(II) sulfate, which drops the variable hydration state and is not exact evidence for the weighed material.
- `kg_microbe_match: mediadive.medium:101` points at DSMZ `NUTRIENT AGAR or BROTH WITH NaCl`, a peptone/meat-extract recipe with 30 g/L NaCl, not this JCM LB agar with 10 g/L NaCl and 10 mg/L variable-hydrate manganese sulfate.

## Evidence

JCM `GRMD=1040` lists 10 g Tryptone, 5 g Yeast extract, 10 g NaCl, 10 mg `MnSO4 x n H2O`, 15 g Agar, and 1 L Distilled water, followed by `Adjust pH to 7.0.` MediaDive REST `J1040` records the same one-liter main solution and pH-adjustment step. The JCM page also carries the default instruction to autoclave media at 121 C for 15 min unless otherwise stated.

The generated YAML preserves pH 7.0 and most non-water masses, including 0.01 g/L for the 10 mg/L manganese sulfate row. It omits two source-supported procedural/formulation claims: the 1 L distilled-water row and the JCM default autoclave instruction.

## Completeness

The record is not complete enough because it lacks the distilled-water component and sterilization. It also has no top-level `references`; both source URLs are only implicit in `media_term` and `notes`, so the reference validator had no URLs to check.

No consequential source was found for incubation temperature, atmosphere, storage, stock-solution nesting, or strain-specific growth. JCM J1040 and MediaDive J1040 do not state those details.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:002225`, `mediadive.medium:J1040`, `GRMD=1040`, `LB AGAR WITH MnSO`, the source slug, and the merge fingerprint found the maintained normalized owner, this generated merge, index rows, and archived validation rows. It also found a separate `html_lb_agar_with_mnso_sub_4_sub_html` Togo import for the same JCM URL; that sibling is not part of this merge fingerprint.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The distilled-water component is missing. | JCM GRMD 1040 and MediaDive J1040 list 1 L or 1000 ml distilled water in the main recipe; the YAML lists only tryptone, yeast extract, NaCl, `MnSO4 x n H2O`, and agar. | `data/normalized_yaml/bacterial/lb_agar_with_mnso_sub_4_sub.yaml` |
| Major | Sterilization is missing. | JCM states its default autoclaving condition of 121 C for 15 min for this medium class unless otherwise stated; the YAML only records pH adjustment. | `data/normalized_yaml/bacterial/lb_agar_with_mnso_sub_4_sub.yaml` |
| Major | The manganese sulfate hydrate is over-grounded. | JCM and MediaDive specify `MnSO4 x n H2O`; `CHEBI:86360` manganese(II) sulfate does not preserve the unspecified hydration state. | `data/normalized_yaml/bacterial/lb_agar_with_mnso_sub_4_sub.yaml` |
| Major | `kg_microbe_match: mediadive.medium:101` points to the wrong medium. | MediaDive medium 101 is DSMZ `NUTRIENT AGAR or BROTH WITH NaCl`, not JCM Medium 1040. | `data/normalized_yaml/bacterial/lb_agar_with_mnso_sub_4_sub.yaml` |
| Minor | Material source URLs are present only in free text. | The record names the JCM URL in `notes`, but it has no `references`, so the reference validator had 0 URL checks. | `data/normalized_yaml/bacterial/lb_agar_with_mnso_sub_4_sub.yaml` |

No blocker findings were found.

## Recommended Edits

1. Add the source 1 L distilled-water row.
2. Add the JCM default autoclave instruction at 121 C for 15 min while preserving the existing pH adjustment.
3. Remove the exact ChEBI grounding from `MnSO4 x n H2O` unless a variable-hydrate or otherwise exact term is available.
4. Remove or recompute `kg_microbe_match: mediadive.medium:101`.
5. Add `references` for the MediaDive J1040 REST endpoint and JCM `GRMD=1040`.
6. Regenerate `data/merge_yaml/merged/lb_agar_with_mnso_sub_4_sub.yaml` after the normalized YAML is curated.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on `data/normalized_yaml/bacterial/lb_agar_with_mnso_sub_4_sub.yaml`.
- Re-run the merge pipeline and verify that the generated `CultureMech:002225` record includes distilled water, source references, JCM autoclaving, no false medium 101 match, and no inexact ChEBI grounding for the variable manganese sulfate hydrate.
- Re-run strict, schema, term, and reference validation on the regenerated `data/merge_yaml/merged/lb_agar_with_mnso_sub_4_sub.yaml`.
- Compare the regenerated record against both the MediaDive J1040 REST payload and the JCM GRMD 1040 table.

## Additional Notes

The separate `html_lb_agar_with_mnso_sub_4_sub_html` Togo import should be reviewed on its own. It appears to represent the same JCM recipe through TogoMedium and may need duplicate cleanup, but it was outside this exact generated target.

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
