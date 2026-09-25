# YAML Record Review: desulfurispirillum_alkaliphilum_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurispirillum_alkaliphilum_medium__d57515a2.yaml`
- Started UTC: 2026-09-22T21:19:43Z
- Finished UTC: 2026-09-22T21:22:03Z
- Verdict: needs curation

## Target

`CultureMech:010195` represents TOGO Medium M786, `Desulfurispirillum Alkaliphilum Medium`, imported from `JCM_M760-2` on the JCM 760 page. The generated record is a single-source merge from `data/normalized_yaml/bacterial/TOGO_M786_Desulfurispirillum_Alkaliphilum_Medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

The external identity is specific enough: TOGO M786 points to JCM medium 760 and to the `JCM_M760-2` sulfur electron-acceptor variant. That variant follows the main Desulfurispirillum alkaliphilum base recipe, omits the 1.0 M KNO3 stock used in the nitrate version, and adds 0.25 g/l NH4Cl plus 2.0 g/l elemental sulfur per the JCM page's sulfur-growth comment.

The top-level identity should remain separate from the nitrate JCM 760 recipe, but it should be deduplicated or linked as a variant rather than standing as another independent `Desulfurispirillum Alkaliphilum Medium` with the same normalized name.

## Evidence

- TOGO M786 reports `original_media_id` `JCM_M760-2` and source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=760`.
- The TOGO M786 base solution lists 1 L distilled water, 6 g NaCl, 0.5 g K2HPO4, 8 g NaHCO3, 22 g Na2CO3, and N2.
- Its second solution lists 2 ml 1% yeast extract solution, 20 ml 1.0 M sodium acetate solution, 10 ml 0.1 M MgSO4 solution, 0.25 g/l NH4Cl, 2.0 g/l sulfur, and 1 ml `SL--4 trace element solution (see Medium [M335])`.
- Its final solution lists 2.5 ml 5% Na2S x 9H2O solution.
- A gitignore-independent `find` over `data/` found the TOGO M786 normalized source plus the related TOGO M785 nitrate variant and MediaDive J760 import.

## Completeness

The record is structurally incomplete. Five recipe additions are present only as `solutions` entries with `composition: []`, and no formula components describe the contents of 1% yeast extract, 1.0 M sodium acetate, 0.1 M MgSO4, SL-4 trace elements, or 5% sodium sulfide.

The main 1 L distilled water row is retained but has been converted to `1 G_PER_L`, so the solvent volume is not recoverable from the generated concentration.

## Findings

- The 1 L distilled water source row is represented as `1 G_PER_L`; this should be modeled as a liter volume, a final water volume, or a percent volume value, not as 1 gram per liter.
- The 2 ml yeast extract, 20 ml sodium acetate, 10 ml MgSO4, 1 ml SL-4, and 2.5 ml sodium sulfide solution additions are all stored as empty solution stubs with their milliliter dose values copied into `G_PER_L` concentrations.
- The SL-4 row retains only text that points to Medium M335. It does not link to the referenced stock's composition or preserve that stock as a nested formulation.
- This variant remains split from the MediaDive J760 record and from the TOGO M785 nitrate variant even though all three derive from the same JCM 760 page and share the same normalized name.

## Recommended Edits

- Correct the distilled-water unit so the 1 L source amount no longer appears as 1 g/l.
- Keep 0.25 g/l NH4Cl and 2.0 g/l sulfur as sulfur-variant ingredients.
- Convert the 1% yeast extract, 1.0 M sodium acetate, 0.1 M MgSO4, SL-4, and 5% Na2S x 9H2O stubs to stock-dose records with milliliter addition amounts.
- Resolve the SL-4 reference to TOGO M335 / JCM 340 or another canonical SL-4 stock so the generated record is not an empty cross-reference.
- Add a parent or variant relationship that prevents M786, M785, and MediaDive J760 from becoming three unconnected generated records with the same name.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that the regenerated M786 formula preserves NH4Cl and sulfur while omitting KNO3.
- Confirm that no solution rows with milliliter source amounts remain encoded as `G_PER_L`.

## Additional Notes

None found.
