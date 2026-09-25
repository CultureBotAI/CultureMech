# YAML Record Review: defined_freshwater_medium_coso4__a30bb78a

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4__a30bb78a.yaml
- Started UTC: 2026-09-22T16:06:46Z
- Finished UTC: 2026-09-22T16:06:46Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007333` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4__a30bb78a.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_430_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:430`
- Merge fingerprint:
  `a30bb78a7aa29f7866275fe07a56f0f1f195681caa0c84bae5a299f904eb1279`
- Merge shape: single source, `MEDIADB_430_Defined_freshwater_medium_CoSO4`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4__a30bb78a.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4__a30bb78a.yaml --out /private/tmp/defined_freshwater_medium_coso4__a30bb78a.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4__a30bb78a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0 and 0 checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4__a30bb78a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is a single-source MediaDB 430 import, but its formulation
does not match the public MediaDB formula:

- `id: CultureMech:007333`
- `media_term.term.id: MEDIADB:430`
- `merged_from: MEDIADB_430_Defined_freshwater_medium_CoSO4`
- The YAML includes LB-derived `Tryptone`, `Yeast extract`, and 10 g/L
  `Sodium chloride` rows that are not present in MediaDB 430.
- The YAML omits the 10.0 mM `3-Methylbutanoic acid` row that distinguishes
  MediaDB 430 from the neighboring CoSO4 ferric oxide variants.

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:430` and
`MEDIADB_430_Defined_freshwater_medium_CoSO4` found only the maintained owner,
this generated record, and generated indexes.

The public MediaDB 430 page resolves as `Defined freshwater medium (coso4) +
100 mm fe2o3 + 10 mm isovalerate`; its tab-delimited export lists
`3-Methylbutanoic acid` at 10.0 mM, `Ferric oxide` at 100.0 mM, and no
`Tryptone`, `Yeast extract`, or 10 g/L `Sodium chloride` LB rows. The
maintained owner has the repaired 2026-08-31 MediaDB label, but both the owner
and generated YAML still carry the unsupported LB-derived ingredient rows and
omit `3-Methylbutanoic acid`.

## Evidence

Supported:

- MediaDB medium 430 denotes the CoSO4-defined freshwater medium plus
  100.0 mM ferric oxide and 10.0 mM 3-Methylbutanoic acid; the public page and
  tab-delimited output agree on those distinctive rows.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- The generated and maintained ingredient lists do not represent the MediaDB
  430 formula: they omit source row `3-Methylbutanoic acid` and inject
  LB-derived `Tryptone`, `Yeast extract`, and 10 g/L `Sodium chloride`.
- The generated record's `medium_type: COMPLEX` and
  `composition_type: UNDEFINED` follow the unsupported LB enrichment rather
  than the explicit 29-compound MediaDB formula.
- The generated record's `original_name` and `media_term.term.label` are stale
  values that no longer match the maintained normalized record or the live
  MediaDB page.
- The generated and maintained `Ferric oxide` row is ungrounded even though the
  public MediaDB export exposes a direct CheBI cross-reference, `50819`, for
  ferric oxide.
- The three generic preparation steps are not supported by the inspected
  MediaDB 430 page or its tab-delimited compound export. The public page does
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 430's 10.0 mM `3-Methylbutanoic acid` ingredient is absent from the
  generated and maintained YAML despite the public export publishing a direct
  CheBI cross-reference of `28484` for that row.
- MediaDB 430 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 817. The generated YAML
  has no `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-31 MediaDB-name repair history event
  present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 430 page did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The maintained formula for MediaDB 430 has LB enrichment in place of its source-specific isovalerate row. | Public MediaDB 430 lists 10.0 mM `3-Methylbutanoic acid` and no `Tryptone`, `Yeast extract`, or 10 g/L `Sodium chloride` LB rows; the normalized and generated YAML omit `3-Methylbutanoic acid` and include those three unsupported LB rows. | Remove the LB enrichment and add the 10.0 mM `3-Methylbutanoic acid` row in `data/normalized_yaml/bacterial/MEDIADB_430_Defined_freshwater_medium_CoSO4.yaml` or in the enrichment rule that injected the LB rows. |
| Major | The generated record is stale relative to the maintained MediaDB name repair. | Generated `original_name` and `media_term.term.label` still contain the old truncated label; the normalized owner has a 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` event with the full name. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Ferric oxide is missing a source-supported ontology grounding. | MediaDB 430 publishes a ferric oxide CheBI cross-reference of `50819`; the generated and maintained `Ferric oxide` ingredient entries have no `term`. | Add or repair ferric oxide grounding in `data/normalized_yaml/bacterial/MEDIADB_430_Defined_freshwater_medium_CoSO4.yaml` or in the MediaDB import/enrichment path that reads source CheBI IDs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 430 page exposes a compound table, organism link, source link, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_430_Defined_freshwater_medium_CoSO4.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 430 links `Geobacter metallireducens`, source 131, and growth-data 817; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_430_Defined_freshwater_medium_CoSO4.yaml`. |

## Recommended Edits

- Remove the unsupported LB-derived `Tryptone`, `Yeast extract`, and 10 g/L
  `Sodium chloride` rows from
  `data/normalized_yaml/bacterial/MEDIADB_430_Defined_freshwater_medium_CoSO4.yaml`;
  then set `medium_type` and `composition_type` back to the source-supported
  defined classification.
- Add MediaDB 430's 10.0 mM `3-Methylbutanoic acid` row, grounded from
  MediaDB's CheBI `28484`, to the maintained owner.
- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_coso4__a30bb78a.yaml`
  from its normalized source so the 2026-08-31 MediaDB-name repair propagates.
- Ground `Ferric oxide` from MediaDB's CheBI `50819` in the maintained owner or
  in the MediaDB ingredient import/enrichment path.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data 817,
  and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 430.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_coso4__a30bb78a.yaml`.
- Revisit public MediaDB 430 and `/defined_media/media_text/430/` and confirm
  the regenerated record has the full MediaDB 430 label, the 10.0 mM
  `3-Methylbutanoic acid` row, no LB rows, grounded ferric oxide, and no
  unsupported generic pH or filter-sterilization steps.

## Additional Notes

- Public MediaDB medium 430 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:430` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
