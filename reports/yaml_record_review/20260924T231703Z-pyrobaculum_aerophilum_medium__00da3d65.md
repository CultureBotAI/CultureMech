# YAML Record Review: Pyrobaculum Aerophilum Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/pyrobaculum_aerophilum_medium__00da3d65.yaml`
- Started UTC: 2026-09-24T23:17:03Z
- Finished UTC: 2026-09-24T23:18:43Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated file | `data/merge_yaml/merged/pyrobaculum_aerophilum_medium__00da3d65.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M208_Pyrobaculum_Aerophilum_Medium.yaml` |
| Source identity | `TOGO:M208`, original source `JCM_M215` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=215` |
| Merge fingerprint | `00da3d651c6f6ef0e714160efb4c84cbe023802f2abcf66e04c04ac323872ffd` |

The reviewed file is a generated merge from a single TOGO wrapper. Future data edits belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream artifacts.

## Validation

| Validator | Result |
| --- | --- |
| Open LinkML schema | Passed; exited 0 with no diagnostics. |
| Strict validator | Passed with 0 ERROR rows; TSV had the header only. |
| Reference validator | Passed; 1 file, 0 checks. |
| Term validator | Passed; emitted only the expected `eutils` `pkg_resources` warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is a TOGO M208 import for JCM medium 215. The live TOGO M208 API identifies `Pyrobaculum Aerophilum Medium`, `JCM_M215`, the JCM `GRMD=215` URL, and pH 7.0; the live JCM 215 page identifies the same `PYROBACULUM AEROPHILUM MEDIUM`.

An ignored-file-inclusive owner search across `data/normalized_yaml` and `data/merge_yaml/merged` for `TOGO:M208$`, `togomedium.org/medium/M208$`, `JCM_M215`, `GRMD=215`, `CultureMech:008680`, the full merge fingerprint, and `TOGO_M208_Pyrobaculum_Aerophilum_Medium` found this TOGO owner plus a separate direct JCM owner, `data/normalized_yaml/archaea/pyrobaculum_aerophilum_medium.yaml`, that points at the same `GRMD=215` source. That direct owner generates `data/merge_yaml/merged/pyrobaculum_aerophilum_medium__bc93f572.yaml`, so the same JCM recipe is stranded in two generated records.

## Evidence

TOGO M208 and JCM 215 agree on the final recipe: 125 ml Marine medium/Synthetic seawater mix solution, 10 ml Trace minerals, Fe(NH4)2(SO4)2 x 6 H2O at 2 mg, NH4Cl at 0.25 g, (NH4)2Ni(SO4)2 x 6 H2O at 2 mg, Na2SeO4 at 0.1 mg, NaWO4 x 2 H2O at 0.1 mg, NaHCO3 at 2.2 g, KH2PO4 at 0.07 g, yeast extract at 0.5 g, Na2S2O3 x 5 H2O at 1 g, and 865 ml distilled water. The YAML stores the final-medium Fe, Ni, Se, and W milligram rows as `2`, `2`, `0.1`, and `0.1` `G_PER_L`.

JCM 215 defines the Marine medium/Synthetic seawater mix solution separately per liter. The generated YAML leaves that solution with `composition: []` while promoting every stock ingredient to a top-level final-medium ingredient. In that promotion, several source milligram rows were interpreted as grams: KBr is `80` `G_PER_L`, SrCl2 x 6 H2O is `72` `G_PER_L`, H3BO3 is `52` `G_PER_L`, Na2HPO4 is `8.1` `G_PER_L`, NaF is `2.4` `G_PER_L`, KI is `0.05` `G_PER_L`, and sodium silicate is `0.4` `G_PER_L`.

The source final recipe adds 10 ml Trace minerals by reference to JCM medium 151, which TOGO represents as M142. JCM 151 and TOGO M142 include a Trace minerals stock with nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, Na2MoO4 x 2 H2O, and water. The reviewed TOGO M208 record keeps only an empty `Trace minerals (see Medium [M142])` solution shell.

JCM 215 instructs curators to adjust the medium to pH 7.0 with 1 N H2SO4, sterilize by filtration, dispense under a N2-CO2-O2 atmosphere, and pressurize inoculated bottles to 200 kPa with the same gas mix. The generated record has no `ph_value` and no preparation steps.

## Completeness

The record is incomplete for a runnable recipe. It needs the pH and preparation instructions from JCM 215, a populated nested seawater stock, a populated nested trace-minerals stock resolved through JCM 151 or TOGO M142, and exact handling for milligram rows before its concentrations are usable.

The duplicate direct JCM owner appears to preserve more of the referenced trace-minerals content than the TOGO M208 owner, but that copy also flattens stock components and sums unrelated stock-local solutes into top-level ingredient totals. It should be reconciled during source repair, not blindly preferred.

## Findings

| Severity | Finding | Evidence | Recommended owner |
| --- | --- | --- | --- |
| Blocker | Four final-medium source milligram quantities are 1000-fold too high. | TOGO M208 and JCM 215 list Fe(NH4)2(SO4)2 x 6 H2O at 2 mg, (NH4)2Ni(SO4)2 x 6 H2O at 2 mg, Na2SeO4 at 0.1 mg, and NaWO4 x 2 H2O at 0.1 mg; the YAML stores them as `2`, `2`, `0.1`, and `0.1` `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M208_Pyrobaculum_Aerophilum_Medium.yaml` |
| Blocker | The seawater stock is flattened into final ingredients and its source milligram rows are recorded as grams. | JCM 215 defines the Marine medium/Synthetic seawater mix solution separately; the YAML has an empty solution plus promoted top-level rows including KBr `80` `G_PER_L`, SrCl2 x 6 H2O `72` `G_PER_L`, and H3BO3 `52` `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M208_Pyrobaculum_Aerophilum_Medium.yaml` |
| Major | The required trace-minerals stock is missing. | The final recipe adds 10 ml Trace minerals; JCM 151/TOGO M142 define that stock, but the generated YAML keeps only `Trace minerals (see Medium [M142])` with `composition: []`. | `data/normalized_yaml/archaea/TOGO_M208_Pyrobaculum_Aerophilum_Medium.yaml` |
| Major | Source pH and preparation are absent. | TOGO M208 carries pH 7.0, and JCM 215 gives filtration, N2-CO2-O2 dispensing, and bottle-pressurization instructions; the YAML has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M208_Pyrobaculum_Aerophilum_Medium.yaml` |
| Major | The same JCM 215 source is split across two generated records. | Ignored-file-inclusive search found `data/normalized_yaml/archaea/pyrobaculum_aerophilum_medium.yaml` and generated `pyrobaculum_aerophilum_medium__bc93f572.yaml`, both pointing to `GRMD=215`. | Merge identity/fingerprint logic plus both normalized owners |

