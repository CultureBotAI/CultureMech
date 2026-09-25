# YAML Record Review: thermodesulfobacterium_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_medium__09d788a8.yaml
- Started UTC: 2026-09-25T10:11:00Z
- Finished UTC: 2026-09-25T10:15:31Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfobacterium_medium__09d788a8`, which represents the direct MediaDive/DSMZ import of DSMZ Medium 206 as `CultureMech:001305`.

## Validation

- Schema: Passed with `No issues found`.
- Strict validation: Passed with 1 file, 0 error files, and 0 rows.
- Reference validation: Passed with 0 checks reported.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The direct branch has the expected `mediadive.medium:206` identity and the DSMZ Medium 206 pH range of 6.8 to 7.0. An exact ignored-inclusive search for `mediadive.medium:206`, `DSMZ_Medium206.pdf`, and `TOGO_M2624` found the same DSMZ recipe split into three generated outputs: this direct DSMZ/MediaDive branch, an uppercase KOMODO `THERMODESULFOBACTERIUM_MEDIUM` branch, and the separate TOGO M2624 branch in `data/merge_yaml/merged/thermodesulfobacterium_medium__2f12e502.yaml`.

## Evidence

MediaDive 206 and the DSMZ Medium 206 PDF both store a 1017 ml main solution with 10 ml Trace element solution, 1.5 ml `FeSO4 x 7 H2O` solution, 0.5 ml sodium resazurin solution, 5 ml Wolin's vitamin solution, and 1000 ml distilled water. The Trace element solution is a separate 1000 ml stock containing 12.8 g nitrilotriacetic acid, metal chlorides, boric acid, molybdate, and sodium selenite; Wolin's vitamin solution is a separate 1000 ml stock containing milligram vitamin quantities.

## Completeness

The direct target preserves the DSMZ pH range and main preparation text. It does not preserve the Trace element solution or Wolin's vitamin solution hierarchy; both stocks are expanded into the final ingredient list with their stock concentrations.

## Findings

- High: the 10 ml Trace element solution was flattened into direct final-medium ingredients at full stock concentration. The generated record carries 12.8 g/L nitrilotriacetic acid, 0.2 g/L `FeCl2 x 4 H2O`, 0.17 g/L `CoCl2 x 6 H2O`, and other Trace element stock rows as if they were added directly per liter.
- High: the 5 ml Wolin's vitamin solution was flattened into direct final-medium ingredients at full stock concentration. The generated biotin, folic acid, pyridoxine, and other vitamin rows are 1 L vitamin-stock concentrations, not the 5 ml addition to Medium 206.
- Medium: the DSMZ Medium 206 recipe is duplicated in two other generated records, one derived from TOGO M2624 and one from KOMODO 206, instead of being canonicalized into the direct DSMZ/MediaDive branch before merge generation.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/thermodesulfobacterium_medium.yaml` so Trace element solution and Wolin's vitamin solution remain 10 ml and 5 ml stock additions with their compositions retained as nested solutions.
- Keep the 1.5 ml `FeSO4 x 7 H2O` solution and 0.5 ml sodium resazurin solution labeled as solution additions rather than reducing them to unlabeled scalar rows.
- Canonicalize direct DSMZ 206, TOGO M2624, and KOMODO 206 imports before generating merged YAML.

## Follow-up Checks

- Regenerate merged YAML and verify DSMZ 206 has one canonical generated record with Trace element and Wolin's vitamin stock additions.
- Confirm the corrected direct DSMZ 206 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:206`, `DSMZ_Medium206.pdf`, and `TOGO_M2624` to ensure no duplicate generated DSMZ 206 branches remain.

## Additional Notes

The initial local source search used `mediadive.medium:206` without a non-digit boundary and also matched 2060-series stock records; that result was discarded and rerun with a boundary.
