# YAML Record Review: Methanoregula Peat Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanoregula_peat_medium.yaml`
- Started UTC: 2026-09-24T04:32:36Z
- Finished UTC: 2026-09-24T04:35:23Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:009209`, the generated one-source merge for TOGO medium
`M2654`, `Methanoregula (Peat) Medium`, derived from
`data/normalized_yaml/archaea/TOGO_M2654_Methanoregula_Peat_Medium.yaml`.

The generated merge was produced on fingerprint
`54c722b77c7f7f8bb9de7d87f01be2c344f43588aabe505bd0e4d7dd50e1c45e` from
`TOGO_M2654_Methanoregula_Peat_Medium`.

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

The top-level medium identity is correct for the TOGO import: the media term is
`TOGO:M2654`, and the TOGO API identifies `M2654` as `Methanoregula (Peat)
Medium` from DSMZ medium 1280.

The immediate TOGO source has the older six-solution DSMZ 1280 formulation:
950 ml Solution A, 10 ml Solution B, 12.55 ml Solution C, 10 ml Solution D,
10 ml Solution E, and 10 ml Solution F. Current DSMZ/MediaDive has drifted to
954 ml Solution A, 13 ml Solution C, a 1007 ml final volume, and Solution F as a
10 ml addition of `Wolin's vitamin solution (10x)`. A repair should decide
whether this record intentionally remains the TOGO snapshot or should be
regenerated from current DSMZ/MediaDive.

Several generated solution term IDs are not grounded by TOGO `M2654` and do
not match current DSMZ 1280 MediaDive IDs. For example,
`mediadive.solution:5342` is an unrelated `Solution A`, and
`mediadive.solution:6129` is a generic trace-elements solution that does not
match DSMZ 1280; the current DSMZ 1280 trace solution is
`mediadive.solution:2568`.

Ingredient grounding is also stale for some rows. `MgSO4 x 7 H2O` has the
correct primary heptahydrate term but a generic `mediaingredientmech_chebi_term`
for magnesium sulfate, and `NiCl2 x 6 H2O` is grounded only to anhydrous nickel
dichloride.

## Evidence

### Supported by inspected sources

- TOGO `M2654` supports top-level assembly from Solutions A through F in the
  quantities 950 ml, 10 ml, 12.55 ml, 10 ml, 10 ml, and 10 ml.
- The TOGO snapshot supports Solution A with 0.5 ml 0.1 percent Na-resazurin
  solution, 2 ml 0.1 percent KCl solution, 950 ml distilled water, 14 mg
  KH2PO4, 27 mg NH4Cl, 17 mg Na-acetate, 1 ml trace elements solution, 1 N HCl,
  and 80 percent H2 plus 20 percent CO2 gas.
- TOGO supports a local trace-elements solution containing 10 ml 25 percent
  HCl, 1000 ml distilled water, MgSO4 x 7 H2O, CaCl2 x 2 H2O, Na2MoO4 x
  2 H2O, H3BO3, CoCl2 x 6 H2O, NiCl2 x 6 H2O, ZnCl2, CuSO4 x 5 H2O,
  AlK(SO4)2 x 12 H2O, MnSO4 x 4 H2O, and FeCl2 x 4 H2O.
- TOGO supports Solution B as 10 ml distilled water, 1.58 g Homo-PIPES,
  0.18 g NaOH, and N2 gas; Solution C as 7.2 ml 0.38 M NaOH, 4.8 ml
  0.5 M nitrilotriacetate solution, 0.55 ml 15 percent TiCl3, and N2 gas;
  Solution D as 10 ml distilled water, 0.2 g yeast extract, and N2 gas; and
  Solution E as 10 ml distilled water, 0.07 g 2-mercaptoethanesulfonate, and
  N2 gas.
- The TOGO snapshot supports its own 100 ml Solution F vitamin stock with
  biotin, p-Aminobenzoic acid, thiamine-HCl, pyridoxine-HCl, folic acid,
  Vitamin B12, riboflavin, nicotinic acid, lipoic acid, D-Ca-pantothenate, and
  N2 gas.
- TOGO includes preparation comments for making the trace-elements solution,
  adjusting Solution B to pH 5.5, gassing and autoclaving Solution A, preparing
  Solutions B through F under N2 and filter-sterilizing them, adding B through F
  to sterile Solution A in order before inoculation, adjusting the complete
  medium to pH 5.1, post-inoculation pressurization with H2/CO2, and a 10 to
  20 percent inoculum note.

