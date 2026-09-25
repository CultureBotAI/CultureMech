# YAML Record Review: methanofollis_ethanolicus_medium__a022ebcd
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanofollis_ethanolicus_medium__a022ebcd.yaml
- Started UTC: 2026-09-24T03:40:00Z
- Finished UTC: 2026-09-24T03:41:15Z
- Verdict: needs curation

## Target
- ID: CultureMech:003028
- Name: methanofollis_ethanolicus_medium
- Label: METHANOFOLLIS ETHANOLICUS MEDIUM
- Category: archaea
- Source: JCM, imported through MediaDive as mediadive.medium:J682
- Merge fingerprint: a022ebcd9098a274c206217475566bc1e3248bbeae1730b3856ef4c09e6b9d5b
- Merged from: methanofollis_ethanolicus_medium
- Maintained owner: data/normalized_yaml/archaea/methanofollis_ethanolicus_medium.yaml

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The ID, label, source accession, and `mediadive.medium:J682` grounding all identify direct MediaDive/JCM medium J682, METHANOFOLLIS ETHANOLICUS MEDIUM.
- An exhaustive hidden and ignored search found that `data/normalized_yaml/archaea/TOGO_M701_Methanofollis_Ethanolicus_Medium.yaml` is another JCM 682 import. Its fingerprint differs because the TOGO import retained empty solution placeholders that this direct MediaDive owner lacks.
- NiCl2 x 6 H2O is grounded to generic nickel dichloride even though the JCM table specifies the hexahydrate. The hydrated source label should remain unresolved or use a hydrate-specific CHEBI term if one is available.

## Evidence
- The JCM 682 source defines Solution A as salts, yeast extract, 2 ml Trace vitamins solution, 1 ml Trace element solution, 2.5 g NaHCO3, 1 mg Resazurin, and 900 ml water.
- The same source defines Solution B as 0.46 ml Ethanol in 100 ml water.
- The complete medium is 0.9 volume Solution A plus 0.1 volume Solution B, followed before inoculation by 0.01 volume each of 3% L-Cysteine HCl x H2O and Na2S x 9 H2O solutions.
- The direct MediaDive owner has no `solutions` array, so Solution A, Solution B, Trace vitamins solution, and Trace element solution are flattened into one final ingredient list. The top-level salts are close to source masses divided by 1003 ml rather than stock-aware final concentrations.
- The trace-vitamin rows are stock concentrations from the 1 L Trace vitamins solution, and the trace-element rows are stock concentrations from the 1 L Trace element solution. They are not diluted by their 2 ml and 1 ml additions to Solution A.
- No ingredient row represents the 3% L-Cysteine HCl x H2O solution or the 3% Na2S x 9 H2O solution.
- The preparation steps preserve the JCM prose for Solution A boiling under N2-CO2, Solution B filter sterilization under N2, anaerobic final assembly, and 10% inoculum, but steps 1 and 3 are only `Solution A:` and `Solution B:` headings because the subrecipes are not structural YAML objects.

## Completeness
- The main Solution A, Solution B, trace-vitamin, and trace-element formulas are all visible in flattened top-level rows.
- The required source structure for local Solution A/B subrecipes and their nested trace stocks is absent.
- The two 3% reducing-agent stock additions are absent from `ingredients` and `solutions`.
- Empty optional fields are acceptable; no optional-field omission was counted as a defect.

## Findings
- Major: JCM 682 stock and final-medium scopes are flattened in `data/normalized_yaml/archaea/methanofollis_ethanolicus_medium.yaml`. Solution A, Solution B, Trace vitamins solution, and Trace element solution need structural subrecipes because the JCM source uses their volumes to define final-medium concentrations.
- Major: Trace-stock formulas are promoted to final-medium concentrations in `data/normalized_yaml/archaea/methanofollis_ethanolicus_medium.yaml`. Values such as `4.9` mg Biotin per liter of trace stock and `1.27` g FeCl3 x 6 H2O per liter of trace stock are asserted as final-medium grams per liter.
- Major: Both 0.01-volume 3% reducing-agent stocks are omitted from `data/normalized_yaml/archaea/methanofollis_ethanolicus_medium.yaml`, so the generated record cannot reproduce JCM 682 prior to inoculation.
- Major: The Solution B ethanol entry in `data/normalized_yaml/archaea/methanofollis_ethanolicus_medium.yaml` is encoded as `0.46 G_PER_L`; JCM gives 0.46 ml in Solution B, and the import does not support a density-based conversion to grams.
- Minor: NiCl2 x 6 H2O is linked to generic nickel dichloride in `data/normalized_yaml/archaea/methanofollis_ethanolicus_medium.yaml`.
- Minor: The direct MediaDive J682 owner and `data/normalized_yaml/archaea/TOGO_M701_Methanofollis_Ethanolicus_Medium.yaml` are separate imports of the same JCM 682 recipe and need an explicit duplicate-resolution decision after both owners are structurally repaired.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/methanofollis_ethanolicus_medium.yaml` from direct JCM 682.
- Add local nested Solution A and Solution B recipes instead of flattening their children into the final medium.
- Nest Trace vitamins solution and Trace element solution under Solution A, each with 1 L water and source-scope concentrations.
- Represent final assembly as 0.9 volume Solution A, 0.1 volume Solution B, and 0.01 volume each of the two 3% reducing-agent stocks.
- Preserve 0.46 ml Ethanol as a volume in Solution B unless a curated density conversion is explicitly evidenced.
- Restore the 3% L-Cysteine HCl x H2O and 3% Na2S x 9 H2O reducing-agent stocks.
- Re-ground NiCl2 x 6 H2O to a hydrate-specific term if a suitable CHEBI term is available; otherwise leave the source label explicit and unresolved.
- After both JCM 682 owners are repaired, decide whether the direct MediaDive and TOGO M701 records should merge or whether one should be marked as a source duplicate of the other.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanofollis_ethanolicus_medium__a022ebcd.yaml`.
- Confirm that the regenerated direct JCM 682 record has explicit structural solutions for Solution A, Solution B, Trace vitamins solution, Trace element solution, and both 3% reducing-agent stocks.
- Confirm that the trace-stock rows no longer appear as top-level final-medium ingredients.
- Confirm that `0.46 ml` Ethanol is no longer represented as `0.46 G_PER_L`.
- Confirm that direct MediaDive J682 and TOGO M701 have a single duplicate-resolution policy after repair.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- The similarly named NBRC 1020/TOGO M1795 record is a distinct source recipe and needs independent review.
