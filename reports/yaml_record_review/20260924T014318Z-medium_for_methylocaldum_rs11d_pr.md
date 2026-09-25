# YAML Record Review: medium_for_methylocaldum_rs11d_pr

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_methylocaldum_rs11d_pr.yaml
- Started UTC: 2026-09-24T01:42:09Z
- Finished UTC: 2026-09-24T01:43:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/medium_for_methylocaldum_rs11d_pr.yaml` |
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:001044` |
| Label | `medium_for_methylocaldum_rs11d_pr` |
| Original name | `MEDIUM FOR METHYLOCALDUM (RS11D-PR)` |
| Category | `bacterial` |
| Source accession | `mediadive.medium:1568` |
| Maintained owner | `data/normalized_yaml/bacterial/medium_for_methylocaldum_rs11d_pr.yaml` |
| Generated status | Generated merge from one normalized MediaDive import, with `merge_fingerprint` `1728163491f51776d7f04813e5b213bbf5c86937750094f301ced4e0e33302b9` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_methylocaldum_rs11d_pr.yaml` | Passed: no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_methylocaldum_rs11d_pr.yaml --out /private/tmp/medium_for_methylocaldum_rs11d_pr.strict.tsv --workers 1 --quiet` | Passed. The TSV had 1 line, so it contained only the header and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_methylocaldum_rs11d_pr.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_methylocaldum_rs11d_pr.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

- The record identity agrees with the inspected MediaDive API payload for medium `1568`: source `DSMZ`, name `MEDIUM FOR METHYLOCALDUM (RS11D-PR)`, `complex_medium` `no`, pH 7.0, and the DSMZ Medium 1568 link are all preserved by the YAML.
- The generated record is a direct copy of `data/normalized_yaml/bacterial/medium_for_methylocaldum_rs11d_pr.yaml` plus the generated merge event, `merge_fingerprint`, and `merged_from` fields.
- An exact, gitignore-independent search that included ignored and hidden files for `mediadive.medium:1568`, `DSMZ_Medium1568`, `MEDIUM FOR METHYLOCALDUM (RS11D-PR)`, and `medium_for_methylocaldum_rs11d_pr` found the generated record and its direct normalized owner as the only record copies.
- The record does not conflate `data/normalized_yaml/bacterial/methylocaldum_marinum_medium.yaml`; that neighboring file is DSMZ Medium 1501, not MediaDive/DSMZ Medium 1568.

## Evidence

Supported claims:

- Source identity, source accession, original label, defined-medium status, bacterial category, liquid default, and pH 7.0 are consistent with the MediaDive medium object for ID 1568.
- The first six direct final-medium ingredients preserve the main solution in source order and at the right amounts: NaNO3 1 g/l, MgSO4 x 7 H2O 0.1 g/l, Na2HPO4 0.5 g/l, KH2PO4 0.22 g/l, CaCl2 x 2 H2O 0.03 g/l, and FeSO4 x 7 H2O 0.002 g/l.
- The two preparation steps preserve the source instructions to adjust the medium to pH 7.0 with NaOH, then dispense it into growth vessels and, for sealed vessels, add 20% methane to the gas phase before autoclaving at 121 C for 15 minutes.

Unsupported or over-scoped claims:

- The generated YAML treats the `Trace elements` stock recipe as direct final-medium ingredients. In MediaDive, the main solution adds `Trace elements`, `solution_id` `3251`, at 1 ml/l; ZnSO4 x 7 H2O, CuSO4 x 5 H2O, MnSO4 x 2 H2O, Na2MoO4, H3BO3, and CoCl2 x 6 H2O are the composition of that 1 l stock, not final-medium masses per liter.
- The NaNO3 ingredient still has a legacy `mediaingredientmech_term` entry even though the record also grounds the ingredient itself to exact `CHEBI:63005` sodium nitrate and the later curation history says legacy links were refreshed to CHEBI keying.

## Completeness

- The record is incomplete for solutions because it drops the MediaDive stock boundary for `Trace elements`. A faithful record should keep the 1 ml/l solution addition instead of multiplying the stock constituents into direct final-medium grams per liter.
- `target_organisms`, growth evidence, publications, salinity, temperature, and storage fields are empty. That is acceptable for a direct MediaDive recipe import because the inspected MediaDive payload for medium 1568 supplies a formulation and preparation protocol, not organism-specific growth observations.
- No duplicate CultureMech record or sibling source record was found by the exact gitignore-independent identity search described above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Trace elements` was flattened from a 1 ml/l stock addition into six direct stock-strength final-medium ingredients. | The MediaDive main solution lists `solution: Trace elements`, `solution_id: 3251`, `amount: 1`, `unit: ml`; the separate `Trace elements` solution lists ZnSO4 x 7 H2O 0.44 g, CuSO4 x 5 H2O 0.2 g, MnSO4 x 2 H2O 0.17 g, Na2MoO4 0.06 g, H3BO3 0.1 g, and CoCl2 x 6 H2O 0.08 g in 1000 ml. The YAML lists those stock recipe quantities directly as `G_PER_L` ingredients. | `data/normalized_yaml/bacterial/medium_for_methylocaldum_rs11d_pr.yaml`; if more generated records share the stale MediaDive flattening shape, rerun or extend `src/culturemech/import/mediadive_importer.py` from the current MediaDive API cache and regenerate merges. |
| Minor | NaNO3 is the only ingredient still using the deprecated `mediaingredientmech_term` key. | NaNO3 has `term.id` `CHEBI:63005` but still stores `mediaingredientmech_term: MediaIngredientMech:000171`, while the other eleven ingredients use `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/medium_for_methylocaldum_rs11d_pr.yaml`, followed by the MediaIngredientMech enrichment or migration step. |

## Recommended Edits

1. Regenerate or repair `data/normalized_yaml/bacterial/medium_for_methylocaldum_rs11d_pr.yaml` from the MediaDive 1568 API payload so the main recipe contains only NaNO3, MgSO4 x 7 H2O, Na2HPO4, KH2PO4, CaCl2 x 2 H2O, and FeSO4 x 7 H2O as direct ingredients, plus a `solutions` entry for `mediadive.solution:3251` / `Trace elements` at 1 ml/l.
2. Keep the pH and the two preparation steps exactly scoped to the main solution: adjust to pH 7.0 with NaOH, then dispense into growth vessels and optionally add 20% methane to sealed vessels before autoclaving at 121 C for 15 minutes.
3. Refresh the NaNO3 MediaIngredientMech enrichment so it uses CHEBI keying like the rest of the record.
4. Regenerate `data/merge_yaml/merged/medium_for_methylocaldum_rs11d_pr.yaml` from the normalized record and rebuild any derived browser or page products.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the normalized owner and regenerated merge.
- Inspect the regenerated YAML and verify that it has no direct ZnSO4 x 7 H2O, CuSO4 x 5 H2O, MnSO4 x 2 H2O, Na2MoO4, H3BO3, or CoCl2 x 6 H2O final-medium ingredient rows for this record.
- Verify that the regenerated record resolves and preserves a `Trace elements` solution reference to `mediadive.solution:3251` at 1 ml/l.
- Run `git diff --check` and read the YAML diff to ensure the only semantic changes are the MediaDive stock-boundary repair, the NaNO3 enrichment refresh, and regenerated merge metadata.

## Additional Notes

- This review did not patch generated YAML or attempt to rerun the MediaDive import. The review artifact records the defect and the maintained owner for a later curation pass.
- Water rows in the MediaDive main and stock solutions were not flagged. They set recipe volumes and do not need direct final-medium ingredient rows.
