# YAML Record Review: thiomicrospira_pelophila_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiomicrospira_pelophila_medium__15fc8af5.yaml
- Started UTC: 2026-09-25T13:05:00Z
- Finished UTC: 2026-09-25T13:05:24Z
- Verdict: needs curation

## Target

- Generated YAML for the direct DSMZ/MediaDive 142 THIOMICROSPIRA PELOPHILA MEDIUM import.
- The record was merged from six DSMZ 142 KOMODO strain variants and `thiomicrospira_pelophila_medium`.
- The checked sources were MediaDive 142, DSMZ Medium 142, and local exact DSMZ 142 sibling imports.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to DSMZ/MediaDive 142, THIOMICROSPIRA PELOPHILA MEDIUM.
- The merged KOMODO 142 strain-specific records all point back to DSMZ 142.
- DSMZ 142 documents several strain-specific variants, including DSM 12346, 12350, 12351, 12352, 12353, and 12354, that omit vitamins and adjust pH to 7.3 to 7.6.

## Evidence

- DSMZ 142 adds 0.2 ml Vishniac and Santer trace element solution and 1 ml seven vitamins solution to the 1005 ml main recipe.
- DSMZ 142 separately autoclaves K2HPO4 and Na2S2O3 in 10% of the final volume and filter-sterilizes the vitamin solution.
- The DSMZ trace and vitamin recipes are 1 L stocks.

## Completeness

- The DSMZ 142 identity, pH 7.2, main salts, and preparation text are present.
- The 0.2 ml trace stock and 1 ml vitamin stock are flattened into final ingredients at stock strength.
- The `CaCl2 x 2 H2O` row sums 0.41791 g/L from the main recipe with 5.54 g/L from the trace stock.
- Source-specific variants that omit vitamins were merged into a vitamin-containing base record as source duplicates.

## Findings

- Trace and vitamin stock rows are overstated by treating 1 L stock concentrations as final medium concentrations.
- `CaCl2 x 2 H2O` was summed across the main medium and trace stock scopes.
- The six DSMZ 142 KOMODO strain variants are not exact duplicates because DSMZ says those strains omit vitamins and use a different pH range.
- The DSMZ 142 water row is omitted.

## Recommended Edits

- Model the 0.2 ml trace solution and 1 ml vitamin solution as separate stock additions.
- Remove duplicate sums across main and stock scopes.
- Split the DSM 12346, 12350, 12351, 12352, 12353, and 12354 vitamin-omission variants from the DSMZ 142 base record.
- Restore the DSMZ water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare every KOMODO 142 strain variant against the DSMZ 142 variant notes before deciding merge relationships.
- Verify the 0.2 ml trace addition is not rounded to a 1 ml default.

## Additional Notes

- None found.
