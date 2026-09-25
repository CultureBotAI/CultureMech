# YAML Record Review: caldinitratiruptor_microaerophilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/caldinitratiruptor_microaerophilus_medium__a882ad30.yaml
- Started UTC: 2026-09-22T02:22:23Z
- Finished UTC: 2026-09-22T02:23:52Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003125`, `caldinitratiruptor_microaerophilus_medium`, `CALDINITRATIRUPTOR MICROAEROPHILUS MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caldinitratiruptor_microaerophilus_medium` on fingerprint `a882ad30b50962c0bb119ec354a8e277c9e86065d6671d799d365da2d59ac1c8`.
- Authoritative owner: `data/normalized_yaml/bacterial/caldinitratiruptor_microaerophilus_medium.yaml`.
- Claimed source identity: JCM Medium 782, `CALDINITRATIRUPTOR MICROAEROPHILUS MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The live JCM `GRMD=782` page is `CALDINITRATIRUPTOR MICROAEROPHILUS MEDIUM`; the source identity is correct.
- KH2PO4, K2HPO4, NH4Cl, KNO3, NaCl, KCl, calcium chloride dihydrate, magnesium chloride hexahydrate, yeast extract, bicarbonate, glucose, and the trace-minerals rows are grounded to source-compatible identities where grounded.
- `KNO3` has a correct current primary potassium nitrate term but still carries a legacy `mediaingredientmech_term` field instead of a `mediaingredientmech_chebi_term` field.
- Yeast extract is intentionally ungrounded as an undefined biological mixture.

## Evidence

- JCM Medium 782 lists KH2PO4 0.3 g, K2HPO4 0.3 g, NH4Cl 1.0 g, KNO3 1.7 g, NaCl 1.0 g, KCl 0.1 g, calcium chloride dihydrate 0.1 g, magnesium chloride hexahydrate 0.25 g, 10 ml trace minerals, yeast extract 1.0 g, and 1 L distilled water in the autoclaved base.
- JCM instructs curators to adjust the base to pH 7.2 with KOH, autoclave under a 4:1 N2 / CO2 gas mixture, and add 25 ml of 8% NaHCO3 solution plus 20 ml of 1 M glucose solution per liter from anaerobic stocks after cooling.
- JCM Medium 151 lists Trace minerals as a separate 1 L stock recipe; it is not a set of direct final-medium ingredient rows in JCM 782.
- The generated record carries JCM 782 base masses divided by approximately 1.055; for example, 0.3 g KH2PO4 appears as 0.28436 g/L, 1.0 g NH4Cl appears as 0.947867 g/L, and 1.7 g KNO3 appears as 1.61137 g/L.
- The 1.055 divisor matches the 10 ml trace-minerals, 25 ml bicarbonate, and 20 ml glucose solution additions, so the imported final-medium masses appear to have been renormalized after treating the source's 55 ml of stock additions as final-volume expansion.

## Completeness

- The pH value and the source preparation paragraph are present.
- The 1 L distilled-water row from JCM 782 is absent.
- The 10 ml trace-minerals addition is absent as a solution ingredient.
- The 25 ml bicarbonate and 20 ml glucose solution additions are absent as solution ingredients.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the inspected JCM source supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: final-medium base masses are lower than the inspected JCM formula by a constant 1000/1055 factor, apparently from renormalizing around 55 ml of post-base solution additions.
- Major: Trace minerals from JCM Medium 151 are flattened into final-medium ingredient rows at stock strength; JCM 782 calls for only 10 ml of this stock per final liter.
- Major: duplicate cleanup merged final-medium NaCl and CaCl2 rows with Trace minerals NaCl and CaCl2 rows, yielding unsupported 1.947867 g/L NaCl and 0.1947867 g/L `CaCl2 x 2 H2O` rows.
- Major: the 25 ml 8% NaHCO3 and 20 ml 1 M glucose additions are represented as 25 g/L NaHCO3 and 20 g/L glucose.
- Major: the 1 L water row from the final medium is absent.
- Major: the same JCM 782 source exists as a separate TOGO M812 generated record, `data/merge_yaml/merged/CALDINITRATIRUPTOR_MICROAEROPHILUS_MEDIUM.yaml`, instead of a `SOURCE_DUPLICATE` merge.
- Minor: `KNO3` still uses a legacy `mediaingredientmech_term` object despite the CHEBI-keying migration recorded in `curation_history`.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldinitratiruptor_microaerophilus_medium.yaml`, not the generated merge.
- Restore exact JCM 782 base concentrations before the 1000/1055 renormalization.
- Model Trace minerals as a 10 ml/L solution addition and move the JCM 151 trace-minerals-only rows into the corresponding stock recipe.
- Restore the 8% NaHCO3 and 1 M Glucose additions as 25 ml/L and 20 ml/L solution additions instead of gram-per-liter direct ingredients.
- Add the 1 L distilled water row from JCM 782.
- Link or merge the direct JCM 782 and TOGO M812 records as source duplicates after both owners preserve equivalent solution semantics.
- Migrate the `KNO3` MediaIngredientMech link to the CHEBI-keyed field.
- Regenerate merged YAML and verify that the direct JCM and TOGO imports no longer split into two generated records.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized direct JCM owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Re-run an ignored-inclusive exact search for `TOGO:M812`, `JCM_M782`, `GRMD=782`, and `mediadive.medium:J782` to confirm the TOGO and direct JCM imports are represented in one generated source-duplicate merge.
- Compare the regenerated merge against JCM 782 and JCM 151, with special attention to exact base concentrations, the 1 L water row, the 10 ml trace-minerals addition, the 25 ml bicarbonate and 20 ml glucose additions, and the absence of flattened trace-minerals rows.

## Additional Notes

- `find . -iname '*caldinitratiruptor*'` included ignored and hidden files and found the base Caldinitratiruptor DSMZ/KOMODO pair, this direct JCM generated split, the TOGO M812 generated split, and their active normalized owners.
- A gitignore-independent search for JCM 782 and direct Caldinitratiruptor microaerophilus identifiers found the active direct JCM owner, the active TOGO owner, their split generated merges, source-index rows, current content review manifest rows, and archived validation rows for the retired JCM 782 filename.
