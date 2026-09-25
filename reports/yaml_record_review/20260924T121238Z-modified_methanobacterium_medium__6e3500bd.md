# YAML Record Review: Modified Methanobacterium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_methanobacterium_medium__6e3500bd.yaml
- Started UTC: 2026-09-24T12:12:38Z
- Finished UTC: 2026-09-24T12:12:38Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_methanobacterium_medium__6e3500bd.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:009606` |
| Name | `modified_methanobacterium_medium` |
| Source identity | `TOGO:M3138` |
| Category | `archaea` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M3138_Modified_Methanobacterium_Medium.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one TOGO-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_methanobacterium_medium__6e3500bd.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_methanobacterium_medium__6e3500bd.yaml --out /private/tmp/modified_methanobacterium_medium__6e3500bd.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_methanobacterium_medium__6e3500bd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_methanobacterium_medium__6e3500bd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes TOGO M3138, a TOGO copy of DSMZ 1523 "MODIFIED METHANOBACTERIUM MEDIUM". The source identity is grounded, but the normalized record collapses stock-solution structure and source units, so many generated concentrations no longer correspond to the DSMZ 1523 PDF or the TOGO M3138 API payload.

An exact gitignore-independent search under `data/normalized_yaml/archaea/` found two additional maintained records with the same normalized name: `data/normalized_yaml/archaea/modified_methanobacterium_medium.yaml` and `data/normalized_yaml/archaea/JCM_J1427_MODIFIED_METHANOBACTERIUM_MEDIUM.yaml`. These should be reviewed before assigning one canonical `modified_methanobacterium_medium` identity.

## Evidence

The DSMZ Medium 1523 PDF lists 1000 ml Distilled water in the main recipe, 990 ml Distilled water in Trace element solution SL-10, and 1000 ml Distilled water in Seven vitamins solution. It lists SL-10 and Seven vitamins as 1 ml additions to the main medium, with milligram quantities for most stock components.

The TOGO M3138 API preserves those source rows and units, including Brain Heart Infusion at 6 g, Trace element solution SL-10 at 1 ml, Seven vitamins solution at 1 ml, HCl at 10 ml inside SL-10, and multiple milligram stock rows. The generated YAML sums the three water rows into a single 2990.0 G_PER_L final-medium ingredient, emits milligram SL-10 and vitamin-stock rows as G_PER_L values such as ZnCl2 70 G_PER_L and p-Aminobenzoic acid 80 G_PER_L, keeps empty Trace element and Seven vitamins placeholders with G_PER_L units, and replaces the source Brain Heart Infusion row with unscaled Brain Heart Infusion product constituents.

## Completeness

The generated record is incomplete because it lacks Brain Heart Infusion as an intact source ingredient and lacks structured Trace element solution SL-10 and Seven vitamins solution compositions.

The DSMZ 1523 PDF contains several DSM strain-specific modifications. They are not represented as target-organism rows in the generated TOGO base-medium record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | Stock-solution water rows were collapsed into the final medium. | The source has 1000 ml main water, 990 ml SL-10 water, and 1000 ml Seven vitamins water; the generated YAML emits one Distilled water row at 2990.0 G_PER_L. | Preserve water rows inside their own source contexts in `data/normalized_yaml/archaea/TOGO_M3138_Modified_Methanobacterium_Medium.yaml`. |
| blocker | Milligram stock ingredients were promoted to top-level gram-per-liter rows. | TOGO M3138 lists SL-10 rows such as 70 mg ZnCl2 and 6 mg H3BO3, and Seven vitamins rows such as 80 mg p-Aminobenzoic acid; the generated YAML emits those as 70, 6, and 80 G_PER_L final-medium rows. | Keep SL-10 and Seven vitamins as 1 ml/L structured stocks and convert milligram stock amounts within the stock compositions. |
| blocker | The source Brain Heart Infusion ingredient was replaced with unscaled commercial-product constituents. | DSMZ 1523 and TOGO M3138 list Brain Heart Infusion at 6 g/L; the generated YAML lacks that row and instead adds full-product constituents such as Proteose peptone 10 g/L, Dextrose 2 g/L, Sodium chloride 5 g/L, and Disodium phosphate 2.5 g/L. | Restore Brain Heart Infusion as a 6 g/L ingredient; if constituent detail is needed, nest it under the product and scale or mark it appropriately. |
| major | Empty solution placeholders have grams-per-liter units for milliliter additions. | TOGO M3138 lists 0.5 ml Na-resazurin solution, 1 ml Trace element solution SL-10, and 1 ml Seven vitamins solution; the generated `solutions` entries have empty `composition` arrays and unit G_PER_L. | Represent these as volume additions with compositions or source-backed stock notes. |

## Recommended Edits

1. Repair the TOGO unit conversion so milligram stock rows remain milligrams per liter of stock instead of becoming grams per liter of final medium.
2. Restore Trace element solution SL-10 and Seven vitamins solution as 1 ml/L stock additions with nested compositions.
3. Keep main, SL-10, and Seven vitamins water in separate source contexts.
4. Restore the 6 g/L Brain Heart Infusion row and remove unscaled BHI constituent rows from top-level `ingredients`.
5. Reconcile this TOGO M3138 import with the same-name DSMZ 1523 MediaDive record and the JCM J1427 record.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated TOGO M3138 YAML.
- Re-open the DSMZ Medium 1523 PDF and TOGO M3138 and confirm mg stock rows are no longer emitted as top-level G_PER_L ingredients.
- Confirm water is not summed across the main medium and stock recipes.
- Confirm the Trace element solution SL-10 and Seven vitamins solution placeholders are no longer empty.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
