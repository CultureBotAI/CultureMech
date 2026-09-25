# YAML Record Review: MODIFIED MEDIUM FOR MARINE SPIROCHAETES

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_medium_for_marine_spirochaetes__cef23954.yaml
- Started UTC: 2026-09-24T12:07:08Z
- Finished UTC: 2026-09-24T12:07:08Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_medium_for_marine_spirochaetes__cef23954.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:015388` |
| Name | `modified_medium_for_marine_spirochaetes` |
| Source identity | `mediadive.medium:J1172` |
| Category | `specialized` |
| Maintained owner | `data/normalized_yaml/specialized/modified_medium_for_marine_spirochaetes.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one MediaDive-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_medium_for_marine_spirochaetes__cef23954.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_medium_for_marine_spirochaetes__cef23954.yaml --out /private/tmp/modified_medium_for_marine_spirochaetes__cef23954.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_medium_for_marine_spirochaetes__cef23954.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_medium_for_marine_spirochaetes__cef23954.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes MediaDive's JCM 1172 copy of "MODIFIED MEDIUM FOR MARINE SPIROCHAETES". Its main salt/nutrient amounts, pH, and N2-CO2 handling agree with the inspected JCM source, but its stock solution boundaries do not: the generated record flattens trace-mineral and trace-vitamin stocks and turns three after-autoclave solution additions into apparent grams-per-liter ingredient rows.

An exact gitignore-independent search under `data/normalized_yaml/` found `data/normalized_yaml/bacterial/modified_medium_for_marine_spirochaetes.yaml`, the TOGO M1255 import of the same JCM 1172 source with CultureMech ID `CultureMech:007786`. The two imports should be reconciled after the five source solution additions are represented consistently.

## Evidence

JCM 1172 lists a main recipe with NH4Cl, KH2PO4, NaCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, yeast extract, maltose, 1 ml Trace mineral solution, 2 ml Trace vitamins solution, 1 mg Resazurin, and 1 L Distilled water. After boiling, cooling under N2-CO2, dispensing, and autoclaving, the source instructs adding 25 ml 8% NaHCO3 solution, 6 ml 5% L-Cysteine HCl x H2O solution, and 6 ml 5% Na2S x 9 H2O solution per liter.

MediaDive J1172 exposes Trace mineral solution and Trace vitamins solution as nested stock recipes. The generated YAML promotes every trace-metal and vitamin stock component to top-level final-medium ingredients at stock concentrations. It also stores the after-autoclave 25 ml, 6 ml, and 6 ml solution additions as `NaHCO3` at 25 g/L, `L-Cysteine HCl x H2O` at 6 g/L, and `Na2S x 9 H2O` at 6 g/L instead of retaining the source solution volumes and concentrations.

## Completeness

The generated record is incomplete because it lacks the explicit 1 ml Trace mineral solution, 2 ml Trace vitamins solution, 25 ml 8% NaHCO3 solution, 6 ml 5% L-cysteine solution, 6 ml 5% sulfide solution, and 1 L Distilled water source rows.

The inspected JCM, TOGO, and MediaDive payloads did not expose organism-specific growth rows, and the generated record makes no target-organism claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The MediaDive J1172 import flattens the Trace mineral and Trace vitamins stocks into unsupported top-level ingredient rows. | JCM 1172 adds Trace mineral solution at 1 ml and Trace vitamins solution at 2 ml; the generated YAML emits all trace-metal and vitamin stock constituents as final-medium ingredients. | Repair `data/normalized_yaml/specialized/modified_medium_for_marine_spirochaetes.yaml` so both trace stocks remain structured additions, then regenerate. |
| blocker | The three after-autoclave percent solutions are modeled as pure final-medium ingredients. | JCM 1172 adds 25 ml 8% NaHCO3 solution, 6 ml 5% L-cysteine solution, and 6 ml 5% Na2S x 9 H2O solution per liter after autoclaving; the generated record emits `NaHCO3` at 25 g/L, `L-Cysteine HCl x H2O` at 6 g/L, and `Na2S x 9 H2O` at 6 g/L. | Preserve these as solution additions with their source percentages and addition volumes. |
| major | The generated record omits the 1 L Distilled water row. | JCM 1172 and MediaDive J1172 both list Distilled water in the main recipe; no water row appears in the generated YAML. | Preserve the main water row during MediaDive import. |
| major | The same JCM 1172 medium is maintained twice with different CultureMech IDs. | `mediadive.medium:J1172` and `TOGO:M1255` both derive from JCM 1172 and generate same-name normalized records in different category folders. | Reconcile the specialized MediaDive J1172 source with the bacterial TOGO M1255 source after their solution additions are represented correctly. |

## Recommended Edits

1. Restore the 1 ml Trace mineral solution and 2 ml Trace vitamins solution additions with their nested stock compositions.
2. Represent the 25 ml 8% NaHCO3, 6 ml 5% L-cysteine, and 6 ml 5% sulfide rows as solution additions, not as grams-per-liter ingredient concentrations.
3. Preserve the main 1 L Distilled water row.
4. Reconcile `mediadive.medium:J1172` with `TOGO:M1255` so JCM 1172 has one CultureMech identity with both source accessions.
5. Regenerate the merged artifact and confirm stock components no longer appear as top-level final-medium ingredients.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated JCM 1172 YAML.
- Re-open JCM 1172, TOGO M1255, and MediaDive J1172 and confirm the generated record keeps all five per-liter solution additions.
- Confirm trace-metal and trace-vitamin components are nested under their stock solutions, not top-level final-medium ingredients.
- Confirm NaHCO3, L-Cysteine HCl x H2O, and Na2S x 9 H2O are modeled as percent-solution additions with 25 ml, 6 ml, and 6 ml addition volumes.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
