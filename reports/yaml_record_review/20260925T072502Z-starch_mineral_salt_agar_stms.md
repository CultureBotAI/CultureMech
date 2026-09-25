# YAML Record Review: starch_mineral_salt_agar_stms
- Repository: CultureMech
- Record: data/merge_yaml/merged/starch_mineral_salt_agar_stms.yaml
- Started UTC: 2026-09-25T07:23:00Z
- Finished UTC: 2026-09-25T07:25:02Z
- Verdict: needs curation

## Target
Reviewed the generated merged record `data/merge_yaml/merged/starch_mineral_salt_agar_stms.yaml`, a 41-source generated merge centered on DSMZ Medium 252 / KOMODO Medium 252.

The generated record uses KOMODO Medium 252, `CultureMech:004654`, as the canonical identity and points back to the DSMZ Medium 252 parent `CultureMech:001351`.

## Validation
- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; scanned 1 file and reported 0 `ERROR` rows. The strict TSV contained the header only.
- Reference validation: Passed; 1 file was validated and 0 reference checks were available.
- Term validation: Passed after the known `eutils` `pkg_resources` deprecation warning.
- Embedded `curation_history`: Not checked. The available `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding
The DSMZ 252 / KOMODO 252 source-duplicate identity is correct. DSMZ Medium 252 is `STARCH - MINERAL SALT - AGAR (STMS)`, pH 7.2, with 1 g/L NaCl and 1 ml/L trace element solution.

An exact source/id search for the DSMZ 252, DSMZ 1240, DSMZ 1241, DSMZ/JCM 547/J58, KOMODO 252, KOMODO 1240, KOMODO 547, and selected `CultureMech` ids included ignored files and found the expected normalized records, this generated merge, and source-index references under `data/normalized_yaml` and `data/merge_yaml/merged`. Those matches are not all source duplicates of DSMZ 252; several are explicit salinity or ISP Medium 4 variants.

## Evidence
DSMZ Medium 252 lists Starch 10.0 g, `(NH4)2SO4` 2.0 g, K2HPO4 1.0 g, MgSO4 x 7 H2O 1.0 g, NaCl 1.0 g, CaCO3 2.0 g, Trace element solution 1.0 ml, Agar 15.0 g, Distilled water 1000.0 ml, and pH 7.2.

MediaDive Medium 1240 is a related `STARCH-MINERAL SALT-AGAR + 10% NACL` recipe that keeps the 1 g/L NaCl row and adds a second 100 g/L NaCl row. MediaDive Medium 1241 is a 15% NaCl variant with a second 150 g/L NaCl row.

MediaDive DSMZ 547 and JCM J58 describe ISP Medium 4 / Inorganic salts-starch agar recipes with a 1 ml/L trace-salt solution and pH handling that differs from DSMZ 252.

## Completeness
No target organisms are present in the generated record; no source evidence in the reviewed DSMZ/MediaDive material names organism growth for this recipe, so that is not a defect.

The generated merge predates the August 7 `apply_cocktail_nesting.py` repair visible in the current normalized DSMZ 252 and KOMODO 252 sources; those normalized files now move FeSO4 x 7 H2O, MnCl2 x 4 H2O, and ZnSO4 x 7 H2O into a nested `Trace element solution` added at 1 ml/L.

## Findings
- High: The generated record presents DSMZ 252 / KOMODO 252 as the canonical identity but contains `NaCl: 101 G_PER_L`, the 10% NaCl variant concentration from DSMZ 1240, rather than base DSMZ 252's 1 g/L NaCl.
- High: The merge collapsed DSMZ 1240 and DSMZ 1241 salinity variants into the same source-duplicate record as base DSMZ 252. DSMZ 1241's 15% NaCl formulation is not represented as its own formula or variant; it survives only as a synonym/source id.
- High: The generated record still flattens the 1 ml/L trace-element stock as 1 g/L FeSO4 x 7 H2O, 1 g/L MnCl2 x 4 H2O, and 1 g/L ZnSO4 x 7 H2O final-medium ingredients. Current normalized sources have already nested those three stock-strength rows, but the generated merged YAML has not been regenerated from them.
- Medium: ISP Medium 4 / Inorganic salts-starch agar sources were also treated as exact duplicates even though DSMZ 547 and JCM J58 have different preparation topology and pH semantics from DSMZ 252.
- Medium: The generated KOMODO-canonical output drops the DSMZ parent's explicit `Adjust pH to 7.2.` preparation step.

## Recommended Edits
- Split the 10% and 15% NaCl records out of the exact duplicate merge and model them as salinity variants of base STMS.
- Re-evaluate the ISP Medium 4 records; preserve them as a distinct parent or as explicit variants rather than exact source duplicates if their preparation/pH semantics need to remain visible.
- Regenerate merged YAML from the current normalized DSMZ 252 and KOMODO 252 records so the trace-element solution stays nested instead of becoming final 1 g/L Fe/Mn/Zn rows.
- Preserve the DSMZ `Adjust pH to 7.2.` step when the KOMODO child is selected as canonical in a duplicate merge.
- Do not patch `data/merge_yaml/merged/starch_mineral_salt_agar_stms.yaml` by hand.

## Follow-up Checks
- After regeneration, verify that base `starch_mineral_salt_agar_stms` has 1 g/L NaCl and no final-medium FeSO4/MnCl2/ZnSO4 rows.
- Verify that DSMZ 1240 and DSMZ 1241 remain discoverable as 10% and 15% NaCl variants.
- Re-run schema, strict, reference, and term validators on the regenerated merged records.

## Additional Notes
MediaDive REST reports 20 g agar for DSMZ 252 while the DSMZ Medium 252 PDF lists 15.0 g and the generated YAML uses 15 g/L. The generated agar value therefore matches the reviewed DSMZ PDF.
