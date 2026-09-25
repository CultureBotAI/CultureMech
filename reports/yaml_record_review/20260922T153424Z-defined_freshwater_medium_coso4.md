# YAML Record Review: defined_freshwater_medium_coso4

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4.yaml
- Started UTC: 2026-09-22T15:34:24Z
- Finished UTC: 2026-09-22T15:34:24Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007317` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4.yaml`
- Maintained owners:
  `data/normalized_yaml/bacterial/MEDIADB_416_Defined_freshwater_medium_CoSO4.yaml`,
  `data/normalized_yaml/bacterial/MEDIADB_417_Defined_freshwater_medium_CoSO4.yaml`,
  `data/normalized_yaml/bacterial/MEDIADB_423_Defined_freshwater_medium_CoSO4.yaml`,
  and
  `data/normalized_yaml/bacterial/MEDIADB_424_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identities: `MEDIADB:416`, `MEDIADB:417`, `MEDIADB:423`, and
  `MEDIADB:424`
- Merge fingerprint:
  `49655c629778a35c0306fd6c3f13817292f2ab346deadad891dc2d572a5e48b2`
- Merge shape: four MediaDB records merged as duplicates, with 417, 423, and
  424 also retained as concentration variant children of 416

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4.yaml --out /private/tmp/defined_freshwater_medium_coso4.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is anchored on MediaDB 416 and its 100 mM Fe2O3 plus
113.2 mM acetate formulation:

- `id: CultureMech:007317`
- `media_term.term.id: MEDIADB:416`
- `ingredients` includes `Ferric oxide` at `100.0` mM and `Acetate` at
  `113.2` mM
- `merged_from` lists MediaDB 416, 417, 423, and 424 owners

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:416`, `MEDIADB:417`, `MEDIADB:423`,
`MEDIADB:424`, and the exact four CoSO4 owner stems found only the four
maintained owners, this generated record, and generated indexes.

The public MediaDB tab-delimited exports distinguish all four source media:
medium 416 is `Defined freshwater medium (coso4) + 100 mm fe2o3 + 113.2 mm
acetate`; 417 changes ferric oxide to 250.0 mM; 423 keeps 100.0 mM ferric
oxide but changes acetate to 10.0 mM; and 424 keeps 100.0 mM ferric oxide but
changes acetate to 50.0 mM. The maintained owners preserve those four
concentration signatures, with 417, 423, and 424 declared as
`CONCENTRATION_VARIANT` children of 416.

The generated record is stale relative to the maintained 416 owner because its
`original_name` and `media_term.term.label` still contain the earlier truncated
`'Defined freshwater medium (CoSO4` label instead of the repaired full MediaDB
416 name.

## Evidence

Supported:

- MediaDB medium 416 denotes the CoSO4-defined freshwater medium plus
  100.0 mM ferric oxide and 113.2 mM acetate; the public page, public
  tab-delimited output, and maintained owner agree on those two distinctive
  concentration rows.
- MediaDB media 417, 423, and 424 denote distinct concentration variants, not
  mere duplicate imports of 416.
- The generated record's canonical ingredient list matches medium 416 rather
  than 417, 423, or 424 by preserving 100.0 mM ferric oxide and 113.2 mM
  acetate.

Unsupported or over-scoped:

- The generated duplicate merge is unsupported. MediaDB 416, 417, 423, and 424
  are concentration variants, not four identical source records that should
  all be in `merged_from` for one fingerprint.
- The generated and maintained `Ferric oxide` row is ungrounded even though the
  public MediaDB exports expose a direct CheBI cross-reference, `50819`, for
  ferric oxide.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB 416
  page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 416, 417, 423, or 424 pages or their tab-delimited compound exports.
  The public pages do not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 416 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 803.
- MediaDB 417 links the same organism and source, and growth-data record 804.
- MediaDB 423 links the same organism and source, and growth-data record 810.
- MediaDB 424 links the same organism and source, and growth-data record 811.
- The generated YAML has no `target_organisms`, organism-scoped growth
  evidence, Lovley source reference, or per-variant growth evidence for any of
  those four MediaDB assertions.
- The generated merge omits the 2026-08-31 name-repair history event present
  on the maintained 416 owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 416, 417, 423, and 424 pages
  did not expose those protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | MediaDB 416, 417, 423, and 424 were merged as duplicates even though they differ in Fe2O3 and acetate concentrations. | The public MediaDB exports list distinct ferric oxide or acetate amounts for all four source records, and the maintained owners already represent 417, 423, and 424 as `CONCENTRATION_VARIANT` children of 416. | Merge generation from the four `data/normalized_yaml/bacterial/MEDIADB_*_Defined_freshwater_medium_CoSO4.yaml` owners; keep the concentration-variant edges but do not collapse all four sources into one duplicate merge. |
| Major | The generated record is stale relative to the maintained MediaDB name repair. | Generated `original_name` and `media_term.term.label` still contain the old truncated label; the normalized 416 owner has a 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` event with the full name. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Ferric oxide is missing a source-supported ontology grounding. | MediaDB 416, 417, 423, and 424 all publish a ferric oxide CheBI cross-reference of `50819`; the generated and maintained `Ferric oxide` ingredient entries have no `term`. | Add or repair ferric oxide grounding in the four CoSO4 normalized owners or in the MediaDB import/enrichment path that reads source CheBI IDs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 416, 417, 423, and 424 pages expose compound tables, organism links, source links, and growth-data links, but not pH or sterilization instructions. | The MediaDB import/enrichment path that seeded generic `preparation_steps` in all four normalized owners. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB pages 416, 417, 423, and 424 all link `Geobacter metallireducens` and source 131, with growth-data records 803, 804, 810, and 811 respectively. The generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns the four CoSO4 normalized owners. |

## Recommended Edits

- Change merge generation so MediaDB 416, 417, 423, and 424 stay distinct
  source records connected only by concentration-variant relationships, then
  regenerate `data/merge_yaml/merged/defined_freshwater_medium_coso4.yaml`.
- Regenerate generated merged YAML from `MEDIADB_416_Defined_freshwater_medium_CoSO4.yaml`
  so the 2026-08-31 full-name repair propagates.
- Ground `Ferric oxide` from MediaDB's CheBI `50819` in all four maintained
  CoSO4 owners or in the MediaDB ingredient import/enrichment path.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for these Fe2O3 and acetate variants.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  803/804/810/811, and the `Geobacter metallireducens` assertions with
  evidence scoped to the specific Fe2O3 and acetate variant.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on the
  regenerated record or replacement records.
- Revisit public MediaDB 416, 417, 423, and 424 plus their
  `/defined_media/media_text/<id>/` exports and confirm the generated corpus
  preserves four Fe2O3/acetate variants instead of folding all four accessions
  into one `merged_from` list.

## Additional Notes

- Public MediaDB media 416, 417, 423, and 424 and their tab-delimited exports
  were reachable during review.
- The bounded `MEDIADB:416`, `MEDIADB:417`, `MEDIADB:423`, and `MEDIADB:424`
  source-owner search included ignored files in `data/normalized_yaml` and
  `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
