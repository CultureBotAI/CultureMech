# YAML Record Review: thermodesulfobium_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobium_medium__063408d5.yaml
- Started UTC: 2026-09-25T10:16:00Z
- Finished UTC: 2026-09-25T10:19:42Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfobium_medium__063408d5`, which represents TOGO Medium M2734 for DSMZ Medium 1005 as `CultureMech:009285`.

## Validation

- Schema: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 1 file, 0 error files, and 0 rows.
- Reference validation: Passed with 0 checks reported.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

TOGO M2734 identifies Thermodesulfobium Medium, cites the DSMZ Medium 1005 PDF, and carries pH 5.5 to 6.0, matching the DSMZ source. An exact ignored-inclusive search for `DSMZ_Medium1005.pdf`, `mediadive.medium:1005`, and `TOGO_M2734` found the same source recipe split across three generated branches: this TOGO branch, the direct MediaDive/DSMZ 1005 branch, and uppercase KOMODO 1005.

## Evidence

DSMZ Medium 1005 lists a main solution with 10 ml Trace element solution, 1 ml Wolin's vitamin solution 10x, 1000 ml distilled water, and direct salts, acetate, and cysteine. Its Trace element solution is a separate 1000 ml stock with 12.8 g nitrilotriacetic acid, chloride salts, boric acid, molybdate, selenite, tungstate, 1 g `NaCl`, and 1000 ml water. Its Wolin's vitamin solution 10x is a separate 1000 ml stock with milligram vitamin amounts.

## Completeness

The TOGO target retains the DSMZ identity through its source URL and has placeholders for Trace element solution and Vitamin solution. It loses the nested recipe scopes by also flattening trace-element and vitamin stock ingredients into the top-level ingredient list.

## Findings

- High: the main medium, Trace element solution, and vitamin solution were flattened into one ingredient scope. The generated record sums three 1000 ml water rows to `3000.0 G_PER_L`, and also merges the direct 0.2 g `NaCl` row with the Trace element stock's 1 g `NaCl` row.
- High: vitamin stock rows from Wolin's 10x solution were imported as gram-per-liter final-medium rows even though the source lists milligram amounts in a 1 L stock and adds only 1 ml of that stock to the final medium. Biotin is `2 G_PER_L`, pyridoxine-HCl is `10 G_PER_L`, and vitamin B12 is `0.1 G_PER_L`.
- High: the Trace element and Vitamin solution stock additions were migrated to placeholders with `10 G_PER_L` concentrations. The DSMZ source uses 10 ml of Trace element solution and 1 ml of Wolin's vitamin solution 10x.
- Medium: the TOGO M2734, direct MediaDive/DSMZ 1005, and KOMODO 1005 records all remain as separate generated branches for the same DSMZ source recipe.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/TOGO_M2734_Thermodesulfobium_Medium.yaml` so the main DSMZ 1005 recipe, Trace element solution, and Wolin's vitamin solution 10x are separate scopes.
- Keep the Trace element and Wolin additions as 10 ml and 1 ml stock additions, with linked or nested stock definitions.
- Fix the TOGO import path that converts milligram vitamin-stock rows to gram-per-liter final-medium rows.
- Canonicalize TOGO M2734, direct DSMZ/MediaDive 1005, and KOMODO 1005 before merge generation.

## Follow-up Checks

- Regenerate merged YAML and verify DSMZ 1005 no longer has `3000.0 G_PER_L` water, gram-per-liter vitamin rows, or `10 G_PER_L` placeholders for stock additions.
- Confirm the corrected DSMZ 1005 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `DSMZ_Medium1005.pdf`, `mediadive.medium:1005`, and `TOGO_M2734` to ensure DSMZ 1005 has one generated target.

## Additional Notes

None found.
