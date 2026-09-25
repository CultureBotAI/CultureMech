# YAML Record Review: rhodovulum_imhoffii_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodovulum_imhoffii_medium__ba892fd4.yaml`
- Started UTC: 2026-09-25T02:26:17Z
- Finished UTC: 2026-09-25T02:26:17Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002871` for JCM Medium J520 / `mediadive.medium:J520`, generated from `data/normalized_yaml/bacterial/rhodovulum_imhoffii_medium.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The target ID, label, category, and `mediadive.medium:J520` grounding match JCM and MediaDive for Rhodovulum imhoffii medium. TOGO M521 cites original media ID `JCM_M520`, the same JCM 520 URL, and the same ingredient set. An exact ignored-inclusive search for `TOGO:M521`, `mediadive.medium:J520`, `JCM_M520`, and `GRMD=520` found only the expected JCM and TOGO owners, their generated records, and their indexes under the relevant data trees.

## Evidence

JCM Medium 520 and MediaDive J520 list 0.5 g KH2PO4, 0.25 g CaCl2 x 2H2O, 3 g MgSO4 x 7H2O, 0.68 g NH4Cl, 20 g NaCl, 3 g sodium L-malate, 3 g sodium pyruvate, 0.4 g yeast extract, 5 ml ferric citrate 0.1% w/v, 1 ml Micronutrient solution SL7, 1 ml vitamin B12 at 2 mg/ml, 1000 ml distilled water, and pH 6.8. JCM, MediaDive, and TOGO all expose the SL7 stock with 1 ml 25% HCl, 70 mg ZnCl2, 100 mg MnCl2 x 4H2O, 60 mg H3BO3, 200 mg CoCl2 x 6H2O, 20 mg CuCl2 x 2H2O, 20 mg NiCl2 x 6H2O, 40 mg Na2MoO4 x 2H2O, and 1000 ml distilled water.

The generated JCM target emits ferric citrate as `5 G_PER_L`, vitamin B12 as `1 G_PER_L`, and every SL7 component as a final-medium ingredient. It also omits the 1000 ml final-water row, the 1 ml/L SL7 row, and the nested SL7 stock water.

## Completeness

The target is missing the source stock structure and final distilled water. The generated corpus also emits a separate uppercase TOGO M521 record for the same JCM 520 source.

Empty optional literature and organism fields are not defects.

## Findings

- Major: `data/normalized_yaml/bacterial/rhodovulum_imhoffii_medium.yaml` flattens three stock additions. The generated target represents 5 ml ferric citrate stock as 5 g/L ferric citrate, 1 ml vitamin B12 stock as 1 g/L vitamin B12, and seven SL7 stock salts plus HCl as final-medium ingredients.
- Major: `data/normalized_yaml/bacterial/rhodovulum_imhoffii_medium.yaml` omits the 1000 ml final distilled-water row and the 1 ml/L Micronutrient solution SL7 row from JCM J520.
- Major: `data/normalized_yaml/bacterial/TOGO_M521_Rhodovulum_Imhoffii_Medium.yaml` imported stock and stock-salt units incorrectly: 5 ml ferric citrate, 1 ml vitamin B12, 1 L water, 1 ml 25% HCl, 70 mg ZnCl2, 100 mg MnCl2 x 4H2O, 60 mg H3BO3, 200 mg CoCl2 x 6H2O, 20 mg NiCl2 x 6H2O, 20 mg CuCl2 x 2H2O, and 40 mg Na2MoO4 x 2H2O became gram-per-liter ingredient rows.
- Major: the TOGO owner leaves the SL7 solution `composition` empty while keeping the SL7 row as `1 G_PER_L`.
- Major: the TOGO owner still has legacy `mediaingredientmech_term` on `Sodium L--malate`, grounds `CoCl2.6H2O` only to anhydrous cobalt dichloride, and has a stale `high_metal: true` flag caused by the false 20 to 200 g/L trace-salt rows.
- Major: `data/merge_yaml/merged` contains separate JCM and TOGO Rhodovulum imhoffii targets instead of one source-duplicate target for JCM 520.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/rhodovulum_imhoffii_medium.yaml` so the J520 final recipe has 5 ml/L ferric citrate stock, 1 ml/L vitamin B12 stock, 1 ml/L Micronutrient solution SL7, and 1000 ml distilled water instead of flattened stock components.
- Add the nested SL7 stock recipe under the direct JCM owner.
- Repair `data/normalized_yaml/bacterial/TOGO_M521_Rhodovulum_Imhoffii_Medium.yaml` so source ml, L, and mg values keep the correct units, SL7 has its nested composition, `Sodium L--malate` has a CHEBI link, and the false high-metal flag is removed.
- Add a source-duplicate relationship between TOGO M521 and direct MediaDive/JCM J520, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for the regenerated Rhodovulum imhoffii medium.
- Confirm the regenerated J520 final recipe has 12 main rows, including ferric citrate stock, SL7, vitamin B12 stock, and distilled water.
- Confirm SL7 components only appear nested under the SL7 stock.
- Confirm `data/merge_yaml/merged` no longer emits both uppercase TOGO and lowercase JCM Rhodovulum imhoffii targets.

## Additional Notes

None found.
