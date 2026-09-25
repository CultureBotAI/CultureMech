# YAML Record Review: Cornmeal Yeast Extract Seawater Agar (CMYSWA)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/cornmeal_yeast_extract_seawater_agar_cmyswa.yaml`
- Started UTC: 2026-09-22T11:44:30Z
- Finished UTC: 2026-09-22T11:47:24Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:007963`
- Normalized source: `data/normalized_yaml/bacterial/cornmeal_yeast_extract_seawater_agar_cmyswa.yaml`
- Source identity: TOGO M1425, `Cornmeal Yeast Extract Seawater Agar (CMYSWA)`, imported from NBRC Medium 24
- Current generated merge: one source recipe, `cornmeal_yeast_extract_seawater_agar_cmyswa`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- NBRC Medium 24 and TOGO M1425 specify 2 g cornmeal extract, 1 g yeast extract, 1 L seawater at 2% salinity, and 15 g agar.
- The source pH range is 7.0-7.5.
- A gitignore-independent search over `data` found no duplicate NBRC 24 / TOGO M1425 YAML records.
- The normalized owner was repaired on September 11, 2026, but this generated record predates that repair.

## Evidence

- TOGO API checked: `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1425`.
- NBRC source checked: `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=24`.
- Local normalized owner checked: `data/normalized_yaml/bacterial/cornmeal_yeast_extract_seawater_agar_cmyswa.yaml`.

## Completeness

- The bacterial category, complex undefined type, solid agar state, yeast extract, cornmeal extract, and agar concentration are appropriate.
- The generated record needs the repaired seawater volume, pH range, yeast-extract grounding, and source references from the normalized owner.

## Findings

1. `Seawater (2% salinity)` is generated as `1 G_PER_L`; NBRC and TOGO list one liter of seawater.
2. The 7.0-7.5 pH range is missing from generated output.
3. The generated `Yeast extract` ingredient lacks the FOODON grounding now present in the normalized owner.
4. The generated record carries TOGO and NBRC URLs only in notes instead of explicit `references`.

## Recommended Edits

1. Regenerate from the already repaired `data/normalized_yaml/bacterial/cornmeal_yeast_extract_seawater_agar_cmyswa.yaml`.
2. Confirm the generated record preserves `Seawater (2% salinity)` as `1.0 L`, yeast extract as `1.0 G_PER_L`, agar as `15.0 G_PER_L`, and cornmeal extract as `2.0 G_PER_L`.
3. Confirm the regenerated record includes both TOGO M1425 and NBRC Medium 24 references.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Re-check the regenerated pH range and ingredient list against both source pages.

## Additional Notes

- The source record is otherwise internally consistent.
- No source-catalogue duplicate or variant relationship was found.
