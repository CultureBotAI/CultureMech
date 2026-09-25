# YAML Record Review: thermodesulfobacterium_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulfobacterium_medium__2f12e502.yaml
- Started UTC: 2026-09-25T10:11:00Z
- Finished UTC: 2026-09-25T10:15:32Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulfobacterium_medium__2f12e502`, which represents TOGO Medium M2624 for DSMZ Medium 206 as `CultureMech:009189`.

## Validation

- Schema: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; the strict TSV had only its header row and no error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The TOGO metadata for M2624 points to the same DSMZ Medium 206 PDF as the direct MediaDive/DSMZ 206 record and carries the same pH range, 6.8 to 7.0. An exact ignored-inclusive search for `mediadive.medium:206`, `DSMZ_Medium206.pdf`, and `TOGO_M2624` found this branch still separated from the direct DSMZ 206 branch and the uppercase KOMODO 206 branch.

## Evidence

The TOGO M2624 API preserves three separate component groups from DSMZ 206: the main medium, the Trace element solution, and Wolin's vitamin solution. The DSMZ PDF lists 1000 ml distilled water in the main medium, 1000 ml distilled water in the Trace element stock, and 1000 ml distilled water in Wolin's vitamin stock. It also specifies 10 ml Trace element solution, 1.5 ml 0.1% `FeSO4 x 7 H2O` in 0.1 N `H2SO4`, 0.5 ml 0.1% sodium resazurin, and 5 ml Wolin's vitamin solution as additions to the main medium.

## Completeness

The generated target retains placeholder solution entries for sodium resazurin, ferrous sulfate, Trace element solution, Wolin's vitamin solution, and KOH solution. Those placeholders have empty compositions or external notes, and the record also duplicates their nested stock ingredients in the top-level ingredient list.

## Findings

- High: the main medium, Trace element stock, and Wolin's vitamin stock were flattened into one ingredient scope. The target sums the three 1000 ml water rows to `3000.0 G_PER_L`, which is a visible symptom of the paragraph hierarchy being lost.
- High: Wolin's vitamin stock amounts were imported as gram-per-liter final-medium concentrations even though DSMZ lists milligram quantities per 1 L vitamin stock and adds only 5 ml of that stock to the medium. For example, biotin is `2 G_PER_L`, pyridoxine hydrochloride is `10 G_PER_L`, and vitamin B12 is `0.1 G_PER_L`.
- High: stock solution additions were migrated to empty or note-only `solutions` entries with gram-per-liter concentrations. `Trace element solution` is `10 G_PER_L`, `Wolin's vitamin solution` is `5 G_PER_L`, `FeSO4 x 7 H2O solution` is `1.5 G_PER_L`, and sodium resazurin solution is `0.5 G_PER_L`; the source units are milliliters.
- Medium: this TOGO M2624 representation of DSMZ Medium 206 is duplicated by the direct MediaDive/DSMZ 206 branch and by KOMODO 206 instead of being canonicalized into one generated record.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/TOGO_M2624_Thermodesulfobacterium_Medium.yaml` with main, Trace element solution, and Wolin's vitamin solution modeled as separate scopes so water rows and stock ingredients are not merged.
- Preserve the 10 ml Trace element, 5 ml Wolin's vitamin, 1.5 ml ferrous sulfate, and 0.5 ml resazurin additions with milliliter units and stock identities.
- Fix the TOGO import path that turns milligram stock rows into gram-per-liter final-medium rows.
- Canonicalize TOGO M2624, direct DSMZ/MediaDive 206, and KOMODO 206 before merge generation.

## Follow-up Checks

- Regenerate merged YAML and verify the DSMZ 206 TOGO path no longer emits `3000.0 G_PER_L` water, gram-per-liter vitamin rows from milligram stock amounts, or `10 G_PER_L` and `5 G_PER_L` stock placeholders.
- Confirm the corrected DSMZ 206 canonical record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:206`, `DSMZ_Medium206.pdf`, and `TOGO_M2624` to ensure DSMZ 206 now has one generated target.

## Additional Notes

The initial local source search used `mediadive.medium:206` without a non-digit boundary and also matched 2060-series stock records; that result was discarded and rerun with a boundary.
