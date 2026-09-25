# YAML Record Review: modified_csy_3_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_csy_3_agar.yaml
- Started UTC: 2026-09-24T10:44:15Z
- Finished UTC: 2026-09-24T10:44:59Z
- Verdict: needs curation

## Target

Generated record `CultureMech:010251` for TOGO medium `M837`, `Modified CSY-3 Agar`, a TOGO import of JCM medium 802.

The exact maintained owner is `data/normalized_yaml/bacterial/TOGO_M837_Modified_CSY-3_Agar.yaml`. The generated YAML was compared with that owner, JCM medium 802, and MediaDive medium `J802`.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_csy_3_agar.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct TOGO M837 identity and source lineage to JCM 802.

The generated artifact is stale relative to the maintained owner. A 2026-09-11 `RESOLVED_TOGO_M837_MODIFIED_CSY3_AGAR` repair restored the source-level sea-water row, pH, complex-nutrient grounding, and preparation steps in `TOGO_M837_Modified_CSY-3_Agar.yaml`, but `data/merge_yaml/merged/modified_csy_3_agar.yaml` was last merged on 2026-08-06 and still contains the pre-repair import.

## Evidence

JCM 802 lists 1 g Casitone, 1 g Phytone peptone, 1 g yeast extract, 0.4 g ferric ammonium citrate, 15 g agar, and 1 L seawater, followed by adjustment to pH 7.5. MediaDive `J802` encodes the same formula as gram-scale rows in 1000 ml sea water with a pH 7.5 preparation step.

The repaired maintained owner now stores Casitone, Phytone peptone, yeast extract, ferric ammonium citrate, and agar with their source amounts, stores `Sea water` as `1000.0` `ML_PER_L`, records `ph_range` 7.5 to 7.5, and adds explicit mix and pH-adjustment steps.

The generated record stores `Seawater` as `1` `G_PER_L`, omits pH 7.5, has no preparation steps, and lacks the repaired owner terms and roles for the complex nutrient rows.

## Completeness

The generated record preserves the source label, source URL, and the five non-solvent ingredient amounts.

It is incomplete for the solvent row, pH, and preparation. The maintained owner already contains those repairs.

## Findings

- High: The generated YAML is stale relative to the 2026-09-11 repair in `TOGO_M837_Modified_CSY-3_Agar.yaml`.
- High: The source 1 L seawater solvent row is represented as 1 g/L.
- Medium: pH 7.5 and the pH-adjustment step are absent from the generated artifact.
- Low: FOODON/role enrichment present in the repaired owner is not present in the generated YAML.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/modified_csy_3_agar.yaml` from the repaired 2026-09-11 maintained owner.
- Confirm that the regenerated artifact keeps `Sea water` at `1000.0` `ML_PER_L`, carries pH 7.5, and includes the mix and pH-adjustment preparation steps.
- Preserve the MediaDive `J802` source-duplicate linkage from the maintained owner.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against JCM 802 and MediaDive `J802` to verify the seawater, agar, ferric ammonium citrate, Casitone, Phytone peptone, and yeast-extract rows.

## Additional Notes

The exact owner was found with `find`, which included ignored files.
