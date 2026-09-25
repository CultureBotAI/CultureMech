# YAML Record Review: caenicola_mobile_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/CAENICOLA_MOBILE_MEDIUM.yaml
- Started UTC: 2026-09-22T01:47:35Z
- Finished UTC: 2026-09-22T01:47:42Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:007790`, `caenicola_mobile_medium`, `Caenicola Mobile Medium`, class `MediaRecipe`.
- Merge lineage: one source recipe, `TOGO_M1259_Caenicola_Mobile_Medium`, on fingerprint `58af89aec3f23ed8681a13cbd79086641385ece1c9ec94538d8afc76131d50a2`.
- Authoritative owner: `data/normalized_yaml/bacterial/TOGO_M1259_Caenicola_Mobile_Medium.yaml`.
- Claimed source identity: TOGO Medium `M1259`, imported from JCM `JCM_M1175`.

## Validation

- Open LinkML schema validation passed for the generated merge.
- Strict CultureMech validation passed for the generated merge.
- LinkML reference validation passed for the generated merge with 0 reference checks.
- LinkML term validation passed for the generated merge.
- Embedded `curation_history` was not separately validated because `just validate-history` checks standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in a merged record.

## Identity and Grounding

- The TOGO identity is internally consistent: live TOGO `M1259` is `Caenicola Mobile Medium`, reports original medium `JCM_M1175`, and links the JCM `1175` page.
- JCM `1175` is currently reachable and names the same `CAENICOLA MOBILE MEDIUM`.
- The same source identity is duplicated locally as `CultureMech:002346` in `data/normalized_yaml/bacterial/caenicola_mobile_medium.yaml` and the generated `data/merge_yaml/merged/caenicola_mobile_medium__7247592a.yaml`. That sibling carries `JCM Medium J1175`, the same pH 7.5, the same preparation prose, and the JCM stock solutions flattened into direct ingredient rows.
- Water, sodium chloride, calcium chloride dihydrate, potassium phosphates, ammonium chloride, magnesium chloride hexahydrate, potassium chloride, L-cysteine, L-arginine, L-histidine, KOH, carbon dioxide, and dinitrogen are grounded to source-compatible chemical forms.
- Yeast extract, Tryptone (BD-Difco), and Casamino acids (BD-Difco) are intentionally ungrounded undefined biological mixtures.

## Evidence

- TOGO `M1259` specifies 975 ml distilled water, 2 g yeast extract, 0.4 g NaCl, 0.05 g CaCl2 x 2H2O, 0.5 g KH2PO4, 0.5 g NH4Cl, 0.5 g K2HPO4, 1 mg resazurin, 0.3 g MgCl2 x 6H2O, 0.4 g KCl, 2.4 g L-cysteine, 4.2 g L-arginine, 4.2 g L-histidine, 2 g Tryptone (BD-Difco), and 2 g Casamino acids (BD-Difco) in its first solution.
- The same source adds 1 ml Trace metal solution from TOGO `M288`, 25 ml 8% NaHCO3, 1 ml Trace vitamins from TOGO `M190`, and 8 ml 5% Na2S x 9H2O solution.
- The live JCM `1175` page agrees on pH 7.5, the 1 mg resazurin row, the 975 ml water row, the 25/1/8 ml stock additions, adjustment with KOH, autoclaving under N2-CO2 4:1, filter-sterilized bicarbonate and vitamin additions, anaerobic distribution into sealed vessels, addition of the autoclaved 5% sulfide solution, and final readjustment to pH 7.5 if needed.

## Completeness

- The top-level gram rows and undefined extract rows match the TOGO/JCM source amounts.
- `ph_value` is absent even though TOGO and JCM both specify pH 7.5.
- The source preparation paragraphs are absent; KOH, N2, and CO2 were left behind as variable-concentration ingredients instead of being modeled as pH adjustment and anaerobic atmosphere instructions.
- The four source solution additions were migrated to empty `Unknown solution` stubs and cannot reconstruct the stock recipes or the added volumes.
- Empty `target_organisms` and `references` are not inherently defects for this import; the source recipe supports the medium formulation but does not make a strain-specific growth claim.

## Findings

- Major: the TOGO and JCM imports for the same JCM `1175` medium are split into two active CultureMech identities, `CultureMech:007790` and `CultureMech:002346`, instead of one curated owner with reconciled TOGO/JCM provenance.
- Major: `Resazurin` was imported as `1 G_PER_L`, not the 1 mg/L row in TOGO and JCM.
- Major: `Trace metal solution`, `8% NaHCO3 solution`, `Trace vitamins`, and `5% Na2S x 9H2O solution` were imported as empty `Unknown solution` records with `1`, `25`, `1`, and `8 G_PER_L` concentrations instead of milliliter additions.
- Major: the pH 7.5 target and source preparation workflow are missing from the TOGO owner.
- Minor: KOH, carbon dioxide gas, and nitrogen gas are modeled as variable final ingredients even though the source uses KOH only for pH adjustment and N2-CO2 only as the anaerobic gas phase.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/TOGO_M1259_Caenicola_Mobile_Medium.yaml` and `data/normalized_yaml/bacterial/caenicola_mobile_medium.yaml`, not either generated merge.
- Collapse the TOGO M1259 and JCM J1175 inputs to one active recipe ID or otherwise mark one as a true source cross-listing instead of an independent medium.
- Correct resazurin to the source 1 mg/L amount.
- Resolve the 1 ml Trace metal solution against TOGO `M288` / JCM `294` and the 1 ml Trace vitamins solution against TOGO `M190` / JCM `197`; model the 25 ml 8% NaHCO3 and 8 ml 5% Na2S x 9H2O additions as solution additions with milliliter units.
- Add pH 7.5, autoclaving under N2-CO2 4:1, filter sterilization of bicarbonate and vitamins, anaerobic dispensing into sealed culture vessels, and final pH readjustment from TOGO/JCM.
- Move KOH and the N2-CO2 gas mixture out of final ingredients and into preparation or atmosphere fields.

## Follow-up Checks

- Re-run open schema, strict validation, reference validation, and term validation against the reconciled normalized owner.
- Re-run `just verify-merges` and `just audit-merge-freshness` after regenerating the merged YAML.
- Compare the regenerated merge against live TOGO `M1259` and JCM `1175`, specifically checking resazurin's milligram unit and the four milliliter stock additions.
- Search for remaining generated duplicates of JCM `1175`, TOGO `M1259`, and the `Caenicola Mobile Medium` label after the merge repair.

## Additional Notes

- `find . -iname '*caenicola*'` included ignored and hidden files and found the reviewed generated merge, the duplicate hashed generated merge, the TOGO normalized owner, the JCM normalized duplicate, and an unrelated Thermoclostridium caenicola medium.
- A gitignore-independent search for `CultureMech:007790`, `TOGO_M1259_Caenicola_Mobile_Medium`, `M1259`, `JCM_M1175`, the JCM `1175` URL, and fingerprint `58af89aec3f23ed8681a13cbd79086641385ece1c9ec94538d8afc76131d50a2` found the active TOGO owner, generated merge, registry/index rows, current review manifest, and archived validation rows.
