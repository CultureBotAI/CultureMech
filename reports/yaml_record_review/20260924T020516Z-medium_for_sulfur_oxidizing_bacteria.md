# YAML Record Review: Medium for sulfur-oxidizing bacteria

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_sulfur_oxidizing_bacteria.yaml
- Started UTC: 2026-09-24T02:04:37Z
- Finished UTC: 2026-09-24T02:05:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008686 |
| Record name | medium_for_sulfur_oxidizing_bacteria |
| Original name | Medium for sulfur-oxidizing bacteria |
| Generated path | data/merge_yaml/merged/medium_for_sulfur_oxidizing_bacteria.yaml |
| Maintained owner | data/normalized_yaml/bacterial/medium_for_sulfur_oxidizing_bacteria.yaml |
| Upstream source | TOGO:M2095, imported from NBRC_M1406 |
| Upstream URL | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1406 |

The reviewed YAML is generated from `data/normalized_yaml/bacterial/medium_for_sulfur_oxidizing_bacteria.yaml`.
Future formula fixes belong in that normalized owner and then need regeneration
of `data/merge_yaml/merged/medium_for_sulfur_oxidizing_bacteria.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_sulfur_oxidizing_bacteria.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_sulfur_oxidizing_bacteria.yaml --out /private/tmp/medium_for_sulfur_oxidizing_bacteria.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_sulfur_oxidizing_bacteria.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_sulfur_oxidizing_bacteria.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in generated YAML. |

## Identity and Grounding

- The record identity is source-consistent: TOGO M2095 reports `Medium for
  sulfur-oxidizing bacteria`, `original_media_id=NBRC_M1406`, and the inspected
  NBRC Medium No. 1406 page has the same title.
- The bacterial category, complex medium type, undefined composition type, and
  liquid physical state are consistent with the source formula.
- An exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` for `TOGO:M2095`, `M2095`, `NBRC_M1406`, `NO=1406`,
  the source label, and `medium_for_sulfur_oxidizing_bacteria` found only this
  maintained owner and its generated record.

## Evidence

- The main-medium gram rows are source-supported: NBRC and TOGO list 1 L water,
  0.3 g MgSO4 x 7 H2O, 20 g NaCl, 0.1 g CaCl2 x 2 H2O, 0.1 g KH2PO4, 0.1 g
  NH4Cl, 3 g MgCl2 x 6 H2O, 0.1 g KCl, and 5 g Na2S2O3 x 5 H2O.
- The four solution additions have source-supported names but unsupported
  units. The source doses Trace element solution at 2 ml/L,
  Selenite-tungstate solution at 2 ml/L, Bicarbonate solution at 15 ml/L, and
  Vitamin solution at 2 ml/L; the YAML records those amounts as `G_PER_L`.
- All four stock recipes are flattened into final-medium ingredients. The
  top-level `Distilled water` sum of `104.0 G_PER_L` combines the main 1 L
  water with 1 L trace-element stock water, 1 L selenite-tungstate stock water,
  100 ml bicarbonate-stock water, and 1 L vitamin-stock water.
- The trace-element stock's 35% HCl, Na2MoO4 x 2 H2O, H3BO3, MnCl2 x 4 H2O,
  CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, ZnCl2, and FeCl3 x 6 H2O are
  stored as direct final-medium rows instead of stock components for the
  2 ml/L addition.
- The selenite-tungstate stock's 1 L water, 0.4 g NaOH, 6 mg
  Na2SeO3 x 5 H2O, and 8 mg Na2WO4 x 2 H2O are also flattened; the two
  mg-scale rows were imported as `6 G_PER_L` and `8 G_PER_L`.
- The bicarbonate stock is 8.4 g NaHCO3 in 100 ml water and is added at
  15 ml/L. The YAML stores NaHCO3 as a direct `8.4 G_PER_L` ingredient.
- The vitamin stock contains 1 L water plus mg-scale biotin,
  p-aminobenzoic acid, thiamine-HCl, Ca-pantothenate, pyridoxine-HCl, folic
  acid, vitamin B12, riboflavin, and nicotinic acid. The YAML stores those
  stock values as final-medium `G_PER_L` ingredients.
