# YAML Record Review: r2a_agar_with_artificial_seawater
- Repository: CultureMech
- Record: data/merge_yaml/merged/r2a_agar_with_artificial_seawater__db9d0bb8.yaml
- Started UTC: 2026-09-25T00:20:46Z
- Finished UTC: 2026-09-25T00:21:29Z
- Verdict: needs curation

## Target
Reviewed generated record `data/merge_yaml/merged/r2a_agar_with_artificial_seawater__db9d0bb8.yaml`.

Owner record:

- `data/normalized_yaml/bacterial/r2a_agar_with_artificial_seawater.yaml`
- `merge_fingerprint`: `db9d0bb824c33ec523b902c636f03290dbcd83ae340720997eccd1d65a8149e4`
- `merged_from`: `r2a_agar_with_artificial_seawater`

The generated YAML is stale relative to the current owner. A 2026-09-06 repair replaced the flattened artificial-seawater salts with a nested `Artificial seawater` solution and added JCM 736 source notes, preparation steps, references, and a source-duplicate link to TOGO M868.

## Validation
- Open LinkML validation against `MediaRecipe`: passed; no issues found.
- Strict validation: passed; `/private/tmp/r2a_agar_with_artificial_seawater__db9d0bb8.strict.tsv` was header-only with 0 data rows.
- LinkML reference validation: passed; 0 reference checks, all validations passed.
- LinkML term validation with labels: passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding
- Identity is correct for JCM `832`, R2A Agar with Artificial Seawater.
- Live JCM 832 lists `R2A agar (BD-Difco)` 18.2 g and `Artificial seawater` from JCM 736 at 1 L.
- Live JCM 736 defines the referenced artificial seawater salts: NaCl, `MgCl2 x 6H2O`, `Na2SO4`, `CaCl2 x 2H2O`, KCl, `NaHCO3`, KBr, `H3BO3`, `SrCl2 x 6H2O`, NaF, and distilled water to 1 L.
- The exact ignored-file search for `mediadive.medium:J832`, `Source: JCM, ID: J832`, and `GRMD=832` found this direct JCM owner and generated target, plus a repaired TOGO M868 owner and stale generated TOGO duplicate for the same JCM page.
- A second exact ignored-file search for `TOGO:M868`, `togomedium.org/medium/M868`, and `JCM_M832` found only the TOGO M868 owner, stale generated TOGO duplicate, and source indexes.

## Evidence
- `data/normalized_yaml/bacterial/r2a_agar_with_artificial_seawater.yaml` now models JCM 832 as 18.2 g/L R2A agar with a 1000 ml/L `Artificial seawater` solution whose nested composition comes from JCM 736.
- `data/normalized_yaml/bacterial/TOGO_M868_R2A_Agar_With_Artificial_Seawater.yaml` has the same repaired nested artificial-seawater solution and is marked as a `SOURCE_DUPLICATE` of the direct JCM owner.
- The reviewed generated file predates the repair and still exposes the JCM 736 artificial-seawater salts as top-level final ingredients.
- `data/merge_yaml/merged/R2A_AGAR_WITH_ARTIFICIAL_SEAWATER.yaml` is also stale; it still has an empty artificial-seawater placeholder at 1 `G_PER_L`.

## Completeness
The current normalized owner is complete for the simple JCM 832 wrapper around artificial seawater. The generated record is incomplete because it is stale and still lacks the repaired solution nesting, preparation steps, references, and duplicate link.

## Findings
1. The generated direct record is stale relative to the repaired owner and still flattens JCM 736 artificial-seawater salts as final top-level ingredients.
2. The generated record has the wrong structural semantics: JCM 832 adds 1 L artificial seawater, while the generated row set makes the seawater salts look like direct components of the R2A medium.
3. The same JCM 832 source remains as a generated TOGO M868 sibling; both normalized owners are repaired, but both generated records predate the repair.

## Recommended Edits
1. Regenerate `data/merge_yaml/merged/r2a_agar_with_artificial_seawater__db9d0bb8.yaml` from the repaired direct JCM owner.
2. Regenerate or retire the TOGO M868 generated sibling so the generated layer does not keep both stale shapes for the same JCM 832 source.
3. Preserve the nested JCM 736 artificial-seawater composition, preparation steps, references, and `SOURCE_DUPLICATE` relationship during regeneration.

## Follow-up Checks
- Re-run open LinkML, strict, reference, and term validators for the regenerated direct and TOGO records.
- Re-run exact ignored-file searches for `mediadive.medium:J832`, `TOGO:M868`, `togomedium.org/medium/M868`, `JCM_M832`, and `GRMD=832` to confirm stale exact-source duplicates are gone.

## Additional Notes
None.
