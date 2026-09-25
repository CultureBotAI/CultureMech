# YAML Record Review: halophilic_no_3_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halophilic_no_3_medium.yaml`
- Started UTC: 2026-09-23T11:00:45Z
- Finished UTC: 2026-09-23T11:01:35Z
- Verdict: needs curation

## Target

Generated merged YAML for Togo Medium M2060, `Halophilic No.3 Medium`, imported from NBRC medium 1362.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches Togo `TOGO:M2060` and NBRC medium 1362.
- An ignored-file-inclusive exact search for `TOGO:M2060`, `medium/M2060`, `NBRC_M1362`, `NO=1362`, and `halophilic_no_3_medium` found only the Togo M2060 import and its merged output.
- NaCl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, and K2SO4 are grounded appropriately.
- Bacto Yeast Extract is intentionally ungrounded as an undefined ingredient.
- Agar is not grounded even though Togo M2060 maps it to the GMO Agar entry.

## Evidence

- NBRC 1362 lists 5 g Bacto Yeast Extract (Difco), 5 g K2SO4, 0.1 g CaCl2 x 2 H2O, 20 g MgCl2 x 6 H2O, 175 g NaCl, 20 g agar if needed, and 1 L distilled water.
- NBRC 1362 states pH 7.0-7.4.
- Togo M2060 preserves the pH range as `7.0-7.4`, the 1 L distilled-water row, and the source's conditional `Agar (if needed)` wording.

## Completeness

- Missing pH: the generated record has no structured pH for the 7.0-7.4 source range.
- Mis-scaled water: the 1 L distilled-water row became `1 G_PER_L`.
- Missing preparation: no pH or final-volume preparation steps are represented.
- Conditional agar issue: `Agar (if needed)` is present on a single `SOLID_AGAR` recipe instead of being scoped as optional or split from the base recipe.

## Findings

1. The generated NBRC 1362 record omits the 7.0-7.4 pH range.
2. Distilled water was imported as `1 G_PER_L` instead of the 1 L final volume.
3. The conditional 20 g agar row is ungrounded and makes the whole recipe `SOLID_AGAR`.
4. Preparation steps are missing entirely.

## Recommended Edits

- Add the 7.0-7.4 source pH range in the available structured pH representation.
- Replace the water row with the correct 1 L final-volume representation.
- Re-ground Agar to CHEBI:2509.
- Split the optional 20 g agar into an explicit solid variant or otherwise scope its `if needed` condition without forcing the base medium to be `SOLID_AGAR`.
- Add any preparation steps needed to capture final volume and pH semantics.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `TOGO:M2060`, `NBRC_M1362`, and `NO=1362` after regeneration.
- Verify that the NBRC source qualifier on `Bacto Yeast Extract (Difco)` remains intact.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
