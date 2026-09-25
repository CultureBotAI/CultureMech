# YAML Record Review: thioglycollate_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thioglycollate_medium__bfdc2c9b.yaml
- Started UTC: 2026-09-25T13:04:10Z
- Finished UTC: 2026-09-25T13:04:34Z
- Verdict: needs curation

## Target

- Generated YAML for the direct JCM/MediaDive J529 THIOGLYCOLLATE MEDIUM import.
- The record was merged from `thioglycollate_medium`.
- The checked sources were MediaDive J529 and the current JCM 529 page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; exited 0 after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to JCM/MediaDive J529, THIOGLYCOLLATE MEDIUM.
- MediaDive J529 still exposes the JCM 529 recipe.
- The live JCM 529 page currently returns `Nothing found`.

## Evidence

- MediaDive J529 lists 29.8 g Thioglycolate with the Sigma attribute and 1000 ml distilled water.
- MediaDive J529 records the JCM comment that the medium is semisolid and that strain JCM 13596 should be prepared anaerobically under N2.

## Completeness

- The 29.8 g/L Sigma thioglycolate ingredient is present.
- The source water row is missing.
- The record has `physical_state: LIQUID` despite the JCM semisolid comment.
- The JCM 13596 anaerobic condition is retained in a free-text preparation step rather than split as a strain-specific condition.

## Findings

- The 1000 ml distilled-water row from MediaDive J529 is omitted.
- The semisolid state is not reflected in `physical_state`.

## Recommended Edits

- Restore the 1000 ml distilled-water row.
- Represent the medium as semisolid if the schema supports it, or document the semisolid source state in notes.
- Keep the JCM 13596 N2 note scoped to that strain instead of treating it as a general base-medium ingredient.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Recheck JCM 529 or an archived JCM page if live JCM continues to return `Nothing found`.
- Compare this direct JCM J529 import with the TOGO M530 and M531 snapshots before merging any of them.

## Additional Notes

- None found.
