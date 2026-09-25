# YAML Record Review: COLUMBIA AGAR WITH 5% SHEEP BLOOD

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_agar_with_5_sheep_blood.yaml`
- Started UTC: `2026-09-22T10:22:13Z`
- Finished UTC: `2026-09-22T10:24:49Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:000788` for DSMZ Medium `1331`, `COLUMBIA AGAR WITH 5% SHEEP BLOOD`, generated from `data/normalized_yaml/bacterial/columbia_agar_with_5_sheep_blood.yaml` on merge fingerprint `e5d7808b77a9b559b544f1012673b62c548608930918aa5da5cd3a62e5e2b3ab`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_agar_with_5_sheep_blood.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is correct: `mediadive.medium:1331` denotes DSMZ Medium 1331, `COLUMBIA AGAR WITH 5% SHEEP BLOOD`.

The record keeps a `kg_microbe_match: mediadive.medium:687` cross-match to DSMZ Columbia Blood Agar. That is close in the Columbia agar family, but it is not the same DSMZ source accession as 1331 and should be treated as a relation to audit rather than exact identity.

An ignored-inclusive generated-record search under `data/merge_yaml/merged` found no sibling `columbia_agar_with_5_sheep_blood*.yaml` record. An ignored-inclusive search for `mediadive.medium:1331` found only this normalized input plus indexes, reports, and generated merge output.

## Evidence

The DSMZ Medium 1331 section supports Columbia Blood Agar Base made from 10.0 g Bacto Panton, 10.0 g Bacto Bitone, 3.0 g tryptic digest of beef heart, 1.0 g corn starch, 5.0 g NaCl, 15.0 g agar, 1000.0 ml distilled water, and 50.0 ml defibrinated blood. The preparation steps to dissolve 44 g base in 1 L water, autoclave, cool to 45 C, add 5% sterile defibrinated sheep blood, and mix well are also source-backed.

The DSMZ PDF continues after Medium 1331 with a separate Medium 220 `CASO AGAR` section. The generated record incorrectly imports Medium 220's 15.0 g peptone from casein, 5.0 g peptone from soymeal, 5.0 g NaCl, and pH 7.3 line into Medium 1331.

## Completeness

The generated record contains the correct Columbia agar base solids apart from the two distinct Bacto Panton and Bacto Bitone peptone products being collapsed into a single Bacto peptone row. The generated `19.04762 G_PER_L` is the scaled total of the two 10 g peptone inputs, but the row no longer says that it represents two distinct DSMZ source rows.

The 50 ml blood addition is represented as `50 G_PER_L` defibrinated blood. DSMZ states a liquid 50.0 ml, equivalent to a 5% sheep-blood supplement in the instructions.

No target organism or growth evidence is present. That is an empty optional area in this source-only record.

## Findings

- Major: the generated record imports three ingredients from the following DSMZ Medium 220 recipe: `Casein peptone`, `Soy peptone`, and a second 5 g NaCl contribution that was summed into the Medium 1331 NaCl row.
- Major: `ph_value: 7.3` and the final adjust-pH preparation step also belong to DSMZ Medium 220, not Medium 1331.
- Major: the blood addition has the wrong unit shape: DSMZ lists 50 ml sterile defibrinated sheep blood, but the generated concentration is `50 G_PER_L`.
- Minor: DSMZ lists Bacto Panton and Bacto Bitone as separate peptone products; the generated output collapses them into one `Bacto peptone` row and preserves only the duplicate-merge note.

## Recommended Edits

- In `data/normalized_yaml/bacterial/columbia_agar_with_5_sheep_blood.yaml`, remove the Medium 220 `Casein peptone`, `Soy peptone`, extra NaCl, pH 7.3, and adjust-pH claims from the DSMZ 1331 record.
- Represent the 50 ml / 5% sterile defibrinated sheep blood addition as a liquid or percent-by-volume addition instead of `50 G_PER_L`.
- Preserve Bacto Panton and Bacto Bitone as two source-distinct peptone rows, or make any combined Bacto peptone row explicitly represent the sum of those two source rows.
- Re-run merge generation so the repaired normalized input replaces the stale summed Bacto peptone artifact in `data/merge_yaml/merged/`.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm `Casein peptone` and `Soy peptone` are absent from DSMZ 1331.
- Confirm the NaCl row is no longer the sum of Medium 1331 NaCl and Medium 220 NaCl.
- Confirm blood is modeled as 50 ml or 5% sheep blood, not 50 g/L.
- Confirm the source-specific 1331 record no longer carries pH 7.3 unless a 1331-specific pH source is added.

## Additional Notes

The maintained normalized input was repaired after the generated merge was last written, so some generated Bacto peptone details are stale relative to `data/normalized_yaml/bacterial/columbia_agar_with_5_sheep_blood.yaml`; the regenerated merge should be checked against DSMZ because that repair also collapsed the two distinct Bacto Panton and Bacto Bitone source rows.
