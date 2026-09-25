# YAML Record Review: Moderate Halophile Medium 2

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/moderate_halophile_medium_2__989bb7d0.yaml
- Started UTC: 2026-09-24T09:58:49Z
- Finished UTC: 2026-09-24T09:58:49Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/moderate_halophile_medium_2__989bb7d0.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007846` |
| Name | `moderate_halophile_medium_2` |
| Original name | `Moderate Halophile Medium 2` |
| Category | `bacterial` |
| Medium source | TOGO `M1310`; original source JCM `JCM_M1220` |
| Maintained owner | `data/normalized_yaml/bacterial/moderate_halophile_medium_2.yaml` |
| Generated status | Generated merge output from one normalized TOGO record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/moderate_halophile_medium_2__989bb7d0.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/moderate_halophile_medium_2__989bb7d0.yaml --out /private/tmp/moderate_halophile_medium_2__989bb7d0.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/moderate_halophile_medium_2__989bb7d0.strict.tsv` contained only the header line, so no strict errors were reported. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/moderate_halophile_medium_2__989bb7d0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/moderate_halophile_medium_2__989bb7d0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The generated record resolves to the TOGO `M1310` import of JCM medium `1220`, `MODERATE HALOPHILE MEDIUM 2`. An exact gitignore-independent `find` located two normalized files named `moderate_halophile_medium_2.yaml`; this target is disambiguated by `CultureMech:007846`, `TOGO:M1310`, and the bacterial owner path rather than by basename alone.

Ingredient identity is mostly coherent. The hydrated magnesium sulfate, hydrated calcium chloride, hydrated magnesium chloride, sodium chloride, potassium chloride, sodium hydrogencarbonate, sodium bromide, glucose, water, yeast extract, malt extract, and peptone rows correspond to the JCM 1220 component list.

The solvent amount is not grounded correctly. JCM and TOGO state that the ingredients are brought to a final volume of 1.0 L with distilled water; the generated record stores `Distilled water` as `1 G_PER_L`.

## Evidence

TOGO `M1310` and the live JCM `GRMD=1220` page support the same liquid formula:

| Source claim | Record representation | Review |
| --- | --- | --- |
| Add components to distilled water and bring volume to 1.0 L. | `Distilled water` is `1 G_PER_L`. | Unsupported unit: a 1 L final volume is not a 1 g/L water concentration. |
| Per 1 L: 9 g MgSO4 x 7H2O, 3 g yeast extract, 100 g NaCl, 0.2 g CaCl2 x 2H2O, 13 g MgCl2 x 6H2O, 1.3 g KCl, 0.05 g NaHCO3, 0.15 g NaBr, 10 g glucose, 3 g malt extract, and 5 g peptone. | All 11 non-water rows are present with matching numeric `G_PER_L` amounts. | Supported for the liquid final-volume interpretation. |
| Adjust pH to 7.0-7.2. | No `ph_value`, pH range, or preparation step records this range. | Materially incomplete. |
| Unless otherwise stated, JCM sterilizes media by autoclaving at 121 C for 15 min. | No autoclaving step is represented. | Materially incomplete. |
| For solid medium, add 20.0 g/L agar. | No agar variant or preparation note is represented. | Incomplete variant detail; the base `LIQUID` physical state remains supported. |

## Completeness

The core liquid composition is almost complete: all non-water compounds and amounts are present and all exact hydrate labels inspected in the source have plausible CHEBI groundings.

The missing pH range and autoclave instruction are consequential because they are explicit JCM preparation requirements. The omitted 20.0 g/L agar instruction is lower risk for this `LIQUID` record, but should be preserved as a solid-medium variant or a scoped preparation note rather than silently lost.

No absence of target organisms was treated as a defect. The inspected JCM and TOGO medium pages provide a recipe, not a strain-specific growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Distilled water is represented with the wrong unit. | The source says to bring the formula to 1.0 L with distilled water; the record stores `Distilled water` as `1 G_PER_L`. | `data/normalized_yaml/bacterial/moderate_halophile_medium_2.yaml`; TOGO volume-unit normalization. |
| major | The pH 7.0-7.2 range is missing. | TOGO `M1310` exposes `"ph": "7.0-7.2"` and JCM 1220 instructs users to adjust pH to 7.0-7.2; no field or preparation step in the generated record captures it. | `data/normalized_yaml/bacterial/moderate_halophile_medium_2.yaml`; TOGO pH import. |
| major | JCM preparation instructions were not imported. | JCM 1220 gives the 1.0 L final volume, pH adjustment, optional 20.0 g/L agar addition, and the default 121 C for 15 min autoclaving instruction; the generated record has no `preparation_steps`. | `data/normalized_yaml/bacterial/moderate_halophile_medium_2.yaml`; JCM/TOGO comment import. |
| minor | The solid agar variant is absent. | The source says to add 20.0 g/L agar for solid medium, while the generated record only represents the liquid base. | `data/normalized_yaml/bacterial/moderate_halophile_medium_2.yaml`; variant or preparation-note curation. |

## Recommended Edits

1. Correct the water representation in `data/normalized_yaml/bacterial/moderate_halophile_medium_2.yaml` so the record preserves "bring volume to 1.0 L" rather than `1 G_PER_L`.
2. Add the supported pH 7.0-7.2 range and JCM preparation notes, including the default autoclaving condition and the 20.0 g/L agar instruction scoped to solid medium.
3. Keep peptone, malt extract, and yeast extract as undefined ingredients unless exact, source-supported ontology terms are curated.
4. Regenerate `data/merge_yaml/merged/moderate_halophile_medium_2__989bb7d0.yaml` from the corrected normalized TOGO owner.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/moderate_halophile_medium_2.yaml` and the regenerated `data/merge_yaml/merged/moderate_halophile_medium_2__989bb7d0.yaml`.
2. Manually compare the regenerated record against TOGO `M1310` and JCM `GRMD=1220`, checking all 11 non-water amounts, the final-volume water instruction, pH 7.0-7.2, and the solid agar note.
3. Verify the regenerated merge still denotes the TOGO bacterial owner and is not silently overwritten by the same-basename MediaDive/JCM record under `data/normalized_yaml/archaea/`.

## Additional Notes

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
