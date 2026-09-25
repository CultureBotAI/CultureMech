# YAML Record Review: Sulfate Reducing Bacterium Medium With Lactate

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_lactate__540ae3ce.yaml` (`CultureMech:009949`)
- Started UTC: `2026-09-25T07:55:44Z`
- Finished UTC: `2026-09-25T07:56:09Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_lactate__540ae3ce.yaml` |
| Normalized sources | `data/normalized_yaml/bacterial/TOGO_M555_Sulfate_Reducing_Bacterium_Medium_With_Lactate.yaml`; `data/normalized_yaml/bacterial/TOGO_M640_Sulfate-Reducing_Bacterium_Medium_With_2_NaCl_And_Lactate.yaml` |
| CultureMech ID | `CultureMech:009949` |
| Media term | `TOGO:M555` |
| Original source | JCM `JCM_M552-2`; merged with TOGO M640 from JCM `JCM_M627-2` |
| Merge fingerprint | `540ae3cea02c54c8bf0323591a339e003e1c5d53e439f6a02550eafc871bbf4f` |
| Merged from | `TOGO_M555_Sulfate_Reducing_Bacterium_Medium_With_Lactate`; `TOGO_M640_Sulfate-Reducing_Bacterium_Medium_With_2_NaCl_And_Lactate` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record primarily identifies TOGO M555/JCM_M552-2, the solid-agar variant of JCM 552. Its `merged_from` and synonyms also include TOGO M640/JCM_M627-2, the solid-agar variant of the 2% NaCl JCM 627 wrapper.

Exact gitignore-independent searches with `--no-ignore --hidden` for `TOGO:M555`, `TOGO:M640`, `JCM_M552-2`, `JCM_M627-2`, `CultureMech:009949`, and `sulfate_reducing_bacterium_medium_with_lactate` found this merged record, the unmerged normalized sources, the related TOGO M554 liquid base, the older MediaDive lactate source, and a later pyruvate record that copied from the older lactate source. No conflicting use of `CultureMech:009949` was found.

The core salt groundings are plausible. `L--Sodium lactate` still lacks a primary ChEBI term, and the formula must be separated into base and 2% NaCl branches before duplicate boundaries can be trusted.

## Evidence

JCM 552 defines the lactate base recipe and says that solid medium is prepared by adding 15 g/L BD-Difco agar. TOGO M555 imports that solid variant with 10 g/L NaCl from the JCM 552 table plus 15 g/L agar.

JCM 627 defines a different 2% final NaCl lactate recipe as Medium 552 supplemented with 2% final NaCl. TOGO M640 imports the solid form of that JCM 627 wrapper, but its extra NaCl is `VARIABLE` in normalized YAML. The generated record's merge history shows M555 and M640 were merged into one fingerprint, which collapses a base agar recipe with its 2% NaCl agar variant.

TOGO M555 keeps the 1 ml vitamin, 1 ml FeCl2, and 1 ml trace-element stock additions from JCM 552, and it retains JCM 552 preparation comments for pH 7.5, N2 autoclaving, and separate lactate/cysteine autoclaving. The generated YAML stores those three stock additions as empty `G_PER_L` solutions and has no `preparation_steps`.

## Completeness

The generated agar record is incomplete and over-merged. It has the 15 g/L agar row, but it loses the source preparation, cannot resolve the three stock additions, and treats the 2% NaCl agar variant as a synonym of the base agar recipe.

`target_organisms` is absent. JCM 552 and JCM 627 describe media recipes but do not assert source-backed growth evidence for this record.

## Findings

- TOGO M555 and TOGO M640 should not have merged: M640 is the agar form of JCM 627, whose defining source instruction is the JCM 552 base plus 2% final NaCl.
- The generated record has only the base 10 g/L NaCl row from M555; M640's 2% final NaCl supplement was already degraded to `VARIABLE` in its normalized source and is absent from the merged ingredient list.
- The base 1 mg resazurin ingredient is stored as `1 G_PER_L`, a 1000x unit slip.
- The 1 ml/L vitamin, FeCl2, and trace-element additions are empty solution records with `G_PER_L` units.
- `NaOH` and `N2` are `VARIABLE` top-level ingredients, losing their procedural roles as sterile 1 N NaOH for pH 7.5 readjustment and N2 for anaerobic autoclaving.
- Preparation steps are missing, including pH adjustment/readjustment, anaerobic autoclaving, and the separate lactate/cysteine autoclave step.

## Recommended Edits

- Repair M555 and M640 in `data/normalized_yaml/bacterial/` or the TOGO wrapper expansion path, then regenerate this merged YAML.
- Keep TOGO M555 as the JCM 552 agar recipe with 10 g/L NaCl and 15 g/L agar.
- Keep TOGO M640 as a separate JCM 627 agar recipe with the source-backed 2% final NaCl supplement represented numerically.
- Convert resazurin from 1 mg/L to `0.001 G_PER_L`.
- Represent the vitamin solution, FeCl2 solution, and trace-element solution as 1 ml/L stock additions or structured cross-references.
- Add pH 7.5, N2 autoclaving, separate lactate/cysteine autoclaving, sterile NaOH readjustment, and solid-medium agar preparation steps.
- Ground `L--Sodium lactate` to a ChEBI sodium L-lactate term.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `TOGO:M555`, `TOGO:M640`, `JCM_M552-2`, `JCM_M627-2`, and `sulfate_reducing_bacterium_medium_with_lactate` to confirm the base agar and 2% NaCl agar variants are no longer over-merged.
- Compare the repaired records with TOGO M554, M639, and copied MediaDive lactate/pyruvate records so stale base-lactate formulae are not propagated.

## Additional Notes

Empty optional fields that are unrelated to source-backed stock references and growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the normalized TOGO sources and the JCM wrapper expansion/merge path.
