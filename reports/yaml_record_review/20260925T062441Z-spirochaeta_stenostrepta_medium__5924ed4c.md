# YAML Record Review: spirochaeta_stenostrepta_medium__5924ed4c

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_stenostrepta_medium__5924ed4c.yaml
- Started UTC: 2026-09-25T06:23:31Z
- Finished UTC: 2026-09-25T06:24:39Z
- Verdict: needs curation

## Target

Generated merged YAML for JCM 809, SPIROCHAETA STENOSTREPTA MEDIUM.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_stenostrepta_medium__5924ed4c.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to the correct JCM 809 source and preserves the liquid-medium pH 7.6 identity.

The generated solute amounts are correct, but the explicit source solvent row is absent and two ingredient labels lose their BD-Difco qualifiers.

## Evidence

JCM 809 lists 5.0 g glucose, 2.0 g yeast extract (BD-Difco), 2.0 g peptone (BD-Difco), 1.0 mg resazurin, 0.5 g thioglycolate, and 1.0 L distilled water.

The source directs adjusting pH to 7.6 with KOH before autoclaving, adding 1% agar for stabs, and preparing pre-reduced medium under a 100% nitrogen atmosphere.

## Completeness

The generated record preserves glucose, yeast extract, peptone, resazurin, thioglycolate, pH 7.6, and the source preparation text. It omits the 1.0 L distilled-water row and shortens `Yeast extract (BD-Difco)` and `Peptone (BD-Difco)` to generic labels.

## Findings

- Major: the 1.0 L distilled-water row is missing from the generated record.
- Minor: the BD-Difco qualifiers for yeast extract and peptone are absent.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/spirochaeta_stenostrepta_medium.yaml` to include the 1.0 L distilled-water row from JCM 809.
- Preserve `Yeast extract (BD-Difco)` and `Peptone (BD-Difco)` in the ingredient labels or notes.
- Regenerate `data/merge_yaml/merged/spirochaeta_stenostrepta_medium__5924ed4c.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm the regenerated record contains 1.0 L distilled water.
- Confirm pH 7.6 and the 1% agar stab note remain present.

## Additional Notes

None found.