- Final pH 7.0 to 7.2 is present in TOGO and NBRC but absent from the YAML.
  The source also says to adjust the main medium to pH 7.0 with NaOH, autoclave
  at 121 C for 20 min, and aseptically add bicarbonate and vitamin solutions
  after autoclaving.

## Completeness

- The trace-element, selenite-tungstate, bicarbonate, and vitamin stock
  boundaries are missing.
- The pH 7.0 to 7.2 final range, main pH adjustment to 7.0, main autoclave,
  post-autoclave additions, trace-element HCl dissolution instruction, and
  filter-sterilized vitamin stock note are missing.
- Empty target-organism growth assertions and empty literature references are
  not defects for this NBRC medium-page import.
- The exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` found no same-slug or same-source duplicate beyond
  this normalized owner and generated record.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Four stock recipes are flattened into final-medium ingredients. | Trace element, selenite-tungstate, bicarbonate, and vitamin stocks are source subrecipes dosed at 2, 2, 15, and 2 ml/L, but their internal components are top-level `ingredients`. | `data/normalized_yaml/bacterial/medium_for_sulfur_oxidizing_bacteria.yaml` |
| Major | The solution additions use `G_PER_L` instead of milliliter-per-liter amounts. | The source gives all four stock additions as ml amounts, while the YAML stores 2, 2, 15, and 2 as grams per liter. | `data/normalized_yaml/bacterial/medium_for_sulfur_oxidizing_bacteria.yaml` |
| Major | Stock units were promoted to impossible final-medium concentrations. | The selenite and tungstate stock lists 6 mg and 8 mg, and the vitamin stock lists 0.01 to 10 mg values, but the YAML stores the same numbers in `G_PER_L`; bicarbonate is likewise a 1.0 M stock added at 15 ml/L, not a direct 8.4 g/L component. | `data/normalized_yaml/bacterial/medium_for_sulfur_oxidizing_bacteria.yaml` |
| Major | Preparation details and pH are missing. | The source gives pH 7.0 to 7.2, a pH 7.0 NaOH adjustment, 121 C for 20 min autoclaving, aseptic post-autoclave additions, HCl dissolution for the trace stock, and filtration for the vitamin stock. | `data/normalized_yaml/bacterial/medium_for_sulfur_oxidizing_bacteria.yaml` |
| Minor | Empty migrated stock names obscure the solution identities. | All four `solutions` entries still have `name: Unknown solution` even though their `preferred_term` values identify them. | `data/normalized_yaml/bacterial/medium_for_sulfur_oxidizing_bacteria.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/medium_for_sulfur_oxidizing_bacteria.yaml`,
   move the trace-element, selenite-tungstate, bicarbonate, and vitamin stock
   internals out of top-level `ingredients`.
2. Correct stock-addition amounts to 2 ml/L, 2 ml/L, 15 ml/L, and 2 ml/L.
3. Preserve the bicarbonate solution as a 1.0 M stock rather than a direct
   `8.4 G_PER_L` NaHCO3 ingredient.
4. Correct selenite, tungstate, and vitamin stock components to their source mg
   quantities inside nested stocks.
5. Preserve final pH 7.0 to 7.2, NaOH adjustment to pH 7.0, main autoclaving,
   trace-stock HCl dissolution, filter-sterilized vitamins, and post-autoclave
   bicarbonate and vitamin addition in preparation fields.
6. Regenerate merged YAML and downstream pages after the normalized owner is
   repaired.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validators on
  `data/merge_yaml/merged/medium_for_sulfur_oxidizing_bacteria.yaml`.
- Re-inspect TOGO M2095 and NBRC Medium 1406 after regeneration and confirm
  that stock-only water, HCl, NaOH, bicarbonate, selenite, tungstate, and
  vitamin rows are absent from top-level `ingredients`.
- Confirm that all four `solutions` entries use milliliter-per-liter amounts
  and retain their own stock compositions or resolvable stock references.
- Repeat an exact gitignore-independent search for `TOGO:M2095`, `NBRC_M1406`,
  `NO=1406`, and `medium_for_sulfur_oxidizing_bacteria` across normalized and
  merged YAML if source identity changes.

## Additional Notes

- Source fetches used the TOGO M2095 API and the live NBRC Medium 1406 page.
- No record YAML was edited during this review.
