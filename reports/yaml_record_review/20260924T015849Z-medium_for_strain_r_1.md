# YAML Record Review: Medium for strain R-1

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_strain_r_1.yaml
- Started UTC: 2026-09-24T01:58:14Z
- Finished UTC: 2026-09-24T01:58:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008433 |
| Record name | medium_for_strain_r_1 |
| Original name | Medium for strain R-1 |
| Generated path | data/merge_yaml/merged/medium_for_strain_r_1.yaml |
| Maintained owner | data/normalized_yaml/bacterial/medium_for_strain_r_1.yaml |
| Upstream source | TOGO:M1859, imported from NBRC_M1103 |
| Upstream URL | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1103 |

The reviewed YAML is generated from `data/normalized_yaml/bacterial/medium_for_strain_r_1.yaml`.
Future formula repairs belong in that normalized owner; `data/merge_yaml/merged`
must be regenerated rather than patched directly.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_strain_r_1.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_strain_r_1.yaml --out /private/tmp/medium_for_strain_r_1.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_strain_r_1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_strain_r_1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in generated YAML. |

## Identity and Grounding

- The record identity matches its source: TOGO M1859 reports `Medium for strain
  R-1`, `original_media_id=NBRC_M1103`, and NBRC Medium No. 1103 is also titled
  `Medium for strain R-1`.
- The imported source URL in the YAML matches the inspected NBRC 1103 page.
- An exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` for the slug, label, TOGO M1859, NBRC_M1103, and
  NBRC `NO=1103` found only this maintained owner and its generated copy.
- The bacterial category and complex, undefined composition type are plausible
  because the source medium contains yeast extract.
- The `SOLID_AGAR` physical state is over-specific: NBRC lists `Agar (if
  needed)` at 20 g, so the source describes an optional solidified form rather
  than a medium that is intrinsically or always agar-solidified.

## Evidence

- The final-medium gram-scale rows are source-supported: NBRC and TOGO list
  1 L distilled water plus MgSO4 x 7 H2O, yeast extract, NaCl,
  CaCl2 x 2 H2O, NH4Cl, K2HPO4, sodium acetate, FeCl3 x 6 H2O, sodium
  succinate, sodium propionate, optional agar, and sodium malate at the same
  numeric amounts imported in the YAML.
- The two vitamin rows have the right numeric values but the wrong unit. NBRC
  and TOGO list biotin at 0.01 mg and thiamine-HCl at 0.2 mg; the YAML stores
  them as `0.01 G_PER_L` and `0.2 G_PER_L`.
- The neutralized sulfide stock was flattened into final-medium ingredients.
  NBRC and TOGO define a separate stock made from 1.5 g Na2S x 9 H2O and
  100 ml distilled water, adjusted after cooling with sterile 2 N H2SO4 under
  N2. The YAML merges the stock's 100 ml water with the main medium's 1 L water
  as `101.0 G_PER_L`, stores Na2S x 9 H2O as a direct `1.5 G_PER_L`
  ingredient, and imports H2SO4 and N2 as variable final ingredients.
- The source final pH is 6.8; the YAML has no `ph_value`.
- NBRC preparation text says to mix ingredients except the biotin and
  thiamine-HCl solutions, adjust to pH 6.8, dispense the medium under nitrogen,
  seal with butyl rubber stoppers, autoclave at 121 C for 15 min, then add
  sterile filtered biotin, sterile filtered thiamine-HCl, and neutralized
  sulfide aseptically and anaerobically before inoculation. Those steps are not
  represented.
- The neutralized sulfide stock preparation says to autoclave the sealed stock
  under N2 at 121 C for 15 min, cool, adjust to about pH 7.3 with sterile 2 N
  H2SO4 drop-wise without opening the bottle, shake continuously to avoid
  elemental sulfur precipitation, and finish with a transparent yellow
  solution. The YAML has no corresponding stock preparation text.

## Completeness

- The neutralized sulfide solution is missing as a stock boundary.
- The biotin and thiamine-HCl solution additions are missing as post-autoclave,
  sterile-filtered additions; only their final quantities survived.
- Final pH 6.8, neutralized-sulfide pH about 7.3, N2 handling, butyl stoppers,
  autoclave conditions, and anaerobic post-autoclave additions are missing.
- Empty target-organism assertions and empty literature references are not
  defects for this NBRC medium-page import.
- The exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` found no same-slug or same-source duplicate beyond
  `data/normalized_yaml/bacterial/medium_for_strain_r_1.yaml` and
  `data/merge_yaml/merged/medium_for_strain_r_1.yaml`.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The neutralized sulfide stock recipe is flattened into final-medium ingredient rows. | The source's 100 ml water, 1.5 g Na2S x 9 H2O, H2SO4 pH adjustment, and N2 atmosphere belong to a separately prepared sulfide solution, not to the final 1 L main medium. | `data/normalized_yaml/bacterial/medium_for_strain_r_1.yaml` |
