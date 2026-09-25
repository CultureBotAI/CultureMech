# YAML Record Review: pyrobaculum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pyrobaculum_medium__5f47a5d9.yaml
- Started UTC: 2026-09-24T23:39:21Z
- Finished UTC: 2026-09-24T23:40:19Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pyrobaculum_medium__5f47a5d9.yaml` as a generated `MediaRecipe` for `CultureMech:009169`, label `pyrobaculum_medium`, with `media_term` `TOGO:M2600`.

The generated record has one normalized input, `data/normalized_yaml/archaea/TOGO_M2600_Pyrobaculum_Medium.yaml`. That maintained TOGO owner cites `DSMZ_Medium390.pdf`; repairs should be made there and then propagated by regenerating `data/merge_yaml/merged`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pyrobaculum_medium__5f47a5d9.yaml` | Passed; printed `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pyrobaculum_medium__5f47a5d9.yaml --out /private/tmp/pyrobaculum_medium__5f47a5d9.strict.tsv --workers 1 --quiet` | Passed; 1 TSV line, header only, 0 error rows. |
| Internal references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pyrobaculum_medium__5f47a5d9.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were configured for this record. |
| Term grounding | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pyrobaculum_medium__5f47a5d9.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils/pkg_resources` warning. |
| Embedded history | `just validate-history` | Not checked: the available validator covers standalone `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

TOGO M2600, DSMZ Medium 390, MediaDive medium 390, and the linked `DSMZ_Medium390.pdf` all identify `Pyrobaculum Medium`/`PYROBACULUM MEDIUM`, so the record's intended source identity is correct.

An ignored-file-inclusive exact search across `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports/yaml_record_review` for `TOGO_M2600_Pyrobaculum_Medium`, `TOGO:M2600`, `togomedium.org/medium/M2600`, `CultureMech:009169`, `DSMZ_Medium390`, and the full `5f47a5d9a054770b78e1af381ecca0825d157f1ec611f3b9837b1a6f0f4bbd0b` fingerprint found only this TOGO M2600 owner plus this generated artifact for M2600. A second ignored-file-inclusive exact search for `mediadive.medium:390`, `TOGO_M2470_Pyrobaculum_Medium`, `TOGO:M2470`, and `togomedium.org/medium/M2470` found the direct DSMZ 390 owner, the KOMODO 390 family, and another TOGO projection of the same DSMZ PDF.

## Evidence

The live TOGO M2600 payload points to the DSMZ 390 PDF and preserves the main solution, the 10 ml Allen's trace element solution reference, and the Allen's stock component group. Its main group includes 0.5 ml 0.1% sodium resazurin, 1000 ml distilled water, 0.25 g magnesium sulfate heptahydrate, 0.07 g calcium chloride dihydrate, 0.28 g potassium dihydrogen phosphate, 0.5 g sodium sulfide nonahydrate, 1.3 g ammonium sulfate, 0.02 g iron chloride hexahydrate, and 10 ml Allen's trace element solution. The DSMZ PDF and MediaDive API additionally specify 0.50 g Trypticase peptone, 0.20 g yeast extract, and 2.00 g sodium thiosulfate pentahydrate in the main formulation.

The generated record is not numerically faithful to those sources:

- `Distilled water` is `2000.0 G_PER_L` because the 1000 ml main-solution water and 1000 ml Allen's stock water were merged as duplicate top-level ingredients.
- `Yeast extract`, `Na2S2O3 x 5 H2O`, and `Trypticase peptone` are `VARIABLE` even though DSMZ 390 gives exact 0.20 g, 2.00 g, and 0.50 g amounts.
- The Allen's stock rows were flattened as `180`, `450`, `22`, `5`, `3`, `3`, and `1 G_PER_L`, treating stock milligrams as final-medium grams per liter.
- The explicit 10 ml Allen's stock addition was retained only as `solutions[0]` with `composition: []` and `10 G_PER_L`.

TOGO M2600 includes comments matching the DSMZ preparation: adjust complete medium to pH 6.0, sparge with 100% N2 for at least 30 min, add peptone, yeast extract, thiosulfate, and sulfide from sterile anoxic stocks, filter-sterilize thiosulfate, readjust final pH to 6.0, and adjust the Allen's stock to pH 2 with 1 N HCl. The generated YAML has no `ph_value` and no `preparation_steps`.

## Completeness

Empty optional fields are not defects.

Consequential omissions:

