# YAML Record Review: methanocella_conradii_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanocella_conradii_medium__0030dc5a.yaml`
- Started UTC: 2026-09-24T03:25:49Z
- Finished UTC: 2026-09-24T03:25:49Z
- Verdict: needs curation

## Target

- Stable ID: `CultureMech:004073`
- Label: `methanocella_conradii_medium`
- Category: `archaea`
- Maintained owners: `data/normalized_yaml/archaea/KOMODO_1318_METHANOCELLA_CONRADII_medium.yaml`; merged with `data/normalized_yaml/archaea/methanocella_conradii_medium.yaml`
- Source identity: KOMODO medium 1318, explicitly linked to DSMZ/MediaDive medium 1318

## Validation

- Open schema: Passed; `linkml-validate` reported no issues.
- Strict validator: Passed; 1 file scanned, 0 files with errors, and 0 error rows.
- Reference validator: Passed; 0 reference checks were applicable.
- Term validator: Passed.
- Embedded history: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- Exact ignored-file search for `CultureMech:004073`, `CultureMech:000776`, `KOMODO_1318_METHANOCELLA_CONRADII_medium`, `komodo.medium:1318`, `mediadive.medium:1318`, `DSMZ Medium 1318`, and `methanocella_conradii_medium` confirms the generated record is a source-duplicate merge of the KOMODO 1318 copy and the DSMZ 1318 parent.
- The duplicate relationship is well supported: the KOMODO owner states that KOMODO 1318 cites DSMZ Medium 1318, and both current normalized owners carry the same reviewed DSMZ 1318 formulation.
- The generated record is stale. It lacks the August 2026 normalized-owner repairs that moved DSMZ 1318 stock-strength rows into nested SL-10, selenite-tungstate, resazurin, Wolin 10x vitamin, and seven-vitamin solutions.
- The generated `parent_media.path` is `data/normalized_yaml/bacterial/methanocella_conradii_medium.yaml`; exact `find` under `data/normalized_yaml/bacterial` found no such file, including ignored files. The current DSMZ owner lives at `data/normalized_yaml/archaea/methanocella_conradii_medium.yaml`.

## Evidence

- MediaDive 1318 encodes a 1004 ml final batch with 1000 ml water, 1 ml `Trace element solution SL-10`, 1 ml `Selenite-tungstate solution`, 0.5 ml 0.1% resazurin, 1 ml `Wolin's vitamin solution (10x)`, and 1 ml `Seven vitamins solution`.
- The current KOMODO owner records the August 25 `CORRECTED_DSMZ_1318_SOLUTION_STRUCTURE` repair, with `ingredients 30 -> 11` and `solutions 3 -> 5`.
- Both current normalized owners preserve the corrected 1 ml stock additions and the scaled one-litre final basis documented for the printed 1004 ml DSMZ batch.

## Completeness

- The DSMZ PDF and MediaDive REST source provide enough evidence to encode direct ingredients, all five stock additions, pH 7.0, anoxic stock handling, and the 100% H2 post-inoculation overpressure.
- Empty `target_organisms` and `growth_data` are optional-field omissions, not review findings for this record.

## Findings

- Blocker: generated YAML still publishes the pre-repair flattened recipe. SL-10 components, selenite-tungstate components, Wolin vitamin components, seven-vitamin components, and the resazurin stock appear as top-level `ingredients` even though the current normalized owners have already moved them into five nested `solutions`.
- Blocker: several stock-only rows are recorded at full stock concentration as if they were final-medium concentrations, including HCl 25%, `FeCl2 x 4 H2O`, ZnCl2, `MnCl2 x 4 H2O`, `CoCl2 x 6 H2O`, `NiCl2 x 6 H2O`, `Na2SeO3 x 5 H2O`, `Na2WO4 x 2 H2O`, biotin, folic acid, thiamine HCl, riboflavin, and lipoic acid.
- Blocker: vitamin rows from different DSMZ stocks were summed across incompatible scopes. The generated file reports `Vitamin B12` as `0.101` g/L from `0.1` plus `0.001`, `p-Aminobenzoic acid` as `0.13` g/L from `0.08` plus `0.05`, `Nicotinic acid` as `0.25` g/L from `0.2` plus `0.05`, and `Pyridoxine hydrochloride` as `0.4` g/L from `0.3` plus `0.1`.
- Major: the generated output omits the current normalized preparation steps for 80% N2 / 20% CO2 sparging, filter-sterilized vitamin addition, sterile anoxic carbonate, cysteine, and DTT stocks, SL-10 preparation, and 1 bar 100% H2 overpressure.
- Major: `parent_media.path` points at nonexistent `data/normalized_yaml/bacterial/methanocella_conradii_medium.yaml` instead of the current archaeal DSMZ parent path.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/methanocella_conradii_medium__0030dc5a.yaml` from the current normalized KOMODO and DSMZ owners.
- Ensure merge generation preserves the five existing nested stocks rather than re-flattening SL-10, selenite-tungstate, sodium-resazurin, Wolin-vitamin, or seven-vitamin components.
- Ensure generated source-duplicate metadata uses `data/normalized_yaml/archaea/methanocella_conradii_medium.yaml` for `CultureMech:000776`.
- Confirm the regenerated recipe keeps only the 11 direct ingredients plus the five structured stock solutions from the August 25 DSMZ 1318 repair.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation after regenerating merged YAML.
- Search regenerated output for `Merged 2 duplicates` scoped to this record and confirm no cross-stock vitamin sums remain.
- Exact-search regenerated output for `data/normalized_yaml/bacterial/methanocella_conradii_medium.yaml` and confirm there are no matches, including ignored files.
- Compare generated ingredients against both normalized owners and confirm the August 25 `CORRECTED_DSMZ_1318_SOLUTION_STRUCTURE` repair is present in the merged record history.

## Additional Notes

None found.
