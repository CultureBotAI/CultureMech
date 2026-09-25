# YAML Record Review: defined_freshwater_medium_cocl2__f0ffbcc6

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__f0ffbcc6.yaml
- Started UTC: 2026-09-22T15:29:51Z
- Finished UTC: 2026-09-22T15:29:51Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007294` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__f0ffbcc6.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:390`
- Merge fingerprint:
  `f0ffbcc6cef9a3a22ac74c6b6e240e0ba8b63dc57d8d2dddb55109ddca38b27c`
- Merge shape: single source, `defined_freshwater_medium_cocl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__f0ffbcc6.yaml` | Passed with exit code 0. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__f0ffbcc6.yaml --out /private/tmp/defined_freshwater_medium_cocl2__f0ffbcc6.strict.tsv --workers 1 --quiet` | Passed with exit code 0. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__f0ffbcc6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit code 0. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__f0ffbcc6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The generated identity is a single MediaDB 390 source with a bare normalized
owner stem:

- `id: CultureMech:007294`
- `media_term.term.id: MEDIADB:390`
- `merged_from: defined_freshwater_medium_cocl2`

A gitignore-independent search over `data/normalized_yaml` and
`data/merge_yaml` for `MEDIADB:390` and the exact `defined_freshwater_medium_cocl2.yaml`
owner filename found only the generated record, the maintained owner, and
generated indexes.

The public MediaDB 390 page resolves as `Defined freshwater medium (cocl2) +
electron donors/acceptors`; its compound table lists 39 compounds, including
`Fe(III)dicitrate` at 56.0 mM, `Ferric nitrilotriacetate` at 5.0 mM,
`Nitrate` at 20.0 mM, `Fumarate` at 30.0 mM, and `Glycolate` at 10.0 mM.
Those electron donor/acceptor rows are present in the maintained and generated
YAML, but the generated record preserves the 56.0 mM Fe(III)dicitrate row
only as parser-damaged `'''Fe(III`.

The generated record is stale relative to its maintained owner. The owner has
a 2026-08-20 `apply_mim_groundings.py` event that grounded three ingredients,
a 2026-08-31 ingredient repair event that restored `Fe(III)dicitrate`, and a
2026-08-31 medium-name repair event that restored `Defined freshwater medium
(CoCl2) + Electron Donors/Acceptors`; the generated record has none of those
updates.

## Evidence

Supported:

- MediaDB medium 390 denotes the CoCl2-defined freshwater medium plus
  electron donors/acceptors; the public page, public tab-delimited output, and
  maintained owner agree on the distinctive donor/acceptor set.
- The generated ingredient list preserves the 56.0 mM iron citrate, 5.0 mM
  ferric nitrilotriacetate, 20.0 mM nitrate, 30.0 mM fumarate, 10.0 mM
  glycolate, sugars, acetate, and lactate rows that distinguish MediaDB 390
  from the smaller Geobacter media.
- The merge history lists one source recipe, so this hash-suffixed output is
  not a false duplicate merge.

Unsupported or over-scoped:

- The generated record still carries `'''Fe(III` instead of the maintained
  owner's repaired `Fe(III)dicitrate` ingredient name.
- `Nitrate`, `Fumarate`, and `Glycolate` are ungrounded in the generated
  record even though the maintained owner now grounds them from the 2026-08-20
  MIM-published mappings.
- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- Both the generated record and the maintained owner repeat `Nicotinate` and
  `Magnesium sulfate` as duplicate rows, while the public MediaDB 390 page
  and tab-delimited export expose only one row for each compound.
- The three generic preparation steps are not supported by the inspected
  MediaDB 390 page or its tab-delimited compound export. The public pages do
  not state pH adjustment or a 0.22 um filtration step.

## Completeness

Consequential gaps:

- MediaDB 390 links `Albidiferax ferrireducens DMS 15236`, source 139
  (`Risso c et al, 2009`), and growth-data record 757. The generated YAML has
  no `target_organisms`, organism-scoped growth evidence, or Risso source
  reference.
- The generated merge omits the 2026-08-20 MIM grounding and both 2026-08-31
  repair history events present on its normalized owner.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 390 pages did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MIM groundings and MediaDB repairs. | Generated `original_name`, `media_term.term.label`, and `'''Fe(III` still contain parser-damaged values, and generated `Nitrate`, `Fumarate`, and `Glycolate` are ungrounded; the normalized owner has 2026-08-20 and 2026-08-31 events covering those fixes. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | The maintained owner has duplicate ingredient rows not present in MediaDB 390. | MediaDB 390 exposes one `Nicotinate` row and one `Magnesium sulfate` row; both the normalized owner and generated YAML repeat those two ingredients with identical concentrations. | `data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml` or the MediaDB import/enrichment path that populated this bare-stem owner. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 390 pages expose the compound table, organism, source, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 390 links `Albidiferax ferrireducens DMS 15236`, source 139, and growth-data 757; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml`. |

## Recommended Edits

- Remove the duplicate `Nicotinate` and `Magnesium sulfate` rows from
  `data/normalized_yaml/bacterial/defined_freshwater_medium_cocl2.yaml`.
- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__f0ffbcc6.yaml`
  from its normalized source so the 2026-08-20 MIM groundings and 2026-08-31
  MediaDB repairs propagate.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Risso-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 139, growth-data
  757, and the `Albidiferax ferrireducens DMS 15236` assertion with evidence
  scoped to MediaDB medium 390.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_cocl2__f0ffbcc6.yaml`.
- Revisit public MediaDB 390 and `/defined_media/media_text/390/` and confirm
  the regenerated record has 39 ingredients, with a single Nicotinate row, a
  single Magnesium sulfate row, and the 56.0 mM Fe(III)dicitrate row.

## Additional Notes

- Public MediaDB medium 390 and its tab-delimited export were reachable during
  review.
- The bounded `MEDIADB:390` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
