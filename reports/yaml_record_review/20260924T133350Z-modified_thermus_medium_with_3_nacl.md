# YAML Record Review: modified_thermus_medium_with_3_nacl
- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_thermus_medium_with_3_nacl.yaml
- Started UTC: 2026-09-24T13:33:00Z
- Finished UTC: 2026-09-24T13:33:50Z
- Verdict: needs curation

## Target
Generated merged YAML for `modified_thermus_medium_with_3_nacl`, CultureMech ID `CultureMech:010034`.

- Reviewed generated record: `data/merge_yaml/merged/modified_thermus_medium_with_3_nacl.yaml`
- Reviewed normalized source: `data/normalized_yaml/bacterial/TOGO_M634_Modified_Thermus_Medium_With_3_NaCl.yaml`
- Reviewed linked JCM duplicate source: `data/normalized_yaml/bacterial/modified_thermus_medium_with_3_nacl.yaml`
- Media term: `TOGO:M634`, `Modified Thermus Medium With 3% NaCl`
- Original source: `JCM_M624`
- Merge fingerprint: `76e39a8f2f5e77c89c5bba1adfcff59230205492501ad49de4c1538988fde54e`

## Validation
- Open LinkML validation: Passed, `No issues found`.
- Strict validation: Passed with 0 error rows across 1 file. The strict TSV had 1 line, the header only.
- LinkML reference validation: Passed; 1 file validated, 0 checks, all validations passed.
- LinkML term validation: Passed; emitted the known `eutils`/`pkg_resources` deprecation warning and exited 0.
- Embedded `curation_history`: Not checked; the available history validator targets standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding
The TOGO/JCM identity is coherent: live JCM `624` and TOGO `M634` describe the same Modified Thermus Medium with 3% NaCl liquid formulation.

The generated grounding is incomplete:

- `NaCl` is grounded correctly.
- `Sodium glutamate x H2O`, peptone, and yeast extract are ungrounded in the generated record even though the 2026-09-11 normalized repairs added better grounding for all three.
- The cross-referenced Castenholz basal salt solution is an ungrounded empty placeholder instead of a 10 ml/L link to the curated `CultureMech:013022` stock.

## Evidence
The live JCM `GRMD=624` page resolves and lists 3.0 g peptone, 1.0 g yeast extract, 1.0 g sodium glutamate x H2O, 30.0 g NaCl, 10.0 ml Castenholz basal salt solution from Medium 273, and distilled water to 1.0 L.

The live TOGO `M634` API mirrors the same recipe under `JCM_M624`, reports pH 7.8, and preserves the source note for optional agar plates at 20.0 g/L agar.

The reviewed generated YAML was emitted on 2026-08-06. The normalized TOGO `M634` source and the linked JCM `J624` duplicate were both repaired on 2026-09-11 with pH 7.8, a 10.0 ml/L Castenholz basal salt solution, a curated `CultureMech:013022` solution link, the corrected water unit, and additional grounding.

## Completeness
The generated record has the four non-water main ingredients at the right amounts, but it is missing source pH, source preparation notes, and the full Castenholz basal salt link. It also preserves the 1 L water and 10 ml Castenholz stock volumes as `G_PER_L`, so two source volumes are typed as masses.

The current normalized YAML files already contain the richer repair; this generated artifact has not been rebuilt from those repaired inputs.

## Findings
1. Needs curation - the merged artifact is stale relative to `data/normalized_yaml/bacterial/TOGO_M634_Modified_Thermus_Medium_With_3_NaCl.yaml`. The normalized file was repaired on 2026-09-11, after the 2026-08-06 merge, and the reviewed YAML still lacks the pH, corrected units, curated Castenholz stock, and improved grounding.

2. Needs curation - `Distilled water` is recorded as `1 G_PER_L`, but both live JCM and TOGO sources list 1 L water.

3. Needs curation - `Castenholz basal salt solution (see Medium [M266])` is an empty `Unknown solution` at `10 G_PER_L`. The source calls for 10 ml Castenholz basal salt solution per liter, and the repaired source now points to curated `CultureMech:013022`.

4. Minor - the generated record dropped `ph_value: 7.8` and the source note that 20.0 g/L agar can be added for agar plates.

5. Minor - `Sodium glutamate x H2O` is ungrounded in the generated YAML, but the repaired normalized sources ground it to hydrated monosodium L-glutamate.

## Recommended Edits
- Regenerate `data/merge_yaml/merged/modified_thermus_medium_with_3_nacl.yaml` from the repaired TOGO `M634` source.
- Confirm that the regenerated artifact carries `ph_value: 7.8`, `Distilled water` as 1 L, and `Castenholz basal salt solution` as 10 ml/L rather than 10 g/L.
- Preserve the Castenholz link to `CultureMech:013022`, including JCM Medium 273 evidence for the stock.
- Reconcile the TOGO `M634` record with the JCM `J624` duplicate in `data/normalized_yaml/bacterial/modified_thermus_medium_with_3_nacl.yaml`.

## Follow-up Checks
- Re-fetch JCM `GRMD=624` and TOGO `M634` and confirm that the regenerated record still matches their five main rows and pH 7.8.
- Confirm that the adjacent agar-plate variant remains separate from this liquid recipe but is linked as a physical-state variant.
- Revalidate the regenerated YAML with open LinkML, strict schema, reference, and term validators.

## Additional Notes
None found.
