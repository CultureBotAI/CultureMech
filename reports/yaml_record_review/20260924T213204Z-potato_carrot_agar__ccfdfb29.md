# YAML Record Review: potato_carrot_agar__ccfdfb29

- Repository: CultureMech
- Record: data/merge_yaml/merged/potato_carrot_agar__ccfdfb29.yaml
- Started UTC: 2026-09-24T21:32:04Z
- Finished UTC: 2026-09-24T21:32:04Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:009858
- Name: potato_carrot_agar
- Source imports: TOGO_M46_Potato-Carrot_Agar, TOGO_M47_1_10_Potato-Carrot_Agar
- Primary external ID: TOGO:M46
- Maintained inputs: data/normalized_yaml/bacterial/TOGO_M46_Potato-Carrot_Agar.yaml and data/normalized_yaml/bacterial/TOGO_M47_1_10_Potato-Carrot_Agar.yaml

This generated record represents TOGO Medium M46 / JCM Medium 54, Potato-Carrot Agar, with TOGO M47 / JCM 55 recorded as its 1/10 concentration variant.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/potato_carrot_agar__ccfdfb29.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct TOGO M46 / JCM 54 Potato-Carrot Agar identity, and the `variant_children` entry correctly names TOGO M47 / JCM 55 as `1_10_potato_carrot_agar`. M47 is a true concentration variant: potato decreases from 300 g/L to 30 g/L, carrot decreases from 25 g/L to 2.5 g/L, and agar remains 15 g/L.

Exact ignored-file searches across `data` for `TOGO:M46`, `TOGO:M47`, `JCM_M54`, `JCM_M55`, `GRMD=54`, `GRMD=55`, `Potato-Carrot_Agar`, `potato_carrot_agar`, and `1_10_potato_carrot_agar` found the TOGO M46/M47 family plus a separate direct JCM 54/55 family. The broad first JCM 55 search also matched unrelated JCM 550-series records, but the bounded `JCM_M55([^0-9-]|$)` search did not.

The generated TOGO merge is stale. Its maintained M46 and M47 YAMLs have a later `RESOLVED_POTATO_CARROT_AGAR_FAMILY` repair that records 1.0 L water as 1000 ML_PER_L, keeps M47 as a concentration variant of M46, and records the JCM 54/55 source references.

## Evidence

- TOGO M46 imports JCM_M54 and lists 1 L distilled water, 25 g carrot, 15 g agar, and 300 g potato; its source comments say to boil potatoes and carrots until cooked, filter through cheesecloth, make up the volume to 1.0 L, add agar, and leave pH unadjusted.
- JCM 54 lists the same 300 g potato, 25 g carrot, 15 g agar, 1 L distilled water, and preparation footnote.
- TOGO M47 imports JCM_M55 and lists 1 L distilled water, 2.5 g carrot, 15 g agar, and 30 g potato; its source points to the JCM 54 preparation footnote.
- JCM 55 lists the same 1/10 Potato-Carrot Agar variant and links Medium 54 for the footnote.

## Completeness

The generated merged record is not complete against either the source or the maintained inputs:

- It leaves the M46 1 L distilled water row as `1 G_PER_L`.
- It omits the JCM 54 preparation instruction to boil potato and carrot, filter through cheesecloth, make volume to 1 L, and add agar.
- It omits the source `pH unadjusted` condition.
- It remains split from the direct JCM 54/55 imports of the same full-strength and 1/10 formulations.

## Findings

1. Major: The generated merged record is stale relative to its repaired TOGO M46 and M47 normalized inputs; future repair belongs in regeneration from `data/normalized_yaml/bacterial/TOGO_M46_Potato-Carrot_Agar.yaml` and `data/normalized_yaml/bacterial/TOGO_M47_1_10_Potato-Carrot_Agar.yaml`, not in direct edits to `data/merge_yaml/merged/potato_carrot_agar__ccfdfb29.yaml`.
2. Major: The generated record still misrepresents source water as 1 G_PER_L and omits the source preparation and pH-unadjusted comments.
3. Major: The TOGO M46/M47 and direct JCM 54/55 imports remain split, even though they describe the same full-strength and 1/10 Potato-Carrot Agar family.

## Recommended Edits

- Regenerate this merged record from the already-corrected TOGO M46 and M47 normalized YAML files so water, preparation, pH, source references, and the explicit concentration-variant relationship propagate into `data/merge_yaml/merged`.
- Reconcile the TOGO M46/M47 normalized records with `data/normalized_yaml/bacterial/JCM_J54_POTATO-CARROT_AGAR.yaml`, `data/normalized_yaml/bacterial/potato_carrot_agar.yaml`, and `data/normalized_yaml/bacterial/1_10_potato_carrot_agar.yaml` so direct JCM and TOGO imports no longer generate separate Potato-Carrot Agar families.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M46`, `TOGO:M47`, `GRMD=54`, and `GRMD=55` with ignored files included to verify the JCM 54/55 and TOGO M46/M47 branches are reconciled or intentionally linked.
- Spot-check the regenerated full-strength and 1/10 Potato-Carrot Agar pages to verify M47 remains a concentration variant and only the potato and carrot amounts are one-tenth of M46.

## Additional Notes

None found.
