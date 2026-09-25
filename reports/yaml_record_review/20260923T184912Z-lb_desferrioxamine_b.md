# YAML Record Review: lb_desferrioxamine_b

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_desferrioxamine_b.yaml
- Started UTC: 2026-09-23T18:48:01Z
- Finished UTC: 2026-09-23T18:49:12Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:008564` for `lb_desferrioxamine_b` in `data/merge_yaml/merged/lb_desferrioxamine_b.yaml`.

- Source identity: TogoMedium `TOGO:M1981`, imported from original NBRC source `NBRC_M1265`.
- Original source URL: `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1265`.
- Generated lineage: `merge_fingerprint: 4e6a994ec6819c4a5a3490246b41272d5d75b59d7117ccba9afd660ebf1b2b24`, `merged_from: lb_desferrioxamine_b`.
- Maintained owner for fixes: `data/normalized_yaml/bacterial/lb_desferrioxamine_b.yaml`.
- Current generated state: stale relative to the maintained normalized record, which already contains a September 2026 NBRC M1265 source repair.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with exit 0 and no output. |
| `scripts/validate_strict.py data/merge_yaml/merged/lb_desferrioxamine_b.yaml --workers 1 --quiet` | Passed with 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lb_desferrioxamine_b.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lb_desferrioxamine_b.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

The TOGO and NBRC identities are aligned: TogoMedium M1981 imports NBRC medium 1265 as `LB + Desferrioxamine B`, and both source views list Bacto Tryptone, yeast extract, NaCl, Deferoxamine mesylate salt, distilled water, optional agar, and pH 7.0.

The generated file itself does not mis-ground Deferoxamine mesylate salt because it has no ontology term for that row. The maintained September 2026 repair grounds that salt row to `CHEBI:4356` desferrioxamine B; that is the active parent compound, but the inspected source weighs 65 mg of `Deferoxamine mesylate salt`. An exact salt term should be used if available, and otherwise the product salt should stay explicit and ungrounded.

## Evidence

NBRC medium 1265 lists 10 g Bacto Tryptone, 5 g yeast extract, 5 g NaCl, 65 mg Deferoxamine mesylate salt, 1 L distilled water, 15 g agar if needed, and pH 7.0. TogoMedium M1981 exposes the same component names, amounts, pH, NBRC accession, and source URL.

The generated merge is stale against those inspected sources and against the maintained September 2026 repair:

- It stores Deferoxamine mesylate salt as `65 G_PER_L`; the source says 65 mg/L.
- It stores distilled water as `1 G_PER_L`; the source says 1 L.
- It lacks pH 7.0.
- It lacks the source-supported parent-media link to the base LB medium.
- It has no top-level `references`, so the TOGO and NBRC URLs visible in the maintained normalized record do not propagate to this generated file.

## Completeness

The generated record is not complete enough because the supplement dose and water unit are wrong by orders of magnitude and the source pH is absent. It is otherwise a single-source record with no stock solutions, strain-specific growth claims, incubation temperature, atmosphere, or storage claims in NBRC M1265 or TogoMedium M1981.

The source makes agar optional. The generated and maintained records both mark the recipe `SOLID_AGAR`, so the future curation should decide whether to keep this as an agar-specific variant, split a broth variant, or represent the optional agar state without making a strictly solid claim.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:008564`, `TOGO:M1981`, `NBRC_M1265`, `NO=1265`, the source slug, and the merge fingerprint found the maintained normalized owner, this generated merge, normalized index rows, and a parent-media reference from `data/normalized_yaml/bacterial/lb_medium.yaml`. It did not find an alternate maintained overlay or a prior archived curation report for this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated Deferoxamine mesylate salt concentration is 1000-fold too high. | NBRC M1265 and TogoMedium M1981 list 65 mg/L; the generated YAML stores `65 G_PER_L`. | Regenerate `data/merge_yaml/merged/lb_desferrioxamine_b.yaml` from the already repaired `data/normalized_yaml/bacterial/lb_desferrioxamine_b.yaml`. |
| Major | The generated distilled-water row has the wrong unit. | Both inspected source views list 1 L distilled water; the generated YAML stores `1 G_PER_L`. | Regenerate from the repaired normalized owner. |
| Major | The generated record is stale and omits curated pH, references, and parent-media structure. | The maintained normalized owner now has `ph_value: 7.0`, source references, and a parent-media relationship to `data/normalized_yaml/bacterial/lb_medium.yaml`; the generated file predates that repair. | Regenerate from the repaired normalized owner. |
| Major | The maintained salt grounding is inexact. | The source weighs `Deferoxamine mesylate salt`; the maintained owner grounds the row to `CHEBI:4356` desferrioxamine B, the active parent rather than the exact supplied salt. | Replace the term in `data/normalized_yaml/bacterial/lb_desferrioxamine_b.yaml` with an exact salt term or leave the ingredient ungrounded. |
| Minor | Optional agar is represented as unconditional solid agar. | NBRC M1265 and TogoMedium M1981 list `Agar (if needed)`, while the generated and maintained records use `physical_state: SOLID_AGAR`. | `data/normalized_yaml/bacterial/lb_desferrioxamine_b.yaml` |

No blocker findings were found.

## Recommended Edits

1. Replace the inexact Deferoxamine mesylate salt term in `data/normalized_yaml/bacterial/lb_desferrioxamine_b.yaml` with an exact salt term, or leave that product row ungrounded.
2. Revisit `physical_state: SOLID_AGAR` and decide how to represent the source's optional agar row.
3. Regenerate `data/merge_yaml/merged/lb_desferrioxamine_b.yaml` so it receives the already curated 65 mg/L supplement, 1000 ml/L water, pH 7.0, source references, parent-media relation, ingredient groundings, and preparation text.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on `data/normalized_yaml/bacterial/lb_desferrioxamine_b.yaml`.
- Re-run the merge pipeline and verify that the generated `CultureMech:008564` record carries 65 mg/L Deferoxamine mesylate salt, volume-based distilled water, pH 7.0, source references, and the curated LB parent relationship.
- Re-run strict, schema, term, and reference validation on the regenerated `data/merge_yaml/merged/lb_desferrioxamine_b.yaml`.
- Manually recompare the regenerated file against NBRC medium 1265 and TogoMedium M1981, especially the supplement unit and optional agar row.

## Additional Notes

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
