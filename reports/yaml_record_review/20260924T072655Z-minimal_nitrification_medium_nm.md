# YAML Record Review: minimal_nitrification_medium_nm

- Repository: CultureMech
- Record: data/merge_yaml/merged/minimal_nitrification_medium_nm.yaml
- Started UTC: 2026-09-24T07:26:55Z
- Finished UTC: 2026-09-24T07:27:21Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009629`
- Generated name: `minimal_nitrification_medium_nm`
- Generated source file: `data/merge_yaml/merged/minimal_nitrification_medium_nm.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/minimal_nitrification_medium_nm.yaml`
- Upstream source: TOGO Medium `M3179`, `Minimal nitrification medium (NM)`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/minimal_nitrification_medium_nm.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with TOGO `M3179`.
- The `media_term` points to `TOGO:M3179` with label `Minimal nitrification medium (NM)`.
- All ten generated ingredients have CHEBI grounding.
- The EDTA row correctly preserves TOGO's unroled ingredient: the upstream item has no GMO role.
- The `high_metal: true` flag is likely an artifact of the unit import defect: the source recipe uses trace-level CaCl2, MgSO4, CuSO4, Na2CO3, FeSO4, and EDTA, not the gram-per-liter concentrations in the YAML.

## Evidence

- TOGO `M3179` defines final concentrations of 3.3 g/L `(NH4)2SO4`, 5.85 g/L `KH2PO4`, 0.48 g/L `NaH2PO4`, 90 mg/L `MgSO4`, 22 ug/L `CaCl2`, 1.5 mg/L `FeSO4`, 5 mg/L `EDTA`, 80 ng/L `CuSO4`, and 400 ug/L `Na2CO3`.
- TOGO `M3179` records pH 8.5 both in metadata and in the extracted source comment.
- The TOGO comment says ammonia-oxidizing bacteria were grown in NM at 30 C with agitation at 100 r.p.m.
- The generated row values for the three gram-per-liter macronutrients match the source.
- The generated row values for all lower-magnitude source units preserve the numeric token but change the unit to `G_PER_L`.

## Completeness

- pH 8.5 is missing from the generated record.
- The 30 C and 100 r.p.m. ammonia-oxidizing-bacteria growth context is missing from the generated record.
- The normalized owner has the same unit defects as the merged record; this requires a source YAML correction, not only a regenerated merge.
- The generated record has no `preparation_notes`; the source comments contain the concise final-concentration formula and growth conditions.

## Findings

- High: Six source units were coerced to `G_PER_L` without conversion. `CaCl2` should be 22 ug/L but is 22 g/L, `CuSO4` should be 80 ng/L but is 80 g/L, `Na2CO3` should be 400 ug/L but is 400 g/L, `MgSO4` should be 90 mg/L but is 90 g/L, `FeSO4` should be 1.5 mg/L but is 1.5 g/L, and `EDTA` should be 5 mg/L but is 5 g/L.
- Medium: pH 8.5 is available in the TOGO metadata and source comment but absent from the record.
- Medium: The record lacks the source growth context for ammonia-oxidizing bacteria at 30 C with 100 r.p.m. agitation.
- Low: `high_metal: true` is probably derived from the misimported gram-per-liter trace metal concentrations and should be recalculated after the unit repair.

## Recommended Edits

- In `data/normalized_yaml/bacterial/minimal_nitrification_medium_nm.yaml`, convert all non-gram TOGO units to gram-per-liter values or switch them to matching schema units without changing their magnitude.
- Preserve pH 8.5 in the record.
- Add the 30 C and 100 r.p.m. source context where CultureMech stores growth-source notes.
- Remove or recompute `high_metal` after the corrected trace-level concentrations are present.
- Regenerate `data/merge_yaml/merged/minimal_nitrification_medium_nm.yaml` from the normalized source.

## Follow-up Checks

- Re-fetch TOGO `M3179` and verify Ca, Mg, Cu, Na2CO3, Fe, and EDTA magnitudes against the curated YAML.
- Confirm the corrected record no longer trips any concentration-derived high-metal heuristic.
- Re-run open LinkML, strict, reference, and term validation after regeneration.
- The normalized-owner lookup used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.
