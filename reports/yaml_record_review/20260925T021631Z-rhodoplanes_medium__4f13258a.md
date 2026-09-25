# YAML Record Review: rhodoplanes_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodoplanes_medium__4f13258a.yaml`
- Started UTC: 2026-09-25T02:16:30Z
- Finished UTC: 2026-09-25T02:16:42Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:003003` for JCM Medium J658 / `mediadive.medium:J658`, generated from `data/normalized_yaml/bacterial/rhodoplanes_medium.yaml`.

## Validation

- Open schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The target ID, label, category, and `mediadive.medium:J658` grounding match JCM and MediaDive for Rhodoplanes medium. An ignored-inclusive search for the exact `mediadive.medium:J658`, `TOGO:M674`, `JCM_M658`, and JCM `GRMD=658` references found one direct JCM owner, one TOGO M674 owner, and their two generated records under `data/normalized_yaml` and `data/merge_yaml`.

The TOGO M674 owner is the same source medium: TOGO cites original media ID `JCM_M658` and the same JCM 658 URL.

## Evidence

JCM Medium 658 and MediaDive J658 list 0.38 g KH2PO4, 0.39 g K2HPO4, 0.2 g MgSO4 x 7H2O, 0.4 g NaCl, 0.6 g NH4Cl, 0.05 g CaCl2 x 2H2O, 3.0 g sodium pyruvate, 0.5 g yeast extract, 5.0 ml ferric citrate 0.1% w/v, 1.0 ml Micronutrient solution SL7, 1.0 L distilled water, and pH 7.0. MediaDive resolves the SL7 stock to 1.0 ml 25% HCl, 70 mg ZnCl2, 100 mg MnCl2 x 4H2O, 60 mg H3BO3, 200 mg CoCl2 x 6H2O, 20 mg CuCl2 x 2H2O, 20 mg NiCl2 x 6H2O, 40 mg Na2MoO4 x 2H2O, and 1.0 L distilled water.

TOGO M674 also lists the JCM 658 main rows and keeps Micronutrient solution SL7 as a 1 ml reference to M535. JCM 533 and TOGO M535 provide the same SL7 stock basis that MediaDive embeds in J658.

## Completeness

The reviewed JCM-derived generated target omits the 1 L final water row and 1 ml/L SL7 row, then emits the eight SL7 stock components as final-medium gram-per-liter rows. The TOGO M674 duplicate is not merged into this target despite sharing JCM 658 as its original source.

Empty optional literature and organism fields are not defects for this imported medium.

## Findings

- Major: `data/normalized_yaml/bacterial/rhodoplanes_medium.yaml` flattens two stock additions. JCM J658 lists 5 ml of ferric citrate 0.1% w/v and 1 ml of Micronutrient solution SL7, but the generated target reports `Ferric citrate` as `5 G_PER_L` and reports HCl plus seven SL7 salts as final-medium ingredients at stock concentrations.
- Major: `data/normalized_yaml/bacterial/rhodoplanes_medium.yaml` omits source rows. The generated target has no final distilled-water row and no `Micronutrient solution SL7` stock row, even though both are explicit in JCM 658 and MediaDive J658.
- Major: `data/normalized_yaml/bacterial/TOGO_M674_Rhodoplanes_Medium.yaml` is an unmerged duplicate of JCM J658 with its own import defects. It converts 5 ml ferric citrate solution, 1 L distilled water, and 1 ml SL7 to `G_PER_L`, leaves the SL7 `composition` empty, and does not carry the source pH 7.0 into `ph_value` or `preparation_steps`.
- Major: `data/merge_yaml/merged` contains two generated records for the same source medium, `rhodoplanes_medium__4f13258a.yaml` for `mediadive.medium:J658` and `RHODOPLANES_MEDIUM.yaml` for TOGO M674/JCM_M658.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/rhodoplanes_medium.yaml` so the J658 main recipe has 5 ml/L ferric citrate 0.1% w/v, 1 ml/L Micronutrient solution SL7, and 1 L distilled water instead of flattened ferric-citrate and SL7 ingredients.
- Add the nested SL7 stock recipe from JCM 533 or the equivalent MediaDive J658 solution, including stock water.
- Repair `data/normalized_yaml/bacterial/TOGO_M674_Rhodoplanes_Medium.yaml` so ml/L and L water inputs are not coerced to `G_PER_L`, SL7 has resolved stock composition, and pH 7.0 is represented.
- Add a source-duplicate relationship between TOGO M674 and the direct JCM J658 owner, then regenerate `data/merge_yaml/merged` so only one Rhodoplanes medium target is emitted with TOGO M674 as a duplicate source.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for the regenerated Rhodoplanes medium.
- Confirm the regenerated final recipe has the JCM 658 rows for ferric citrate solution, SL7, and distilled water, not top-level HCl, ZnCl2, MnCl2 x 4H2O, H3BO3, CoCl2 x 6H2O, CuCl2 x 2H2O, NiCl2 x 6H2O, or Na2MoO4 x 2H2O.
- Confirm `data/merge_yaml/merged` no longer emits both uppercase TOGO and lowercase JCM Rhodoplanes targets.

## Additional Notes

The exact source-ID search included ignored files under the relevant data trees and did not find a third maintained owner for JCM 658.
