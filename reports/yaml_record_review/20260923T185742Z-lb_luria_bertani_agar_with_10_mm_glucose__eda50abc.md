# YAML Record Review: lb_luria_bertani_agar_with_10_mm_glucose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose__eda50abc.yaml
- Started UTC: 2026-09-23T18:56:55Z
- Finished UTC: 2026-09-23T18:57:42Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:003134` for `lb_luria_bertani_agar_with_10_mm_glucose` in `data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose__eda50abc.yaml`.

- Source identity: MediaDive/JCM `mediadive.medium:J790`, labeled `LB (LURIA-BERTANI) AGAR WITH 10 mM GLUCOSE`.
- JCM source URL: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=790`.
- Generated lineage: `merge_fingerprint: eda50abce3ff5542d59c17751b7d0f6213784775f0461eed632ead380c8a040f`, `merged_from: lb_luria_bertani_agar_with_10_mm_glucose`.
- Maintained owner for fixes: `data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_10_mm_glucose.yaml`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with "No issues found". |
| `scripts/validate_strict.py data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose__eda50abc.yaml --workers 1 --quiet` | Passed with 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose__eda50abc.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose__eda50abc.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

The record identity is correct. MediaDive J790 imports JCM Medium 790 as `LB (LURIA-BERTANI) AGAR WITH 10 mM GLUCOSE` and links to the same JCM `GRMD=790` table inspected during review.

The checked small-molecule groundings are appropriate for sodium chloride, glucose, and agar. Tryptone and yeast extract are complex BD-Difco products and are not incorrectly grounded.

## Evidence

JCM `GRMD=790` lists 10 g Tryptone, 5 g Yeast extract, 10 g NaCl, 1.8 g Glucose, 15 g Agar, and 1 L Distilled water, followed by pH adjustment to 7.0. The page also carries JCM's default autoclaving instruction of 121 C for 15 min. MediaDive REST J790 records the same components as 10, 5, 10, 1.8, 15 g/L plus 1000 ml water in a one-liter main solution, and it preserves the pH-adjustment step.

The generated YAML preserves the pH 7.0 adjustment, the solid component amounts, and the 1.8 g/L glucose conversion. It omits two source-supported claims: the 1 L distilled-water row and the JCM default autoclave instruction.

## Completeness

The record is not complete enough because it lacks the solvent component and sterilization. It also has no top-level `references`; the JCM URL is only present in `notes`, so the reference validator had no URLs to check.

No consequential source was found for incubation temperature, atmosphere, storage, stock-solution nesting, or strain-specific growth. JCM Medium 790 is a base agar formulation rather than an organism growth experiment.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:003134`, `mediadive.medium:J790`, `GRMD=790`, the source slug, and the merge fingerprint found the maintained normalized owner, this generated merge, archived validation rows, and the sibling TOGO M822 import of the same JCM URL. It did not find a prior archived curation report for this generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The distilled-water component is missing. | JCM GRMD 790 and MediaDive J790 list 1 L or 1000 ml distilled water; the YAML has no water ingredient. | `data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_10_mm_glucose.yaml` |
| Major | Sterilization is missing. | JCM states the default autoclave condition of 121 C for 15 min for media unless otherwise stated; the YAML only records pH adjustment. | `data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_10_mm_glucose.yaml` |
| Minor | Material source URLs are present only in free text. | The record names the JCM URL in `notes`, but it has no `references`, so the reference validator had 0 URL checks. | `data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_10_mm_glucose.yaml` |

No blocker findings were found.

## Recommended Edits

1. Add the source 1 L distilled-water row.
2. Add the JCM default autoclave step at 121 C for 15 min while preserving the existing pH adjustment.
3. Add `references` for the MediaDive J790 REST endpoint and JCM `GRMD=790`.
4. Regenerate `data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose__eda50abc.yaml` after the normalized YAML is curated.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on `data/normalized_yaml/bacterial/lb_luria_bertani_agar_with_10_mm_glucose.yaml`.
- Re-run the merge pipeline and verify that the generated `CultureMech:003134` record carries 1 L distilled water, JCM autoclaving, and source references.
- Re-run strict, schema, term, and reference validation on the regenerated `data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose__eda50abc.yaml`.
- Manually compare the regenerated file against MediaDive J790 and JCM GRMD 790.

## Additional Notes

The TOGO M822 import of the same JCM GRMD 790 recipe should be curated separately; it uses a distinct CultureMech ID and maintained owner.

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
