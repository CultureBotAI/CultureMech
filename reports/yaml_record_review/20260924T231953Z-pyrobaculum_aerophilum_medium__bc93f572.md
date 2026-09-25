# YAML Record Review: PYROBACULUM AEROPHILUM MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/pyrobaculum_aerophilum_medium__bc93f572.yaml`
- Started UTC: 2026-09-24T23:19:53Z
- Finished UTC: 2026-09-24T23:20:08Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated file | `data/merge_yaml/merged/pyrobaculum_aerophilum_medium__bc93f572.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/pyrobaculum_aerophilum_medium.yaml` |
| Source identity | JCM medium 215, imported as `mediadive.medium:J215` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=215` |
| Merge fingerprint | `bc93f572c0f4e93733b3ea65fe6cf45067eac9f86b7616cca60b27384a76926f` |

The reviewed file is a generated merge from a single direct JCM owner. Future data edits belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream artifacts.

## Validation

| Validator | Result |
| --- | --- |
| Open LinkML schema | Passed; no schema issues found. |
| Strict validator | Passed with 0 ERROR rows; TSV had the header only. |
| Reference validator | Passed; 1 file, 0 checks. |
| Term validator | Passed; emitted only the expected `eutils` `pkg_resources` warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is the direct JCM import for JCM medium 215, `PYROBACULUM AEROPHILUM MEDIUM`. The `GRMD=215` page confirms the title, pH 7.0 final recipe, and its references to Marine medium/Synthetic seawater mix solution and Trace minerals.

An ignored-file-inclusive owner search across `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:002577`, `mediadive.medium:J215`, `Source: JCM, ID: J215`, `GRMD=215`, the full merge fingerprint, and `pyrobaculum_aerophilum_medium.yaml` found this direct owner plus `data/normalized_yaml/archaea/TOGO_M208_Pyrobaculum_Aerophilum_Medium.yaml`, a TOGO M208 wrapper around the same JCM `GRMD=215` source. The exact same source is therefore split into two generated records.

## Evidence

JCM 215 defines a final recipe containing 125 ml Marine medium/Synthetic seawater mix solution, 10 ml Trace minerals, 865 ml distilled water, Fe(NH4)2(SO4)2 x 6 H2O at 2 mg, NH4Cl at 0.25 g, (NH4)2Ni(SO4)2 x 6 H2O at 2 mg, Na2SeO4 at 0.1 mg, NaWO4 x 2 H2O at 0.1 mg, NaHCO3 at 2.2 g, KH2PO4 at 0.07 g, yeast extract at 0.5 g, and Na2S2O3 x 5 H2O at 1 g. The generated YAML omits the 865 ml distilled water row and both 125 ml and 10 ml stock additions.

JCM 215 defines Marine medium/Synthetic seawater mix solution as a separate per-liter stock. The YAML promotes the stock-local rows into top-level final-medium ingredients with no `solutions` array and no record that those rows came from only 125 ml of stock per liter of final medium.

The Trace minerals stock referenced by JCM 215 is defined by JCM 151 and TOGO M142. The YAML also promotes those stock-local rows into top-level final-medium ingredients with no 10 ml/L stock addition. That flattening produced impossible source totals across unrelated stocks: NaCl is `48.15` `G_PER_L` from 47.15 g/L in seawater plus 1 g/L in trace minerals, MgSO4 x 7 H2O is `10.0` `G_PER_L` from 7 g/L plus 3 g/L, CaCl2 x 2 H2O is `3.23` `G_PER_L` from 3.13 g/L plus 0.1 g/L, and H3BO3 is `0.062` `G_PER_L` from 52 mg/L plus 0.01 g/L.

The first JCM 215 preparation instruction is represented: the record stores pH 7.0 and the final filtration, N2-CO2-O2 dispensing, and 200 kPa pressurization instruction. The second preparation step belongs to the referenced trace-minerals stock; it is present in the YAML as a top-level `ADJUST_PH` step because the stock itself is missing.

## Completeness

The record captures the JCM title, pH, and main gas-handling preparation, but it does not preserve the stock-addition graph that JCM 215 requires. Without explicit 125 ml/L seawater and 10 ml/L trace-minerals additions, the top-level ingredient list has stock concentrations rather than final-medium concentrations or nested stock compositions.

The sibling TOGO M208 owner is a duplicate wrapper for the same JCM recipe and should be reconciled at the same time as this direct owner. The TOGO copy preserves the stock-addition row labels but has empty solution compositions and inflated milligram rows; this direct copy preserves the trace-minerals internals but loses the source stock boundaries.

## Findings

| Severity | Finding | Evidence | Recommended owner |
| --- | --- | --- | --- |
| Blocker | The seawater and trace-minerals stocks are flattened into final-medium ingredients. | JCM 215 uses 125 ml Marine medium/Synthetic seawater mix solution and 10 ml Trace minerals; the YAML has no `solutions` and no top-level stock-addition rows. | `data/normalized_yaml/archaea/pyrobaculum_aerophilum_medium.yaml` |
| Blocker | Stock-local gram concentrations were summed across unrelated stocks. | NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and H3BO3 are stored as arithmetic sums of seawater and trace-minerals stock rows despite different stock volumes. | `data/normalized_yaml/archaea/pyrobaculum_aerophilum_medium.yaml` |
| Major | The source 865 ml distilled water final row is omitted. | JCM 215 lists 865 ml distilled water in the final recipe; the YAML has no final water ingredient. | `data/normalized_yaml/archaea/pyrobaculum_aerophilum_medium.yaml` |
| Major | The trace-minerals stock preparation step is scoped to the final recipe. | The nitrilotriacetic acid/KOH pH 6.5 instruction belongs to the JCM 151 trace-minerals stock, but the missing stock boundary leaves it as a top-level `ADJUST_PH` step after the JCM 215 final-medium pressurization step. | `data/normalized_yaml/archaea/pyrobaculum_aerophilum_medium.yaml` |
| Major | The same JCM 215 source is split across two generated records. | Ignored-file-inclusive search found `data/normalized_yaml/archaea/TOGO_M208_Pyrobaculum_Aerophilum_Medium.yaml` and generated `pyrobaculum_aerophilum_medium__00da3d65.yaml`, both pointing to `GRMD=215`. | Merge identity/fingerprint logic plus both normalized owners |

## Recommended Edits

1. Rebuild Marine medium/Synthetic seawater mix solution as a populated solution used at 125 ml/L by the final recipe.
2. Rebuild Trace minerals as a populated solution from JCM 151 or TOGO M142 used at 10 ml/L by the final recipe.
3. Stop summing same-named stock-local salts across seawater and trace-minerals stocks.
4. Restore the final 865 ml distilled water row.
5. Keep JCM 215 final-medium preparation separate from trace-minerals stock preparation.
6. Reconcile the direct JCM owner with the TOGO M208 wrapper so exact `GRMD=215` duplicates merge or one wrapper is intentionally suppressed.
7. Regenerate `data/merge_yaml/merged/` after the maintained YAML and merge identity are repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated record.
- Re-open JCM 215, JCM 151, TOGO M208, and TOGO M142 to confirm final-medium rows and stock-local rows are no longer conflated.
- Re-run an ignored-file-inclusive search for `GRMD=215`, `Source: JCM, ID: J215`, and `JCM_M215` to confirm the same-source duplicate is resolved.
- Confirm top-level NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and H3BO3 are not sums of separate stock formulas.

## Additional Notes

None found.
