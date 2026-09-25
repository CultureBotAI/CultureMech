# YAML Record Review: haloquadratum_walsbyi_medium__94116a4d

- Repository: CultureMech
- Record: `data/merge_yaml/merged/haloquadratum_walsbyi_medium__94116a4d.yaml`
- Started UTC: 2026-09-23T11:05:57Z
- Finished UTC: 2026-09-23T11:07:09Z
- Verdict: needs curation

## Target

Generated merged YAML for Togo Medium M2375, `Haloquadratum Walsbyi Medium`, imported from DSMZ medium 1091.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches Togo `TOGO:M2375`, which points to the DSMZ 1091 PDF.
- An ignored-file-inclusive exact search for `TOGO:M2375`, `DSMZ_Medium1091.pdf`, `haloquadratum_walsbyi_medium`, and `mediadive.medium:1091` found this Togo M2375 import plus direct DSMZ 1091 and KOMODO 1091 imports that were merged separately.
- The core salts, sodium bicarbonate, sodium nitrate, sodium pyruvate, and Tris groundings are appropriate.
- The MgSO4 x 7 H2O primary `term` is correct, but its `mediaingredientmech_chebi_term` still points to generic magnesium sulfate.

## Evidence

- DSMZ 1091 lists a 1 L formula with 195 g NaCl, 50 g MgSO4 x 7 H2O, 35 g MgCl2 x 6 H2O, 5 g KCl, 0.25 g NaHCO3, 1 g NaNO3, 0.5 g CaCl2 x 2 H2O, 0.05 g KH2PO4, 0.03 g NH4Cl, 20 ml 1 M Tris buffer, and 1000 ml distilled water.
- DSMZ 1091 instructs adding 0.05 g/L yeast extract and 1 g/L sodium pyruvate after autoclaving from sterile autoclaved stock solutions, with final pH 7.4.
- DSMZ 1091 states that DSM 29227 should use 4.0 g/L sodium pyruvate.
- MediaDive 1091 represents 20 ml 1 M Tris buffer as 2.4228 g/L Tris and preserves the 1000 ml distilled-water row.
- Togo M2375 preserves pH `7.4` and retains the Tris buffer row as a 20 ml volume.

## Completeness

- Missing pH: the generated record omits `ph_value: 7.4`.
- Mis-scaled water: the 1000 ml water row became `1000 G_PER_L`.
- Mis-scaled buffer: 20 ml 1 M Tris buffer became `20 G_PER_L`.
- Missing post-autoclave semantics: yeast extract and sodium pyruvate have no sterile-stock or add-after-autoclaving structure.
- Missing strain condition: the DSM 29227-specific 4 g/L sodium pyruvate instruction was dropped.

## Findings

1. The generated Togo M2375 record omits pH 7.4.
2. Distilled water is misrepresented as `1000 G_PER_L`.
3. The 20 ml 1 M Tris buffer addition is misrepresented as `20 G_PER_L`.
4. Yeast extract and sodium pyruvate are flattened into ordinary top-level ingredients with no post-autoclave sterile-stock semantics.
5. The DSM 29227 sodium-pyruvate override is missing.
6. MgSO4 x 7 H2O still carries a generic magnesium sulfate MediaIngredientMech link.

## Recommended Edits

- Add `ph_value: 7.4`.
- Replace distilled water with the correct 1000 ml final-volume representation.
- Represent 20 ml 1 M Tris buffer as a volume addition or convert it consistently to the equivalent Tris concentration.
- Add post-autoclave sterile-stock addition semantics for yeast extract and sodium pyruvate.
- Add a strain-scoped DSM 29227 sodium-pyruvate override at 4 g/L.
- Refresh the MgSO4 x 7 H2O MediaIngredientMech link to the heptahydrate CHEBI key.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `TOGO:M2375`, `mediadive.medium:1091`, and `komodo.medium:1091` after regeneration.
- Verify that this Togo M2375 import reconciles with the direct DSMZ 1091 and KOMODO 1091 duplicate family after water and Tris are fixed.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
