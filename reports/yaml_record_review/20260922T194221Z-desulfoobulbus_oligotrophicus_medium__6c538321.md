# YAML Record Review: desulfoobulbus_oligotrophicus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfoobulbus_oligotrophicus_medium__6c538321.yaml
- Started UTC: 2026-09-22T19:42:28Z
- Finished UTC: 2026-09-22T19:42:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfoobulbus_oligotrophicus_medium__6c538321.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owner | `data/normalized_yaml/bacterial/desulfoobulbus_oligotrophicus_medium.yaml` |
| Related solution owners | `data/normalized_yaml/bacterial/mediadive_3861_Trace_vitamins.yaml`, `data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml` |
| Same-upstream sibling owner | `data/normalized_yaml/bacterial/TOGO_M1237_Desulfoobulbus_Oligotrophicus_Medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002327` |
| Label | `desulfoobulbus_oligotrophicus_medium` |
| Original label | `DESULFOOBULBUS OLIGOTROPHICUS MEDIUM` |
| Source identity | MediaDive J1155 / JCM Medium 1155 |
| Merge lineage | `merge_recipes.py` merged `desulfoobulbus_oligotrophicus_medium.yaml` into fingerprint `6c5383210d00f3af201339dce80c98ad84c1e97ae9143b082fe32f80d692e184` |

