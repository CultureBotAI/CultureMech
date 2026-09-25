# YAML Record Review: Natronolimnobius AHT32 Medium (B)

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronolimnobius_aht32_medium_b.yaml
- Started UTC: 2026-09-24T16:53:46Z
- Finished UTC: 2026-09-24T16:53:46Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:007686` for TOGO M1162, a JCM M1092 import of `Natronolimnobius AHT32 Medium (B)`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to TOGO M1162 and its original JCM Medium 1092 page.

An exact repository search including ignored and hidden files for `TOGO:M1162`, `CultureMech:007686`, `CultureMech:002272`, `GRMD=1092`, `mediadive.medium:J1092`, `JCM_M1092`, and `natronolimnobius_aht32_medium_b` found this TOGO M1162 generated record plus its normalized owner, an active direct MediaDive/JCM J1092 owner, and a 2026-09-10 targeted repair in `scripts/repair_togo_jcm_archaea_score15.py`.

The generated row for nitrogen is grounded, but the source atmosphere is N2 containing 5% O2 by volume, not separate variable ingredients. The oxygen row is ungrounded in the generated output.

## Evidence

JCM Medium 1092 lists 1.0 L sterilized Soda based mineral medium from JCM Medium 1081.

The source then instructs aseptically adding 10.0 ml trace vitamins, 0.2 ml 10% yeast extract solution, 20.0 ml 1 M sodium butyrate, and 20.0 ml 1 M sodium acetate per liter, and replacing the gas phase with N2 containing 5% O2 by volume before sealing the vessels with butyl rubber stoppers.

The normalized TOGO owner has already been repaired to represent those JCM Medium 1092 additions as `ML_PER_L` solution additions, including nested composition for the JCM 1081 soda based mineral medium and the JCM 197 trace-vitamins stock.

## Completeness

The generated record was merged on 2026-08-06 and is stale relative to the 2026-09-10 normalized-owner repair.

The generated output lacks the repaired Soda based mineral medium, trace-vitamins, yeast-extract, sodium-butyrate, sodium-acetate, and gas-atmosphere structure.

## Findings

- Major: The generated record is stale relative to its maintained normalized owner; the owner now contains the repair from `repair_togo_jcm_archaea_score15.py`, but the generated record still has pre-repair empty solution wrappers.
- Major: `Soda based mineral medium`, `10% Yeast extract solution`, and `Trace vitamins` are empty `Unknown solution` entries.
- Major: The JCM 1.0 L, 10.0 ml, 0.2 ml, 20.0 ml, and 20.0 ml addition volumes are stored as `G_PER_L` values.
- Major: The N2 plus 5% O2 gas phase and butyl-rubber-stopper instruction are absent.
- Major: TOGO M1162 remains unlinked from the active direct JCM/MediaDive J1092 record for the same medium.
- Minor: Oxygen gas is ungrounded and both gases are modeled as variable ingredients rather than an atmosphere condition.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/natronolimnobius_aht32_medium_b.yaml` from the repaired `data/normalized_yaml/archaea/TOGO_M1162_Natronolimnobius_AHT32_Medium_B.yaml` owner.
- Confirm the regenerated record preserves the JCM 1081 Soda based mineral medium, JCM 197 Trace vitamins, 10% yeast extract, 1 M sodium butyrate, and 1 M sodium acetate as solution additions.
- Replace nitrogen and oxygen ingredients with a scoped N2 plus 5% O2 atmosphere condition if the schema supports that representation.
- Link or collapse TOGO M1162 with the direct JCM/MediaDive J1092 owner.

## Follow-up Checks

- Re-run the merge for TOGO M1162 and verify the reviewed generated record no longer has empty `Unknown solution` wrappers.
- Re-run open schema, strict, reference, and term validation after regeneration.
- Search including ignored and hidden files for `TOGO:M1162`, `mediadive.medium:J1092`, and `GRMD=1092` to verify the direct and TOGO JCM imports are linked or collapsed.

## Additional Notes

None found.
