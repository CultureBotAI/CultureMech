# YAML Record Review: MODIFIED MARINE MEDIUM FOR DETHIOSULFOBACTER

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_marine_medium_for_dethiosulfobacter__3e9fd0fe.yaml
- Started UTC: 2026-09-24T12:01:33Z
- Finished UTC: 2026-09-24T12:01:33Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_marine_medium_for_dethiosulfobacter__3e9fd0fe.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:015408` |
| Name | `modified_marine_medium_for_dethiosulfobacter` |
| Source identity | `mediadive.medium:J501` |
| Category | `specialized` |
| Maintained owner | `data/normalized_yaml/specialized/modified_marine_medium_for_dethiosulfobacter.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one MediaDive-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_marine_medium_for_dethiosulfobacter__3e9fd0fe.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_marine_medium_for_dethiosulfobacter__3e9fd0fe.yaml --out /private/tmp/modified_marine_medium_for_dethiosulfobacter__3e9fd0fe.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_marine_medium_for_dethiosulfobacter__3e9fd0fe.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_marine_medium_for_dethiosulfobacter__3e9fd0fe.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes MediaDive's JCM 501 copy of "MODIFIED MARINE MEDIUM FOR DETHIOSULFOBACTER". The inspected JCM page describes a multi-stock recipe with Solution A, Solution B, Solution C, Solution D, and Solution E, plus FeCl2, trace-element, selenite-tungstate, vitamin, and vitamin B12 stock additions inside Solution A. The generated artifact instead flattens nested MediaDive solution recipes into one top-level `ingredients` list.

An exact gitignore-independent search under `data/normalized_yaml/` found `data/normalized_yaml/bacterial/modified_marine_medium_for_dethiosulfobacter.yaml`, the TOGO M502 import of the same JCM 501 source with CultureMech ID `CultureMech:009892`. The two imports should be reconciled after the five final-solution additions and cross-referenced stock additions are represented consistently.

## Evidence

JCM 501 builds the final medium from Solution A, Solution B, Solution C, Solution D, and Solution E. Solution A contains salts, yeast extract, 760 ml distilled water, and 1 ml additions of FeCl2 solution, Trace element solution, Selenite-tungstate solution, Vitamin solution, and Vitamin B12 solution. Solution B contains 1.87 g sodium glutamate monohydrate in 100 ml distilled water, Solution C contains 5 g Na2S2O3 x 5 H2O in 100 ml distilled water, Solution D contains 2.5 g NaHCO3 in 30 ml distilled water, and Solution E contains 20 mg sodium dithionite in 10 ml distilled water.

MediaDive J501 exposes the same structure as separate solutions for Main sol. J501, Solution A, Solution B, Solution C, Solution D, Solution E, FeCl2 solution, Trace element solution, Selenite-tungstate solution, and Vitamin solution. The generated YAML lifts the component rows from those MediaDive solutions into top-level final-medium ingredients using stock `g_l` values, so sodium glutamate appears as 18.7 g/L, Na2S2O3 x 5 H2O appears as 50 g/L, NaHCO3 appears as 83.3333 g/L, and sodium dithionite appears as 2 g/L. It also treats the 1 ml Vitamin B12 solution addition as `Vitamin B12` at 1 g/L.

## Completeness

The record is incomplete because the final-medium Solution A through Solution E additions, five cross-referenced 1 ml stock additions, and all five distilled-water rows are not retained as structured solution components.

The inspected JCM, TOGO, and MediaDive recipe payloads did not expose organism-specific growth rows, and the generated record makes no target-organism claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The MediaDive J501 import flattens nested final-medium solutions and stock solutions into unsupported top-level final-medium ingredient rows. | JCM 501 assembles the medium from Solution A, Solution B, Solution C, Solution D, and Solution E; the generated YAML lists components from all of those stocks directly under `ingredients` with stock `g_l` values. | Repair `data/normalized_yaml/specialized/modified_marine_medium_for_dethiosulfobacter.yaml` so Solution A through Solution E remain structured additions. |
| blocker | Cross-referenced 1 ml stock additions are lost or represented at their stock concentrations. | JCM 501 adds FeCl2 solution, Trace element solution, Selenite-tungstate solution, Vitamin solution, and Vitamin B12 solution to Solution A at 1 ml each; the generated record emits the FeCl2, trace-element, selenite-tungstate, and vitamin stock ingredients as final-medium ingredients and emits Vitamin B12 as 1 g/L instead of a 1 ml stock addition. | Keep the five 1 ml stock additions as stock references inside Solution A before regeneration. |
| major | The generated record omits all explicit distilled-water rows. | JCM 501 lists 760 ml water in Solution A, 100 ml in Solution B, 100 ml in Solution C, 30 ml in Solution D, and 10 ml in Solution E; none of those rows appears in the generated YAML. | Preserve water inside each structured solution rather than dropping it during MediaDive import. |
| major | The same JCM 501 medium is maintained twice with different CultureMech IDs. | `mediadive.medium:J501` and `TOGO:M502` both derive from JCM 501 and generate same-name normalized records in different category folders. | Reconcile the specialized MediaDive J501 source with the bacterial TOGO M502 source after their nested solution structures are represented correctly. |

## Recommended Edits

1. Model the five final-medium Solution A through Solution E additions instead of flattening their contents into top-level final-medium `ingredients`.
2. Keep the FeCl2, Trace element, Selenite-tungstate, Vitamin, and Vitamin B12 additions as 1 ml stock additions inside Solution A.
3. Preserve the distilled-water rows inside Solutions A, B, C, D, and E.
4. Reconcile `mediadive.medium:J501` with `TOGO:M502` so JCM 501 has one CultureMech identity with both source accessions.
5. Regenerate the merged artifact and confirm stock `g_l` values are no longer emitted as final-medium concentrations.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated JCM 501 YAML.
- Re-open JCM 501, TOGO M502, and MediaDive J501 and confirm the generated record contains the five top-level Solution A through Solution E additions.
- Confirm `Vitamin B12`, trace-metal rows, selenite-tungstate rows, and vitamin rows are nested under their stock solutions, not top-level ingredients.
- Confirm the generated record preserves the five solution water rows, or a deliberately modeled equivalent that keeps those water amounts tied to their source solutions.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
