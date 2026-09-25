# YAML Record Review: saline_tryptone_yeast_extract_broth

- Repository: CultureMech
- Record: data/merge_yaml/merged/saline_tryptone_yeast_extract_broth.yaml
- Started UTC: 2026-09-25T03:43:40Z
- Finished UTC: 2026-09-25T03:43:40Z
- Verdict: pass with minor issues

## Target

Reviewed generated `MediaRecipe` `CultureMech:010091`, `saline_tryptone_yeast_extract_broth`, from `data/merge_yaml/merged/saline_tryptone_yeast_extract_broth.yaml`.

The record is a single-source TOGO M686 import with JCM_M668 listed as TOGO's original source.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The CultureMech record is grounded to `TOGO:M686`, `Saline Tryptone-Yeast Extract Broth`, and preserves TOGO's JCM_M668 provenance in `notes`.

The live JCM `GRMD=668` page currently returns "Nothing found", so the original JCM formulation was not independently confirmed during this review.

## Evidence

TOGO M686 lists one main solution containing 1 L distilled water, 2 g MgSO4 x 7 H2O, 100 g NaCl, 3 g yeast extract, and 5 g tryptone.

TOGO also carries a pH range of 7.0-7.2 and a comment to adjust the pH to that range.

## Completeness

The five source ingredient rows are present and no extra ingredients were introduced.

The TOGO pH range and adjust-pH comment are absent from the structured generated record.

No organism growth evidence is embedded, and no organism claims were assessed.

## Findings

The formula is complete for the TOGO M686 main solution, except that the pH range and "Adjust pH to 7.0-7.2" instruction were lost during import.

The TOGO 1 L distilled-water row is represented as `1 G_PER_L`, which preserves the row but not the source volume unit.

## Recommended Edits

Populate the normalized TOGO record with `ph_value` or a pH range representation for 7.0-7.2, and add a concise `ADJUST_PH` preparation step from the TOGO comment.

Prefer a volume-preserving representation for the 1 L distilled-water row, or omit the filler water row if the schema cannot distinguish "bring volume to" water from gram-per-liter solutes.

## Follow-up Checks

After regenerating the merged YAML, confirm the five TOGO ingredients remain unchanged and that the generated recipe carries the 7.0-7.2 pH adjustment.

Recheck the JCM_M668 source URL later; if JCM restores that medium page, compare it against TOGO M686 and capture any drift.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
