# YAML Record Review: defined_freshwater_medium_coso4__c7f52b71

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4__c7f52b71.yaml
- Started UTC: 2026-09-22T16:20:33Z
- Finished UTC: 2026-09-22T16:20:33Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007328` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4__c7f52b71.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_426_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:426`
- Merge fingerprint:
  `c7f52b710f5ac34fc1589d5ccd92aacb424c7eecef3725b6a8471a09d3332d2a`
- Merge shape: single source, `MEDIADB_426_Defined_freshwater_medium_CoSO4`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4__c7f52b71.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4__c7f52b71.yaml --out /private/tmp/defined_freshwater_medium_coso4__c7f52b71.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4__c7f52b71.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0 and 0 checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4__c7f52b71.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is a single-source MediaDB 426 import with no variant or
duplicate sources:

- `id: CultureMech:007328`
- `media_term.term.id: MEDIADB:426`
- `ingredients` includes `Propanoate` at `20.0` mM and `Ferric oxide` at
  `100.0` mM
- `merged_from: MEDIADB_426_Defined_freshwater_medium_CoSO4`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:426` and
`MEDIADB_426_Defined_freshwater_medium_CoSO4` found only the maintained owner,
this generated record, and generated indexes.

The public MediaDB 426 page resolves as `Defined freshwater medium (coso4) +
100 mm fe2o3 + 20 mm propionate`; its tab-delimited export lists `Propanoate`
at 20.0 mM and `Ferric oxide` at 100.0 mM. The distinctive rows match the
generated record's imported quantities, but both remain ungrounded in the
generated and maintained YAML despite MediaDB publishing direct CheBI
cross-references: `CHEBI:30768` for `Propanoate` and `CHEBI:50819` for
`Ferric oxide`.

The generated record is stale relative to its maintained owner. The owner has
a 2026-08-31 MediaDB-name repair event that restored
`Defined freshwater medium (CoSO4) + 100 mM Fe2O3 + 20 mM Propionate`, while
the generated record still has the old truncated `original_name` and
`media_term.term.label`.

## Evidence

Supported:

- MediaDB medium 426 denotes the CoSO4-defined freshwater medium plus
  100.0 mM ferric oxide and 20.0 mM Propanoate; the public page, public
  tab-delimited output, and maintained owner agree on those distinctive
  ingredient rows.
- The generated ingredient list preserves the 20.0 mM Propanoate row that
  distinguishes MediaDB 426 from the CoSO4 ferric oxide and acetate variants.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- The generated record's `original_name` and `media_term.term.label` are stale
  values that no longer match the maintained normalized record or the live
  MediaDB page.
- The generated and maintained `Propanoate` row is ungrounded even though the
  public MediaDB export exposes a direct CheBI cross-reference, `30768`, for
  propionate.
- The generated and maintained `Ferric oxide` row is ungrounded even though the
  public MediaDB export exposes a direct CheBI cross-reference, `50819`, for
  ferric oxide.
- The three generic preparation steps are not supported by the inspected
  MediaDB 426 page or its tab-delimited compound export. The public page does
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 426 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 813. The generated YAML
  has no `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-31 MediaDB-name repair history event
  present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 426 page did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MediaDB name repair. | Generated `original_name` and `media_term.term.label` still contain the old truncated label; the normalized owner has a 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` event with the full name. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Propanoate is missing a source-supported ontology grounding. | MediaDB 426 publishes a Propanoate CheBI cross-reference of `30768`; the generated and maintained `Propanoate` ingredient entries have no `term`. | Add or repair Propanoate grounding in `data/normalized_yaml/bacterial/MEDIADB_426_Defined_freshwater_medium_CoSO4.yaml` or in the MediaDB import/enrichment path that reads source CheBI IDs. |
| Major | Ferric oxide is missing a source-supported ontology grounding. | MediaDB 426 publishes a ferric oxide CheBI cross-reference of `50819`; the generated and maintained `Ferric oxide` ingredient entries have no `term`. | Add or repair ferric oxide grounding in `data/normalized_yaml/bacterial/MEDIADB_426_Defined_freshwater_medium_CoSO4.yaml` or in the MediaDB import/enrichment path that reads source CheBI IDs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 426 page exposes a compound table, organism link, source link, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_426_Defined_freshwater_medium_CoSO4.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 426 links `Geobacter metallireducens`, source 131, and growth-data 813; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_426_Defined_freshwater_medium_CoSO4.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_coso4__c7f52b71.yaml`
  from its normalized source so the 2026-08-31 MediaDB-name repair propagates.
- Ground `Propanoate` from MediaDB's CheBI `30768` in
  `data/normalized_yaml/bacterial/MEDIADB_426_Defined_freshwater_medium_CoSO4.yaml`
  or in the MediaDB ingredient import/enrichment path.
- Ground `Ferric oxide` from MediaDB's CheBI `50819` in the maintained owner or
  in the MediaDB ingredient import/enrichment path.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data 813,
  and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 426.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_coso4__c7f52b71.yaml`.
- Revisit public MediaDB 426 and `/defined_media/media_text/426/` and confirm
  the regenerated record has the full MediaDB 426 label, grounded Propanoate
  and ferric oxide, and no unsupported generic pH or filter-sterilization
  steps.

## Additional Notes

- Public MediaDB medium 426 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:426` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
