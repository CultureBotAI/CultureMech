# YAML Record Review: antarctic_bacterial_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml
- Started UTC: 2026-09-21T13:25:08Z
- Finished UTC: 2026-09-21T13:25:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:009689 |
| Label | antarctic_bacterial_medium |
| Original label | Antarctic Bacterial Medium |
| Source term | TOGO:M326 |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml |
| Generated record | data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml |

This is a generated merge record derived from one normalized TOGO owner. Future
fixes should land in `data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml`
or the TOGO import mapping that produced it, then the generated merge should be
rebuilt.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml` returned `No issues found`. |
| Strict schema | Passed: `scripts/validate_strict.py data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml --workers 1 --quiet` scanned 1 file and emitted 0 error rows. |
| References | Passed: `linkml-reference-validator validate data data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` found 0 active checks and reported all validations passed. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/ANTARCTIC_BACTERIAL_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone files under `history/`, not a focused validator for one embedded `MediaRecipe.curation_history` block in a generated merge. |

The repository's documented `just validate-schema`, `just validate-strict`,
`just validate-references`, and `just validate-terms` wrappers are currently
blocked before target-specific validation by the project `uv` environment
attempting to build `llvmlite==0.46.0` under Python 3.13 and failing inside
`setuptools` with `TypeError: Popen.__init__() got an unexpected keyword
argument 'dry_run'`. The equivalent validators above were run through
`uv --no-project` on Python 3.11 with the same schema and target file.

## Identity and Grounding

The record correctly identifies TOGO Medium M326, `Antarctic Bacterial Medium`,
which TOGO records as original JCM medium M331. The current JCM `GRMD=331` page
is source-rotted and returns `Nothing found`, but the live TOGO API still
exposes the JCM M331 source identity.

The material groundings for the two defined ingredients are exact enough for
this record: distilled water is grounded to `CHEBI:15377` / water and agar is
grounded to `CHEBI:2509` / agar. The complex BD-Difco yeast extract and Bacto
peptone rows correctly remain ungrounded.

## Evidence

The live TOGO M326 API supports the source name and the recipe shape: 1 L
distilled water, 15 g agar, 1 g Yeast extract (BD-Difco), 5 g Bacto peptone
(BD-Difco), and pH 6.9. The reviewed record correctly preserves the agar, yeast
extract, peptone, solid-agar state, and undefined/complex classification.

The water and pH claims are not faithfully represented. The TOGO API reports
the water as `1 L`; the YAML stores it as `1 G_PER_L`. The TOGO API reports
`ph: 6.9`; the YAML has no `ph_value`, `ph_range`, or preparation step for that
adjustment.

## Completeness

The pH 6.9 assertion from TOGO is missing. There are no `preparation_steps`; the
current TOGO API does not expose a preparation comment for M326, and the
original JCM page can no longer be used to check whether JCM had additional
default or medium-specific preparation text.

An ignored-inclusive exact search for
`CultureMech:009689|TOGO:M326|TOGO_M326_Antarctic_Bacterial_Medium|JCM_M331|GRMD=331|Antarctic_Bacterial_Medium`
covered `data`, `src`, `reports`, `.claude`, `CLAUDE.md`, and `justfile`.
It found the normalized TOGO owner, generated TOGO merge, registry/index rows,
import-tracking reports, and a second normalized MediaDive/JCM owner at
`data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml` generated as
`data/merge_yaml/merged/antarctic_bacterial_medium__115440a9.yaml`.

The absence of `target_organisms` is not by itself a defect because the TOGO
medium recipe does not assert a specific growth claim.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| major | The distilled-water amount has the wrong unit and magnitude. | TOGO M326 stores `Distilled water` as `1 L`; the record stores `1 G_PER_L`, which is not a liter-scale final volume. | `data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml`; TOGO import unit mapping |
| major | The source pH is missing. | TOGO M326 reports `ph: 6.9`, and the MediaDive/JCM sibling also has `ph_value: 6.9`; the reviewed TOGO merge has no pH field or pH preparation step. | `data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml`; TOGO import mapping |
| minor | The same JCM M331 source is present as a second unmerged record. | `data/normalized_yaml/bacterial/antarctic_bacterial_medium.yaml` cites JCM `GRMD=331`, stores MediaDive `J331`, and generates `antarctic_bacterial_medium__115440a9.yaml`. | Merge fingerprinting after TOGO and MediaDive source normalization |

## Recommended Edits

1. Preserve `Distilled water 1 L` as a volume/final-volume row or convert it to
   the repository's explicit liter-scale water representation without treating
   `1 L` as `1 G_PER_L`.
2. Import TOGO's pH 6.9 into the normalized TOGO owner.
3. Compare the TOGO and MediaDive JCM M331 owners once the water and pH fields
   are corrected, then regenerate and verify whether the duplicate merge should
   collapse them.

## Follow-up Checks

- Re-run `just validate data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml`,
  `just validate-strict data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml`,
  `just validate-terms data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml`,
  and `just validate-references data/normalized_yaml/bacterial/TOGO_M326_Antarctic_Bacterial_Medium.yaml`
  after the normalized owner or importer is changed.
- Re-run `just verify-merges` after regenerating `data/merge_yaml/merged/`.
- Re-query TOGO M326 and rerun an ignored-inclusive exact search for JCM
  `GRMD=331`, `TOGO:M326`, and `mediadive.medium:J331` before closing the
  duplicate-record follow-up.

## Additional Notes

The current JCM `GRMD=331` page returned `Nothing found` during this review, so
the live JCM page could not be used to verify the preparation text or pH. The
TOGO API is still useful because it stores the original JCM identifier, source
URL, ingredient rows, and pH copied from its upstream source.
