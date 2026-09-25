# YAML Record Review: halodesulfuriarchaeum_medium__13fcab0a

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halodesulfuriarchaeum_medium__13fcab0a.yaml`
- Started UTC: 2026-09-23T10:19:28Z
- Finished UTC: 2026-09-23T10:20:43Z
- Verdict: needs curation

## Target

Generated merged YAML for the direct MediaDive/DSMZ import of DSMZ medium 1479, `HALODESULFURIARCHAEUM MEDIUM`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed; `/private/tmp/halodesulfuriarchaeum_medium__13fcab0a.strict.tsv` contained only the header row.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:1479` and DSMZ medium 1479.
- An ignored-file-inclusive exact search for `mediadive.medium:1479` and `DSMZ_Medium1479.pdf` found only the expected normalized DSMZ 1479 source and this generated merged record.
- A broader ignored-file-inclusive exact search for the shared Halodesulfuriarchaeum name also found separate JCM 1080 and TOGO M1149 records; those use a JCM source and should not be collapsed with DSMZ 1479 without source-level curation.
- Most simple salt and organic ingredients use appropriate CHEBI terms, but `NiCl2 x 6 H2O` is grounded only to generic nickel dichloride instead of a hexahydrate-specific term.

## Evidence

- The DSMZ PDF and MediaDive 1479 REST payload list 240 g NaCl, 2.5 g K2HPO4, 0.5 g ammonium sulfate, 10 g HEPES, 1 ml trace element solution, 2 g sulfur powder, and 1000 ml distilled water in the main liquid recipe.
- DSMZ then adds 3 mM MgCl2 x 6 H2O, 5 mM NaHCO3, 50 mM sodium formate, 0.2 g/L yeast extract, 1 ml/L vitamin mix, and 1 mM sulfide from a 1 M filter-sterilized stock before inoculation.
- The trace element solution and vitamin mix are stock recipes; each is dosed into the final medium at 1 ml/L.

## Completeness

- Missing main water: the explicit 1000 ml distilled-water row is absent.
- Missing trace-stock water: the trace element solution's 1000 ml distilled-water row is absent.
- Missing stock structure: trace element and vitamin stock concentrations are flattened into final medium ingredient rows.
- The final pH 3.0-4.0 instruction from DSMZ is present only as a trace-solution `ADJUST_PH` step, not as a final-medium pH range.

## Findings

1. The trace element solution was flattened at stock strength. EDTA, FeSO4 x 7 H2O, ZnSO4, MnCl2, H3BO3, CoCl2 x 6 H2O, CuCl2 x 5 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O are all 1000-fold higher than their final-medium concentrations because DSMZ adds only 1 ml of trace stock per liter.
2. The vitamin mix was also flattened at stock strength. Thiamin, calcium pantothenate, biotin, PABA, nicotinic acid, pyridoxine, folic acid, riboflavin, and B12 are all stock concentrations, not final medium concentrations after the 1 ml/L dose.
3. Water rows for the main medium and trace element solution were dropped, leaving the 1 L main volume and 1 L trace stock volume implicit.
4. Trace-element and vitamin-stock preparation steps were appended as ordinary medium-level steps. As a result, the final recipe appears to autoclave at 121 C, handle acidic and basic vitamin subsolutions, and filter-sterilize with no scope tying those operations to the trace and vitamin stocks.
5. The first preparation step is misclassified as `POUR_PLATES`, although DSMZ describes dispensing liquid medium into Hungate tubes or serum bottles under N2.

## Recommended Edits

- Model the trace element solution and vitamin mix as named stock solutions dosed at 1 ml/L, or scale every stock ingredient by 0.001 when flattening to the final medium.
- Restore distilled water to the main medium and trace element stock.
- Scope the pH, autoclaving, vitamin subsolution, and filtration instructions to the specific stock or final recipe they describe.
- Change the liquid Hungate/serum-bottle dispensing step from `POUR_PLATES` to an anaerobic dispensing operation.
- Add `ph_range` 3.0-4.0 for the final medium.
- Re-ground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term or leave it ungrounded if no exact term is available.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Compare the final recipe against both the DSMZ PDF and MediaDive 1479 REST payload, paying special attention to the 1 ml/L trace and vitamin stock doses.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:1479` and `DSMZ_Medium1479.pdf` to confirm there is still only one DSMZ 1479 normalized source after regeneration.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
