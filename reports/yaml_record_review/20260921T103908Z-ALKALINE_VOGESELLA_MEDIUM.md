# YAML Record Review: ALKALINE VOGESELLA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ALKALINE_VOGESELLA_MEDIUM.yaml`
- Started UTC: 2026-09-21T10:38:41Z
- Finished UTC: 2026-09-21T10:39:08Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ALKALINE_VOGESELLA_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001056` |
| Name | `alkaline_vogesella_medium` |
| Original name | `ALKALINE VOGESELLA MEDIUM` |
| Category | `bacterial` |
| Media term | `mediadive.medium:1581` / ALKALINE VOGESELLA MEDIUM |
| Generated from | `data/normalized_yaml/bacterial/alkaline_vogesella_medium.yaml` |

This is a generated merge record with one normalized DSMZ/MediaDive parent.
Future fixes belong in
`data/normalized_yaml/bacterial/alkaline_vogesella_medium.yaml` and then should
be regenerated into `data/merge_yaml/merged`.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALKALINE_VOGESELLA_MEDIUM.yaml` |
| Strict validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALKALINE_VOGESELLA_MEDIUM.yaml --out /private/tmp/ALKALINE_VOGESELLA_MEDIUM.strict.tsv --workers 1 --quiet` emitted 0 error rows |
| Reference validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALKALINE_VOGESELLA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 total checks |
| Term validator | Pass: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALKALINE_VOGESELLA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not a single embedded `MediaRecipe.curation_history` list in `data/merge_yaml/merged` |

The project-level `just validate-schema`, `just validate-strict`, and
`just validate-terms` wrappers currently fail before target-specific validation
because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`; the same LinkML and validator entry points were
therefore run through an offline `--no-project` Python 3.11 environment.

## Identity and Grounding

DSMZ Medium 1581 is ALKALINE VOGESELLA MEDIUM, matching the generated record's
media term, label, category, and liquid physical state. The one-source merge
lineage points directly to the maintained DSMZ/MediaDive normalized record for
that source.

The exact gitignore-independent search
`mediadive.medium:1581\b|DSMZ_Medium1581|alkaline_vogesella_medium|ALKALINE
VOGESELLA MEDIUM` covered `data/normalized_yaml`, `data/merge_yaml`, and
`data/import_tracking`. It found only this normalized source and this generated
merge as matching recipe records, with no same-label sibling variants in the
searched corpus.

## Evidence

- Supported: DSMZ Medium 1581 lists 0.50 g glucose, 3.00 g Na-pyruvate, 0.50 g
  Casamino acids, 3.00 g peptone, 3.00 g yeast extract, 2.83 g HEPES, 0.50 g
  KCl, 0.15 g CaCl2 x 2 H2O, 1.00 g NaCl, 0.62 g MgCl2 x 6 H2O, and 1000 ml
  distilled water, with pH adjusted to 8.0.
- Supported: the generated record's ChEBI groundings for glucose, sodium
  pyruvate, HEPES, potassium chloride, calcium chloride dihydrate, sodium
  chloride, and magnesium dichloride hexahydrate match the source labels at the
  chemical specificity used by the record.
- Correctly ungrounded: Casamino acids, peptone, and yeast extract are complex
  undefined components and should not receive a single ChEBI small-molecule
  grounding.
- Missing: the 1000 ml distilled-water row from DSMZ Medium 1581 is absent from
  both the generated merge and its normalized parent.

## Completeness

- All non-water ingredients from DSMZ Medium 1581 are present with the right
  numeric amounts.
- The pH 8.0 adjustment is present as both `ph_value` and a one-step
  `ADJUST_PH` preparation.
- Empty target-organism, temperature, atmosphere, storage, and growth-evidence
  slots are acceptable for this medium-level DSMZ source because the inspected
  source supplies no organism-specific growth claims or incubation conditions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Distilled water is missing. | DSMZ Medium 1581 lists 1000 ml distilled water; neither `data/normalized_yaml/bacterial/alkaline_vogesella_medium.yaml` nor the generated merge has a water row. | `data/normalized_yaml/bacterial/alkaline_vogesella_medium.yaml` |
| Minor | Source provenance is free text only. | The DSMZ PDF URL appears only in `notes`; there is no structured `references` list or per-claim evidence. | `data/normalized_yaml/bacterial/alkaline_vogesella_medium.yaml` |

## Recommended Edits

1. Add 1000 `ML_PER_L` distilled water to
   `data/normalized_yaml/bacterial/alkaline_vogesella_medium.yaml`.
2. Promote `DSMZ_Medium1581.pdf` into a structured reference or per-claim
   evidence field supported by the current schema.
3. Regenerate the merge layer so
   `data/merge_yaml/merged/ALKALINE_VOGESELLA_MEDIUM.yaml` inherits the
   repaired normalized source.

## Follow-up Checks

- Re-run open schema validation on the repaired normalized source and the
  regenerated merge.
- Re-run `scripts/validate_strict.py` on both files and confirm that it emits 0
  error rows.
- Re-run the term validator and reference validator after adding structured
  source links.
- Manually compare the regenerated record with `DSMZ_Medium1581.pdf` to confirm
  that all eleven source rows and pH 8.0 are present.

## Additional Notes

- No previous `ALKALINE_VOGESELLA_MEDIUM` review report existed in
  `reports/yaml_record_review`; this was checked with `find`, which includes
  gitignored report files.
