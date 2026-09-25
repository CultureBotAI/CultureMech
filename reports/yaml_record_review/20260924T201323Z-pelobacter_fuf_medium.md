# YAML Record Review: pelobacter_fuf_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/pelobacter_fuf_medium.yaml`
- Started UTC: 2026-09-24T20:13:23Z
- Finished UTC: 2026-09-24T20:13:23Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pelobacter_fuf_medium.yaml`, a generated `MediaRecipe` merge record.

- ID: `CultureMech:001417`
- Label: `pelobacter_fuf_medium`
- Category: `bacterial`
- Source term: `mediadive.medium:318a`
- Source name: DSMZ Medium 318a, PELOBACTER (FUF) MEDIUM
- Physical state: `LIQUID`
- Maintained owner: `data/normalized_yaml/bacterial/pelobacter_fuf_medium.yaml`
- Generated from: `pelobacter_fuf_medium`

## Validation

- Passed: open LinkML validation of `data/merge_yaml/merged/pelobacter_fuf_medium.yaml` against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`; no issues found.
- Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pelobacter_fuf_medium.yaml --out /private/tmp/pelobacter_fuf_medium.strict.tsv --workers 1 --quiet`; the TSV contained only its header, so strict validation found 0 errors.
- Passed: focused `linkml-reference-validator validate data data/merge_yaml/merged/pelobacter_fuf_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 0 references were checked.
- Passed: focused `linkml-term-validator validate-data data/merge_yaml/merged/pelobacter_fuf_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
- Not checked: embedded `curation_history`; the documented `just validate-history` target validates standalone `history/` YAML rather than `MediaRecipe.curation_history` embedded in generated records.

## Identity and Grounding

`mediadive.medium:318a` resolves to DSMZ Medium 318a, PELOBACTER (FUF) MEDIUM, with source `DSMZ`, final volume 1011 ml, pH range 7.0 to 7.2, a Trace element solution, and Wolin's vitamin solution (10x). The DSMZ 318a PDF confirms the same identity and formulation.

The record's medium identity, category, liquid physical state, defined/defined medium typing, pH range, and main-medium identity are supported. Most simple chemical groundings are plausible at the compound level, but the stock-solution boundaries are lost, so many grounded chemicals sit at the wrong concentration and the wrong recipe scope.

## Evidence

- DSMZ 318a and MediaDive 318a list the final medium as HEPES, KH2PO4, NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, 10 ml Trace element solution, NH4Cl, 0.5 ml Sodium resazurin stock, 2-Furoic acid, 1 ml Wolin's vitamin solution (10x), L-Cysteine HCl x H2O, Na2S x 9 H2O, and 1000 ml Distilled water.
- The Trace element solution is a 1000 ml stock that contains NTA, FeCl2 x 4 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, NaCl, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and Distilled water.
- Wolin's vitamin solution (10x) is a 1000 ml stock that contains mg/L vitamin amounts and Distilled water.
- The generated record has no `solutions` block. It emits every Trace element and Wolin vitamin component as a direct final-medium `ingredient` at the stock concentration, omits the 10 ml and 1 ml stock-addition rows, omits Distilled water, and sums final NaCl/CaCl2 with stock NaCl/CaCl2.

## Completeness

The generated record is materially incomplete because it lacks the stock-solution structure required to interpret the DSMZ recipe. Without a `solutions` entry for 10 ml Trace element solution and 1 ml Wolin's vitamin solution (10x), the record cannot distinguish final-medium NaCl and CaCl2 from stock-solution NaCl and CaCl2, and it represents trace metals and vitamins at concentrations that are orders of magnitude too high for the final 1011 ml medium.

Empty optional fields are not defects.

An ignored-inclusive exact search of `data`, `src`, and `scripts` for `mediadive.medium:318a`, `CultureMech:001417`, `DSMZ_Medium318a`, and `pelobacter_fuf_medium` found only this maintained owner and its generated merge record for `CultureMech:001417`. A second normalized KOMODO-derived `data/normalized_yaml/bacterial/fuf_medium.yaml` mentions `DSMZ Medium: 318a` in `notes`, but has a different FUF MEDIUM formulation and is not merged into this generated target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | DSMZ stock recipes are flattened into final-medium ingredients at stock strength. | DSMZ 318a adds 10 ml Trace element solution and 1 ml Wolin's vitamin solution (10x) to the final medium. The generated record has no stock-addition rows and lists all trace elements plus vitamins as direct `G_PER_L` ingredients. | `data/normalized_yaml/bacterial/pelobacter_fuf_medium.yaml` |
| Major | Duplicate `NaCl` and `CaCl2 x 2 H2O` rows were summed across incompatible scopes. | The generated record stores `NaCl` as 1.593472 g/L from `0.593472` final-medium g/L plus `1.0` stock g/L, and `CaCl2 x 2 H2O` as 0.1791296 g/L from `0.0791296` final-medium g/L plus `0.1` stock g/L. DSMZ scopes the first amount to the final 1011 ml medium and the second to the 1000 ml Trace element solution. | `data/normalized_yaml/bacterial/pelobacter_fuf_medium.yaml` |
| Major | Distilled water and the Trace element preparation are not represented with the right scope. | DSMZ 318a has 1000 ml Distilled water in the final medium and 1000 ml Distilled water in each of the Trace element and Wolin vitamin stocks. The generated record omits all water rows and turns the Trace element stock's pH 6.5 preparation into a top-level final-medium `ADJUST_PH` step. | `data/normalized_yaml/bacterial/pelobacter_fuf_medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/pelobacter_fuf_medium.yaml`, keep the HEPES, KH2PO4, NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, NH4Cl, Sodium resazurin, 2-Furoic acid, L-Cysteine HCl x H2O, Na2S x 9 H2O, and final Distilled water rows as final-medium `ingredients`.
2. Add a 10 ml/L `Trace element solution` entry under `solutions`, move NTA and the trace salts into that solution at the DSMZ stock concentrations, and keep the NTA/pH 6.5 preparation text scoped to that stock solution rather than the final medium.
3. Add a 1 ml/L `Wolin's vitamin solution (10x)` entry under `solutions`, move Biotin through `(DL)-alpha-Lipoic acid` into that solution at the DSMZ stock concentrations, and include the stock's 1000 ml water.
4. Remove the summed cross-scope duplicate concentrations for `NaCl` and `CaCl2 x 2 H2O`; the final-medium rows and Trace element stock rows must remain separate.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on `data/normalized_yaml/bacterial/pelobacter_fuf_medium.yaml`, then regenerate `data/merge_yaml/merged/pelobacter_fuf_medium.yaml` and rerun the same focused validators on the generated record.
- Manually compare the regenerated final medium and both stock solutions against the DSMZ 318a PDF and the MediaDive 318a REST record.
- Review `data/normalized_yaml/bacterial/fuf_medium.yaml` separately for the `DSMZ Medium: 318a` note found by the ignored-inclusive exact search; it appears to be a different KOMODO-derived FUF record and should not be silently merged into this target.

## Additional Notes

The local reports already contain useful leads for this record: `data/import_tracking/reports/merged_duplicates.tsv` flags the cross-scope `NaCl` and `CaCl2 x 2 H2O` sums, and `data/import_tracking/reports/concentration_plausibility.tsv` flags stock-magnitude trace and vitamin concentrations.
