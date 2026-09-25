# YAML Record Review: thermoflexus_hungenholtzii_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoflexus_hungenholtzii_medium__598b509d.yaml
- Started UTC: 2026-09-25T10:20:00Z
- Finished UTC: 2026-09-25T10:23:57Z
- Verdict: needs curation

## Target

Reviewed the generated merged record for `thermoflexus_hungenholtzii_medium__598b509d`, which represents direct MediaDive/JCM medium `J976` as `CultureMech:003325`.

## Validation

- Schema: Passed with `No issues found`.
- Strict validation: Passed; the strict TSV had only its header row and no error rows.
- Reference validation: Passed; exited 0 after printing only the cache banner.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

The target has the expected MediaDive term `mediadive.medium:J976`, JCM 976 link, and pH 6.0. An exact ignored-inclusive search for `mediadive.medium:J976`, `GRMD=976`, and `TOGO_M1029` found a separate `TOGO_M1029_Thermoflexus_Hungenholtzii_Medium` branch that still generates `THERMOFLEXUS_HUNGENHOLTZII_MEDIUM.yaml`.

## Evidence

MediaDive J976 and the live JCM 976 page list a 1025 ml main solution with basal salts, 5 ml Mineral solution, 1000 ml water, 10 ml Trace vitamins from JCM Medium 197, and 10 ml of 10% peptone. The Mineral solution is a 1000 ml stock with 3.7 g EDTA, 1.1 g `FeSO4 x 7 H2O`, and mg-scale manganese, zinc, cobalt, copper, molybdate, and borate salts.

## Completeness

The generated target preserves the JCM identity, pH, basal salts, and preparation text. It does not preserve the Mineral solution, Trace vitamins, or 10% peptone additions as stock additions.

## Findings

- High: the 5 ml Mineral solution stock was flattened into direct final-medium ingredients at stock concentration. The target carries 3.7 g/L EDTA, 1.1 g/L `FeSO4 x 7 H2O`, and undiluted trace salts as top-level rows.
- High: the 10 ml Trace vitamins stock from JCM 197 was flattened into top-level vitamin rows at 1 L stock concentrations.
- High: 10 ml of 10% peptone was converted to `Peptone` at `10 G_PER_L`; the source quantity is a milliliter addition of a 10% stock.
- Medium: the TOGO M1029 import of the same JCM 976 recipe is unmerged with the direct MediaDive/JCM branch.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/thermoflexus_hungenholtzii_medium.yaml` so Mineral solution, JCM 197 Trace vitamins, and 10% peptone remain 5 ml, 10 ml, and 10 ml stock additions.
- Preserve the stock compositions under nested or linked solution records rather than promoting stock rows to final-medium ingredient rows.
- Canonicalize TOGO M1029 and direct MediaDive/JCM J976 before generating merged YAML.

## Follow-up Checks

- Regenerate merged YAML and verify J976 no longer contains 3.7 g/L EDTA, undiluted vitamin rows, or 10 g/L peptone as direct final-medium ingredients.
- Confirm the corrected J976 record still validates by schema, strict, reference, and term validators.
- Search with ignored files included for `mediadive.medium:J976`, `GRMD=976`, and `TOGO_M1029` to ensure JCM 976 has one generated target.

## Additional Notes

None found.
