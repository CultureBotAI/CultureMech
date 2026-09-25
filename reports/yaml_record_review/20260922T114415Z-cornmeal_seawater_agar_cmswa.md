# YAML Record Review: Cornmeal Seawater Agar (CMSWA)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/cornmeal_seawater_agar_cmswa.yaml`
- Started UTC: 2026-09-22T11:42:00Z
- Finished UTC: 2026-09-22T11:44:15Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:007956`
- Normalized source: `data/normalized_yaml/bacterial/cornmeal_seawater_agar_cmswa.yaml`
- Source identity: TOGO M1419, `Cornmeal Seawater Agar (CMSWA)`, imported from NBRC Medium 16
- Current generated merge: one source recipe, `cornmeal_seawater_agar_cmswa`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- NBRC Medium 16 and TOGO M1419 specify 2 g cornmeal extract, 1 L seawater at 2% salinity, and 15 g agar.
- The source pH range is 7.0-7.5.
- A gitignore-independent search over `data` found no duplicate NBRC 16 / TOGO M1419 YAML records.
- The normalized owner was repaired on September 11, 2026, but this generated record predates that repair.

## Evidence

- TOGO API checked: `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1419`.
- NBRC source checked: `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=16`.
- Local normalized owner checked: `data/normalized_yaml/bacterial/cornmeal_seawater_agar_cmswa.yaml`.

## Completeness

- The bacterial category, complex undefined type, and solid agar state are appropriate.
- The 2 g/l cornmeal extract and 15 g/l agar concentrations are correct.
- The generated record needs the repaired seawater volume, pH range, and source references from the normalized owner.

## Findings

1. `Seawater (2% Salinity)` is generated as `1 G_PER_L`; NBRC and TOGO list one liter of seawater.
2. The 7.0-7.5 pH range is missing from generated output.
3. The generated record carries TOGO and NBRC URLs only in notes instead of explicit `references`.

## Recommended Edits

1. Regenerate from the already repaired `data/normalized_yaml/bacterial/cornmeal_seawater_agar_cmswa.yaml`.
2. Confirm the generated record preserves `Seawater (2% Salinity)` as `1.0 L`, agar as `15.0 G_PER_L`, and cornmeal extract as `2.0 G_PER_L`.
3. Confirm the regenerated record includes both TOGO M1419 and NBRC Medium 16 references.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Re-check the regenerated pH range and ingredient list against both source pages.

## Additional Notes

- The source record is otherwise internally consistent.
- No source-catalogue duplicate or variant relationship was found.
