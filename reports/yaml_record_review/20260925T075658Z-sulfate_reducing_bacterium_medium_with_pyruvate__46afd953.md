# YAML Record Review: SULFATE REDUCING BACTERIUM MEDIUM WITH PYRUVATE

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_pyruvate__46afd953.yaml` (`CultureMech:002901`)
- Started UTC: `2026-09-25T07:56:58Z`
- Finished UTC: `2026-09-25T07:57:31Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_pyruvate__46afd953.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/sulfate_reducing_bacterium_medium_with_pyruvate.yaml` |
| CultureMech ID | `CultureMech:002901` |
| Media term | `mediadive.medium:J553` |
| Original source | JCM `J553`, SULFATE REDUCING BACTERIUM MEDIUM WITH PYRUVATE |
| Merge fingerprint | `46afd953ba8cd9db576179446829a2e1196bbafd719cdc526399fcb44713c646` |
| Merged from | `sulfate_reducing_bacterium_medium_with_2_nacl_and_lactate`; `sulfate_reducing_bacterium_medium_with_lactate`; `sulfate_reducing_bacterium_medium_with_pyruvate` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` exited 0 with no diagnostics for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` exited 0 and wrote a header-only TSV with 0 errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record's primary identity is the MediaDive import of JCM 553, the pyruvate wrapper around JCM 552. The merge history also folds in the older MediaDive J552 lactate source and J627 2% NaCl lactate source, which should be distinct recipes.

Exact gitignore-independent searches with `--no-ignore --hidden` for `mediadive.medium:J553`, `CultureMech:002901`, `sulfate_reducing_bacterium_medium_with_pyruvate`, `sulfate_reducing_bacterium_medium_with_lactate`, and `sulfate_reducing_bacterium_medium_with_2_nacl_and_lactate` found the three older MediaDive sources, TOGO M554-M557, TOGO M639-M640, and the two generated pyruvate records that need to keep pyruvate/lactate and 2% NaCl boundaries separate.

Ingredient groundings inherited from JCM 552 are plausible in isolation, but the top-level formula contains `L-Sodium lactate` even though the JCM 553 source says to replace sodium lactate with sodium pyruvate.

## Evidence

The JCM 553 page and the MediaDive J553 REST payload both define the recipe as JCM 552 supplemented with final 30.0 g/L NaCl, with sodium lactate replaced by 1.9 g/L sodium pyruvate, and pH adjusted to 6.7.

The generated record preserves only part of that wrapper: `ph_value` is 6.7 and its single preparation step repeats the pyruvate wrapper text. The structured ingredient list still contains the copied JCM 552 `L-Sodium lactate` row at `2.29312 G_PER_L`, still contains only the copied base NaCl value at `9.97009 G_PER_L`, and has no sodium pyruvate row.

The generated record also retains stock rows copied from the old lactate composition, including vitamin and trace-element stock components at full stock strength, because the `copy_referenced_compositions` step copied from `CultureMech:002900` instead of rebuilding the JCM 553 final formula.

## Completeness

The generated record is not a faithful pyruvate recipe. The pH and wrapper comment are present, but the ingredient array still encodes the lactate base formula and stale stock expansions.

`target_organisms` is absent. The JCM and MediaDive medium pages identify a recipe but do not assert a source-backed organism that grew on it.

## Findings

- The defining replacement was not applied structurally: `L-Sodium lactate` remains in the ingredient list and sodium pyruvate at 1.9 g/L is absent.
- The final 30.0 g/L NaCl requirement was not applied; NaCl remains at the copied JCM 552 base value near 10 g/L.
- Three distinct MediaDive sources were merged into one generated pyruvate record: J552 lactate, J627 2% NaCl lactate, and J553 pyruvate.
- The vitamin and trace-element rows copied from the lactate base are full stock-strength rows, not final 1 ml/L contributions.
- Only the wrapper step is present; the pH 7.5 anaerobic preparation and separate lactate/cysteine autoclaving steps from JCM 552 were not converted into pyruvate-aware preparation steps.
- `NiCl2 x 6 H2O` remains grounded to an anhydrous nickel dichloride label in the copied trace-element stock rows.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/sulfate_reducing_bacterium_medium_with_pyruvate.yaml` or the MediaDive referenced-composition copy path, then regenerate `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_pyruvate__46afd953.yaml`.
- Start from the repaired JCM 552 base, then apply the JCM 553 wrapper structurally: use final 30.0 g/L NaCl, replace sodium lactate with 1.9 g/L sodium pyruvate, and retain pH 6.7.
- Preserve JCM 552 vitamin, FeCl2, and trace-element stocks as stock additions instead of copied full-strength top-level rows.
- Keep MediaDive J552, J627, and J553 as separate recipes or intentional variants; do not merge lactate and pyruvate media into the J553 record.
- Add pyruvate-aware preparation steps that combine the JCM 552 anaerobic workflow with the pH 6.7 final adjustment.
- Check exact hydrate grounding for `NiCl2 x 6 H2O` while repairing the trace-element stock.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `mediadive.medium:J553`, `CultureMech:002901`, `sulfate_reducing_bacterium_medium_with_pyruvate`, and the two lactate slugs to confirm the pyruvate recipe is no longer merged with lactate records.
- Compare the repaired MediaDive J553 output against TOGO M556/M557, which import the same JCM 553 pyruvate family through TOGO.

## Additional Notes

Empty optional fields that are unrelated to source-backed stock references and growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained MediaDive normalized source and the referenced-composition expansion path.
