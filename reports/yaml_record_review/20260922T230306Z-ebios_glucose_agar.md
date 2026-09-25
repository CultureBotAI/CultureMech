# YAML Record Review: ebios_glucose_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/ebios_glucose_agar.yaml
- Started UTC: 2026-09-22T23:01:42Z
- Finished UTC: 2026-09-22T23:03:06Z
- Verdict: needs curation

## Target

Generated TOGO M1019 record `CultureMech:007533`, named `ebios_glucose_agar`, with `JCM_M969` carried as the original source in the notes.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation against `scripts/validate_strict.py`: passed with 0 error rows.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the focused history validator targets standalone files under `history/`, not inline `MediaRecipe.curation_history` entries.

## Identity and Grounding

The Togo identity is present as `TOGO:M1019`, and the note correctly points back to JCM medium 969. This record is nevertheless a duplicate of the direct JCM/MediaDive import in `data/merge_yaml/merged/ebios_glucose_agar__f620f7f5.yaml`; an exact ignored-inclusive search for the JCM and EBIOS identifiers found both generated records.

Glucose, agar, and water are grounded correctly. `EBIOS* (dried yeast tablets)` is intentionally undefined and has no ChEBI term.

## Evidence

Togo M1019 and JCM 969 list 10 g EBIOS dried yeast tablets, 20 g glucose, 15 g agar, and 1 L distilled water. JCM also adds the general instruction to sterilize by autoclaving at 121 C for 15 minutes unless otherwise stated, plus the source-specific note that pH is not adjusted.

The generated TOGO record captures the three dry masses as 10, 20, and 15 g/L, but imports the solvent basis as `Distilled water 1 G_PER_L`.

## Completeness

The three substantive ingredients and source URL are present. The record loses the pH-not-adjusted note, omits the JCM autoclave default, lacks a structured JCM source/reference, and should not be separate from the JCM J969 copy.

## Findings

- `Distilled water` is represented as `1 G_PER_L` instead of a 1 L final-volume basis.
- The equivalent TOGO M1019 and JCM J969 imports failed to merge, leaving duplicate generated records with different stable CultureMech IDs.
- JCM's pH-not-adjusted note and 121 C for 15 minutes default autoclave instruction are missing from this TOGO-derived generated record.
- The original JCM source is embedded in `notes` but not promoted into structured `sources` or `references`.

## Recommended Edits

- Normalize distilled-water `1 L` entries as final-volume bases before fingerprinting and rendering.
- Merge TOGO M1019 with the JCM J969 record so EBIOS-Glucose Agar has one generated canonical record.
- Preserve the Togo source ID, JCM source ID, and JCM URL as structured provenance on the merged record.
- Carry forward the JCM default autoclave instruction and the pH-not-adjusted note.

## Follow-up Checks

- Re-run open, strict, reference, and term validators after rebuilding.
- Compare the rebuilt record against Togo M1019 and JCM 969.
- Search with ignored files included for duplicate `J969`, `JCM_M969`, and `TOGO_M1019_EBIOS-Glucose_Agar` generated records after the merge logic is fixed.

## Additional Notes

The generated record has no explicit organism growth data to review.
