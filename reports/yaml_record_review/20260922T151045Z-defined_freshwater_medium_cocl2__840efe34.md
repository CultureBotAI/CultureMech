# YAML Record Review: defined_freshwater_medium_cocl2__840efe34

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__840efe34.yaml
- Started UTC: 2026-09-22T15:10:45Z
- Finished UTC: 2026-09-22T15:10:45Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007366` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__840efe34.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_460_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:460`
- Merge fingerprint:
  `840efe348eab84ef470d799694f5bec40e4c0991e6466e5d725d4a969a72242f`
- Merge shape: single source, `MEDIADB_460_Defined_freshwater_medium_CoCl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__840efe34.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__840efe34.yaml --out /private/tmp/defined_freshwater_medium_cocl2__840efe34.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__840efe34.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__840efe34.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated identity is a single MediaDB 460 source:

- `id: CultureMech:007366`
- `media_term.term.id: MEDIADB:460`
- `merged_from: MEDIADB_460_Defined_freshwater_medium_CoCl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:460` and the exact normalized owner stem found
only the generated record, the maintained owner, and generated indexes.

The public MediaDB 460 page resolves as `Defined freshwater medium (cocl2) +
100 mm fe2o3 + 10 mm isovalerate`; its compound table lists
`3-Methylbutanoic acid` at 10.0 mM and `Ferric oxide` at 100.0 mM. The
maintained and generated YAML match the MediaDB identity but not the
MediaDB compound table.

The generated record is stale relative to its maintained owner. The
normalized `MEDIADB_460_Defined_freshwater_medium_CoCl2.yaml` file has a
2026-08-31 `repair_mediadb_names.py` event and the restored
`Defined freshwater medium (CoCl2) + 100 mM Fe2O3 + 10 mM Isovalerate` label,
but the generated record still carries the older parser-damaged
`'''Defined freshwater medium (CoCl2` in both `original_name` and
`media_term.term.label`.

## Evidence

Supported:

- MediaDB medium 460 denotes the 100 mM Fe2O3 / 10 mM isovalerate member of
  the CoCl2-defined freshwater medium set.
- The generated ingredient list preserves the shared CoCl2-defined freshwater
  salts, trace metals, and vitamin rows, including `Ferric oxide` at 100.0 mM.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- The `3-Methylbutanoic acid` ingredient at 10.0 mM from MediaDB 460 is
  missing from both the generated record and the normalized owner.
- The generated and normalized records carry LB Miller constituents
  `Tryptone`, `Yeast extract`, and 10.0 g/L `Sodium chloride`, plus
  `medium_type: COMPLEX` and `composition_type: UNDEFINED`; the inspected
  MediaDB 460 page and tab-delimited export expose a 29-compound formulation
  without those LB rows.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 460 page or its tab-delimited compound export. The public pages do
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 460 links `Geobacter metallireducens`, source 131 (`Lovley dr et al,
  1993`), and growth-data record 847. The generated YAML has no
  `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-31 name-repair history event present
  on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 460 pages did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The MediaDB 460 formula was overwritten with unsupported LB Miller constituents. | Public MediaDB 460 lists 3-Methylbutanoic acid at 10.0 mM and no `Tryptone`, `Yeast extract`, or 10.0 g/L Sodium chloride rows; the maintained and generated YAML omit 3-Methylbutanoic acid, add those LB rows, and classify the record as complex/undefined. | `data/normalized_yaml/bacterial/MEDIADB_460_Defined_freshwater_medium_CoCl2.yaml` or the product-enrichment logic that added LB constituents. |
| Major | The generated record is stale relative to the maintained MediaDB name repair. | Generated `original_name` and `media_term.term.label` still contain `'''Defined freshwater medium (CoCl2`; the normalized owner has the 2026-08-31 repair event and the full MediaDB 460 label. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 460 pages expose the compound table, organism, source, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_460_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 460 links `Geobacter metallireducens`, source 131, and growth-data 847; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_460_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Restore MediaDB 460 as a defined CoCl2 freshwater formula with 10.0 mM
  `3-Methylbutanoic acid`; remove the unrelated LB Miller constituent rows and
  product note from
  `data/normalized_yaml/bacterial/MEDIADB_460_Defined_freshwater_medium_CoCl2.yaml`.
- Reclassify the owner as `medium_type: DEFINED` and
  `composition_type: DEFINED` after removing the unsupported complex
  constituents.
- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__840efe34.yaml`
  from its repaired normalized source so the formula and 2026-08-31 MediaDB
  name repair propagate.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  847, and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 460.

## Follow-up Checks

- Search for the same LB Miller product-enrichment pattern across the other
  MediaDB CoCl2 normalized records before regenerating.
- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_cocl2__840efe34.yaml`.
- Revisit public MediaDB 460 and `/defined_media/media_text/460/` and confirm
  the regenerated record contains the 10.0 mM `3-Methylbutanoic acid` and
  100.0 mM `Ferric oxide` formulation for `MEDIADB:460`.

## Additional Notes

- Public MediaDB medium 460 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:460` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
