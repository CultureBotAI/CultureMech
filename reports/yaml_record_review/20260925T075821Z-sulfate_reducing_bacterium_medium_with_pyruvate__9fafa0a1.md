# YAML Record Review: Sulfate Reducing Bacterium Medium With Pyruvate

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_pyruvate__9fafa0a1.yaml` (`CultureMech:009951`)
- Started UTC: `2026-09-25T07:58:21Z`
- Finished UTC: `2026-09-25T07:58:52Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_pyruvate__9fafa0a1.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/TOGO_M557_Sulfate_Reducing_Bacterium_Medium_With_Pyruvate.yaml` |
| CultureMech ID | `CultureMech:009951` |
| Media term | `TOGO:M557` |
| Original source | JCM `JCM_M553-2`, Sulfate Reducing Bacterium Medium With Pyruvate |
| Merge fingerprint | `9fafa0a147d91880b5068333cd4754cb03d83853427c84f6c0f2a42a8b8e5c64` |
| Merged from | `TOGO_M557_Sulfate_Reducing_Bacterium_Medium_With_Pyruvate` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected stable identifier, TOGO M557 media term, JCM_M553-2 source, and single-source merge fingerprint. M557 is the solid-agar TOGO import of the JCM 553 pyruvate wrapper.

Exact gitignore-independent searches with `--no-ignore --hidden` for `TOGO:M557`, `JCM_M553-2`, `CultureMech:009951`, and `sulfate_reducing_bacterium_medium_with_pyruvate` found this M557 owner, the related TOGO M556 liquid pyruvate source, and the older MediaDive J553 source. No conflicting use of `CultureMech:009951` was found.

The NaCl, sodium pyruvate, agar, and sulfate-reducing base salt rows are grounded plausibly and preserve the JCM 553 wrapper better than the old MediaDive import.

## Evidence

JCM 553 defines the pyruvate recipe as JCM 552 supplemented with final 30.0 g/L NaCl, with sodium lactate replaced by 1.9 g/L sodium pyruvate, and pH adjusted to 6.7. The TOGO M557 source adds the solid-medium instruction of 15 g/L agar from the JCM 552 page.

The generated YAML has the correct distinguishing formula rows for the agar pyruvate variant: 30 g/L NaCl, 1.9 g/L sodium pyruvate, and 15 g/L agar. The same generated record lacks `ph_value: 6.7`, lacks preparation steps, and stores the 1 ml vitamin, 1 ml FeCl2, and 1 ml trace-element additions as empty `G_PER_L` solution records.

The TOGO M557 raw payload still carries the imported JCM 552 base preparation comment that mentions L-sodium lactate plus the JCM 553 wrapper comment that replaces lactate with pyruvate. A repaired import needs to merge those instructions into pyruvate-aware pH and anaerobic steps rather than keeping no preparation text at all.

## Completeness

The generated agar pyruvate record is incomplete for preparation and stocks even though its major top-level formula changes are present.

`target_organisms` is absent. The JCM and TOGO medium pages identify a recipe but do not assert a source-backed growth organism.

## Findings

- `ph_value` is missing even though JCM 553 explicitly sets pH 6.7.
- The 1 ml/L vitamin, FeCl2, and trace-element additions are empty `solutions` entries with `G_PER_L` units instead of structured stock references.
- The source's 1 mg resazurin row is stored as `1 G_PER_L`, a 1000x unit slip.
- `NaOH` is retained as a variable top-level ingredient instead of as sterile 1 N NaOH for pH adjustment.
- `N2` is retained as a variable top-level ingredient instead of as the anaerobic autoclaving atmosphere.
- Preparation steps for the pH-adjusted pyruvate variant are absent, including the N2 autoclaving, supplement handling, final pH 6.7 adjustment, and solid-medium agar addition.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M557_Sulfate_Reducing_Bacterium_Medium_With_Pyruvate.yaml` or the TOGO wrapper expansion, then regenerate `data/merge_yaml/merged/sulfate_reducing_bacterium_medium_with_pyruvate__9fafa0a1.yaml`.
- Preserve 30 g/L NaCl, 1.9 g/L sodium pyruvate, and 15 g/L agar as the distinguishing JCM 553/JCM_M553-2 formula rows.
- Add source pH 6.7.
- Represent vitamin solution M554, FeCl2 solution M180, and trace element solution M180 as 1 ml/L stock additions or structured cross-references.
- Convert resazurin from 1 mg/L to `0.001 G_PER_L`.
- Add preparation steps that adapt the JCM 552 anaerobic workflow to the JCM 553 pyruvate replacement and final pH 6.7 adjustment.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `TOGO:M557`, `JCM_M553-2`, `CultureMech:009951`, and `sulfate_reducing_bacterium_medium_with_pyruvate` to confirm M556, M557, and MediaDive J553 remain intentionally distinct.
- Compare the repaired M557 agar record against the M556 liquid pyruvate source and the MediaDive J553 source.

## Additional Notes

Empty optional fields that are unrelated to source-backed stock references and growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source and the JCM wrapper expansion path.
