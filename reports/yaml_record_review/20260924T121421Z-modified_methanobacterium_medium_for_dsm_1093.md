# YAML Record Review: Modified Methanobacterium Medium (For DSM 1093)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_methanobacterium_medium_for_dsm_1093.yaml
- Started UTC: 2026-09-24T12:14:21Z
- Finished UTC: 2026-09-24T12:14:21Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_methanobacterium_medium_for_dsm_1093.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:009215` |
| Name | `modified_methanobacterium_medium_for_dsm_1093` |
| Source identity | `TOGO:M2660` |
| Category | `archaea` |
| Maintained owner | `data/normalized_yaml/archaea/modified_methanobacterium_medium_for_dsm_1093.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one TOGO-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_methanobacterium_medium_for_dsm_1093.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_methanobacterium_medium_for_dsm_1093.yaml --out /private/tmp/modified_methanobacterium_medium_for_dsm_1093.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_methanobacterium_medium_for_dsm_1093.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_methanobacterium_medium_for_dsm_1093.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes TOGO M2660, the DSM 1093-specific variant of DSMZ 1523 "MODIFIED METHANOBACTERIUM MEDIUM". The variant overlay is recognizable: relative to the base medium, the record omits L-Cysteine HCl x H2O and Na2S x 9 H2O and includes Coenzyme M at 0.5 g/L and DTT at 0.3 g/L, matching the DSMZ 1523 instruction for DSM 1093. It still inherits stock-solution, unit-conversion, water-collapsing, and Brain Heart Infusion expansion errors from the same TOGO import family.

An exact gitignore-independent search under `data/normalized_yaml/archaea/` found this maintained owner for `CultureMech:009215`. Other `modified_methanobacterium_medium` base-medium records exist, but none has the exact normalized DSM 1093 variant name.

## Evidence

The DSMZ Medium 1523 PDF lists a DSM 1093-specific note for DSM 862, DSM 1093, DSM 1125, DSM 11977, DSM 11978, DSM 11995, DSM 16643, DSM 116060, and DSM 118696: supplement the autoclaved medium with 0.50 g/L coenzyme M and 0.30 g/L DTT from filter-sterilized anoxic stocks prepared under N2, and omit sulfide and cysteine.

TOGO M2660 preserves those DSM-specific coenzyme M and DTT rows while retaining the same main DSMZ 1523 stock rows as TOGO M3138: 1000 ml main water, 1 ml Trace element solution SL-10, 1 ml Seven vitamins solution, 990 ml SL-10 water, and 1000 ml vitamin-stock water. The generated YAML sums the three water rows into one 2990.0 G_PER_L ingredient, emits milligram stock constituents such as ZnCl2 70 mg and p-Aminobenzoic acid 80 mg as 70 and 80 G_PER_L top-level rows, keeps empty Trace element and Seven vitamins placeholders with G_PER_L units, and replaces the source Brain Heart Infusion row with unscaled Brain Heart Infusion product constituents.

## Completeness

The DSM 1093 overlay is present, but the generated record is incomplete because it lacks Brain Heart Infusion as an intact source ingredient and lacks structured Trace element solution SL-10 and Seven vitamins solution compositions.

The generated record does not make explicit target-organism claims for DSM 1093 or the other DSM strains covered by the same DSMZ 1523 variant note.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | Stock-solution water rows were collapsed into the final medium. | The source has 1000 ml main water, 990 ml SL-10 water, and 1000 ml Seven vitamins water; the generated YAML emits one Distilled water row at 2990.0 G_PER_L. | Preserve water rows inside their own source contexts in `data/normalized_yaml/archaea/modified_methanobacterium_medium_for_dsm_1093.yaml`. |
| blocker | Milligram stock ingredients were promoted to top-level gram-per-liter rows. | TOGO M2660 lists SL-10 rows such as 70 mg ZnCl2 and 6 mg H3BO3, and Seven vitamins rows such as 80 mg p-Aminobenzoic acid; the generated YAML emits those as 70, 6, and 80 G_PER_L final-medium rows. | Keep SL-10 and Seven vitamins as 1 ml/L structured stocks and convert milligram stock amounts within the stock compositions. |
| blocker | The source Brain Heart Infusion ingredient was replaced with unscaled commercial-product constituents. | DSMZ 1523 and TOGO M2660 list Brain Heart Infusion at 6 g/L; the generated YAML lacks that row and instead adds full-product constituents such as Proteose peptone 10 g/L, Dextrose 2 g/L, Sodium chloride 5 g/L, and Disodium phosphate 2.5 g/L. | Restore Brain Heart Infusion as a 6 g/L ingredient; if constituent detail is needed, nest it under the product and scale or mark it appropriately. |
| major | Empty solution placeholders have grams-per-liter units for milliliter additions. | TOGO M2660 lists 0.5 ml Na-resazurin solution, 1 ml Trace element solution SL-10, and 1 ml Seven vitamins solution; the generated `solutions` entries have empty `composition` arrays and unit G_PER_L. | Represent these as volume additions with compositions or source-backed stock notes. |

## Recommended Edits

1. Repair the TOGO unit conversion so milligram stock rows remain milligrams per liter of stock instead of becoming grams per liter of final medium.
2. Restore Trace element solution SL-10 and Seven vitamins solution as 1 ml/L stock additions with nested compositions.
3. Keep main, SL-10, and Seven vitamins water in separate source contexts.
4. Restore the 6 g/L Brain Heart Infusion row and remove unscaled BHI constituent rows from top-level `ingredients`.
5. Preserve the DSM 1093 overlay: omit sulfide and cysteine, and keep 0.5 g/L coenzyme M plus 0.3 g/L DTT.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated TOGO M2660 YAML.
- Re-open the DSMZ Medium 1523 PDF and TOGO M2660 and confirm the DSM 1093-specific supplement and omission instructions are still represented.
- Confirm mg stock rows are no longer emitted as top-level G_PER_L ingredients.
- Confirm water is not summed across the main medium and stock recipes.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
