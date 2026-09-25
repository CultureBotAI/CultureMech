# YAML Record Review: st21_agar_for_cellulose_degraders__23024327
- Repository: CultureMech
- Record: data/merge_yaml/merged/st21_agar_for_cellulose_degraders__23024327.yaml
- Started UTC: 2026-09-25T07:12:30Z
- Finished UTC: 2026-09-25T07:13:44Z
- Verdict: needs curation

## Target
Reviewed the generated merged record `data/merge_yaml/merged/st21_agar_for_cellulose_degraders__23024327.yaml`, a single-source DSMZ/MediaDive import from `data/normalized_yaml/bacterial/st21_agar_for_cellulose_degraders.yaml`.

The record is identified as DSMZ Medium 938, `ST21 AGAR FOR CELLULOSE DEGRADERS`, with MediaDive source id `mediadive.medium:938`.

## Validation
- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; scanned 1 file and reported 0 `ERROR` rows. The strict TSV contained the header only.
- Reference validation: Passed; 1 file was validated and 0 reference checks were available.
- Term validation: Passed after the known `eutils` `pkg_resources` deprecation warning.
- Embedded `curation_history`: Not checked. The available `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding
The media identity is correct. MediaDive `/rest/medium/938` returned one DSMZ record named `ST21 AGAR FOR CELLULOSE DEGRADERS`, pH 7.2, with source `DSMZ` and a DSMZ Medium 938 PDF link. The generated YAML carries the matching `mediadive.medium:938` term and DSMZ PDF URL.

An exact source/id search for `mediadive.medium:938`, `CultureMech:002113`, and `ST21 AGAR FOR CELLULOSE DEGRADERS` included ignored files and found the expected normalized DSMZ file, this generated merged file, and index references. It also found `data/normalized_yaml/bacterial/KOMODO_938_ST21_AGAR_FOR_CELLULOSE_DEGRADERS.yaml` and `data/merge_yaml/merged/ST21_AGAR_FOR_CELLULOSE_DEGRADERS.yaml`, a second local record for the same upstream DSMZ recipe.

## Evidence
DSMZ Medium 938 makes the final liter by combining Solution A, Solution B, and Solution C after separate autoclaving:

- Solution A: K2HPO4 1.0 g, Yeast extract 20.0 mg, Agar 14.0 g, Tap water 600.0 ml.
- Solution B: KNO3 1.0 g, MgSO4 x 7 H2O 1.0 g, CaCl2 x 2 H2O 1.0 g, MnSO4 x 7 H2O 0.1 g, Tap water 300.0 ml.
- Solution C: FeCl3 0.2 g, Tap or distilled water 100.0 ml.

The source then autoclaves the three solutions separately, combines them after cooling to 50 C, adjusts pH to 7.2 with KOH before pouring plates, and adds filter-paper strips on the gelated plates.

## Completeness
No target organisms are present in the generated record; no source evidence in the reviewed DSMZ/MediaDive material names organism growth for this recipe, so that is not a defect.

The generated record keeps the combined 1000 ml water total and the main preparation instruction, but it loses the A/B/C solution structure and treats all 1000 ml as `Tap water` even though Solution C allows tap or distilled water.

## Findings
- High: The generated record stores MediaDive's within-subsolution `g_l` values as final-medium concentrations. The correct final values are K2HPO4 1 g/L, Yeast extract 0.02 g/L, Agar 14 g/L, KNO3 1 g/L, MgSO4 x 7 H2O 1 g/L, CaCl2 x 2 H2O 1 g/L, MnSO4 x 7 H2O 0.1 g/L, and FeCl3 0.2 g/L.
- Medium: The A/B/C solution topology is collapsed into one `Tap water` row, obscuring the source instruction to autoclave the solutions separately before combining them after cooling to 50 C.
- Low: The KNO3 row still has a legacy `mediaingredientmech_term` instead of a CHEBI-keyed `mediaingredientmech_chebi_term`, despite having a valid CHEBI primary term.
- Low: The same upstream DSMZ 938 recipe also exists as a separate KOMODO-derived generated record because that derivative has an extra variable KOH pH-adjustment row and did not merge with the DSMZ record.

## Recommended Edits
- Fix MediaDive subsolution flattening for DSMZ 938 so the generated `G_PER_L` values reflect the total 1 L final medium rather than each subsolution's local volume.
- Preserve Solution A, B, and C preparation context where the schema allows, including the separately autoclaved solution semantics.
- Add or refresh the CHEBI-keyed MediaIngredientMech link for `KNO3`.
- Model the KOH pH adjustment consistently between the DSMZ and KOMODO 938 records so they can collapse as duplicates after the concentration fix.
- Regenerate merged YAML after editing the normalized source or import logic; do not patch `data/merge_yaml/merged/st21_agar_for_cellulose_degraders__23024327.yaml` by hand.

## Follow-up Checks
- After regeneration, verify that Agar is 14 g/L rather than 23.3333 g/L and FeCl3 is 0.2 g/L rather than 2 g/L in the generated DSMZ 938 formula.
- Re-run schema, strict, reference, and term validators on the regenerated merged record.
- Confirm whether `ST21_AGAR_FOR_CELLULOSE_DEGRADERS.yaml` still remains as a separate generated record for the same DSMZ recipe.

## Additional Notes
None found
