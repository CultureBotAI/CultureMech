# YAML Record Review: freshwater_iron_oxidizing_bacteria_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium.yaml
- Started UTC: 2026-09-23T04:27:36Z
- Finished UTC: 2026-09-23T04:29:11Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:010042` / `freshwater_iron_oxidizing_bacteria_medium`, the TOGO Medium M641 import of JCM Medium 628.
- Compared it with maintained source `data/normalized_yaml/bacterial/TOGO_M641_Freshwater_Iron-Oxidizing_Bacteria_Medium.yaml`.
- Cross-checked the TOGO M641 API payload, the live JCM GRMD=628 page, and the direct JCM/MediaDive duplicate generated as `data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium__ab2f29b3.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `TOGO:M641` correctly identifies Freshwater Iron-Oxidizing Bacteria Medium, TOGO's import of JCM Medium 628.
- Exact ignored-inclusive lookup for `TOGO:M641`, `TOGO_M641_Freshwater_Iron-Oxidizing_Bacteria_Medium`, and the JCM GRMD=628 URL covered normalized and generated bacterial YAML and found the maintained TOGO owner plus a separate direct JCM J628 copy of the same source medium.
- The generated record's main identity is correct, but it is not linked or merged with the direct JCM J628 record even though the TOGO metadata names `JCM_M628` as the original source.
- CO2, N2, and O2 are grounded gas-phase conditions in the source, not quantified top-layer solutes.

## Evidence

- The JCM 628 and TOGO M641 sources define a two-layer tube medium: a bottom FeS layer, a semisolid mineral top layer, pH 6.2 adjustment, post-autoclave pH adjustment to 6.1-6.4 by sterile CO2 bubbling, 0.75 ml bottom plus 3.75 ml top per 10 ml vial, and an N2/CO2/O2 gas phase.
- Bottom and top layer rows in TOGO are volume subcomponent rows. The generated record imports `Bottom layer` as 100 g/L and `Top layer` as 101 g/L top-level ingredients, which are not chemical concentrations.
- FeS solution and Modified Wolfe's mineral solution are source stock solutions. The generated record both creates empty `Unknown solution` stubs for those stocks and flattens their internal FeSO4, Na2S, NH4Cl, MgSO4, CaCl2, KH2PO4, and water rows into top-level final-medium ingredients.
- Source agarose is layer-specific: 1 g in the 100 ml bottom layer and 0.15 g in the 101 ml top layer. The generated record sums those layer-local rows into one 1.15 g/L agarose row.
- The top-layer 1 ml trace mineral solution from JCM Medium 197 is retained only as an empty stock reference, so the required cross-medium solution is not resolvable from the generated YAML.

## Completeness

- The layered recipe is materially incomplete because bottom and top layers are not represented as composed stock or layer solutions.
- FeS solution and Modified Wolfe's solution compositions are present as unsupported top-level ingredient rows and missing from the corresponding solution objects.
- The JCM 197 trace mineral reference has no composition, and the Medium 197 trace vitamins addition mentioned in preparation text is not represented as a structured addition.
- The duplicate direct JCM J628 import remains generated separately under `freshwater_iron_oxidizing_bacteria_medium__ab2f29b3.yaml`.

## Findings

- Major: TOGO M641 layer and stock volumes are imported as `G_PER_L` ingredient or solution concentrations; the fix belongs in `data/normalized_yaml/bacterial/TOGO_M641_Freshwater_Iron-Oxidizing_Bacteria_Medium.yaml` or the TOGO import transform.
- Major: FeS solution, Modified Wolfe's mineral solution, and trace mineral solution are empty `Unknown solution` records while their component rows are flattened into the parent recipe.
- Major: the bottom-layer and top-layer agarose rows were merged into a single parent agarose ingredient, losing layer identity and units.
- Major: the TOGO M641 record is not linked or merged with the direct JCM J628 record for the same original source medium.
- Minor: imported TOGO gas-property notes retain non-English source text instead of an English or normalized gas-phase note.

## Recommended Edits

- Rebuild normalized TOGO M641 with explicit bottom-layer and top-layer solution records that preserve source volumes and compositions.
- Nest FeS solution and Modified Wolfe's mineral solution under the proper layers instead of flattening their stock contents into final-medium ingredients.
- Represent JCM Medium 197 trace minerals and trace vitamins as cross-medium stock additions or explicit unresolved solution references rather than empty compositions.
- Keep bottom and top agarose additions separate.
- Add a `SOURCE_DUPLICATE` relationship to the direct JCM J628 record, or converge the TOGO and JCM imports so regeneration emits one record for JCM 628.
- Regenerate `data/merge_yaml/merged/freshwater_iron_oxidizing_bacteria_medium.yaml` after normalized/import curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated TOGO M641 YAML.
- Confirm `Bottom layer` and `Top layer` do not appear as g/L chemical ingredients.
- Confirm FeSO4 x 7 H2O and Na2S x 9 H2O remain scoped inside FeS solution, and NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and KH2PO4 remain scoped inside Modified Wolfe's mineral solution.
- Confirm TOGO M641 and direct JCM J628 have an explicit duplicate relationship or generate as one reviewed record.

## Additional Notes

- The JCM GRMD=628 page was live during review and matched the TOGO M641 API for the key layer, stock, and preparation structure. The generated file is derived data, so the repair should target the normalized TOGO record or the importer rather than patching `data/merge_yaml/merged` directly.