- No `ph_value: 6.0` survives from TOGO/DSMZ.
- Exact DSMZ amounts for yeast extract, sodium thiosulfate pentahydrate, and Trypticase peptone were replaced with `VARIABLE` defaults.
- The Allen's stock is empty, and its internal pH adjustment is modeled as a variable top-level `1 N HCl` ingredient.
- The DSMZ anaerobic preparation is absent.
- No relationship links the TOGO M2600 owner to the direct MediaDive/DSMZ 390 owner or the parallel TOGO M2470 projection of the same PDF.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The Allen's stock solution has been flattened and its milligram rows are inflated to grams per liter. | TOGO M2600 and DSMZ 390 define a 10 ml Allen's trace element solution addition with 180 mg manganese chloride tetrahydrate, 450 mg sodium tetraborate decahydrate, 22 mg zinc sulfate heptahydrate, 5 mg copper chloride dihydrate, 3 mg sodium molybdate dihydrate, 3 mg vanadyl sulfate dihydrate, and 1 mg cobalt sulfate heptahydrate per liter of stock. The YAML emits those as `180`, `450`, `22`, `5`, `3`, `3`, and `1 G_PER_L` final-medium rows. | `data/normalized_yaml/archaea/TOGO_M2600_Pyrobaculum_Medium.yaml` |
| Major | Main and stock distilled water were merged into one nonsensical top-level concentration. | The source has 1000 ml water in the main medium and 1000 ml water inside the Allen's stock; the YAML records one `Distilled water` ingredient at `2000.0 G_PER_L` with a duplicate-merge note. | `data/normalized_yaml/archaea/TOGO_M2600_Pyrobaculum_Medium.yaml` |
| Major | Exact DSMZ main-ingredient amounts and preparation steps are missing. | DSMZ 390 specifies 0.50 g Trypticase peptone, 0.20 g yeast extract, 2.00 g sodium thiosulfate pentahydrate, pH 6.0, and the anaerobic preparation workflow. The YAML defaults those three ingredients to `VARIABLE`, omits pH, and has no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M2600_Pyrobaculum_Medium.yaml` |
| Major | Same-source DSMZ 390 records are not reconciled. | The ignored-file-inclusive source search found direct DSMZ 390, TOGO M2600, TOGO M2470, and KOMODO 390 records. M2600 currently stands alone because its water, stock rows, and variable defaults no longer match the direct owner. | `data/normalized_yaml/archaea/TOGO_M2600_Pyrobaculum_Medium.yaml`; DSMZ 390 duplicate-link curation |
| Minor | Some CHEBI cross-links are stale after primary term repair. | `MgSO4 x 7 H2O` has primary `term.id: CHEBI:31795` but `mediaingredientmech_chebi_term.id: CHEBI:32599`, and `VOSO4 x 2 H2O` still uses the legacy `mediaingredientmech_term` slot. | `data/normalized_yaml/archaea/TOGO_M2600_Pyrobaculum_Medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/archaea/TOGO_M2600_Pyrobaculum_Medium.yaml`, rehydrate `Allen's trace element solution` as a 10 ml stock addition with the seven trace salts and 1000 ml distilled water inside the stock, preserving the stock's pH 2 HCl adjustment.

2. Restore the DSMZ 390 exact amounts for Trypticase peptone, yeast extract, and sodium thiosulfate pentahydrate; keep the main 1000 ml water separate from the stock 1000 ml water.

3. Add `ph_value: 6.0` and the DSMZ/TOGO preparation comments as structured preparation steps.

4. Refresh the magnesium sulfate heptahydrate MediaIngredientMech CHEBI link and migrate the vanadyl sulfate dihydrate link off the legacy `mediaingredientmech_term` field.

5. Reconcile TOGO M2600 with the direct DSMZ 390 owner and the existing TOGO M2470 projection while preserving true DSMZ/KOMODO strain variants as variants rather than source duplicates.

## Follow-up Checks

- Re-run the focused schema, strict, reference, and term validators on the repaired TOGO owner and regenerated merged YAML.
- Re-run an ignored-file-inclusive exact search for `TOGO:M2600`, `TOGO:M2470`, `DSMZ_Medium390`, and `mediadive.medium:390` across `data/normalized_yaml` and `data/merge_yaml/merged` to confirm true duplicates and strain variants are separated.
- Manually compare the regenerated YAML against live TOGO M2600, live MediaDive 390, and `DSMZ_Medium390.pdf` to confirm the Allen's stock boundary, water rows, pH, and DSMZ main-ingredient amounts are correct.

## Additional Notes

The direct DSMZ/MediaDive 390 owner already has the exact main-solution gram amounts and the correct `COMPLEX`/`UNDEFINED` type flags, but it also lacks an explicit Allen's stock boundary. The TOGO M2600 repair should therefore copy DSMZ values where TOGO is lossy while still preserving TOGO's explicit stock group rather than only matching the direct flattened DSMZ owner.
