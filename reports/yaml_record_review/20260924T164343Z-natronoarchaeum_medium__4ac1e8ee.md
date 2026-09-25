# YAML Record Review: Natronoarchaeum Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronoarchaeum_medium__4ac1e8ee.yaml
- Started UTC: 2026-09-24T16:43:43Z
- Finished UTC: 2026-09-24T16:43:43Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:010233` for TOGO M820, a solid-agar import of JCM Medium 788, `Natronoarchaeum Medium`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to the intended TOGO M820 import of the JCM `GRMD=788` solid-medium variant.

An exact repository search including ignored files for `CultureMech:003131`, `GRMD=788`, `mediadive.medium:J788`, `natronoarchaeum_medium__27e57f44`, `natronoarchaeum_medium__4ac1e8ee`, and `name: natronoarchaeum_medium` found this TOGO M820 owner plus the active direct JCM owner and TOGO M819 liquid owner for the same JCM page.

`K2HSO4` remains ungrounded.

## Evidence

JCM Medium 788 lists 4.0 g Casamino acids, 0.5 g yeast extract, 3.0 g glucose, 0.1 g sodium glutamate, 0.3 g trisodium citrate, 1.0 g K2HSO4, 1.0 g MgCl2 x 6H2O, 2.0 g KCl, 220.0 g NaCl, 36.0 mg FeCl2 x 4H2O, and 0.36 mg MnCl2 x 4H2O.

The JCM source brings the components to 1.0 L with distilled water, adjusts pH to 8.5 - 8.8 before autoclaving, and instructs adding 20.0 g/L Noble agar for solid medium.

The generated M820 record includes the 20 g/L agar row and is correctly typed as `SOLID_AGAR`.

## Completeness

The generated record lacks the pH 8.5 - 8.8 adjustment and autoclave preparation step.

The water row is present but mis-unitized as `1 G_PER_L` rather than 1.0 L.

## Findings

- The source milligram FeCl2 x 4H2O and MnCl2 x 4H2O amounts were promoted to gram-per-liter values, so 36 mg became `36 G_PER_L` and 0.36 mg became `0.36 G_PER_L`.
- Distilled water is mis-unitized as `1 G_PER_L`.
- The source pH range 8.5 - 8.8 and autoclaving instruction are absent.
- TOGO M820 is unlinked from the direct JCM liquid owner and the TOGO M819 liquid mirror, even though all three records cite JCM `GRMD=788`.
- `K2HSO4` has no ontology grounding.

## Recommended Edits

- Correct FeCl2 x 4H2O and MnCl2 x 4H2O to `MG_PER_L` source amounts.
- Correct the water row to 1.0 L.
- Restore the pH range and autoclave preparation step from the source.
- Link M820 as the agar variant of JCM 788 and collapse or link the duplicate M819 liquid mirror with the direct JCM liquid owner.
- Ground `K2HSO4` or document it as an unresolved source term.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronoarchaeum_medium__4ac1e8ee.yaml` and verify the Fe and Mn rows retain `MG_PER_L`.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored files for `GRMD=788`, `TOGO:M819`, and `TOGO:M820` to verify the liquid and agar variants are linked as intended.

## Additional Notes

None found.
