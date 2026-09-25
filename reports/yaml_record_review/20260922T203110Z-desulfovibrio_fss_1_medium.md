# YAML Record Review: DESULFOVIBRIO FSS-1 MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_fss_1_medium.yaml`
- Started UTC: 2026-09-22T20:31:10Z
- Finished UTC: 2026-09-22T20:31:53Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:002374` for `desulfovibrio_fss_1_medium`, a MediaDive import of JCM Medium J1205.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, exit 0).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The record is grounded to `mediadive.medium:J1205`, `DESULFOVIBRIO FSS-1 MEDIUM`, with JCM as the imported source and JCM GRMD 1205 in `notes`.

A gitignore-independent exact source search found only `data/normalized_yaml/bacterial/desulfovibrio_fss_1_medium.yaml` and its generated merged record for this name or source identifier. No TOGO companion record was found for JCM J1205.

## Evidence

MediaDive J1205 represents the recipe as `Main sol. J1205`, volume 1006 ml. The main solution contains 0.3 g ammonium chloride, 0.1 g magnesium sulfate heptahydrate, 5 ml Modified Wolfe's mineral solution, 0.02 g yeast extract, 0.5 mg resazurin, and 957 ml distilled water, followed by anaerobic stock additions.

Those after-cooling additions are 5.6 ml 0.25 M potassium phosphate buffer at pH 7.0, 20 ml 1.0 M sodium lactate, 5 ml filter-sterilized Vitamin solution, 8 ml 5% cysteine hydrochloride hydrate at pH 7.0, and 5 ml filter-sterilized 10 mM Fe(III)-EDTA.

MediaDive exposes a complete 100 ml Vitamin solution with thiamine, myo-inositol, calcium pantothenate, p-aminobenzoic acid, vitamin B12, pyridoxine hydrochloride, nicotinic acid, biotin, folic acid, and water. The Modified Wolfe's mineral solution is an explicit 5 ml stock addition whose source text says to use trace minerals from Medium No. 151 with final molybdate, copper sulfate, and nickel chloride adjustments.

## Completeness

The generated record preserves the pH, the anaerobic autoclave/addition/distribution instructions, and the source comment about allowing an oxygen gradient to form after filling the headspace with air.

The composition is incomplete because the 957 ml main water row and the 5 ml Modified Wolfe's mineral solution addition are absent, the Vitamin solution is flattened into nine final ingredients, and four after-cooling stocks are present only as misleading top-level G/L rows.

## Findings

- High: The 5 ml Modified Wolfe's mineral solution addition is missing as a composition row. Its trace-mineral adjustment survives only as free-text preparation step 3, so consumers cannot tell that the main recipe receives 5 ml/L of that stock.
- High: The 5 ml Vitamin solution addition was flattened. The target lists thiamine, myo-inositol, calcium pantothenate, p-aminobenzoic acid, vitamin B12, pyridoxine hydrochloride, nicotinic acid, biotin, and folic acid at their 100 ml stock concentrations rather than as a 5 ml/L stock addition.
- High: Four final stock volumes were copied into `G_PER_L` rows: 5.6 ml potassium phosphate buffer as 5.6 G/L, 20 ml 1.0 M sodium lactate as 20 G/L, 8 ml 5% cysteine as 8 G/L, and 5 ml 10 mM Fe(III)-EDTA as 5 G/L.
- Medium: The 957 ml distilled-water row from the JCM main solution is absent.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_fss_1_medium.yaml` so the main solution preserves 957 ml distilled water and a 5 ml Modified Wolfe's mineral solution addition.
- Model the 5.6 ml phosphate buffer, 20 ml sodium lactate, 5 ml Vitamin solution, 8 ml cysteine, and 5 ml Fe(III)-EDTA rows as stock additions with their source concentration attributes.
- Move the Vitamin solution recipe into a subordinate solution with its 100 ml water row.
- Preserve the Modified Wolfe's mineral solution instruction as an annotation on the 5 ml addition or its solution object so the Medium No. 151 trace-mineral adjustment is not reduced to an unlinked preparation step.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate the merged YAML and confirm the main solution has 957 ml water, 5 ml Modified Wolfe's mineral solution, and the correct five anaerobic after-cooling additions.
- Verify the regenerated record no longer has vitamin components, potassium phosphate buffer, sodium lactate, cysteine, or Fe(III)-EDTA as top-level stock-strength G/L rows.

## Additional Notes

None found.
