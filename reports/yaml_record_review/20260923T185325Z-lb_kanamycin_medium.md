# YAML Record Review: lb_kanamycin_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_kanamycin_medium.yaml
- Started UTC: 2026-09-23T18:51:56Z
- Finished UTC: 2026-09-23T18:53:25Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:008515` for `lb_kanamycin_medium` in `data/merge_yaml/merged/lb_kanamycin_medium.yaml`.

- Primary source identity: TogoMedium `TOGO:M1937`, imported from NBRC Medium 1204, `LB + Kanamycin medium`.
- Old merged sources: `lb_50_ug_ml_kanamycin_medium` from TogoMedium `M2099` and `lb_ampicillin_medium` from TogoMedium `M1685`.
- Generated lineage: `merge_fingerprint: e971202adc752bdedf4447173841d5e75a9a588ff7de9fcfd3e67e41a3298c26`.
- Maintained owners for fixes: `data/normalized_yaml/bacterial/lb_kanamycin_medium.yaml`, `data/normalized_yaml/bacterial/lb_50_ug_ml_kanamycin_medium.yaml`, `data/normalized_yaml/bacterial/lb_ampicillin_medium.yaml`, and the merge grouping if regeneration still collapses those records.
- Current generated state: stale relative to the three maintained normalized records, which already contain September 2026 antibiotic-stock repairs.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with "No issues found". |
| `scripts/validate_strict.py data/merge_yaml/merged/lb_kanamycin_medium.yaml --workers 1 --quiet` | Passed with 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lb_kanamycin_medium.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lb_kanamycin_medium.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

TogoMedium M1937 and NBRC Medium 1204 both identify the canonical source as `LB + Kanamycin medium`, with 1 ml/L `Kanamycin sulfate solution (20 mg/ml)` added to an LB base. The generated `media_term` points at the correct TOGO accession, but the generated merge now has stale synonym and variant-child claims: TogoMedium M2099 is a 50 mg/ml kanamycin-stock record, and TogoMedium M1685 is a 50 mg/ml sodium-ampicillin-stock record.

The repaired normalized owners correctly distinguish those three antibiotic variants. The generated merge still reflects their pre-repair state, where each antibiotic stock had been migrated into an empty `Unknown solution` and the merge grouped them as source duplicates.

## Evidence

NBRC Medium 1204 lists 10 g `Bacto Tyrptone (Difco)`, 5 g yeast extract, 5 g NaCl, 1 ml `Kanamycin sulfate solution (20 mg/ml)*`, 1 L distilled water, 15 g agar if needed, and pH 7.0. The footnote says to sterilize the starred kanamycin solution separately by filtration. TogoMedium M1937 exposes the same component list, pH, source URL, and filtration footnote. TogoMedium M2099 differs by using `Kanamycin sulfate solution (50 mg/ml)*`; TogoMedium M1685 differs by using `Sodium ampicillin solution (50 mg/ml)*`.

The generated YAML is stale against all three repaired owners:

- It stores distilled water as `1 G_PER_L`; all three inspected TOGO/NBRC source families say 1 L.
- It stores `Kanamycin sulfate solution (20 mg/ml)*` as `1 G_PER_L` in an empty `Unknown solution`, rather than a 1 ml/L solution with 20 mg/ml kanamycin sulfate composition.
- It omits pH 7.0 and the kanamycin stock filtration step.
- It still declares M2099 and M1685 as `SOURCE_DUPLICATE` children of M1937 even though the maintained owners now show distinct 20 mg/ml kanamycin, 50 mg/ml kanamycin, and 50 mg/ml sodium ampicillin variants.
- It has no top-level `references`, so the repaired TOGO and NBRC URLs do not propagate to this generated file.

## Completeness

The generated record is not complete enough because the antibiotic stock is not represented as a stock, the pH and filtration details are missing, and the generated merge boundary is wrong. The maintained normalized records for all three old sources now carry parent LB relationships, variant modifications, nested antibiotic stock compositions, pH values, and NBRC/TOGO references.

The source makes agar optional. The generated and maintained records mark these recipes `SOLID_AGAR`, so future curation should decide whether to keep them as agar-specific variants, split broth variants, or represent the optional agar state without making a strict solid claim.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:008515`, `TOGO:M1937`, `TOGO:M2099`, `TOGO:M1685`, the source slugs, `NBRC_M1204`, and the merge fingerprint found the three maintained normalized owners, this generated merge, normalized index rows, and parent-media references from `data/normalized_yaml/bacterial/lb_medium.yaml`. It did not find a prior archived curation report for this generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge still conflates distinct antibiotic variants. | M1937 uses 1 ml/L 20 mg/ml kanamycin sulfate stock; M2099 uses 1 ml/L 50 mg/ml kanamycin sulfate stock; M1685 uses 1 ml/L 50 mg/ml sodium ampicillin stock. The generated file marks the latter two as source duplicates of M1937. | The three normalized source records have already been repaired; fix the merge grouping if regeneration still collapses them. |
| Major | The generated kanamycin stock is an empty unknown solution with the wrong unit. | NBRC M1204 and TogoMedium M1937 list 1 ml/L of 20 mg/ml kanamycin sulfate stock, sterilized separately by filtration; the generated YAML has `name: Unknown solution`, `composition: []`, and `1 G_PER_L`. | Regenerate from `data/normalized_yaml/bacterial/lb_kanamycin_medium.yaml`. |
| Major | The generated water row has the wrong unit. | All three source families list 1 L distilled water; the generated YAML stores `1 G_PER_L`. | Regenerate from the repaired normalized owners. |
| Major | The generated record is stale and omits pH, filtration, variant, and reference structure. | The maintained M1937 owner now has pH 7.0, a filter-sterilized 20 mg/ml kanamycin sulfate stock composition, an LB parent relationship, variant modifications, and NBRC/TOGO references. | Regenerate from the repaired normalized owners. |
| Minor | Optional agar is represented as unconditional solid agar. | NBRC M1204, M1415, and M890 list `Agar (if needed)`, while the generated and maintained records use `physical_state: SOLID_AGAR`. | Revisit the physical-state policy in all three normalized antibiotic-variant owners. |

No blocker findings were found.

## Recommended Edits

1. Regenerate the merge products from the already repaired normalized antibiotic records.
2. If `lb_kanamycin_medium`, `lb_50_ug_ml_kanamycin_medium`, and `lb_ampicillin_medium` still collapse after regeneration, update the merge grouping rule so antibiotic stock identity and concentration are part of the fingerprint.
3. Revisit `physical_state: SOLID_AGAR` on the three normalized owners and decide how to represent the optional source agar.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on `data/normalized_yaml/bacterial/lb_kanamycin_medium.yaml`, `data/normalized_yaml/bacterial/lb_50_ug_ml_kanamycin_medium.yaml`, and `data/normalized_yaml/bacterial/lb_ampicillin_medium.yaml`.
- Re-run the merge pipeline and verify that M1937, M2099, and M1685 are no longer source duplicates unless the regenerated ingredient signatures preserve the antibiotic differences.
- Re-run strict, schema, term, and reference validation on the regenerated generated records.
- Manually compare the regenerated M1937 record against NBRC Medium 1204 and TogoMedium M1937, especially the 20 mg/ml stock strength, 1 ml/L dose, pH 7.0, and filtration footnote.

## Additional Notes

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
