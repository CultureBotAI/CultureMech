# YAML Record Review: NATRANAEROARCHAEUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/natranaeroarchaeum_medium__65df3e2f.yaml
- Started UTC: 2026-09-24T16:36:31Z
- Finished UTC: 2026-09-24T16:36:31Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002261` for the direct JCM import of JCM Medium 1081, `NATRANAEROARCHAEUM MEDIUM`, with MediaDive term `mediadive.medium:J1081`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to the intended direct JCM `GRMD=1081` source through `mediadive.medium:J1081`.

An exact repository search including ignored files for `natranaeroarchaeum_medium`, `GRMD=1081`, and `mediadive.medium:J1081` found this direct JCM owner and generated file plus an active TOGO M1150 owner at `data/normalized_yaml/archaea/TOGO_M1150_Natranaeroarchaeum_Medium.yaml`. That TOGO owner cites the same JCM Medium 1081 source and was repaired on 2026-09-10 to preserve nested stock solutions. The search also found other archaeal media that legitimately reference JCM 1081 as a source component.

## Evidence

JCM Medium 1081 composes the final medium from 250.0 ml sterilized JCM Medium 1079 Basal mineral NaCl medium and 750.0 ml sterilized Soda based mineral medium. To complete the medium, it adds 5.0 ml 2 M sodium pyruvate, 10.0 ml Trace vitamins from JCM Medium 197, and 0.2 ml 10% yeast extract.

The JCM 1081 Soda based mineral medium is made by adding 185.0 g Na2CO3, 35.0 g NaHCO3, 16.0 g NaCl, 1.0 g K2HPO4, and 5.0 g KCl to distilled water and bringing the volume to 1.0 L. It is autoclaved, left standing for three days, decanted, and then receives 1.0 ml each of 4 M NH4Cl, JCM Medium 431 Selenite-tungstate solution, JCM Medium 1079 Trace element solution, and 1 M MgCl2.

MediaDive J1081 exposes the Soda based mineral medium as a nested solution. It reports that nested solution with `volume: 4`, and the direct generated record consequently emits impossible stock-local values such as 46250 g/L Na2CO3, 8750 g/L NaHCO3, 4000 g/L NaCl, and 1250 g/L KCl instead of the JCM 1081 per-liter stock recipe.

The repaired TOGO M1150 owner now models the 250 ml Basal mineral NaCl medium, 750 ml Soda based mineral medium, 5 ml sodium pyruvate, 10 ml Trace vitamins, and 0.2 ml yeast extract as solution additions with nested stock compositions and `ML_PER_L` units.

## Completeness

The direct generated record is missing structured final solution additions for the 250 ml Basal mineral NaCl medium, 750 ml Soda based mineral medium, 5 ml 2 M sodium pyruvate, 10 ml Trace vitamins, and 0.2 ml 10% yeast extract rows.

It omits the water used to bring the Soda based mineral medium to 1 L and the water in the Selenite-tungstate and Trace element stocks. The source JCM 1079 Basal mineral NaCl stock and Trace element stock are represented only by a bare `Basal mineral NaCl medium` row and flattened Trace element internals, so HEPES from the JCM 1079 basal stock is absent.

## Findings

- The 250 ml Basal mineral NaCl medium and 750 ml Soda based mineral medium additions are stored as top-level `G_PER_L` ingredients rather than volume additions.
- Soda based mineral medium concentrations are corrupted by the MediaDive nested `volume: 4` value; the generated 46250 g/L Na2CO3 row should be a 185 g/L stock-local row inside a 750 ml/L stock addition.
- The 5 ml 2 M sodium pyruvate, 10 ml Trace vitamins, 1 ml 4 M NH4Cl, 1 ml Selenite-tungstate, 1 ml Trace element, and 1 ml 1 M MgCl2 additions are either flattened or represented as `G_PER_L` values equal to their milliliter additions.
- JCM 431, JCM 1079, and JCM 197 stock internals are flattened into the direct ingredient list, while several water rows and the JCM 1079 HEPES component are missing.
- The active TOGO M1150 duplicate was repaired after this generated snapshot and should be linked, merged, or used to replace the direct JCM owner.

## Recommended Edits

- Re-curate the direct JCM owner with the same nested stock structure used by the repaired TOGO M1150 owner.
- Correct Soda based mineral medium to a 750 ml/L stock addition whose composition is the JCM 1081 recipe brought to 1 L, not the MediaDive `volume: 4`-derived g/L values.
- Link or retire the TOGO M1150 owner so JCM Medium 1081 does not continue producing two Natranaeroarchaeum Medium records.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natranaeroarchaeum_medium__65df3e2f.yaml` and verify no 46250 g/L, 8750 g/L, 4000 g/L, or 1250 g/L rows remain.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored files for `GRMD=1081`, `TOGO:M1150`, and `mediadive.medium:J1081` to verify the intended owner topology and check records that reuse JCM 1081 as a stock source.

## Additional Notes

None found.
