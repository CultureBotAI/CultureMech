# YAML Record Review: ARCHAEOGLOBUS VENEFICUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml
- Started UTC: 2026-09-21T14:27:21Z
- Finished UTC: 2026-09-21T14:31:11Z
- Verdict: needs curation

## Target

- Reviewed generated `MediaRecipe` `CultureMech:001940` for `ARCHAEOGLOBUS VENEFICUS MEDIUM`.
- Immediate source: DSMZ/MediaDive medium `796`, represented as `mediadive.medium:796`.
- Maintained owner: `data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml`.
- Generated status: `data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml` was produced from one source recipe, `archaeoglobus_veneficus_medium`, with `merge_fingerprint: 884ff4f1466b6345a733b3760139ea9c5f46c6285b3e4a208348ee695e5ebd0e`.
- Nearby duplicate lead: exact ignored-inclusive searches found a separate KOMODO record for the same DSMZ accession at `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml` | Passed: `No issues found`. |
| Strict schema layer with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml --out /private/tmp/archaeoglobus_veneficus_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows. |
| References with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Terms with `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only output before `Validation passed` was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone history paths; no narrower embedded-history validator is exposed for one merged recipe. |

## Identity and Grounding

The reviewed file's stable ID, `name`, `original_name`, `category: archaea`, `media_term`, and DSMZ URL all identify DSMZ Medium 796, `ARCHAEOGLOBUS VENEFICUS MEDIUM`. The extracted DSMZ PDF at `/private/tmp/dsmz_796.txt` confirms pH 7.0, the same final-medium salts and anoxic 80% N2 / 20% CO2 plus post-inoculation H2 / CO2 preparation.

The generated merge is stale relative to its normalized owner. `data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml` has an `apply_cocktail_nesting.py` event dated 2026-08-07 and one `solutions` entry for four trace-stock components; `data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml` was generated on 2026-08-06, has no `solutions`, and still carries those four components as top-level ingredients.

The normalized stock nesting is itself incomplete. DSMZ 796 adds a single 1 ml `Trace element solution` to the medium, then prints a separate 1000 ml trace stock containing 13 salts plus water and pH adjustment to 1.0 with HCl. Only four of those salts were moved into the normalized `solutions` entry; NaCl and CaCl2 x 2 H2O were summed with final-medium salts, and `(NH4)2Ni(SO4)2`, CuSO4 x 5 H2O, H3BO3, AlK(SO4)2 x 12 H2O, Na2MoO4 x 2 H2O, Na2WO4 x 2 H2O, and Na2SeO3 x 5 H2O remain as direct final-medium ingredients at stock strength.

## Evidence

- The DSMZ 796 PDF was fetched and extracted locally. Its final recipe lists 1 ml `Trace element solution`, 2 ml 0.1% w/v ferrous ammonium sulfate, 0.5 ml 0.1% w/v sodium resazurin, final-medium NaCl/CaCl2 amounts of 18.00 g and 0.14 g, and a 1000 ml final water row.
- The same DSMZ PDF then lists the trace element stock separately with MnCl2 x 4 H2O, NaCl, `(NH4)2Ni(SO4)2`, FeSO4 x 7 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, H3BO3, AlK(SO4)2 x 12 H2O, Na2MoO4 x 2 H2O, Na2WO4 x 2 H2O, Na2SeO3 x 5 H2O, water, and pH 1.0 adjustment with HCl.
- The target already uses the explicit-volume arithmetic for final medium rows: 18 g NaCl in 1003 ml becomes 17.9462 G_PER_L. Summing the trace stock's 10 g/L NaCl instead of adding it at 1 ml/liter inflates that value to 27.9462 G_PER_L; preserving the stock dilution would contribute about 0.009970 G_PER_L NaCl.
- The maintained stock recipe `data/normalized_yaml/bacterial/trace_element_solution_medium_796.yaml`, `CultureMech:004324`, already represents all DSMZ trace stock chemicals plus HCl and water from KOMODO Medium 2051.
- `data/import_tracking/reports/merged_duplicates.tsv` already flags NaCl and CaCl2 x 2 H2O in `archaeoglobus_veneficus_medium.yaml` and in the KOMODO duplicate as `DIFFERING_PARTS` rows.

## Completeness

- Consequentially incomplete: the generated merge has no `solutions` entry for the trace stock and was not regenerated after the normalized owner gained partial trace-stock nesting.
- Consequentially incomplete: the normalized owner only nested four of the 13 trace-stock salts and does not point at the existing complete `trace_element_solution_medium_796` record.
- Consequentially incomplete: a duplicate KOMODO record for Medium 796 is present as `archeoglobus_veneficus_medium`, but the misspelled source label prevented it from merging with `ARCHAEOGLOBUS VENEFICUS MEDIUM`.
- Correctly empty: `target_organisms` is absent. DSMZ Medium 796 is a medium formulation sheet, not a primary growth record for a specific isolate.
- Correctly empty: literature `references`, `source_data`, and external `sources` are absent from this DSMZ import; the source URL is carried in `notes`.
- Bounded searches: exact `rg --no-ignore --hidden` searches over `data`, `reports`, and import-tracking outputs found the canonical DSMZ owner, the KOMODO duplicate, registry/catalog rows, manifest rows, and existing duplicate reports. An exact `rg --no-ignore --hidden` search under the ignored `reports/yaml_record_review/` directory found no prior report for `ARCHAEOGLOBUS_VENEFICUS_MEDIUM`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated merge is stale and re-flattens the four trace-stock salts that the normalized owner already nested. | The generated file has no `solutions` key and lists MnCl2 x 4 H2O, FeSO4 x 7 H2O, CoCl2 x 6 H2O, and ZnSO4 x 7 H2O as direct ingredients. The normalized owner has a later `NESTED_FLATTENED_COCKTAIL` event and a partial `Trace element solution` with those four salts at 1 ML_PER_L. | Regenerate `data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml` from `data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml`. |
| major | The normalized owner still flattens seven trace-stock-only salts as final-medium G_PER_L rows. | DSMZ prints `(NH4)2Ni(SO4)2`, CuSO4 x 5 H2O, H3BO3, AlK(SO4)2 x 12 H2O, Na2MoO4 x 2 H2O, Na2WO4 x 2 H2O, and Na2SeO3 x 5 H2O inside the 1000 ml trace element stock, not in the final recipe. At 1 ml/liter, the 2 G_PER_L stock nickel row should contribute about 0.001994 G_PER_L, not 2 G_PER_L. | `data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml` and the cocktail-nesting/source import rule that decides stock boundaries. |
| major | NaCl and CaCl2 x 2 H2O are duplicate-summed across the final medium and trace stock. | The source has 18 g final NaCl plus 10 g/L NaCl inside a 1 ml stock, but the record says `27.9462 G_PER_L` with `[Merged 2 duplicates: 17.9462, 10.0]`. The source has 0.14 g final CaCl2 x 2 H2O plus 1 g/L CaCl2 x 2 H2O inside the same stock, but the record says `1.139581 G_PER_L`. | `data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml` and the duplicate-ingredient cleanup that sums same-named rows before stock boundaries are preserved. |
| major | The KOMODO source duplicate for the same DSMZ 796 formulation was not merged with the DSMZ owner. | Exact searches found `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml` with `komodo.medium:796`, a note tying it to `mediadive.medium:796`, and the same misspelled `ARCHEOGLOBUS VENEFICUS MEDIUM` label. The uppercase generated target only lists `archaeoglobus_veneficus_medium` in `merged_from`. | `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml` and the merge synonym/fingerprint rules. |
| major | The KOMODO duplicate conflicts with the source on atmosphere and procedural context. | The KOMODO duplicate notes `Aerobic: Yes` and omits `preparation_steps`; DSMZ 796 is explicitly made anoxic with 80% N2 / 20% CO2, receives sulfite, acetate, and sulfide from sterile anoxic stocks, and is pressurized after inoculation with sterile 80% H2 / 20% CO2. | `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml` and the KOMODO DSMZ-enrichment path. |
| minor | The trace-stock ammonium nickel formula needs exact-form preservation when the row is moved. | DSMZ 796 prints `(NH4)2Ni(SO4)2` without a hydrate suffix, while KOMODO 2051 and some MIM labels also use `(NH4)2Ni(SO4)2 x 6 H2O`. The current row keeps the DSMZ preferred term but labels the CHEBI term `ammonium nickel sulfate hexahydrate`. | The normalized trace-stock representation, whichever of inline `solutions` or `data/normalized_yaml/bacterial/trace_element_solution_medium_796.yaml` becomes authoritative for this DSMZ stock. |

## Recommended Edits

1. In `data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml`, finish moving every trace stock component out of top-level `ingredients`: preserve the final NaCl and CaCl2 rows, undo the duplicate sums, and put all 13 DSMZ trace stock salts in the `Trace element solution`.
2. Either reference or reconcile `data/normalized_yaml/bacterial/trace_element_solution_medium_796.yaml` so this medium reuses the complete stock with its water and HCl pH-adjustment context instead of an inline four-ingredient fragment.
3. Harden cocktail nesting or duplicate cleanup so repeated names are not summed across final-medium and stock-solution boundaries.
4. Repair `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml` so its misspelled KOMODO duplicate is either merged with the DSMZ record or explicitly linked as the same DSMZ 796 formulation, and remove or qualify `Aerobic: Yes`.
5. Regenerate `data/merge_yaml/merged/ARCHAEOGLOBUS_VENEFICUS_MEDIUM.yaml` after the normalized repairs; do not patch this derived file directly.
6. Preserve the exact `(NH4)2Ni(SO4)2` versus `(NH4)2Ni(SO4)2 x 6 H2O` source form in the stock solution rather than letting one label silently stand for both hydrate states.

## Follow-up Checks

- Rerun the focused LinkML, strict, reference, and term validators on `data/normalized_yaml/archaea/archaeoglobus_veneficus_medium.yaml`, `data/normalized_yaml/bacterial/archeoglobus_veneficus_medium.yaml`, any edited stock solution, and the regenerated uppercase merge.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regenerating the merge because the target under review is derived.
- Recheck `data/import_tracking/reports/merged_duplicates.tsv`; `CultureMech:001940` should no longer report `DIFFERING_PARTS` for NaCl or CaCl2 x 2 H2O.
- Confirm the regenerated record has 12 direct non-water final-medium ingredients plus one complete trace stock added at 1 ML_PER_L.
- Manually compare the regenerated preparation text with DSMZ 796 to verify that final-medium anoxic preparation, trace-stock pH 1.0 adjustment, and post-inoculation H2/CO2 pressurization remain in the correct contexts.

## Additional Notes

- The final ferrous ammonium sulfate and sodium resazurin rows are explicit 0.1% w/v final recipe additions, not part of the trace stock flattening defect.
- The normalized owner already fixed four obvious trace-stock rows; this review should be read as a request to finish that partial repair and then regenerate the stale merge artifact.
