# YAML Record Review: Methanopyrus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanopyrus_medium__c796d637.yaml
- Started UTC: 2026-09-24T04:27:24Z
- Finished UTC: 2026-09-24T04:29:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009218 |
| Name | methanopyrus_medium |
| Original name | Methanopyrus Medium |
| Category | archaea |
| Media term | TOGO:M2663 |
| Source | TOGO M2663 / DSMZ Medium 511 |
| Generated path reviewed | data/merge_yaml/merged/methanopyrus_medium__c796d637.yaml |
| Canonical owner | data/normalized_yaml/archaea/TOGO_M2663_Methanopyrus_Medium.yaml |

The reviewed file is a generated merge of one TOGO owner that cites DSMZ Medium
511. Its source identity is plausible, but the TOGO payload has drifted from
the current DSMZ 511 PDF and the imported YAML lost every solution boundary.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanopyrus_medium__c796d637.yaml` printed `No issues found`. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanopyrus_medium__c796d637.yaml --out /private/tmp/methanopyrus_medium__c796d637.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanopyrus_medium__c796d637.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanopyrus_medium__c796d637.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **The TOGO medium identity is coherent.** TOGO M2663 is named
  `Methanopyrus Medium` and cites the DSMZ Medium 511 PDF.
- **The cited current DSMZ PDF is not identical to the TOGO payload.** The
  current PDF and direct MediaDive 511 record use 980 ml main water and 1 ml
  Wolin's vitamin solution (10x); TOGO M2663 stores 970 ml water and 10 ml of a
  different local `Vitamins solution`.
- **Two local stock links point to unrelated generic MediaDive stocks.**
  `mediadive.solution:6187` is an EDTA-based generic trace element solution,
  not TOGO M2663's Modified Wolin-like trace stock; `mediadive.solution:5788`
  is not the lower-concentration TOGO vitamin stock.
- **Several links are stale or broad.** The MgSO4 x 7H2O primary term was
  repaired to heptahydrate, but `mediaingredientmech_chebi_term` still points
  to generic magnesium sulfate; KNO3 still has a legacy
  `mediaingredientmech_term`; NiCl2 x 6H2O and K2HPO4 x 3H2O have broad
  CHEBI terms.

## Evidence

### Supported by inspected sources

- TOGO M2663 supports the main recipe captured here: 970 ml water; 0.5 ml
  0.1 percent Na-resazurin; 2 ml each of 0.1 percent Fe, Ni, and tungstate
  solutions; MgSO4 x 7H2O, NaCl, CaCl2 x 2H2O, KH2PO4, NH4Cl, MgCl2 x 6H2O,
  Na2S x 9H2O, KCl, NaHCO3, Na2SO4, K2HPO4 x 3H2O; 10 ml Trace element
  solution; 10 ml Marine trace elements; and 10 ml Vitamins solution.
- TOGO M2663 supports a local Marine trace elements solution with 1000 ml
  water, H3BO3, KNO3, NaBr, SrCl2 x 6H2O, KI, NaF, Na-silicate, and Na2HPO4 x
  3H2O.
- TOGO M2663 supports a local Trace element solution with 1000 ml water, MgSO4
  x 7H2O, NaCl, CaCl2 x 2H2O, Na2MoO4 x 2H2O, H3BO3, FeSO4 x 7H2O, NiCl2 x
  6H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, Na2SeO3 x 5H2O, CoSO4 x 7H2O,
  KAl(SO4)2 x 12H2O, NTA, Na2WO4 x 2H2O, MnSO4 x H2O, and KOH pH adjustment.
- TOGO M2663 supports a local vitamin stock with biotin, p-Aminobenzoic acid,
  Thiamine-HCl, Pyridoxine-HCl, folic acid, Vitamin B12, riboflavin, nicotinic
  acid, lipoic acid, D-Ca-pantothenate, and N2.
- TOGO M2663 preserves DSMZ-style preparation comments for H2/CO2 anoxic
  sparging, sterile anoxic vitamin, sulfide, and bicarbonate stocks,
  post-inoculation 2 bar H2/CO2 pressurization, and trace-stock pH adjustment.

### Unsupported or over-scoped in the YAML

- All four water rows are summed to `3970.0 G_PER_L`.
- Trace element, Marine trace element, and Vitamin stock components are
  flattened into the top-level ingredient list.
- 0.5 ml Na-resazurin and the 2 ml Fe, Ni, and tungstate stock additions are
  empty solutions with volumes represented as `G_PER_L`.
- Milligram stock rows such as KNO3, KI, NaF, Na-silicate, Na2HPO4 x 3H2O,
  Na2SeO3 x 5H2O, Na2WO4 x 2H2O, and all vitamins are represented as
  `G_PER_L`.
- The TOGO preparation comments are absent from `preparation_steps`.

## Completeness

- **Cited-source versioning is unresolved.** The record either needs to be
  preserved as a TOGO M2663 snapshot with a retrieved-date note or updated to
  the current DSMZ 511 PDF formulation.
- **Eight migrated solutions are empty.** Three 0.1 percent stocks, the
  resazurin stock, three local nested stocks, and KOH are placeholders rather
  than scoped solution records.
- **Stock components are mixed into the final medium.** The row list cannot
  distinguish main-solution salts from stock-strength trace elements and
  vitamins.
- **Preparation is missing.** The record loses the H2/CO2, N2, filtration,
  post-autoclave stock, overpressure, pH, and KOH stock-assembly instructions.
- Empty target-organism and growth-evidence sections are not defects for this
  provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The TOGO snapshot and its cited current DSMZ 511 PDF disagree. | DSMZ 511 lists 980 ml water and 1 ml Wolin's vitamin solution (10x); TOGO M2663 lists 970 ml water and 10 ml of a different Vitamins solution. | `data/normalized_yaml/archaea/TOGO_M2663_Methanopyrus_Medium.yaml` |
| Major | Nested solutions were migrated to empty placeholders and flattened ingredients. | The generated YAML has eight `Unknown solution` entries and copies Marine trace, Trace element, Vitamin, resazurin, Fe, Ni, and tungstate stock rows into the top-level ingredient list. | `data/normalized_yaml/archaea/TOGO_M2663_Methanopyrus_Medium.yaml` and solution migration |
| Major | Stock-addition volumes and milligram rows use the wrong dimension. | 0.5 ml resazurin, 2 ml Fe/Ni/tungstate stocks, 10 ml local stocks, and multiple mg rows are stored as `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M2663_Methanopyrus_Medium.yaml` and import unit handling |
| Major | Generic MediaDive links point at the wrong stock recipes. | MediaDive 6187 and 5788 have different component lists from the TOGO M2663 Trace element and Vitamins solutions. | `data/normalized_yaml/archaea/TOGO_M2663_Methanopyrus_Medium.yaml` |
| Major | TOGO preparation comments are absent. | TOGO M2663 preserves H2/CO2 sparging, sterile anoxic stock addition, overpressure, and KOH trace-stock assembly; the YAML has no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M2663_Methanopyrus_Medium.yaml` |
| Minor | Several term links are stale or broad. | MgSO4 x 7H2O has a stale generic MediaIngredientMech CHEBI link; KNO3 has a legacy MediaIngredientMech link; NiCl2 x 6H2O and K2HPO4 x 3H2O need exact hydrate terms. | Shared ingredient grounding maps |

