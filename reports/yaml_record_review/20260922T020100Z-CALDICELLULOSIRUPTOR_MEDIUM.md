# YAML Record Review: caldicellulosiruptor_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CALDICELLULOSIRUPTOR_MEDIUM.yaml
- Started UTC: 2026-09-22T01:59:38Z
- Finished UTC: 2026-09-22T02:01:00Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001777`, `caldicellulosiruptor_medium`, `CALDICELLULOSIRUPTOR MEDIUM`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caldicellulosiruptor_medium` on fingerprint `7c02afddf8a605a893151de9539475fffcb2c04a658654ac112faead2d613f23`.
- Authoritative owner: `data/normalized_yaml/bacterial/caldicellulosiruptor_medium.yaml`.
- Claimed source identity: DSMZ / MediaDive Medium `640`, `CALDICELLULOSIRUPTOR MEDIUM`.
- Related unmerged peer: `data/normalized_yaml/bacterial/KOMODO_640_CALDICELLULOSIRUPTOR_medium.yaml` also claims KOMODO 640 / DSMZ Medium 640.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- DSMZ Medium `640` is `CALDICELLULOSIRUPTOR MEDIUM`; the live DSMZ PDF agrees with the record's pH 7.2 and its preparation text.
- NH4Cl, NaCl, magnesium chloride hexahydrate, KH2PO4, K2HPO4, iron trichloride hexahydrate, L-cysteine hydrochloride hydrate, cellobiose, HCl, iron dichloride tetrahydrate, zinc chloride, manganese(II) chloride tetrahydrate, boric acid, cobalt chloride hexahydrate, copper(II) chloride dihydrate, and sodium molybdate dihydrate are grounded to source-compatible identities.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Trypticase peptone and yeast extract are intentionally ungrounded as undefined biological mixtures.

## Evidence

- DSMZ Medium 640 lists NH4Cl 0.90 g, NaCl 0.90 g, `MgCl2 x 6 H2O` 0.40 g, KH2PO4 0.75 g, K2HPO4 1.50 g, Trypticase peptone 2.00 g, yeast extract 1.00 g, Trace element solution SL-10 1.00 ml, 2.50 ml of 0.1% `FeCl3 x 6 H2O` in 0.2 N HCl, 0.50 ml of 0.1% sodium resazurin, `L-Cysteine HCl x H2O` 0.75 g, cellobiose 1.00 g, and distilled water 1000.00 ml.
- DSMZ lists Trace element solution SL-10 as a separate 1 L stock formulation, not direct final-medium ingredient rows.
- DSMZ instructs curators to leave cysteine and cellobiose out of the initial medium; sparge the base medium with 100% N2 for 30 to 45 min; add cysteine before pH adjustment; distribute and autoclave the medium under the same gas atmosphere; add cellobiose from a filter-sterilized anoxic stock after autoclaving; and adjust the completed medium to pH 7.2 if necessary.
- The DSMZ PDF also lists strain-specific replacements for cellobiose with D-xylose, D-glucose, D-fructose, or Na-pyruvate for multiple DSM strains.

## Completeness

- The pH 7.2 and preparation prose are present.
- The 1 L distilled water row is absent.
- The 1 ml/L Trace element solution SL-10 addition is absent as a solution addition.
- The 2.5 ml addition of acidified 0.1% `FeCl3 x 6 H2O` is represented only as final `FeCl3 x 6 H2O`; the record does not preserve the 0.2 N HCl stock carrier.
- The base record does not model DSMZ's strain-specific carbohydrate and pH variants.
- Empty `target_organisms` and `source_references` are not inherently defects for the base import; the DSMZ PDF supports the formulation but does not make a strain-specific growth claim.

## Findings

- Major: Trace element solution SL-10 is flattened into final-medium ingredient rows at stock strength; DSMZ calls for only 1 ml of SL-10 per final liter.
- Major: the generated record omits the 1000 ml distilled-water row from the final medium.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: DSMZ's acidified `FeCl3 x 6 H2O` addition lost the 0.2 N HCl stock context.
- Minor: the unmerged `KOMODO_640_CALDICELLULOSIRUPTOR_medium.yaml` peer cites DSMZ 640 but is not modeled as a source duplicate of the DSMZ / MediaDive owner and disagrees with DSMZ 640 by using 2.0 g/L NaHCO3 and 0.5 g/L cysteine.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldicellulosiruptor_medium.yaml`, not the generated merge.
- Model Trace element solution SL-10 as a 1 ml/L solution addition and move the stock-only HCl and metals into the stock recipe.
- Preserve the 2.5 ml/L acidified `FeCl3 x 6 H2O` stock context rather than representing it solely as an anonymous final 0.0025 g/L ferric chloride row.
- Add the 1 L distilled water row from DSMZ 640.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Audit the KOMODO 640 owner and strain-specific 640 variants against DSMZ 640 before linking source duplicates or regenerating merged YAML.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against DSMZ Medium 640, with special attention to the 1 ml/L SL-10 addition, the acidified ferric chloride addition, the 1 L water row, the absence of stock-strength SL-10 rows from final `ingredients`, and the hydrate-specific nickel chloride grounding.
- Separately verify which DSMZ 640 cellobiose-replacement instructions are already covered by KOMODO or TOGO variants and add missing supported variants as separate normalized records.

## Additional Notes

- `find . -iname '*caldicellulosiruptor*'` included ignored and hidden files and found the reviewed generated merge plus multiple Caldicellulosiruptor, modified Caldicellulosiruptor, JCM, TOGO, and KOMODO normalized/generated relatives.
- A gitignore-independent search for `CALDICELLULOSIRUPTOR_MEDIUM`, `mediadive.medium:640`, `komodo.medium:640`, `KOMODO_640_CALDICELLULOSIRUPTOR`, and `caldicellulosiruptor_medium` found the active DSMZ owner, the active KOMODO 640 peer, same-source KOMODO 640 strain records, related generated merges, registry/catalog rows, current content review manifest rows, and archived validation rows.
