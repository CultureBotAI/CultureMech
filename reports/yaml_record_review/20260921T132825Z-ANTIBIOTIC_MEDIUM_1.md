# YAML Record Review: antibiotic_medium_1

- Repository: CultureMech
- Record: data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml
- Started UTC: 2026-09-21T13:27:26Z
- Finished UTC: 2026-09-21T13:28:25Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:001010 |
| Label | antibiotic_medium_1 |
| Original label | ANTIBIOTIC MEDIUM 1 |
| Source term | mediadive.medium:1532 |
| Maintained owner | data/normalized_yaml/bacterial/antibiotic_medium_1.yaml |
| Generated record | data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml |

This is a generated merge record derived from one normalized DSMZ/MediaDive
owner. Future fixes should land in
`data/normalized_yaml/bacterial/antibiotic_medium_1.yaml` or the DSMZ import
mapping that produced it, then the generated merge should be rebuilt.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml` returned `No issues found`. |
| Strict schema | Passed: `scripts/validate_strict.py data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml --workers 1 --quiet` scanned 1 file and emitted 0 error rows. |
| References | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` found 0 active checks and reported all validations passed. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/ANTIBIOTIC_MEDIUM_1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone files under `history/`, not a focused validator for one embedded `MediaRecipe.curation_history` block in a generated merge. |

The repository's documented `just validate-schema`, `just validate-strict`,
`just validate-references`, and `just validate-terms` wrappers are currently
blocked before target-specific validation by the project `uv` environment
attempting to build `llvmlite==0.46.0` under Python 3.13 and failing inside
`setuptools` with `TypeError: Popen.__init__() got an unexpected keyword
argument 'dry_run'`. The equivalent validators above were run through
`uv --no-project` on Python 3.11 with the same schema and target file.

## Identity and Grounding

The record correctly identifies DSMZ Medium 1532, `ANTIBIOTIC MEDIUM 1`; the
current DSMZ PDF is live and carries the same number and title.

The defined glucose and agar rows are exactly grounded to ChEBI. Yeast extract,
Beef extract, Pancreatic digest of casein, and Peptone are complex ingredients
whose non-ChEBI local terms do not create a formulation mismatch.

## Evidence

The inspected DSMZ PDF fully supports the represented ingredient list: 3.0 g
Yeast extract, 1.5 g Beef extract, 4.0 g Pancreatic Digest of Casein, 6.0 g
Peptone, 1.0 g Glucose, and 20.0 g Agar. It also supports the solid-agar
physical state, undefined/complex classification, and generic microbial
cultivation use.

The PDF supports final pH 6.55 and has a product alternative note for Difco
Antibiotic Medium 1. The generated record preserves both pieces of text, but
also rounds the structured `ph_value` to 6.5.

## Completeness

No ingredient, water, source duplicate, or source-specific preparation step was
missing from the inspected DSMZ recipe. The PDF does not name a target organism
or strain, so the empty `target_organisms` slot is not a defect.

An ignored-inclusive exact search for
`CultureMech:001010|mediadive.medium:1532|DSMZ_Medium1532|antibiotic_medium_1|ANTIBIOTIC_MEDIUM_1`
covered `data`, `src`, `reports`, `.claude`, `CLAUDE.md`, and `justfile`.
It found the normalized owner, the generated merge, registry/catalog/index
rows, and historical validation reports only.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| minor | The exact source pH is rounded in the structured field. | DSMZ 1532 states pH 6.55; the record has `ph_value: 6.5`, while the generated `preparation_steps[0].description` still says `pH 6.55`. | `data/normalized_yaml/bacterial/antibiotic_medium_1.yaml`; DSMZ import mapping |
| minor | Two source comments are encoded as generic `MIX` actions. | `pH 6.55` is a final pH statement, and `or Difco Antibiotic Medium 1 (BD, order number 226340)` is an alternative-product note, not recipe mixing instructions. | `data/normalized_yaml/bacterial/antibiotic_medium_1.yaml`; DSMZ comment-to-step mapping |

## Recommended Edits

1. Preserve the exact final pH as 6.55 in the structured pH field if the schema
   accepts the value.
2. Reclassify the pH and Difco product comments as a final-pH statement and a
   note or source alternative instead of `MIX` preparation steps.

## Follow-up Checks

- Re-run `just validate data/normalized_yaml/bacterial/antibiotic_medium_1.yaml`,
  `just validate-strict data/normalized_yaml/bacterial/antibiotic_medium_1.yaml`,
  `just validate-terms data/normalized_yaml/bacterial/antibiotic_medium_1.yaml`,
  and `just validate-references data/normalized_yaml/bacterial/antibiotic_medium_1.yaml`
  after the normalized owner or importer is changed.
- Re-run `just verify-merges` after regenerating `data/merge_yaml/merged/`.
- Manually compare the regenerated record against DSMZ Medium 1532 to verify
  the six ingredients and final pH 6.55 are unchanged.

## Additional Notes

None found.
