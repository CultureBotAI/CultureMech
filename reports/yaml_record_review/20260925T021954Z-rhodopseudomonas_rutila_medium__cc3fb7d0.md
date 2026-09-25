# YAML Record Review: rhodopseudomonas_rutila_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodopseudomonas_rutila_medium__cc3fb7d0.yaml`
- Started UTC: 2026-09-25T02:19:53Z
- Finished UTC: 2026-09-25T02:20:02Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:010298` for TOGO Medium M87 / JCM_M95, generated from `data/normalized_yaml/bacterial/TOGO_M87_Rhodopseudomonas_Rutila_Medium.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M87 cites original media ID `JCM_M95` and the JCM Medium 95 URL for Rhodopseudomonas rutila medium. The generated target correctly denotes that TOGO/JCM source, but it is split from `data/normalized_yaml/bacterial/JCM_J95_RHODOPSEUDOMONAS_RUTILA_MEDIUM.yaml`, another owner of the same JCM 95 source.

An exact ignored-inclusive search for `TOGO:M87`, `mediadive.medium:J95`, `mediadive.medium:633`, `JCM_M95`, `GRMD=95`, and `DSMZ_Medium633` found only the three expected Rhodopseudomonas rutila owners and their generated targets under the relevant data trees. DSMZ Medium 633 shares the label but is not a duplicate of JCM 95 because its own MediaDive record lists 1 mg/L biotin and MnSO4 x H2O, while JCM 95 lists 0.01 mg/L biotin and MnSO4 x n H2O.

## Evidence

JCM Medium 95 and MediaDive J95 list 2 g yeast extract, 2 g sodium L-malate, 2 g sodium glutamate, 1 g KH2PO4, 0.5 g NaHCO3, 0.2 g MgSO4 x 7H2O, 0.1 g CaCl2 x 2H2O, 2 mg MnSO4 x n H2O, 0.5 mg FeSO4 x 7H2O, 0.5 mg CoCl2 x 6H2O, 1 mg thiamine HCl, 1 mg nicotinic acid, 0.01 mg biotin, and 1 L distilled water.

TOGO M87 preserves the same source rows and units, but the generated TOGO record converts every low-abundance milligram row to a gram-per-liter value: `MnSO4.xH2O` is 2 g/L instead of 0.002 g/L, `FeSO4.7H2O` and `CoCl2.6H2O` are 0.5 g/L instead of 0.0005 g/L, `Thiamine.HCl` and nicotinic acid are 1 g/L instead of 0.001 g/L, and biotin is 0.01 g/L instead of 0.00001 g/L.

## Completeness

The reviewed target carries JCM 95's water row but stores the 1 L source quantity as `1 G_PER_L`. The direct JCM J95 duplicate has the correct non-water concentrations but omits the same 1 L distilled-water row.

Empty optional pH, literature, and organism fields are not defects; JCM 95 and TOGO M87 do not provide pH.

## Findings

- Major: `data/normalized_yaml/bacterial/TOGO_M87_Rhodopseudomonas_Rutila_Medium.yaml` converted source milligrams to whole gram-per-liter values for six trace and vitamin ingredients, making the generated target 1000x too concentrated for those rows.
- Major: `data/normalized_yaml/bacterial/TOGO_M87_Rhodopseudomonas_Rutila_Medium.yaml` also converted 1 L distilled water to `1 G_PER_L`; the source row is volumetric.
- Major: the TOGO owner still has legacy `mediaingredientmech_term` on `Sodium L--malate` instead of a CHEBI primary link, and its `CoCl2.6H2O` row is grounded only to anhydrous cobalt dichloride rather than cobalt chloride hexahydrate.
- Major: the JCM 95 duplicate owner omits the 1000 ml distilled-water row that MediaDive J95 exposes.
- Major: `data/merge_yaml/merged` emits separate targets for TOGO M87 and JCM J95 even though both owners cite the same JCM 95 source recipe.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M87_Rhodopseudomonas_Rutila_Medium.yaml` so milligram ingredients are 0.002, 0.0005, 0.0005, 0.001, 0.001, and 0.00001 g/L, and so distilled water stays volumetric.
- Replace the legacy sodium L-malate MediaIngredientMech link with the CHEBI grounding used by the JCM J95 owner, and ground `CoCl2.6H2O` to cobalt chloride hexahydrate.
- Add the 1000 ml/L distilled-water row to `data/normalized_yaml/bacterial/JCM_J95_RHODOPSEUDOMONAS_RUTILA_MEDIUM.yaml`.
- Add a source-duplicate relationship between TOGO M87 and JCM J95, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for the regenerated TOGO/JCM J95 target.
- Confirm the regenerated target has one water row and JCM 95 gram-per-liter conversions for every milligram row.
- Confirm `data/merge_yaml/merged` no longer emits both `rhodopseudomonas_rutila_medium__cc3fb7d0.yaml` and `RHODOPSEUDOMONAS_RUTILA_MEDIUM.yaml`.
- Confirm DSMZ Medium 633 remains separate from JCM 95 unless a curated relationship explicitly captures its distinct biotin and manganese-source choices.

## Additional Notes

No additional issues.
