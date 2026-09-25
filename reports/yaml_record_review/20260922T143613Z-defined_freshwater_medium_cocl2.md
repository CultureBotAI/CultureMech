# YAML Record Review: defined_freshwater_medium_cocl2

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/defined_freshwater_medium_cocl2.yaml
- Started UTC: 2026-09-22T14:28:38Z
- Finished UTC: 2026-09-22T14:36:13Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007348` for
`defined_freshwater_medium_cocl2`.

- Generated record: `data/merge_yaml/merged/defined_freshwater_medium_cocl2.yaml`
- Maintained canonical owner: `data/normalized_yaml/bacterial/MEDIADB_444_Defined_freshwater_medium_CoCl2.yaml`
- Maintained concentration-variant owners:
  `data/normalized_yaml/bacterial/MEDIADB_447_Defined_freshwater_medium_CoCl2.yaml`,
  `data/normalized_yaml/bacterial/MEDIADB_451_Defined_freshwater_medium_CoCl2.yaml`,
  and `data/normalized_yaml/bacterial/MEDIADB_455_Defined_freshwater_medium_CoCl2.yaml`
- Class: `MediaRecipe`
- Source identity in the generated record: `MEDIADB:444`
- Generated merge fingerprint:
  `c1e57ec062a8f0a72817c54424c2272fe1461d445d07ed0259a52f235456f171`

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/defined_freshwater_medium_cocl2.yaml` | Passed with no issues. |
| Strict schema, `python scripts/validate_strict.py data/merge_yaml/merged/defined_freshwater_medium_cocl2.yaml --out /private/tmp/defined_freshwater_medium_cocl2.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/defined_freshwater_medium_cocl2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/defined_freshwater_medium_cocl2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with exit code 0. |
| Embedded `curation_history` history validation | Not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

`just` wrappers were not used because this environment resolves the project
through Python 3.13 and attempts to build `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 through the populated
`/private/tmp/uv-cache-culturemech-review` cache.

## Identity and Grounding

The generated record currently mixes one source identity with four source
records:

| Record | MediaDB term | Public MediaDB identity | Distinguished values |
|---|---|---|---|
| Generated merge | `MEDIADB:444` | Stale/truncated as `'''Defined freshwater medium (CoCl2` | Acetate 113.2 mM; ferric oxide 100.0 mM |
| Maintained 444 | `MEDIADB:444` | `Defined freshwater medium (CoCl2) + 100 mM Fe2O3 + 113.2 mM Acetate` | Acetate 113.2 mM; ferric oxide 100.0 mM |
| Maintained 447 | `MEDIADB:447` | `Defined freshwater medium (CoCl2) + 250 mM Fe2O3 + 113.2 mM Acetate` | Acetate 113.2 mM; ferric oxide 250.0 mM; `high_metal: true` |
| Maintained 451 | `MEDIADB:451` | `Defined freshwater medium (CoCl2) + 100 mM Fe2O3 + 50 mM Acetate` | Acetate 50.0 mM; ferric oxide 100.0 mM |
| Maintained 455 | `MEDIADB:455` | `Defined freshwater medium (CoCl2) + 100 mM Fe2O3 + 10 mM Acetate` | Acetate 10.0 mM; ferric oxide 100.0 mM |

The generated ingredients and `media_term` denote MediaDB medium 444, and the
generated `variant_children` also list 447, 451, and 455 as concentration
variants of 444. Those same three maintained records point back to 444 as
`CONCENTRATION_VARIANT` children. The duplicate-merge history and `merged_from`
array nevertheless say 447, 451, and 455 were merged into 444 as duplicate
source recipes. That internal contradiction is the main defect.

The public MediaDB pages for `/defined_media/media/444/`, `/447/`, `/451/`,
and `/455/` still resolve as distinct medium records with the same mM
differences modeled in the normalized YAML. The public 444 tab-delimited page
also lists the 29 compounds and amounts used by the maintained 444 recipe.

The generated record is stale relative to its maintained 444 owner: the
normalized file contains a 2026-08-31 `repair_mediadb_names.py` event and a
restored `original_name` / `media_term.term.label`, while the generated merge
still has the earlier parser-damaged name.

## Evidence

Supported:

- MediaDB medium 444 has 29 mM-scale compounds, including acetate at
  113.2 mM and ferric oxide at 100.0 mM; the generated 444 ingredient values
  match those two values and the public MediaDB 444 table.
- The normalized 444, 447, 451, and 455 records all model the four MediaDB
  pages as concentration variants that vary acetate and/or ferric oxide while
  keeping the same base ingredient signature.
- The generated `MediaRecipe` kept 444 as the canonical ID and kept the 444
  acetate/ferric oxide values.

Unsupported or over-scoped:

- `curation_history` claims that 447, 451, and 455 were duplicate recipes of
  444. The maintained YAML and the live MediaDB pages both distinguish the
  recipes by concentration.
- `merged_from` repeats the same false duplicate assertion by listing the
  three concentration variants as source records folded into 444.
- `original_name` and `media_term.term.label` in the generated merge are
  stale, parser-damaged strings; the maintained 444 owner has the repaired
  MediaDB label.
