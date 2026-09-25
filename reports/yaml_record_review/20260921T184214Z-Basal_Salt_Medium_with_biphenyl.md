# YAML Record Review: Basal Salt Medium with biphenyl

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml`
- Started UTC: 2026-09-21T18:41:15Z
- Finished UTC: 2026-09-21T18:42:14Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:008625` |
| Merged record | `data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml` |
| Source identity | TOGO `M2036` / NBRC `M1333` |
| Merge status | Generated from one normalized source, `basal_salt_medium_with_biphenyl` |

The reviewed record is the generated singleton for TOGO M2036, "Basal Salt Medium with biphenyl". A gitignore-independent search for `CultureMech:008625`, `basal_salt_medium_with_biphenyl`, `TOGO:M2036`, `M2036`, and the merge fingerprint `4b93845f` across `data/normalized_yaml`, `data/merge_yaml/merged`, `reports/yaml_record_review`, registry/catalog files, and `data/import_tracking/reports` found one live normalized owner plus the generated singleton and registry/index/import-tracking rows. It found no prior review report. The search included ignored files.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml`. |
| Strict schema | Passed with `scripts/validate_strict.py`; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference snippets | Passed with `linkml-reference-validator validate data ...`; 1 file validated, 0 snippet checks, all validations passed. |
| Term labels | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: no documented focused validator exists for embedded `MediaRecipe.curation_history` on one generated merge record; `just validate-history` targets standalone history files. |

The direct `just` validators remain unavailable in this checkout because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and exits inside `setuptools`. I used the no-project Python 3.11 validator workaround for the focused schema, strict, reference, and term checks above.

## Identity and Grounding

The record ID, TOGO accession, NBRC provenance, and name match the fetched TOGO M2036 payload.

The generated merge is stale relative to the normalized owner: `data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml` has an `apply_mim_groundings.py` event from `2026-08-20` that grounded biphenyl, while the generated merge from `2026-08-06` still leaves `biphenyl` without a `term`.

## Evidence

TOGO M2036 defines a 936 ml main solution with 1 g biphenyl, optional 15 g agar, 50 ml of 20x PO4, 10 ml of 100x ammonium sulfate, and 1 ml each of 1000x FeSO4, 1000x MgCl2, 1000x trace elements, and 1000x Na2MoO4. It then defines the six stock recipes:

| Stock | Source components |
| --- | --- |
| 20x PO4 | 1 L distilled water, 68.05 g KH2PO4, 87.09 g K2HPO4, KOH with no numeric amount |
| 100x ammonium sulfate | 1 L distilled water, 198.66 g ammonium sulfate, NaOH with no numeric amount |
| 1000x FeSO4 | 100 ml distilled water, 0.056 g FeSO4 |
| 1000x MgCl2 | 100 ml distilled water, 16.26 g MgCl2 |
| 1000x Trace elements | 100 ml distilled water, 0.1 g MnCl2.4H2O, 2.65 g CaCl2 |
| 1000x Na2MoO4 | 100 ml distilled water, 0.1 g Na2MoO4.4H2O |

The local record flattened every stock component into the top-level ingredient list at stock concentration, summed seven different water rows into one 1338 g/L row, and also left empty `solutions` placeholders for each stock with the source addition volumes stored as `G_PER_L` rather than `ML_PER_L`.

## Completeness

The source formula is materially incomplete because the stock boundaries are unusable. A reader cannot distinguish final-medium biphenyl and agar from the six concentrated stock recipes, and the empty `Unknown solution` wrappers carry no composition.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated merge is stale relative to its normalized owner. | The normalized owner gained an `2026-08-20` biphenyl grounding after the generated merge was written on `2026-08-06`; the merge still lacks that term. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml` |
| Major | Six concentrated stocks are flattened to top-level ingredients. | TOGO groups KH2PO4/K2HPO4/KOH, ammonium sulfate/NaOH, FeSO4, MgCl2, MnCl2/CaCl2, and Na2MoO4 into six named stocks; the YAML also stores their components as final `ingredients`. | `data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml` |
| Major | All six stock additions have wrong units and empty composition. | TOGO uses 50 ml, 10 ml, and four 1 ml stock additions; the YAML uses `G_PER_L` for every solution and leaves all six `composition` arrays empty with `name: Unknown solution`. | `data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml` |
| Major | The water row is a sum of different preparation volumes. | TOGO has 936 ml in the main solution, 1 L in two stock recipes, and 100 ml in four stock recipes; the YAML stores a single 1338 g/L `Distilled water` row with those values merged. | `data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml` |
| Major | KOH and NaOH are modeled as final variable ingredients. | TOGO lists KOH only under 20x PO4 and NaOH only under 100x ammonium sulfate; neither belongs as a top-level final ingredient. | `data/normalized_yaml/bacterial/basal_salt_medium_with_biphenyl.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml` so the current biphenyl grounding is published.
2. Rebuild the six source stock solutions with their TOGO names, compositions, and 50 ml / 10 ml / 1 ml addition volumes.
3. Move every stock component out of top-level `ingredients`; keep only the final-medium 936 ml water, 1 g biphenyl, 15 g optional agar, and the six stock additions at the top level.
4. Split the summed water row into the main-solution and stock-local water volumes.
5. Leave KOH and NaOH as stock-local variable reagents or pH adjusters rather than final-medium ingredients.

## Follow-up Checks

1. Re-run the focused schema, strict, term, and reference validators on `data/merge_yaml/merged/Basal_Salt_Medium_with_biphenyl.yaml` after regeneration.
2. Re-fetch TOGO `gmdb_medium_by_gmid?gm_id=M2036` and compare all six regenerated stock solutions against the API payload.
3. Re-run the duplicate-ingredient and concentration-plausibility audits and confirm `CultureMech:008625` is no longer flagged for a summed water row.

## Additional Notes

The import-tracking reports already flag the summed water row and all six empty stock names on `CultureMech:008625`. This review confirms that those warnings correspond to distinct TOGO M2036 stock recipes.
