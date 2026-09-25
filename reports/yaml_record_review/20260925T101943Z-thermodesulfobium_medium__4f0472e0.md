# YAML Record Review: thermodesulfobium_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobium_medium__4f0472e0.yaml
- Started UTC: 2026-09-25T10:16:00Z
- Finished UTC: 2026-09-25T10:19:43Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfobium_medium__4f0472e0`, which represents the direct MediaDive/DSMZ import of DSMZ Medium 1005 as `CultureMech:000421`.

## Validation

- Schema: Passed with `No issues found`.
- Strict validation: Passed with 1 file, 0 error files, and 0 rows.
- Reference validation: Passed with 0 checks reported.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The direct branch has the expected `mediadive.medium:1005` identity, DSMZ Medium 1005 citation, and pH range of 5.5 to 6.0. An exact ignored-inclusive search for `DSMZ_Medium1005.pdf`, `mediadive.medium:1005`, and `TOGO_M2734` found the same source recipe split across this direct branch, the TOGO M2734 branch, and uppercase KOMODO 1005.

## Evidence

MediaDive 1005 and the DSMZ Medium 1005 PDF both store a 1011 ml main solution with 10 ml Trace element solution, 1 ml Wolin's vitamin solution 10x, 1000 ml water, and direct salts, acetate, and cysteine. The Trace element solution is a separate 1000 ml stock containing 12.8 g nitrilotriacetic acid, 1 g `FeCl2 x 4 H2O`, trace salts, 1 g `NaCl`, 0.1 g `CaCl2 x 2 H2O`, and 0.04 g `Na2WO4 x 2 H2O`. Wolin's vitamin solution 10x is a separate 1000 ml stock with milligram vitamin quantities.

## Completeness

The direct target preserves the DSMZ pH range and preparation text. It does not preserve Trace element solution or Wolin's vitamin solution as stock additions; both stocks are expanded into the final ingredient list at their stock concentrations.

## Findings

- High: the 10 ml Trace element solution was flattened into final-medium ingredients at full stock strength. The generated target carries 12.8 g/L nitrilotriacetic acid, 1 g/L `FeCl2 x 4 H2O`, 0.1 g/L `NiCl2 x 6 H2O`, and other 1 L stock rows as direct ingredients.
- High: stock salts were merged with basal salts. `CaCl2 x 2 H2O` is `0.1296736` g/L with `Merged 2 duplicates: 0.0296736, 0.1`, and `NaCl` is `1.197824` g/L with `Merged 2 duplicates: 0.197824, 1.0`; the larger duplicate rows belong to the Trace element stock.
- High: the 1 ml Wolin's vitamin solution 10x addition was flattened into final-medium vitamin rows at full stock concentration.
- Medium: the direct MediaDive/DSMZ 1005 branch is duplicated by the TOGO M2734 and KOMODO 1005 generated branches.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/thermodesulfobium_medium.yaml` so the 10 ml Trace element solution and 1 ml Wolin's vitamin solution 10x additions remain nested stock additions.
- Prevent duplicate-ingredient merging from summing basal salts with salts that belong to nested stock recipes.
- Canonicalize direct DSMZ 1005, TOGO M2734, and KOMODO 1005 imports before generating merged YAML.

## Follow-up Checks

- Regenerate merged YAML and verify DSMZ 1005 no longer has undiluted Trace element rows or Wolin vitamin rows in the final ingredient list.
- Confirm the corrected DSMZ 1005 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `DSMZ_Medium1005.pdf`, `mediadive.medium:1005`, and `TOGO_M2734` to ensure DSMZ 1005 has one generated target.

## Additional Notes

None found.
