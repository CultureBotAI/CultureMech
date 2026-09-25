# YAML Record Review: defined_freshwater_medium_cocl2__66450107

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__66450107.yaml
- Started UTC: 2026-09-22T15:03:01Z
- Finished UTC: 2026-09-22T15:03:01Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007378` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__66450107.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_471_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:471`
- Merge fingerprint:
  `66450107231ec08346e3901ecb86cfc3f56ab6f6a298db7df54e52904a2b16c0`
- Merge shape: single source, `MEDIADB_471_Defined_freshwater_medium_CoCl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__66450107.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__66450107.yaml --out /private/tmp/defined_freshwater_medium_cocl2__66450107.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__66450107.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__66450107.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated identity is a single MediaDB 471 source:

- `id: CultureMech:007378`
- `media_term.term.id: MEDIADB:471`
- `merged_from: MEDIADB_471_Defined_freshwater_medium_CoCl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:471` and the exact normalized owner stem found
only the generated record, the maintained owner, and generated indexes.

The public MediaDB 471 page resolves as `Defined freshwater medium (cocl2) +
100 mm fe2o3 + 0.5 mm benzaldehyde`; its compound table lists `Benzaldehyde`
at 0.5 mM and `Ferric oxide` at 100.0 mM. The distinctive ingredient and both
concentrations match the generated and maintained YAML.

The generated record is stale relative to its maintained owner. The
normalized `MEDIADB_471_Defined_freshwater_medium_CoCl2.yaml` file has a
2026-08-31 `repair_mediadb_names.py` event and the restored
`Defined freshwater medium (CoCl2) + 100 mM Fe2O3 + 0.5 mM Benzaldehyde`
label, but the generated record still carries the older parser-damaged
`'''Defined freshwater medium (CoCl2` in both `original_name` and
`media_term.term.label`.

## Evidence

Supported:

- MediaDB medium 471 denotes the 100 mM Fe2O3 / 0.5 mM benzaldehyde member of
  the CoCl2-defined freshwater medium set; the public page, public
  tab-delimited output, and maintained owner agree on that formula.
- The generated ingredient list preserves `Benzaldehyde` at 0.5 mM and
  `Ferric oxide` at 100.0 mM.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- `Benzaldehyde` is ungrounded despite the MediaDB tab-delimited export
  carrying KEGG `bzal`, ModelSEED `cpd00225`, and ChEBI `17169`
  cross-references for that ingredient.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 471 page or its tab-delimited compound export. The public pages do
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 471 links `Geobacter metallireducens`, source 131 (`Lovley dr et al,
  1993`), and growth-data record 858. The generated YAML has no
  `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-31 name-repair history event present
  on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 471 pages did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MediaDB name repair. | Generated `original_name` and `media_term.term.label` still contain `'''Defined freshwater medium (CoCl2`; the normalized owner has the 2026-08-31 repair event and the full MediaDB 471 label. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 471 pages expose the compound table, organism, source, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_471_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 471 links `Geobacter metallireducens`, source 131, and growth-data 858; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_471_Defined_freshwater_medium_CoCl2.yaml`. |
| Minor | `Benzaldehyde` is ungrounded. | The generated and maintained ingredient has no `term` or `mediaingredientmech_chebi_term`, while MediaDB's tab-delimited export carries ChEBI `17169` for that same 0.5 mM ingredient row. | MediaDB chemical-mapping enrichment for `data/normalized_yaml/bacterial/MEDIADB_471_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__66450107.yaml`
  from its normalized source so the 2026-08-31 MediaDB name repair propagates.
- Ground `Benzaldehyde` to `CHEBI:17169` if an OAK verification confirms that
  the live ChEBI label and MediaDB cross-reference identify the same compound.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  858, and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 471.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_cocl2__66450107.yaml`.
- Revisit public MediaDB 471 and `/defined_media/media_text/471/` and confirm
  the regenerated record still contains the 0.5 mM Benzaldehyde and 100.0 mM
  Ferric oxide formulation for `MEDIADB:471`.

## Additional Notes

- Public MediaDB medium 471 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:471` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
