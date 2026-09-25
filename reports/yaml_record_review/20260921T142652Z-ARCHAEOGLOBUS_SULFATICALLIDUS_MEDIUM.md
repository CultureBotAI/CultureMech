# YAML Record Review: ARCHAEOGLOBUS SULFATICALLIDUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.yaml
- Started UTC: 2026-09-21T14:23:40Z
- Finished UTC: 2026-09-21T14:27:09Z
- Verdict: needs curation

## Target

- Reviewed generated `MediaRecipe` `CultureMech:000741` for `ARCHAEOGLOBUS SULFATICALLIDUS MEDIUM`.
- Immediate source: DSMZ/MediaDive medium `1278`, exposed as `mediadive.medium:1278`.
- Maintained canonical owner: `data/normalized_yaml/archaea/archaeoglobus_sulfaticallidus_medium.yaml`.
- Merged duplicate owner: `data/normalized_yaml/bacterial/KOMODO_1278_HYL_medium.yaml`, `CultureMech:004031`, `komodo.medium:1278`.
- Generated status: `data/merge_yaml/merged/ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.yaml` is a merge product with `merge_fingerprint: 32c6f5a4a303523b80904fd9742d846d29516aeeaa23ad3144abaeb23829c352`; future fixes belong upstream.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.yaml` | Passed: `No issues found`. |
| Strict schema layer with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.yaml --out /private/tmp/archaeoglobus_sulfaticallidus_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| References with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Terms with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only output before `Validation passed` was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone history paths; no narrower embedded-history validator is exposed for one merged recipe. |

## Identity and Grounding

`CultureMech:000741`, the normalized archaeal owner, the generated merge record, `mediadive.medium:1278`, and the extracted DSMZ Medium 1278 PDF all identify the same Archaeoglobus sulfaticallidus medium. The `original_name`, source URL, `ph_value: 7.0`, liquid physical state, anoxic preparation text, and DSMZ 1278 accession agree.

The generated record is not, however, formulation-accurate. The DSMZ source lists a final medium that receives 10 ml of `Modified Wolin's mineral solution` and 1 ml of `Wolin's vitamin solution (10x)`. The record flattens both stock recipes into 22 top-level mineral and vitamin ingredients at their undiluted stock concentrations.

Ingredient grounding is mostly exact for the represented forms, but `NiCl2 x 6 H2O` is grounded to generic nickel dichloride (`CHEBI:34887`). The packaged MediaIngredientMech index has an exact `Nickel (II) chloride hexahydrate` mapping to `CHEBI:53542`, so the current hydrate grounding is weaker than the source formula.

## Evidence

- The DSMZ 1278 PDF was inspected from `/private/tmp/dsmz_1278.txt`; it contains the final recipe, the complete `Modified Wolin's mineral solution` recipe from medium 141, and the complete `Wolin's vitamin solution (10x)` recipe from medium 120.
- The top-level DSMZ rows for NaCl, Na2SO4, MgCl2 x 6 H2O, NH4Cl, KCl, CaCl2 x 2 H2O, KH2PO4, Na-DL-lactate, yeast extract, sodium resazurin, Na2CO3, and DL-dithiothreitol support the corresponding final-medium ingredients after the importer divides them by the 1011.5 ml explicit addition basis it already uses.
- The DSMZ stock rows for nitrilotriacetic acid through Na2WO4 x 2 H2O support `data/normalized_yaml/bacterial/mediadive_241_Modified_Wolin_s_mineral_solution.yaml`; they do not support those minerals as final-medium grams per liter.
- The DSMZ stock rows for biotin through `(DL)-alpha-Lipoic acid` support `data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml`; they do not support those vitamins as final-medium grams per liter.
- `data/import_tracking/reports/merged_duplicates.tsv` already flags both normalized parents for `NaCl` and `CaCl2 x 2 H2O` as `DIFFERING_PARTS`, and `data/import_tracking/reports/concentration_plausibility.tsv` flags both parents for the 0.1 G_PER_L pyridoxine stock concentration. These exact records are present even though `reports/media_content_review_manifest.tsv` marks both owners `PASS`.

## Completeness

- Consequentially incomplete: the generated recipe has no `solutions` entries for `mediadive.solution:241` or `mediadive.solution:5980`, even though both normalized solution recipes already exist.
- Consequentially incomplete: the final medium loses the water rows and preparation boundary for both stock solutions by flattening their compositions into `ingredients`.
- Consequentially incomplete in the KOMODO duplicate: `KOMODO_1278_HYL_medium.yaml` has no preparation steps and carries `Aerobic: Yes` in `notes`, which conflicts with DSMZ's 80% N2 / 20% CO2 anoxic sparging and sealed-vessel preparation.
- Correctly empty: the generated record has no `target_organisms`; DSMZ Medium 1278 is a formulation sheet, not primary growth evidence for a named strain.
- Correctly empty: the generated record has no `sources`, `source_data`, or external literature `references`; the imported DSMZ URL in `notes` is the only recipe source inspected for this review.
- Bounded searches: an exact `rg --no-ignore --hidden` search over `data`, `reports`, and import-tracking outputs found the canonical owner, KOMODO owner, registry/catalog rows, manifest rows, and existing duplicate/plausibility reports for this ID pair. An exact `rg --no-ignore --hidden` search under ignored `reports/yaml_record_review/` found no prior report for `ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM`. A `find data/normalized_yaml/bacterial -name archaeoglobus_sulfaticallidus_medium.yaml` search found no bacterial-path owner for the KOMODO back-reference.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The two Wolin stock solutions are flattened into final-medium ingredients at stock strength. `Nitrilotriacetic acid 1.5 G_PER_L`, `MgSO4 x 7 H2O 3 G_PER_L`, `Biotin 0.02 G_PER_L`, and `Pyridoxine hydrochloride 0.1 G_PER_L` are stock concentrations, not final concentrations after 10 ml/liter and 1 ml/liter additions. On the importer basis already used for final salts, the 10 ml mineral stock contributes a 0.009886 dilution and the 1 ml vitamin stock contributes a 0.000989 dilution. | DSMZ 1278 lists the final medium with `Modified Wolin's mineral solution 10.00 ml` and `Wolin's vitamin solution (10x) 1.00 ml`, then prints the two 1000 ml stock recipes separately. | `data/normalized_yaml/archaea/archaeoglobus_sulfaticallidus_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_1278_HYL_medium.yaml`, and the source importers that materialize DSMZ/KOMODO stock rows. |
| major | Flattening also corrupts duplicate arithmetic for NaCl and CaCl2 x 2 H2O. The record sums the final-medium NaCl and CaCl2 amounts with undiluted 1.0 G_PER_L and 0.1 G_PER_L mineral-stock rows instead of preserving a 10 ml stock addition or diluting those rows. | The generated record carries `[Merged 2 duplicates: 19.7824, 1.0]` for NaCl and `[Merged 2 duplicates: 0.138477, 0.1]` for CaCl2 x 2 H2O; `merged_duplicates.tsv` independently reports both as `DIFFERING_PARTS` in both normalized parents. | The same two normalized parents and the duplicate-ingredient cleanup that sums repeated names inside one imported recipe. |
| major | The KOMODO source duplicate contradicts the DSMZ protocol and loses the anoxic preparation while being merged as a same-signature source duplicate. | `KOMODO_1278_HYL_medium.yaml` says `DSMZ Medium: 1278` and `Aerobic: Yes`, has no `preparation_steps`, and was imported with the same flattened ingredient signature as the DSMZ owner. DSMZ 1278 instead sparges with an 80% N2 / 20% CO2 gas mixture, dispenses under the same gas phase, autoclaves sealed vessels, and adds carbonate, vitamins, and dithiothreitol from sterile anoxic stocks. | `data/normalized_yaml/bacterial/KOMODO_1278_HYL_medium.yaml` and the KOMODO DSMZ-enrichment path. |
| major | `NiCl2 x 6 H2O` is hydrated nickel chloride but is grounded to generic `CHEBI:34887` nickel dichloride. | The source formula contains six waters. The local MediaIngredientMech label index maps `NiCl2 x 6 H2O` to `CHEBI:53542` as `Nickel (II) chloride hexahydrate`, while the generated row uses `CHEBI:34887`. | The normalized stock-solution ingredient or ingredient-grounding rule used when flattening `mediadive.solution:241`. |
| minor | The KOMODO back-reference points at a non-existent bacterial-path copy of the MediaDive recipe. | `KOMODO_1278_HYL_medium.yaml` has `variant_children[0].path: data/normalized_yaml/bacterial/archaeoglobus_sulfaticallidus_medium.yaml`; the only current owner found by `find data/normalized_yaml -name archaeoglobus_sulfaticallidus_medium.yaml` is `data/normalized_yaml/archaea/archaeoglobus_sulfaticallidus_medium.yaml`. | `data/normalized_yaml/bacterial/KOMODO_1278_HYL_medium.yaml` or the merge backlink generator. |
| minor | `Calcium D-(+)-pantothenate` has a CHEBI term but no `mediaingredientmech_chebi_term`. | The generated row maps it to `CHEBI:31345` and the local MIM label index has a unique `Calcium D-(+)-pantothenate` synonym for `CHEBI:31345`, but this ingredient is the only missing MIM link in the manifest's 34/35 MIM count for both normalized parents. | The same two normalized parents after the solution/flattening decision is corrected. |

## Recommended Edits

1. In the two normalized parent records, remove the flattened `Modified Wolin's mineral solution` children from top-level `ingredients` and add a `solutions` descriptor for `mediadive.solution:241` at the 10 ml DSMZ amount.
2. In the same parents, remove the flattened `Wolin's vitamin solution (10x)` children from top-level `ingredients` and add a `solutions` descriptor for `mediadive.solution:5980` at the 1 ml DSMZ amount.
3. Stop the duplicate-ingredient cleanup from summing a final-medium row with an undiluted same-named stock child when the upstream recipe had a stock boundary.
4. Correct or regenerate the KOMODO duplicate so `Aerobic: Yes` is not asserted for DSMZ Medium 1278 and the DSMZ anoxic preparation is not lost.
5. Reground `NiCl2 x 6 H2O` to the exact CHEBI hexahydrate term where this stock solution is normalized, then allow the parent media to inherit that corrected stock composition.
6. Regenerate merge backlinks so the KOMODO `variant_children.path` points to `data/normalized_yaml/archaea/archaeoglobus_sulfaticallidus_medium.yaml`.
7. After the stock-boundary repair, rerun MIM enrichment for any remaining direct `Calcium D-(+)-pantothenate` row or confirm that the row exists only inside `Wolin's vitamin solution (10x)`.

