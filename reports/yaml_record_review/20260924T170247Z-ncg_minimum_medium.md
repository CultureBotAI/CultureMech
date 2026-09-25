# YAML Record Review: NCG (minimum medium)

- Repository: CultureMech
- Record: data/merge_yaml/merged/ncg_minimum_medium.yaml
- Started UTC: 2026-09-24T17:02:46Z
- Finished UTC: 2026-09-24T17:02:47Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:009384` for TOGO M2842, `NCG (minimum medium)`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to TOGO M2842.

An exact repository search including ignored and hidden files for `TOGO:M2842`, `CultureMech:009384`, `ncg_minimum_medium`, `NCG (minimum medium)`, `mediadive.medium:780`, and `M2842` found this generated record, its normalized owner, the targeted `repair_nutrient_ncg_nssm_score15.py` repair, and unrelated records that show `mediadive.medium:780` belongs to DSMZ/KOMODO Medium 780 rather than NCG.

The source mixture rows for yeast nitrogen base and casamino acid are correctly ungrounded to CHEBI; glycerol is grounded correctly.

## Evidence

TOGO M2842 lists 2% glycerol, 0.5% yeast nitrogen base from BD Difco, and 0.5% casamino acid from BD Difco.

The TOGO payload also carries a comment that the culture was grown routinely at 30 C.

The normalized owner was repaired on 2026-09-12 to preserve those three ingredient claims with source-scoped notes, add `temperature_value: 30.0`, and remove the unrelated MediaDive 780 match.

## Completeness

The generated record was merged on 2026-08-06 and is stale relative to the 2026-09-12 normalized-owner repair.

The generated record lacks the 30 C condition, `references`, and `data_quality_flags` from the repaired owner.

## Findings

- Major: The generated record is stale relative to its maintained normalized owner; the owner now contains the `RESOLVED_TOGO_M2842_SCORE15` repair from `repair_nutrient_ncg_nssm_score15.py`.
- Major: The generated record still has `kg_microbe_match: mediadive.medium:780`, which points to unrelated Medium 780 records and was removed from the repaired owner.
- Major: The generated record omits the TOGO 30 C growth condition captured in the repaired owner.
- Minor: The generated record omits the repaired owner's source-scoped ingredient notes, reference, and data-quality flags.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/ncg_minimum_medium.yaml` from the repaired `data/normalized_yaml/bacterial/ncg_minimum_medium.yaml` owner.
- Verify the regenerated record carries `temperature_value: 30.0` and no `kg_microbe_match`.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Search including ignored and hidden files for `TOGO:M2842`, `CultureMech:009384`, and `mediadive.medium:780` to verify the NCG generated record is no longer linked to MediaDive 780.

## Additional Notes

None found.
