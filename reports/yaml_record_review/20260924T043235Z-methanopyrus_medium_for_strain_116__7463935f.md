# YAML Record Review: Methanopyrus Medium For Strain 116

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanopyrus_medium_for_strain_116__7463935f.yaml`
- Started UTC: 2026-09-24T04:29:30Z
- Finished UTC: 2026-09-24T04:32:35Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:003018`, the generated `methanopyrus_medium_for_strain_116`
merge for MediaDive medium `J673` / JCM medium 673,
`METHANOPYRUS MEDIUM FOR STRAIN 116`.

The inspected normalized owner was
`data/normalized_yaml/archaea/methanopyrus_medium_for_strain_116.yaml`; the
generated file is a one-source merge from that owner on fingerprint
`7463935fa35c830166a16c3a1b9822e2e5b201c6f962e0fa52fad138738ab6c6`.

## Validation

- LinkML open validation: passed with `No issues found`.
- Strict schema validation: passed with 0 error rows; the TSV contained the
  header only.
- Reference validation: passed; 1 file validated, 0 total checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked. The available history validator
  targets standalone files under `history/`, not `MediaRecipe.curation_history`
  blocks embedded in generated YAML.

## Identity and Grounding

The record identity is correctly grounded as the direct MediaDive/JCM import:
the YAML cites JCM medium 673, and both the live JCM page and the MediaDive REST
payload identify `J673` as `METHANOPYRUS MEDIUM FOR STRAIN 116`.

Ingredient-level grounding is mixed. The main salts, gases, reducer, and iron
powder are identifiable, but `NiCl2 x 6 H2O` is linked to anhydrous nickel
dichloride, `Na2HPO4 x 12 H2O` is linked to broad disodium hydrogenphosphate,
and `KI` and `KNO3` still carry legacy `mediaingredientmech_term` links rather
than the CHEBI-keyed field used by the current enrichment.

## Evidence

### Supported by inspected sources

- JCM 673 and MediaDive `J673` support the main solution rows for NaCl,
  K2HPO4, KH2PO4, CaCl2 x 2 H2O, NH4Cl, MgSO4 x 7 H2O, MgCl2 x 6 H2O, KCl,
  NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Fe2(SO4)3 x n H2O, FeSO4 x 7 H2O,
  Na2WO4 x 2 H2O, resazurin, iron powder, NaHCO3, Na2S x 9 H2O, and 970 ml
  distilled water.
- JCM 673 supports adding 30 ml marine trace elements from JCM 216, 10 ml trace
  vitamins from JCM 197, and 10 ml trace mineral solution from JCM 368.
- MediaDive carries those three referenced stocks as solution IDs 3884, 3861,
  and 4090 and preserves the same stock recipes shown by the JCM pages.
- The YAML preserves the JCM/MediaDive main preparation paragraph for
  filter-sterilizing the medium except iron powder, dispensing under H2/CO2,
  reducing with 5 percent Na2S x 9 H2O, and pressurizing the inoculated bottle
  to 200 kPa H2/CO2.
- The YAML also preserves the MediaDive/JCM 368 trace-mineral pH instruction to
  dissolve nitrilotriacetic acid, adjust to pH 6.5 with KOH, add minerals, and
  adjust the final pH to 7.0.

### Unsupported or over-scoped in the YAML

- No source supports deleting all water rows. The JCM page lists 970 ml
  distilled water in the main solution, and each of the three MediaDive stocks
  has a 1000 ml water basis.
- The YAML has no explicit rows for the 30 ml `Marine trace elements solution`,
  10 ml `Trace vitamins`, or 10 ml `Trace mineral solution` additions.
- Every chemical inside the three nested stock solutions is flattened to the
  top-level ingredient list at stock concentration. For example, the final
  J673 medium receives 30 ml of a 4 g/L NaBr marine stock plus 10 ml of a
  0.01 g/L NaBr trace-mineral stock, but the YAML reports `NaBr` as
  `4.01 G_PER_L`.
- The duplicate cleanup merged independent stock-scope rows for NaBr,
  SrCl2 x 6 H2O, H3BO3, and KI even though MediaDive solution 3884 and
  solution 4090 define them in different stocks.

## Completeness

The record is not complete enough for a faithful recipe. It has the direct main
J673 components and two preparation paragraphs, but it drops the main and stock
water rows, drops the stock-addition rows that explain how the recipe is
assembled, and collapses the three referenced solutions into final-medium
ingredients without dilution.

Empty optional fields were not treated as defects.

## Findings

- `needs curation`: `Distilled water` is missing for the 970 ml main solution
  and all three 1000 ml referenced stock solutions.
- `needs curation`: the three JCM/MediaDive stock additions are not represented
  as additions; 30 ml marine trace elements, 10 ml trace vitamins, and 10 ml
  trace mineral solution must remain distinguishable from their internal stock
  formulas.
- `needs curation`: stock-scope compounds are expressed at stock strength in
  `G_PER_L`, so vitamins and trace minerals are orders of magnitude too high if
  read as final-medium concentrations.
- `needs curation`: the March duplicate merge summed NaBr, SrCl2 x 6 H2O,
  H3BO3, and KI across marine-trace and trace-mineral contexts that should stay
  separate.
- `needs curation`: hydrate-sensitive or migrated grounding is stale for
  `NiCl2 x 6 H2O`, `Na2HPO4 x 12 H2O`, `KI`, and `KNO3`.

## Recommended Edits

- Repair the MediaDive import/normalization path so `solution` rows are retained
  as local additions instead of flattening only their chemical children.
- Preserve water rows within each solution scope: 970 ml in main solution 4564,
  1000 ml in marine trace solution 3884, 1000 ml in trace vitamins solution
  3861, and 1000 ml in trace mineral solution 4090.
- Remove the cross-scope duplicate sums for NaBr, SrCl2 x 6 H2O, H3BO3, and KI;
  keep the 3884 and 4090 source rows under their own stock solutions.
- Keep JCM 216, JCM 197, and JCM 368 provenance on the referenced stock recipes
  or equivalent MediaDive solution IDs so future reviews can tell which stock
  formula supplied each trace row.
- Refresh hydrate and legacy ingredient groundings after the structural repair.

## Follow-up Checks

- Re-run the focused LinkML, strict, reference, and term validators on the
  normalized owner and regenerated merge.
- Diff regenerated `methanopyrus_medium_for_strain_116__7463935f.yaml` against
  MediaDive `J673` and JCM 673, then spot-check JCM 216, 197, and 368 for the
  three nested stock formulas.
- Confirm that no duplicate-merge note remains on NaBr, SrCl2 x 6 H2O, H3BO3,
  or KI unless it is within one solution scope.

## Additional Notes

The source pages and the generated record all describe a defined liquid medium;
the `medium_type: DEFINED`, `composition_type: DEFINED`, and
`physical_state: LIQUID` values are appropriate.
