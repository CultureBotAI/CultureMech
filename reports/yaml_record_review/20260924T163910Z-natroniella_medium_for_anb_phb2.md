# YAML Record Review: Natroniella Medium For ANB-PHB2

- Repository: CultureMech
- Record: data/merge_yaml/merged/natroniella_medium_for_anb_phb2.yaml
- Started UTC: 2026-09-24T16:39:10Z
- Finished UTC: 2026-09-24T16:39:10Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:007919` for TOGO M1385, `Natroniella Medium For ANB-PHB2`, imported from JCM Medium 1289.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to the intended TOGO M1385 import of JCM Medium 1289.

An exact repository search including ignored files for `TOGO:M1385`, `CultureMech:007919`, `GRMD=1289`, `mediadive.medium:J1289`, and `natroniella_medium_for_anb_phb2` found this TOGO owner and generated file plus an active direct JCM owner at `data/normalized_yaml/bacterial/natroniella_medium_for_anb_phb2.yaml`. Both owners cite JCM Medium 1289 and both still generate.

The live JCM `GRMD=1289` page currently returns "Nothing found"; MediaDive J1289 and the TOGO M1385 API still carry the structured recipe that was imported from that historical source.

## Evidence

The TOGO M1385 API lists a 1 L carbonate-phosphate base with 64 g Na2CO3, 40 g NaHCO3, 18 g NaCl, 1 g K2HPO4, distilled water, and a 6 N HCl pH adjustment.

MediaDive J1289 records that this base is adjusted to pH 9.6 with 6 N HCl, autoclaved, and then receives five aseptic post-autoclave additions: 4 ml 1 N NH4Cl, 1 ml 1 M MgCl2, 1 ml Trace element solution, 1 ml Selenite-tungstate solution, and 1 ml Trace vitamins. It then distributes the medium into culture vessels under argon and adds 2 ml 1.0% yeast extract, 2.5 ml 5% Na2S x 9H2O, 10 ml 2 M sodium crotonate, and 2 ml 0.1% sodium dithionite in 1 M NaHCO3.

The normalized TOGO owner was repaired on 2026-09-11. It now preserves pH 9.6, an argon gas row, all nine stock additions with `ML_PER_L` units, and nested compositions for NH4Cl, MgCl2, Trace element, Selenite-tungstate, Trace vitamins, yeast extract, Na2S x 9H2O, sodium crotonate, and sodium dithionite stocks.

## Completeness

The generated record is stale relative to the repaired owner. It has the correct base salt masses but still stores the 1 L distilled water row as `1 G_PER_L`, omits `ph_value: 9.6`, omits argon, and lacks structured preparation steps.

All nine source stock additions are still empty solution stubs. Their `G_PER_L` values are the source milliliter additions, not final solute concentrations or stock-local concentrations.

## Findings

- `1 N NH4Cl`, `1 M MgCl2`, `Trace element`, `Selenite-tungstate`, `Trace vitamins`, `1.0% Yeast extract`, `5% Na2S x 9H2O`, `2 M Sodium crotonate`, and `0.1% Sodium dithionite in 1 M NaHCO3` are empty wrappers with addition volumes mis-unitized as g/L.
- The generated artifact predates the 2026-09-11 repair of `TOGO_M1385_Natroniella_Medium_For_ANB-PHB2.yaml`, so it omits all nested stock compositions added during that pass.
- The base water row is wrong as `1 G_PER_L`.
- pH 9.6, HCl adjustment context, argon distribution, and the two-stage post-autoclave addition order are missing from the generated record.
- The active direct JCM J1289 owner is unmerged and produces `data/merge_yaml/merged/natroniella_medium_for_anb_phb2__18cdf3c0.yaml`.

## Recommended Edits

- Regenerate from the repaired TOGO M1385 owner so the nested stock solutions, pH, argon gas, and preparation steps reach `data/merge_yaml/merged/natroniella_medium_for_anb_phb2.yaml`.
- Link, merge, or retire the direct JCM J1289 owner before publishing generated Natroniella Medium records.
- Verify the regenerated water row preserves the source's 1 L base volume instead of `1 G_PER_L`.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natroniella_medium_for_anb_phb2.yaml` and confirm all nine stock additions have `ML_PER_L` concentrations and non-empty nested compositions.
- Re-run open schema, strict, reference, and term validation after regeneration.
- Search including ignored files for `TOGO:M1385`, `GRMD=1289`, and `mediadive.medium:J1289` to verify the TOGO and direct JCM owners are intentionally linked or collapsed.

## Additional Notes

None found.
