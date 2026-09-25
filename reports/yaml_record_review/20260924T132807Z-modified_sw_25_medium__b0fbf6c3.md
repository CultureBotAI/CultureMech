# YAML Record Review: modified_sw_25_medium__b0fbf6c3
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_sw_25_medium__b0fbf6c3.yaml
- Started UTC: 2026-09-24T13:27:10Z
- Finished UTC: 2026-09-24T13:28:07Z
- Verdict: needs curation

## Target
Generated merged YAML for the solid-agar `modified_sw_25_medium`, CultureMech ID `CultureMech:007718`.

- Reviewed generated record: `data/merge_yaml/merged/modified_sw_25_medium__b0fbf6c3.yaml`
- Reviewed normalized source: `data/normalized_yaml/bacterial/TOGO_M1192_Modified_SW-25_Medium.yaml`
- Media term: `TOGO:M1192`, `Modified SW-25 Medium`
- Original source: `JCM_M1114-2`
- Cross-referenced base solution: `TOGO:M1191`
- Merge fingerprint: `b0fbf6c34310df649fbb0654084e9908e20ed5f977c4a17342f5d7bd009232f5`
- `merged_from`: `TOGO_M1192_Modified_SW-25_Medium`

## Validation
- Open LinkML validation: Passed, `No issues found`.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
The TOGO/JCM medium identity is mostly correct: TOGO `M1192` records `JCM_M1114-2`, a solid-agar Modified SW-25 Medium variant that uses the SW-25 solution from `M1191`.

The agar grounding to `CHEBI:2509` is correct. `Yeast extract` and `Casamino acids (BD-Difco)` are acceptable as ungrounded undefined complex ingredients. The SW-25 salt terms are absent from the generated record because its solution is empty.

The `kg_microbe_match` is wrong. The generated record points to `mediadive.medium:12`; a live MediaDive fetch for medium `12` returned `SOIL EXTRACT MEDIUM`, not Modified SW-25 Medium.

## Evidence
The live TOGO API for `M1192` reports a solid medium containing `Yeast extract`, 1 g; `agar`, 20 g/L; `Casamino acids (BD-Difco)`, 1 g; and `SW--25 solution (see Medium [M1191])`, 1 L. Its only comment says to adjust pH to 7.5, autoclave, and add 20.0 g/L agar for solid medium.

The live MediaDive `J1114` payload supplies the complete base recipe: 1000 ml `SW-25 solution`, 1 g `Casamino acids`, 1 g `Yeast extract`, pH 7.5, and a nested `SW-25 solution` containing 195 g NaCl, 32.5 g MgCl2 x 6 H2O, 51 g MgSO4 x 7 H2O, 5 g KCl, 0.6 g NaBr, 0.16 g NaHCO3, and 0.8 g CaCl2 x 2 H2O.

The normalized source already reflects that later evidence in a 2026-09-11 repair, with `ph_value: 7.5`, full SW-25 solution composition, ordered preparation steps, and explicit references. The reviewed merged YAML was last generated on 2026-08-06 and still reflects the older imported shape.

## Completeness
The generated record keeps the three final solid-medium additions from `M1192`, but it drops the actual SW-25 solution. Its `solutions` array has `SW--25 solution (see Medium [M1191])` with an empty `composition`, an `Unknown solution` name, and `1 G_PER_L` concentration even though the TOGO source gives a 1 L referenced solution.

Because the generated record is stale, it is also missing the repaired pH, SW-25 salt composition, water volume, preparation notes, preparation steps, and reference list that now exist in `data/normalized_yaml/bacterial/TOGO_M1192_Modified_SW-25_Medium.yaml`.

## Findings
1. Needs curation - the merged record is stale relative to its normalized source. The normalized YAML was repaired on 2026-09-11 to expand the referenced SW-25 solution and add pH and preparation steps, while the reviewed merged artifact was generated on 2026-08-06 and still omits those fields.

2. Needs curation - `SW--25 solution (see Medium [M1191])` is structurally empty and has the wrong unit. The source calls for 1 L of a referenced SW-25 solution, not a 1 g/L unknown solution with no composition.

3. Needs curation - `kg_microbe_match: mediadive.medium:12` points to the wrong MediaDive record. MediaDive medium `12` is DSMZ `SOIL EXTRACT MEDIUM`; this SW-25 branch should not carry that cross-link.

4. Minor - the direct JCM URL for `GRMD=1114` no longer returns the medium recipe, so the record should keep the resolvable TOGO `M1192`, TOGO `M1191`, and MediaDive `J1114` provenance that the normalized source now records.

## Recommended Edits
- Regenerate `data/merge_yaml/merged/modified_sw_25_medium__b0fbf6c3.yaml` from `data/normalized_yaml/bacterial/TOGO_M1192_Modified_SW-25_Medium.yaml` so the reviewed output picks up the 2026-09-11 repair.
- Ensure the regenerated artifact retains `ph_value: 7.5`, the `SW-25 solution` composition, `1000 ML_PER_L` of SW-25 solution, and the ordered mix, pH-adjustment, and autoclave steps.
- Remove or correct `kg_microbe_match: mediadive.medium:12`.
- Preserve `20.0 G_PER_L` agar as the distinguishing final ingredient for this `SOLID_AGAR` variant.

## Follow-up Checks
- After regeneration, compare the generated `solutions[0].composition` with live MediaDive `J1114` and confirm that all seven SW-25 salts are present.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.
- Recheck the KG-Microbe cross-link and confirm it no longer resolves to DSMZ Soil Extract Medium.

## Additional Notes
None found.
