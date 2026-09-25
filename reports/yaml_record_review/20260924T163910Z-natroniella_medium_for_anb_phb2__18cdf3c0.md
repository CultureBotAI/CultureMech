# YAML Record Review: NATRONIELLA MEDIUM FOR ANB-PHB2

- Repository: CultureMech
- Record: data/merge_yaml/merged/natroniella_medium_for_anb_phb2__18cdf3c0.yaml
- Started UTC: 2026-09-24T16:39:10Z
- Finished UTC: 2026-09-24T16:39:10Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002451` for the direct JCM/MediaDive import of JCM Medium 1289, `NATRONIELLA MEDIUM FOR ANB-PHB2`, with MediaDive term `mediadive.medium:J1289`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to the intended direct JCM/MediaDive source for JCM Medium 1289.

An exact repository search including ignored files for `TOGO:M1385`, `CultureMech:007919`, `GRMD=1289`, `mediadive.medium:J1289`, and `natroniella_medium_for_anb_phb2` found this direct JCM owner and generated file plus an active repaired TOGO M1385 owner at `data/normalized_yaml/bacterial/TOGO_M1385_Natroniella_Medium_For_ANB-PHB2.yaml`. Both owners cite JCM Medium 1289 and both still generate.

The live JCM `GRMD=1289` page currently returns "Nothing found"; MediaDive J1289 and TOGO M1385 still carry the imported JCM 1289 recipe.

## Evidence

MediaDive J1289 records a base with 64 g Na2CO3, 40 g NaHCO3, 18 g NaCl, 1 g K2HPO4, distilled water brought to 1 L, pH adjustment to 9.6 with 6 N HCl, and autoclaving.

After cooling, MediaDive J1289 adds 4 ml 1 N NH4Cl, 1 ml 1 M MgCl2, 1 ml Trace element solution, 1 ml Selenite-tungstate solution, and 1 ml Trace vitamins. It then distributes the medium under argon and adds 2 ml 1.0% yeast extract, 2.5 ml 5% Na2S x 9H2O, 10 ml 2 M sodium crotonate, and 2 ml 0.1% sodium dithionite in 1 M NaHCO3.

The MediaDive REST payload reports `volume: 24` for the main solution even though the preparation text says the carbonate-phosphate base is brought to 1.0 L.

The repaired TOGO M1385 owner records 64, 40, 18, and 1 g/L for the base salts, records distilled water as 1 L, stores all nine additions as `ML_PER_L` solution additions, nests the stock compositions, and preserves argon as a gas ingredient.

## Completeness

The direct generated record is missing the 1 L distilled water base row, structured solution rows for all nine stock additions, water rows in the Trace element, Selenite-tungstate, and Trace vitamins stocks, and a structured argon gas ingredient.

It preserves pH 9.6 and source preparation text, but the preparation steps point to stock additions that no longer exist structurally.

## Findings

- The base concentrations are inflated by MediaDive's `volume: 24` value: 64 g Na2CO3 becomes 2666.67 g/L, 40 g NaHCO3 becomes 1666.67 g/L, 18 g NaCl becomes 750 g/L, and 1 g K2HPO4 becomes 41.6667 g/L.
- All nine stock additions are flattened. The NH4Cl, MgCl2, yeast extract, Na2S x 9H2O, sodium crotonate, and sodium dithionite rows use milliliter addition values as final `G_PER_L` masses.
- Trace element, Selenite-tungstate, and Trace vitamins internals are emitted as direct final ingredients at their stock-local concentrations.
- The repaired TOGO M1385 owner is unmerged and should replace, link to, or subsume this direct JCM owner.

## Recommended Edits

- Re-curate the direct JCM owner using the repaired TOGO M1385 structure, or retire it as a duplicate of TOGO M1385.
- Correct the base carbonate-phosphate solution to 1 L so the base salts remain 64, 40, 18, and 1 g/L instead of the `volume: 24` inflated values.
- Restore all nine post-autoclave stock additions as nested solution additions with `ML_PER_L` concentrations.
- Preserve argon as a structured gas ingredient.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natroniella_medium_for_anb_phb2__18cdf3c0.yaml` and verify no 2666.67 g/L, 1666.67 g/L, 750 g/L, or 41.6667 g/L base rows remain.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored files for `GRMD=1289`, `mediadive.medium:J1289`, and `TOGO:M1385` to verify only the intended owner remains active.

## Additional Notes

None found.
