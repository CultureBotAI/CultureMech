# YAML Record Review: caldicellulosiruptor_medium_with_2_5_nacl

- Repository: CultureMech
- Record: data/merge_yaml/merged/caldicellulosiruptor_medium_with_2_5_nacl__fdda7690.yaml
- Started UTC: 2026-09-22T02:06:09Z
- Finished UTC: 2026-09-22T02:07:27Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003295`, `caldicellulosiruptor_medium_with_2_5_nacl`, `CALDICELLULOSIRUPTOR MEDIUM WITH 2.5% NaCl`, class `MediaRecipe`.
- Merge lineage: generated one-source merge of `caldicellulosiruptor_medium_with_2_5_nacl` on fingerprint `fdda7690921ea772e3f458c75640bb5cd42f46d2006c5a1e1f20a5e9b954b618`.
- Authoritative owner: `data/normalized_yaml/bacterial/caldicellulosiruptor_medium_with_2_5_nacl.yaml`.
- Claimed source identity: MediaDive / JCM Medium `J947`, `CALDICELLULOSIRUPTOR MEDIUM WITH 2.5% NaCl`.
- Related unmerged duplicate: `data/normalized_yaml/bacterial/TOGO_M994_Caldicellulosiruptor_Medium_With_2.5_NaCl.yaml` claims TOGO `M994` for the same JCM `JCM_M947` source.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- TOGO `M994` corroborates that JCM M947 is Caldicellulosiruptor Medium With 2.5% NaCl.
- The live JCM `GRMD=947` page returned `Nothing found`, so the original JCM page could not be independently checked.
- NH4Cl, NaCl, magnesium chloride hexahydrate, KH2PO4, K2HPO4, ferric chloride hexahydrate, cellobiose, glucose, L-cysteine hydrochloride hydrate, resazurin, HCl, iron dichloride tetrahydrate, zinc chloride, manganese(II) chloride tetrahydrate, boric acid, cobalt chloride hexahydrate, copper(II) chloride dihydrate, and sodium molybdate dihydrate are grounded to source-compatible identities.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Trypticase peptone and yeast extract are intentionally ungrounded as undefined biological mixtures.

## Evidence

- TOGO M994 lists the same JCM M947 identity and confirms 1 L distilled water, 1 g yeast extract, 25 g NaCl, 0.75 g KH2PO4, 0.9 g NH4Cl, 1.5 g K2HPO4, 0.5 mg resazurin, 0.4 g `MgCl2.6H2O`, 2.5 mg `FeCl3.6H2O`, 1 g cellobiose, 1 g glucose, 2 g Trypticase peptone, 0.75 g `L-Cysteine.HCl.H2O`, 1 ml Trace element solution SL-10 from Medium M433, and N2 in the main solution.
- TOGO preserves two preparation comments matching the JCM import: adjust pH to 7.5, and prepare the medium anaerobically under 100% N2 with filter-sterilized cellobiose added after autoclaving from an anoxic N2 stock.
- The normalized MediaDive `Main sol. J947` record represents the final base solution, not the SL-10 stock; it carries the same main ingredients and preparation notes, plus a placeholder `See source for composition` ingredient and an `incomplete_composition` flag.

## Completeness

- The pH 7.5 and preparation prose are present.
- The 1 L distilled water row from JCM / TOGO is absent from the generated medium.
- The 1 ml/L Trace element solution SL-10 addition is absent as a solution addition; instead, the SL-10 internal HCl and metals were promoted to final-medium ingredients.
- Empty `target_organisms` and `source_references` are not inherently defects for this import; the source formulation does not make a strain-specific growth claim.

## Findings

- Major: Trace element solution SL-10 is flattened into final-medium ingredient rows at stock strength; the source calls for only 1 ml of SL-10 per final liter.
- Major: the generated record omits the 1 L distilled-water row from the final medium.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.
- Minor: the acidified SL-10 stock HCl row is modeled as a final-medium `HCl` ingredient instead of stock solvent.
- Minor: the generated merge remains separate from the TOGO M994 duplicate, which carries the same JCM source identity with complementary pH and unit defects.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caldicellulosiruptor_medium_with_2_5_nacl.yaml`, not the generated merge.
- Model Trace element solution SL-10 as a 1 ml/L solution addition and move the stock-only HCl and metals into the stock recipe.
- Add the 1 L distilled water row from the JCM / TOGO recipe.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate grounding if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave the exact source label ungrounded.
- Keep `data/normalized_yaml/bacterial/mediadive_4969_Main_sol_J947.yaml` from leaking its placeholder `See source for composition` row into generated media.
- Reconcile this MediaDive / JCM owner with `data/normalized_yaml/bacterial/TOGO_M994_Caldicellulosiruptor_Medium_With_2.5_NaCl.yaml` as a source duplicate after both records agree on water, resazurin, ferric chloride, SL-10, pH, and anoxic preparation.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Compare the regenerated merge against the JCM M947 / TOGO M994 formulation, with special attention to the 1 L water row, the 1 ml/L M433 SL-10 addition, the pH 7.5, and the absence of stock-strength SL-10 components from final `ingredients`.

## Additional Notes

- `find . -iname '*caldicellulosiruptor*2*5*nacl*'` included ignored and hidden files and found both generated duplicate records, their active TOGO and MediaDive / JCM normalized owners, and the prior M994 review report.
- A gitignore-independent search for `mediadive.medium:J947`, `J947`, `GRMD=947`, `fdda7690`, `CALDICELLULOSIRUPTOR MEDIUM WITH 2.5% NaCl`, and `caldicellulosiruptor_medium_with_2_5_nacl` found the active MediaDive / JCM owner, the active TOGO owner, the related MediaDive `Main sol. J947` solution, both generated merges, registry/catalog rows, current content review manifest rows, the prior TOGO review report, and archived validation rows.
