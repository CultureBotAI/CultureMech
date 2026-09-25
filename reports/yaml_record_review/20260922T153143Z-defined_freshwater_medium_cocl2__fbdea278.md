# YAML Record Review: defined_freshwater_medium_cocl2__fbdea278

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__fbdea278.yaml
- Started UTC: 2026-09-22T15:31:43Z
- Finished UTC: 2026-09-22T15:31:43Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007350` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__fbdea278.yaml`
- Maintained owners:
  `data/normalized_yaml/bacterial/MEDIADB_446_Defined_freshwater_medium_CoCl2.yaml`
  and
  `data/normalized_yaml/bacterial/MEDIADB_448_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identities: `MEDIADB:446` and `MEDIADB:448`
- Merge fingerprint:
  `fbdea2788324ad006e977b266f8b620790c3c2bf04900c4107532ebae344b3b9`
- Merge shape: two MediaDB records merged as duplicates, with
  `MEDIADB_448_Defined_freshwater_medium_CoCl2` also retained as a
  concentration variant child

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__fbdea278.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__fbdea278.yaml --out /private/tmp/defined_freshwater_medium_cocl2__fbdea278.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__fbdea278.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__fbdea278.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is anchored on MediaDB 446 and its 5.0 mM nitrate
formulation:

- `id: CultureMech:007350`
- `media_term.term.id: MEDIADB:446`
- `ingredients` includes `Nitrate` at `5.0` mM
- `merged_from` lists both `MEDIADB_446_Defined_freshwater_medium_CoCl2` and
  `MEDIADB_448_Defined_freshwater_medium_CoCl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:446`, `MEDIADB:448`,
`MEDIADB_446_Defined_freshwater_medium_CoCl2`, and
`MEDIADB_448_Defined_freshwater_medium_CoCl2` found only the two maintained
owners, this generated record, and generated indexes.

The public MediaDB tab-delimited exports distinguish the two source media:
medium 446 is `Defined freshwater medium (cocl2) + 5 mm nitrate + 113.2 mm
acetate`, while medium 448 is `Defined freshwater medium (cocl2) + 20 mm
nitrate + 113.2 mm acetate`. Both exports list the same 29 compound names and
amounts except for the `Nitrate` row: 5.0 mM in 446 and 20.0 mM in 448.

The maintained owners preserve that distinction. The 446 owner has 5.0 mM
`Nitrate`, the 448 owner has 20.0 mM `Nitrate`, both owners ground that row to
`CHEBI:17632`, and the 448 owner declares the nitrate increase as a
`CONCENTRATION_VARIANT` of 446. The generated record is stale relative to both
owners because its `Nitrate` row has no `term`, and its `original_name` and
`media_term.term.label` still contain the earlier truncated
`'Defined freshwater medium (CoCl2` label.

## Evidence

Supported:

- MediaDB medium 446 denotes the CoCl2-defined freshwater medium plus 5.0 mM
  nitrate and 113.2 mM acetate; the public page, public tab-delimited output,
  and maintained owner agree on those two distinctive concentration rows.
- MediaDB medium 448 denotes the CoCl2-defined freshwater medium plus 20.0 mM
  nitrate and 113.2 mM acetate; the public page, public tab-delimited output,
  and maintained owner agree on those two distinctive concentration rows.
- The generated record's canonical ingredient list matches medium 446 rather
  than medium 448 by preserving the 5.0 mM nitrate row.

Unsupported or over-scoped:

- The generated duplicate merge is unsupported. MediaDB 446 and MediaDB 448
  are concentration variants with different nitrate concentrations, not
  identical records that should both be in `merged_from` for one fingerprint.
- The generated `Nitrate` ingredient is ungrounded even though both maintained
  owners now ground nitrate to `CHEBI:17632` and the public MediaDB exports
  include a CheBI cross-reference for nitrate.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized records or the live MediaDB pages.
- The three generic preparation steps are not supported by the inspected
  MediaDB 446 or 448 pages or their tab-delimited compound exports. The public
  pages do not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 446 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 833. The generated YAML
  has no `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference for the 5.0 mM nitrate variant.
- MediaDB 448 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 835. The generated YAML
  has no organism-scoped growth evidence that would preserve that 20.0 mM
  nitrate variant.
- The generated merge omits the 2026-08-20 MIM nitrate grounding and 2026-08-31
  name-repair history events present on the maintained owners.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 446 and 448 pages did not
  expose those protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | MediaDB 446 and 448 were merged as duplicates even though they differ in nitrate concentration. | The public MediaDB exports list 5.0 mM nitrate for 446 and 20.0 mM nitrate for 448, and the maintained 448 owner already declares `Nitrate increased from 5 mM to 20 mM`. | Merge generation from `data/normalized_yaml/bacterial/MEDIADB_446_Defined_freshwater_medium_CoCl2.yaml` and `data/normalized_yaml/bacterial/MEDIADB_448_Defined_freshwater_medium_CoCl2.yaml`; keep the concentration-variant edge but do not collapse both source records into one duplicate merge. |
| Major | The generated record is stale relative to the maintained MIM groundings and label repairs. | Generated `Nitrate` has no `term`, and generated `original_name` and `media_term.term.label` still contain the old truncated label; both normalized owners have 2026-08-20 and 2026-08-31 events covering those fixes. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 446 and 448 pages expose compound tables, organism links, source links, and growth-data links, but not pH or sterilization instructions. | The MediaDB import/enrichment path that seeded generic `preparation_steps` in both normalized owners. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 446 links `Geobacter metallireducens`, source 131, and growth-data 833; public MediaDB 448 links the same organism and source but growth-data 835. The generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_446_Defined_freshwater_medium_CoCl2.yaml` and `data/normalized_yaml/bacterial/MEDIADB_448_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Change merge generation so MediaDB 446 and 448 stay distinct source records
  connected only by the existing concentration-variant relationship, then
  regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__fbdea278.yaml`.
- Regenerate generated merged YAML from both normalized CoCl2 owners so the
  2026-08-20 MIM nitrate grounding and 2026-08-31 label repairs propagate.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for these nitrate variants.
- Extend the MediaDB owner or importer to preserve source 131, growth-data 833
  and 835, and the `Geobacter metallireducens` assertions with evidence scoped
  to the specific 5.0 mM or 20.0 mM nitrate variant.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on the
  regenerated record or replacement records.
- Revisit public MediaDB 446 and 448 plus `/defined_media/media_text/446/` and
  `/defined_media/media_text/448/` and confirm the generated corpus preserves
  two nitrate variants instead of folding both accessions into one
  `merged_from` list.

## Additional Notes

- Public MediaDB media 446 and 448 and their tab-delimited exports were
  reachable during review.
- The bounded `MEDIADB:446` and `MEDIADB:448` source-owner search included
  ignored files in `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
