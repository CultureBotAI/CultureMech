# YAML Record Review: acidihalobacter_prosperus_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDIHALOBACTER_PROSPERUS_MEDIUM.yaml`
- Started UTC: 2026-09-21T09:04:35Z
- Finished UTC: 2026-09-21T09:06:07Z
- Verdict: needs curation

## Target

Generated merge record `ACIDIHALOBACTER_PROSPERUS_MEDIUM.yaml` is a singleton merge from `data/normalized_yaml/bacterial/acidihalobacter_prosperus_medium.yaml`. It represents DSMZ Medium 477 / ACIDIHALOBACTER PROSPERUS MEDIUM.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history/` files.

## Identity and Grounding

The direct DSMZ identity is correct: `mediadive.medium:477` points at `DSMZ_Medium477.pdf`, and the fetched DSMZ PDF names Medium 477 as ACIDIHALOBACTER PROSPERUS MEDIUM.

There is still a same-DSMZ duplicate split. The ignored-inclusive exact source-ID search found `KOMODO_477_THIOBACILLUS_PROSPERUS_MEDIUM.yaml` and generated `THIOBACILLUS_PROSPERUS_MEDIUM.yaml` with KOMODO Medium 477 / `mediadive.medium:477` in notes. That is the same DSMZ Medium 477 formula under the historical Thiobacillus prosperus name and should eventually merge with the direct DSMZ 477 source.

## Evidence

- Primary DSMZ Medium 477 PDF fetched during review: lists a base recipe with KCl, MgCl2.6H2O, MgSO4.7H2O, NH4Cl, CaCl2.2H2O, K2HPO4, KH2PO4, NaCl, 10 ml Modified Wolin's mineral solution, 2 ml NiCl2 0.1%, 50 ml FeSO4.7H2O 40%, and 940 ml distilled water; it instructs adding FeSO4 from a 40% stock in 0.2 N H2SO4 under 100% N2. It also gives the separate Modified Wolin's mineral solution formula from Medium 141.
- Generated target: stores the base rows and every Modified Wolin component in one flat `ingredients` list, with duplicate same-salt rows summed.
- KOMODO 477 normalized record: copies the same flattened DSMZ Medium 477 signature into a separate Thiobacillus prosperus generated record.

## Completeness

The generated target keeps the DSMZ pH and some key preparation text, including the 40% FeSO4 / 0.2 N H2SO4 / 100% N2 stock instruction. It does not preserve the recipe hierarchy, however: Modified Wolin's mineral solution, 0.1% NiCl2, and 40% FeSO4 are not represented as added stock solutions.

Because those boundaries are gone, the final ingredient list cannot distinguish base-medium salts from 10 ml of Wolin's mineral stock and cannot distinguish 2 ml of NiCl2 0.1% from the NiCl2 row within Wolin's solution.

## Findings

- CRITICAL: Modified Wolin's mineral solution was flattened into final ingredients. Its 1 L stock formula contributes rows such as 3 g/L MgSO4.7H2O, 1 g/L NaCl, and 0.1 g/L FeSO4.7H2O to the generated final medium even though DSMZ calls for only 10 ml of that stock per liter.
- MAJOR: Duplicate ingredients from separate compartments were summed. The target adds base-medium MgSO4, CaCl2, NaCl, NiCl2, and FeSO4 rows to same-named stock-solution rows, producing inflated concentrations such as `20.060100000000002 G_PER_L` FeSO4.7H2O and `6.44311 G_PER_L` MgSO4.7H2O.
- MAJOR: The 2 ml 0.1% NiCl2 addition and 50 ml 40% FeSO4 addition were flattened into top-level final rows instead of being modeled as separately prepared solution additions.
- MAJOR: DSMZ Medium 477 is split from the KOMODO Medium 477 / THIOBACILLUS PROSPERUS record, which cites the same DSMZ source ID and carries the same flattened formula.
- MINOR: The generated target omits the explicit `Distilled water 940 ml` base row; this is secondary to the stock-boundary loss but should be handled consistently when DSMZ 477 is re-curated.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/acidihalobacter_prosperus_medium.yaml` with the DSMZ hierarchy intact: base salts plus 940 ml water, 10 ml Modified Wolin's mineral solution, 2 ml 0.1% NiCl2, and 50 ml 40% FeSO4 stock solution.
- Move the Medium 141 Wolin formula into the Modified Wolin stock `composition` or a structured cross-reference rather than flattening it into final `ingredients`.
- Keep the 40% FeSO4 stock prepared in 0.2 N H2SO4 under 100% N2 as a separate solution addition and preserve the existing pre-inoculation addition text.
- Merge or otherwise alias `KOMODO_477_THIOBACILLUS_PROSPERUS_MEDIUM` with the corrected DSMZ Medium 477 source so exact `mediadive.medium:477` does not appear in two generated recipes.

## Follow-up Checks

- Run schema, strict, reference, and term validation on the corrected DSMZ 477 normalized source and regenerated target.
- Re-run an ignored-inclusive exact search for `mediadive.medium:477` and `DSMZ_Medium477.pdf` to verify direct DSMZ and KOMODO-derived DSMZ 477 sources are reconciled.
- Confirm regenerated DSMZ 477 no longer has `Merged 2 duplicates` notes on salts that came from different stock compartments.

## Additional Notes

The DSMZ PDF's `For DSM 14174` K2S4O6 supplementation is a strain-specific instruction. It should remain represented as a separate DSM 14174 variant rather than being folded unconditionally into the base ACIDIHALOBACTER PROSPERUS MEDIUM record.
