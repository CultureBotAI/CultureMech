# YAML Record Review: ANOXYBACILLUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml
- Started UTC: 2026-09-21T13:14:55Z
- Finished UTC: 2026-09-21T13:15:52Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002061` / `anoxybacillus_medium` in `data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml`.

- The generated record was produced by `merge_recipes.py` from `anoxybacillus_medium.yaml` and `anaerobacillus_medium.yaml`.
- The maintained owners are `data/normalized_yaml/bacterial/anoxybacillus_medium.yaml` for DSMZ 898 and `data/normalized_yaml/bacterial/anaerobacillus_medium.yaml` for DSMZ 898a.
- An ignored-inclusive exact search across `data`, `.claude`, and `reports` for `ANOXYBACILLUS_MEDIUM`, `Anoxybacillus Medium`, and `ANOXYBACILLUS MEDIUM` found only the expected normalized owner, this generated merge, registry/index/report rows, and curation side tables.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml` through the Python 3.11 no-project workaround | Pass; no issues found. |
| `python scripts/validate_strict.py data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml --out /private/tmp/anoxybacillus.strict.tsv --workers 1 --quiet` through the Python 3.11 no-project workaround | Pass; 1 file scanned and 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` through the Python 3.11 no-project workaround | Pass; 0 reference checks were discovered. |
| `linkml-term-validator validate-data data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` through the Python 3.11 no-project workaround | Pass; only the known `eutils` `pkg_resources` deprecation warning was emitted. |
| Embedded `MediaRecipe.curation_history` | Not checked: the documented `just validate-history` gate targets standalone files under `history/`, not embedded history on one generated merge record. |

The documented `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` wrappers were not rerun directly because project-level `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before any target-specific validation begins. The equivalent LinkML/strict/reference/term checks above were run with `uv run --no-project --python /usr/local/bin/python3.11`.

## Identity and Grounding

The generated record is internally conflicted. Its `media_term`, notes, and pH range identify DSMZ Medium 898 / `ANOXYBACILLUS MEDIUM`, and the live DSMZ 898 PDF supports pH 9.5-9.7. Its NaCl row and `merged_from` list also incorporate DSMZ 898a / `ANAEROBACILLUS MEDIUM`, which the maintained data correctly marks as a `SALINITY_VARIANT` of DSMZ 898 rather than a duplicate.

The non-stock base salts use the correct ChEBI terms. `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887` / `nickel dichloride`, and the `HCl` row inherited from Trace element solution SL-10 represents a 25 percent HCl solution rather than pure hydrogen chloride.

## Evidence

The inspected DSMZ 898 PDF supports these final-medium rows before dilution adjustment: 0.20 g KH2PO4, 0.10 g MgCl2 x 6 H2O, 0.20 g KCl, 1.00 g NH4Cl, 5.00 g NaCl, 0.50 ml 0.1% resazurin, 2.76 g Na2CO3, 10.00 g NaHCO3, 0.50 g yeast extract, 5.00 g D-glucose, 0.50 g Na2S x 9 H2O, 1.00 ml Trace element solution SL-10, 1.00 ml Wolin's vitamin solution (10x), and 1000.00 ml distilled water. It also supports the final pH 9.5-9.7 and the two preparation paragraphs preserved in the generated record.

The generated record is not a faithful projection of that source: it uses 14.9701 g/L NaCl from DSMZ 898a instead of 4.99002 g/L from DSMZ 898, omits the 1000 ml distilled water row, and expands the two 1 ml stock additions into final-medium rows at stock strength.

## Completeness

The record is incomplete as a stock-aware recipe. Trace element solution SL-10 and Wolin's vitamin solution remain flattened; their internal components are present, but not nested under stock additions, and the SL-10-specific dissolution paragraph is root-scoped.

The DSMZ 898a `ANAEROBACILLUS MEDIUM` salinity variant is found in `data/normalized_yaml/bacterial/anaerobacillus_medium.yaml` by ignored-inclusive exact search and should remain a child variant rather than a co-merged source for DSMZ 898.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated DSMZ 898 record picked up the NaCl amount from DSMZ 898a. | DSMZ 898 and `data/normalized_yaml/bacterial/anoxybacillus_medium.yaml` use 4.99002 g/L after volume normalization; DSMZ 898a and `anaerobacillus_medium.yaml` use 14.9701 g/L. The generated DSMZ 898 merge stores 14.9701 g/L while retaining media term `mediadive.medium:898` and pH 9.5-9.7. | Merge rules for `SALINITY_VARIANT` records; `data/normalized_yaml/bacterial/anoxybacillus_medium.yaml` should not merge its child as a duplicate. |
| major | Trace element solution SL-10 and Wolin's vitamin solution are flattened at stock concentration. | DSMZ 898 adds each stock at 1.00 ml, but the generated final-medium ingredient list contains 18 internal SL-10/vitamin rows at stock strengths, including FeCl2 1.5 `G_PER_L`, ZnCl2 0.07 `G_PER_L`, Biotin 0.02 `G_PER_L`, and Pyridoxine hydrochloride 0.1 `G_PER_L`. | DSMZ/MediaDive 898 stock parser and `data/normalized_yaml/bacterial/anoxybacillus_medium.yaml`. |
| major | Distilled water from the final medium is absent. | DSMZ 898 lists 1000.00 ml distilled water in the final medium; the generated record has no water ingredient. | DSMZ/MediaDive 898 normalized owner. |
| major | The SL-10 stock preparation step is attached to the final-medium root. | `First dissolve FeCl2 in the HCl...` describes preparing Trace element solution SL-10 from DSMZ medium 320; it is not a final-medium step for DSMZ 898. | DSMZ/MediaDive stock parser. |
| major | `NiCl2 x 6 H2O` and `HCl` are over-narrowly grounded. | DSMZ specifies nickel chloride hexahydrate and 25 percent HCl in SL-10, but the generated rows point to anhydrous nickel dichloride and pure hydrogen chloride. | `data/normalized_yaml/bacterial/anoxybacillus_medium.yaml` after stock modeling is repaired. |

## Recommended Edits

1. Fix merge grouping so `anaerobacillus_medium.yaml` remains a `SALINITY_VARIANT` child of DSMZ 898 instead of a source merged into `ANOXYBACILLUS_MEDIUM.yaml`.
2. Rebuild DSMZ 898 with Trace element solution SL-10 and Wolin's vitamin solution as 1 ml/L stock additions, not flattened stock ingredients.
3. Restore the final-medium 1000 ml distilled water row.
4. Scope the FeCl2/HCl dissolution instruction to the SL-10 stock.
5. Correct hydrate and solution groundings after the stock rows have a structural owner.
6. Regenerate `data/merge_yaml/merged/ANOXYBACILLUS_MEDIUM.yaml` from normalized data instead of hand-editing the generated merge.

## Follow-up Checks

- Rerun focused open-schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/anoxybacillus_medium.yaml` and `data/normalized_yaml/bacterial/anaerobacillus_medium.yaml`.
- Rerun `just verify-merges` and `just audit-merge-freshness` to confirm salinity variants no longer co-merge with their parents.
- Inspect the regenerated `ANOXYBACILLUS_MEDIUM.yaml` and confirm it contains DSMZ 898 NaCl at 4.99002 g/L, pH 9.5-9.7, the DSMZ 898 source URL, and no 898a merge source.

## Additional Notes

The KOMODO 898 record was not part of this generated merge, but an ignored-inclusive search found it as another same-number source whose variant topology was repaired in September 2026. Future DSMZ 898 work should reconcile all three maintained inputs: DSMZ, KOMODO, and DSMZ 898a.
