# YAML Record Review: freshwater_iron_oxidizing_bacteria_medium_ii

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium_ii.yaml
- Started UTC: 2026-09-23T04:32:30Z
- Finished UTC: 2026-09-23T04:34:02Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:007658` / `freshwater_iron_oxidizing_bacteria_medium_ii`, the TOGO Medium M1136 import of JCM Medium 1067.
- Compared it with repaired maintained source `data/normalized_yaml/bacterial/TOGO_M1136_Freshwater_Iron-Oxidizing_Bacteria_Medium-II.yaml`.
- Cross-checked TOGO M1136, JCM 1067, and the cross-medium JCM 628, 151, and 197 stock sources used by the September repair.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `TOGO:M1136` correctly identifies Freshwater Iron-Oxidizing Bacteria Medium-II, TOGO's import of JCM Medium 1067.
- Exact ignored-inclusive lookup for `TOGO:M1136`, `mediadive.medium:J1067`, `JCM_M1067`, and the JCM GRMD=1067 URL covered normalized and generated bacterial YAML; it found the TOGO owner, a direct JCM J1067 owner, and generated files for both source paths.
- The generated TOGO record is stale relative to the September normalized repair: generated history ends at the August merge, while normalized YAML has `RESOLVED_TOGO_M1136_SCORE15` and restored structured stock solutions.
- Carbon dioxide and nitrogen are gas-phase conditions in the JCM source, not top-layer solutes.

## Evidence

- JCM 1067 defines a 100 ml bottom layer containing 50 ml FeS solution from JCM 628, 50 ml Modified Wolfe's solution from JCM 628, and 1.5 g Agar, Noble.
- JCM 1067 defines a 1.01 L top layer containing 1 L Modified Wolfe's solution from JCM 628 and 10 ml Trace minerals from JCM 151.
- After autoclaving both layers, JCM 1067 adds 10 ml/L filter-sterilized Trace vitamins from JCM 197 and 5.25 ml/L filter-sterilized 8% NaHCO3 to the cooled top layer, then uses a five- to six-fold top:bottom layer volume and an N2/CO2 gas phase.
- The generated record instead turns `Bottom layer` and `Top layer` into 100 g/L and 1010 g/L ingredients.
- The generated `solutions` array consists of six `Unknown solution` entries with empty compositions and source volumes such as 50 ml, 10 ml, and 5.25 ml imported as `G_PER_L`.
- The repaired normalized record restores FeS, Modified Wolfe's, Trace minerals, 8% NaHCO3, and Trace vitamins as structured solutions with JCM 628, 151, and 197 component recipes.

## Completeness

- The generated record lacks the September normalized repair and is incomplete for every referenced stock solution.
- FeS solution, Modified Wolfe's solution, Trace minerals, 8% NaHCO3 solution, and Trace vitamins are empty generated stubs despite being populated upstream.
- The preparation workflow from JCM 1067 is absent from generated YAML but present upstream in repaired normalized YAML.
- The direct JCM J1067 duplicate remains generated separately as `freshwater_iron_oxidizing_bacteria_medium_ii__3950b409.yaml`.

## Findings

- Major: generated TOGO M1136 is stale relative to the repaired normalized record; regeneration must include the `RESOLVED_TOGO_M1136_SCORE15` layer, solution, stock-composition, reference, and preparation fixes.
- Major: layer rows and stock-addition rows were imported as `G_PER_L` concentrations in generated YAML, so 100 ml bottom layer, 1.01 L top layer, 50 ml FeS solution, 10 ml Trace minerals, 5.25 ml NaHCO3 solution, and 10 ml Trace vitamins all have wrong units.
- Major: all generated solution objects are empty `Unknown solution` records, losing the repaired FeS, Modified Wolfe's, JCM 151 Trace minerals, JCM 197 Trace vitamins, and NaHCO3 stock compositions.
- Major: direct JCM J1067 and TOGO M1136 remain generated as separate records without a duplicate relationship.
- Minor: generated gas-property notes retain non-English source text instead of the normalized N2/CO2 gas-phase statement.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium_ii.yaml` from current normalized YAML and verify that the September 11 repaired solution graph is preserved.
- If regeneration still drops `solutions.composition`, update merge logic to preserve the nested stock compositions, per-liter stock-addition amounts, references, and preparation steps from the normalized M1136 record.
- Keep `Bottom layer` and `Top layer` as solution structure, not ingredient rows.
- Add a `SOURCE_DUPLICATE` relationship to direct JCM J1067 or converge the TOGO and JCM imports after both use equivalent layer topology.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated TOGO M1136 YAML.
- Confirm generated M1136 contains populated FeS, Modified Wolfe's, Trace minerals, 8% NaHCO3, and Trace vitamins solution compositions.
- Confirm generated M1136 includes the JCM 1067 autoclave, cooling, filter-sterile addition, overlay, gas-phase, and storage steps from the repaired normalized record.
- Confirm no layer volume or stock-addition volume is emitted as `G_PER_L`.

## Additional Notes

- The maintained TOGO M1136 source was already curated on September 11, 2026. The generated review target still reflects the pre-repair August merge output.
