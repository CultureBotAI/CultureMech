# YAML Record Review: Ethane-C Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ethane_c_medium.yaml
- Started UTC: 2026-09-23T00:31:10Z
- Finished UTC: 2026-09-23T00:35:18Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/ethane_c_medium.yaml` is the generated TOGO M1198 / JCM M1120 Ethane-C Medium record. Its maintained owner is `data/normalized_yaml/bacterial/TOGO_M1198_Ethane-C_Medium.yaml`.

This generated merge was emitted from the TOGO import on 2026-08-06. The owner was substantially repaired on 2026-09-11 by `repair_togo_m1192_m1198_score15.py`, so the generated file is stale relative to the current curated source YAML.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/ethane_togo.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The TOGO identifier, JCM cross-reference, and Ethane-C name are coherent for M1198 / JCM M1120.

The old generated grounding is incomplete. `Fe(III)-EDTA` is left ungrounded in the generated file because TOGO used the interpuncted spelling `Fe(III) EDTA`, but the repaired normalized owner maps it to `CHEBI:30729`. The generated `Vitamin mixture`, `Metal mixture`, and `Artificial seawater` solution shells have no composition and only point to Medium M1196 in notes.

An exact ignored-file-inclusive local search found two generated Ethane-C records: this TOGO-derived merge and `data/merge_yaml/merged/ethane_c_medium__2510f74f.yaml`, which came from a direct JCM/MediaDive `ethane_c_medium.yaml` parent. The two are not merged together yet even though they represent the same JCM formula.

## Evidence

TOGO M1198 identifies `JCM_M1120` as Ethane-C Medium and records:

- 0.01 g KH2PO4.
- 0.1 g NH4NO3.
- 2.5 mg Fe(III)-EDTA.
- 2.5 ml Vitamin mixture from M1196.
- 1 ml Metal mixture from M1196.
- 1 L Artificial seawater from M1196.
- NaOH to adjust pH 8.0.
- Distribution into sealed serum bottles, autoclaving at 110 C for 5 min, overnight standing, and 10-50% ethane in the gas phase.

MediaDive J1120 supplies the same JCM main solution normalized to a 1004 ml volume, complete subrecipes for `Vitamin mixture`, `Metal mixture`, and `Artificial seawater`, and the ethane gas-phase preparation text now copied into the normalized owner.

## Completeness

The generated record is incomplete. It has only the three inorganic main-solution ingredients, a variable NaOH row, and three empty M1196 cross-reference solution shells. It omits the vitamin, metal, and artificial seawater compositions, the pH value, the autoclaving and gas-phase preparation, the 10-50% v/v ethane addition, and the structured sterilization details now present in the maintained owner.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | The generated merge is stale relative to the curated normalized owner. | `data/normalized_yaml/bacterial/TOGO_M1198_Ethane-C_Medium.yaml` has a 2026-09-11 repair with normalized JCM J1120 ingredients, full solution compositions, `ph_value: 8.0`, 110 C sterilization, and an Ethane gas ingredient; this generated merge still reflects the January TOGO import plus March solution migration. | Regenerate `data/merge_yaml/merged/ethane_c_medium.yaml` from the repaired normalized owner after confirming the direct JCM parent should merge with it. |
| Major | Fe(III)-EDTA has the wrong concentration by three orders of magnitude. | TOGO lists `2.5 mg`; MediaDive J1120 normalizes that main-solution row to `0.00249004 G_PER_L`; the generated file has `2.5 G_PER_L`. | Keep the repaired owner value and regenerate. |
| Major | Cross-referenced M1196 stocks are empty and have incorrect units. | TOGO uses 2.5 ml Vitamin mixture, 1 ml Metal mixture, and 1 L Artificial seawater; the generated YAML has empty `solutions` with `2.5`, `1`, and `1` all typed as `G_PER_L`. | Resolve the M1196 subrecipes from MediaDive/JCM and encode the three additions as `ML_PER_L` or `L` solution additions with nested compositions. |
| Major | Ethane is missing as a gas-phase addition. | The source preparation adds ethane to 10-50% of the gas phase by volume; the repaired owner now has an `Ethane` ingredient at `10-50 PERCENT_V_V`, while the generated file has no ethane row or preparation step. | Add or retain the gas-phase ethane row during regeneration. |
| Major | Preparation semantics were dropped. | TOGO M1198 records pH 8.0, sealed serum bottle aliquoting, autoclaving at 110 C for 5 min, overnight standing, and later gas-phase ethane addition; the generated file has no `preparation_steps` or `sterilization` block. | Preserve the repaired owner preparation steps and sterilization metadata. |

## Recommended Edits

1. Regenerate this merge from `data/normalized_yaml/bacterial/TOGO_M1198_Ethane-C_Medium.yaml` so the September 2026 repair is reflected in generated output.
2. De-duplicate with the direct JCM/MediaDive generated sibling `data/merge_yaml/merged/ethane_c_medium__2510f74f.yaml` if the merge fingerprint should treat `TOGO:M1198` and `mediadive.medium:J1120` as the same recipe.
3. Retain `Fe(III)-EDTA` at `0.00249004 G_PER_L`, `Vitamin mixture` at `2.5 ML_PER_L`, `Metal mixture` at `1 ML_PER_L`, `Artificial seawater` at `1000 ML_PER_L`, and `Ethane` at `10-50 PERCENT_V_V`.
4. Carry forward the repaired preparation steps for pH adjustment, sealed-vessel aliquoting, 110 C autoclaving, overnight standing, and ethane gas addition.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merge.
- Confirm the regenerated Ethane-C output has populated `Vitamin mixture`, `Metal mixture`, and `Artificial seawater` solutions.
- Confirm no `Unknown solution` entries remain.
- Confirm the direct JCM sibling and TOGO M1198 record either merge to one generated output or have an explicit reason to remain separate.

## Additional Notes

The live JCM URL from the source currently returned a "Nothing found" page for GRMD 1120, so this review used the TOGO M1198 payload and MediaDive J1120 REST response for formula details.
