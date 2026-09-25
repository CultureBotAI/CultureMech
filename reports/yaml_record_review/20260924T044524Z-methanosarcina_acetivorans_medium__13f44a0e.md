# YAML Record Review: Methanosarcina Acetivorans Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanosarcina_acetivorans_medium__13f44a0e.yaml`
- Started UTC: 2026-09-24T04:43:18Z
- Finished UTC: 2026-09-24T04:45:24Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:002742`, the generated `methanosarcina_acetivorans_medium`
merge for MediaDive medium `J385` / JCM medium 385,
`METHANOSARCINA ACETIVORANS MEDIUM`.

The generated file is a one-source merge from
`data/normalized_yaml/archaea/methanosarcina_acetivorans_medium.yaml` on
fingerprint `13f44a0eb1866e634d7a56ae6398bc4a3bd97f36caac7aadf09c3a207a0e2e70`.

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

The top-level identity is correct for the direct JCM import: MediaDive `J385`
and the live JCM medium 385 page both identify the source as
`METHANOSARCINA ACETIVORANS MEDIUM` with final pH 7.0.

Ingredient grounding is mostly exact for named salts. The record loses
structured grounding for several solution additions, however: 8 percent
NaHCO3, 5 percent L-Cysteine HCl x H2O, 5 percent Na2S x 9 H2O, and 6.5 ml
methanol are represented as if they were final gram-per-liter rows.

## Evidence

### Supported by inspected sources

- JCM 385 and MediaDive `J385` support the main medium rows for NaCl,
  MgSO4 x 7 H2O, NH4Cl, KCl, CaCl2 x 2 H2O, Na2HPO4, yeast extract, 10 ml
  Trace minerals, 6.5 ml methanol, 1 mg resazurin, and 1 L distilled water.
- JCM 385 supports adding, per liter after autoclaving, 30 ml 8 percent
  NaHCO3 solution, 6 ml 5 percent L-Cysteine HCl x H2O solution, and 6 ml
  5 percent Na2S x 9 H2O solution.
- MediaDive solution 3804 and the JCM 151 trace-minerals recipe support a
  1000 ml stock containing nitrilotriacetic acid, MgSO4 x 7 H2O,
  MnSO4 x n H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O,
  ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, Na2MoO4 x 2 H2O, and
  distilled water.
- The generated record preserves the JCM/MediaDive preparation paragraph for
  boiling, N2/CO2 cooling, methanol addition, pH adjustment, dispensing under
  N2/CO2, autoclaving, and adding sterile anaerobic stock solutions.
- The trace-minerals pH adjustment step is also preserved.

### Unsupported or over-scoped in the YAML

- The 10 ml `Trace minerals` addition is missing as an addition row; its
  internal stock ingredients are flattened into the top-level list.
- Both water rows are absent: the 1 L main-medium water row and the 1 L
  trace-minerals stock water row.
- `NaCl`, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` have duplicate-merge sums across
  the main solution and trace-mineral stock. For example, JCM 385 has 9.45 g
  MgSO4 x 7 H2O in the main solution and 3 g/L MgSO4 x 7 H2O inside a stock
  added at 10 ml/L; the YAML reports `11.93195 G_PER_L`.
- Post-autoclave stock additions are represented as unsupported
  gram-per-liter amounts: `30 G_PER_L` NaHCO3, `6 G_PER_L`
  L-Cysteine HCl x H2O, and `6 G_PER_L` Na2S x 9 H2O.
- The 6.5 ml methanol addition is represented as `6.5 G_PER_L` without a source
  mass or density conversion.

## Completeness

The record has the correct JCM identity and preparation narrative, but it lacks
the stock-addition rows and water rows needed to reconstruct the recipe. Because
several stock additions have been flattened and merged across scopes, the
top-level ingredient concentrations are not reliable final-medium
concentrations.

Empty optional fields were not treated as defects.

## Findings

- `needs curation`: the 10 ml Trace minerals addition is flattened away.
- `needs curation`: main and stock water rows are missing.
- `needs curation`: NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O are summed across
  main and trace-mineral stock scopes.
- `needs curation`: post-autoclave 8 percent NaHCO3, 5 percent L-Cysteine HCl x
  H2O, and 5 percent Na2S x 9 H2O solution additions are stored as pure
  compound `G_PER_L` rows.
- `needs curation`: methanol is stored as `6.5 G_PER_L` even though JCM lists
  6.5 ml.

## Recommended Edits

- Preserve the JCM/MediaDive `Trace minerals` row as a 10 ml stock addition.
- Keep the Trace minerals formula scoped to that stock, including its 1000 ml
  water row.
- Restore the 1 L main-medium water row.
- Preserve the three post-autoclave stock additions with their source
  percentages and milliliter amounts instead of coercing them to pure-compound
  `G_PER_L`.
- Store methanol as a volume addition or convert it only with an explicit,
  evidence-backed density calculation.
- Remove the cross-scope duplicate sums for NaCl, MgSO4 x 7 H2O, and
  CaCl2 x 2 H2O.

## Follow-up Checks

- Re-run the focused LinkML, strict, reference, and term validators after
  regenerating the normalized owner and merged record.
- Diff the regenerated record against MediaDive `J385` and the live JCM 385,
  with explicit checks for the 10 ml trace-mineral stock and three
  post-autoclave solution additions.
- Confirm that no duplicate-merge notes remain on NaCl, MgSO4 x 7 H2O, or
  CaCl2 x 2 H2O.

## Additional Notes

Archived DSMZ/KOMODO and TOGO records for Methanosarcina acetivorans are
generated separately and may represent different source snapshots or variants.
