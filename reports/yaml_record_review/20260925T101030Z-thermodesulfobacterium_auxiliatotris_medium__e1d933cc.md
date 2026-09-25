# YAML Record Review: thermodesulfobacterium_auxiliatotris_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_auxiliatotris_medium__e1d933cc.yaml
- Started UTC: 2026-09-25T10:10:04Z
- Finished UTC: 2026-09-25T10:10:30Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfobacterium_auxiliatotris_medium__e1d933cc`, which represents direct MediaDive/JCM medium `J1229` as `CultureMech:002395`.

## Validation

- Schema: Passed with `No issues found`.
- Strict validation: Passed with 1 file, 0 error files, and 0 rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The record identity, `J1229` MediaDive term, pH 7.0, and JCM 1229 note agree with the direct MediaDive import branch. An exact ignored-inclusive search for `mediadive.medium:J1229`, `GRMD=1229`, and `TOGO_M1321` found a separate uppercase TOGO branch, `TOGO_M1321_Thermodesulfobacterium_Auxiliatotris_Medium`, for the same source recipe. That branch remains separately merged as `data/merge_yaml/merged/THERMODESULFOBACTERIUM_AUXILIATOTRIS_MEDIUM.yaml`. The JCM `GRMD=1229` page currently returns no medium content, so the MediaDive and local TOGO imports are the available JCM-derived source traces for this review.

## Evidence

MediaDive J1229 stores a 1030 ml main solution with basal salts, 5 ml of Mineral solution 5001, 10 ml of Solution A, 1 ml of 1.0 M sodium acetate, 1 ml of 1.0 M sodium thiosulfate, 2 ml of 5% `Na2S x 9 H2O`, 1 ml of 8% `NaHCO3`, and small separate `MgSO4 x 7 H2O` and `CaCl2 x 2 H2O` additions. The nested Mineral solution stock contains 3.7 g/L EDTA, 1.1 g/L `FeSO4 x 7 H2O`, and mg/L trace salts. `data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml` shows Solution A is a 500 ml organic/salt stock with yeast extract, casamino acids, sodium glutamate, sodium citrate, magnesium sulfate, calcium sulfate, potassium chloride, and sodium chloride.

## Completeness

The target has a placeholder `solutions` entry for Solution A, but the final medium does not preserve the 10 ml Solution A addition or the linked Solution A composition. The imported final ingredient list is also incomplete because it flattens the 5 ml Mineral solution stock into direct ingredients and converts four liquid stock additions to bare g/L ingredient rows.

## Findings

- High: the 5 ml Mineral solution stock was flattened into final-medium ingredients at full stock concentration. EDTA appears as 3.7 g/L and `FeSO4 x 7 H2O` as 1.1 g/L in the target even though those values belong to the nested 1 L Mineral solution stock.
- High: Solution A was migrated to an empty placeholder with `concentration: 10 G_PER_L` and a note pointing to `mediadive_5342_Solution_A.yaml`; the source addition is 10 ml of a 500 ml stock, not 10 g/L.
- High: the 1 ml 1.0 M sodium acetate, 1 ml 1.0 M sodium thiosulfate, 2 ml 5% `Na2S x 9 H2O`, and 1 ml 8% `NaHCO3` additions were converted to 1, 1, 2, and 1 g/L top-level ingredient concentrations, losing the molarity or percent strength of each source stock.
- Medium: the TOGO M1321 import of the same JCM-derived medium is unmerged with the direct MediaDive/JCM J1229 branch, leaving duplicate source coverage split between uppercase and lowercase generated records.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/thermodesulfobacterium_auxiliatotris_medium.yaml` so the 5 ml Mineral solution, 10 ml Solution A, and acetate, thiosulfate, sulfide, and bicarbonate stock additions stay modeled as stock additions with source units.
- Link Solution A to `data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml` by identity or embed its composition; do not encode the 10 ml addition as `10 G_PER_L`.
- Fix the MediaDive import path that converts milliliter stock additions to g/L rows without carrying stock concentration metadata.
- Canonicalize the TOGO M1321 and direct MediaDive/JCM J1229 branches before generation so the JCM-derived recipe has one generated merged target.

## Follow-up Checks

- Regenerate merged YAML and verify Mineral solution, Solution A, and the four anaerobic stock additions survive as nested additions rather than top-level g/L ingredients.
- Confirm the corrected J1229 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:J1229`, `GRMD=1229`, and `TOGO_M1321` to confirm the duplicate uppercase generated record has collapsed into the canonical J1229 output.

## Additional Notes

None found.
