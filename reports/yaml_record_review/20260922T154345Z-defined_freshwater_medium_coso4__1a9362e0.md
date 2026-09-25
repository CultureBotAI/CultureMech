# YAML Record Review: defined_freshwater_medium_coso4__1a9362e0

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4__1a9362e0.yaml
- Started UTC: 2026-09-22T15:43:45Z
- Finished UTC: 2026-09-22T15:43:45Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007341` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4__1a9362e0.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_438_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:438`
- Merge fingerprint:
  `1a9362e01a735c695446036523805c528bd94256d07b80f212e46820e6d0c668`
- Merge shape: single source, `MEDIADB_438_Defined_freshwater_medium_CoSO4`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4__1a9362e0.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4__1a9362e0.yaml --out /private/tmp/defined_freshwater_medium_coso4__1a9362e0.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4__1a9362e0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4__1a9362e0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is a single-source MediaDB 438 import with no variant or
duplicate sources:

- `id: CultureMech:007341`
- `media_term.term.id: MEDIADB:438`
- `ingredients` includes `Ferric oxide` at `100.0` mM and `Benzyl alcohol` at
  `0.5` mM
- `merged_from: MEDIADB_438_Defined_freshwater_medium_CoSO4`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:438` and
`MEDIADB_438_Defined_freshwater_medium_CoSO4` found only the maintained owner,
this generated record, and generated indexes.

The public MediaDB 438 page resolves as `Defined freshwater medium (coso4) +
100 mm fe2o3 + 0.5 mm benzyl alcohol`; its tab-delimited export lists `Ferric
oxide` at 100.0 mM and `Benzyl alcohol` at 0.5 mM. The maintained owner
matches that identity and now grounds `Benzyl alcohol` to `CHEBI:17987`.

The generated record is stale relative to its maintained owner. The owner has
a 2026-08-20 `apply_mim_groundings.py` event that grounded `Benzyl alcohol`
from the MIM published mappings and a 2026-08-31 MediaDB-name repair event
that restored the full original name; the generated record has neither update.

## Evidence

Supported:

- MediaDB medium 438 denotes the CoSO4-defined freshwater medium plus 100.0 mM
  ferric oxide and 0.5 mM benzyl alcohol; the public page, public
  tab-delimited output, and maintained owner agree on those distinctive
  ingredient rows.
- The generated ingredient list preserves the 0.5 mM benzyl alcohol row that
  distinguishes MediaDB 438 from the CoSO4 ferric oxide and acetate variants.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- `Benzyl alcohol` is ungrounded in the generated record even though the
  maintained owner now grounds it to `CHEBI:17987` and the public MediaDB
  export exposes the same CheBI cross-reference.
- The generated and maintained `Ferric oxide` row is ungrounded even though the
  public MediaDB export exposes a direct CheBI cross-reference, `50819`, for
  ferric oxide.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 438 page or its tab-delimited compound export. The public page does
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 438 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 825. The generated YAML
  has no `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-20 MIM grounding and 2026-08-31
  MediaDB-name repair history events present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 438 page did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MIM grounding and MediaDB name repair. | Generated `Benzyl alcohol` has no `term`, and generated `original_name` and `media_term.term.label` still contain the old truncated label; the normalized owner has 2026-08-20 and 2026-08-31 events covering those fixes. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Ferric oxide is missing a source-supported ontology grounding. | MediaDB 438 publishes a ferric oxide CheBI cross-reference of `50819`; the generated and maintained `Ferric oxide` ingredient entries have no `term`. | Add or repair ferric oxide grounding in `data/normalized_yaml/bacterial/MEDIADB_438_Defined_freshwater_medium_CoSO4.yaml` or in the MediaDB import/enrichment path that reads source CheBI IDs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 438 page exposes a compound table, organism link, source link, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_438_Defined_freshwater_medium_CoSO4.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 438 links `Geobacter metallireducens`, source 131, and growth-data 825; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_438_Defined_freshwater_medium_CoSO4.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_coso4__1a9362e0.yaml`
  from its normalized source so the 2026-08-20 MIM grounding and 2026-08-31
  MediaDB-name repair propagate.
- Ground `Ferric oxide` from MediaDB's CheBI `50819` in
  `data/normalized_yaml/bacterial/MEDIADB_438_Defined_freshwater_medium_CoSO4.yaml`
  or in the MediaDB ingredient import/enrichment path.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data 825,
  and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 438.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_coso4__1a9362e0.yaml`.
- Revisit public MediaDB 438 and `/defined_media/media_text/438/` and confirm
  the regenerated record has grounded 0.5 mM Benzyl alcohol, the full MediaDB
  438 label, and no unsupported generic pH or filter-sterilization steps.

## Additional Notes

- Public MediaDB medium 438 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:438` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
