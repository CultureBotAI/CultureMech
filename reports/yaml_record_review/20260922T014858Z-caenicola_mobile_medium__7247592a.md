# YAML Record Review: caenicola_mobile_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/caenicola_mobile_medium__7247592a.yaml
- Started UTC: 2026-09-22T01:48:58Z
- Finished UTC: 2026-09-22T01:49:06Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:002346`, `caenicola_mobile_medium`, `CAENICOLA MOBILE MEDIUM`, class `MediaRecipe`.
- Merge lineage: one source recipe, `caenicola_mobile_medium`, on fingerprint `7247592ad6984faf6ec0ab052393c661b7ed4bcd2d8d642491cdcde0a5070157`.
- Authoritative owner: `data/normalized_yaml/bacterial/caenicola_mobile_medium.yaml`.
- Claimed source identity: JCM Medium `J1175`, mirrored by TOGO `M1259`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The source identity matches a live JCM page: JCM `1175` is `CAENICOLA MOBILE MEDIUM`, and the recipe's pH 7.5 plus three preparation paragraphs are copied from that source.
- TOGO `M1259` carries the same source as original medium `JCM_M1175`, so this record is a duplicate of the active TOGO import at `data/normalized_yaml/bacterial/TOGO_M1259_Caenicola_Mobile_Medium.yaml`.
- The first 13 non-water ingredient amounts are scaled by 1/1.01 from the JCM gram rows, which indicates the importer divided by the 1.010 L sum of 975 ml base water plus 25 ml bicarbonate, 1 ml trace metal, 1 ml vitamin, and 8 ml sulfide additions.
- `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride (`CHEBI:34887`), not nickel dichloride hexahydrate.
- Yeast extract, Tryptone, and Casamino acids are intentionally ungrounded undefined biological mixtures.

## Evidence

- JCM `1175` lists KH2PO4 0.5 g, K2HPO4 0.5 g, NH4Cl 0.5 g, NaCl 0.4 g, MgCl2 x 6H2O 0.3 g, CaCl2 x 2H2O 0.05 g, KCl 0.4 g, yeast extract 2 g, Tryptone 2 g, Casamino acids 2 g, L-cysteine 2.4 g, L-arginine 4.2 g, L-histidine 4.2 g, 1 ml Trace metal solution from JCM Medium 294, 1 mg resazurin, and 975 ml distilled water.
- After autoclaving under N2-CO2, JCM adds 25 ml 8% NaHCO3 solution and 1 ml filter-sterilized Trace vitamins from JCM Medium 197; after anaerobic distribution, it adds 8 ml 5% Na2S x 9H2O solution per liter.
- JCM has pH 7.5 and a final readjust-pH-if-necessary step.

## Completeness

- The preparation text and pH are present, unlike the separate TOGO owner.
- The 975 ml distilled water row is absent.
- The Trace metal and Trace vitamins additions are not represented as stock additions or solution references; their internal JCM 294 and JCM 197 stock compositions are mixed into the final medium at stock strength.
- The 25 ml 8% NaHCO3 and 8 ml 5% Na2S x 9H2O additions were converted to `25 G_PER_L` and `8 G_PER_L` final ingredients instead of preserving the source solution strengths and volumes.
- Empty `target_organisms` and `references` are not inherently defects for this import; the JCM page supports the medium formulation but does not make a strain-specific growth claim.

## Findings

- Major: this active JCM `1175` recipe duplicates TOGO M1259 / JCM `1175` as a separate active CultureMech identity instead of being merged or marked as a source cross-listing.
- Major: 1 ml/L Trace metal solution from JCM 294 and 1 ml/L Trace vitamins from JCM 197 were flattened into final-medium rows at stock concentrations; every HCl, metal, and vitamin amount in those blocks is therefore about 1000-fold high.
- Major: 25 ml 8% NaHCO3 and 8 ml 5% Na2S x 9H2O stock additions were misrepresented as 25 g/L NaHCO3 and 8 g/L Na2S x 9H2O.
- Major: the 975 ml distilled water row is missing.
- Major: `NiCl2 x 6 H2O` is grounded to the wrong hydrate form.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/caenicola_mobile_medium.yaml` together with `data/normalized_yaml/bacterial/TOGO_M1259_Caenicola_Mobile_Medium.yaml`, not either generated merge.
- Collapse JCM `1175` and TOGO `M1259` to one active recipe ID or model one as a true source cross-listing.
- Restore distilled water as 975 ml, keep JCM 294 and JCM 197 as 1 ml/L stock additions, and keep the bicarbonate and sulfide additions as 25 ml of 8% NaHCO3 and 8 ml of 5% Na2S x 9H2O.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific nickel chloride hexahydrate term if a verified MediaIngredientMech/CHEBI mapping exists; otherwise leave it ungrounded.
- Regenerate the merged record and verify that the duplicate `CAENICOLA_MOBILE_MEDIUM` and `caenicola_mobile_medium__7247592a` generated records no longer coexist as independent recipes for JCM 1175.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the reconciled normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating merged YAML.
- Compare the regenerated formulation against live JCM `1175`, JCM `294`, JCM `197`, TOGO `M1259`, TOGO `M288`, and TOGO `M190`, checking that no stock composition is flattened at full strength.
- Run a gitignore-independent search for JCM `1175`, TOGO `M1259`, and the Caenicola label to confirm no active duplicate remains.

## Additional Notes

- `find . -iname '*caenicola*'` included ignored and hidden files and found this generated merge, the TOGO generated duplicate, the TOGO normalized duplicate, this normalized owner, and an unrelated Thermoclostridium caenicola medium.
- A gitignore-independent search for `CultureMech:002346`, `JCM Medium J1175`, `CAENICOLA MOBILE MEDIUM`, `CultureMech:007790`, and the duplicate generated filename found the active JCM and TOGO normalized owners, both generated merges, registry/catalog rows for both IDs, the current content review manifest, and archived validation rows.
