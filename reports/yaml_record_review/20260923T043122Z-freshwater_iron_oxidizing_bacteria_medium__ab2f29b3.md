# YAML Record Review: freshwater_iron_oxidizing_bacteria_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium__ab2f29b3.yaml
- Started UTC: 2026-09-23T04:30:29Z
- Finished UTC: 2026-09-23T04:31:22Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:002974` / `freshwater_iron_oxidizing_bacteria_medium`, the direct MediaDive/JCM Medium J628 import.
- Compared it with maintained source `data/normalized_yaml/bacterial/freshwater_iron_oxidizing_bacteria_medium.yaml`.
- Cross-checked the MediaDive REST payload for J628, the live JCM GRMD=628 page, and the TOGO M641 duplicate generated as `data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:J628` correctly identifies JCM Medium 628, FRESHWATER IRON-OXIDIZING BACTERIA MEDIUM.
- Exact ignored-inclusive lookup for `mediadive.medium:J628`, `CultureMech:002974`, and `freshwater_iron_oxidizing_bacteria_medium__ab2f29b3` covered normalized and generated bacterial YAML; it found this single maintained JCM J628 owner and the suffixed generated file.
- The generated file lacks an explicit duplicate relationship to the TOGO M641 import even though TOGO M641 declares JCM 628 as its original source.
- Ingredient grounding for retained simple compounds is mostly exact, but the malformed `Trace minerals (see Medium No. 197` row is not grounded and is not a chemical ingredient.

## Evidence

- MediaDive and JCM both model J628 as a two-layer medium, with a 100 ml bottom layer composed of 50 ml FeS solution, 50 ml Modified Wolfe's mineral solution, and 1 g agarose, plus a 101 ml top layer composed of 100 ml Modified Wolfe's mineral solution, 1 ml trace minerals from Medium 197, 0.195 g MES, 0.042 g NaHCO3, and 0.15 g agarose.
- The generated record drops the bottom and top layer structures entirely and flattens every retained component into one parent ingredient list.
- The generated 154 g/L FeSO4 x 7 H2O and 132 g/L Na2S x 9 H2O values are FeS stock concentrations from 46.2 g and 39.6 g in 300 ml, not final medium concentrations.
- The generated NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and KH2PO4 rows are Modified Wolfe's mineral solution stock concentrations, not layer-specific additions.
- The generated 11.48515 g/L agarose row is a sum of the MediaDive bottom-layer and top-layer `g_l` projections, losing that the source has 1 g agarose in the 100 ml bottom layer and 0.15 g agarose in the 101 ml top layer.
- The preparation prose preserves the key JCM pH, autoclaving, overlay, gas-phase, FeS stock-preparation, and inoculation instructions, but the 10 ul inoculum value is mojibake in the imported text.

## Completeness

- Bottom layer, top layer, FeS solution, and Modified Wolfe's mineral solution are not structurally represented.
- The 1 ml trace vitamins addition from JCM Medium 197 is mentioned in preparation text but absent from the ingredient or solution graph.
- Trace minerals from JCM Medium 197 are represented as a malformed top-level ingredient instead of a cross-medium stock addition.
- The cross-source TOGO M641 duplicate remains generated as a separate record.

## Findings

- Major: MediaDive J628 layer and solution topology was flattened into a single ingredient list; the fix belongs in `data/normalized_yaml/bacterial/freshwater_iron_oxidizing_bacteria_medium.yaml` or the MediaDive/JCM importer.
- Major: FeS solution and Modified Wolfe's mineral solution stock concentrations are represented as final-medium g/L ingredients.
- Major: bottom- and top-layer agarose rows were summed across layers, erasing the source amounts and layer identity.
- Major: JCM Medium 197 trace minerals and trace vitamins are not represented as stock additions or resolvable cross-medium references.
- Major: the direct JCM J628 record is not linked or merged with the TOGO M641 record for the same JCM source.
- Minor: the imported preparation text mojibakes the 10 ul inoculation volume.

## Recommended Edits

- Rebuild the maintained JCM J628 record with explicit bottom-layer, top-layer, FeS-solution, and Modified Wolfe's-mineral-solution structure from MediaDive/JCM.
- Keep FeSO4 x 7 H2O and Na2S x 9 H2O inside FeS solution; keep NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and KH2PO4 inside Modified Wolfe's mineral solution.
- Represent JCM Medium 197 trace minerals and trace vitamins as cross-medium stock additions or explicit unresolved solution references.
- Preserve the two agarose additions separately rather than merging them.
- Add a `SOURCE_DUPLICATE` relationship to TOGO M641 or converge the JCM and TOGO imports into one generated record after they share the same topology.
- Regenerate `data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium__ab2f29b3.yaml` after normalized/import curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated JCM J628 YAML.
- Confirm no FeS or Modified Wolfe's stock component appears as a top-level final-medium ingredient.
- Confirm the bottom layer contains 50 ml FeS solution, 50 ml Modified Wolfe's mineral solution, and 1 g agarose, while the top layer contains 100 ml Modified Wolfe's mineral solution, 1 ml trace minerals from JCM 197, 0.195 g MES, 0.042 g NaHCO3, and 0.15 g agarose.
- Confirm TOGO M641 and direct JCM J628 have an explicit duplicate relationship or generate as one reviewed record.

## Additional Notes

- The generated file is derived data and is a one-source merge. The layer-flattening defects are already present in the normalized JCM J628 record.
