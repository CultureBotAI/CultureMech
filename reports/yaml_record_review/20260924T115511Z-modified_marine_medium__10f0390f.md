# YAML Record Review: MODIFIED MARINE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_marine_medium__10f0390f.yaml
- Started UTC: 2026-09-24T11:55:11Z
- Finished UTC: 2026-09-24T11:55:11Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_marine_medium__10f0390f.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:015405` |
| Name | `modified_marine_medium` |
| Source identity | `mediadive.medium:J416` |
| Category | `specialized` |
| Maintained owner | `data/normalized_yaml/specialized/modified_marine_medium.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one MediaDive-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_marine_medium__10f0390f.yaml` exited 0 with no diagnostics. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_marine_medium__10f0390f.yaml --out /private/tmp/modified_marine_medium__10f0390f.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_marine_medium__10f0390f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_marine_medium__10f0390f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes MediaDive's JCM 416 copy of "MODIFIED MARINE MEDIUM". Its pH and most main-salt identities agree with the inspected MediaDive/JCM source, but its ingredient list conflates a referenced vitamin stock with the final medium and drops another referenced stock entirely.

An exact gitignore-independent search under `data/normalized_yaml/` found `data/normalized_yaml/bacterial/modified_marine_medium.yaml`, the TOGO M414 import of the same old JCM 416 source with CultureMech ID `CultureMech:009799`. The two imports should eventually collapse to one JCM 416 identity after their stock boundaries are repaired.

## Evidence

JCM 416 and MediaDive J416 both list the main recipe with NaCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, CaCl2 x 2 H2O, KCl, KH2PO4, `(NH4)2SO4`, NaBr, SrCl2 x 6 H2O, yeast extract, Na2SeO4, DL-sodium malate, KNO3, 10 ml Trace vitamins, 10 ml Trace mineral solution, L-cysteine HCl x H2O, and 1 L distilled water. The source protocol adjusts pH to 6.5, autoclaves under N2, adds sterile L-cysteine after autoclaving, and pressurizes inoculated vessels to 100 kPa N2.

MediaDive J416 exposes Trace vitamins as a separate stock recipe and carries Trace mineral solution as a separate solution addition with a source note. The generated YAML instead promotes all ten Trace vitamins components to top-level final-medium ingredients at stock concentrations, omits the 10 ml Trace mineral solution addition, and omits the 1 L distilled-water row.

## Completeness

The generated record is incomplete because it lacks two explicit final-medium additions, `Trace vitamins` and `Trace mineral solution`, and loses the main water row.

The inspected source did not expose organism-specific growth rows for this medium, and the record makes no target-organism claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The MediaDive J416 import flattens the Trace vitamins stock into unsupported final-medium ingredient rows. | JCM 416 adds 10 ml Trace vitamins; MediaDive exposes a separate Trace vitamins stock; the generated YAML promotes the ten vitamin-stock components to top-level ingredients at stock concentrations. | Repair `data/normalized_yaml/specialized/modified_marine_medium.yaml` so Trace vitamins remains a 10 ml stock addition, then regenerate. |
| major | The generated record omits the 10 ml Trace mineral solution addition. | JCM 416 and MediaDive J416 list a 10 ml Trace mineral solution addition; the generated YAML only carries a preparation note about trace minerals and no ingredient or `solutions` entry for the addition. | Add a structured Trace mineral solution reference to the maintained MediaDive J416 source. |
| major | The generated record omits 1 L distilled water. | JCM 416 and MediaDive J416 both list Distilled water; neither the specialized normalized source nor the generated record has a water row. | Preserve the MediaDive 1 L water row in the maintained source. |
| major | The same JCM 416 medium is maintained twice with different CultureMech IDs. | `mediadive.medium:J416` and `TOGO:M414` both derive from JCM 416 and generate same-slug normalized records in different category folders. | Reconcile the specialized MediaDive J416 source with the bacterial TOGO M414 source after their stock solution structures are represented correctly. |

## Recommended Edits

1. Replace flattened Trace vitamins ingredient rows with a 10 ml/L stock addition and a structured stock composition.
2. Add the missing Trace mineral solution and Distilled water source rows to the maintained MediaDive J416 record.
3. Reconcile `mediadive.medium:J416` with `TOGO:M414` so JCM 416 has one CultureMech identity with both source accessions.
4. Rerun the merge so the generated YAML keeps both trace-stock additions and no longer treats stock vitamin concentrations as final-medium concentrations.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated JCM 416 YAML.
- Re-open JCM 416, TOGO M414, and MediaDive J416 and confirm the generated YAML contains one 10 ml/L Trace vitamins addition, one 10 ml/L Trace mineral solution addition, and a 1 L water row.
- Confirm no generated `modified_marine_medium` row has Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium pantothenate, Vitamin B12, p-Aminobenzoic acid, or Lipoic acid as top-level final-medium ingredients.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
- Trace minerals need a dedicated follow-up against the exact JCM stock source because JCM 416 and the TOGO M414 payload point to different source-number namespaces for that stock.
