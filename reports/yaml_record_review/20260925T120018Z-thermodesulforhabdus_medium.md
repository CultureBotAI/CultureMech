# YAML Record Review: thermodesulforhabdus_medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermodesulforhabdus_medium.yaml
- Started UTC: 2026-09-25T12:00:18Z
- Finished UTC: 2026-09-25T12:00:18Z
- Verdict: needs curation

## Target
Reviewed the generated KOMODO 707 record for Thermodesulforhabdus medium.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict exited 0 with a header-only TSV and 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The record is grounded to komodo.medium:707.
- The KOMODO note cites DSMZ Medium 707 as mediadive.medium:707 and pH 6.8.
- The direct DSMZ PDF URL for Medium 707 returned a 404 page during review, and MediaDive REST returned DataNotFound for numeric medium 707.

## Evidence
- The local source record contains only a variable-concentration sodium row extracted from a sodium bicarbonate pH-buffer note.
- No direct DSMZ 707 formula was available from the exact DSMZ or MediaDive URLs checked during this review.

## Completeness
- The Thermodesulforhabdus medium formula is effectively absent.
- pH 6.8 is present.
- The pH buffer was reduced to a variable sodium placeholder instead of sodium bicarbonate handling.

## Findings
- The generated record contains no source formula ingredients beyond an extraction artifact named sodium.
- Sodium bicarbonate in the KOMODO note was mis-parsed as sodium.
- The KOMODO note says Aerobic: Yes, but the cited DSMZ formulation could not be checked to confirm the atmosphere.
- The cited DSMZ/MediaDive source must be remapped because the exact numeric endpoints no longer resolve.

## Recommended Edits
- Resolve the current source for DSMZ Medium 707 or mark the record as uncurated until the formulation is available.
- Re-import the full Thermodesulforhabdus formula from a direct source.
- Replace the extracted sodium placeholder with structured sodium bicarbonate pH-buffer metadata if the source supports it.
- Do not rely on the KOMODO Aerobic flag without a current formulation source.

## Follow-up Checks
- Search DSMZ/MediaDive release history or culture collection pages for a replacement Thermodesulforhabdus medium source.
- Re-run schema, strict, reference, and term validation after the formula is restored.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
