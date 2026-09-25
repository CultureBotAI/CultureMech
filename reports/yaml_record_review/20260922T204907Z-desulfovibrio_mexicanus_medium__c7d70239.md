# YAML Record Review: DESULFOVIBRIO MEXICANUS MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_mexicanus_medium__c7d70239.yaml`
- Started UTC: 2026-09-22T20:49:07Z
- Finished UTC: 2026-09-22T20:50:10Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:003100` for `desulfovibrio_mexicanus_medium__c7d70239`, a MediaDive import of JCM Medium J757.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `mediadive.medium:J757`, `DESULFOVIBRIO MEXICANUS MEDIUM`, with JCM GRMD 757 in `notes`.

A gitignore-independent exact lookup found the MediaDive normalized source and a TOGO M782 companion that also imports JCM_M757. The TOGO provider currently generates separately as `data/merge_yaml/merged/DESULFOVIBRIO_MEXICANUS_MEDIUM.yaml`.

## Evidence

MediaDive J757 represents the main solution as 900 ml water, seven basal salts, yeast extract, 1 ml FeCl2 solution, 1 ml Trace element solution, cysteine, resazurin, 50 ml 8% sodium bicarbonate, 100 ml Substrate solution, and 10 ml 3% sodium sulfide.

The Substrate solution is a 100 ml stock containing 12.5 g L-sodium lactate, 12.5 g sodium thiosulfate pentahydrate, and water. FeCl2 solution and Trace element solution are separate 1000 ml stocks.

## Completeness

The target preserves the pH 7.0 and the high-level preparation instructions for autoclaving the basal medium, adding sterile anaerobic stocks after cooling, and readjusting pH.

The composition is incomplete because it has no `solutions` section. FeCl2 solution, Trace element solution, Substrate solution, bicarbonate, and sulfide were all flattened to top-level ingredient rows, and the water rows for the main solution and stocks are absent.

## Findings

- High: FeCl2 solution and Trace element solution were flattened. HCl, ferrous chloride, zinc, manganese, borate, cobalt, copper, nickel, and molybdate are listed at stock strengths instead of inside two 1 ml/L additions.
- High: The 100 ml Substrate solution was flattened. L-sodium lactate and sodium thiosulfate pentahydrate are listed at 125 G/L stock strengths even though the final medium receives 100 ml of that stock per liter.
- High: The 50 ml 8% sodium bicarbonate and 10 ml 3% sodium sulfide post-autoclave additions were copied into 50 G/L and 10 G/L top-level rows.
- Medium: The 900 ml basal water row, 100 ml Substrate solution water row, 990 ml FeCl2 solution water row, and Trace element solution water row are absent.
- Medium: The exact TOGO M782 JCM_M757 duplicate remains split from the MediaDive record and carries empty `Unknown solution` stubs for FeCl2 solution, Trace element solution, bicarbonate, sulfide, and Substrate solution.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_mexicanus_medium.yaml` so JCM J757 has structured FeCl2, Trace element, Substrate, bicarbonate, and sulfide stock additions with source volumes.
- Move the FeCl2, Trace element, and Substrate solution recipes into subordinate `solutions` entries with water rows.
- Convert or model the 50 ml 8% bicarbonate and 10 ml 3% sulfide rows as final post-autoclave stock additions rather than G/L masses.
- Repair `data/normalized_yaml/bacterial/TOGO_M782_Desulfovibrio_Mexicanus_Medium.yaml` so it no longer has empty solution stubs and can merge with the repaired MediaDive J757 import.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm JCM M757 is no longer split across the MediaDive and TOGO generated records unless they are deliberately retained as documented source duplicates.
- Verify the regenerated main recipe keeps 900 ml basal water, 1 ml FeCl2 solution, 1 ml Trace element solution, 50 ml bicarbonate, 100 ml Substrate solution, and 10 ml sulfide.

## Additional Notes

None found.
