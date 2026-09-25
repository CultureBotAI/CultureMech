# YAML Record Review: NATRONOLIMNOBIUS AHT32 MEDIUM (B)

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronolimnobius_aht32_medium_b__22c9a085.yaml
- Started UTC: 2026-09-24T16:54:20Z
- Finished UTC: 2026-09-24T16:54:21Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002272` for direct MediaDive/JCM J1092, `NATRONOLIMNOBIUS AHT32 MEDIUM (B)`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to MediaDive/JCM J1092 for `NATRONOLIMNOBIUS AHT32 MEDIUM (B)`.

An exact repository search including ignored and hidden files for `TOGO:M1162`, `CultureMech:007686`, `CultureMech:002272`, `GRMD=1092`, `mediadive.medium:J1092`, `JCM_M1092`, and `natronolimnobius_aht32_medium_b` found this direct JCM generated record plus its normalized owner and an active TOGO M1162 generated import of the same JCM medium.

No wrong ontology grounding was found in the direct generated ingredients, but the ingredient list has been over-flattened enough that several legitimate solution groundings are absent.

## Evidence

The JCM Medium 1092 page lists 1.0 L sterilized Soda based mineral medium from JCM Medium 1081.

The source then lists per-liter additions of 10.0 ml Trace vitamins, 0.2 ml 10% Yeast extract solution, 20.0 ml 1 M Sodium butyrate, and 20.0 ml 1 M Sodium acetate.

The source instructs replacing the gas phase with N2 containing 5% O2 by volume and sealing with butyl rubber stoppers.

The MediaDive J1092 record agrees with the source page and models the Soda based mineral medium as its own solution with Na2CO3, NaHCO3, NaCl, K2HPO4, KCl, 4 M NH4Cl, Selenite-tungstate solution, Trace element solution, and 1 M MgCl2.

## Completeness

The generated record has no solution entries; every top-level J1092 addition and every nested JCM 1081 Soda based mineral medium component was flattened into direct ingredients.

The preparation steps preserve relevant text but are ordered with the J1092 aseptic-addition step before the nested Soda based mineral medium preparation step.

## Findings

- Major: The 1.0 L Soda based mineral medium addition is absent, and the nested JCM 1081 stock was flattened into direct final-medium ingredients.
- Major: JCM 1081 base salts were scaled against MediaDive's internal 4 ml `Soda based mineral medium` volume, producing 46250, 8750, 4000, 250, and 1250 `G_PER_L` for Na2CO3, NaHCO3, NaCl, K2HPO4, and KCl.
- Major: The 10.0 ml trace-vitamins, 0.2 ml yeast-extract, 20.0 ml sodium-butyrate, and 20.0 ml sodium-acetate additions were flattened as `G_PER_L` direct ingredients.
- Major: The 4 M NH4Cl, 1 M MgCl2, selenite-tungstate, and trace-element solution additions inside the soda based mineral medium were flattened or dropped.
- Major: TOGO M1162 remains unlinked from the active direct JCM/MediaDive J1092 owner for the same medium.
- Minor: Preparation steps are present but reversed across the nested JCM 1081 and top-level JCM 1092 phases.

## Recommended Edits

- In `data/normalized_yaml/archaea/natronolimnobius_aht32_medium_b.yaml`, preserve Soda based mineral medium as a 1.0 L nested solution addition instead of flattening JCM 1081.
- Represent 10.0 ml Trace vitamins, 0.2 ml 10% Yeast extract solution, 20.0 ml 1 M Sodium butyrate, and 20.0 ml 1 M Sodium acetate as top-level JCM 1092 solution additions.
- Preserve 4 M NH4Cl, Selenite-tungstate solution, Trace element solution, and 1 M MgCl2 as nested JCM 1081 additions.
- Reorder the preparation steps so Soda based mineral medium is prepared before the JCM 1092 aseptic additions.
- Link or collapse the direct JCM/MediaDive J1092 owner with TOGO M1162.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronolimnobius_aht32_medium_b__22c9a085.yaml` and verify no JCM 1081 component is normalized to MediaDive's internal 4 ml volume.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `TOGO:M1162`, `mediadive.medium:J1092`, and `GRMD=1092` to verify the duplicate source records are linked or collapsed.

## Additional Notes

None found.
