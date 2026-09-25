# YAML Record Review: modified_thermus_medium_with_3_nacl__d058b9c6
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_thermus_medium_with_3_nacl__d058b9c6.yaml
- Started UTC: 2026-09-24T13:34:33Z
- Finished UTC: 2026-09-24T13:35:11Z
- Verdict: needs curation

## Target
Generated merged YAML for the solid-agar `modified_thermus_medium_with_3_nacl`, CultureMech ID `CultureMech:010035`.

- Reviewed generated record: `data/merge_yaml/merged/modified_thermus_medium_with_3_nacl__d058b9c6.yaml`
- Reviewed normalized source: `data/normalized_yaml/bacterial/TOGO_M635_Modified_Thermus_Medium_With_3_NaCl.yaml`
- Media term: `TOGO:M635`, `Modified Thermus Medium With 3% NaCl`
- Original source: `JCM_M624-2`
- Parent liquid medium: JCM Medium `624`, TOGO `M634`
- Merge fingerprint: `d058b9c67cda0d14f03ec1d06ff89c01a2e59bd634fdf1b0756782d90a4eee4e`

## Validation
- Open LinkML validation: Passed, `No issues found`.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
The TOGO identity is coherent. Live TOGO `M635` is the agar-plate formulation of JCM Medium 624: it has the same Thermus 3% NaCl liquid base as TOGO `M634` plus 20 g/L agar.

The generated grounding is incomplete:

- `NaCl` and `agar` are grounded correctly.
- `Sodium glutamate x H2O`, peptone, and yeast extract are ungrounded in the generated record even though the 2026-09-11 normalized repair grounded all three.
- The cross-referenced Castenholz basal salt solution is an ungrounded empty placeholder instead of a 10 ml/L link to curated `CultureMech:013022`.

## Evidence
The live TOGO `M635` API reports `JCM_M624-2` and lists 1 L distilled water, 1 g yeast extract, 30 g NaCl, 1 g Sodium glutamate x H2O, 20 g/L agar, 3 g peptone, and 10 ml `Castenholz basal salt solution (see Medium [M266])`.

The same TOGO payload has the two comments from JCM Medium 624: adjust pH to 7.8, and add 20.0 g/L agar for agar plates. The live JCM `GRMD=624` page resolves and carries the same base formula and pH instruction.

The normalized TOGO `M635` source was repaired on 2026-09-11 to correct the water and Castenholz stock units, add pH 7.8, ground peptone, yeast extract, sodium glutamate, and agar, and represent M635 as the JCM 624 agar-plate variant. The generated artifact was emitted earlier, on 2026-08-06.

## Completeness
The generated record keeps the final peptone, yeast extract, NaCl, sodium glutamate, and agar amounts, and `physical_state: SOLID_AGAR` is appropriate.

It is incomplete in the same way as the liquid M634 artifact: the water volume is typed as mass, the 10 ml Castenholz addition is a `10 G_PER_L` unknown empty solution, and pH 7.8 is absent. The correct Castenholz stock composition is already curated in `CultureMech:013022`.

## Findings
1. Needs curation - the merged artifact is stale relative to `data/normalized_yaml/bacterial/TOGO_M635_Modified_Thermus_Medium_With_3_NaCl.yaml`. The normalized file was repaired on 2026-09-11, while the reviewed YAML still reflects the 2026-08-06 empty-solution import.

2. Needs curation - `Distilled water` is recorded as `1 G_PER_L`, but TOGO `M635` lists 1 L water.

3. Needs curation - `Castenholz basal salt solution (see Medium [M266])` is an empty `Unknown solution` at `10 G_PER_L`. The source calls for 10 ml Castenholz basal salt solution per liter from JCM Medium 273.

4. Minor - `ph_value: 7.8` is missing even though TOGO `M635` retains the JCM pH comment.

5. Minor - `Sodium glutamate x H2O` is ungrounded in the generated YAML, but the repaired normalized source grounds it to hydrated monosodium L-glutamate.

## Recommended Edits
- Regenerate `data/merge_yaml/merged/modified_thermus_medium_with_3_nacl__d058b9c6.yaml` from the repaired TOGO `M635` source.
- Confirm that the regenerated artifact carries `ph_value: 7.8`, `Distilled water` as 1 L, `Castenholz basal salt solution` as 10 ml/L, and `Agar` at 20.0 g/L.
- Preserve this record as `SOLID_AGAR` and keep it linked to the M634 liquid parent as a physical-state variant.
- Preserve the Castenholz link to `CultureMech:013022`, including JCM Medium 273 evidence for the stock.

## Follow-up Checks
- Re-fetch TOGO `M635` and JCM `GRMD=624` and confirm that the regenerated record still matches the agar-plate variant.
- Confirm that M634 and M635 remain separate records with identical liquid bases and only the 20.0 g/L agar difference.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.

## Additional Notes
None found.
