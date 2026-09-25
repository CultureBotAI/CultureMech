# YAML Record Review: CLOSTRIDIUM KLUYVERI MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_kluyveri_medium__0da19d24.yaml`
- Started UTC: `2026-09-22T09:20:07Z`
- Finished UTC: `2026-09-22T09:20:17Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:001661` for MediaDive medium `52`, DSMZ Medium 52 `CLOSTRIDIUM KLUYVERI MEDIUM`. The generated record merges the direct MediaDive record `clostridium_kluyveri_medium.yaml` with KOMODO source duplicate `clostridium_kluyveri_medium_modified.yaml` on merge fingerprint `0da19d24806a5bbd8a3c6671fc62b66aa59334726e94faba7c0eb01f1ccc2290`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_kluyveri_medium__0da19d24.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The main DSMZ/MediaDive identity is recognizable: the record links to `mediadive.medium:52`, names DSMZ Medium 52, and cites `DSMZ_Medium52.pdf`.

The KOMODO child has the same ingredient signature as the DSMZ source and is plausibly a duplicate, but its notes still say `Aerobic: Yes` while DSMZ Medium 52 is explicitly prepared anoxically under 80% N2 / 20% CO2 and with 100% N2 stock solutions.

Ingredient grounding is mostly specific, but `NiCl2 x 6 H2O` is still grounded to generic `CHEBI:34887` / nickel dichloride. `Ethanol absolute` also retains a legacy `mediaingredientmech_term` rather than a CHEBI-keyed `mediaingredientmech_chebi_term`.

An unmerged generated TOGO branch, `data/merge_yaml/merged/CLOSTRIDIUM_KLUYVERI_MEDIUM.yaml`, points to the same DSMZ Medium 52 PDF through TOGO `M2703`.

## Evidence

The DSMZ Medium 52 PDF supports the base ingredients, pH 6.8-7.0, the anaerobic Hungate/serum-vial preparation, the optional post-inoculation sodium dithionite note, and Trace element solution SL-10 preparation text copied into `preparation_steps`.

The PDF also shows that Trace element solution SL-10, Selenite-tungstate solution, and Seven vitamins solution are one-liter stock recipes. The final medium receives only 1 ml of each stock. DSMZ additionally lists ethanol as `20.00 ml`, not 20 g.

The ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found the canonical DSMZ source, the KOMODO duplicate, and the TOGO `M2703` branch for DSMZ Medium 52.

## Completeness

The record preserves pH and the major preparation instructions, but it is incomplete as a structured stock solution record:

- There is no `solutions` entry for Trace element solution SL-10.
- There is no `solutions` entry for Selenite-tungstate solution.
- There is no `solutions` entry for Seven vitamins solution.
- The Selenite-tungstate and Seven vitamins stock recipes have no structured stock context.
- The TOGO `M2703` source is not merged with this DSMZ/KOMODO branch.

## Findings

- Trace element solution SL-10 is flattened into parent final-medium ingredients. `HCl` `2.5 G_PER_L`, `FeCl2 x 4 H2O` `1.5 G_PER_L`, `ZnCl2` `0.07 G_PER_L`, `MnCl2 x 4 H2O` `0.1 G_PER_L`, `H3BO3` `0.006 G_PER_L`, `CoCl2 x 6 H2O` `0.19 G_PER_L`, `CuCl2 x 2 H2O` `0.002 G_PER_L`, `NiCl2 x 6 H2O` `0.024 G_PER_L`, and `Na2MoO4 x 2 H2O` `0.036 G_PER_L` are one-liter stock concentrations for a stock dosed at 1 ml/l of final medium.
- Selenite-tungstate internals are also flattened. `NaOH`, `Na2SeO3 x 5 H2O`, and `Na2WO4 x 2 H2O` are final ingredients at their stock concentrations even though the source adds only 1 ml/l of that stock.
- Seven vitamins internals are flattened. Rows such as `Vitamin B12` `0.1 G_PER_L`, `p-Aminobenzoic acid` `0.08 G_PER_L`, `Nicotinic acid` `0.2 G_PER_L`, and `Pyridoxine hydrochloride` `0.3 G_PER_L` are stock strengths, not final concentrations.
- `Ethanol absolute` is stored as `20 G_PER_L`, but DSMZ specifies 20 ml per liter. This should be modeled as a volume aliquot or converted with an explicit density rule, not silently treated as grams.
- The current duplicate graph leaves TOGO `M2703` as a separate generated recipe for the same DSMZ source. That branch has the more severe TOGO flattening failure: summed water across all stocks, gram-per-liter reinterpretation of stock milligrams, gas atmosphere rows as variable ingredients, and empty solution shells.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/clostridium_kluyveri_medium.yaml` or the MediaDive stock import logic, then regenerate; `data/merge_yaml/merged/clostridium_kluyveri_medium__0da19d24.yaml` is derived.
- Move Trace element solution SL-10, Selenite-tungstate solution, and Seven vitamins solution into `solutions[*]` with their real stock compositions and 1 ml/l aliquots.
- Keep trace, selenite-tungstate, and vitamin stock internals out of the parent final-medium `ingredients`.
- Model DSMZ's 20 ml ethanol aliquot using an appropriate volume unit, or convert it to a mass concentration through a documented density transform.
- Re-ground `NiCl2 x 6 H2O` to nickel chloride hexahydrate and replace the remaining legacy `mediaingredientmech_term` on `Ethanol absolute` if a CHEBI-keyed MediaIngredientMech link exists.
- Reconcile the TOGO `M2703` branch with this DSMZ/KOMODO branch once both import paths represent stock solutions consistently.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the parent ingredient list contains only the DSMZ base ingredients and stock aliquots, not one-liter stock internals.
- Confirm Seven vitamins, Selenite-tungstate, and SL-10 internals are retained in stock solution compositions.
- Confirm ethanol is no longer represented as an unsupported 20 g/l interpretation of a 20 ml source row.
- Confirm the corrected TOGO `M2703` and direct MediaDive/KOMODO branches merge or have a documented reason to remain separate.

## Additional Notes

Empty optional fields are not defects. The record is structurally close to the DSMZ source in pH and preparation text; the main blocker is the same stock-solution boundary loss seen in other clostridial DSMZ imports.