| Major | The generated water amount is impossible. | `Distilled water` was merged from `1.0` and `100.0` into `101.0 G_PER_L`, combining the 1 L main-medium basis with the 100 ml sulfide-stock basis. | `data/normalized_yaml/bacterial/medium_for_strain_r_1.yaml` |
| Major | The vitamin quantities are off by 1000x because milligrams were imported as grams per liter. | NBRC and TOGO list biotin at 0.01 mg and thiamine-HCl at 0.2 mg; the YAML stores those same numeric values in `G_PER_L`. | `data/normalized_yaml/bacterial/medium_for_strain_r_1.yaml` |
| Major | Required pH and preparation details are absent. | The source gives final pH 6.8 plus anaerobic dispensing, butyl-stopper sealing, autoclaving, sterile-filtered vitamin additions, sulfide-stock addition, and sulfide-stock pH adjustment under N2. | `data/normalized_yaml/bacterial/medium_for_strain_r_1.yaml` |
| Minor | The physical state promotes an optional agar variant to an unconditional state. | The source names `Agar (if needed)`, but the YAML classifies the recipe as `SOLID_AGAR`. | `data/normalized_yaml/bacterial/medium_for_strain_r_1.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/medium_for_strain_r_1.yaml`, model the
   neutralized sulfide solution as a stock recipe with 100 ml water, 1.5 g
   Na2S x 9 H2O, 2 N H2SO4 adjustment to about pH 7.3, and N2 autoclaving and
   handling instructions; remove those stock-only rows from final
   `ingredients`.
2. Correct biotin from `0.01 G_PER_L` to a 0.01 mg/L representation and
   thiamine-HCl from `0.2 G_PER_L` to a 0.2 mg/L representation.
3. Preserve pH 6.8 and the NBRC main-medium preparation sequence, including
   deferred sterile-filtered vitamin additions and the anaerobic sulfide
   addition before inoculation.
4. Revisit `physical_state` so optional agar is represented without implying
   that the base R-1 recipe is always solidified.
5. Regenerate merged YAML and downstream pages after the normalized owner is
   repaired.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validators on
  `data/merge_yaml/merged/medium_for_strain_r_1.yaml`.
- Re-inspect TOGO M1859 and NBRC Medium 1103 after regeneration and confirm
  that the final-medium ingredients no longer include sulfide-stock water,
  H2SO4, or N2.
- Confirm that biotin and thiamine-HCl serialize as milligram-scale quantities.
- Confirm that `Agar (if needed)` remains optional in the regenerated recipe.
- Repeat an exact gitignore-independent search for `TOGO:M1859`, `NBRC_M1103`,
  `NO=1103`, and `medium_for_strain_r_1` across normalized and merged YAML if
  the source identity is changed.

## Additional Notes

- Source fetches used the TOGO M1859 API and the live NBRC Medium 1103 page.
- No record YAML was edited during this review.
