# YAML Record Review: thermodesulforhabdus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulforhabdus_medium.yaml
- Started UTC: 2026-09-25T10:16:00Z
- Finished UTC: 2026-09-25T10:19:44Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermodesulforhabdus_medium`, which is the KOMODO 707 Thermodesulforhabdus Medium branch for `CultureMech:006339`.

## Validation

- Schema: Passed with `No issues found`.
- Strict validation: Passed with 1 file, 0 error files, and 0 rows.
- Reference validation: Passed with 0 checks reported.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The generated target is stale relative to `data/normalized_yaml/bacterial/thermodesulforhabdus_medium.yaml`. The normalized record has a 2026-09-10 `RESOLVED_KOMODO_707_SCORE35` repair grounded to archived DSMZ Medium 707 and archived DSMZ Medium 320 PDFs; the generated target still has the pre-repair KOMODO placeholder with only a variable `sodium` ingredient. Live checks found that MediaDive REST currently returns `DataNotFound` for medium 707 and the current DSMZ Medium 707 PDF URL returns a 404 HTML page, so the archive URLs cited in the repaired normalized record are the authoritative source trace.

## Evidence

Archived DSMZ Medium 707 lists Thermodesulforhabdus Medium with sodium acetate trihydrate, `Na2SO4`, `NH4Cl`, `KH2PO4`, `NaCl`, `MgCl2 x 6 H2O`, `CaCl2 x 2 H2O`, 1 ml Trace element solution SL-10 from DSMZ Medium 320, 0.5 mg resazurin, and 1000 ml distilled water. The archived instructions prepare the medium anaerobically under 100% `N2`, adjust pH to 6.8 with sterile 5% sodium bicarbonate, and reduce with 0.15 g/L sodium sulfide plus 50 mg/L sodium dithionite. Archived DSMZ Medium 320 provides the SL-10 stock composition.

## Completeness

The repaired normalized record already expands DSMZ 707 and DSMZ 320 into a complete ingredient set with per-liter SL-10 contributions, bicarbonate, reducing agents, gases, and references. The generated merged record lacks all of that curated content and retained only a note-extracted `sodium` placeholder.

## Findings

- High: `data/merge_yaml/merged/thermodesulforhabdus_medium.yaml` is stale relative to the repaired normalized YAML. It lacks the 2026-09-10 `RESOLVED_KOMODO_707_SCORE35` repair, archived DSMZ references, and every curated DSMZ 707 ingredient except a placeholder sodium row.
- High: the generated record is functionally empty as a medium recipe. It omits acetate, sulfate, ammonium, phosphate, chloride, magnesium, calcium, the SL-10 trace element addition, resazurin, sodium bicarbonate, sodium sulfide, sodium dithionite, anaerobic gases, and distilled water.
- Medium: the generated target preserves the pH 6.8 scalar but keeps the old `pH buffer: sodium bicarbonate` KOMODO note and `Aerobic: Yes`, which conflict with the repaired archived DSMZ preparation under anaerobic `N2`.

## Recommended Edits

- Regenerate merged YAML from `data/normalized_yaml/bacterial/thermodesulforhabdus_medium.yaml` so the archived DSMZ repair is reflected in `data/merge_yaml/merged/thermodesulforhabdus_medium.yaml`.
- Verify the merge path does not prefer an older KOMODO score-35 placeholder over the repaired normalized record for the same normalized filename.
- Keep the archived DSMZ 707 and 320 references from the normalized record in the generated output.

## Follow-up Checks

- Regenerate merged YAML and verify `thermodesulforhabdus_medium.yaml` contains sodium acetate trihydrate, sulfate, mineral salts, expanded SL-10 trace rows, bicarbonate, sodium sulfide, sodium dithionite, `N2`, `CO2`, and archived DSMZ references.
- Confirm the regenerated KOMODO 707 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `thermodesulforhabdus_medium`, `KOMODO_707`, and `DSMZ Medium: 707` to confirm no stale generated target remains.

## Additional Notes

None found.
