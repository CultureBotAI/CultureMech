# YAML Record Review: Modified Melin Norkrans (MMN) Media

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_melin_norkrans_mmn_media.yaml
- Started UTC: 2026-09-24T12:09:03Z
- Finished UTC: 2026-09-24T12:09:03Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_melin_norkrans_mmn_media.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:008678` |
| Name | `modified_melin_norkrans_mmn_media` |
| Source identity | `TOGO:M2088` |
| Category | `bacterial` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_melin_norkrans_mmn_media.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one TOGO-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_melin_norkrans_mmn_media.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_melin_norkrans_mmn_media.yaml --out /private/tmp/modified_melin_norkrans_mmn_media.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_melin_norkrans_mmn_media.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_melin_norkrans_mmn_media.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes TOGO M2088, derived from NBRC 1398 "Modified Melin Norkrans (MMN) Media". The name, agar state, and unadjusted-pH absence are consistent with the inspected NBRC and TOGO sources, but several source units were not converted correctly.

An exact gitignore-independent search under `data/normalized_yaml/` found no second maintained YAML source with the exact normalized name `modified_melin_norkrans_mmn_media`.

## Evidence

NBRC 1398 lists Malt extract 3 g, Glucose 10 g, Amonium phosphate-dibasic 0.25 g, Potassium Phosphate monobasic crystal 0.5 g, Magnesium sulfate 0.15 g, CaCl2 50 mg, FeCl3 (1% aqueous solution) 1 ml, Distilled water 1 L, and Agar 15 g. The source also says pH is not adjusted.

TOGO M2088 preserves the same source quantities and units. The generated YAML instead represents the 50 mg CaCl2 row as `50` G_PER_L, represents 1 L distilled water as `1` G_PER_L, and moves 1 ml FeCl3 (1% aqueous solution) into `solutions` with an empty composition and `1` G_PER_L.

## Completeness

The record carries all source row labels, but CaCl2, Distilled water, and FeCl3 solution require unit and stock-structure repair before the generated amounts match NBRC 1398.

The inspected NBRC and TOGO payloads did not expose organism-specific growth rows, and the generated record makes no target-organism claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The CaCl2 source amount is inflated 1000-fold. | NBRC 1398 and TOGO M2088 list CaCl2 at 50 mg; the generated YAML records CaCl2 as 50 G_PER_L. | Convert the NBRC milligram row to 0.05 g/L in `data/normalized_yaml/bacterial/modified_melin_norkrans_mmn_media.yaml`, then regenerate. |
| major | The 1 L Distilled water row is encoded as 1 G_PER_L. | NBRC 1398 and TOGO M2088 list Distilled water at 1 L, which should be represented as 1000 ml/L or the repository's standard water equivalent, not 1 G_PER_L. | Fix the TOGO `L` unit conversion for water in the maintained source. |
| major | The FeCl3 stock addition has the wrong unit and no stock strength. | The source adds 1 ml FeCl3 (1% aqueous solution); the generated `solutions` row records value `1` with unit G_PER_L and an empty `composition`. | Represent the row as a 1 ml 1% FeCl3 aqueous-solution addition. |

## Recommended Edits

1. Convert CaCl2 from 50 mg to 0.05 g/L.
2. Convert the 1 L distilled-water row to the standard 1 L water representation.
3. Model FeCl3 (1% aqueous solution) as a 1 ml stock addition with the 1% stock concentration retained.
4. Regenerate the merged artifact and confirm the physical state remains `SOLID_AGAR` and no pH is assigned.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated NBRC 1398 YAML.
- Re-open NBRC 1398 and TOGO M2088 and confirm CaCl2, FeCl3, and Distilled water have the corrected units.
- Confirm the FeCl3 row is not left as an empty `Unknown solution` placeholder.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
