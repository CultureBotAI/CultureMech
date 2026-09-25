# YAML Record Review: paenibacillus_dc_8a_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/paenibacillus_dc_8a_medium.yaml
- Started UTC: 2026-09-24T19:42:44Z
- Finished UTC: 2026-09-24T19:42:44Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:007931`, `paenibacillus_dc_8a_medium`, generated from `data/normalized_yaml/bacterial/TOGO_M1396_Paenibacillus_DC-8A_Medium.yaml` for TOGO M1396 / JCM Medium 1299.

## Validation

- Open LinkML validation: Passed; exited 0 with `No issues found`.
- Strict validation: Passed; scanned 1 file with 0 ERROR rows. `/private/tmp/paenibacillus_dc_8a_medium.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The generated record has the expected TOGO M1396 identity for an import of JCM Medium 1299 / Paenibacillus DC-8A Medium. An ignored-inclusive exact search for `TOGO:M1396`, `JCM_M1299`, `GRMD=1299`, `Paenibacillus DC-8A`, and `paenibacillus_dc_8a_medium` across `data/merge_yaml` and `data/normalized_yaml` found the TOGO source, the direct JCM J1299 source, the DC-8A parent medium, and a generated direct-MediaDive sibling.

## Evidence

JCM 1299 lists a 900 ml base containing K2HPO4 2.9 g, Urea 4.2 g, Yeast extract 2.0 g, CaCl2 x 2 H2O 0.01 g, Na2CO3 1.0 g, L-Cysteine HCl x H2O 0.5 g, Resazurin 0.5 mg, Mineral solution 0.2 ml, and Distilled water 900 ml. After pH 9.0 adjustment, N2 gassing, sealing, and autoclaving, it adds 100 ml of 10% (w/v) Xylose solution per 900 ml. The separate Mineral solution contains MgCl2 x 6 H2O 25.0 g, CaCl2 x 2 H2O 37.5 g, FeSO4 x 7 H2O 0.312 g, and Distilled water 1.0 L.

## Completeness

The generated TOGO record loses the source scopes: it sums base and mineral-solution water into 901 `G_PER_L`, sums base calcium chloride and mineral-solution calcium chloride into 37.51 `G_PER_L`, omits the 900 ml main water row, represents Mineral solution 0.2 ml as 0.2 `G_PER_L`, represents 10% (w/v) Xylose solution 100 ml as 100 `G_PER_L`, flattens mineral stock ingredients into final ingredients at stock strength, and omits pH 9.0 plus the anaerobic preparation step.

## Findings

1. Mineral solution was flattened into the final ingredient list.

   JCM 1299 uses only 0.2 ml of Mineral solution per 900 ml base. The generated record emits the mineral-solution MgCl2 x 6 H2O, CaCl2 x 2 H2O, FeSO4 x 7 H2O, and 1 L stock water as if they were final-medium ingredients, then sums CaCl2 x 2 H2O with the separate 0.01 g base row.

2. The xylose stock addition was converted to a false mass concentration.

   JCM 1299 adds 100 ml of 10% (w/v) Xylose solution after cooling. The generated record stores `10% (w/v) Xylose solution` as 100 `G_PER_L`, dropping both the 100 ml addition volume and the 10% stock concentration.

3. pH 9.0 and anaerobic preparation were lost.

   The JCM source explicitly adjusts to pH 9.0, replaces the gas phase with N2, seals with butyl rubber stoppers, autoclaves, and then adds the xylose solution aseptically and anaerobically. The generated TOGO record has no `ph_value` or `preparation_steps` and instead emits N2 as a variable ingredient.

4. TOGO M1396 is split from the direct JCM J1299 source.

   TOGO M1396 imports JCM Medium 1299. The generated TOGO record remains a singleton, while the direct JCM J1299 MediaDive source generated separately in `paenibacillus_dc_8a_medium__63089040.yaml`.

## Recommended Edits

- Model `Mineral solution` as a 0.2 ml stock addition with nested MgCl2 x 6 H2O, CaCl2 x 2 H2O, FeSO4 x 7 H2O, and 1 L water composition.
- Model the 100 ml 10% (w/v) Xylose solution as a separate post-autoclave stock addition.
- Restore the 900 ml base Distilled water row and pH 9.0 anaerobic preparation.
- Link TOGO M1396 as a source duplicate of the direct JCM J1299 source before regeneration.

## Follow-up Checks

- Re-run an ignored-inclusive exact search for `GRMD=1299`, `JCM_M1299`, and `TOGO:M1396` after regeneration and confirm the direct JCM and TOGO sources no longer emit as separate source duplicates.
- Confirm regenerated calcium chloride has distinct base and mineral-stock scopes rather than one summed 37.51 `G_PER_L` top-level ingredient.
- Re-run open, strict, reference, and term validation on the regenerated YAML.

## Additional Notes

The direct JCM J1299 / DSMZ 1809 generated sibling has the same mineral-solution flattening defect and should be repaired with the same stock-solution model.
