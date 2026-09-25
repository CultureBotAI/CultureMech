# YAML Record Review: Medium for Strain T-1-35

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_strain_t_1_35.yaml
- Started UTC: 2026-09-24T01:59:28Z
- Finished UTC: 2026-09-24T02:00:06Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008566 |
| Record name | medium_for_strain_t_1_35 |
| Original name | Medium for Strain T-1-35 |
| Generated path | data/merge_yaml/merged/medium_for_strain_t_1_35.yaml |
| Maintained owner | data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml |
| Upstream source | TOGO:M1983, imported from NBRC_M1269 |
| Upstream URL | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1269 |

The reviewed YAML is generated from `data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml`.
Formula fixes belong in that normalized owner and then need regeneration of
`data/merge_yaml/merged/medium_for_strain_t_1_35.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_strain_t_1_35.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_strain_t_1_35.yaml --out /private/tmp/medium_for_strain_t_1_35.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_strain_t_1_35.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_strain_t_1_35.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in generated YAML. |

## Identity and Grounding

- The record identity matches its source. TOGO M1983 reports
  `Medium for Strain T-1-35`, `original_media_id=NBRC_M1269`, and the inspected
  NBRC Medium No. 1269 page is titled `Medium for Strain T-1-35`.
- The imported NBRC source URL in the YAML matches the inspected NBRC page.
- The bacterial category, complex medium type, undefined composition type, and
  liquid physical state are consistent with the source formula.
- An exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` for `TOGO:M1983`, `M1983`, `NBRC_M1269`, `NO=1269`,
  the source label, and `medium_for_strain_t_1_35` found only this normalized
  owner and generated record.

## Evidence

- The main solution rows before the stock additions are source-supported:
  NBRC and TOGO list 1 L distilled water, 1 g yeast extract, 1 g NaCl, 0.15 g
  CaCl2 x 2 H2O, 0.2 g KH2PO4, 0.25 g NH4Cl, 2 mg resazurin, 0.4 g
  MgCl2 x 6 H2O, 0.36 g Na2S x 9 H2O, 0.5 g KCl, 2.52 g NaHCO3, and 10 g
  cellobiose.
- Resazurin has the right numeric value but the wrong unit. The source gives
  2 mg; the YAML stores `2 G_PER_L`.
- All four stock additions are supported as milliliter-per-liter additions but
  not as gram additions. The source adds Trace element SL-10 at 1 ml, a
  selenite-tungstate solution at 1 ml, a vitamin solution at 2 ml, and a
  vitamin B12 solution at 1 ml; the `solutions` entries store `1`, `1`, `2`,
  and `1` as `G_PER_L`.
- The Trace element SL-10 recipe was flattened into final-medium ingredients.
  Its 990 ml water, 10 ml HCl, 1.5 g FeCl2 x 4 H2O, and mg-scale ZnCl2,
  MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and
  Na2MoO4 x 2 H2O rows belong to a stock dosed at 1 ml/L.
- The selenite-tungstate recipe was flattened into final-medium ingredients:
  1 L water, 0.5 g NaOH, 3 mg Na2SeO3 x 5 H2O, and 4 mg Na2WO4 x 2 H2O are
  stock components for a 1 ml/L addition that is autoclaved separately.
- The vitamin stocks were flattened. The vitamin solution contains 100 ml water
  plus 1 mg biotin, 4 mg p-aminobenzoic acid, and 10 mg thiamine-HCl; the
  vitamin B12 solution contains 100 ml water plus 5 mg cyanocobalamin. Both
  vitamin stocks are source-filtered and used as 2 ml/L and 1 ml/L additions.
- The `Distilled water` row sums five incompatible bases into `1192.0 G_PER_L`:
  the main medium's 1 L, Trace element SL-10's 990 ml, the
  selenite-tungstate stock's 1 L, the vitamin solution's 100 ml, and the
  vitamin B12 solution's 100 ml.
- The final pH range, 8 to 8.5, is present in TOGO and NBRC but absent from the
  YAML.
- NBRC instructs curators to mix the medium except for vitamins, NaHCO3, and
  Na2S x 9 H2O; dispense under nitrogen; seal with butyl rubber stoppers;
  autoclave at 121 C for 15 min; separately autoclave the Na2S x 9 H2O solution
  under N2; filter-sterilize vitamin and NaHCO3 solutions; and add the deferred
  solutions aseptically and anaerobically before inoculation. The YAML has no
  preparation field for these steps and keeps nitrogen as a variable ingredient.

