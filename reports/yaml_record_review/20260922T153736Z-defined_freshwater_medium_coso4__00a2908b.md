# YAML Record Review: defined_freshwater_medium_coso4__00a2908b

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_coso4__00a2908b.yaml
- Started UTC: 2026-09-22T15:37:36Z
- Finished UTC: 2026-09-22T15:37:36Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007344` for
`defined_freshwater_medium_coso4`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_coso4__00a2908b.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_440_Defined_freshwater_medium_CoSO4.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:440`
- Merge fingerprint:
  `00a2908bc4d2f3f28fe68c721f08a9a3c7b131202188ed7b0037d33c02af6b0c`
- Merge shape: single source, `MEDIADB_440_Defined_freshwater_medium_CoSO4`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_coso4__00a2908b.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_coso4__00a2908b.yaml --out /private/tmp/defined_freshwater_medium_coso4__00a2908b.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_coso4__00a2908b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_coso4__00a2908b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated record is a single-source MediaDB 440 import with no variant or
duplicate sources:

- `id: CultureMech:007344`
- `media_term.term.id: MEDIADB:440`
- `ingredients` includes `Ferric oxide` at `100.0` mM and
  `4-Hydroxybenzaldehyde` at `0.5` mM
- `merged_from: MEDIADB_440_Defined_freshwater_medium_CoSO4`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:440` and
`MEDIADB_440_Defined_freshwater_medium_CoSO4` found only the maintained owner,
this generated record, and generated indexes.

The public MediaDB 440 page resolves as `Defined freshwater medium (coso4) +
100 mm fe2o3 + 0.5 mm p-hydroxybenzaldehyde`; its tab-delimited export lists
`Ferric oxide` at 100.0 mM and `4-Hydroxybenzaldehyde` at 0.5 mM. The
maintained owner matches that identity and now grounds `4-Hydroxybenzaldehyde`
to `CHEBI:17597`.

The generated record is stale relative to its maintained owner. The owner has
a 2026-08-20 `apply_mim_groundings.py` event that grounded
`4-Hydroxybenzaldehyde` from the MIM published mappings and a 2026-08-31
MediaDB-name repair event that restored the full original name; the generated
record has neither update.

## Evidence

Supported:

- MediaDB medium 440 denotes the CoSO4-defined freshwater medium plus 100.0 mM
  ferric oxide and 0.5 mM 4-Hydroxybenzaldehyde; the public page, public
  tab-delimited output, and maintained owner agree on those distinctive
  ingredient rows.
- The generated ingredient list preserves the 0.5 mM
  4-Hydroxybenzaldehyde row that distinguishes MediaDB 440 from the CoSO4
  ferric oxide and acetate variants.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- `4-Hydroxybenzaldehyde` is ungrounded in the generated record even though
  the maintained owner now grounds it to `CHEBI:17597` and the public MediaDB
  export exposes the same CheBI cross-reference.
- The generated and maintained `Ferric oxide` row is ungrounded even though the
  public MediaDB export exposes a direct CheBI cross-reference, `50819`, for
  ferric oxide.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 440 page or its tab-delimited compound export. The public page does
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 440 links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 827. The generated YAML
  has no `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference.
- The generated merge omits the 2026-08-20 MIM grounding and 2026-08-31
  MediaDB-name repair history events present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 440 page did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MIM grounding and MediaDB name repair. | Generated `4-Hydroxybenzaldehyde` has no `term`, and generated `original_name` and `media_term.term.label` still contain the old truncated label; the normalized owner has 2026-08-20 and 2026-08-31 events covering those fixes. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Ferric oxide is missing a source-supported ontology grounding. | MediaDB 440 publishes a ferric oxide CheBI cross-reference of `50819`; the generated and maintained `Ferric oxide` ingredient entries have no `term`. | Add or repair ferric oxide grounding in `data/normalized_yaml/bacterial/MEDIADB_440_Defined_freshwater_medium_CoSO4.yaml` or in the MediaDB import/enrichment path that reads source CheBI IDs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 440 page exposes a compound table, organism link, source link, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_440_Defined_freshwater_medium_CoSO4.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 440 links `Geobacter metallireducens`, source 131, and growth-data 827; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_440_Defined_freshwater_medium_CoSO4.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_coso4__00a2908b.yaml`
  from its normalized source so the 2026-08-20 MIM grounding and 2026-08-31
  MediaDB-name repair propagate.
- Ground `Ferric oxide` from MediaDB's CheBI `50819` in
  `data/normalized_yaml/bacterial/MEDIADB_440_Defined_freshwater_medium_CoSO4.yaml`
  or in the MediaDB ingredient import/enrichment path.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data 827,
  and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 440.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_coso4__00a2908b.yaml`.
- Revisit public MediaDB 440 and `/defined_media/media_text/440/` and confirm
  the regenerated record has grounded 0.5 mM 4-Hydroxybenzaldehyde, the full
  MediaDB 440 label, and no unsupported generic pH or filter-sterilization
  steps.

## Additional Notes

- Public MediaDB medium 440 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:440` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
