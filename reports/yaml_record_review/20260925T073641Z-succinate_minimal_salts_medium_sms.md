# YAML Record Review: SUCCINATE MINIMAL SALTS MEDIUM (SMS)
- Repository: CultureMech
- Record: data/merge_yaml/merged/succinate_minimal_salts_medium_sms.yaml
- Started UTC: 2026-09-25T07:36:41Z
- Finished UTC: 2026-09-25T07:36:41Z
- Verdict: needs curation

## Target
Reviewed generated record `CultureMech:000833` / `succinate_minimal_salts_medium_sms` from `data/merge_yaml/merged/succinate_minimal_salts_medium_sms.yaml`.

The generated record has one source, direct MediaDive/DSMZ medium 1372.

## Validation
- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The record identity is preserved: the generated record cites `mediadive.medium:1372`, links to `DSMZ_Medium1372.pdf`, and carries the DSMZ name `SUCCINATE MINIMAL SALTS MEDIUM (SMS)`.

The exact source search found one normalized DSMZ source, one generated merged record, and the expected indexes for `CultureMech:000833` / `mediadive.medium:1372`.

## Evidence
The DSMZ medium 1372 PDF and the MediaDive payload agree on a 1 L main recipe with EDTA 0.010 g, KH2PO4 0.600 g, K2HPO4 0.900 g, NH4Cl 1.000 g, MgSO4 x 7 H2O 0.200 g, CaCl2 x 6 H2O 0.075 g, sodium succinate 2.200 g, yeast extract 0.100 g, 2.000 ml Trace elements solution, 2.000 ml Vitamin solution, and 1000.000 ml distilled water, adjusted to pH 6.8.

The trace-elements formula is a separate 1 L stock with FeSO4 x 6 H2O 0.300 g, ZnSO4 x 7 H2O 0.005 g, MnCl2 x 4 H2O 0.003 g, H3BO3 0.002 g, CoCl2 x 6 H2O 0.005 g, CuCl2 x 2 H2O 0.001 g, NiCl2 x 6 H2O 0.002 g, and Na2MoO4 x 2 H2O 0.003 g.

The vitamin formula is also a separate 1 L stock with 80 mg biotin, 400 mg thiamine-HCl x 2 H2O, 400 mg nicotinic acid, 20 mg vitamin B12, and 1000 ml distilled water. DSMZ says to prepare the main medium without this vitamin solution, autoclave, then add the vitamin solution from a filter-sterilised stock solution.

## Completeness
The direct main-solution salts, sodium succinate, yeast extract, pH 6.8 value, and preparation steps are represented correctly.

The trace-elements and vitamin rows are not final concentrations. The source adds 2 ml of each stock per 1000 ml, so every trace and vitamin stock concentration must be scaled by 0.002 if it is flattened into the final ingredient list. The generated record instead exposes FeSO4 x 6 H2O at 0.3 `G_PER_L`, ZnSO4 x 7 H2O at 0.005 `G_PER_L`, biotin at 0.08 `G_PER_L`, thiamine-HCl x 2 H2O at 0.4 `G_PER_L`, and the other stock components at full stock strength.

The generated record also omits explicit stock-solution rows, which hides why the trace and vitamin ingredients must be added after dilution and, for vitamins, after filter sterilization.

## Findings
- `Trace elements solution` and `Vitamin solution` were flattened as full-strength stock recipes instead of 2 ml/L additions.
- The final trace-metal and vitamin ingredient concentrations are therefore 500 times too high.
- The vitamin stock is filter-sterilised and added after autoclaving, but the ingredients are indistinguishable from autoclaved main-solution ingredients in the generated top-level list.
- No generated solution structure records the two 2 ml/L stock additions.

## Recommended Edits
- Fix `data/normalized_yaml/bacterial/succinate_minimal_salts_medium_sms.yaml` or the MediaDive import logic, then regenerate `data/merge_yaml/merged/succinate_minimal_salts_medium_sms.yaml`; do not hand-edit the generated merged YAML.
- Preserve Trace elements solution and Vitamin solution as structured stocks with 2 ml/L addition volumes, or scale their constituents by 0.002 before flattening.
- Keep the pH 6.8 and the existing vitamin-after-autoclave preparation instruction.

## Follow-up Checks
- Verify FeSO4 x 6 H2O, ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O are no longer present at full stock strength.
- Verify biotin, thiamine-HCl x 2 H2O, nicotinic acid, and vitamin B12 are no longer present at full stock strength.
- Confirm `ph_value: 6.8` and the filtered vitamin-addition preparation step survive regeneration.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The exact local search for `mediadive.medium:1372`, `CultureMech:000833`, and `succinate_minimal_salts_medium_sms` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`.
