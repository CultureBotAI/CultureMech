# YAML Record Review: modified_csy_3_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_csy_3_agar__3fe99fb3.yaml
- Started UTC: 2026-09-24T10:45:07Z
- Finished UTC: 2026-09-24T10:45:43Z
- Verdict: needs curation

## Target

Generated record `CultureMech:003147` for JCM/MediaDive medium `J802`, `MODIFIED CSY-3 AGAR`.

The generated record merges `modified_csy_3_agar` from `data/normalized_yaml/bacterial/modified_csy_3_agar.yaml`. The generated YAML was compared with that maintained owner, JCM medium 802, and MediaDive medium `J802`.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_csy_3_agar__3fe99fb3.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct JCM/MediaDive medium identity and preserves pH 7.5.

The generated artifact is stale relative to a 2026-09-11 `RESOLVED_JCM_802_MODIFIED_CSY3_AGAR` repair in `data/normalized_yaml/bacterial/modified_csy_3_agar.yaml`. The maintained owner now restores source-specific product qualifiers, FOODON grounding for Phytone peptone and yeast extract, ENVO grounding for sea water, explicit preparation steps, and a TOGO M837 source-duplicate child.

## Evidence

JCM 802 lists 1 g Casitone, 1 g Phytone peptone, 1 g yeast extract, 0.4 g ferric ammonium citrate, 15 g agar, and 1 L seawater, followed by adjustment to pH 7.5. MediaDive `J802` encodes the same formula as gram-scale rows in 1000 ml sea water with a pH 7.5 preparation step.

The repaired maintained owner now keeps the complex rows as `Casitone (BD-Difco)`, `Phytone peptone (BD-BBL)`, and `Yeast extract (BD-Difco)`, stores `Sea water` as `1000.0` `ML_PER_L`, grounds sea water to `ENVO:00002149`, and adds explicit mix and pH-adjustment steps.

The generated record stores `Sea water` as `1000` `G_PER_L`, omits the BD-Difco and BD-BBL qualifiers from the three complex nutrient row labels, has no sea-water term, and contains only the pH-adjustment preparation step.

## Completeness

The generated record preserves the JCM/MediaDive identity, pH 7.5, and all five non-solvent ingredient amounts.

It is incomplete for the seawater unit, source qualifiers, source-duplicate linkage, and the explicit mix step. The maintained owner already contains those repairs.

## Findings

- High: The generated YAML is stale relative to the 2026-09-11 repair in `modified_csy_3_agar.yaml`.
- High: The source 1000 ml seawater solvent row is represented as 1000 g/L.
- Low: BD-Difco and BD-BBL qualifiers, FOODON/ENVO grounding, source-duplicate linkage, and the explicit mix step are absent from the generated artifact.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/modified_csy_3_agar__3fe99fb3.yaml` from the repaired 2026-09-11 maintained owner.
- Confirm that the regenerated artifact keeps `Sea water` at `1000.0` `ML_PER_L`, carries ENVO grounding for sea water, and includes the repaired mix and pH-adjustment preparation steps.
- Preserve the TOGO M837 source-duplicate linkage from the maintained owner so this MediaDive/JCM record does not drift from the TOGO import of the same source formula.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against JCM 802 and MediaDive `J802` to verify the seawater, pH, agar, ferric ammonium citrate, Casitone, Phytone peptone, and yeast-extract rows.

## Additional Notes

None found.
