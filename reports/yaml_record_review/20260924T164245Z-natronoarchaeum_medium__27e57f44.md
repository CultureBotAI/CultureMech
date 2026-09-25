# YAML Record Review: NATRONOARCHAEUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronoarchaeum_medium__27e57f44.yaml
- Started UTC: 2026-09-24T16:42:45Z
- Finished UTC: 2026-09-24T16:42:45Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:003131` for the direct JCM import of JCM Medium 788, `NATRONOARCHAEUM MEDIUM`, with MediaDive term `mediadive.medium:J788`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to the intended direct JCM `GRMD=788` source through `mediadive.medium:J788`.

An exact repository search including ignored files for `CultureMech:003131`, `GRMD=788`, `mediadive.medium:J788`, `natronoarchaeum_medium__27e57f44`, `natronoarchaeum_medium__4ac1e8ee`, and `name: natronoarchaeum_medium` found this direct JCM owner plus two active TOGO owners, `TOGO_M819_Natronoarchaeum_Medium.yaml` and `TOGO_M820_Natronoarchaeum_Medium.yaml`, that cite the same JCM page.

`K2HSO4` remains ungrounded.

## Evidence

JCM Medium 788 lists 4.0 g Casamino acids, 0.5 g yeast extract, 3.0 g glucose, 0.1 g sodium glutamate, 0.3 g trisodium citrate, 1.0 g K2HSO4, 1.0 g MgCl2 x 6H2O, 2.0 g KCl, 220.0 g NaCl, 36.0 mg FeCl2 x 4H2O, and 0.36 mg MnCl2 x 4H2O. The source then instructs adding the components to distilled water, bringing the volume to 1.0 L, and adjusting pH to 8.5 - 8.8 before autoclaving.

For solid medium, the same JCM page adds 20.0 g/L Noble agar.

MediaDive J788 preserves the source masses and the milligram FeCl2 x 4H2O and MnCl2 x 4H2O rows, but stores `min_pH` and `max_pH` as 8.7 rather than the live source's 8.5 - 8.8 range.

## Completeness

The generated direct JCM record omits the 1.0 L distilled water row.

It records `ph_value: 8.7`, losing the source pH range.

It preserves the source solid-medium note as a preparation step without turning agar into a liquid-medium ingredient, which is appropriate for this liquid record.

## Findings

- The source water row is missing even though JCM explicitly says to bring the medium to 1.0 L with distilled water.
- The pH range 8.5 - 8.8 is collapsed to the MediaDive midpoint 8.7.
- JCM Medium 788 is represented by three active owners: the direct JCM/MediaDive owner, a TOGO liquid mirror, and a TOGO solid-agar mirror.
- `K2HSO4` has no ontology grounding.

## Recommended Edits

- Add the missing 1.0 L distilled water to the direct JCM owner.
- Preserve the JCM pH range instead of reducing it to a single 8.7 value.
- Link the direct, TOGO M819, and TOGO M820 owners intentionally, with M820 represented as an agar variant rather than a source duplicate.
- Ground `K2HSO4` or document it as an unresolved source term.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronoarchaeum_medium__27e57f44.yaml` and verify it contains the 1.0 L water row and the source pH range.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored files for `GRMD=788`, `mediadive.medium:J788`, `TOGO:M819`, and `TOGO:M820` to verify the owner relationships.

## Additional Notes

None found.