## Completeness

- The four nested stock recipes are absent as stock structures.
- Preparation notes for autoclaving the selenite-tungstate stock and
  filter-sterilizing the two vitamin stocks are absent.
- The final pH range and anaerobic, post-autoclave addition sequence are absent.
- The `high_metal: true` flag is likely an artifact of the flattened SL-10
  stock values rather than an evidence-backed final-medium classification.
- Empty target-organism assertions and empty literature references are not
  defects for this NBRC medium-page import.
- The exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` found no same-slug or same-source duplicate beyond
  the normalized owner and its generated copy.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Four stock recipes are flattened into final-medium rows. | Trace element SL-10, selenite-tungstate, vitamin, and vitamin B12 stocks are used at 1 ml/L, 1 ml/L, 2 ml/L, and 1 ml/L respectively, but their internal components are stored under top-level `ingredients`. | `data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml` |
| Major | Stock and milligram quantities were imported as final `G_PER_L` values. | The source has SL-10 and vitamin components in mg and HCl in ml; the YAML stores values such as `CoCl2 x 6 H2O` at `190 G_PER_L`, `Na2MoO4 x 2 H2O` at `36 G_PER_L`, and `Cyanocobalamin` at `5 G_PER_L`. | `data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml` |
| Major | Distinct water bases were summed into one impossible final concentration. | `Distilled water` is the sum of 1 L, 990 ml, 1 L, 100 ml, and 100 ml from the final medium and four stocks. | `data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml` |
| Major | The stock-addition amounts have the wrong unit. | The source adds the four stocks in milliliters; the YAML stores all four solution entries as `G_PER_L`. | `data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml` |
| Major | Final pH and anaerobic preparation instructions are missing. | NBRC gives pH 8 to 8.5 plus nitrogen dispensing, butyl-stopper sealing, the main autoclave, separate Na2S x 9 H2O autoclaving under N2, filter-sterilized vitamin and NaHCO3 solutions, and anaerobic additions before inoculation. | `data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml` |
| Minor | `high_metal: true` is not supported after stock nesting is restored. | The large metal values in this YAML come from SL-10 stock concentrations before 1 ml/L dilution, not from direct final-medium metal additions. | `data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml` |
| Minor | Empty migrated stock names obscure the imported solution identities. | All four `solutions` entries are still named `Unknown solution` even though their `preferred_term` values identify them. | `data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/medium_for_strain_t_1_35.yaml`, move the
   SL-10, selenite-tungstate, vitamin, and vitamin B12 internal components into
   stock solution records or structured nested solution compositions.
2. Correct the four stock additions to 1 ml/L, 1 ml/L, 2 ml/L, and 1 ml/L rather
   than `G_PER_L` additions.
3. Keep resazurin in the final medium but correct it from `2 G_PER_L` to a
   2 mg/L representation.
4. Remove stock-only water, HCl, FeCl2 x 4 H2O, trace metals, selenite,
   tungstate, NaOH, and vitamin components from top-level final-medium
   `ingredients`.
5. Preserve final pH 8 to 8.5 and the deferred anaerobic additions in
   structured preparation text or condition fields.
6. Recompute `high_metal` after stock nesting and final concentration units are
   fixed.
7. Regenerate merged YAML and downstream pages after the normalized owner is
   repaired.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validators on
  `data/merge_yaml/merged/medium_for_strain_t_1_35.yaml`.
- Re-inspect TOGO M1983 and NBRC Medium 1269 after regeneration and confirm
  that only the main-medium rows remain under top-level `ingredients`.
- Confirm that the four `solutions` entries use milliliter-per-liter amounts
  and resolve to stock compositions or stock records.
- Confirm that `high_metal` is absent or explicitly justified by final
  concentrations after 1 ml/L SL-10 dilution.
- Repeat an exact gitignore-independent search for `TOGO:M1983`, `NBRC_M1269`,
  `NO=1269`, and `medium_for_strain_t_1_35` across normalized and merged YAML
  if the source identity is changed.

## Additional Notes

- Source fetches used the TOGO M1983 API and the live NBRC Medium 1269 page.
- The source spells the vitamin stock heading as `Vitamine solution`; this
  review uses `vitamin solution` for readability.
- No record YAML was edited during this review.
