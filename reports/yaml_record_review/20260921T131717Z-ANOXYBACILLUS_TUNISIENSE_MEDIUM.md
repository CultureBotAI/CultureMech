# YAML Record Review: Anoxybacillus Tunisiense Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANOXYBACILLUS_TUNISIENSE_MEDIUM.yaml
- Started UTC: 2026-09-21T13:16:41Z
- Finished UTC: 2026-09-21T13:17:18Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:010134` / `anoxybacillus_tunisiense_medium` in `data/merge_yaml/merged/ANOXYBACILLUS_TUNISIENSE_MEDIUM.yaml`.

- The generated record was produced by `merge_recipes.py` from `TOGO_M726_Anoxybacillus_Tunisiense_Medium.yaml`.
- The maintained owner is `data/normalized_yaml/bacterial/TOGO_M726_Anoxybacillus_Tunisiense_Medium.yaml`.
- An ignored-inclusive exact search across `data`, `.claude`, and `reports` for `ANOXYBACILLUS_TUNISIENSE_MEDIUM`, `Anoxybacillus Tunisiense Medium`, `ANOXYBACILLUS TUNISIENSE MEDIUM`, and `tunisiense` found the TOGO M726 owner, the separate MediaDive/JCM J704 owner, this generated merge, its generated sibling, and unrelated `Halanaerobaculum tunisiense` records.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANOXYBACILLUS_TUNISIENSE_MEDIUM.yaml` through the Python 3.11 no-project workaround | Pass; no issues found. |
| `python scripts/validate_strict.py data/merge_yaml/merged/ANOXYBACILLUS_TUNISIENSE_MEDIUM.yaml --out /private/tmp/anoxybacillus_tunisiense.strict.tsv --workers 1 --quiet` through the Python 3.11 no-project workaround | Pass; 1 file scanned and 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/ANOXYBACILLUS_TUNISIENSE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` through the Python 3.11 no-project workaround | Pass; 0 reference checks were discovered. |
| `linkml-term-validator validate-data data/merge_yaml/merged/ANOXYBACILLUS_TUNISIENSE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` through the Python 3.11 no-project workaround | Pass; only the known `eutils` `pkg_resources` deprecation warning was emitted. |
| Embedded `MediaRecipe.curation_history` | Not checked: the documented `just validate-history` gate targets standalone files under `history/`, not embedded history on one generated merge record. |

The documented `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` wrappers were not rerun directly because project-level `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before any target-specific validation begins. The equivalent LinkML/strict/reference/term checks above were run with `uv run --no-project --python /usr/local/bin/python3.11`.

## Identity and Grounding

The record correctly identifies TOGO Medium M726 / JCM M704, `Anoxybacillus Tunisiense Medium`; the live TOGO M726 API and the current JCM `GRMD=704` page both support that identity.

Several simple ingredient groundings are correct, including MgCl2 x 6 H2O, CaSO4 x 2 H2O, KH2PO4, Na2MoO4 x 2 H2O, H3BO3, MnCl2 x 4 H2O, CuCl2 x 2 H2O, ZnCl2, FeCl2 x 4 H2O, and FeCl3 x 6 H2O. The `Na2HPO4 x 2 H2O` row is grounded to anhydrous disodium hydrogenphosphate, `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` are grounded to anhydrous chloride terms, and the sodium citrate dihydrate row has no term.

## Evidence

The live TOGO M726 API and JCM M704 page agree on the source topology: the final medium contains 880 ml distilled water, 2.5 g each yeast extract and tryptone, 100 ml Base solution A, and 20 ml Base solution B; Base A contains 990 ml distilled water, 1.32 g nitrilotriacetic acid, 0.2 g MgCl2 x 6 H2O, 0.4 g CaSO4 x 2 H2O, 5 ml Trace elements, and 5 ml Fe citrate solution; Base B contains KH2PO4, Na2HPO4 x 2 H2O, and 1 L water; Trace elements and Fe citrate solution are separately defined stocks. TOGO and JCM also both carry the pH adjustments to 8.0, 7.2, and 6.0-6.5.

The generated record does not preserve that topology. It collapses all Base A, Base B, Trace element, and Fe citrate stock components into one final ingredient list, merges repeated components across different solutions, and also keeps four empty `Unknown solution` rows for the same stocks.

## Completeness

The record is not complete as a runnable recipe because all four stock additions are placeholders with empty `composition` and `G_PER_L` pseudo-units. The three pH adjustment comments from M726 are also absent, as is a `ph_value` for the main 8.0 pH.

