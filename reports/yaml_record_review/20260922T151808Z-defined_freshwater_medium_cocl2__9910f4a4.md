# YAML Record Review: defined_freshwater_medium_cocl2__9910f4a4

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__9910f4a4.yaml
- Started UTC: 2026-09-22T15:18:08Z
- Finished UTC: 2026-09-22T15:18:08Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007355` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__9910f4a4.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_450_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:450`
- Merge fingerprint:
  `9910f4a4d232ae1542c298363372b1ece1bfe32652c0c33f4cf2ad1216916f04`
- Merge shape: single source, `MEDIADB_450_Defined_freshwater_medium_CoCl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__9910f4a4.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__9910f4a4.yaml --out /private/tmp/defined_freshwater_medium_cocl2__9910f4a4.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__9910f4a4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__9910f4a4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated identity is a single MediaDB 450 source:

- `id: CultureMech:007355`
- `media_term.term.id: MEDIADB:450`
- `merged_from: MEDIADB_450_Defined_freshwater_medium_CoCl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:450` and the exact normalized owner stem found
only the generated record, the maintained owner, and generated indexes.

The public MediaDB 450 page resolves as `Defined freshwater medium (cocl2) +
15 mm mno2 + 113.2 mm acetate`; its compound table lists `Acetate` at
113.2 mM, `Manganese(IV) oxide` at 15.0 mM, and `Ferric oxide` at
100.0 mM. Those distinctive ingredients and concentrations are present in the
maintained YAML; the generated record preserves the 15.0 mM manganese oxide
row only as parser-damaged `'''Manganese(IV`.

The generated record is stale relative to its maintained owner. The
normalized `MEDIADB_450_Defined_freshwater_medium_CoCl2.yaml` file has a
2026-08-31 ingredient repair event that restored `Manganese(IV) oxide` and a
2026-08-31 medium-name repair event that restored
`Defined freshwater medium (CoCl2) + 15 mM MnO2 + 113.2 mM Acetate`; the
generated record still carries the older parser-damaged ingredient and
medium-label values.

## Evidence

Supported:

- MediaDB medium 450 denotes the 15 mM MnO2 / 113.2 mM acetate member of the
  CoCl2-defined freshwater medium set; the public page, public tab-delimited
  output, and maintained owner agree on that formula.
- The generated ingredient list preserves `Acetate` at 113.2 mM and a damaged
  15.0 mM manganese oxide row corresponding to the maintained owner's
  `Manganese(IV) oxide`.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- The generated record still carries `'''Manganese(IV` instead of the
  maintained owner's repaired `Manganese(IV) oxide` ingredient name.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 450 page or its tab-delimited compound export. The public pages do
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 450 links `Geobacter metallireducens`, source 131 (`Lovley dr et al,
  1993`), and growth-data record 837. The generated YAML has no
  `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits both 2026-08-31 repair events present on its
  normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 450 pages did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MediaDB ingredient and name repairs. | Generated `original_name`, `media_term.term.label`, and the manganese oxide ingredient still contain parser-damaged values; the normalized owner has 2026-08-31 repair events for `Manganese(IV) oxide` and the full MediaDB 450 label. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 450 pages expose the compound table, organism, source, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_450_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 450 links `Geobacter metallireducens`, source 131, and growth-data 837; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_450_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__9910f4a4.yaml`
  from its normalized source so the 2026-08-31 MediaDB ingredient and name
  repairs propagate.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  837, and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 450.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_cocl2__9910f4a4.yaml`.
- Revisit public MediaDB 450 and `/defined_media/media_text/450/` and confirm
  the regenerated record still contains the 113.2 mM Acetate, 15.0 mM
  Manganese(IV) oxide, and 100.0 mM Ferric oxide formulation for
  `MEDIADB:450`.

## Additional Notes

- Public MediaDB medium 450 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:450` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
