# YAML Record Review: Sucrose-Bennett's Agar
- Repository: CultureMech
- Record: data/merge_yaml/merged/sucrose_bennetts_agar__6b93df42.yaml
- Started UTC: 2026-09-25T07:44:11Z
- Finished UTC: 2026-09-25T07:44:11Z
- Verdict: needs curation

## Target
Reviewed generated record `CultureMech:008097` / `sucrose_bennetts_agar` from `data/merge_yaml/merged/sucrose_bennetts_agar__6b93df42.yaml`.

The generated record has one source, `TOGO:M1549`, imported from NBRC medium 343.

## Validation
- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The TOGO and generated identities are coherent for NBRC medium 343: the record cites `TOGO:M1549`, notes original source `NBRC_M343`, and links to the NBRC medium detail page.

The exact local search found the TOGO M1549 record plus the related `mediadive.medium:1762` DSMZ Sucrose-Bennett record. Both are 20 g/L agar versions of Sucrose-Bennett's Agar, but NBRC/TOGO gives pH 7.3 while DSMZ 1762 gives pH 7.2.

## Evidence
NBRC medium 343 lists 1 g yeast extract, 1 g beef extract, 2 g N-Z-Amine A, 10 g sucrose, 1 L distilled water, 20 g agar, and pH 7.3.

TOGO M1549 carries the same NBRC formula and pH: 1 L distilled water, 1 g yeast extract, 10 g sucrose, 20 g agar, 1 g beef extract, 2 g N-Z-Amine A, and pH 7.3.

The DSMZ 1762 Sucrose-Bennett's Agar source has the same component quantities but pH 7.2.

## Completeness
The generated NBRC ingredient list has the correct non-water masses for TOGO M1549 and NBRC 343.

The 1 L distilled-water row is incorrectly represented as 1 `G_PER_L`, and the pH 7.3 value from both NBRC and TOGO is absent.

The formula should be aligned with the DSMZ 1762 20 g/L agar Sucrose-Bennett record after water normalization, while preserving NBRC's pH 7.3 difference from DSMZ's pH 7.2.

## Findings
- Non-water masses match NBRC 343.
- The water make-up volume is imported as a 1 g/L ingredient.
- The pH 7.3 target is missing.
- This 20 g/L agar variant remains split from the DSMZ 1762 20 g/L agar record because water and metadata normalization are incomplete.

## Recommended Edits
- Fix `data/normalized_yaml/bacterial/TOGO_M1549_Sucrose-Bennett_s_Agar.yaml` or the TOGO import logic, then regenerate `data/merge_yaml/merged/sucrose_bennetts_agar__6b93df42.yaml`; do not hand-edit the generated merged YAML.
- Convert 1 L distilled water into volume metadata rather than a 1 g/L final ingredient.
- Restore `ph_value: 7.3` from TOGO or NBRC.
- Link this NBRC recipe to the DSMZ 1762 Sucrose-Bennett record as the same 20 g/L agar formulation with a pH-source difference.

## Follow-up Checks
- Confirm the regenerated record has no 1 g/L water row.
- Confirm pH 7.3 is present.
- Confirm the relationship to the DSMZ 1762 20 g/L agar record is represented without overwriting the pH difference.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The exact local search for `TOGO:M1549`, `NBRC_M343`, `CultureMech:008097`, and `mediadive.medium:1762` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`.
