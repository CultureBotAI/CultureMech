# YAML Record Review: DESULFOVIBRIO B0109P2 MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_b0109p2_medium__a5c9bbc2.yaml`
- Started UTC: 2026-09-22T20:26:44Z
- Finished UTC: 2026-09-22T20:27:18Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:003174` for `desulfovibrio_b0109p2_medium__a5c9bbc2`, a MediaDive import of JCM Medium J830.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The generated record is grounded to `mediadive.medium:J830`, `DESULFOVIBRIO B0109P2 MEDIUM`, with the original JCM GRMD 830 URL preserved in `notes`.

The MediaDive REST record for J830 confirms that this is JCM Medium J830 and lists the same basal medium, 1 ml of Trace element solution, and four anaerobic stock additions per liter final volume. The TOGO M866 normalized record has the same recipe name and notes `Original source: JCM - JCM_M830`, so it is an exact provider duplicate of this JCM medium even though it currently generates separately as `data/merge_yaml/merged/DESULFOVIBRIO_B0109P2_MEDIUM.yaml`.

## Evidence

The basal ingredient quantities imported from MediaDive J830 are internally scaled by the 1001 ml main-solution volume and correspond to the source table: ammonium chloride, phosphate salts, sodium sulfate, sodium chloride, potassium chloride, calcium chloride dihydrate, sodium thiosulfate pentahydrate, yeast extract, cysteine hydrochloride hydrate, and resazurin.

The source then adds 1 ml Trace element solution, 20 ml 1.0 M Sodium lactate, 20 ml 15% `MgCl2 x 6 H2O`, 40 ml 5% `NaHCO3`, and 20 ml 2% `Na2S x 9 H2O` to reach 1 liter final volume. The generated record does not preserve those additions as stock solutions.

The Trace element solution in MediaDive uses 12.5 ml 25% HCl, 2.1 g `FeSO4 x 7 H2O`, 30 mg `H3BO3`, 100 mg `MnCl2 x 4 H2O`, 190 mg `CoCl2 x 6 H2O`, 24 mg `NiCl2 x 6 H2O`, 2 mg `CuCl2 x 2 H2O`, 144 mg `ZnSO4 x 7 H2O`, 36 mg `Na2MoO4 x 2 H2O`, and 987 ml water. Those values are stock-solution recipe values, not final medium concentrations.

## Completeness

The record keeps the core anaerobic preparation text: mix and adjust to pH 7.4, boil, cool under `N2-CO2 (4:1, v/v)`, distribute under the same gas mixture, autoclave, add stock solutions aseptically and anaerobically, filter-sterilize sodium bicarbonate, autoclave the other solutions under nitrogen, and readjust pH.

The composition is incomplete because the 900 ml distilled-water row from the main JCM solution is absent and every subordinate solution is flattened or reduced to a top-level ingredient instead of being represented as a `solutions` entry.

## Findings

- High: The Trace element solution was flattened into nine target ingredients. The generated final medium now shows stock recipe values such as HCl 12.5 G/L, `FeSO4 x 7 H2O` 2.1 G/L, `H3BO3` 0.03 G/L, and `CuCl2 x 2 H2O` 0.002 G/L as final ingredients, even though the source adds only 1 ml of that stock solution per liter.
- High: The four final-volume stock additions were copied from source milliliter quantities into `G_PER_L` rows. `Sodium lactate`, `MgCl2 x 6 H2O`, `NaHCO3`, and `Na2S x 9 H2O` should be modeled as 20 ml, 20 ml, 40 ml, and 20 ml solution additions, respectively, or converted from their 1.0 M, 15%, 5%, and 2% stock strengths.
- Medium: The generated record omits the 900 ml distilled-water row from the MediaDive J830 main solution.
- Medium: The exact JCM M830 provider duplicate remains split. The MediaDive J830 import produced this record, while the TOGO M866 import produced `DESULFOVIBRIO_B0109P2_MEDIUM.yaml`; TOGO also carries empty `Unknown solution` stubs and an unsupported `NaCO3 solution` stub that should be cleaned before rematching.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_b0109p2_medium.yaml` so the 1 ml Trace element solution is a subordinate solution with the MediaDive/JCM stock composition and water.
- Represent the 20 ml sodium lactate, 20 ml magnesium chloride, 40 ml sodium bicarbonate, and 20 ml sodium sulfide post-autoclave additions as solution additions rather than final 20/20/40/20 G/L ingredients.
- Restore the 900 ml distilled-water row in the main solution.
- Repair `data/normalized_yaml/bacterial/TOGO_M866_Desulfovibrio_B0109P2_Medium.yaml`, remove source-unsupported empty solution stubs, and ensure the TOGO and MediaDive JCM M830 records either merge or are explicitly related as exact source duplicates after regeneration.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on both normalized records and the regenerated merged records.
- Regenerate `data/merge_yaml/merged` and confirm there is a single generated record for JCM Medium J830, or a documented exact duplicate relation if the providers intentionally remain separate.
- Compare the regenerated solution additions against MediaDive J830 and TOGO M866 so the Trace element solution remains at 1 ml/L and the four post-autoclave stock additions keep their source volumes.

## Additional Notes

None found.
