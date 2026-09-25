# YAML Record Review: HALANAEROBIUM SEHLINENSE MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/halanaerobium_sehlinense_medium__ec2311ec.yaml
- Started UTC: 2026-09-23T08:47:35Z
- Finished UTC: 2026-09-23T08:48:38Z
- Verdict: needs curation

## Target

- Reviewed generated YAML for `HALANAEROBIUM SEHLINENSE MEDIUM`.
- Stable ID: `CultureMech:003276`.
- Primary source in generated record: direct JCM/MediaDive `mediadive.medium:J929`.
- Merge fingerprint: `ec2311ecf8376e0f2484c582c7c8e811b78e8e07b610335dd1a7485766a63562`.

## Validation

- LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`: pass.
- Strict validation with `scripts/validate_strict.py`: pass, 0 error rows in `/private/tmp/halanaerobium_sehlinense_medium_ec2311ec.strict.tsv`.
- LinkML reference validation: pass, 0 checked references.
- LinkML term validation with `conf/oak_config.yaml`: pass.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record is the direct JCM/MediaDive import for JCM medium 929.
- An exact `rg --no-ignore --hidden` search for `JCM_M929`, `GRMD=929`, and `mediadive.medium:J929` found the direct JCM/MediaDive source plus a source-equivalent Togo `M975` / `JCM_M929` import in `data/merge_yaml` and `data/normalized_yaml`.
- The generated direct JCM import and Togo `M975` sibling remain split. The Togo branch also appears in a separate merged output together with `TOGO_M697_Halanaerobaculum_Tunisiense_Medium`.

## Evidence

- The live JCM `GRMD=929` page lists KH2PO4 0.3 g, K2HPO4 0.3 g, NH4Cl 1.0 g, NaCl 200 g, KCl 0.1 g, CaCl2 x 2 H2O 0.1 g, KNO3 2.0 g, 10 ml trace minerals from JCM medium 151, yeast extract 1.0 g, and distilled water brought to 1.0 L.
- JCM instructs adjustment to pH 8.3, boiling and cooling under N2, dispensing under N2-CO2 4:1, autoclaving at 110C for 20 min, and then aseptically adding 25 ml of 8 percent NaHCO3 solution, 15 ml of 10 percent MgCl2 x 6 H2O solution, 20 ml of 1 M glucose solution, and 8 ml of 5 percent Na2S x 9 H2O solution per liter.
- The generated record models the four post-autoclave stock additions as if their aliquot volumes were gram-per-liter formula concentrations: NaHCO3 25 g/L, MgCl2 x 6 H2O 15 g/L, glucose 20 g/L, and Na2S x 9 H2O 8 g/L.
- JCM's trace-minerals reference is a 10 ml stock addition, but the generated record flattens the JCM medium 151 stock recipe into top-level ingredients at stock concentration.

## Completeness

- pH 8.3 and the main anaerobic preparation instruction are preserved.
- The stock addition volumes are present but have the wrong units and semantics.
- Nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x n H2O, FeSO4 x 7 H2O, CoSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, and Na2MoO4 x 2 H2O belong to the referenced trace-minerals stock, not to the final top-level formula.
- `KNO3` still carries a legacy `mediaingredientmech_term` after the June 2026 ChEBI-key migration, and `Yeast extract` is ungrounded.

## Findings

- Major: Post-autoclave stock volumes are imported as gram-per-liter top-level ingredients.
- Major: The trace-minerals stock is flattened at stock strength.
- Major: Duplicate-ingredient cleanup sums salts across unrelated main-medium and trace-mineral contexts.
- Minor: The record still has one legacy MediaIngredientMech identifier on `KNO3`.
- Minor: The source-equivalent Togo import remains split from the direct JCM/MediaDive record.

## Recommended Edits

- Recurate JCM 929 with the four post-autoclave additions represented as stock aliquots or as final concentrations computed from their concentration and volume.
- Keep the 10 ml JCM 151 trace-minerals addition nested or convert it by the actual 10 ml per liter aliquot.
- Stop summing duplicate salts across stock boundaries.
- Migrate the leftover `KNO3` legacy `MediaIngredientMech:000170` link to the ChEBI-key field.
- Add source-equivalence handling so `TOGO:M975` / `JCM_M929` merges with direct `mediadive.medium:J929` after the Togo and direct imports are corrected.

## Follow-up Checks

- After repair, verify that NaHCO3, MgCl2 x 6 H2O, glucose, and Na2S x 9 H2O no longer have values equal to their milliliter stock-addition volumes.

## Additional Notes

- None found.
