# YAML Record Review: methanoculleus_medium__46bb4cbf
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanoculleus_medium__46bb4cbf.yaml
- Started UTC: 2026-09-24T03:36:52Z
- Finished UTC: 2026-09-24T03:38:12Z
- Verdict: needs curation

## Target
- ID: CultureMech:009119
- Name: methanoculleus_medium
- Label: Methanoculleus Medium
- Category: archaea
- Source: TOGO:M254, imported from JCM_M262
- Merge fingerprint: 46bb4cbfa16ef82f85a2cedee2f790fd6c8959187a3bcea5d87a8207dd3c3060
- Merged from: TOGO_M254_Methanoculleus_Medium

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity matches TOGO M254 and JCM 262.
- JCM 262 is a derivative recipe: use JCM Medium 265 and change final NaCl to 6.0 g.
- The generated record keeps the 6 g NaCl override.
- The referenced Wolfe mineral and trace-vitamin stocks inherited from JCM 265 are unresolved empty `Unknown solution` stubs.

## Evidence
- JCM 262 says to use Medium No. 265 with 6.0 g final NaCl.
- JCM 265 defines the methanogen base recipe with Wolfe's mineral solution, trace vitamins, 5% L-Cysteine HCl x H2O solution, and 5% Na2S x 9 H2O solution.
- JCM 265 also supplies the anaerobic preparation instructions: boil, cool under N2-CO2 80:20, dispense under H2-CO2 80:20, autoclave, add the separately autoclaved reducing solutions anaerobically, and pressurize inoculated vessels to 200 kPa H2-CO2 80:20.
- The generated YAML has final salts and the 6 g NaCl override, but its four inherited stock entries are empty and the record has no preparation steps.
- The generated YAML encodes source milligram rows as `G_PER_L`: 1 mg Resazurin appears as `1 G_PER_L`, and 2 mg Fe(NH4)2(SO4)2 x 6 H2O appears as `2 G_PER_L`.

## Completeness
- Main JCM 265 salts are mostly present with JCM 262's lower NaCl amount.
- Wolfe's mineral solution and Trace vitamins are absent except for empty cross-reference placeholders.
- The two 5% reducing-agent stocks are not curated as stock recipes.
- The JCM 265 anaerobic preparation procedure is missing.
- Empty optional fields are acceptable, but these stocks and preparation steps are part of the required source recipe.

## Findings
- Four source stock additions are empty placeholders: `Wolfe's mineral solution (see Medium [M257])`, `Trace vitamins (see Medium [M190])`, `5% Na2S x 9 H2O solution`, and `5% L-Cysteine-HCl-H2O solution`.
- The source stock additions use the wrong unit. Each 10 ml source addition is represented as `10 G_PER_L`.
- The reducing-agent stocks are duplicated in an inconsistent form: 0.5 g/L Cysteine-HCl and Na2S final-equivalent ingredient rows coexist with empty 10 ml stock placeholders.
- Resazurin and Fe(NH4)2(SO4)2 x 6 H2O were imported 1000-fold too high from JCM 265 milligram quantities.
- The record inherits no JCM 265 preparation text even though JCM 262 instructs users to use Medium No. 265.
- The direct MediaDive/JCM J262 owner is an active duplicate for the same source and appears to have resolved JCM 265 without retaining the 6 g final NaCl override.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/TOGO_M254_Methanoculleus_Medium.yaml` as JCM Medium 265 plus JCM 262's final 6 g NaCl override.
- Resolve or nest Wolfe's mineral solution, Trace vitamins, and the two 5% reducing-agent stocks.
- Represent the reducing stocks consistently: either as 10 ml additions of 5% stocks with nested stock recipes, or as final-equivalent 0.5 g/L rows without duplicate stock stubs.
- Convert 1 mg/L Resazurin to 0.001 G_PER_L and 2 mg/L Fe(NH4)2(SO4)2 x 6 H2O to 0.002 G_PER_L.
- Restore the inherited JCM 265 anaerobic preparation text and pH handling.
- After repairing both source owners, deduplicate the TOGO M254/JCM_M262 record with the direct `mediadive.medium:J262` record.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanoculleus_medium__46bb4cbf.yaml`.
- Confirm that `Unknown solution` is gone from this record.
- Confirm that 10 ml stock additions are no longer encoded as `G_PER_L`.
- Confirm that NaCl remains 6 g/L after resolving the JCM 265 base recipe.
- Confirm that source milligram quantities are not inflated to whole-number grams per liter.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- The exact hidden and ignored local search showed that `data/normalized_yaml/archaea/methanoculleus_medium.yaml` is the direct MediaDive/JCM import for the same JCM 262 source.
