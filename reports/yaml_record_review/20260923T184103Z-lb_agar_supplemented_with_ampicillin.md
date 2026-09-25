# YAML Record Review: lb_agar_supplemented_with_ampicillin

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_agar_supplemented_with_ampicillin.yaml
- Started UTC: 2026-09-23T18:39:51Z
- Finished UTC: 2026-09-23T18:41:03Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009088` for `lb_agar_supplemented_with_ampicillin` in `data/merge_yaml/merged/lb_agar_supplemented_with_ampicillin.yaml`.

- Source identity: TogoMedium `TOGO:M2518`, labeled `LB agar (supplemented with ampicillin)`.
- Generated lineage: `merge_fingerprint: 0937fbc4a265aedcb8d23e2ea8c6acbd12ec62bfe7eb39b5be79ab6df89ae355`, `merged_from: lb_agar_supplemented_with_ampicillin`.
- Maintained owner for fixes: `data/normalized_yaml/bacterial/lb_agar_supplemented_with_ampicillin.yaml`.
- Source limitation: TogoMedium M2518 has no `src_url` in its API payload.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with exit 0 and no output. |
| `scripts/validate_strict.py data/merge_yaml/merged/lb_agar_supplemented_with_ampicillin.yaml --workers 1 --quiet` | Passed with 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lb_agar_supplemented_with_ampicillin.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lb_agar_supplemented_with_ampicillin.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

The TOGO accession is aligned with the record label: TogoMedium API record `M2518` is `LB agar (supplemented with ampicillin)`. The generated `media_term` points at the correct TOGO CURIE and the ampicillin ChEBI grounding is appropriate for the supplement named by TOGO.

The record is over-grounded beyond that source identity. M2518 contains an `ampicillin` component and an unresolved `LB agar` component. It does not identify the LB agar as Miller LB, does not give tryptone/yeast extract/sodium chloride amounts, and gives no primary source URL. The three imported LB Miller constituents and their `laboratorynotes.com` supplier metadata are therefore unsupported by the inspected TogoMedium source.

## Evidence

TogoMedium M2518 lists two components: `ampicillin` at 150 `ug/ml` and `LB agar` without a concentration. Its comment says cultures of `X. nematophila ATCC 19061` and `X. bovienii SS-2004` were grown on LB agar supplemented with ampicillin at 150 ug/ml, then scraped into 10 ml LB broth and subcultured into 500 ml LB for 18.5 hours at 30 C.

The generated YAML fails to preserve that narrow evidence:

- It converts ampicillin to `150 G_PER_L`; 150 ug/ml is 0.15 g/L, so the recorded mass concentration is 1000-fold too high.
- It drops the source `LB agar` component and replaces it with a partial LB Miller expansion of tryptone, yeast extract, and sodium chloride.
- It omits both agar and water, even though the medium label and physical state are agar.
- It does not carry the TogoMedium comment into growth evidence for the two named Xenorhabdus strains, and TogoMedium does not provide a primary source URL that would let a curator verify the comment.

## Completeness

The record is not complete enough because the central supplement has the wrong unit, the unresolved `LB agar` base medium is replaced with unsupported LB Miller constituents, and the source's growth context is lost. The `schema-defaulter-v1.0` history event states that a default concentration was added for `LB agar`; that defaulted source component is no longer present in the merged ingredient list.

No pH, incubation atmosphere, agar concentration, or sterilization procedure was available from the inspected TogoMedium M2518 payload.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:009088`, `TOGO:M2518`, `lb_agar_supplemented_with_ampicillin`, and the merge fingerprint found the maintained normalized owner, this generated merge, and normalized index rows. It did not find an alternate maintained overlay or a prior archived curation report for this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Ampicillin has the wrong concentration unit and magnitude. | TogoMedium M2518 records 150 ug/ml ampicillin; the YAML stores `150 G_PER_L` instead of 0.15 g/L or an equivalent 150 ug/ml representation. | `data/normalized_yaml/bacterial/lb_agar_supplemented_with_ampicillin.yaml` |
| Major | The LB agar base is unsupported and incomplete. | TogoMedium M2518 records an unresolved `LB agar` component with no formula, while the YAML substitutes LB Miller tryptone, yeast extract, and sodium chloride, omitting agar and water. | `data/normalized_yaml/bacterial/lb_agar_supplemented_with_ampicillin.yaml` |
| Major | Growth context is present only in the TOGO comment and lacks the primary source needed for verification. | TogoMedium M2518 names two Xenorhabdus strains and a multi-step LB growth workflow, but it provides no `src_url`; the YAML has no references or target-organism evidence. | `data/normalized_yaml/bacterial/lb_agar_supplemented_with_ampicillin.yaml` |
| Minor | Material source URLs are present only in free text. | The generated record names TogoMedium M2518 in `notes`, but it has no `references`, so the reference validator had 0 URL checks. | `data/normalized_yaml/bacterial/lb_agar_supplemented_with_ampicillin.yaml` |

No blocker findings were found.

## Recommended Edits

1. Correct ampicillin from `150 G_PER_L` to a unit/value preserving the source 150 ug/ml.
2. Restore `LB agar` as an unresolved base-medium component or replace it only with a primary-source-supported formulation.
3. Remove the unsupported LB Miller constituent expansion and `laboratorynotes.com` supplier metadata unless a curated primary source proves that M2518 used Miller LB.
4. Add a discussion or quality flag that TogoMedium M2518 has no original source URL, so the Xenorhabdus growth comment cannot yet be primary-verified.
5. Add a TogoMedium M2518 `references` entry and regenerate `data/merge_yaml/merged/lb_agar_supplemented_with_ampicillin.yaml`.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on `data/normalized_yaml/bacterial/lb_agar_supplemented_with_ampicillin.yaml`.
- Re-run the merge pipeline and verify that the generated `CultureMech:009088` record carries 150 ug/ml ampicillin, a source-supported LB agar base, no unsupported LB Miller expansion, and a TogoMedium M2518 reference.
- Re-run strict, schema, term, and reference validation on the regenerated `data/merge_yaml/merged/lb_agar_supplemented_with_ampicillin.yaml`.
- Search for the exact TogoMedium M2518 growth sentence to identify the primary Xenorhabdus study before adding target-organism growth evidence.

## Additional Notes

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