I read the full generated record, its maintained MediaDive normalized owner, the same-upstream TOGO M1237 owner, and the MediaDive solution records for solution IDs 3861 and 6187. A gitignore-independent exact search for the label, fingerprint, M1237, and J1155 found the same MediaDive and TOGO owners plus the sibling generated TOGO record `data/merge_yaml/merged/DESULFOOBULBUS_OLIGOTROPHICUS_MEDIUM.yaml`.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfoobulbus_oligotrophicus_medium__6c538321.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfoobulbus_oligotrophicus_medium__6c538321.yaml --out /private/tmp/desulfoobulbus_oligotrophicus_medium__6c538321.strict.tsv --workers 1 --quiet` | Passed; 0 errors |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfoobulbus_oligotrophicus_medium__6c538321.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfoobulbus_oligotrophicus_medium__6c538321.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The record denotes JCM Medium 1155 as mirrored through MediaDive. The generated `media_term`, normalized owner, MediaDive REST response, and live JCM page all agree on `J1155` / `GRMD=1155` and the `DESULFOOBULBUS OLIGOTROPHICUS MEDIUM` source label. The `ph_value: 7.6`, `composition_type: DEFINED`, and compatibility `medium_type: DEFINED` are supported by JCM and MediaDive.

The main salt CHEBI groundings match the JCM formula. The generated record's vitamin CHEBI groundings also match the ingredients in MediaDive solution 3861, but those vitamin rows are stock-solution constituents that have been promoted to top-level final-medium ingredients at stock concentrations.

## Evidence

JCM and MediaDive support the main base formula: 0.5 g each KH2PO4, K2HPO4, and NH4Cl; 5.0 g NaCl; 2.84 g Na2SO4; 0.3 g MgCl2 x 6H2O; 0.05 g CaCl2 x 2H2O; 0.4 g KCl; 1.0 ml trace element solution from JCM Medium 294; 1.0 mg resazurin; and 955 ml distilled water. MediaDive converts the gram and milligram rows to final g/L values over a 1010 ml final volume, and the generated record preserves those g/L values for the salts and resazurin.

JCM and MediaDive then add three post-autoclave stocks after cooling: 25.0 ml 8% NaHCO3, 20.0 ml 1 M sodium propionate, and 1.0 ml trace vitamins from JCM Medium 197. They add a fourth stock, 8.0 ml 5% Na2S x 9H2O, after the medium is anaerobically distributed under N2-CO2 and sealed. The generated record instead writes NaHCO3, sodium propionate, and Na2S x 9H2O as top-level `25`, `20`, and `8 G_PER_L` ingredients, dropping the stock strengths, milliliter units, and addition boundaries.

JCM and MediaDive support the three generated preparation steps: autoclaving the basal medium under N2-CO2 4:1, adding autoclaved or filter-sterilized post-autoclave solutions, anaerobic vessel distribution and sealing under the same gas mix, adding sulfide stored under N2, and readjusting the pH to 7.6 if needed.

MediaDive solution 3861 contains the Trace vitamins stock, but the generated MediaRecipe copies those ten vitamin stock concentrations into its top-level ingredient list. The generated 0.002 g/L biotin row, for example, is the 2 mg/L stock strength before a 1.0 ml/L addition, not the final medium concentration.

## Completeness

The generated record is incomplete for solution structure even though the source identity and main salts are sound. It has a `mediadive.solution:6187` row for `Trace element solution`, but the row has `name: Unknown solution`, `1 G_PER_L`, and no `composition`; the local `mediadive_6187_Trace_element_solution.yaml` stock is present but still carries `data_quality_flags: [incomplete_composition]` and a placeholder `ingredients:` list. Its `Trace vitamins` stock is not represented as a stock addition at all.

The empty `target_organisms` and `references` slots are not defects for this imported source recipe because JCM and MediaDive provide formulation evidence rather than primary growth evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Three milliliter stock additions are encoded as g/L final ingredients. | JCM J1155 adds 25.0 ml 8% NaHCO3, 20.0 ml 1 M sodium propionate, and 8.0 ml 5% Na2S x 9H2O. The generated target has `NaHCO3`, `Sodium propionate`, and `Na2S x 9 H2O` rows at `25`, `20`, and `8 G_PER_L`. | `data/normalized_yaml/bacterial/desulfoobulbus_oligotrophicus_medium.yaml` and MediaDive main-solution import logic. |
| Major | The Trace vitamins stock is flattened into top-level ingredient rows. | MediaDive J1155 adds 1.0 ml of solution 3861; the generated target instead places the 3861 stock's biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid concentrations directly under `ingredients`. | `data/normalized_yaml/bacterial/desulfoobulbus_oligotrophicus_medium.yaml`, `data/normalized_yaml/bacterial/mediadive_3861_Trace_vitamins.yaml`, and the MediaDive solution-flattening path. |
| Major | The Trace element solution addition is unresolved in the MediaRecipe and only partially curated as a local SolutionRecipe. | JCM uses 1.0 ml Trace element solution from Medium 294. The generated target has a `mediadive.solution:6187` row but no composition and a `G_PER_L` unit; `mediadive_6187_Trace_element_solution.yaml` exists but remains flagged as incomplete. | `data/normalized_yaml/bacterial/desulfoobulbus_oligotrophicus_medium.yaml` and `data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml`. |
| Major | The same JCM 1155 recipe remains split into two generated records. | The MediaDive normalized file cites JCM J1155, while TOGO M1237 cites `JCM_M1155`; both point at `GRMD=1155`, but they generate separate merge outputs: this record and `DESULFOOBULBUS_OLIGOTROPHICUS_MEDIUM.yaml`. | The MediaDive and TOGO normalized owners plus merge-deduplication rules. |
| Minor | The maintained MediaDive main-solution stock still stores source volumes under misleading percent units. | `mediadive_5265_Main_sol_J1155.yaml` uses `PERCENT_V_V` for the 955 ml water row and for 1, 25, 20, and 8 ml stock additions even though the values are milliliters per liter over the 1010 ml final volume. | `data/normalized_yaml/bacterial/mediadive_5265_Main_sol_J1155.yaml` and MediaDive SolutionRecipe import logic. |

## Recommended Edits

1. Move the 8% NaHCO3, 1 M sodium propionate, 5% Na2S x 9H2O, Trace vitamins, and Trace element solution rows out of top-level final `ingredients` and into solution additions with milliliter volumes, stock strengths, and preparation timing retained.
2. Link `mediadive.solution:3861` as a 1.0 ml/L Trace vitamins stock instead of flattening its vitamin constituents into the J1155 medium.
3. Complete and link `mediadive.solution:6187` as the JCM Medium 294 Trace element solution, or leave the cross-reference explicit without an empty `Unknown solution` row until the stock is curated.
4. Repair `mediadive_5265_Main_sol_J1155.yaml` so milliliter stock additions and the 955 ml water amount are represented with volume semantics rather than `PERCENT_V_V`.
5. Collapse TOGO M1237 and MediaDive J1155 into one same-upstream generated record, or add a merge rule that recognizes `JCM_M1155` and `mediadive.medium:J1155` as the same source before regenerating `data/merge_yaml/merged/`.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on the edited MediaDive normalized record, affected stock SolutionRecipes, the TOGO sibling if edited, and the regenerated merged output.
2. Compare the regenerated J1155 record against the live JCM page, checking each gram/milligram basal component, each milliliter post-autoclave stock, the N2-CO2 preparation sequence, and pH 7.6.
3. Confirm the regenerated MediaRecipe has no top-level vitamin stock constituents and no `25`, `20`, or `8 G_PER_L` rows for bicarbonate, propionate, or sulfide.
4. Confirm merge regeneration leaves one JCM 1155 generated record rather than separate MediaDive and TOGO fingerprints.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfoobulbus_oligotrophicus_medium__6c538321` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
