# YAML Record Review: defined_freshwater_medium_coso4__0930ab53

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4__0930ab53.yaml
- Started UTC: 2026-09-22T15:39:43Z
- Finished UTC: 2026-09-22T15:39:43Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007346` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4__0930ab53.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_442_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:442`
- Merge fingerprint:
  `0930ab531cb11f7559e0f34fe642cf3cc6e2a494d62d2aaff5c24c3000ec3bb3`
- Merge shape: single source, `MEDIADB_442_Defined_freshwater_medium_CoSO4`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4__0930ab53.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4__0930ab53.yaml --out /private/tmp/defined_freshwater_medium_coso4__0930ab53.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4__0930ab53.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4__0930ab53.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is a single-source MediaDB 442 import with no variant or
duplicate sources:

- `id: CultureMech:007346`
- `media_term.term.id: MEDIADB:442`
- `ingredients` includes `Ferric oxide` at `100.0` mM and `Phenol` at
  `0.5` mM
- `merged_from: MEDIADB_442_Defined_freshwater_medium_CoSO4`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:442` and
`MEDIADB_442_Defined_freshwater_medium_CoSO4` found only the maintained owner,
this generated record, and generated indexes.

The public MediaDB 442 page resolves as `Defined freshwater medium (coso4) +
100 mm fe2o3 + 0.5 mm phenol`; its tab-delimited export lists `Ferric oxide`
at 100.0 mM and `Phenol` at 0.5 mM. The generated and maintained records both
preserve the 0.5 mM phenol row and ground it to `CHEBI:15882`.

The generated record is stale relative to its maintained owner. The owner has
a 2026-08-31 MediaDB-name repair event that restored
`Defined freshwater medium (CoSO4) + 100 mM Fe2O3 + 0.5 mM Phenol`, while the
generated record still has the old truncated `original_name` and
`media_term.term.label`.

## Evidence

Supported:

- MediaDB medium 442 denotes the CoSO4-defined freshwater medium plus 100.0 mM
  ferric oxide and 0.5 mM phenol; the public page, public tab-delimited
  output, and maintained owner agree on those distinctive ingredient rows.
- The generated ingredient list preserves the 0.5 mM phenol row that
  distinguishes MediaDB 442 from the CoSO4 ferric oxide and acetate variants.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- The generated record's `original_name` and `media_term.term.label` are stale
  values that no longer match the maintained normalized record or the live
  MediaDB page.
- The generated and maintained `Ferric oxide` row is ungrounded even though the
  public MediaDB export exposes a direct CheBI cross-reference, `50819`, for
  ferric oxide.
- The three generic preparation steps are not supported by the inspected
  MediaDB 442 page or its tab-delimited compound export. The public page does
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 442 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 829. The generated YAML
  has no `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-31 MediaDB-name repair history event
  present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 442 page did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MediaDB name repair. | Generated `original_name` and `media_term.term.label` still contain the old truncated label; the normalized owner has a 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` event with the full name. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Ferric oxide is missing a source-supported ontology grounding. | MediaDB 442 publishes a ferric oxide CheBI cross-reference of `50819`; the generated and maintained `Ferric oxide` ingredient entries have no `term`. | Add or repair ferric oxide grounding in `data/normalized_yaml/bacterial/MEDIADB_442_Defined_freshwater_medium_CoSO4.yaml` or in the MediaDB import/enrichment path that reads source CheBI IDs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 442 page exposes a compound table, organism link, source link, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_442_Defined_freshwater_medium_CoSO4.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 442 links `Geobacter metallireducens`, source 131, and growth-data 829; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_442_Defined_freshwater_medium_CoSO4.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_coso4__0930ab53.yaml`
  from its normalized source so the 2026-08-31 MediaDB-name repair propagates.
- Ground `Ferric oxide` from MediaDB's CheBI `50819` in
  `data/normalized_yaml/bacterial/MEDIADB_442_Defined_freshwater_medium_CoSO4.yaml`
  or in the MediaDB ingredient import/enrichment path.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data 829,
  and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 442.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_coso4__0930ab53.yaml`.
- Revisit public MediaDB 442 and `/defined_media/media_text/442/` and confirm
  the regenerated record has the full MediaDB 442 label, a ferric oxide term,
  and no unsupported generic pH or filter-sterilization steps.

## Additional Notes

- Public MediaDB medium 442 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:442` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
