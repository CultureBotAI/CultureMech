# YAML Record Review: Medium for sulfur-disproportionating bacterium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_sulfur_disproportionating_bacterium.yaml
- Started UTC: 2026-09-24T02:03:16Z
- Finished UTC: 2026-09-24T02:03:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008642 |
| Record name | medium_for_sulfur_disproportionating_bacterium |
| Original name | Medium for sulfur-disproportionating bacterium |
| Generated path | data/merge_yaml/merged/medium_for_sulfur_disproportionating_bacterium.yaml |
| Maintained owner | data/normalized_yaml/bacterial/medium_for_sulfur_disproportionating_bacterium.yaml |
| Upstream source | TOGO:M2051, imported from NBRC_M1351 |
| Upstream URL | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1351 |

The reviewed YAML is generated from `data/normalized_yaml/bacterial/medium_for_sulfur_disproportionating_bacterium.yaml`.
Stock-boundary fixes belong in that normalized owner; the generated record also
needs regeneration because it predates a later duplicate-collapse repair in the
owner.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_sulfur_disproportionating_bacterium.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_sulfur_disproportionating_bacterium.yaml --out /private/tmp/medium_for_sulfur_disproportionating_bacterium.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_sulfur_disproportionating_bacterium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_sulfur_disproportionating_bacterium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in generated YAML. |

## Identity and Grounding

- The record identity is source-consistent: TOGO M2051 reports `Medium for
  sulfur-disproportionating bacterium`, `original_media_id=NBRC_M1351`, and the
  inspected NBRC Medium No. 1351 page has the same title.
- The bacterial category, complex medium type, undefined composition type, and
  liquid physical state are consistent with the source formula.
- An exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` for the slug, source label, TOGO M2051, NBRC_M1351,
  and NBRC `NO=1351` found only this maintained owner and its generated copy.

## Evidence

- The final-medium simple rows are source-supported before duplicate merging:
  NBRC and TOGO list 1 L water, 0.1 g CaCl2 x 2 H2O, 0.1 g KH2PO4, 0.1 g
  NH4Cl, 0.2 g MgCl2 x 6 H2O, 0.1 g KCl, 2.5 g NaHCO3, and 5 g
  Na2S2O3 x 5 H2O.
- The generated YAML is stale relative to the maintained owner. It still stores
  `Distilled water` as `3.0 G_PER_L` and `CaCl2 x 2 H2O` as `0.2 G_PER_L`,
  while the owner collapsed those identical duplicate sums to `1.0 G_PER_L`
  and `0.1 G_PER_L` on 2026-09-02.
- Trace elements, vitamins, and Fe(III) slurry are stock additions in the
  source at 2 ml/L, 10 ml/L, and 50 ml/L. The YAML stores all three additions
  as `G_PER_L` solutions, while also leaving the trace-element and vitamin
  stock components in top-level `ingredients`.
- The trace-element stock contains its own 1 L water, 1 g NaCl, 0.1 g
  CaCl2 x 2 H2O, metals, NTA, tungstate, selenate, and a NaOH pH adjustment.
  Those components are not final-medium rows at their stock concentrations.
- The vitamin stock contains its own 1 L water plus mg-scale biotin,
  p-aminobenzoic acid, thiamine-HCl, Ca-pantothenate, pyridoxine-HCl, folic
  acid, vitamin B12, riboflavin, and nicotinic acid. The YAML stores the mg
  values as direct `G_PER_L` rows.
- The Fe(III) slurry solution is not a simple 50 g/L ingredient. The source
  says to neutralize 0.4 M FeCl3 x 6 H2O solution with NaOH, wash with pure
  water several times, and autoclave under N2.
- N2 and CO2 are gas atmospheres for preparation, not final ingredients. The
  source says to autoclave the main medium under N2/CO2 at 80/20 and the
  Fe(III) slurry under N2.
- The final pH range 6.5 to 7.0 is present in NBRC and TOGO but absent from the
  YAML. The trace-element stock also has a pH 6.5 NaOH adjustment and final
  pH 7.0 instruction that are missing.

## Completeness

- The trace-element, vitamin, and Fe(III) slurry stock recipes are absent as
  stock boundaries.
- The final pH range, trace-element pH handling, gas atmosphere ratios, vitamin
  filtration, Fe(III) slurry washing, and post-autoclave addition sequence are
  absent.
- Empty target-organism growth assertions and empty literature references are
  not defects for this NBRC medium-page import.
- The exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` found no same-slug or same-source duplicate beyond
  this normalized owner and generated record.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Trace-element and vitamin stocks are flattened into final-medium ingredients. | The source adds those stocks at 2 ml/L and 10 ml/L, but the YAML stores their water, salts, trace metals, and vitamins as top-level final-medium `G_PER_L` ingredients. | `data/normalized_yaml/bacterial/medium_for_sulfur_disproportionating_bacterium.yaml` |
