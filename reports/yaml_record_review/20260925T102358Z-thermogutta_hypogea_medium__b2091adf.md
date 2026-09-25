# YAML Record Review: thermogutta_hypogea_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermogutta_hypogea_medium__b2091adf.yaml
- Started UTC: 2026-09-25T10:20:00Z
- Finished UTC: 2026-09-25T10:23:58Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermogutta_hypogea_medium__b2091adf`, which represents direct MediaDive/JCM medium `J1031` as `CultureMech:002215`.

## Validation

- Schema: Passed with `No issues found`.
- Strict validation: Passed with 1 file, 0 error files, and 0 rows.
- Reference validation: Passed; exited 0 after printing only the cache banner.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The target has the expected MediaDive term `mediadive.medium:J1031` and JCM 1031 link. An exact ignored-inclusive search for `mediadive.medium:J1031`, `GRMD=1031`, and `TOGO_M1095` found a separate `TOGO_M1095_Thermogutta_Hypogea_Medium` branch that still generates `THERMOGUTTA_HYPOGEA_MEDIUM.yaml`.

## Evidence

MediaDive J1031 and the live JCM 1031 page list a 1060 ml main solution with basal salts, 10 ml Trace elements solution from JCM Medium 1030, 1000 ml water, 10 ml Trace vitamins from JCM Medium 197, 2 g bicarbonate, 20 ml of 10% glucose, 10 ml of 1% yeast extract, and 10 ml of 1 M `KNO3`. The Trace elements stock is a 1000 ml solution with mg-scale iron, cobalt, nickel, molybdate, tungstate, zinc, copper, selenate, borate, manganese, strontium, chromium, aluminium, barium, silicate, bromide, iodide, and sulfate salts.

## Completeness

The generated target retains the JCM identity and preparation text. It does not preserve Trace elements, Trace vitamins, glucose, yeast extract, or nitrate as stock additions with source concentrations.

## Findings

- High: the 10 ml Trace elements stock from JCM 1030 was flattened into final-medium ingredient rows at full stock concentration, including low-mass stock rows such as 0.0784 g/L `Fe(NH4)2(SO4)2 x 6 H2O`, 0.0005 g/L `CrK(SO4)2 x 12 H2O`, and 0.071 g/L `Na2SO4`.
- High: the 10 ml Trace vitamins stock from JCM 197 was flattened into top-level vitamin rows at 1 L stock concentrations.
- High: several milliliter stock additions were converted to bare gram-per-liter final-medium rows. The generated target lists 20 g/L Glucose from a 20 ml 10% stock, 10 g/L Yeast extract from a 10 ml 1% stock, and 10 g/L `KNO3` from a 10 ml 1 M stock.
- Medium: the TOGO M1095 import of the same JCM 1031 recipe is unmerged with the direct MediaDive/JCM branch.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/thermogutta_hypogea_medium.yaml` so JCM 1030 Trace elements, JCM 197 Trace vitamins, 10% glucose, 1% yeast extract, and 1 M nitrate remain scoped as stock additions with milliliter amounts.
- Do not convert stock-addition milliliter amounts directly to gram-per-liter rows without preserving the source stock concentration.
- Canonicalize TOGO M1095 and direct MediaDive/JCM J1031 before generating merged YAML.

## Follow-up Checks

- Regenerate merged YAML and verify J1031 no longer contains undiluted Trace elements, undiluted Trace vitamins, 20 g/L glucose, 10 g/L yeast extract, or 10 g/L nitrate as direct final-medium rows.
- Confirm the corrected J1031 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:J1031`, `GRMD=1031`, and `TOGO_M1095` to ensure JCM 1031 has one generated target.

## Additional Notes

The initial local source search included a bare `TOGO_M` pattern and swept through unrelated TOGO records; that result was discarded and rerun with exact JCM and TOGO identifiers.
