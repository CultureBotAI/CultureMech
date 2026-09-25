# YAML Record Review: thiophaeococcus_mangrovi_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiophaeococcus_mangrovi_medium.yaml`
- Started UTC: 2026-09-25T13:09:01Z
- Finished UTC: 2026-09-25T13:09:01Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003873`
- Name: `thiophaeococcus_mangrovi_medium`
- Source grounding: KOMODO Medium 1162 merged with DSMZ Medium 1162 and DSMZ Medium 1358

## Validation

- Schema validation: passed with no issues.
- Strict validation: passed with zero errors; `/private/tmp/thiophaeococcus_mangrovi_medium.strict.tsv` was header-only.
- Reference validation: passed with zero checks.
- Term validation: passed after the known EUtils warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- KOMODO 1162 explicitly cites DSMZ Medium 1162.
- The merged record also absorbs DSMZ Medium 1358, `THIORHODOCOCCUS MEDIUM`, as `thiorhodococcus_medium`.
- The exact source search found DSMZ 1162, KOMODO 1162, and DSMZ 1358 as the only relevant local source records in this merge group; the search included ignored and hidden files.

## Evidence

- DSMZ 1162 lists the parent medium with KH2PO4 0.50 g, CaCl2 x 2 H2O 0.15 g, MgSO4 x 7 H2O 2.00 g, NH4Cl 0.64 g, NaCl 20.00 g, yeast extract 0.40 g, sodium pyruvate 3.00 g, 1 ml Micronutrient solution SL 8, 10 ml NaHCO3 at 10% w/v, 1 ml vitamin B12 at 2 mg/ml w/v, 1 mM Na2S x 9 H2O, 6 mM Na2S2O3 x 5 H2O, and 1000 ml water.
- DSMZ 1162 says to adjust to pH 7.5, bubble with nitrogen, and add filter-sterilized vitamin B12, Na2S x 9 H2O, and Na2S2O3 x 5 H2O only after autoclaving.
- Micronutrient solution SL 8 is a 1 L stock dosed at 1 ml into the parent recipe.
- DSMZ 1358 has a different parent formulation: NaCl 10.00 g, NH4Cl 0.60 g, NaHCO3 5 ml at 10% w/v, Na2S x 9 H2O 1 ml at 24% w/v, Na2S2O3 x 5 H2O 5 ml at 24% w/v, and yeast extract 0.30 g.

## Completeness

- The ingredient rows contain the DSMZ 1162 parent salts and SL 8 stock components.
- The KOMODO-selected merged record lacks the DSMZ nitrogen-bubbling and post-autoclave addition steps.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- The SL 8 micronutrient stock is flattened into final ingredients at stock concentration even though the source doses 1 ml of that stock.
- Vitamin B12 is recorded as `1` `G_PER_L`; DSMZ 1162 specifies 1 ml of a 2 mg/ml solution.
- DSMZ 1358 is merged as an exact duplicate even though its NaCl, NH4Cl, NaHCO3, sulfide, thiosulfate, and yeast extract amounts differ from DSMZ 1162.
- Choosing the KOMODO source as canonical dropped DSMZ 1162 preparation steps that matter for anaerobic, post-autoclave additions.

## Recommended Edits

- Restore DSMZ 1162 as a parent medium with a nested SL 8 stock dosed at 1 ml/L.
- Convert the vitamin B12 stock addition to final concentration or preserve it explicitly as a 1 ml stock dose.
- Split DSMZ 1358 back out of the exact-duplicate merge group and model it as a related formulation only after a curator reviews the differences.
- Preserve the DSMZ 1162 nitrogen and post-autoclave instructions in the canonical record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after stock and merge repair.
- Cross-check DSMZ 1162 against JCM J650, which uses a closely related SL8/thiosulfate formulation but is not byte-identical.

## Additional Notes

- Empty optional fields were not treated as defects.
