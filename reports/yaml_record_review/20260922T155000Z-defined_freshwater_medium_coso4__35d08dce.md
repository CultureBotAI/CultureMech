# YAML Record Review: defined_freshwater_medium_coso4__35d08dce

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4__35d08dce.yaml
- Started UTC: 2026-09-22T15:50:00Z
- Finished UTC: 2026-09-22T15:50:00Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007337` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4__35d08dce.yaml`
- Maintained owners:
  `data/normalized_yaml/bacterial/MEDIADB_434_Defined_freshwater_medium_CoSO4.yaml`
  and
  `data/normalized_yaml/bacterial/MEDIADB_435_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identities: `MEDIADB:434` and `MEDIADB:435`
- Merge fingerprint:
  `35d08dce5d91fa2ebbaa82ba8875f659d51aaabd031e55fa30ab0e745afde1ea`
- Merge shape: two MediaDB records merged as duplicates, with 434 also linked
  to 435 by a concentration-variant relationship

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4__35d08dce.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4__35d08dce.yaml --out /private/tmp/defined_freshwater_medium_coso4__35d08dce.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4__35d08dce.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4__35d08dce.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is anchored on MediaDB 434 and its 10.0 mM toluene
formulation:

- `id: CultureMech:007337`
- `media_term.term.id: MEDIADB:434`
- `ingredients` includes `Toluene` at `10.0` mM and `Ferric oxide` at
  `100.0` mM
- `merged_from` lists both `MEDIADB_434_Defined_freshwater_medium_CoSO4` and
  `MEDIADB_435_Defined_freshwater_medium_CoSO4`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:434`, `MEDIADB:435`,
`MEDIADB_434_Defined_freshwater_medium_CoSO4`, and
`MEDIADB_435_Defined_freshwater_medium_CoSO4` found only the two maintained
owners, this generated record, and generated indexes.

The public MediaDB tab-delimited exports distinguish the two source media:
medium 434 is `Defined freshwater medium (coso4) + 100 mm fe2o3 + 10 mm
toluene`, while medium 435 is `Defined freshwater medium (coso4) + 100 mm
fe2o3 + 1 mm toluene`. The maintained owners preserve that distinction and
link the two records as `CONCENTRATION_VARIANT` records.

The generated record is stale relative to both maintained owners. The owners
have 2026-08-31 MediaDB-name repair events that restored the full source
labels, while the generated record still has the old truncated `original_name`
and `media_term.term.label`.

## Evidence

Supported:

- MediaDB medium 434 denotes the CoSO4-defined freshwater medium plus
  100.0 mM ferric oxide and 10.0 mM toluene; the public page, public
  tab-delimited output, and maintained owner agree on those concentration rows.
- MediaDB medium 435 denotes the same CoSO4-defined freshwater medium plus
  100.0 mM ferric oxide and 1.0 mM toluene; the public page, public
  tab-delimited output, and maintained owner agree on those concentration rows.
- The generated record's canonical ingredient list matches medium 434 rather
  than medium 435 by preserving 10.0 mM toluene.

Unsupported or over-scoped:

- The generated duplicate merge is unsupported. MediaDB 434 and MediaDB 435
  are toluene concentration variants, not identical records that should both
  be in `merged_from` for one fingerprint.
- The generated and maintained `Ferric oxide` row is ungrounded even though
  both public MediaDB exports expose a direct CheBI cross-reference, `50819`,
  for ferric oxide.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized records or the live MediaDB pages.
- The three generic preparation steps are not supported by the inspected
  MediaDB 434 or 435 pages or their tab-delimited compound exports. The public
  pages do not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 434 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 821.
- MediaDB 435 links the same organism and source, and growth-data record 822.
- The generated YAML has no `target_organisms`, organism-scoped growth
  evidence, Lovley source reference, or per-variant growth evidence for either
  toluene concentration.
- The generated merge omits the 2026-08-31 MediaDB-name repair history event
  present on both normalized owners.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 434 and 435 pages did not
  expose those protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | MediaDB 434 and 435 were merged as duplicates even though they differ in toluene concentration. | The public MediaDB exports list 10.0 mM toluene for 434 and 1.0 mM toluene for 435, and the maintained owners already model them as `CONCENTRATION_VARIANT` records. | Merge generation from `data/normalized_yaml/bacterial/MEDIADB_434_Defined_freshwater_medium_CoSO4.yaml` and `data/normalized_yaml/bacterial/MEDIADB_435_Defined_freshwater_medium_CoSO4.yaml`; keep the concentration-variant edge but do not collapse both source records into one duplicate merge. |
| Major | The generated record is stale relative to the maintained MediaDB name repairs. | Generated `original_name` and `media_term.term.label` still contain the old truncated label; both normalized owners have 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` events with the full names. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Ferric oxide is missing a source-supported ontology grounding. | MediaDB 434 and 435 publish a ferric oxide CheBI cross-reference of `50819`; the generated and maintained `Ferric oxide` ingredient entries have no `term`. | Add or repair ferric oxide grounding in the two normalized owners or in the MediaDB import/enrichment path that reads source CheBI IDs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 434 and 435 pages expose compound tables, organism links, source links, and growth-data links, but not pH or sterilization instructions. | The MediaDB import/enrichment path that seeded generic `preparation_steps` in both normalized owners. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 434 links `Geobacter metallireducens`, source 131, and growth-data 821; public MediaDB 435 links the same organism and source but growth-data 822. The generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns the two CoSO4 normalized owners. |

## Recommended Edits

- Change merge generation so MediaDB 434 and 435 stay distinct source records
  connected only by the existing concentration-variant relationship, then
  regenerate `data/merge_yaml/merged/defined_freshwater_medium_coso4__35d08dce.yaml`.
- Regenerate generated merged YAML from both normalized CoSO4 toluene owners
  so the 2026-08-31 label repairs propagate.
- Ground `Ferric oxide` from MediaDB's CheBI `50819` in both maintained CoSO4
  toluene owners or in the MediaDB ingredient import/enrichment path.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for these toluene variants.
- Extend the MediaDB owner or importer to preserve source 131, growth-data 821
  and 822, and the `Geobacter metallireducens` assertions with evidence scoped
  to the specific 10.0 mM or 1.0 mM toluene variant.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on the
  regenerated record or replacement records.
- Revisit public MediaDB 434 and 435 plus `/defined_media/media_text/434/` and
  `/defined_media/media_text/435/` and confirm the generated corpus preserves
  two toluene variants instead of folding both accessions into one
  `merged_from` list.

## Additional Notes

- Public MediaDB media 434 and 435 and their tab-delimited exports were
  reachable during review.
- The bounded `MEDIADB:434` and `MEDIADB:435` source-owner search included
  ignored files in `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
