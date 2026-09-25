# YAML Record Review: GYP medium (pH 6) for anaerobe

- Repository: CultureMech
- Record: `data/merge_yaml/merged/gyp_medium_ph_6_for_anaerobe.yaml`
- Started UTC: 2026-09-23T08:27:59Z
- Finished UTC: 2026-09-23T08:28:57Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008716`, `gyp_medium_ph_6_for_anaerobe`, imported from Togo `M2123` / `NBRC_M1451`.

## Validation

- LinkML validation: passed.
- Strict validation: passed with 0 ERROR rows in `/private/tmp/gyp_medium_ph_6_for_anaerobe.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked: the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The source identity is coherent: exact ignored-file-inclusive search found only the expected normalized and generated records for `TOGO:M2123`, `NBRC_M1451`, and `gyp_medium_ph_6_for_anaerobe` in `data/normalized_yaml/bacterial` and `data/merge_yaml/merged`.

Most simple components are grounded. Bacto Yeast Extract and Hipolypepton are ungrounded complex components.

## Evidence

The Togo `M2123` payload lists a main solution with 1 L Distilled water, 1 mg Resazurin, 2 g Sodium acetate, 10 g Glucose, 10 g Bacto Yeast Extract, 3 g Cysteine-HCl x H2O, 5 g Hipolypepton, 10 ml Tween 80 solution, 5 ml Salts solution, and N2. Its Tween stock contains 50 g Tween 80 in 1 L water; its salts stock contains 40 g MgSO4 x 7 H2O, 2 g NaCl, 2 g FeSO4 x 7 H2O, 2 g MnSO4 x 4 H2O, and a drop of 12 N HCl to 500 ml of the salts solution.

Togo also records pH 6.0 and instructs curators to mix all ingredients except cysteine-HCl, dispense under a stream of N2, seal with butyl rubber stoppers, autoclave cysteine-HCl separately as a 5% solution under N2, and add that cysteine-HCl solution aseptically and anaerobically before inoculation.

## Completeness

The record has the expected main ingredient names, stock component names, and gas name, but it is incomplete for units, stock structure, pH, and anaerobic preparation. The generated record is also stale relative to `data/normalized_yaml/bacterial/gyp_medium_ph_6_for_anaerobe.yaml`, where the September duplicate-water repair collapsed the three merged water rows.

## Findings

- Resazurin is misunitized. Togo records 1 mg, while the generated record stores `1 G_PER_L`.
- The generated record is missing pH 6.0 from Togo.
- `Hipolypepton*` is a 5 g main-medium ingredient but is stored as an empty solution with `Unknown solution`.
- Tween 80 solution and Salts solution are flattened at stock strength instead of preserved as nested stocks added at 10 ml and 5 ml.
- The HCl instruction belongs to Salts solution preparation; it should not be a top-level variable ingredient.
- N2 is a preparation atmosphere, but the generated row lacks the source instructions to dispense under N2, stopper vessels, autoclave cysteine-HCl separately under N2, and add cysteine-HCl aseptically and anaerobically before inoculation.
- Distilled water is stale and wrong. The generated row sums three 1 L solvent rows as `3.0 G_PER_L`, while the normalized parent has already repaired that duplicate-water merge back to `1.0`.

## Recommended Edits

- Convert the 1 mg Resazurin row correctly during import.
- Preserve pH 6.0 and the anaerobic preparation text from Togo.
- Keep Hipolypepton as a main ingredient.
- Preserve the 10 ml Tween 80 stock addition and the 5 ml Salts solution addition as nested solutions.
- Move the HCl text into the Salts solution preparation notes and retain N2 as preparation/gas-atmosphere context.
- Regenerate from the repaired normalized parent so the duplicate-water repair is reflected.
- Attempt complex-component groundings for Bacto Yeast Extract and Hipolypepton.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validators after recuration.
- Recompare the regenerated record against Togo `M2123`, with explicit checks for Resazurin units, pH 6.0, the 5% cysteine-HCl preparation, and the two stock addition volumes.

## Additional Notes

None found.