## Follow-up Checks

- Rerun the focused LinkML, strict, reference, and term validators on both normalized parents and on regenerated `data/merge_yaml/merged/ARCHAEOGLOBUS_SULFATICALLIDUS_MEDIUM.yaml`.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regenerating the merge, because the target under review is derived.
- Rerun `just validate-media-variant-links` or the narrowest backlink validator after correcting `variant_children`.
- Recheck `data/import_tracking/reports/merged_duplicates.tsv` for `CultureMech:000741` and `CultureMech:004031`; neither parent should still show NaCl or CaCl2 x 2 H2O as `DIFFERING_PARTS` caused by a stock row.
- Manually compare the regenerated merge against DSMZ 1278 and confirm that the only direct final-medium ingredients are the explicit DSMZ final rows, while `Modified Wolin's mineral solution` and `Wolin's vitamin solution (10x)` remain stock references.

## Additional Notes

- `data/import_tracking/reports/concentration_plausibility.tsv` flags only pyridoxine in these two parents, but the same unit/stock-boundary problem affects every vitamin row and every Modified Wolin mineral row that was flattened.
- Sodium resazurin is a separate 0.1% w/v stock row in the final DSMZ ingredient list. Its calculated final mass is plausible on the importer's 1011.5 ml basis; it should not be grouped with the two named Wolin stock recipes above.
- The MediaDive normalized owner retains the DSMZ preparation prose. The main procedural loss is that the stock-solution pH adjustment prose is stored as an unscoped top-level `ADJUST_PH` step because the stock itself is missing from `solutions`.
