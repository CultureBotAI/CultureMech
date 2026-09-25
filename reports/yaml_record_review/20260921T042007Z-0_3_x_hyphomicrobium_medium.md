# YAML Record Review: 0.3 x HYPHOMICROBIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/0_3_x_hyphomicrobium_medium.yaml`
- Started UTC: 2026-09-21T04:19:34Z
- Finished UTC: 2026-09-21T04:20:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/0_3_x_hyphomicrobium_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002268` |
| Name | `0_3_x_hyphomicrobium_medium` |
| Label | `0.3 x HYPHOMICROBIUM MEDIUM` |
| Source | JCM Medium 1088 via `mediadive.medium:J1088` |
| Generated? | Yes; single-source merge from `data/normalized_yaml/bacterial/0_3_x_hyphomicrobium_medium.yaml` |

Future scientific fixes belong in
`data/normalized_yaml/bacterial/0_3_x_hyphomicrobium_medium.yaml`; this generated
merge should then be regenerated.

## Validation

| Check | Result |
|---|---|
| Documented `just validate-*` validators | Not rerun for this third report: in the same checkout, the documented project `uv` path fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13. |
| No-project LinkML schema fallback | Passed: `linkml-validate` reported `No issues found`. |
| No-project strict-schema fallback | Passed: 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| No-project reference fallback | Passed: 1 file validated, 0 reference checks, all validations passed. |
| No-project term fallback | Passed: `linkml-term-validator` reported `Validation passed`. |
| History validation | Not checked: this review did not create a `history/*.yaml` record. |

## Identity and Grounding

The record identity is correct for JCM medium 1088. MediaDive J1088 and the live
JCM `GRMD=1088` page both identify the source as `0.3 x HYPHOMICROBIUM MEDIUM`
and list the same main medium, trace vitamin stock, Visniac trace-element stock,
post-autoclave vitamin/methanol addition, and agar amount.

The main basal rows were converted to final concentrations by dividing by
1005 ml final volume, so they are near the MediaDive/JCM values:

| Ingredient | Generated value | Source value |
|---|---:|---:|
| `K2HPO4` | 0.845771 g/L | 0.85 g per 1005 ml |
| `NaH2PO4` | 0.746269 g/L | 0.75 g per 1005 ml |
| `(NH4)2SO4` | 0.199005 g/L | 0.2 g per 1005 ml |
| `MgSO4 x 7 H2O` | 0.0696517 g/L | 0.07 g per 1005 ml |
| `Agar` | 14.9254 g/L | 15 g per 1005 ml |

The same final-volume conversion was not applied to methanol or the two stock
solutions.

## Evidence

The inspected sources were:

- live MediaDive REST response for `J1088`;
- live JCM `GRMD=1088` HTML.

JCM 1088 gives the main formula as 0.85 g `K2HPO4`, 0.75 g `NaH2PO4`, 0.2 g
`(NH4)2SO4`, 0.07 g `MgSO4 x 7 H2O`, 1 ml Visniac trace elements, 2 ml trace
vitamins, 2 ml methanol, 15 g agar, and 1 L distilled water. It instructs
aseptic addition of filter-sterilized trace vitamins and methanol after
autoclaving. MediaDive J1088 reports the same main solution and expands the
Visniac and trace-vitamin stocks.

## Completeness

The record has the source identity and one post-autoclave preparation step.
However, it omits 1000 ml distilled water, erases the Visniac and
trace-vitamin stock boundaries, and therefore cannot be used to reconstruct the
source recipe. No target-organism or growth-evidence claims are present.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Trace vitamins` at 2 ml/L was flattened into final ingredient rows at full stock strength. | JCM and MediaDive have a 500 ml trace-vitamin stock containing 125 mg vitamin B12, 25 mg thiamine HCl, 12.5 mg folic acid, 40 mg ascorbic acid, 25 mg riboflavin, 25 mg niacin, and 25 mg pantothenic acid; only 2 ml of that stock is added to the main medium. | `data/normalized_yaml/bacterial/0_3_x_hyphomicrobium_medium.yaml` |
| Major | `Visniac trace elements` at 1 ml/L was flattened into final ingredient rows at full stock strength. | MediaDive expands the 500 ml Visniac stock as 5 g Na2-EDTA, 2.2 g ZnSO4, 0.733 g CaCl2, 0.506 g MnCl2, 0.499 g FeSO4, 0.11 g ammonium molybdate, 0.157 g CuSO4, and 0.161 g CoCl2; the main medium uses 1 ml. | `data/normalized_yaml/bacterial/0_3_x_hyphomicrobium_medium.yaml` |
| Major | 2 ml/L methanol is represented as `2 G_PER_L`, which assumes a density and ignores the 1005 ml final volume used for the solid ingredients. | MediaDive/JCM list `Methanol` as 2 ml in the main solution. | `data/normalized_yaml/bacterial/0_3_x_hyphomicrobium_medium.yaml` |
| Major | 1000 ml distilled water is omitted. | MediaDive/JCM include 1000 ml distilled water in the main solution. | `data/normalized_yaml/bacterial/0_3_x_hyphomicrobium_medium.yaml` |

## Recommended Edits

1. Restore `Trace vitamins` as a named stock solution added at 2 ml/L, with the
   MediaDive/JCM stock composition nested under that solution or linked to an
   authoritative stock record.
2. Restore `Visniac trace elements` as a named stock solution added at 1 ml/L,
   preserving the JCM Medium 884 / MediaDive stock boundary.
3. Represent methanol as 2 ml/L or a schema-supported liquid volume, not 2 g/L.
4. Add 1000 ml distilled water to the main solution.
5. Regenerate `data/merge_yaml/merged/` and recipe indexes.

## Follow-up Checks

- Run schema, strict, term, and reference validators on the normalized file
  after the stock boundaries are restored.
- Recompare the regenerated merge to MediaDive J1088: the generated top-level
  rows should be only the basal salts, methanol, agar, water, and the two stock
  additions, not the 15 stock-internal vitamin/trace rows.
- Run `just merge-recipes`, `just verify-merges`, and
  `just audit-merge-freshness`.

## Additional Notes

The record has no merge conflation: `merged_from` contains only
`0_3_x_hyphomicrobium_medium`. The defect is the MediaDive import/normalization
that flattened two stocks into the final medium.
