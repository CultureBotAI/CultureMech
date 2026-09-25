# YAML Record Review: MODIFIED METHANOBACTERIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_methanobacterium_medium__3288cf7e.yaml
- Started UTC: 2026-09-24T12:10:43Z
- Finished UTC: 2026-09-24T12:10:43Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_methanobacterium_medium__3288cf7e.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:000994` |
| Name | `modified_methanobacterium_medium` |
| Source identity | `mediadive.medium:1523` |
| Category | `archaea` |
| Maintained owner | `data/normalized_yaml/archaea/modified_methanobacterium_medium.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one MediaDive-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_methanobacterium_medium__3288cf7e.yaml` exited 0 with no diagnostics. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_methanobacterium_medium__3288cf7e.yaml --out /private/tmp/modified_methanobacterium_medium__3288cf7e.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_methanobacterium_medium__3288cf7e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_methanobacterium_medium__3288cf7e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes MediaDive's DSMZ 1523 copy of "MODIFIED METHANOBACTERIUM MEDIUM". The main DSMZ identity and pH range are correct, but the generated record no longer contains DSMZ's 6 g Brain heart infusion ingredient and flattens both DSMZ stock solutions into final-medium rows.

An exact gitignore-independent search under `data/normalized_yaml/` found two additional maintained records with the same normalized name: `data/normalized_yaml/archaea/TOGO_M3138_Modified_Methanobacterium_Medium.yaml` and `data/normalized_yaml/archaea/JCM_J1427_MODIFIED_METHANOBACTERIUM_MEDIUM.yaml`. These should be reviewed before assigning one canonical `modified_methanobacterium_medium` identity.

## Evidence

DSMZ Medium 1523 lists KH2PO4, MgSO4 x 7 H2O, NaCl, NH4Cl, CaCl2 x 2 H2O, 1 ml Trace element solution SL-10, 6 g Brain heart infusion (BD Bacto), 6 g Proteose peptone, 2 g Yeast extract, Na-acetate, Na-formate, 0.5 ml Sodium resazurin, NaHCO3, 1 ml Seven vitamins solution, L-Cysteine HCl x H2O, Na2S x 9 H2O, and 1000 ml Distilled water. The PDF also gives full stock compositions for SL-10 and Seven vitamins solution.

MediaDive 1523 exposes the same main recipe and stock recipes. The generated YAML replaces the 6 g Brain heart infusion row with six unscaled Brain Heart Infusion product constituents from a secondary web source. It also promotes SL-10 trace elements and Seven vitamins stock components to top-level ingredients at their stock g/L concentrations and omits the 1000 ml main water, 990 ml SL-10 water, and 1000 ml Seven vitamins water rows.

The maintained DSMZ 1523 source has a 2026-08-07 `NESTED_FLATTENED_COCKTAIL` curation event that moved five stock-strength rows into two `solutions` entries after this generated artifact was created. That repair is partial: FeCl2 and four vitamin rows are now nested in the maintained file, but ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, p-Aminobenzoic acid, D-(+)-biotin, and Calcium pantothenate remain flattened.

## Completeness

The generated record is incomplete because it lacks Brain heart infusion as an intact commercial ingredient, both source stock solution additions, and all three explicit water rows.

The DSMZ 1523 PDF contains several DSM strain-specific modifications. They are not represented as target-organism rows in the generated base-medium record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The source Brain heart infusion ingredient was replaced with unscaled commercial-product constituents. | DSMZ Medium 1523 and MediaDive 1523 list `Brain heart infusion` at 6 g/L; the generated YAML lacks that row and instead adds full-product constituents such as Proteose peptone 10 g/L, Dextrose 2 g/L, Sodium chloride 5 g/L, and Disodium phosphate 2.5 g/L. | Restore Brain heart infusion as a 6 g/L source ingredient in `data/normalized_yaml/archaea/modified_methanobacterium_medium.yaml`; if constituent detail is needed, nest it under the commercial product and scale or mark it appropriately. |
| blocker | The generated record flattens DSMZ stock solutions into final-medium ingredients. | DSMZ 1523 adds Trace element solution SL-10 and Seven vitamins solution at 1 ml/L each; the generated YAML promotes their trace-metal and vitamin components to top-level ingredients at stock concentrations. | Finish nesting all SL-10 and Seven vitamins stock constituents under `solutions`, then regenerate. |
| major | The generated artifact is stale relative to a later partial repair in the maintained source. | The generated YAML was merged on 2026-08-06 and still contains all stock rows in `ingredients`; the maintained source has a 2026-08-07 `NESTED_FLATTENED_COCKTAIL` entry and already moved FeCl2 and four vitamin rows into `solutions`. | Rerun the merge after completing the remaining stock-boundary fixes. |
| major | The generated record omits all source water rows. | DSMZ 1523 lists 1000 ml main water, 990 ml SL-10 water, and 1000 ml Seven vitamins water; no water row appears in the generated YAML. | Preserve water rows in the main medium and both stocks. |

## Recommended Edits

1. Restore the 6 g/L Brain heart infusion source row and remove unscaled BHI constituent rows from top-level `ingredients`.
2. Keep Trace element solution SL-10 and Seven vitamins solution as 1 ml/L stock additions with complete nested compositions.
3. Preserve the main, SL-10, and Seven vitamins distilled-water rows.
4. Regenerate the DSMZ 1523 merged artifact from the repaired maintained owner.
5. Reconcile DSMZ 1523 against the same-name TOGO M3138 and JCM J1427 records before collapsing or splitting CultureMech identities.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated DSMZ 1523 YAML.
- Re-open the DSMZ Medium 1523 PDF and MediaDive 1523 and confirm the generated YAML contains one 6 g/L Brain heart infusion row, one 1 ml/L SL-10 addition, and one 1 ml/L Seven vitamins addition.
- Confirm no trace-metal or vitamin stock rows remain as top-level final-medium ingredients.
- Confirm the BHI constituent rows are not present as unscaled top-level ingredients.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
