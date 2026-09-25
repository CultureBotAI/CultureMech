# YAML Record Review: caldicoprobacter_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDICOPROBACTER_MEDIUM.yaml
- Started UTC: 2026-09-22T02:11:49Z
- Finished UTC: 2026-09-22T02:14:24Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003989`, `caldicoprobacter_medium`, `CALDICOPROBACTER medium`, class `MediaRecipe`.
- Merge lineage: generated two-source merge of `KOMODO_1233_CALDICOPROBACTER_medium` and `caldicoprobacter_medium` on fingerprint `6abc9c91eecf54cd97c5e7d0a7f66fd86e7b5843b1bafea4319766df1302bcba`.
- Authoritative owners: `data/normalized_yaml/bacterial/KOMODO_1233_CALDICOPROBACTER_medium.yaml` for KOMODO 1233 and `data/normalized_yaml/bacterial/caldicoprobacter_medium.yaml` for DSMZ / MediaDive Medium 1233.
- Claimed source identity: KOMODO Medium 1233, `CALDICOPROBACTER medium`, merged with DSMZ / MediaDive Medium 1233, `CALDICOPROBACTER MEDIUM`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium 1233 is `CALDICOPROBACTER MEDIUM`; the live DSMZ PDF agrees with the record's pH range 7.3 to 7.5 and with the DSMZ owner's preparation prose.
- KOMODO Medium 1233 cites DSMZ Medium 1233 and has the same ingredient signature as the active DSMZ owner, so the `SOURCE_DUPLICATE` relationship is source-compatible.
- NaCl, KCl, magnesium chloride hexahydrate, NH4Cl, HEPES, ferrous ammonium sulfate hexahydrate, calcium chloride dihydrate, manganese(II) chloride tetrahydrate, L-cysteine hydrochloride hydrate, D-glucose, and resazurin are grounded to source-compatible identities.
- `Na2HPO4 x 7 H2O` is grounded to anhydrous disodium hydrogenphosphate (`CHEBI:34683`), not the heptahydrate used by the source.
- Yeast extract and Tryptone are intentionally ungrounded as undefined biological mixtures.

## Evidence

- DSMZ Medium 1233 lists NaCl 0.50 g, KCl 0.20 g, `MgCl2 x 6 H2O` 0.18 g, NH4Cl 0.10 g, HEPES 4.80 g, `Na2HPO4 x 7 H2O` 54 mg, 4 ml of 0.1% ferrous ammonium sulfate hexahydrate, 2 ml of 0.1% calcium chloride dihydrate, 1 ml of 0.1% manganese chloride tetrahydrate, yeast extract 5.00 g, Tryptone 2.50 g, 0.50 ml of 0.1% sodium resazurin, L-cysteine HCl hydrate 1.00 g, D-glucose 5.00 g, and distilled water 1000.00 ml.
- Both maintained owners carry all mass concentrations at approximately `source_value / 1.007`; for example, DSMZ's 0.50 g NaCl appears as 0.496524 g/L, 4.80 g HEPES appears as 4.76663 g/L, 5.00 g D-glucose appears as 4.96524 g/L, and the 54 mg sodium phosphate row appears as 0.0536246 g/L.
- The 1.007 divisor matches the 4 ml, 2 ml, and 1 ml source stock additions, so the imported concentrations appear to have been renormalized after treating simple 0.1% w/v stock volumes as 7 ml of final-volume expansion.
- DSMZ instructs curators to dissolve ingredients except cysteine and glucose, sparge with 100% N2, add solid cysteine, adjust to pH 7.3 to 7.5, dispense and autoclave under 100% N2, and add glucose from a sterile anoxic 100% N2 stock before inoculation.
- DSMZ describes 10 to 20 mg/L sodium dithionite as an optional reducing addition.

## Completeness

- The pH range is present.
- The DSMZ owner's preparation steps are absent from the generated merge because the merge chose the KOMODO owner.
- The 1000 ml distilled-water row is absent.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: all ingredient concentrations in both maintained owners are lower than the inspected DSMZ formula by a constant 1000/1007 factor, apparently from renormalizing the formula around 7 ml of simple 0.1% stock additions.
- Major: the generated merge chose the KOMODO owner and dropped the DSMZ owner's N2 sparging, autoclaving, glucose-addition, pH-adjustment, and optional sodium dithionite preparation steps.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: `Na2HPO4 x 7 H2O` is grounded to the wrong hydrate form.
- Major: the generated record inherits KOMODO's note `Aerobic: Yes`, but DSMZ Medium 1233 is explicitly prepared anoxically under 100% N2.
- Minor: the 0.1% w/v Fe, Ca, and Mn solution additions are present only as computed grams per liter, so the source stock concentrations and addition volumes are not recoverable from the ingredient list.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/KOMODO_1233_CALDICOPROBACTER_medium.yaml` and `data/normalized_yaml/bacterial/caldicoprobacter_medium.yaml`, not the generated merge.
- Restore exact DSMZ Medium 1233 concentrations before the 1000/1007 renormalization.
- Add the 1 L distilled water row from DSMZ Medium 1233.
- Preserve the DSMZ preparation steps in the generated duplicate merge, either by enriching the KOMODO owner or by making the DSMZ owner canonical when it has the same formulation plus richer preparation evidence.
- Remove or qualify KOMODO's `Aerobic: Yes` note during DSMZ enrichment for this anoxic medium.
- Correct `Na2HPO4 x 7 H2O` to a hydrate-specific disodium hydrogen phosphate heptahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Consider modeling the Fe, Ca, and Mn 0.1% w/v stock additions explicitly so the imported ingredient list preserves DSMZ's solution volumes as well as final masses.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against both normalized owners.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 1233, with special attention to exact source concentration values, the 1 L water row, the anoxic DSMZ preparation steps, and the sodium phosphate hydrate grounding.

## Additional Notes

- `find . -iname '*caldicoprobacter*'` included ignored and hidden files and found only the two reviewed Caldicoprobacter generated merges, three active normalized owners, and the prior Caldicoprobacter Algeriensis review report.
- A gitignore-independent search for Caldicoprobacter Medium labels, slugs, and DSMZ / KOMODO 1233 identifiers found the active DSMZ owner, the active KOMODO duplicate owner, the generated merge, registry/catalog rows, current content review manifest rows, archived DSMZ 1233 validation rows, and the archived DSMZ/KOMODO source-duplicate review row.