| Major | Stock-addition amounts use `G_PER_L` instead of milliliters per liter. | NBRC lists 2 ml trace elements, 10 ml vitamin solution, and 50 ml Fe(III) slurry; the YAML stores `2`, `10`, and `50` as grams per liter. | `data/normalized_yaml/bacterial/medium_for_sulfur_disproportionating_bacterium.yaml` |
| Major | The Fe(III) slurry preparation is not represented. | The source recipe starts from 0.4 M FeCl3 x 6 H2O, neutralizes with NaOH, washes repeatedly, and autoclaves under N2; the YAML has only a 50 g/L empty solution and a variable FeCl3 solution. | `data/normalized_yaml/bacterial/medium_for_sulfur_disproportionating_bacterium.yaml` |
| Major | Gas, pH, filtration, and autoclave instructions are missing or mis-scoped as ingredients. | N2/CO2, N2, and NaOH are preparation details for the main medium, trace stock, and Fe(III) slurry, but the YAML keeps them as variable ingredients and omits the final pH 6.5 to 7.0 and stock pH steps. | `data/normalized_yaml/bacterial/medium_for_sulfur_disproportionating_bacterium.yaml` |
| Minor | The generated file is stale relative to the owner's duplicate-collapse repair. | The owner has corrected the water and CaCl2 x 2 H2O sums; the reviewed generated YAML still has `3.0 G_PER_L` water and `0.2 G_PER_L` calcium chloride dihydrate. | Regenerate `data/merge_yaml/merged/medium_for_sulfur_disproportionating_bacterium.yaml` from the normalized owner. |
| Minor | Empty migrated stock names obscure the stock identities. | All four entries in `solutions` still have `name: Unknown solution` even though their `preferred_term` values identify the imported stocks. | `data/normalized_yaml/bacterial/medium_for_sulfur_disproportionating_bacterium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/medium_for_sulfur_disproportionating_bacterium.yaml`,
   move the trace-element stock and vitamin stock internals out of top-level
   `ingredients` and into structured stock recipes.
2. Correct trace element solution, vitamin solution, and Fe(III) slurry
   additions to 2 ml/L, 10 ml/L, and 50 ml/L.
3. Rebuild the Fe(III) slurry as a preparation from 0.4 M FeCl3 x 6 H2O
   solution, NaOH neutralization, pure-water washing, and N2 autoclaving.
4. Preserve final pH 6.5 to 7.0, trace stock pH 6.5 to 7.0 handling,
   80/20 N2/CO2 main-medium autoclaving, vitamin filtration, and the
   post-autoclave addition sequence.
5. Regenerate merged YAML and downstream pages so the reviewed generated record
   picks up the 2026-09-02 water and CaCl2 x 2 H2O duplicate repair.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validators on
  `data/merge_yaml/merged/medium_for_sulfur_disproportionating_bacterium.yaml`.
- Re-inspect TOGO M2051 and NBRC Medium 1351 after regeneration and confirm
  that stock-only trace, vitamin, NaOH, FeCl3, and gas rows are no longer
  top-level final ingredients.
- Confirm that the generated water and CaCl2 x 2 H2O rows match the normalized
  owner rather than the stale duplicate sums.
- Repeat an exact gitignore-independent search for `TOGO:M2051`, `NBRC_M1351`,
  `NO=1351`, and `medium_for_sulfur_disproportionating_bacterium` across
  normalized and merged YAML if source identity changes.

## Additional Notes

- Source fetches used the TOGO M2051 API and the live NBRC Medium 1351 page.
- No record YAML was edited during this review.
