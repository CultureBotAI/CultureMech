# YAML Record Review: ARCHEOGLOBUS VENEFICUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/archeoglobus_veneficus_medium.yaml
- Started UTC: 2026-09-21T14:31:30Z
- Finished UTC: 2026-09-21T14:33:24Z
- Verdict: needs curation

## Target

- Reviewed generated `MediaRecipe` `CultureMech:006506` for `ARCHEOGLOBUS VENEFICUS MEDIUM`.
- Immediate source: KOMODO medium `796`, represented as `komodo.medium:796`.
- Maintained owner: `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml`.
- Generated status: `data/merge_yaml/merged/archeoglobus_veneficus_medium.yaml` was produced from one source recipe, `archeoglobus_veneficus_medium`, with `merge_fingerprint: 394c953e63b2c317cb1d64196552d8d8284bcdc4ddeb080c2ad0b98e10c147d8`.
- Source-duplicate lead: the KOMODO page and the normalized `notes` both tie this misspelled record to DSMZ Medium 796, which already has `data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml` as a separate generated record.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archeoglobus_veneficus_medium.yaml` | Passed: `No issues found`. |
| Strict schema layer with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archeoglobus_veneficus_medium.yaml --out /private/tmp/archeoglobus_veneficus_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| References with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archeoglobus_veneficus_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Terms with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archeoglobus_veneficus_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only output before `Validation passed` was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone history paths; no narrower embedded-history validator is exposed for one merged recipe. |

## Identity and Grounding

`CultureMech:006506` identifies KOMODO Medium 796. The fetched KOMODO page names the medium `ARCHEOGLOBUS VENEFICUS MEDIUM`, reports pH 7.0 with HCl, marks the medium non-complex and aerobic, and links DSMZ Medium 796 as its instructions page. The source label is misspelled relative to DSMZ `ARCHAEOGLOBUS VENEFICUS MEDIUM`, and the record is filed as `category: bacterial` even though the DSMZ duplicate is maintained as an archaeal recipe.

The generated record is stale relative to its normalized owner. `data/merge_yaml/merged/archeoglobus_veneficus_medium.yaml` has no `solutions` section and still carries every trace-stock row as a top-level ingredient, but `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml` has an `apply_cocktail_nesting.py` event dated 2026-08-15 that moved four stock-strength rows into a partial `Trace element solution`.

The KOMODO page stores most trace-stock chemicals at diluted final-medium mass magnitudes, while DSMZ 796 prints the undiluted stock formulation after its final recipe. The generated record combines the wrong sides of those sources: it links to KOMODO Medium 796 but carries undiluted DSMZ trace-stock G_PER_L amounts as final ingredients.

## Evidence

- KOMODO Medium 796 was fetched to `/private/tmp/komodo_796.html`; it has ID `796`, the misspelled name `ARCHEOGLOBUS VENEFICUS MEDIUM`, `PH Info` of `7.0, HCl`, `Is Aerobic: true`, and an instructions link to DSMZ Medium 796.
- The fetched KOMODO metabolite table lists trace chemicals at final-medium magnitudes, for example `MnCl2 x 4 H2O` at `5.66E-3`, `(NH4)2Ni(SO4)2 x 6 H2O` at `1.95E-3`, and the 0.10 g/L stock salts at `9.76E-5`.
- DSMZ Medium 796 was extracted to `/private/tmp/dsmz_796.txt`. Its final recipe adds 1 ml of `Trace element solution` and then defines that stock separately with MnCl2 x 4 H2O, NaCl, `(NH4)2Ni(SO4)2`, FeSO4 x 7 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, H3BO3, AlK(SO4)2 x 12 H2O, Na2MoO4 x 2 H2O, Na2WO4 x 2 H2O, Na2SeO3 x 5 H2O, water, and pH 1.0 adjustment with HCl.
- `data/import_tracking/reports/merged_duplicates.tsv` already flags this normalized owner for NaCl and CaCl2 x 2 H2O `DIFFERING_PARTS` rows, reflecting the sum of final-medium and stock-solution entries.
- The maintained `data/normalized_yaml/bacterial/trace_element_solution_medium_796.yaml`, `CultureMech:004324`, already represents the complete KOMODO/DSMZ trace stock as a `record_kind: SOLUTION` recipe.

## Completeness

- Consequentially incomplete in the generated target: the file has no `solutions` entry even for the four trace-stock salts that were already nested upstream.
- Consequentially incomplete in the maintained owner: the partial `Trace element solution` has no asserted `concentration`, causing `reports/media_content_review_manifest.tsv` to flag `MISSING_SOLUTION_CONCENTRATION`.
- Consequentially incomplete in the maintained owner: seven trace-stock salts, NaCl, CaCl2 x 2 H2O, stock HCl, and stock water are still not attached to the trace stock with the right preparation boundary.
- Consequentially incomplete: the DSMZ preparation steps are absent, despite the upstream KOMODO page pointing at DSMZ Medium 796 for instructions.
- Correctly empty: `target_organisms` is absent. KOMODO and DSMZ Medium 796 are medium formulation records, not primary growth evidence for a specific strain.
- Correctly empty: literature `references` and `source_data` are absent; this generated copy only carries the KOMODO table and its DSMZ instruction link through `notes`.
- Bounded searches: an exact `rg --no-ignore --hidden` search over `data` and `reports` found this record's owner, registry/catalog rows, manifest row, import-tracking duplicate rows, and the prior uppercase DSMZ duplicate review. A `find` search under the ignored `reports/yaml_record_review/` directory found no existing filename for `archeoglobus_veneficus_medium.md`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge is stale and does not include the normalized owner's partial trace-stock nesting. | The generated target has no `solutions`. Its source owner has a 2026-08-15 `NESTED_FLATTENED_COCKTAIL` event that moved MnCl2 x 4 H2O, FeSO4 x 7 H2O, CoCl2 x 6 H2O, and ZnSO4 x 7 H2O into `solutions[0]`. | Regenerate `data/merge_yaml/merged/archeoglobus_veneficus_medium.yaml` from `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml`. |
| major | The trace element stock is still incompletely represented upstream. | DSMZ 796 and KOMODO Medium 796 both support final diluted trace amounts or a 1 ml stock addition. The normalized owner leaves `(NH4)2Ni(SO4)2`, CuSO4 x 5 H2O, H3BO3, AlK(SO4)2 x 12 H2O, Na2MoO4 x 2 H2O, Na2WO4 x 2 H2O, and Na2SeO3 x 5 H2O as direct stock-strength ingredients, and keeps the 1 ML_PER_L trace-stock addition only as a candidate. | `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml` and the KOMODO DSMZ-enrichment/cocktail-nesting path. |
| major | NaCl and CaCl2 x 2 H2O were summed across final-medium and trace-stock rows. | `data/import_tracking/reports/merged_duplicates.tsv` reports `17.9462;10.0` summed into `27.9462 G_PER_L` NaCl and `0.139581;1.0` summed into `1.139581 G_PER_L` CaCl2 x 2 H2O for this exact owner. DSMZ puts the 10 G_PER_L NaCl and 1 G_PER_L CaCl2 x 2 H2O rows inside a 1 ml/liter stock. | `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml` and duplicate cleanup before stock boundaries are preserved. |
| major | This KOMODO record is a misspelled, separately generated duplicate of DSMZ Medium 796. | The KOMODO page and record label say `ARCHEOGLOBUS`; `notes` link the record to `mediadive.medium:796`; an ignored-inclusive exact search also found the DSMZ owner `CultureMech:001940` for `ARCHAEOGLOBUS VENEFICUS MEDIUM`. Each generated file lists only one `merged_from` entry. | The KOMODO owner and merge synonym/fingerprint rules. |
| major | The record asserts aerobic context and omits source preparation for an anoxic archaeal medium. | The source KOMODO table says `Is Aerobic: true`, and the imported note preserves `Aerobic: Yes`. The DSMZ instructions linked from the same KOMODO page instead require sparging with 80% N2 and 20% CO2, dispensing under that atmosphere, adding sulfite/acetate/sulfide from sterile anoxic stocks, and post-inoculation pressurization with sterile 80% H2 and 20% CO2. | `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml` and the KOMODO DSMZ-enrichment path. |
| major | HCl is represented as a variable top-level final-medium ingredient even though the DSMZ HCl adjustment belongs to the trace stock. | The generated record has direct `HCl` with `unit: VARIABLE` and notes `pH adjustment`; DSMZ 796 only mentions HCl for adjusting the trace element solution to pH 1.0. The complete `trace_element_solution_medium_796` stock already carries HCl as a variable stock ingredient. | `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml`. |
| minor | The ammonium nickel stock formula needs exact-form reconciliation when the row is nested. | DSMZ 796 prints `(NH4)2Ni(SO4)2`; KOMODO 796 and KOMODO 2051 print `(NH4)2Ni(SO4)2 x 6 H2O`; the local MIM index maps both labels to `CHEBI:86149`. The current KOMODO row uses the anhydrous preferred label but the hexahydrate CHEBI label. | The normalized trace-stock representation used by this record. |

## Recommended Edits

1. Merge or explicitly mark `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml` as a source duplicate of `data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml` despite the KOMODO misspelling, then regenerate both merge outputs.
2. Finish moving the complete trace element stock into `solutions`, including NaCl, CaCl2 x 2 H2O, `(NH4)2Ni(SO4)2`, CuSO4 x 5 H2O, H3BO3, AlK(SO4)2 x 12 H2O, Na2MoO4 x 2 H2O, Na2WO4 x 2 H2O, Na2SeO3 x 5 H2O, HCl, and water.
3. Assert the 1 ML_PER_L trace element solution addition for this record, because both the KOMODO DSMZ link and the DSMZ 796 PDF identify the same recipe with that volume.
4. Undo the NaCl and CaCl2 x 2 H2O sums so direct ingredients hold only the final-medium salts, not stock-solution salts.
5. Remove the top-level variable HCl after HCl is scoped under `Trace element solution`, and copy or link the DSMZ anoxic preparation steps so `Aerobic: Yes` no longer stands as the only atmosphere claim.
6. Preserve the exact ammonium nickel hydrate string per source when reconciling this inline stock with `data/normalized_yaml/bacterial/trace_element_solution_medium_796.yaml`.

## Follow-up Checks

- Rerun the focused LinkML, strict, reference, and term validators on `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml`, `data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml`, `data/normalized_yaml/bacterial/trace_element_solution_medium_796.yaml`, and both regenerated merges.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regenerating the merge outputs.
- Recheck `reports/media_content_review_manifest.tsv`; this normalized owner should no longer show `MISSING_SOLUTION_CONCENTRATION` or `VARIABLE_CONCENTRATION` for the trace stock and HCl.
- Recheck `data/import_tracking/reports/merged_duplicates.tsv`; this owner should no longer report `DIFFERING_PARTS` for NaCl or CaCl2 x 2 H2O.
- Compare the regenerated KOMODO-derived record against both the KOMODO 796 page and the DSMZ 796 PDF to verify final trace concentrations, the 1 ML_PER_L trace stock addition, pH 7.0 final medium context, and pH 1.0 trace-stock context.

## Additional Notes

- The KOMODO source itself records diluted final-medium trace-metal masses; none of the undiluted 5.8, 2, 1, or 0.1 G_PER_L trace-stock rows should remain as top-level ingredients.
- Fe(NH4)2(SO4)2 x 6 H2O and Sodium resazurin are final-recipe 0.1% w/v additions in DSMZ 796, so they are not part of the trace element stock defect.
