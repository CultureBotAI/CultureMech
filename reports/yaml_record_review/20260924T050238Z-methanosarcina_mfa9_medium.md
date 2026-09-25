# YAML Record Review: methanosarcina_mfa9_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosarcina_mfa9_medium.yaml
- Started UTC: 2026-09-24T05:02:38Z
- Finished UTC: 2026-09-24T05:02:38Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:015881` for JCM medium 1463, "METHANOSARCINA MFA9 MEDIUM", imported as a derivative of JCM medium 1462.

## Validation

- LinkML open schema validation: Passed with "No issues found".
- Strict recipe validation: Passed; `/private/tmp/methanosarcina_mfa9_medium.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The medium identity is correctly grounded to JCM GRMD 1463, and the live JCM page still identifies GRMD 1463 as "METHANOSARCINA MFA9 MEDIUM".
- JCM 1463 is a derivative recipe: it instructs the user to use JCM 1462 with 21.0 g/L NaCl instead of 9.0 g/L.
- The generated YAML inherits the 1462 ingredient list but leaves `NaCl` at `9.0 G_PER_L`, so the final parent formula is still the T3 base medium rather than the MFA9 derivative.
- The derivative instruction is preserved only as two broken `preparation_steps` fragments, `Use Medium No.` and `1462 with 21.0 g/L NaCl, instead of 9.0 g/L.`

## Evidence

- The live JCM 1463 page has only one formulation sentence: "Use Medium No. 1462 with 21.0 g/L NaCl, instead of 9.0 g/L."
- The live JCM 1462 base page lists the inherited salts, 9.0 g NaCl, 10 ml trace mineral solution from Medium No. 151, 10 ml local Ni-Se-W solution, 2.0 mg ferrous ammonium sulfate hexahydrate, 5.0 g NaHCO3, 0.5 mg resazurin, and 980 ml distilled water.
- JCM 1462 then adds a second per-liter solution table with 10 ml trace vitamins from Medium No. 197, 35 ml 2 M trimethylammonium chloride solution, 5 ml methanol, 10 ml 5% L-Cysteine-HCl-H2O solution, and 10 ml 5% Na2S x 9 H2O solution.
- JCM 1462 also defines a local Ni-Se-W stock below the main formula, with 30.0 mg NiCl2 x 6 H2O, 0.3 mg Na2SeO3 x 5 H2O, 0.4 mg Na2WO2 x 2 H2O, and 1.0 L distilled water.

## Completeness

- The inherited 1462 main and post-autoclave addition rows are present.
- The JCM 1463 NaCl substitution has not been applied to the ingredient list.
- The JCM 1462 base preparation instructions, pH 6.5 pre-autoclave target, pH 7.0 final adjustment, and local Ni-Se-W stock composition are absent.
- References to stock media 151 and 197 are carried only as text inside preferred terms, not as structured medium references.

## Findings

1. Major - The defining MFA9 derivative substitution is unapplied. The generated record is for JCM 1463 but still contains `NaCl` at `9.0 G_PER_L`; JCM 1463 changes the inherited JCM 1462 value to 21.0 g/L.
2. Major - The only JCM 1463 instruction was split into two preparation rows and cannot stand alone as an executable recipe. The current rows read `Use Medium No.` and `1462 with 21.0 g/L NaCl, instead of 9.0 g/L.` instead of a single derivative transformation.
3. Major - JCM 1462 preparation context was not inherited. The live base page instructs users to mix the base, adjust to pH 6.5, dispense under N2-CO2, seal with butyl rubber stoppers, autoclave, stand overnight, add specific sterile or filter-sterile solutions stored under N2, and adjust pH to 7.0 if needed; none of those steps appear in JCM 1463 after inheritance.
4. Major - The local Ni-Se-W stock formula from the JCM 1462 "see below" table is missing. The record has only a `Ni-Se-W solution (see below)` parent row, with no child composition for the nickel, selenite, tungsten, or water stock.
5. Minor - The JCM 151 and JCM 197 stock references are unresolved text. `Trace mineral solution (see Medium No. 151 )` and `Trace vitamins* (see Medium No. 197 )` should link to the referenced JCM media or be expanded as structured stock solutions if that is the repository convention.

## Recommended Edits

- Materialize JCM 1463 as a concrete derivative: clone the curated JCM 1462 formula, replace `NaCl` with `21.0 G_PER_L`, and record the substitution as provenance instead of leaving it for downstream users.
- Preserve the JCM 1463 derivative sentence as one instruction or history note, not two broken preparation steps.
- Inherit the 1462 anaerobic dispensing, overnight standing, post-autoclave addition, pH 6.5, and pH 7.0 instructions.
- Add the local Ni-Se-W stock table as a child solution or a linked stock recipe.
- Resolve Medium No. 151 and Medium No. 197 references using structured terms or linked child recipes.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Compare regenerated JCM 1463 against live JCM 1462 and 1463 to confirm that the only parent-salt difference is `NaCl` at 21.0 g/L.
- Confirm that no parser step splits an HTML link in the middle of a derivative sentence.

## Additional Notes

The generated note explicitly says the derivative modification is "still to be applied." That is useful audit provenance, but the merged YAML should not publish an intentionally unapplied source transformation as the effective recipe.
