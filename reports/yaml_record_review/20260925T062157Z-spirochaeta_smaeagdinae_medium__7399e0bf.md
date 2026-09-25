# YAML Record Review: spirochaeta_smaeagdinae_medium__7399e0bf

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_smaeagdinae_medium__7399e0bf.yaml
- Started UTC: 2026-09-25T06:20:36Z
- Finished UTC: 2026-09-25T06:21:58Z
- Verdict: needs curation

## Target

Generated merged YAML for JCM 694, SPIROCHAETA SMAEAGDINAE MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_smaeagdinae_medium__7399e0bf.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to the correct JCM 694 source and preserves the final pH 7.0.

The generated ingredient list is not structurally faithful because JCM 694 has separately autoclaved Solutions A and B, a 10 ml trace-minerals addition from JCM 151, and 50 ml/4 ml anaerobic stock additions that have all been flattened into parent ingredients.

## Evidence

JCM 694 lists Solution A as 50.0 g NaCl, 1.0 g NH4Cl, 0.33 g K2HPO4, 0.33 g KH2PO4, 0.2 g KCl, 5.0 g yeast extract, 10.0 ml trace minerals from JCM 151, 0.5 g L-cysteine HCl x H2O, 1.0 mg resazurin, and 900.0 ml distilled water.

JCM 694 lists Solution B as 0.2 g MgCl2 x 6 H2O, 0.1 g CaCl2 x 2 H2O, and 50.0 ml distilled water. It then directs separately autoclaving Solutions A and B under N2-CO2 (4:1), combining them after cooling, adding 50.0 ml 8% NaHCO3 solution and 4.0 ml 5% Na2S x 9 H2O solution from sterile anaerobic stocks, and checking that the final pH is 7.0.

The referenced JCM 151 trace-minerals stock contains its own NaCl, CaCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, and 1.0 L distilled-water rows.

## Completeness

The generated record loses the Solution A and Solution B water rows, the two sterile stock additions, the 10 ml trace-minerals addition, and the JCM 151 trace-minerals stock water row.

## Findings

- Major: Solution A, Solution B, the JCM 151 trace-minerals stock, 8% NaHCO3 solution, and 5% Na2S x 9 H2O solution are flattened into a single parent ingredient list.
- Major: NaCl from Solution A was summed with NaCl from the JCM 151 trace-minerals stock even though those are distinct solution-scope rows.
- Major: CaCl2 x 2 H2O from Solution B was summed with CaCl2 x 2 H2O from the JCM 151 trace-minerals stock even though those are distinct solution-scope rows.
- Major: NaHCO3 and Na2S x 9 H2O are represented as `50` and `4` `G_PER_L`, which are the milliliter stock-addition amounts misread as concentrations.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/spirochaeta_smaeagdinae_medium.yaml` to preserve Solution A and Solution B as separate solution records with their source water rows.
- Model the JCM 151 trace-minerals row as a 10.0 ml addition under Solution A and keep its stock composition nested.
- Model 8% NaHCO3 solution and 5% Na2S x 9 H2O solution as sterile anaerobic additions with 50.0 ml and 4.0 ml volumes.
- Prevent duplicate-ingredient cleanup from summing same-name chemicals that occur in different solution scopes.
- Regenerate `data/merge_yaml/merged/spirochaeta_smaeagdinae_medium__7399e0bf.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm NaCl and CaCl2 x 2 H2O are no longer summed across Solution A/B and JCM 151.
- Confirm Solution A, Solution B, trace minerals, 8% NaHCO3 solution, and 5% Na2S x 9 H2O solution remain represented as separate solution-scope rows.
- Confirm final pH remains 7.0.

## Additional Notes

None found.
