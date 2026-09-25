# YAML Record Review: MODIFIED MAKKAR'S MEDIUM C

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_makkars_medium_c__6e4cba69.yaml
- Started UTC: 2026-09-24T11:45:25Z
- Finished UTC: 2026-09-24T11:45:25Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_makkars_medium_c__6e4cba69.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:002381` |
| Name | `modified_makkars_medium_c` |
| Source identity | `mediadive.medium:J1212` |
| Category | `bacterial` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_makkars_medium_c.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one MediaDive-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_makkars_medium_c__6e4cba69.yaml` exited 0 with no diagnostics. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_makkars_medium_c__6e4cba69.yaml --out /private/tmp/modified_makkars_medium_c__6e4cba69.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_makkars_medium_c__6e4cba69.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_makkars_medium_c__6e4cba69.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes MediaDive's JCM 1212 copy of "MODIFIED MAKKAR'S MEDIUM C". Its `mediadive.medium:J1212` identity, title, category, and liquid complex-medium classification agree with the inspected MediaDive REST payload.

An exact gitignore-independent search under `data/normalized_yaml/bacterial/` also found `data/normalized_yaml/bacterial/TOGO_M1299_Modified_Makkar_s_Medium_C.yaml`, which is the TOGO M1299 import of the same old JCM `JCM_M1212` recipe with CultureMech ID `CultureMech:007832`. The two same-slug JCM 1212 imports generated separate merged artifacts because the importers flattened the stock recipe differently instead of reconciling source accessions for one medium.

## Evidence

MediaDive J1212 supports the same nested structure as the TOGO M1299 archive: a main solution with 650 ml distilled water, 2.5 g yeast extract, 10 g Casitone, 6 g NaHCO3, 1 g L-cysteine HCl x H2O, 1 mg resazurin, 150 ml Solution I, 150 ml Solution II, 50 ml clarified rumen fluid, CO2, and N2, followed after autoclaving by 20 ml of 0.2 M cellobiose solution per liter.

MediaDive also exposes stock solution recipes, and all three are present as standalone normalized SolutionRecipes:

| MediaDive solution | Local file | Source contents |
|---|---|---|
| `mediadive.solution:5334` | `data/normalized_yaml/bacterial/mediadive_5334_Main_sol_J1212.yaml` | main solution additions and 1020 ml original volume |
| `mediadive.solution:5335` | `data/normalized_yaml/bacterial/mediadive_5335_Solution_I.yaml` | 3 g K2HPO4 in 1 L distilled water |
| `mediadive.solution:5336` | `data/normalized_yaml/bacterial/mediadive_5336_Solution_II.yaml` | 3 g KH2PO4, 6 g `(NH4)2SO4`, 6 g NaCl, 0.6 g MgSO4 x 7 H2O, 0.6 g CaCl2 x 2 H2O in 1 L distilled water |

The generated MediaRecipe flattens K2HPO4, KH2PO4, `(NH4)2SO4`, NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O into top-level ingredients at their stock concentrations. The final medium should instead represent 150 ml of Solution I and 150 ml of Solution II as main-medium additions or explicitly compute diluted final concentrations.

The generated MediaRecipe also represents the cellobiose addition as `Cellobiose` at `20 G_PER_L`. The source supports 20 ml of a 0.2 M cellobiose solution per liter, not 20 g cellobiose per liter.

The direct JCM CGI URL still named by MediaDive was inspected but now returns `Nothing found` for medium number 1212.

## Completeness

The record is incomplete because it drops all nested stock-solution references from the medium. Its sibling MediaDive `SolutionRecipe` YAML files preserve useful pieces of the stock structure, but the generated medium neither links to them nor preserves the 150 ml/150 ml stock addition amounts.

No target organism claims were expected from the inspected MediaDive recipe payload.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The MediaDive JCM 1212 medium flattens nested stock recipes into unsupported top-level final-medium ingredients. | MediaDive J1212 adds 150 ml Solution I and 150 ml Solution II to the main solution; the generated YAML stores their stock recipe components as top-level ingredients at stock concentrations and has no `solutions` entries or SolutionRecipe references. | Update `data/normalized_yaml/bacterial/modified_makkars_medium_c.yaml` and the MediaDive medium importer/merger to reference `mediadive.solution:5335` and `mediadive.solution:5336` with the correct 150 ml addition amounts. |
| blocker | The cellobiose addition has the wrong unit and magnitude. | MediaDive encodes 20 ml of 0.2 M cellobiose solution added after autoclaving; the generated record encodes `Cellobiose` at `20 G_PER_L`. | Preserve the 0.2 M cellobiose stock addition in `data/normalized_yaml/bacterial/modified_makkars_medium_c.yaml` instead of flattening the 20 ml volume into a gram-per-liter ingredient. |
| major | The same JCM M1212 medium is maintained twice with different CultureMech IDs. | The MediaDive source is `mediadive.medium:J1212`; the TOGO source `TOGO:M1299` declares original source `JCM_M1212` and has the same medium name but a different CultureMech ID. | Reconcile `data/normalized_yaml/bacterial/modified_makkars_medium_c.yaml` with `data/normalized_yaml/bacterial/TOGO_M1299_Modified_Makkar_s_Medium_C.yaml` after both import paths preserve nested stock recipes. |

## Recommended Edits

1. Represent the MediaDive main recipe as additions of Solution I, Solution II, rumen fluid, and 0.2 M cellobiose solution with the original ml quantities.
2. Link Solution I and Solution II from the MediaRecipe to the existing MediaDive SolutionRecipe records or an equivalent maintained stock representation.
3. Remove stock-only salts from the top-level final-medium ingredient list unless final concentrations are explicitly calculated from a source volume model.
4. Preserve the 20 ml of 0.2 M cellobiose as a stock addition instead of `20 G_PER_L` cellobiose.
5. Reconcile the duplicate TOGO and MediaDive imports of JCM 1212 so the merged output has one CultureMech identity and both source accessions.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on `data/merge_yaml/merged/modified_makkars_medium_c__6e4cba69.yaml`.
- Re-open the MediaDive J1212 REST payload and confirm the generated YAML preserves Solution I, Solution II, clarified rumen fluid, and 0.2 M cellobiose at the correct main-medium amounts.
- Confirm the generated `modified_makkars_medium_c` outputs no longer contain top-level 3 `G_PER_L` K2HPO4, 3 `G_PER_L` KH2PO4, 20 `G_PER_L` cellobiose, or two distinct CultureMech IDs for the same JCM 1212 identity.
- Run an exact gitignore-independent search for `JCM_M1212`, `J1212`, `TOGO:M1299`, and `mediadive.medium:J1212` under `data/normalized_yaml/` to confirm the source identities have been reconciled.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
- Direct JCM lookup for `GRMD=1212` is no longer sufficient for this review because JCM returned `Nothing found`; MediaDive REST still preserved the old JCM formula.
