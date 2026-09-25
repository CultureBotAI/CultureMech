# YAML Record Review: lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml
- Started UTC: 2026-09-23T18:33:08Z
- Finished UTC: 2026-09-23T18:34:45Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:008590` for `lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids` in `data/merge_yaml/merged/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml`.

- Source identity: TogoMedium `TOGO:M2003`, imported from original NBRC source `NBRC_M1290`.
- Original source URL: `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1290`.
- Generated lineage: `merge_fingerprint: f9af2596e3c7334b4c2cbdc5560d2321b61154e8e0905620ee0e852ed1b27b2c`, `merged_from: lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids`.
- Maintained owner for fixes: `data/normalized_yaml/bacterial/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with "No issues found". |
| `scripts/validate_strict.py data/merge_yaml/merged/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml --workers 1 --quiet` | Passed with 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

The record identity is correct. TogoMedium API record `M2003` names `LB + 10mM MgSO4, 3mM CaCl2 and 0.1% Casamino acids`, cites `NBRC_M1290` as the original medium ID, and links to NBRC medium detail `NO=1290`. The NBRC page for medium 1290 has the same name and ingredient table.

The checked ChEBI groundings are appropriate for the exact hydrated salts that remain structured: `MgSO4.7H2O` is grounded to magnesium sulfate heptahydrate, `CaCl2.2H2O` to calcium chloride dihydrate, `NaCl` to sodium chloride, and distilled water to water. Yeast extract, tryptone, casamino acids, and conditional agar are complex or source-qualified materials and are left without misleading small-molecule ChEBI IDs.

## Evidence

The NBRC medium 1290 page lists 10 g tryptone, 5 g yeast extract, 5 g NaCl, 2.5 g `MgSO4.7H2O`, 0.45 g `CaCl2.2H2O`, 3 g casamino acids, 1 L distilled water, optional 15 g agar, and `pH 7.0`. The TogoMedium `M2003` API returns the same component names and amounts in a one-liter main solution and repeats `pH 7.0` in both metadata and comments.

Most ingredient masses in the YAML match the source. The record also preserves `Agar (if needed)`, which is important because the source makes the 15 g agar addition conditional. Three source-supported claims are missing or wrong:

- Distilled water is imported as `1 G_PER_L`; both source views say `1 L`, so the record has the water unit wrong.
- The source pH is 7.0, but the YAML has no pH object or pH preparation note.
- The source title says `0.1% Casamino acids`, while the tabulated formulation says 3 g casamino acids in 1 L, or 0.3% w/v. The record imports the 3 g/L table value but has no `discussion` or quality flag documenting that source-internal conflict.

## Completeness

The record is not complete enough as curated YAML because it has a wrong water unit and omits a stated pH. It also keeps the source URL only inside `notes`; there are no top-level `references`, which leaves reference validation with 0 checks even though both the TogoMedium and NBRC URLs are material evidence for the record.

No consequential source was found for incubation temperature, sterilization, strain-specific growth, atmosphere, or storage. NBRC M1290 and TogoMedium M2003 do not state those details.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:008590`, `TOGO:M2003`, `NBRC_M1290`, `NO=1290`, the source slug, and the merge fingerprint found the maintained normalized owner, this generated merge, and normalized index rows. It did not find an alternate maintained overlay or a prior archived curation report for this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water has the wrong unit. | NBRC M1290 and TogoMedium M2003 both list `Distilled water` as 1 L; the YAML stores `value: '1'` with `unit: G_PER_L`. | `data/normalized_yaml/bacterial/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml` |
| Major | The source pH is missing. | Both the NBRC page and the TogoMedium API state `pH 7.0`; the YAML has no pH field. | `data/normalized_yaml/bacterial/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml` |
| Minor | The source-internal Casamino acids inconsistency is not documented. | The medium title says `0.1% Casamino acids`, but both source component tables list 3 g casamino acids in 1 L. | `data/normalized_yaml/bacterial/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml` |
| Minor | Material source URLs are present only in free text. | The generated record names TogoMedium M2003 and the NBRC 1290 URL in `notes`, but it has no `references`, so the reference validator had 0 URL checks. | `data/normalized_yaml/bacterial/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml` |

No blocker findings were found.

## Recommended Edits

1. Change the distilled-water ingredient to a volume unit that preserves the source `1 L`.
2. Add `pH 7.0` from NBRC M1290 / TogoMedium M2003 in the structured pH slot.
3. Add `references` for `https://togomedium.org/medium/M2003`, the TogoMedium API source if retained, and `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1290`.
4. Add a bounded `discussion` or `data_quality_flags` entry noting that the medium title says `0.1% Casamino acids` while the component table lists 3 g/L.
5. Regenerate `data/merge_yaml/merged/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml` after the normalized YAML is curated.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on `data/normalized_yaml/bacterial/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml`.
- Re-run the merge pipeline and verify that the generated `CultureMech:008590` record carries the corrected distilled-water unit, `pH 7.0`, and source references.
- Re-run strict, schema, term, and reference validation on the regenerated `data/merge_yaml/merged/lb_10mm_mgso4_3mm_cacl2_and_0_1_casamino_acids.yaml`.
- Manually recompare the regenerated record against NBRC medium 1290 and TogoMedium M2003, especially the conditional agar row and the unresolved `0.1%` versus 3 g/L Casamino acids mismatch.

## Additional Notes

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