## Recommended Edits

1. Decide whether TOGO M2663 remains an archived TOGO snapshot or is updated to
   current DSMZ 511, then document that source decision in the owner.
2. Remove the false `mediadive.solution:6187` and `mediadive.solution:5788`
   links from TOGO-local stocks.
3. Restore the four 0.1 percent stock additions and the three nested local
   stock recipes with their ml addition amounts.
4. Stop flattening stock-strength Marine trace, Trace element, and Vitamin
   rows into top-level ingredients.
5. Restore milligram and milliliter source units throughout.
6. Add the TOGO preparation comments as structured preparation steps.
7. Repair stale MediaIngredientMech links and broad hydrate groundings.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on
  `data/normalized_yaml/archaea/TOGO_M2663_Methanopyrus_Medium.yaml` and the
  regenerated merged record.
- Manually compare the regenerated YAML against TOGO M2663 and whichever DSMZ
  511 source version is selected.
- Confirm no empty `Unknown solution` placeholders remain and no stock-strength
  trace or vitamin rows leak into the main ingredient list.

## Additional Notes

- `data/merge_yaml/merged/methanopyrus_medium__b882b2e7.yaml` is the direct
  MediaDive DSMZ 511 import. It has the current DSMZ 511 identity and source
  structure but still flattens nested MediaDive stocks.
