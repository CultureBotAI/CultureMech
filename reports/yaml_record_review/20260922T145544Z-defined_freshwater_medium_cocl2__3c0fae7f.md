# YAML Record Review: defined_freshwater_medium_cocl2__3c0fae7f

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__3c0fae7f.yaml
- Started UTC: 2026-09-22T14:52:59Z
- Finished UTC: 2026-09-22T14:55:44Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007370` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__3c0fae7f.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_464_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:464`
- Merge fingerprint:
  `3c0fae7f937ec2c494c58409e92aa554b7cc9b74bd2b4cb3b7fead3259fb5ccc`
- Merge shape: single source, `MEDIADB_464_Defined_freshwater_medium_CoCl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__3c0fae7f.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__3c0fae7f.yaml --out /private/tmp/defined_freshwater_medium_cocl2__3c0fae7f.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__3c0fae7f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__3c0fae7f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated identity is a single MediaDB 464 source:

- `id: CultureMech:007370`
- `media_term.term.id: MEDIADB:464`
- `merged_from: MEDIADB_464_Defined_freshwater_medium_CoCl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:464` and the exact normalized owner stem found
only the generated record, the maintained owner, and generated indexes.

The public MediaDB 464 page resolves as `Defined freshwater medium (cocl2) +
100 mm fe2o3 + 1 mm benzoate`; its compound table lists `Benzoate` at
1.0 mM and ferric oxide at 100.0 mM. The distinctive ingredient and both
concentrations match the generated and maintained YAML.

The generated record is stale relative to its maintained owner. The
normalized `MEDIADB_464_Defined_freshwater_medium_CoCl2.yaml` file has a
2026-08-20 `apply_mim_groundings.py` event that grounds `Benzoate` to
`CHEBI:16150` and a 2026-08-31 `repair_mediadb_names.py` event that restores
the full MediaDB 464 label. The generated record lacks both updates: `Benzoate`
remains ungrounded and `original_name` / `media_term.term.label` are still the
parser-damaged `'''Defined freshwater medium (CoCl2`.

## Evidence

Supported:

- MediaDB medium 464 denotes the 100 mM Fe2O3 / 1 mM benzoate member of the
  CoCl2-defined freshwater medium set; the public page, public tab-delimited
  output, and maintained owner agree on that formula.
- The generated ingredient list preserves `Benzoate` at 1.0 mM and the KEGG
  `bz` cross-reference.
- The maintained owner now carries `CHEBI:16150`, while the MediaDB
  tab-delimited export also exposes a ChEBI cross-reference for the Benzoate
  row.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 464 page or its tab-delimited compound export. The public pages do
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 464 links `Geobacter metallireducens`, source 131 (`Lovley dr et al,
  1993`), and growth-data record 851. The generated YAML has no
  `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-20 MIM grounding event and 2026-08-31
  name-repair event present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 464 pages did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to maintained MediaDB repairs. | Generated `Benzoate` has no `term`, and generated `original_name` / `media_term.term.label` are still truncated; normalized 464 has the 2026-08-20 MIM grounding event, the 2026-08-31 name-repair event, `CHEBI:16150`, and the full MediaDB 464 label. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 464 pages expose the compound table, organism, source, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_464_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 464 links `Geobacter metallireducens`, source 131, and growth-data 851; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_464_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__3c0fae7f.yaml`
  from its normalized source so the 2026-08-20 grounding and 2026-08-31
  MediaDB name repair propagate.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  851, and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 464.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_cocl2__3c0fae7f.yaml`.
- Revisit public MediaDB 464 and `/defined_media/media_text/464/` and confirm
  the regenerated record still contains the 1.0 mM Benzoate and 100.0 mM
  ferric oxide formulation for `MEDIADB:464`.

## Additional Notes

- Public MediaDB medium 464 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:464` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
