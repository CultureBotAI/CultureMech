# YAML Record Review: NATRONOSPIRA PROTEINIVORA MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronospira_proteinivora_medium__300a6059.yaml
- Started UTC: 2026-09-24T16:55:38Z
- Finished UTC: 2026-09-24T16:55:38Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002312` for direct MediaDive/JCM J1139, `NATRONOSPIRA PROTEINIVORA MEDIUM`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to MediaDive/JCM J1139 for `NATRONOSPIRA PROTEINIVORA MEDIUM`.

An exact repository search including ignored and hidden files for `CultureMech:002312`, `GRMD=1139`, `mediadive.medium:J1139`, `natronospira_proteinivora_medium`, and `NATRONOSPIRA PROTEINIVORA` found this direct generated record plus its normalized owner, an active TOGO M1220 owner for the same JCM 1139 source, the TOGO generated record, and the targeted `scripts/repair_togo_m1220_score15.py` repair.

`NiCl2 x 6 H2O` is grounded to generic nickel dichloride.

## Evidence

JCM Medium 1139 defines the final medium by aseptically combining 500.0 ml Basic mineral salt medium 1, 500.0 ml Basal medium 2, 15.0 ml 10% Tryptone solution, and 2.0 ml 1.0% Yeast extract solution.

Basic mineral salt medium 1 is a 1 L stock containing 240.0 g NaCl, 2.5 g K2HPO4, and 0.5 g `(NH4)2SO4`, adjusted to pH 6.8 - 6.9 with 1 M K2HPO4, autoclaved, cooled, then amended with 1.0 ml 1 M MgCl2 and 1.0 ml JCM 1079 Trace element solution.

Basal medium 2 is a 1 L stock containing 190.0 g Na2CO3, 30.0 g NaHCO3, 16.0 g NaCl, and 2.0 g K2HPO4, adjusted to pH 9.9 - 10.0, autoclaved, settled for three days, decanted, and amended with 4.0 ml 2 M NH4Cl, 1.0 ml 1 M MgCl2, and 2.0 ml JCM 1079 Trace element solution.

The JCM page prints a 5% Casein solution subrecipe but never includes that solution in the final main recipe.

## Completeness

The generated record has no solution entries and flattens every top-level, nested, and trace-element stock row into direct ingredients.

The active TOGO M1220 owner has already been repaired to preserve the JCM 1139 stock boundaries and to omit Casein solution from the final medium because the source gives no final addition volume.

## Findings

- Major: The 500.0 ml Basic mineral salt medium 1 and 500.0 ml Basal medium 2 final additions are absent; their internal salts were flattened into direct ingredients.
- Major: MediaDive internal volumes for Basic mineral salt medium 1 and Basal medium 2 were used as concentration denominators, producing NaCl at `122285.71 G_PER_L`, K2HPO4 at `1535.714 G_PER_L`, Na2CO3 at `27142.9 G_PER_L`, and NaHCO3 at `4285.71 G_PER_L`.
- Major: The 15.0 ml 10% Tryptone and 2.0 ml 1.0% Yeast extract additions were converted to 15 and 2 `G_PER_L`.
- Major: The printed Casein solution subrecipe was flattened into the final medium even though JCM 1139 gives no final Casein solution addition.
- Major: The 1.0 ml, 2.0 ml, and 4.0 ml nested stock additions for MgCl2, NH4Cl, and JCM 1079 Trace element solution were flattened into direct ingredients.
- Major: The direct JCM/MediaDive J1139 owner is unlinked from the already repaired TOGO M1220 owner.
- Minor: `NiCl2 x 6 H2O` is grounded to generic nickel dichloride.

## Recommended Edits

- In `data/normalized_yaml/bacterial/natronospira_proteinivora_medium.yaml`, use the repaired TOGO M1220 model to restore Basic mineral salt medium 1 and Basal medium 2 as 500.0 ml final additions.
- Preserve the 10% Tryptone and 1.0% Yeast extract additions as 15.0 ml and 2.0 ml stock additions.
- Preserve MgCl2, NH4Cl, and JCM 1079 Trace element solution as nested milliliter additions inside the appropriate stock media.
- Remove Casein solution from the final medium unless a final addition volume is found in an authoritative source.
- Link or collapse the direct JCM/MediaDive J1139 owner with the repaired TOGO M1220 owner.
- Re-ground `NiCl2 x 6 H2O` to an exact hydrate term where one is available, or document it as unresolved.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronospira_proteinivora_medium__300a6059.yaml` and verify the large MediaDive-volume-derived gram-per-liter rows are gone.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `TOGO:M1220`, `mediadive.medium:J1139`, and `GRMD=1139` to verify the TOGO and direct JCM owners are linked or collapsed.

## Additional Notes

None found.
