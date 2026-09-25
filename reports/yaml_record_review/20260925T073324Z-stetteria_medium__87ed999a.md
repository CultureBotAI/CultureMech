# YAML Record Review: STETTERIA MEDIUM
- Repository: CultureMech
- Record: data/merge_yaml/merged/stetteria_medium__87ed999a.yaml
- Started UTC: 2026-09-25T07:33:24Z
- Finished UTC: 2026-09-25T07:33:24Z
- Verdict: needs curation

## Target
Reviewed generated record `CultureMech:001938` / `stetteria_medium` from `data/merge_yaml/merged/stetteria_medium__87ed999a.yaml`.

The generated record has one source, direct MediaDive/DSMZ medium 795, and it corresponds to DSMZ `STETTERIA MEDIUM`.

## Validation
- Schema validation: Passed with `No issues found`.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The source identity is preserved for the direct DSMZ import: the generated record cites `mediadive.medium:795`, links to `DSMZ_Medium795.pdf`, and carries pH 6.0 from the MediaDive/DSMZ source.

An exact source search also found normalized and generated KOMODO records for `komodo.medium:795`; those records have the same DSMZ medium number but a different ingredient signature, so they remain separate from the direct DSMZ generated record reviewed here.

## Evidence
The DSMZ medium 795 PDF and MediaDive payload define a 1018 ml main solution. The main solution adds 500 ml 2x Synthetic seawater, 0.16 g NaHCO3, 0.5 g KH2PO4, 15 ml Modified Wolin's mineral solution, 3 ml NiCl2 x 6 H2O at 0.1% w/v, 2 g peptone, 1 g yeast extract, 0.5 ml sodium resazurin at 0.1% w/v, 10 g powdered sulfur, 0.5 g Na2S x 9 H2O, and 500 ml distilled water.

Modified Wolin's mineral solution is a 1 L stock with nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O. Only 15 ml of that stock goes into 1018 ml of main solution.

Synthetic seawater is a separate 2x, 1 L stock with 55.4 g NaCl, 0.03 g SrCl2 x 6 H2O, 14 g MgSO4 x 7 H2O, 0.1 mg KI, 11 g MgCl2 x 6 H2O, 20 mg Na3-citrate, 1.3 g KCl, 1.5 g CaCl2 x 2 H2O, 0.2 g NaBr, and 0.06 g H3BO3. The main recipe adds 500 ml of that stock, so those concentrations must be scaled to the final 1018 ml main volume.

The source preparation also says to sparge with 80% N2 and 20% CO2 for 30 to 45 minutes, dispense into sulfur-containing vials under the same gas, pressurize with 80% H2 and 20% CO2 to 2 bar overpressure, heat at 100 C for 1.5 hours on each of 3 successive days, then add sulfide from a sterile anoxic stock prepared under 100% N2 and adjust complete medium to pH 6.0 if necessary.

## Completeness
The generated record preserves DSMZ pH and preparation text, and it correctly converted direct main-solution amounts such as NaHCO3, KH2PO4, peptone, yeast extract, sodium resazurin, sulfur, and sodium sulfide by using the 1018 ml main-solution denominator.

The stock compounds are not scaled correctly. Modified Wolin's mineral entries were copied at full stock concentration even though only 15 ml is added to 1018 ml, and 2x synthetic seawater entries were copied at full stock concentration even though only 500 ml is added to 1018 ml. Shared salts were then summed across unrelated stocks, yielding rows such as MgSO4 x 7 H2O 17 g/L from 3 plus 14, NaCl 56.4 g/L from 1 plus 55.4, CaCl2 x 2 H2O 1.6 g/L from 0.1 plus 1.5, and H3BO3 0.07 g/L from 0.01 plus 0.06.

The extra 3 ml 0.1% NiCl2 x 6 H2O addition was converted correctly to 0.00294695 g/L, but it was summed with the unscaled 0.03 g/L Wolin-stock NiCl2 row. The expected Wolin contribution should be divided by the stock-addition volume before summing.

The sulfur row is grounded to `CHEBI:26833` / `sulfur atom`, which is too atomic for powdered elemental sulfur as a supplied medium ingredient.

## Findings
- The direct main-solution concentrations are on the 1018 ml basis, but the Wolin and seawater stock rows are on their own 1 L stock basis.
- Duplicate collapse summed stock-internal salts across different stock solutions before stock dilution was applied.
- The NiCl2 row mixes one correctly scaled main addition with one unscaled Wolin-stock contribution.
- Synthetic seawater is a 2x stock and should not leave NaCl, MgSO4, CaCl2, H3BO3, or other seawater ions at full 2x strength in the final medium.
- Powdered sulfur should be re-grounded to an elemental sulfur material term rather than to the sulfur atom class.

## Recommended Edits
- Fix `data/normalized_yaml/archaea/stetteria_medium.yaml` or the MediaDive import logic, then regenerate `data/merge_yaml/merged/stetteria_medium__87ed999a.yaml`; do not hand-edit the generated merged YAML.
- Preserve Modified Wolin's mineral solution and 2x Synthetic seawater as stock additions, or scale each stock by its addition volume before flattening into final ingredient rows.
- Apply duplicate collapse only after all contributions use the same final-medium concentration basis.
- Keep the current direct scaling for main-solution gram, milliliter stock, and sulfur/sulfide rows.
- Re-ground powdered `Sulfur` to a CHEBI term appropriate for elemental sulfur as a bulk ingredient.

## Follow-up Checks
- Recompute MgSO4, NaCl, CaCl2, H3BO3, and NiCl2 after applying the 15/1018 and 500/1018 stock volume factors.
- Confirm `ph_value: 6.0` and both DSMZ preparation steps survive regeneration.
- Confirm no final row still contains a summed duplicate note whose parts are unscaled stock concentrations.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The exact local search for `mediadive.medium:795`, `komodo.medium:795`, and `CultureMech:001938` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`. An earlier unbounded search for `mediadive.medium:795` also matched `mediadive.medium:795a` and was discarded.