## Recommended Edits

1. Repair the TOGO M208 owner by converting all source `mg` quantities to g/L where they remain final-medium ingredients.
2. Rebuild `Marine medium/Synthetic seawater mix solution` as a populated nested solution, leaving only the 125 ml/L stock addition in the top-level ingredient or solution addition.
3. Resolve `Trace minerals` through TOGO M142 or JCM 151 and add its stock composition under the 10 ml/L stock addition.
4. Restore `ph_value: 7.0` and the JCM 215 filtration and N2-CO2-O2 pressurization instructions.
5. Reconcile the direct JCM owner with this TOGO owner so exact `GRMD=215` duplicates merge or one wrapper is intentionally suppressed.
6. Regenerate `data/merge_yaml/merged/` after the maintained YAML and merge identity are repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated record.
- Re-open TOGO M208, JCM 215, TOGO M142, and JCM 151 to confirm the seawater and trace-minerals stocks are nested and that milligram rows are converted correctly.
- Re-run an ignored-file-inclusive search for `JCM_M215`, `GRMD=215`, and `TOGO:M208$` to confirm the same-source duplicate is no longer stranded.
- Confirm no generated top-level ingredient is the unscaled member of a stock solution.

## Additional Notes

The generated `pyrobaculum_aerophilum_medium__bc93f572` direct JCM record will need its own review; this report used it only to establish the same-source duplication and to identify that the TOGO and direct importers failed differently on the same nested JCM recipe.
