# YAML Record Review: saltwater_iron_oxidizing_bacteria_medium__fbf85ad5

- Repository: CultureMech
- Record: data/merge_yaml/merged/saltwater_iron_oxidizing_bacteria_medium__fbf85ad5.yaml
- Started UTC: 2026-09-25T04:05:45Z
- Finished UTC: 2026-09-25T04:05:45Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002975`, `saltwater_iron_oxidizing_bacteria_medium`, from `data/merge_yaml/merged/saltwater_iron_oxidizing_bacteria_medium__fbf85ad5.yaml`.

The record is a single-source MediaDive/JCM J629 import for `SALTWATER IRON-OXIDIZING BACTERIA MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to JCM Medium J629, but it is not a complete structured recipe for JCM 629.

JCM 629 defines this medium by reference: it uses JCM 628 with artificial saltwater instead of Modified Wolfe's mineral solution. MediaDive imported the artificial saltwater table but did not expand the referenced JCM 628 bottom and top layers.

## Evidence

JCM 629 and MediaDive J629 contain one explicit artificial-saltwater stock with 27.5 g NaCl, 5.38 g MgCl2 x 6 H2O, 6.78 g MgSO4 x 7 H2O, 0.72 g KCl, 0.2 g NaHCO3, 1.4 g CaCl2 x 2 H2O, 1 g NH4Cl, 0.05 g KH2PO4, and 1 L distilled water.

The JCM 629 page says to use JCM 628 with this artificial saltwater in place of Modified Wolfe's mineral solution. JCM 628 is the two-layer iron-oxidizing bacteria medium with a FeS bottom layer, a semisolid mineral-salts top layer, trace minerals, trace vitamins, pH adjustments, and N2-CO2-O2 headspace replacement.

## Completeness

The artificial-saltwater salts are present.

The artificial-saltwater distilled-water row is absent.

All JCM 628-derived layer structure is absent: bottom layer, top layer, FeS solution, trace minerals, trace vitamins, agarose, MES, pH handling, vial assembly, and N2-CO2-O2 headspace handling.

## Findings

The generated direct MediaDive record incorrectly represents JCM 629 as a liquid artificial-saltwater recipe. The source is a layered iron-gradient medium that uses artificial saltwater as one stock.

The JCM 628 reference was left as a prose preparation step instead of being expanded into bottom and top layer solution scopes.

The record is a duplicate split from TOGO M642, which captured the JCM 628-derived layer scaffolding but then flattened it incorrectly. These two JCM 629 imports should converge after the reference expansion and TOGO layer-scope fixes are applied.

The 1 L artificial-saltwater distilled-water row is missing.

## Recommended Edits

Expand the MediaDive/JCM J629 import with the JCM 628 bottom and top layer recipe, substituting artificial saltwater wherever JCM 628 uses Modified Wolfe's mineral solution.

Represent artificial saltwater as a stock used by the two layers, not as the complete JCM 629 parent recipe.

Regenerate the merge layer after the MediaDive and TOGO JCM 629 paths carry equivalent layer semantics so they collapse into one generated record.

## Follow-up Checks

After regeneration, confirm there is no direct generated `saltwater_iron_oxidizing_bacteria_medium` record that consists only of artificial-saltwater salts.

Confirm the direct MediaDive and TOGO M642 records both retain JCM 629 provenance and one regenerated two-layer formulation.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