- The generic preparation steps claim to dissolve all ingredients, adjust pH
  if specified, and filter-sterilize through 0.22 um. The inspected public
  MediaDB 444 page and tab-delimited page list compounds, amounts, organism,
  source, and growth-data links; they do not specify a pH or filter
  sterilization procedure.

## Completeness

Consequential gaps:

- MediaDB 444 links `Geobacter metallireducens` as its organism, Lovley et al.
  1993 as its source, and growth-data record 831 for the organism/medium pair.
  The generated record lacks `target_organisms`, source-specific growth
  evidence, and a narrow reference to the Lovley source.
- The generated merge does not contain the 2026-08-31 MediaDB name-repair
  curation event that is present on `MEDIADB_444_Defined_freshwater_medium_CoCl2.yaml`.
- A gitignore-independent search over `data/raw`, `data/import_tracking`,
  `data/normalized_yaml`, and `data/merge_yaml` for the four exact MediaDB
  accessions and the CoCl2 label found the normalized owners, generated merge,
  generated indexes, and MediaDB-derived normalized CoCl2 siblings. It did not
  find an authoritative per-record raw capture or
  `media_database.07Oct2015.sql` under `data/raw`, so the restored labels were
  checked against the public MediaDB pages rather than re-parsed from the
  archived SQL dump.

Empty optional fields not treated as defects:

- No salinity, temperature, atmosphere, or storage fields were flagged solely
  because they are empty; the inspected MediaDB 444 pages did not expose those
  protocol details.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | `MEDIADB:447`, `MEDIADB:451`, and `MEDIADB:455` were merged into `MEDIADB:444` as duplicate recipes even though they are concentration variants. | The generated `merged_from` and merge history list all four records under one fingerprint, while the normalized records and the public MediaDB pages distinguish 447 by 250.0 mM ferric oxide, 451 by 50.0 mM acetate, and 455 by 10.0 mM acetate. | Merge fingerprinting / duplicate-selection logic, then regeneration of `data/merge_yaml/merged/defined_freshwater_medium_cocl2.yaml`. |
| Major | The generated record is stale relative to `MEDIADB:444`'s maintained name repair. | The generated `original_name` and `media_term.term.label` still contain the truncated `'''Defined freshwater medium (CoCl2`; normalized 444 has the repaired full 444 label from the 2026-08-31 `repair_mediadb_names.py` event. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/` after ensuring merge freshness catches stale generated records. |
| Major | The record contains unsupported generic preparation steps. | MediaDB 444 exposes the compound table, organism, source, and growth-data link, but the inspected MediaDB 444 pages do not state pH adjustment or 0.22 um filter sterilization. | `data/normalized_yaml/bacterial/MEDIADB_444_Defined_freshwater_medium_CoCl2.yaml` or the MediaDB import/enrichment logic that seeded generic `preparation_steps`. |
| Major | The MediaDB organism, source, and growth-data assertions were not imported. | The public MediaDB 444 page links `Geobacter metallireducens`, source 131, and growth-data 831; the generated YAML has no `target_organisms`, growth evidence, or Lovley et al. source reference. | MediaDB importer/enrichment path that owns `data/normalized_yaml/bacterial/MEDIADB_444_Defined_freshwater_medium_CoCl2.yaml`. |

## Recommended Edits

- Correct merge fingerprinting so concentration variants are not selected as
  duplicate source recipes merely because their ingredient identities match.
  Regenerate this merged record and confirm `MEDIADB:447`, `MEDIADB:451`, and
  `MEDIADB:455` no longer appear in `merged_from`.
- Regenerate merged YAML from the repaired normalized MediaDB records so the
  canonical 444 output carries
  `Defined freshwater medium (CoCl2) + 100 mM Fe2O3 + 113.2 mM Acetate`
  instead of the stale parser-damaged label.
- Replace or remove the generic imported `preparation_steps` unless a checked
  source is found for pH adjustment and 0.22 um filter sterilization of this
  medium.
- Extend the MediaDB owner or importer to preserve source 131, growth-data
  831, and the `Geobacter metallireducens` organism assertion with evidence
  scoped to MediaDB medium 444.

## Follow-up Checks

- Re-run `just verify-merges` and `just audit-merge-freshness` after changing
  merge rules or regenerating `data/merge_yaml/merged/`.
- Re-run the focused open-schema, strict, reference, and term validators on the
  regenerated `defined_freshwater_medium_cocl2.yaml`.
- Compare the regenerated canonical against the public MediaDB 444 page and
  the tab-delimited `/defined_media/media_text/444/` output to confirm all 29
  compound names and mM amounts still match.
- Revisit public MediaDB pages 447, 451, and 455 and verify they remain linked
  only as concentration variants, not duplicate merge sources.

## Additional Notes

- Public MediaDB records 444, 447, 451, and 455 were reachable during the
  review.
- The gitignore-independent source search deliberately covered only the
  relevant data subtrees after an earlier too-broad exploratory search included
  generated HTML and reports.
- This was a read-only review; no YAML record, merge logic, generated page, or
  GitHub issue was edited.
