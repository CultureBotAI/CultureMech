# YAML Record Review: pplo_pleuropneumonia_like_organism_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/pplo_pleuropneumonia_like_organism_medium.yaml
- Started UTC: 2026-09-24T21:50:32Z
- Finished UTC: 2026-09-24T21:50:32Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:009512`, the generated bacterial liquid `PPLO (pleuropneumonia-like organism) medium` record merged from `data/normalized_yaml/bacterial/pplo_pleuropneumonia_like_organism_medium.yaml` and grounded to `TOGO:M2996`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The identity is correct: the generated record, the direct normalized input, and TOGO all describe `M2996`, `PPLO (pleuropneumonia-like organism) medium`. An exact ignored YAML search for `TOGO:M2996`, `M2996`, and `pplo_pleuropneumonia_like_organism_medium` found only this generated output, the direct normalized input, and one curation-history mention in `marine_broth_2216.yaml`.

## Evidence

The TOGO `M2996` API reports one liter of Difco PPLO broth, growth in a 5% CO2 atmosphere, and the source comment "A. pleuropneumoniae strains were cultivated in PPLO (pleuropneumonia-like organism) medium (Difco, Detroit, Mich.) with NAD (10 ug/ml) at 37 C in a 5% CO2 atmosphere."

The normalized source record has already applied that evidence: PPLO medium is 1000 ml/L, NAD is 10 mg/L, CO2 is 5% v/v, `temperature_value` is 37.0, source notes are attached to each ingredient, and `references` includes the TOGO `M2996` URL.

## Completeness

The generated YAML is stale relative to the repaired normalized input. It lacks the NAD ingredient, lacks `temperature_value`, leaves CO2 at the schema-default `variable` value, and does not carry the source-specific ingredient notes or `references` that were added during the normalized repair.

## Findings

- The generated PPLO base row is the stale TOGO import artifact `1 G_PER_L`, even though TOGO records one liter of the already prepared PPLO medium and the normalized record now represents it as `1000 ML_PER_L`.
- The generated record omits the 10 ug/ml NAD supplement that is stated in TOGO's source comment and represented as 10 mg/L in the repaired normalized YAML.
- The generated CO2 row is `variable`; TOGO explicitly reports a 5% CO2 atmosphere and the normalized input already uses `PERCENT_V_V`.
- The generated output lost the 37 C incubation temperature and still has only the pre-repair source string in `notes`.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/pplo_pleuropneumonia_like_organism_medium.yaml` from the repaired normalized input so the merged output carries 1000 ml/L PPLO medium, 10 mg/L NAD, 5% CO2, the 37 C temperature, ingredient evidence notes, and `references`.
- Confirm that no merge/import path is still reading a stale pre-repair copy of `TOGO:M2996` before publishing the regenerated file.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat the exact ignored YAML search for `TOGO:M2996` and `pplo_pleuropneumonia_like_organism_medium` to verify that the normalized repair is reflected by the generated output and no duplicate stale branch was emitted.

## Additional Notes

None.
