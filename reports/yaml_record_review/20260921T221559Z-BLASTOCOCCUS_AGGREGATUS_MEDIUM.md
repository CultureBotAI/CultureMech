# YAML Record Review: blastococcus_aggregatus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml
- Started UTC: 2026-09-21T22:15:59Z
- Finished UTC: 2026-09-21T22:17:43Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:006077` |
| Name | `blastococcus_aggregatus_medium` |
| Original name | `BLASTOCOCCUS AGGREGATUS MEDIUM` |
| Source identity | `komodo.medium:596`, KOMODO Medium 596 |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| Merge fingerprint | `860a829af02682b64b54287e92430d338cca43409cd70789576b1e077e5a4466` |
| Merged from | `KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM`, `blastococcus_aggregatus_medium` |
| Maintained owners | `data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml`, `data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml` |
| Generated status | Derived merge product; future fixes belong in normalized source records or merge regeneration, not in this generated YAML. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml` | Passed, `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml --out /private/tmp/BLASTOCOCCUS_AGGREGATUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed with exit 0; the emitted TSV contained only the header row. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit 0 and no reference diagnostics. The generated record has no structured `references` to check. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a non-fatal `eutils` `pkg_resources` warning. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone files under `history/`. |

`just validate-schema`, `just validate-strict`, and `just validate-terms` were not used directly because the project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation starts. The no-project Python 3.11 commands above are the same focused checks run without installing the project dependency set.

## Identity and Grounding

- `CultureMech:006077`, `komodo.medium:596`, and `BLASTOCOCCUS AGGREGATUS MEDIUM` agree with the live KOMODO Medium 596 page.
- The KOMODO page reports ID `596`, the same medium name, pH `7.0`, `Is Complex: true`, `Is Aerobic: false`, and the DSMZ Medium 596 PDF as its instruction source.
- The generated source-duplicate link to `CultureMech:001723` is identity-correct: the ignored-file-inclusive exact search found `data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml` as the active `mediadive.medium:596` owner for the same DSMZ 596 recipe.
- The generated composition is stale. Both normalized owners now have a `Trace elements` solution at `1 ML_PER_L` containing `H3BO3`, `MnCl2 x 4 H2O`, and `FeSO4`; the generated merge still lists those three stock-strength salts as top-level final-medium ingredients.
- The maintained normalized records are still only partly nested. DSMZ Medium 596 lists `Na-tartrate`, `CuCl2 x 2 H2O`, `ZnCl2`, `CoCl2 x 6 H2O`, `Na2MoO4 x 2 H2O`, and `Distilled water` under the same `Trace elements` stock; the two active normalized records still leave those five salts at top level and omit the stock water row.

## Evidence

| Claim | Review |
|---|---|
| KOMODO source identity | Supported by the live KOMODO page for Medium 596. |
| DSMZ duplicate identity | Supported by the KOMODO `Instructions` link and by the DSMZ Medium 596 PDF title. |
| Bulk formulation | Mostly supported: the generated record captures KNO3 0.5 g/L, Na-glycerophosphate 0.1 g/L, Tris HCl 1 g/L, Tryptone 2 g/L, and Yeast extract 2 g/L. |
| Artificial sea water amount | Incorrect unit in the generated and normalized records. DSMZ lists `999.00 ml` artificial sea water; the YAML stores `Sea water` as `999 G_PER_L`. |
| Trace elements | Incorrectly flattened. DSMZ lists a 1 ml/L `Trace elements` stock with eight salts in 1000 ml distilled water; the generated record flattens all eight salts as final g/L ingredients. |
| pH | Supported: DSMZ and KOMODO both state pH 7.0. |
| Preparation notes | Incomplete in the generated merge. The DSMZ owner has an artificial-sea-water preparation step, but the generated merge and KOMODO owner do not. |

## Completeness

- The generated record has no structured `references`, so the reference validator cannot dereference the KOMODO or DSMZ source pages.
- The generated merge has no `preparation_steps`, even though the DSMZ owner already stores the source note that artificial sea water is prepared from a marine aquarium salts mixture.
- The source does not specify strain-level growth evidence, incubation temperature, incubation duration, gas atmosphere beyond KOMODO's non-aerobic boolean, or storage conditions. Empty optional growth and storage fields are not defects.
- Exact ignored-file-inclusive searches for `CultureMech:006077`, `CultureMech:001723`, `komodo.medium:596`, `mediadive.medium:596`, `KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM`, and `blastococcus_aggregatus_medium` over `data/normalized_yaml`, `data/merge_yaml/merged`, the registry/catalog TSVs, `scripts`, `tests`, `reports/yaml_record_review`, and `history` found the two active normalized owners, their registry/catalog/by-source index rows, and the generated merge.
- No existing `*-BLASTOCOCCUS_AGGREGATUS_MEDIUM.md` report was found under ignored `reports/yaml_record_review/` before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner for a fix |
|---|---|---|---|
| Major | The generated merge is stale relative to the partial trace-element stock nesting in both normalized owners. | The generated file still lists `H3BO3`, `MnCl2 x 4 H2O`, and `FeSO4` as top-level ingredients. Both normalized owners now keep those rows inside a `Trace elements` solution added at `1 ML_PER_L`. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml` and `data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml`. |
| Major | The normalized owners still leave five DSMZ trace-stock salts as final-medium ingredients. | DSMZ Medium 596 places `Na-tartrate`, `CuCl2 x 2 H2O`, `ZnCl2`, `CoCl2 x 6 H2O`, and `Na2MoO4 x 2 H2O` under `Trace elements`; both active normalized files keep those five salts in top-level `ingredients` at stock concentrations. | Complete the `Trace elements` nesting in both normalized owner files, preserving the source-duplicate relationship. |
| Major | The trace-element stock omits distilled water. | DSMZ prepares the stock with `Distilled water 1000.00 ml`; neither active normalized owner carries that stock component under `solutions[].composition`. | Add `Distilled water` to the `Trace elements` solution composition in both normalized owner files. |
| Major | Artificial sea water uses a mass unit and a narrowed label. | DSMZ lists `Artificial sea water 999.00 ml`; the generated and normalized records store `preferred_term: Sea water`, `value: '999'`, `unit: G_PER_L`. | Change the row to artificial sea water at `999 ML_PER_L` in both normalized owner files. |
| Major | Source URLs and DSMZ preparation text are not preserved in the generated merge. | The generated record has no `references` and no `preparation_steps`; DSMZ is reachable through KOMODO and says artificial sea water is prepared from a marine aquarium salts mixture. | Add structured source references and the missing preparation note to normalized source records, then regenerate. |

