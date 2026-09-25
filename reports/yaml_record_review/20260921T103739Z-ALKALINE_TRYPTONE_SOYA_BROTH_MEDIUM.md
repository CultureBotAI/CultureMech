# YAML Record Review: Alkaline Tryptone Soya Broth Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml`
- Started UTC: 2026-09-21T10:37:01Z
- Finished UTC: 2026-09-21T10:37:39Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010198` |
| Name | `alkaline_tryptone_soya_broth_medium` |
| Original name | `Alkaline Tryptone Soya Broth Medium` |
| Category | `bacterial` |
| Media term | `TOGO:M789` / Alkaline Tryptone Soya Broth Medium |
| Generated from | `data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml` |

This is a generated merge record with one normalized parent. The maintained TOGO
M789 parent and the direct MediaDive/JCM parent were both repaired on
2026-09-11; this generated record is stale relative to those maintained inputs.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml` |
| Strict validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml --out /private/tmp/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.strict.tsv --workers 1 --quiet` emitted 0 error rows |
| Reference validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 total checks |
| Term validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not a single embedded `MediaRecipe.curation_history` list in `data/merge_yaml/merged` |

The project-level `just validate-schema`, `just validate-strict`, and
`just validate-terms` wrappers currently fail before target-specific validation
because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`; the same LinkML and validator entry points were
therefore run through an offline `--no-project` Python 3.11 environment.

## Identity and Grounding

TOGO M789 identifies JCM Medium 763 Alkaline Tryptone Soya Broth Medium. The
live JCM `GRMD=763` endpoint now returns a `Nothing found` page, but the TOGO
M789 API is available and internally cites the same JCM accession. The repaired
TOGO M789 parent points to the direct MediaDive J763 parent
`data/normalized_yaml/bacterial/alkaline_tryptone_soya_broth_medium.yaml`; both
maintained records now describe the same liquid JCM 763 recipe.

The exact gitignore-independent search
`TOGO:M789\b|JCM_M763\b|GRMD=763\b|TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium|Alkaline
Tryptone Soya Broth Medium|alkaline_tryptone_soya_broth_medium` covered
`data/normalized_yaml`, `data/merge_yaml`, and `data/import_tracking`. It found
this TOGO M789 generated record, its repaired TOGO parent, the repaired
MediaDive J763 parent, and TOGO M790, which is the 20 g/L agar solid variant
and should remain separate.

## Evidence

- Supported by TOGO M789: the liquid medium contains 30 g/L Oxoid Tryptone soya
  broth in 1 L distilled water.
- Supported by TOGO M789: after cooling, the pH should be adjusted to 8.5-9.0
  with sterile autoclaved 20% sodium carbonate solution; that solution is a
  variable pH adjuster, not a fixed-volume stock addition.
- Correct upstream: the current normalized TOGO M789 and MediaDive J763 parents
  already encode `1000.0 ML_PER_L` water, the pH 8.5-9.0 range, a nested 20%
  sodium carbonate solution with Na2CO3 at `20.0 PERCENT_W_V`, basal-medium and
  sodium-carbonate autoclaving, post-cooling pH adjustment, source links, and a
  source-duplicate relationship to one another.
- Not supported in the generated merge: distilled water is still `1 G_PER_L`,
  the sodium carbonate solution remains an empty `VARIABLE` stub, and no pH,
  sterilization, or pH-adjustment step has been regenerated.

## Completeness

- The liquid ingredient set is minimal by design: Oxoid Tryptone soya broth is
  a complex dehydrated medium row and should not be expanded into Wikipedia- or
  vendor-derived constituent rows.
- The generated record is complete only in identity. It is missing the repaired
  stock composition, pH range, autoclave/pH-adjustment steps, references,
  source annotations, and source-duplicate relationship from its normalized
  parent.
- Empty target-organism, temperature, atmosphere, storage, and growth-evidence
  slots are acceptable for this import because neither TOGO M789 nor the
  inspected parent records supply organism-specific growth claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge is stale relative to its repaired normalized TOGO parent. | `TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml` has a 2026-09-11 repair that corrected water to `1000.0 ML_PER_L`, nested 20% sodium carbonate, added pH 8.5-9.0 and preparation steps, and added references; the generated merge still has `1 G_PER_L` water, an empty sodium-carbonate solution, and no pH or preparation steps. | Regenerate `data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml` from the current normalized TOGO source |
| Minor | The generated record still has only free-text source provenance. | The repaired normalized parent has `references` for TOGO M789 and MediaDive J763, but the generated merge predates that change and only cites TOGO/JCM in `notes`. | Merge regeneration |

## Recommended Edits

1. Regenerate the merge layer from the current
   `data/normalized_yaml/bacterial/TOGO_M789_Alkaline_Tryptone_Soya_Broth_Medium.yaml`
   so the generated target inherits the September 2026 repair.
2. Confirm that the regenerated record keeps TOGO M789 as the liquid recipe and
   does not merge in TOGO M790's 20 g/L agar solid variant.
3. Confirm that the regenerated record carries `1000.0 ML_PER_L` water, 30.0
   `G_PER_L` Tryptone soya broth, a nested 20% sodium carbonate pH adjuster,
   pH 8.5-9.0, autoclaving, and post-cooling pH adjustment.

## Follow-up Checks

- Re-run open schema validation on the regenerated
  `data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml`.
- Re-run `scripts/validate_strict.py` on the regenerated merge and confirm that
  it emits 0 error rows.
- Re-run the term validator and reference validator on the regenerated merge.
- Manually compare the regenerated merge against TOGO M789 and the repaired
  normalized TOGO parent to confirm that the merge now reflects the maintained
  2026-09-11 repair.

## Additional Notes

- No previous `ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM` review report existed in
  `reports/yaml_record_review`; this was checked with `find`, which includes
  gitignored report files.
- This review found a stale generated artifact, not an unfixed normalized
  source. Do not patch `data/merge_yaml/merged/ALKALINE_TRYPTONE_SOYA_BROTH_MEDIUM.yaml`
  directly.
