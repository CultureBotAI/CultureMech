# YAML Record Review: lb_luria_bertani_agar_with_10_mm_glucose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose.yaml
- Started UTC: 2026-09-23T18:54:19Z
- Finished UTC: 2026-09-23T18:55:35Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:010235` for `lb_luria_bertani_agar_with_10_mm_glucose` in `data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose.yaml`.

- Source identity: TogoMedium `TOGO:M822`, imported from JCM Medium 790.
- Original source URL: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=790`.
- Generated lineage: `merge_fingerprint: d77a19b59fd7357179cfb82773f3eec9370f08951df90837ea69358643606e95`, `merged_from: TOGO_M822_LB_Luria-Bertani_Agar_With_10_mM_Glucose`.
- Maintained owner for fixes: `data/normalized_yaml/bacterial/TOGO_M822_LB_Luria-Bertani_Agar_With_10_mM_Glucose.yaml`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with exit 0 and no output. |
| `scripts/validate_strict.py data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose.yaml --workers 1 --quiet` | Passed with 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

The record identity is correct. TogoMedium M822 imports JCM Medium 790, `LB (Luria-Bertani) Agar With 10 mM Glucose`, and its original URL points to the same JCM `GRMD=790` table inspected during review.

The checked small-molecule groundings are appropriate for the rows they annotate: glucose, sodium chloride, water, and agar. Yeast extract and tryptone are source-qualified complex products and are not grounded to misleading ChEBI small molecules.

## Evidence

JCM `GRMD=790` lists 10 g tryptone, 5 g yeast extract, 10 g NaCl, 1.8 g glucose, 15 g agar, 1 L distilled water, and the instruction `Adjust pH to 7.0.` The page also carries JCM's default autoclaving instruction of 121 C for 15 min. TogoMedium M822 exposes the same six components, pH instruction, JCM accession, and source URL.

The generated YAML preserves the 10 mM glucose conversion as 1.8 g/L and matches all non-water masses. It misses three source-supported claims:

- Distilled water is represented as `1 G_PER_L` instead of 1 L.
- pH 7.0 is not represented.
- The JCM default autoclave step is absent.

## Completeness

The record is not complete enough because the solvent unit is wrong and following the YAML would omit pH adjustment and sterilization. It also has no top-level `references`; TOGO M822 and JCM GRMD 790 are only in `notes`, so the reference validator had no URLs to check.

No consequential source was found for incubation temperature, atmosphere, storage, stock-solution nesting, or strain-specific growth. JCM Medium 790 is a base agar formulation rather than an organism growth experiment.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:010235`, `TOGO:M822`, `GRMD=790`, `JCM_M790`, the source slug, and the merge fingerprint found the maintained normalized owner, this generated merge, a sibling direct MediaDive/JCM generated import for the same JCM URL, index rows, and archived validation rows for this target. It did not find a prior archived curation report for this generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water has the wrong unit. | JCM GRMD 790 and TogoMedium M822 list 1 L distilled water; the YAML stores `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M822_LB_Luria-Bertani_Agar_With_10_mM_Glucose.yaml` |
| Major | pH and sterilization are missing. | Both source views state pH 7.0, and JCM supplies the default 121 C for 15 min autoclave condition; neither is structured in the YAML. | `data/normalized_yaml/bacterial/TOGO_M822_LB_Luria-Bertani_Agar_With_10_mM_Glucose.yaml` |
| Minor | Material source URLs are present only in free text. | The record names TogoMedium M822 and the JCM 790 URL in `notes`, but it has no `references`, so the reference validator had 0 URL checks. | `data/normalized_yaml/bacterial/TOGO_M822_LB_Luria-Bertani_Agar_With_10_mM_Glucose.yaml` |

No blocker findings were found.

## Recommended Edits

1. Change distilled water to a volume-preserving 1 L amount.
2. Add pH 7.0.
3. Add the JCM default autoclave step at 121 C for 15 min.
4. Add `references` for TogoMedium M822 and JCM `GRMD=790`.
5. Regenerate `data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose.yaml` after the normalized YAML is curated.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on `data/normalized_yaml/bacterial/TOGO_M822_LB_Luria-Bertani_Agar_With_10_mM_Glucose.yaml`.
- Re-run the merge pipeline and verify that the generated `CultureMech:010235` record carries 1 L water, pH 7.0, JCM autoclaving, and source references while retaining the 1.8 g/L glucose conversion.
- Re-run strict, schema, term, and reference validation on the regenerated `data/merge_yaml/merged/lb_luria_bertani_agar_with_10_mm_glucose.yaml`.
- Manually compare the regenerated file against JCM GRMD 790 and TogoMedium M822.

## Additional Notes

The direct MediaDive/JCM import of the same GRMD 790 source should be reviewed as its own generated record. It was outside this exact TOGO M822 target.

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
