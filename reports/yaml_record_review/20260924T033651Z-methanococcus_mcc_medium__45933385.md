# YAML Record Review: methanococcus_mcc_medium__45933385
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanococcus_mcc_medium__45933385.yaml
- Started UTC: 2026-09-24T03:35:35Z
- Finished UTC: 2026-09-24T03:36:51Z
- Verdict: needs curation

## Target
- ID: CultureMech:002588
- Name: methanococcus_mcc_medium
- Label: METHANOCOCCUS McC MEDIUM
- Category: archaea
- Source: MediaDive/JCM medium J228
- Merge fingerprint: 45933385d4fdc778673084b064784cf4b9a3a65ea2135a19211d7ef31638691d
- Merged from: methanococcus_mcc_medium

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity matches JCM 228, METHANOCOCCUS McC MEDIUM, and MediaDive medium J228.
- Main salts and reducing agents have chemically specific CHEBI grounding.
- NiCl2 x 6 H2O is grounded to generic nickel dichloride rather than a hexahydrate-specific term.
- MnSO4 x n H2O is grounded to generic manganese(II) sulfate, which is acceptable for a variable-hydrate source label.

## Evidence
- JCM 228 lists a main formula containing 500 ml General salts solution, 10 ml Trace minerals solution, 5 ml Iron stock solution, NaCl, K2HPO4, Sodium acetate, Yeast extract, 1 mg Resazurin, NaHCO3, L-Cysteine HCl x H2O, Na2S x 9 H2O, and 485 ml distilled water.
- The General salts solution contains MgCl2 x 6 H2O, MgSO4 x 7 H2O, NH4Cl, KCl, and CaCl2 x 2 H2O.
- The Trace minerals solution contains Nitrilotriacetic acid, Fe(NH4)2(SO4)2 x 6 H2O, Na2SeO3, Na2MoO4 x 2 H2O, Na2WO4 x 2 H2O, MnSO4 x n H2O, ZnSO4 x 7 H2O, NiCl2 x 6 H2O, CuSO4 x 5 H2O, and 1 L distilled water.
- The Iron stock solution dissolves 0.2 g Fe(NH4)2(SO4)2 x 6 H2O in acidified water and brings the volume to 100 ml.
- The generated YAML has no `solutions` array or structured rows for 500 ml General salts solution, 10 ml Trace minerals solution, or 5 ml Iron stock solution.

## Completeness
- The final-medium standalone salts, pH value, and anaerobic preparation text are present.
- The source stock additions are not represented as stocks, and their contents were flattened into the final ingredient list.
- The Iron stock addition is present only as a preparation description; the 5 ml addition itself is not modeled.
- Empty optional fields are acceptable, but losing stock volumes makes the final concentrations ambiguous or inflated.

## Findings
- JCM source stocks were flattened. General salts, trace minerals, and iron stock are absent as solution additions even though the source main formula uses 500 ml, 10 ml, and 5 ml of those stocks.
- Trace minerals are represented at stock strength. For example, 1 g/L Na2WO4 x 2 H2O and 1.5 g/L NTA are the one-liter Trace minerals solution recipe, not final-medium concentrations after a 10 ml/L addition.
- The Iron stock solution is not included as a 5 ml/L addition. The preparation step describes its 0.2 g per 100 ml recipe, but no top-level or nested stock row preserves the source addition.
- The top-level Fe(NH4)2(SO4)2 x 6 H2O row is ambiguous because JCM lists the same compound in both Trace minerals solution and Iron stock solution.
- NiCl2 x 6 H2O needs hydrate-specific grounding if a suitable CHEBI identifier is available.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/methanococcus_mcc_medium.yaml` with explicit `General salts solution`, `Trace minerals solution`, and `Iron stock solution` entries.
- Preserve 500 ml/L, 10 ml/L, and 5 ml/L as source solution additions instead of promoting all stock contents to final-medium ingredients.
- Keep the 485 ml distilled water final-medium row separate from the trace-stock 1 L water row and the acidified Iron stock makeup volume.
- Keep the existing JCM anaerobic main preparation and attach the NTA/KOH and final pH steps to the trace-minerals stock.
- Ground NiCl2 x 6 H2O to a hydrate-specific term where possible.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanococcus_mcc_medium__45933385.yaml`.
- Confirm that the regenerated record contains the three JCM stock additions with source volumes.
- Confirm that trace-mineral stock rows are no longer top-level final-medium ingredients at stock strength.
- Confirm that the 5 ml Iron stock solution addition is represented.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- An exact local search with hidden and ignored files included found a separate TOGO M221/JCM_M228 owner for the same JCM source URL. Deduplicate the direct MediaDive/JCM and TOGO imports after both source owners are repaired.
