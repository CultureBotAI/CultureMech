# YAML Record Review: freshwater_medium_for_soil_aoa

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_medium_for_soil_aoa__83395c34.yaml
- Started UTC: 2026-09-23T04:37:25Z
- Finished UTC: 2026-09-23T04:38:20Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:002190` / `freshwater_medium_for_soil_aoa`, the direct MediaDive/JCM Medium J1004 import.
- Compared it with maintained source `data/normalized_yaml/bacterial/freshwater_medium_for_soil_aoa.yaml`.
- Cross-checked the MediaDive REST payload for J1004 and the live JCM GRMD=1004 page.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:J1004` correctly identifies JCM Medium 1004, FRESHWATER MEDIUM FOR SOIL AOA.
- Exact ignored-inclusive lookup for `mediadive.medium:J1004`, `CultureMech:002190`, and `freshwater_medium_for_soil_aoa__83395c34` covered normalized and generated bacterial YAML; it found this single maintained JCM J1004 owner and the suffixed generated file.
- The generated record's base medium identity is correct, but its ingredients do not preserve Basic FWM solution, Modified trace element mixture, Vitamin solution, HEPES solution, or sterile addition boundaries.
- NiCl2 x 6 H2O is grounded only to nickel dichloride, losing the source hexahydrate form.

## Evidence

- JCM 1004 defines a 1 L Basic FWM solution with 1 g NaCl, 0.5 g KCl, 0.4 g MgCl2 x 6 H2O, 0.2 g KH2PO4, and 0.1 g CaCl2 x 2 H2O before post-autoclave stock additions.
- MediaDive represents that base as 1017 ml after adding 1 ml modified trace elements, 1 ml vitamins, 1 ml 7.5 mM FeNa-EDTA, 2 ml 1 M NaHCO3, 10 ml HEPES, 1 ml 1 M NH4Cl, and 1 ml 1 M sodium pyruvate. The generated base salt rows use MediaDive's 1017 ml `g_l` projections, so all five base salts are slightly underrepresented.
- The generated rows for FeNa-EDTA, NaHCO3, NH4Cl, and sodium pyruvate convert ml stock additions into 1 or 2 g/L ingredient rows.
- Modified trace element mixture and Vitamin solution stock recipes are flattened into top-level final-medium ingredients at stock concentrations.
- The generated 12 g/L NaOH and 119.2 g/L HEPES rows belong to a 500 ml HEPES stock prepared separately and added at 10 ml/L.
- Source asterisks that mark filter-sterilized Vitamin solution, FeNa-EDTA, NaHCO3, and sodium pyruvate are not attached to the corresponding generated rows.

## Completeness

- Basic FWM solution, Modified trace element mixture, Vitamin solution, and HEPES solution are not structurally represented.
- Sterilization boundaries are incomplete because the generated record does not mark which additions are filter-sterilized and which are autoclaved.
- HEPES stock preparation is present as prose but not connected to a HEPES solution object.
- The JCM 31640 pH 7.0 strain note is missing from the generated preparation and notes.

## Findings

- Major: Basic FWM base salts were normalized over 1017 ml instead of retaining the 1 L source amounts before additive stocks; the fix belongs in `data/normalized_yaml/bacterial/freshwater_medium_for_soil_aoa.yaml` or the MediaDive/JCM importer.
- Major: ml additions of FeNa-EDTA, NaHCO3, NH4Cl, and sodium pyruvate stocks were imported as g/L final concentrations.
- Major: Modified trace element mixture, Vitamin solution, and HEPES solution are flattened into top-level stock-strength ingredients.
- Major: filter-sterile versus autoclaved addition boundaries from JCM 1004 are not represented structurally.
- Minor: the NiCl2 x 6 H2O source form is grounded to an anhydrous nickel dichloride term.
- Minor: the JCM 31640 pH adjustment note is absent.

## Recommended Edits

- Rebuild the maintained JCM 1004 record with Basic FWM, Modified trace element mixture, Vitamin solution, and HEPES solution as explicit solution structures.
- Restore the five Basic FWM salts to their 1 L source amounts instead of the 1017 ml post-addition normalization.
- Represent 7.5 mM FeNa-EDTA, 1 M NaHCO3, 1 M NH4Cl, and 1 M sodium pyruvate as ml/L stock additions with the correct filter-sterilization status.
- Keep Modified trace element, Vitamin, and HEPES stock ingredients inside their stock recipes and mark the 500 ml HEPES final volume.
- Preserve the JCM 31640 pH 7.0 note.
- Regenerate `data/merge_yaml/merged/freshwater_medium_for_soil_aoa__83395c34.yaml` after normalized/import curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated JCM J1004 YAML.
- Confirm NaCl, KCl, MgCl2 x 6 H2O, KH2PO4, and CaCl2 x 2 H2O retain 1 L Basic FWM source amounts.
- Confirm stock-only vitamin, trace-element, and HEPES components do not appear as top-level final-medium g/L rows.
- Confirm filter-sterilized additions are distinguishable from autoclaved additions.

## Additional Notes

- The generated file is derived data and is a one-source merge. The same JCM 1004 flattening is present in normalized YAML.
