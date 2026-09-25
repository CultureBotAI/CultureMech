# YAML Record Review: 0.01% LB SEAWATER MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/0_01_lb_seawater_medium.yaml`
- Started UTC: 2026-09-21T04:15:05Z
- Finished UTC: 2026-09-21T04:17:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/0_01_lb_seawater_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002439` |
| Name | `0_01_lb_seawater_medium` |
| Label | `0.01% LB SEAWATER MEDIUM` |
| Source | JCM medium 1273 via `mediadive.medium:J1273` |
| Generated? | Yes; single-source merge from `data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml` |

The record is a generated merge artifact. Its scientific fields match the
authoritative normalized source, so future corrections belong in
`data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml`, followed by
`just merge-recipes` / index regeneration rather than a direct patch to this
file.

## Validation

| Check | Result |
|---|---|
| `just validate-schema data/merge_yaml/merged/0_01_lb_seawater_medium.yaml` | Not usable: the project `uv` environment attempted to build `llvmlite==0.46.0` under Python 3.13 and failed in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. |
| `just validate-strict data/merge_yaml/merged/0_01_lb_seawater_medium.yaml --out /private/tmp/culturemech-review-0_01_lb.strict.tsv --workers 1 --quiet` | Not usable: same `llvmlite==0.46.0` build failure. |
| `just validate-terms data/merge_yaml/merged/0_01_lb_seawater_medium.yaml` | Not usable: same `llvmlite==0.46.0` build failure. |
| No-project LinkML schema fallback | Passed: `linkml-validate` reported `No issues found`. |
| No-project strict-schema fallback | Passed: 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| No-project reference fallback | Passed: 1 file validated, 0 reference checks, all validations passed. |
| No-project term fallback | Passed: `linkml-term-validator` reported `Validation passed`. |
| History validation | Not checked: this review did not create a `history/*.yaml` record. |

## Identity and Grounding

The record identity is correct for the named source medium: MediaDive J1273
identifies JCM medium 1273 as `0.01% LB SEAWATER MEDIUM`, links to the same JCM
`GRMD=1273` page, and reports final pH 8.0. The JCM page likewise titles the
recipe `1273 0.01% LB SEAWATER MEDIUM`.

The simple salts and buffer are grounded plausibly:

| Ingredient | Record value | Source value | Review |
|---|---:|---:|---|
| `NaNO3` | 0.12 g/L | 120 mg/L | Supported |
| `K2HPO4` | 0.005 g/L | 5 mg/L | Supported |
| `Tris(hydroxymethyl)aminomethane` | 1 g/L | 1 g/L | Supported |

Several amount/unit claims are not source-faithful, and one source ingredient
has been replaced with unsupported decomposition rows. Those are detailed under
**Findings**.

## Evidence

The inspected sources were:

- live MediaDive REST response for `J1273`;
- live JCM `GRMD=1273` HTML.

MediaDive and JCM agree on the formulation:

| Source ingredient | Source amount | Generated representation |
|---|---:|---|
| `NaNO3` | 120 mg | 0.12 g/L |
| `K2HPO4` | 5 mg | 0.005 g/L |
| `Vitamin B12` | 1 ug | 1 g/L |
| `Biotin` | 1 ug | 1 g/L |
| `Thiamine HCl` | 100 ug | 100 g/L |
| `Fe(III)-EDTA` | 259 ug | 259 g/L |
| `Mn(II) x EDTA` | 332 ug | 332 g/L |
| `Tris(hydroxymethyl)aminomethane` | 1 g | 1 g/L |
| `LB Broth, Lennox (BD-Difco)` / `LB Broth` | 0.1 g | Missing; replaced by full-strength LB Miller constituents |
| `Seawater` | 1 L / 1000 ml | 1000 g/L |

The generated preparation steps preserve the source pH 8.0 HCl/autoclave step
and the source comment that artificial seawater, such as JCM medium 1118, can
replace natural seawater.

The notes block is only partly source-supported. The recipe source names
`LB Broth, Lennox (BD-Difco)` / `LB Broth`; the generated note about a
commercial LB Miller formulation, multiple suppliers, Sigma and BD catalogs,
and a non-authoritative `laboratorynotes.com` source does not correspond to
JCM 1273's stated Lennox product row.

## Completeness

The record captures the source medium identity, pH, preparation text, and the
two supported seawater-related steps. It is materially incomplete and
misleading for stock/final arithmetic because the final recipe cannot be
reconstructed from the generated ingredient table:

- microgram rows were imported as grams per liter;
- 1 L seawater was imported as grams per liter;
- the sole LB source ingredient was dropped and replaced with unsupported
  full-strength LB Miller constituents;
- `high_metal: true` appears to be an artifact of the Fe/Mn microgram-to-gram
  import error.

No target-organism or growth-evidence claims are present to review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Vitamin and metal microgram rows are inflated by 1,000,000x. `Vitamin B12`, `Biotin`, `Thiamine HCl`, `Fe(III)-EDTA`, and `Mn(II) x EDTA` are recorded as `1`, `1`, `100`, `259`, and `332` g/L, while JCM and MediaDive list those values in micrograms per liter. | JCM 1273 and MediaDive J1273 list 1 ug vitamin B12, 1 ug biotin, 100 ug thiamine HCl, 259 ug Fe(III)-EDTA, and 332 ug Mn(II) x EDTA. | `data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml` importer-normalized amounts |
| Major | The source's 0.1 g/L `LB Broth, Lennox (BD-Difco)` was replaced with full-strength LB Miller internals: 10 g/L tryptone, 5 g/L yeast extract, and 10 g/L sodium chloride. | JCM 1273 lists 0.1 g `LB Broth, Lennox (BD-Difco)` and does not decompose it; MediaDive J1273 similarly lists 0.1 g `LB Broth`. | `data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml` LB commercial-product enrichment |
| Major | `Sea water` is modeled as `1000 G_PER_L` instead of a liquid volume of 1000 ml/L. | JCM lists 1 L seawater; MediaDive lists 1000 ml seawater for a 1000 ml main solution. | `data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml` volume import |
| Minor | `high_metal: true` is likely a false flag caused by the microgram-to-gram Fe/Mn import. | The source metals are sub-milligram quantities, not hundreds of grams per liter. | `data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml` plus any high-metal derivation rule |
| Minor | The notes cite a generic LB Miller web page and supplier/catalog details that do not support JCM 1273's source ingredient. | JCM 1273 names `LB Broth, Lennox (BD-Difco)`, not LB Miller medium from multiple suppliers. | `data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml` notes |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml`, convert the
   five microgram rows to correct final mass concentrations: 1 ug/L vitamin B12,
   1 ug/L biotin, 100 ug/L thiamine HCl, 259 ug/L Fe(III)-EDTA, and 332 ug/L
   Mn(II)-EDTA.
2. Replace the unsupported full-strength LB Miller decomposition with the source
   ingredient `LB Broth, Lennox (BD-Difco)` at 0.1 g/L. Preserve the BD-Difco
   attribute if the schema has an appropriate source/product slot; otherwise keep
   it in a narrow note on that ingredient.
3. Represent seawater as 1000 ml/L or another supported volume unit, not grams
   per liter.
4. Remove the unsupported generic LB Miller notes and the `laboratorynotes.com`
   provenance from this record.
5. Recompute or remove `high_metal` after the Fe/Mn concentrations are corrected.
6. Regenerate `data/merge_yaml/merged/` and indexes from the normalized record.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml`
  and `just validate-strict data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml`
  after the normalized edit once the project `uv` environment is usable.
- Run `just validate-terms data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml`
  to confirm the retained chemical groundings and any unresolved `Mn(II)-EDTA`
  representation.
- Run `just validate-references data/normalized_yaml/bacterial/0_01_lb_seawater_medium.yaml`
  if stable JCM/MediaDive evidence is promoted into `references`.
- Run `just merge-recipes`, `just verify-merges`, and
  `just audit-merge-freshness` after regenerating this generated record.
- Manually compare the regenerated merged record to JCM 1273 / MediaDive J1273:
  the only source ingredient not represented by a simple final concentration
  should be `LB Broth, Lennox (BD-Difco)` at 0.1 g/L.

## Additional Notes

This review found no ambiguity in the source identity: the generated
`media_term` points at the same JCM medium exposed by both upstream providers.
The major defects are representation defects in the imported/normalized
ingredient table, not a wrong-medium merge.
