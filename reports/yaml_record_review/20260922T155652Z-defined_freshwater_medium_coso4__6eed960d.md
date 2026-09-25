# YAML Record Review: defined_freshwater_medium_coso4__6eed960d

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4__6eed960d.yaml
- Started UTC: 2026-09-22T15:56:52Z
- Finished UTC: 2026-09-22T15:56:52Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007322` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4__6eed960d.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_420_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:420`
- Merge fingerprint:
  `6eed960d96f47c49cdc123f2852f7c68b11c0608bac94174bfe40606790f53ae`
- Merge shape: single source, `MEDIADB_420_Defined_freshwater_medium_CoSO4`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4__6eed960d.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4__6eed960d.yaml --out /private/tmp/defined_freshwater_medium_coso4__6eed960d.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4__6eed960d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4__6eed960d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is a single-source MediaDB 420 import with no variant or
duplicate sources:

- `id: CultureMech:007322`
- `media_term.term.id: MEDIADB:420`
- `ingredients` includes `'''Fe(III` at `50.0` mM and `Acetate` at
  `113.2` mM
- `merged_from: MEDIADB_420_Defined_freshwater_medium_CoSO4`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:420` and
`MEDIADB_420_Defined_freshwater_medium_CoSO4` found only the maintained owner,
this generated record, and generated indexes.

The public MediaDB 420 page resolves as `Defined freshwater medium (coso4) +
50 mm iron citrate + 113.2 mm acetate`; its tab-delimited export lists
`Fe(III)dicitrate` at 50.0 mM and `Acetate` at 113.2 mM.

The generated record is stale relative to its maintained owner. The owner has
a 2026-08-31 ingredient repair event that restored `Fe(III)dicitrate` and a
2026-08-31 MediaDB-name repair event that restored the full MediaDB 420 name;
the generated record has neither update.

## Evidence

Supported:

- MediaDB medium 420 denotes the CoSO4-defined freshwater medium plus 50.0 mM
  iron citrate and 113.2 mM acetate; the public page, public tab-delimited
  output, and maintained owner agree on those distinctive ingredient rows.
- The generated ingredient list preserves the 50.0 mM Fe(III)dicitrate row
  that distinguishes MediaDB 420 from the 100 mM Fe2O3 plus acetate variants.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- The generated record still carries `'''Fe(III` instead of the maintained
  owner's repaired `Fe(III)dicitrate` ingredient name.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 420 page or its tab-delimited compound export. The public page does
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 420 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 807. The generated YAML
  has no `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits both 2026-08-31 MediaDB repair history events
  present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 420 page did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained Fe(III)dicitrate and medium-label repairs. | Generated `'''Fe(III`, `original_name`, and `media_term.term.label` still contain the old parser-damaged values; the normalized owner has two 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` events covering those fixes. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 420 page exposes a compound table, organism link, source link, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_420_Defined_freshwater_medium_CoSO4.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 420 links `Geobacter metallireducens`, source 131, and growth-data 807; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_420_Defined_freshwater_medium_CoSO4.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_coso4__6eed960d.yaml`
  from its normalized source so the 2026-08-31 Fe(III)dicitrate and medium-name
  repairs propagate.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data 807,
  and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 420.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_coso4__6eed960d.yaml`.
- Revisit public MediaDB 420 and `/defined_media/media_text/420/` and confirm
  the regenerated record has the 50.0 mM Fe(III)dicitrate row, the full
  MediaDB 420 label, and no unsupported generic pH or filter-sterilization
  steps.

## Additional Notes

- Public MediaDB medium 420 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:420` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
