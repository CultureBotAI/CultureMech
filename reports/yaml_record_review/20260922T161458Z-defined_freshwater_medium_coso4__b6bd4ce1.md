# YAML Record Review: defined_freshwater_medium_coso4__b6bd4ce1

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4__b6bd4ce1.yaml
- Started UTC: 2026-09-22T16:14:58Z
- Finished UTC: 2026-09-22T16:14:58Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007320` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4__b6bd4ce1.yaml`
- Maintained owners:
  `data/normalized_yaml/bacterial/MEDIADB_419_Defined_freshwater_medium_CoSO4.yaml`
  and
  `data/normalized_yaml/bacterial/MEDIADB_421_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identities: `MEDIADB:419`, `MEDIADB:421`
- Merge fingerprint:
  `b6bd4ce1bc6d342d2c6c86871b0da08b2c2756a9b3b45435969b326d522bd3e3`
- Merge shape: two sources,
  `MEDIADB_419_Defined_freshwater_medium_CoSO4` and
  `MEDIADB_421_Defined_freshwater_medium_CoSO4`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4__b6bd4ce1.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4__b6bd4ce1.yaml --out /private/tmp/defined_freshwater_medium_coso4__b6bd4ce1.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4__b6bd4ce1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0 and 0 checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4__b6bd4ce1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record incorrectly merged two MediaDB imports that are explicitly
related as concentration variants:

- `id: CultureMech:007320`
- `media_term.term.id: MEDIADB:419`
- `merged_from` includes `MEDIADB_419_Defined_freshwater_medium_CoSO4` and
  `MEDIADB_421_Defined_freshwater_medium_CoSO4`
- `variant_children` points at the MediaDB 421 owner and notes that nitrate
  increased from 5 mM to 20 mM.

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:419`, `MEDIADB:421`, and their two
`MEDIADB_*_Defined_freshwater_medium_CoSO4` owner stems found the two
maintained owners, this generated record, and generated indexes.

The public MediaDB 419 page resolves as `Defined freshwater medium (coso4) +
5 mm nitrate + 113.2 mm acetate`; its tab-delimited export lists `Nitrate` at
5.0 mM. The public MediaDB 421 page resolves as `Defined freshwater medium
(coso4) + 20 mm nitrate + 113.2 mm acetate`; its tab-delimited export lists
`Nitrate` at 20.0 mM. Collapsing them under one merge fingerprint erases that
source-level concentration difference.

The generated record is also stale relative to both maintained owners. The
owners have 2026-08-20 MIM grounding events that ground `Nitrate` and
2026-08-31 MediaDB-name repair events that restored their full source labels;
the generated merge still has an ungrounded `Nitrate` row plus the old
truncated `original_name` and `media_term.term.label`.

## Evidence

Supported:

- The 5.0 mM `Nitrate` and 113.2 mM `Acetate` rows in the generated record
  match the MediaDB 419 formula.
- The generated record correctly preserves MediaDB 421 as a
  `CONCENTRATION_VARIANT` child of MediaDB 419.

Unsupported or over-scoped:

- `MEDIADB:419` and `MEDIADB:421` are not duplicates: public MediaDB exposes
  distinct 5.0 mM and 20.0 mM nitrate formulas, and the maintained owners
  preserve that concentration difference.
- The generated record's `original_name`, `media_term.term.label`, and
  ungrounded `Nitrate` ingredient are stale relative to both maintained
  normalized records.
- The three generic preparation steps are not supported by the inspected
  MediaDB 419/421 pages or their tab-delimited compound exports. The public
  pages do not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 419 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 806; MediaDB 421 links
  `Geobacter metallireducens`, source 131, and growth-data record 808. The
  generated YAML has no `target_organisms`, organism-scoped growth evidence,
  or Lovley source reference for either MediaDB formula.
- The generated merge omits the 2026-08-20 nitrate grounding and 2026-08-31
  MediaDB-name repair history events present on the normalized owners.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 419 and 421 pages did not
  expose those protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Distinct 5 mM and 20 mM nitrate formulas were false-merged as duplicates. | Public MediaDB 419 lists 5.0 mM nitrate; public MediaDB 421 lists 20.0 mM nitrate; the maintained owners also encode the two recipes as concentration variants, not duplicates. | Fix the merge-key or duplicate-collapse logic that produced `data/merge_yaml/merged/defined_freshwater_medium_coso4__b6bd4ce1.yaml` so concentration variants remain separate generated records. |
| Major | The generated record is stale relative to the maintained MIM nitrate grounding and MediaDB name repairs. | The generated `Nitrate` row is ungrounded and its `original_name`/`media_term.term.label` still contain the old truncated label; both normalized owners have 2026-08-20 MIM grounding events and 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` events. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 419/421 pages expose compound tables, organism links, source links, and growth-data links, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_419_Defined_freshwater_medium_CoSO4.yaml`, `data/normalized_yaml/bacterial/MEDIADB_421_Defined_freshwater_medium_CoSO4.yaml`, or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 419 links growth-data 806 and MediaDB 421 links growth-data 808, both for `Geobacter metallireducens` and source 131; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns both normalized MediaDB records. |

## Recommended Edits

- Fix the merge-key or duplicate-collapse logic so MediaDB 419 and 421 remain
  separate generated recipes linked only by their `CONCENTRATION_VARIANT`
  relationship.
- Regenerate `data/merge_yaml/merged/` from the normalized sources so the
  2026-08-20 nitrate groundings and 2026-08-31 MediaDB-name repairs propagate.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for these two media.
- Extend the MediaDB owners or importer to preserve source 131 and the two
  inspected growth-data records with evidence scoped to MediaDB 419 and 421.

## Follow-up Checks

- Re-run `just verify-merges` and `just audit-merge-freshness` after repairing
  merge behavior and regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on the
  regenerated MediaDB 419 and MediaDB 421 merge outputs.
- Revisit public MediaDB 419/421 and their `/defined_media/media_text/` exports
  and confirm generated records preserve the 5.0 mM versus 20.0 mM nitrate
  difference, the full MediaDB labels, grounded nitrate, and no unsupported
  generic pH or filter-sterilization steps.

## Additional Notes

- Public MediaDB media 419 and 421 and their tab-delimited exports were
  reachable during review.
- The bounded `MEDIADB:419`/`MEDIADB:421` source-owner search included ignored
  files in `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
