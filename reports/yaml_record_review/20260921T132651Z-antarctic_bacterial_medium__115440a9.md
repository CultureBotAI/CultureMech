# YAML Record Review: antarctic_bacterial_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/antarctic_bacterial_medium__115440a9.yaml
- Started UTC: 2026-09-21T13:26:32Z
- Finished UTC: 2026-09-21T13:26:52Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:002690 |
| Label | antarctic_bacterial_medium |
| Original label | ANTARCTIC BACTERIAL MEDIUM |
| Source term | mediadive.medium:J331 |
| Maintained owner | data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml |
| Generated record | data/merge_yaml/merged/antarctic_bacterial_medium__115440a9.yaml |

This is a generated merge record derived from one normalized MediaDive/JCM
owner. Future fixes should land in
`data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml` or the
MediaDive/JCM import mapping that produced it, then the generated merge should
be rebuilt.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/antarctic_bacterial_medium__115440a9.yaml` returned `No issues found`. |
| Strict schema | Passed: `scripts/validate_strict.py data/merge_yaml/merged/antarctic_bacterial_medium__115440a9.yaml --workers 1 --quiet` scanned 1 file and emitted 0 error rows. |
| References | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/antarctic_bacterial_medium__115440a9.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` found 0 active checks and reported all validations passed. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/antarctic_bacterial_medium__115440a9.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone files under `history/`, not a focused validator for one embedded `MediaRecipe.curation_history` block in a generated merge. |

The repository's documented `just validate-schema`, `just validate-strict`,
`just validate-references`, and `just validate-terms` wrappers are currently
blocked before target-specific validation by the project `uv` environment
attempting to build `llvmlite==0.46.0` under Python 3.13 and failing inside
`setuptools` with `TypeError: Popen.__init__() got an unexpected keyword
argument 'dry_run'`. The equivalent validators above were run through
`uv --no-project` on Python 3.11 with the same schema and target file.

## Identity and Grounding

The record identifies MediaDive/JCM medium J331, `ANTARCTIC BACTERIAL MEDIUM`.
The current JCM `GRMD=331` page returns `Nothing found`, so the live JCM page
cannot directly verify the MediaDive accession. TOGO Medium M326 still records
the same title, the same JCM M331 original source, the same pH 6.9, and the
same three non-water ingredient amounts, which supports the local identity as a
same-source copy.

The agar row is exactly grounded to `CHEBI:2509`. Bacto peptone and Yeast
extract are complex ingredients; their absence of ChEBI `term` values in the
generated merge is not a defect.

## Evidence

The live TOGO copy of JCM M331 supports 5 g/L Bacto peptone, 1 g/L Yeast
extract, 15 g/L agar, 1 L water, and pH 6.9. The generated MediaDive/JCM record
preserves the three non-water ingredient amounts, the pH value, and the pH
adjustment step.

The TOGO copy also demonstrates that the source formulation has an explicit 1 L
distilled-water row. That row is missing from the MediaDive/JCM record.

## Completeness

The water/final-volume component is missing. The current JCM page is
source-rotted, so no JCM preparation text beyond the pH 6.9 adjustment could be
checked against the original page.

An ignored-inclusive exact search for
`CultureMech:002690|mediadive.medium:J331|antarctic_bacterial_medium__115440a9|Source: JCM, ID: J331`
covered `data`, `src`, `reports`, `.claude`, `CLAUDE.md`, and `justfile`.
It found the normalized MediaDive owner, generated merge, registry/catalog
rows, generated indexes, prior validation reports, and the prior review of the
TOGO sibling, but no third maintained owner for MediaDive `J331`.

The separate ignored-inclusive search for JCM `GRMD=331` during the TOGO M326
review found the duplicate TOGO owner at
`data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml`.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| major | The JCM formulation's water/final-volume row is absent. | TOGO's copy of JCM M331 has `Distilled water 1 L`; the MediaDive/JCM record has only Bacto peptone, Yeast extract, and Agar. | `data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml`; MediaDive/JCM import mapping |
| minor | The generated record carries a stale `kg_microbe_match`. | The record's source identity is `mediadive.medium:J331`, but `kg_microbe_match` is `mediadive.medium:12`, a shared stale value found across many unrelated imported records. | `data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml`; KG-Microbe match assignment |
| minor | The same JCM M331 source is present as a second unmerged TOGO record. | `data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml` stores TOGO M326 and the same JCM `GRMD=331` source. | Merge fingerprinting after TOGO and MediaDive source normalization |

## Recommended Edits

1. Restore the `Distilled water 1 L` source row, represented as an explicit
   final volume or water volume rather than omitting it.
2. Remove or correct the stale `kg_microbe_match: mediadive.medium:12` value.
3. After the TOGO owner and MediaDive owner agree on pH and water/final-volume
   representation, regenerate merges and verify whether the duplicate records
   collapse into one canonical generated recipe.

## Follow-up Checks

- Re-run `just validate data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml`,
  `just validate-strict data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml`,
  `just validate-terms data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml`,
  and `just validate-references data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml`
  after the normalized owner or importer is changed.
- Re-run `just verify-merges` after regenerating `data/merge_yaml/merged/`.
- Re-run an ignored-inclusive exact search for JCM `GRMD=331`, `TOGO:M326`, and
  `mediadive.medium:J331` before closing the duplicate-record follow-up.

## Additional Notes

The current JCM `GRMD=331` endpoint returned `Nothing found`, so the reviewed
record's source URL is no longer enough to recover the original JCM page. TOGO
M326 remains the usable source copy for this JCM formulation.
