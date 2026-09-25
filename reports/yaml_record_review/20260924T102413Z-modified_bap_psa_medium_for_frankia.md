# YAML Record Review: modified BAP+ (PSA) MEDIUM FOR FRANKIA

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_bap_psa_medium_for_frankia.yaml
- Started UTC: 2026-09-24T10:24:13Z
- Finished UTC: 2026-09-24T10:24:13Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_bap_psa_medium_for_frankia.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001143` |
| Name | `modified_bap_psa_medium_for_frankia` |
| Original name | `modified BAP+ (PSA) MEDIUM FOR FRANKIA` |
| Category | `bacterial` |
| Medium source | DSMZ / MediaDive `1660` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_bap_psa_medium_for_frankia.yaml` |
| Generated status | Stale generated output with stock solutions still flattened |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_bap_psa_medium_for_frankia.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_bap_psa_medium_for_frankia.yaml --out /private/tmp/modified_bap_psa_medium_for_frankia.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_bap_psa_medium_for_frankia.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_bap_psa_medium_for_frankia.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_bap_psa_medium_for_frankia.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:001143`, `mediadive.medium:1660`, the label, the DSMZ source link, and pH 6.3 all identify modified BAP+ (PSA) MEDIUM FOR FRANKIA.

An exact `find data/normalized_yaml -name modified_bap_psa_medium_for_frankia.yaml` search, which covers ignored files, found one maintained owner at `data/normalized_yaml/bacterial/modified_bap_psa_medium_for_frankia.yaml`. A second exact `find data/normalized_yaml -name mediadive_3183_Chelated_iron_solution.yaml` search found a standalone maintained copy of MediaDive solution 3183 at `data/normalized_yaml/bacterial/mediadive_3183_Chelated_iron_solution.yaml`.

## Evidence

DSMZ Medium 1660 and the MediaDive 1660 REST record agree on the main formulation, the three 100 ml stocks, and the pH adjustment.

| Source claim | Record representation | Review |
| --- | --- | --- |
| Main solution 1660 contains KH2PO4, K2HPO4, NH4Cl, Na-propionate, sodium succinate dibasic, pyruvic acid sodium salt, sodium acetate, MgSO4 x 7 H2O, and CaCl2 x 2 H2O. | The generated record has these nine rows at the source gram amounts. | Supported. |
| Main solution 1660 adds 1 ml Vitamine solution, 1 ml Chelated iron solution, and 0.1 ml Trace element solution. | The generated record has no solution additions; it stores the vitamin, chelated-iron, and trace-element stock compounds as top-level ingredients at stock concentration. | Unsupported stock flattening. |
| The Vitamine solution contains thiamine HCl, nicotinic acid, and pyridoxine HCl in 100 ml water and is added at 1 ml/L. | The maintained normalized owner already nests these three rows under `Vitamine solution` at `1 ML_PER_L`, but the generated merge still lists them as `G_PER_L` top-level ingredients. | Stale generated output. |
| The Trace element solution contains CoSO4 x 7 H2O, CuSO4 x 5 H2O, H3BO3, MnCl2 x 4 H2O, Na2MoO4 x 2 H2O, and ZnSO4 x 7 H2O in 100 ml water and is added at 0.1 ml/L. | The maintained normalized owner already nests three trace rows under `Trace element solution`, but the generated merge still lists all six trace rows as `G_PER_L` top-level ingredients. | Stale and incomplete stock repair. |
| The Chelated iron solution contains citric acid and Eisencitrat in 100 ml water and is added at 1 ml/L. | Citric acid and Eisencitrat remain top-level `10 G_PER_L` ingredients in both the normalized owner and the generated record. | Unsupported stock flattening in the maintained owner. |
| The main solution and all three stock solutions include distilled water. | The generated record has no water rows. | Incomplete water representation. |

## Completeness

The generated record is incomplete because none of the three source stock-solution additions are represented as structured final-medium ingredients. Two stocks have already been partly repaired in the maintained normalized owner, but the generated file has not been regenerated and the Chelated iron solution is still flat upstream.

Empty target-organism and growth-evidence fields were not treated as defects. DSMZ Medium 1660 is a formulation page, not a growth-evidence page.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The generated merge is stale relative to the normalized BAP+ PSA owner. | The maintained owner has the 2026-08-07 `NESTED_FLATTENED_COCKTAIL` repair and nests the Vitamine and Trace element stocks; the generated file lacks that history entry and still has those rows at top level. | Merge generation from `data/normalized_yaml/bacterial/modified_bap_psa_medium_for_frankia.yaml`. |
| major | The Chelated iron solution is still flattened in the maintained owner. | DSMZ and MediaDive call for a 1 ml Chelated iron solution addition; the record stores Citric acid and Eisencitrat as final-medium `10 G_PER_L` ingredients. | `data/normalized_yaml/bacterial/modified_bap_psa_medium_for_frankia.yaml`; MediaDive stock migration logic. |
| major | The stock solution water rows are absent. | DSMZ and MediaDive list 100 ml distilled water in the Vitamine, Chelated iron, and Trace element solutions; none are present in the generated record and the repaired nested stocks in the maintained owner also omit water. | `data/normalized_yaml/bacterial/modified_bap_psa_medium_for_frankia.yaml`; MediaDive water import for nested stocks. |
| major | The Trace element solution repair is incomplete. | Source solution 3184 has six compounds; the maintained owner nests only H3BO3, MnCl2 x 4 H2O, and ZnSO4 x 7 H2O, leaving CoSO4 x 7 H2O, CuSO4 x 5 H2O, and Na2MoO4 x 2 H2O flattened at top level. | `data/normalized_yaml/bacterial/modified_bap_psa_medium_for_frankia.yaml`; `apply_cocktail_nesting.py` matching logic. |

## Recommended Edits

1. Complete stock nesting in `data/normalized_yaml/bacterial/modified_bap_psa_medium_for_frankia.yaml`: add the 1 ml/L Chelated iron solution, move its Citric acid and Eisencitrat rows under it, and move the three remaining Trace element rows under the existing 0.1 ml/L Trace element solution.
2. Restore the distilled-water rows in the main solution and all three stock solutions while preserving their stock-local 100 ml volumes.
3. Regenerate `data/merge_yaml/merged/modified_bap_psa_medium_for_frankia.yaml` so the merged record carries the existing Vitamine and Trace element repairs.
4. Compare the regenerated record against DSMZ Medium 1660 and MediaDive 1660, confirming that only the nine base compounds remain as top-level final-medium gram rows and all stock ingredients are compartment-scoped.

## Follow-up Checks

1. Run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_bap_psa_medium_for_frankia.yaml`.
2. Regenerate `data/merge_yaml/merged/modified_bap_psa_medium_for_frankia.yaml` and re-run the same validators on the generated record.
3. Manually verify the regenerated record against DSMZ Medium 1660 and MediaDive 1660 for the three stock addition volumes, stock-local water rows, the PSA carbon-source rows, and pH 6.3.
4. Verify that MediaDive solution 3183 is reused or faithfully copied instead of flattened as two final-medium grams-per-liter rows.

## Additional Notes

The DSMZ PDF at the record's stored source URL still resolves. The MediaDive REST record for `1660` also resolves and matches the PDF formulation, including the unusual chelated-iron autoclaving note.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
