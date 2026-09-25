# YAML Record Review: magnetospirillum_gryphiswaldense_medium

- Repository: `CultureBotAI/CultureMech`
- Record: `data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__d93424fd.yaml`
- Started UTC: `2026-09-23T22:38:21Z`
- Finished UTC: `2026-09-23T22:38:21Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:010082` |
| Record name | `magnetospirillum_gryphiswaldense_medium` |
| Original name | `Magnetospirillum Gryphiswaldense Medium` |
| Source accession | `TOGO:M678` |
| Category | `bacterial` |
| Maintained input | `data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml` |
| Generated record | `data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__d93424fd.yaml` |

`data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__d93424fd.yaml`
is a generated merge from
`data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml`
with fingerprint
`d93424fd368eeac4310c357476d105fdd40ace2006c8691d40de51b62508a348`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__d93424fd.yaml` | Passed. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__d93424fd.yaml --out /private/tmp/magnetospirillum_gryphiswaldense_medium__d93424fd.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows emitted to `/private/tmp/magnetospirillum_gryphiswaldense_medium__d93424fd.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__d93424fd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks executed. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__d93424fd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: this validator targets standalone YAML files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged recipe YAML. |

## Identity and Grounding

- The source identity points to a real TOGO derivative of JCM medium 660. The
  TOGO `M678` API returns `JCM_M660-2`, the JCM medium 660 URL, the same base
  Magnetospirillum gryphiswaldense formulation, and an added 1 g/L agar row
  derived from JCM's semisolid-medium comment for strain JCM 21280.
- `CultureMech:010082` is a unique active ID in the current corpus. An
  ignored-file-inclusive exact search for `CultureMech:010082` across `data`,
  `src`, `reports`, and `.claude` found this maintained input, this generated
  merge, current catalog/index entries, and historical import reports. It did
  not find another live maintained record with this ID.
- `TOGO:M678` is unique to this record. An ignored-file-inclusive exact search
  for that CURIE across `data`, `src`, `reports`, and `.claude` found only this
  maintained input, this generated merge, and derived indexes/reports.
- An ignored-file-inclusive exact search for `JCM_M660-2` across
  `data/normalized_yaml`, `data/merge_yaml`, import-tracking reports,
  `reports/media_content_review_manifest.tsv`, and `reports/archive` found only
  this maintained input and this generated record.

## Evidence

- TOGO `M678` supports the row set imported here: distilled water 1 L,
  `MgSO4 x 7 H2O` 0.1 g, `NH4Cl` 0.1 g, `K2HPO4` 0.5 g, sodium acetate 1 g,
  ferric citrate 6 mg, agar 1 g/L, yeast extract 0.1 g, and sodium
  thioglycolate 0.5 g.
- The source has a pH comment, `Adjust pH to 6.8.`, but the generated record has
  no `ph_value` and no preparation step for the pH adjustment.
- The original JCM page says media should be autoclaved at 121 C for 15 minutes
  unless otherwise stated. This JCM default sterilization instruction is absent.
- TOGO `M678` represents agar as `1 g/L` for a semisolid variant. The generated
  record keeps `1 G_PER_L`, but maps the physical state to `SOLID_AGAR` instead
  of `SEMISOLID`.
- The ferric citrate row has a 1000x unit error: TOGO and JCM state 6 mg, while
  the generated row is `6 G_PER_L`.
- Distilled water is a 1 L solvent/final-volume row in TOGO and JCM. The
  generated row incorrectly treats it as `1 G_PER_L`.
- The source-specific target organism is missing. `M678` exists because the JCM
  page states that strain JCM 21280 grows well in semisolid medium with 1 g/L
  agar, but the generated record has no target organism or strain note.

## Completeness

- Consequentially incomplete: the pH 6.8 adjustment and JCM default autoclave
  step are absent from `preparation_steps`.
- Consequentially incomplete: the semisolid state is not represented exactly.
- Consequentially incomplete: no structured target-organism entry preserves the
  source-stated JCM 21280 strain context.
- Empty optional growth-evidence fields were not treated as defects. TOGO and
  JCM provide recipe and strain-use context, not quantitative growth metrics.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Ferric citrate is off by 1000x. | TOGO `M678` and JCM medium 660 state 6 mg ferric citrate per liter; the generated YAML stores `Ferric citrate` as `6 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml` and the TOGO unit-conversion transform. |
| Major | Distilled water is modeled as mass concentration. | The source says 1 L distilled water; the generated YAML stores `Distilled water` at `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml` and the TOGO final-volume import transform. |
| Major | pH and sterilization instructions are absent. | TOGO preserves the pH 6.8 comment and JCM provides a default 121 C, 15 minute autoclave instruction; the record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml` and the TOGO/JCM comment importer. |
| Major | The semisolid variant is typed as solid agar. | The source-specific agar addition is 1 g/L for semisolid growth of strain JCM 21280; the generated `physical_state` is `SOLID_AGAR`. | `data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml` and agar-to-physical-state normalization. |
| Minor | The source-stated JCM 21280 strain context is missing. | The agar-bearing `M678` derivative exists only because JCM says JCM 21280 grows well in semisolid medium with 1 g/L agar, but the record has no target-organism entry or preparation note for that strain. | `data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml`. |
| Minor | Structured source provenance is missing. | TOGO, the original JCM source name, and the original JCM URL appear only in `media_term`, `notes`, and history; no structured `sources` or `references` entries are available for reference validation. | `data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml` if structured source provenance is adopted for TOGO imports. |

## Recommended Edits

1. Convert ferric citrate to 0.006 g/L or preserve it as 6 mg/L in
   `data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml`.
2. Remove distilled water from the concentration ingredient list or represent it
   as final volume rather than `1 G_PER_L`.
3. Add `ph_value: 6.8`, the pH adjustment step, and JCM's default autoclave
   condition.
4. Change `physical_state` from `SOLID_AGAR` to `SEMISOLID`.
5. Preserve the JCM 21280 strain context for the 1 g/L agar variant.
6. Add structured TOGO and JCM provenance if this importer supports source
   fields.
7. Regenerate `data/merge_yaml/merged/` after the normalized-source repair.

## Follow-up Checks

- Run open-schema validation for the corrected normalized record and generated
  merge:
  `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe <record>`.
- Run strict validation for the corrected normalized record and generated
  merge: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py <record> --out /private/tmp/<record>.strict.tsv --workers 1 --quiet`.
- Run reference validation after adding structured TOGO/JCM provenance.
- Run term validation after removing or remapping distilled water and ferric
  citrate.
- Manually compare the regenerated YAML to TOGO `M678` and the JCM 660 page for
  the ferric citrate unit, the agar unit, pH 6.8, default autoclaving, and the
  JCM 21280 semisolid comment.

## Additional Notes

- TOGO `M677` is the sibling liquid import from original ID `JCM_M660`.
  `M678` is the semisolid `JCM_M660-2` derivative and should stay distinct, but
  it shares the same ferric citrate and distilled-water import hazards.
