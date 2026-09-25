# YAML Record Review: potato_sucrose_agar_psa

- Repository: CultureMech
- Record: data/merge_yaml/merged/potato_sucrose_agar_psa.yaml
- Started UTC: 2026-09-24T21:38:16Z
- Finished UTC: 2026-09-24T21:38:16Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:007942
- Name: potato_sucrose_agar_psa
- Source import: TOGO M1406 / NBRC_M1
- Primary external ID: TOGO:M1406
- Maintained input: data/normalized_yaml/bacterial/potato_sucrose_agar_psa.yaml

This generated record represents Potato Sucrose Agar from TOGO M1406 / NBRC 1, merged with TOGO M328 for JCM 333.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/potato_sucrose_agar_psa.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

TOGO M1406 and NBRC 1 agree on the Potato Sucrose Agar (PSA) identity: 200 g potato, 20 g sucrose, 20 g agar, 1 L distilled water, pH 5.6, and a potato-extract preparation ending with autoclaving.

TOGO M328 imports the same formulation from JCM 333. JCM phrases the procedure differently but has the same 200 g potato, 20 g sucrose, 20 g agar, 1 L distilled water, and pH 5.6 endpoint.

The generated record is therefore grounded to real NBRC and JCM sources, but the maintained TOGO inputs are stale: both encode 1 L distilled water as 1 G_PER_L and neither carries the pH 5.6 preparation into the generated merge. The same JCM 333 source is also duplicated by the separate direct-JCM `data/merge_yaml/merged/potato_sucrose_agar.yaml` output.

Exact ignored-file searches across `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M1406`, `TOGO:M328`, `NBRC_M1`, `JCM_M333`, `NO=1`, `GRMD=333`, `potato_sucrose_agar_psa`, and `TOGO_M328_Potato-Sucrose_Agar` found the TOGO M1406 and TOGO M328 normalized YAMLs, the separate direct JCM 333 normalized YAML, and two generated records for Potato-Sucrose Agar.

## Evidence

- TOGO M1406 / NBRC 1 list 200 g potato, 20 g sucrose, 20 g agar, 1 L distilled water, pH 5.6, a detailed potato-extract preparation, and the note that commercial PDA can substitute for PSA.
- TOGO M328 / JCM 333 list 200 g potato, 20 g sucrose, 20 g agar, 1 L distilled water, pH 5.6, and a detailed potato-extract preparation.
- `data/merge_yaml/merged/potato_sucrose_agar.yaml` imports the same JCM 333 source directly but remains a separate generated record.

## Completeness

The generated record is incomplete relative to both source branches. It imports the shared 1 L distilled-water row as 1 G_PER_L, lacks the pH 5.6 setting, omits the NBRC and JCM preparation steps, omits the NBRC commercial-PDA substitution note, and does not reconcile the direct JCM 333 import.

## Findings

1. Major: Both maintained TOGO inputs import the source 1 L distilled-water row as `1 G_PER_L`, and the generated merge preserves that unit error.
2. Major: The generated record omits pH 5.6 and the detailed preparation text that are present in both the NBRC M1 and JCM 333 source branches.
3. Major: JCM 333 is still emitted twice: once via TOGO M328 in this generated record and once via the direct JCM import in `data/merge_yaml/merged/potato_sucrose_agar.yaml`.
4. Minor: The NBRC M1 commercial-PDA substitution note is not represented in the maintained normalized record or generated merge.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/potato_sucrose_agar_psa.yaml` so the NBRC M1 1 L water row, pH 5.6 setting, preparation text, and commercial-PDA note are represented.
- Repair `data/normalized_yaml/bacterial/TOGO_M328_Potato-Sucrose_Agar.yaml` so the JCM 333 1 L water row and pH 5.6 preparation are represented.
- Reconcile the direct JCM 333 import with the TOGO M328 import so one JCM source does not generate a second Potato-Sucrose Agar record.
- Regenerate `data/merge_yaml/merged/potato_sucrose_agar_psa.yaml` after the maintained inputs have been repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the repaired normalized inputs and regenerated merged outputs.
- Run exact ignored-file searches for `TOGO:M1406`, `TOGO:M328`, `NBRC_M1`, `JCM_M333`, `NO=1`, and `GRMD=333` to confirm the NBRC and JCM source records have been reconciled deliberately.
- Spot-check regenerated output for 200 g potato, 20 g sucrose, 20 g agar, 1 L distilled water, pH 5.6, and the expected NBRC/JCM source identities.

## Additional Notes

None found.
