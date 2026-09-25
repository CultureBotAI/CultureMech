# YAML Record Review: defined_freshwater_medium_cocl2__1e8859da

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__1e8859da.yaml
- Started UTC: 2026-09-22T14:43:22Z
- Finished UTC: 2026-09-22T14:45:56Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007374` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__1e8859da.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_468_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:468`
- Merge fingerprint:
  `1e8859dab58ec464546d8535cda5320fc76cc42fb49bce4dd9124fa170a6d691`
- Merge shape: single source, `MEDIADB_468_Defined_freshwater_medium_CoCl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__1e8859da.yaml` | Passed with no issues. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__1e8859da.yaml --out /private/tmp/defined_freshwater_medium_cocl2__1e8859da.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__1e8859da.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__1e8859da.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated identity is a single MediaDB 468 source:

- `id: CultureMech:007374`
- `media_term.term.id: MEDIADB:468`
- `merged_from: MEDIADB_468_Defined_freshwater_medium_CoCl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:468` and the exact normalized owner stem found
only the generated record, the maintained owner, and generated indexes.

The public MediaDB 468 page resolves as `Defined freshwater medium (cocl2) +
100 mm fe2o3 + 0.5 mm p-hydroxybenzaldehyde`; its compound table lists
`4-Hydroxybenzaldehyde` at 0.5 mM and ferric oxide at 100.0 mM. The distinctive
ingredient and both concentrations match the generated and maintained YAML.

The generated record is stale relative to its maintained owner. The
normalized `MEDIADB_468_Defined_freshwater_medium_CoCl2.yaml` file has a
2026-08-20 `apply_mim_groundings.py` event that grounds
`4-Hydroxybenzaldehyde` to `CHEBI:17597` and a 2026-08-31
`repair_mediadb_names.py` event that restores the full MediaDB 468 label. The
generated record lacks both updates: its distinctive ingredient remains
ungrounded and its `original_name` / `media_term.term.label` are still the
parser-damaged `'''Defined freshwater medium (CoCl2`.

## Evidence

Supported:

- MediaDB medium 468 denotes the 100 mM Fe2O3 / 0.5 mM
  p-hydroxybenzaldehyde member of the CoCl2-defined freshwater medium set; the
  public page, public tab-delimited output, and maintained owner agree on that
  formula.
- The generated ingredient list preserves `4-Hydroxybenzaldehyde` at 0.5 mM
  and the KEGG `4hbald` cross-reference.
- MediaDB's tab-delimited export lists ChEBI 17597 for
  `4-Hydroxybenzaldehyde`, matching the maintained owner's curated
  `CHEBI:17597` grounding.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 468 page or its tab-delimited compound export. The public pages do
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 468 links `Geobacter metallireducens`, source 131 (`Lovley dr et al,
  1993`), and growth-data record 855. The generated YAML has no
  `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-20 MIM grounding event and 2026-08-31
  name-repair event present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 468 pages did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to maintained MediaDB repairs. | Generated `original_name` and `media_term.term.label` are still truncated, and generated `4-Hydroxybenzaldehyde` has no `term`; normalized 468 has the 2026-08-20 MIM grounding event, the 2026-08-31 name-repair event, the full MediaDB 468 label, and `CHEBI:17597`. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 468 pages expose the compound table, organism, source, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_468_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 468 links `Geobacter metallireducens`, source 131, and growth-data 855; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_468_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__1e8859da.yaml`
  from its normalized source so the 2026-08-20 grounding and 2026-08-31
  MediaDB name repair propagate.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  855, and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 468.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_cocl2__1e8859da.yaml`.
- Revisit public MediaDB 468 and `/defined_media/media_text/468/` and confirm
  the regenerated record still contains the 0.5 mM 4-Hydroxybenzaldehyde and
  100.0 mM ferric oxide formulation for `MEDIADB:468`.

## Additional Notes

- Public MediaDB medium 468 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:468` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
