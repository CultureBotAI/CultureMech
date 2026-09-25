# YAML Record Review: haloneutrophile_medium__94db902d

- Repository: CultureMech
- Record: `data/merge_yaml/merged/haloneutrophile_medium__94db902d.yaml`
- Started UTC: 2026-09-23T10:52:20Z
- Finished UTC: 2026-09-23T10:53:14Z
- Verdict: needs curation

## Target

Generated merged YAML for direct MediaDive/JCM medium J307, `HALONEUTROPHILE MEDIUM`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:J307` and the JCM 307 source page.
- An ignored-file-inclusive exact search for `mediadive.medium:J307`, `GRMD=307`, `HALONEUTROPHILE MEDIUM`, and `haloneutrophile_medium` found the direct JCM J307 import, the Togo M302 import from the same JCM page, and their two merged outputs.
- The hydrate-sensitive MgSO4 x 7 H2O, CaCl2 x 2 H2O, FeCl2 x 4 H2O, and MnCl2 x 4 H2O groundings are appropriate.
- Yeast extract and Casamino acids are intentionally ungrounded undefined ingredients but lost their `BD-Difco` qualifiers.

## Evidence

- JCM 307 lists 2 g Yeast extract (BD-Difco), 2 g Casamino acids (BD-Difco), 1 g sodium glutamate, 3 g trisodium citrate, 10 g MgSO4 x 7 H2O, 1 g CaCl2 x 2 H2O, 1 g KCl, 200 g NaCl, 0.36 mg FeCl2 x 4 H2O, and 0.36 mg MnCl2 x 4 H2O brought to a final 1 L with distilled water.
- JCM 307 instructs adjustment to pH 7.0-7.2 and supplies the default JCM 121 C, 15 min autoclaving header.
- MediaDive J307 preserves the two `BD-Difco` attributes and the two 0.36 mg trace-metal amounts.
- The generated direct JCM record keeps the 0.36 mg/L Fe/Mn concentrations and the pH range in the `ADJUST_PH` step, but it omits water and the BD-Difco qualifiers.

## Completeness

- Missing final volume: distilled water to 1 L is present only in a `MIX` prose step, not as a structured water/final-volume row.
- Missing qualifiers: Yeast extract and Casamino acids lost `BD-Difco`.
- Missing preparation: the JCM default autoclaving step is absent.

## Findings

1. The generated direct JCM J307 record omits a structured distilled-water/final-volume representation.
2. Yeast extract and Casamino acids lost their source `BD-Difco` qualifiers.
3. The default JCM autoclaving semantics are missing.

## Recommended Edits

- Add distilled water or an equivalent structured final-volume representation for the 1 L formula.
- Restore `BD-Difco` on Yeast extract and Casamino acids.
- Add the JCM default 121 C, 15 min autoclaving step if the curation model captures default source sterilization.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:J307`, `TOGO:M302`, and `GRMD=307` after regeneration.
- Verify that the regenerated direct record keeps FeCl2 x 4 H2O and MnCl2 x 4 H2O at 0.36 mg/L and does not inherit the Togo M302 gram-per-liter conversion error.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
