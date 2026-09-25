# YAML Record Review: thermosulfidibacter_medium__9a2ae38b

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermosulfidibacter_medium__9a2ae38b.yaml
- Started UTC: 2026-09-25T10:52:13Z
- Finished UTC: 2026-09-25T10:52:14Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M3128, Thermosulfidibacter Medium.
- The record was merged from `TOGO_M3128_Thermosulfidibacter_Medium`.
- The main checked sources were TOGO M3128, DSMZ Medium 1092, and MediaDive REST entry 1092.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 after the startup line only and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; exited 0 with no diagnostics.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The TOGO identity points to M3128 and the original DSMZ Medium 1092 PDF.
- TOGO M3128 and DSMZ 1092 both identify the pH range as 7.0-7.2, but the generated TOGO record has no `ph_range`.
- Sulfur powder is not grounded in the TOGO record; the corresponding direct DSMZ/KOMODO duplicate is grounded to sulfur atom rather than elemental sulfur.

## Evidence

- DSMZ/MediaDive 1092 lists a 1003 ml final volume with 1000 ml water, 30 g Sea Salt, 1 ml Wolfe's mineral elixir, 0.5 ml sodium resazurin solution, 3 g sulfur powder, 2.5 g NaHCO3, 2 g yeast extract, 2 ml Wolin's vitamin solution, and 0.5 g Na2S x 9 H2O.
- The DSMZ source includes two preparation steps: the initial H2/CO2 sparge and 110 C autoclave, followed by pressurization with sterile 80:20 H2/CO2 gas.
- TOGO M3128 also contains the Wolfe and Wolin stock recipes, but these are subordinate stocks added at 1 ml/L and 2 ml/L, respectively.
- A direct DSMZ/KOMODO 1092 duplicate exists as `THERMOSULFIDIBACTER_MEDIUM`.

## Completeness

- The generated TOGO record omits the pH range and all DSMZ preparation steps.
- Main, Wolfe-stock, and Wolin-stock water rows were summed into a 3000 g/L top-level distilled-water artifact.
- Wolfe's mineral elixir and Wolin's vitamin solution are represented twice: once as source-volume solution placeholders and again as full-strength stock ingredients at top level.

## Findings

- The formula has blocking stock-solution flattening. One milliliter of Wolfe's mineral elixir and two milliliters of Wolin's vitamin solution were migrated into gram-per-liter top-level ingredients, so the final record overstates magnesium sulfate, trace metals, and vitamins by stock-strength factors.
- The source addition volumes were also converted to placeholder solution concentrations, for example 1 g/L Wolfe's mineral elixir and 2 g/L Wolin's vitamin solution, with no composition on the solution records.
- The DSMZ pH range and preparation are missing from the TOGO import, so the generated record loses required anoxic handling and gas-pressure context.

## Recommended Edits

- Regenerate DSMZ 1092 from the direct DSMZ/MediaDive source, preserving pH 7.0-7.2, 1003 ml final volume, and the two DSMZ preparation steps.
- Model Wolfe's mineral elixir and Wolin's vitamin solution as subordinate stock additions instead of top-level stock concentrations.
- Merge or retire the stale TOGO M3128 record after the direct DSMZ 1092 representation is fixed.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm the repaired generated set has no 3000 g/L water row and no gram-per-liter top-level vitamin rows for this 2 ml/L Wolin addition.
- Confirm sulfur powder is grounded to an elemental sulfur concept, not sulfur atom.

## Additional Notes

- None found.
