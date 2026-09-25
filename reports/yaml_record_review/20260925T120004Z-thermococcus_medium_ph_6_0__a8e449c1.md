# YAML Record Review: thermococcus_medium_ph_6_0
- Repository: CultureMech
- Record: data/merge_yaml/merged/thermococcus_medium_ph_6_0__a8e449c1.yaml
- Started UTC: 2026-09-25T12:00:04Z
- Finished UTC: 2026-09-25T12:00:04Z
- Verdict: needs curation

## Target
Reviewed the generated TOGO M345 record for Thermococcus Medium, pH 6.0.

## Validation
- Schema: Passed; linkml-validate exited 0 with no issues.
- Strict: Passed; validate_strict reported 0 ERROR rows.
- References: Passed; the reference validator exited 0 with 0 checks.
- Terms: Passed; linkml-term-validator exited 0 with Validation passed.
- Embedded history: Not checked: the available history validator checks standalone history records, not MediaRecipe.curation_history in merged YAML.

## Identity and Grounding
- The canonical record is grounded to TOGO:M345.
- TOGO M345 is a JCM_M350 cross-reference to 1 L of Thermococcus Medium M273, followed by pH readjustment to 6.0 with 1.0 N H2SO4.
- The generated merge groups TOGO M345 with unrelated Desulfurococcus, Picrophilus, Sulfolobus, salt-solution, trace-element, and Wolfe's mineral elixir records that share the same degraded H2SO4-only signature.

## Evidence
- TOGO M345 lists Thermococcus medium, see Medium M273, at 1 L.
- TOGO M345 lists H2SO4 as a 1.0 N pH-adjustment solution and records source pH 6.0.
- The TOGO comment says to readjust the reduced medium to pH 6.0 with 1.0 N H2SO4.

## Completeness
- The record carries the TOGO M345 source identifier.
- The referenced M273 formulation is represented only as an empty Unknown solution with concentration 1 G_PER_L.
- The explicit pH 6.0 value is absent from ph_value.

## Findings
- The recipe collapsed 1 L of Medium M273 into an empty solution at 1 G_PER_L instead of linking or expanding the referenced parent medium.
- The pH adjustment H2SO4 was imported as a variable-concentration ingredient rather than as a preparation reagent.
- pH 6.0 is present in TOGO but missing from the generated record.
- The merge fingerprint falsely combined M345 with seven unrelated media or stock-solution records after their recipes degraded to the same sparse H2SO4 shape.

## Recommended Edits
- Model M345 as a pH 6.0 variant of M273 and preserve the 1.0 N H2SO4 readjustment as preparation metadata.
- Stop cross-reference media rows such as Medium M273 from being converted to gram-per-liter solutes.
- Include pH 6.0 in the normalized record before merge generation.
- Exclude source records with unrelated source IDs and names from this canonical recipe.

## Follow-up Checks
- Rebuild the merge and verify that only M345 or an explicit J350/M345 equivalent contributes to this generated record.
- Re-run schema, strict, reference, and term validation on the rebuilt record.

## Additional Notes
- Empty optional fields were not treated as defects.
- Source lookup used exact source identifiers with ignored files included.
