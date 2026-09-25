# YAML Record Review: methanosarcina_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosarcina_medium__44446b1f.yaml
- Started UTC: 2026-09-24T05:01:13Z
- Finished UTC: 2026-09-24T05:01:13Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:008189` for TOGO medium `M1634`, "Methanosarcina Medium", imported from NBRC medium 837.

## Validation

- LinkML open schema validation: Passed; exited 0 with no diagnostics.
- Strict recipe validation: Passed; `/private/tmp/methanosarcina_medium_44446b1f.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The source identity is grounded to TOGO `M1634`, the source metadata points to NBRC `NBRC_M837`, and the NBRC page still publishes a recipe named "Methanosarcina Medium" with final pH 6.8.
- The generated parent record does not preserve the NBRC formulation shape. NBRC has a main 981 ml water recipe plus 9 ml trace mineral solution and 10 ml trace vitamins additions; the generated YAML flattens both stock recipes into the parent ingredients while also retaining empty or wrong solution stubs.
- The generated YAML has no `ph_range` or `preparation_steps` top-level keys; an exact `rg --no-ignore --hidden` check against this record returned no matches for those keys.

## Evidence

- The NBRC recipe lists, in the main solution, KH2PO4, K2HPO4, MgCl2 x 6 H2O, NH4Cl, Bacto Yeast Extract, Hipolypepton, sodium acetate, trimethylamine-HCl, 9 ml trace mineral solution, 10 ml trace vitamins, NaHCO3, Na2S x 9 H2O, cysteine-HCl, 1 mg resazurin, and 981 ml distilled water.
- The inline NBRC trace mineral stock contains nitrilotriacetic acid, FeCl2 x 4 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, ZnCl2, CaCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, 1 L water, and pH adjustment to 7.0 with 1 N KOH.
- The inline NBRC trace vitamins stock contains 2 mg biotin, 2 mg folic acid, 10 mg pyridoxine-HCl, 5 mg thiamine-HCl, 5 mg riboflavin, 5 mg nicotinic acid, 5 mg Ca-pantothenate, 0.1 mg Vitamin B12, 5 mg p-Aminobenzoic acid, 5 mg lipoic acid, and 1 L water.
- The live MediaDive solution records linked by the generated stubs do not match the NBRC inline stocks. Solution 5445 points at a different trace-mineral composition with a nested "Trace minerals" solution plus selenite and tungstate, and solution 5469 has the same vitamin names as the NBRC stock but at ten times the NBRC masses.

## Completeness

- The main soluble ingredients are present.
- `Hipolypepton*` is absent from the parent ingredient list and appears only as an empty `solutions` entry named `Unknown solution`, even though the asterisk is only an NBRC supplier footnote.
- The NBRC preparation instructions and final pH are absent.
- The local trace mineral and trace vitamin stocks are not represented as child solutions with their NBRC compositions.

## Findings

1. Major - Trace mineral and trace vitamin stocks are flattened into parent ingredients at stock strength. NBRC adds only 9 ml trace mineral solution and 10 ml trace vitamins to the main 981 ml recipe, but the generated `ingredients` list includes nitrilotriacetic acid, FeCl2 x 4 H2O, all trace salts, KOH, and every vitamin as parent ingredients rather than nesting them under local stock solutions.
2. Major - Milligram source rows were serialized as grams per liter. The 1 mg resazurin main row became `1 G_PER_L`; vitamin rows such as 2 mg biotin, 5 mg p-Aminobenzoic acid, and 0.1 mg Vitamin B12 became `2 G_PER_L`, `5 G_PER_L`, and `0.1 G_PER_L`.
3. Major - Source water rows were merged across incompatible scopes. The parent water ingredient says `983.0 G_PER_L` and records that it merged `981.0, 1.0, 1.0`, which corresponds to the main 981 ml water row plus the separate 1 L water rows from the mineral and vitamin stocks.
4. Major - The `solutions` entries are not source-faithful. `Hipolypepton*` is a main 0.1 g ingredient with a Wako supplier footnote, not an empty solution, while the `Trace mineral solution**` and `Trace vitamins***` stubs incorrectly cite unrelated or tenfold-stronger live MediaDive solutions instead of carrying the NBRC inline formulas.
5. Major - Preparation and pH evidence was dropped. NBRC instructs curators to autoclave the base under 80/20 N2/CO2, autoclave Na2S x 9 H2O and cysteine-HCl separately as 5% solutions under N2, add the filter-sterile vitamin solution aseptically and anaerobically, and adjust the final medium to pH 6.8.

## Recommended Edits

- Reparse NBRC_M837 with three solution scopes: the main medium, the inline trace mineral solution, and the inline trace vitamins solution.
- Keep `Hipolypepton*` as a 0.1 g main ingredient and store the Wako footnote as a note, not as an empty child solution.
- Store the 9 ml and 10 ml stock additions on the parent formula with volume units, and keep the mineral/vitamin stock recipes in child solutions at their source milligram or gram masses per 1 L stock.
- Remove the `mediadive.solution:5445` and `mediadive.solution:5469` links unless a source proves they are the same as the NBRC inline footnote stocks.
- Restore the pH 6.8 target and the anaerobic autoclave, filter-sterilization, and reducing-agent handling instructions.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Inspect the regenerated record for unit drift from mg to g and from ml stock additions to G_PER_L solution concentrations.
- Confirm that distilled water remains scoped separately to the parent medium, trace mineral stock, and trace vitamin stock.

## Additional Notes

The optional gas defaults for nitrogen and carbon dioxide are not the central defect. The NBRC preparation text does use an 80/20 N2/CO2 atmosphere for the base medium, so those gases are source-relevant if they are linked to that instruction rather than treated as free-floating variable ingredients.
