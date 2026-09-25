# YAML Record Review: mj_medium_for_defferibacter_sp_strain_nejineji__fb1ffbb2

- Repository: CultureMech
- Record: data/merge_yaml/merged/mj_medium_for_defferibacter_sp_strain_nejineji__fb1ffbb2.yaml
- Started UTC: 2026-09-24T07:44:23Z
- Finished UTC: 2026-09-24T07:44:55Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003097`
- Generated name: `mj_medium_for_defferibacter_sp_strain_nejineji`
- Generated source file: `data/merge_yaml/merged/mj_medium_for_defferibacter_sp_strain_nejineji__fb1ffbb2.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/mj_medium_for_defferibacter_sp_strain_nejineji.yaml`
- Duplicate generated record: `data/merge_yaml/merged/mj_medium_for_defferibacter_sp_strain_nejineji.yaml`
- Upstream source: MediaDive/JCM medium `J754`, `MJ MEDIUM FOR DEFFERIBACTER SP. STRAIN NEJINEJI`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mj_medium_for_defferibacter_sp_strain_nejineji__fb1ffbb2.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with MediaDive/JCM `J754`.
- The `media_term` points to `mediadive.medium:J754`.
- MediaDive `J754` and TOGO `M779` both point back to JCM `GRMD=754`, but an ignored-file-inclusive exact path search found they generated two CultureMech records.
- The direct salt, sulfur, resazurin, and vitamin rows are mostly grounded to CHEBI terms.
- `NiCl2 x 6 H2O` is grounded to generic nickel dichloride.
- The `Na2WO2 x 2 H2O` row has no ontology grounding and preserves MediaDive's source formula typo for sodium tungstate.

## Evidence

- MediaDive `J754` defines main solution `4693` with 30 g NaCl, 6.5 g `MgCl2 x 6 H2O`, 0.5 g `CaCl2 x 2 H2O`, 0.33 g KCl, 0.25 g NH4Cl, 0.14 g K2HPO4, milligram-scale Mn, Se, Ni, Co, Zn, Mo, Fe, W, H3BO3, resazurin, 10 g sulfur, 1000 ml water, 1 ml Trace vitamins solution `3861`, and 12.5 ml 8% NaHCO3.
- The MediaDive `g_l` values for the direct main-solution mineral rows match the generated values, including `0.00394477` `G_PER_L` for 4 mg manganese chloride and `0.000493097` `G_PER_L` for 0.5 mg resazurin.
- MediaDive Trace vitamins solution `3861` is a 1000 ml stock with ten vitamins plus water; the main solution uses only 1 ml of that stock.
- MediaDive records the 12.5 ml NaHCO3 addition with an `8%` attribute, not as 12.5 g/L direct sodium bicarbonate.
- The MediaDive/JCM preparation text adds `Na2S x 9H2O` from an anaerobic stock at final 0.1 g/L after distributing the medium into sulfur-containing culture vessels.

## Completeness

- The generated record has no `solutions` array, so MediaDive Trace vitamins solution `3861` was flattened into ten top-level vitamin ingredients.
- Each vitamin uses the raw stock concentration from solution `3861`; the 1 ml addition to 1014 ml of main solution was not applied.
- The 12.5 ml 8% NaHCO3 stock addition was flattened to a direct `12.5 G_PER_L` NaHCO3 ingredient.
- The final 0.1 g/L `Na2S x 9H2O` reducing-agent addition is absent as a structured ingredient and survives only in preparation prose.
- The TOGO import of the same JCM recipe publishes separately as `CultureMech:010187`.

## Findings

- High: The M190/MediaDive Trace vitamins stock was flattened at undiluted stock concentration even though `J754` calls for only 1 ml in the final 1014 ml main solution.
- High: The 12.5 ml 8% NaHCO3 addition was imported as `12.5 G_PER_L`, losing the percent stock concentration and ml addition semantics.
- High: The final 0.1 g/L sulfide addition is missing from structured ingredients.
- Medium: The MediaDive/JCM record was not merged with the TOGO `M779` record for the same original JCM medium.
- Medium: `Na2WO2 x 2 H2O` lacks ontology grounding.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/mj_medium_for_defferibacter_sp_strain_nejineji.yaml` with explicit Trace vitamins, 8% NaHCO3, and `Na2S x 9H2O` solution semantics.
- Dilute the Trace vitamins stock through the 1 ml addition to the 1014 ml MediaDive main solution or preserve it as a nested stock that records the 1 ml addition.
- Replace the direct `12.5 G_PER_L` NaHCO3 row with the 12.5 ml addition from an 8% stock.
- Add the final 0.1 g/L `Na2S x 9H2O` reducing-agent concentration to the structured recipe.
- Merge or alias the duplicate TOGO `M779` generated record after both normalized sources are repaired.
- Regenerate the merged record after repairing the normalized source.

## Follow-up Checks

- Re-fetch MediaDive `J754` and verify solution `3861` is no longer flattened at raw stock concentration.
- Confirm NaHCO3 and sulfide preserve their stock/final concentration semantics outside preparation prose.
- Repeat the ignored-file-inclusive exact path search for `mj_medium_for_defferibacter_sp_strain_nejineji` to verify the duplicate TOGO generated record is gone or intentionally aliased.
- Confirm `Na2WO2 x 2 H2O` is either grounded to the intended sodium tungstate term or corrected from the upstream typo with a curation note.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.

## Additional Notes

- None found.
