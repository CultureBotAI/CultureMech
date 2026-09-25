# YAML Record Review: defined_freshwater_medium_cocl2__3594eb8e

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__3594eb8e.yaml
- Started UTC: 2026-09-22T14:48:14Z
- Finished UTC: 2026-09-22T14:50:42Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007349` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__3594eb8e.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_445_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:445`
- Merge fingerprint:
  `3594eb8e5302216e8e4425fe8fd0ff43be1425c0a047594518e588b75ed3351b`
- Merge shape: single source, `MEDIADB_445_Defined_freshwater_medium_CoCl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__3594eb8e.yaml` | Passed with no issues. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__3594eb8e.yaml --out /private/tmp/defined_freshwater_medium_cocl2__3594eb8e.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__3594eb8e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__3594eb8e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated identity is a single MediaDB 445 source:

- `id: CultureMech:007349`
- `media_term.term.id: MEDIADB:445`
- `merged_from: MEDIADB_445_Defined_freshwater_medium_CoCl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:445` and the exact normalized owner stem found
only the generated record, the maintained owner, and generated indexes.

The public MediaDB 445 page resolves as `Defined freshwater medium (cocl2) +
50 mm iron citrate + 113.2 mm acetate`; its compound table lists
`Fe(III)dicitrate` at 50.0 mM, acetate at 113.2 mM, and one `Boric acid` row.

The generated record is stale relative to its maintained owner. The normalized
`MEDIADB_445_Defined_freshwater_medium_CoCl2.yaml` file has a 2026-08-31
repair event that restores the truncated `'''Fe(III` ingredient to
`Fe(III)dicitrate`, plus a second 2026-08-31 event that restores the full
MediaDB 445 label. The generated record still has the damaged ingredient name
and damaged `original_name` / `media_term.term.label` values.

The maintained owner is also still incomplete: even after the Fe(III)dicitrate
repair, it contains `Boric acid` twice at 0.001617 mM. MediaDB 445 exposes only
one `Boric acid` row.

## Evidence

Supported:

- MediaDB medium 445 denotes the 50 mM iron citrate / 113.2 mM acetate member
  of the CoCl2-defined freshwater medium set; the public page, public
  tab-delimited output, and maintained owner agree on those distinctive
  concentrations once the normalized Fe(III)dicitrate repair is considered.
- The generated recipe has the correct `MEDIADB:445` source identity and a
  single source in `merged_from`.

Unsupported or over-scoped:

- `'''Fe(III` is a parser-damaged ingredient name; the public MediaDB 445 pages
  and repaired normalized owner both identify this row as `Fe(III)dicitrate`
  at 50.0 mM.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- Duplicate `Boric acid` entries are unsupported. The live MediaDB 445 pages
  list `Boric acid` once, but the generated and normalized YAML list it twice.
- The three generic preparation steps are not supported by the inspected
  MediaDB 445 page or its tab-delimited compound export. The public pages do
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 445 links `Geobacter metallireducens`, source 131 (`Lovley dr et al,
  1993`), and growth-data record 832. The generated YAML has no
  `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits both 2026-08-31 MediaDB repair history events
  present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 445 pages did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to repaired ingredient and medium names. | Generated YAML still contains `'''Fe(III` and a truncated MediaDB label; normalized 445 has 2026-08-31 repair events for `Fe(III)dicitrate` and the full `MEDIADB:445` label. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | `Boric acid` is duplicated in both generated and maintained YAML. | MediaDB 445 lists one `Boric acid` row at 0.001617 mM; the YAML includes that ingredient twice at the same concentration. | `data/normalized_yaml/bacterial/MEDIADB_445_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB importer that produced the duplicate row. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 445 pages expose the compound table, organism, source, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_445_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 445 links `Geobacter metallireducens`, source 131, and growth-data 832; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_445_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__3594eb8e.yaml`
  from its normalized source so both 2026-08-31 MediaDB repairs propagate.
- Remove the duplicate `Boric acid` row from the maintained MediaDB 445 owner
  or repair the importer so MediaDB compound rows are not duplicated.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  832, and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 445.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_cocl2__3594eb8e.yaml`.
- Revisit public MediaDB 445 and `/defined_media/media_text/445/` and confirm
  the regenerated record has exactly one `Boric acid` ingredient plus the
  50.0 mM Fe(III)dicitrate and 113.2 mM acetate formulation for `MEDIADB:445`.

## Additional Notes

- Public MediaDB medium 445 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:445` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
