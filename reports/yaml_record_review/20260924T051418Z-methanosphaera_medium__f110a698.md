# YAML Record Review: methanosphaera_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosphaera_medium__f110a698.yaml
- Started UTC: 2026-09-24T05:14:18Z
- Finished UTC: 2026-09-24T05:14:18Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:001424` for DSMZ/MediaDive medium 322, "METHANOSPHAERA MEDIUM", merged with a KOMODO duplicate carrying the same DSMZ ID.

## Validation

- LinkML open schema validation: Passed with "No issues found".
- Strict recipe validation: Passed; `/private/tmp/methanosphaera_medium_f110a698.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The primary identity is grounded to DSMZ/MediaDive medium 322 and preserves the DSMZ pH range of 6.7-6.9.
- DSMZ 322 has a parent solution plus clarified rumen fluid, Modified Wolin mineral, FeSO4, and Wolin vitamin child stocks.
- The generated record preserves the DTT row and DSMZ preparation prose, but it drops the clarified-rumen-fluid parent addition and flattens the mineral, FeSO4, and vitamin stocks into the parent ingredient list.

## Evidence

- DSMZ 322 and MediaDive 322 agree on a parent formula with 100 ml clarified rumen fluid, 10 ml Modified Wolin's mineral solution, 1.9 ml 0.1% Na2SeO4, 0.7 ml 0.1% NiCl2 x 6 H2O, 3 ml 0.1% FeSO4 x 7 H2O solution, 2 ml Wolin's vitamin solution (10x), 0.5 g DL-Dithiothreitol, and 900 ml distilled water.
- MediaDive represents Modified Wolin's mineral solution as solution 241, FeSO4 x 7 H2O solution as solution 5861, and Wolin's vitamin solution (10x) as solution 5980; the DSMZ PDF prints each of those child formulas separately.
- The generated FeSO4 row is a duplicate sum of `0.1` from Modified Wolin and `1.0` from the FeSO4 stock, and the generated formula has an extra `H2SO4` row at `1000 G_PER_L` from the FeSO4 stock solvent.
- An exact `rg --no-ignore --hidden` search found no `preferred_term` for clarified rumen fluid in the generated YAML, despite its required 100 ml parent addition in the source.

## Completeness

- Parent salts, organics, DTT, 0.1% selenate and nickel additions, pH, and preparation text are present.
- Clarified rumen fluid is absent as an ingredient.
- Parent water and stock water rows are absent.
- Modified Wolin, FeSO4, and Wolin vitamin stock boundaries are absent.

## Findings

1. Major - The required clarified-rumen-fluid addition is missing. DSMZ 322 adds 100 ml clarified rumen fluid to the parent formula, but the generated record only carries clarified-rumen-fluid preparation prose.
2. Major - Modified Wolin mineral stock is flattened into the parent formula. Parent values for NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, NiCl2 x 6 H2O, FeSO4 x 7 H2O, and multiple trace components include full stock-strength values rather than the 10 ml/l stock addition.
3. Major - FeSO4 stock is also flattened, adding `1.0 G_PER_L` FeSO4 x 7 H2O and `1000 G_PER_L` H2SO4 to the parent formula even though the source adds only 3 ml of a 0.1% FeSO4 stock.
4. Major - Wolin vitamin stock is flattened at 10x stock strength. The source adds 2 ml of 10x Wolin solution, but all vitamin rows appear as full stock concentrations in the parent.
5. Major - Required solvent rows are absent. DSMZ 322 includes 900 ml parent water and separate waters for Modified Wolin, FeSO4, and Wolin vitamin stocks; none are represented with the correct solution scope.

## Recommended Edits

- Recurate DSMZ/MediaDive 322 with child solution boundaries for clarified rumen fluid, Modified Wolin's mineral solution, FeSO4 x 7 H2O solution, and Wolin's vitamin solution.
- Restore the 100 ml clarified-rumen-fluid parent addition.
- Keep the 10 ml, 3 ml, and 2 ml stock additions as volumes instead of exposing their solutes at stock strength.
- Restore parent and child solvent rows in their proper solution scopes.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Confirm that `H2SO4` no longer appears as a parent ingredient.
- Confirm that clarified rumen fluid appears exactly once as a 100 ml parent addition.

## Additional Notes

Unlike the TOGO `M2658` rendering of DSMZ 322, this MediaDive-derived record kept the DTT ingredient and the main DSMZ preparation steps. A repair should preserve those parts while fixing ingredient scope.
