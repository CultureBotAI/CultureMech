# YAML Record Review: minimal_mineral_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/minimal_mineral_medium.yaml
- Started UTC: 2026-09-24T07:25:15Z
- Finished UTC: 2026-09-24T07:26:09Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009388`
- Generated name: `minimal_mineral_medium`
- Generated source file: `data/merge_yaml/merged/minimal_mineral_medium.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/minimal_mineral_medium.yaml`
- Upstream source: TOGO Medium `M2846`, `minimal mineral medium`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/minimal_mineral_medium.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with TOGO `M2846`.
- The `media_term` points to `TOGO:M2846` with label `minimal mineral medium`.
- The imported ammonium metavanadate row is ungrounded.
- Several hydrated trace salts have overbroad or incorrect CHEBI grounding after flattening:
  - `Na2MoO4 x H2O` is grounded to anhydrous sodium molybdate.
  - `CuCl2 x H2O` is grounded to generic copper(II) chloride.
  - `NiSO4 x 6H2O` is grounded to generic nickel sulfate.
- The generated trace solution link points to `mediadive.solution:6187`, which is a different MediaDive trace-element solution rather than the trace stock defined by TOGO `M2846`.

## Evidence

- TOGO `M2846` defines a basal formula per liter with distilled water, `KH2PO4` at 1.9 g, `Na2HPO4` at 5.1 g, `(NH4)2SO4` at 2.0 g, and `MgSO4 x 7H2O` at 0.1 g, adjusted to pH 7.2.
- TOGO `M2846` then adds two stocks after sterilization: 1 ml of a trace element solution and 1 ml of a 25 g/liter `Ca(NO3)2` solution to 1 liter of medium.
- The TOGO trace solution is in the same `M2846` payload and contains, per liter of stock, `FeSO4 x 7H2O` 1.0 g, `MnSO4 x H2O` 1.0 g, `Na2MoO4 x H2O` 0.25 g, `H3BO3` 0.10 g, `CuCl2 x H2O` 0.25 g, `ZnCl` 0.25 g, `NH4VO3` 0.10 g, `Co(NO3)2 x 6H2O` 0.25 g, `NiSO4 x 6H2O` 0.10 g, and `H2SO4` 9.2 g.
- The generated top-level ingredient list matches the basal salts and the raw stock component concentrations, but that is not the same final-medium recipe: the trace-solution salts and calcium nitrate stock are late additions at 1 ml/L.
- `data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml` and the MediaDive REST response for solution 6187 contain an EDTA/chloride/molybdate trace solution with `Na2-EDTA`, `FeCl3 x 6 H2O`, `MnCl2 x 4 H2O`, `ZnCl2 x 6 H2O`, `CoCl2 x 6 H2O`, and `Na2MoO4 x 2 H2O`; that is not the TOGO `M2846` trace-solution composition.

## Completeness

- The normalized owner has only 1.0 for the water row, while this generated file still has 3.0 and `Merged 3 duplicates`, so `data/merge_yaml/merged/minimal_mineral_medium.yaml` is stale relative to the repaired normalized record.
- The generated `solutions` array preserves a trace-solution placeholder and a `solution of Ca(NO3)2` placeholder, but the trace-solution placeholder points at the wrong standalone solution and the calcium nitrate solution has an empty `composition`.
- The generated record does not preserve pH 7.2.
- The generated record does not preserve the source preparation statement that the two 1 ml stocks are added after sterilization.
- The generated record does not preserve the source growth context of 30 C, 180 rpm, and sealed 5-liter Erlenmeyer flasks.

## Findings

- High: TOGO `M2846` subrecipes were flattened into the main ingredient list at stock concentrations. The generated final medium reports 0.25 g/L `Na2MoO4 x H2O`, 9.2 g/L `H2SO4`, and 25 g/L `Ca(NO3)2` as if they were direct final-medium concentrations even though the source adds only 1 ml of each stock per liter of basal medium.
- High: The generated trace solution links to `mediadive.solution:6187`, an unrelated trace-element stock, and therefore loses the actual TOGO-defined `M2846` trace recipe.
- High: `solution of Ca(NO3)2` has no composition even though the source explicitly defines the stock as 25 g/liter.
- Medium: The generated merged file is stale relative to `data/normalized_yaml/bacterial/minimal_mineral_medium.yaml`; the owner has the repaired 1.0 water row but this generated file still has a summed 3.0 value from the main water and both subrecipe waters.
- Medium: pH, sterilization timing, and growth context are not represented.
- Medium: Several trace-salt ontology links are missing, overbroad, or inconsistent with the hydrated source strings.

## Recommended Edits

- In `data/normalized_yaml/bacterial/minimal_mineral_medium.yaml`, keep only the basal salts as direct final-medium ingredients and represent the two 1 ml/L late additions as solution additions rather than flattening raw stock components into the final medium.
- Replace the `mediadive.solution:6187` link with an inline or local solution that contains the TOGO `M2846` trace element solution.
- Populate `solution of Ca(NO3)2` with 25 g/L `Ca(NO3)2` and its 1 liter water basis, or otherwise preserve the source stock recipe without flattening its calcium nitrate into the top level.
- Add pH 7.2 and the post-sterilization addition instruction to `preparation_notes`.
- Add the 30 C, 180 rpm, and sealed 5-liter Erlenmeyer-flask growth context if the model has a suitable location for organism-agnostic source context.
- Re-run the merge so `data/merge_yaml/merged/minimal_mineral_medium.yaml` reflects the September 2026 normalized water repair.

## Follow-up Checks

- Re-fetch TOGO `M2846` and confirm the basal formula, trace solution, calcium nitrate stock, pH, and late-addition instruction are all preserved after curation.
- Confirm no trace-stock component appears as a direct top-level final-medium ingredient unless it has been converted through the 1 ml/L stock dilution.
- Confirm the final generated water row no longer sums main-medium and stock-solution waters.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.
- The normalized-owner lookup used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.
