# YAML Record Review: defined_freshwater_medium_cocl2__0cf425f7

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2__0cf425f7.yaml
- Started UTC: 2026-09-22T14:36:14Z
- Finished UTC: 2026-09-22T14:38:55Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007358` for
`defined_freshwater_medium_cocl2`.

- Generated record:
  `data/merge_yaml/merged/defined_freshwater_medium_cocl2__0cf425f7.yaml`
- Maintained owner:
  `data/normalized_yaml/bacterial/MEDIADB_453_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identity: `MEDIADB:453`
- Merge fingerprint:
  `0cf425f7438845049e215a59595407cb4cdbb3fd683c3630c8cff04c078af9a9`
- Merge shape: single source, `MEDIADB_453_Defined_freshwater_medium_CoCl2`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2__0cf425f7.yaml` | Passed with no issues. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2__0cf425f7.yaml --out /private/tmp/defined_freshwater_medium_cocl2__0cf425f7.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2__0cf425f7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2__0cf425f7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

The focused validators were run offline with Python 3.11 through
`/private/tmp/uv-cache-culturemech-review`; project `just` validators were not
used because this checkout attempts to build `llvmlite==0.46.0` under
Python 3.13.

## Identity and Grounding

The source identity is singular and internally stable: the generated record
has `id: CultureMech:007358`, `media_term.term.id: MEDIADB:453`, and
`merged_from: MEDIADB_453_Defined_freshwater_medium_CoCl2`. A
gitignore-independent search over `data/normalized_yaml` and `data/merge_yaml`
for `MEDIADB:453` and the exact normalized owner stem found only the generated
record, the maintained owner, and generated indexes.

The public MediaDB 453 page resolves as `Defined freshwater medium (cocl2) +
100 mm fe2o3 + 20 mm ethanol`; its table contains the same distinctive
20.0 mM ethanol and 100.0 mM ferric oxide values found in this YAML.

The generated record is stale relative to its maintained owner. The
normalized `MEDIADB_453_Defined_freshwater_medium_CoCl2.yaml` file has a
2026-08-31 `repair_mediadb_names.py` event and the restored
`Defined freshwater medium (CoCl2) + 100 mM Fe2O3 + 20 mM Ethanol` label, but
the generated record still carries the older parser-damaged
`'''Defined freshwater medium (CoCl2` in both `original_name` and
`media_term.term.label`.

## Evidence

Supported:

- MediaDB medium 453 denotes the 100 mM Fe2O3 / 20 mM ethanol member of the
  CoCl2-defined freshwater medium set; the public MediaDB page and the
  maintained owner agree on those distinctive concentrations.
- The generated ingredients preserve the 29-compound MediaDB 453 formulation
  and keep `Ethanol` grounded to `CHEBI:16236`.
- The merge history for this hash-suffixed output lists one source recipe, so
  this record does not repeat the adjacent canonical 444 duplicate-merge
  collapse.

Unsupported or over-scoped:

- `original_name` and `media_term.term.label` are stale generated values that
  no longer match the maintained normalized record or the live MediaDB page.
- The three generic preparation steps are not supported by the inspected
  MediaDB 453 page. MediaDB 453 lists a compound table, organism, source, and
  growth-data link, but not a pH-adjustment instruction or a 0.22 um
  filtration step.

## Completeness

Consequential gaps:

- The public MediaDB 453 page links `Geobacter metallireducens`, source 131
  (`Lovley dr et al, 1993`), and growth-data record 840 for the
  organism/medium pair. The generated YAML has no `target_organisms`,
  organism-scoped growth evidence, or Lovley source reference.
- The generated merge omits the 2026-08-31 name-repair history event present
  on its normalized owner.
- A `find data -name media_database.07Oct2015.sql` search included ignored
  files and found no archived MediaDB SQL dump under `data`; this review
  therefore checked the restored 453 identity against the maintained owner and
  public MediaDB page rather than re-parsing the archival SQL source.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 453 page did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is stale relative to the maintained MediaDB name repair. | Generated `original_name` and `media_term.term.label` still contain `'''Defined freshwater medium (CoCl2`; the normalized owner has the 2026-08-31 repair event and the full MediaDB 453 label. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` and ensure merge-freshness checks catch stale generated outputs. |
| Major | Generic preparation steps assert unsupported pH adjustment and filter sterilization. | The inspected public MediaDB 453 page exposes the compound table, organism, source, and growth-data link, but not pH or sterilization instructions. | `data/normalized_yaml/bacterial/MEDIADB_453_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | Public MediaDB 453 links `Geobacter metallireducens`, source 131, and growth-data 840; the generated YAML has no `target_organisms` or growth-evidence block. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_453_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/defined_freshwater_medium_cocl2__0cf425f7.yaml`
  from its normalized source so the 2026-08-31 MediaDB name repair propagates.
- Replace or remove the generic imported `preparation_steps` unless a checked
  MediaDB or Lovley-source protocol supports pH adjustment and 0.22 um filter
  sterilization for this medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  840, and the `Geobacter metallireducens` assertion with evidence scoped to
  MediaDB medium 453.

## Follow-up Checks

- Re-run `just audit-merge-freshness` after regenerating generated merged YAML.
- Re-run the focused open-schema, strict, reference, and term validators on
  `defined_freshwater_medium_cocl2__0cf425f7.yaml`.
- Revisit the public MediaDB 453 page and confirm the regenerated record still
  contains exactly the 20.0 mM ethanol and 100.0 mM ferric oxide formulation
  for `MEDIADB:453`.

## Additional Notes

- Public MediaDB medium 453 was reachable during review.
- The bounded `MEDIADB:453` source-owner search included ignored files in
  `data/normalized_yaml` and `data/merge_yaml`.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