An ignored-inclusive exact search found a separate MediaDive/JCM owner at `data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml` and generated sibling `data/merge_yaml/merged/anoxybacillus_tunisiense_medium__3d9581d2.yaml`. That sibling preserves `ph_value: 6.2` plus the three pH comments but flattens the same stock components, so it is corroborating context rather than a clean owner.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock scopes were collapsed and summed into final-medium rows. | Water was merged as `1873.0 G_PER_L` from 880 ml, 990 ml, and three 1 L stock waters; nitrilotriacetic acid was merged as `14.120000000000001 G_PER_L` from 1.32 g in Base A and 12.8 g in Trace elements. These are different solution-local quantities in JCM M704. | `data/normalized_yaml/bacterial/TOGO_M726_Anoxybacillus_Tunisiense_Medium.yaml` or the TOGO importer/duplicate-merger that collapsed repeated labels. |
| major | Four source stock additions are present only as empty placeholders with wrong units. | JCM M704 adds 100 ml Base solution A, 20 ml Base solution B, 5 ml Trace elements, and 5 ml Fe citrate solution. The generated `solutions` rows have those numeric values as `G_PER_L`, `composition: []`, and `name: Unknown solution`. | TOGO M726 normalized owner and the solution migrator. |
| major | Stock-local concentrations are exposed as final-medium concentrations. | Base B salts, Trace elements salts, and Fe citrate salts all appear directly as final ingredients at their per-stock amounts, e.g. KH2PO4 5.44 `G_PER_L`, Na2HPO4 x 2 H2O 21.4 `G_PER_L`, FeCl2 x 4 H2O 1 `G_PER_L`, and FeCl3 x 6 H2O 2.7 `G_PER_L`, instead of being nested or diluted through their source stock additions. | TOGO M726 normalized owner or generated TOGO component flattener. |
| major | All pH adjustment comments were dropped. | M726 has pH adjustments for the final medium, Base solution A, and Trace elements. The generated record has no `ph_value` and no `preparation_steps`. | TOGO comments importer for M726. |
| major | Several hydrate-specific ingredients are over-narrowly grounded or unresolved. | The source specifies Na2HPO4 x 2 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, and sodium citrate x 2 H2O; the generated record uses anhydrous terms for phosphate/cobalt/nickel and leaves sodium citrate ungrounded. | TOGO M726 normalized owner after stock modeling is repaired. |
| minor | The same JCM M704 source exists as a second unmerged record. | `data/normalized_yaml/bacterial/anoxybacillus_tunisiense_medium.yaml` cites `mediadive.medium:J704` / the same JCM `GRMD=704` page and generates `anoxybacillus_tunisiense_medium__3d9581d2.yaml`. | Merge fingerprinting once TOGO and MediaDive stock boundaries are corrected. |

## Recommended Edits

1. Restore Base solution A, Base solution B, Trace elements, and Fe citrate solution as nested solution records or correctly linked internal solution additions with ml units.
2. Remove stock-local components from the top-level final-medium ingredient list unless they have been deliberately converted through the stated 100 ml, 20 ml, 5 ml, and 5 ml additions.
3. Undo cross-solution duplicate sums for water and nitrilotriacetic acid.
4. Import the three pH adjustment comments from TOGO/JCM M726.
5. Correct hydrate-specific ChEBI terms after the stock rows have a structural owner.
6. Reconcile the TOGO M726 and MediaDive J704 records, then regenerate `data/merge_yaml/merged/ANOXYBACILLUS_TUNISIENSE_MEDIUM.yaml`.

## Follow-up Checks

- Rerun focused open-schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/TOGO_M726_Anoxybacillus_Tunisiense_Medium.yaml`.
- Rerun the concentration plausibility report and confirm `FeCl2 x 4 H2O` and `FeCl3 x 6 H2O` no longer appear as stock-strength trace salts in the final medium.
- Rerun `just verify-merges` and `just audit-merge-freshness` after the TOGO/MediaDive M704 reconciliation.
- Inspect the regenerated M726 merge and confirm it has one final 880 ml water row plus structured stock rows rather than a summed 1873 water row.

## Additional Notes

The TOGO public `/medium/M726` page was not useful directly because public TOGO medium pages are rendered from a small SPA shell; the review used the TOGO `gmdb_medium_by_gmid` API and the original JCM GRMD page instead.
