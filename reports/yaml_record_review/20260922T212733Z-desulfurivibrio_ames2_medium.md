# YAML Record Review: desulfurivibrio_ames2_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfurivibrio_ames2_medium.yaml`
- Started UTC: 2026-09-22T21:25:32Z
- Finished UTC: 2026-09-22T21:27:33Z
- Verdict: needs curation

## Target

`CultureMech:015831` represents direct JCM GRMD 1333, `DESULFURIVIBRIO AMeS2 MEDIUM`. The generated record is a single-source merge from `data/normalized_yaml/bacterial/JCM_J1333_DESULFURIVIBRIO_AMeS2_MEDIUM.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

The identity and final-medium base ingredients match JCM 1333. The source page lists 22.0 g Na2CO3, 8.0 g NaHCO3, 6.0 g NaCl, 1.0 g K2HPO4, and 5.0 g sulfur per liter, followed by 1 ml 1 M MgCl2, 4 ml 1 M NH4Cl, 1 ml Trace element solution from JCM 1079, 1 ml Se/W solution from JCM 852, 1 ml Trace vitamins from JCM 197, and a conditional 5 ml 5% Na2S x 9H2O addition.

JCM 1333 does not currently exist in the MediaDive REST API, so the direct JCM page is the authoritative external recipe for this record.

## Evidence

- JCM GRMD 1333 lists the carbonate, bicarbonate, chloride, phosphate, and sulfur base table and instructs the curator to add all components except sulfur to distilled water and bring the base volume to 1.0 L.
- The JCM post-cooling table lists the MgCl2, NH4Cl, Trace element, Se/W, and Trace vitamins stocks at 1, 4, 1, 1, and 1 ml per liter, respectively.
- JCM marks Se/W and Trace vitamins as filter-sterilized and says sulfur should be steamed for 3 hr on each of 3 successive days.
- JCM lists 5 ml of 5% Na2S x 9H2O per liter as an addition only when the inoculum lacks sulfide or polysulfide.
- The normalized YAML was repaired after merge generation by `repair_jcm_1333_desulfurivibrio_score15.py`, which moved all six stock additions into `solutions` and added nested compositions for 1 M MgCl2, 1 M NH4Cl, and 5% Na2S x 9H2O.
- A gitignore-independent, case-insensitive `find` over `data/` found only this generated record and its `JCM_J1333_DESULFURIVIBRIO_AMeS2_MEDIUM.yaml` normalized source for Desulfurivibrio / AMeS2.

## Completeness

The current generated record is stale relative to the repaired normalized source. It still stores all six stock additions in `ingredients`; the generated YAML has no nested composition for the simple molar MgCl2/NH4Cl stocks or the 5% Na2S x 9H2O stock, and it has no dedicated `solutions` block for the three referenced external stocks.

## Findings

- The generated record predates the September JCM 1333 repair and has not incorporated the normalized stock-solution model.
- `1 M MgCl2 solution`, `1 M NH4Cl solution`, Trace element solution, Se/W solution, Trace vitamins, and 5% Na2S x 9H2O solution are still top-level ingredient entries in the generated record.
- The generated `5% Na2S x 9H2O solution` row does not preserve the source condition that it is added only if the inoculum lacks sulfide or polysulfide.
- The generated preparation step that introduces the stock-addition table also contains the sulfur-steaming sentence, so the timing of sterilized sulfur handling is less clear than in the repaired normalized source.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/desulfurivibrio_ames2_medium.yaml` from the current repaired normalized JCM 1333 source.
- Verify the regenerated record keeps MgCl2, NH4Cl, Trace element, Se/W, Trace vitamins, and Na2S as `solutions`, not plain ingredients.
- Preserve the conditional nature of the 5% Na2S x 9H2O addition in the generated solution notes or preparation text.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after regeneration.
- Compare the regenerated stock rows against JCM 1333 and confirm the addition rates are 1, 4, 1, 1, 1, and 5 ml/l.
- Recheck that no additional Desulfurivibrio / AMeS2 duplicate emerges after regeneration.

## Additional Notes

None found.
