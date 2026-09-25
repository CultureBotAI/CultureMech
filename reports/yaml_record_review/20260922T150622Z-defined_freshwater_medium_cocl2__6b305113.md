# YAML Record Review: defined_freshwater_medium_cocl2__6b305113

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__6b305113.yaml
- Started UTC: 2026-09-22T15:06:22Z
- Finished UTC: 2026-09-22T15:06:22Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007362` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__6b305113.yaml`
- Maintained owners:
  `data/normalized_yaml/bacterial/MEDIADB_457_Defined_freshwater_medium_CoCl2.yaml`
  and
  `data/normalized_yaml/bacterial/MEDIADB_463_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identities: `MEDIADB:457`, `MEDIADB:463`
- Merge fingerprint:
  `6b305113e95cdb72e2eb7b36585a0ec81e5818e2b237876e4050fa326f7ec744`
- Merge shape: two MediaDB records merged from
  `MEDIADB_457_Defined_freshwater_medium_CoCl2` and
  `MEDIADB_463_Defined_freshwater_medium_CoCl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__6b305113.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__6b305113.yaml --out /private/tmp/defined_freshwater_medium_cocl2__6b305113.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__6b305113.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__6b305113.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated identity merges two MediaDB toluene variants:

- `id: CultureMech:007362`
- `media_term.term.id: MEDIADB:457`
- `merged_from: MEDIADB_457_Defined_freshwater_medium_CoCl2`
- `merged_from: MEDIADB_463_Defined_freshwater_medium_CoCl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:457`, `MEDIADB:463`, and the exact normalized
owner stems found only the generated record, the two maintained owners, and
generated indexes.

The public MediaDB records are distinct. MediaDB 457 is `Defined freshwater
medium (cocl2) + 100 mm fe2o3 + 10 mm toluene`; MediaDB 463 is `Defined
freshwater medium (cocl2) + 100 mm fe2o3 + 1 mm toluene`. Their public pages
and tab-delimited exports agree that the only formula difference is `Toluene`
at 10.0 mM versus 1.0 mM, and the normalized owners encode that relationship
as `CONCENTRATION_VARIANT`.

The generated record is also stale relative to both maintained owners. The
normalized owner files have 2026-08-31 `repair_mediadb_names.py` events and
restored MediaDB labels, but the generated record still carries the older
parser-damaged `'''Defined freshwater medium (CoCl2` in both `original_name`
and `media_term.term.label`.

## Evidence

Supported:

- MediaDB medium 457 denotes the 100 mM Fe2O3 / 10 mM toluene member of the
  CoCl2-defined freshwater medium set.
- MediaDB medium 463 denotes the 100 mM Fe2O3 / 1 mM toluene member of the
  same set.
- The generated `parent_media`, `variant_relationship`, and
  `variant_modifications` fields correctly describe 457 as a 10 mM toluene
  concentration variant of 463.

Unsupported or over-scoped:

- The generated record collapses two distinct concentration variants into one
  merged output, preserving only the 10.0 mM `Toluene` row from MediaDB 457
  while also listing MediaDB 463 as a duplicate source.
- The generated record points `parent_media` at MediaDB 463 even though that
  same 1 mM toluene owner has been merged into the generated output.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match either maintained normalized record or live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 457/463 pages or their tab-delimited compound exports. The public
  pages do not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 457 links `Geobacter metallireducens`, source 131 (`Lovley dr et al,
  1993`), and growth-data record 844. MediaDB 463 links the same organism and
  source with growth-data record 850. The generated YAML has no
  `target_organisms`, organism-scoped growth evidence, or Lovley source
  reference for either MediaDB assertion.
- The generated merge omits the 2026-08-31 name-repair history events present
  on both normalized owners.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 457/463 pages did not expose
  those protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Two distinct toluene concentration variants were merged as if they were duplicates. | MediaDB 457 is 10.0 mM toluene, MediaDB 463 is 1.0 mM toluene, and both normalized records already encode `CONCENTRATION_VARIANT`; generated `merged_from` lists both owners and preserves only the 10.0 mM value. | Merge fingerprinting and `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/`. |
| Major | The generated record is stale relative to the maintained MediaDB name repairs. | Generated `original_name` and `media_term.term.label` still contain `'''Defined freshwater medium (CoCl2`; both normalized owners have the 2026-08-31 repair event and full MediaDB labels. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 457/463 pages expose compound tables, organisms, sources, and growth-data links, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_457_Defined_freshwater_medium_CoCl2.yaml`, `data/normalized_yaml/bacterial/MEDIADB_463_Defined_freshwater_medium_CoCl2.yaml`, or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 457 links growth-data 844; public MediaDB 463 links growth-data 850; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns the two normalized MediaDB records. |

## Recommended Edits

- Adjust merge fingerprinting so the 1 mM and 10 mM toluene MediaDB records
  stay as separate generated records linked by `CONCENTRATION_VARIANT`, not as
  duplicate inputs to one generated YAML.
- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__6b305113.yaml`
  after the duplicate merge is split so the 2026-08-31 MediaDB name repairs
  propagate to both toluene outputs.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for these media.
- Extend the MediaDB owners or importer to preserve source 131, growth-data
  844/850, and the `Geobacter metallireducens` assertions with evidence scoped
  to the appropriate MediaDB medium.

## Follow-up Checks

- Re-run the merge process and verify MediaDB 457 and 463 have distinct
  generated outputs.
- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  the regenerated toluene-variant records.
- Revisit public MediaDB 457, public MediaDB 463, and their
  `/defined_media/media_text/` exports and confirm the two regenerated records
  preserve 10.0 mM versus 1.0 mM `Toluene` exactly.

## Additional Notes

- Public MediaDB media 457 and 463 and their tab-delimited exports were
  reachable during review.
- The bounded `MEDIADB:457`/`MEDIADB:463` source-owner search included ignored
  files in `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
