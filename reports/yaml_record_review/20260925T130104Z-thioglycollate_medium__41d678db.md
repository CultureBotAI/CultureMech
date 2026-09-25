# YAML Record Review: thioglycollate_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thioglycollate_medium__41d678db.yaml
- Started UTC: 2026-09-25T13:02:40Z
- Finished UTC: 2026-09-25T13:03:04Z
- Verdict: needs curation

## Target

- Generated YAML for the TOGO M531 Thioglycollate Medium import derived from JCM_M529-2.
- The record was merged from `TOGO_M531_Thioglycollate_Medium`.
- The checked sources were TOGO M531 and the current JCM 529 page.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to TOGO M531, a Thioglycollate Medium snapshot of JCM_M529-2.
- The JCM GRMD 529 URL embedded in TOGO currently returns `Nothing found`, so the live JCM page did not independently confirm the snapshot.
- A nearby normalized sibling for `thioglycollate_medium` records TOGO M530 as a snapshot of JCM_M529, distinct from this M531/JCM_M529-2 generated record.

## Evidence

- TOGO M531 lists 1 L distilled water and 29.8 g Thioglycollate medium (Sigma).
- TOGO M531 notes that the medium is semisolid.
- TOGO M531 notes that strain JCM 13596 should be prepared anaerobically under N2.

## Completeness

- The Sigma dehydrated-medium amount is present as 29.8 g/L.
- The 1 L distilled-water row is stored as 1 g/L water.
- N2 from the JCM 13596 strain-specific note is modeled as a generic top-level ingredient.
- The semisolid physical state is lost; `physical_state` is `LIQUID`.
- The JCM 13596 anaerobic-preparation scope is lost.

## Findings

- The TOGO water volume is unit-swapped into a false 1 g/L water concentration.
- The record broadens a strain-specific N2 handling note into a generic ingredient.
- The physical state contradicts the TOGO note that the medium is semisolid.

## Recommended Edits

- Preserve the 1 L water volume and 29.8 g/L Sigma dehydrated medium as the core TOGO M531 formula.
- Model the JCM 13596 N2 instruction as a strain-specific preparation note rather than a top-level ingredient.
- Set the physical state to semisolid if the schema supports it, or document the semisolid source state in notes.
- Compare M531/JCM_M529-2 to the existing M530/JCM_M529 snapshot before merging.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Recheck JCM 529 or an archived JCM page if live JCM continues to return `Nothing found`.
- Verify no TOGO L units are normalized to `G_PER_L`.

## Additional Notes

- None found.