### Unsupported or over-scoped in the YAML

- The YAML flattens stock-local components into the top-level ingredient list
  and gives them `G_PER_L` units equal to the TOGO amount text. Examples include
  `KH2PO4` at `14 G_PER_L` although TOGO lists 14 mg in Solution A, and
  `Na2MoO4 x 2 H2O` at `24 G_PER_L` although TOGO lists 24 mg in the
  trace-elements solution.
- The `Distilled water` row sums six independent solution-scope water rows
  into `2080.0 G_PER_L`, with a duplicate note showing the unsupported
  cross-scope sum `950.0, 1000.0, 10.0, 10.0, 10.0, 100.0`.
- `NaOH (0.38 M)`, `HCl (25%)`, vitamin rows, and several trace salts are
  recorded as if they were final-medium gram-per-liter ingredients even though
  the source uses them inside local stock recipes.
- The Solution C rows for nitrilotriacetate and TiCl3 were moved into
  top-level empty solution stubs, so their parent relationship to Solution C is
  lost.
- The generated `solutions` array gives milliliter additions `G_PER_L` units
  and generic `Unknown solution` names; those rows do not preserve the source
  assembly semantics.
- None of the TOGO preparation comments were migrated into
  `preparation_steps`.
- Several `mediadive.solution` links point to unrelated stock formulas rather
  than TOGO-local subcomponents or the current DSMZ 1280 MediaDive solutions.

## Completeness

The record is incomplete as a curation artifact. It has most of the compound
names from the TOGO snapshot, but the nested Solution A through F structure,
the trace-elements and vitamin stock scopes, the dilution relationships, the
Solution C reducer additions, and the anaerobic preparation workflow are not
represented faithfully.

Empty optional fields were not treated as defects.

## Findings

- `needs curation`: all source-local solutions are flattened; stock-local
  masses and volumes are misrepresented as top-level final `G_PER_L`
  concentrations.
- `needs curation`: the six water rows were merged into an impossible
  `2080.0 G_PER_L` top-level water row.
- `needs curation`: solution additions in the `solutions` array use `G_PER_L`
  for milliliter source amounts, have placeholder `Unknown solution` names, and
  in several cases link to unrelated MediaDive stock IDs.
- `needs curation`: the nitrilotriacetate and TiCl3 additions from Solution C
  are detached from Solution C as empty top-level solution stubs.
- `needs curation`: no TOGO preparation comments were carried into the
  generated record.
- `needs curation`: the generated record should either stay pinned to the TOGO
  snapshot or be regenerated from current DSMZ 1280/MediaDive 1280 before
  comparing expected volumes.
- `needs curation`: `MgSO4 x 7 H2O` and `NiCl2 x 6 H2O` have stale or broad
  ingredient grounding.

## Recommended Edits

- Rework the TOGO importer/solution migrator so `reference_media_id: M2654`
  rows become local solution additions with milliliter units, not top-level
  `G_PER_L` ingredients.
- Preserve Solution A through F and the trace-elements and vitamin stocks as
  independent subrecipes; keep each water row and amount within its source
  solution instead of merging by `preferred_term`.
- Keep 0.1 percent Na-resazurin, 0.1 percent KCl, nitrilotriacetate, and TiCl3
  additions scoped to the specific source solutions that contain them.
- Migrate the TOGO comments into ordered `preparation_steps`, including the
  anoxic H2/CO2 and N2 handling, pH adjustments, filtration, and inoculum note.
- Remove the generic MediaDive solution IDs unless the row can be grounded to
  the exact current DSMZ 1280 solution or to a TOGO-local blank node.
- Refresh CHEBI and `mediaingredientmech_chebi_term` grounding after the
  structural repair.

## Follow-up Checks

- Re-run the focused LinkML, strict, reference, and term validators after
  regenerating the normalized owner and merged file.
- Diff the regenerated TOGO owner against the `gmdb_medium_by_gmid?gm_id=M2654`
  payload, with special attention to the Solution C and Solution F scopes.
- Separately compare TOGO `M2654` against current DSMZ/MediaDive 1280 and make a
  curation decision about source drift before opening a fix PR.
- Verify that the rebuilt generated YAML has no duplicate-merge note on water
  and no `Unknown solution` placeholders.

## Additional Notes

The direct MediaDive DSMZ 1280 import already exists as
`data/normalized_yaml/archaea/methanoregula_peat_medium.yaml` and will be
reviewed separately via
`data/merge_yaml/merged/methanoregula_peat_medium__84e41704.yaml`.