## Recommended Edits

1. Complete `Trace elements` stock nesting in both normalized owners by moving the five remaining trace salts into `solutions[Trace elements].composition` and adding `Distilled water 1000 ML_PER_L`.
2. Correct `Artificial sea water` to `999 ML_PER_L` in both normalized owners.
3. Add structured references for KOMODO Medium 596 and DSMZ Medium 596 as appropriate on the two normalized owners.
4. Add the DSMZ artificial-sea-water preparation note to the KOMODO owner or adjust merge generation so the DSMZ duplicate's existing `preparation_steps` survive in the generated canonical merge.
5. Regenerate `data/merge_yaml/merged/` so `BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml` no longer carries stock-strength trace salts as final-medium ingredients.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validation on both normalized owner files and the regenerated merge.
- Rerun `just validate-media-variant-links` to verify the bidirectional `SOURCE_DUPLICATE` relationship between the KOMODO and DSMZ owners.
- Rerun `just verify-merges` and inspect `data/merge_yaml/merged/BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml` to confirm the trace-element stock is nested once, at `1 ML_PER_L`, with all eight salts plus stock water under the solution.
- Re-open the regenerated rendered page for Medium 596 and confirm it shows artificial sea water as 999 ml/L and does not render trace salts as g/L final-medium ingredients.

## Additional Notes

- This was a read-only review. I did not edit normalized YAML, generated merge YAML, generated pages, GitHub issues, or PR state.
- The exact ignored-file-inclusive search of `data/raw` and `data/import_tracking` for exact BLASTOCOCCUS/KOMODO/DSMZ Medium 596 strings found the generated deep-research priority report entry, but no local raw capture more authoritative than the live KOMODO page and DSMZ PDF fetched for this review.
