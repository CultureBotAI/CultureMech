# YAML Record Review: defined_freshwater_medium_cocl2__5fdd46bf

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__5fdd46bf.yaml
- Started UTC: 2026-09-22T14:55:45Z
- Finished UTC: 2026-09-22T14:58:47Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007359` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__5fdd46bf.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_454_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:454`
- Merge fingerprint:
  `5fdd46bffaf9eaa8d69685fefc21efc952b05387d9b19fccd1571385e3fbc724`
- Merge shape: single source, `MEDIADB_454_Defined_freshwater_medium_CoCl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__5fdd46bf.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__5fdd46bf.yaml --out /private/tmp/defined_freshwater_medium_cocl2__5fdd46bf.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__5fdd46bf.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__5fdd46bf.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated identity is a single MediaDB 454 source:

- `id: CultureMech:007359`
- `media_term.term.id: MEDIADB:454`
- `merged_from: MEDIADB_454_Defined_freshwater_medium_CoCl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:454` and the exact normalized owner stem found
only the generated record, the maintained owner, and generated indexes.

The public MediaDB 454 page resolves as `Defined freshwater medium (cocl2) +
100 mm fe2o3 + 20 mm butyrate`; its compound table lists `Butanoic acid` at
20.0 mM and ferric oxide at 100.0 mM. The distinctive ingredient and both
concentrations match the generated and maintained YAML.

The generated record is stale relative to its maintained owner. The
normalized `MEDIADB_454_Defined_freshwater_medium_CoCl2.yaml` file has a
2026-08-31 `repair_mediadb_names.py` event and the restored
`Defined freshwater medium (CoCl2) + 100 mM Fe2O3 + 20 mM Butyrate` label, but
the generated record still carries the older parser-damaged
`'''Defined freshwater medium (CoCl2` in both `original_name` and
`media_term.term.label`.

## Evidence

Supported:

- MediaDB medium 454 denotes the 100 mM Fe2O3 / 20 mM butyrate member of the
  CoCl2-defined freshwater medium set; the public page, public tab-delimited
  output, and maintained owner agree on that formula.
- The generated ingredient list preserves `Butanoic acid` at 20.0 mM with
  `CHEBI:30772` and the KEGG `but` cross-reference.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 454 page or its tab-delimited compound export. The public pages do
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 454 links `Geobacter metallireducens`, source 131 (`Lovley dr et al,
  1993`), and growth-data record 841. The generated YAML has no
  `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-31 name-repair history event present
  on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 454 pages did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MediaDB name repair. | Generated `original_name` and `media_term.term.label` still contain `'''Defined freshwater medium (CoCl2`; the normalized owner has the 2026-08-31 repair event and the full MediaDB 454 label. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 454 pages expose the compound table, organism, source, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_454_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 454 links `Geobacter metallireducens`, source 131, and growth-data 841; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_454_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__5fdd46bf.yaml`
  from its normalized source so the 2026-08-31 MediaDB name repair propagates.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  841, and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 454.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_cocl2__5fdd46bf.yaml`.
- Revisit public MediaDB 454 and `/defined_media/media_text/454/` and confirm
  the regenerated record still contains the 20.0 mM Butanoic acid and 100.0 mM
  ferric oxide formulation for `MEDIADB:454`.

## Additional Notes

- Public MediaDB medium 454 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:454` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
