# YAML Record Review: methanosarcina_z_7115_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosarcina_z_7115_medium.yaml
- Started UTC: 2026-09-24T05:10:06Z
- Finished UTC: 2026-09-24T05:10:06Z
- Verdict: pass with minor issues

## Target

Generated `MediaRecipe` `CultureMech:015858` for JCM medium 1415, "METHANOSARCINA Z-7115 MEDIUM".

## Validation

- LinkML open schema validation: Passed with "No issues found".
- Strict recipe validation: Passed; `/private/tmp/methanosarcina_z_7115_medium.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The identity is grounded to JCM GRMD 1415, and the live JCM page still serves "METHANOSARCINA Z-7115 MEDIUM".
- The generated parent ingredients, post-autoclave stock additions, pH 7.0 value, 960 ml water row, and solution-addition volumes match the JCM 1415 source.
- JCM 899 and JCM 197 both still resolve as live stock-medium pages for the referenced trace element and vitamin additions.

## Evidence

- JCM 1415 lists NH4Cl, CaCl2 x 2 H2O, KH2PO4, MgCl2 x 6 H2O, sodium acetate, 1 ml Trace element solution from Medium 899, 0.5 mg resazurin, and 960 ml distilled water before autoclaving.
- The live source then adds 25 ml 8% NaHCO3 solution, 10 ml Trace vitamins from Medium 197, and 4 ml 50% methanol aseptically and anaerobically after cooling.
- The source dispenses the medium into culture vessels under the same gas mixture, seals with butyl rubber stoppers, and finally adds 5 ml each of 5% L-Cysteine HCl H2O and 5% Na2S x 9 H2O per liter.
- The generated record preserves all of those volume and mass rows, but step 3 stops after the first post-cooling solution table and the dispensing sentence.

## Completeness

- No scalar ingredients are missing.
- No source stock table was flattened into the parent ingredient list.
- The final cysteine and sulfide addition instruction is absent.
- Medium 899 and Medium 197 are preserved only in preferred-term text, not as structured linked stock media.

## Findings

1. Minor - The final reducing-agent addition prose was dropped. The source says to add 5% L-Cysteine HCl H2O and 5% Na2S x 9 H2O after dispensing and sealing the bottles, but the generated `preparation_steps` end after the earlier bicarbonate/vitamin/methanol addition and dispensing sentence.
2. Minor - Cross-medium stock references are unstructured. The Medium 899 trace element solution and Medium 197 trace vitamin solution are retained as preferred-term strings rather than linked JCM stock recipes.
3. Minor - The JCM default autoclave condition is implicit only. The source page header says JCM media are autoclaved at 121 C for 15 min unless otherwise stated; the generated record records an autoclave step under N2-CO2 but omits the default temperature and time.

## Recommended Edits

- Append the final cysteine/sulfide addition sentence to the preparation sequence after the gas-phase dispensing step.
- Resolve JCM Medium 899 and JCM Medium 197 references as structured stock links or curated child recipes.
- Carry JCM's default 121 C, 15 min autoclave condition into preparation metadata if the schema supports it.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Compare the regenerated ingredient list against JCM 1415 to confirm no Medium 899 or Medium 197 stock components are pulled into the parent formula.

## Additional Notes

The source itself spells `8% NaHCO3 soluiton*`; the generated preferred term preserves that source typo. That is harmless for source fidelity, though a display label cleanup could store the corrected spelling with the original row text in provenance.
