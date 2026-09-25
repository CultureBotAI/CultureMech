# YAML Record Review: Methanosaeta Thermophila Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanosaeta_thermophila_medium__8ffe3304.yaml`
- Started UTC: 2026-09-24T04:37:28Z
- Finished UTC: 2026-09-24T04:39:46Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:000296`, the generated `methanosaeta_thermophila_medium`
merge for MediaDive medium `J285` / JCM medium 285,
`METHANOSAETA THERMOPHILA MEDIUM`.

The generated file is a one-source merge from
`data/normalized_yaml/archaea/methanosaeta_thermophila_medium.yaml` on
fingerprint `8ffe330479200ad0820eca7237d72bfc338b2749784e93ba50e8ba694297b4f5`.

## Validation

- LinkML open validation: passed; the validator exited 0 with no diagnostics.
- Strict schema validation: passed with 0 error rows; the TSV contained the
  header only.
- Reference validation: passed; 1 file validated, 0 total checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked. The available history validator
  targets standalone files under `history/`, not `MediaRecipe.curation_history`
  blocks embedded in generated YAML.

## Identity and Grounding

The top-level identity is correct for the direct JCM import. The generated
record cites JCM medium 285, and the live JCM page plus MediaDive `J285` both
identify that source as `METHANOSAETA THERMOPHILA MEDIUM` at final pH 6.5.

The term grounding is adequate for many base and stock compounds, but several
solution additives have lost important source qualifiers: `NaHCO3`,
`Sodium acetate`, `Coenzyme M`, and `Na2S x 9 H2O` originate as 5 percent,
33 percent, 1.42 percent, and 5 percent sterile stock solutions. Their rows are
grounded as pure chemicals and no longer show those stock concentrations in a
structured way.

## Evidence

### Supported by inspected sources

- JCM 285 and MediaDive `J285` support a main solution with 0.5 g NH4Cl,
  0.4 g K2HPO4, 0.1 g MgCl2 x 6 H2O, 1 mg resazurin, 10 ml trace minerals,
  and 1000 ml distilled water.
- JCM 285 supports six anaerobic sterile stock additions per liter after
  autoclaving: 20 ml of 5 percent NaHCO3, 10 ml of 1 percent CaCl2 x 2 H2O,
  10 ml of 33 percent sodium acetate, 10 ml trace vitamins, 10 ml of
  1.42 percent coenzyme M, and 5 ml of 5 percent Na2S x 9 H2O.
- MediaDive solution 3804 and the trace-minerals block on JCM 151 support the
  trace-minerals recipe with 1000 ml water, nitrilotriacetic acid,
  MgSO4 x 7 H2O, MnSO4 x n H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O,
  CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, and
  Na2MoO4 x 2 H2O.
- MediaDive solution 3861 and the trace-vitamin block on JCM 197 support a
  1000 ml vitamin stock with biotin, folic acid, pyridoxine hydrochloride,
  thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, Vitamin B12,
  p-Aminobenzoic acid, and lipoic acid.
- The generated YAML preserves the main anaerobic preparation paragraph, the
  final filter-sterilized CO2 instruction, and the trace-minerals pH
  preparation paragraph.

### Unsupported or over-scoped in the YAML

- The 10 ml `Trace minerals` and 10 ml `Trace vitamins` additions are missing
  as named stock-addition rows; only their internal compounds remain.
- All three water rows are missing: 1000 ml from the main solution, 1000 ml
  from the trace-minerals stock, and 1000 ml from the trace-vitamins stock.
- The six anaerobic sterile additions after autoclaving are stored as if their
  milliliter volumes were gram-per-liter amounts. For example, `20 ml` of
  `5% NaHCO3 solution` becomes `NaHCO3` at `20 G_PER_L`.
- `CaCl2 x 2 H2O` incorrectly merges the 10 ml 1 percent CaCl2 stock addition
  with the 0.1 g/L calcium chloride row inside trace minerals.
- Trace-mineral and trace-vitamin components are flattened to top-level rows at
  stock strength, not final-medium strength.
- The first preparation step is categorized as `POUR_PLATES`, but the JCM and
  MediaDive text describes boiling, cooling, anoxic gassing, dispensing, and
  autoclaving a liquid medium.

## Completeness

The record has the direct base ingredients and all source preparation text, but
it is incomplete for stock-aware cultivation. It lacks main and stock water,
explicit trace-mineral and trace-vitamin additions, the percent-stock
concentrations for the six anaerobic additions, and a separation between
post-autoclave additions and stock internals.

Empty optional fields were not treated as defects.

## Findings

- `needs curation`: water was dropped from the main solution, trace-minerals
  stock, and trace-vitamins stock.
- `needs curation`: 10 ml trace-mineral and 10 ml trace-vitamin additions were
  flattened away.
- `needs curation`: milliliter additions of 5 percent NaHCO3, 1 percent
  CaCl2 x 2 H2O, 33 percent sodium acetate, 1.42 percent Coenzyme M, and
  5 percent Na2S x 9 H2O are represented as pure-compound `G_PER_L` values.
- `needs curation`: `CaCl2 x 2 H2O` contains a cross-scope duplicate merge.
- `needs curation`: trace-mineral and trace-vitamin child ingredients are
  top-level stock-strength rows.
- `pass with minor issues`: preparation text is present, but the first action
  enum is wrong for the described liquid-medium workflow.

## Recommended Edits

- Preserve solution rows from MediaDive/JCM imports, including the two named
  stocks and the four percent-stock additions.
- Keep the internal `Trace minerals` and `Trace vitamins` recipes in separate
  local scopes with their own 1000 ml water rows.
- Remove the cross-scope duplicate merge for `CaCl2 x 2 H2O`.
- Retain the source stock attributes for 5 percent NaHCO3, 1 percent
  CaCl2 x 2 H2O, 33 percent sodium acetate, 1.42 percent Coenzyme M, and
  5 percent Na2S x 9 H2O.
- Reclassify the first preparation step to an action that matches boiling,
  anoxic cooling, dispensing, and autoclaving rather than `POUR_PLATES`.

## Follow-up Checks

- Re-run the focused LinkML, strict, reference, and term validators after
  regenerating the normalized owner and merged record.
- Diff the regenerated record against MediaDive `J285` and the live JCM 285,
  then spot-check JCM 151 and JCM 197 for the two referenced stocks.
- Confirm that `CaCl2 x 2 H2O` no longer has a duplicate-merge note and that the
  two stock-water rows are not merged into the main-medium water row.

## Additional Notes

TOGO also has `M279` and `M1974` records with the same normalized name; those
generated records should be reviewed separately because their immediate source
shape differs from this direct JCM import.
