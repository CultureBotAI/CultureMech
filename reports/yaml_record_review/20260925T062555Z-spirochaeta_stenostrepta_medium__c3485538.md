# YAML Record Review: spirochaeta_stenostrepta_medium__c3485538

- Repository: CultureMech
- Record: data/merge_yaml/merged/spirochaeta_stenostrepta_medium__c3485538.yaml
- Started UTC: 2026-09-25T06:24:40Z
- Finished UTC: 2026-09-25T06:25:56Z
- Verdict: needs curation

## Target

Generated merged YAML for TOGO M844, Spirochaeta Stenostrepta Medium, derived from JCM 809.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/spirochaeta_stenostrepta_medium__c3485538.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The record is grounded to TOGO M844 and correctly carries the original JCM_M809 identity.

The generated record is stale relative to both TOGO M844 and JCM 809: it changes the primary physical state to solid agar, converts liter and milligram quantities to `G_PER_L`, and moves preparation-context reagents into the ingredient list.

## Evidence

JCM 809 and TOGO M844 list a liquid main recipe with 1 L distilled water, 1 mg resazurin, 0.5 g thioglycolate, 5 g glucose, 2 g yeast extract (BD-Difco), and 2 g peptone (BD-Difco) at pH 7.6.

JCM 809's free-text instructions say to adjust the pH to 7.6 with KOH before autoclaving, add 1% agar for stabs, and prepare pre-reduced medium under a 100% nitrogen atmosphere.

## Completeness

The generated record preserves the TOGO water row and the BD-Difco labels, but it imports 1 L water as `1` `G_PER_L`, imports 1 mg resazurin as `1` `G_PER_L`, marks the medium itself as `SOLID_AGAR`, and adds variable agar, KOH, and N2 ingredient rows that are only conditional or preparative in the source.

## Findings

- Major: the primary source medium is liquid, but the generated record has `physical_state: SOLID_AGAR` because the optional `Add 1% agar for stabs` note was promoted to the medium state.
- Major: the 1 L distilled-water row is represented as `1` `G_PER_L`.
- Major: the 1 mg resazurin row is represented as `1` `G_PER_L`.
- Major: KOH and N2 are preparation-context terms, not source ingredient rows.
- Minor: 1% agar is optional for stabs and should be modeled as a stab variant or preparation note, not a required variable parent ingredient.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M844_Spirochaeta_Stenostrepta_Medium.yaml` to set the primary recipe to `LIQUID`.
- Convert distilled water and resazurin from the original 1 L and 1 mg source units without treating them as grams per liter.
- Move KOH, N2, and optional 1% agar back into preparation text or an explicit stab variant.
- Regenerate `data/merge_yaml/merged/spirochaeta_stenostrepta_medium__c3485538.yaml` from the repaired normalized record.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated record.
- Confirm `physical_state` is liquid for the base recipe.
- Confirm resazurin is not `1` `G_PER_L`.
- Confirm KOH, N2, and optional agar no longer appear as required variable parent ingredients.

## Additional Notes

None found.
