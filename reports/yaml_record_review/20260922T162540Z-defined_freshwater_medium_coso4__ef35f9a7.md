# YAML Record Review: defined_freshwater_medium_coso4__ef35f9a7

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4__ef35f9a7.yaml
- Started UTC: 2026-09-22T16:25:40Z
- Finished UTC: 2026-09-22T16:25:40Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007324` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4__ef35f9a7.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_422_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:422`
- Merge fingerprint:
  `ef35f9a794bf06ad22789fc9d502e0a46cb0a0fc7df98f4debb185a73bcc031d`
- Merge shape: single source, `MEDIADB_422_Defined_freshwater_medium_CoSO4`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4__ef35f9a7.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4__ef35f9a7.yaml --out /private/tmp/defined_freshwater_medium_coso4__ef35f9a7.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4__ef35f9a7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0 and 0 checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4__ef35f9a7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is a single-source MediaDB 422 import with no variant or
duplicate sources:

- `id: CultureMech:007324`
- `media_term.term.id: MEDIADB:422`
- `ingredients` includes `'''Manganese(IV` at `15.0` mM and `Ferric oxide` at
  `100.0` mM
- `merged_from: MEDIADB_422_Defined_freshwater_medium_CoSO4`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:422` and
`MEDIADB_422_Defined_freshwater_medium_CoSO4` found only the maintained owner,
this generated record, and generated indexes.

The public MediaDB 422 page resolves as `Defined freshwater medium (coso4) +
15 mm mno2 + 113.2 mm acetate`; its tab-delimited export lists
`Manganese(IV) oxide` at 15.0 mM and `Ferric oxide` at 100.0 mM. The generated
record is stale relative to its maintained owner: the owner has a 2026-08-31
ingredient-name repair that restored `Manganese(IV) oxide` and a second
2026-08-31 MediaDB-name repair that restored
`Defined freshwater medium (CoSO4) + 15 mM MnO2 + 113.2 mM Acetate`.

## Evidence

Supported:

- MediaDB medium 422 denotes the CoSO4-defined freshwater medium plus
  100.0 mM ferric oxide, 15.0 mM Manganese(IV) oxide, and 113.2 mM Acetate;
  the public page, public tab-delimited output, and maintained owner agree on
  those distinctive ingredient rows.
- The generated ingredient list preserves the 15.0 mM manganese(IV) oxide row,
  but not the restored ingredient spelling, that distinguishes MediaDB 422 from
  the CoSO4 ferric oxide and acetate-only variants.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- The generated record's `Manganese(IV) oxide` row, `original_name`, and
  `media_term.term.label` are stale values that no longer match the maintained
  normalized record or the live MediaDB page.
- The generated and maintained `Ferric oxide` row is ungrounded even though the
  public MediaDB export exposes a direct CheBI cross-reference, `50819`, for
  ferric oxide.
- The three generic preparation steps are not supported by the inspected
  MediaDB 422 page or its tab-delimited compound export. The public page does
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 422 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 809. The generated YAML
  has no `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-31 MediaDB ingredient-name and
  medium-name repair history events present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 422 page did not expose those
  protocol details.
- The `Manganese(IV) oxide` ingredient was left unresolved by this review; the
  inspected MediaDB tab-delimited export lists PubChem `14801`, but no CheBI
  cross-reference.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MediaDB ingredient-name and medium-name repairs. | Generated `preferred_term` still contains the old truncated `'''Manganese(IV` string, and generated `original_name`/`media_term.term.label` still contain the old truncated label; the normalized owner has two 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` events with the restored ingredient and medium names. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Ferric oxide is missing a source-supported ontology grounding. | MediaDB 422 publishes a ferric oxide CheBI cross-reference of `50819`; the generated and maintained `Ferric oxide` ingredient entries have no `term`. | Add or repair ferric oxide grounding in `data/normalized_yaml/bacterial/MEDIADB_422_Defined_freshwater_medium_CoSO4.yaml` or in the MediaDB import/enrichment path that reads source CheBI IDs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 422 page exposes a compound table, organism link, source link, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_422_Defined_freshwater_medium_CoSO4.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 422 links `Geobacter metallireducens`, source 131, and growth-data 809; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_422_Defined_freshwater_medium_CoSO4.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_coso4__ef35f9a7.yaml`
  from its normalized source so both 2026-08-31 MediaDB parser repairs
  propagate.
- Ground `Ferric oxide` from MediaDB's CheBI `50819` in
  `data/normalized_yaml/bacterial/MEDIADB_422_Defined_freshwater_medium_CoSO4.yaml`
  or in the MediaDB ingredient import/enrichment path.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data 809,
  and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 422.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_coso4__ef35f9a7.yaml`.
- Revisit public MediaDB 422 and `/defined_media/media_text/422/` and confirm
  the regenerated record has the full MediaDB 422 label, the restored
  `Manganese(IV) oxide` ingredient label, grounded ferric oxide, and no
  unsupported generic pH or filter-sterilization steps.

## Additional Notes

- Public MediaDB medium 422 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:422` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
