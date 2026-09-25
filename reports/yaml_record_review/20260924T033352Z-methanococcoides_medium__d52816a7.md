# YAML Record Review: methanococcoides_medium__d52816a7
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanococcoides_medium__d52816a7.yaml
- Started UTC: 2026-09-24T03:32:15Z
- Finished UTC: 2026-09-24T03:33:53Z
- Verdict: needs curation

## Target
- ID: CultureMech:007554
- Name: methanococcoides_medium
- Label: Methanococcoides Medium
- Category: archaea
- Source: TOGO:M1039, imported from JCM_M986
- Merge fingerprint: d52816a7adab75740cb8e2039241a30925a017c0b2487c2064fe1fd625aa07db
- Merged from: TOGO_M1039_Methanococcoides_Medium

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity is the JCM 986 Methanococcoides Medium imported through TOGO M1039.
- The source recipe is a derivative of JCM 265: use Methanogenium Medium, add 3.0 g/L trimethylamine-HCl, adjust pH to 7.0 to 7.2, and use an 80:20 N2-CO2 gas mixture.
- The derivative Methanogenium Medium reference is not resolved. It remains an `Unknown solution` named `METHANOGENIUM MEDIUM (see Medium [M257])`.
- The trimethylamine-HCl ingredient is not grounded even though TOGO labels it as trimethylamine hydrochloride and other generated records use CHEBI:64700 for that reagent.

## Evidence
- The live JCM 986 page says to use Medium No. 265 supplemented with 3.0 g/L trimethylamine-HCl, adjust pH to 7.0 to 7.2, and prepare and cultivate under an N2-CO2 80:20 gas mixture.
- TOGO M1039 preserves that derivative formula as 3 g/L trimethylamine-HCl plus a 1 L reference to M257, the TOGO import of JCM 265.
- JCM 265 and TOGO M257 are non-empty Methanogenium Medium recipes with base salts, Wolfe's mineral solution, trace vitamins, reducing solutions, and anaerobic preparation text.
- The generated YAML only has trimethylamine-HCl, Carbon dioxide gas, Nitrogen gas, and a single empty cross-reference solution.
- The generated YAML has no `ph_value`, `preparation_steps`, base JCM 265 ingredients, nested stock recipes, or structured cross-reference to CultureMech:009148/TOGO:M257.

## Completeness
- The 3 g/L trimethylamine-HCl supplement from JCM 986 is present.
- The underlying JCM 265/M257 base medium is absent except for a placeholder `Unknown solution`.
- The pH range and N2-CO2 ratio from JCM 986 are absent.
- Empty optional fields are acceptable, but this record is missing the referenced medium that defines the bulk of the recipe.

## Findings
- The Medium M257 cross-reference was not resolved. The record should include, nest, or explicitly link the one-liter JCM 265/M257 base medium instead of leaving `composition: []`.
- The medium reference uses the wrong quantity model: one liter of Methanogenium Medium is represented as `1 G_PER_L`.
- JCM 986 pH metadata was dropped. TOGO captured `ph: 7.0-7.2`, and the direct JCM-derived local record records the midpoint as `ph_value: 7.1`, but this TOGO-derived YAML has no pH field or preparation step describing the range.
- The 80:20 N2-CO2 atmosphere was flattened into two variable gas ingredients, losing the source ratio and the fact that it applies to preparation and cultivation.
- The only chemical supplement, trimethylamine-HCl, lacks a `term` and `mediaingredientmech_chebi_term`.

## Recommended Edits
- Resolve the `METHANOGENIUM MEDIUM (see Medium [M257])` placeholder against TOGO:M257/JCM 265 after that base record's stock-solution issues are fixed.
- Replace the `1 G_PER_L` placeholder with either an explicit nested 1 L base-medium recipe or a structured cross-reference that cannot be confused with a solute concentration.
- Add `ph_value: 7.1` or equivalent range-preserving preparation text for JCM's pH 7.0 to 7.2 instruction.
- Preserve the JCM 986 N2-CO2 80:20 gas mixture in preparation text.
- Ground trimethylamine-HCl to trimethylamine hydrochloride, CHEBI:64700, if that term is still the project-preferred mapping.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanococcoides_medium__d52816a7.yaml`.
- Confirm that `Unknown solution` is gone from this record.
- Confirm that no referenced liter of base medium is represented as `G_PER_L`.
- Confirm that the regenerated record contains the pH range or midpoint, the 80:20 N2-CO2 gas mixture, and a grounded trimethylamine-HCl row.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- An exact local search with hidden and ignored files included found `data/normalized_yaml/archaea/JCM_J986_METHANOCOCCOIDES_MEDIUM.yaml`, an active direct-JCM record for the same JCM 986 source. After both owners are repaired, deduplicate the direct JCM 986 and TOGO M1039 imports so one source recipe does not remain as two unrelated CultureMech records.
