# YAML Record Review: thiobacillus_novellus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiobacillus_novellus_medium.yaml
- Started UTC: 2026-09-25T12:58:06Z
- Finished UTC: 2026-09-25T12:58:30Z
- Verdict: needs curation

## Target

- Generated YAML for the KOMODO 69 THIOBACILLUS NOVELLUS medium record enriched from DSMZ 69.
- The record was merged from `thiobacillus_novellus_medium`.
- The checked sources were the local KOMODO 69 enrichment metadata, MediaDive 69, and DSMZ Medium 69.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to KOMODO 69, THIOBACILLUS NOVELLUS medium.
- The notes map KOMODO 69 to DSMZ 69.
- DSMZ/MediaDive 69 identifies the exact DSMZ formulation as STARKEYA NOVELLA MEDIUM, and a separate exact DSMZ 69 normalized record exists as `starkeya_novella_medium`.

## Evidence

- DSMZ 69 combines 900 ml Solution A, 50 ml Solution B, 5 ml Solution C, and 50 ml Solution D after separate autoclaving.
- Solution C is 5 ml trace element solution from a 1 L Vishniac and Santer stock.
- The complete medium is adjusted to pH 8.5 with sterile 0.5 N NaOH after the cooled solutions are mixed.

## Completeness

- The imported pH 8.5 value matches DSMZ 69.
- Ingredients from Solutions A, B, C, D, and the nested trace stock are flattened as though each solution were the final medium.
- The separate autoclaving and post-mix pH-adjustment step is missing.
- `target_organisms` contains the raw string `THIOBACILLUS NOVELLUS` without an organism term or source evidence.

## Findings

- The record identity is inconsistent: the YAML keeps the KOMODO Thiobacillus novellus name while the copied DSMZ 69 source is Starkeya novella medium.
- Solution B, Solution D, and the Vishniac and Santer trace solution are stored at stock strength instead of their 50 ml, 50 ml, and 5 ml additions.
- Solution A concentrations are normalized to its 900 ml solution volume rather than the 1005 ml final medium volume.
- The DSMZ 69 preparation instructions are omitted.
- The target organism is ungrounded.

## Recommended Edits

- Reconcile KOMODO 69 with the direct DSMZ 69 `starkeya_novella_medium` record before retaining a separate Thiobacillus novellus record.
- Preserve Solutions A through D as separate stocks or recalculate final ingredient concentrations from their documented volumes.
- Restore the separate-sterilization and post-mixing pH-adjustment instruction.
- Ground or remove the raw `THIOBACILLUS NOVELLUS` target organism.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm whether Thiobacillus novellus should be retained only as a legacy alias of Starkeya novella.
- Verify that nested trace-solution ingredients are not imported at full stock strength.

## Additional Notes

- None found.
