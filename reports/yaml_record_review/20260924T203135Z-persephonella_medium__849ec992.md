# YAML Record Review: persephonella_medium__849ec992

- Repository: CultureMech
- Record: data/merge_yaml/merged/persephonella_medium__849ec992.yaml
- Started UTC: 2026-09-24T20:31:35Z
- Finished UTC: 2026-09-24T20:31:35Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:008870`, `persephonella_medium`, from the maintained TOGO owner `data/normalized_yaml/bacterial/TOGO_M2284_Persephonella_Medium.yaml`.

The record represents TOGO M2284, Persephonella Medium, sourced from DSMZ medium 996. It currently contains the DSMZ final-medium salts, 990 g/L water, several variable gas or acid rows, flattened trace-element stock components, and an empty `Trace element solution (see below)` solution stub.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/persephonella_medium__849ec992.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The TOGO source identity is clear: TOGO M2284 points directly to the DSMZ medium 996 PDF for PERSEPHONELLA MEDIUM.

An exact ignored-inclusive search also found `data/normalized_yaml/bacterial/persephonella_medium.yaml`, the direct MediaDive/DSMZ 996 owner that generates `data/merge_yaml/merged/persephonella_medium__fd71a565.yaml`. That sibling uses the same DSMZ medium 996 source and should be reconciled with this TOGO owner; it has pH 6.0 and defined-medium metadata but still flattens the trace-element stock recipe into final ingredients.

## Evidence

The TOGO M2284 API and the DSMZ medium 996 PDF both list a final medium made from 29 g NaCl, 2 g NaOH, 0.5 g KCl, 1.36 g MgCl2 x 6 H2O, 7 g MgSO4 x 7 H2O, 2 g Na2S2O3 x 5 H2O, 0.4 g CaCl2 x 2 H2O, 0.2 g NH4Cl, 0.3 g K2HPO4 x 3 H2O, 10 ml Trace element stock solution, and 990 ml distilled water.

Both sources also list a separate 1 L Trace element solution whose components are milligram-scale salts, plus instructions to adjust that stock to pH 3. The final medium is adjusted to pH 6 with H2SO4, dispensed under CO2, given O2 in sealed tubes, and pressurized with H2 after inoculation.

MediaDive medium 996 agrees with the DSMZ structure: the 10 ml trace solution is a solution addition in the final recipe, and the trace-element rows belong to a separate `Trace element solution` recipe with their own 1000 ml water row.

## Completeness

The record preserves the source link and most source rows, but not their scope. It misses `ph_value: 6.0`, marks a defined inorganic recipe as `COMPLEX` / `UNDEFINED`, encodes source volume rows as `G_PER_L`, and flattens the stock solution into the final medium.

The record also loses the DSMZ preparation and gas-handling text as structured preparation steps; instead, it promotes H2SO4, CO2, O2, and H2 from instructions/comments to variable-concentration ingredients.

## Findings

1. Needs curation: `Distilled water` is encoded as `990 G_PER_L`, and the `Trace element solution (see below)` solution stub is encoded as `10 G_PER_L`; DSMZ 996 and TOGO M2284 specify 990 ml water plus 10 ml trace-element stock in the final medium.
2. Needs curation: the trace-element stock composition is flattened into top-level ingredients and the generated `solutions` entry is empty. The Na2MoO4, H3BO3, FeSO4, MnCl2, CoCl2, ZnCl2, Na2O4W, NiSO4, AlCl3, H2SeO3, CuCl, and Na-EDTA rows belong to a separate 1 L stock solution.
3. Needs curation: the trace-element stock milligram quantities are represented as grams per liter in the TOGO owner. For example, 100 mg FeSO4 x 7 H2O in the stock is encoded as `100 G_PER_L`, and 500 mg Na-EDTA x 2 H2O is encoded as `500 G_PER_L`.
4. Needs curation: `ph_value: 6.0` is missing, and the owner is classified as `COMPLEX` / `UNDEFINED` even though DSMZ and MediaDive treat the medium as defined.
5. Needs curation: H2SO4, CO2, O2, and H2 are source preparation/gas instructions, not variable-concentration final-medium ingredient rows.
6. Needs curation: this TOGO generated record is split from the direct MediaDive/DSMZ 996 generated sibling; both need stock-solution scoping repairs before they can be reconciled.
7. Needs curation: several trace-element formulas or groundings need review while the stock is repaired, including `Ni2SO4x 6 H2O`, ungrounded `Na2O4W x 2 H2O`, ungrounded `H2SeO3(selenous acid)`, and the stale generic `mediaingredientmech_chebi_term` on MgSO4 x 7 H2O.

## Recommended Edits

1. Keep final-medium rows to the DSMZ main solution and encode `Distilled water` and `Trace element solution` as 990 ml and 10 ml volume additions.
2. Move all trace-element stock components into a populated `Trace element solution` with its own 1000 ml distilled water row and milligram-derived concentrations.
3. Restore `ph_value: 6.0`, `medium_type: DEFINED`, and `composition_type: DEFINED`.
4. Move the H2SO4, CO2, O2, and H2 details into preparation or gas-handling instructions rather than variable ingredient rows.
5. Repair the trace-element formula and grounding issues while preserving source labels where needed.
6. Reconcile and regenerate the TOGO M2284 and direct DSMZ 996 owners so the same DSMZ medium is no longer split into two generated records.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `TOGO:M2284`, `DSMZ_Medium996`, `mediadive.medium:996`, and both Persephonella owners after regeneration to confirm DSMZ medium 996 has the intended representation.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `TOGO:M2284`, `M2284`, `DSMZ_Medium996`, `CultureMech:008870`, and `Persephonella_Medium`.
